import math

from energy_lab.toec import SCENARIOS, audit_case
from energy_lab.toec_calibration import (
    FourStageMeasurement,
    conservative_packaging_boundary,
    project_16_from_4,
    rss_relative_uncertainty,
)


def _measurement_from_scenario(name: str) -> FourStageMeasurement:
    s = SCENARIOS[name]
    c4 = audit_case(s, 80.0, 40.0, 4)
    return FourStageMeasurement(
        gross_hydraulic_power_density_w_m2=c4["gross_hydraulic_power_density_w_m2"],
        hydraulic_efficiency=c4["hydraulic_efficiency"],
        header_pressure_loss_fraction=s.header_pressure_loss_fraction,
        membrane_area_density_m2_per_l=s.membrane_area_density_m2_per_l,
        thermal_network_specific_duty_w_per_l=s.thermal_network_specific_duty_w_per_l,
        stage_dead_volume_l=s.stage_overhead_l,
        hydraulic_to_electric_efficiency=s.hydraulic_to_electric_efficiency,
        electric_parasitic_w=s.electric_parasitic_w,
        pto_volume_l=s.pto_fixed_volume_l + 10.0 / s.pto_specific_power_w_per_l,
        housing_volume_l=s.housing_volume_l,
    )


def test_four_stage_calibration_projection_reproduces_r075_n16_envelopes():
    for name in ("optimistic", "conservative"):
        direct = audit_case(SCENARIOS[name], 80.0, 40.0, 16)
        projected = project_16_from_4(_measurement_from_scenario(name))
        assert math.isclose(projected["total_volume_l"], direct["volume_l"]["total"], rel_tol=1e-10)
        assert math.isclose(projected["source_heat_w"], direct["source_heat_w"], rel_tol=1e-10)


def test_conservative_packaging_boundary_matches_r076_thresholds():
    absolute = conservative_packaging_boundary()
    assert 0.82 < absolute["absolute_min_membrane_area_density_m2_per_l"] < 0.84
    assert 500 < absolute["absolute_min_thermal_network_specific_duty_w_per_l"] < 510

    at_rho_11 = conservative_packaging_boundary(membrane_area_density_m2_per_l=1.1)
    assert 2050 < at_rho_11["required_thermal_network_specific_duty_w_per_l"] < 2065

    at_qv_1000 = conservative_packaging_boundary(thermal_network_specific_duty_w_per_l=1000.0)
    assert 1.67 < at_qv_1000["required_membrane_area_density_m2_per_l"] < 1.69


def test_measurement_uncertainty_is_small_relative_to_package_gap():
    # Representative 1-sigma terms: pressure 0.3%, flow 0.5%, calorimetry 2.5%.
    hydraulic = rss_relative_uncertainty(0.003, 0.005)
    efficiency = rss_relative_uncertainty(hydraulic, 0.025)
    assert hydraulic < 0.006
    assert efficiency < 0.027
