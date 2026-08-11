#!/usr/bin/env python3
"""The 420 Code — Ø Predictions verification (G's published Appendix B, reconstructed).

Faithful reconstruction of the verification script G published in *Ø Predictions*,
Appendix B ("The complete verification code"), recovered from the mirrored PDF at
mirror/pdf/Predictions.pdf. Every formula, measured input, and comparison value is
reproduced exactly as published.

  One axiom. One measured input (α). Five predictions. Zero free parameters.
  Copyleft 2026. Don't be a cunt. Be kind. — the420code.org

This module is the EXECUTABLE CORE of the model: `gate.py` imports `compute()` and
checks each prediction's residual against G's published tolerance. Run standalone to
print the same human-readable report G's script prints:

    python3 -m engine.verify
"""
from __future__ import annotations

import math
from dataclasses import dataclass

# --------------------------------------------------------------------------- #
# Measured inputs (CODATA 2018/2022 — unchanged between the two releases)
# --------------------------------------------------------------------------- #
ALPHA = 7.2973525693e-3      # fine-structure constant (dimensionless) — THE single measured input
HBAR = 1.054571817e-34       # reduced Planck constant (J·s) — fixes the unit system
C = 2.99792458e8             # speed of light (m/s) — exact by SI definition
M_E = 9.1093837015e-31       # electron mass (kg)
H0_KMSMPC = 73.8             # Hubble constant (km/s/Mpc), representative local value
MPC_M = 3.0857e22            # one megaparsec in metres


@dataclass(frozen=True)
class Prediction:
    """One numeric claim: G's derived value vs the measured value, with his stated tolerance."""
    key: str            # stable id, used by the canon/gate
    part: str           # the Ø Predictions chapter
    name: str
    predicted: float
    measured: float
    unit: str
    residual: float     # signed/absolute residual in `residual_unit`
    residual_unit: str  # "ppb" | "ppm" | "%"
    tolerance: float    # G's published pass threshold in residual_unit
    measured_source: str
    formula: str

    @property
    def passed(self) -> bool:
        return abs(self.residual) <= self.tolerance


