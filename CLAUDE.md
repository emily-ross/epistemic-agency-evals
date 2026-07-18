# CLAUDE.md

Guidance for AI coding agents (Claude Code, Cursor, etc.) working in this repository.

## What this is

`epistemic-agency-evals` is a **pilot** behavioral evaluation, built on [Inspect](https://inspect.aisi.org.uk) (UK AISI's open-source eval framework), measuring whether frontier language models **scaffold** a user's reasoning or **substitute** for it.

The behavior, from Marchal et al. 2026, *Architecting Trust in Artificial Epistemic Agents* ([arXiv:2603.02960](https://arxiv.org/abs/2603.02960), §4.2): when a user signals they are trying to learn or think something through, does the model produce the finished output for them (**substitution** — the deskilling-relevant failure) or coach them — ask what they think, point at weaknesses, prompt revision (**scaffolding**)? This repo operationalizes that rubric as a runnable eval.

### Honesty guardrails (important — this is the whole credibility of the artifact)

This is a **pilot**, and every artifact here must read as one:
- **Do not call it a "benchmark."** It is a small pilot eval.
- **Do not imply endorsement** by UK AISI, the Inspect maintainers, or the paper's authors. It builds on public work; it is not affiliated with them.
- Keep **limitations prominent**: pilot scale; model-graded scoring (always report measured human-grader agreement); prompt distribution not validated.
- Every claim in the README/write-up must be **literally true at the repo link**.

## Stack & environment

- **Python** 3.11–3.13 (3.10 floor). Local venv lives at `inspect-env/` (git-ignored).
- **Inspect** — pinned: `inspect-ai==0.3.247` (they release near-daily; keep it pinned). Plus `anthropic`.
- **Model access** via API keys in `.env` (git-ignored; see `.env.example`). At minimum `ANTHROPIC_API_KEY`; optionally `OPENAI_API_KEY` / `OPENROUTER_API_KEY` for cross-model runs.

Setup:
```bash
python3.13 -m venv inspect-env
source inspect-env/bin/activate
pip install -r requirements.txt        # or: pip install inspect-ai==0.3.247 anthropic
cp .env.example .env                    # then add your real key(s) to .env
```

## Inspect mental model

**Task = dataset + solver + scorer.** A minimal task:
```python
from inspect_ai import Task, task
from inspect_ai.dataset import json_dataset
from inspect_ai.scorer import model_graded_qa
from inspect_ai.solver import generate

@task
def scaffolding_vs_substitution():
    return Task(
        dataset=json_dataset("data/prompts.jsonl"),
        solver=generate(),
        scorer=model_graded_qa(template=RUBRIC, model="anthropic/claude-opus-4-8"),
    )
```

- **dataset** — a fixed, versioned JSONL of prompts (the artifact that makes runs comparable across models and over time). Every sample carries `metadata` (e.g. `domain`, `signal_strength`) so results can be sliced later.
- **solver** — how the model is prompted. Default `generate()`; put `system_message(...)` ahead of it in the solver list when needed.
- **scorer** — `model_graded_qa()` with a custom multi-criterion rubric and an **independent grader model** (a *different* family than the model under test), at **temperature 0**.

## Common commands
```bash
inspect eval src/task.py --model anthropic/claude-sonnet-5 --limit 10   # dev run — ALWAYS --limit while iterating (cost control)
inspect eval src/task.py --model anthropic/claude-sonnet-5              # full run
inspect view                                                           # browse transcripts + grades locally
inspect view bundle --log-dir logs --output-dir docs/                  # static log site for GitHub Pages
```
Analysis: `evals_df()` / `samples_df()` from `inspect_ai.analysis` → results table + charts, sliced by metadata.

## Conventions & guardrails

- **Pin `inspect-ai`.** Near-daily releases; don't float the version.
- **Always `--limit` during dev.** Model-graded scoring doubles API calls; keep dev runs small (pilot budget ~$10–30 total).
- **Never commit secrets.** Keys live in `.env` (git-ignored). `logs/` and `inspect-env/` are git-ignored too.
- **Manually review every dataset prompt.** Model-generated prompts drift generic fast — cut ruthlessly. Record `domain` and learning-signal strength in each sample's `metadata`.
- **Grader reliability is the make-or-break.** "Scaffolding vs. substitution" is a soft construct. Validate the grader against blind human grading (~20 transcripts) and report the agreement % in the README. Pre-committed fallback if agreement is poor: switch to the **false-premise-challenge** behavior (§4.2's other half — near-objective scoring).
- **Published logs are public evidence.** The bundled log site under `docs/` gets published; make sure transcripts contain nothing that shouldn't be public.

## Planned layout
```
src/        Inspect task + scorer (the rubric)
data/       prompts.jsonl (versioned dataset)
logs/       raw eval run logs (git-ignored)
docs/       bundled static log viewer → GitHub Pages
SPEC.md     one-page eval spec: behavior definition, citations, example pairs, rubric
SOURCES.md  annotated reading list (the lit-review artifact, folded in)
```

## Key references
- Inspect docs: https://inspect.aisi.org.uk · Tutorial: https://inspect.aisi.org.uk/tutorial.html · Model-graded scoring: https://inspect.aisi.org.uk/model-graded.html · Log publishing: https://inspect.aisi.org.uk/log-viewer.html
- Inspect docs as one LLM-readable file: https://inspect.aisi.org.uk/llms.txt — point agents at this when stuck.
- The paper: https://arxiv.org/abs/2603.02960 (§3–4 core; §6 for discussion framing).
