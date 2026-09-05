#!/usr/bin/env bash
# (Re-)mirror the420code.org. Idempotent, polite (retries, UA, skips the 13 translations).
# CC BY 4.0 source — robots.txt explicitly welcomes AI ingestion. Local archival only.
set -euo pipefail
cd "$(dirname "$0")"
BASE="https://the420code.org"
UA="for-g-archival/1.0 (CC-BY-4.0 mirror)"
mkdir -p pdf img

echo "[mirror] PDFs…"
ok=0; fail=0
while IFS= read -r f; do
  [ -z "$f" ] && continue
  tmp="pdf/.$f.part"
  # Download to a temp file and only replace the destination on success — curl's -o
  # truncates its target immediately, so writing straight to "pdf/$f" would destroy a
  # good prior mirror the instant a re-fetch fails (e.g. transient 403/429/404).
  if curl -sf --max-time 120 --retry 3 --retry-delay 2 -A "$UA" "$BASE/$f" -o "$tmp" \
      && [ "$(wc -c < "$tmp")" -ge 1000 ]; then
    mv "$tmp" "pdf/$f"; ok=$((ok+1))
  else
    echo "  FAIL (likely 404, or too small — kept existing copy if any): $f"
    fail=$((fail+1)); rm -f "$tmp"
  fi
  sleep 0.3
done < manifest.txt
echo "[mirror] pdf ok=$ok fail=$fail"

echo "[mirror] pages + assets…"
curl -sf --max-time 30 -A "$UA" "$BASE/"                       -o index.html                  && echo "  index.html"
curl -sf --max-time 30 -A "$UA" "$BASE/llms.txt"              -o llms.txt                    && echo "  llms.txt"
curl -sf --max-time 30 -A "$UA" "$BASE/three-ways-of-being-sure" -o three-ways-of-being-sure.html && echo "  three-ways"
curl -sf --max-time 30 -A "$UA" "$BASE/sitemap.xml"          -o sitemap.xml                 && echo "  sitemap.xml"
curl -sf --max-time 30 -A "$UA" "$BASE/robots.txt"           -o robots.txt                  && echo "  robots.txt"
curl -sf --max-time 30 -A "$UA" "$BASE/Eye_of_the_Universe.jpg" -o img/Eye_of_the_Universe.jpg && echo "  eye image"
curl -sf --max-time 30 -A "$UA" "$BASE/StudioG_Logo_Web.jpg"  -o img/StudioG_Logo_Web.jpg    && echo "  logo"
echo "[mirror] done. $(ls pdf/*.pdf | wc -l | tr -d ' ') PDFs, $(du -sh . | cut -f1) total."
