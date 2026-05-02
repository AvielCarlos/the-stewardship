#!/usr/bin/env python3
"""Refresh Mission Control state.json from live sources.

Sources (best-effort; missing tools just leave fields as-is):
- gh CLI for PRs/issues
- curl for backend health
- railway CLI for deploy info (optional)

Safe to run multiple times. No external writes.
"""
from __future__ import annotations

import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "state.json"

REPOS = ["AvielCarlos/connectome-backend", "AvielCarlos/connectome-web", "AvielCarlos/the-stewardship"]
HEALTH_URL = "https://connectome-api-production.up.railway.app/health"


def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def run(cmd: list[str], timeout: int = 30) -> str:
    try:
        out = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=timeout)
        return out.stdout.strip()
    except Exception:
        return ""


def gh_open_prs(repo: str) -> list[dict]:
    if not have("gh"):
        return []
    raw = run(["gh", "pr", "list", "-R", repo, "--state", "open", "--json", "number,title,author,isDraft,reviewDecision,updatedAt"])
    if not raw:
        return []
    try:
        return json.loads(raw)
    except Exception:
        return []


def gh_top_issues(repo: str, limit: int = 10) -> list[dict]:
    if not have("gh"):
        return []
    raw = run(["gh", "issue", "list", "-R", repo, "--state", "open", "--limit", str(limit), "--json", "number,title,labels,updatedAt"])
    if not raw:
        return []
    try:
        return json.loads(raw)
    except Exception:
        return []


def backend_health() -> str:
    code = run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", HEALTH_URL], timeout=15)
    return code or "unknown"


def main() -> None:
    state = json.loads(STATE_PATH.read_text())
    state["last_refresh"] = datetime.now(timezone.utc).isoformat()

    for full in REPOS:
        short = full.split("/", 1)[1]
        if short not in state["repos"]:
            continue
        state["repos"][short]["open_prs"] = gh_open_prs(full)
        state["repos"][short]["top_issues"] = gh_top_issues(full)

    state["deploys"]["connectome-api_health"] = backend_health()
    state["deploys"]["last_check"] = state["last_refresh"]

    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n")
    print(f"Mission Control state refreshed at {state['last_refresh']}")


if __name__ == "__main__":
    main()
