# Golden Solution - part2-006-oscillates-change

Considering the oscillation does not make `RX` much larger. The effective resistance is set by the dynamic charging and discharging of the oscillator nodes, not by a dc path that is mostly off.

Using `f0 = 1/(6 TD)` for a three-stage ring, the equivalent supply resistance can be written approximately as

`RX ~= 2 TD / CL`.

Since the delay `TD` is roughly `Req CL`, this gives `RX` on the order of the MOS on-resistance or inverse transconductance. It is not much larger merely because individual devices are off for part of the cycle.
