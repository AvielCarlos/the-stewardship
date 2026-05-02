# Voting Model

Status: v0 design.

## Vote types

1. **Temperature check** — emoji reactions on a proposal. Non-binding. Gives signal in days, not weeks.
2. **Standard vote** — verified-member ballots. One member = one base vote. CP adds a quadratic boost.
3. **Constitutional vote** — for changes to the Steward Constitution, surplus distribution, anti-capture caps, or other "hard rules". Requires 75% supermajority + (first 24 months) Avi sign-off.
4. **Treasury vote** — for any expenditure above a published threshold. Each line-item is voted on independently.
5. **Recall vote** — to remove a steward, freeze a runaway proposal, or revert a recent decision. Lower threshold (simple majority of verified members).

## CP and influence

Voting power = `1 + sqrt(CP / CP_norm)` where:
- `CP_norm` is calibrated quarterly so the median active member has a multiplier of `~1.5–2.0`.
- Hard cap: no individual's voting power exceeds 5% of total active voting power.
- Hard cap: no aggregated "delegation cluster" exceeds 10% of total voting power.

This protects against:
- whale capture (sqrt scaling),
- collusion (delegation cluster cap),
- founder capture (Ascension Technologies and Avi count as one delegation cluster, capped at 10%).

## Quorum

- Standard vote: 10% of verified active members participating.
- Constitutional vote: 25% of verified active members participating + 75% of those voting in favour.
- Treasury vote: scales with size (small = 5% quorum / simple majority; large = 25% quorum / 60% in favour).
- Recall: 15% quorum / simple majority.

## Voting windows

- Standard: 7 days.
- Constitutional: 21 days (with two formal review periods).
- Treasury: 5–14 days depending on amount.
- Recall: 72 hours for time-sensitive items.

## Tooling

- Phase 1: emoji reactions on GitHub issues (signal only).
- Phase 2: Snapshot or a custom signed-message voter using GitHub or a verified-membership token.
- Phase 3: on-chain or semi-on-chain treasury executor wired to the vote outcome.

We will **not** use closed Discord polls, opaque off-chain tallies, or any system that hides individual vote weights.
