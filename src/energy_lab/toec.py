from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import math
from pathlib import Path

STAGE_COUNTS = (1, 4, 8, 16, 38)
TEMPERATURE_CASES_C = ((60.0, 20.0), (80.0, 40.0))


@dataclass(frozen=True)
class Scenario:
    name: str
    eta38_8040: float
    eta38_6020: float
    power_density38_8040_w_m2: float
    power_density38_6020_w_m2: float
    stage_factor_n1_eta: float
    stage_factor_n1_power: float
    header_pressure_loss_fraction: float
    hydraulic_to_electric_efficiency: float
    electric_parasitic_w: float
    membrane_area_density_m2_per_l: float
    stage_overhead_l: float
    thermal_network_specific_duty_w_per_l: float
    pto_fixed_volume_l: float
    pto_specific_power_w_per_l: float
    housing_volume_l: float


SCENARIOS = {
    "conservative": Scenario(
        name="conservative",
        eta38_8040=0.035,
        eta38_6020=0.030,
        power_density38_8040_w_m2=22.0,
        power_density38_6020_w_m2=9.5,
        stage_factor_n1_eta=0.58,
        stage_factor_n1_power=0.50,
        header_pressure_loss_fraction=0.12,
        hydraulic_to_electric_efficiency=0.75,
        electric_parasitic_w=0.50,
        membrane_area_density_m2_per_l=0.55,
        stage_overhead_l=0.018,
        thermal_network_specific_duty_w_per_l=300.0,
        pto_fixed_volume_l=0.20,
        pto_specific_power_w_per_l=35.0,
        housing_volume_l=0.18,
    ),
    "optimistic": Scenario(
        name="optimistic-but-defensible",
        eta38_8040=0.0472,
        eta38_6020=0.041,
        power_density38_8040_w_m2=34.05,
        power_density38_6020_w_m2=15.0,
        stage_factor_n1_eta=0.64,
        stage_factor_n1_power=0.50,
        header_pressure_loss_fraction=0.05,
        hydraulic_to_electric_efficiency=0.85,
        electric_parasitic_w=0.20,
        membrane_area_density_m2_per_l=1.10,
        stage_overhead_l=0.008,
        thermal_network_specific_duty_w_per_l=600.0,
        pto_fixed_volume_l=0.12,
        pto_specific_power_w_per_l=70.0,
        housing_volume_l=0.10,
    ),
}


def carnot_efficiency(th_c: float, tc_c: float) -> float:
    th_k = th_c + 273.15
    tc_k = tc_c + 273.15
    if th_k <= tc_k:
        raise ValueError("hot temperature must exceed cold temperature")
    return 1.0 - tc_k / th_k


def stage_temperatures_c(th_c: float, tc_c: float, stages: int) -> list[tuple[float, float]]:
    """A non-double-counting audit profile: the source span is partitioned once.

    This is not a claim about the exact plumbing of Zhang et al. (2025). It is an
    exergy-accounting profile that prevents every stage from being assigned the
    full source temperature difference.
    """
    if stages < 1:
        raise ValueError("stages must be >= 1")
    step = (th_c - tc_c) / stages
    return [(th_c - i * step, th_c - (i + 1) * step) for i in range(stages)]


def stage_factor(stages: int, n1_fraction: float, exponent: float = 0.45) -> float:
    """Interpolation for package screening, normalized to 1.0 at 38 stages.

    The interpolation is a free engineering assumption, not literature data.
    Sensitivity to stage count is therefore reported rather than treated as a
    validated transport law.
    """
    if stages not in STAGE_COUNTS:
        raise ValueError(f"stages must be one of {STAGE_COUNTS}")
    x = (stages - 1.0) / 37.0
    return n1_fraction + (1.0 - n1_fraction) * x**exponent


def _case_anchor(s: Scenario, th_c: float, tc_c: float) -> tuple[float, float]:
    key = (int(th_c), int(tc_c))
    if key == (80, 40):
        return s.eta38_8040, s.power_density38_8040_w_m2
    if key == (60, 20):
        return s.eta38_6020, s.power_density38_6020_w_m2
    raise ValueError("unsupported temperature case")


