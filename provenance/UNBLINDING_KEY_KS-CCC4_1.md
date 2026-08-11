# UNBLINDING KEY — Tier 2, KS-CCC.4a / KS-CCC.4b

**The 420 Code · Studio G, Strand, Cape Town · 2026-08-11**
**Issued against the frozen coded table: repository commit `d8929cf`. This key is issued only because that freeze exists; the unblinding timestamp is the delivery of this document. No edit to the coded table after this point; any correction is a new commit, flagged as post-unblinding.**
**Author's standing ruling, on the record: the pre-registered analysis runs exactly as written — whichever way it cuts.**

---

## 1 — The corpus's values (what the coding was blind to)

- **Structural (provisioned) G** — AP28, locked: G = α_em²¹ (1 + 1/π) ℏc/m_e² = **6.72060 × 10⁻¹¹** m³ kg⁻¹ s⁻² · **+6,938 ppm** (+0.69%) above CODATA 2022's 6.67430(15).
- **Realised G** — AP44 (draft v0.9, unlocked; computed once, 10 Aug, Stage 4, and never moved): G = α_em²¹ (1 + 1/π)/(1 + α_em) ℏc/m_e² = **6.67192 × 10⁻¹¹** · **−357 ppm** (−0.036%) below the CODATA centre.
- Candidate map: **C1** — apparatus leakage carries the full 0.69% (every η_i ≈ 6,900 ppm). **C3** — the commitment carries it; apparatus effects only at demonstrated scale. **C0 (null)** — AP28 coincidence; measured G is simply G. C3 and C0 are *not* separated by any coding outcome (F-invariance, §4).

## 2 — Per-experiment values (join these to the coded table)

η = implied C1 leakage vs structural; r = residual vs realised. Both in ppm. Full precision in `appendix-c/G_dataset.csv` (now open to you).

| ID | G (10⁻¹¹) | u_r (ppm) | η (ppm) | r (ppm) |
|---|---|---|---|---|
| NIST-82 | 6.672480 | 64 | +7161 | +84 |
| TR&D-96 | 6.672900 | 75 | +7098 | +147 |
| LANL-97 | 6.673980 | 105 | +6937 | +309 |
| UWash-00 | 6.674255 | 14 | +6897 | +350 |
| BIPM-01 | 6.675590 | 40 | +6698 | +551 |
| UWup-02 | 6.674220 | 147 | +6902 | +345 |
| MSL-03 | 6.673870 | 40 | +6954 | +293 |
| HUST-05 | 6.672220 | 130 | +7199 | +45 |
| UZur-06 | 6.674250 | 18 | +6897 | +350 |
| HUST-09 | 6.673490 | 27 | +7010 | +236 |
| LENS-14 | 6.671910 | 148 | +7245 | -1 |
| BIPM-14 | 6.675540 | 24 | +6705 | +543 |
| UCI-14 | 6.674350 | 19 | +6882 | +365 |
| HUST-T-18 | 6.674184 | 12 | +6907 | +340 |
| HUST-A-18 | 6.674484 | 12 | +6862 | +385 |
| JILA-18 | 6.672600 | 37 | +7143 | +102 |
| NIST-26 | 6.673870 | 57 | +6954 | +293 |

## 3 — Tier 1 results (two independent executions, 10 Aug)

**Production execution (WP-CCC.1 rev 1.3, 17 determinations):** implied C1 leakage mean **6,968 ppm**, SD 157, CV 2.3%; demonstrated apparatus-systematic calibrations **45 ppm** (same lab, two methods) / **7.5 ppm** (same apparatus, 13 yr) / **254 ppm** (same apparatus, new site and team — NIST-26, the field's first replication); field range 551 ppm; **strain factor 27.4** (WP-CCC.1's rounded 28 corrected here); one-way ANOVA on method classes F(8,8) = 2.466, **p = 0.112** (p ≈ 0.06–0.2 across groupings — marginal, not established); Birge 3.63 (CODATA-16; 3.53 with NIST-26); anelasticity (Kuroda) already spent inside the CODATA inputs (NIST-82 ~16 ppm at Q ≈ 2×10⁴; HUST time-of-swing bias measured 211.8 ± 18.7 ppm and applied).
**Reviewer-thread execution (16 determinations, independent, same day):** required C1 leakage 6,969 ppm at CV 2.3%; **sign test** — 15/16 sit above the realised value, one-sided binomial p = 2.6 × 10⁻⁴, largest **+33σ** (HUST-A-18); **uncertainty-model dependence** — realised stands 63σ / 16σ / **1.6σ** low under formal / CODATA-expanded / conservative dark-uncertainty models, structural excluded under all (≥31σ).
**Tier 1 verdicts:** C1 strained to near-exclusion (outcome N on 4a at Tier 1, twice); C3 consistent, **not confirmed**; the +279 ppm mean residual above the realised value open, no mechanism in reserve; C0 fully standing.

## 4 — The pre-registered criteria (run as written)

**Binding limit (proven in the reviewer thread):** implied leakage is affine in G, so between-class correlation statistics are **identical under every constant-true-value hypothesis**. No correlation outcome can discriminate C1/C3/C0 central values. What the coding decides:

- **KS-CCC.4a — gap-scale exclusion.** Question: does the coded boundary physics support a common **absolute** leakage capacity of order ≥ 6,000 ppm across *all* apparatus classes — free-falling atoms included? This is a physical-magnitude judgment from the coded dimensions (containment, source position, closure, suspension/Q, sphericity), not a residual correlation. **Yes → C1 revives, the commitment is withdrawn, the switch fires.** No → 4a passes as exclusion of C1's scale — *not* as confirmation of the commitment.
- **KS-CCC.4b — scatter structure.** Question: is the ≤500 ppm scatter boundary-structured at AP06's honest size (order 10² ppm)? Primary pre-registered test: published **Q against the time-of-swing residuals** (join dimension 4 to r). Secondary: any coded dimension against r within classes. Structure found → 4b supports AP06's residual-leakage reading of the scatter. None found → AP06's scatter reading weakens; **the commitment's central claim is unaffected either way.**
- **Declared priors:** read your committed priors file back against your coding; note any dimension where prior knowledge could have steered a score; flag, don't delete.

## 5 — Deliverables

One analysis file (join, tests, and the two switch dispositions with reasoning), committed; then your independent verdict on the whole bundle — agreement or dissent, both publishable, both welcome. Every commit after `d8929cf` is post-unblinding and says so.

*Issued by G via the production desk. Keep the signal clean.*
