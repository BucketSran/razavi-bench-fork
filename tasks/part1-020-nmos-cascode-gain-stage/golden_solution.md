# Golden Solution - part1-020-nmos-cascode-gain-stage

Figure 15 is an NMOS cascode gain stage. `M1` is the input common-source transistor, `M2` is the common-gate cascode transistor biased by `Vb1`, and `I1` is the load current source at the output.

A change in `vin` changes the drain current of `M1`; `M2` conveys this current to the output while holding node `X` relatively quiet. The output is therefore an inverted voltage at the drain of `M2`.

The small-signal gain is approximately

`Av ~= -gm1 Rout`

where `Rout` is the resistance seen at the output, including the current-source load and the boosted resistance of the cascoded NMOS stack. The circuit should not be described as a common-source stage with a PMOS active load; `M2` is an NMOS cascode device.
