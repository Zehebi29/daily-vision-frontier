#!/usr/bin/env python3
"""Fetch fresh HF models (created in last N days) across industrial-vision-relevant buckets."""
import json, sys, time, urllib.request, urllib.parse, re
from datetime import datetime, timedelta

BASE = "https://huggingface.co/api/models"
NOW = datetime(2026, 10, 22)
CUT = (NOW - timedelta(days=21)).strftime("%Y-%m-%dT00:00:00.000Z")

_last = [0.0]
def fetch(url, timeout=25):
    el = time.time() - _last[0]
    if el < 1.2: time.sleep(1.2 - el)
    _last[0] = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": "daily-digest/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        print(f"[WARN] {url} -> {e}", file=sys.stderr)
        return []

QUERIES = [
    ("vla", "search=vla"),
    ("vla", "search=vision-language-action"),
    ("vla", "search=robot"),
    ("edge", "search=gguf"),
    ("edge", "pipeline_tag=object-detection"),
    ("edge", "pipeline_tag=image-classification"),
    ("edge", "pipeline_tag=image-segmentation"),
    ("edge", "search=anomaly"),
    ("vlm", "pipeline_tag=image-text-to-text"),
    ("edge", "search=smol"),
    ("edge", "search=npu"),
    ("edge", "search=int4"),
    ("edge", "search=awq"),
    ("vla", "search=manipulation"),
    ("vla", "search=policy"),
]

results = {}
for area, qs in QUERIES:
    for sort in ("createdAt", "trendingScore"):
        url = f"{BASE}?{qs}&sort={sort}&direction=-1&limit=40"
        for m in fetch(url):
            mid = m.get("id")
            if not mid: continue
            created = m.get("createdAt") or ""
            if created < CUT: continue
            rec = results.setdefault(mid, {
                "id": mid, "area": area, "created": created[:10],
                "dl": m.get("downloads") or 0, "likes": m.get("likes") or 0,
                "tags": [t for t in (m.get("tags") or []) if not t.startswith(("dataset:", "base_model:"))][:8],
                "pipe": m.get("pipeline_tag"),
            })
            rec["dl"] = max(rec["dl"], m.get("downloads") or 0)
            rec["likes"] = max(rec["likes"], m.get("likes") or 0)

items = sorted(results.values(), key=lambda x: (x["created"], x["likes"], x["dl"]), reverse=True)
print(json.dumps(items, ensure_ascii=False, indent=1))
print(f"[OK] {len(items)} models since {CUT[:10]}", file=sys.stderr)
