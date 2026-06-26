<h1 align="center">Razavi-bench</h1>

<p align="center">
  <strong>A compact benchmark for analog-design reasoning.</strong>
</p>

<p align="center">
  <a href="https://github.com/Arcadia-1/razavi-bench/stargazers"><img src="https://img.shields.io/github/stars/Arcadia-1/razavi-bench?style=flat-square&color=f5c542&logo=github" alt="GitHub stars"/></a>
  <a href="https://github.com/Arcadia-1/razavi-bench/network/members"><img src="https://img.shields.io/github/forks/Arcadia-1/razavi-bench?style=flat-square&color=f5c542" alt="GitHub forks"/></a>
  <a href="https://github.com/Arcadia-1/razavi-bench/issues"><img src="https://img.shields.io/github/issues/Arcadia-1/razavi-bench?style=flat-square&color=3fb950" alt="Open issues"/></a>
  <a href="https://github.com/Arcadia-1/razavi-bench/commits/main"><img src="https://img.shields.io/github/last-commit/Arcadia-1/razavi-bench?style=flat-square&color=3fb950" alt="Last commit"/></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/tasks-50-blue?style=flat-square" alt="50 tasks"/>
  <img src="https://img.shields.io/badge/figures-44-blue?style=flat-square" alt="44 figures"/>
  <img src="https://img.shields.io/badge/domain-analog%20design-8a63d2?style=flat-square" alt="Analog design"/>
  <img src="https://img.shields.io/badge/format-markdown-lightgrey?style=flat-square" alt="Markdown format"/>
</p>

<p align="center">
  <img src="docs/assets/razavi_3rollout_model_rows.png" alt="Razavi-bench model comparison" width="86%"/>
</p>

Razavi-bench packages the question-answer assessments from Behzad Razavi's
*Analog Design Experiments With AI* Part 1 and Part 2 into a clean
one-task-per-directory benchmark. The tasks probe whether a model can reason
about MOS devices, small-signal circuits, feedback, oscillators, comparators,
dividers, LNAs, TIAs, and LC oscillators.

The repository keeps only the prompt, figure, and curated golden answer for each
task. The historical ChatGPT/Gemini responses and their article scores are not
stored as task data.

## At a Glance

| Item | Count / Status |
|---|---:|
| Total tasks | 50 |
| Part 1 | 30 questions, Q1-Q30 |
| Part 2 | 20 questions, Q1-Q20 |
| Task figures | 44 |
| `task.toml` files | 0 |
| Source PDFs | Not tracked |

## Repository Layout

```text
tasks/<part>-<number>-<semantic-slug>/
  instruction.md
  golden_solution.md
  figure-xx.png  # only when the question has a figure
```

Top-level files:

| Path | Purpose |
|---|---|
| `manifest.json` | Machine-readable task index |
| `manifest.jsonl` | Line-delimited task index |
| `evaluation_rubric.md` | Inferred 0-4 grading rubric from Razavi's comments and scores |
| `verification/` | Human audit notes and representative simulation checks |

## Task Format

Each `instruction.md` contains only the benchmark prompt and any local figure
reference. It intentionally excludes source metadata, original model answers,
scores, and explanatory commentary.

Each `golden_solution.md` contains the expected reasoning and final answer for
evaluation. The golden answers were reviewed against the source articles,
figures, and circuit analysis.

## Curation

The golden answers have been reviewed task by task. The review record is:

```text
verification/golden_solution_review.md
```

Representative ngspice/Sky130 checks are summarized in:

```text
verification/sky130_ngspice/summary.md
```

These simulations validate selected device and trend claims. They are not meant
to be a one-netlist-per-task proof, because many questions are topology,
feedback, or conceptual reasoning tasks without specified sizes and biases.

## Notes

The user request originally mentioned 40 questions for Part 1, but the available
Part 1 article contains Q1 through Q30. No synthetic questions were added.

## References

- B. Razavi, "Analog Design Experiments With AI—Part 1 [The Analog Mind]," in
  IEEE Solid-State Circuits Magazine, vol. 17, no. 4, pp. 11-15, Fall 2025.
- B. Razavi, "Analog Design Experiments With AI—Part 2 [The Analog Mind]," in
  IEEE Solid-State Circuits Magazine, vol. 18, no. 2, pp. 8-13, Spring 2026.
