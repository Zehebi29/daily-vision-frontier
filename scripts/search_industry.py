#!/usr/bin/env python3
"""
Industry tools/repos scanner for Computer Vision.
Fetches from: GitHub Trending, HuggingFace, PapersWithCode, Reddit.
Output: JSON of interesting CV/vision-related findings.
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (compatible; DailyVisionPaper/1.0)"
TIMEOUT = 15

# ─── GitHub Trending ────────────────────────────────────────

def fetch_github_trending(language="", since="daily"):
    """Scrape GitHub trending page for CV-related repos."""
    url = f"https://github.com/trending/{language}?since={since}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        html = resp.read().decode("utf-8")
    except Exception as e:
        return {"source": "github_trending", "error": str(e), "items": []}
    
    repos = []
    # Simple regex-based scraping for trending repos
    # Find repo blocks
    blocks = re.findall(
        r'<h2[^>]*class="[^"]*h3[^"]*"[^>]*>.*?<a[^>]*href="/([^"]+)"[^>]*>([^<]+)</a>',
        html, re.DOTALL
    )
    for path, name in blocks:
        full_name = path.strip()
        if len(full_name.split("/")) == 2:  # user/repo format
            repos.append({
                "full_name": full_name,
                "name": name.strip(),
                "url": f"https://github.com/{full_name}",
                "language": language or "unknown",
            })
    
    # Also try to get descriptions
    desc_blocks = re.findall(
        r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>\s*([^<]+?)\s*</p>',
        html, re.DOTALL
    )
    for i, desc in enumerate(desc_blocks[:len(repos)]):
        repos[i]["description"] = desc.strip()
    
    return {"source": "github_trending", "error": None, "items": repos}


def fetch_huggingface_models(pipeline="computer-vision", sort="downloads", limit=10):
    """Fetch trending models from HuggingFace Hub."""
    url = (f"https://huggingface.co/api/models"
           f"?pipeline_tag={pipeline}"
           f"&sort={sort}"
           f"&direction=-1"
           f"&limit={limit}")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        return {"source": "huggingface_models", "error": str(e), "items": []}
    
    items = []
    for m in data:
        items.append({
            "model_id": m.get("modelId", ""),
            "pipeline_tag": m.get("pipeline_tag", ""),
            "downloads": m.get("downloads", 0),
            "likes": m.get("likes", 0),
            "url": f"https://huggingface.co/{m.get('modelId', '')}",
            "tags": [t for t in m.get("tags", []) if t not in ("pytorch", "transformers")][:5],
        })
    return {"source": "huggingface_models", "error": None, "items": items}


def fetch_huggingface_daily_papers(limit=10):
    """Fetch daily papers from HuggingFace Papers page."""
    # HF Papers API
    url = f"https://huggingface.co/api/daily_papers?limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        return {"source": "huggingface_papers", "error": str(e), "items": []}
    
    items = []
    for p in data:
        paper = p.get("paper", {})
        items.append({
            "title": paper.get("title", ""),
            "id": paper.get("id", ""),
            "url": paper.get("url", ""),
            "upvotes": p.get("upvotes", 0),
            "pipeline_tag": paper.get("pipeline_tag", ""),
            "summary": paper.get("summary", "")[:200],
        })
    return {"source": "huggingface_papers", "error": None, "items": items}


def fetch_reddit_hot(subreddit="computervision", limit=10):
    """Fetch hot posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        return {"source": f"reddit_r_{subreddit}", "error": str(e), "items": []}
    
    items = []
    for child in data.get("data", {}).get("children", []):
        post = child.get("data", {})
        items.append({
            "title": post.get("title", ""),
            "url": post.get("url", ""),
            "permalink": f"https://www.reddit.com{post.get('permalink', '')}",
            "score": post.get("score", 0),
            "num_comments": post.get("num_comments", 0),
            "created_utc": post.get("created_utc", 0),
            "domain": post.get("domain", ""),
        })
    return {"source": f"reddit_r_{subreddit}", "error": None, "items": items}


