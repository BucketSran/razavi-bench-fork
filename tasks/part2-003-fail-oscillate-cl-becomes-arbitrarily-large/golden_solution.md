# Golden Solution - part2-003-fail-oscillate-cl-becomes-arbitrarily-large

Yes. When a large capacitor is added to only one node, it creates a dominant pole that causes excessive gain roll-off around the loop.

For sufficiently large `CL`, the loop gain falls below unity at the phase-crossover frequency, so the Barkhausen condition is no longer satisfied and oscillation fails.
