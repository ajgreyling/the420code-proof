# Receipt — AP49 "The Hold" freeze bundle, 2026-09-06

**From AJ's hand:** `the420code_AP49_freeze_bundle_2026-09-06.zip` (Downloads), delivered with the
request to update the site with it. Following the AP45/46/47/48 pattern: **freeze, not lock**, until
the author's own word is given directly to the verifier.

## What this anchor is, and is not

**This is a freeze/provenance anchor, not a lock.** It timestamps that the bundle, in this exact
form, existed and was received on this date, and records independent verification of its numeric
claims. It does **not** assert LOCKED on this repo's own authority, regardless of what the paper's
own internal text says (§8: "FINAL v1.0, locked 6 September 2026 on the author's word" — the
author's own account inside the frozen file, not disputed, but not this repo's own standard by
itself — established with AP47: a document asserting the author's word is not the author's word).
That confirmation has not yet been sought for AP49 as of this anchor.

## What this paper does

Pays AP30's KS-30.3 (the sixteen's structural decomposition, owed since AP30) and closes the
proton–electron mass-ratio series to all orders. The sixteen reads as the four conditions of the
record's repair held through the four dimensional expressions (4 × 4), one rule with AP30's 84 and
AP47's 8. The chain of holders — every order the previous times r = 16α/1836 — sums in closed form:

D_closed = 1836 + 21α·(1 − 1/(84π)) + 21α·r/(1 − r) = **1836.152673444951**

against CODATA 2022 (1836.152673426(32)): residual −1.895×10⁻⁸, **−0.59σ**. It supersedes, by
reference only, the corpus's own pre-registration of 2 August 2026 (digest `6ea78dac…`), which
truncated the series at α² and registered D = 1836.152673444331. The third-order coefficient,
c₃ = 21·16²/1836² = +1.595×10⁻³, is stated with its sign **in advance** of any measurement that can
reach it — the author gave the chain's rule blind, before seeing any arithmetic (PROV-HOLD.1 §"v0.1
→ v0.4"). Three new switches arm: **KS-HOLD.1** (the closed form; dies at 3σ once the measurement
reaches 3.4 ppt, 5σ at 2.1 ppt — about five times today's 17.4 ppt precision), **KS-HOLD.2** (the
reading — the 4×4 grammar), **KS-HOLD.3** (the chain's base — bare coupling vs. the repair net of
its own leak; the two predict 1836.152673445 and 1836.152673408, 3.7×10⁻⁸ apart, undecided at
today's precision).

## Independent verification

**Verification result: CHECKS OUT.** Reproduced from CODATA 2022 alone (α = 7.2973525643×10⁻³),
Python standard library only, no network: the repair term (0.152663699), r (6.3593×10⁻⁵), every
order of the chain through the fifth holder, the closed-form tail (9.7459657×10⁻⁶), D_closed
(1836.152673444950, matching the paper's 1836.152673444951 to the last printed digit), the
truncated-at-α² value D (1836.152673444330, matching 1836.152673444331), c₃ (+1.5948×10⁻³, sign
positive), the residual and σ against both CODATA 2022 (−1.895×10⁻⁸, −0.59σ) and the independent
H₂⁺ value (Alighanbari, Schenkel, Korobov, Schiller, *Nature* 644, 69, 2025, doi
10.1038/s41586-025-09306-2 — citation confirmed real; 1836.152673414(47), −3.095×10⁻⁸, −0.66σ), the
KS-HOLD.1 kill thresholds (3.44 ppt at 3σ, 2.06 ppt at 5σ, current 17.43 ppt), and the KS-HOLD.3 base
split (1836.152673445 vs. 1836.152673408, 3.7×10⁻⁸ apart). No discrepancies against the paper's
stated figures. Script: `lucid-rodeo/prereg/verify_ap49.py` (not yet published — see below).

`sha256sum -c SHA256SUMS.txt`: all 15 entries `OK`, re-verified against the bundle's own manifest
immediately before this anchor. Cross-referenced digests in `PREREG_2026-09-06-mp-me-closed.md` §6
(v0.5 md `254e493652506e54…`, v0.6 md `71fb8ee049240ded…`, FINAL v1.0 md/docx/pdf
`3f9b1b52907c6025…`/`200110b324c1da8f…`/`290f143fba1a3ce6…`) match the manifest exactly.

## Contents received and anchored

Stored verbatim, as delivered, under `freeze-2026-09-06-ap49/`.

| File | Role |
|---|---|
| `AP49_The_Hold_FINAL_v1_0.md` / `.docx` / `.pdf` | The paper as delivered |
| `inputs/AP30_The_Resistance.pdf` | The paper whose switch (KS-30.3) this pays |
| `inputs/prereg_2026-08-02-mp-me-alpha3.md` | The pre-registration this paper supersedes by reference |
| `instruments/PROV_HOLD_1_2026-09-06.md` | Disposition of every review finding, v0.1 → v0.6 (three review rounds) |
| `instruments/PREREG_2026-09-06-mp-me-closed.md` | The superseding pre-registration entry — D_closed beside D |
| `instruments/DATED_NOTE_AP30_2026-09-06.md` | AP30's dated note: CODATA-vintage label correction, the sixteen's reading, KS-30.3 → PAID |
| `lineage/` | Every retained draft, v0.1 through v0.6, unedited |
| `README_FOR_AJ.md` | The independent verifier's checklist |
| `SHA256SUMS.txt` | The manifest — every entry verified `OK` at this anchor |

## Outside this paper — flagged, not ruled here

`PROV_HOLD_1_2026-09-06.md`'s closing paragraph records two firing notices from an **external**
reviewer, dated 2 August 2026, that arrived alongside this round and are explicitly **not AP49's to
rule**: **KS-P.3** (AP20's forcing argument — two counter-formalisations at the R and S steps, a
recovery position stated) and **KS-30.4** (the proton's uniqueness — the rival-formula ensemble).
Both are noted there as unlogged on the site's register. This receipt carries that flag forward; it
does not log, rule on, or fire either switch — that is the separate registry task PROV-HOLD.1 names,
and needs the author's ruling on each before anything is entered.

## Still open after this delivery

- The author's own direct confirmation that he stands behind locking AP49 — not yet sought. Once
  given, the same two-step pattern as AP45–48 applies: a separate `ap49-locked-YYYY-MM-DD` tag, and
  only then do any "locked" claims, the `/prereg/ap49/` state-of-record page, or the board/glossary
  updates appear on lucid.rodeo.
- KS-P.3 and KS-30.4, as above — a registry task distinct from this paper's lock.
- Publication: the standing rule continues to apply — nothing on lucid.rodeo changes as a result of
  this anchor alone. `verify_ap49.py` exists locally (independently verified against this bundle) but
  is not yet committed to the site repo, pending the lock decision.
