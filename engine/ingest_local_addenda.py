#!/usr/bin/env python3
"""Local addenda to the canon: switches and status changes not yet on the420code.org.

The public mirror (`./run.sh mirror`) only pulls what's actually published at
the420code.org. AP44-47 are locked/anchored on THIS repo (private, verifier-side)
but their public wave is explicitly deferred until after AP48 -- so the public
Master Kill Switch Registry PDF still reads v5.26 (July 2026) and knows nothing
about them. `engine.ingest.build()` alone therefore under-counts the corpus's
actual current state.

This module patches the freshly-built canon DB with exactly the switches and
status changes that ARE anchored on this repo (not merely delivered/pending):

  * KS-NPP.1: LIVE -> FIRED. Empirical fact, independent of any paper's lock
    status -- the neutron-proton mass-difference prediction departed the
    measured value by 7.24 sigma on 2026-08-02. Documented in AP45 FINAL v1.7
    section 10 ("the first death") and AP47 section 7 ("the deaths, shown").
    Still not repaired by either -- both explicitly refuse to repair it.
  * AP45 (The Blink, FINAL v1.7) and AP46 (The Stretch, FINAL v1.5): four new
    kill switches each, sourced verbatim from FREEZE_REGISTER_AP45_AP46_2026-09-02.md
    section headers, anchored on this repo at tag ap45-ap46-locked-2026-09-02.
  * AP47 (The Flip, FINAL v3): four new kill switches (KS-FLIP.1-4), sourced
    verbatim from AP47_The_Flip_FINAL_v3.md section 10, anchored on this repo
    at tag ap47-locked-2026-09-03 -- LOCKED at the author's own direct
    confirmation, not merely Studio G's attestation (see
    provenance/RECEIPT_2026-09-03_AP47_lock_attestation.md for why that
    distinction mattered here).

Historical note: KS-FLIP.1-4 were deliberately withheld from this module for
two days while AP47 sat at "pending lock" (freeze-anchored, receipted, but not
authorized) -- added only once the lock was actually confirmed by the author
directly, not by a delivered document asserting it on his behalf. That's the
same discipline this module applies to AP45/AP46 and to the KS-NPP.1 status
change: only what's actually anchored, never what's merely claimed.

Run after `engine.ingest.build()` (or via `./run.sh addenda`, which does both):

    python3 -m engine.ingest_local_addenda
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "canon" / "420code.db"

# (id, description, fire_condition, status, status_raw, kind_token, test_kind, origin, section)
_NEW_SWITCHES = [
    (
        "KS-BLINK.1", "The balanced break",
        "Fires if D-CCC.1's algebra permits balanced breaks; recovery: Theorem 1's existence clause falls.",
        "LIVE", "LIVE — STRUCTURAL", "STRUCTURAL", "structural", "AP45", "physics",
    ),
    (
        "KS-BLINK.2", "The Born identification",
        "Nature-facing by inheritance of AP25's KS-56 and AP01's KS-V.3 (one test, two entries); "
        "recovery: the identification retires, the toll stands unpriced.",
        "LIVE", "LIVE — STRUCTURAL", "STRUCTURAL", "structural", "AP45", "physics",
    ),
    (
        "KS-BLINK.3", "The dimension label",
        "Methodological; binds the claim, not a person.",
        "LIVE", "LIVE — METHODOLOGICAL", "METHODOLOGICAL", "structural", "AP45", "physics",
    ),
    (
        "KS-BLINK.4", "The grain count",
        "Fires if the formalism forces per-alternative pricing.",
        "LIVE", "LIVE — STRUCTURAL", "STRUCTURAL", "structural", "AP45", "physics",
    ),
    (
        "KS-STRETCH.1", "The clock joint",
        "Fires with AP42's KS-42.3/KS-42.6.",
        "LIVE", "LIVE", None, "structural", "AP46", "physics",
    ),
    (
        "KS-STRETCH.2", "The stance",
        "Empirical on its wrong-way edge with KS-42.4: fires if w evolves increasingly phantom at "
        "late times. Structural on its drift clause.",
        "LIVE", "LIVE — EMPIRICAL / STRUCTURAL", "EMPIRICAL", "empirical", "AP46", "physics",
    ),
    (
        "KS-STRETCH.3", "The age chain",
        "Fires if the age, as the data settle it, differs from one cycle by more than one lane-time "
        "(0.66 Gyr) either way. An early-dark-energy age near 12.9 Gyr fires it; the corpus's own H0 "
        "under the standard expansion history fires it. D-STRETCH.1 (AP48) is load-bearing here.",
        "LIVE", "LIVE — STRUCTURAL / EMPIRICAL", "STRUCTURAL / EMPIRICAL", "empirical", "AP46", "physics",
    ),
    (
        "KS-STRETCH.4", "The era surface",
        "Registered for AP48: the storm's tail must reproduce a proportional-to-t^(1/2) era, a "
        "proportional-to-t^(2/3) era, the transition, BBN, and the relic glow, or AP48 dies and "
        "AP46's standing stays docked.",
        "REGISTERED", "REGISTERED — for AP48", None, "structural", "AP46", "physics",
    ),
    (
        "KS-FLIP.1", "The frozen row",
        "Dies if an improved measurement of the neutron-proton mass difference departs from "
        "Delta_real = Delta_bare/(1+alpha^2/8pi) (displayed 2.53098857035) beyond the audited 1-sigma "
        "bar: 7.4e-7 m_e (0.29 ppm), CODATA 2022. Nature-facing, live from this lock.",
        "LIVE", "ARMED", "STRUCTURAL", "empirical", "AP47", "physics",
    ),
    (
        "KS-FLIP.2", "Forced structure",
        "Binding on author and desks. Fires if any element of the construction -- the order, the "
        "divisor, the scope, the form, the process claim -- is ever shown to have been selected by "
        "comparison with measurement rather than by the stated structural argument.",
        "LIVE", "ARMED — binding on author and desks", "METHODOLOGICAL", "structural", "AP47", "physics",
    ),
    (
        "KS-FLIP.3", "The truncation",
        "The construction terminates at second order: no alpha^3 term exists. The absent "
        "third-order piece sits at 3.9e-8 (5.3% of the audited bar, 0.020 eV) -- adjudication waits "
        "on roughly twentyfold better metrology on the deuteron binding energy.",
        "LIVE", "ARMED", "STRUCTURAL", "structural", "AP47", "physics",
    ),
    (
        "KS-FLIP.4", "The scope",
        "Formal domain: the cost operator's domain is the set of configurations holding a non-zero "
        "second-scale epsilon (an orientation differing from its ground state under the same grip); "
        "ground states are outside the domain by construction. Dies if a ground state is ever shown "
        "to require the cost, or a configuration inside the domain shown to escape it.",
        "LIVE", "ARMED", "STRUCTURAL", "structural", "AP47", "physics",
    ),
]

_SOURCE_NOTE_45_46 = (
    "Sourced from FREEZE_REGISTER_AP45_AP46_2026-09-02.md, anchored on this repo at tag "
    "ap45-ap46-locked-2026-09-02. Not yet on the public the420code.org mirror (wave deferred "
    "until after AP48)."
)
_SOURCE_NOTE_47 = (
    "Sourced from AP47_The_Flip_FINAL_v3.md section 10, anchored on this repo at tag "
    "ap47-locked-2026-09-03. Not yet on the public the420code.org mirror (wave deferred "
    "until after AP48)."
)
_SOURCE_NOTES = {"AP45": _SOURCE_NOTE_45_46, "AP46": _SOURCE_NOTE_45_46, "AP47": _SOURCE_NOTE_47}


_NEW_PROOFS = [
    # (id, kind, title, domain, pdf)
    ("AP45", "artist_proof", "The Blink",
     "physics", "freeze-2026-09-02-ap45-ap46/AP45_The_Blink_FINAL_v1_7.md"),
    ("AP46", "artist_proof", "The Stretch",
     "physics", "freeze-2026-09-02-ap45-ap46/AP46_The_Stretch_FINAL_v1_5.md"),
    ("AP47", "artist_proof", "The Flip",
     "physics", "freeze-2026-09-01-ap47/AP47_The_Flip_FINAL_v3.md"),
]


def apply(conn: sqlite3.Connection) -> dict:
    report = {"npp_fired": False, "inserted": [], "already_present": [], "proofs_inserted": []}

    for ap_id, kind, title, domain, pdf in _NEW_PROOFS:
        existing = conn.execute("SELECT id FROM proof WHERE id=?", (ap_id,)).fetchone()
        if existing:
            continue
        conn.execute(
            "INSERT INTO proof(id,kind,title,domain,pdf,ks_count) VALUES(?,?,?,?,?,0)",
            (ap_id, kind, title, domain, pdf),
        )
        report["proofs_inserted"].append(ap_id)

    # KS-NPP.1: LIVE -> FIRED.
    row = conn.execute("SELECT status FROM kill_switch WHERE id='KS-NPP.1'").fetchone()
    if row is not None:
        conn.execute(
            "UPDATE kill_switch SET status='FIRED', status_raw=? WHERE id='KS-NPP.1'",
            ("FIRED — 7.24σ, 2026-08-02 (neutron-proton mass difference; AP45 §10 "
             "'the first death'; AP47 §7 'the deaths, shown'; not repaired by either)",),
        )
        report["npp_fired"] = True

    for sw_id, desc, fire_cond, status, status_raw, kind_token, test_kind, origin, section in _NEW_SWITCHES:
        existing = conn.execute("SELECT id FROM kill_switch WHERE id=?", (sw_id,)).fetchone()
        if existing:
            report["already_present"].append(sw_id)
            continue
        full_desc = f"{desc} [local addendum -- {_SOURCE_NOTES[origin]}]"
        conn.execute(
            "INSERT INTO kill_switch(id,description,fire_condition,status,status_raw,"
            "kind_token,test_kind,origin,section,non_negotiable,sharpest,global) "
            "VALUES(?,?,?,?,?,?,?,?,?,0,0,0)",
            (sw_id, full_desc, fire_cond, status, status_raw, kind_token, test_kind, origin, section),
        )
        conn.execute(
            "INSERT OR IGNORE INTO edge(src,dst,rel) VALUES(?,?, 'falsified_by')", (origin, sw_id)
        )
        report["inserted"].append(sw_id)

    for ap in ("AP45", "AP46", "AP47"):
        n = conn.execute(
            "SELECT count(*) FROM edge WHERE src=? AND rel='falsified_by'", (ap,)
        ).fetchone()[0]
        conn.execute("UPDATE proof SET ks_count=? WHERE id=?", (n, ap))

    conn.commit()
    return report


def main() -> int:
    if not DB.exists():
        print(f"[addenda] {DB} not found -- run './run.sh ingest' first")
        return 1
    conn = sqlite3.connect(DB)
    report = apply(conn)
    n_total = conn.execute("SELECT count(*) FROM kill_switch").fetchone()[0]
    conn.close()
    print(f"[addenda] KS-NPP.1 -> FIRED: {report['npp_fired']}")
    print(f"[addenda] inserted: {', '.join(report['inserted']) or '(none)'}")
    if report["already_present"]:
        print(f"[addenda] already present, skipped: {', '.join(report['already_present'])}")
    print(f"[addenda] kill_switches now = {n_total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
