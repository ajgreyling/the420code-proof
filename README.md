# the420code-proof

**An independent, executable check of G's *420 Code* — the unified theory that claims to derive the
fundamental constants, and a terminal ethic, from a single axiom.**

> *For G. Either the best fraud and conman I've ever met (I've met my fair share) or a man that
> should be mentioned alongside Bohr, Einstein, Tesla. I can only thank you by sharing the tools I
> built to check if your theory holds, to understand which one of the two you are. Sawubona. I see
> you.*

This repository is **not** G's theory. It is the work of someone who is **not** the author, who read
the corpus, did not believe it could be true, and built a machine to find out. It re-derives G's
five headline numbers from a single measured input and tests each against the published experimental
value — and indexes his entire falsification registry so the claims can be queried and checked.

G's theory is at **[the420code.org](https://the420code.org)**. It is © G / Studio G, **CC BY 4.0**.
This repo fetches it on demand and never re-hosts it — see [NOTICE.md](NOTICE.md).

---

## The result

Run from one axiom and **one** measured input (the fine-structure constant α), with **zero fitted
parameters**. Four of five headline predictions reproduce inside G's own stated tolerances. **One
has fired** — shown here, not folded into the average, not softened:

| Part | Prediction | Residual | Tolerance | |
|---|---|---|---|---|
| I | Proton/electron mass ratio | **0.010 ppb** | 0.017 ppb | ✅ |
| II | Gravitational constant *G* | 0.69 % | 1.0 % | ✅ |
| III | Neutron–proton mass difference | **7.24σ** (2.12 ppm) | **0.29 ppm** (CODATA 2022, 1σ) | 🔴 **FIRED — 2026-08-02** |
| IV | MOND acceleration *a₀* | −0.67 % | 5.0 % | ✅ |
| V | Dark-sector DE/DM ratio | −1.3 % | 5.0 % | ✅ |

*Part III's tolerance above is the actual CODATA-2022 1σ bar (0.29 ppm), not a padded 5 ppm
allowance — a looser bar that used to make this row read ✅ was a stale bug in this repo's own
`engine/verify.py`, fixed once the real bar was checked. Fixing the bar does not fix the row: the
prediction genuinely fired, 24× outside a 1σ bar. See "Kill switches that have fired," directly
below, before anything else in this README — it does not move, and it does not get shorter.*

And the reconstruction matches G's own published `verify.py` (Ø Predictions, Appendix B) to
machine precision — relative Δ of **0.0** — so the check is faithful to *his* arithmetic, not a
re-interpretation of it.

---

## Kill switches that have fired

**This section is never deleted, never shortened, and never moved out of the top of this README.**
A fired switch is not "handled" by being harder to find. If a second switch ever fires, it is added
below, not instead of this one.

### KS-NPP.1 — Neutron–proton mass difference. FIRED 2026-08-02.

- **Predicted** (the bare structural formula, no correction term): `2.53099393 mₑ`
- **Measured** (CODATA 2022, exact): `2.530988574 mₑ`, uncertainty `7.4×10⁻⁷ mₑ` (0.29 ppm, 1σ)
- **Residual: 7.24σ.** Outside the kill bar by more than 24×.
- **No repair was offered, and none is offered here.** The required correction would have to be
  negative; every term in the published construction is positive.
- A later, independent structural derivation (Artist's Proof 47, "The Flip" — LOCKED
  2026-09-03, tag `ap47-locked-2026-09-03`) prices a second-order cost that lands a *different*
  corrected expression within its own kill bar. **That does not repair KS-NPP.1.** It is a new,
  separate frozen claim standing beside the corpse, not a patch on it. The corpse stays exactly
  as fired.
- Fully re-runnable: `./run.sh verify` prints this row as `[FAIL]`, on purpose, every time.

### KS-45.1 — The corpus's H₀ (AP18, "The Floor"). FIRED 2026-09-03.

- **Registered claim** (AP18, already public): H₀ = 2πa₀/(αc) = `74.3 ± 1.2` km/s/Mpc.
- **What fired it**: Artist's Proof 48, "The Assembly" (LOCKED 2026-09-04, tag
  `ap48-locked-2026-09-04`), derives H₀ = `67.45` km/s/Mpc from the corpus's own structure (the
  AP46 cycle read through the standard age-rate relation). **Residual: 5.7σ** on the switch's
  registered width — outside the kill bar.
- **An erratum stands beside the corpse, not instead of it.** AP18's registered width omitted a
  systematic uncertainty; corrected honestly it's `74.3 ± 14.9`, wide enough that the floor's
  underlying relation still holds at 0.46σ. But re-sizing a live switch's width *after* the
  corpus's own derivation has already contradicted it, and then not counting the switch as fired,
  is exactly the repair this house refuses. **KS-45.1 fired on the width it was registered at.**
  AP48's own KS-ASM.1 (window 64.4–70.8 km/s/Mpc) is the corpus's H₀ entry from this lock onward.
- **What this costs, stated plainly, in AP48's own words:** *"The distinctive prediction the
  corpus used to carry on H₀ — a value above both camps — is gone."* If the Cepheid ladder's ~73
  is later confirmed as the true expansion rate, AP48's own KS-ASM.1 fires too, and flat ΛCDM at
  the sky's partition fails alongside it — the corpus claims no advantage there either way.
