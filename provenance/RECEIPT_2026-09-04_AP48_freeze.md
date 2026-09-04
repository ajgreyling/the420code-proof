# Receipt — AP48 "The Assembly" freeze bundle, 2026-09-04

**From AJ's hand:** directory `the420code_AP48_freeze_bundle_2026-09-04.zip` (Downloads), delivered by
Studio G with the request "sal jy asb freeze vir my solank" — freeze it for me, for now. Same word
as the AP45/AP46 and the original AP47 delivery: **freeze, not lock.**

## What this anchor is, and is not

**This is a freeze/provenance anchor, not a lock.** It timestamps that the bundle, in this exact
form, existed and was received on this date. It does **not** assert LOCKED on this repo's own
authority, regardless of what the paper's own internal text says about its lock status (the paper's
§13 states "FINAL v1.1, locked 4 September 2026 on the author's word" — that is the author's own
claim inside the frozen file, which this repo does not dispute, but this repo's own anchor requires
the same standing it required for AP47: the author's own word given **directly to the verifier**,
not merely a document asserting it. That confirmation has not yet been sought for AP48 as of this
anchor.

## Why this one gets extra scrutiny before any lock question is even asked

AP48 fires a kill switch on an **already-public** paper — KS-45.1, registered by AP18 ("The Floor"),
which claims H₀ = 74.3 ± 1.2 km/s/Mpc. AP48 derives H₀ = 67.45 km/s/Mpc from the corpus's own
structure (the AP46 cycle, read through the standard H₀t₀ relation) and fires KS-45.1 at 5.7σ on its
registered width. The paper is explicit and unflinching about what this costs: *"The distinctive
prediction the corpus used to carry on H₀... is gone."* An erratum against AP18 (`ERRATUM_AP18_The_Floor_2026-09-03.md`,
included here) corrects the registered width (it omitted a systematic uncertainty) but does **not**
un-fire the switch — the paper is explicit that widening the bar after contradiction and not counting
the fire would itself be a repair, which the house rule forbids.

This is the second kill switch this corpus has fired, after KS-NPP.1 (AP47/AP45). Independent
computational verification of the numeric chain (two blind passes) was run before this anchor,
covering: the H₀t₀ closed-form relation, the AP46 cycle, the derived 67.45 km/s/Mpc rate and its
64.4–70.8 window, the 5.7σ firing figure, the corrected AP18 floor check, the error-propagation
arithmetic behind the erratum's ±14.9 corrected width, and a dead-end serial-storm figure the paper
itself rejects. See the verification note filed alongside this receipt.

**Verification result (two independent blind Python passes, cross-checked): CHECKS OUT.**
All 10-11 internal numeric claims in sections 8-10 reproduce exactly from first principles
(CODATA-2022 constants, the AP46 cycle, root-found window bounds, the sigma/kill-switch
arithmetic, the corrected AP18 floor check, the erratum's error-propagation arithmetic, and
the arithmetic of the paper's own rejected serial-storm reading). No discrepancies found
between the two passes or against the paper's stated figures. External citations spot-checked
directly (not just trusted): Riess et al. 2025 ApJL 992, L34 (doi 10.3847/2041-8213/ae0ad6,
H0=73.49+/-0.93 -- confirmed exact); Freedman et al. 2025 ApJ (doi 10.3847/1538-4357/adce78,
H0=70.39+/-1.22+/-1.33+/-0.70 TRGB, 68.81/67.80 JWST-only TRGB/JAGB -- confirmed exact); Li
et al. 2026 ApJ 997, 115 (doi 10.3847/1538-4357/ae1f17 -- confirmed real, consistent with the
paper's description). Planck 2018 Table 2 figures (67.4+/-0.5; 67.66+/-0.42 with BAO) match
well-established literature values.

## Contents received and anchored

Stored verbatim, as delivered, under `freeze-2026-09-04-ap48/`. Every file's SHA-256 re-verified
against the bundle's own `SHA256SUMS.txt` immediately before this anchor — all entries `OK`.

| File | Role |
|---|---|
| `AP48_The_Assembly_FINAL_v1_1.md` / `.docx` / `.pdf` | The paper as delivered |
| `inputs/WP_ASM1_Assembly_Primer.md` / `.docx` | The primer of record the paper was written from |
| `inputs/G_answers_to_WP_ASM1_Assembly_Primer.docx` | The author's own answers, 3 September |
| `inputs/CONTINUATION_README_AP48.md` | The desk's continuation note, pre-registered targets before arithmetic |
| `inputs/AP18_The_Floor_FINAL.docx` | The paper whose switch KS-45.1 fires here |
| `instruments/PROV_ASM_1_2026-09-03.md` | Disposition of every review finding, v0.1 → v1.1 (two reviews of v1.0: composite 9.3 and 8.8) |
| `instruments/ERRATUM_AP18_The_Floor_2026-09-03.md` | The AP18 width correction — corrects the bar, does not un-fire the switch |
| `instruments/ERRATA_NOTES_2026-09-03.md`, `DATED_NOTE_AP46_2026-09-04.md` | Working corrections, dated, standing beside the frozen files they touch |
| `instruments/AP48_Open_Derivations_v1_0.md` | The author's own drawer — what remains open, explicitly not blocking this lock |
| `lineage/` | Every retained draft, v0.1 through v1.1, unedited |
| `SHA256SUMS.txt` | The manifest — every entry verified `OK` at this anchor |

## Still open after this delivery

- The author's own direct confirmation that he stands behind locking AP48 — not yet sought for this
  paper. Once given, the same two-step pattern as AP47 applies: a separate `ap48-locked-YYYY-MM-DD`
  tag, and only then do any "locked" claims appear on lucid.rodeo.
- Two counts explicitly named as still owed in `AP48_Open_Derivations_v1_0.md`: the storm's length /
  completing count (D-ASM.1), held open and stated as not blocking this paper.
- KS-STRETCH.4 (AP46's era-surface switch) is marked MET/CLOSED at this lock but re-opens if
  KS-ASM.2 ever fires — a dependency carried forward, not a closed book.
- Publication: the standing ONE-WAVE rule continues to apply (nothing on lucid.rodeo changes as a
  result of this anchor alone).
