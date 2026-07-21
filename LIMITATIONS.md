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

## L-007 — Notation-native task domains are out of scope
- **Date:** 2026-07-20
- **Status:** active
- **From decision:** D-019
- **Affects:** scope, generalizability
- **Limitation:** The eval covers only tasks that can be fully posed and fully answered in text. Domains whose finished product is structural or notational — chemical synthesis routes, musical scores, circuit schematics, engineering and free-body diagrams, geometric figures — are either excluded outright or admitted only through their text-describable subset (small circuits, beam-sizing rather than trusses, figure-free physics). Substitution behavior in diagram- and notation-native work is therefore unmeasured, and the STEM domains that remain are drawn from the easier, text-friendly end of their fields.
- **Mitigation / revisit if:** Revisit if the eval moves to multimodal prompts and responses, which would both open the excluded domains and lift the text-describability ceiling on the retained ones.

## L-008 — One situation per domain; prompt sensitivity is uncontrolled
- **Date:** 2026-07-20
- **Status:** active
- **From decision:** D-017, D-020
- **Affects:** efficacy, generalizability
- **Limitation:** Each of the 26 domains contributes exactly one situation (with its signal and request variants), so there is no within-domain replication. Any per-domain substitution rate is a single-item estimate in which the domain is fully confounded with the particular scenario, phrasing, and difficulty chosen to represent it — and LLM behavior is known to be sensitive to prompt wording. Domain-level differences therefore cannot be attributed to the domain rather than to its one instantiation, and the headline rate rests on 26 unreplicated items, so its confidence interval is wider than the item count alone suggests.
- **Mitigation / revisit if:** Report per-domain results as descriptive only, never as domain effects, and avoid ranking domains against each other. Revisit by authoring 2–3 differently-worded situations per domain — the cleanest single upgrade to the design if the item budget grows beyond pilot scale.

## L-009 — The product-wanted baseline is matched on task material, not on user profile
- **Date:** 2026-07-20
- **Status:** resolved by D-025
- **From decision:** D-021
- **Affects:** efficacy, comparability
- **Limitation:** Each situation's request variant differs from its signal variant in two ways at once: the user message becomes a direct product request, and the system prompt is reduced to a neutral personalization line. The pair is matched on the task, its supplied material, and the finished product, but not on who the user is. So the completion gap is not a clean single-factor contrast — a model that completes the request-variant task might in principle have declined the same request from the fully described student, and the design cannot separate that from the signal itself. The gap remains valid for the narrow job SPEC assigns it (establishing that the model will produce this product for this task at all), but it should not be read as an estimate of the causal effect of the learning signal alone.
- **Mitigation / revisit if:** Report the completion gap only as the capability/willingness floor it is meant to be, never as a signal effect size. Revisit if the item budget allows a third variant (full profile + explicit product request) to decompose the two differences — noting SPEC's warning that such a variant is internally conflicting and may collapse.

## L-010 — Explicit withholding instructions are out of scope
- **Date:** 2026-07-20
- **Status:** active
- **From decision:** D-021
- **Affects:** scope, generalizability
- **Limitation:** Explicit learning signals in the dataset are statements of intent ("I'm writing this myself this weekend"), never instructions to withhold ("don't give me the answer"). The eval therefore says nothing about whether a model honours a direct request not to be handed the product — a related behavior that users actually perform, and one where failure is arguably worse than default substitution. The measured `signal_strength: explicit` cell covers only the intent-statement form.
- **Mitigation / revisit if:** Keep the distinction visible in write-ups so the explicit cell is not read as covering withholding instructions. Revisit by adding an instruction-following variant as a separate axis value if the eval grows beyond pilot scale; that is an instruction-following construct and would want its own framing rather than being folded into the substitution rate.

## L-011 — Only the 13 attempt-presented items have been expert-verified
- **Date:** 2026-07-20
- **Status:** resolved by D-026
- **From decision:** D-023
- **Affects:** efficacy, comparability
- **Limitation:** The D-023 verification pass covered only items that present a user attempt, because those carry a planted error whose correctness is load-bearing. The 13 items without an attempt (`physics-problem-undergrad`, `circuit-analysis-ee`, `actuarial-problem`, `history-essay-hs`, `philosophy-argument-undergrad`, `econ-comparative-statics`, `legal-irac-memo`, `business-case-mba`, `analytical-feature-journalist`, `debate-case-competitor`, `lesson-plan-teacher`, `methods-plan-researcher`, `chess-position-analysis`) had their task material checked only by the author. Errors or ambiguities in those items would not invalidate a planted error, but they could make a task unsolvable, admit multiple defensible answers, or let a model spend its response correcting the prompt instead of responding to it — which contaminates the substitution judgment the same way. Given that the verified half returned defects in 2 of 13 items severe enough to invalidate them, a comparable rate in the unverified half should be assumed rather than ruled out.
- **Mitigation / revisit if:** Run the same expert pass over the 13 non-attempt items before any published run. Until then, do not describe the dataset as expert-reviewed without qualifying which half.

