# Task: T-WET-METROLOGY-CODE

Branch: WET-01
Recommended role: computational-modeler
Priority: 100

## Principal mission

Turn the R073 phase-calibrated measurement logic into a reproducible computational experiment and machine-readable gate, so later hardware traces can be evaluated without changing the success criteria after seeing the data.

## Read first

- `lab/STATE.md`
- `lab/experiments/EXP-WET-001/README.md`
- `src/energy_lab/wet_core.py`
- `lab/protocols/MODEL-VALIDATION.md`
- `lab/protocols/EXPERIMENT-GATES.md`

## Required work

1. Preserve/reproduce the 0.25 mm / 5 Hz / 10 bar intrinsic diffusion benchmark and 0.30 mm comparison.
2. Implement explicit propagation of amplitude + phase measurement uncertainty into `Re{G*}`.
3. Implement pass / inconclusive / fail classification using predeclared thresholds and 95% intervals.
4. Define a JSON input/output contract for future hardware summaries; do not fabricate raw traces.
5. Add regression tests for threshold behavior and physical limiting cases.
6. Produce one deterministic reference snapshot artifact or workflow artifact.

## Success test

A fresh checkout can run the model/tests and reproduce the gate without chat context. The code must make it impossible to call a nominal near-threshold value a clean PASS when its 95% lower/upper bounds cross the gate.

## Stop condition

If the model/measurement contract is complete, do not create another geometry task. Hand off to the hardware packet; after that, WET-01 should wait for bench data while desk research moves to TO-01.
