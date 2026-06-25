---
name: ngspice-sky130
description: "Use ngspice with the Razavi-Bench Sky130 model bundle for small analog-circuit probes. Provides minimal, reusable workflows for operating-point checks, small-signal parameter extraction, and simple AC/transient sanity tests. Use as supporting evidence only; final answers must still be analog-circuit reasoning."
---

# Sky130 Ngspice Skill

Use this skill when a Razavi-Bench task benefits from checking a circuit intuition with ngspice and the bundled Sky130 1.8 V primitive models.

Do not treat simulation as the answer. Many tasks are qualitative, depend on small-signal assumptions, or omit exact device sizes and bias points. A simulation is useful only if the deck topology, bias condition, device sizes, and measured quantity match the question you are answering.

## Environment

In the Razavi-Bench `ngspice-sky130` setting:

- task files are in `/app`;
- Sky130 models are in `/tools/ngspice-sky130/models`;
- example decks are in `/tools/ngspice-sky130/examples`;
- this skill, when installed for Claude Code, is in `/app/.claude/skills/ngspice-sky130`.

The core include is:

```spice
.include "/tools/ngspice-sky130/models/sky130.lib.spice"
```

If you are running from a checkout instead of Vela, use a relative path to `eval/ngspice-sky130/models/sky130.lib.spice`.

## Minimal Workflow

1. Read `/app/instruction.md` and inspect any PNGs in `/app`.
2. Decide what the simulation is supposed to test: operating point, sign, trend, pole, gain, or impedance.
3. Create a new deck under `/app`, or copy an example from `/tools/ngspice-sky130/examples`.
4. Check that the deck matches the question. Do not blindly reuse example topology, sizes, or bias.
5. Run:

```bash
ngspice -b /app/your_deck.cir > /app/your_deck.log 2>&1
```

6. Read the log, then write only the final reasoning to `/app/answer.md`.

## Zero-Start Quickstart

If you have never used ngspice in this environment, do this first:

```bash
ls -la /app
ls -la /tools/ngspice-sky130/models
ls -la /tools/ngspice-sky130/examples
ngspice --version
```

Then run a known-good probe:

```bash
python3 /app/.claude/skills/ngspice-sky130/assets/run_op_probe.py \
  --template nfet_op \
  --out /app/nfet_op.cir

sed -n '1,120p' /app/nfet_op.cir
sed -n '1,160p' /app/nfet_op.log
```

This teaches the three essential pieces:

- a deck includes `sky130.lib.spice`;
- the transistor instance name `Xn` maps to ngspice operating-point variables such as `@m.xn.msky130_fd_pr__nfet_01v8[gm]`;
- `.control ... print ... .endc` prints values into the log.

After that, copy the closest generated deck and change only what the question requires.

Available helper templates:

```text
nfet_op
pfet_op
common_source_op
source_follower_op
```

Example:

```bash
python3 /app/.claude/skills/ngspice-sky130/assets/run_op_probe.py \
  --template source_follower_op \
  --out /app/source_follower_op.cir
```

## Choosing A Probe

Before writing a deck, classify the task. Use ngspice only when the task has a concrete electrical quantity that can be probed under a stated bias condition.

| Question type | Useful probe | Avoid |
| --- | --- | --- |
| Device region, saturation, overdrive, bias feasibility | `.op`, print node voltages and device operating-point values | treating one arbitrary bias as proof for all operating points |
| Gain, source follower gain, transconductance trend | `.op` for `gm`, `gds`, `gmbs`; optional `.ac` if the topology is fully specified | using a common-source deck for a different topology |
| Input/output resistance | inject a small test current or voltage source and compute `v/i` | measuring the wrong port or leaving independent sources active incorrectly |
| Capacitance, pole, speed, or phase-noise trend | use simulation only as a sanity check for sign/trend after deriving the mechanism | pretending Sky130 short-channel numbers are the textbook answer |
| Feedback interpretation, latch topology, oscillation condition, qualitative “why” questions | usually answer from analog reasoning directly | forcing a simulation without a complete transient setup |

If the figure or prompt omits sizes, loads, bias currents, clock waveforms, or initial conditions, state the missing assumption. A simulation with invented values can support a trend, but it cannot replace the reasoning.

## Common Checks

Operating point:

```spice
.op
.control
run
print v(out)
let gm=@m.xn.msky130_fd_pr__nfet_01v8[gm]
let gds=@m.xn.msky130_fd_pr__nfet_01v8[gds]
print gm gds
.endc
```

Small-signal gain estimate:

```spice
let gain_cs=-gm/(gds+1/20000)
print gain_cs
```

Source-follower estimate:

```spice
let gain_sf=gm/(gm+@m.xn.msky130_fd_pr__nfet_01v8[gmbs]+1/10000)
print gain_sf
```

Sanity checks before trusting a result:

- Is the device in the intended region? Check `vds`, `vgs`, threshold, and `vdsat` when possible.
- Are you holding the same quantity fixed as the question? For example, fixed overdrive, fixed current, fixed geometry ratio, and fixed VGS can produce different trends.
- Are the model limits relevant? A Sky130 short-channel simulation may disagree with a long-channel textbook assumption.
- Does the sign convention match the circuit? PMOS and NMOS signs can look different while the small-signal form is equivalent.
- Does the question provide enough numerical detail for simulation? If not, state the assumption and use simulation only as a qualitative sanity check.
- Did the deck answer the same question? A common-source example does not answer a source-follower question; a fixed-`VGS` sweep does not answer a fixed-current design question.

## When Not To Simulate

Skip simulation, or treat it only as secondary evidence, when:

- the question asks for a pure topology classification;
- the figure lacks enough device sizes, loads, or bias points;
- the intended answer is a long-channel textbook trend;
- the question asks about sign conventions, model form, or feedback interpretation.

In these cases, write the analog reasoning directly and mention any assumptions.

## Writing The Final Answer

The grader reads `/app/answer.md`, not your `.cir` files or logs. Your final answer should include:

- the circuit conclusion;
- the key analog mechanism;
- the relevant assumption, if simulation required one;
- at most one concise simulation-backed number or trend, only if it truly supports the conclusion.

Do not paste raw ngspice logs into `/app/answer.md`.

## Helper Scripts

The `assets/` directory contains small Python helpers that copy templates into `/app`, run ngspice, and print parsed output. They are convenience tools, not required.

Example:

```bash
python3 /app/.claude/skills/ngspice-sky130/assets/run_op_probe.py \
  --template nfet_op \
  --out /app/nfet_op.cir
```

Then inspect `/app/nfet_op.log`.
