#!/usr/bin/env python3
"""Ad-hoc multi-source fetch for the models & compute digest."""
import json, re, sys, time, urllib.request, urllib.parse
import xml.etree.ElementTree as ET

UA = {"User-Agent": "Mozilla/5.0 (compatible; daily-vision-paper/1.0)"}

def get(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as e:
        print(f"[WARN] {url} -> {e}", file=sys.stderr)
        return ""

def arxiv(query, n=25):
    url = ("https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(query, safe=":+%()\"")
           + f"&start=0&max_results={n}&sortBy=submittedDate&sortOrder=descending")
    x = get(url)
    if not x:
        return
    ns = {"a": "http://www.w3.org/2005/Atom"}
    try:
        r = ET.fromstring(x)
    except Exception as e:
        print("[WARN] parse", e, file=sys.stderr); return
    for e in r.findall("a:entry", ns):
        t = " ".join(e.find("a:title", ns).text.split())
        l = e.find("a:id", ns).text
        d = e.find("a:published", ns).text[:10]
        print(f"  {d} | {t} | {l}")

def hf_api(path):
    x = get("https://huggingface.co/api/" + path)
    if not x:
        return []
    try:
        return json.loads(x)
    except Exception:
        return []

print("=" * 30, "arXiv cs.RO / VLA", "=" * 30)
arxiv('cat:cs.RO AND (abs:"vision-language-action" OR abs:"robot foundation" OR abs:"manipulation policy" OR abs:"world model robot")', 30)

print()
print("=" * 30, "arXiv efficient-vision / edge / quantization", "=" * 30)
arxiv('(abs:"quantization" OR abs:"edge deployment" OR abs:"small vision-language model") AND cat:cs.CV', 25)

print()
print("=" * 30, "arXiv industrial defect / inspection", "=" * 30)
arxiv('(abs:"industrial anomaly detection" OR abs:"defect detection" OR abs:"industrial inspection") AND cat:cs.CV', 20)

print()
print("=" * 30, "HF models: recently created (VLA/robot)", "=" * 30)
for kw in ["vla", "robot", "manipulation"]:
    ms = hf_api(f"models?search={kw}&sort=createdAt&direction=-1&limit=12")
    for m in ms:
        print(f"  {m.get('createdAt','')[:10]} | dl={m.get('downloads')} | {m.get('id')} | {m.get('pipeline_tag')}")
    time.sleep(1)

print()
print("=" * 30, "HF models: trending small VLM / detection", "=" * 30)
for tag in ["image-text-to-text", "object-detection", "image-classification", "image-segmentation"]:
    ms = hf_api(f"models?pipeline_tag={tag}&sort=trendingScore&direction=-1&limit=12")
    for m in ms:
        print(f"  {m.get('createdAt','')[:10]} | dl={m.get('downloads')} | {m.get('id')}")
    time.sleep(1)

print()
print("=" * 30, "HF models: recent gguf / quantized", "=" * 30)
for kw in ["gguf", "awq", "int4"]:
    ms = hf_api(f"models?search={kw}&sort=createdAt&direction=-1&limit=10")
    for m in ms:
        print(f"  {m.get('createdAt','')[:10]} | dl={m.get('downloads')} | {m.get('id')}")
    time.sleep(1)
