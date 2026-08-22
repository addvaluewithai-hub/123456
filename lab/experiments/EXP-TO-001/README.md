# EXP-TO-001 — Multi-stage thermo-osmotic scaling and heat-recovery gate

Status: **SIMULATED / NEEDS MODULE DATA**
Branch: TO-01
Origin: R074; computational gate R075

## Question

Can a resistance-reduced, staged thermo-osmotic energy converter with explicit latent-heat recovery produce a credible path to ~10 W DC in <=2 L from a low-grade thermal gradient after real stage temperature drops and package parasitics are included?

## Evidence anchors

- Foundational thermo-osmotic pressure generation against substantial hydraulic back-pressure is experimentally established.
- Zhang et al. (Applied Energy 2025, DOI 10.1016/j.apenergy.2025.125740) report **56.69 L m^-2 h^-1 experimentally for a single-stage system**.
- The same paper reports **4.72% operational efficiency and 34.05 W/m² from a theoretical 38-stage 80/40°C model**. Those values are not our measurements and must not be combined as though they are the same loaded operating point.
- Li et al. (ACS AMI 2021, DOI 10.1021/acsami.1c03395) experimentally demonstrated a pump-free multistage architecture at 1.39±0.25 W/m² and modelled 30 stages at 2.72% / 14 W/m².
- Straub & Elimelech (ES&T 2017, DOI 10.1021/acs.est.7b02213) modelled an optimized 60/20°C system up to 4.1% absolute efficiency (~34% Carnot) and warned that high power density and finite heat exchangers reduce efficiency.
- Liu et al. (Water Research 2024, DOI 10.1016/j.watres.2024.121586) experimentally support in-situ latent-heat recovery in a neighboring hollow-fiber membrane-distillation architecture; it motivates heat recovery but does not validate a TOEC module.

## R075 computational audit

Reusable model: `src/energy_lab/toec.py`
Regression tests: `tests/test_toec.py`
Reference sweep: `artifacts/r075-toec-sweep.csv`
Cases: 60/20°C and 80/40°C; N=1/4/8/16/38; conservative and optimistic-but-defensible package screens.

The temperature span is partitioned across stages exactly once in the audit profile. The model then applies literature-anchored 38-stage efficiency/power-density envelopes plus explicit header loss, PTO, membrane-area density, per-stage overhead, thermal-network specific duty, parasitics and housing volume. Packaging numbers are deliberately labelled free screening assumptions rather than evidence.

### Decisive results

- **Optimistic 80/40°C passes the 10 W / 2 L gate for all tested stage counts.** The minimum projected package is at **N=16: ~1.40 L**, ~0.445 m² membrane, ~304 W source heat, ~3.29% electric efficiency = ~29% of Carnot. N=38 is slightly larger (~1.45 L) because added stage overhead outweighs the membrane/thermal savings.
- **Conservative 80/40°C fails compactness badly:** best case is ~4.18 L at N=38; N=16 is ~4.29 L. Efficiency itself still clears the 10–15% Carnot target at moderate/high N, so the dominant failure is **package compactness**, especially membrane-core area density plus thermal-network duty density, not a thermodynamic impossibility.
- **Optimistic 60/20°C is borderline:** N=16 ~1.99 L and N=38 ~1.95 L, leaving almost no packaging margin. Conservative cases are ~6–10 L.
- At conservative 80/40°C, N=16 needs roughly a **3.2× combined reduction** in membrane-core + thermal-network volume to fit the remaining 2 L envelope. This is the sharp design target.

### Anchor-consistency warning

A deliberately adversarial diagnostic shows why the 56.69 L m^-2 h^-1 measured single-stage flux cannot be naively multiplied into the 38-stage 34.05 W/m² / 4.72% model point. At ~2.358 MJ/kg latent heat, that flux corresponds to ~37.1 kW/m² latent transport, while 34.05/0.0472 implies only ~0.721 kW/m² source heat. Treating them as one operating point would imply ~98.06% latent-heat recovery, exceeding the simple ideal 38-effect value 97.37%. That is a normalization/operating-condition mismatch flag, not an energy anomaly.

## Current gate

Do **not** promote to HIGH PRIORITY from R075. The branch is conditionally viable but model-sensitive. The next decisive physical step is a **2–4 stage instrumented module**, not a 38-stage build. It must measure source heat, stage temperatures, loaded water flux/pressure, hydraulic output, heat recovery and header loss simultaneously. The key question is whether measured module data land closer to the optimistic compactness envelope or the conservative one.

Promotion requires a calibrated model whose 95% bounds still project >=10 W DC in <=2 L and >=15% of Carnot preferred, with no borrowed single-stage flux or hidden thermal recycle.
