# Appendix C — Execution

## The Leakage Discriminator

*Ø Predictions, Part II · supporting document to KS-CCC.4*

*Does apparatus leakage carry the gap, or the scatter?*

**Draft v0.1 — for the author's ruling. Not adopted. Number and placement open.**

---

## Artist's Note

*What this document does — and why.*

Ø Predictions Part II holds the 0.69% discrepancy in G open between two candidates and declines to pick. Appendix C proposes the test that would decide: characterise each published determination of G by its boundary geometry and see whether the leakage corrections the candidates require are of gap scale or scatter scale. The proposal has stood unexecuted. This document executes it against the sixteen determinations CODATA uses, and rules on what the published record can and cannot support.

**The result is not the comfortable one.** Candidate 1 — apparatus leakage carries the whole gap — fails, and fails hard: it requires every boundary in the record, from a cloud of cold rubidium atoms to a thirteen-tonne mercury beam balance, to leak to within 2.3% of one common value, against AP06's own catalogue of leakage ratios spanning twelve orders of magnitude. That is the internal inconsistency of §11 of The Snap, now quantified.

But the same analysis makes the residual under Candidate 3 substantially worse than "small and open." Under the realised prediction, fifteen of the sixteen determinations sit **above** the predicted true value — and leakage lowers a reading, it cannot raise one. The residual is therefore not merely unattributed: it runs in the one direction the corpus's only systematic mechanism cannot produce, consistently, across every apparatus class in the record. Nine determinations exceed the prediction by more than three of their own standard deviations; the largest by thirty-three.

One honest counterweight is stated in full at §2.5: the verdict depends on which uncertainty model is used, and that choice is not the corpus's to make. Under CODATA's own expanded uncertainty the realised prediction stands sixteen standard deviations low. Under the most conservative published dark-uncertainty model it stands one-and-a-half standard deviations low. The document reports both and selects neither.

Three debts open. Two live kill switches take a disposition. Nothing here amends AP28, AP30 or The Snap; execution is not adoption.

✨

*the420code.org*

*Copyleft 2026*

---

## 0 — Dependency and Scope

### 0.1 — What this document does

It fixes the data set and the boundary characterisation (§1.1–1.2), states the two candidates in testable form (§1.3), specifies three tests and a decision rule with three outcomes before the analysis is read (§1.4–1.5), executes them (§2), and issues findings and dispositions (§3).

**What it does not do.** It performs no new measurement. It re-analyses published central values and published uncertainties; it does not re-derive any laboratory's systematic budget. It does not select an uncertainty model (§2.5). It does not adopt or amend anything.

### 0.2 — Dependencies

**AP06 (The Leakage Constant).** Theorem 3.1 and the domain-dependence of η — the leakage ratio is set by boundary physics and varies with the boundary. Load-bearing for Test 1: the homogeneity requirement is a test *of AP06's own claim*, applied to Candidate 1.

**AP28 (The Constant).** The provisioned coupling and the structural value of G. Load-bearing for Candidate 1's target.

**The Snap (AP_CCC, draft).** The realised coupling α_G∗ = α_G/(1 + ε) and Candidate 3. Load-bearing for Candidate 3's target. This document supplies the execution KS-CCC.4 binds to.

**Ø Predictions Part II and Appendix C.** The open register of candidates and the proposal this document executes.

**External data.** The sixteen values of G that are input data to the 2018 and 2022 CODATA adjustments, with their published uncertainties and method descriptions (Mohr, Newell, Taylor & Tiesinga, *CODATA Recommended Values… 2022*, Table XXX); the method taxonomy of the Bayesian systematic-error re-analysis (Eur. Phys. J. C, 2023); the conservative dark-uncertainty model (Bodnar & Elster, *Shades of dark uncertainty…*, 2019).

### 0.3 — Epistemic status per section

