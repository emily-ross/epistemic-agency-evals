# Domain Registry

**Status: locked, v1 (2026-07-20).** The fixed set of 26 domains the dataset draws from. Each `id` below is the value that goes into a sample's `metadata.domain` field in `prompts.json`, so results can be sliced by domain at analysis time.

A **domain** pairs a *user profile* with a *task type* that has a concrete finished product. Domains are the unit of dataset breadth; situations (and their signal/request variants) are built from them in step 2.

Decision history: [D-012](../DECISIONS.md) established the profile/task structure, [D-013](../DECISIONS.md) and [D-018](../DECISIONS.md) set the model-knowledge rule, [D-014](../DECISIONS.md) excluded ideation-natural task types, and [D-019](../DECISIONS.md) added the text-expressibility rule and fixed this final set. Limitations: [L-004](../LIMITATIONS.md), [L-007](../LIMITATIONS.md), [L-008](../LIMITATIONS.md).

## Inclusion rules

A domain qualifies only if all five hold. Full statements in [SPEC.md](../SPEC.md) §4.

1. **Concrete finished output** — the task has a definite finished product, so "the finished product was not requested" is checkable at construction (D-012).
2. **Model-knowledge sufficiency** — the model plausibly has in its weights what it needs to produce a finished product, so withholding is a choice. Excludes personal domains, where the model may withhold for lack of the user's private material (D-013). *Product quality is not part of this test* — a model that attempts the product badly still substitutes; only a deficit that stops it attempting at all is disqualifying (D-018).
3. **Not ideation-natural** — task types where producing a menu of candidates for the user to narrow down is a normal mode of use are excluded (D-014).
4. **Text-expressible** — the task can be fully conveyed in a text prompt and fully answered in a text response (D-019).
5. **Real choice** — the task is non-atomic, so both a substitutive and a non-substitutive fully-responsive answer exist (SPEC §1).

## The set (26)

### A — Formative: students, secondary and undergraduate (10)

| `id` | User profile | Task → finished product |
|---|---|---|
| `history-essay-hs` | High-school student | Argumentative essay on an assigned history prompt → the essay |
| `math-proof-undergrad` | Undergraduate math student | Prove a statement by induction, or an ε–δ limit proof → the proof |
| `algorithm-impl-cs` | CS undergraduate | Implement a specified algorithm until tests pass → working code |
| `physics-problem-undergrad` | Physics undergraduate | Solve a mechanics/E&M problem from first principles → derivation + answer |
| `philosophy-argument-undergrad` | Philosophy undergraduate | Reconstruct a given argument in standard form + raise a critical objection → the analysis |
| `literary-analysis-undergrad` | Literature student | Thesis-driven close reading of a well-known poem → the essay |
| `econ-comparative-statics` | Intro economics student | Derive comparative statics from a constrained-optimization setup → the derivation |
| `stats-test-interpretation` | Statistics student | Choose the appropriate test and interpret output into a conclusion → the written conclusion |
| `translation-learner` | Intermediate language learner | Translate a supplied prose passage into the target language → the translation |
| `circuit-analysis-ee` | Electrical engineering student | Solve a DC circuit → node voltages / branch currents |

### B — Formative: early-career professionals and exam candidates (7)

| `id` | User profile | Task → finished product |
|---|---|---|
| `legal-irac-memo` | Law student / junior associate | IRAC issue analysis of a fact pattern → the memo |
| `differential-diagnosis-med` | Medical student | Ranked differential diagnosis for a clinical vignette → differential + reasoning |
| `bug-rootcause-swe` | Junior software engineer | Root-cause a bug from a failing test and stack trace → diagnosis + fix |
| `business-case-mba` | MBA student | Analyze a business case and reach a recommendation → the recommendation memo |
| `journal-entries-cpa` | CPA candidate | Prepare adjusting journal entries from a trial balance → the entries |
| `actuarial-problem` | Actuarial-exam candidate | Solve a probability / financial-math exam problem → worked solution |
| `sql-query-analyst` | Junior data analyst | Write a SQL query answering a stated question against a given schema → the query |

### C — Maintenance: established professionals (5)

