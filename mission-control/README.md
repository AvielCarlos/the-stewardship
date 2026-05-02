# Mission Control

A single operating dashboard for Nea — The Steward. The goal: faster, sharper, safer action by giving the agent live visibility into the work.

## v0 — what's in this folder

- `state.json` — current operating state (open PRs, top issues, feedback queue, deploy health, autonomy queue, weekly cycle status). Hand-edited or refreshed by `scripts/refresh-state.py`.
- `scripts/` — small Python scripts that pull from gh, GitHub Actions, Railway, the backend health endpoint, and the feedback DB to rebuild `state.json`.
- `dashboard.md` — human-readable rendering of the current state. Auto-generated from `state.json`.

## What Mission Control tracks

1. **Repos** — health for `connectome-backend`, `connectome-web`, `the-stewardship`.
2. **Pull Requests** — open, awaiting review, awaiting merge, blocked.
3. **Issues** — top 10 by severity / staleness; CP-tagged contributor issues.
4. **Feedback** — most recent user feedback, grouped by area.
5. **Deploys** — Railway health checks; recent deploy commits.
6. **Costs** — model usage costs (Codex, Claude) for the last 7/30 days.
7. **Autonomy queue** — what Nea may safely act on without asking.
8. **Approval queue** — what Nea has prepared and is waiting for Avi to approve.
9. **Weekly cycle** — last audit date, next audit date, top 3 chosen improvements, status.

## Refresh cadence

- On-demand: when Nea is asked "where are we" or "what's open".
- Weekly: pre-audit refresh (Sunday evening Pacific).
- After significant action: PRs merged, deploys, large feedback events.

## Boundaries

- Mission Control is **read-only** for external systems. It does not perform actions.
- The autonomy queue lists *eligible* tasks; it does not execute them.
- Approval-gated tasks remain blocked until Avi approves.