| Section | Status |
|---|---|
| §1.1–1.2 Data set and boundary classes | **FIXED** — external, stated before analysis |
| §1.3 Candidates in testable form | **DERIVED** from the candidates' own definitions |
| §1.4–1.5 Tests and decision rule | **METHOD** — pre-committed; see §5.1 on hashing |
| §2.2 Test 1 (homogeneity) | **EMPIRICAL** — decisive |
| §2.3 Test 2 (boundary correlation) | **EMPIRICAL** — marginal, and non-discriminating by construction |
| §2.4 Test 3 (sign) | **EMPIRICAL** — decisive, and adverse to Candidate 3 |
| §2.5 Uncertainty-model dependence | **REPORTED, NOT SELECTED** |
| §3 Findings and dispositions | **RULING** |

### 0.4 — Debts opened

**D-APC.1 (Predictive η).** AP06 supplies no formula for the leakage ratio η as a function of apparatus geometry. Consequently Candidate 1 can be tested only in its *homogeneity* form, not in its *quantitative* form. Until AP06 supplies a predictive η, no boundary-geometry correlation can be confronted with a number rather than a class label. **Load-bearing for any future revival of Candidate 1.**

**D-APC.2 (Direction of the residual).** Under Candidate 3, fifteen of sixteen determinations lie above the predicted true value. The corpus contains no mechanism that raises a laboratory reading. Either such a mechanism is named and derived, or the residual is conceded as unmodelled laboratory systematics lying outside the corpus's account. **Load-bearing for §9 of The Snap.**

**D-APC.3 (Laboratory–class confound).** The boundary-class signal of Test 2 is confounded with laboratory identity: one class is dominated by two determinations from the same instrument and team. Separating boundary geometry from laboratory practice requires either more determinations or a within-laboratory boundary variation. **Non-load-bearing.**

### 0.5 — Kill switch dispositions issued

**KS-CCC.4 (the discriminator).** Executed. **Does not fire.** The apparatus-leakage corrections required by Candidate 1 are of gap scale but fail the homogeneity condition; corrections at scatter scale are what the record supports. See §3.3 for the precise disposition and for why this is a weaker pass than the switch's wording implies.

**KS-L.5 / AP06 (shared parameterisation).** Not fired, but tightened: Test 1 shows that any shared parameterisation must accommodate a twelve-order-of-magnitude range in η across boundaries, which is inconsistent with the near-constant η Candidate 1 requires. Recorded against AP06 as D-APC.1.

---

## PART A — THE PROTOCOL

## 1.1 — The data set (fixed)

The sixteen determinations of G that are input data to the CODATA 2018 and 2022 adjustments. This set is fixed by an external body, was fixed before this document existed, and is not selected by the author. No determination is added, removed or reweighted. Values in units of 10⁻¹¹ m³ kg⁻¹ s⁻².

## 1.2 — Boundary characterisation (fixed before analysis)

Each determination is assigned to one of five boundary classes on the basis of its published method description alone. The taxonomy follows the standard division used in the metrology literature, not one constructed here.

| Class | Boundary | Members |
|---|---|---|
| **TOS** | Fibre-suspended torsion pendulum, period measurement (dynamic mode) | 7 |
| **AAF** | Torsion pendulum on a rotating turntable, angular-acceleration feedback | 2 |
| **ESC** | Strip-suspended torsion balance, electrostatic compensation / static deflection | 3 |
| **NTB** | Macroscopic non-torsion: beam balance, suspended body with interferometric or resonator readout | 3 |
| **AI** | Atom interferometry — a freely falling cloud of laser-cooled atoms; no macroscopic absorbing boundary | 1 |

The classes are ordered by nothing and weighted by nothing. The physical point of the taxonomy is that these boundaries are not similar: TOS and AAF differ in whether the fibre is loaded, ESC in suspension geometry and in measuring deflection rather than period, NTB in having no torsional element at all, and AI in having no solid test-mass boundary whatsoever. One member of TOS is cryogenic.

## 1.3 — The two candidates in testable form

Both candidates assert a true value G_true and attribute the difference between it and each laboratory's reading to apparatus leakage η_i, where AP06 fixes the sign: **leakage lowers a reading.** A leaky apparatus reads low; it never reads high.

