# Experiment: 2026-06-26 direct-qa

This directory contains cleaned AI question-answer pairs from one Razavi-Bench
experiment.

## Experiment

- Run date: 2026-06-26
- Benchmark release: direct-mm-v4-newgolden
- Models: GPT-5.5 Thinking XHigh, Gemini 3.1 Pro CC Thinking High, Claude Opus
  4.8 Thinking Max
- Rollouts: 3 per model
- Records: 450 total, stored as 9 model-output JSONL files

## Files

- `model_outputs/`: cleaned GPT, Gemini, and Claude answer JSONL files, split
  by model family and rollout.
- `judge_outputs/`: per-answer judge model output JSONL files.
- `judge_scores/summary.csv`: aggregate score table for reports and plots.
- `tools/`: scripts used to generate `judge_outputs/*.jsonl`.

Each `model_outputs/*.jsonl` line is one JSON object with the effective
benchmark question, final visible model answer, run date, rollout number,
answer round count, model call count, and internet/tool evidence flag.
There are 9 files: 3 model families times 3 rollouts, with 50 records each.

The model output files exclude system prompts, process instructions, hidden
reasoning, Vela session IDs, provider metadata, token/cost data, and internal
record IDs.

`internet_or_tool_evidence` is `false` for every record in this experiment. The
original audit checked exposed tools/functions, structured tool calls, and
web-search request counters.

Judge outputs are stored separately under `judge_outputs/` because they are tied
to the rubric and golden answers used at judge time. If the rubric or golden
answers change, add a new judge output artifact under this experiment rather
than modifying the cleaned model output files.

`judge_scores/summary.csv` is derived from the judge outputs. Use it as the
single summary source for reports and plots; use `judge_outputs/*.jsonl` when
per-answer scores and rationales are needed.

The judge scripts read API keys from environment variables or interactive input.
They do not store credentials in the repository.

See `../../LICENSE` for dataset, code, and source-material terms.
