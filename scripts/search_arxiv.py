#!/usr/bin/env python3
"""
Daily CV Paper Finder — Search arXiv for recent (< 6 months) CV/vision/VLM papers.
Usage: python3 scripts/search_arxiv.py [--max N] [--skip N]
"""
import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import sys
import os
import re
import json
import time
from datetime import datetime, timedelta

ARXIV_API = "https://export.arxiv.org/api/query"
# arXiv API rate limit: ~1 request per 3 seconds. Sleep between queries to avoid HTTP 429.
REQUEST_INTERVAL = 3.0
_last_request_time = [0.0]

# Major CV/vision categories and keywords
CATEGORIES = [
    "cs.CV",      # Computer Vision
    "cs.AI",      # AI
    "cs.LG",      # Machine Learning
    "cs.MM",      # Multimedia
    "cs.RO",      # Robotics
    "cs.CL",      # Computation & Language (for VLMs)
]

# ── Priority research areas (茜茜's focus) — tagged & ranked first ──
# Each entry: (arxiv query, area key). Order = priority order.
PRIORITY_QUERIES = [
    # 1. Industrial defect detection (esp. semiconductor)
    ("cat:cs.CV+AND+all:wafer+AND+all:defect", "industrial_defect"),
    ("cat:cs.CV+AND+all:semiconductor+AND+all:inspection", "industrial_defect"),
    ("cat:cs.CV+AND+all:surface+AND+all:defect+AND+all:detection", "industrial_defect"),
    ("cat:cs.CV+AND+all:anomaly+AND+all:detection+AND+all:industrial", "industrial_defect"),
    # 2. Explainability of detection / segmentation
    ("cat:cs.CV+AND+all:explainable+AND+all:detection", "explainability"),
    ("cat:cs.CV+AND+all:interpretable+AND+all:segmentation", "explainability"),
    ("cat:cs.CV+AND+all:explanation+AND+all:object+detection", "explainability"),
    # 3. Vision agents
    ("cat:cs.CV+AND+all:vision+AND+all:agent", "vision_agent"),
    ("cat:cs.AI+AND+all:multimodal+AND+all:agent", "vision_agent"),
    ("cat:cs.CV+AND+all:visual+AND+all:grounding+AND+all:agent", "vision_agent"),
    # 4. Active learning / RLHF for images
    ("cat:cs.CV+AND+all:active+AND+all:learning", "active_learning"),
    ("cat:cs.CV+AND+all:rlhf", "active_learning"),
    ("cat:cs.CV+AND+all:preference+AND+all:optimization+AND+all:image", "active_learning"),
]

PRIORITY_NAMES = {
    "industrial_defect": "工业缺陷检测(半导体)",
    "explainability": "检测/分割可解释性",
    "vision_agent": "视觉Agent",
    "active_learning": "图像主动学习/RLHF",
}

CORE_QUERIES = [
    # Vision
    "all:computer+vision",
    "all:object+detection",
    "all:image+segmentation",
    "all:visual+recognition",
    # Vision-Language / Multimodal
    "all:vision+language",
    "all:multimodal+learning",
    "all:visual+language+model",
    "all:VLM",
    "all:LLaVA+OR+all:Qwen-VL+OR+all:CogVLM",
    "all:CLIP+OR+all:BLIP+OR+all:SigLIP",
    # Image/Video Generation
    "all:diffusion+model+image",
    "all:Stable+Diffusion+OR+all:DiT",
    "all:image+generation+OR+all:text+to+image",
    "all:video+generation+OR+all:text+to+video",
    "all:ControlNet+OR+all:IP-Adapter",
    # 3D Vision
    "all:3D+vision+OR+all:point+cloud",
    "all:neural+rendering+OR+all:NeRF+OR+all:3D+Gaussian",
    "all:3D+reconstruction",
    # Visual Understanding
    "all:visual+question+answering",
    "all:image+captioning",
    "all:visual+grounding",
    "all:scene+understanding",
    # Foundation Models for Vision
    "all:vision+transformer+OR+all:ViT",
    "all:visual+foundation+model",
    "all:segment+anything",
    # Special topics
    "all:visual+reasoning",
    "all:embodied+vision+OR+all:visual+navi",
    "all:document+understanding+OR+all:OCR+vision",
    "all:medical+image+analysis+OR+all:satellite+imagery",
]


