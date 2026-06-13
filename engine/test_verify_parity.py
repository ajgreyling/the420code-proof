#!/usr/bin/env python3
"""Parity test: the structured engine.verify.compute() must equal G's published script.

Two independent computations of the same five numbers:
  1. engine.verify.compute()        — the structured reconstruction (returns data)
  2. engine.verify_g_original       — G's verbatim Appendix B script (prints, run as a module)

This test recomputes each prediction inline from G's exact formulas/constants and asserts the
structured values agree to 1e-12. If engine/verify.py ever drifts from G's published math, this
fails — keeping the executable claim honest.

    python3 -m engine.test_verify_parity     # prints PASS/FAIL, exit 0/1
"""
from __future__ import annotations

import math

from . import verify


def _g_values() -> dict[str, float]:
    """Recompute the five headline numbers directly from G's Appendix B (independent path)."""
    alpha = 7.2973525693e-3
    hbar = 1.054571817e-34
    c = 2.99792458e8
    m_e = 9.1093837015e-31
    H0 = 73.8 * 1000 / 3.0857e22

    mp_me = (21**2 * 4 + 21 * 3 + 3**2
             + alpha * 21 * (1 - 1/(84*math.pi))
             + alpha**2 * 21 * 16 / 1836)
    G = alpha**21 * (1 + 1/math.pi) * hbar * c / m_e**2
    npd = 3 * (1 - 1/(2*math.pi)) + alpha * (1 + 1/(2*math.pi))
    C_S2 = 2 * math.log(1/math.cos(0.5) + math.tan(0.5))
    a0 = C_S2 * c * H0 / (2 * math.pi)
    tau = 6/21
    dm = tau * (1 - math.exp(-1/tau))
    de = 1 - dm
    de_dm = (de * 20/21) / (dm * 20/21)
    return {
        "proton_electron_mass_ratio": mp_me,
        "gravitational_constant": G,
        "neutron_proton_mass_diff": npd,
        "mond_acceleration_a0": a0,
        "dark_sector_de_dm_ratio": de_dm,
    }


def main() -> int:
    g = _g_values()
    structured = {p.key: p.predicted for p in verify.compute()}
    ok = True
    print("PARITY — structured engine.verify vs G's published Appendix B\n")
    for key, gval in g.items():
        sval = structured.get(key)
        rel = abs(sval - gval) / abs(gval) if gval else abs(sval)
        good = rel < 1e-12
        ok &= good
        print(f"  [{'OK ' if good else 'XX '}] {key:<32} {sval:.12g}  (rel Δ {rel:.1e})")
    print("\n" + ("PASS — reconstruction matches G's script." if ok else "FAIL — drift detected."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
