# Golden Solution - part2-011-structure-provide-quadrature-outputs

The structure does not provide ideal quadrature outputs in a robust sense.

The internal nodes can appear phase-shifted, but the delay through `Inv3` skews node `Z`. Also, the two latches do not necessarily see equal load capacitances. For example, the gate-drain capacitances in `Inv3` experience Miller multiplication, while the corresponding capacitances in the secondary latch do not. These asymmetries prevent accurate quadrature over process and loading variations.
