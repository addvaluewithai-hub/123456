from __future__ import annotations

from dataclasses import dataclass, asdict
import json
import math


R_GAS = 8.314462618
M_WATER_KG_PER_MOL = 0.01801528


@dataclass(frozen=True)
class EvosmAssumptions:
    target_net_power_w: float = 10.0
    measured_large_area_power_density_w_m2: float = 0.66
    measured_small_area_power_density_w_m2: float = 8.5
    membrane_thickness_m: float = 100e-6
    package_volume_m3: float = 2e-3
    favorable_evaporation_resource_w_m2: float = 10.49
    ambient_temperature_k: float = 298.15
    relative_humidity: float = 0.50
    pro_pressure_pa: float = 5e6
    water_density_kg_m3: float = 1000.0


def required_membrane_area(power_w: float, power_density_w_m2: float) -> float:
    if power_w <= 0 or power_density_w_m2 <= 0:
        raise ValueError("power and power density must be positive")
    return power_w / power_density_w_m2


def membrane_solid_volume_m3(area_m2: float, thickness_m: float) -> float:
    if area_m2 <= 0 or thickness_m <= 0:
        raise ValueError("area and thickness must be positive")
    return area_m2 * thickness_m


def stack_pitch_limit_m(package_volume_m3: float, area_m2: float) -> float:
    """Absolute average repeat pitch if all required active area must fit in package volume."""
    if package_volume_m3 <= 0 or area_m2 <= 0:
        raise ValueError("volume and area must be positive")
    return package_volume_m3 / area_m2


def required_power_density_for_pitch(
    target_power_w: float, package_volume_m3: float, stack_pitch_m: float
) -> float:
    """Power density needed if active area packs at area/V = 1/pitch."""
    if target_power_w <= 0 or package_volume_m3 <= 0 or stack_pitch_m <= 0:
        raise ValueError("magnitudes must be positive")
    max_area_m2 = package_volume_m3 / stack_pitch_m
    return target_power_w / max_area_m2


def humidity_specific_exergy_j_kg(relative_humidity: float, temperature_k: float) -> float:
    """Ideal isothermal water-vapor chemical-potential drop RT ln(1/RH), per kg water."""
    if not 0 < relative_humidity < 1:
        raise ValueError("relative humidity must lie between 0 and 1")
    if temperature_k <= 0:
        raise ValueError("temperature must be positive")
    molar_j = R_GAS * temperature_k * math.log(1.0 / relative_humidity)
    return molar_j / M_WATER_KG_PER_MOL


def ideal_evaporation_mass_flow_kg_h(power_w: float, specific_exergy_j_kg: float) -> float:
    if power_w <= 0 or specific_exergy_j_kg <= 0:
        raise ValueError("magnitudes must be positive")
    return power_w * 3600.0 / specific_exergy_j_kg


def pro_water_flow_kg_h(power_w: float, pressure_pa: float, density_kg_m3: float = 1000.0) -> float:
    """Ideal water throughput for hydraulic output P = ΔP * volumetric flow."""
    if power_w <= 0 or pressure_pa <= 0 or density_kg_m3 <= 0:
        raise ValueError("magnitudes must be positive")
    hydraulic_specific_work_j_kg = pressure_pa / density_kg_m3
    return power_w * 3600.0 / hydraulic_specific_work_j_kg


def reference_envelope(parasitic_fraction: float = 0.0) -> dict[str, float | dict[str, float]]:
    p = EvosmAssumptions()
    if not 0 <= parasitic_fraction < 1:
        raise ValueError("parasitic_fraction must be in [0, 1)")

    gross_w = p.target_net_power_w / (1.0 - parasitic_fraction)
    area = required_membrane_area(gross_w, p.measured_large_area_power_density_w_m2)
    solid_v = membrane_solid_volume_m3(area, p.membrane_thickness_m)
    pitch_limit = stack_pitch_limit_m(p.package_volume_m3, area)
    gap_budget = pitch_limit - p.membrane_thickness_m
    source_area = gross_w / p.favorable_evaporation_resource_w_m2
    specific_exergy = humidity_specific_exergy_j_kg(p.relative_humidity, p.ambient_temperature_k)
    ideal_water = ideal_evaporation_mass_flow_kg_h(gross_w, specific_exergy)
    pro_water = pro_water_flow_kg_h(gross_w, p.pro_pressure_pa, p.water_density_kg_m3)
    pro_specific = p.pro_pressure_pa / p.water_density_kg_m3

    pitch_cases = {}
    for pitch_mm in (0.25, 0.50, 1.00):
        pitch_m = pitch_mm * 1e-3
        pd_req = required_power_density_for_pitch(gross_w, p.package_volume_m3, pitch_m)
        pitch_cases[f"{pitch_mm:.2f}mm"] = {
            "required_power_density_w_m2": pd_req,
            "improvement_vs_measured_large_area": pd_req / p.measured_large_area_power_density_w_m2,
        }

    return {
        "assumptions": asdict(p),
        "parasitic_fraction": parasitic_fraction,
        "gross_power_required_w": gross_w,
        "measured_scale_degradation_factor": p.measured_small_area_power_density_w_m2 / p.measured_large_area_power_density_w_m2,
        "required_membrane_area_m2": area,
        "membrane_solid_volume_l": solid_v * 1000.0,
        "membrane_solid_fraction_of_2l": solid_v / p.package_volume_m3,
        "absolute_stack_pitch_limit_um": pitch_limit * 1e6,
        "nonmembrane_pitch_budget_um": gap_budget * 1e6,
        "pitch_cases": pitch_cases,
        "ideal_evaporation_source_area_m2": source_area,
        "membrane_to_source_area_ratio": area / source_area,
        "measured_electric_to_resource_areal_ratio": p.measured_large_area_power_density_w_m2 / p.favorable_evaporation_resource_w_m2,
        "rh50_specific_exergy_kj_kg": specific_exergy / 1000.0,
        "ideal_evaporation_mass_flow_kg_h": ideal_water,
        "pro_50bar_ideal_water_flow_kg_h": pro_water,
        "pro_50bar_fraction_of_rh50_specific_exergy": pro_specific / specific_exergy,
        "pro_to_ideal_exergy_water_flow_ratio": pro_water / ideal_water,
    }


def main() -> None:
    print(json.dumps(reference_envelope(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
