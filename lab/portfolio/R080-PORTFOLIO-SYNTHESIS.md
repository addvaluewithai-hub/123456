# R080 Portfolio Synthesis

Evidence state: analytical/scaling + published experiment. No new bench measurements.

## Mission

Re-rank the lab after WET-01 and TO-01 both became honestly hardware-limited, and seed only a third branch whose decisive uncertainty can still be reduced by desk work.

## Bottleneck

The two strongest compact low-grade-heat branches now require physical measurements; continuing parameter sweeps would create false progress.

## Portfolio decision

1. **WET-01 — rank 1, NEEDS DATA, waiting-hardware.** Preserve R077/R079 gates exactly. The next decision-changing evidence is EXP-WET-001 bench data.
2. **TO-01 — rank 2, NEEDS DATA, waiting-hardware.** Preserve the R075/R076 matched 4-stage calibration gate. No more stage-count sweeps.
3. **EVOSM-01 — rank 3, PROMISING for distributed/large-area harvesting, not yet credible as a compact 10 W / 2 L converter.** Reopen the R019 evaporation-regenerated osmotic family in its stronger 2026 direct-electric form, because a June 2026 Joule experiment now demonstrates continuous day/night osmotic generation at large area rather than only a hydraulic-loop proposal.
4. **MAG-01 — rank 4, LOW PRIORITY / parked.** Keep only as a conversion/impedance-shaping tool.

## Why EVOSM-01 is worth exactly one desk audit

The June 17, 2026 Joule paper reports a 1 cm² single cell at 8.5 W/m² but, crucially, a 1000 cm² device at **0.66 W/m²** and a 400-unit series assembly reaching 100 V. This is published experimental evidence of the basic scalable salinity-to-electric conversion and of evaporation-maintained day/night operation, but it also exposes a 12.9× power-density scale-down from the tiny cell to the 0.1 m² device.

For a 10 W electrical target:

- at the demonstrated 1000 cm² scale density, membrane area required is `10/0.66 ≈ 15.15 m²`;
- if the 1 cm² record density survived scale-up, area would be `10/8.5 ≈ 1.18 m²`;
- therefore the existing experiment spans a **12.9× uncertainty in area requirement** before counting evaporator, saline reservoirs, boundary layers, wiring and regeneration.

If a compact converter had only 2 L total internal volume, the demonstrated 0.66 W/m² point would require effective membrane packing around `15.15/0.002 ≈ 7,576 m²/m³` before allocating any fluid channels or evaporator. At the small-cell 8.5 W/m² point the corresponding geometric requirement is ~588 m²/m³, which is physically plausible in high-area membrane modules but is not demonstrated at that power density. Thus the compactness question is not settled by either headline number.

A second independent bound comes from the real environmental source. Cavusoglu et al. modelled natural evaporation power availability up to ~10.49 W/m² annual average in the most favorable U.S. locations and up to ~15 W/m² in warm/dry instantaneous conditions. Even a reversible 10 W device would therefore require roughly **0.95 m²** of favorable evaporation footprint at the 10.49 W/m² resource bound; practical conversion requires more. That makes EVOSM-01 intrinsically more attractive as a distributed surface/roof/reservoir architecture than as a self-contained 2 L box unless it uses a concentrated external heat/solar evaporation source.

## Energy/source/reset ledger

- **Source:** chemical-potential gradient of a maintained salinity difference plus solar/ambient heat and unsaturated air that regenerate the concentrated stream through evaporation.
- **Power stroke:** ion transport through an ion-selective membrane generates electrical current/voltage.
- **Reset/regeneration:** water removal by evaporation restores concentration; salt is working inventory, not fuel, if retained.
- **Hidden costs:** concentration polarization, membrane resistance, saline hydraulic circulation, evaporator area, salt leakage/crossover, reservoir mixing, electrode/contact losses where applicable, and any powered pumping/fans.
- **Ceiling:** source exergy and evaporation/salinity free energy; neither membrane voltage nor series stacking creates energy.

## Counter-hypothesis

The 0.66 W/m² large-area result may already indicate that concentration polarization and ionic path resistance make compact volumetric power fundamentally unattractive at useful scale. Evaporation regeneration may further force square-metre source footprints, so the architecture could be valid but only as a low-power-density surface technology.

## Next decisive task

Seed exactly one task: `T-EVOSM-SCALING-AUDIT`. Build a matched system model from the 2026 measured large-area point, not the 1 cm² record. Close membrane packing, concentration polarization, salt/water inventory, evaporation area/flux, parasitic flow, and source exergy. Compare direct electrical osmotic conversion against the old R019 hydraulic PRO/pressure-recovery route under the same salinity and evaporation source. Kill compact EVOSM if a 10 W / 2 L package requires >3× improvement in more than one independent measured bottleneck; retain a distributed-area branch if source-to-electric areal performance is competitive even when compactness fails.

## Sources

- Joule 2026, *Natural evaporation-maintained scalable day-and-night osmotic power generation*, DOI: 10.1016/j.joule.2026.102359.
- Nature Communications 2017, *Potential for natural evaporation as a reliable renewable energy resource*, DOI: 10.1038/s41467-017-00581-w.
