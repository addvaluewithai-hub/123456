# Research Portfolio

## 1 — WET-01: wet phase-change liquid-piston + direct linear alternator

Current verdict: **NEEDS DATA / waiting-hardware** after R079.

Why it remains #1: the branch has a concrete 10 W / <=2 L target, a frozen 0.25 mm / 5 Hz / ~10 bar experiment, deterministic R077 uncertainty gates, and a buildable R079 measurement packet. The remaining uncertainty is physical wet-interface conductance/phase/loss, not another geometry sweep.

Current rule: no new pore/frequency/metrology desk variants until EXP-WET-001 bench data arrive.

## 2 — TO-01: thermo-osmotic hydraulic conversion

Current verdict: **NEEDS DATA / waiting-hardware** after R076.

Why it remains #2: R075 showed an optimistic ~1.4 L 80/40°C package but a conservative ~4.2 L envelope; R076 reduced that gap to a matched 4-stage measurement contract. Further stage-count optimization before hardware would be lower-value than measurement.

Current rule: wait for EXP-TO-001 matched transport/heat-recovery/header-loss data.

## 3 — EVOSM-01: evaporation-maintained salinity-gradient direct electricity

Current verdict: **PROMISING for distributed/large-area harvesting; compactness unproven** after R080.

Why it reopens: a June 2026 Joule experiment reports 8.5 W/m² at 1 cm² and, more importantly, 0.66 W/m² at 1000 cm² with evaporation-maintained day/night osmotic generation. The 12.9× scale degradation is itself the decisive clue. At the measured large-area density, 10 W requires ~15.15 m² membrane; fitting that active area inside 2 L would require ~7,576 m²/m³ effective packing before fluid/evaporator hardware. Natural-evaporation resource modelling independently places favorable annual-average source power near ~10.49 W/m² of exposed water surface, implying ~0.95 m² source footprint even at an ideal 10 W conversion.

Current rule: run one fair system-level scaling audit using the measured large-area point. Compare direct osmotic electricity to R019's hydraulic PRO/pressure-recovery route under the same evaporation/salinity source. Do not extrapolate the 1 cm² record power density directly to module scale.

## 4 — MAG-01: magnetic force shaping / vibration conversion

Current verdict: **LOW PRIORITY / parked**.

Retain as a tool for commutation, impedance shaping, frequency up-conversion, coupling, or actuator design. Any advantage must use equal-resource source-work accounting against a strong baseline.

## Portfolio policy

Do not spend repeated shifts on hardware-blocked branches. Desk research may reopen an old family only when new external evidence changes a premise or when one reproducible model can close a decisive uncertainty. If EVOSM-01's system audit shows that compactness requires multiple simultaneous heroic improvements, the honest next state is an intentionally empty desk queue pending hardware rather than inventing a fourth branch.
