#!/usr/bin/env python3
"""
Vision hardware scanner — sensors, chips, compute.
Fetches from: GitHub (embedded/CV hardware repos), Reddit, hardware news RSS.
Output: JSON of interesting vision-hardware-related findings.
"""
import json
import re
import urllib.parse
import urllib.request
import urllib.error
from datetime import datetime, timedelta

UA = "Mozilla/5.0 (compatible; DailyVisionFrontier/1.0)"
TIMEOUT = 15

HARDWARE_KEYWORDS = [
    "event camera", "image sensor", "cmos sensor", "isp", "lidar", "tof",
    "depth sensor", "edge ai", "embedded vision", "jetson", "fpga vision",
    "neuromorphic", "slam", "hailo", "risc-v vision", "gpu", "accelerator",
]


# ─── GitHub Trending (embedded / C++ / hardware-ish) ──────────

def fetch_github_trending(language="", since="daily"):
    """Scrape GitHub trending page."""
    url = f"https://github.com/trending/{language}?since={since}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        html = resp.read().decode("utf-8")
    except Exception as e:
        return {"source": f"github_trending/{language}", "error": str(e), "items": []}

    repos = []
    blocks = re.findall(
        r'<h2[^>]*class="[^"]*h3[^"]*"[^>]*>.*?<a[^>]*href="/([^"]+)"[^>]*>([^<]+)</a>',
        html, re.DOTALL
    )
    for path, name in blocks:
        full_name = path.strip()
        if len(full_name.split("/")) == 2:
            repos.append({
                "full_name": full_name,
                "name": name.strip(),
                "url": f"https://github.com/{full_name}",
                "language": language or "unknown",
            })
    return {"source": f"github_trending/{language}", "error": None, "items": repos}


# ─── GitHub Search (hardware/embedded CV, past week) ──────────

def fetch_github_search(query, created_after):
    """GitHub repo search API for recent vision-hardware repos."""
    url = ("https://api.github.com/search/repositories"
           f"?q={urllib.parse.quote(query)}+created:%3E{created_after}"
           "&sort=stars&order=desc&per_page=10")
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "application/vnd.github+json",
    })
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        return {"source": f"github_search/{query}", "error": str(e), "items": []}

    items = []
    for r in data.get("items", []):
        items.append({
            "full_name": r.get("full_name", ""),
            "name": r.get("name", ""),
            "url": r.get("html_url", ""),
            "description": (r.get("description") or "")[:120],
            "stars": r.get("stargazers_count", 0),
            "language": r.get("language", ""),
        })
    return {"source": f"github_search/{query}", "error": None, "items": items}


# ─── Reddit ───────────────────────────────────────────────────

def fetch_reddit(subreddit, limit=15):
    """Fetch hot posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        data = json.loads(resp.read().decode("utf-8"))
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
            "subreddit": subreddit,
        })
    return {"source": f"reddit/r/{subreddit}", "error": None, "items": items}


# ─── RSS feeds (hardware news) ────────────────────────────────

def fetch_rss(url):
    """Fetch an RSS feed and return entries."""
    import xml.etree.ElementTree as ET
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        raw = resp.read()
        root = ET.fromstring(raw)
    except Exception as e:
        return {"source": url, "error": str(e), "items": []}

    items = []
    for item in root.findall(".//item"):
        title = item.findtext("title", "")
        link = item.findtext("link", "")
        pub = item.findtext("pubDate", "")
        items.append({"title": title, "url": link, "published": pub[:16]})
    return {"source": url, "error": None, "items": items}


def keyword_match(text, keywords):
    t = text.lower()
    return any(k in t for k in keywords)


def main():
    out = {}
    created_after = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    # GitHub trending: embedded / C++ / Python
    for lang in ["", "c++", "python"]:
        out[f"trending_{lang or 'all'}"] = fetch_github_trending(lang)

    # GitHub search for hardware-specific repos
    for q in ["event camera", "image signal processor", "embedded vision", "lidar perception"]:
        out[f"gh_{q.replace(' ', '_')}"] = fetch_github_search(q, created_after)

    # Reddit
    for sub in ["computervision", "embedded", "MachineLearning"]:
        out[f"reddit_{sub}"] = fetch_reddit(sub)

    # Hardware news RSS
    feeds = {
        "semianalysis": "https://semianalysis.com/feed/",
        "eetimes": "https://www.eetimes.com/feed/",
        "nvidia_newsroom": "https://blogs.nvidia.com/feed/",
    }
    for name, url in feeds.items():
        out[f"rss_{name}"] = fetch_rss(url)

    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
