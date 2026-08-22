# Task: T-TOEC-MODULE-CALIBRATION

Branch: TO-01
Recommended role: experimentalist-metrologist
Priority: 100
Origin: R075

## Principal mission

Turn the R075 optimistic-vs-conservative package gap into a smallest decisive 2–4 stage measurement contract. The task is not to fabricate data or design 38 stages; it is to specify what must be measured and what numerical thresholds would validate a compact scale path.

## Read first

- `lab/STATE.md`
- `lab/experiments/EXP-TO-001/README.md`
- `src/energy_lab/toec.py`
- `artifacts/r075-toec-sweep.csv`
- `lab/runs/2026-08-22/R075-TOEC-SCALING-MODEL.md`
- `lab/protocols/EXPERIMENT-GATES.md`
- `lab/protocols/ENERGY-ACCOUNTING.md`

## Required outputs

1. Exact 2–4 stage topology and measurement points for hot/cold source heat, every stage temperature, loaded pressure/flow, hydraulic output, recovery heat and header loss.
2. Sensor bandwidth/accuracy and an uncertainty propagation sufficient to separate the ~1.4 L optimistic and ~4.2 L conservative envelopes.
3. Invert the R075 model to give pass/fail thresholds for: loaded hydraulic W/m², membrane area density, thermal-network W/L, stage/header dead volume, PTO efficiency and heat-recovery effectiveness.
4. A predeclared decision rule for whether TO-01 remains active, becomes hardware-blocked, or is downgraded.
5. No claim of BENCH-MEASURED until real data exist.

## Stop condition

Stop once one instrumented 2–4 stage experiment can decisively calibrate the compactness envelope. Do not create additional stage-count variants merely to fill a shift.
