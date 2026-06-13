#!/usr/bin/env python3
"""Parse the Master Kill Switch Registry PDF text into structured rows.

The registry is a published column table (KS ID | DESCRIPTION | STATUS | ORIGIN), grouped
into three sections (Physics / Philosophy / Ø Models). `pdftotext -layout` preserves the
columns horizontally, but a single logical row wraps across 1–3 physical lines (the
description and the "LIVE — / EMPIRICAL" status straddle the KS-ID line).

Strategy — column-aware, anchored on the KS-ID token:
  * Detect each KS-ID occurrence (handles the unicode non-breaking hyphen U+2011 the PDF uses).
  * The STATUS column holds one of LIVE / CLOSED / COND. CLOSED / ADDRESSED, sometimes split
    as "LIVE —" + "EMPIRICAL" on adjacent lines; collect tokens from the row's line window.
  * ORIGIN is the trailing ``AP## [letter]`` (or a volume name) on the KS-ID line or its window.
  * DESCRIPTION = the text-column fragments in the window, minus the ID/STATUS/ORIGIN tokens.

This is deterministic and free. The output is a list of dicts the canon ingest upserts.
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_TXT = ROOT / "extract" / "txt" / "Master_Kill_Switch_Registry.txt"

# Five switch-id families across the registry:
#   KS-*  physics + philosophy   (KS-V.1, KS-Q.7, KS-NPP.2, KS-30.4, bare KS-7)
#   PZ-*  Dissolutions   RES-*  Resolutions   HOR-*  Horizons   APP-*  Applications  (Ø Models)
# The number part may itself be dotted (RES-8.5.1). Exclude the literal "N.M" placeholder used
# in prose ("PZ-N.M format throughout") by requiring a digit lead in the number group.
_SWITCH = re.compile(
    r"\b(KS|PZ|RES|HOR|APP)[-‑–]"
    r"([A-Z]{1,4}|\d{1,3})"           # family/section token: letters (V, Q, NPP) or a number
    r"(?:\.(\d{1,3}(?:\.\d{1,3})?))?"  # optional dotted index, possibly two-deep (8.5.1)
    r"\b")
_ORIGIN = re.compile(r"\b(AP\d{2}(?:\s+[A-Z])?|Doors?|Five Doors|Predictions|Dissolutions|"
                     r"Resolutions|Horizons|Applications)\b")
_STATUS_TOKENS = ("COND. CLOSED", "COND CLOSED", "OPEN DEBT", "CLOSED", "ADDRESSED", "LIVE",
                  "EMPIRICAL", "STRUCTURAL", "THEORETICAL")

# Section boundaries (line-anchored headers in the registry text).
_SECTIONS = [
    ("physics", re.compile(r"^Section I\b.*Physics", re.I)),
    ("philosophy", re.compile(r"^Section II\b.*Philosophy", re.I)),
    ("oh_models", re.compile(r"^Section III\b.*Models", re.I)),
]


def _norm(s: str) -> str:
    # Normalise the PDF's non-breaking hyphen (U+2011) and odd spaces to ASCII for matching.
    s = s.replace("‑", "-").replace("–", "-")
    return unicodedata.normalize("NFKC", s)


def _canon_id(m: re.Match) -> str:
    prefix, fam, num = m.group(1), m.group(2), m.group(3)
    return f"{prefix}-{fam}.{num}" if num else f"{prefix}-{fam}"


def _classify_status(window_text: str) -> tuple[str, str]:
    """Return (status_enum, status_raw) from the text window around a KS row."""
    t = window_text.upper()
    raw_bits = []
    if "COND" in t and "CLOSED" in t:
        return "COND_CLOSED", "COND. CLOSED"
    if "OPEN DEBT" in t:
        return "OPEN_DEBT", "OPEN DEBT"
    if "ADDRESSED" in t:
        return "ADDRESSED", "ADDRESSED"
    if "CLOSED" in t:
        return "CLOSED", "CLOSED"
    if "LIVE" in t:
        raw_bits.append("LIVE")
        for kind in ("EMPIRICAL", "STRUCTURAL", "THEORETICAL"):
            if kind[:6] in t:
                raw_bits.append(kind)
                break
        return "LIVE", " — ".join(raw_bits)
    return "LIVE", "LIVE"  # registry default for an un-annotated switch in a live section


def _strip_known(text: str) -> str:
    """Remove ID/status/origin tokens and registry chrome from a description blob."""
    t = _norm(text)
    t = _SWITCH.sub("", t)
    t = _ORIGIN.sub("", t)
    for tok in _STATUS_TOKENS:
        t = re.sub(re.escape(tok), "", t, flags=re.I)
    t = re.sub(r"\b(KS ID|DESCRIPTION|STATUS|ORIGIN)\b", "", t, flags=re.I)
    t = re.sub(r"^\s*\d+\s*$", "", t)          # stray page numbers
    t = re.sub(r"[—–-]\s*$", "", t)
    t = re.sub(r"\s+", " ", t).strip(" .—–-‑")
    return t


def parse(path: Path = REGISTRY_TXT) -> list[dict]:
    lines = _norm(path.read_text(encoding="utf-8")).splitlines()

    # Map each line to its section.
    section_of = [None] * len(lines)
    cur = "physics"  # everything before "Section I" is the closed-list preamble → physics
    for i, ln in enumerate(lines):
        for name, rx in _SECTIONS:
            if rx.search(ln.strip()):
                cur = name
        section_of[i] = cur

    # Bare-letter family ids with no number that are actually truncations of longer tokens
    # in the source text: "KS-AP" ← "KS-AP29", "KS-L" ← "KS-L.1". Not real switches.
    _NOISE = {"KS-AP", "KS-L", "KS-N"}

    rows: dict[str, dict] = {}
    for i, ln in enumerate(lines):
        for m in _SWITCH.finditer(ln):
            ksid = _canon_id(m)
            if m.group(2) == "N":  # the literal "PZ-N.M"/"RES-N.M" placeholder in prose
                continue
            if ksid in _NOISE:     # truncation false-positives
                continue
            # window: the KS-ID line plus 2 lines above/below catches wrapped desc + status.
            lo, hi = max(0, i - 2), min(len(lines), i + 3)
            window = "\n".join(lines[lo:hi])
            status, status_raw = _classify_status(window)
            origin_m = _ORIGIN.search(ln) or _ORIGIN.search(window)
            origin = re.sub(r"\s+", " ", origin_m.group(1)).strip() if origin_m else None
            desc = _strip_known(window)

            # First occurrence wins for status/origin (the defining row); later mentions only
            # enrich the description if the first was empty.
            if ksid not in rows:
                rows[ksid] = {
                    "id": ksid,
                    "description": desc,
                    "status": status,
                    "status_raw": status_raw,
                    "origin": origin,
                    "section": section_of[i],
                    "non_negotiable": 0,
                    "global": 1 if "GLOBAL KILL SWITCH" in window.upper() else 0,
                }
            else:
                r = rows[ksid]
                if (not r["description"]) and desc:
                    r["description"] = desc
                if r["global"] == 0 and "GLOBAL KILL SWITCH" in window.upper():
                    r["global"] = 1

    return list(rows.values())


def summary(rows: list[dict]) -> dict:
    by_status: dict[str, int] = {}
    by_section: dict[str, int] = {}
    for r in rows:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
        by_section[r["section"]] = by_section.get(r["section"], 0) + 1
    return {"total": len(rows), "by_status": by_status, "by_section": by_section}


if __name__ == "__main__":
    import json
    rows = parse()
    print(json.dumps(summary(rows), indent=2))
    print("\nsample rows:")
    for r in rows[:12]:
        print(f"  {r['id']:10} [{r['status']:11}] ({r['section']:10}) "
              f"<{r['origin']}>  {r['description'][:60]}")
