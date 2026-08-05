#!/usr/bin/env python3
"""Robust vision-hardware news fetcher for the daily digest (2026-08-05)."""
import json
import re
import html
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
TIMEOUT = 20


def get(url, headers=None, timeout=TIMEOUT):
    h = {"User-Agent": UA, "Accept": "*/*"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    return urllib.request.urlopen(req, timeout=timeout).read()


def fetch_rss(url):
    """Handle both RSS 2.0 <item> and Atom <entry>."""
    try:
        raw = get(url)
        root = ET.fromstring(raw)
    except Exception as e:
        return {"source": url, "error": str(e), "items": []}
    items = []
    for item in root.findall(".//item") + root.findall(".//{http://www.w3.org/2005/Atom}entry"):
        title = item.findtext("title") or item.findtext("{http://www.w3.org/2005/Atom}title") or ""
        link_el = item.find("link")
        if link_el is not None and link_el.get("href"):
            link = link_el.get("href")
        else:
            link = item.findtext("link") or ""
        pub = item.findtext("pubDate") or item.findtext("published") or ""
        items.append({"title": html.unescape(title).strip(), "url": link.strip(), "published": pub[:25]})
    return {"source": url, "error": None, "items": items}


def fetch_html_links(url, link_regex, limit=30):
    """Fetch a vendor news page and pull matching <a> links with text."""
    try:
        raw = get(url)
        text = raw.decode("utf-8", errors="ignore")
    except Exception as e:
        return {"source": url, "error": str(e), "items": []}
    items = []
    seen = set()
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', text, re.DOTALL):
        href, label = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if not label or len(label) < 8:
            continue
        if not re.search(link_regex, href, re.I):
            continue
        full = urllib.parse.urljoin(url, href)
        if full in seen:
            continue
        seen.add(full)
        items.append({"title": html.unescape(label)[:140], "url": full})
        if len(items) >= limit:
            break
    return {"source": url, "error": None, "items": items}


def fetch_reddit(subreddit, limit=15):
    try:
        raw = get(f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}")
        data = json.loads(raw.decode("utf-8"))
    except Exception as e:
        return {"source": f"reddit/r/{subreddit}", "error": str(e), "items": []}
    items = []
    for child in data.get("data", {}).get("children", []):
        d = child.get("data", {})
        items.append({
            "title": d.get("title", ""),
            "url": f"https://www.reddit.com{d.get('permalink', '')}",
            "score": d.get("score", 0),
            "num_comments": d.get("num_comments", 0),
        })
    return {"source": f"reddit/r/{subreddit}", "error": None, "items": items}


def fetch_github_trending(language="", since="daily"):
    try:
        raw = get(f"https://github.com/trending/{language}?since={since}")
        text = raw.decode("utf-8", errors="ignore")
    except Exception as e:
        return {"source": f"github_trending/{language}", "error": str(e), "items": []}
    items = []
    for m in re.finditer(r'<h2[^>]*class="[^"]*h3[^"]*"[^>]*>.*?<a[^>]*href="/([^"]+)"[^>]*>([^<]+)</a>', text, re.DOTALL):
        full_name = m.group(1).strip()
        if full_name.count("/") == 1:
            items.append({"title": full_name, "url": f"https://github.com/{full_name}", "lang": language or "any"})
    return {"source": f"github_trending/{language}", "error": None, "items": items}


def main():
    out = {}

    # RSS feeds
    feeds = {
        "semianalysis": "https://semianalysis.com/feed/",
        "eetimes": "https://www.eetimes.com/feed/",
        "nvidia": "https://blogs.nvidia.com/feed/",
        "semiengineering": "https://semiengineering.com/feed/",
        "tomshardware": "https://www.tomshardware.com/feeds/all",
        "sony": "https://www.sony-semicon.com/en/news/rss.xml",
    }
    for name, url in feeds.items():
        out[f"rss_{name}"] = fetch_rss(url)

    # Vendor news pages (HTML link extraction)
    out["vendor_nvidia"] = fetch_html_links("https://www.nvidia.com/en-us/newsroom/", r"newsroom|article|press|blog", 25)
    out["vendor_sony"] = fetch_html_links("https://www.sony-semicon.com/en/news/", r"news|press|release", 25)
    out["vendor_ovt"] = fetch_html_links("https://www.ovt.com/news/", r"news|press|release|2026", 25)
    out["vendor_amd"] = fetch_html_links("https://www.amd.com/en/newsroom.html", r"news|press|release", 25)

    # Reddit
    for sub in ["computervision", "embedded", "MachineLearning"]:
        out[f"reddit_{sub}"] = fetch_reddit(sub)

    # GitHub trending
    for lang in ["", "c++"]:
        out[f"gh_trend_{lang or 'all'}"] = fetch_github_trending(lang)

    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
