#!/usr/bin/env python3
"""Pass 3: robust re-fetch of the sources that pass 1/2 failed on.

Pass-1 `search_industry.py` returned 0 GitHub-trending items (stale regex) and an
empty HF-newest list, and Reddit's `hot.json` is 403. This script covers:

  - GitHub trending (all + python), parsed by `<article class="Box-row">` blocks
  - GitHub Search API: new repos created in the last 7 days
  - HF models ranked by trendingScore, over CV pipelines
  - HF models that are recent *and* notable (likes-ranked, then age-filtered)
  - HF daily papers
  - Reddit via the RSS endpoint (json is 403 / 429)
"""
import json, re, time, urllib.request
from datetime import datetime, timedelta

UA = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "text/html,application/json,*/*",
}

CV_PIPES = ["text-to-image", "image-to-image", "image-segmentation", "object-detection",
            "image-text-to-text", "video-text-to-text", "depth-estimation",
            "image-classification", "text-to-video", "image-to-video", "any-to-any",
            "keypoint-detection", "zero-shot-image-classification", "mask-generation"]

# tags that add no signal to a digest line
_NOISE = {"pytorch", "transformers", "safetensors", "license:other", "region:us",
          "diffusers", "en", "endpoints_compatible", "eval-results"}


def raw(url, timeout=25):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read().decode("utf-8", "ignore")


def js(url, timeout=25):
    return json.loads(raw(url, timeout))


# ── pure parsers (imported by tests; no network) ─────────────────────────────

def parse_gh_trending(html):
    """Parse a github.com/trending page into repo records."""
    items = []
    for block in re.split(r'<article class="Box-row">', html)[1:]:
        m = re.search(r'<h2[^>]*>\s*<a[^>]*href="/([^"]+)"', block)
        if not m:
            continue
        full = m.group(1).strip()
        desc = re.search(r'<p class="col-9 color-fg-muted my-1 pr-4">\s*(.*?)\s*</p>',
                         block, re.DOTALL)
        stars = re.search(r'href="/[^"]+/stargazers"[^>]*>.*?</svg>\s*([\d,]+)', block, re.DOTALL)
        today = re.search(r'([\d,]+)\s*stars today', block)
        lang = re.search(r'itemprop="programmingLanguage">([^<]+)<', block)
        items.append({
            "repo": full,
            "desc": re.sub(r"<[^>]+>", "", desc.group(1)).strip()[:200] if desc else "",
            "stars": stars.group(1) if stars else "",
            "stars_today": today.group(1) if today else "",
            "lang": lang.group(1) if lang else "",
            "url": f"https://github.com/{full}",
        })
    return items


def parse_reddit_rss(xml):
    """Parse a Reddit .rss feed into post records."""
    items = []
    for entry in re.findall(r"<entry>(.*?)</entry>", xml, re.DOTALL):
        title = re.search(r"<title>(.*?)</title>", entry, re.DOTALL)
        link = re.search(r'<link href="([^"]+)"', entry)
        updated = re.search(r"<updated>(.*?)</updated>", entry)
        items.append({
            "title": re.sub(r"<[^>]+>", "", title.group(1)).strip() if title else "",
            "url": link.group(1) if link else "",
            "updated": updated.group(1)[:10] if updated else "",
        })
    return items


# ── fetchers ────────────────────────────────────────────────────────────────

def gh_trending(lang=""):
    try:
        return parse_gh_trending(raw(f"https://github.com/trending/{lang}?since=daily"))
    except Exception as e:
        return {"error": str(e)}


def github_search(queries, since):
    out = {}
    for label, q in queries.items():
        try:
            data = js(f"https://api.github.com/search/repositories?q={q}+created:%3E{since}"
                      f"&sort=stars&order=desc&per_page=6")
            out[label] = [{
                "full_name": i["full_name"], "stars": i["stargazers_count"],
                "desc": (i.get("description") or "")[:180], "lang": i.get("language"),
                "created": (i.get("created_at") or "")[:10], "pushed": (i.get("pushed_at") or "")[:10],
                "url": i["html_url"], "topics": i.get("topics", [])[:6],
                "license": (i.get("license") or {}).get("spdx_id"),
            } for i in data.get("items", [])]
        except Exception as e:
            out[label] = {"error": str(e)}          # unauth API rate-limits freely
        time.sleep(1.5)
    return out


