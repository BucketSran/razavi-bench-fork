# Golden Solution - part2-007-initial-voltage-gain-as-width-m7-increases

As the width of tail transistor `M7` increases, the initial voltage gain decreases.

A wider `M7` increases the tail current available during regeneration. In the StrongARM comparator relation cited by Razavi, the initial gain scales roughly like

`Av ~= gm1,2 VTHN / ICM`,

where `ICM` is tied to the current through `M7`. Since `gm1,2` grows more slowly than the current, increasing `M7` lowers the initial gain.
