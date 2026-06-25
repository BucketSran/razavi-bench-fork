# Golden Solution - part2-020-estimate-oscillation-frequency

Start from the tank resonance

`omega0 = 1 / sqrt(L Cnode)`.

The coupling shifts the oscillation frequency away from resonance. The shift is

`Delta omega = alpha omega0 / (2 Q)`

where `alpha` is the coupling coefficient. In a typical large-signal design with nearly complete switching,

`alpha ~= I1 / ISS`,

so

`Delta omega ~= (I1 / ISS) omega0 / (2 Q)`.

For a small-signal estimate, `alpha ~= gmc/gm1`, giving

`Delta omega ~= (gmc/gm1) omega0/(2Q) = (gmc/gm1) / (2 Cnode Rp)`.

Thus the oscillation frequency is approximately `omegaosc = omega0 + Delta omega` with the sign determined by the coupling orientation. It is incorrect to use only `gmc/(2 Cnode)` unless the oscillator is assumed to be exactly at the edge of oscillation.
