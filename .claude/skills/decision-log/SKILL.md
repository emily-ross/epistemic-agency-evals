---
name: decision-log
description: Maintain this repo's decision log (DECISIONS.md) and known-limitations log (LIMITATIONS.md). Use proactively during any work in the epistemic-agency-evals repo whenever a decision is made that shapes the eval's scope, design, dataset, rubric, scoring, models, budget, or implementation — especially when a decision carries a tradeoff or limits the eval's scope, efficacy, or generalizability. Trigger at the moment the decision happens (user picks an option, approves a tradeoff, defers or cuts something, or Claude makes a significant unprompted choice); do not wait to be asked to log it.
---

# Decision Log

Maintain two append-only logs at the repo root:

- **DECISIONS.md** — every decision that shapes the eval, with rationale and alternatives (entries `D-001`, `D-002`, …)
- **LIMITATIONS.md** — every known tradeoff/limitation accepted along the way (entries `L-001`, `L-002`, …), cross-linked to the decision that created it

These logs are part of the repo's credibility: the project's honesty guardrails require limitations to be tracked as they arise, not reconstructed at write-up time. LIMITATIONS.md is the source for the README's limitations section.

## What counts as a loggable decision

Log it when any of these happen:

- Scope: what the eval does/doesn't measure; behavior definition; fallback plans invoked or pre-committed
- Design: rubric wording or criteria, scoring scheme, grader model choice, dataset composition, sample size, metadata schema, prompt-selection criteria
- Implementation choices with consequences: pinned versions, model/temperature settings, solver structure, anything affecting comparability of runs
- Anything cut, deferred, simplified, or accepted as "good enough for a pilot"
- Reversals and revisions of prior decisions (see "Interacting with prior decisions")

Do NOT log: trivial mechanical choices (file naming, formatting, refactors with no behavioral effect), or restatements of things already decided.

## Workflow

1. **Recognize the moment.** A decision usually appears as: the user picks between options, approves/rejects a proposal, states a constraint ("keep it under $30", "use Opus as grader"), or Claude makes a significant judgment call without asking.
2. **Log it in the same turn**, without interrupting the task and without asking permission to log. If several decisions happen in one stretch of work, batch them into one edit at a natural pause.
3. **Append** the entry to DECISIONS.md using the next sequential ID. Never renumber or delete existing entries.
4. **If the decision carries a tradeoff or limitation**, also append an entry to LIMITATIONS.md and cross-reference both ways (`Limitations: L-00X` / `From decision: D-00X`). A limitation can also arise without a discrete decision (e.g., discovered mid-implementation) — log it standalone with `From decision: —`.
5. **Mention it briefly** in the response, e.g. "Logged as D-007 (+ L-004)." One line, no more.

## Entry formats

DECISIONS.md entry:

```markdown
## D-00X — <short imperative title>
- **Date:** YYYY-MM-DD
- **Status:** active | amended by D-0YY | superseded by D-0YY
- **Decided by:** Emily | Claude (unreviewed) | Emily + Claude
- **Decision:** What was decided, in one or two sentences.
- **Why:** The actual rationale. Use the user's stated reasoning where given.
- **Alternatives considered:** What else was on the table and why it lost. "None discussed" is a valid entry.
- **Supersedes / amends:** D-0ZZ (only when this decision revises a prior one; omit otherwise)
- **Limitations:** L-00X, L-0YY | none known
```

LIMITATIONS.md entry:

```markdown
## L-00X — <short title of what is limited>
- **Date:** YYYY-MM-DD
- **Status:** active | resolved by D-0YY
- **From decision:** D-00X | —
- **Affects:** scope | efficacy | generalizability | comparability | cost (pick all that apply)
- **Limitation:** What the eval can't claim or do because of this, concretely.
- **Mitigation / revisit if:** What would fix it, or the condition under which to revisit. "None planned (pilot)" is valid.
```

## Interacting with prior decisions

When a new decision touches an earlier one, classify the relationship and record it on both ends. The invariant everywhere: **old entries never lose content — they only gain a status.** The history of being wrong is part of the audit trail, not clutter.

- **Supersede (full walk-back).** Log a new entry with `Supersedes / amends: D-0XX`. Its **Why must explain what changed** — new information, a failed assumption, a cost that materialized — not just restate the new position. Flip the old entry's Status to `superseded by D-0YY`. Touch nothing else in the old entry.
- **Amend (partial revision).** Same mechanics, but the old entry's Status becomes `amended by D-0YY` — it is still mostly in force. Use this when narrowing, extending, or adjusting a decision rather than reversing it.
- **Reconcile limitations.** After superseding or amending, check every limitation linked from the old entry (its `Limitations:` line, and any `From decision:` back-references). For each one that no longer holds, set its Status to `resolved by D-0YY`; leave genuinely persisting ones active. The new decision may also introduce new limitations — log those as usual. An out-of-date LIMITATIONS.md misstates the eval in either direction; both directions are honesty failures.
- **Cascade check — flag, don't auto-edit.** Search DECISIONS.md for other entries that reference or clearly build on the superseded/amended decision. If any look undermined, say so to Emily in one or two sentences and let her decide; whether a downstream decision still stands is itself a new decision, not a mechanical restamp. Never silently change the status of entries the new decision didn't explicitly address.
- **Depends on / builds on.** A new decision that merely relies on an earlier one needs no status change anywhere — just mention the earlier ID in its Decision or Why text so the dependency is findable by the cascade check later.

## Integrity rules

- **Never fabricate rationale.** If the user decided but the "why" wasn't stated and isn't obvious from context, record the decision and either ask one short question to fill in Why, or write `Why: not stated; inferred: <inference>` so the inference is clearly flagged.
- **Record who decided.** Significant choices Claude made without explicit user sign-off stay marked `Claude (unreviewed)` until the user confirms; flip to `Emily + Claude` when confirmed.
- **Append-only.** History stays intact. Corrections and reversals get new entries; a superseded entry only gets its Status line updated.
- **Before any public write-up or README update**, sweep LIMITATIONS.md and make sure every active limitation is reflected in the README's limitations section (per CLAUDE.md's honesty guardrails).
