#!/usr/bin/env python3
"""Round 3: fetch abstracts by arXiv id + HF card snippets."""
import json, re, sys, time, urllib.request
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

IDS = [
    "2609.38164",  # Rho
    "2609.35570",  # EdgeVLN
    "2609.38811",  # DCM-SAM
    "2609.39514",  # Spike-driven VLA
    "2609.39822",  # Real-time VLAs
    "2609.33325",  # VisionHOPE
    "2609.28262",  # RAMP
    "2609.39973",  # EWAM
    "2609.39870",  # Magic-W0
    "2609.34867",  # P4Q
    "2609.30629",  # FRESHLATENT
    "2609.24526",  # ME-VLM
    "2609.39427",  # PCB-MC
    "2609.37314",  # FLASH
    "2609.24875",  # SPHQuant
]

url = "https://export.arxiv.org/api/query?id_list=" + ",".join(IDS) + "&max_results=50"
x = get(url)
ns = {"a": "http://www.w3.org/2005/Atom"}
r = ET.fromstring(x)
for e in r.findall("a:entry", ns):
    aid = e.find("a:id", ns).text.split("/abs/")[-1]
    t = " ".join((e.find("a:title", ns).text or "").split())
    s = " ".join((e.find("a:summary", ns).text or "").split())
    print(f"### {aid} | {t}")
    print(s[:1300])
    print()
