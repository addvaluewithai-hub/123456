# R079 — WET hardware packet shift

- Run: R079
- Shift: shift-20260822-1725-wetpkt
- Task: T-WET-HARDWARE-PACKET
- Branch: WET-01
- Role: experimentalist-metrologist
- Time: 2026-08-22 17:25–17:47 Africa/Cairo
- State before: WET-01 active desk / NEEDS DATA; R077 digital classifier frozen
- Principal mission: convert the frozen 0.25 mm / 5 Hz / 10 bar coupon into a buildable, phase-calibrated measurement contract without inventing bench data
- Success test: exact sensor/geometry/calibration/BOM-level contract frozen, risks explicit, then mark branch waiting-hardware

## Files read

`lab/RUNNER.md`, lab charter/OS/protocols, queue/counter/branches/state/handoff, role catalog, `EXP-WET-001/README.md`, `R077-DIGITAL-GATE.md`, accepted decisions, and latest Sheet1 ledger through R077.

## Bottleneck

The physics gate is already digital and predeclared; the last desk uncertainty is whether a real apparatus can measure dynamic pressure, flow/displacement, thermal phase, heat rates and wet loss with enough phase/amplitude accuracy to make that gate meaningful.

## Work completed

Created `lab/experiments/EXP-WET-001/R079-HARDWARE-PACKET.md` and `contracts/hardware-run-manifest.schema.json`.

Key freezes:

- primary cartridge realized as 100 wide slits, 0.500 mm free gap, 150 mm width, 30 mm active length -> 75 cm² open area and 225 cm³ gas volume; 0.30 mm comparator uses 83 x 0.600 mm slots with nearly matched open area/volume;
- pressure-balanced actuator reference uses 50 mm effective piston diameter and ~20 mL displacement amplitude -> ~10.19 mm displacement and 0.628 L/s flow amplitude at 5 Hz;
- 20/40 kPa forcing corresponds to ~5.65/~11.31 W acoustic scale at cos(phi)=0.9;
- all phase-critical channels use simultaneous sampling, >=10 kS/s/ch, >=16 bit, <=10 us skew;
- two flush dynamic pressure sensors, separate mean pressure, calibrated displacement, >=3 valid fast thermal phase sites (5 planned), and hot/cold liquid-loop calorimetry are mandatory;
- complex calibration at 1/3/5/7/10 Hz is predeclared; at 5 Hz, 2° is only 1.11 ms;
- primary sequence is DRY20 x3, DRY40 x3, WET20 x3, WET40 x3, each 60–120 s after steady state;
- raw/calibration hashes and Git SHA are mandatory before a measurement summary is scientifically admissible.

## External evidence

Fresh vendor evidence was used only to test instrument feasibility, not as bench evidence:

- PCB 113B28-class flush dynamic sensor: 344.7 kPa range, 6.895 MPa max pressure, 0.007 kPa typical resolution, microsecond response, 0.5 Hz LF response.
- NI simultaneous modules: NI-9220 16 ch / 100 kS/s/ch / 16-bit; NI-9222 4 ch / 500 kS/s/ch / 16-bit.
- Bronkhorst liquid Coriolis accuracy about ±0.2% reading; Endress+Hauser Promass A documents ±0.10% reading under reference conditions.
- sub-millisecond thin-film heat-flux sensing is technically demonstrated; the cited Vatell 17-us HFM is discontinued, so a current equivalent plus in-situ FRF is an explicit procurement risk.

## Energy/source/reset ledger

No generation claim was added. The eventual architecture source remains the real ~293→333 K heat gradient. In this identification rig, servo/piston acoustic work is deliberate experimental input. It is measured by p-U / p-V and cannot be credited as useful output. Steady-state closure is `Q_hot - Q_cold - P_acoustic - known_aux`, with <=5% residual required.

## Adversarial review

Strongest false-positive paths are pressure-channel subtraction phase error, mounting-induced thermal lag, wetting-induced geometry change, insufficient liquid-side ΔT, omission of servo forcing, and attractive flooding/dryout transients. The packet directly gates all six rather than relying on operator judgment after data exist.

## Result

The instrumentation itself does not impose a fundamental phase barrier: simultaneous electronic acquisition and flush dynamic pressure sensing have orders of magnitude more bandwidth than 5 Hz. The narrow risk is **installed thermal-interface phase calibration**, not ADC timing. Calorimetry at >=3 K liquid-side ΔT can be comfortably below the 5% budget with current flow-meter accuracy classes.

Verdict: **NEEDS DATA**.

The last WET desk-design uncertainty is closed. After Sheet publication, WET-01 should be marked waiting-hardware. A future BENCH-MEASURED state requires physical data and the R077 gate; this shift remains PROPOSED experiment design.

## Sources

https://www.pcb.com/products?m=113b28
https://www.pcb.com/products/product-compare?cm=113B28%2C113B27%2C113B26%2C113B24%2C113B22%2C113B23%2C113B03
https://www.ni.com/en/shop/hardware/voltage/model-ni-9220
https://www.ni.com/en/shop/hardware/voltage/model-ni-9222
https://www.bronkhorst.com/products/liquid-flow/mini-cori-flow/
https://www.vatell.com/index.php/hfm

## Next

No further WET desk variant. Execute the existing portfolio synthesis task and seed work only where a decisive uncertainty is not already hardware-only.
