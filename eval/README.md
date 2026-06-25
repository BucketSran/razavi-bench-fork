# Evaluation Settings

Razavi-bench exposes two public evaluation settings.

## `closed-book`

The agent receives only the task text and figures, then writes:

```text
/app/answer.md
```

This measures direct analog-circuit reasoning without simulator support.

Build from the repository root:

```bash
docker build -f eval/closed-book/Dockerfile -t razavi-bench-closed-book .
```

## `ngspice-sky130`

The agent receives the same task text and figures, plus `ngspice`, a lightweight
Sky130 model bundle, and example SPICE decks.

The final required output is still:

```text
/app/answer.md
```

Intermediate simulation decks and logs are not directly graded.

Build from the repository root:

```bash
docker build -f eval/ngspice-sky130/Dockerfile -t razavi-bench-ngspice-sky130 .
```

Run the public examples locally:

```bash
cd eval/ngspice-sky130
./run_examples.sh
```

