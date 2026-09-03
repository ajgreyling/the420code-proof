# Receipt — AP47 verification bundle, freeze anchor, 2026-09-03

**From AJ's hand:** directory `AP47_bundle` (Downloads), delivered by Studio G 1 September 2026,
requested to be frozen at receipt (same standing ask as the AP44 and AP45/AP46 anchors).

## What this anchor is, and is not

**This is a freeze/provenance anchor, not a lock.** It timestamps that the bundle, in this exact
form, existed and was received on this date — matching the `ap44-provenance-anchor-2026-08-1{0,1}`
precedent, which preceded `ap44-locked-2026-08-11` by a separate step. It does **not** assert
"LOCKED," a composite score, or a ceiling ruling — those are the author's own calls to make, and
AP47's own canon audit (`CANON_AUDIT_v1_2.md`, included below) says plainly: *"What remains is the
author's walk of v0.7, and his word."* That walk has not happened yet. No commit or tag on this
repo claims AP47 as locked.

## Contents received and anchored

Stored verbatim, as delivered, under `freeze-2026-09-01-ap47/`. Every file's SHA-256 re-verified
against the bundle's own `SHA256SUMS.txt` immediately before this anchor was made — all entries
`OK`, no mismatch.

| File | Role |
|---|---|
| `AP47_The_Flip_FINAL_v3.md` / `.docx` | The paper as delivered (md canonical; FINAL v1/v2 retained in lineage) |
| `AP47_The_Flip_v1_0.md` | The pre-conversion lock (lineage) |
| `THE_FLIP_draft_v0_1.md` … `v0_7.md` | Full same-day draft lineage, retained |
| `FLIP_SOURCE_AUDIT_v1_0.md` | Every measured number to its named CODATA-2022 line |
| `CANON_AUDIT_v1_1.md`, `CANON_AUDIT_v1_2.md` | Every citation to its file's version of record; v1.2 is the one stating the author's walk is still owed |
| `ERRATA_FLIP_2026-09-01.md` | Corrections standing beside the frozen origin instruments (the (74)→7.4×10⁻⁷ decade slip; 223σ→121,576σ proton-exclusion correction) |
| `neutron.docx`, `WP_FLIP1_Structure_Strategy.docx` | The frozen origin instruments, untouched |
| `SHA256SUMS.txt` | The manifest — every entry verified `OK` at this anchor |

## Independent computational verification (already done, stands independent of the lock question)

Every figure in the paper reproduces from CODATA 2022 alone — this was checked via two blind
reimplementations, cross-checked against each other and the paper's claimed figures, before this
anchor was made:

- Δ_bare = 2.53099393 mₑ (the original, uncorrected claim) — matches the already-published
  lucid.rodeo figure, fired at 7.24σ on 2026-08-02 (KS-NPP.1), stays fired, not touched by this bundle
- Δ_real = Δ_bare/(1+α²/8π) = 2.53098857035 mₑ, landing at −0.005σ against measured 2.530988574
- The elimination table (section 5): only the support-2 (8π) divisor lands, matching the paper's own table
- The proton-elimination check: 121,576σ (correcting an earlier miscalculated 223σ, per the errata)

Verification confirms the arithmetic is sound. It does not, and cannot, substitute for the author's
own walk — those are different questions, and this repo keeps them separate on purpose.

## Still open after this delivery

- The author's own walk of v0.7 (his word closes it — see `CANON_AUDIT_v1_2.md`).
- Once walked and locked, a separate `ap47-locked-YYYY-MM-DD` tag follows, the same two-step pattern
  AP44 used (`ap44-provenance-anchor-*` then `ap44-locked-2026-08-11`).
- AP47's four kill switches (KS-FLIP.1–4) are NOT yet in this repo's canon DB — deliberately, per
  `engine/ingest_local_addenda.py`'s own comment — until AP47 has its own lock anchor.
- Publication on lucid.rodeo already exists at `/prereg/ap47/`, explicitly marked pending-lock and
  `noindex`, consistent with this anchor's own status.
