#!/usr/bin/env python3
"""Fetch article details (title + meta description) for candidate stories."""
import json, re, urllib.request, urllib.error

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
TIMEOUT = 20

urls = {
    "sony_semicon_news": "https://www.sony-semicon.com/en/news/",
    "semianalysis_rubin_cpx": "https://semianalysis.com/2026/08/14/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack/",
    "eetimes_jetson_agents": "https://www.eetimes.com/using-agents-to-maximize-nvidia-jetson-memory-usage-at-the-edge/",
    "semiengineering_npu": "https://semiengineering.com/packet-based-npus-in-the-llm-era-from-compute-bound-cnns-to-memory-bound-edge-and-automotive-workloads/",
    "eetimes_neuromorphic": "https://www.eetimes.com/neuromorphic-computing-needs-more-than-novel-chips/",
    "eetasia_helios": "https://www.eetasia.com/amd-launches-helios-the-highest-performing-rackscale-ai-infrastructure-solution/",
    "tomshardware_nvidia_stake": "https://www.tomshardware.com/pc-components/gpus/nvidia-turns-usd5b-intel-stock-bet-into-usd30b-windfall-filing-reveals-new-usd21b-spacex-stake-and-complete-intel-exit",
    "semiengineering_1mw_rack": "https://semiengineering.com/the-1-megawatt-rack-debate/",
    "eetasia_smartphone_soc": "https://www.eetasia.com/global-smartphone-soc-shipments-drop-15-as-memory-crisis-hits-1h-2026/",
    "eetimes_equipment": "https://www.eetimes.com/semiconductor-equipment-shifts-to-build-to-print-manufacturing/",
    "seeed_hailo8": "https://github.com/Seeed-Projects/reComputer-Hailo8-CV",
    "zynq_accel": "https://github.com/a2307588073-arch/zynq-yolov3-tiny-accelerator",
    "neuromorphic_webcam": "https://github.com/Syedmeasum14/Neuromorphic-Webcam",
    "amd_newsroom_search": "https://www.amd.com/en/newsroom.html",
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
    # grab some text: og:title, first h1
    og = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)', raw, re.IGNORECASE)
    og = re.sub(r"\s+", " ", og.group(1)).strip() if og else ""
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.DOTALL | re.IGNORECASE)
    h1 = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else ""
    h1 = re.sub(r"\s+", " ", h1)
    return {"url": url, "title": title, "og_title": og, "h1": h1[:160], "description": desc[:600]}

res = {}
for name, u in urls.items():
    res[name] = fetch(u)

print(json.dumps(res, ensure_ascii=False, indent=1))
