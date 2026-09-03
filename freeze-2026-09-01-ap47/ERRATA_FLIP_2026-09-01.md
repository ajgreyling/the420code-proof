# Errata — corrections standing beside frozen instruments (1 September 2026)

**The 420 Code · Studio G · AP47 conversion-day ledger. Nothing frozen is edited; every correction below stands beside its instrument. Each was found by the house's own audits or reviewers before anchoring, and AP47 carries the corrected figures with sources named.**

## neutron.docx (origin note, frozen 2eba7533…)

1. The measured line is written "2.530988574(74)". The central value is exact (it is CODATA 2022's m_n/m_e − m_p/m_e to the digit), but the parenthetical, carried over from m_n/m_e = 1838.68366200(74) — an eight-decimal display where (74) means 7.4×10⁻⁷ — landed on a nine-decimal value, silently reading as 7.4×10⁻⁸. **Correct uncertainty: u = 7.4×10⁻⁷ (0.29 ppm).** Consequence: the note's "+72.4σ with (74) error" inherits the slip; the operative firing figure was always the 7.24σ computed on the true bar.
2. "223σ" for the proton exclusion used an unnamed coarser bar. **Correct figure: ≈121,576σ** at u(m_p/m_e) = 3.2×10⁻⁸ (CODATA 2022). The elimination only strengthens.
3. The realised row is displayed there at ten decimals; AP47 freezes the expression at CODATA-2022 α, displayed at eleven (see AP47 section 6 for the rounding-boundary reason).

## WP-FLIP.1 (strategy instrument, frozen c6039917…/fae10ecf…)

4. Section 1 carries the same "(74)" line — same correction as item 1.
5. Section 7's bound-neutron edge ("an order of magnitude and more below current binding-energy precision on the deuteron") is wrong twice — the bar direction, and the observable itself. Superseded by AP47 section 8: the capture-chain identity makes the tabulated neutron mass the free booking always; the binding ruling carries no mass-face observable, declared.
6. Section 9's "touches no locked value anywhere" is superseded as stated in AP47 section 5: no locked value is touched, but the Flip shares AP30's construction and inherits KS-30.2.
7. The "0.288 ppm" bar label in the freeze-era documents is a display slip; the audited bar is 0.2926 ppm. The 7.24σ was computed on the true bar and stands.

## WP-ROAD.1 v1.2 (family instrument)

8. The state table lists "AP45 v0.3 (658402ef…)". No such file exists in the author's archive; **AP45 v0.2.1 is the version of record by the author's word.** The line is corrected at the ROAD's next revision. Standing rule: should any file answering that entry ever surface, its four fence clauses are re-read before anything relies on it.

## Review-note display slip

9. One reviewer note in the session record writes the required divisor as "N = δ_needed/f₂"; the correct formula is **N = α²·Δ_bare/δ_needed** (the number quoted, 25.1499, was computed correctly).

*All corrected figures appear in AP47 with their CODATA-2022 source lines named, and in FLIP_SOURCE_AUDIT_v1_0 with the full derivations.*
