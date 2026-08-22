from __future__ import annotations

from dataclasses import dataclass
import math

from .toec import carnot_efficiency, stage_factor


@dataclass(frozen=True)
class FourStageMeasurement:
    """Measured/calibrated module quantities used only for a scale projection.

    Values here are inputs. Supplying them does not make them bench evidence.
    The caller must preserve the evidence label of every field.
    """

    gross_hydraulic_power_density_w_m2: float
    hydraulic_efficiency: float
    header_pressure_loss_fraction: float
    membrane_area_density_m2_per_l: float
    thermal_network_specific_duty_w_per_l: float
    stage_dead_volume_l: float
    hydraulic_to_electric_efficiency: float
    electric_parasitic_w: float
    pto_volume_l: float
    housing_volume_l: float


# Predeclared R075 interpolation ratios. These are model assumptions, not data.
R075_ETA_SCALE_4_TO_16 = stage_factor(16, 0.64) / stage_factor(4, 0.64)
R075_PDEN_SCALE_4_TO_16 = stage_factor(16, 0.50) / stage_factor(4, 0.50)


def project_16_from_4(
    measurement: FourStageMeasurement,
    target_dc_w: float = 10.0,
    hot_c: float = 80.0,
    cold_c: float = 40.0,
) -> dict[str, float | bool]:
    """Project a 4-stage calibrated point to N=16 using the frozen R075 law.

    This function intentionally does not fit a new stage law. It is a
    falsification bridge: measured 4-stage quantities can collapse the R075
    optimistic/conservative package envelope, while the 4->16 interpolation
    remains explicitly modelled and must carry a scale-law uncertainty.
    """
    m = measurement
    positive = [
        m.gross_hydraulic_power_density_w_m2,
        m.hydraulic_efficiency,
        m.membrane_area_density_m2_per_l,
        m.thermal_network_specific_duty_w_per_l,
        m.stage_dead_volume_l,
        m.hydraulic_to_electric_efficiency,
        m.pto_volume_l,
        m.housing_volume_l,
        target_dc_w,
    ]
    if any(v <= 0 for v in positive):
        raise ValueError("positive inputs required")
    if not 0 <= m.header_pressure_loss_fraction < 1:
        raise ValueError("header loss fraction must be in [0,1)")
    if m.electric_parasitic_w < 0:
        raise ValueError("electric parasitic must be non-negative")

    pden16 = m.gross_hydraulic_power_density_w_m2 * R075_PDEN_SCALE_4_TO_16
    eta16 = m.hydraulic_efficiency * R075_ETA_SCALE_4_TO_16
    gross_hydraulic_w = (target_dc_w + m.electric_parasitic_w) / (
        m.hydraulic_to_electric_efficiency * (1 - m.header_pressure_loss_fraction)
    )
    area_m2 = gross_hydraulic_w / pden16
    source_heat_w = gross_hydraulic_w / eta16

    membrane_l = area_m2 / m.membrane_area_density_m2_per_l
    thermal_l = source_heat_w / m.thermal_network_specific_duty_w_per_l
    stage_l = 16 * m.stage_dead_volume_l
    total_l = membrane_l + thermal_l + stage_l + m.pto_volume_l + m.housing_volume_l

    electric_efficiency = target_dc_w / source_heat_w
    frac_carnot = electric_efficiency / carnot_efficiency(hot_c, cold_c)
    return {
        "projected_pden16_w_m2": pden16,
        "projected_eta16": eta16,
        "gross_hydraulic_w": gross_hydraulic_w,
        "membrane_area_m2": area_m2,
        "source_heat_w": source_heat_w,
        "membrane_volume_l": membrane_l,
        "thermal_network_volume_l": thermal_l,
        "stage_dead_volume_l": stage_l,
        "total_volume_l": total_l,
        "electric_efficiency": electric_efficiency,
        "fraction_of_carnot_electric": frac_carnot,
        "passes_2l": total_l <= 2.0,
        "passes_15pct_carnot": frac_carnot >= 0.15,
        "passes_preferred": total_l <= 2.0 and frac_carnot >= 0.15,
    }


def conservative_packaging_boundary(
    membrane_area_m2: float = 0.86805506,
    source_heat_w: float = 528.68324,
    fixed_volume_l: float = 0.95371429,
    total_volume_limit_l: float = 2.0,
    membrane_area_density_m2_per_l: float | None = None,
    thermal_network_specific_duty_w_per_l: float | None = None,
) -> dict[str, float]:
    """Invert the conservative R075 N=16 volume ledger.

    Exactly one of membrane_area_density_m2_per_l or
    thermal_network_specific_duty_w_per_l may be supplied to calculate the
    minimum value of the other. With neither supplied, return absolute minima
    obtained if the other subsystem had zero volume.
    """
    available = total_volume_limit_l - fixed_volume_l
    if available <= 0:
        raise ValueError("no volume remains for membrane+thermal network")
    if membrane_area_density_m2_per_l is not None and thermal_network_specific_duty_w_per_l is not None:
        raise ValueError("supply at most one packaging density")

    if membrane_area_density_m2_per_l is None and thermal_network_specific_duty_w_per_l is None:
        return {
            "available_membrane_plus_thermal_l": available,
            "absolute_min_membrane_area_density_m2_per_l": membrane_area_m2 / available,
            "absolute_min_thermal_network_specific_duty_w_per_l": source_heat_w / available,
        }

    if membrane_area_density_m2_per_l is not None:
        remaining = available - membrane_area_m2 / membrane_area_density_m2_per_l
        if remaining <= 0:
            return {"required_thermal_network_specific_duty_w_per_l": math.inf}
        return {"required_thermal_network_specific_duty_w_per_l": source_heat_w / remaining}

    remaining = available - source_heat_w / float(thermal_network_specific_duty_w_per_l)
    if remaining <= 0:
        return {"required_membrane_area_density_m2_per_l": math.inf}
    return {"required_membrane_area_density_m2_per_l": membrane_area_m2 / remaining}


def rss_relative_uncertainty(*relative_1sigma: float) -> float:
    """Root-sum-square relative uncertainty for independent small errors."""
    if any(v < 0 for v in relative_1sigma):
        raise ValueError("uncertainties must be non-negative")
    return math.sqrt(sum(v * v for v in relative_1sigma))
