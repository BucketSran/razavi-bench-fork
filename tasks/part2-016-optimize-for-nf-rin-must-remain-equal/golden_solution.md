# Golden Solution - part2-016-optimize-for-nf-rin-must-remain-equal

The circuit should be optimized by using channel-length modulation and feedback together, not by simply making the load resistance as large as possible.

With `Rin` constrained to 50 ohm, the design variables must be chosen so that the input match is maintained while the noise contribution of the active devices and feedback network is minimized. Razavi notes that channel-length modulation changes the relation between `Rin` and noise factor, making it possible to obtain `NF < 1 + gamma`. Thus the optimum is not the limiting case of very large output resistance and `NF = 1 + gamma`; it requires finite output resistance/device sizing chosen jointly with `RF` and transconductance.
