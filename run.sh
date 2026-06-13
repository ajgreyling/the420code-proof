#!/usr/bin/env bash
# the420code-proof — front door.
#
# An independent, executable check of G's *420 Code* unified theory: re-derive the five headline
# numbers from a single measured input (α) and test each against the published experimental value,
# then index the falsification registry ("kill switches") into a queryable canon.
#
#   ./run.sh mirror     (re-)download G's corpus from the420code.org into mirror/  (network; polite)
#   ./run.sh extract    pdftotext every mirrored PDF → extract/txt/                (free, local)
#   ./run.sh ingest     build the canon SQLite DB from the mirror                  (free, local)
#   ./run.sh gate       re-ingest + EXECUTE predictions + audit                    (free; exit 0/1/2)
#   ./run.sh verify     structured reconstruction of G's 5 predictions             (free)
#   ./run.sh verify-g   G's VERBATIM Appendix B script (his published verify.py)   (free)
#   ./run.sh parity     prove reconstruction == G's script (drift check)           (free)
#   ./run.sh scorecard  prediction pass/fail table with residuals vs measured      (free)
#   ./run.sh proofs     the 42 proofs by part                                      (free)
#   ./run.sh switches   query kill switches (--live --paper AP15 --section physics --kind empirical
#                        --moral  the NON-NEGOTIABLE/moral switches · --sharpest  G's sharpest tests)
#   ./run.sh axiom B    which proofs invoke an axiom                               (free)
#   ./run.sh depends AP31   a proof's dependency neighbourhood                     (free)
#   ./run.sh stats      declared-vs-extracted corpus counts                        (free)
#   ./run.sh report     full canon report → build/CANON_REPORT.md                  (free)
#   ./run.sh build      extract + ingest + gate + report (the whole free pipeline)
#   ./run.sh enrich     OPTIONAL local Ollama: classify switches by test kind      (free, offline)
#
# Everything here is FREE, LOCAL, OFFLINE and DEPENDENCY-FREE (Python 3 stdlib + `pdftotext`).
# `enrich` additionally needs a local Ollama daemon, but the prover does not.
#
# G's corpus is NOT redistributed here. `./run.sh mirror` fetches it from G's own site (which
# explicitly welcomes it). G's work is © G / Studio G, CC BY 4.0 — see NOTICE.md.
set -euo pipefail
cd "$(dirname "$0")"

# Use whatever python3 is on PATH. No virtualenv, no SDKs required for the prover.
PY="${PY:-python3}"

cmd="${1:-help}"; shift || true
case "$cmd" in
  mirror)    exec bash mirror/fetch.sh "$@";;
  extract)
    command -v pdftotext >/dev/null 2>&1 || { echo "[extract] needs 'pdftotext' (poppler-utils)"; exit 1; }
    mkdir -p extract/txt; n=0
    for p in mirror/pdf/*.pdf; do
      [ -e "$p" ] || { echo "[extract] no PDFs in mirror/pdf — run './run.sh mirror' first"; exit 1; }
      pdftotext -layout -nopgbrk "$p" "extract/txt/$(basename "$p" .pdf).txt" && n=$((n+1))
    done
    echo "[extract] $n PDFs → extract/txt/";;
  ingest)    exec "$PY" -m engine.ingest "$@";;
  gate)      exec "$PY" -m engine.gate "$@";;
  verify)    exec "$PY" -m engine.verify "$@";;
  verify-g)  exec "$PY" -m engine.verify_g_original "$@";;
  parity)    exec "$PY" -m engine.test_verify_parity "$@";;
  scorecard) exec "$PY" -m engine.report scorecard "$@";;
  proofs)    exec "$PY" -m engine.report proofs "$@";;
  switches)  exec "$PY" -m engine.report switches "$@";;
  axiom)     exec "$PY" -m engine.report axiom "$@";;
  depends)   exec "$PY" -m engine.report depends "$@";;
  stats)     exec "$PY" -m engine.report stats "$@";;
  report)
    mkdir -p build
    "$PY" -m engine.report markdown > build/CANON_REPORT.md
    echo "[report] → build/CANON_REPORT.md";;
  build)
    bash "$0" extract
    "$PY" -m engine.ingest
    "$PY" -m engine.gate || true
    bash "$0" report
    echo "[build] free pipeline complete.";;
  enrich)    exec "$PY" -m engine.ollama_enrich "$@";;
  help|*)
    sed -n '2,30p' "$0" | sed 's/^# \{0,1\}//';;
esac
