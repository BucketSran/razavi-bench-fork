#!/usr/bin/env python3
import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


DEFAULT_EXPERIMENT_DIR = Path(__file__).resolve().parents[1]
MODEL_ORDER = ["claude", "gemini", "gpt"]
MODEL_LABELS = {
    "claude": "Claude",
    "gemini": "Gemini",
    "gpt": "GPT",
}
ROLLOUT_ORDER = [1, 2, 3]
PART_ORDER = ["part1_first_30", "part2_last_20", "all"]
PART_LABELS = {
    "part1_first_30": "Part 1 (30 tasks)",
    "part2_last_20": "Part 2 (20 tasks)",
    "all": "Overall",
}
JUDGE_ORDER = ["minimax", "deepseek"]
JUDGE_LABELS = {
    "minimax": "MiniMax M3",
    "deepseek": "DeepSeek V4 Pro",
}
JUDGE_COLORS = {
    "minimax": "#4062bb",
    "deepseek": "#e36414",
}
SUMMARY_FIELDS = [
    "judge_family",
    "source_judge_runs",
    "answer_model_family",
    "rollout",
    "part",
    "n_answers",
    "n_judgments",
    "avg_score_0_to_4",
    "avg_percent",
    "score_distribution",
]


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def load_summary(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    if not rows:
        raise SystemExit(f"No rows found in {path}")
    return rows


def judge_family(row: dict, path: Path) -> str:
    label = f"{row.get('judge_model', '')} {path.name}".lower()
    if "minimax" in label:
        return "minimax"
    if "deepseek" in label:
        return "deepseek"
    raise ValueError(f"Unknown judge model for {path}: {row.get('judge_model')}")


def part_for_task(task_slug: str) -> str:
    if task_slug.startswith("part1-"):
        return "part1_first_30"
    if task_slug.startswith("part2-"):
        return "part2_last_20"
    raise ValueError(f"Unknown task part: {task_slug}")


def build_summary_rows(judge_output_dir: Path) -> list[dict]:
    buckets: dict[tuple[str, str, int, str], list[int]] = defaultdict(list)
    task_sets: dict[tuple[str, str, int, str], set[str]] = defaultdict(set)
    source_runs: dict[str, set[str]] = defaultdict(set)

    paths = sorted(judge_output_dir.glob("*.jsonl"))
    if not paths:
        raise SystemExit(f"No judge output JSONL files found in {judge_output_dir}")

    for path in paths:
        for row in load_jsonl(path):
            score = row.get("score_0_to_4")
            if score is None:
                continue
            judge = judge_family(row, path)
            model = row["answer_model_family"]
            rollout = int(row["rollout"])
            task_slug = row["task_slug"]
            part = part_for_task(task_slug)
            source_runs[judge].add(path.stem)
            for part_key in (part, "all"):
                key = (judge, model, rollout, part_key)
                buckets[key].append(int(score))
                task_sets[key].add(task_slug)

    rows = []
    for judge in JUDGE_ORDER:
        for model in MODEL_ORDER:
            for rollout in ROLLOUT_ORDER:
                for part in PART_ORDER:
                    key = (judge, model, rollout, part)
                    scores = buckets[key]
                    distribution = Counter(scores)
                    avg_score = sum(scores) / len(scores)
                    rows.append(
                        {
                            "judge_family": judge,
                            "source_judge_runs": ";".join(sorted(source_runs[judge])),
                            "answer_model_family": model,
                            "rollout": rollout,
                            "part": part,
                            "n_answers": len(task_sets[key]),
                            "n_judgments": len(scores),
                            "avg_score_0_to_4": round(avg_score, 6),
                            "avg_percent": round(avg_score / 4 * 100, 4),
                            "score_distribution": json.dumps(dict(sorted(distribution.items())), sort_keys=True),
                        }
                    )
    return rows


def write_summary(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=SUMMARY_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def score_lookup(rows: list[dict]) -> dict[tuple[str, str, int, str], float]:
    values = {}
    for row in rows:
        key = (
            row["judge_family"],
            row["answer_model_family"],
            int(row["rollout"]),
            row["part"],
        )
        values[key] = float(row["avg_percent"])
    return values


def y_labels() -> list[str]:
    labels = []
    for model in MODEL_ORDER:
        for rollout in ROLLOUT_ORDER:
            labels.append(f"{MODEL_LABELS[model]} R{rollout}")
    return labels


def plot_scores(rows: list[dict], output_png: Path, output_svg: Path) -> None:
    scores = score_lookup(rows)
    fig, axes = plt.subplots(1, len(PART_ORDER), figsize=(14.8, 7.0), sharey=True)
    fig.patch.set_facecolor("white")

    y_positions = list(range(len(MODEL_ORDER) * len(ROLLOUT_ORDER)))
    bar_height = 0.32
    offsets = {
        "minimax": -bar_height / 2,
        "deepseek": bar_height / 2,
    }

    for ax, part in zip(axes, PART_ORDER):
        for judge in JUDGE_ORDER:
            values = []
            for model in MODEL_ORDER:
                for rollout in ROLLOUT_ORDER:
                    values.append(scores[(judge, model, rollout, part)])
            ys = [y + offsets[judge] for y in y_positions]
            bars = ax.barh(
                ys,
                values,
                height=bar_height,
                label=JUDGE_LABELS[judge],
                color=JUDGE_COLORS[judge],
            )
            for value, bar in zip(values, bars):
                ax.text(
                    value + 0.45,
                    bar.get_y() + bar.get_height() / 2,
                    f"{value:.1f}",
                    va="center",
                    ha="left",
                    fontsize=8,
                    color="#2f2f2f",
                )

        ax.set_title(PART_LABELS[part], fontsize=12, weight="bold")
        ax.set_xlim(50, 100)
        ax.set_xlabel("Average score (%)")
        ax.grid(axis="x", color="#d8d8d8", linewidth=0.8, alpha=0.8)
        ax.set_axisbelow(True)
        for spine in ("top", "right", "left"):
            ax.spines[spine].set_visible(False)

    axes[0].set_yticks(y_positions)
    axes[0].set_yticklabels(y_labels())
    axes[0].invert_yaxis()

    for boundary in (2.5, 5.5):
        for ax in axes:
            ax.axhline(boundary, color="#c9c9c9", linewidth=0.9)

    fig.suptitle("Razavi-Bench Direct QA Scores by Rollout", fontsize=16, weight="bold", y=0.98)
    fig.text(
        0.5,
        0.925,
        "Each row is one model rollout. MiniMax and DeepSeek bars average the two available judge runs.",
        ha="center",
        fontsize=10,
        color="#4a4a4a",
    )
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 0.02))

    output_png.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout(rect=[0.03, 0.08, 1, 0.9])
    fig.savefig(output_png, dpi=220)
    fig.savefig(output_svg)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--summary",
        type=Path,
        default=DEFAULT_EXPERIMENT_DIR / "judge_scores" / "summary.csv",
        help="Rollout-aware score summary CSV.",
    )
    parser.add_argument(
        "--judge-output-dir",
        type=Path,
        default=DEFAULT_EXPERIMENT_DIR / "judge_outputs",
        help="Directory containing per-answer judge output JSONL files.",
    )
    parser.add_argument(
        "--rebuild-summary",
        action="store_true",
        help="Regenerate summary CSV from judge output JSONL before plotting.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=DEFAULT_EXPERIMENT_DIR / "figures",
        help="Directory for generated figures.",
    )
    args = parser.parse_args()

    if args.rebuild_summary:
        write_summary(args.summary, build_summary_rows(args.judge_output_dir))
    rows = load_summary(args.summary)
    output_png = args.out_dir / "judge_scores.png"
    output_svg = args.out_dir / "judge_scores.svg"
    plot_scores(rows, output_png, output_svg)
    print(output_png)
    print(output_svg)


if __name__ == "__main__":
    main()
