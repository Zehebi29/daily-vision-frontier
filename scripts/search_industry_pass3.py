#!/usr/bin/env python3
"""Pass 3: robust re-fetch of the sources that failed in pass 1/2.

- GitHub trending: parse with BeautifulSoup-ish regex on data-href / h2 > a
- GitHub search API for NEW CV repos (past week) -- multiple query shapes
- HF trending models by trendingScore, CV pipelines
- HF newest models by createdAt, CV pipelines
- HF daily papers
- Reddit via old.reddit.com/.rss (json is 403)
- HuggingFace blog / GitHub trending python
"""
import json, re, time, urllib.request, urllib.error
from datetime import datetime, timedelta

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
      "Accept": "text/html,application/json,*/*"}

def raw(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "ignore")

def js(url, timeout=25):
    return json.loads(raw(url, timeout))

out = {}

# ── 1. GitHub trending (both all + python), robust block parse ──
def gh_trending(lang=""):
    try:
        html = raw(f"https://github.com/trending/{lang}?since=daily")
    except Exception as e:
        return {"error": str(e)}
    arts = re.split(r'<article class="Box-row">', html)[1:]
    items = []
    for a in arts:
        m = re.search(r'<h2[^>]*>\s*<a[^>]*href="/([^"]+)"', a)
        if not m:
            continue
        full = m.group(1).strip()
        d = re.search(r'<p class="col-9 color-fg-muted my-1 pr-4">\s*(.*?)\s*</p>', a, re.DOTALL)
        desc = re.sub(r"<[^>]+>", "", d.group(1)).strip() if d else ""
        s = re.search(r'/stargazers">\s*<svg.*?</svg>\s*([\d,]+)', a, re.DOTALL)
        today = re.search(r'([\d,]+)\s*stars today', a)
        langm = re.search(r'itemprop="programmingLanguage">([^<]+)<', a)
        items.append({"repo": full, "desc": desc[:200],
                      "stars": s.group(1) if s else "",
                      "stars_today": today.group(1) if today else "",
                      "lang": langm.group(1) if langm else "",
                      "url": f"https://github.com/{full}"})
    return items

out["gh_trending_all"] = gh_trending("")
out["gh_trending_python"] = gh_trending("python")

# ── 2. GitHub search: new repos past week ──
week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
gh = {}
queries = {
    "cv": "computer+vision",
    "diffusion": "diffusion+model",
    "imagegen": "image+generation",
    "vlm": "vision+language",
    "segment": "segmentation",
    "3dvision": "3d+reconstruction",
    "video": "video+generation",
    "ocr": "document+understanding",
}
for label, q in queries.items():
    url = (f"https://api.github.com/search/repositories?q={q}+created:%3E{week_ago}"
           f"&sort=stars&order=desc&per_page=6")
    try:
        data = js(url)
        gh[label] = [{
            "full_name": i["full_name"], "stars": i["stargazers_count"],
            "desc": (i.get("description") or "")[:180], "lang": i.get("language"),
            "created": i.get("created_at", "")[:10], "pushed": i.get("pushed_at", "")[:10],
            "url": i["html_url"], "topics": i.get("topics", [])[:6],
            "license": (i.get("license") or {}).get("spdx_id"),
        } for i in data.get("items", [])]
    except Exception as e:
        gh[label] = {"error": str(e)}
    time.sleep(1.5)
out["github_search"] = gh
out["github_search_date_filter"] = week_ago

# ── 3. HF trending models (trendingScore) ──
CV_PIPES = ["text-to-image", "image-to-image", "image-segmentation", "object-detection",
            "image-text-to-text", "video-text-to-text", "depth-estimation",
            "image-classification", "text-to-video", "image-to-video", "any-to-any",
            "keypoint-detection", "zero-shot-image-classification", "mask-generation"]
hf = {}
for tag in CV_PIPES:
    url = (f"https://huggingface.co/api/models?pipeline_tag={tag}"
           f"&sort=trendingScore&direction=-1&limit=6")
    try:
        data = js(url)
        hf[tag] = [{
            "model_id": m.get("modelId"), "ts": m.get("trendingScore", 0),
            "downloads": m.get("downloads", 0), "likes": m.get("likes", 0),
            "created": (m.get("createdAt") or "")[:10],
            "tags": [t for t in m.get("tags", []) if t not in
                     ("pytorch", "transformers", "safetensors", "license:other", "region:us",
                      "diffusers", "en")][:6],
            "license": next((t.split(":", 1)[1] for t in m.get("tags", []) if t.startswith("license:")), ""),
            "url": f"https://huggingface.co/{m.get('modelId')}",
        } for m in data]
    except Exception as e:
        hf[tag] = {"error": str(e)}
out["hf_trending"] = hf

# ── 4. HF newest models created recently ──
try:
    data = js("https://huggingface.co/api/models?sort=createdAt&direction=-1&limit=200")
    newest = []
    for m in data:
        if m.get("pipeline_tag") in CV_PIPES:
            if (m.get("downloads", 0) + m.get("likes", 0)) < 30:
                continue
            newest.append({"model_id": m.get("modelId"), "tag": m.get("pipeline_tag"),
                           "dl": m.get("downloads", 0), "likes": m.get("likes", 0),
                           "ts": m.get("trendingScore", 0),
                           "created": (m.get("createdAt") or "")[:10],
                           "url": f"https://huggingface.co/{m.get('modelId')}"})
    out["hf_newest_cv"] = newest[:40]
except Exception as e:
    out["hf_newest_cv"] = {"error": str(e)}

# ── 5. HF daily papers ──
try:
    data = js("https://huggingface.co/api/daily_papers?limit=30")
    out["hf_papers"] = [{
        "title": p.get("paper", {}).get("title", ""),
        "id": p.get("paper", {}).get("id", ""),
        "url": p.get("paper", {}).get("url", ""),
        "upvotes": p.get("upvotes", 0),
        "tag": p.get("paper", {}).get("pipeline_tag", ""),
        "published": (p.get("paper", {}).get("publishedAt") or "")[:10],
        "summary": (p.get("paper", {}).get("summary") or "")[:300],
    } for p in data]
except Exception as e:
    out["hf_papers"] = {"error": str(e)}

# ── 6. Reddit RSS fallback ──
def reddit_rss(sub):
    try:
        xml = raw(f"https://www.reddit.com/r/{sub}/hot/.rss?limit=15")
        entries = re.findall(r"<entry>(.*?)</entry>", xml, re.DOTALL)
        items = []
        for e in entries:
            t = re.search(r"<title>(.*?)</title>", e, re.DOTALL)
            l = re.search(r'<link href="([^"]+)"', e)
            u = re.search(r"<updated>(.*?)</updated>", e)
            items.append({
                "title": re.sub(r"<[^>]+>", "", t.group(1)).strip() if t else "",
                "url": l.group(1) if l else "",
                "updated": u.group(1)[:10] if u else "",
            })
        return items
    except Exception as ex:
        return {"error": str(ex)}

for sub in ["computervision", "MachineLearning", "StableDiffusion", "LocalLLaMA"]:
    out[f"reddit_{sub}"] = reddit_rss(sub)
    time.sleep(1)

print(json.dumps(out, indent=1, ensure_ascii=False))