def fetch_arxiv(query: str, max_results: int = 5) -> list:
    """Search arXiv and return parsed entries."""
    params = urllib.parse.urlencode({
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results,
    })
    url = f"{ARXIV_API}?{params}"
    
    # Respect arXiv rate limit (1 req / 3s)
    elapsed = time.time() - _last_request_time[0]
    if elapsed < REQUEST_INTERVAL:
        time.sleep(REQUEST_INTERVAL - elapsed)
    
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "DailyCVPaper/1.0"})
        resp = urllib.request.urlopen(req, timeout=20)
        _last_request_time[0] = time.time()
        xml_data = resp.read().decode("utf-8")
    except Exception as e:
        print(f"  [WARN] Query failed: {query[:60]}... -> {e}", file=sys.stderr)
        return []

    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_data)
    papers = []
    
    for entry in root.findall("a:entry", ns):
        arxiv_url = entry.find("a:id", ns).text.strip()
        arxiv_id = arxiv_url.split("/abs/")[-1]
        title = entry.find("a:title", ns).text.strip().replace("\n", " ").strip()
        published = entry.find("a:published", ns).text[:10]
        updated = entry.find("a:updated", ns).text[:10] if entry.find("a:updated", ns) is not None else published
        summary = entry.find("a:summary", ns).text.strip()
        authors = ", ".join([a.find("a:name", ns).text for a in entry.findall("a:author", ns)])
        cats = [c.get("term") for c in entry.findall("a:category", ns)]
        
        # Clean title
        title = re.sub(r'\s+', ' ', title).strip()
        
        papers.append({
            "id": arxiv_id,
            "title": title,
            "authors": authors,
            "published": published,
            "updated": updated,
            "categories": cats,
            "summary": summary,
            "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
            "abs_url": f"https://arxiv.org/abs/{arxiv_id}",
        })
    
    return papers


def is_recent(published_date: str, months: int = 6) -> bool:
    """Check if published_date is within the last N months."""
    pub = datetime.strptime(published_date, "%Y-%m-%d")
    cutoff = datetime.now() - timedelta(days=months * 30)
    return pub >= cutoff


def slugify(title: str) -> str:
    """Convert paper title to a URL-friendly slug."""
    s = title.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s-]+', '-', s)
    return s[:80]


def load_existing_ids(repo_path: str) -> set:
    """Load arXiv IDs already covered from existing papers."""
    existing = set()
    papers_dir = os.path.join(repo_path, "papers")
    if not os.path.isdir(papers_dir):
        return existing
    for fname in os.listdir(papers_dir):
        if fname.endswith(".md"):
            # Check for arXiv ID in the file
            fpath = os.path.join(papers_dir, fname)
            try:
                with open(fpath, "r") as f:
                    content = f.read()
                    m = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)', content)
                    if m:
                        existing.add(m.group(1))
            except:
                pass
    return existing


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Search arXiv for recent CV/vision papers")
    parser.add_argument("--max", type=int, default=3, help="Results per query")
    parser.add_argument("--skip", type=int, default=0, help="Skip first N newest papers (to rotate picks)")
    parser.add_argument("--repo", type=str, default="/home/ubuntu/daily-vision-paper", help="Repo path for dedup")
    parser.add_argument("--diversity", action="store_true", default=True, help="Encourage diverse topics across days")
    args = parser.parse_args()

    repo_path = os.path.abspath(args.repo)
    existing_ids = load_existing_ids(repo_path)
    print(f"[INFO] Already covered {len(existing_ids)} papers", file=sys.stderr)

    all_papers = []
    seen_ids = set(existing_ids)  # Don't re-fetch already covered papers
    num_queries_shown = 0

    # Priority queries first (tagged), then general core queries as fallback
    all_queries = [(q, area) for q, area in PRIORITY_QUERIES] + [(q, None) for q in CORE_QUERIES]
    for query, area in all_queries:
        results = fetch_arxiv(query, max_results=args.max)
        for p in results:
            pid = p["id"].split("v")[0]  # Remove version suffix
            if pid in seen_ids:
                continue
            if not is_recent(p["published"], months=6):
                continue
            seen_ids.add(pid)
            p["priority"] = area is not None
            p["priority_area"] = area
            p["priority_area_name"] = PRIORITY_NAMES.get(area, "") if area else ""
            all_papers.append(p)
        
        # Brief progress
        num_queries_shown += 1
        if num_queries_shown % 5 == 0:
            print(f"[INFO] Queried {num_queries_shown}/{len(all_queries)} topics, collected {len(all_papers)} candidates so far", file=sys.stderr)
    
    if not all_papers:
        print("[WARN] No new papers found. All recent papers may already be covered.", file=sys.stderr)
        # Fallback: show one existing paper anyway? No, return empty.
    
    # Deduplicate by normalized title
    seen_titles = set()
    unique_papers = []
    for p in all_papers:
        t = p["title"].lower().strip()
        if t not in seen_titles:
            seen_titles.add(t)
            unique_papers.append(p)
    
    # Sort: priority-area papers first (each group newest first)
    unique_papers.sort(key=lambda x: (0 if x.get("priority") else 1,
                                      -int(x["published"].replace("-", ""))))
    
    if args.skip > 0 and args.skip < len(unique_papers):
        # Skip the first N to rotate picks
        unique_papers = unique_papers[args.skip:]
    
    # Output as JSON for consumption
    result = {
        "count": len(unique_papers),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "papers": unique_papers[:5],  # Top 5 unique papers
        "search_date": datetime.now().isoformat(),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