> **Candidate 1.** G_true = G_struct = 6.7206038 × 10⁻¹¹ (AP28 provisioned). Required per-laboratory leakage η_i = 1 − G_i/G_struct.
>
> **Candidate 3.** G_true = G_real = 6.6719165 × 10⁻¹¹ (The Snap, realised). Required per-laboratory leakage η_i = 1 − G_i/G_real.

Two scale references, both fixed externally:

- **gap scale** ≡ the AP28 discrepancy from the recommended value, **6,938 ppm**
- **scatter scale** ≡ the spread of the published determinations, **551 ppm** (range), **164 ppm** (unweighted SD)

## 1.4 — The three tests

**Test 1 — Homogeneity.** AP06 holds that η is set by boundary physics and varies with the boundary; its own catalogue runs from ≈10⁻¹⁷ at a gravitational boundary to ≈10⁻⁵ at a retinal one. A candidate that requires η to be *near-identical across radically different boundaries* is inconsistent with the mechanism it invokes. Metric: the coefficient of variation, CV = |SD(η)/mean(η)|. A boundary-driven effect should have CV of order unity. A CV near zero means the required correction is universal — which is to say structural, not apparatus-dependent.

**Test 2 — Boundary correlation.** If leakage explains the dispersion, the dispersion should be organised by boundary class. Metric: one-way ANOVA of η across the five classes; F-ratio, p, and the fraction of variance explained (η²).

**Test 3 — Sign.** Leakage lowers readings. Under a candidate whose G_true is correct, every determination must therefore lie **at or below** G_true, up to its own uncertainty. Metric: the count of determinations lying above G_true, their deviations in units of their own published standard uncertainty, and a binomial test on the count.

## 1.5 — The decision rule (three outcomes)

Committed before the analysis is read. Note that the rule can go against Candidate 3 as well as against Candidate 1; a test that only one side can lose is not a test.

> **Outcome G — gap-scale, homogeneous, boundary-correlated.**
> Required corrections ≈ gap scale, CV of order unity, and significant class structure.
> → Candidate 1 supported. Candidate 3's commitment is unnecessary; **KS-CCC.4 fires** and The Snap's correction is withdrawn.
>
> **Outcome S — scatter-scale, boundary-correlated.**
> Required corrections ≈ scatter scale, correctly signed, with significant class structure.
> → Candidate 3 supported *with* its leakage account of the residual intact. KS-CCC.4 does not fire.
>
> **Outcome N — no coherent leakage account at either scale.**
> Corrections fail homogeneity at gap scale, or fail sign at scatter scale, or show no class structure.
> → Candidate 1 falls (it has no mechanism left). Candidate 3 survives *as a universal term only*, and loses any leakage account of its residual, which reverts to unattributed laboratory systematics outside the corpus. KS-CCC.4 does not fire, but §9 of The Snap must say what it now cannot explain.

---

## PART B — EXECUTION

## 2.1 — The record

Determinations sorted by value. η₁ is the leakage Candidate 1 requires; η₃ is the leakage Candidate 3 requires; the last column is the determination's distance above the Candidate-3 predicted true value in units of its own published uncertainty.

| Determination | Class | G | u(G) | η₁ (ppm) | η₃ (ppm) | σ above G_real |
|---|---|---|---|---|---|---|
| LENS-14 | AI | 6.671910 | 0.00099 | +7245 | +1 | −0.01 |
| HUST-05 | TOS | 6.672220 | 0.00087 | +7199 | −46 | +0.35 |
| NIST-82 | TOS | 6.672480 | 0.00043 | +7161 | −85 | +1.31 |
| JILA-18 | NTB | 6.672600 | 0.00025 | +7143 | −102 | +2.73 |
| TR&D-96 | TOS | 6.672900 | 0.00050 | +7098 | −147 | +1.97 |
| HUST-09 | TOS | 6.673490 | 0.00018 | +7010 | −236 | +8.74 |
| MSL-03 | ESC | 6.673870 | 0.00027 | +6954 | −293 | +7.24 |
| LANL-97 | TOS | 6.673980 | 0.00070 | +6937 | −309 | +2.95 |
| HUSTᴛ-18 | TOS | 6.674184 | 0.000078 | +6907 | −340 | +29.07 |
| UWup-02 | NTB | 6.674220 | 0.00098 | +6902 | −345 | +2.35 |
| UZur-06 | NTB | 6.674250 | 0.00012 | +6897 | −350 | +19.45 |
| UWash-00 | AAF | 6.674255 | 0.000092 | +6897 | −351 | +25.42 |
| UCI-14 | TOS | 6.674350 | 0.00013 | +6882 | −365 | +18.72 |
| HUSTᴀ-18 | AAF | 6.674484 | 0.000077 | +6862 | −385 | +33.34 |
| BIPM-14 | ESC | 6.675540 | 0.00016 | +6705 | −543 | +22.65 |
| BIPM-01 | ESC | 6.675590 | 0.00027 | +6698 | −551 | +13.61 |

