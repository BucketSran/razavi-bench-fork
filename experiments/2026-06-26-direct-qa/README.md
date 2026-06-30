# Experiment: 2026-06-26 direct-qa

This directory contains cleaned AI question-answer pairs from one Razavi-Bench
experiment.

## Experiment

- Run date: 2026-06-26
- Benchmark release: direct-mm-v4-newgolden
- Models: GPT-5.5 Thinking XHigh, Gemini 3.1 Pro CC Thinking High, Claude Opus
  4.8 Thinking Max
- Rollouts: 3 per model
- Records: 450 total

## Files

- `gpt.jsonl`: GPT-5.5 Thinking XHigh, 3 rollouts, 150 records.
- `gemini.jsonl`: Gemini 3.1 Pro CC Thinking High, 3 rollouts, 150 records.
- `claude.jsonl`: Claude Opus 4.8 Thinking Max, 3 rollouts, 150 records.
- `judge_scores/`: per-answer judge scores and `summary.csv`.
- `tools/`: scripts used to generate the judge score JSONL files.

Each line is one JSON object with the effective benchmark question, final
visible model answer, run date, rollout number, answer round count, model call
count, and internet/tool evidence flag.

The files exclude system prompts, process instructions, hidden reasoning, Vela
session IDs, provider metadata, token/cost data, and internal record IDs.

`internet_or_tool_evidence` is `false` for every record in this experiment. The
original audit checked exposed tools/functions, structured tool calls, and
web-search request counters.

Judge scores are stored separately under `judge_scores/` because they are tied
to the rubric and golden answers used at judge time. If the rubric or golden
answers change, add a new judge result artifact under this experiment rather
than modifying the cleaned model-output files.

The judge scripts read API keys from environment variables or interactive input.
They do not store credentials in the repository.

See `../../LICENSE` for dataset, code, and source-material terms.
