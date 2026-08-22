# R079 — Buildable phase-aware wet-coupon hardware packet

Evidence state: **EXPERIMENT DESIGN / INSTRUMENTATION CONTRACT**. No bench data are claimed.

## Mission and falsification test

Freeze one buildable experiment for the already-frozen WET-01 point so a later bench run can make a binary, uncertainty-bounded decision without reopening pore geometry.

Primary physics point:

- free-gas hydraulic radius `r_h = 0.250 mm` (wide-slit free gap `g = 0.500 mm`);
- `f = 5.000 Hz`;
- mean gas pressure `P_mean ≈ 10 bar abs`;
- acoustic pressure amplitude `p_hat = 20 kPa`, then `40 kPa`;
- thermal boundary nominally `293.15 K -> 333.15 K`;
- DRY first, then WET under matched geometry and forcing;
- only comparison cartridge: `r_h = 0.300 mm` (`g = 0.600 mm`).

The experiment may promote WET-01 only through the predeclared R077 classifier. It must not be reinterpreted after seeing data.

## 1. Frozen cartridge geometry

The coupon preserves the R069–R073 active gas volume and open flow area with a manufacturable parallel-slit realization.

### Primary 0.25 mm cartridge

- 100 parallel free-gas slots.
- clear slot width: `150.0 ± 0.1 mm`.
- free gas gap **after the installed wetting layer is accounted for**: `0.500 ± 0.010 mm`.
- active axial length: `30.00 ± 0.05 mm`.
- nominal total gas-flow area: `75.00 cm²`.
- nominal active gas volume: `225.0 cm³`.
- equivalent wide-slit hydraulic radius: `0.250 mm` to first order; exact `A/P` from as-built metrology is what enters analysis.

### 0.30 mm comparison cartridge

- 83 parallel free-gas slots.
- clear slot width: `150.0 ± 0.1 mm`.
- free gas gap after wetting-layer allowance: `0.600 ± 0.012 mm`.
- active axial length: `30.00 ± 0.05 mm`.
- nominal gas-flow area: `74.70 cm²`.
- nominal active gas volume: `224.1 cm³`.

### Manufacturing/metrology rule

Spacer thickness is chosen only after measuring the dry wetting-layer thickness. The **free gas gap**, not nominal shim thickness, is the controlled dimension. Measure at least 10 distributed gaps before assembly and after the final compression stack is torqued; record mean, standard deviation and extrema. Analysis uses measured open area, wetted perimeter and active length. Reject/rework a cartridge when effective `r_h` differs by >2% from its target or when a local free gap differs by >5% from nominal. The 0.30 mm cartridge is a comparison only; failure of 0.25 mm does not authorize geometry churn.

The cartridge itself is not a 10-bar pressure boundary. It sits entirely inside one pressure-rated housing so thin internal plates see near-common-mode mean pressure rather than a 10-bar structural differential.

## 2. Acoustic drive geometry and scale

Use a pressure-balanced actuator architecture so the drive does not continuously fight the 10-bar mean load. The working-side displacement is measured directly; actuator electrical input is recorded for diagnostics but is not credited as generated power.

Freeze a nominal effective piston diameter of `50.00 mm` for the identification rig unless the final pressure-rated actuator has a separately calibrated effective area. Area is then `1.9635e-3 m²`.

The R072 displacement-volume target of about `20.0 mL` amplitude corresponds to:

- displacement amplitude `x_hat ≈ 10.19 mm`;
- velocity/volume-flow amplitude at 5 Hz `U_hat = 2π f V_hat ≈ 6.283e-4 m³/s = 0.628 L/s`.

At `cos(phi_pU)=0.9`, the corresponding acoustic powers are approximately:

- 20 kPa: `5.65 W`;
- 40 kPa: `11.31 W`.

Those are forcing/reference scales, not generated output.

## 3. Mandatory measurement channels

All **phase-critical dynamic channels** terminate on one simultaneous-sampling ADC clock. Minimum acquisition requirement: >=16 bit, >=10 kS/s/channel, channel-to-channel skew <=10 microseconds. Record raw at the native common rate; analysis may decimate only after anti-alias filtering. A current NI-9220-class module (16 simultaneous differential channels, 100 kS/s/ch, 16 bit) exceeds this requirement; NI also lists NI-9222 at 500 kS/s/ch. These are reference implementations, not exclusive vendors.

### P1/P2 — dynamic pressure upstream/downstream

Two flush-mounted dynamic pressure transducers, mounted in the same axial plane convention used by the model and without remote pressure tubing.

