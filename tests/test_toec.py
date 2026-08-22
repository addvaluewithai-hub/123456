import math

from energy_lab.toec import (
    SCENARIOS,
    STAGE_COUNTS,
    audit_case,
    carnot_efficiency,
    stage_temperatures_c,
    sweep,
    transport_anchor_diagnostic,
)


def test_stage_profile_uses_source_span_once():
    for n in STAGE_COUNTS:
        profile = stage_temperatures_c(80.0, 40.0, n)
        assert len(profile) == n
        assert math.isclose(profile[0][0], 80.0)
        assert math.isclose(profile[-1][1], 40.0)
        assert math.isclose(sum(a - b for a, b in profile), 40.0, rel_tol=0, abs_tol=1e-10)


def test_energy_efficiency_below_carnot_and_closes():
    for case in sweep()["cases"]:
        assert 0 < case["electric_efficiency"] < case["carnot_efficiency"]
        expected = 10.0 / case["source_heat_w"]
        assert math.isclose(case["electric_efficiency"], expected, rel_tol=1e-12)


def test_published_38_stage_optimistic_anchor_is_preserved_before_bom_losses():
    case = audit_case(SCENARIOS["optimistic"], 80.0, 40.0, 38)
    assert math.isclose(case["hydraulic_efficiency"], 0.0472, rel_tol=1e-12)
    assert math.isclose(case["gross_hydraulic_power_density_w_m2"], 34.05, rel_tol=1e-12)


def test_naive_flux_benchmark_combination_is_flagged():
    d = transport_anchor_diagnostic()
    assert d["naive_implied_latent_heat_recovery"] > d["ideal_simple_n_effect_recovery"]
    assert d["latent_heat_flux_w_m2"] > 30_000
    assert 700 < d["benchmark_source_heat_w_m2"] < 750


def test_gate_is_not_hardcoded_to_pass():
    optimistic = audit_case(SCENARIOS["optimistic"], 80.0, 40.0, 16)
    conservative = audit_case(SCENARIOS["conservative"], 80.0, 40.0, 16)
    assert optimistic["gate"]["passes_preferred"]
    assert not conservative["gate"]["passes_floor"]


def test_carnot_known_cases():
    assert 0.11 < carnot_efficiency(80, 40) < 0.12
    assert 0.12 - 0.001 < carnot_efficiency(60, 20) < 0.121
