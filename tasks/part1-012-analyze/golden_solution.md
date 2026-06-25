# Golden Solution - part1-012-analyze

Figure 9 is a common-source amplifier with resistive feedback from the output to the input/gate node through the `R1`-`R2` network.

The output is taken at the drain through `RD`, so the intrinsic stage is inverting. The feedback samples the output voltage and returns a fraction to the input node, producing negative feedback for the appropriate bias polarity. This reduces gain, improves linearity, and changes the input/output resistances compared with an open-loop common-source stage.

The source of `M1` is not grounded in the feedback sense by the divider; the important point is the feedback path from `vout` to the gate/input node.