Required:

- survives >=1.2 MPa absolute normal pressure with margin;
- dynamic full-scale >=100 kPa and resolution <=0.1 kPa around 5 Hz;
- calibrated complex response from 1–10 Hz;
- flush diaphragm or cavity correction experimentally characterized.

Reference implementation: PCB 113B28-class quartz dynamic pressure sensor. PCB specifies 344.7 kPa measurement range, 6.895 MPa maximum pressure, 0.007 kPa typical resolution, <=1 microsecond rise time, and 0.5 Hz low-frequency response. Two matched channels plus external ICP conditioning provide ample raw bandwidth while surviving the 10-bar common-mode pressure. A lower-frequency phase calibration is still mandatory because the experiment is at 5 Hz.

`p'(t)` is the mean of appropriately located acoustic pressure channels when estimating acoustic power; `Δp'(t)=P1-P2` is also retained for dissipative-loss estimation. Never infer kPa-scale loss from long tubes whose phase response has not been calibrated.

### P0 — mean pressure

Separate static absolute-pressure transducer, `0–16 bar abs` or narrower safe range, accuracy <=0.05% FS, with an independent mechanical gauge used only as a sanity check. P0 is not substituted for the dynamic pressure channels.

### X — piston displacement

Analog LVDT or laser displacement channel with:

- usable range at least `±15 mm` around center;
- calibrated displacement amplitude error <=0.5%;
- dynamic phase uncertainty <=0.5° at 5 Hz after conditioning;
- analog bandwidth >=100 Hz.

Derive velocity and gas volume flow by harmonic regression of calibrated `x(t)` and the measured effective piston area. Do **not** numerically differentiate raw displacement samples.

### HF/Tdyn — dynamic heat-flux / wall-temperature phase

Install at least five axial dynamic sites at nominal `x/L = 0.10, 0.30, 0.50, 0.70, 0.90`; at least three sites must remain valid for a run to be accepted. The phase-identification channel must have:

- physical time response <=0.5 ms before calibration (equivalent to <~0.9° at 5 Hz for a first-order lag);
- in-situ complex calibration at 1/3/5/7/10 Hz;
- calibrated phase uncertainty <=1.0° at 5 Hz;
- amplitude calibration <=3% for heat flux or an equivalent calibrated wall-temperature transfer function.

A thin-film heat-flux technology is physically capable of far faster response: Vatell documents 17 microsecond uncoated HFM response and ±3% calibration accuracy, but that HFM product line is marked unavailable since 2021. Therefore it is **evidence of feasibility, not a procurement recommendation**. A current equivalent must pass the in-situ FRF test before use.

### TH/TC + FH/FC — hot/cold loop calorimetry

Each liquid loop uses:

- one calibrated mass-flow meter;
- matched 4-wire Pt100-class inlet/outlet RTDs, calibrated as pairs across 293–333 K;
- differential-temperature uncertainty target <=0.03 K (1 sigma) after pair calibration;
- mass-flow uncertainty <=0.5% of reading.

Set loop flow so each exchanger produces `ΔT_liquid >= 3 K` during the decision runs. Around the earlier ~250 W coupon thermal scale, water at ~1.2 L/min gives roughly a 3 K rise. A Bronkhorst mini CORI-FLOW M15-class meter covers this neighborhood; current Bronkhorst data state ±0.2% of reading for liquid flow. Endress+Hauser also documents ±0.10% of reading for liquid Promass A under reference conditions. Either performance class is comfortably below the 5% heat-rate budget when paired differential temperature is calibrated.

### Auxiliary channels

Mandatory logging, not all phase-critical:

- hot/cold bath supply temperatures;
- gas mean temperature and pressure;
- liquid inventory / reservoir mass before and after each WET block (resolution <=0.1 g preferred);
- dew point or water-vapour concentration when a pressure-compatible sensor is available; otherwise sample composition and preparation protocol are logged and this remains an uncertainty item;
- actuator electrical V/I for diagnostic source accounting;
- relief/overpressure switch state and emergency-stop state.

## 4. Phase and amplitude calibration contract

At 5 Hz, 1° equals `0.556 ms`; 2° equals `1.111 ms`; 3° equals `1.667 ms`. R077 permits only 2–3° total calibrated phase uncertainty, so calibration is a first-class experimental step.

Before WET data are accepted:

