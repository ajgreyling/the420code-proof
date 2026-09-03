# The Flip — Pre-Freeze Source Audit v1.0

**The 420 Code · Studio G, Strand, Cape Town · 1 September 2026**
**Scope: every measured number the Flip paper touches, audited against the source of record. Source of record: CODATA 2022 (the current adjustment; CODATA 2026 does not yet exist), tables as published by NIST. Where a corpus instrument is already frozen, nothing in it is edited — corrections stand beside, in the house's erratum pattern.**

---

## The audit table

| Quantity | Corpus carried | Source of record (named line, CODATA 2022) | Audited value | Verdict |
|---|---|---|---|---|
| Δ_meas central | 2.530988574 | m_n/m_e = 1838.68366200(74); m_p/m_e = 1836.152673426(32); subtraction | **2.530988574 exactly** | ✓ CONFIRMED — the corpus central *is* the CODATA-2022 ratio difference, to the last digit |
| u(Δ_meas) | written "(74)" after a 9-decimal value → reads 7.4×10⁻⁸ | m_n/m_e's (74) sits on an **8-decimal** display → 7.4×10⁻⁷; combined with m_p/m_e's 3.2×10⁻⁸ | **7.41×10⁻⁷ mₑ = 0.293 ppm** | ✗ DECADE SLIP, mechanism now proven (Finding F1) |
| Firing of KS-NPP.1 | 7.24σ (frozen 2 Aug) | δ_needed / audited bar = 5.3590×10⁻⁶ / 7.407×10⁻⁷ | **7.235σ** | ✓ CONFIRMED — the frozen 7.24σ was computed on the true bar |
| Landing of the realised row | −0.005σ | residual −3.65×10⁻⁹ / audited bar | **−0.0049σ** | ✓ CONFIRMED |
| α | neutron.docx used 7.2973525693×10⁻³ (CODATA 2018) | CODATA 2022: α = 7.2973525643(11)×10⁻³; α⁻¹ = 137.035999177(21) | vintage named for freeze | ✓ row insensitive (Finding F3); corpse keeps its own vintage |
| u(m_p/m_e) | 3.2×10⁻⁸ | m_p/m_e = 1836.152673426(32) | 3.2×10⁻⁸ | ✓ CONFIRMED — proton elimination **121,576σ** |
| B_d (deuteron binding) | reviewer: 2,224,566.362 ± 0.373 eV | CODATA-2022 mass triplet: m_n = 1.00866491606(40) u, m_p = 1.0072764665789(83) u, m_d = 2.013553212544(15) u; conversion 931.4941037 MeV/u self-consistent | **2,224,566.362 ± 0.373 eV** | ✓ CONFIRMED to the reviewer's digit |
| KS-FLIP.3 truncation piece | ~3.9×10⁻⁸, "five percent of bar", ~0.02 eV | α³·Δ_bare/(8π) at audited bar | **3.913×10⁻⁸ = 5.28% of bar = 0.0200 eV** | ✓ CONFIRMED; adjudication ≈ 19× better B_d metrology |
| Elimination window | [22.10, 29.18] | α²·Δ_bare/(δ_needed ± bar), audited bar | **[22.096, 29.183]**; supports under N = s·4·π: [1.758, 2.322] | ✓ CONFIRMED — only support 2 survives |
| 9π candidate | +0.8σ, no construction | residual +5.92×10⁻⁷ / audited bar | **+0.80σ**; separation from 8π reaches ~2.4σ at 3× bar improvement | ✓ CONFIRMED |
| Flip quantum | 2.74 eV | Δ_bare·f2·mₑc² (the cost) vs δ_needed·mₑc² (the gap) | cost **2.7403 eV**; gap 2.7385 eV (the reviewer's 2.738) | ✓ noted for the record; moot — no observable (§G) |

## Findings

**F1 — The (74), solved at source.** The corpus's measured line came from subtracting the two CODATA-2022 ratios: 1838.68366200 − 1836.152673426 = 2.530988574, exact. The "(74)" was carried over verbatim from m_n/m_e = 1838.68366200(74) — where it sits on an eight-decimal display and means 7.4×10⁻⁷. The subtraction produced a nine-decimal central, and the unmoved parenthetical silently became 7.4×10⁻⁸: right digits, right uncertainty digits, wrong decade by exactly the one decimal the subtraction added. Consequence, now closed: the corpus's "two bars" — the (74) and the ~0.29 ppm firing bar — were **one bar all along**, read at two decades. The honest line, decade-safe: **Δ_meas = 2.530988574, u = 7.4×10⁻⁷ (0.29 ppm), CODATA 2022, from m_n/m_e = 1838.68366200(74) and m_p/m_e = 1836.152673426(32).** Cross-check route — (m_n−m_p) = 1.38844948(40)×10⁻³ u divided by m_e — gives 7.29×10⁻⁷, agreeing within the display rounding of the published parentheticals; the ratio route is adopted because the frozen quantity is the ratio difference.

**F2 — The frozen firing stands, exactly.** KS-NPP.1's 7.24σ recomputes as 7.235σ on the audited bar: the 2-August freeze used the true uncertainty. The corpse needs nothing and gets nothing. One display slip inside the old freeze docs — "0.288 ppm" where the bar is 0.2926 ppm — is a label error only (the σ quoted was computed on the right bar); its correction stands beside the frozen instruments, never inside them.

**F3 — α vintage.** CODATA 2018 → 2022 moves α by −5.0×10⁻¹², shifting Δ_bare by −5.8×10⁻¹² and the realised row at the twelfth decimal. The row is vintage-insensitive at any displayed precision; the freeze names CODATA 2022 (7.2973525643(11)×10⁻³) for cleanliness. The 2-August corpse keeps its own 2018 vintage, as frozen things do.

**F4 — The last displayed digit of the frozen row (needs the author's ruling).** At full precision the quotient form gives 2.5309885703518 (α-2022) and the subtractive form 2.5309885703405; they differ by ~1.1×10⁻¹¹ — one thirty-seven-thousandth of the bar, physically nothing — but the ten-decimal display sits exactly on the rounding boundary: the quotient rounds to …5704, the subtractive to …5703. The v0.1/v0.2 display "2.5309885703" matches the subtractive rounding while the paper wears the quotient. Recommendation: freeze the **expression** — Δ_real = Δ_bare/(1 + α²/8π), α = CODATA-2022 — as the claim, display it at eleven decimals, **2.53098857035**, and state KS-FLIP.1's kill test against the expression, not the display. The author rules.

**F5 — Corrections to propagate at conversion (frozen items untouched).** neutron.docx: the "(74)" line and the "72.4σ with (74) error" line inherit F1; the "223σ" proton figure inherits the named-bar correction (121,576σ at u(m_p/m_e) = 3.2×10⁻⁸). WP-FLIP.1 §1's "(74)"; §7's deuteron-bar sentence (already superseded by the §G identity ruling). The reviewer's N-formula display slip (N = α²Δ_bare/δ_needed) is corrected wherever the elimination is quoted. All of these land in the papers' next versions and in an erratum note beside anything already hashed; nothing frozen is edited.

**F6 — What did not move.** Every structural quantity — the construction, the supports, the grades, the window's integer survivors, the 9π structural death, the ruling of §G — is untouched by the audit. The audit moved displays and named lines; it moved no claims.

---

*Audit run by the desk, 1 September 2026, on the author's word. Sources: CODATA 2022 adjustment (NIST); all arithmetic recomputed at 28-digit precision, both α vintages, both uncertainty routes.*
