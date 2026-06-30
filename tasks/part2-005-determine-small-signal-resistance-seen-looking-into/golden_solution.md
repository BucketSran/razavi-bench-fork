# Golden Solution - part2-005-determine-small-signal-resistance-seen-looking-into

The resistance seen looking into the supply node of the oscillating ring is not simply the static resistance of diode-connected inverter devices. Oscillation matters because the supply current charges and discharges the three load capacitances each cycle.

Here, `CL` is the effective load capacitance at each internal oscillator node, and `f0` is the oscillation frequency. For a three-stage ring, the equivalent resistance is approximately

`RX ~= 1 / (3 f0 CL)`.

This can also be derived from power: `P = 3 f0 CL VDD^2 = VDD IDD`, so the incremental supply conductance is on the order of `3 f0 CL`.

Full-credit rule: give full credit only if the answer identifies the oscillation-driven dynamic charging/discharging mechanism and gives `RX ~= 1/(3 f0 CL)` or an equivalent charge-per-cycle or power derivation.

Low-credit rule: an answer that analyzes the metastable/static small-signal operating point and derives a `gm`-based resistance such as `(1/3)(1/gmp + 1/gmn)` or `2/(3gm)` is analyzing a different, non-oscillating operating condition. Even if that static derivation is internally consistent, it misses the dominant mechanism and should receive at most 1 point.
