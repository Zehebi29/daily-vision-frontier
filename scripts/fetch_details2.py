#!/usr/bin/env python3
"""Fetch article details round 2 — corrected URLs."""
import json, re, urllib.request

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
TIMEOUT = 30

urls = {
    "eetimes_jetson_agents": "https://www.eetimes.com/using-agents-to-maximize-nvidia-jetson-memory-usage-at-the-edge/",
    "eetimes_neuromorphic": "https://www.eetimes.com/neuromorphic-computing-needs-more-than-novel-chips/",
    "eetasia_helios": "https://www.eetasia.com/embeddedblog-amd-launches-helios-the-highest-performing-rackscale-ai-infrastructure-solution/",
    "tomshardware_nvidia_stake": "https://www.tomshardware.com/tech-industry/nvidia-turns-usd5b-intel-stock-bet-into-usd30b-windfall-filing-reveals-new-usd21b-spacex-stake-and-complete-exit-from-arm-stock",
    "tomshardware_jetson_missile": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-jetson-chip-found-in-russian-cruise-missile-ukraine-claims-presence-in-s-71-monochrome-weapon-may-indicate-use-of-ai-tech",
    "eetimes_equipment": "https://www.eetimes.com/semiconductor-equipment-shifts-to-build-to-print-manufacturing/",
    "eetasia_lisa_su": "https://www.eetasia.com/embeddednews-lisa-su-puts-rack-scale-ai-at-center-of-amds-next-growth-phase/",
    "eetasia_smartphone_soc": "https://www.eetasia.com/global-smartphone-soc-shipments-drop-15-as-memory-crisis-hits-1h-2026/",
    "nvidia_jetson_blog": "https://blogs.nvidia.com/blog/build-ai-with-nvidia-jetson/",
    "eetimes_intel_memory": "https://www.eetimes.com/intel-at-a-memory-crossroads-again/",
}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        raw = resp.read().decode("utf-8", "replace")
    except Exception as e:
        return {"url": url, "error": str(e)}
    title = re.search(r"<title[^>]*>(.*?)</title>", raw, re.DOTALL | re.IGNORECASE)
    title = re.sub(r"\s+", " ", title.group(1)).strip() if title else ""
    desc = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)', raw, re.IGNORECASE)
    if not desc:
        desc = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']description["\']', raw, re.IGNORECASE)
    desc = re.sub(r"\s+", " ", desc.group(1)).strip() if desc else ""
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.DOTALL | re.IGNORECASE)
    h1 = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else ""
    h1 = re.sub(r"\s+", " ", h1)
    # article body first paragraphs (strip tags, take meaningful text near top)
    body = re.search(r"<article[^>]*>(.*?)</article>", raw, re.DOTALL | re.IGNORECASE)
    text = ""
    if body:
        text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", body.group(1), flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
    return {"url": url, "title": title, "h1": h1[:200], "description": desc[:500], "body_head": text[:900]}

res = {}
for name, u in urls.items():
    res[name] = fetch(u)

print(json.dumps(res, ensure_ascii=False, indent=1))
