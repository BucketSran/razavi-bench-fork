# Golden Solution - part2-018-ldo-regulator-generates-thermal-noise-with-spectrum

The LDO output noise modulates the VCO frequency through the supply-pushing gain. First determine the pushing gain

`Kpush = d fosc / d Vout`

usually by simulation or perturbation analysis. Then convert the LDO noise spectrum `Sth` to phase noise through frequency modulation. In the notation of the article, the single-sideband phase noise is proportional to

`L(Delta f) ~= 10 log10( Kpush^2 Sth / (2 Delta f^2) )`.

Because the supply perturbation appears directly on the varactors in this circuit, `Kpush` is closely related to `KVCO`. A design with lower `KVCO` also reduces this supply-noise-to-phase-noise conversion.