def audit_case(
    scenario: Scenario,
    th_c: float,
    tc_c: float,
    stages: int,
    target_dc_w: float = 10.0,
) -> dict[str, object]:
    eta38, pdens38 = _case_anchor(scenario, th_c, tc_c)
    eta_hyd = eta38 * stage_factor(stages, scenario.stage_factor_n1_eta)
    gross_pdens = pdens38 * stage_factor(stages, scenario.stage_factor_n1_power)
    usable_pdens = gross_pdens * (1.0 - scenario.header_pressure_loss_fraction)

    gross_hydraulic_w = (target_dc_w + scenario.electric_parasitic_w) / (
        scenario.hydraulic_to_electric_efficiency
        * (1.0 - scenario.header_pressure_loss_fraction)
    )
    membrane_area_m2 = gross_hydraulic_w / gross_pdens
    source_heat_w = gross_hydraulic_w / eta_hyd

    membrane_core_l = membrane_area_m2 / scenario.membrane_area_density_m2_per_l
    stage_overhead_l = stages * scenario.stage_overhead_l
    thermal_network_l = source_heat_w / scenario.thermal_network_specific_duty_w_per_l
    pto_l = scenario.pto_fixed_volume_l + target_dc_w / scenario.pto_specific_power_w_per_l
    total_l = (
        membrane_core_l
        + stage_overhead_l
        + thermal_network_l
        + pto_l
        + scenario.housing_volume_l
    )

    electric_eta = target_dc_w / source_heat_w
    eta_c = carnot_efficiency(th_c, tc_c)
    profile = stage_temperatures_c(th_c, tc_c, stages)

    return {
        "scenario": scenario.name,
        "hot_c": th_c,
        "cold_c": tc_c,
        "stages": stages,
        "stage_temperature_profile_c": profile,
        "carnot_efficiency": eta_c,
        "hydraulic_efficiency": eta_hyd,
        "gross_hydraulic_power_density_w_m2": gross_pdens,
        "usable_hydraulic_power_density_w_m2": usable_pdens,
        "gross_hydraulic_power_w": gross_hydraulic_w,
        "membrane_area_m2": membrane_area_m2,
        "source_heat_w": source_heat_w,
        "electric_efficiency": electric_eta,
        "fraction_of_carnot_electric": electric_eta / eta_c,
        "volume_l": {
            "membrane_core": membrane_core_l,
            "stage_overhead": stage_overhead_l,
            "thermal_network": thermal_network_l,
            "pto": pto_l,
            "housing": scenario.housing_volume_l,
            "total": total_l,
        },
        "gate": {
            "power": target_dc_w >= 10.0,
            "volume": total_l <= 2.0,
            "carnot_fraction_10pct": electric_eta / eta_c >= 0.10,
            "carnot_fraction_15pct": electric_eta / eta_c >= 0.15,
            "passes_floor": target_dc_w >= 10.0 and total_l <= 2.0 and electric_eta / eta_c >= 0.10,
            "passes_preferred": target_dc_w >= 10.0 and total_l <= 2.0 and electric_eta / eta_c >= 0.15,
        },
    }


def transport_anchor_diagnostic(
    measured_flux_l_m2_h: float = 56.69,
    latent_heat_j_kg: float = 2.358e6,
    benchmark_power_density_w_m2: float = 34.05,
    benchmark_efficiency: float = 0.0472,
    stages: int = 38,
) -> dict[str, float]:
    """Detect an invalid shortcut: combining unrelated measured/modelled anchors.

    The measured 56.69 L m^-2 h^-1 is a single-stage experimental flux, while
    34.05 W m^-2 and 4.72% are 38-stage model outputs. If they are naively
    combined as if they described the same loaded operating point, the implied
    latent-heat recovery exceeds the ideal 1-1/N simple-effect benchmark. That
    flags a normalization/operating-condition mismatch rather than new physics.
    """
    mass_flux_kg_m2_s = measured_flux_l_m2_h / 3600.0
    latent_heat_flux_w_m2 = mass_flux_kg_m2_s * latent_heat_j_kg
    benchmark_source_heat_w_m2 = benchmark_power_density_w_m2 / benchmark_efficiency
    implied_recovery = 1.0 - benchmark_source_heat_w_m2 / latent_heat_flux_w_m2
    simple_n_effect_recovery = 1.0 - 1.0 / stages
    return {
        "mass_flux_kg_m2_s": mass_flux_kg_m2_s,
        "latent_heat_flux_w_m2": latent_heat_flux_w_m2,
        "benchmark_source_heat_w_m2": benchmark_source_heat_w_m2,
        "naive_implied_latent_heat_recovery": implied_recovery,
        "ideal_simple_n_effect_recovery": simple_n_effect_recovery,
        "recovery_gap": implied_recovery - simple_n_effect_recovery,
    }


def sweep() -> dict[str, object]:
    cases = []
    for scenario in SCENARIOS.values():
        for th_c, tc_c in TEMPERATURE_CASES_C:
            for stages in STAGE_COUNTS:
                cases.append(audit_case(scenario, th_c, tc_c, stages))
    return {
        "model": "R075 TOEC source-to-electric/package audit",
        "evidence_labels": {
            "56.69_L_m2_h": "published experiment; single-stage transport anchor only",
            "34.05_W_m2_and_4.72pct": "published 2025 model; 38-stage 80/40 benchmark",
            "scenario_packaging_parameters": "our free screening assumptions; sensitivity required",
        },
        "scenarios": {k: asdict(v) for k, v in SCENARIOS.items()},
        "transport_anchor_diagnostic": transport_anchor_diagnostic(),
        "cases": cases,
    }


def write_reference(path: str | Path) -> None:
    Path(path).write_text(json.dumps(sweep(), indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/r075-toec-sweep.json")
    args = parser.parse_args()
    write_reference(args.output)
