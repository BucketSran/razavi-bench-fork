# Golden Solution - part1-030-pmos-current-input-feedback

Figure 24 is a current-input feedback circuit using a common-gate NMOS input device and a PMOS feedback device. `M1` is an NMOS biased by `Vb`, with its source connected to the input/summing node and its drain connected to `Vout`. `M2` is the upper PMOS device connected to `VDD`, with its gate driven by `Vout` and its drain connected to the input/summing node.

The main signal path is `Iin -> input/summing node -> M1 -> Vout`: the input current perturbs the source of the common-gate NMOS `M1`, and this perturbation is transferred to the output node. The resulting `Vout` variation drives the gate of PMOS `M2`, whose drain current feeds back into the input-side node. The feedback loop is therefore `input/summing node -> M1 -> Vout -> M2 -> input/summing node`.

The key behavior is set by this two-node current-feedback loop, not by a two-PMOS interpretation. A correct small-signal analysis should write KCL at the input/summing node and at `Vout`, include the transconductance of the NMOS `M1` and the PMOS `M2`, and solve the closed-loop transimpedance from `Iin` to `Vout`.
