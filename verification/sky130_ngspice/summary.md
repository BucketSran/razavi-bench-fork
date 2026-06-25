# Sky130 ngspice Verification Summary

Model: volare `sky130A`, version `c6d73a35f524070e85faff4a6a9eef49553ebc2b`, TT corner, via:

```spice
.lib sources/sky130/volare/volare/sky130/versions/c6d73a35f524070e85faff4a6a9eef49553ebc2b/sky130A/libs.tech/ngspice/sky130.lib.spice tt
```

These simulations are representative checks of device and circuit trends used by the golden solutions. They do not prove all 50 tasks one by one because many tasks omit concrete sizing, bias currents, supplies, and load values, and several are topology/feedback-recognition questions.

## 01_mos_gain_length

Netlist: `verification/sky130_ngspice/01_mos_gain_length.cir`

```text
gm_short   = 4.547594e-04
gds_short  = 2.102947e-05
gain_short = 2.162487e+01
gm_long    = 5.083926e-04
gds_long   = 6.097476e-06
gain_long  = 8.337756e+01
```

Result: doubling both width and length increased intrinsic gain from about 21.6 to 83.4 in this Sky130 bias example. This supports the Part 1 Q1 trend that increasing length improves `ro` and intrinsic gain when the operating point is comparable.

## 02_source_follower_tf

Netlist: `verification/sky130_ngspice/02_source_follower_tf.cir`

```text
transfer_function = 6.838461e-01
output_impedance_at_v(out) = 2.015856e+03
vin#input_impedance = 1.000000e+20
```

Result: the source follower has positive gain below unity, supporting the source-follower golden solutions.

## 03_common_source_tf

Netlist: `verification/sky130_ngspice/03_common_source_tf.cir`

```text
transfer_function = -5.03422e+00
output_impedance_at_v(out) = 1.401314e+04
vin#input_impedance = 1.000000e+20
```

Result: the common-source stage is inverting, supporting the common-source polarity/gain statements.

## 05_ring_cl_5f and 05_ring_cl_20f

Netlists: `verification/sky130_ngspice/05_ring_cl_5f.cir`, `verification/sky130_ngspice/05_ring_cl_20f.cir`

```text
CL = 5 fF:  freq = 4.826423e+09 Hz
CL = 20 fF: freq = 2.115587e+09 Hz
```

Result: increasing all three ring-oscillator load capacitors lowers oscillation frequency, supporting the Part 2 ring-oscillator trend questions.

## 06_q5_ix_vs_vx

Netlist: `verification/sky130_ngspice/06_q5_ix_vs_vx.cir`

```text
v(g)=0.0 V: ix = 1.08e-12 A
v(g)=0.7 V: ix = 4.10e-06 A
v(g)=1.0 V: ix = 8.94e-05 A
v(g)=1.4 V: ix = 3.16e-04 A
v(g)=1.8 V: ix = 5.64e-04 A
```

Result: with the drain fixed at 1 V and the gate swept by `VX`, the current is near zero below threshold, rises rapidly after turn-on, and becomes roughly linear at high `VX` when the fixed `VDS` limits the device. This supports the corrected Part 1 Q5 segmentation.

## 07_q9_common_gate_tf

Netlist: `verification/sky130_ngspice/07_q9_common_gate_tf.cir`

```text
transfer_function = 3.011505e-01
output_impedance_at_v(out) = 9.904225e+03
vin#input_impedance = 3.320678e+04
```

Result: a source-driven, gate-biased NMOS stage has a positive small-signal transfer from source input to drain output under this Sky130 bias point. This supports the corrected Part 1 Q9 common-gate interpretation and sign.

## 08_q10_shorted_source_ac

Netlist: `verification/sky130_ngspice/08_q10_shorted_source_ac.cir`

```text
frequency = 1.0e+03 Hz: vm(out) = 0
frequency = 1.0e+04 Hz: vm(out) = 0
frequency = 1.0e+05 Hz: vm(out) = 0
frequency = 1.0e+06 Hz: vm(out) = 0
```

Result: when the input capacitor is connected to a node that is also an ideal ground short, no small-signal output is produced. This supports the corrected Part 1 Q10 answer.

## Inconclusive / Not Used as Proof

A cascode output-resistance check was attempted, but without the original problem's exact device sizes and bias conditions the operating point is highly bias-sensitive. The available run is therefore not used as evidence for the golden solutions. Those tasks should remain analytical/topological unless explicit sizing and bias specifications are added.

## Coverage Map

- MOS `gm`, `gds`, and intrinsic-gain trends: supports Part 1 Q1-Q2.
- Source follower / common-source polarity and gain: supports Part 1 Q7-Q10, Q13, Q23, Q26.
- Direct corrected-case checks: supports Part 1 Q5, Q9, and Q10.
- Ring oscillator capacitance/frequency trend: supports Part 2 Q1-Q3 and parts of Q5-Q6.
- Divider, LNA, TIA, LC oscillator, and detailed feedback questions require topology-specific analytical review unless full sizing/bias specifications are added.
