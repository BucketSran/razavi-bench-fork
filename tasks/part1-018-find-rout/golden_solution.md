# Golden Solution - part1-018-find-rout

Figure 14 is a PMOS cascode-style current-source stack. The output resistance is found by applying a test signal at the indicated output node and using the small-signal model of the stacked devices.

For a cascoded current source, the resistance is boosted by the gain of the cascode device. To first order,

`Rout ~= ro1 + ro2 + gm2 ro1 ro2`

for the usual notation in which the cascode device contributes the gain boost. If `gm2 ro2 >> 1`, this is approximately `gm2 ro1 ro2`.

The key is that `M2` is the PMOS cascode device and the output resistance is much larger than either individual `ro`.
