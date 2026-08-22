# Model and Compute Validation

## Fidelity ladder

Use the lowest-fidelity model that can answer the current question, then promote only survivors:

`scaling -> closed-form -> reduced numerical -> sweep/Monte Carlo -> higher-fidelity multiphysics -> bench`.

## Reproducibility record

For any result materially affecting a verdict, record:

- Git commit SHA;
- code/module and config;
- command/workflow used;
- units and parameter sources;
- random seed when stochastic;
- output artifact path/hash when available;
- invariant/regression checks;
- sensitivity/uncertainty around dominant assumptions.

## Scientific regression tests

Tests should encode invariants, not desired conclusions. Examples: Carnot bound sanity, unit consistency, closed-cycle energy closure, zero-source limiting behavior, monotonic limiting cases, agreement of two independent methods, and reproduction of previously accepted benchmark numbers within tolerance.

A surprising positive result that disappears with tighter tolerances, reverse-path integration, independent energy method, or convergence is a numerical artifact until proven otherwise.

## Optimization

Do not optimize against a loophole in the objective. Include reset/control/source work and constraints. Report the best baseline under the same resource budget. Keep training/calibration data separate from final validation data when fitted models are used.
