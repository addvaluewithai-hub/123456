from __future__ import annotations

from dataclasses import dataclass
import math
import cmath


@dataclass(frozen=True)
class WetCorePoint:
    hydraulic_radius_m: float = 0.25e-3
    frequency_hz: float = 5.0
    mean_pressure_pa: float = 10e5
    tc_k: float = 293.15
    th_k: float = 333.15
    alpha_m2_s: float = 2.2e-6
    vapor_diffusivity_m2_s: float = 2.6e-6


def carnot_efficiency(tc_k: float, th_k: float) -> float:
    if th_k <= tc_k:
        raise ValueError("th_k must be greater than tc_k")
    return 1.0 - tc_k / th_k


def penetration_depth(diffusivity_m2_s: float, frequency_hz: float) -> float:
    if diffusivity_m2_s <= 0 or frequency_hz <= 0:
        raise ValueError("diffusivity and frequency must be positive")
    return math.sqrt(diffusivity_m2_s / (math.pi * frequency_hz))


def first_mode_relaxation_time(hydraulic_radius_m: float, diffusivity_m2_s: float) -> float:
    if hydraulic_radius_m <= 0 or diffusivity_m2_s <= 0:
        raise ValueError("radius and diffusivity must be positive")
    return 4.0 * hydraulic_radius_m**2 / (math.pi**2 * diffusivity_m2_s)


def complex_diffusion_factor(hydraulic_radius_m: float, penetration_depth_m: float) -> complex:
    """Rott-style slab diffusion screen used for pre-prototype ranking.

    f = tanh(z)/z, z=(1+i) r_h/delta
    This is a screening model, not a substitute for calibrated hardware data.
    """
    if hydraulic_radius_m <= 0 or penetration_depth_m <= 0:
        raise ValueError("radius and penetration depth must be positive")
    z = (1.0 + 1.0j) * hydraulic_radius_m / penetration_depth_m
    return cmath.tanh(z) / z


def phase_deg(value: complex) -> float:
    return math.degrees(cmath.phase(value))


def required_effective_conductance_density(
    p_dc_w: float,
    carnot_fraction: float,
    tc_k: float,
    th_k: float,
    total_hx_volume_m3: float,
    local_delta_t_k: float,
    hx_count: int = 2,
) -> float:
    """Return required usable Re{G*}/V in W m^-3 K^-1.

    Uses the current Energy Lab screening ledger:
    Q_hot = P_dc / (eta_Carnot * carnot_fraction)
    G_eff/V = hx_count * Q_hot / (V_HX,total * DeltaT_local)
    """
    if p_dc_w <= 0 or carnot_fraction <= 0 or total_hx_volume_m3 <= 0 or local_delta_t_k <= 0:
        raise ValueError("all magnitudes must be positive")
    eta_c = carnot_efficiency(tc_k, th_k)
    q_hot_w = p_dc_w / (eta_c * carnot_fraction)
    return hx_count * q_hot_w / (total_hx_volume_m3 * local_delta_t_k)


def frozen_r073_point() -> dict[str, float]:
    p = WetCorePoint()
    delta_th = penetration_depth(p.alpha_m2_s, p.frequency_hz)
    delta_mass = penetration_depth(p.vapor_diffusivity_m2_s, p.frequency_hz)
    f_th = complex_diffusion_factor(p.hydraulic_radius_m, delta_th)
    f_mass = complex_diffusion_factor(p.hydraulic_radius_m, delta_mass)
    return {
        "carnot_efficiency": carnot_efficiency(p.tc_k, p.th_k),
        "thermal_penetration_depth_m": delta_th,
        "mass_penetration_depth_m": delta_mass,
        "thermal_relaxation_time_s": first_mode_relaxation_time(p.hydraulic_radius_m, p.alpha_m2_s),
        "mass_relaxation_time_s": first_mode_relaxation_time(p.hydraulic_radius_m, p.vapor_diffusivity_m2_s),
        "thermal_factor_real": f_th.real,
        "thermal_factor_phase_deg": phase_deg(f_th),
        "mass_factor_real": f_mass.real,
        "mass_factor_phase_deg": phase_deg(f_mass),
    }


if __name__ == "__main__":
    for key, value in frozen_r073_point().items():
        print(f"{key}: {value:.8g}")
