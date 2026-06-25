# Golden Solution - part1-005-sketch-ix-versus-vx

The gate is held at 1 V and the source is grounded, so `VGS = 1 V` is fixed. The drain voltage is `VX`.

For `VX` below the threshold for conduction, `IX` is approximately zero. Once the device conducts, it first operates in the triode region and `IX` increases roughly linearly for small `VX`. When `VX >= VGS - VTH = 1 V - VTH`, the device enters saturation and `IX` approaches the saturation current

`ID ~= (1/2) mu Cox (W/L) (1 V - VTH)^2`.

With channel-length modulation, the saturation-region current has a small positive slope.
