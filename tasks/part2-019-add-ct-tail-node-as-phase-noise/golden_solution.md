# Golden Solution - part2-019-add-ct-tail-node-as-phase-noise

Adding `CT` to the tail node has a nonmonotonic effect on phase noise.

For small or moderate `CT`, the tail-node waveform changes and the flicker noise of `M1` and `M2` can be upconverted to phase noise unless the devices follow an ideal square law. For a certain range of `CT`, the cross-coupled devices enter class-C-like switching and deliver peak tank currents larger than `ISS`, which can lower phase noise. In that mode the large currents can also push `M1` and `M2` into the triode region.

If `CT` becomes too large, the oscillator can exhibit low-frequency instability. Thus `CT` is an optimization variable, not a guaranteed phase-noise improvement.
