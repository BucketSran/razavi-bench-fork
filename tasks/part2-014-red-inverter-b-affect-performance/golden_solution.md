# Golden Solution - part2-014-red-inverter-b-affect-performance

The red inverter creates a feedforward path around the first latch. This feedforward path improves divider speed because part of the signal can bypass the main latch path.

It is not simply a keeper or a cross-coupled latch with `Inv1`. At low clock frequencies, the unclocked feedforward branch can dominate the main path, so it raises the lower bound on the clock frequency that the divider can handle.
