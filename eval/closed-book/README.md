# Closed-Book Evaluation

This setting evaluates analog-design reasoning without simulator access.

The agent receives only:

- the task instruction from `tasks/<task>/instruction.md`;
- any figure PNG files that live beside the instruction.

The agent must write its final answer to:

```text
/app/answer.md
```

Scoring is based only on the final answer. A judge compares `/app/answer.md`
against the task's `golden_solution.md` and the repository-level
`evaluation_rubric.md`.

This setting is intended to measure direct conceptual reasoning, topology
recognition, and concise analog-circuit explanation.

