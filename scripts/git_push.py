#!/usr/bin/env python3
"""
Git helper for daily-vision-paper.
Commits and pushes all new/modified files.
Usage: python3 scripts/git_push.py "commit message"
"""
import subprocess
import sys
import os

REPO_DIR = "/home/ubuntu/daily-vision-paper"

def run(cmd, capture=True):
    result = subprocess.run(
        cmd, cwd=REPO_DIR, capture_output=capture, text=True, timeout=30
    )
    return result.returncode, result.stdout, result.stderr

def main():
    msg = " ".join(sys.argv[1:]) or "📷 Daily paper update"
    
    # Git config
    os.environ["GIT_TERMINAL_PROMPT"] = "0"
    
    # Stage all changes
    rc, out, err = run(["git", "add", "-A"])
    if rc != 0:
        print(f"git add failed: {err}")
        return 1
    
    # Check if there's something to commit
    rc, out, err = run(["git", "diff", "--cached", "--quiet"])
    if rc == 0:
        print("Nothing to commit.")
        return 0
    
    # Commit
    rc, out, err = run(["git", "commit", "-m", msg])
    if rc != 0:
        print(f"git commit failed: {err}")
        return 1
    print(out.strip())
    
    # Push
    rc, out, err = run(["git", "push"])
    if rc != 0:
        print(f"git push failed: {err}")
        return 1
    print(out.strip())
    
    print(f"✅ Pushed: {msg}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
