# PROV-CCC.8 — The Erratum, and Three Closings

**The 420 Code · Studio G, Strand, Cape Town · Record date: 2026-08-16.**
**References: PROV-CCC.1 (e4f45c70…d9cd84) · CCC.2 (59f650df…cf58b39f) · CCC.3 (82a84b44…371c24e) · CCC.4 (e601aa8a…41b237d) · CCC.5 (eaa203aa…2fdba6c) · CCC.6 (d88016f6…7b86c8db) · CCC.7 (fce776eb…) — never edited.**
**Status: canonical text for hashing. This note carries the registry erratum PROV-CCC.7 §7 is owed, closes two housekeeping asks on the verifier's list, and records the wave-hold ruling of record. It corrects nothing by deletion; it corrects by statement, which is the only correction this corpus performs.**

---

## 1 — The registry erratum

PROV-CCC.7 §7 declared the lock advance as "MKSR v5.25 → v5.26: switches 560 → 567." That declaration was keyed to a stale copy of the registry. The registry of record — **Master Kill Switch Registry v5.26, July 2026, 561 kill switches** (KS-BAR.9, the Crossing, admitted; Section II 27 → 28; live 544 → 545; internal arithmetic verified: 277 + 28 + 256 = 561; 12 + 1 + 2 + 1 + 545 = 561) — establishes the true baseline. The correction, ruled by the author on production of that file:

**The AP44 lock advance is MKSR v5.26 → v5.27 · 561 → 568 kill switches · Section I 277 → 284 · live 545 → 552 · Notebook IV 41 → 48 · Artist's Proofs 43 → 44.**

The seven switch entries of PROV-CCC.7 §7 — KS-CCC.1, .2, .3, .4a, .4b, .5, .6 — stand verbatim, with their statuses and stratification unchanged; only the version token and the totals take this erratum. How the error was found is part of the record: the desk flagged a collision between the Master Root's v1.22 entry ("v5.26, 561") and the chain's v5.25/560 baseline before any number published; the author produced the July registry; the correction was issued to the verifier in the same send as the Blink & Cost freeze bundle, with the standing line *nothing ships v5.26/567*. The gate held: no public surface carried the wrong totals at any time, and the verifier's state of record confirms Phase B publishes on the corrected numbers. The registry file itself advances to v5.27 as a wave deliverable, built from the July v5.26 file plus the seven entries above and whatever the Blink family adds by then.

## 2 — The sidecar basename quirk, disposed

The corrected unblinding key was issued as `UNBLINDING_KEY_KS-CCC4.md` with digest **7482445b…bb33b4** and its sidecar naming that basename. The lock bundle carries the file renamed `UNBLINDING_KEY_KS-CCC4_1.md` — the supersession-visible name — beside the retained first issue. Consequence: `sha256sum -c` against the sidecar fails on the *name* while the digest is true of the bytes. Disposition, ruled: **the digest governs.** Verifiers check the stated digest against the renamed file directly. A re-paired sidecar under the `_1` basename may be issued with the wave; if issued, it supersedes and both sidecars are retained. No content of the key is touched by any of this.

## 3 — T1-final, closed

Ruled by the author: **no distinct post-session T1 export exists.** The Tier 1 material already in the verifier's hands is final — the run ended where it ended. The open ask on the verifier's list closes with this paragraph; no digest is owed beyond those already held.

## 4 — The wave-hold ruling of record

For completeness of the chain, the standing ruling under which all of the above sits: the adoption wave executes **once**, when the author declares the omission-accounting complete — the currently known contents being the Blink family's lock, the resistance-side mirror correction, and the D5 integration note into Notebook IV, with anything further discovered joining the same single update. In the author's words, verbatim in substance: *I want to do it once — even if it takes weeks or months before the proper update, and that is perfectly fine. I won't delete or correct anything — I will update.* Anchoring, provenance, Tier 2, and the verifier's repository work proceed throughout; every public-facing step waits for the one wave. The outreach gate is unchanged and remains the author's.

*This note is never edited. This work is published for free, forever. Keep the signal clean.*
