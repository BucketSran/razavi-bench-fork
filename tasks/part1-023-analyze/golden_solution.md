# Golden Solution - part1-023-analyze

Figure 17 is a common-gate NMOS stage with a PMOS current-source load. The input `Vin` is applied at the source side of `M2`, while the gate of `M2` is biased by `Vb1`. `M1`, biased by `Vb2`, provides the PMOS load from `VDD`.

Because the input is at the source of `M2`, the stage is not a gate-driven common-source amplifier. A small increase in the source input tends to reduce `vgs2`, reducing the NMOS current and moving the output in the common-gate manner. The input resistance is low, on the order of `1/gm2`, and the voltage gain is set by `gm2` times the resistance seen at the output node.
