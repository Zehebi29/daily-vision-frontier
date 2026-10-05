#!/usr/bin/env python3
import json, re, sys, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (compatible; daily-vision-paper/1.0)"}
GH = {**UA, "Accept": "application/vnd.github+json"}

def get(url, hdr=None, timeout=25):
    req = urllib.request.Request(url, headers=hdr or UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as e:
        print(f"[WARN] {url} -> {e}", file=sys.stderr)
        return ""

for repo in ["zhengzihaoPKU/RoboECC", "Zhenxintao/MiniVLA", "FastCrest/tether"]:
    print("=" * 60)
    d = json.loads(get(f"https://api.github.com/repos/{repo}") or "{}")
    print(f"{repo} ★{d.get('stargazers_count')} | {d.get('description')}")
    print("  created:", (d.get('created_at') or '')[:10], "| lang:", d.get('language'), "| license:", (d.get('license') or {}).get('spdx_id'))
    md = get(f"https://raw.githubusercontent.com/{repo}/main/README.md")
    if not md:
        md = get(f"https://raw.githubusercontent.com/{repo}/master/README.md")
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)
    md = re.sub(r"<[^>]+>", "", md)
    print(md[:1600])
    print()

print("=" * 60)
print("HF search: rho vla / streamvln / small vla")
for kw in ["rho+vla", "streamvln", "lingbot-vla"]:
    d = json.loads(get(f"https://huggingface.co/api/models?search={kw}&limit=6") or "[]")
    for m in d:
        print(f"  {m.get('id')} | dl={m.get('downloads')} | {m.get('pipeline_tag')}")
