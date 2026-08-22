# Current Lab State

Updated: 2026-08-22 11:42 Africa/Cairo (post-migration reconciliation)

## Published frontier

- Latest Sheet1 research run: **R074**
- Verdict: **PROMISING**
- Active desk-research branch: **TO-01 — thermo-osmotic hydraulic conversion**
- Hardware-waiting branch: **WET-01 — wet phase-change liquid-piston / wet thermoacoustic core + direct linear alternator**
- Magnetic/vibration shaping: **LOW PRIORITY** as a general energy architecture; retain for niche impedance/frequency shaping.

## What R074 changed

R074 used the explicit R073 fallback rule because no wet-coupon bench data existed. Newer evidence materially strengthened TO-01: a 2025 resistance-reduced thermo-osmotic energy-conversion study reported 56.69 L m^-2 h^-1 single-stage water flux experimentally and modelled a 38-stage 80/40°C system at 4.72% absolute operational efficiency and 34.05 W/m². A related 2024 heat-recovery membrane-distillation result motivates local latent-heat reuse. These are evidence anchors, not yet a compact-generator proof.

## Current decisive question

Does a complete multi-stage TOEC model—explicitly including per-stage temperature drop, conductive heat leak, condensation/vapour resistance, hydraulic pressure-flow, headers/separators, accumulator/PTO and package volume—still project >=10 W DC in <=2 L at >=10–15% of Carnot electric without unrealistically preserving source ΔT across many stages?

## WET-01 preserved gate

When hardware becomes available, WET-01 still requires approximately:

- 0.25 mm primary / 0.30 mm comparison;
- 5 Hz, ~10 bar, p-hat ~20/40 kPa, DRY→WET;
- 95% lower bound `Re{G*}/V >= 108 kW m^-3 K^-1`;
- total physical phase preferably `<30°`;
- 95% upper bound wet dissipative loss `<2.3 W`.

## Next task

`T-TOEC-SCALING-MODEL` — implement the R074 stage-by-stage scaling/heat-recovery/package model and make its assumptions and gates machine-readable.
