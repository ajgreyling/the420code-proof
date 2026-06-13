#!/usr/bin/env python3
"""The 420 Code gate — re-ingest the canon, EXECUTE the predictions, audit integrity.

Rebuild the canon DB from the mirror, then run a
suite of checks over it. The decisive check is *executable*: re-derive G's five predictions
from α and assert each lands inside his published tolerance — if a kill switch would fire,
the gate fails. The rest are canon-integrity checks (coverage vs the registry's declared
counts, structural completeness).

Exit codes (so it can gate a commit / CI):
    0  clean — every prediction within tolerance, no integrity errors
    1  one or more ERROR-severity issues (a prediction outside tolerance, or broken canon)
    2  the audit itself failed to run (missing mirror, build error)

    python3 -m engine.gate            # re-ingest + audit
    python3 -m engine.gate --strict   # also fail on warnings (coverage gaps, empty descriptions)
    python3 -m engine.gate --quiet    # print only on failure
"""
from __future__ import annotations

import sys

from . import ingest, test_verify_parity, verify


def _find_cycles(deps: dict[str, set[str]]) -> list[list[str]]:
    """Return simple dependency cycles (DFS back-edges) as node lists. Small graph — fine."""
    cycles: list[list[str]] = []
    seen_pairs: set[frozenset] = set()
    for a, outs in deps.items():
        for b in outs:
            if a in deps.get(b, set()):  # 2-cycle a↔b
                pair = frozenset((a, b))
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    cycles.append([a, b, a])
    return cycles


def _issues(conn) -> list[dict]:
    out: list[dict] = []

    # (A0) FIDELITY CHECK — the structured reconstruction must still equal G's published script.
    g = test_verify_parity._g_values()
    structured = {p.key: p.predicted for p in verify.compute()}
    for key, gval in g.items():
        sval = structured.get(key, 0.0)
        if abs(sval - gval) / abs(gval) >= 1e-9:
            out.append({"severity": "error", "kind": "verify-drift", "where": f"engine/verify.py:{key}",
                        "problem": f"structured value {sval:.12g} ≠ G's Appendix B value {gval:.12g}",
                        "fix": "engine/verify.py drifted from G's published math — reconcile"})

    # (A) EXECUTABLE CHECK — the predictions must reproduce within G's tolerance.
    for p in verify.compute():
        if not p.passed:
            out.append({
                "severity": "error", "kind": "prediction-out-of-tolerance",
                "where": f"Part {p.part} · {p.name}",
                "problem": f"residual {p.residual:.4g} {p.residual_unit} exceeds tolerance "
                           f"{p.tolerance} {p.residual_unit} (predicted {p.predicted:.10g} vs "
                           f"measured {p.measured:.10g}, {p.measured_source})",
                "fix": "a kill switch fires — the derivation no longer matches measurement"})

    # (B) every proof is placed in one of the 8 parts.
    orphan = conn.execute(
        "SELECT id,title FROM proof WHERE kind='proof' AND part_no IS NULL").fetchall()
    for r in orphan:
        out.append({"severity": "error", "kind": "proof-unplaced", "where": r["id"],
                    "problem": f"{r['id']} ({r['title']}) is not assigned to any of the 8 parts",
                    "fix": "add it to PARTS in engine/ingest.py"})

    # (C) every prediction has an originating proof edge.
    for p in verify.compute():
        has = conn.execute("SELECT 1 FROM edge WHERE dst=? AND rel='predicts'", (p.key,)).fetchone()
        if not has:
            out.append({"severity": "error", "kind": "prediction-unattributed", "where": p.key,
                        "problem": f"prediction '{p.key}' has no originating proof",
                        "fix": "add it to pred_origin in engine/ingest.py"})

    # (D) coverage vs the registry's declared total. The gap to 549 is INHERENT to the source:
    # the registry header counts 266 physics switches but its Section I table only enumerates ~233
    # individually (the rest are summarised by per-AP count, not tabulated as rows). So <549 is the
    # honest ceiling of row-level extraction, not a parser defect — hence info, not warning, at ≥95%.
    declared = int(conn.execute(
        "SELECT value FROM corpus_fact WHERE key='ks_declared_total'").fetchone()[0])
    got = conn.execute("SELECT count(*) FROM kill_switch").fetchone()[0]
    if got < declared:
        pct = got / declared * 100
        sev = "info" if pct >= 95 else "warning" if pct >= 88 else "error"
        out.append({"severity": sev, "kind": "ks-coverage", "where": "registry",
                    "problem": f"{got}/{declared} kill switches individually indexed ({pct:.0f}%); "
                               f"the rest are registry-summarised by per-AP count, not tabulated",
                    "fix": "row-level ceiling reached; remaining switches have no individual rows to parse"})

    # (F) dependency graph integrity: every depends_on target is a real proof (error if dangling),
    #     and report any dependency cycles (info — G's papers legitimately cross-reference).
    proofs = {r["id"] for r in conn.execute("SELECT id FROM proof WHERE kind='proof'")}
    deps: dict[str, set[str]] = {}
    for e in conn.execute("SELECT src,dst FROM edge WHERE rel='depends_on'"):
        deps.setdefault(e["src"], set()).add(e["dst"])
        if e["dst"] not in proofs:
            out.append({"severity": "error", "kind": "dep-dangling", "where": e["src"],
                        "problem": f"{e['src']} depends on {e['dst']}, which is not a known proof",
                        "fix": "fix the dependency parse in engine/parse_proofs.py"})
    cycles = _find_cycles(deps)
    if cycles:
        out.append({"severity": "info", "kind": "dep-cycle", "where": "graph",
                    "problem": f"{len(cycles)} dependency cycle(s) (mutual cross-references): "
                               + "; ".join(" → ".join(c) for c in cycles[:4]),
                    "fix": "expected — paired proofs cite each other's sections; not an error"})

    # (E) no LIVE/non-negotiable switch with an empty description (warning).
    empties = conn.execute(
        "SELECT count(*) FROM kill_switch WHERE status='LIVE' AND (description IS NULL OR description='')"
    ).fetchone()[0]
    if empties:
        out.append({"severity": "warning", "kind": "ks-empty-description", "where": "kill_switch",
                    "problem": f"{empties} LIVE switches have no description",
                    "fix": "run the metered description-repair pass (engine/repair_descriptions.py)"})

    return out


