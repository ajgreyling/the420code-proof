#!/usr/bin/env python3
"""Local (Ollama) semantic enrichment of the kill-switch canon — free, offline.

The deterministic parser gives each switch an id, status, origin, and description. What it
CANNOT give is semantic structure: *what kind of test is this?* (an experiment to run, a maths
theorem to check, an observation to make, a logical proof). That classification is cheap
semantic work — exactly what a small local model is for. This is the standard use of
Ollama (`llama3.2:1b` at http://localhost:11434/api/generate) for bulk semantic passes that
don't justify a metered call.

For each LIVE switch it asks the local model to classify the test as one of
{empirical, structural, theoretical, logical, observational} and to extract, in ≤12 words,
the condition that would FIRE it. Results go into kill_switch.test_kind / fire_condition (added
here if absent), so `./run.sh switches` and the gate can use them. Falls back gracefully if
Ollama is down (the rest of the model is unaffected).

    python3 -m engine.ollama_enrich            # enrich LIVE switches lacking a test_kind
    python3 -m engine.ollama_enrich --limit 20 # cap how many (it's ~0.3s each on llama3.2:1b)
    python3 -m engine.ollama_enrich --all      # re-enrich everything, overwriting
"""
from __future__ import annotations

import json
import re
import sqlite3
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "canon" / "420code.db"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:1b"
KINDS = {"empirical", "structural", "theoretical", "logical", "observational"}

# The local model is reliable at CLASSIFICATION (a constrained label) but a 1B model hallucinates
# free text, so we DO NOT ask it to generate the fire condition — we extract that faithfully from
# the switch's own description (below). The model only picks the test_kind.
_SYS = (
    "You classify one falsification condition ('kill switch') from a physics/philosophy framework "
    "by the KIND of test it demands. Reply with STRICT JSON only: "
    '{"test_kind": one of [empirical, structural, theoretical, logical, observational]}. '
    "empirical=needs a lab experiment/measurement; observational=needs astronomical or real-world "
    "data observation; structural=internal consistency of the model's own mathematics; "
    "theoretical=a derivation/calculation must come out a certain way; logical=a proof or "
    "contradiction. Judge only from the text given. No prose, no markdown, no extra keys."
)

# The fire condition is usually stated IN the description ("If <X>, <claim> fails"). Pull it out
# verbatim rather than letting a 1B model invent one.
_FIRE = re.compile(r"\bIf\b(.+?)(?:,?\s+(?:the\s+)?[\w -]+\s+(?:fails|breaks|is false|collapses))",
                   re.I | re.S)


def _ollama_up() -> bool:
    try:
        urllib.request.urlopen("http://localhost:11434/api/tags", timeout=3).read()
        return True
    except (urllib.error.URLError, TimeoutError, OSError):
        return False


def _extract_fire(desc: str) -> str:
    """Faithfully pull the 'If X, … fails' fire condition from the switch's own description."""
    m = _FIRE.search(desc)
    if m:
        return ("If" + m.group(1)).strip()[:140]
    return ""  # many terse switches state no explicit 'if' clause; leave blank rather than invent


def _classify(desc: str, status_raw: str) -> dict | None:
    prompt = f"{_SYS}\n\nSWITCH (status: {status_raw}): {desc}\n\nJSON:"
    payload = {"model": MODEL, "prompt": prompt, "stream": False,
               "format": "json", "options": {"temperature": 0.0, "num_predict": 40}}
    data = json.dumps(payload).encode()
    try:
        req = urllib.request.Request(OLLAMA_URL, data=data,
                                     headers={"content-type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=30) as r:
            resp = json.loads(r.read().decode())
        obj = json.loads(resp.get("response", "{}"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError):
        return None
    kind = str(obj.get("test_kind", "")).strip().lower()
    if kind not in KINDS:
        # fall back to the registry's own status annotation when the model is unsure
        sr = status_raw.lower()
        kind = ("empirical" if "empiric" in sr else "structural" if "structural" in sr
                else "theoretical" if "theor" in sr else "structural")
    return {"test_kind": kind, "fire_condition": _extract_fire(desc)}


def _ensure_columns(conn) -> None:
    cols = {r[1] for r in conn.execute("PRAGMA table_info(kill_switch)")}
    if "test_kind" not in cols:
        conn.execute("ALTER TABLE kill_switch ADD COLUMN test_kind TEXT")
    if "fire_condition" not in cols:
        conn.execute("ALTER TABLE kill_switch ADD COLUMN fire_condition TEXT")


def main() -> int:
    if not DB_PATH.exists():
        sys.exit("canon not built — run `./run.sh ingest` first")
    if not _ollama_up():
        print("[ollama-enrich] Ollama not reachable at :11434 — skipping (model unaffected). "
              "Start it with `ollama serve` and pull llama3.2:1b.")
        return 0

    argv = sys.argv[1:]
    limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else None
    do_all = "--all" in argv

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    _ensure_columns(conn)

    where = "status='LIVE'" + ("" if do_all else " AND (test_kind IS NULL OR test_kind='')")
    where += " AND description IS NOT NULL AND length(description) >= 8"
    rows = conn.execute(f"SELECT id,description,status_raw FROM kill_switch WHERE {where} "
                        f"ORDER BY id" + (f" LIMIT {limit}" if limit else "")).fetchall()
    if not rows:
        print("[ollama-enrich] nothing to enrich (all LIVE switches already classified).")
        return 0

    print(f"[ollama-enrich] classifying {len(rows)} switches with {MODEL} (local, free)…")
    n = 0
    kinds: dict[str, int] = {}
    for i, r in enumerate(rows, 1):
        res = _classify(r["description"], r["status_raw"] or "")
        if not res:
            continue
        conn.execute("UPDATE kill_switch SET test_kind=?, fire_condition=? WHERE id=?",
                     (res["test_kind"], res["fire_condition"], r["id"]))
        kinds[res["test_kind"]] = kinds.get(res["test_kind"], 0) + 1
        n += 1
        if i % 25 == 0:
            conn.commit()
            print(f"  …{i}/{len(rows)}")
    conn.commit()

    # Persist as a checked-in overlay so a fresh ingest can re-apply it for free (the same
    # durability pattern as the description repair). ingest folds it back in.
    overlay_path = ROOT / "canon" / "ks_enrichment.json"
    overlay = json.loads(overlay_path.read_text()) if overlay_path.exists() else {}
    for r in conn.execute("SELECT id,test_kind,fire_condition FROM kill_switch "
                          "WHERE test_kind IS NOT NULL AND test_kind!=''"):
        overlay[r["id"]] = {"test_kind": r["test_kind"], "fire_condition": r["fire_condition"] or ""}
    overlay_path.write_text(json.dumps(dict(sorted(overlay.items())), ensure_ascii=False, indent=2))
    conn.close()
    print(f"[ollama-enrich] classified {n} switches. by kind: {kinds}")
    print(f"[ollama-enrich] overlay → {overlay_path.relative_to(ROOT)} "
          f"({len(overlay)} total; survives ingest).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
