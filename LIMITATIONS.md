# Known Limitations

A running, append-only log of known tradeoffs and limitations of this eval, recorded as they arise during development (not reconstructed afterwards). Each entry links back to the decision in [DECISIONS.md](DECISIONS.md) that created it, where one exists. Before any public write-up, every active entry here must be reflected in the README's limitations section.

Maintained via the repo's `decision-log` skill (see `.claude/skills/decision-log/`).

---

## L-001 — Threat model covers only the demand-side path to collective harm
- **Date:** 2026-07-20
- **Status:** active
- **From decision:** D-003
- **Affects:** scope
- **Limitation:** The threat model traces collective harm only through aggregation of individual atrophy (demand-side vulnerability). The paper's supply-side pathways to societal epistemic harm — recursive AI-content contamination of the commons, adversarial injection, epistemic homogenization as a system property — are acknowledged but not modeled, and the eval built from this threat model will say nothing about them.
- **Mitigation / revisit if:** None planned (pilot). Revisit if the eval is ever extended toward multi-agent or ecosystem-level measurement.

## L-002 — Single-turn behavioral proxy for a longitudinal harm
- **Date:** 2026-07-20
- **Status:** active
- **From decision:** D-007
- **Affects:** efficacy, generalizability
- **Limitation:** The harm pathway (cognitive atrophy) unfolds over months-to-years of repeated interaction; the paper itself notes deskilling effects "may take years to manifest." This eval measures a single-response behavioral propensity claimed to sit causally upstream. A model's substitution rate here is evidence about the model's behavior, not a measurement of user deskilling — the eval cannot confirm the downstream harm occurs.
- **Mitigation / revisit if:** State the proxy relationship explicitly in every write-up. The behavior→harm edges and their evidence strength are documented in SPEC.md's threat model.

## L-003 — Per-item grader criteria add reviewer burden and grader degrees of freedom
- **Date:** 2026-07-20
- **Status:** active
- **From decision:** D-011
- **Affects:** efficacy, comparability, cost
- **Limitation:** Because "core reasoning steps" vary by task, each item carries its own generated-then-reviewed grading criterion. Poorly written criteria can smuggle judgment calls back into grading, and criterion quality varies with the reviewer's attention; cross-item comparability depends on the criterion-writing protocol being applied consistently.
- **Mitigation / revisit if:** All criteria generated from the single fixed protocol in SPEC.md §4 and manually reviewed alongside prompts (per CLAUDE.md's review mandate); grader-vs-human agreement check (~20 transcripts) will surface criterion failures. Revisit protocol if agreement is poor on specific item types.

## L-004 — Personal (ownership-heavy) domains are out of scope
- **Date:** 2026-07-20
- **Status:** active
- **From decision:** D-013
- **Affects:** scope, generalizability
- **Limitation:** The eval only covers domains where the model could plausibly produce a good finished product from its weights alone. It says nothing about substitution behavior in personal domains (toasts, sermons, poems, personal creative work) — contexts where AI displacement of self-expression is itself a live concern. Findings generalize only to knowledge-sufficient task domains.
- **Mitigation / revisit if:** Revisit if a future version can supply enough personal context in-prompt to make substitution genuinely feasible there (removing the ambiguity that motivated the scope-out).

## L-005 — Signal-strength and attempt-presence effects are confounded with situation
- **Date:** 2026-07-20
- **Status:** active
- **From decision:** D-017
- **Affects:** efficacy, generalizability
- **Limitation:** `signal_strength` and `attempt_presented` are varied between situations, not as matched within-situation pairs. Any difference in substitution rate across these axes is confounded with the situations that happen to carry each value (domain, difficulty, phrasing), so their reported effects are descriptive and directional, not clean causal contrasts. Only the `condition` contrast (the completion gap) is matched and confound-controlled.
- **Mitigation / revisit if:** Balance the axes across the domain set so marginal cells are comparable, and report these slices as descriptive. Revisit by promoting an axis to a matched pair if a specific effect (e.g. explicit vs. implicit signal) becomes the question of interest.

## L-006 — Task specification is held roughly constant, not measured, and only coarsely controlled
- **Date:** 2026-07-20
- **Status:** active
- **From decision:** D-017
- **Affects:** scope, efficacy
- **Limitation:** `task_specification` was dropped as an axis, so the eval says nothing about how the amount of task detail a user provides affects substitution — even though design-time probing suggested this effect is large. Separately, "substitution-capable" is a floor, not a fixed level: items can still vary in specificity above that floor, and that residual, uncontrolled variation could influence substitution rates and add noise to cross-item and cross-slice comparisons.
- **Mitigation / revisit if:** Keep specificity as uniform as practical across items during construction and review; a future version could reintroduce task_specification as a matched axis to measure the effect directly rather than hold it out.
