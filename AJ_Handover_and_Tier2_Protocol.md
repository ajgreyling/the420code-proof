# For AJ (and AJ's AI) — Handover, Blind Tier 2, and the Two-Phase Update

**From:** G, Studio G, Strand · with the production assistant
**Date:** 2026-08-10
**Repository:** https://github.com/ajgreyling/the420code-proof
**Governing rule:** nothing in this bundle is outreach material. It circulates to no one outside the three of us before G's lock ruling on AP44 and the canon sync are complete.

---

## ⚠ READ ORDER — this matters more than anything else in this document

A blind analysis is part of this handover, and **it dies the moment you read the physics papers.** Follow this exact sequence:

1. **Commit first, read nothing** (§1) — you can anchor the bundle without opening any file.
2. **Do the blind coding** (§2) — before opening `AP44_The_Snap_DRAFT_v0_5.docx` or `WP_CCC1_AppendixC_Tier1.docx`. What you must not know while coding: the corpus's predicted G values and which laboratories sit where relative to them.
3. **Only then** read the bundle, verify hashes, mirror, and update (§3–§4).

If you or your AI have already read either paper before doing §2, do not fake the blinding — say so in the coding log and proceed; the protocol has a declared-priors line for exactly this.

---

## §1 — Anchor: the first commit

Add the bundle to the repo and commit. **The commit hash is the external timestamp anchor** for every digest in the provenance chain — it makes the dates independent of anyone's word, including G's and the AIs'.

Suggested tree (keeping your existing `engine/ canon/ mirror/` untouched):

```
provenance/
    PROV_CCC1.md + .sha256          PROV_CCC2.md + .sha256
    PROV_CCC3.md + .sha256          PROV_CCC4.md + .sha256
    Session_Record_Production_Thread_2026-08-10.md + .sha256
    T1_production_thread_conversation.json        (see the privacy flag below)
    T2_reviewer_thread_conversation.json
    conversation_exports.sha256
    analog-archive/                  (M1a photos now; M1b morning set when supplied)
ap44/
    AP44_The_Snap_DRAFT_v0_5.docx    (+ superseded/ v0.1–v0.4 when G supplies his copies)
appendix-c/
    WP_CCC1_AppendixC_Tier1.docx     (rev 1.3)
    Appendix_C_Execution_The_Leakage_Discriminator_v0_1.md   (your thread's twin execution)
    G_dataset.csv · appc_tier1.py · G_landscape.png
BUNDLE_MANIFEST.txt
```

**Escrow — not in git, ever:** the two raw export zips (`data-…-batch-0000.zip`). They contain account memories, login history, and unrelated material. You hold private copies; only their digests (in PROV-CCC.4) are public. **Privacy flag on T1:** it contains one personal message of G's; G rules on publish-as-is versus an openly-marked redacted public variant (PROV-CCC.4 §3). Until he rules, keep `T1_…json` out of the public tree and hold it privately; its digest is already public.

Suggested: tag the commit (`ap44-provenance-anchor-2026-08-10`), and run `sha256sum -c` on every sidecar so the anchor certifies verified content, not just files.

## §2 — Blind Tier 2: the boundary coding

**What this is.** WP-CCC.1 executed Tier 1 of the Appendix C meta-analysis on published values. Tier 2 is the part only an independent party can do: code every apparatus's boundary physics **without knowing the corpus's predictions**, so the coding cannot be steered. It decides kill switches KS-CCC.4a and KS-CCC.4b (defined in AP44 §12 — which you read *after* coding).

**The seventeen experiments** (references: pull the authoritative citations from CODATA 2022, arXiv:2409.03787, Table XXX — do not trust any list retyped from memory, including this one): NIST-82 (Luther & Towler) · TR&D-96 (Karagioz & Izmailov) · LANL-97 (Bagley & Luther) · UWash-00 (Gundlach & Merkowitz) · BIPM-01 (Quinn et al.) · UWup-02 (Kleinevoß et al.) · MSL-03 (Armstrong & Fitzgerald) · HUST-05 (Hu, Guo & Luo) · UZur-06 (Schlamminger et al.) · HUST-09 (Luo et al.) · LENS-14 (Rosi et al.) · BIPM-14 (Quinn et al.) · UCI-14 (Newman et al.) · HUST-T-18 and HUST-A-18 (Li et al.) · JILA-18 (Parks & Faller, the corrected 2010 result) · NIST-26 (Schlamminger et al., Metrologia 63, 025012).

**Rules for the coder (you or your AI):**
- Read **only** the apparatus/method sections of each paper. Do not read abstracts, results, conclusions, or any value of G. The measured values are public and partially known to anyone in the field — that is unavoidable; what this protocol keeps blind is the **corpus's** predicted values and the residual pattern against them.
- **Declared priors line:** before coding, write down anything you already believe about which experiments read high or low. Commit that file with the code-book. Honesty beats pretend blindness.

