# Golden Solution - part1-009-analyze

Figure 6 is not a normal common-source amplifier because the source of `M1` is tied to `VDD`, which is ac ground. For small signals the source is fixed, while the input is applied to the gate and the output is at the drain through `RD`.

The circuit behaves as a common-source stage only if the device polarity and biasing are consistent with the supply connection. With the shown PMOS-style source-to-`VDD` connection, it should be treated as a PMOS common-source device. The small-signal gain is inverting, approximately `-gm RD` when `ro` is neglected.

The key point is that the device type and source connection must be read from the symbol and supply connection; treating it as an NMOS common-source stage is wrong.
