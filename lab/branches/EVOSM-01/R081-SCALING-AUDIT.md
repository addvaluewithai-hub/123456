# R081 — EVOSM-01 whole-system scaling audit

Evidence state: analytical model anchored to published experimental large-area membrane performance; no new bench data.

## Bottleneck

The measured 1000 cm² device delivers 0.66 W/m², while the membrane itself is ~100 µm thick. At 10 W this simultaneously drives active area and solid membrane volume toward the entire 2 L package budget before fluid channels, electrodes, manifolds, or salinity inventory are added.

## Hypothesis / counter-hypothesis

Hypothesis: evaporation can continuously regenerate the salinity gradient, while a stacked ion-selective membrane cassette converts the gradient directly to electricity and avoids the large hydraulic throughput of a low-pressure PRO route.

Counter-hypothesis: large-area power-density collapse plus finite membrane thickness/module pitch makes a compact 10 W / 2 L device unattractive even if a distributed-area system remains physically valid.

## Measured anchors

Joule 2026 reports 8.5 W/m² at 1 cm² and 0.66 W/m² at 1000 cm², a 12.88× scale degradation. The NGO membrane fabrication section reports a typical ~100 µm thickness. The 1000 cm² performance point is the scale anchor; the 1 cm² record is not extrapolated.

## Geometry ledger at 10 W net, zero added parasitics

- Required membrane area at 0.66 W/m²: 15.15 m².
- Solid membrane volume at 100 µm thickness: 1.515 L, already 75.8% of a 2 L target.
- Absolute average repeat pitch if all 15.15 m² must fit in 2 L: 132 µm.
- After subtracting the 100 µm membrane itself, only 32 µm total remains for both solution channels, electrodes/current collection, spacers and structural separation. This is an absolute geometric budget, not a practical design recommendation.
- If an engineered cassette needs 0.50 mm average pitch, the 2 L package can contain only 4.0 m² active area and therefore needs 2.50 W/m², 3.79× the measured 1000 cm² density. At 1.0 mm pitch it needs 5.0 W/m², 7.58× measured. Even a 0.25 mm pitch needs 1.25 W/m², 1.89× measured.
- A 20% parasitic allowance raises gross required output to 12.5 W, membrane area to 18.94 m² and makes the geometric constraint correspondingly worse.

## External source / reset ledger

The energy source is the chemical-potential drop maintained by evaporation; salt is working inventory only if retained/recovered. Nature Communications 2017 gives an optimistic natural-evaporation resource bound up to 10.49 W/m² annual-average in favorable locations. Therefore even an ideal 10 W device needs >=0.953 m² external evaporation source area; this source footprint is separate from converter package volume.

At 25°C and 50% RH, the reversible vapor chemical-potential drop RT ln(1/RH) is ~95.38 kJ/kg (~26.49 Wh/kg). An ideal 10 W engine would therefore require at least ~0.377 kg/h water evaporation. This is a thermodynamic lower bound, not the Joule device's measured water rate.

At the measured 0.66 W/m² membrane density, electrical output is only 6.29% of the optimistic 10.49 W/m² evaporation resource density if membrane area and source footprint are forced one-for-one. A distributed architecture can decouple these areas by stacking membrane: the ideal area ratio at 10 W is ~15.9 m² membrane per m² of evaporation source.

Salt crossover, concentration polarization, channel pumping/circulation and electrode/contact losses remain unmeasured system terms and can only worsen the zero-parasitic geometry bound. They are not assigned fabricated values.

## Fair comparison to R019 hydraulic PRO

At 50 bar, ideal hydraulic specific work is ΔP/ρ≈5 kJ/kg. Producing 10 W hydraulically therefore requires ~7.2 kg/h permeate before pressure-exchanger/generator losses. Relative to the 50% RH vapor exergy bound (~95.38 kJ/kg), 50 bar captures only ~5.24% of the available specific water-vapor chemical exergy; the ideal water throughput is ~19.1× the reversible 10 W evaporation minimum. Thus the direct ion-selective route has a real source-throughput advantage in principle, while PRO retains advantages in mature hydraulic energy recovery and separation of membrane from electrical contacts. Neither comparison proves the Joule direct system's complete source-to-electric efficiency because its matched evaporation mass flow and regeneration losses were not available in the accessible primary text.

## Serious mutation: distributed evaporator + stacked membrane cassette

Compact 2 L is not the natural application. A more defensible architecture uses a ~1 m²-class external evaporation/regeneration surface with a separate many-square-meter membrane cassette and salinity reservoirs. This preserves the external source and day/night regeneration idea without forcing the evaporator into the 2 L converter volume. It remains useful only if matched measurements show that evaporation can maintain the gradient at the required salt/water flux and that pumping/crossover/contact parasitics do not erase the ~0.66 W/m² large-area output.

## Decision

Compact EVOSM-01: LOW PRIORITY. The 2 L target is already nearly consumed by 100 µm membrane solid at measured large-area power density. A minimally credible 0.5–1.0 mm module pitch demands ~3.8–7.6× higher large-area power density, while the published scale-up itself already lost 12.9× versus 1 cm². This is an engineering compactness failure, not a fundamental thermodynamic failure.

Distributed EVOSM: NEEDS DATA / preserve as niche branch. The external evaporation footprint lower bound is ~0.95 m² per 10 W under favorable resource conditions, but a stacked membrane/source-area ratio ~15.9 is geometrically conceivable when volume is relaxed. The decisive missing matched data are evaporation mass rate, salinity inventory/crossover and net auxiliaries at the 1000 cm² operating point.

No further compact-geometry optimization should be seeded without a measured large-area improvement or a substantially thinner membrane that preserves 0.66+ W/m² at scale.
