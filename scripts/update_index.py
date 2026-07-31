#!/usr/bin/env python3
"""
Update papers/index.md with latest paper listing.
Scans papers/ directory and regenerates the index.
"""
import os
import re
from datetime import datetime

REPO_DIR = "/home/ubuntu/daily-vision-paper"
PAPERS_DIR = os.path.join(REPO_DIR, "papers")
INDEX_PATH = os.path.join(PAPERS_DIR, "index.md")


def parse_paper_meta(filepath):
    """Extract metadata from a paper markdown file."""
    with open(filepath, "r") as f:
        content = f.read()
    
    meta = {
        "title": "Unknown",
        "arxiv_id": "",
        "categories": "cs.CV",
        "published": "",
        "tags": "",
        "date": "",  # The paper's analysis date (from filename)
        "filename": os.path.basename(filepath),
    }
    
    # Extract date from filename: YYYY-MM-DD-*.md
    m = re.match(r"(\d{4}-\d{2}-\d{2})", meta["filename"])
    if m:
        meta["date"] = m.group(1)
    
    # Extract title from h1
    m = re.search(r"^# (.+)$", content, re.MULTILINE)
    if m:
        meta["title"] = m.group(1).strip()
    
    # Extract arXiv ID
    m = re.search(r'arxiv\.org/(?:abs|pdf)/([\d\.]+)', content)
    if m:
        meta["arxiv_id"] = m.group(1)
    
    # Extract categories
    m = re.search(r'Category.*?:\s*([^\n]+)', content)
    if m:
        meta["categories"] = m.group(1).strip()
    
    # Extract published date
    m = re.search(r'Published.*?:\s*(\d{4}-\d{2}-\d{2})', content)
    if m:
        meta["published"] = m.group(1)
    
    # Extract tags (support both Chinese 标签 and English Tags)
    m = re.search(r'(?:标签|Tags)\s*\n+`(.+?)`', content)
    if not m:
        m = re.search(r'标签.*?`(.+?)`', content)
    if m:
        meta["tags"] = m.group(1)
    
    return meta


def generate_index():
    """Regenerate the archive index."""
    if not os.path.isdir(PAPERS_DIR):
        os.makedirs(PAPERS_DIR, exist_ok=True)
    
    papers = []
    for fname in sorted(os.listdir(PAPERS_DIR), reverse=True):
        if fname.endswith(".md") and fname not in ("README.md", "index.md"):
            fpath = os.path.join(PAPERS_DIR, fname)
            meta = parse_paper_meta(fpath)
            papers.append(meta)
    
    lines = [
        "# 🔬 学术界 · 论文精读归档",
        "",
        f"> 共收录 **{len(papers)}** 篇论文 | 最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "| 日期 | 论文标题 | arXiv ID | 领域标签 |",
        "|------|----------|----------|----------|",
    ]
    
    for p in papers:
        date = p["date"] or "—"
        title = p["title"]
        arxiv = p["arxiv_id"]
        if arxiv:
            arxiv_link = f"[`{arxiv}`](https://arxiv.org/abs/{arxiv})"
        else:
            arxiv_link = "—"
        tags = p["tags"] or p["categories"]
        
        # Link to the paper file
        paper_link = f"[{title}](https://github.com/Zehebi29/daily-vision-paper/blob/main/papers/{p['filename']})"
        
        lines.append(f"| {date} | {paper_link} | {arxiv_link} | {tags} |")
    
    lines.extend([
        "",
        "---",
        "",
        "*📅 每日更新*",
        "",
    ])
    
    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
    with open(INDEX_PATH, "w") as f:
        f.write("\n".join(lines) + "\n")
    
    print(f"✅ Index updated with {len(papers)} papers")
    return len(papers)


if __name__ == "__main__":
    generate_index()
