#!/usr/bin/env python3
"""
Search HuggingFace for recently trending / newly released open models relevant to
industrial vision deployment: VLA (vision-language-action), edge/small vision models,
small VLMs, and quantized/deployable variants.

Output: JSON list on stdout, one model per entry, tagged with priority area.
Built-in topic bias (priority order):
  1. VLA / robot foundation models (manipulation, action)
  2. Edge / small vision models (<7B: classification / detection / segmentation / VLM)
  3. Quantized / deployable variants (GGUF / INT4 / AWQ / edge-ready)
"""
import json
import re
import sys
import time
import urllib.request
import urllib.parse

BASE = "https://huggingface.co/api/models"

# Priority areas, ordered (highest first) — matches user's industrial-vision focus
PRIORITY_QUERIES = [
    # (hf search kw or pipeline tag, area_key)
    ("search=vla", "vla"),
    ("search=vision-language-action", "vla"),
    ("search=robot+foundation", "vla"),
    ("search=manipulation", "vla"),
    ("search=act+predict", "vla"),
    ("pipeline_tag=image-classification", "edge_vision"),
    ("pipeline_tag=object-detection", "edge_vision"),
    ("pipeline_tag=image-segmentation", "edge_vision"),
    ("pipeline_tag=zero-shot-image-classification", "edge_vision"),
    ("search=smol", "small_vlm"),
    ("search=paligemma", "small_vlm"),
    ("search=moondream", "small_vlm"),
    ("search=gguf", "quantized"),
    ("search=quantized", "quantized"),
    ("search=int4", "quantized"),
    ("pipeline_tag=image-text-to-text", "vlm_general"),
]

AREA_NAMES = {
    "vla": "VLA/机器人操作",
    "edge_vision": "边缘视觉(分类/检测/分割)",
    "small_vlm": "小VLM(<7B)",
    "quantized": "量化/可部署",
    "vlm_general": "VLM通用(参考)",
}

# Small-model keyword filter for image-text-to-text results (keep only light models)
SMALL_VLM_KW = re.compile(
    r"(smol|gemma|qwen3|paligemma|phi|llava|internvl|moondream|blip|tiny|mini|nano|edge|gguf|quantiz)",
    re.IGNORECASE,
)

_last_request_time = [0.0]


def fetch(url, timeout=20):
    """Fetch JSON from HF API with 3s rate-limit spacing."""
    elapsed = time.time() - _last_request_time[0]
    if elapsed < 3.0:
        time.sleep(3.0 - elapsed)
    _last_request_time[0] = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": "daily-vision-paper/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"[WARN] fetch failed: {url} -> {e}", file=sys.stderr)
        return []


def query_models(qs, sort="trendingScore", limit=15):
    """Build HF API URL from query string params and fetch."""
    url = f"{BASE}?{qs}&sort={sort}&direction=-1&limit={limit}"
    return fetch(url)


def classify(model, area):
    """Apply extra small-model filter; return None if should drop."""
    mid = model.get("id", "").lower()
    if area == "vlm_general":
        # only keep small-ish VLMs for general VLM bucket
        if not SMALL_VLM_KW.search(mid):
            return None
    # drop pure text-generation LLMs >7B-ish in the vlm bucket (keep only image-text-to-text)
    if area == "vlm_general" and model.get("pipeline_tag") not in (None, "image-text-to-text"):
        return None
    return model


def main():
    seen = {}
    for qs, area in PRIORITY_QUERIES:
        models = query_models(qs)
        for m in models:
            m2 = classify(m, area)
            if m2 is None:
                continue
            mid = m2.get("id")
            if mid in seen:
                continue
            m2["priority_area"] = area
            m2["priority_area_name"] = AREA_NAMES.get(area, area)
            seen[mid] = m2

    # sort: priority order first, then by trendingScore/downloads desc
    area_rank = {k: i for i, k in enumerate([a for _, a in PRIORITY_QUERIES])}
    order = {name: idx for idx, name in enumerate(AREA_NAMES.keys())}
    items = list(seen.values())
    items.sort(
        key=lambda x: (
            order.get(x.get("priority_area"), 99),
            -int(x.get("trendingScore") or 0),
            -int(x.get("downloads") or 0),
        )
    )

    out = []
    for m in items[:25]:  # cap at 25 to keep LLM input small (~1.5k tokens)
        out.append(
            {
                "id": m.get("id"),
                "downloads": m.get("downloads"),
                "priority_area": m.get("priority_area"),
                "priority_area_name": m.get("priority_area_name"),
                "url": f"https://huggingface.co/{m.get('id')}",
            }
        )

    print(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"[OK] {len(out)} unique models", file=sys.stderr)


if __name__ == "__main__":
    main()
