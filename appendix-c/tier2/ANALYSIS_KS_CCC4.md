# Tier 2 analysis — KS-CCC.4a / KS-CCC.4b

**Post-unblinding.** Issued against frozen coded table `d8929cf` and corrected
unblinding key `UNBLINDING_KEY_KS-CCC4_1.md` (7482445b…). Analysis runs exactly
as pre-registered — whichever way it cuts.
**Analyst:** Klaus (AJ's AI), 2026-08-11.
**Binding limit recalled:** implied leakage is affine in G; class-correlation
statistics are identical under every constant-true-value hypothesis. Correlations
cannot pick between C1/C3/C0 central values.

---

## Join

Per-experiment η (vs structural) and r (vs realised) from the key, joined to the
five coded dimensions in `CODED_TABLE.csv`. Full join retained in working notes;
headlines:

| ID | D1 | D2 | D3 | Q (coded) | D5 | r (ppm) | η (ppm) |
|---|---|---|---|---|---|---|---|
| NIST-82 | SUS | OUT | 1 | 2e4 | 4 | +84 | 7161 |
| TR&D-96 | SUS | UNSOURCED | UNSOURCED | 2e4 | UNSOURCED | +147 | 7098 |
| LANL-97 | SUS | OUT | 1 | ~1e3 | 4 | +309 | 6937 |
| UWash-00 | SUS | OUT | 2 | 4e3 | 4 | +350 | 6897 |
| BIPM-01 | SUS | OUT | 1 | 3e5 | 4 | +551 | 6698 |
| UWup-02 | SUS | OUT | 1 | n/s | 4 | +345 | 6902 |
| MSL-03 | SUS | OUT | 1 | n/s | 4 | +293 | 6954 |
| HUST-05 | SUS | OUT | 1 | ~3.6e4 | 4 | +45 | 7199 |
| UZur-06 | SUS | OUT | 2 | n/a | 4 | +350 | 6897 |
| HUST-09 | SUS | IN | 0 | 1.7e3 | 4 | +236 | 7010 |
| **LENS-14** | **FF** | OUT | 3 | n/a | 4 | **−1** | **7245** |
| BIPM-14 | SUS | OUT | 1 | 3e5 | 4 | +543 | 6705 |
| UCI-14 | SUS | OUT | 3 | ~1e5 | 4 | +365 | 6882 |
| HUST-T-18 | SUS | IN | 1 | ~5e4 | 4 | +340 | 6907 |
| HUST-A-18 | SUS | OUT | 1 | n/s | 4 | +385 | 6862 |
| JILA-18 | SUS | OUT | 1 | n/s | 4 | +102 | 7143 |
| NIST-26 | SUS | OUT | 1 | 2.4e5 | 4 | +293 | 6954 |

---

## KS-CCC.4a — gap-scale exclusion

**Question:** does the coded boundary physics support a common *absolute*
leakage capacity of order ≥ 6,000 ppm across **all** apparatus classes —
free-falling atoms included?

**Physical-magnitude judgment from the coded dimensions:**

1. Sixteen of seventeen experiments are **SUS** (suspended test mass). One —
   **LENS-14** — is **FF** (free-fall atoms, D4 = none). Under C1, LENS-14's
   implied leakage is **η = 7,245 ppm** — the same absolute scale demanded of
   the torsion balances.
2. The free-fall apparatus has **no suspension element** and therefore no
   fibre/strip anelasticity channel of the kind that could carry thousands of
   ppm in a suspended balance. Its boundary (vacuum tube + µ-metal, D3 = 3)
   is a magnetic/vacuum enclosure around ballistic atoms, not a mechanical
   hold against which a 6,000 ppm absolute "leakage capacity" has a natural
   reading.
3. Across the SUS class, D2 (IN vs OUT) does not sort the η scale
   (IN mean r ≈ OUT mean r; η remains ~6,900 ppm everywhere). D5 is almost
   uniformly 4 — no geometry ladder that could host a common absolute
   capacity. TR&D-96's enclosure dimensions remain UNSOURCED and do not
   rescue the claim.

**Disposition: NO.** The coded boundary physics does **not** support a common
absolute leakage capacity of order ≥ 6,000 ppm across all seventeen,
free-falling atoms included. **KS-CCC.4a passes as exclusion of C1's scale**
— not as confirmation of the commitment. Aligns with Tier 1's outcome N,
twice. C1 does not revive.

---

## KS-CCC.4b — scatter structure

**Question:** is the ≤500 ppm inter-laboratory scatter boundary-structured at
AP06's honest size (~10² ppm)? Primary test: published **Q against
time-of-swing residuals**.

**Primary test (pre-registered):** ToS subset with parseable Q —
NIST-82, TR&D-96, LANL-97, HUST-05, HUST-09, HUST-T-18 (n = 6):

| ID | Q | r (ppm) |
|---|---|---|
| NIST-82 | 2×10⁴ | +84 |
| TR&D-96 | 2×10⁴ | +147 |
| LANL-97 | ~10³ | +309 |
| HUST-05 | ~3.6×10⁴ | +45 |
| HUST-09 | 1.7×10³ | +236 |
| HUST-T-18 | ~5×10⁴ | +340 |

- Pearson(log₁₀ Q, r) = **−0.41**
- Spearman(Q, r) = **−0.09**

Anelasticity would predict higher Q → lower elevation; the Pearson sign is
consistent but the Spearman is essentially null, and n = 6 with several Q
values inherited from reviews (not methods sections) is thin. No established
structure.

**Secondary:** D5 against r — **no variance** (nearly every coded D5 = 4).
D2 IN/OUT against r — means indistinguishable (~288 vs ~287 ppm). D1 FF vs
SUS — LENS sits alone at r ≈ −1; one point cannot structure the scatter.

**Disposition: structure not found at the pre-registered bar.** AP06's
residual-leakage reading of the ≤500 ppm scatter **weakens**. Per the key:
**the commitment's central claim is unaffected either way.** Aligns with
Tier 1's marginal ANOVA (p ≈ 0.06–0.2).

---

## Declared priors check

Supervising priors (`DECLARED_PRIORS.md`) and coder priors
(`DECLARED_PRIORS_CODER.md`) were re-read against the coding. Material
flags already on the record: LENS-14's recalled proximity to the realised
value; the NIST-26 search unblinding in the coding log. No dimension score
was revised post-unblinding. TR&D-96's UNSOURCED enclosure cells stay
UNSOURCED.

---

## Switch summary

| Switch | Disposition | Reasoning in one line |
|---|---|---|
| **KS-CCC.4a** | **Passes (C1 scale excluded)** | Free-fall class cannot carry ≥6,000 ppm absolute leakage; common-capacity claim fails across all seventeen. |
| **KS-CCC.4b** | **Structure not found** | Q–ToS Spearman ≈ 0; D5/D2 give no handle. AP06 scatter reading weakens; commitment unaffected. |

C3 remains consistent and **not confirmed**. C0 stands. The +279 ppm mean
residual above the realised value remains open, with no mechanism in reserve
from this coding.
