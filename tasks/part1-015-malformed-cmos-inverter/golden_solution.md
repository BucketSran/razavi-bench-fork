# Golden Solution - part1-015-malformed-cmos-inverter

Figure 11(b) is not a proper CMOS inverter. Compared with the normal inverter in Figure 11(a), the device polarities/source-drain orientations are effectively swapped: the upper device is an NMOS connected to `VDD`, and the lower device is a PMOS connected to ground.

Although both gates are driven by `Vin`, the topology does not provide the standard PMOS pull-up to `VDD` and NMOS pull-down to ground. Around a bias point it may still exhibit a small-signal response because the two transconductances act in opposite directions at the output node. A useful small-signal form is therefore set by the difference of the device transconductances, for example proportional to `(gm2 - gm1) / (gm2 + 1/ro1 + 1/ro2)` under the simplified model.

The important point is that this small-signal response does not make the circuit a valid logic inverter. It does not provide the normal regenerative, rail-to-rail CMOS inverter transfer characteristic, and it should not be interpreted as a proper complementary pull-up/pull-down logic stage.