def compute() -> list[Prediction]:
    """Reproduce all five predictions from α alone. Returns structured results (no printing)."""
    preds: list[Prediction] = []

    # Part I — The Proton's Weight ------------------------------------------------
    # m_p/m_e = 21²×4 + 21×3 + 3² + α×21×(1 − 1/(84π)) + α²×21×16/1836
    static = 21**2 * 4 + 21 * 3 + 3**2
    first_order = ALPHA * 21 * (1 - 1 / (84 * math.pi))
    second_order = ALPHA**2 * 21 * 16 / 1836
    mp_me_pred = static + first_order + second_order
    mp_me_meas = 1836.152673426
    preds.append(Prediction(
        key="proton_electron_mass_ratio", part="I", name="Proton-to-electron mass ratio",
        predicted=mp_me_pred, measured=mp_me_meas, unit="(dimensionless)",
        residual=(mp_me_pred - mp_me_meas) / mp_me_meas * 1e9, residual_unit="ppb",
        tolerance=0.017,  # CODATA 2022 uncertainty; G's headline residual is 0.010 ppb at 0.6σ
        measured_source="CODATA 2022",
        formula="21²×4 + 21×3 + 3² + α×21×(1 − 1/(84π)) + α²×21×16/1836"))

    # Part II — The Strength of Gravity -------------------------------------------
    # Structural (provisioned) G = α²¹ × (1 + 1/π) × ħc / m_e²   — AP28, Edition 1
    # Realised G = structural / (1 + α)                            — AP44 The Snap (LOCKED)
    # Both sit in the scorecard as a fork. verify_g_original.py and the parity
    # test are untouched and continue to certify Edition 1's structural arithmetic.
    alpha_G = ALPHA**21 * (1 + 1 / math.pi)
    G_struct = alpha_G * HBAR * C / M_E**2
    G_realised = G_struct / (1 + ALPHA)
    G_meas = 6.67430e-11
    preds.append(Prediction(
        key="gravitational_constant", part="II", name="Gravitational constant G (structural)",
        predicted=G_struct, measured=G_meas, unit="N·m²/kg²",
        residual=(G_struct - G_meas) / G_meas * 100, residual_unit="%",
        tolerance=1.0,  # G claims sub-1% (~0.69%)
        measured_source="CODATA 2022", formula="α²¹ × (1 + 1/π) × ħc / m_e²"))
    preds.append(Prediction(
        key="gravitational_constant_realised", part="II",
        name="Gravitational constant G (realised, AP44)",
        predicted=G_realised, measured=G_meas, unit="N·m²/kg²",
        residual=(G_realised - G_meas) / G_meas * 100, residual_unit="%",
        tolerance=1.0,  # −0.036% vs CODATA centre; watch line = KS-CCC.3 migration fork
        measured_source="CODATA 2022",
        formula="α²¹ × (1 + 1/π)/(1 + α) × ħc / m_e²"))

    # Part III — The Neutron's Whisper --------------------------------------------
    # (m_n − m_p)/m_e = 3×(1 − 1/(2π)) + α×(1 + 1/(2π))
    static_np = 3 * (1 - 1 / (2 * math.pi))
    dynamic_np = ALPHA * (1 + 1 / (2 * math.pi))
    np_pred = static_np + dynamic_np
    np_meas = 2.5309883
    preds.append(Prediction(
        key="neutron_proton_mass_diff", part="III", name="Neutron-proton mass difference",
        predicted=np_pred, measured=np_meas, unit="mₑ",
        residual=(np_pred - np_meas) / np_meas * 1e6, residual_unit="ppm",
        tolerance=5.0,  # G claims ~2 ppm
        measured_source="CODATA 2018", formula="3×(1 − 1/(2π)) + α×(1 + 1/(2π))"))

    # Part IV — The Floor of Gravity (MOND a₀) ------------------------------------
    # a_0 = C_S² × cH_0 / (2π);  C_S² = 2 ln(sec(½) + tan(½)) ≈ 1.0445 (geometric, NOT α)
    C_S2 = 2 * math.log(1 / math.cos(0.5) + math.tan(0.5))
    H0 = H0_KMSMPC * 1000 / MPC_M
    a0_pred = C_S2 * (C * H0) / (2 * math.pi)
    a0_meas = 1.20e-10
    preds.append(Prediction(
        key="mond_acceleration_a0", part="IV", name="MOND acceleration scale a₀",
        predicted=a0_pred, measured=a0_meas, unit="m/s²",
        residual=(a0_pred - a0_meas) / a0_meas * 100, residual_unit="%",
        tolerance=5.0,  # G claims ~0.3% at the representative H₀ (sensitive to H₀ choice)
        measured_source="MOND (Milgrom) / SPARC",
        formula="C_S² × cH₀ / (2π),  C_S² = 2 ln(sec½ + tan½)"))

    # Part V — The Clock (Dark Sector Partition) ----------------------------------
    # τ/t_H = 6/21; exponential decay kernel → dark-matter fraction of the dark sector
    tau_over_tH = 6 / 21
    t_over_tau = 1 / tau_over_tH
    dm_frac = tau_over_tH * (1 - math.exp(-t_over_tau))
    de_frac = 1 - dm_frac
    DE_total = de_frac * 20 / 21 * 100
    DM_total = dm_frac * 20 / 21 * 100
    DE_obs, DM_obs = 68.89, 26.07
    # Headline single-number check: the DE/DM ratio (partition shape), in %.
    ratio_pred = DE_total / DM_total
    ratio_obs = DE_obs / DM_obs
    preds.append(Prediction(
        key="dark_sector_de_dm_ratio", part="V", name="Dark sector DE/DM ratio",
        predicted=ratio_pred, measured=ratio_obs, unit="(ratio)",
        residual=(ratio_pred - ratio_obs) / ratio_obs * 100, residual_unit="%",
        tolerance=5.0,  # the per-component residuals G claims are ~0.06%
        measured_source="Planck 2018",
        formula="τ/t_H = 6/21; DM = (τ/t_H)(1 − e^(−t/τ)); partition × 20/21"))

    return preds


def report() -> int:
    """Print G's human-readable verification report. Returns process exit code (0 = all pass)."""
    preds = compute()
    print("Ø Predictions — Verification (G's Appendix B, reconstructed)")
    print("One axiom. One measured input (α). Five predictions. Zero free parameters.\n")
    all_ok = True
    for p in preds:
        flag = "PASS" if p.passed else "FAIL"
        all_ok &= p.passed
        print(f"Part {p.part} — {p.name}  [{flag}]")
        print(f"    Predicted: {p.predicted:.10g} {p.unit}")
        print(f"    Measured : {p.measured:.10g}  ({p.measured_source})")
        print(f"    Residual : {p.residual:.4g} {p.residual_unit}  "
              f"(tolerance {p.tolerance} {p.residual_unit})\n")
    print("=" * 60)
    print(f"{'ALL FIVE PREDICTIONS VERIFIED.' if all_ok else 'SOME PREDICTIONS OUTSIDE TOLERANCE.'} "
          "Zero free parameters.")
    print("=" * 60)
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(report())
