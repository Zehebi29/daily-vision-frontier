#!/usr/bin/env python3
"""arXiv recent-listing scraper — API-free fallback.

The Atom API (export.arxiv.org/api/query) 429s hard under cron; the /list pages
do not. Parse <dt>/<dd> blocks straight off the listing, keep keyword hits.

Usage: python3 scripts/search_arxiv_recent.py [--cats cs.RO,cs.CV] [--pages 2] [--grep vla,edge]
"""
import argparse, html, re, sys, urllib.request

URL = "https://arxiv.org/list/{cat}/recent?skip={skip}&show=100"
DEFAULT_GREP = ("vla", "vision-language-action", "robot", "edge", "on-device", "quantiz",
                "distill", "jetson", "npu", "industrial", "defect", "anomaly", "efficient", "tiny")

_ID = re.compile(r'id="(\d{4}\.\d{4,5})"')
_TITLE = re.compile(r"<span class='descriptor'>Title:</span>\s*(.*?)\s*</div>", re.S)
_TAGS = re.compile(r"<[^>]+>")


def parse_listing(page: str):
    """HTML -> [(arxiv_id, title), ...] in listing order. Pure; no I/O."""
    out = []
    for block in page.split("<dt>")[1:]:
        mid, mti = _ID.search(block), _TITLE.search(block)
        if mid and mti:
            title = " ".join(html.unescape(_TAGS.sub("", mti.group(1))).split())
            out.append((mid.group(1), title))
    return out


def fetch(cat: str, pages: int = 2):
    """Yield de-duped (id, title) across pages. arXiv caps show at 100."""
    seen = set()
    for page in range(pages):
        url = URL.format(cat=cat, skip=page * 100)
        req = urllib.request.Request(url, headers={"User-Agent": "daily-vision-paper/1.0"})
        try:
            body = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")
        except Exception as e:                      # noqa: BLE001 — cron must not die on one cat
            print(f"[WARN] {cat} page {page}: {e}", file=sys.stderr)
            continue
        for aid, title in parse_listing(body):
            if aid not in seen:
                seen.add(aid)
                yield aid, title


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cats", default="cs.RO")
    ap.add_argument("--pages", type=int, default=2)
    ap.add_argument("--grep", default=",".join(DEFAULT_GREP))
    a = ap.parse_args()
    kws = [k.strip().lower() for k in a.grep.split(",") if k.strip()]

    hits = 0
    for cat in [c.strip() for c in a.cats.split(",") if c.strip()]:
        for aid, title in fetch(cat, a.pages):
            if any(k in title.lower() for k in kws):
                hits += 1
                print(f"{cat}\t{aid}\thttps://arxiv.org/abs/{aid}\t{title}")
    print(f"[OK] {hits} keyword hits", file=sys.stderr)


if __name__ == "__main__":
    main()
