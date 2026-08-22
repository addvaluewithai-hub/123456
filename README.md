# Energy Research Lab

Computational notebook/codebase for the ongoing energy-conversion research program.

## Current branch: R073 wet phase-change coupon

The active candidate is a pressurized wet phase-change liquid-piston / thermoacoustic core coupled to a direct linear alternator.

Frozen first test point:

- hydraulic radius: ~0.25 mm
- frequency: ~5 Hz
- mean pressure: ~10 bar
- source temperature span: ~293 K -> 333 K
- dynamic pressure cases: ~20 and 40 kPa

### Promotion gate

The concept is not considered validated unless a calibrated DRY -> WET coupon can support all of the following simultaneously:

- Re{G*}/V >= 108 kW m^-3 K^-1
- total thermal/mass-transfer phase lag preferably < 30 deg
- wet dissipative acoustic loss < 2.3 W
- complete projection: >=10 W DC in <=2 L

The repository exists to make every calculation reproducible, run parameter sweeps/uncertainty tests, and later ingest real sensor data. Simulation is not treated as experimental proof.

## Planned structure

- `src/energy_lab/` — physics models and energy ledger
- `scripts/` — parameter sweeps and R0xx analyses
- `tests/` — conservation/regression tests
- `.github/workflows/` — automated CI checks
- `results/` — machine-readable outputs from each research run

## Rule

Every apparent gain must close the full energy ledger. Resonance, magnets, pressure, capillarity, geometry, and control are conversion mechanisms—not untracked energy sources.