Characterisation of the record itself: range **551 ppm**; unweighted SD **164 ppm**; formal weighted mean **6.674290** with formal uncertainty **0.000038**; χ²/ν = **13.2**, Birge ratio **3.63**. CODATA applies a **3.9** expansion factor to these uncertainties precisely because the set is mutually inconsistent. That expansion factor is used wherever σ figures are quoted as "expanded" below.

## 2.2 — Test 1: Homogeneity

| | Candidate 1 | Candidate 3 |
|---|---|---|
| mean required η | **+6,969 ppm** | **−278 ppm** |
| SD of required η | 163 ppm | 164 ppm |
| **CV = \|SD/mean\|** | **0.023** | **0.590** |

Candidate 1 requires every boundary in the record to leak to within **2.3%** of one common value.

The boundaries in question are: a fused-silica fibre carrying a torsion pendulum; a strip suspension measuring static deflection; a turntable under angular-acceleration feedback; a cryogenic pendulum; a thirteen-tonne mercury beam balance; a suspended body read by laser interferometry; and a freely falling cloud of laser-cooled rubidium atoms with no solid test-mass boundary at all.

AP06's own catalogue of η across boundaries spans **twelve orders of magnitude**. Candidate 1 asks the same mechanism to be constant to two per cent across the most heterogeneous set of boundaries the record contains.

**Test 1 verdict: Candidate 1 fails.** An effect that is 97.7% apparatus-independent is not an apparatus effect. This is the internal inconsistency of The Snap §11, now with a number on it: the corpus identifies scatter as leakage's signature, the signature is 164 ppm, and Candidate 1 asks leakage to carry 6,969 ppm — forty-three times its own signature, with almost no boundary dependence.

Candidate 3's CV of 0.59 is of the order a genuinely apparatus-dependent effect would show. That is the *shape* Candidate 3 needs. Test 3 addresses whether it has the *sign*.

## 2.3 — Test 2: Boundary correlation

One-way ANOVA of required η across the five boundary classes:

**F(4, 11) = 3.355, p = 0.050, η² = 55.0%**

Class means (Candidate 1 frame; the Candidate 3 frame differs only by an offset):

| Class | n | mean η₁ | SD |
|---|---|---|---|
| AI | 1 | +7,246 ppm | — |
| TOS | 7 | +7,028 ppm | 127 ppm |
| NTB | 3 | +6,981 ppm | 141 ppm |
| AAF | 2 | +6,880 ppm | 24 ppm |
| ESC | 3 | +6,786 ppm | 146 ppm |

Two findings, and the second matters more than the first.

**(a) The signal is marginal and confounded.** p = 0.050 sits exactly on the conventional threshold, with 16 points across 5 classes and one class of a single member. The ESC class is dominated by two BIPM determinations from the same instrument and the same team, so "boundary class" is not cleanly separated from "laboratory." Booked as D-APC.3. Torsion-balance versus non-torsion-balance as a two-class split gives a difference of only **104 ppm** — smaller than the within-class SD.

**(b) Test 2 cannot discriminate the candidates, and this is forced, not incidental.** The required leakage η_i = 1 − G_i/G_true is an affine function of G_i, and the F-ratio is invariant under affine rescaling. **Every hypothesis of the form "G_true = a constant" therefore yields the identical F, p and η².** Test 2 measures whether the dispersion is organised by boundary at all; it carries no information about which candidate carries the gap. Any future use of Appendix C that presents a boundary correlation as support for one candidate over another is making a mistake this section forecloses.

