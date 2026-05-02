#!/usr/bin/env python3
"""Render Mission Control state.json into a human-readable dashboard.md."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "state.json"
DASH_PATH = ROOT / "dashboard.md"


def main() -> None:
    state = json.loads(STATE_PATH.read_text())
    lines: list[str] = []
    lines.append("# Mission Control — Live Dashboard")
    lines.append("")
    lines.append(f"_Last refresh: {state.get('last_refresh') or 'never'}_")
    lines.append("")

    lines.append("## Repos")
    for name, info in state.get("repos", {}).items():
        lines.append(f"### {name}")
        lines.append(f"- branch: `{info.get('default_branch')}`")
        lines.append(f"- health: {info.get('health')}")
        prs = info.get("open_prs") or []
        if prs:
            lines.append(f"- open PRs ({len(prs)}):")
            for pr in prs[:10]:
                lines.append(f"  - #{pr.get('number')} {pr.get('title')} (by {pr.get('author', {}).get('login') if isinstance(pr.get('author'), dict) else pr.get('author')})")
        else:
            lines.append("- open PRs: none")
        issues = info.get("top_issues") or []
        if issues:
            lines.append(f"- open issues ({len(issues)}):")
            for iss in issues[:10]:
                lines.append(f"  - #{iss.get('number')} {iss.get('title')}")
        lines.append("")

    deploys = state.get("deploys", {})
    lines.append("## Deploys")
    lines.append(f"- connectome-api health: {deploys.get('connectome-api_health')}")
    lines.append(f"- last check: {deploys.get('last_check')}")
    lines.append("")

    lines.append("## Autonomy Queue")
    for item in state.get("autonomy_queue", []):
        lines.append(f"- {item}")
    lines.append("")

    lines.append("## Approval Queue")
    for item in state.get("approval_queue", []):
        lines.append(f"- {item}")
    lines.append("")

    weekly = state.get("weekly_cycle", {})
    lines.append("## Weekly Cycle")
    lines.append(f"- last audit: {weekly.get('last_audit')}")
    lines.append(f"- next audit: {weekly.get('next_audit')}")
    lines.append(f"- status: {weekly.get('status')}")
    if weekly.get("top3_improvements"):
        lines.append("- top 3:")
        for it in weekly["top3_improvements"]:
            lines.append(f"  - {it}")
    lines.append("")

    DASH_PATH.write_text("\n".join(lines))
    print(f"Wrote {DASH_PATH}")


if __name__ == "__main__":
    main()