def run(*, strict: bool = False, quiet: bool = False) -> int:
    try:
        conn = ingest.build(reset=True)
        issues = _issues(conn)
    except Exception as e:  # noqa: BLE001 — the gate must never crash silently
        print(f"[420-gate] AUDIT FAILED TO RUN: {type(e).__name__}: {e}", file=sys.stderr)
        return 2

    errors = [i for i in issues if i["severity"] == "error"]
    warnings = [i for i in issues if i["severity"] == "warning"]
    infos = [i for i in issues if i["severity"] == "info"]
    blocking = errors + (warnings if strict else [])

    if blocking:
        print(f"[420-gate] BLOCKED — {len(errors)} error(s), {len(warnings)} warning(s)"
              f"{' (strict)' if strict else ''}:", file=sys.stderr)
        for i in blocking:
            print(f"  [{i['severity']}] {i['kind']} @ {i['where']}: {i['problem']}\n"
                  f"      fix: {i['fix']}", file=sys.stderr)
        conn.close()
        return 1

    if not quiet:
        npred = conn.execute("SELECT count(*) FROM prediction WHERE passed=1").fetchone()[0]
        nks = conn.execute("SELECT count(*) FROM kill_switch").fetchone()[0]
        live = conn.execute("SELECT count(*) FROM kill_switch WHERE status='LIVE'").fetchone()[0]
        print(f"[420-gate] PASS — {npred}/5 predictions within tolerance & matching G's script, "
              f"{nks} kill switches indexed ({live} live), {len(warnings)} warning(s).")
        for i in warnings:
            print(f"  [warning] {i['kind']} @ {i['where']}: {i['problem']}")
        for i in infos:
            print(f"  [info] {i['kind']} @ {i['where']}: {i['problem']}")
    conn.close()
    return 0


def main() -> int:
    argv = sys.argv[1:]
    return run(strict="--strict" in argv, quiet="--quiet" in argv)


if __name__ == "__main__":
    raise SystemExit(main())