def hf_row(m):
    return {
        "model_id": m.get("modelId"), "ts": m.get("trendingScore", 0),
        "downloads": m.get("downloads", 0), "likes": m.get("likes", 0),
        "created": (m.get("createdAt") or "")[:10],
        "tags": [t for t in m.get("tags", []) if t not in _NOISE][:6],
        "license": next((t.split(":", 1)[1] for t in m.get("tags", [])
                         if t.startswith("license:")), ""),
        "url": f"https://huggingface.co/{m.get('modelId')}",
    }


def hf_trending(pipelines):
    out = {}
    for tag in pipelines:
        try:
            out[tag] = [hf_row(m) for m in js(
                f"https://huggingface.co/api/models?pipeline_tag={tag}"
                f"&sort=trendingScore&direction=-1&limit=6")]
        except Exception as e:
            out[tag] = {"error": str(e)}
    return out


def hf_recent_notable(pipelines, days=30, min_likes=5, window=500):
    """CV-pipeline models created in the last `days` days with real traction.

    Note: sorting by createdAt is a firehose -- brand-new uploads have zero
    likes/downloads, so a signal filter over that feed structurally yields
    nothing. Rank by likes instead, then filter by age.
    """
    cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    try:
        rows = [m for m in js(f"https://huggingface.co/api/models?sort=likes"
                              f"&direction=-1&limit={window}")
                if m.get("pipeline_tag") in pipelines
                and (m.get("createdAt") or "")[:10] >= cutoff
                and m.get("likes", 0) >= min_likes]
        rows.sort(key=lambda m: -m.get("likes", 0))
        return [{"model_id": m.get("modelId"), "tag": m.get("pipeline_tag"),
                 "dl": m.get("downloads", 0), "likes": m.get("likes", 0),
                 "ts": m.get("trendingScore", 0), "created": (m.get("createdAt") or "")[:10],
                 "url": f"https://huggingface.co/{m.get('modelId')}"} for m in rows][:40]
    except Exception as e:
        return {"error": str(e)}


def hf_papers(limit=30):
    try:
        return [{
            "title": p.get("paper", {}).get("title", ""),
            "id": p.get("paper", {}).get("id", ""),
            "url": p.get("paper", {}).get("url", ""),
            "upvotes": p.get("upvotes", 0),
            "tag": p.get("paper", {}).get("pipeline_tag", ""),
            "published": (p.get("paper", {}).get("publishedAt") or "")[:10],
            "summary": (p.get("paper", {}).get("summary") or "")[:300],
        } for p in js(f"https://huggingface.co/api/daily_papers?limit={limit}")]
    except Exception as e:
        return {"error": str(e)}


def reddit(sub):
    try:
        return parse_reddit_rss(raw(f"https://www.reddit.com/r/{sub}/hot/.rss?limit=15"))
    except Exception as e:
        return {"error": str(e)}


def main():
    since = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    out = {
        "gh_trending_all": gh_trending(""),
        "gh_trending_python": gh_trending("python"),
        "github_search_date_filter": since,
        "github_search": github_search({
            "cv": "computer+vision", "diffusion": "diffusion+model", "imagegen": "image+generation",
            "vlm": "vision+language", "segment": "segmentation", "3dvision": "3d+reconstruction",
            "video": "video+generation", "ocr": "document+understanding",
        }, since),
        "hf_trending": hf_trending(CV_PIPES),
        "hf_recent_notable": hf_recent_notable(CV_PIPES),
        "hf_papers": hf_papers(),
    }
    for sub in ["computervision", "MachineLearning", "StableDiffusion", "LocalLLaMA"]:
        out[f"reddit_{sub}"] = reddit(sub)
        time.sleep(1)
    print(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
