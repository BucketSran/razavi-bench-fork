# Golden Solution - part2-017-compute-input-impedance

Use the simplified model in Figure 14(b) and apply Miller's theorem to the feedback resistor.

The exact input resistance is

`Rin = (RF + RD2) / (1 + A0)`

where the unloaded gain is

`A0 = (1/2) gm1 gm2,3 RD1 RD2`.

This expression is preferable to a generic shunt-shunt feedback formula because it follows the actual two-stage model and includes the resistance at the output side of the feedback path.

A complete answer should reject the generic `RF/(1 + Avol)` expression and give the exact Miller-theorem result `Rin = (RF + RD2)/(1 + A0)`, with `A0 = (1/2) gm1 gm2,3 RD1 RD2` or an equivalent unloaded-gain definition.

An answer that only identifies the circuit as shunt-shunt feedback and writes `Rin = RF/(1 + Avol)` misses the exact resistance at the output side of the feedback path.
