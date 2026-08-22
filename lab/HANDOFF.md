# Handoff

## Read first

1. `lab/STATE.md`
2. `lab/registry/queue.json`
3. `lab/tasks/T-TOEC-SCALING-MODEL.md`
4. `lab/experiments/EXP-TO-001/README.md`
5. `lab/protocols/ENERGY-ACCOUNTING.md`
6. `lab/protocols/MODEL-VALIDATION.md`
7. `lab/portfolio/PORTFOLIO.md`

## Current bottleneck

TO-01 now has enough evidence to justify quantitative modelling, but its strongest number (34.05 W/m² at 80/40°C, 38 stages) is a modelled membrane/system benchmark, not a measured compact module. The risk is that preserved ΔT, heat-recovery effectiveness, conductive leak, headers, stage hardware and PTO erase the membrane-level promise.

## Next recommended role

`computational-modeler`, with theoretical-thermo and systems-packaging checks.

## Exact next mission

Build and validate a first complete multi-stage TOEC scaling model for 60/20°C and 80/40°C with N=1/4/8/16/38. Explicitly track source heat, per-stage ΔT, transport, pressure-flow work, heat recovery, conductive/parasitic heat, area, structural/header volume, accumulator/PTO efficiency, and final W/L. Anchor transport to measured data where legitimate and keep the 34.05 W/m² result labelled as a modelled upper benchmark.

## Decision gate

Promote/co-lead only if a realistic stage count can project >=10 W DC in <=2 L at >=10–15% of Carnot electric with a credible thermal profile and no hidden source/reset term. Otherwise identify the exact stage/packaging/heat-recovery term that closes the opportunity.

## Preserve WET-01

Do not delete or rewrite the wet-coupon work. It is waiting for hardware-quality evidence. The metrology-code task remains useful but is lower desk priority than the R074 TOEC question.
