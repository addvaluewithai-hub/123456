from __future__ import annotations

from dataclasses import asdict, dataclass
import math
from typing import Literal

from .wet_core import WetCorePoint, complex_diffusion_factor, penetration_depth, phase_deg

Z95 = 1.959963984540054
GateVerdict = Literal["PASS", "INCONCLUSIVE", "FAIL"]


@dataclass(frozen=True)
class WetGate:
    min_re_g_per_v_w_m3_k: float = 108_000.0
    max_abs_phase_deg: float = 30.0
    max_wet_loss_w: float = 2.3
    max_work_disagreement_fraction: float = 0.05
    max_energy_closure_fraction: float = 0.05
    max_repeatability_fraction: float = 0.05


@dataclass(frozen=True)
class WetMeasurementSummary:
    """Calibrated summary values, never a substitute for raw traces.

    All uncertainty fields are 1-sigma standard uncertainties. `physical_phase_deg`
    is the inferred physical phase after correcting the instrument transfer function.
    The conductance input is |G*|/V.
    """

    conductance_magnitude_density_w_m3_k: float
    physical_phase_deg: float
    amplitude_relative_sigma: float
    phase_sigma_deg: float
    geometry_relative_sigma: float
    wet_loss_w: float
    wet_loss_sigma_w: float
    work_disagreement_fraction: float = 0.0
    energy_closure_fraction: float = 0.0
    repeatability_fraction: float = 0.0

    def validate(self) -> None:
        if self.conductance_magnitude_density_w_m3_k < 0:
            raise ValueError("conductance magnitude must be non-negative")
        if self.amplitude_relative_sigma < 0 or self.geometry_relative_sigma < 0:
            raise ValueError("relative uncertainties must be non-negative")
        if self.phase_sigma_deg < 0 or self.wet_loss_sigma_w < 0:
            raise ValueError("standard uncertainties must be non-negative")
        if self.wet_loss_w < 0:
            raise ValueError("wet loss must be non-negative")
        for value in (
            self.work_disagreement_fraction,
            self.energy_closure_fraction,
            self.repeatability_fraction,
        ):
            if value < 0:
                raise ValueError("quality fractions must be non-negative")


def re_conductance_and_sigma(
    magnitude_density_w_m3_k: float,
    phase_deg_value: float,
    amplitude_relative_sigma: float,
    phase_sigma_deg: float,
    geometry_relative_sigma: float,
) -> tuple[float, float]:
    """Propagate independent amplitude, phase and geometry uncertainty into Re{G*}/V.

    Uses first-order (delta-method) propagation for
    Re{G*}/V = (|G*|/V) cos(phi). Phase uncertainty is expressed in degrees at
    the API boundary and converted to radians for differentiation.
    """

    if magnitude_density_w_m3_k < 0:
        raise ValueError("magnitude must be non-negative")
    if min(amplitude_relative_sigma, phase_sigma_deg, geometry_relative_sigma) < 0:
        raise ValueError("uncertainties must be non-negative")

    phi = math.radians(phase_deg_value)
    sigma_phi = math.radians(phase_sigma_deg)
    re_value = magnitude_density_w_m3_k * math.cos(phi)
    amplitude_geometry_sigma = abs(re_value) * math.hypot(
        amplitude_relative_sigma, geometry_relative_sigma
    )
    phase_sigma = abs(magnitude_density_w_m3_k * math.sin(phi) * sigma_phi)
    return re_value, math.hypot(amplitude_geometry_sigma, phase_sigma)


def confidence_interval_95(value: float, sigma: float) -> tuple[float, float]:
    if sigma < 0:
        raise ValueError("sigma must be non-negative")
    return value - Z95 * sigma, value + Z95 * sigma


def absolute_phase_interval_95(
    phase_deg_value: float, phase_sigma_deg: float
) -> tuple[float, float]:
    """Conservative 95% interval for |phase|, clipped to zero on the lower side."""

    if phase_sigma_deg < 0:
        raise ValueError("phase sigma must be non-negative")
    center = abs(phase_deg_value)
    return max(0.0, center - Z95 * phase_sigma_deg), center + Z95 * phase_sigma_deg


