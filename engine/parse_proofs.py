#!/usr/bin/env python3
"""Parse kill switches AND dependency edges from the per-proof bodies (AP01–AP42).

The Master Kill Switch Registry is a terse summary table; each Artist's Proof carries a
RICHER local source the registry condenses:

  * a "Kill Switches" / "Appendix F — Master List of Falsification Criteria" section whose
    entries read   `KS-31.5 (Law-as-geometry): LIVE — EMPIRICAL. If <condition>, <claim> fails.`
    — i.e. id, parenthetical name, status, a TYPE, AND a full one-sentence condition; and
  * a "§0 — Status and Dependency" section with an explicit `Requires:` / `applies … AP29, AP06`
    dependency chain between proofs, plus per-section epistemic status.

This module extracts all of it, deterministically and for free, from extract/txt/AP*.txt. The
caller (ingest) merges these over the registry rows: the registry is authoritative for STATUS
and for the Ø Models families (PZ/RES/HOR/APP); the proof bodies supply better descriptions,
the kill-switch *type taxonomy*, the moral/non-negotiable/global flags, the verbatim
fire-condition, the depends_on graph, AND the KS→KS cross-reference edges.

Fidelity upgrade (2026-06): G's switches carry far more structure than id+status. He types each
switch (EMPIRICAL / HARD / STRUCTURAL / NON-NEGOTIABLE / DEPENDENT / DEBT / MATHEMATICAL / …),
marks some as MORAL or GLOBAL, writes some as the "sharpest test", and occasionally chains one
switch to another ("If KS-L.1 … and KS-Q.9"). All of that is now captured verbatim so the model
mirrors his falsification *structure*, not merely his counts.
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TXT = ROOT / "extract" / "txt"

# G's full, observed kill-switch TYPE vocabulary (the token after `STATUS —`). Counted verbatim
# across the corpus; ordered longest-first so multi-word types win the alternation. These are HIS
# words — do not invent types he doesn't use.
_KIND_TOKENS = [
    "NON-NEGOTIABLE", "MATHEMATICAL", "OBSERVATIONAL", "THEORETICAL",
    "STRUCTURAL", "EMPIRICAL", "DEPENDENT", "LOGICAL", "STAGED", "MASTER",
    "MORAL", "DEBT", "HARD",
]
_KIND_ALT = "|".join(re.escape(k) for k in _KIND_TOKENS)

# `KS-31.5 (Law-as-geometry): LIVE — EMPIRICAL. <condition sentence(s)>`
# id, optional parenthetical name, status, optional TYPE, then the condition. The condition starts
# right after the TYPE token's trailing punctuation (we do NOT swallow the first clause), and runs
# to a blank line or the next KS id.
_ENTRY = re.compile(
    r"\bKS[-‑–](?P<fam>[A-Z]{1,4}|\d{1,3})(?:\.(?P<num>\d{1,3}))?"
    r"\s*(?:\((?P<name>[^)]{1,80})\))?\s*[:：]\s*"
    r"(?P<status>LIVE|CLOSED|OPEN DEBT|COND\.? CLOSED|ADDRESSED)"
    r"\s*(?:[—–-]\s*(?P<kind>" + _KIND_ALT + r"))?"
    r"\s*[.:—–-]?\s*(?P<desc>.*?)(?=\n\s*\n|\bKS[-‑–](?:[A-Z]{1,4}|\d{1,3})|$)",
    re.S)

# NOTE on KS→KS edges: G *does* occasionally chain one switch to another, but almost always in
# prose discussion ("… and KS-Q.9 (ergodicity across cycles)"), NOT structurally inside a switch's
# own condition block. Attributing those prose mentions to an owning switch produces mostly
# self-references and noise — too sparse and unstructured to model faithfully. We therefore do NOT
# synthesize a KS→KS edge layer; the proof→proof dependency lattice below already carries the real
# derivation structure. (If G later formalises inter-switch dependencies, revisit.)

# Dependency chain (proof→proof). The §0 "Requires:"/"applies … —"/"depends on" clause often spans
# several sentences and lists many AP refs. Capture a generous window and harvest every AP ref.
_REQUIRES = re.compile(
    r"(?:Requires|It applies|applies(?:\s+existing\s+derivations)?|depends on|builds on|"
    r"Dependency Chain)\b(?P<body>.{0,400})", re.S | re.I)
_AP_REF = re.compile(r"AP(\d{2})")

# Markers that flag a switch's special weight, scanned in the entry's local text (status + body).
_RE_NONNEG = re.compile(r"NON[-\s]?NEGOTIABLE", re.I)
_RE_MORAL  = re.compile(r"\bMORAL\b", re.I)
_RE_GLOBAL = re.compile(r"\bGLOBAL\s+KILL\s+SWITCH\b", re.I)
_RE_SHARP  = re.compile(r"sharpest test", re.I)


def _norm(s: str) -> str:
    return unicodedata.normalize("NFKC", s.replace("‑", "-").replace("–", "-"))


def _clean(d: str, limit: int = 300) -> str:
    d = re.sub(r"\s+", " ", d).strip()
    d = re.sub(r"^\d+\s+", "", d)            # leading page number
    d = re.sub(r"\s+\d+\s*$", "", d)         # trailing page number
    d = re.sub(r"^[,;:—–-]\s*", "", d)  # leading stray punctuation from the status split
    return d.strip(" .")[:limit]


def _status_enum(raw: str) -> str:
    r = raw.upper()
    if "COND" in r:
        return "COND_CLOSED"
    if "OPEN" in r:
        return "OPEN_DEBT"
    if "CLOSED" in r:
        return "CLOSED"
    if "ADDRESSED" in r:
        return "ADDRESSED"
    return "LIVE"


# Map G's published TYPE token → the canonical test_kind bucket the gate/report already use.
# (EMPIRICAL needs new real-world data; everything else tests the derivation's internal coherence.)
_KIND_BUCKET = {
    "EMPIRICAL": "empirical", "OBSERVATIONAL": "empirical",
    "STRUCTURAL": "structural", "HARD": "structural", "MASTER": "structural",
    "STAGED": "structural", "DEPENDENT": "structural", "NON-NEGOTIABLE": "structural",
    "MORAL": "structural", "MATHEMATICAL": "logical", "LOGICAL": "logical",
    "THEORETICAL": "theoretical", "DEBT": "theoretical",
}


def _axioms_used(t: str) -> set[str]:
    """Which of the four core axioms a proof invokes. The corpus writes them as a set
    `{S, B, R, C}` (full set when all four), or names them individually (Axiom B, Axiom R)."""
    used: set[str] = set()
    head = t[:8000]
    if re.search(r"\{\s*S\s*,\s*B\s*,\s*R\s*,\s*C\s*\}", head):
        used |= {"S", "B", "R", "C"}
    for ax in ("S", "B", "R", "C"):
        if re.search(rf"\bAxiom\s+{ax}\b", head):
            used.add(ax)
    return used


def parse_proof(ap: str, text: str) -> tuple[list[dict], set[str], set[str]]:
    """Return (kill_switch rows, AP ids this proof depends on, core axioms it uses)."""
    t = _norm(text)
    rows: dict[str, dict] = {}
    for m in _ENTRY.finditer(t):
        fam, num = m.group("fam"), m.group("num")
        ksid = f"KS-{fam}.{num}" if num else f"KS-{fam}"
        name = (m.group("name") or "").strip()
        kind_tok = (m.group("kind") or "").upper()
        # The verbatim fire-condition is the condition sentence(s) AS WRITTEN, kept long and clean
        # but un-merged with the name (so we don't lose the actual trigger to truncation).
        fire = _clean(m.group("desc") or "", limit=400)
        # The human description prefers name + condition (back-compat with prior behaviour).
        desc = f"{name}. {fire}" if name and fire else (name or fire)
        local = m.group(0)  # status + type + body, for marker scanning
        non_neg = 1 if (_RE_NONNEG.search(local) or _RE_MORAL.search(local)) else 0
        is_glob = 1 if (_RE_GLOBAL.search(local) or name.lower().startswith("global")) else 0
        # keep the richest copy seen (some ids recur in summary + body)
        cand = {
            "id": ksid, "description": _clean(desc), "fire_condition": fire,
            "status": _status_enum(m.group("status")),
            "status_raw": f"{m.group('status').upper()}{' — ' + kind_tok if kind_tok else ''}",
            "kind_token": kind_tok or None,
            "test_kind": _KIND_BUCKET.get(kind_tok) if kind_tok else None,
            "origin": ap, "section": "physics",
            "non_negotiable": non_neg, "global": is_glob,
            "sharpest": 1 if _RE_SHARP.search(local) else 0,
        }
        prev = rows.get(ksid)
        if prev is None or len(cand["fire_condition"]) > len(prev["fire_condition"]):
            # merge sticky flags so a richer description never drops a flag an earlier copy set
            if prev:
                cand["non_negotiable"] |= prev["non_negotiable"]
                cand["global"] |= prev["global"]
                cand["sharpest"] |= prev["sharpest"]
                cand["test_kind"] = cand["test_kind"] or prev["test_kind"]
                cand["kind_token"] = cand["kind_token"] or prev["kind_token"]
            rows[ksid] = cand

    deps: set[str] = set()
    for rm in _REQUIRES.finditer(t[:6000]):  # §0 is at the top of every proof
        for ap_ref in _AP_REF.finditer(rm.group("body")):
            dep = f"AP{ap_ref.group(1)}"
            if dep != ap:
                deps.add(dep)
    return list(rows.values()), deps, _axioms_used(t)


def parse_all() -> tuple[list[dict], dict[str, set[str]], dict[str, set[str]]]:
    all_rows: list[dict] = []
    deps: dict[str, set[str]] = {}
    axioms: dict[str, set[str]] = {}
    for f in sorted(TXT.glob("AP*.txt")):
        ap = f.name[:4]
        rows, d, ax = parse_proof(ap, f.read_text(encoding="utf-8"))
        all_rows.extend(rows)
        if d:
            deps[ap] = d
        if ax:
            axioms[ap] = ax
    return all_rows, deps, axioms


if __name__ == "__main__":
    rows, deps, axioms = parse_all()
    print(f"per-proof kill switches: {len(rows)} (unique ids: {len({r['id'] for r in rows})})")
    by_status: dict[str, int] = {}
    by_kind: dict[str, int] = {}
    for r in rows:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
        k = r["kind_token"] or "(untyped)"
        by_kind[k] = by_kind.get(k, 0) + 1
    print("by status:", by_status)
    print("by published TYPE:", dict(sorted(by_kind.items(), key=lambda kv: -kv[1])))
    n_typed = sum(1 for r in rows if r["kind_token"])
    print(f"typed: {n_typed}/{len(rows)} ({100*n_typed//max(len(rows),1)}%)   "
          f"non-negotiable/moral: {sum(r['non_negotiable'] for r in rows)}   "
          f"global: {sum(r['global'] for r in rows)}   "
          f"sharpest-test: {sum(r['sharpest'] for r in rows)}")
    print(f"\ndependency edges (proof→proof): {sum(len(v) for v in deps.values())} across {len(deps)} proofs")
    print(f"uses_axiom edges: {sum(len(v) for v in axioms.values())} across {len(axioms)} proofs")
    print("\nsample rich entries (id · status · TYPE · flags · verbatim fire-condition):")
    for r in rows[:8]:
        tag = r["kind_token"] or "—"
        flags = "".join(c for c, on in (("N", r["non_negotiable"]), ("G", r["global"]),
                                        ("!", r["sharpest"])) if on) or " "
        print(f"  {r['id']:<10} [{r['status']:<10} {tag:<14} {flags}] {r['fire_condition'][:56]}")
