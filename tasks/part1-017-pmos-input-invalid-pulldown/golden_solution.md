# Golden Solution - part1-017-pmos-input-invalid-pulldown

Figure 13 has a PMOS device `M2` on top and an NMOS device `M1` below. The input `Vin` is applied to the gate of `M2`, and the output is the common drain node.

The lower NMOS is not a diode-connected load and should not be treated as a second stacked NMOS. As drawn, the gate and source of `M1` are tied to ground, so `M1` is not a proper biased current-source load for an analog gain stage.

The only intentional signal transconductance is from the PMOS `M2`. A decrease in `Vin` turns `M2` on harder and tends to pull `Vout` upward; an increase in `Vin` weakens the pull-up. Without a valid pull-down bias device, however, the circuit is not a normal common-source amplifier with active load.
