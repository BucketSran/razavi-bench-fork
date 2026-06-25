# Ngspice + Sky130 Evaluation

This setting evaluates the same final-answer task as the closed-book setting,
but gives the agent a simulator environment for optional reasoning.

The agent receives:

- the task instruction from `tasks/<task>/instruction.md`;
- any figure PNG files that live beside the instruction;
- `ngspice`;
- a lightweight Sky130 1.8 V model bundle under `eval/ngspice-sky130/models`;
- example netlists under `eval/ngspice-sky130/examples`.

The agent may write and run its own SPICE decks while solving the problem. The
benchmark does not grade those intermediate files. The only required output is:

```text
/app/answer.md
```

Scoring is still based only on the final answer. A judge compares
`/app/answer.md` against the task's `golden_solution.md` and the
repository-level `evaluation_rubric.md`.

The simulator setting is intended to test whether an agent can use circuit
simulation as evidence for analog reasoning. Many Razavi questions are
qualitative or under-specified, so simulation should be used as a supporting
tool, not as a replacement for small-signal reasoning.

## Sky130 Ngspice Skill

This directory also includes a lightweight skill-style guide under:

```text
skills/ngspice-sky130/
```

It is adapted from the ngspice workflow in
`Arcadia-1/gmoverid-skill`, but stripped down for this benchmark:

- it uses this directory's Sky130 model bundle, not PTM models;
- it focuses on operating-point and small-signal probes;
- it warns agents to verify topology, bias condition, device sizes, and measured
  quantity before trusting simulation output.

The helper entry point is:

```bash
python ../../skills/ngspice-sky130/assets/run_op_probe.py \
  --template nfet_op \
  --out /tmp/nfet_op.cir
```

In Vela, the same skill can be exposed at
`/tools/ngspice-sky130/skills/ngspice-sky130/`.

## Run The Examples

From the repository root:

```bash
cd eval/ngspice-sky130
./run_examples.sh
```

Each example writes an ngspice log next to the `.cir` file.

## Model Bundle

The included model files are a minimal subset derived from the open-source
SkyWater SKY130 primitive models, licensed under Apache 2.0. They are included
to make the benchmark environment reproducible without requiring a full local
PDK installation.