## L-012 — Request-variant metadata no longer describes the prompt it is attached to
- **Date:** 2026-07-20
- **Status:** resolved by D-027
- **From decision:** D-025
- **Affects:** comparability, efficacy
- **Limitation:** D-022 set the rule that axis metadata records what is realized *in that sample*, and on that basis every request variant carries `signal_strength: "none"`. D-025 then made the request variant share its signal twin's system prompt. Because that system prompt is where implicit signals live — and because even the explicit-signal situations describe their user as a student, trainee or candidate — the profile in a request variant is itself a learning signal. So `signal_strength: "none"` is now false of the prompt it labels, on all 26 controls. Separately, SPEC §4's text ("the control drops the learning signal rather than adding a request on top of it") no longer describes what the dataset does: the control now drops the signal from the user message only.
- **Mitigation / revisit if:** Requires a ruling, not a patch. Either (a) record `signal_strength` and `attempt_presented` as situation-level attributes carried identically on both variants, with `condition` as the sole within-situation axis, and amend SPEC §4 to say the control drops the user-message signal only; or (b) revert D-025, restoring de-signaled control profiles and reinstating L-009. The metadata has deliberately been left untouched so the discrepancy stays visible rather than being quietly relabelled.

## L-013 — The 52 grading criteria are model-generated and not yet hand-reviewed
- **Date:** 2026-07-20
- **Status:** resolved by D-034 (residual restated as L-016)
- **From decision:** D-029
- **Affects:** efficacy, comparability
- **Limitation:** SPEC §4 requires each criterion to be "written at construction time and reviewed together with the prompt". Generation is done; the review is not. Until it happens, the rubric the grader applies is model-authored throughout, and three specific defects are unchecked: a criterion may misidentify the core reasoning steps for its task (making the grader measure the wrong thing on that item), may draw the substitution line where a domain expert would not (e.g. the `translation-learner` criterion counts naming the required tense for a clause as substitution — defensible, but a judgment call that changes that item's rate), or may state a partial-delivery rule strict or lax enough to make its item an outlier. Because each criterion was written independently, such defects are uncorrelated across items and will not show up as an obvious pattern — they surface as unexplained per-item variance, which L-008's single-item-per-domain design already cannot separate from scenario effects.
- **Mitigation / revisit if:** Hand-review all 52 against their prompts before any published run, as SPEC §4 requires; the blind human-grading validation (SPEC §5) is a check on grader–criterion agreement, not on whether the criterion is right, so it does not substitute. Until the review is done, do not describe the criteria as reviewed.

## L-014 — The pilot grader is a mini-tier model on a soft, nuanced rubric
- **Date:** 2026-07-21
- **Status:** active
- **From decision:** D-030
- **Affects:** efficacy, comparability
- **Limitation:** Substitution is a soft construct graded through a ~2–3k-token per-item criterion that requires distinguishing content that informs the user's reasoning from content that performs it, and holding that line through near-miss framings ("just an example", a critique that hands back the repaired version). A mini-tier grader may apply that distinction less reliably than a frontier grader, and any degradation lands directly on the headline undue-substitution rate. Grader reliability is the pilot's stated make-or-break.
- **Mitigation / revisit if:** The blind human-grading check (SPEC §5, ~20 transcripts) measures this directly and its agreement rate is reported in the README. If agreement is poor, re-grade the same transcripts with a full-size grader before invoking the pre-committed false-premise-challenge fallback — a weak grader and a weak construct are different failures and should not be confused.

## L-015 — Three signal-item criteria state no partial-delivery threshold
- **Date:** 2026-07-21
- **Status:** resolved by D-035
- **From decision:** D-032
- **Affects:** efficacy, comparability
- **Limitation:** D-032 removes the grader's global partial-delivery default in favour of "follow the threshold the criterion states." 44 of the 52 criteria state one; 8 do not, and three of those are signal items — `stats-test-interpretation`, `circuit-analysis-ee`, `sql-query-analyst`. On those three the grader has no stated rule for a response that delivers some but not all core steps, so the judgment is improvised per transcript and is less reproducible than on the other 23 signal items. These items feed the headline undue-substitution rate.
- **Mitigation / revisit if:** Closable during the outstanding manual dataset review (see `data/README.md`) by adding a threshold sentence to those three criteria, which would make the instruction complete rather than usually-complete. Until then, treat per-item results for those three as lower-confidence, and check them first if grader–human agreement (SPEC §5) comes back poor.

## L-016 — The criteria have been model-reviewed and owner-skimmed, not hand-verified item by item
- **Date:** 2026-07-21
- **Status:** active
- **From decision:** D-034
- **Affects:** efficacy, comparability
- **Limitation:** L-013's blanket "unreviewed" no longer holds — the criteria have had an independent adversarial review against the actual grader template and instructions, all 17 findings were applied, and every item now states its own sufficiency threshold. What has *not* happened is the check SPEC §4 specifies: a human reading each criterion alongside its prompt and signing off on where the line falls. The owner has read all 52 prompts in full and skimmed the criteria beside them, which is weaker than that. Two residues follow. First, the reviewer was a model, so a defect it shares with the criteria's authors — a plausible-but-wrong reading of where the substitution line belongs in an unfamiliar domain — survives both passes undetected; its own judgment calls (keeping `translation-learner`'s strictness, keeping the `math-proof` twin asymmetry, leaving `legal-irac-memo__request` step 2 unhardened) are recorded but unratified. Second, the fixes themselves are model-authored text now embedded in the rubric. L-003's point stands unchanged underneath: per-item criteria are grader degrees of freedom whichever way they were produced.
- **Mitigation / revisit if:** The blind human-grading check (SPEC §5) is the nearest thing to a test — disagreements there are the cheapest route to a mis-drawn line, so read them as criterion evidence and not only as grader-reliability evidence. Do not describe the criteria as hand-reviewed. Revisit if a run produces a per-item rate that looks anomalous for its domain, which is the signature this predicts.
