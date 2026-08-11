# Declared priors — Tier 2 blind coding

**Declared:** 2026-08-11, before any of the seventeen papers was opened.
**Declarant:** Klaus (AJ's AI), the supervising coder.

Honesty beats pretend blindness. This file records everything the
supervising agent already knows that the protocol wishes it did not.

## What has been seen (contamination, unavoidable)

1. **The corpus's predicted values are known.** The handover document
   itself (§4 Phase B) states them: structural G = 6.72060 × 10⁻¹¹
   (+0.69%) and realised G = 6.67192 × 10⁻¹¹ (−0.036% vs the adjusted
   value). AJ's covering message also named the −0.036%.
2. **Tier 1 headline outcomes are known** from the same handover text:
   Tier 1 (run twice) answers KS-CCC.4a "no", and finds KS-CCC.4b at
   best marginal (p ≈ 0.06–0.2).
3. **Not seen:** `AP44_The_Snap_DRAFT_v0_6.docx` (or any draft),
   `WP_CCC1_AppendixC_Tier1.docx`, `G_dataset.csv`, `G_landscape.png`,
   `appc_tier1.py`, and the per-laboratory residual pattern. No lookups
   of any G measurement (including NIST-26) have been made or will be
   made before the coded table is committed.

## Training-data beliefs about where experiments read (approximate,
from memory, not looked up — declared so steering is auditable)

- BIPM-01 and BIPM-14: read **high**, both near ~6.6754 × 10⁻¹¹,
  mutually consistent — the famous high outlier pair.
- JILA-18 (corrected Parks & Faller): reads **low**, near ~6.6726.
- NIST-82 (Luther & Towler): near ~6.6726 (basis of the old CODATA value).
- LENS-14 (Rosi et al., atom interferometry): recalled as **low**,
  near ~6.6719 — noted explicitly because it is a free-fall experiment
  and its recalled central value lies close to the corpus's realised
  prediction. This is the single most material prior in this file.
- UWash-00: near ~6.6742. HUST-T-18 / HUST-A-18: near ~6.6742/6.6743.
  UZur-06: near ~6.6743. UWup-02: near ~6.6742. LANL-97: near ~6.674.
- TR&D-96, MSL-03, HUST-05, HUST-09, UCI-14: vaguer recollections,
  roughly within the 6.672–6.675 band; no confident placement.
- NIST-26 (Metrologia 63, 025012): **genuinely unknown** — post-dates
  the declarant's training data. No prior.

## Prior beliefs about the boundary-structure question itself

None held before reading the handover. After reading it, the declarant
carries the second-hand knowledge that Tier 1 found the 6,000 ppm common
leakage capacity unsupported and the Q/time-of-swing tracking marginal.
The coding pass is therefore delegated to a fresh agent context that has
not read the handover (see CODEBOOK.md, "Blinding guard"); that agent's
own residual training-data priors are subject to the same unavoidability
clause as any coder in the field.
