# Note — unblinding-key sidecar basename (2026-08-11)

`UNBLINDING_KEY_KS-CCC4_1.sha256` carries digest `7482445b…` (correct for
`UNBLINDING_KEY_KS-CCC4_1.md`, matching PROV-CCC.7 and `BUNDLE_MANIFEST.txt`)
but the path *inside* the sidecar still names `UNBLINDING_KEY_KS-CCC4.md`.

Not silently repaired (supersession-only rule). Digest and manifest are the
load-bearing checks; this note flags the sidecar basename mismatch for the
next provenance erratum (PROV-CCC.8 territory).
