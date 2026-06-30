# Judge Scores

This directory contains judge-model scores for the
`2026-06-26-direct-qa` experiment.

Scores are separate from the cleaned model outputs because the rubric and
golden answers may change. Add a new score file when re-judging with a new
model, rubric, or golden-answer revision.

Each score row joins to `../gpt.jsonl`, `../gemini.jsonl`, or `../claude.jsonl`
by:

- `answer_model_family`
- `rollout`
- `task_slug`

Each row stores the judge model, judge run date, rubric hash, golden-solution
hash, score, and concise rationale.

## Files

- `minimax-m3-20260630-120035.jsonl`: MiniMax-M3 judge scores for all 450
  answers.
- `deepseek-v4-pro-20260630-121054.jsonl`: DeepSeek-V4-Pro judge scores for all
  450 answers.
- `minimax-m3-20260630-123355.jsonl`: MiniMax-M3 judge scores from the later
  8192-token run.
- `deepseek-v4-pro-20260630-123714.jsonl`: DeepSeek-V4-Pro judge scores from
  the later 8192-token run.
- `judge_runs_manifest.csv`: judge run names, completion timestamps, and
  available duration notes.
- `judge_runs_summary.csv`: aggregate summary across all judge runs.
- `judge_runs_pairwise_summary.csv`: pairwise agreement summary across judge
  runs.