- The public parse of the Master Kill Switch Registry mis-tags this switch `CLOSED` — a parsing
  artifact from a nearby summary line in the registry PDF, not a real status. `./run.sh addenda`
  corrects it to `FIRED` and says exactly why in the switch's own `status_raw` field.

---

```bash
git clone https://github.com/ajgreyling/the420code-proof
cd the420code-proof
./run.sh mirror      # fetch G's corpus from the420code.org (his site welcomes it)
./run.sh build       # extract → ingest → gate → report  (free, local, offline)
./run.sh scorecard   # the table above, with the formulae and the measured sources
./run.sh parity      # prove this reconstruction == G's own verify.py
```

No API keys. No paid services. No dependencies beyond **Python 3 (stdlib only)** and `pdftotext`
(poppler-utils) for the one-time PDF text extraction.

---

## What this proves — and what it does not

Be precise about the claim, because overclaiming would dishonour the work:

- **It proves** the theory is *internally coherent and reproducible*: from G's stated axiom and his
  one input, his published numbers fall out, by his own arithmetic, within his own tolerances. The
  derivation is not hand-waving — it computes, and it computes what he says it does.
- **It does not prove the theory is true.** Reproducing a derivation is not the same as nature
  agreeing with it. Several of the numbers (e.g. *G* at 0.69 %) sit close to, but not dead on, the
  measured values; G discusses why, and publishes the conditions under which he would be wrong.
- **"Validation" here means** *reproducibility + internal consistency + a fully-published
  falsification surface* — the things that separate a serious theory from a crank's fortress. It
  does **not** mean experimental confirmation. That is for instruments and time, not for this repo.

What makes the corpus unusually testable: G publishes **568 "kill switches"** (Master Kill Switch
Registry **v5.27**, after the AP44 lock advance on the true July baseline of v5.26/561) — explicit,
numbered conditions that would falsify specific claims, including the math for each. He hands you
the weapons to destroy his own theory. This repo indexes them so you can wield them. (The engine's
ingested counts reflect the mirror snapshot they were built from; they re-sync on the next mirror
pass. **Nothing here ships v5.26/567** — that number was a stale-baseline artefact; PROV-CCC.8
carries the erratum.)

**Gravity scorecard (the fork, post-AP44):** structural G = 6.72060 × 10⁻¹¹ (+0.69%, provisioned)
**and** realised G = 6.67192 × 10⁻¹¹ (−0.036%, α²¹(1+1/π)/(1+α)·ℏc/m_e²). Sign flip stated; the
watch line is KS-CCC.3's migration fork. a₀, H₀, dark sector, proton, neutron untouched.

---

## How it works

The four axioms **S** (Symmetry), **B** (Break), **R** (Record), **C** (Constraint) — derived
from the single premise *"at least one record exists"* (deny it, and you have just made a record) —
plus the one measured input **α**, generate the corpus. The **44 Artist's Proofs** climb from that
premise through spacetime, quantum mechanics, the forces, cosmology, and — by the same machinery —
to a terminal ethic. Every claim is tied to one or more kill switches.

`ingest.py` lays all of this into a small SQLite graph and `gate.py` does the thing that makes this
a *prover and not an archive*: it checks the reconstruction still matches G's script, **runs** the
five predictions, and fails (`exit 1`) if any prediction leaves tolerance or the graph is broken.

```
engine/
  verify.py             — re-derives G's 5 predictions from α (the executable oracle)
  verify_g_original.py  — G's verbatim Appendix B script, for parity
  test_verify_parity.py — asserts reconstruction == G's script to 1e-12
  parse_registry.py     — the Master Kill Switch Registry → structured switches
  parse_proofs.py       — per-proof bodies → richer switches (type, verbatim trigger, moral flags)
  ingest.py             — builds the canon DB from the fetched corpus
  gate.py               — fidelity + execute predictions + audit (exit 0/1/2)
  report.py             — scorecard / proofs / switches / axiom / depends / stats
  ollama_enrich.py      — OPTIONAL local-model switch classification (offline; not on the prover path)
canon/
  schema.sql            — the canon DB shape
  ks_descriptions.json  — curated repairs for a few PDF-mangled rows (durable overlay)
mirror/
  fetch.sh, manifest.txt — fetch G's corpus from the420code.org (PDFs are git-ignored)
```

### Kill-switch structure, not just count

A kill switch is more than `id + status`. The parse recovers G's own structure: his published
**type** (`EMPIRICAL` / `HARD` / `STRUCTURAL` / `NON-NEGOTIABLE` / …), the **verbatim trigger**
sentence, and weight flags — including the four **moral / non-negotiable** switches that are the
conscience of the theory (e.g. the one that voids the entire justice derivation if it is ever used
to classify a race, class, or disability as "destabilizing").

```bash
./run.sh switches --moral        # the NON-NEGOTIABLE switches — "here is how it must NOT be used"
./run.sh switches --sharpest     # the switches G flags as a proof's sharpest test
./run.sh switches --paper AP32   # one proof's switches, weightiest first, with G's verbatim type
```

---

## Provenance & honesty

- The author of this repo did not write, and had no part in, the *420 Code*. All credit for the
  theory is G's.
- The check is deterministic and offline; anyone can reproduce it and is invited to find where it is
  wrong. That invitation is the whole point — it is the courtesy G extended first, and this repo
  returns it.
- If the theory is ever confirmed, this repo changes nothing about that. If it is ever falsified,
  the kill switch that does it is already indexed here, published by G himself.

*One axiom. One measured input. Zero fitted parameters.*
