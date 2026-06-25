# Golden Solution - part1-017-analyze

Figure 13 has a PMOS device on top and an NMOS device below, with the output at their common drain node. The input is applied to the PMOS gate, so the stage should be analyzed according to that actual signal path rather than by assuming both devices are NMOS.

The lower transistor provides the current-source/load function, while the upper PMOS is the signal device. The small-signal output is taken at the shared drain node, and the gain is set by the transconductance of the input device multiplied by the resistance seen at the output node.
