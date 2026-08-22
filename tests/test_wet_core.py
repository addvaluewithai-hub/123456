import math

from energy_lab.wet_core import (
    WetCorePoint,
    carnot_efficiency,
    penetration_depth,
    complex_diffusion_factor,
    phase_deg,
    required_effective_conductance_density,
)


def test_carnot_matches_r070_screen():
    eta = carnot_efficiency(293.15, 333.15)
    assert math.isclose(eta, 0.120066, rel_tol=5e-4)


def test_r073_intrinsic_phase_is_inside_gate():
    p = WetCorePoint()
    dth = penetration_depth(p.alpha_m2_s, p.frequency_hz)
    dm = penetration_depth(p.vapor_diffusivity_m2_s, p.frequency_hz)
    fth = complex_diffusion_factor(p.hydraulic_radius_m, dth)
    fm = complex_diffusion_factor(p.hydraulic_radius_m, dm)
    assert abs(phase_deg(fth)) < 20.0
    assert abs(phase_deg(fm)) < 20.0


def test_r070_15_percent_carnot_gate():
    # 2 L total package - 0.975 L non-HX allowance = 1.025 L for both HXs.
    g = required_effective_conductance_density(
        p_dc_w=10.0,
        carnot_fraction=0.15,
        tc_k=293.15,
        th_k=333.15,
        total_hx_volume_m3=1.025e-3,
        local_delta_t_k=10.0,
        hx_count=2,
    )
    assert 107e3 < g < 110e3
