# Governance — Open Stewardship

Created: 2026-05-02
Owner: Nea / The Steward
Status: v0 design. Implementation phased, none of it deployed yet.

This folder defines how The Stewardship governs itself: how proposals are made, how laws (rules, doctrine changes, governance changes) are amended, how expenditures are decided, and how the community votes.

It is **not** a system for governing nations. It is the internal governance of The Stewardship community itself, designed so that:

- **anyone can propose a change to any rule** at any time
- **expenditures from the Stewardship treasury** are voted on collectively, line-by-line, in the open
- **every vote is auditable**, **every decision is reversible**, and **no single steward can override the membership**

The goal: governance that is more legitimate, more transparent, and more participatory than any closed organisation — and never coercive of those outside The Stewardship.

---

## Design principles

1. **Open proposals** — any member can propose a change to any rule, doctrine clause, expenditure, or governance parameter.
2. **Quadratic voting where possible** — voting power grows with the square root of CP, not linearly, to prevent CP-whale capture.
3. **Membership baseline** — every verified human member gets a base vote; CP scales influence, but does not eliminate the base vote.
4. **Subsidiarity** — local stewardship circles vote on local matters; global stewardship votes only on global matters.
5. **Reversibility** — any decision can be re-opened by a counter-proposal.
6. **Quorum + supermajority for sensitive items** — doctrine changes, hard-rule changes, large expenditures require higher thresholds.
7. **Transparency by default** — every proposal, vote, and expenditure is public and auditable.
8. **Anti-capture** — no entity (including Ascension Technologies) may control more than a published cap of voting power.
9. **Sybil resistance** — verified human membership is the cornerstone; we do not rely on wallet count alone.
10. **Quiet exit** — any member may leave at any time, taking nothing they didn't earn, harming nothing they didn't damage.

---

## Phases

### Phase 0 — design (now)
- This document, voting taxonomy (`voting.md`), proposal lifecycle (`proposals.md`), expenditure model (`treasury.md`).
- Governance issue templates on GitHub for proposals and amendments (lightweight, cost-zero, public).
- A simple sign-up page on the site that collects expressions of interest (no PII beyond email + handle).

### Phase 1 — minimum viable signal
- GitHub-issue-based proposals: anyone can open a proposal in this repo using a template.
- Emoji-reaction voting (👍/👎/❤️/🙏/🚫) gives a temperature check.
- Stewards review weekly, summarise outcomes in the public log.
- No money moves through this phase; surplus tracking is preview-only.

### Phase 2 — verified-member voting
- Sign-up flow → verified human membership (no biometrics; reasonable identity proof + community vouch).
- Member rolls published with consent (handle only; PII never exposed).
- One-member-one-base-vote; CP layered on top via quadratic boost.
- Voting via signed messages or a small custom voting app; results posted to the log.

### Phase 3 — treasury & expenditure
- A small Stewardship treasury (DAO-held), seeded transparently.
- Every line-item expenditure proposed publicly; voted by members; executed only on approval.
- Standing categories: doctrine work, infrastructure, dividends, audits, partnerships, dignity grants.
- Quarterly public ledger.

### Phase 4 — federated stewardship circles
- Local circles (community / cohort / region) inherit the constitution, set their own local rules.
- Global votes only on global matters; subsidiarity preserved.

### Phase 5 — open ratification
- Members may ratify The Stewardship Pact, individually or organisationally.
- Adoption is voluntary, public, and revocable.

---

## Hard rules (constitutional layer)

These rules require **75% supermajority of verified members + Avi explicit sign-off for the first 24 months** to change:

- Surplus distribution (50% universal / 50% CP / 0% capture).
- Steward Constitution principles 1–10.
- Anti-capture caps.
- Reversibility of decisions.
- Member exit rights.

This protects the doctrine from runaway capture during the bootstrap phase. After 24 months the Avi-signoff requirement automatically sunsets to a 75% supermajority alone.

---

## Anti-patterns we explicitly reject

- Plutocracy (1 token = 1 vote).
- Closed-door governance.
- Steward elections without recall mechanism.
- Treasury opaqueness.
- Vote-buying or delegation cartels.
- Coercive participation requirements.
- Surveillance of voters.
