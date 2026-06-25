# Golden Solution Review

Date: 2026-06-25

Scope: all 50 `golden_solution.md` files under `tasks/`.

Method:

- Compared each task against the extracted text and figures from Razavi, "Analog Design Experiments With AI - Part 1" and "Part 2".
- Visually inspected ambiguous topology figures.
- Ran representative Sky130/ngspice checks for device trends, gain polarity, source follower/common-source/common-gate behavior, the corrected Q5/Q9/Q10 cases, and ring-oscillator capacitance trends. See `verification/sky130_ngspice/summary.md`.

Limit: not every question is directly SPICE-verifiable without adding arbitrary sizes, bias currents, supplies, and loads. For topology-recognition and feedback questions, the review basis is the source figure plus circuit analysis.

## Part 1

| Q | Task | Status | Review note |
|---|---|---|---|
| 1 | `part1-001-double-length-and-width-mosfet-its-intrinsic` | OK | Matches Razavi's constant-overdrive interpretation; Sky130 trend check supports increased intrinsic gain with longer channel. |
| 2 | `part1-002-student-says-transconductance-mosfet-goes-up-as` | OK | Correctly distinguishes fixed `W/L` from fixed `ID`; matches Razavi's preferred reading. |
| 3 | `part1-003-small-signal-model-pmos-device-identical-nmos` | OK | Correct with consistent sign conventions. |
| 4 | `part1-004-sketch-ix-versus-vx` | OK | Diode-connected NMOS current is zero below threshold and quadratic after turn-on. |
| 5 | `part1-005-sketch-ix-versus-vx` | Fixed | Corrected from drain-voltage sweep to gate-voltage sweep with drain fixed at 1 V; Sky130 DC sweep supports the revised trend. |
| 6 | `part1-006-device-act-as-current-source` | OK | Correctly rejects diode-connected MOS as a good current source due low small-signal resistance. |
| 7 | `part1-007-pmos-common-source-source-degeneration` | OK | Correct PMOS common-source with source degeneration; sign and degeneration factor are appropriate. |
| 8 | `part1-008-source-follower` | OK | Correct source follower; Sky130 source-follower `.tf` supports positive sub-unity gain. |
| 9 | `part1-009-common-gate-source-input` | Fixed | Corrected from common-source/PMOS interpretation to source-driven common-gate stage; Sky130 `.tf` supports positive gain. |
| 10 | `part1-010-source-input-shorted-to-ground` | Fixed | Corrected to note that the input is applied to a source node shorted to ground, so ideal transfer is zero; Sky130 AC check supports zero output. |
| 11 | `part1-011-many-poles-have` | Fixed | Corrected pole count from three to two independent dynamic nodes, matching Razavi's comment. |
| 12 | `part1-012-source-input-resistive-feedback` | Fixed | Corrected input/source connection and feedback divider role; source of `M1` is not grounded. |
| 13 | `part1-013-source-follower-current-source-load` | OK | Correctly identifies source follower rather than common-source active-load stage. |
| 14 | `part1-014-cmos-inverter` | OK | Correct CMOS inverter and analog inverting-stage interpretation. |
| 15 | `part1-015-malformed-cmos-inverter` | OK | Correctly rejects Figure 11(b) as a proper CMOS inverter. |
| 16 | `part1-016-common-source-diode-connected-load` | OK | Correct common-source stage with diode-connected PMOS load. |
| 17 | `part1-017-pmos-input-invalid-pulldown` | Fixed | Corrected device roles: top `M2` is PMOS driven by `Vin`; lower `M1` is not a valid diode/current-source load as drawn. |
| 18 | `part1-018-find-rout` | Fixed | Corrected cascode role: output resistance boost comes from lower PMOS `M1`, not upper `M2`. |
| 19 | `part1-019-ensure-m2-saturation` | OK | Matches Razavi's condition tying saturation to `Vb1` and node `X`, not only `Vb2`. |
| 20 | `part1-020-nmos-cascode-gain-stage` | OK | Correctly identifies NMOS cascode gain stage with `M2` as NMOS cascode. |
| 21 | `part1-021-cascode-structure` | OK | Correctly says not a standard cascode and uses Razavi's output-resistance expression. |
| 22 | `part1-022-explain-why-miller-effect-less-pronounced-cascode` | OK | Correctly states reduced, not zero, Miller multiplication; includes Razavi's `-2` caveat. |
| 23 | `part1-023-common-gate-pmos-load` | OK | Correct common-gate NMOS with PMOS current-source load; input is at source side of `M2`. |
| 24 | `part1-024-many-poles-have` | OK | Correct two-pole count and corrects `CGS2` placement misconception. |
| 25 | `part1-025-series-nmos-effective-long-channel` | OK | Correct equivalent longer-channel interpretation for identical series NMOS devices. |
| 26 | `part1-026-source-follower-drives-common-gate` | OK | Correct source follower driving common-gate stage interpretation. |
| 27 | `part1-027-explain-why-output-impedance-be-inductive` | OK | Correct low-frequency `1/gm1`, high-frequency `RS` intuition for inductive-looking impedance. |
| 28 | `part1-028-current-input-positive-feedback` | OK | Correctly identifies positive feedback via `M2` gate tied to output, not diode connection. |
| 29 | `part1-029-feedback-transimpedance-amplifier` | OK | Corrects connections: `M1` common-gate input device, `M2` gate driven by node `X`, feedback through `RF`. |
| 30 | `part1-030-pmos-current-input-feedback` | OK | Correct PMOS/feedback-loop interpretation; not an NMOS cascode. |

