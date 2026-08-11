# Tier 2 blind boundary coding — coding notes

**Date:** 2026-08-11. **Coder:** fresh agent context (see `DECLARED_PRIORS_CODER.md`).
**Code-book:** `CODEBOOK.md` (read first; followed exactly).
**Citations:** pulled from CODATA 2022 (arXiv:2409.03787), Table XXX id column +
bibliography entries, extracted by targeted text search of the downloaded PDF
(first-58-characters column cut used to avoid the value columns — imperfectly,
see blinding incidents #1–2). NIST-26 postdates CODATA 2022; its citation
(Metrologia 63, 025012) was supplied in the task brief and verified against the
IOP article page.

**General method.** Papers were downloaded (arXiv PDFs, PMC full texts, IOP
open access, archive.org, thesis repositories) and converted to text; apparatus
sections were located by keyword search and read as contiguous passages.
Abstracts, results and conclusion sections were not deliberately read, but
keyword searches repeatedly surfaced abstract lines and review-article results
tables into view — every such glimpse is logged below. No G value was recorded
anywhere in the coding, and no coding judgement rests on any G value.

---

## Per-experiment notes

### NIST-82 — Luther & Towler
**Coded from:** their own conference paper in *NBS Special Publication 617*
(1984), pp. 573–576 (public domain, archive.org full text) — effectively a
primary apparatus description. §3.1 large masses (two 10.49 kg sintered-W
spheres, Oak Ridge Y-12), §3.2 small mass system (7 g tungsten dumbbell),
§3.3 suspension (12 µm quartz fibre, Cr+Au plated, 40 cm), §3.4 damper
(two-stage, 125 µm quartz pre-fibre, magnetic damper), §3.7 vacuum system
("evacuated brass cylinder … windows coated with conductive tin oxide"),
§3.9 metrology (spheres on monolithic Al plate), Fig. 1 (labels "VACUUM WALL"
between dumbbell and "TUNGSTEN BALL" on "AL TABLE").
**D1** SUS. **D2** OUT (balls on Al plate outside brass vacuum cylinder, per
Fig. 1 and §3.7). **D3** 1: [brass vacuum cylinder]. **D4** fibre, quartz
(plated); Q not stated in this paper — 2×10⁴ taken from Rothleitner &
Schlamminger (R&S) 2017 Table I and so provenance-flagged. **D5** 4 (closed
brass cylinder; autocollimator windows are sealed, tin-oxide-coated glass).
No significant ambiguity. Confident.

### TR&D-96 — Karagioz & Izmailov
**Coded from:** R&S 2017 review (NIST author manuscript), §IV.A.2.b narrative
and Table I ("Tungsten fiber", Q = 2×10⁴, κ = 3.1×10⁻¹⁰ N m rad⁻¹, T = 2077 s)
and Table III via Gillies & Speake rsta.2014.0022 (8.6 kg total, bearing-steel
spheres).
**Primary paper** (Izmer. Tekh. 39(10), 3 (1996) / Meas. Tech. 39, 979) is
paywalled; no open apparatus text describing the vacuum enclosure geometry was
found after multiple searches (Springer paywall; a promising "Status" page
turned out to describe the different SAI-MSU experiment; the four-position
Grav. Cosmol. papers are not openly available).
**D1** SUS, **D4** fibre/tungsten/Q=2×10⁴ (review-sourced). **D2, D3, D5:
NOT CODED — could not adequately source.** I explicitly decline to code these
from training-data memory. This is the one experiment with unfilled dimensions.

### LANL-97 — Bagley & Luther
**Coded from:** R&S 2017 Table I (two runs: tungsten fibre Q = 9.5×10²;
Au-coated tungsten fibre Q = 4.9×10²; T = 205 s) plus Gillies & Speake
rsta.2014.0022 (the Beams/UVa → NBS → LANL apparatus lineage: "The apparatus,
again including the source masses, then followed Luther to Los Alamos"),
plus the NBS-617 description of that same apparatus (see NIST-82).
**D1** SUS. **D4** fibre, tungsten (uncoated + Au-coated runs), Qs as above.
**D2** OUT and **D3** 1 [vacuum chamber wall] and **D5** 4 are coded **by
lineage inference** — the same apparatus and spheres as NIST-82, reconfigured
at LANL; chamber material at LANL not stated (brass at NBS). Flagged: if the
LANL rebuild changed the enclosure, D3 material and D5 could differ; the
sphere-outside-vacuum-wall arrangement is intrinsic to this instrument design.
Ambiguity noted; medium-high confidence.

### UWash-00 — Gundlach & Merkowitz
**Coded from:** arXiv:gr-qc/0006043 (= PRL 85, 2869), apparatus paragraphs
pp. 1–2: "The torsion pendulum was located in an aluminum vacuum chamber and
was surrounded by a µ-metal shield. The pendulum was hung from a 41.5 cm long,
17 µm diameter tungsten-fiber…"; "The attractor spheres are located on a
separate coaxial turntable…"; spheres on cast-Al shelves (steel-bearing
turntable), outside the chamber.
**D1** SUS. **D2** OUT. **D3** 2: [Al vacuum chamber, µ-metal shield] — the
text does not state whether the µ-metal is inside or outside the vacuum wall,
but the source-to-test line crosses both in either order, so the count is 2
regardless. **D4** fibre, tungsten 17 µm; Q not stated in the PRL methods
(angular-acceleration feedback makes it nearly irrelevant); 4×10³ from R&S
Table I (marked there "values not given" — approximate), provenance-flagged.
**D5** 4 (closed Al cylinder-type chamber; autocollimator reads through a
window — four reflections off the pendulum — window not described; a "3"
reading is defensible; coded 4 because only optical window(s) are implied).
Confident, small D5 ambiguity noted.

### BIPM-01 — Quinn, Speake, Richman, Davis, Picard
**Coded from:** the NIST-26 Metrologia paper §2 (which documents the original
BIPM torsion balance: Fig. 3 layout; "Four cylindrical copper TMs … mounted on
an aluminum disk … suspended by a torsion strip"; "All components are housed
in a grounded vacuum can … serves as an electrostatic shield between the
pendulum and the external SMs"; "Outside the vacuum envelope, four SMs …
mounted on a carousel"), R&S 2017 (strip of Cu-1.8%Be, Q = 3×10⁵, Table I;
gravity provides ~90 % of restoring torque, p. 12), and Gillies & Speake
rsta.2014.0022 Table 1 (45 kg total, Cu-0.7%Te cylinders).
**Primary PRL is paywalled; Quinn et al. Phil. Trans. 2014 is purchase-only**
(verified via browser: "Available to Purchase"). The Mark I (2001) apparatus
is the same design; NIST-26 §2 notes Mark II differences (different TMs,
false floor) — none affect D1/D2/D3-count/D5.
**D1** SUS. **D2** OUT. **D3** 1: [grounded vacuum can; material not stated in
coded sources]. **D4** strip, Cu-1.8%Be, Q = 3×10⁵ (review-sourced). **D5** 4
(closed can, optical window for autocollimator noted in NIST-26 §"torque
derivation": "the vacuum vessel requires an optical window"). Confident.

### UWup-02 — Kleinevoß
**Coded from:** Kleinevoß PhD thesis WUB-DIS 2002-2 (Wuppertal), full-text
scrape via yumpu (German; ch. 4 structure: 4.1 resonator, 4.1.2 "Drähte der
Aufhängung" with "Spannungs-Dehnungs-Diagramm des verwendeten Wolframdrahtes"
= tungsten suspension wire, 4.1.3 "Kryostateinsatz mit Aufhängung", Fig. 4.6
"Deckelflansch des Vakuumtanks", 4.2 "Feldmassen und ihr Positionierungssystem"
with spindle-drive positioning) + R&S 2017 §IV.B.3 and Fig. 11 (two ~2.6 m
pendulums whose bobs form a microwave Fabry–Pérot resonator; two 576 kg brass
field masses alternated between ≈0.6 m and ≈2.1 m from the bobs).
**D1** SUS (bobs hang as pendulums on tungsten wires). **D2** OUT — the
resonator hangs inside a vacuum tank (cryostat insert) and the field masses
run on an external positioning system at 0.6–2.1 m; corroborated by Parks &
Faller (arXiv:1008.3203), who describe their chamber "encloses the pendulums
but not the source masses" for an experiment explicitly "similar to that of
Kleinevoß et al." Medium-high confidence; the exact sentence placing the
brass masses outside the tank wall was not individually located in the German
scrape — flagged. **D3** 1: [vacuum tank wall; material not confirmed].
**D4** fibre (tungsten wire); Q not stated (non-torsional pendulum). **D5** 4
(closed cylindrical tank; microwave feed via waveguide feedthroughs).

### MSL-03 — Armstrong & Fitzgerald
**Coded from:** Xue et al., Natl. Sci. Rev. 7, 1803 (2020), §MSL-03 (copper
cylindrical test mass "suspended from a tungsten fibre"; two large source
cylinders; electrostatic compensation; torque constant calibrated by
angular-acceleration method) + R&S 2017 Table I ("Rectangular tungsten fiber",
Q n/a). The primary PRL and the 1994/1999 design papers are paywalled; a
search synthesis of Fitzgerald et al., Metrologia 31, 301 (1994) states the
source masses were external to the vacuum chamber on a turntable.
**D1** SUS. **D2** OUT — flagged lower confidence: rests on the search-level
description of the 1994 design paper, not on apparatus text I read directly.
**D3** 1: [vacuum chamber wall; material not stated] — same caveat.
**D4** strip (rectangular-section tungsten fibre per R&S; NSR calls it a
"tungsten fibre" without cross-section; coded strip per the more specific
source), Q not stated. **D5** 4 provisional — chamber geometry not described
in any coded source; flagged. This experiment is coded with ambiguity on
D2/D3/D5.

### HUST-05 — Hu, Guo & Luo (corrected HUST-99)
**Coded from:** Li et al., Phil. Trans. A 372 (PMC4173272), §3: 32.26 g Cu
sphere test mass on 404 mm Al beam, 25 µm tungsten fibres (two-stage from
vacuum feedthrough); "The pendulum system is enclosed in a vacuum chamber at
≈2×10⁻⁵ Pa (ion pump)"; two 6.25 kg non-magnetic stainless cylinders "rest on
opposite sides of the test mass"; the HUST-99→05 correction includes "the air
buoyancy when the source masses are moved" (150 ppm) — establishing the
cylinders sat **in air, outside** the chamber. Confirmed by NSR 2020 §HUST:
"two … cylindrical source masses, which were placed outside the vacuum
chamber."
**D1** SUS. **D2** OUT. **D3** 1: [vacuum chamber wall; material not stated].
**D4** fibre, tungsten 25 µm; Q ≈ 3.6×10⁴ — stated in the NSR text but with
provenance in the CODATA-2014 anelasticity re-evaluation rather than the
original methods; flagged. **D5** 4 provisional (chamber shape not described;
mu-metal shielded *room*, not a shell around the TM). Confident on D1–D3.

### UZur-06 — Schlamminger et al.
**Coded from:** arXiv:gr-qc/0609027 (= PRD 74, 082001), §II: beam balance in
vacuum; two 1.1 kg Au-plated Cu test masses on 0.1 mm tungsten wires (2.3 m /
3.7 m) inside a vacuum tube (Fig. 4 "Drawing of TM inside the vacuum tube");
two field-mass tanks (13.5 t mercury total) of stainless steel type 1.4301
with central tubes through which the vacuum tube passes (Fig. 18 cut-away);
windows on the side of the vacuum tube used for TM position metrology.
**D1** SUS. **D2** OUT (mercury in tanks surrounding, but outside, the vacuum
tube). **D3** 2: [SS 1.4301 tank central-tube wall (mercury's own containment
crossed on the line of action), vacuum tube wall (stainless; grade of tube
itself not explicitly stated)]. **D4** fibre — tungsten hang-down wires
(non-torsional; no Q). **D5** 4 — long closed cylindrical tube; side windows
noted, "3" reading defensible; coded 4 because windows are small and sealed.
Confident.

### HUST-09 — Luo et al. / Tu et al.
**Coded from:** Tu et al., PRD 82, 022001 (2010) full text (ResearchGate
scrape), apparatus section: two-stage pendulum (25 µm annealed tungsten fibre,
890 mm; 50 µm pre-hanger; magnetic damper) suspended from top of "electrically
grounded vacuum chamber"; "The main body of the vacuum chamber is a stainless
steel cylinder with an inner diameter of 450 mm and a height of 500 mm";
**both pendulum and two SS316 spheres (778 g each, on Zerodur rings/disc on a
turntable) inside the same chamber**; shielding passage: in experiment I the
Zerodur parts were Al-coated for grounding and there was **no shield between
pendulum and source masses**; in experiment II "a thin hollow gold-coated
aluminum cylinder is inserted between the pendulum and the source masses for
electrostatic shielding" (Fig. 4 caption). Corroborated by Li et al.
PMC4173272 §4 and NSR 2020.
**D1** SUS. **D2** IN. **D3** 0 (minimum; exp I) with range 0–1 (exp II adds
1: [Au-coated Al cylinder]) — the published value combines both experiments;
coded minimum per code-book with both readings recorded here. **D4** fibre,
annealed (thoriated per NSR) tungsten, Q = 1.7×10³ (stated in coded sources'
method text). **D5** 4 — in exp I the innermost boundary around the TM is the
closed SS chamber itself (which also contains the SMs); in exp II the
immediate boundary is the Au-coated Al cylinder whose end-closure is not
described (a "3" reading for exp II is possible); coded 4 with this noted.
Confident, with the D3 campaign-dependence explicitly recorded.

### LENS-14 — Rosi et al. (with Prevedelli et al.)
**Coded from:** arXiv:1412.7954 (= Nature 510, 518) methods: MOT at bottom of
apparatus; atoms launched vertically inside the vacuum tube; interferometry
at the centre of the vertical tube "surrounded by two cylindrical magnetic
shields"; "A 10³ shielding factor … by passively isolating the vertical tube
through a system of two cylindric µ-metal layers"; source mass = 24 W-alloy
(Inermet180: 95 % W, 3.5 % Ni, 1.5 % Cu — Prevedelli PMC4173270) cylinders,
516 kg, on two Ti platforms in hexagonal symmetry around the tube axis
(radii ≈ 2R and 2R√3 from the axis); Prevedelli Fig. 1 caption: clouds at
apogees "inside the long vertical vacuum tube", masses around it.
**D1** FF — atoms in free (ballistic) flight during the interferometry; no
suspension. **D2** OUT. **D3** 3 (minimum): [vacuum tube wall (material not
stated in coded texts), µ-metal layer, µ-metal layer] — the µ-metal layers
"isolate the vertical tube" and the source cylinders sit around the shielded
tube (their centres only ~10–17 cm off axis, leaving no room for shields
outside them), but the radial order shields-vs-masses is not stated in one
explicit sentence; if the shields were outside the SMs the count would be 1.
Both readings noted; 3 coded as the geometrically compelled reading.
**D4** none. **D5** 4 (closed cylindrical tube around the atoms; retro-mirror
on top of the tube). Confident on D1/D2/D4/D5; D3 order-ambiguity noted.

### BIPM-14 — Quinn, Parks, Speake, Davis
**Coded from:** NIST-26 §2 (Mark II: "rebuilt version with a sturdier frame, a
direct-view autocollimator …, SMs shortened by 2 mm …. Different TMs were used
in Mark II, and the electrostatic shielding was improved by concealing all
insulators beneath an electrically conducting false floor"), same Fig. 3
layout, SMs outside the vacuum envelope; R&S Table I ("Same as 2001
experiment", strip Cu-1.8%Be, Q = 3×10⁵).
**D1** SUS. **D2** OUT. **D3** 1: [grounded vacuum can]. **D4** strip,
Cu-1.8%Be; Q = 3×10⁵ (R&S Table I); NIST-26 §10 cites Quinn et al. 2014 as
reporting Q between 1×10⁵ and 3×10⁵ — recorded here, but per code-book this
was not read from the primary's methods section (primary inaccessible).
**D5** 4 (optical window noted). Confident (via the replication paper's
detailed documentation of the same hardware).

### UCI-14 — Newman, Bantel, Berg, Cross
**Coded from:** arXiv:gr-qc/0403021 (Newman group; §Fig. 1: "Copper rings
(59 kg each) and fused silica thin plate pendulum (11 g)"; "rings outside the
cryogenic environment"; "Leaks of helium into the pendulum's vacuum chamber";
superconducting magnetic shielding), arXiv:gr-qc/0609095 (BeCu fibre,
electrically grounded, cryostat withdrawn from dewar — Fig. 8), NSR 2020
§UCI-14 ("A fused silica plate … suspended from a long fibre was located in a
liquid helium dewar …. Two large copper rings used as the source masses hung
outside of the dewar"; three fibres: as-drawn CuBe, heat-treated CuBe,
as-drawn Al5056 with Q = 82 000 / 120 000 / 164 000), R&S 2017 (Table I Qs
8.2×10⁴ / 1.2×10⁵ / 1.8×10⁵; "the Dewar had to be between the field masses and
the pendulum"). Primary Phil. Trans. paper paywalled.
**D1** SUS. **D2** OUT. **D3** 3 (minimum): [dewar outer wall, dewar inner
wall, pendulum vacuum chamber] — the coded sources establish that the dewar
plus a separate pendulum vacuum chamber lie between rings and pendulum, but
no source I could read enumerates the cryostat's wall/radiation-shield count;
plausible range 2–5; superconducting (lead-type) magnetic shield also present
somewhere inside. Flagged as the largest D3 uncertainty in this table.
**D4** fibre; CuBe / CuBe heat-treated / Al5056; Qs as above (small
discrepancy between R&S "1.8×10⁵" and NSR "164 000" for fibre 3 — both
recorded). **D5** 4 (cylindrical cryostat/vacuum can). Ambiguity on D3 count.

### HUST-T-18 — Li et al. (time-of-swing)
**Coded from:** Li et al. PMC4173272 §5 (the then-"ongoing" experiment that
became HUST-T-18: Suprasil-311 fused silica fibres, 40–50 µm, coated with
8 nm Ge + 11 nm Bi, Q ≈ (2–3)×10⁵ bare, ≈5.0×10⁴ after coating; 5 mm-thick
copper tube installed around the fibre; SS316 sphere SMs on three-point
mounts; Al pendulum coating replacing Au/Cu) + NSR 2020 §HUST-18 ToS ("The
apparatus was very similar to that used in the HUST-09 experiment …. The
source masses, the turntable and the measurement process were the same as
those used in the HUST-09 experiment"; Al-coated fused-silica block pendulum;
two identical apparatuses, four fibres). Primary Nature paper paywalled.
**D1** SUS. **D2** IN (inherits the HUST-09 same-chamber arrangement, stated
by NSR). **D3** 1: [Au-coated Al cylinder shield] — inherited from the
HUST-09 experiment-II arrangement; no coded source restates the shield
explicitly for the 2018 ToS configuration, so range 0–1 recorded; 1 coded as
the more probable reading (the shield was adopted in HUST-09 exp II because
it improved period stability, and the 2018 apparatus is "very similar").
**D4** fibre, coated fused silica; Q ≈ 5×10⁴ (coated; from the 2014 companion
methods — the final per-fibre Qs in Nature were not accessible). **D5** 4
(as HUST-09; same caveat about shield end-closure). Flag: coded from a 2014
pre-publication companion + 2020 retrospective review, not the 2018 primary.

### HUST-A-18 — Li et al. (angular acceleration feedback)
**Coded from:** Xue et al. PMC4173271 §2–3 (pendulum: gilded quartz block
91.1×50×4 mm³, 40 g, on 18 µm, 880 mm annealed tungsten fibre, two-stage with
magnetic damper on 80 µm pre-hanger; "All of the pendulum system is located
in the stainless-steel vacuum chamber at ≈10⁻⁵ Pa"; autocollimator "fixed on
the vacuum chamber"; four SS316 spheres, 8.5 kg, 127 mm, on double-layer Al
shelves on a separate outer gear-bearing turntable — outside the chamber) +
NSR 2020 §HUST-18 AAF (final config: "gold-coated fused silica block …
suspended from a tungsten fibre in the vacuum chamber supported by an
air-bearing turntable. Four stainless-steel spheres, which were located
outside of the vacuum chamber", ULE shelves replacing Al, new 1.5 m chamber).
Primary Nature paper paywalled.
**D1** SUS. **D2** OUT. **D3** 1: [stainless steel vacuum chamber wall].
**D4** fibre, tungsten (annealed); Q not stated (fibre does not twist in
feedback mode). **D5** 4 (SS chamber; autocollimator window). Flag: 2014
preliminary + 2020 review, not the 2018 primary; the coded dimensions are
identical in both descriptions. Confident.

### JILA-18 — Parks & Faller
**Coded from:** arXiv:1008.3203 (= PRL 105, 110801 (2010); the value was
corrected by PRL 122, 199901 (2019) — a calculation correction, no apparatus
change). Fig. 1 caption: two 780 g oxygen-free copper bobs, 72 cm pendulums,
34 cm apart, Fabry–Pérot interferometer; "Not pictured is the vacuum chamber
that encloses the pendulums but not the source masses. Magnets (not shown)
outside of the vacuum system and below the pendulum bobs damp the swinging
motion." Methods: four-wire suspension per bob; four 120 kg tungsten
(95.5 % W sintered alloy) source-mass stacks; finite-Q corrections "less than
about 1 part in 10⁶ … ignored".
**D1** SUS. **D2** OUT (explicit in Fig. 1 caption). **D3** 1: [vacuum
chamber wall; material not stated]. **D4** fibre (four wires per bob); wire
material not stated in the coded text; Q not stated. **D5** 4 provisional —
chamber shape not described anywhere in the arXiv text; laser light path
implies at least one window; flagged. Confident on D1–D3.

### NIST-26 — Schlamminger et al.
**Coded from:** the primary paper itself, Metrologia 63, 025012 (2026), open
access (IOP HTML full text + PDF-derived text). §2 apparatus (Fig. 3: four Cu
TMs on Al disk on carousel radius ≈120 mm; Cu-Be torsion strip from gimbal;
grounded vacuum can as electrostatic shield; eight Cu electrode rods inside;
four SMs outside the vacuum envelope on carousel, MCR ≈ 213.96 mm; Cu SMs
11 191.68 g; second SM set of single-crystal sapphire, 5 015.60 g, §4.4);
§4 modifications at NIST (same vacuum chamber as BIPM, different pumping
geometry; strip viewed edge-on); §5 dimensional metrology (CMM access
restricted by "the inner ledge of the vacuum chamber base" and the overhead
yoke); §7–8 pressure and stiffness (Q from free-decay envelopes vs pressure,
Fig. 20: Qmax = 2.4(4)×10⁵, pQ = 8.8(6)×10² Pa); §"torque derivation" notes
the optical window in the vacuum vessel for the autocollimator.
**D1** SUS. **D2** OUT. **D3** 1: [grounded vacuum can with optical window;
can material not stated]. **D4** strip, Cu-Be, Qmax = 2.4(4)×10⁵ (measured,
methods §8). **D5** 4. Confident — best-documented apparatus in the set.

---

## Summary of confidence

- **Coded with confidence:** NIST-82, UWash-00, BIPM-01, UZur-06, HUST-05,
  HUST-09, LENS-14, BIPM-14, HUST-A-18, JILA-18, NIST-26.
- **Coded with noted ambiguities/inference:** LANL-97 (enclosure by apparatus
  lineage), UWup-02 (D2 from design geometry + corroborating JILA analogy),
  MSL-03 (D2/D3/D5 rest partly on a search-level description of the 1994
  design paper), UCI-14 (D3 layer count of the cryostat, range 2–5),
  HUST-T-18 (coded from 2014 companion + 2020 review, shield inferred,
  D3 range 0–1), HUST-09 (D3 campaign-dependent 0/1 — coded minimum),
  LENS-14 (D3 radial order of shields vs masses).
- **Not adequately sourced:** TR&D-96 — D2, D3, D5 left UNSOURCED (D1, D4
  coded from the Rothleitner–Schlamminger review). No open apparatus text
  found; I did not guess.

## Q-value provenance caveat

Per code-book, Q belongs in D4 only where it appears in apparatus/method text
of the coded source. For NIST-82, UWash-00, BIPM-01/14, LANL-97, TR&D-96 and
UCI-14 the Q values come from the Rothleitner–Schlamminger review's Table I
(which *is* the coded source for those experiments, but is itself secondary).
HUST-09 (1.7×10³), HUST-T-18 (≈5×10⁴ coated) and NIST-26 (2.4(4)×10⁵) are
stated in method text of the coded sources. HUST-05's ≈3.6×10⁴ traces to the
CODATA-2014 re-evaluation as quoted in NSR 2020. MSL-03, UWup-02, JILA-18,
HUST-A-18, UZur-06, LENS-14: no Q stated / not applicable.

---

## Blinding incident log

Every incident below is a G value (or pattern claim) that entered my context
unavoidably via search-tool output, abstract lines caught by keyword grep, or
review-article tables. None was sought, none was recorded in the coded table,
and none changes any physical apparatus coding. Directions seen were
consistent with the training-data priors I declared in advance, with one
exception (#3), which was genuinely new information.

1. **CODATA 2022 recommended G value** — appeared in grep output while
   locating the gravitation section of arXiv:2409.03787 (lines listing the
   adjusted-constants tables). Consensus value only; already in training data.
2. **UWup-02 and MSL-03 input values** — two rows of CODATA Table XXX
   appeared in a grep match before I narrowed extraction to the bibliography
   region. Directions matched declared priors.
3. **NIST-26 value and its offset direction vs BIPM** — displayed in the
   web-search synthesis/highlights while locating the Metrologia 63, 025012
   paper (also in NIST/ScienceDaily press summaries in the same results).
   **This is the significant incident:** I had declared "no prior" for
   NIST-26, and the glimpse un-blinded me to its approximate value and its
   direction relative to BIPM. Logged; value not recorded; the apparatus
   coding for NIST-26 (D1–D5) consists of physical facts unaffected by it.
4. **UWup-02 thesis abstract value** — in search highlights when locating the
   Kleinevoß thesis.
5. **JILA-10 abstract value** — abstract line caught by keyword grep of
   arXiv:1008.3203 text.
6. **HUST-99/05/09 values, CODATA-2010, and relative statements (BIPM high,
   JILA low, UWash slightly above CODATA-2010)** — abstract/intro lines of
   PMC4173272 caught by keyword grep.
7. **Rose-1969 and UWash-00 values** — intro line of PMC4173271 caught by
   keyword grep.
8. **NSR 2020 results table and per-experiment values** (13 values incl. both
   HUST-18 results, BIPM-01/14 mode-by-mode values, JILA correction history)
   — the review's Table 3 and narrative lines surfaced in grep output. This
   was the largest single exposure; all directions matched declared priors.
9. **Gillies & Speake rsta.2014.0022** — its Table 1 pairs source-mass data
   with G values (several glimpsed), and the paper *claims a visual tendency
   for experiments with source masses ≳30 kg to read higher G* (their fit:
   R² = 0.169, i.e. weak). This is a residual-pattern claim in the published
   literature, glimpsed while sourcing apparatus facts. Explicitly logged:
   I have not used it, and my coding dimensions do not include source-mass
   size. It is not the corpus's hypothesis so far as I know (I still do not
   know what the corpus predicts).
10. **Misc. search-result tables** — a book-scan table with 1996–2006 values
    (TR&D-96, LANL-97, UWash-00, BIPM-01, UWup-02, MSL-03, HUST-05, UZur-06),
    earlier MSL 1995/1999 values, NIST-82 value (twice, incl. PRL abstract
    which also gave "two 10.5-kg tungsten balls" — an apparatus fact I later
    confirmed in NBS-617), LANL-97 value, and qualitative direction statements
    (PTB +0.6 %, Wuppertal low, MSL low) in a Science news piece.
11. **Numerological "theoretical G" claims** — an academia.edu aggregation
    page served unrelated crank abstracts deriving G from Planck-mass
    numerology. Not sought (rule 3 was not violated by the search terms),
    not read further, not used; logged for completeness.
12. **HUST-09 value** — abstract of the Tu et al. 2010 scrape.
13. **Historical 19th-century G values** — a history table inside the
    Kleinevoß thesis scrape (Cavendish-era to Heyl; no modern values).
14. **NIST-26 §10 diagnostic** — while extracting the Q value from the PDF
    text, a long discussion-section paragraph rendered as one line, exposing
    method-level diagnostics (e.g. the BIPM servo-vs-Cavendish internal
    difference and Q range 1–3×10⁵). Treated as method text for the Q; the
    internal-difference figure was not recorded in the table.

**Abstract-reading admission:** although I never navigated to results
sections, keyword grep on full-text files repeatedly returned abstract lines
(incidents #5, #6, #7, #12). In each case I stopped reading the abstract at
the matched line and coded only from apparatus text. Short of pre-stripping
abstracts from every file (which I adopted partway through by reading
line-ranges instead of whole-file greps), these were not fully avoidable.

## Files written

1. `DECLARED_PRIORS_CODER.md` (before any paper was opened)
2. `CODED_TABLE.csv` (17 rows, header per code-book)
3. `CODING_NOTES.md` (this file)

No git commands were run. No other repository file was read besides
`CODEBOOK.md`.
