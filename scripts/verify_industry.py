#!/usr/bin/env python3
"""Verify details for curated candidates."""
import json, urllib.request, re

UA = {"User-Agent": "Mozilla/5.0 (compatible; DailyVisionPaper/1.0)"}
def get(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

out = {}

# GitHub repos
repos = ["csslc/PixRestore", "zhaozhen2333/Turbo-Learning", "TedLentsch/TokenGraph3D",
         "shanliuling/dsh-image-gen", "MJorgin/dsh-media-skills", "JackCD99/Native-Adversariality-Mining",
         "ZSeven-W/dsh-crew", "forever-free1/FIRE-VLA"]
gh = {}
for r in repos:
    try:
        d = json.loads(get(f"https://api.github.com/repos/{r}"))
        gh[r] = {"stars": d.get("stargazers_count"), "created": d.get("created_at", "")[:10],
                 "updated": d.get("pushed_at", "")[:10], "desc": (d.get("description") or "")[:200],
                 "lang": d.get("language"), "license": (d.get("license") or {}).get("spdx_id")}
    except Exception as e:
        gh[r] = {"error": str(e)}
out["github"] = gh

# HF model cards
models = ["realrebelai/Rebels_w4a8s", "OpenMOSS-Team/MOSS-VL-Realtime-FP8",
          "bench-labs/objectmodel-v1", "Qwen/Qwen3.8-27B", "lodestones/Kroma",
          "NemoStation/Marlin-2B"]
hf = {}
for m in models:
    try:
        d = json.loads(get(f"https://huggingface.co/api/models/{m}"))
        hf[m] = {"dl": d.get("downloads"), "likes": d.get("likes"), "ts": d.get("trendingScore"),
                 "created": d.get("createdAt", "")[:10], "tag": d.get("pipeline_tag"),
                 "card": (d.get("cardData") or {}),
                 "tags": [t for t in d.get("tags", []) if t not in ("pytorch","transformers","safetensors","license:other","region:us")][:8]}
    except Exception as e:
        hf[m] = {"error": str(e)}
out["hf"] = hf

# Roboflow blog headline
try:
    html = get("https://blog.roboflow.com/openai-gpt-5-6/").decode("utf-8", "ignore")
    m = re.search(r"<title>(.*?)</title>", html, re.DOTALL)
    out["roboflow_title"] = m.group(1).strip() if m else ""
    # grab first paragraph-ish text
    txt = re.sub(r"<script.*?</script>", "", html, flags=re.DOTALL)
    txt = re.sub(r"<[^>]+>", " ", txt)
    txt = re.sub(r"\s+", " ", txt)
    i = txt.find("GPT-5.6")
    out["roboflow_snippet"] = txt[max(0,i-100):i+600] if i >= 0 else txt[:400]
except Exception as e:
    out["roboflow"] = {"error": str(e)}

print(json.dumps(out, indent=1, ensure_ascii=False))
