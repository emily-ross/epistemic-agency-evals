# Dataset

## ⚠️ Status: prompts reviewed; grading criteria model-reviewed, not hand-verified

**The 52 prompts have been read end-to-end and approved by the repo owner**, with no changes requested (D-031).

**The 52 grading criteria in the `target` field are model-authored and have been model-reviewed.** They were generated one item per subagent (D-029), then put through an independent adversarial review against the actual grader template and instructions; all 17 findings were applied, and a second sweep resolved for every numbered step in every item whether delivering that step alone counts (D-034, D-035). The owner has skimmed them alongside the prompts. What has *not* happened is the check SPEC §4 specifies — a human reading each criterion beside its prompt and signing off on where the substitution line falls. **Do not describe the criteria as hand-reviewed**; see [L-016](../LIMITATIONS.md) for what that leaves open.

## What is in it

`prompts.json` — a JSON array of 52 [Inspect](https://inspect.aisi.org.uk) samples: **26 situations × 2 conditions**, one situation per domain in [domains.md](domains.md). Read with `json_dataset("data/prompts.json")`.

Each record:

```json
{
  "id": "<domain>__<condition>",
  "input": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}],
  "target": "<the item's grading criterion>",
  "metadata": { "domain": "...", "stratum": "A|B|C|D", "situation": "...",
                "pair_id": "<domain>", "condition": "signal|request",
                "signal_strength": "explicit|implicit", "attempt_presented": "yes|no" }
}
```

`target` holds the item's per-item grading criterion (D-029): the task's core reasoning steps, what counts as delivering them in usable form (substitution) versus informing or verifying the user's own performance of them, and the transcription test applied to that item. `stratum` records which threat-model population the domain's user belongs to — A/B formative, C/D maintenance; the four are defined in [domains.md](domains.md) and in SPEC §4's axis table.

### Reading the metadata

`signal_strength` and `attempt_presented` describe the **situation**, not the individual sample (D-027). Both variants of a pair carry the situation's values and differ only in `condition`. So a `request` record can read `attempt_presented: "yes"` while presenting no attempt — read it as "the control for a situation whose signal item presented an attempt." Slice the 26 `signal` records by axis; join their controls via `pair_id`.

Balance across the 26 situations: 13 explicit / 13 implicit, 13 attempt / 13 no-attempt, spread across all four strata.

## How it was built, and what has been checked

Authored per the construction rules in [SPEC.md](../SPEC.md) §4, then put through a domain-expert verification pass covering all 26 situations (D-023, D-026) — one reviewer per discipline, checking planted errors, task-material accuracy, ambiguity, false premises and pair symmetry. 81 corrections were applied. Four items were invalid as written and were repaired: `sql-query-analyst`, `feature-impl-hobbyist`, `debate-case-competitor`, `lesson-plan-teacher`.

**What that pass did not substitute for:** a human reading the prompts for tone, realism, and whether each one actually reads like something a person would send. That check has since been done and the prompts approved as they stand (D-031). The equivalent check on the grading criteria has not.

## Contains deliberately incorrect content

Every item with `attempt_presented: "yes"` embeds a **planted conceptual error** in the user's work — a wrong differential diagnosis, an invalid proof step, a miscalculated beam moment. This is by design; the eval measures whether the model repairs the error for the user or coaches them to find it.

All people, institutions, cities, cases, companies and figures in the prompts are fictional. Model responses to these items will elaborate on incorrect reasoning. **Before any transcript is published, the log site needs a banner saying so** — see the open publication-safety item in the session notes.

## Decision history

Dataset construction: D-021 through D-028 in [DECISIONS.md](../DECISIONS.md). Active limitations bearing on this dataset: L-005 (axis effects confounded with situation), L-006 (task specification only coarsely controlled), L-008 (one situation per domain), L-010 (explicit withholding instructions out of scope).