def classify_wet_measurement(
    measurement: WetMeasurementSummary,
    gate: WetGate = WetGate(),
) -> dict:
    """Apply the predeclared R073 gates to calibrated summary data.

    PASS requires every relevant 95% confidence bound to clear its gate and all
    measurement-quality checks to be within tolerance. FAIL is reserved for a
    physics interval wholly beyond at least one gate. Everything else is
    INCONCLUSIVE, so near-threshold nominal values can never be promoted by
    ignoring uncertainty.
    """

    measurement.validate()
    re_value, re_sigma = re_conductance_and_sigma(
        measurement.conductance_magnitude_density_w_m3_k,
        measurement.physical_phase_deg,
        measurement.amplitude_relative_sigma,
        measurement.phase_sigma_deg,
        measurement.geometry_relative_sigma,
    )
    re_ci = confidence_interval_95(re_value, re_sigma)
    phase_ci = absolute_phase_interval_95(
        measurement.physical_phase_deg, measurement.phase_sigma_deg
    )
    loss_low, loss_high = confidence_interval_95(
        measurement.wet_loss_w, measurement.wet_loss_sigma_w
    )
    loss_ci = (max(0.0, loss_low), loss_high)

    validity_ok = (
        measurement.work_disagreement_fraction <= gate.max_work_disagreement_fraction
        and measurement.energy_closure_fraction <= gate.max_energy_closure_fraction
        and measurement.repeatability_fraction <= gate.max_repeatability_fraction
    )

    pass_physics = (
        re_ci[0] >= gate.min_re_g_per_v_w_m3_k
        and phase_ci[1] <= gate.max_abs_phase_deg
        and loss_ci[1] <= gate.max_wet_loss_w
    )
    definite_physics_fail = (
        re_ci[1] < gate.min_re_g_per_v_w_m3_k
        or phase_ci[0] > gate.max_abs_phase_deg
        or loss_ci[0] > gate.max_wet_loss_w
    )

    if not validity_ok:
        verdict: GateVerdict = "INCONCLUSIVE"
        reason = "measurement-quality gate not closed"
    elif pass_physics:
        verdict = "PASS"
        reason = "all 95% confidence bounds clear the predeclared physics gates"
    elif definite_physics_fail:
        verdict = "FAIL"
        reason = "at least one 95% interval lies wholly beyond a predeclared physics gate"
    else:
        verdict = "INCONCLUSIVE"
        reason = "at least one 95% interval crosses a predeclared physics gate"

    return {
        "verdict": verdict,
        "reason": reason,
        "evidence_state": "MEASUREMENT_SUMMARY_ONLY",
        "input": asdict(measurement),
        "gate": asdict(gate),
        "derived": {
            "re_g_per_v_w_m3_k": re_value,
            "re_g_per_v_sigma_w_m3_k": re_sigma,
            "re_g_per_v_95_ci_w_m3_k": list(re_ci),
            "abs_phase_95_ci_deg": list(phase_ci),
            "wet_loss_95_ci_w": list(loss_ci),
            "measurement_quality_ok": validity_ok,
        },
    }


def clean_pass_guardbands(
    re_relative_sigma: float,
    phase_sigma_deg: float,
    wet_loss_sigma_w: float,
    gate: WetGate = WetGate(),
) -> dict[str, float]:
    """Nominal targets needed for 95%-bound clean PASS.

    `re_relative_sigma` is sigma(Re)/Re after amplitude, phase and geometry have
    already been propagated. This helper is for metrology design, not for
    classifying data.
    """

    if not 0 <= re_relative_sigma < 1.0 / Z95:
        raise ValueError("re_relative_sigma is outside the supported range")
    if phase_sigma_deg < 0 or wet_loss_sigma_w < 0:
        raise ValueError("uncertainties must be non-negative")
    return {
        "min_nominal_re_g_per_v_w_m3_k": gate.min_re_g_per_v_w_m3_k
        / (1.0 - Z95 * re_relative_sigma),
        "max_nominal_abs_phase_deg": gate.max_abs_phase_deg - Z95 * phase_sigma_deg,
        "max_nominal_wet_loss_w": gate.max_wet_loss_w - Z95 * wet_loss_sigma_w,
    }


def frozen_diffusion_screen() -> dict:
    """Reproduce the frozen 0.25 mm point and 0.30 mm comparison at 5 Hz."""

    base = WetCorePoint()
    points = []
    for radius_mm in (0.25, 0.30):
        radius_m = radius_mm * 1e-3
        thermal_delta = penetration_depth(base.alpha_m2_s, base.frequency_hz)
        mass_delta = penetration_depth(base.vapor_diffusivity_m2_s, base.frequency_hz)
        thermal = complex_diffusion_factor(radius_m, thermal_delta)
        mass = complex_diffusion_factor(radius_m, mass_delta)
        points.append(
            {
                "hydraulic_radius_mm": radius_mm,
                "frequency_hz": base.frequency_hz,
                "mean_pressure_bar": base.mean_pressure_pa / 1e5,
                "thermal_factor_real": thermal.real,
                "thermal_phase_deg": phase_deg(thermal),
                "mass_factor_real": mass.real,
                "mass_phase_deg": phase_deg(mass),
            }
        )
    return {
        "evidence_state": "ANALYTICAL_SCREEN",
        "points": points,
        "warning": "Intrinsic transverse diffusion only; no wall/contact/wet-film/interface or bench response is invented.",
    }


def reference_snapshot() -> dict:
    """Deterministic R077 reference artifact for a fresh checkout."""

    return {
        "schema_version": 1,
        "run": "R077",
        "branch": "WET-01",
        "experiment": "EXP-WET-001",
        "gate": asdict(WetGate()),
        "frozen_diffusion_screen": frozen_diffusion_screen(),
        "clean_pass_guardbands": {
            "example_uncertainty_assumptions": {
                "re_relative_sigma": 0.05,
                "phase_sigma_deg": 2.0,
                "wet_loss_sigma_w": 0.2,
            },
            "targets": clean_pass_guardbands(0.05, 2.0, 0.2),
        },
        "interpretation": "Reference values are analytical/metrology-design outputs, not hardware measurements.",
    }
