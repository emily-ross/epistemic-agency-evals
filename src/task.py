"""Scaffolding vs. substitution — a propensity eval (pilot).

Measures how often a model hands a user the finished product of the user's own
cognitive task when the user signalled an intent to do that work themselves.
Full design in SPEC.md; decision history in DECISIONS.md.

    inspect eval src/task.py --model anthropic/claude-sonnet-5 --limit 6
    inspect eval src/task.py --model anthropic/claude-sonnet-5

Samples are interleaved signal/request, so an even --limit keeps pairs intact.
"""

from pathlib import Path

from inspect_ai import Epochs, Task, task
from inspect_ai.dataset import json_dataset
from inspect_ai.scorer import mode_score
from inspect_ai.solver import generate
from inspect_ai.viewer import TaskSamplesView, ViewerConfig

from grading import substitution

DATASET = Path(__file__).parent.parent / "data" / "prompts.json"

# The model under test and its grader must be different families, so that no
# model is judging its own output style (D-030).
DEFAULT_GRADER = "openai/gpt-5.4-mini"


@task
def scaffolding_vs_substitution(
    grader: str = DEFAULT_GRADER,
    condition: str | None = None,
    epochs: int = 1,
) -> Task:
    """The eval.

    Args:
        grader: independent grader model, run at temperature 0.
        condition: restrict to "signal" or "request" (dev runs, or costing the
            control separately — SPEC §7 open item 1). Both by default.
        epochs: repeats per sample; verdicts reduce by majority. 1 for the
            pilot.
    """
    dataset = json_dataset(str(DATASET))
    if condition is not None:
        dataset = dataset.filter(lambda s: s.metadata["condition"] == condition)

    return Task(
        dataset=dataset,
        # No system_message: the samples carry their own profile, and any added
        # persona would break the plain-assistant-mode claim in SPEC §1. No
        # temperature override either — deployment-realistic defaults, recorded
        # in the log. No max_tokens: a truncated response would grade as
        # non-substitution, which is a silent false negative.
        solver=generate(),
        scorer=substitution(grader),
        # Epoch reduction runs even at epochs=1, and the default mean_score()
        # reducer converts values with Inspect's *default* value_to_float —
        # which silently maps every verdict string to 0.0 before the metrics
        # ever see it. mode_score() is value-agnostic: it passes the verdict
        # through at one epoch, and takes the majority verdict at more.
        epochs=Epochs(epochs, mode_score()),
        viewer=ViewerConfig(
            task_samples_view=TaskSamplesView(
                name="Substitution",
                score_labels={"substitution": "Substitution"},
                score_color_scales={
                    "substitution": {"SUBSTITUTION": "bad", "NOT_SUBSTITUTION": "good"}
                },
            )
        ),
        metadata={"grader": grader},
    )
