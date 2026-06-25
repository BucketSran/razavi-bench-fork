# Analog Design AI Benchmark

This repository extracts the question-answer assessments from Behzad Razavi's
`Analog Design Experiments With AI` Part 1 and Part 2 articles into an
rtl-forge-style one-task-per-directory layout.

Layout:

```text
tasks/<part>-<number>-<slug>/
  instruction.md
  golden_solution.md
  figure-xx.png  # when the question has a figure

eval/
  README.md
  closed-book/
    Dockerfile
    README.md
  ngspice-sky130/
    Dockerfile
    README.md
    examples/
    models/
```


Solution files:

- `golden_solution.md` contains the standard answer written for benchmark evaluation.
- Historical ChatGPT/Gemini answers from the articles are intentionally not stored in task directories.
- Figure PNGs, when present, live directly beside `instruction.md`.

Counts from the parsed source PDFs:

- Part 1: 30 questions (article numbering Q1-Q30).
- Part 2: 20 questions (article numbering Q1-Q20).

Note: the user request mentioned 40 questions for Part 1, but the available
Part 1 PDF contains Q1 through Q30. No synthetic questions were added.

Evaluation guidance:

- See `evaluation_rubric.md` for the inferred 0-4 grading rubric. The rubric is
  summarized from Razavi's comments and scores in the source articles; it is not
  a verbatim per-point rubric published in the articles.
- The benchmark defines two public evaluation settings:
  - `eval/closed-book`: the agent sees only the question text and figures, then
    writes `/app/answer.md`.
  - `eval/ngspice-sky130`: the agent sees the same question text and figures,
    but can also use ngspice plus a lightweight Sky130 model bundle while
    reasoning. The required final output is still `/app/answer.md`.
- Both settings are scored from the final answer only, using
  `golden_solution.md` and `evaluation_rubric.md`. Simulator transcripts,
  netlists, and other intermediate files are not directly graded.

Verification notes:

- `verification/sky130_ngspice/summary.md` records representative ngspice checks run with a local volare Sky130A PDK. These checks validate selected device and trend claims; they are not a complete one-netlist-per-task proof.
