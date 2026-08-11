#!/usr/bin/env python3
"""Ingest the mirrored 420 Code into the canon SQLite DB.

Rebuilds canon/420code.db from the mirror, deterministically and for free:
  * axioms S/B/R/C (from llms.txt)            → axiom
  * 42 Artist's Proofs + companion prose      → proof  (8-part structure from llms.txt)
  * 5 executable predictions                  → prediction  (from engine.verify — the oracle)
  * 515 kill switches                         → kill_switch  (from engine.parse_registry)
  * provenance / declared corpus counts       → corpus_fact
  * dependency edges (proof→axiom, pred→proof, ks→proof, proof→part) → edge

This is the analogue of storygraph's ingest_* + build_graph: the canon is the queryable
graph the gate re-ingests and audits. Run:  python3 -m engine.ingest
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

from . import parse_proofs, parse_registry, verify

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "canon" / "420code.db"
SCHEMA = ROOT / "canon" / "schema.sql"
TXT = ROOT / "extract" / "txt"

# The four founding axioms (verbatim from llms.txt).
AXIOMS = [
    ("S", "Selection", "A record must be distinguishable from no record"),
    ("B", "Break/Symmetry Breaking", "Recording requires irreversibility"),
    ("R", "Accumulation", "Records accumulate forward (time's arrow)"),
    ("C", "Coupling", "No record is fully isolated; every record is coupled to at least one other"),
]

# The 8-part structure and AP titles (from llms.txt + the PDF cover pages).
PARTS = {
    "I":    ("The Premise", "Axioms, foundations, logical proof", ["AP40", "AP01", "AP20"]),
    "II":   ("Spacetime", "Relativity, dimensions, field equations", ["AP03", "AP05", "AP10", "AP08"]),
    "III":  ("Quantum Mechanics", "Quantization, spin, uncertainty, decoherence",
             ["AP04", "AP11", "AP12", "AP13", "AP09"]),
    "IV":   ("Forces & Particles", "Gauge symmetry, Standard Model, corrections",
             ["AP06", "AP15", "AP16", "AP14", "AP02"]),
    "V":    ("Cosmology", "Measurement, dark sector, MOND, gravity",
             ["AP07", "AP17", "AP18", "AP19", "AP28"]),
    "VI":   ("Consciousness & Agency", "Observer, mass ratios, alignment, ethics",
             ["AP29", "AP30", "AP31", "AP32", "AP33"]),
    "VII":  ("Applications", "Inversion, economics, information, boundaries",
             ["AP34", "AP35", "AP36", "AP37", "AP38"]),
    "VIII": ("Closure", "Scaffold, loop, clock, completeness",
             ["AP39", "AP41", "AP42", "AP21", "AP22", "AP23", "AP24", "AP25", "AP26", "AP27"]),
}

# AP id → human title, recovered from each PDF's cover (basename after the number).
AP_TITLES = {
    "AP01": "The Actualization State", "AP02": "The Operator", "AP03": "The Ratio",
    "AP04": "The Loop Hypothesis", "AP05": "The Break", "AP06": "The Leakage Constant",
    "AP07": "The Record Measure", "AP08": "The Identity", "AP09": "The Break (Empty Set)",
    "AP10": "The Dimension", "AP11": "The Spin", "AP12": "The Limit", "AP13": "The Grain",
    "AP14": "The Correction", "AP15": "The Connection", "AP16": "The Break (Electroweak)",
    "AP17": "The Room", "AP18": "The Floor", "AP19": "The Direction", "AP20": "The Proof",
    "AP21": "The Web", "AP22": "The Ledger", "AP23": "The Single Record", "AP24": "The Residual",
    "AP25": "The Measure", "AP26": "The Surplus", "AP27": "The Harmonics", "AP28": "The Constant",
    "AP29": "The Actualization Proof", "AP30": "The Resistance", "AP31": "The Alignment",
    "AP32": "The Correction (Ethics)", "AP33": "The Boundary", "AP34": "The Inversion",
    "AP35": "The Ledger (Economics)", "AP36": "The Feed", "AP37": "The First Boundary",
    "AP38": "The Exit", "AP39": "The Scaffold", "AP40": "The Irrational", "AP41": "The Loop",
    "AP42": "The Clock",
}

# Declared corpus facts (from the registry header + llms.txt + provenance findings).
CORPUS_FACTS = {
    "author": "G (Studio G, Strand, Cape Town)",
    "doi": "10.5281/zenodo.19208226",
    "license": "CC BY 4.0 (Copyleft)",
    "url": "https://the420code.org",
    "measured_input": "alpha (fine-structure constant) ~ 1/137",
    "free_parameters": "0",
    "ks_declared_total": "568",
    "ks_declared_physics": "284",
    "ks_declared_philosophy": "28",
    "ks_declared_oh_models": "256",
    "ks_declared_closed": "12",
    "ks_declared_live": "552",
    "ks_declared_non_negotiable": "6",
    "ap_published": "44 (AP01-AP44); AP44 The Snap LOCKED 2026-08-11",
    "registry_version_note": "MKSR v5.27 after AP44 lock on true July baseline v5.26/561; nothing ships v5.26/567 (PROV-CCC.8 erratum)",
}


def _part_for(ap: str) -> tuple[str | None, str | None, str | None]:
    for no, (title, domain, members) in PARTS.items():
        if ap in members:
            return no, title, domain
    return None, None, None


def _words(pdf_base: str) -> int | None:
    f = TXT / f"{pdf_base}.txt"
    return len(f.read_text(encoding="utf-8").split()) if f.exists() else None


def build(reset: bool = True) -> sqlite3.Connection:
    if reset and DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA.read_text(encoding="utf-8"))

    # --- axioms ---
    for sym, name, stmt in AXIOMS:
        conn.execute("INSERT INTO axiom(id,symbol,name,statement,family) VALUES(?,?,?,?, 'core')",
                     (sym, sym, name, stmt))

    # --- proofs (42 APs) ---
    for ap, title in AP_TITLES.items():
        no, ptitle, domain = _part_for(ap)
        pdf = next((p.name for p in (ROOT / "mirror" / "pdf").glob(f"{ap}_*.pdf")), f"{ap}.pdf")
        base = pdf[:-4]
        conn.execute(
            "INSERT INTO proof(id,kind,title,part_no,part_title,domain,pdf,words) "
            "VALUES(?,?,?,?,?,?,?,?)",
            (ap, "proof", title, no, ptitle, domain, pdf, _words(base)))
        if no:
            conn.execute("INSERT OR IGNORE INTO edge(src,dst,rel) VALUES(?,?, 'in_part')", (ap, no))

    # --- companion prose volumes ---
    for pdf in sorted((ROOT / "mirror" / "pdf").glob("*.pdf")):
        if pdf.name.startswith("AP"):
            continue
        pid = f"PROSE:{pdf.stem}"
        conn.execute("INSERT INTO proof(id,kind,title,pdf,words) VALUES(?,?,?,?,?)",
                     (pid, "prose", pdf.stem.replace("_", " "), pdf.name, _words(pdf.stem)))

    # --- predictions (the executable oracle) ---
    for p in verify.compute():
        conn.execute(
            "INSERT INTO prediction(key,part,name,formula,predicted,measured,unit,residual,"
            "residual_unit,tolerance,measured_source,passed) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (p.key, p.part, p.name, p.formula, p.predicted, p.measured, p.unit, p.residual,
             p.residual_unit, p.tolerance, p.measured_source, int(p.passed)))

    # prediction → originating AP (from Ø Predictions' own attribution)
    pred_origin = {
        "proton_electron_mass_ratio": "AP30", "gravitational_constant": "AP28",
        "gravitational_constant_realised": "AP44",

        "neutron_proton_mass_diff": "AP30", "mond_acceleration_a0": "AP18",
        "dark_sector_de_dm_ratio": "AP42",
    }
    for k, ap in pred_origin.items():
        conn.execute("INSERT OR IGNORE INTO edge(src,dst,rel) VALUES(?,?, 'predicts')", (ap, k))

    # --- kill switches ---
    ks_rows = parse_registry.parse()
    # Fold in the checked-in description overlay (the metered repair pass output), so the few
    # PDF-mangled descriptions stay clean across this reset=True rebuild — for free.
    overlay_path = ROOT / "canon" / "ks_descriptions.json"
    if overlay_path.exists():
        import json as _json
        overlay = _json.loads(overlay_path.read_text(encoding="utf-8"))
        for r in ks_rows:
            if r["id"] in overlay:
                r["description"] = overlay[r["id"]]
    # Merge: registry is authoritative for STATUS + the Ø Models families; the per-proof bodies
    # (parse_proofs) supply RICHER descriptions and catch switches the summary table omits.
    by_id: dict[str, dict] = {r["id"]: r for r in ks_rows}
    proof_rows, deps, axioms_used = parse_proofs.parse_all()
    for pr in proof_rows:
        existing = by_id.get(pr["id"])
        if not existing:
            by_id[pr["id"]] = pr  # a switch the registry summary missed
            continue
        # Description precedence: the per-proof body is the authoritative, un-bled source. When it
        # parsed a real fire-condition, its description WINS over the registry's — even if shorter —
        # because the registry summary table suffers PDF column-bleed on some rows (e.g. KS-32.4
        # bleeds "debt). in The Interior …"). Absent a clean body condition, keep the longer string.
        if pr.get("fire_condition"):
            existing["description"] = pr["description"]
        elif len(pr["description"]) > len(existing["description"] or ""):
            existing["description"] = pr["description"]
        if not existing.get("origin") and pr.get("origin"):
            existing["origin"] = pr["origin"]
        if existing["global"] == 0 and pr.get("global"):
            existing["global"] = 1
        # The per-proof body is the authoritative source for G's switch STRUCTURE: the published
        # TYPE token, the verbatim fire-condition, and the moral/sharpest flags. The terse registry
        # table carries none of these, so the proof parse always supplies them.
        if pr.get("kind_token"):
            existing["kind_token"] = pr["kind_token"]
            existing["test_kind"] = pr.get("test_kind")
            # promote the richer typed status_raw (e.g. 'LIVE — NON-NEGOTIABLE') over the bare one
            if pr.get("status_raw") and "—" in pr["status_raw"]:
                existing["status_raw"] = pr["status_raw"]
        if pr.get("fire_condition") and len(pr["fire_condition"]) > len(existing.get("fire_condition") or ""):
            existing["fire_condition"] = pr["fire_condition"]
        if pr.get("non_negotiable"):
            existing["non_negotiable"] = 1
        if pr.get("sharpest"):
            existing["sharpest"] = 1
    # re-apply the overlay last so manual repairs always win.
    if overlay_path.exists():
        for kid, desc in overlay.items():
            if kid in by_id:
                by_id[kid]["description"] = desc

    ap_ks_count: dict[str, int] = {}
    for r in by_id.values():
        conn.execute(
            "INSERT OR REPLACE INTO kill_switch(id,description,fire_condition,status,status_raw,"
            "kind_token,test_kind,origin,section,non_negotiable,sharpest,global) "
            "VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (r["id"], r["description"], r.get("fire_condition"), r["status"], r["status_raw"],
             r.get("kind_token"), r.get("test_kind"), r.get("origin"),
             r["section"], r["non_negotiable"], r.get("sharpest", 0), r["global"]))
        if r.get("origin") and r["origin"].startswith("AP"):
            ap = r["origin"][:4]
            conn.execute("INSERT OR IGNORE INTO edge(src,dst,rel) VALUES(?,?, 'falsified_by')",
                         (ap, r["id"]))
            ap_ks_count[ap] = ap_ks_count.get(ap, 0) + 1
    for ap, n in ap_ks_count.items():
        conn.execute("UPDATE proof SET ks_count=? WHERE id=?", (n, ap))

    # Fold in the Ollama enrichment overlay (test_kind + fire_condition) ONLY where the deterministic
    # parse left a gap. G's own per-proof text is authoritative for both, so the 1B-model overlay now
    # fills holes rather than overwriting verbatim values. (COALESCE keeps the existing non-null.)
    enrich_path = ROOT / "canon" / "ks_enrichment.json"
    if enrich_path.exists():
        import json as _json2
        cols = {r[1] for r in conn.execute("PRAGMA table_info(kill_switch)")}
        if "test_kind" not in cols:
            conn.execute("ALTER TABLE kill_switch ADD COLUMN test_kind TEXT")
        if "fire_condition" not in cols:
            conn.execute("ALTER TABLE kill_switch ADD COLUMN fire_condition TEXT")
        for kid, e in _json2.loads(enrich_path.read_text(encoding="utf-8")).items():
            tk = e.get("test_kind") or None
            fc = e.get("fire_condition") or None
            conn.execute(
                "UPDATE kill_switch SET test_kind=COALESCE(test_kind,?), "
                "fire_condition=COALESCE(NULLIF(fire_condition,''),?) WHERE id=?",
                (tk, fc, kid))

    # --- dependency + axiom-usage edges (the queryable derivation graph) ---
    for ap, dep_set in deps.items():
        for dep in dep_set:
            conn.execute("INSERT OR IGNORE INTO edge(src,dst,rel) VALUES(?,?, 'depends_on')",
                         (ap, dep))
    for ap, ax_set in axioms_used.items():
        for ax in ax_set:
            conn.execute("INSERT OR IGNORE INTO edge(src,dst,rel) VALUES(?,?, 'uses_axiom')",
                         (ap, ax))

    # --- corpus facts ---
    for k, v in CORPUS_FACTS.items():
        conn.execute("INSERT OR REPLACE INTO corpus_fact(key,value) VALUES(?,?)", (k, v))
    conn.execute("INSERT OR REPLACE INTO corpus_fact(key,value) VALUES('ks_extracted_total',?)",
                 (str(len(ks_rows)),))

    conn.commit()
    return conn


def main() -> int:
    conn = build(reset=True)
    n_ax = conn.execute("SELECT count(*) FROM axiom").fetchone()[0]
    n_pf = conn.execute("SELECT count(*) FROM proof WHERE kind='proof'").fetchone()[0]
    n_prose = conn.execute("SELECT count(*) FROM proof WHERE kind='prose'").fetchone()[0]
    n_pred = conn.execute("SELECT count(*) FROM prediction").fetchone()[0]
    n_ks = conn.execute("SELECT count(*) FROM kill_switch").fetchone()[0]
    n_edge = conn.execute("SELECT count(*) FROM edge").fetchone()[0]
    print(f"[ingest] canon built at {DB_PATH.relative_to(ROOT.parent)}")
    print(f"  axioms={n_ax}  proofs={n_pf}  prose={n_prose}  predictions={n_pred}  "
          f"kill_switches={n_ks}  edges={n_edge}")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
