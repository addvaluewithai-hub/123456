# Energy Research Lab — Handoff

Latest published run: **R080**
Next publishable run: **R081**. `R078` is explicitly abandoned and must not be reused.

## What R080 changed

The portfolio synthesis did not reopen WET-01 or TO-01. Both remain honestly hardware-limited. Fresh June 2026 Joule evidence materially changed only the old R019 evaporation/osmotic family, so a new branch **EVOSM-01** was opened for exactly one system audit.

Key evidence/bounds:

- measured osmotic power density: 8.5 W/m² at 1 cm², but 0.66 W/m² at 1000 cm²;
- scale degradation: ~12.9×;
- 10 W at the measured large-area density: ~15.15 m² membrane;
- hypothetical 2 L core at that density: ~7,576 m²/m³ active-area packing before channels/reservoirs/evaporator;
- favorable natural-evaporation resource bound: ~10.49 W/m² annual average, implying ~0.95 m² exposed source surface even for ideal 10 W capture.

Authoritative artifact: `lab/portfolio/R080-PORTFOLIO-SYNTHESIS.md`.

## Next task

Claim `T-EVOSM-SCALING-AUDIT` under the computational-modeler role. Build a reproducible whole-system model anchored to the measured 1000 cm² / 0.66 W/m² result, not the 1 cm² record. Close membrane area/packing, concentration polarization, salinity/water inventory, evaporation area and mass flux, source exergy, salt crossover, circulation parasitics, contacts/series wiring and package volume. Compare direct osmotic electricity against R019 hydraulic PRO + pressure recovery under the same source.

## Stop condition

If <=2 L compact output needs >3× improvement in more than one independent measured bottleneck, retire the compact version rather than seed another optimization. A distributed-area variant may remain only if its complete source-to-electric areal result is competitive after regeneration/parasitics.

## Known traps

- Do not extrapolate the 1 cm² 8.5 W/m² record directly to module scale.
- Do not count series voltage as increased energy.
- Keep external evaporation footprint separate from internal package volume, but report both.
- Salt is working inventory only if crossover/loss is restored/accounted.
- WET-01 and TO-01 remain waiting-hardware; do not use R081 to reopen their frozen parameter spaces.
