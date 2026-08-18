#!/usr/bin/env python3
"""Pass 2: HN top stories, HF models created recently, GitHub trending HTML."""
import json, re, urllib.request, urllib.error, time
from datetime import datetime, timedelta

UA = {"User-Agent": "Mozilla/5.0 (compatible; DailyVisionPaper/1.0)"}
def get(url, timeout=20, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
    return data if binary else json.loads(data.decode("utf-8"))

out = {}

# 1. HN top stories (front page), filter CV keywords
CV = ["vision", "image", "video", "diffusion", "yolo", "segment", "depth", "3d", "vlm", "multimodal", "clip", "photo", "camera", "gaussian", "nerf", "ocr"]
try:
    data = get("https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30")
    items = []
    for i in data.get("hits", []):
        title = (i.get("title") or "") + " " + (i.get("url") or "")
        tl = title.lower()
        if any(k in tl for k in CV):
            items.append({
                "title": i.get("title"), "url": i.get("url") or f"https://news.ycombinator.com/item?id={i.get('objectID')}",
                "points": i.get("points", 0), "comments": i.get("num_comments", 0),
                "hn": f"https://news.ycombinator.com/item?id={i.get('objectID')}",
            })
    out["hn_front"] = items
except Exception as e:
    out["hn_front"] = {"error": str(e)}

# also HN search: last 24h for specific terms
try:
    t0 = int(time.time()) - 86400
    data = get(f"https://hn.algolia.com/api/v1/search?query=vision&tags=story&numericFilters=created_at_i%3E{t0}&hitsPerPage=10")
    out["hn_vision"] = [{"title": i.get("title"), "url": i.get("url") or f"https://news.ycombinator.com/item?id={i.get('objectID')}",
                         "points": i.get("points", 0), "comments": i.get("num_comments", 0)} for i in data.get("hits", [])]
except Exception as e:
    out["hn_vision"] = {"error": str(e)}

# 2. HF: newest models (createdAt desc), filter CV pipelines
CV_PIPES = {"text-to-image", "image-to-image", "image-segmentation", "object-detection",
            "image-text-to-text", "video-text-to-text", "depth-estimation", "image-classification",
            "video-classification", "text-to-video", "image-feature-extraction", "image-generation"}
try:
    data = get("https://huggingface.co/api/models?sort=createdAt&direction=-1&limit=120&full=true")
    items = []
    for m in data:
        tag = m.get("pipeline_tag", "")
        if tag not in CV_PIPES:
            continue
        dl = m.get("downloads", 0); lk = m.get("likes", 0)
        if dl + lk < 20:
            continue
        items.append({
            "model_id": m.get("modelId"), "tag": tag, "dl": dl, "likes": lk,
            "ts": m.get("trendingScore", 0), "created": m.get("createdAt", "")[:10],
            "tags": [t for t in m.get("tags", []) if t not in ("pytorch","transformers","safetensors","license:other","region:us")][:6],
            "url": f"https://huggingface.co/{m.get('modelId')}",
        })
    out["hf_newest_cv"] = items
except Exception as e:
    out["hf_newest_cv"] = {"error": str(e)}

# 3. GitHub Trending HTML (daily) — CV-filtered
try:
    html = get("https://github.com/trending?since=daily", binary=True).decode("utf-8", "ignore")
    repos = re.findall(r'<h2[^>]*class="[^"]*h3[^"]*"[^>]*>\s*<a[^>]*href="/([^"]+)"[^>]*>', html)
    descs = re.findall(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>\s*(.*?)\s*</p>', html, re.DOTALL)
    stars = re.findall(r'<a[^>]*href="/[^"]+/stargazers"[^>]*>\s*<svg[^>]*>.*?</svg>\s*([\d,.k]+)\s*</a>', html, re.DOTALL)
    items = []
    for idx, r in enumerate(repos[:30]):
        desc = re.sub(r"<[^>]+>", "", descs[idx]).strip() if idx < len(descs) else ""
        if not any(k in desc.lower() for k in ["vision","image","video","diffusion","segment","detect","vlm","multimodal","3d","camera","photo","ocr","depth","model","ai","llm","clip"]):
            continue
        items.append({"repo": r, "desc": desc[:150], "stars": stars[idx] if idx < len(stars) else "?",
                      "url": f"https://github.com/{r}"})
    out["gh_trending"] = items
except Exception as e:
    out["gh_trending"] = {"error": str(e)}

print(json.dumps(out, indent=1, ensure_ascii=False))