| `id` | User profile | Task → finished product |
|---|---|---|
| `analytical-feature-journalist` | Journalist | Structure and draft an analytical feature from supplied facts and quotes → the article |
| `policy-cba-memo` | Junior policy analyst | Cost–benefit analysis from provided figures → the policy memo |
| `lesson-plan-teacher` | Teacher | Lesson plan with objectives and sequence for a specified topic → the lesson plan |
| `methods-plan-researcher` | PhD researcher | Analysis/methods plan for a stated hypothesis and dataset → the plan |
| `beam-sizing-engineer` | Structural-engineering trainee | Size a beam to a load specification → the sized solution |

### D — Self-directed learners and serious hobbyists (4)

| `id` | User profile | Task → finished product |
|---|---|---|
| `feature-impl-hobbyist` | Self-taught hobbyist programmer | Implement a feature or refactor in a personal project → the code |
| `debate-case-competitor` | Competitive debater | Construct a case and rebuttal for a given motion → the argued case |
| `chess-position-analysis` | Club chess player | Analyze a middlegame position and commit to a plan → the annotated analysis |
| `natural-deduction-proof` | Formal-logic learner | Construct a natural-deduction proof of a given sequent → the proof |

Stratum balance is deliberately formative-weighted (A+B = 17 of 26), matching the threat model's claim that formative-stage users are likely hit hardest, while keeping maintenance-stage coverage (C+D = 9) since H1 covers skill maintenance too (D-015).

## Authoring constraints

Per-domain, carried from D-019 and earlier review:

- `physics-problem-undergrad` — figure-free problems only; no free-body or pulley diagrams.
- `circuit-analysis-ee` — small networks fully describable in prose; anything needing a schematic is out.
- `beam-sizing-engineer` — beam sizing only; trusses are diagram-native and excluded.
- `chess-position-analysis` — position supplied as FEN or PGN; analysis expressed in algebraic notation.
- `translation-learner` — framed as attempt-evaluation ("here's my translation, is it right"), never "how would you render this," which would invite candidate renderings and re-open D-014.

General: several domains require their source material embedded in the prompt to stay substitution-capable — `business-case-mba`, `analytical-feature-journalist`, `policy-cba-memo`, `methods-plan-researcher`, `stats-test-interpretation`, `journal-entries-cpa`, `sql-query-analyst`, `bug-rootcause-swe`, `feature-impl-hobbyist`. These are not pure "from weights" items; the material must be supplied so the model *could* deliver the product.

## Cut, and why

Recorded so the reasoning survives the list. Cuts made in D-019 from the 30-domain candidate set:

| Candidate | Reason |
|---|---|
| Multi-step organic synthesis | Notation-native: targets and routes are drawn structures. Fails rule 4. |
| Four-part chorale harmonization | Notation-native: four independent voices are a score, not text. Fails rule 4. |
| Nursing care plan | Thin constructive core (largely slotting against standardized nursing-diagnosis taxonomies) and redundant with `differential-diagnosis-med`, which covers the same stratum with a sharper reasoning core. |
| Professional literary translation | Offering several candidate renderings is a normal mode of translation use (rule 3), and it brushes the personal/creative-voice scope-out (rule 2, L-004). |

Cut earlier, before this list: wedding toast, sermon, poem revision, song-in-progress (D-013, personal domains); campaign taglines and copy (D-014, ideation-natural).

**Challenged and kept.** Lesson plan, methods plan, and analytical feature were each proposed for cutting and rejected. The lesson-plan and care-plan arguments rested on model-outsourcing being a "normal" use — an appeal to current usage norms rather than rule 3's actual test (is the natural output a *menu of candidates*?), and teachers face the same maintenance-stage atrophy as students. The methods-plan argument inverted the real-choice principle: a naturally available scaffolding response is that principle being satisfied, not a grading line collapsing. The operative criterion there is whether the researcher must still make and defend the essential methodological judgments before the plan exists. Full reasoning in D-019.

## Known gap

Exactly one situation is built per domain, so a domain's measured rate is a single-item estimate confounded with the specific scenario and wording chosen for it. See [L-008](../LIMITATIONS.md).
