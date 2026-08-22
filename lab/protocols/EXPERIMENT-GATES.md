# Experiment and Hardware Gates

## Evidence labels

Use these exact concepts in prose/artifacts:

- **PROPOSED** — geometry/instrumentation specified only.
- **SIMULATED** — model executed with explicit assumptions.
- **BENCH-MEASURED** — our physical apparatus produced calibrated data.
- **REPEATED** — our measurement repeated with stated reproducibility.
- **REPLICATED** — independent setup/operator/lab reproduces the decisive result.

Never describe PROPOSED/SIMULATED work as “tested” without qualification.

## Smallest decisive experiment

Prefer experiments that can kill or promote the mechanism without building the full product. Define before data collection:

- primary metric;
- pass/fail/inconclusive thresholds;
- calibration plan;
- uncertainty target;
- controls/baseline;
- data capture format;
- energy/source accounting;
- safety/pressure/temperature/electrical boundaries;
- repeat count.

## Current WET-01 gate

For EXP-WET-001, a clean promotion requires the calibrated 95% bounds to support `Re{G*}/V >= 108 kW m^-3 K^-1`, total physical phase preferably `<30°`, and wet dissipative loss `<2.3 W`, plus p-U vs p-V work agreement and heat-flow closure within stated uncertainty. A nominal value sitting on the threshold is `NEEDS DATA`, not a pass.
