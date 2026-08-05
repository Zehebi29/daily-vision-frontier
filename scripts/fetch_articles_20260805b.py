#!/usr/bin/env python3
"""Round 2 fetches: retries + alternates."""
import re, html, urllib.request, json

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
TIMEOUT = 45

URLS = {
    "nxp_ambarella": "https://www.eetimes.com/nxp-eying-ambarella-is-it-about-automotive-or-edge-ai/",
    "hbf_toms": "https://www.tomshardware.com/pc-components/ssds/sandisk-and-sk-hynix-unveil-hbf-spec-up-to-16-hi-nan",
    "kioxia_nand": "https://www.tomshardware.com/pc-components/ssds/kioxia-and-sandisk-demonstrate-the-worlds-highest-de",
    "amd_embedded_presskit": "https://www.amd.com/press-kits/advancing-ai-2026-all-news/",
    "amd_earnings": "https://www.amd.com/news/amd-2q-2026-earnings/",
    "sony_xray": "https://www.sony-semicon.com/en/news/2026/2026060901.html",
    "ovt_news": "https://www.ovt.com/news/",
    "ovt_news2": "https://www.ovt.com/news-events/",
}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})
    try:
        raw = urllib.request.urlopen(req, timeout=TIMEOUT).read()
        return raw.decode("utf-8", errors="ignore")
    except Exception as e:
        return f"ERROR: {e}"

def clean_text(html_text):
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
    lines = [l.strip() for l in txt.split("\n") if len(l.strip()) > 40]
    # dedupe consecutive
    dedup = []
    for l in lines:
        if not dedup or dedup[-1] != l:
            dedup.append(l)
    out[name] = {"url": url, "error": None, "text": "\n".join(dedup[:80])}

print(json.dumps(out, ensure_ascii=False, indent=1))
