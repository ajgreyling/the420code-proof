#!/usr/bin/env python3
"""Query / report over the 420 Code canon — the storygraph dashboard analogue.

Read-only views into canon/420code.db. Sub-commands:

    python3 -m engine.report scorecard          # the 5 executable predictions, pass/fail
    python3 -m engine.report proofs             # the 42 proofs by part, with KS counts
    python3 -m engine.report switches [--live] [--paper AP15] [--section physics]
    python3 -m engine.report axiom B            # what derives-from / uses Axiom B
    python3 -m engine.report stats              # corpus-level counts (declared vs extracted)
    python3 -m engine.report markdown           # full canon report → stdout (Markdown)
"""
from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "canon" / "420code.db"


def _conn() -> sqlite3.Connection:
    if not DB_PATH.exists():
        sys.exit("canon not built — run `./run.sh ingest` first")
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


def scorecard(c) -> None:
    print("THE 420 CODE — PREDICTION SCORECARD  (one axiom, one input α, zero free parameters)\n")
    rows = c.execute("SELECT * FROM prediction ORDER BY part").fetchall()
    for r in rows:
        flag = "PASS" if r["passed"] else "FAIL"
        print(f"  [{flag}] Part {r['part']:<4} {r['name']}")
        print(f"         {r['formula']}")
        print(f"         predicted {r['predicted']:.10g} vs measured {r['measured']:.10g} "
              f"({r['measured_source']})")
        print(f"         residual {r['residual']:.4g} {r['residual_unit']}  "
              f"(tolerance {r['tolerance']} {r['residual_unit']})\n")
    n_ok = sum(r["passed"] for r in rows)
    print(f"  {n_ok}/{len(rows)} within tolerance.")


def proofs(c) -> None:
    print("THE 42 ARTIST'S PROOFS — by part\n")
    parts = c.execute(
        "SELECT DISTINCT part_no, part_title, domain FROM proof "
        "WHERE kind='proof' AND part_no IS NOT NULL "
        "ORDER BY CASE part_no WHEN 'I' THEN 1 WHEN 'II' THEN 2 WHEN 'III' THEN 3 "
        "WHEN 'IV' THEN 4 WHEN 'V' THEN 5 WHEN 'VI' THEN 6 WHEN 'VII' THEN 7 ELSE 8 END"
    ).fetchall()
    for p in parts:
        print(f"  Part {p['part_no']} — {p['part_title']}  ({p['domain']})")
        for r in c.execute(
            "SELECT id,title,ks_count,words FROM proof WHERE part_no=? ORDER BY id", (p["part_no"],)):
            w = f"{r['words']//1000}k" if r["words"] else "?"
            print(f"      {r['id']}  {r['title']:<28} {r['ks_count']:>3} KS · {w} words")
        print()


def switches(c, *, live=False, paper=None, section=None, kind=None, moral=False, sharpest=False) -> None:
    tcols = {r[1] for r in c.execute("PRAGMA table_info(kill_switch)")}
    has_kind = "test_kind" in tcols
    has_tok = "kind_token" in tcols
    has_nn = "non_negotiable" in tcols
    has_sharp = "sharpest" in tcols
    extra = [x for x, ok in (("test_kind", has_kind), ("kind_token", has_tok),
                             ("non_negotiable", has_nn), ("sharpest", has_sharp)) if ok]
    cols = "id,status,status_raw,origin,section,description" + ("," + ",".join(extra) if extra else "")
    q = f"SELECT {cols} FROM kill_switch WHERE 1=1"
    args: list = []
    if live:
        q += " AND status='LIVE'"
    if paper:
        q += " AND origin LIKE ?"
        args.append(f"{paper}%")
    if section:
        q += " AND section=?"
        args.append(section)
    if kind and has_kind:
        q += " AND test_kind=?"
        args.append(kind)
    if moral and has_nn:
        q += " AND non_negotiable=1"
    if sharpest and has_sharp:
        q += " AND sharpest=1"
    # surface the weightiest switches first: moral/non-negotiable, then sharpest, then the rest
    order = []
    if has_nn:
        order.append("non_negotiable DESC")
    if has_sharp:
        order.append("sharpest DESC")
    order += ["section", "origin", "id"]
    q += " ORDER BY " + ", ".join(order)
    rows = c.execute(q, args).fetchall()
    flags = [f for f, on in (("live", live), (f"{paper}", paper), (f"{section}", section),
                             (f"{kind}", kind), ("moral", moral), ("sharpest", sharpest)) if on]
    print(f"KILL SWITCHES — {len(rows)} match{(' [' + ', '.join(flags) + ']') if flags else ''}\n")
    for r in rows:
        desc = (r["description"] or "").strip()[:60]
        # prefer G's verbatim published TYPE token; fall back to the canonical bucket
        tok = r["kind_token"] if has_tok and r["kind_token"] else (r["test_kind"] if has_kind else None)
        k = f"{{{tok}}}" if tok else ""
        mark = ""
        if has_nn and r["non_negotiable"]:
            mark += "⊘"   # moral / NON-NEGOTIABLE: forbids a USE, not just falsifies
        if has_sharp and r["sharpest"]:
            mark += "✦"   # G's "sharpest test" of its proof
        print(f"  {r['id']:<11} [{r['status']:<8}] {mark:<2} <{r['origin'] or '?'}> {k:<16} {desc}")


