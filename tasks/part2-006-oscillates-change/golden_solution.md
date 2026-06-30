# Golden Solution - part2-006-oscillates-change

Considering the oscillation does change the mechanism: `RX` is set by dynamic charging and discharging of the oscillator nodes, not by the static resistance of diode-connected inverter devices.

Here, `CL` is the effective load capacitance at each internal oscillator node, `f0` is the oscillation frequency, and `TD` is the delay of one inverter stage. From the dynamic-power result,

`RX ~= 1/(3 f0 CL)`.

Using `f0 = 1/(6 TD)` for a three-stage ring, this can also be written as

`RX ~= 2 TD / CL`.

Since the delay `TD` is roughly `Req CL`, this gives `RX` on the order of the MOS on-resistance or inverse transconductance. Thus the static diode-connected answer is not the correct derivation or primary expression, but the dynamic result is not much larger merely because individual devices are off for part of the cycle.

Full-credit rule: a correct answer should disagree with the static diode-connected derivation, explain that oscillation-driven charging/discharging of `CL` sets the effective supply resistance, and give `RX ~= 1/(3 f0 CL)` or equivalently `RX ~= 2 TD/CL` with `f0 = 1/(6 TD)`.
