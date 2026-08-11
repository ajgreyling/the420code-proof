# Tier 2 blind boundary coding — code-book

**Written:** 2026-08-11, before opening any of the seventeen papers.
**Coder:** Klaus (AJ's AI), per `AJ_Handover_and_Tier2_Protocol.md` §2.
**Scope:** code each apparatus's boundary physics from the apparatus/method
sections only. No abstracts, no results, no conclusions, no values of G.
Any unavoidable glimpse of a G value is logged in the coding notes.

## The seventeen experiments

Authoritative citations to be pulled from CODATA 2022 (arXiv:2409.03787,
Table XXX) at coding time — not retyped from memory here.

NIST-82 · TR&D-96 · LANL-97 · UWash-00 · BIPM-01 · UWup-02 · MSL-03 ·
HUST-05 · UZur-06 · HUST-09 · LENS-14 · BIPM-14 · UCI-14 · HUST-T-18 ·
HUST-A-18 · JILA-18 · NIST-26

## Operational definitions — the five dimensions

Coded per experiment, from apparatus/method text and figures only.

### D1 — Test-mass containment
Categorical: **FF** (test mass in free fall during the science measurement,
no mechanical suspension) / **SUS** (test mass suspended inside a sealed
chamber). The state during the actual G-sensitive measurement governs;
loading/handling states are ignored.

### D2 — Source-mass position
Categorical: **IN** (source mass inside the vacuum boundary that encloses
the test mass) / **OUT** (outside it). "Vacuum boundary" = the outermost
wall of the evacuated volume containing the test mass. If source masses sit
in a separate evacuated volume, they are OUT unless the two volumes share
one common boundary wall enclosing both.

### D3 — Enclosure closure
Integer count of distinct solid boundary layers crossed on the straight
line from source-mass surface to test-mass surface, with the material of
each layer recorded in order (e.g. `2: [Al vacuum can, Cu shield]`).
A window or port counts as part of its layer; apertures (open holes) are
noted separately and do not reduce the count of layers actually crossed
if the line of action passes through solid material. Where geometry makes
the count direction-dependent, code the minimum and note the range.

### D4 — Suspension element
Categorical: **none** / **fibre** / **strip**, with material, and the
published quality factor **Q** where it appears in the apparatus/method
text. Q values that appear only in results/analysis sections are recorded
as "not stated in methods" — we do not chase them.

### D5 — Boundary sphericity class (geometry only)
Ordinal 1–5, judged from drawings and apparatus description, answering
"how spherical/closed is the boundary immediately around the test mass":
- **5** — closed shell, near-spherical or highly symmetric, fully
  surrounding the test mass
- **4** — closed shell, cylindrical or rectangular
- **3** — mostly closed; significant ports, windows, or feedthroughs
- **2** — partial enclosure (open on one or more sides)
- **1** — essentially open geometry

## Recording format

One row per experiment in `CODED_TABLE.csv`:
`id, source_paper, sections_pages_read, D1, D2, D3_count, D3_materials,
D4_element, D4_material, D4_Q, D5, notes`

Notes must include page/figure references for every coded judgement, any
ambiguity and how it was resolved (conservative coding, both readings
noted), and any blinding incident (a G value or residual glimpsed).

## Blinding guard

The coding pass will be executed by a fresh agent context given only this
code-book and the experiment list — not the handover document, not the
corpus's predicted values, not the Tier 1 results. Training-data knowledge
of published G values is unavoidable (the protocol acknowledges this);
what this guard protects is knowledge of the corpus's predictions and the
residual pattern against them. The supervising agent's own contaminated
priors are declared in `DECLARED_PRIORS.md`.

## Choreography (each step its own commit, in order)

1. This code-book + declared priors. *(this commit)*
2. `CODED_TABLE.csv` — all seventeen coded, with notes.
3. Unblinding key requested from G.
4. Analysis per the pre-registered criteria (KS-CCC.4a, KS-CCC.4b),
   under the declared limit that class-correlation statistics are
   identical under every constant-true-value hypothesis.
5. Read AP44 + WP-CCC.1 in full; independent verdict committed,
   agreement or dissent.
