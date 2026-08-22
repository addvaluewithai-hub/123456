# EXP-TO-001 — Multi-stage thermo-osmotic scaling and heat-recovery gate

Status: **PROPOSED / COMPUTATIONAL FIRST**
Branch: TO-01
Origin: R074

## Question

Can a resistance-reduced, staged thermo-osmotic energy converter with explicit latent-heat recovery produce a credible path to ~10 W DC in <=2 L from a low-grade thermal gradient after real stage temperature drops and package parasitics are included?

## Evidence anchors from R074

- Foundational thermo-osmotic pressure generation against substantial hydraulic back-pressure is experimentally established.
- R074 cites a 2025 Applied Energy study reporting 56.69 L m^-2 h^-1 single-stage water flux experimentally after attacking liquid-side and transmembrane resistance.
- The same work modelled a 38-stage 80/40°C system at 4.72% absolute operational efficiency and 34.05 W/m². Treat these as **published model outputs**, not bench-measured compact-module output.
- A related 2024 hollow-fiber membrane-distillation experiment showed that local condensation-to-evaporation heat recovery can materially raise flux/GOR in a neighboring process, motivating but not proving the TOEC heat-recovery mutation.

## Computational sweep

Temperatures: 60/20°C and 80/40°C.
Stages: 1, 4, 8, 16, 38.
Scenarios: conservative + optimistic-but-defensible.

Track: stage ΔT, heat/recovery flows, transport, hydraulic pressure/flow, conductive and pressure losses, membrane area, header/separator/thermal-network volume, accumulator/PTO efficiency, electric power, W/L, absolute efficiency, Carnot fraction.

## Predeclared gate

`PROMISING -> co-leading/HIGH PRIORITY` only if a realistic staged configuration projects >=10 W DC in <=2 L and >=10–15% of Carnot electric without assigning full source ΔT independently to every stage or omitting balance-of-module losses.

If modelled performance is attractive, the next physical experiment should be a 2–4 stage instrumented module, not a 38-stage build. Bench promotion requires measured heat input and hydraulic/electric output with complete thermal/hydraulic state accounting.

## Evidence state

Current: published experiments + published modelling + our proposed computational model. No `BENCH-MEASURED` data from our lab exists.
