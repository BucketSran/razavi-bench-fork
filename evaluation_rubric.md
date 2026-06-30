# Evaluation Rubric

The source Razavi articles provide AI responses, Razavi's comments, and 0-4
scores, but not a detailed per-point grading table. This file is an inferred
evaluation guide for re-scoring new model answers.

## Scale

| Score | Meaning | Criteria |
|---:|---|---|
| 4 | Correct | Correct conclusion and reasoning; topology, device roles, dominant mechanism, trend, and key assumptions are right. |
| 3 | Mostly correct | Main conclusion is right, with a minor omission, imprecision, or modeling flaw that does not change the result. |
| 2 | Partially correct | Identifies some relevant mechanism, but misses an important circuit detail, trend, or design consequence. |
| 1 | Mostly incorrect | Main conclusion is wrong, but the answer contains a small amount of relevant circuit understanding. |
| 0 | Incorrect or unusable | Fundamentally wrong, internally inconsistent, or based on a mistaken topology/device/connection. |

## Guidance

Evaluate against the task's `golden_solution.md`, prioritizing analog-circuit
reasoning over surface similarity to the original article answer. Reward correct
identification of device types, signal paths, feedback, loading, dominant
mechanisms, and valid boundary conditions. Penalize memorized formulas used
outside their assumptions, wrong topology recognition, missed shorts or
connections, and right final claims supported by misleading physical reasoning.

Do not treat Razavi's historical scores for article responses as hidden labels
for new model answers. They are examples used to infer this guide.
