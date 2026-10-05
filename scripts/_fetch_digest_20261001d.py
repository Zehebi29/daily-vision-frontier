#!/usr/bin/env python3
import json, sys, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (compatible; daily-vision-paper/1.0)"}

def get(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as e:
        print(f"[WARN] {url} -> {e}", file=sys.stderr)
        return ""

# HF model cards (README) snippets
for mid in [
    "XingChen-AGI/TeleOCR",
    "amd/gemma-4-e4b-it-mobius-int4_rai_1.8.0_medusa_1.0_npu",
    "Ultralytics/YOLO26",
    "microsoft/VITRA-VLA-3B",
]:
    print("=" * 60)
    print("README:", mid)
    md = get(f"https://huggingface.co/{mid}/raw/main/README.md")
    # strip yaml front matter
    if md.startswith("---"):
        parts = md.split("---", 2)
        md = parts[2] if len(parts) > 2 else md
    print(md[:1400])
    print()