def axiom(c, sym: str) -> None:
    a = c.execute("SELECT * FROM axiom WHERE id=?", (sym,)).fetchone()
    if not a:
        sys.exit(f"no axiom '{sym}' (have S, B, R, C)")
    print(f"AXIOM {a['symbol']} — {a['name']}\n  {a['statement']}\n")
    users = c.execute("SELECT src FROM edge WHERE dst=? AND rel='uses_axiom' ORDER BY src",
                      (sym,)).fetchall()
    if users:
        print(f"  used by {len(users)} proofs: " + ", ".join(u["src"] for u in users))
    else:
        print("  (no explicit uses_axiom edges ingested; the core 4 underlie the whole corpus)")


def depends(c, ap: str) -> None:
    """Show a proof's dependency neighbourhood: what it needs, and what needs it."""
    p = c.execute("SELECT id,title FROM proof WHERE id=?", (ap,)).fetchone()
    if not p:
        sys.exit(f"no proof '{ap}' (e.g. AP10, AP31)")
    print(f"{p['id']} — {p['title']}\n")
    needs = c.execute("SELECT dst FROM edge WHERE src=? AND rel='depends_on' ORDER BY dst",
                      (ap,)).fetchall()
    uses = c.execute("SELECT dst FROM edge WHERE src=? AND rel='uses_axiom' ORDER BY dst",
                     (ap,)).fetchall()
    needed_by = c.execute("SELECT src FROM edge WHERE dst=? AND rel='depends_on' ORDER BY src",
                          (ap,)).fetchall()
    print("  uses axioms : " + (", ".join(u["dst"] for u in uses) or "—"))
    print("  depends on  : " + (", ".join(n["dst"] for n in needs) or "— (foundational / self-contained)"))
    print("  required by : " + (", ".join(n["src"] for n in needed_by) or "—"))
    nks = c.execute("SELECT count(*) FROM kill_switch WHERE origin LIKE ?", (f"{ap}%",)).fetchone()[0]
    print(f"  kill switches: {nks}")


def stats(c) -> None:
    print("CORPUS STATS — declared (registry/llms.txt) vs extracted (this mirror)\n")
    for r in c.execute("SELECT key,value FROM corpus_fact ORDER BY key"):
        print(f"  {r['key']:<28} {r['value']}")
    print()
    by_sec = c.execute(
        "SELECT section, count(*) n, sum(status='LIVE') live FROM kill_switch GROUP BY section"
    ).fetchall()
    print("  extracted kill switches by section:")
    for r in by_sec:
        print(f"      {r['section']:<12} {r['n']:>4} total, {r['live']:>4} live")


