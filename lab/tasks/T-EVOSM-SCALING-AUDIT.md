# T-EVOSM-SCALING-AUDIT

Branch: EVOSM-01
Recommended role: computational-modeler + research-lead-falsifier

## Mission

Build the first fair system-level scaling audit of evaporation-maintained salinity-gradient direct electricity using the June 2026 **measured 1000 cm² / 0.66 W/m²** point as the primary scale anchor, not the 1 cm² / 8.5 W/m² record.

## Read first

- `lab/portfolio/R080-PORTFOLIO-SYNTHESIS.md`
- R019 row in Sheet1
- Joule 2026 DOI 10.1016/j.joule.2026.102359
- Nature Communications 2017 DOI 10.1038/s41467-017-00581-w

## Required model ledger

Track membrane active area and packing, measured size-dependent power density, concentration polarization, salinity/water inventory, evaporation regeneration area and mass flux, source exergy, salt crossover, hydraulic/circulation parasitics, electrical contacts/series wiring, and package volume. Compare direct osmotic electricity against the R019 hydraulic PRO + pressure-recovery architecture under the same salinity and evaporation source.

## Quantitative starting bounds

- 10 W at 0.66 W/m² requires ~15.15 m² membrane.
- 10 W at 8.5 W/m² would require ~1.18 m², but that density is only demonstrated at 1 cm².
- 2 L package at the measured large-area density implies ~7,576 m²/m³ effective active-area density before fluid hardware.
- favorable natural-evaporation source bound ~10.49 W/m² annual average implies ~0.95 m² exposed source surface for 10 W even before conversion losses.

## Success/falsification test

Produce a reproducible envelope for 10 W DC showing membrane area, source/evaporator footprint, volume, salinity inventory and source-to-electric efficiency. Compact EVOSM is downgraded if <=2 L needs >3× improvement in more than one independent measured bottleneck (for example both scaled membrane power density and effective packing/transport). A distributed-area branch may remain promising even if compactness fails, but only if whole-source areal output remains competitive after regeneration/parasitics.
