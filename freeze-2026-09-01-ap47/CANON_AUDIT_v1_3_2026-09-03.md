# The Flip — Canon Audit v1.3 (independent pass, post-freeze)

**Verifier's audit · 3 September 2026 · supersedes nothing in v1.1/v1.2, adds to them**

**Nothing frozen is edited.** v1.1 and v1.2 (both retained in this bundle, unchanged) stand exactly
as closed. This is a fourth, independent pass — run after the freeze anchor
(`ap47-freeze-anchor-2026-09-03`), against the mirrored, already-published source papers directly
(AP30, AP06 from the420code.org public mirror; AP44, AP45, AP46 from their own locked files) —
checking two things the paper's own checklist names as the author's remaining walk: citation
fidelity, and chain order (words before arithmetic).

## Method

Every quoted fragment in `AP47_The_Flip_FINAL_v3.md` attributed to AP30, AP06, AP44, AP45, or AP46
was located in the actual source file and compared character-for-character. The origin note
(`neutron.docx`) was opened directly to check whether its structural prose predates its arithmetic.

## Result: citations

**AP30 (4 quotes checked) — verbatim, all confirmed.**
- *"the substrate speaks at α_em"* — found verbatim.
- *"three spatial + one temporal"* — found verbatim (§ preceding the 21×4=84 derivation, not
  immediately adjacent to it — a reader skimming only the nearby lines would miss it; it is there).
- *"the leakage is normalised by the very structure it leaks through"* — found verbatim.
- The 21 geometric channels / 4 spacetime dimensions / 21×4=84 construction, and KS-30.2's exact
  wording — found verbatim.

**AP06 (§0.7 domain field) — confirmed.** Section 0.7 exists exactly where cited and reads as
described: the canonical corpus-wide value ε = α_em is one of several domain readings held open
there, matching AP47's characterisation.

**AP44 — verbatim, confirmed.** *"the value is not [derived], and the paper says so"* matches
AP44 FINAL v1.0's actual sentence, *"The form above is derived; the value is not, and the paper
says so,"* to the word (AP47's bracketed `[derived]` is a legitimate ellipsis-fill, not an
alteration). The D-CCC.4 booking is stated identically in both files.

**AP45 — verbatim, confirmed.** *"one ε-grain, α-worth, dimensionless"* matches AP45 FINAL v1.7
word-for-word, and is unchanged from the draft AP47 actually had in hand through today's lock.

**AP46 — two fidelity issues, non-substantive.** AP47 places quotation marks around two fragments
attributed to AP46 that are not verbatim:

1. *"one part in α⁻¹⁸ per electron-tick"* — not found in AP46 in this form. AP46 §6 states *"One
   escape per α⁻¹⁸ ticks"* — the same claim, reworded, not a direct lift.
2. *"threading eighteen sequential gates — one α-transparent door each"* — this splices two
   separate AP46 §6 clauses (*"the shed must cross all eighteen faces — one α-transparent door
   each, all in one tick"* and, ~15 words later, *"the chance of threading eighteen sequential
   gates"*) into what reads as one continuous quotation.

**Assessment.** Both issues are citation-hygiene, not substance: the physics being described is
accurate to what AP46 actually claims (verified independently in this same pass — AP46's own §9
chain reproduces from CODATA-2022 exactly as published), and no number, formula, or conclusion in
AP47 depends on the exact wording of either fragment. But quotation marks assert verbatim sourcing,
and here they don't fully deliver it. Recommended fix at AP47's next revision: either locate and
quote AP46's actual wording precisely, or drop the quotation marks and cite the section (§6)
directly, paraphrased.

## Result: chain order

Confirmed structurally in `neutron.docx` itself: the file is organised under an explicit heading
*"1. WORDS ONLY — how it works structurally,"* containing the prose argument for a held distinction
costing a second-order tax, followed by a section headed *"2. MATH — for AJ,"* containing the first
arithmetic. Words precede numbers in the source file, on its face.

AP47's own account of its history is corroborated, not merely asserted: `neutron.docx`'s original
justification for the divisor 8π really is the weaker "four conditions × 2π" reading AP47 §5
explicitly retires ("on the record"), and the final paper's replacement derivation (from AP30's own
21-channel/4-dimension construction) is the one that survives. The paper does not hide its own
earlier, weaker reasoning — it names and retires it in the open, matching the house rule.

Also corroborated in `neutron.docx`: the uncorrected `(74)`/`0.288 ppm`/`223σ` figures the errata
(`ERRATA_FLIP_2026-09-01.md`) documents as needing correction are exactly what the origin note
carries — consistent chain of custody from origin note through to the corrected published figures.

## What this audit does not do

It does not constitute the author's walk of v0.7. It is exactly what its title says: a canon audit
— citations checked against sources, order checked against the record. The author's own reading and
endorsement remains the separate, non-delegable step this bundle's v1.2 audit already named.
