# Weekly Audit Checklist

Use this for each Sunday-evening (Pacific) audit cycle.

## Product / experience
- [ ] Any new user feedback in the last 7 days?
- [ ] Any patterns in negative feedback?
- [ ] Any cards/screens consistently failing?
- [ ] Any UX friction worth a quick fix?
- [ ] Did goal-aware Now check-ins help users this week?

## Code health
- [ ] Open PRs older than 7 days?
- [ ] Stale issues over 30 days that should be closed or re-scoped?
- [ ] Any failing CI runs?
- [ ] Any secrets accidentally committed (run `git diff` scanners)?
- [ ] Any TODOs in code that are now done or stale?

## Infra / deploy
- [ ] Backend `/health` returning 200?
- [ ] Recent deploy commits match expected merges?
- [ ] Any error spikes in logs?
- [ ] Any cost spikes (model usage, infra)?

## Doctrine / Stewardship
- [ ] Any external response to outreach (if approved + sent)?
- [ ] Any new public AI policy events worth reflecting in doctrine?
- [ ] Any drift between doctrine and operating practice?

## Agents / intelligence
- [ ] Any agent prompts that produced bad recommendations?
- [ ] Any IOO graph edges with unusual outcomes?
- [ ] Any cohort-learning signals that should boost or demote a path?

## Memory / continuity
- [ ] `MEMORY.md` lean and accurate?
- [ ] Daily memory files written for the last 7 days?
- [ ] Any decisions that should be promoted to long-term memory?

## Costs / sustainability
- [ ] Cost trend over 7d vs 30d?
- [ ] Any model worth swapping out?

## Safety
- [ ] Any near-misses where Nea almost acted without approval?
- [ ] Any new attack surface?
- [ ] Any privacy concern in recent code?
