# Handoff

## Read first

1. `lab/STATE.md`
2. `lab/registry/queue.json`
3. `lab/tasks/T-TOEC-MODULE-CALIBRATION.md`
4. `lab/experiments/EXP-TO-001/README.md`
5. `src/energy_lab/toec.py`
6. `artifacts/r075-toec-sweep.csv`
7. `lab/runs/2026-08-22/R075-TOEC-SCALING-MODEL.md`

## Current bottleneck

R075 did not kill TO-01, but it exposed a wide module-level uncertainty band: optimistic 80/40°C packaging passes at ~1.40 L around N=16, while the conservative envelope is ~4.2 L. The decisive unknown is no longer stage-count algebra; it is measured loaded multi-stage transport, heat recovery, thermal-network compactness and header loss.

## Next recommended role

`experimentalist-metrologist`, with computational-modeler support.

## Exact next mission

Freeze a 2–4 stage instrumented module/calibration contract. Specify synchronized measurements for source heat, all stage temperatures, pressure rise/drop, loaded water flow, hydraulic output and heat recovery. Then invert the R075 model to state the measured thresholds for membrane packing, thermal-network W/L, recovery effectiveness and header loss required for a credible N≈16 <=2 L projection.

## Hard rules

- Do not build or optimize 38 stages yet.
- Do not use the 56.69 L m^-2 h^-1 single-stage measured flux as the loaded 38-stage flux.
- Keep modelled/published/bench evidence labels separate.
- If no defensible measurement can collapse the optimistic-vs-conservative gap, mark TO-01 hardware-blocked rather than generating more stage-count variants.

## Decision gate

Promote only if calibrated 2–4 stage measurements support >=10 W DC in <=2 L and >=15% Carnot preferred with uncertainty margin. Downgrade if measured compactness/heat recovery implies the conservative ~4.2 L envelope or worse.