def fetch_paperswithcode_latest(limit=10):
    """Fetch latest papers/projects from PapersWithCode."""
    url = f"https://paperswithcode.com/api/v1/papers/?items_per_page={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        return {"source": "paperswithcode", "error": str(e), "items": []}
    
    items = []
    for p in data.get("results", []):
        items.append({
            "title": p.get("title", ""),
            "url": p.get("url_abs", ""),
            "github_url": (p.get("github_url") or ""),
            "arxiv_id": (p.get("arxiv_id") or ""),
            "abstract": (p.get("abstract") or "")[:200],
        })
    return {"source": "paperswithcode", "error": None, "items": items}


# ─── CV-related keywords filter ──────────────────────────────

CV_KEYWORDS = [
    "vision", "visual", "image", "video", "detect", "segment",
    "diffusion", "gan", "vlm", "multimodal", "multi-modal",
    "clip", "llava", "blip", "siglip",
    "face", "pose", "ocr", "caption", "depth", "nerf",
    "3d", "point cloud", "mesh", "gaussian splat",
    "super resolution", "restoration", "inpaint",
    "semantic", "panoptic", "track", "reid",
    "object", "recognition", "classification",
    "yolo", "sam", "vit", "transformer",
    "lane", "driving", "autonomous",
    "medical imaging", "radiology", "histopathology",
    "scene", "layout", "document",
    "style transfer", "neural rendering",
    "flow", "warp", "motion",
    "slam", "structure from motion",
    "generation", "synthesis", "edit",
    "foundation model", "pretrain", "self-supervised",
    "contrastive", "representation learning",
    "adapter", "lora", "fine-tune",
]


def is_cv_related(text: str) -> bool:
    """Check if text is related to computer vision."""
    if not text:
        return False
    text_lower = text.lower()
    for kw in CV_KEYWORDS:
        if kw in text_lower:
            return True
    return False


# ─── Main ────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Scan industry sources for CV tools/repos")
    parser.add_argument("--min-score", type=int, default=0, help="Min Reddit score / HF likes")
    args = parser.parse_args()
    
    results = {}
    
    # 1. GitHub Trending
    results["github_python"] = fetch_github_trending("python", "daily")
    results["github_unknown"] = fetch_github_trending("", "daily")
    
    # 2. HuggingFace Models (CV pipeline tags)
    for tag in ["computer-vision", "image-classification", "object-detection", 
                "image-segmentation", "text-to-image", "image-to-image",
                "video-classification", "depth-estimation"]:
        results[f"hf_{tag}"] = fetch_huggingface_models(tag, "downloads", 5)
    
    # 3. HuggingFace Daily Papers
    results["hf_papers"] = fetch_huggingface_daily_papers(10)
    
    # 4. Reddit
    for sub in ["computervision", "MachineLearning", "StableDiffusion"]:
        results[f"reddit_{sub}"] = fetch_reddit_hot(sub, 10)
    
    # 5. PapersWithCode
    results["paperswithcode"] = fetch_paperswithcode_latest(10)
    
    # Filter and aggregate CV-related items
    all_items = []
    seen_urls = set()
    
    for source_key, source_data in results.items():
        if source_data.get("error"):
            continue
        for item in source_data.get("items", []):
            # Build a text to check for CV relevance
            check_text = json.dumps(item, ensure_ascii=False)
            if not is_cv_related(check_text):
                continue
            
            # Dedup by URL
            url = item.get("url") or item.get("permalink") or item.get("github_url") or ""
            if url and url in seen_urls:
                continue
            if url:
                seen_urls.add(url)
            
            item["_source"] = source_key
            all_items.append(item)
    
    # Sort: higher score/likes first
    def item_score(item):
        return (
            item.get("score", 0) or 
            item.get("likes", 0) or 
            item.get("downloads", 0) or 
            item.get("upvotes", 0) or 
            0
        )
    all_items.sort(key=item_score, reverse=True)
    
    output = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "total_sources": len(results),
        "total_found": len(all_items),
        "items": all_items[:30],  # Top 30
        "sources_summary": {
            k: {"items_count": len(v.get("items", [])), "error": v.get("error")}
            for k, v in results.items()
        },
    }
    
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
