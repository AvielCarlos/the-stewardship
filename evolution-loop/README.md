# Evolution Loop

A weekly autonomous improvement cycle for Nea — The Steward.

## The cycle

```
audit → propose → categorise → act safely → request approval → record → learn
```

1. **Audit** — pull state from Mission Control, recent feedback, recent merges, recent failures.
2. **Propose** — list candidate improvements (bugs, polish, doctrine refinements, agent prompts, scoring tweaks, infra, tests).
3. **Categorise** — split into:
   - **Safe-to-do** (reversible, internal, no public surface)
   - **Approval-required** (anything affecting prod, money, governance, or external comms)
   - **Defer** (unclear, low-value, or out of scope)
4. **Act safely** — implement Safe-to-do items, open PRs, run tests.
5. **Request approval** — present Approval-required items as briefings to Avi with two recommended options each.
6. **Record** — write `cycles/YYYY-MM-DD.md` capturing what was done, what was deferred, what was learned.
7. **Learn** — feed lessons into doctrine, agent prompts, autonomy queue, and the audit checklist.

## Cadence

- **Weekly**: Sunday evening Pacific.
- **Triggered**: after a major event (incident, big merge, large feedback wave).

## Files

- `cycles/` — one Markdown per cycle.
- `audit-checklist.md` — the rubric used during each audit.
- `proposals-template.md` — the structure for proposing improvements.
- `safety-rules.md` — what is and isn't allowed under autonomous action.

## Hard limits

- No merges to `main` without Avi briefing + approval.
- No external sends (email, social, outreach) without Avi approval.
- No money movement without Avi approval.
- No governance changes without Avi approval.
- No deletion of user data ever.
- Reversibility first. When in doubt, draft a PR and ask.
