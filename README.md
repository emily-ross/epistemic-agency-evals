# Epistemic Agency Evals

A **pilot** evaluation, built on [Inspect](https://inspect.aisi.org.uk) (UK AISI's open-source eval framework), measuring whether frontier language models **scaffold** a user's reasoning or **substitute** for it — when someone is trying to learn, does the model coach them, or just hand over the finished answer?

The behavior comes from Marchal et al. 2026, *Architecting Trust in Artificial Epistemic Agents* ([arXiv:2603.02960](https://arxiv.org/abs/2603.02960), §4.2): when a user signals a learning goal, a model that produces the completed output *substitutes* for their reasoning (the deskilling-relevant failure); one that asks what they think, flags weaknesses, and prompts revision *scaffolds* it.

> ⚠️ **Status: work in progress (pilot).** This is a small, self-directed study project — **not a benchmark**, and **not affiliated with or endorsed by** UK AISI, the Inspect maintainers, or the paper's authors. It builds on their public work. Dataset, results across models, and a full write-up (with limitations foregrounded) will land here as the pilot progresses.

## Plan

A versioned dataset of ~50–80 prompts (each carrying an explicit learning signal), run identically across 2–4 frontier models, scored by an independent grader model against a multi-criterion rubric, with browsable transcript logs published via GitHub Pages.

## Development

See [CLAUDE.md](CLAUDE.md) for the full setup, the Inspect mental model, and project conventions.

```bash
python3.13 -m venv inspect-env && source inspect-env/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your ANTHROPIC_API_KEY to .env
```

## License

MIT — see [LICENSE](LICENSE).
