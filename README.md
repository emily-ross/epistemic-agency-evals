# Epistemic Agency Evals

A pilot eval, built on [Inspect](https://inspect.aisi.org.uk), that aims to measure one dimension of model alignment with individual, longterm epistemic goods, as described in Marchal et al. 2026, *Architecting Trust in Artificial Epistemic Agents* ([arXiv:2603.02960](https://arxiv.org/abs/2603.02960), §4.2): whether frontier language models **scaffold** a user's reasoning or **substitute** for it, in situations where neither is explicitly requested. This behavior was selected because if exhibited frequently enough in certain types of situations, it could lead to cognitive deskilling. Unlike existing tutoring benchmarks, which test whether a model *can* scaffold when told to act as a tutor, this eval measures whether it *does* scaffold by default — in ordinary assistant mode, when the user only signals an intent to learn.

> ⚠️ **Status: work in progress.** This is a small, self-directed study project — **not a benchmark**, and **not affiliated with or endorsed by** UK AISI, the Inspect maintainers, or the paper's authors. It builds on their public work. Dataset, results across models, and a full write-up (with limitations foregrounded) will land here as the pilot progresses.

## Plan

A versioned dataset of 26 situations — one per domain, each carrying an explicit or implicit learning signal, plus a matched product-request control (N≈52) — run identically across 2–4 frontier models, scored by an independent grader model making a single binary substitution judgment against a per-item criterion, with browsable transcript logs published via GitHub Pages.

The full eval spec — threat model, definitions, grading protocol, and dataset design — is in [SPEC.md](SPEC.md). The reasoning behind every design decision is logged in [DECISIONS.md](DECISIONS.md), with accepted tradeoffs in [LIMITATIONS.md](LIMITATIONS.md).

## Limitations

This is a pilot, and its limits are part of the artifact (full list in [LIMITATIONS.md](LIMITATIONS.md)):
- **A single-turn proxy for a slow harm** — it measures a model behavior claimed to sit upstream of cognitive deskilling, not deskilling itself, which unfolds over months or years.
- **A soft, model-graded construct** — "substitution vs. scaffolding" is judged by a model; measured human-grader agreement will be reported, with a pre-committed fallback to a near-objectively-scored behavior if agreement is poor.
- **One behavior, one path** — the demand-side (atrophy) path only, in model-knowledge-sufficient task domains; personal/creative domains and supply-side epistemic harms are out of scope.
- **One clean contrast** — only the product-request control is matched within a situation; other axes (how the learning signal is carried, how much task detail is given) are held roughly constant or varied loosely across situations and reported descriptively, not as clean effects.
- **A constructed prompt set** — hand-built and reviewed, not sampled from real usage.

## Development

See [CLAUDE.md](CLAUDE.md) for the full setup, the Inspect mental model, and project conventions.

```bash
python3.13 -m venv inspect-env && source inspect-env/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your ANTHROPIC_API_KEY to .env
```

## License

MIT — see [LICENSE](LICENSE).