def markdown(c) -> None:
    """Emit the whole canon as a Markdown report (build artifact)."""
    P = print
    P("# The 420 Code — Canon Report\n")
    P("*Generated from the mirror by `engine/report.py`. The canon is derived; the mirror is source.*\n")
    facts = {r["key"]: r["value"] for r in c.execute("SELECT key,value FROM corpus_fact")}
    P(f"**Author:** {facts.get('author')} · **DOI:** {facts.get('doi')} · "
      f"**License:** {facts.get('license')} · **Free parameters:** {facts.get('free_parameters')}\n")
    P("## Executable predictions\n")
    P("| Part | Prediction | Predicted | Measured | Residual | Tol | Status |")
    P("|---|---|---|---|---|---|---|")
    for r in c.execute("SELECT * FROM prediction ORDER BY part"):
        P(f"| {r['part']} | {r['name']} | {r['predicted']:.10g} | {r['measured']:.10g} "
          f"| {r['residual']:.3g} {r['residual_unit']} | {r['tolerance']} {r['residual_unit']} "
          f"| {'✅' if r['passed'] else '❌'} |")
    P("\n## Kill-switch coverage\n")
    P(f"Extracted **{facts.get('ks_extracted_total')}** of a declared **{facts.get('ks_declared_total')}**.\n")
    P("| Section | Extracted | Live |")
    P("|---|---|---|")
    for r in c.execute("SELECT section, count(*) n, sum(status='LIVE') live "
                       "FROM kill_switch GROUP BY section"):
        P(f"| {r['section']} | {r['n']} | {r['live']} |")
    P("\n## Derivation graph\n")
    P("Each proof's axiom usage and inter-proof dependencies (parsed from the §0 dependency chains).\n")
    P("| Proof | Part | Uses axioms | Depends on |")
    P("|---|---|---|---|")
    for p in c.execute("SELECT DISTINCT part_no,part_title FROM proof WHERE part_no IS NOT NULL "
                       "ORDER BY CASE part_no WHEN 'I' THEN 1 WHEN 'II' THEN 2 WHEN 'III' THEN 3 "
                       "WHEN 'IV' THEN 4 WHEN 'V' THEN 5 WHEN 'VI' THEN 6 WHEN 'VII' THEN 7 ELSE 8 END"):
        for r in c.execute("SELECT id,title FROM proof WHERE part_no=? ORDER BY id", (p["part_no"],)):
            ax = ", ".join(e["dst"] for e in c.execute(
                "SELECT dst FROM edge WHERE src=? AND rel='uses_axiom' ORDER BY dst", (r["id"],)))
            dep = ", ".join(e["dst"] for e in c.execute(
                "SELECT dst FROM edge WHERE src=? AND rel='depends_on' ORDER BY dst", (r["id"],)))
            P(f"| `{r['id']}` {r['title']} | {p['part_no']} | {ax or '—'} | {dep or '—'} |")

    P("\n## The 42 proofs\n")
    for p in c.execute("SELECT DISTINCT part_no,part_title FROM proof WHERE part_no IS NOT NULL "
                       "ORDER BY CASE part_no WHEN 'I' THEN 1 WHEN 'II' THEN 2 WHEN 'III' THEN 3 "
                       "WHEN 'IV' THEN 4 WHEN 'V' THEN 5 WHEN 'VI' THEN 6 WHEN 'VII' THEN 7 ELSE 8 END"):
        P(f"\n**Part {p['part_no']} — {p['part_title']}**\n")
        for r in c.execute("SELECT id,title,ks_count FROM proof WHERE part_no=? ORDER BY id",
                           (p["part_no"],)):
            P(f"- `{r['id']}` {r['title']} — {r['ks_count']} kill switches")


def main() -> int:
    args = sys.argv[1:]
    cmd = args[0] if args else "scorecard"
    c = _conn()
    if cmd == "scorecard":
        scorecard(c)
    elif cmd == "proofs":
        proofs(c)
    elif cmd == "switches":
        switches(c, live="--live" in args,
                 paper=(args[args.index("--paper") + 1] if "--paper" in args else None),
                 section=(args[args.index("--section") + 1] if "--section" in args else None),
                 kind=(args[args.index("--kind") + 1] if "--kind" in args else None),
                 moral=("--moral" in args or "--nonneg" in args),
                 sharpest="--sharpest" in args)
    elif cmd == "axiom":
        axiom(c, args[1] if len(args) > 1 else "B")
    elif cmd == "depends":
        depends(c, (args[1] if len(args) > 1 else "AP10").upper())
    elif cmd == "stats":
        stats(c)
    elif cmd == "markdown":
        markdown(c)
    else:
        sys.exit(f"unknown command '{cmd}' — see module docstring")
    c.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