**Test 2 verdict: weak, ambiguous, and non-discriminating.** Boundary class accounts for at most about half the dispersion, on 16 points, with laboratory identity unseparated.

## 2.4 — Test 3: Sign

This is the test the original Appendix C proposal did not contain, and it is the one that bites.

Under Candidate 3, G_true = 6.6719165 × 10⁻¹¹, and leakage can only lower a reading. Every determination should therefore lie at or below that value.

- Determinations lying **above** the predicted true value: **15 of 16**
- Binomial test against 50/50: **p = 2.6 × 10⁻⁴**
- Determinations more than 3σ above (own published uncertainty): **9 of 16**
- Median excess: **+8.7σ**; maximum excess: **+33.3σ** (HUSTᴀ-18)
- Only LENS-14 sits on the prediction, at −0.01σ — and LENS-14 has the second-largest uncertainty in the set

The required η₃ column of §2.1 is negative for fifteen of sixteen determinations. A negative leakage is a *refund*: it would require a mechanism that raises a laboratory reading. AP06 contains no such mechanism, and neither does the rest of the corpus.

**Test 3 verdict: Candidate 3's residual has the wrong sign for a leakage account, systematically, across every boundary class.** The Snap §9 already reports the sign flip and declines to attribute the residual. This document makes the size of what is unattributed explicit: it is not a small open item but a consistent 300-ppm-scale excess in fifteen independent determinations spanning four decades and five boundary geometries, of a kind the corpus cannot currently produce.

Booked as D-APC.2.

## 2.5 — Uncertainty-model dependence (reported, not selected)

The severity of §2.4 depends entirely on which uncertainty model is applied to the record, and that choice belongs to the metrology community, not to this corpus. Three published treatments, all applied to the same sixteen numbers:

| Uncertainty model | Realised prediction stands | Structural prediction stands |
|---|---|---|
| Formal weighted mean, ±0.000038 | **63σ low** | 1,232σ high |
| CODATA recommended, ±0.00015 (3.9 expansion) | **16σ low** | 316σ high |
| Conservative dark-uncertainty model, ±0.0015 | **1.6σ low** | 31σ high |

The most conservative published model — which argues that the recommended uncertainty is substantially underestimated given the mutual inconsistency of the data — leaves the realised prediction **1.6σ** below consensus, which is unremarkable. The structural prediction is excluded under every model, by 31σ at the most generous.

**This table is the honest summary of the empirical standing of both candidates**, and it should travel with any statement of either. Selecting the model that flatters the prediction would be the same error KS-CCC.1 exists to prevent, transposed from the magnitude of the commitment to the width of the target.

---

## PART C — FINDINGS AND DISPOSITIONS

## 3.1 — Candidate 1: falsified on homogeneity

Apparatus leakage cannot carry the 0.69% gap. It would require the mechanism AP06 defines as boundary-dependent to be constant to 2.3% across the most heterogeneous set of boundaries in precision metrology, while AP06's own values for that mechanism span twelve orders of magnitude. The corpus cannot identify inter-laboratory scatter as leakage's signature and simultaneously ask leakage to carry forty-three times that signature.

Ø Predictions Part II should be amended on adoption to retire Candidate 1 in its strong form. Its weak form — that leakage contributes at scatter scale — survives and is consistent with Test 2's marginal class structure.

## 3.2 — Candidate 3: survives the elimination, with the residual worsened

The commitment survives as the universal term, and it is the only one of the three candidates not excluded by Test 1. But it acquires a specific and stated problem: fifteen of sixteen determinations lie above its predicted value, up to 33σ, and the corpus has no mechanism that raises a reading. Under CODATA's own expanded uncertainty the prediction is 16σ low; under the most conservative published model, 1.6σ low.

The honest statement is: **the commitment is the only surviving structural account of the gap, and it is not yet reconciled with the record it is meant to explain.** Both halves of that sentence belong in §9 of The Snap.

