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
- this skill, when installed, is in `/tools/ngspice-sky130/skills/ngspice-sky130`.

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

## Helper Scripts

The `assets/` directory contains small Python helpers that copy templates into `/app`, run ngspice, and print parsed output. They are convenience tools, not required.

Example:

```bash
python /tools/ngspice-sky130/skills/ngspice-sky130/assets/run_op_probe.py \
  --template nfet_op \
  --out /app/nfet_op.cir
```

Then inspect `/app/nfet_op.log`.