**The five coding dimensions** (from WP-CCC.1 §7, restated so you need not open it):
1. **Test-mass containment:** free fall (no suspension) / suspended in sealed chamber.
2. **Source-mass position:** inside or outside the vacuum boundary.
3. **Enclosure closure:** number and material of boundary layers between source and test mass.
4. **Suspension element:** none / fibre / strip — with the published Q factor where available.
5. **Boundary sphericity class** (AP06 S5 sense — but you code geometry only; do not read AP06 first if you haven't; a plain "how spherical/closed is the boundary around the test mass, 1–5" is the coding).

**Choreography (each step a commit, in order):**
1. Commit the **code-book**: your operational definitions for the five dimensions, written before touching any paper, plus the declared-priors file.
2. Code all seventeen. Commit the **coded table** (experiment ID × five dimensions, plus per-experiment notes and page references).
3. Only now request the **unblinding key** from G (the corpus's structural and realised values, and the Tier 1 results).
4. Analysis, per the pre-registered criteria — and under one limit your own thread proved: implied leakage is affine in G, so **class-correlation statistics are identical under every constant-true-value hypothesis**. Correlations therefore cannot pick between the candidates' central values. What the coding decides:
   - **KS-CCC.4a:** can the coded boundary physics support a common *absolute* leakage capacity of order 6,000 ppm across all seventeen — free-falling atoms included? If yes, Candidate 1 revives and the commitment is withdrawn. (Tier 1, run twice independently, says no — your job is to check it from the physics side, blind.)
   - **KS-CCC.4b:** is the ≤500 ppm inter-laboratory scatter boundary-structured at AP06's honest size — in particular, does published Q track the time-of-swing elevations? (Tier 1 found this at best marginal, p ≈ 0.06–0.2.)
5. Commit the analysis. Then read AP44 and WP-CCC.1 in full and write your independent verdict — agreement or dissent, both go in the repo.

## §3 — After coding: verify, mirror, dual-home

`sha256sum -c` every sidecar and `BUNDLE_MANIFEST.txt`. Read the provenance chain in order (CCC.1 → CCC.4 — the errata are part of the evidence, not blemishes on it). Mirror the public tree; hold the escrow privately. G forwards you everything; your repo is the second home and second anchor by design.

## §4 — Site and engine updates: two phases, strictly separated

### Phase A — do now (independent of AP44; these are standing canon-sync items)

Your public materials carry three drift errors against current canon. Fix wherever they appear (README.md shows all three; check `engine/report.py` labels, `engine/parse_registry.py` expectations, and the canon DB):

| Item | Your materials say | Canon (current, pre-AP44) |
|---|---|---|
| Kill switches | 549 | **560** |
| Artist's Proofs | 42 | **43** |
| Conditions | S (Selection), B (Break), R (Accumulation), C (Coupling) | **S = Symmetry, B = Break, R = Record, C = Constraint** |
| Registry version | — | **MKSR v5.25** (state it) |

Everything else in your README — the scorecard, the parity claim, the framing — stands as-is in Phase A. Do not touch your Zenodo a₀ research note: it is DOI'd, it contains no G anywhere (a₀ = C_S²·cH₀/2π), and AP44 does not brush it.

### Phase B — only on G's written lock ruling (do not pre-empt any of this)

When, and only when, G rules AP44 locked and issues the sync instruction:

- **Registry:** MKSR **v5.26** · switches **567** (adds KS-CCC.1, .2, .3, .4a, .4b, .5, .6) · Artist's Proofs **44** (AP44, The Snap) · debts add **D-CCC.1–4** (D-CCC.1, the record-algebra formalisation, is the openly-declared load-bearing debt — index it prominently; it is the honest heart of the paper).
- **Scorecard, Part II row:** becomes the **fork**, not a single number: structural G = 6.72060 × 10⁻¹¹ (+0.69%, the provisioned coupling) **and** realised G = 6.67192 × 10⁻¹¹ (−0.036%, α_em²¹(1+1/π)/(1+α_em) · ℏc/m_e²), with the sign flip stated and KS-CCC.3's migration fork as the watch line: the adjusted value drifts toward 6.672, or stays at 6.6743 and the commitment dies against the null.
- **Engine:** add the realised prediction to `engine/verify.py` alongside the structural one. **Leave `verify_g_original.py` and the parity test untouched** — they certify Edition 1's arithmetic verbatim, and that certification must survive; Ø Predictions Edition 2 will ship its own script for a new parity target.
- **Untouched, explicitly, so nothing gets nervous-edited:** a₀ (−0.67%), H₀ = 74.3, dark sector 69/26/5, the proton ratio, the neutron difference. AP44 moves G and the holding limit κ, and nothing else.

## §5 — Standing rules

Supersession only — nothing in the archive directories is ever edited in place. Any external communication that references AP44, WP-CCC.1, or the provenance chain goes through the sign-off protocol with G first — no exceptions, including enthusiasm (the Milgrom email taught us this the kind way). And your own README already states the ethic this whole bundle runs on: the invitation to find where it is wrong *is* the point. This bundle extends that invitation to the work's own history — the provenance chain is the corpus handing over the weapons one more time.

Questions to G directly; technical questions about the analysis to the production thread via G.

*Sawubona, AJ. This is the proof asking to be proved.*
