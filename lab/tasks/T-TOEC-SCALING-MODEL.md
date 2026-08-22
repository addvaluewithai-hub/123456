# Task: T-TOEC-SCALING-MODEL

Branch: TO-01
Recommended role: computational-modeler
Priority: 100
Origin: R074

## Principal mission

Turn the strengthened thermo-osmotic evidence from R074 into a complete, reproducible multi-stage source-to-electric scaling model. The model must decide whether membrane-level promise survives realistic thermal staging and package overhead.

## Read first

- `lab/STATE.md`
- `lab/experiments/EXP-TO-001/README.md`
- `lab/protocols/ENERGY-ACCOUNTING.md`
- `lab/protocols/MODEL-VALIDATION.md`
- `lab/portfolio/PORTFOLIO.md`

## Mandatory cases

- source temperatures: 60/20°C and 80/40°C;
- stages N = 1, 4, 8, 16, 38;
- transport anchor: measured single-stage flux reported in the R074 evidence, used only inside its defensible operating range;
- 34.05 W/m² / 4.72% at 80/40°C, 38 stages is a **published modelled benchmark**, not our measured result and not a universal constant.

## State variables and losses to track

1. source hot/cold temperatures and heat input;
2. stage inlet/outlet temperatures and available ΔT;
3. membrane area and transport law/uncertainty;
4. thermo-osmotic hydraulic pressure-flow power;
5. vapor/condensation resistance and non-condensables where represented;
6. conductive heat leak through membrane/support/network;
7. inter-stage latent/sensible heat-recovery effectiveness;
8. manifolds/headers/separators and pressure loss;
9. accumulator/hydraulic-to-electric PTO efficiency;
10. active and balance-of-module volume;
11. electric output, W/L, absolute efficiency and fraction of Carnot.

## Required model discipline

- implement a conservative baseline and an optimistic-but-defensible scenario rather than one tuned answer;
- identify which assumptions are measured, literature-modelled, inferred, or free design variables;
- enforce energy balance and Carnot sanity as tests;
- do not let every stage see the full source ΔT unless a real heat-routing topology justifies it;
- compare against a fair direct converter / simpler thermal architecture where enough data exist;
- perform sensitivity on the few parameters that dominate the pass/fail boundary.

## Binary decision gate

A path is genuinely interesting only if a realistic stage count can project >=10 W DC in <=2 L at >=10–15% of Carnot electric with a credible thermal profile and no omitted source/reset/parasitic term. If it misses, report the exact term that kills it and whether one serious nearby mutation could attack that term.

## Durable output

Add reusable TOEC model/config code under `src/energy_lab/`, regression tests, and a deterministic JSON/CSV reference artifact path documented in the run log. Any result affecting the verdict must name the Git commit/config/command that produced it.
