#!/usr/bin/env python3
"""Supplement industry scan: fresh signals only.
GitHub Search API (new repos), HF trendingScore models, HF daily papers, HN Algolia.
"""
import json, urllib.request, urllib.error, time
from datetime import datetime, timedelta

UA = {"User-Agent": "Mozilla/5.0 (compatible; DailyVisionPaper/1.0)"}
def get(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))

out = {}
today = datetime.now()
week_ago = (today - timedelta(days=7)).strftime("%Y-%m-%d")

# 1. GitHub Search: new CV repos past week, sorted by stars
queries = [
    ("cv", "computer+vision"),
    ("diffusion", "diffusion"),
    ("image-gen", "image+generation"),
    ("vlm", "vision+language+model"),
    ("segmentation", "segmentation"),
    ("video", "video+understanding"),
    ("3d", "3d+vision"),
]
gh = {}
for label, q in queries:
    url = f"https://api.github.com/search/repositories?q={q}+created:%3E{week_ago}&sort=stars&order=desc&per_page=8"
    try:
        data = get(url)
        items = [{
            "full_name": i["full_name"], "stars": i["stargazers_count"],
            "desc": (i.get("description") or "")[:160], "lang": i.get("language"),
            "created": i.get("created_at", "")[:10], "url": i["html_url"],
            "topics": i.get("topics", [])[:5],
        } for i in data.get("items", [])]
        gh[label] = items
    except Exception as e:
        gh[label] = {"error": str(e)}
    time.sleep(1)
out["github_search"] = gh

# 2. HF trending models (trendingScore) for key pipelines
hf = {}
for tag in ["text-to-image", "image-to-image", "image-segmentation", "object-detection",
            "image-text-to-text", "video-text-to-text", "depth-estimation", "computer-vision"]:
    url = f"https://huggingface.co/api/models?pipeline_tag={tag}&sort=trendingScore&direction=-1&limit=8&full=true"
    try:
        data = get(url)
        items = []
        for m in data:
            items.append({
                "model_id": m.get("modelId"), "ts": m.get("trendingScore", 0),
                "downloads": m.get("downloads", 0), "likes": m.get("likes", 0),
                "created": m.get("createdAt", "")[:10],
                "tags": [t for t in m.get("tags", []) if t not in ("pytorch","transformers","safetensors","license:other")][:6],
                "url": f"https://huggingface.co/{m.get('modelId')}",
            })
        hf[tag] = items
    except Exception as e:
        hf[tag] = {"error": str(e)}
out["hf_trending"] = hf

# 3. HF daily papers
try:
    data = get("https://huggingface.co/api/daily_papers?limit=30")
    out["hf_papers"] = [{
        "title": p.get("paper", {}).get("title", ""),
        "id": p.get("paper", {}).get("id", ""),
        "url": p.get("paper", {}).get("url", ""),
        "upvotes": p.get("upvotes", 0),
        "tag": p.get("paper", {}).get("pipeline_tag", ""),
    } for p in data]
except Exception as e:
    out["hf_papers"] = {"error": str(e)}

# 4. Hacker News Algolia: search CV-related terms, last 24h, top
try:
    data = get("https://hn.algolia.com/api/v1/search_by_date?query=(computer%20vision)%20OR%20(image%20generation)%20OR%20(diffusion)%20OR%20(vision%20model)&tags=story&numericFilters=created_at_i%3E" + str(int(time.time()) - 86400) + "&hitsPerPage=15")
    out["hn"] = [{
        "title": i.get("title"), "url": i.get("url") or f"https://news.ycombinator.com/item?id={i.get('objectID')}",
        "points": i.get("points", 0), "comments": i.get("num_comments", 0),
        "hn_url": f"https://news.ycombinator.com/item?id={i.get('objectID')}",
    } for i in data.get("hits", [])]
except Exception as e:
    out["hn"] = {"error": str(e)}

print(json.dumps(out, indent=1, ensure_ascii=False))