## Part 2

| Q | Task | Status | Review note |
|---|---|---|---|
| 1 | `part2-001-fail-oscillate-three-capacitors-become-arbitrarily-large` | OK | Matches Razavi: all three equal capacitors slow the ring but do not by themselves stop oscillation. |
| 2 | `part2-002-phase-noise-three-capacitors-doubled` | OK | Correct factor-of-four, 6 dB reduction from halved `f0`. |
| 3 | `part2-003-fail-oscillate-cl-becomes-arbitrarily-large` | OK | Correct dominant-pole loop-gain failure for one large `CL`. |
| 4 | `part2-004-double-widths-nmos-and-pmos-devices-phase` | OK | Correct 3 dB phase-noise improvement by linear scaling/two-rings-in-parallel view. |
| 5 | `part2-005-determine-small-signal-resistance-seen-looking-into` | OK | Correct dynamic `RX ~= 1/(3 f0 CL)` supply resistance for oscillating ring. |
| 6 | `part2-006-oscillates-change` | Fixed | Reworded to avoid implying `RX` becomes much larger; correct result is `RX ~= 2 TD/CL ~= 2 Req`. |
| 7 | `part2-007-initial-voltage-gain-as-width-m7-increases` | OK | Matches Razavi: increasing `M7` current reduces initial voltage gain. |
| 8 | `part2-008-initial-voltage-gain-increase-capacitance-at-nodes` | OK | Correct: initial gain expression does not depend directly on `P/Q` capacitance. |
| 9 | `part2-009-increase-widths-m5-and-m6-speed-improve` | OK | Correct: speed improves initially until added capacitance dominates. |
| 10 | `part2-010-speed-improve-or-degrade-increase-widths-clocked` | OK | Correct initial speed improvement with clocked transistor sizing tradeoff. |
| 11 | `part2-011-structure-provide-quadrature-outputs` | OK | Correctly rejects ideal robust quadrature due `Inv3` skew and load mismatch. |
| 12 | `part2-012-repeat-question-10-for-topology` | OK | Correct: Figure 11 speed improves considerably; charge sharing acceptable over range. |
| 13 | `part2-013-dynamic-latch-divide-by-two` | OK | Correct dynamic-latch divide-by-two interpretation. |
| 14 | `part2-014-red-inverter-b-affect-performance` | OK | Correct feedforward-path explanation and low-clock-rate limitation. |
| 15 | `part2-015-but-input-red-inverter-not-tied-output` | OK | Correctly says not a keeper/cross-coupled inverter; it is feedforward. |
| 16 | `part2-016-optimize-for-nf-rin-must-remain-equal` | OK | Correctly notes channel-length modulation changes NF/matching relation and can allow `NF < 1 + gamma`. |
| 17 | `part2-017-compute-input-impedance` | OK | Correct exact Miller-theorem result `Rin = (RF + RD2)/(1 + A0)`. |
| 18 | `part2-018-ldo-regulator-generates-thermal-noise-with-spectrum` | OK | Correct supply-pushing conversion and notes `Kpush` relation to `KVCO`. |
| 19 | `part2-019-add-ct-tail-node-as-phase-noise` | OK | Correct nonmonotonic `CT` effect: flicker upconversion, class-C improvement range, large-`CT` instability. |
| 20 | `part2-020-estimate-oscillation-frequency` | OK | Corrects frequency shift to `Delta omega = alpha omega0/(2Q)` rather than bare `gmc/(2Cnode)`. |

## Files Changed During Review

- Fixed golden solutions: Part 1 Q5, Q9, Q10, Q11, Q12, Q17, Q18; Part 2 Q6.
- Added direct Sky130/ngspice netlists for Part 1 Q5, Q9, and Q10.
