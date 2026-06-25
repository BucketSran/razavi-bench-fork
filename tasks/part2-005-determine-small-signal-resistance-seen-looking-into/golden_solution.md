# Golden Solution - part2-005-determine-small-signal-resistance-seen-looking-into

The resistance seen looking into the supply node of the oscillating ring is not simply the static resistance of diode-connected inverter devices. Oscillation matters because the supply current charges and discharges the three load capacitances each cycle.

For a three-stage ring with node capacitance `CL` and oscillation frequency `f0`, the equivalent resistance is approximately

`RX ~= 1 / (3 f0 CL)`.

This can also be derived from power: `P = 3 f0 CL VDD^2 = VDD IDD`, so the incremental supply conductance is on the order of `3 f0 CL`.
