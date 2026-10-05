#!/usr/bin/env python3
"""Round 2: arXiv (simpler queries), HF model details, GitHub search."""
import json, sys, time, urllib.request, urllib.parse
import xml.etree.ElementTree as ET

UA = {"User-Agent": "Mozilla/5.0 (compatible; daily-vision-paper/1.0)"}

def get(url, timeout=30, hdr=None):
    req = urllib.request.Request(url, headers=hdr or UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as e:
        print(f"[WARN] {url} -> {e}", file=sys.stderr)
        return ""

def arxiv(query, n=25, label=""):
    url = ("https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(query, safe=":")
           + f"&start=0&max_results={n}&sortBy=submittedDate&sortOrder=descending")
    x = get(url)
    print(f"--- {label} ---")
    if not x:
        return
    ns = {"a": "http://www.w3.org/2005/Atom"}
    try:
        r = ET.fromstring(x)
    except Exception as e:
        print("  [WARN] parse", e, file=sys.stderr); return
    for e in r.findall("a:entry", ns):
        t = " ".join((e.find("a:title", ns).text or "").split())
        l = e.find("a:id", ns).text
        d = e.find("a:published", ns).text[:10]
        print(f"  {d} | {t} | {l}")

def hf_details(mid):
    x = get("https://huggingface.co/api/models/" + mid)
    if not x:
        return None
    try:
        return json.loads(x)
    except Exception:
        return None

arxiv("all:vision-language-action", 25, "VLA (all fields)")
print()
arxiv("all:robot+foundation+model", 20, "robot foundation model")
print()
arxiv("cat:cs.CV AND all:quantization", 20, "cs.CV quantization")
print()
arxiv("cat:cs.CV AND all:edge+deployment", 20, "cs.CV edge deployment")
print()
arxiv("all:industrial+anomaly+detection", 20, "industrial anomaly detection")
print()
arxiv("cat:cs.RO AND all:world+model", 15, "cs.RO world model")
print()

print("=" * 30, "HF model details", "=" * 30)
for mid in [
    "microsoft/VITRA-VLA-3B",
    "tencent/Hy-Embodied-0.5-VLA-UMI",
    "apple/LensVLM-9B",
    "PSRben/VisionHOPE",
    "asgersvenning/MAMBO-v3",
    "Ultralytics/YOLO26",
    "amd/gemma-4-e4b-it-mobius-int4_rai_1.8.0_medusa_1.0_npu",
    "DILL-VLA/disentangled-vla-libero-eef-qwen25vl",
    "tsangb34/lingbot-vla-v2-6b-so101-cube-drawer-10ep",
    "nvidia/Cosmos-Predict2-2B-Sample-Action-Conditioned",
    "Robot-Haus/Qwen3.8-Flash-Next-oQ3.5e-fp16-mtp",
    "XingChen-AGI/TeleOCR",
]:
    d = hf_details(mid)
    if not d:
        print(f"  [MISS] {mid}"); continue
    saf = d.get("safetensors") or {}
    print(f"  {mid}")
    print(f"     created={str(d.get('createdAt'))[:10]} dl={d.get('downloads')} likes={d.get('likes')} pipe={d.get('pipeline_tag')}")
    print(f"     tags={[t for t in (d.get('tags') or [])][:14]}")
    print(f"     params={saf.get('total')} dtype={saf.get('parameters')}")
    time.sleep(0.5)

print()
print("=" * 30, "GitHub search (created last 21d)", "=" * 30)
since = time.strftime("%Y-%m-%d", time.gmtime(time.time() - 21 * 86400))
for q in ["vision+language+action", "robot+foundation+model", "edge+vision", "industrial+inspection", "vla+robot"]:
    url = f"https://api.github.com/search/repositories?q={q}+created:>{since}&sort=stars&order=desc&per_page=8"
    x = get(url, hdr={**UA, "Accept": "application/vnd.github+json"})
    print(f"--- {q} ---")
    if not x:
        continue
    try:
        d = json.loads(x)
    except Exception:
        print("  parse fail"); continue
    for it in d.get("items", []):
        print(f"  ★{it['stargazers_count']:>5} | {it['full_name']} | {(it.get('description') or '')[:95]} | {it['created_at'][:10]}")
    time.sleep(2)
