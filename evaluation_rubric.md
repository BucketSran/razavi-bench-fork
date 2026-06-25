# Evaluation Rubric

This benchmark is derived from Behzad Razavi's *Analog Design Experiments With AI* articles. The source articles provide each AI response, Razavi's comments, and a 0-4 score for that response, but they do not define a detailed per-point grading rubric.

The rubric below is an inferred evaluator guide, summarized from the pattern of Razavi's comments and scores across the 50 questions. It should be used as guidance for evaluating new answers, not as a verbatim rule stated in the articles.

## Scoring Scale

| Score | Meaning | Typical Criteria |
|---:|---|---|
| 4 | Correct | The answer matches the correct circuit behavior. The topology, device roles, dominant mechanism, trend, and any key formula or boundary condition are correct. A concise answer can receive full credit if the essential reasoning is right. |
| 3 | Mostly correct | The main conclusion is correct, but the answer has a minor flaw: an imprecise attribution, an unnecessary or inconsistent modeling detail, a small parasitic-location mistake, or an incomplete explanation that does not overturn the main result. |
| 2 | Partially correct | The answer captures some relevant mechanism or analysis framework, but misses an important circuit detail, trend, topology implication, or design consequence. It is not reliable as a complete answer. |
| 1 | Mostly incorrect | The final conclusion or main trend is wrong, but the answer shows a small amount of relevant understanding, such as identifying one local effect, one device role, or one partially applicable idea. |
| 0 | Incorrect or unusable | The answer is fundamentally wrong. Common causes include misidentifying NMOS/PMOS devices, misunderstanding circuit connections, missing a feedback path, classifying the topology incorrectly, giving internally inconsistent reasoning, or dismissing a valid circuit instead of analyzing it. |

## What Razavi Appears to Reward

Razavi's scoring emphasizes analog-design judgment, not just algebraic manipulation. A good answer should:

- Identify device types and terminal connections correctly.
- Recognize the circuit topology and signal path.
- Notice feedback paths, shorts, bias constraints, and loading effects.
- Predict the correct qualitative trend when a parameter changes.
- Explain the dominant physical mechanism behind the trend.
- Use formulas only when their assumptions match the circuit.
- State important boundary conditions, such as constant overdrive, saturation, oscillation condition, load dominance, or large-signal switching behavior.
- Avoid design-misleading conclusions, even if some local calculation looks plausible.

## Common Failure Modes

The original AI answers often lose credit for these reasons:

- Confusing PMOS and NMOS symbols.
- Treating a source follower, common-gate stage, cascode, inverter, or feedback structure as the wrong topology.
- Ignoring a short, gate connection, source connection, or feedback loop.
- Applying a memorized formula without checking whether its assumptions hold.
- Predicting the wrong performance trend because capacitance, transconductance, resistance, or switching behavior is considered in isolation.
- Missing large-signal behavior in oscillators, latches, and dividers.
- Giving an answer that discourages a useful circuit exploration because the circuit was misunderstood.

## Recommended Use in This Benchmark

Do not store Razavi's original numeric scores inside individual task files. They were scores for the historical ChatGPT/Gemini responses in the articles, not labels that should be exposed to models solving the benchmark.

For evaluating a new model response:

1. Compare the response against the task's `golden_solution.md`, especially Razavi's comment and corrected reasoning.
2. Assign 0-4 using the inferred scale above.
3. Prefer correctness of analog reasoning over surface similarity to the original AI answer.
4. Penalize answers that reach the right final word for the wrong physical reason when that reason would mislead design decisions.
5. Award partial credit when the response identifies a real mechanism but misses another mechanism that changes the conclusion.

## Caveat

This rubric is inferred from the articles. Razavi did not publish a formal grading table that defines every score level. Borderline cases should be judged by expert analog-circuit reasoning and by consistency with the examples in the source articles.