1. **Electronic common-signal test.** Inject one reference sine into every phase-critical acquisition chain at 1/3/5/7/10 Hz. Correct channel delay and require residual channel-to-channel phase <=0.5° at 5 Hz.
2. **Pressure FRF.** Mount P1/P2 beside the reference sensor in a common pressure cavity and drive sinusoidally through the calibration frequencies. Repeat at the experiment mean pressure when practical. Fit complex gain, not scalar sensitivity. Residual relative P1/P2 phase uncertainty must be <=1° at 5 Hz.
3. **Displacement calibration.** Static scale/offset with traceable length standards over the used ±12 mm region, then dynamic cross-check at 1/3/5/7/10 Hz against a reference optical channel or calibrated actuator encoder. Require <=0.5° residual phase at 5 Hz.
4. **Heat-flux/temperature FRF.** Calibrate each installed dynamic thermal site in situ using a reference sinusoidal heater/flux input with electrically measured power and common timing. Require <=1° phase uncertainty at 5 Hz after correction. Any site that cannot meet this is excluded before looking at the physics result.
5. **Calorimetry calibration.** Zero/flow check each mass-flow meter; perform matched RTD bath calibration and a zero-heat / known-heat loop check. Require hot and cold calorimetric bias closure within 3% on a known electrical heat load before coupon testing.

Calibration IDs, coefficients, covariance/uncertainty, raw-file hashes and dates are immutable inputs to the analysis manifest.

## 5. Predeclared run sequence

Gas composition/carrier gas, pressure and humidity preparation must be identical except for the intentional DRY/WET water state. The exact carrier gas is frozen in the build record before data collection and cannot be changed between the paired blocks.

After thermal steady state:

1. DRY, 20 kPa: 3 independent 60–120 s records.
2. DRY, 40 kPa: 3 independent 60–120 s records.
3. WET, 20 kPa: 3 independent 60–120 s records.
4. WET, 40 kPa: 3 independent 60–120 s records.

Each 60 s record contains 300 cycles at 5 Hz. A repeat is independent only after the condition is re-established and steady-state acceptance is rechecked. The primary decision uses the 0.25 mm cartridge. Run the 0.30 mm cartridge only after the full primary dataset is locked; it is not used to rescue a failed primary result by post-hoc selection.

Pre-run steady-state acceptance:

- mean pressure drift <0.2% over 60 s;
- hot and cold inlet temperature drift <0.05 K/min;
- liquid-loop flow drift <0.5% over 60 s;
- WET reservoir mass trend consistent with no gross dryout/flooding; visible/pressure evidence of flooding is logged as a failed condition, not discarded silently.

## 6. Derived quantities and independent cross-checks

Primary acoustic power, two ways:

`P_ac,phasor = 0.5 Re{p_hat U_hat*}`

and

`P_ac,PV = f ∮ p dV`.

They must agree within 5%.

Calorimetry:

`Q_dot = m_dot c_p (T_out - T_in)`

using the calibrated water/fluid properties and measured temperatures.

Steady-state energy residual:

`epsilon_E = |Q_hot - Q_cold - P_ac - Q_known_aux| / max(|Q_hot|, |Q_cold|)`.

It must be <=5%; known electrical heater/auxiliary terms are explicit. Servo wall-plug input is recorded but the gas-side `p-U` work is the experimental mechanical forcing term relevant to the coupon ledger. No actuator input is ever counted as useful output.

Wet dissipative acoustic loss is obtained from the calibrated WET-minus-DRY pressure/flow response with covariance propagated through the subtraction. The digital classifier receives only the predeclared reduced quantities after calibration/provenance checks pass.

## 7. Uncertainty allocation

Target 1-sigma components:

- derived `Re{G*}/V` amplitude/geometry: <=5% relative;
- calibrated physical phase: <=2.0° preferred, never >3.0° for a decision run;
- wet-loss uncertainty: <=0.20 W;
- as-built geometry: <=2% on effective `r_h`/conductance-volume mapping;
- hot/cold heat rate: <=3% each after calibration;
- acoustic power cross-check discrepancy: <=5%;
- repeatability coefficient of variation: <=5%.

With the illustrative R077 5% / 2° / 0.2 W metrology capability, a **clean nominal** PASS needs approximately `Re{G*}/V >=119.73 kW m^-3 K^-1`, `|phase| <=26.08°`, and wet loss `<=1.908 W`. The underlying physics gates remain 108 kW/m³K, 30° and 2.3 W at the required 95% bound.

## 8. Data/provenance contract

Every record gets a manifest conforming to `contracts/hardware-run-manifest.schema.json`. Raw data are immutable and hashed before reduction. The manifest must identify:

