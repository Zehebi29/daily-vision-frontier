#!/usr/bin/env python3
"""Supplementary vision-hardware scanner — extra feeds, vendor news, HF, GH."""
import json
import re
import urllib.parse
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
TIMEOUT = 20
out = {}

def fetch_rss(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        root = ET.fromstring(resp.read())
    except Exception as e:
        return {"source": url, "error": str(e), "items": []}
    items = []
    for item in root.findall(".//item"):
        title = item.findtext("title", "")
        link = item.findtext("link", "")
        pub = item.findtext("pubDate", "")
        items.append({"title": title, "url": link, "published": pub[:16]})
    return {"source": url, "error": None, "items": items}

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        return json.loads(resp.read().decode("utf-8", "replace"))
    except Exception as e:
        return {"error": str(e)}

def fetch_html_titles(url, link_re=None, title_re=None):
    """Fetch HTML page, extract (title, link) pairs heuristically."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        html = resp.read().decode("utf-8", "replace")
    except Exception as e:
        return {"source": url, "error": str(e), "items": []}
    items = []
    # generic: <a href="...">title</a> in news-ish list
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL):
        link, text = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if not text or len(text) < 15:
            continue
        text = re.sub(r"\s+", " ", text)
        if link.startswith("/"):
            from urllib.parse import urljoin
            link = urljoin(url, link)
        if link_re and not re.search(link_re, link):
            continue
        items.append({"title": text[:120], "url": link})
    # dedupe by title
    seen, uniq = set(), []
    for it in items:
        if it["title"] not in seen:
            seen.add(it["title"])
            uniq.append(it)
    return {"source": url, "error": None, "items": uniq[:25]}

# Feeds
for name, url in {
    "semiengineering": "https://semiengineering.com/feed/",
    "tomshardware": "https://www.tomshardware.com/feeds/all",
    "eetasia": "https://www.eetasia.com/feed/",
    "hackaday": "https://hackaday.com/feed/",
}.items():
    out[f"rss_{name}"] = fetch_rss(url)

# Vendor news pages
out["nvidia_newsroom_html"] = fetch_html_titles(
    "https://www.nvidia.com/en-us/newsroom/", link_re=r"/newsroom/")
out["amd_newsroom_html"] = fetch_html_titles(
    "https://www.amd.com/en/newsroom.html", link_re=r"newsroom")
out["sony_semicon_html"] = fetch_html_titles(
    "https://www.sony-semicon.com/en/news/", link_re=r"/en/news/")
out["ovt_news_html"] = fetch_html_titles(
    "https://www.ovt.com/news/", link_re=r"news|press")

# HuggingFace trending models by pipeline (use API)
for tag in ["image-segmentation", "depth-estimation", "image-classification", "object-detection", "image-to-image"]:
    d = fetch_json(f"https://huggingface.co/api/models?pipeline_tag={tag}&sort=trendingScore&direction=-1&limit=12")
    if isinstance(d, list):
        items = [{
            "model": m.get("id", ""),
            "downloads": m.get("downloads", 0),
            "likes": m.get("likes", 0),
            "pipeline": m.get("pipeline_tag", ""),
            "tags": [t for t in m.get("tags", []) if t.startswith(("onnx", "tflite", "safetensors", "coreml", "openvino", "rust", "axolotl"))][:6],
        } for m in d]
        out[f"hf_{tag}"] = {"source": tag, "error": None, "items": items}
    else:
        out[f"hf_{tag}"] = {"source": tag, "error": d, "items": []}

# GitHub search — more hardware-oriented queries, last 14 days
created_after = (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d")
for q in ["event camera", "neuromorphic camera", "image sensor driver",
          "embedded vision", "lidar perception", "depth camera",
          "risc-v vision", "hailo", "jetson orin", "raspberry pi camera ai",
          "FPGA ISP", "CIS image sensor"]:
    url = ("https://api.github.com/search/repositories"
           f"?q={urllib.parse.quote(q)}+created:%3E{created_after}"
           "&sort=stars&order=desc&per_page=8")
    d = fetch_json(url)
    if isinstance(d, dict) and "items" in d:
        items = [{
            "full_name": r.get("full_name", ""),
            "url": r.get("html_url", ""),
            "description": (r.get("description") or "")[:140],
            "stars": r.get("stargazers_count", 0),
            "language": r.get("language", ""),
        } for r in d["items"]]
        out[f"gh2_{q.replace(' ', '_')}"] = {"source": q, "error": None, "items": items}
    else:
        out[f"gh2_{q.replace(' ', '_')}"] = {"source": q, "error": d, "items": []}

# Reddit via old.reddit JSON (sometimes bypasses 403)
for sub in ["computervision", "embedded", "hardware", "MachineLearning"]:
    d = fetch_json(f"https://old.reddit.com/r/{sub}/hot.json?limit=15")
    if isinstance(d, dict) and "data" in d:
        items = [{
            "title": c["data"].get("title", ""),
            "url": f"https://www.reddit.com{c['data'].get('permalink', '')}",
            "score": c["data"].get("score", 0),
            "comments": c["data"].get("num_comments", 0),
        } for c in d["data"].get("children", [])]
        out[f"reddit2_{sub}"] = {"source": sub, "error": None, "items": items}
    else:
        out[f"reddit2_{sub}"] = {"source": sub, "error": d, "items": []}

print(json.dumps(out, ensure_ascii=False, indent=1))
