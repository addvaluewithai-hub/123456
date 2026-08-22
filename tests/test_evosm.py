import math

from energy_lab.evosm import (
    EvosmAssumptions,
    humidity_specific_exergy_j_kg,
    reference_envelope,
    required_power_density_for_pitch,
)


def test_reference_large_area_geometry_bound():
    r = reference_envelope()
    assert math.isclose(r["required_membrane_area_m2"], 15.1515151515, rel_tol=1e-10)
    assert math.isclose(r["membrane_solid_volume_l"], 1.51515151515, rel_tol=1e-10)
    assert math.isclose(r["absolute_stack_pitch_limit_um"], 132.0, rel_tol=1e-10)
    assert math.isclose(r["nonmembrane_pitch_budget_um"], 32.0, rel_tol=1e-10)


def test_measured_scale_degradation():
    r = reference_envelope()
    assert math.isclose(r["measured_scale_degradation_factor"], 8.5 / 0.66, rel_tol=1e-12)


def test_half_rh_exergy_and_pro_comparison():
    p = EvosmAssumptions()
    ex = humidity_specific_exergy_j_kg(0.5, 298.15)
    assert 95_000 < ex < 96_000
    r = reference_envelope()
    assert 0.37 < r["ideal_evaporation_mass_flow_kg_h"] < 0.39
    assert math.isclose(r["pro_50bar_ideal_water_flow_kg_h"], 7.2, rel_tol=1e-12)
    assert 19.0 < r["pro_to_ideal_exergy_water_flow_ratio"] < 19.2


def test_pitch_case_500um_needs_more_than_3x_measured_pd():
    p = EvosmAssumptions()
    pd = required_power_density_for_pitch(10.0, p.package_volume_m3, 0.5e-3)
    assert math.isclose(pd, 2.5, rel_tol=1e-12)
    assert pd / p.measured_large_area_power_density_w_m2 > 3.7


def test_parasitics_increase_area_and_source_requirement():
    base = reference_envelope(0.0)
    derated = reference_envelope(0.2)
    assert derated["required_membrane_area_m2"] > base["required_membrane_area_m2"]
    assert derated["ideal_evaporation_source_area_m2"] > base["ideal_evaporation_source_area_m2"]
