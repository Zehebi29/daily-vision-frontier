#!/usr/bin/env python3
"""
Update models/index.md with latest model & compute digest entries.
Scans models/ directory and regenerates the index.
"""
import os
import re
from datetime import datetime

REPO_DIR = "/home/ubuntu/daily-vision-paper"
MODELS_DIR = os.path.join(REPO_DIR, "models")
INDEX_PATH = os.path.join(MODELS_DIR, "index.md")


def parse_models_meta(filepath):
    """Extract metadata from a model & compute digest markdown file."""
    with open(filepath, "r") as f:
        content = f.read()

    meta = {
        "title": "Models & Compute Digest",
        "date": "",
        "highlights": "",
        "filename": os.path.basename(filepath),
        "item_count": 0,
    }

    # Extract date from filename: YYYY-MM-DD-*.md
    m = re.match(r"(\d{4}-\d{2}-\d{2})", meta["filename"])
    if m:
        meta["date"] = m.group(1)

    # Extract h1 title
    m = re.search(r"^# (.+)$", content, re.MULTILINE)
    if m:
        meta["title"] = m.group(1).strip()

    # Count entries (digest items use h3 headings: "### 1. [Name](link)" or "### [Name](link)")
    items = re.findall(r'^###\s+\d*\.?\s*\[(.+?)\]', content, re.MULTILINE)
    meta["item_count"] = len(items)

    # Extract first few item names as highlights
    highlights = items[:3]
    meta["highlights"] = " · ".join(highlights) if highlights else f"{meta['item_count']} items"

    return meta


def generate_index():
    """Regenerate the models index."""
    os.makedirs(MODELS_DIR, exist_ok=True)

    entries = []
    for fname in sorted(os.listdir(MODELS_DIR), reverse=True):
        if fname.endswith(".md") and fname not in ("index.md", "README.md"):
            fpath = os.path.join(MODELS_DIR, fname)
            meta = parse_models_meta(fpath)
            entries.append(meta)

    lines = [
        "# 🤖 模型层 · 开源模型 & 算力追踪",
        "",
        f"> 共收录 **{len(entries)}** 篇模型/算力日报 | 最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "| 日期 | 摘要 | 亮点 |",
        "|------|------|------|",
    ]

    for e in entries:
        date = e["date"] or "—"
        title = e["title"][:80]
        highlights = e["highlights"] or f"{e['item_count']} items"

        # Link to the digest file on GitHub
        link = f"[{title}](https://github.com/Zehebi29/daily-vision-frontier/blob/main/models/{e['filename']})"

        lines.append(f"| {date} | {link} | {highlights} |")

    lines.extend([
        "",
        "---",
        "",
        "*📅 每日更新*",
        "",
    ])

    with open(INDEX_PATH, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"✅ Models index updated with {len(entries)} entries")
    return len(entries)


if __name__ == "__main__":
    generate_index()