## 3.3 — Disposition of KS-CCC.4

The switch as written fires if apparatus-leakage corrections come out at gap scale rather than scatter scale. They come out at gap scale in *magnitude* but fail the homogeneity condition that would make them leakage at all. **KS-CCC.4 does not fire.**

But the pass is weaker than the switch's wording suggests, and the wording should be tightened on adoption. As written, the switch could be read as confirmed by this execution. It is not: **the outcome is Outcome N, not Outcome S.** Candidate 1 falls, and Candidate 3 survives without a leakage account of its own residual. The switch should be reworded to separate the two claims it currently conflates:

> **KS-CCC.4a** — fires if leakage corrections of gap scale are shown to be boundary-homogeneous by a mechanism AP06 supplies. (Revives Candidate 1.)
> **KS-CCC.4b** — fires if the residual excess of §2.4 is shown to be structural rather than laboratory systematics. (Kills Candidate 3's universal term.)

## 3.4 — What this does not settle

It does not measure G. It does not re-derive any laboratory's systematic budget, and a single unrecognised systematic in the two BIPM determinations — the two highest values in the record, from one instrument — would move both Test 2 and Test 3. It does not test Candidate 2, the puncture normalisation, which The Snap §11 excludes by sign independently. It does not decide the uncertainty model, and §2.5 shows the verdict on Candidate 3 turns on that choice.

Most importantly: with no predictive η from AP06 (D-APC.1), Test 2 can only ask whether class labels organise the dispersion. It cannot ask whether the *right* boundary geometries leak by the *right* amounts. Until that debt is paid, the leakage account of the scatter is a hypothesis with a class label, not a prediction.

---

## 4 — Method notes and limitations

**4.1 — On the pre-registration.** Part A was written from the definitions of the two candidates and from AP06's own domain-dependence claim, with both scale references (gap 6,938 ppm; scatter 551/164 ppm) fixed by external numbers before any η was computed. Tests 1 and 3 are forced by the mechanism: leakage is boundary-dependent, and leakage lowers readings. Neither threshold was chosen to produce an outcome. **However**, Part A and Part B were produced in one pass, so the ordering is asserted rather than demonstrated. If this document is to carry pre-registration weight under KS-CCC.1's discipline, Part A should be hashed and published separately before Part B is released. That is a procedural recommendation, not a finding.

**4.2 — Small-n.** Sixteen determinations across five classes, one of them singleton. The ANOVA is fragile; the two-class split is not. No result in §2.2 or §2.4 depends on the ANOVA.

**4.3 — Published central values only.** Some values in the set differ from their originally published versions after later corrections (NIST-82 for fibre anelasticity; JILA for calculation errors identified in 2019). The CODATA 2022 set is used as CODATA states it, without adjustment.

**4.4 — Correlations ignored.** CODATA records three correlation coefficients among these data. They are not modelled here; including them would slightly change the weighted mean and χ², and none of the three tests depends on the weighted mean except §2.5's first row.

---

## 5 — Data provenance

Sixteen values of G, uncertainties, and method descriptions: CODATA 2022 recommended values, Table XXX (Mohr, Newell, Taylor & Tiesinga; the same set as the 2018 adjustment, with no new datum admitted and the same 3.9 expansion factor applied). Method taxonomy: the Bayesian systematic-error re-analysis of the same set, Eur. Phys. J. C (2023). Conservative uncertainty model: Bodnar & Elster, *Shades of dark uncertainty and consensus value for the Newtonian constant of gravitation* (2019). CODATA recommended value: G = 6.67430(15) × 10⁻¹¹ m³ kg⁻¹ s⁻², unchanged between the 2018 and 2022 adjustments.

Structural and realised targets: AP28 (The Constant) and The Snap (AP_CCC draft), computed at 30-digit precision from CODATA 2022 α_em, ℏ, c, m_e.

---

## 6 — Verification script

```python
import math
from statistics import mean, stdev

# CODATA 2022 Table XXX — the 16 input data for G (units 1e-11 m^3 kg^-1 s^-2)
D = [
 ("NIST-82","TOS",6.67248,0.00043),  ("TR&D-96","TOS",6.6729,0.00050),
 ("LANL-97","TOS",6.67398,0.00070),  ("UWash-00","AAF",6.674255,0.000092),
 ("BIPM-01","ESC",6.67559,0.00027),  ("UWup-02","NTB",6.67422,0.00098),
 ("MSL-03","ESC",6.67387,0.00027),   ("HUST-05","TOS",6.67222,0.00087),
 ("UZur-06","NTB",6.67425,0.00012),  ("HUST-09","TOS",6.67349,0.00018),
 ("BIPM-14","ESC",6.67554,0.00016),  ("LENS-14","AI", 6.67191,0.00099),
 ("UCI-14","TOS",6.67435,0.00013),   ("HUSTt-18","TOS",6.674184,0.000078),
 ("HUSTa-18","AAF",6.674484,0.000077),("JILA-18","NTB",6.67260,0.00025),
]
G_COD, G_STRUCT, G_REAL = 6.67430, 6.7206038, 6.6719165

vals = [d[2] for d in D]; w = [1/d[3]**2 for d in D]
wm = sum(x*v for x,v in zip(w,vals))/sum(w); uwm = math.sqrt(1/sum(w))
chi2 = sum(x*(v-wm)**2 for x,v in zip(w,vals))
print(f"spread {(max(vals)-min(vals))/G_COD*1e6:.0f} ppm | SD {stdev(vals)/G_COD*1e6:.0f} ppm")
print(f"weighted mean {wm:.6f}+/-{uwm:.6f} | chi2/nu {chi2/(len(D)-1):.2f} | Birge {math.sqrt(chi2/(len(D)-1)):.2f}")
print(f"AP28 gap {(G_STRUCT-G_COD)/G_COD*1e6:.0f} ppm")

for name, Gt in [("Candidate 1", G_STRUCT), ("Candidate 3", G_REAL)]:
    e = [(1 - d[2]/Gt)*1e6 for d in D]
    print(f"\n{name}: mean {mean(e):+.0f} ppm  SD {stdev(e):.0f} ppm  CV {abs(stdev(e)/mean(e)):.3f}")
    cls = {}
    for d, x in zip(D, e): cls.setdefault(d[1], []).append(x)
    gm = mean(e); k, n = len(cls), len(e)
    ssb = sum(len(v)*(mean(v)-gm)**2 for v in cls.values())
    ssw = sum((x-mean(v))**2 for v in cls.values() for x in v)
    print(f"  F({k-1},{n-k}) = {(ssb/(k-1))/(ssw/(n-k)):.3f}   eta^2 = {ssb/(ssb+ssw)*100:.1f}%")

above = [(d[0], (d[2]-G_REAL)/d[3]) for d in D if d[2] > G_REAL]
print(f"\nTest 3: {len(above)}/16 above the realised prediction; "
      f"max {max(s for _,s in above):+.1f} sigma; "
      f">3 sigma: {sum(1 for _,s in above if s>3)}")
for u, lbl in [(uwm,"formal"), (0.00015,"CODATA"), (0.0015,"conservative")]:
    print(f"  realised is {(wm-G_REAL)/u:+.1f} sigma ({lbl}) | "
          f"structural is {(wm-G_STRUCT)/u:+.1f} sigma")
```

Expected output: spread 551 ppm, SD 164 ppm, weighted mean 6.674290 ± 0.000038, χ²/ν 13.19, Birge 3.63, gap 6938 ppm; Candidate 1 CV 0.023, Candidate 3 CV 0.590; F(4,11) = 3.355, η² 55.0%; 15/16 above, max +33.3σ.

---

*This work is published for free, forever.*

*Don't be a cunt. Be kind.*

**the420code.org**

| | |
|---|---|
| **Series** | The 420 Code |
| **Catalogue** | Ø Predictions — supporting documents |
| **Title** | Appendix C — Execution: The Leakage Discriminator |
| **Medium** | Natural Philosophy / Physics |
| **Artist** | G |
| **Status** | Draft v0.1 — unlocked, not adopted |
