#!/usr/bin/env python3
"""Fetch article pages and extract readable text snippets for curation."""
import re, html, urllib.request, json

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
TIMEOUT = 20

URLS = {
    "sony_mitsubishi": "https://www.sony-semicon.com/en/news/2026/2026072201.html",
    "sony_sensor": "https://www.sony-semicon.com/en/news/2026/2026062401.html",
    "nxp_ambarella": "https://www.eetimes.com/nxp-eying-ambarella-is-it-about-automotive-or-edge-ai/",
    "neuromorphic": "https://semiengineering.com/chip-bridges-neuromorphic-and-deep-network-computing-tu-dresden/",
    "amd_x100": "https://www.amd.com/news/aai-2026-ryzen-ai-embedded-x100/",
    "amd_kria": "https://www.amd.com/news/aai-2026-kria-robotics-dev-platform/",
    "nvidia_alpamayo": "https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/",
    "hbf_spec": "https://www.tomshardware.com/pc-components/ssds/sandisk-and-sk-hynix-unveil-hbf-spec-up-to-16-hi-nan",
    "cn_litho": "https://www.tomshardware.com/tech-industry/semiconductors/chinese-chipmaking-tool-roadmap-examined",
    "largest_chips": "https://semiengineering.com/from-blueprint-to-build-engineering-the-worlds-largest-ai-chips/",
}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"})
    try:
        raw = urllib.request.urlopen(req, timeout=TIMEOUT).read()
        return raw.decode("utf-8", errors="ignore")
    except Exception as e:
        return f"ERROR: {e}"

def clean_text(html_text):
    # drop scripts/styles
    html_text = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", " ", html_text, flags=re.DOTALL | re.I)
    html_text = re.sub(r"<br\s*/?>", "\n", html_text, flags=re.I)
    html_text = re.sub(r"</(p|div|h1|h2|h3|li|tr)>", "\n", html_text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", html_text)
    text = html.unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    return text.strip()

out = {}
for name, url in URLS.items():
    raw = fetch(url)
    if raw.startswith("ERROR"):
        out[name] = {"url": url, "error": raw, "text": ""}
        continue
    txt = clean_text(raw)
    # grab the meaty middle
    lines = [l.strip() for l in txt.split("\n") if len(l.strip()) > 40]
    out[name] = {"url": url, "error": None, "text": "\n".join(lines[:60])}

print(json.dumps(out, ensure_ascii=False, indent=1))
