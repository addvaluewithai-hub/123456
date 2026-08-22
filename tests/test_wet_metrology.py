import json
import math
from pathlib import Path

from energy_lab.wet_metrology import (
    WetMeasurementSummary,
    classify_wet_measurement,
    clean_pass_guardbands,
    frozen_diffusion_screen,
    re_conductance_and_sigma,
    reference_snapshot,
)


def test_frozen_diffusion_screen_reproduces_r072_r073():
    points = frozen_diffusion_screen()["points"]
    primary, comparison = points
    assert math.isclose(primary["thermal_factor_real"], 0.9060636563, rel_tol=1e-8)
    assert math.isclose(primary["thermal_phase_deg"], -16.21951592, rel_tol=1e-8)
    assert math.isclose(primary["mass_factor_real"], 0.9304622368, rel_tol=1e-8)
    assert math.isclose(primary["mass_phase_deg"], -13.91223196, rel_tol=1e-8)
    assert comparison["thermal_phase_deg"] < primary["thermal_phase_deg"]


def test_re_conductance_zero_phase_has_no_phase_sensitivity():
    value, sigma = re_conductance_and_sigma(120_000.0, 0.0, 0.05, 2.0, 0.0)
    assert math.isclose(value, 120_000.0)
    assert math.isclose(sigma, 6_000.0)


def test_nominally_above_gate_can_still_be_inconclusive():
    result = classify_wet_measurement(
        WetMeasurementSummary(
            conductance_magnitude_density_w_m3_k=120_000.0,
            physical_phase_deg=20.0,
            amplitude_relative_sigma=0.05,
            phase_sigma_deg=2.0,
            geometry_relative_sigma=0.015,
            wet_loss_w=1.8,
            wet_loss_sigma_w=0.2,
        )
    )
    assert result["verdict"] == "INCONCLUSIVE"
    assert result["derived"]["re_g_per_v_95_ci_w_m3_k"][0] < 108_000.0


def test_clear_pass_requires_all_95_percent_bounds():
    result = classify_wet_measurement(
        WetMeasurementSummary(
            conductance_magnitude_density_w_m3_k=135_000.0,
            physical_phase_deg=20.0,
            amplitude_relative_sigma=0.03,
            phase_sigma_deg=1.5,
            geometry_relative_sigma=0.01,
            wet_loss_w=1.5,
            wet_loss_sigma_w=0.15,
            work_disagreement_fraction=0.03,
            energy_closure_fraction=0.04,
            repeatability_fraction=0.03,
        )
    )
    assert result["verdict"] == "PASS"


def test_definite_fail_when_conductance_interval_is_wholly_below_gate():
    result = classify_wet_measurement(
        WetMeasurementSummary(
            conductance_magnitude_density_w_m3_k=100_000.0,
            physical_phase_deg=20.0,
            amplitude_relative_sigma=0.02,
            phase_sigma_deg=1.0,
            geometry_relative_sigma=0.01,
            wet_loss_w=1.0,
            wet_loss_sigma_w=0.1,
        )
    )
    assert result["verdict"] == "FAIL"
    assert result["derived"]["re_g_per_v_95_ci_w_m3_k"][1] < 108_000.0


def test_bad_energy_closure_is_inconclusive_not_physics_fail():
    result = classify_wet_measurement(
        WetMeasurementSummary(
            conductance_magnitude_density_w_m3_k=150_000.0,
            physical_phase_deg=15.0,
            amplitude_relative_sigma=0.01,
            phase_sigma_deg=1.0,
            geometry_relative_sigma=0.01,
            wet_loss_w=1.0,
            wet_loss_sigma_w=0.1,
            energy_closure_fraction=0.08,
        )
    )
    assert result["verdict"] == "INCONCLUSIVE"
    assert result["derived"]["measurement_quality_ok"] is False


def test_guardbands_quantify_clean_pass_margin():
    bands = clean_pass_guardbands(0.05, 2.0, 0.2)
    assert math.isclose(bands["min_nominal_re_g_per_v_w_m3_k"], 119733.6856, rel_tol=1e-8)
    assert math.isclose(bands["max_nominal_abs_phase_deg"], 26.08007203, rel_tol=1e-8)
    assert math.isclose(bands["max_nominal_wet_loss_w"], 1.908007203, rel_tol=1e-8)


def test_committed_reference_snapshot_is_reproducible():
    path = Path("lab/experiments/EXP-WET-001/reference/R077-metrology-gate.json")
    committed = json.loads(path.read_text(encoding="utf-8"))
    assert committed == reference_snapshot()