- cartridge ID and as-built geometry measurement file;
- sensor serial/asset IDs;
- calibration IDs and calibration data hashes;
- DAQ model, sample rate, channel map and clock;
- gas/liquid identity;
- DRY/WET condition, p-hat target and temperatures;
- raw-data location/hash;
- code Git SHA used for reduction;
- operator/time and anomaly log.

A standalone `measurement-summary.json` without the raw/calibration provenance is insufficient for scientific promotion.

## 9. Pressure / thermal safety boundary

Do not fabricate a pressure vessel from this packet. Use a commercially pressure-rated housing, fittings, viewports (if any), feedthroughs and valves with MAWP comfortably above the maximum operating pressure at the maximum test temperature and compatible with wet gas/water. A competent pressure-systems reviewer must approve the assembly, relief device set point and proof/leak procedure before 10-bar operation.

Minimum controls:

- mechanical relief device that opens below vessel MAWP and above normal operating excursions;
- independent electronic high-pressure trip;
- guarded/remote pressurization and operation;
- controlled depressurization before access;
- no unrated glass or improvised pressure boundary;
- low-pressure leak test followed by the manufacturer's/code-compliant proof procedure;
- thermal over-temperature trip on hot loop.

These are experiment prerequisites, not evidence that any test has been performed.

## 10. Evidence-backed instrumentation audit

Fresh vendor evidence checked during R079:

- PCB 113B28: 344.7 kPa dynamic range, 6.895 MPa maximum pressure, 0.007 kPa typical resolution, >=500 kHz resonance, <=1 µs rise time, and 0.5 Hz low-frequency response. This supports flush, high-headroom dynamic pressure measurement at 5 Hz, but does not remove the mandatory in-situ FRF correction.
- NI lists NI-9220 as 16-channel simultaneous 16-bit 100 kS/s/ch and NI-9222 as 4-channel simultaneous 16-bit 500 kS/s/ch. This makes sub-millisecond electronic timing an engineering choice rather than a fundamental limit.
- Bronkhorst lists liquid Coriolis accuracy around ±0.2% of reading; its M15 family covers up to hundreds of kg/h. Endress+Hauser documents ±0.10% of reading for liquid Promass A under reference conditions. Loop flow measurement is therefore not expected to dominate the heat-rate uncertainty.
- Thin-film heat-flux response well below 1 ms is technically demonstrated, but the cited Vatell HFM line is discontinued. A current qualified equivalent and its in-situ calibration remain a procurement/engineering risk.

## 11. Adversarial review

What can still fool us?

1. Subtracting two large pressure waveforms can manufacture loss if relative phase calibration drifts. Therefore P1/P2 get a common-cavity FRF and WET-minus-DRY covariance is retained.
2. A fast catalog sensor can become slow after mounting, coating or a thermal contact layer. Therefore only **in-situ** thermal FRF counts.
3. Wetting changes free gap. Therefore `r_h` is defined after wetting-layer allowance and as-built geometry is measured.
4. Calorimetry can look precise while a tiny liquid-side ΔT dominates error. Therefore decision runs require >=3 K loop ΔT.
5. A servo-driven coupon can appear to 'produce' acoustic power if the forcing source is omitted. Therefore the servo is explicitly experimental input and full gas-side energy closure is mandatory.
6. Flooding/dryout can create attractive transient phases. Such states are failed conditions unless explicitly reproduced and modeled; they cannot be cherry-picked.

## Decision

**NEEDS DATA.** The remaining decisive uncertainty is now physical wet-interface behavior, not an unresolved desk design choice. The hardware packet is sufficiently specific to procure/build/review without changing the frozen physics point. WET-01 should move to **waiting-hardware** after publication of R079. No additional WET geometry or metrology desk work is justified until calibrated bench data arrive.

Next desk action is the existing portfolio synthesis task, which should rank genuinely non-hardware opportunities rather than manufacture more WET/TOEC variants.

## Sources checked in R079

- https://www.pcb.com/products?m=113b28
- https://www.pcb.com/products/product-compare?cm=113B28%2C113B27%2C113B26%2C113B24%2C113B22%2C113B23%2C113B03
- https://www.ni.com/en/shop/hardware/voltage/model-ni-9220
- https://www.ni.com/en/shop/hardware/voltage/model-ni-9222
- https://www.bronkhorst.com/products/liquid-flow/mini-cori-flow/
- https://www.vatell.com/index.php/hfm
