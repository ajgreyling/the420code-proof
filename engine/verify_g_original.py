# Predictions Ø — Verification Code
#
# One axiom. One measured input (alpha). Five predictions. Zero free parameters.
# This script verifies every numerical claim in the book. It runs in under a
# second on any modern computer. Requires only the Python standard library
# (math), no external dependencies.
#
# To run: python3 verify.py
#
# Copyleft 2026. Don't be a cunt. Be kind.
# the420code.org
#
# ---------------------------------------------------------------------------
# THIS FILE IS G's PUBLISHED SCRIPT, reproduced VERBATIM from Ø Predictions,
# Appendix B ("The complete verification code"), recovered from the mirrored
# PDF (mirror/pdf/Predictions.pdf). PDF line-wrap and embedded page numbers were
# undone; the code, comments, constants, and formulas are exactly as published.
# The engine's own engine/verify.py is a *structured* reconstruction of this same
# script (it returns data instead of printing); engine/test_verify_parity.py
# asserts the two agree to 1e-12. Keep THIS file faithful to the page — do not
# "improve" it. ---------------------------------------------------------------

import math

# ---------------------------------------------------------------------------
# Measured inputs (CODATA 2018/2022)
# ---------------------------------------------------------------------------
alpha = 7.2973525693e-3   # fine-structure constant (dimensionless)
hbar = 1.054571817e-34    # Planck's constant over 2pi (J·s)
c = 2.99792458e8          # speed of light (m/s) — exact by SI definition
m_e = 9.1093837015e-31    # electron mass (kg)
H0_kmsMpc = 73.8          # Hubble constant (km/s/Mpc), representative local value
Mpc_m = 3.0857e22         # one megaparsec in metres

# ---------------------------------------------------------------------------
# Part I — The Proton's Weight
# ---------------------------------------------------------------------------
# Formula: m_p/m_e = 21² × 4 + 21 × 3 + 3² + α × 21 × (1 − 1/(84π))
#          + α² × 21 × 16 / 1836
print("Part I — Proton-to-electron mass ratio")
static = 21**2 * 4 + 21 * 3 + 3**2
first_order = alpha * 21 * (1 - 1/(84*math.pi))
second_order = alpha**2 * 21 * 16 / 1836
mp_me_predicted = static + first_order + second_order
mp_me_measured = 1836.152673426
residual_ppb = (mp_me_predicted - mp_me_measured) / mp_me_measured * 1e9
print(f"  Predicted: {mp_me_predicted:.9f}")
print(f"  Measured : {mp_me_measured:.9f}")
print(f"  Residual : {residual_ppb:.3f} ppb")
print()

# ---------------------------------------------------------------------------
# Part II — The Strength of Gravity
# ---------------------------------------------------------------------------
# Formula: G = α²¹ × (1 + 1/π) × ħc / m_e²
print("Part II — Gravitational constant")
alpha_G = alpha**21 * (1 + 1/math.pi)
G_predicted = alpha_G * hbar * c / m_e**2
G_measured = 6.67430e-11
discrepancy_percent = (G_predicted - G_measured) / G_measured * 100
print(f"  Predicted: {G_predicted:.4e} N·m²/kg²")
print(f"  Measured : {G_measured:.4e}")
print(f"  Residual : {discrepancy_percent:.2f}%")
print()

# ---------------------------------------------------------------------------
# Part III — The Neutron's Whisper
# ---------------------------------------------------------------------------
# Formula: (m_n − m_p)/m_e = 3 × (1 − 1/(2π)) + α × (1 + 1/(2π))
print("Part III — Neutron-proton mass difference")
static_np = 3 * (1 - 1/(2*math.pi))
dynamic_np = alpha * (1 + 1/(2*math.pi))
np_diff_predicted = static_np + dynamic_np
np_diff_measured = 2.5309883
residual_ppm = (np_diff_predicted - np_diff_measured) / np_diff_measured * 1e6
print(f"  Predicted: {np_diff_predicted:.10f}")
print(f"  Measured : {np_diff_measured:.10f}")
print(f"  Residual : {residual_ppm:.2f} ppm")
print()

# ---------------------------------------------------------------------------
# Part IV — The Floor of Gravity
# ---------------------------------------------------------------------------
# Formula: a_0 = C_S² × cH_0 / (2π)
# where C_S² = 2 ln(sec(½) + tan(½)) ≈ 1.0445 (NOT the fine structure constant)
print("Part IV — MOND acceleration scale + Hubble prediction")
C_S2 = 2 * math.log(1/math.cos(0.5) + math.tan(0.5))  # geometric correction, ≈ 1.0445
H0 = H0_kmsMpc * 1000 / Mpc_m   # H_0 in inverse seconds
cH0 = c * H0
a0_predicted = C_S2 * cH0 / (2 * math.pi)
a0_measured = 1.20e-10
discrepancy_a0 = (a0_predicted - a0_measured) / a0_measured * 100
# Inverse: predict H_0 from measured a_0
H0_inverse_Hz = 2 * math.pi * a0_measured / (C_S2 * c)
H0_inverse_kmsMpc = H0_inverse_Hz * Mpc_m / 1000
print(f"  C_S²          : {C_S2:.4f}")
print(f"  a_0 predicted : {a0_predicted:.3e} m/s² (at H_0 = {H0_kmsMpc} km/s/Mpc)")
print(f"  a_0 measured  : {a0_measured:.3e}")
print(f"  Residual      : {discrepancy_a0:.2f}%")
print(f"  H_0 predicted : {H0_inverse_kmsMpc:.1f} km/s/Mpc (from measured a_0)")
print()

# ---------------------------------------------------------------------------
# Part V — The Clock (Dark Sector Partition)
# ---------------------------------------------------------------------------
# Formula: tau/t_H = 6/21, then exponential decay kernel for dark matter fraction
print("Part V — Dark sector partition")
tau_over_tH = 6/21
t_over_tau = 1/tau_over_tH   # 21/6 = 3.5
dark_matter_fraction_of_dark = tau_over_tH * (1 - math.exp(-t_over_tau))
dark_energy_fraction_of_dark = 1 - dark_matter_fraction_of_dark
DE_total = dark_energy_fraction_of_dark * 20/21 * 100
DM_total = dark_matter_fraction_of_dark * 20/21 * 100
Vis_total = (1/21) * 100
# Planck 2018 observed
DE_obs, DM_obs, Vis_obs = 68.89, 26.07, 4.86
print(f"  Dark energy : {DE_total:.2f}% (observed {DE_obs}%, residual {abs(DE_total-DE_obs)/DE_obs*100:.2f}%)")
print(f"  Dark matter : {DM_total:.2f}% (observed {DM_obs}%, residual {abs(DM_total-DM_obs)/DM_obs*100:.2f}%)")
print(f"  Visible     : {Vis_total:.2f}% (observed {Vis_obs}%, residual {abs(Vis_total-Vis_obs)/Vis_obs*100:.2f}%)")
print(f"  DE/DM ratio : {DE_total/DM_total:.4f} (observed {DE_obs/DM_obs:.4f})")
print()

print("=" * 60)
print("All five predictions verified. Zero free parameters.")
print("=" * 60)
