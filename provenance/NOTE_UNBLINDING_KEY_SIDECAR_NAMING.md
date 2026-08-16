# Note — unblinding-key sidecar basename (2026-08-11; disposition 2026-08-16)

`UNBLINDING_KEY_KS-CCC4_1.sha256` carries digest `7482445b…` (correct for
`UNBLINDING_KEY_KS-CCC4_1.md`, matching PROV-CCC.7 and `BUNDLE_MANIFEST.txt`)
but the path *inside* the sidecar still names `UNBLINDING_KEY_KS-CCC4.md`.

**Disposition (PROV-CCC.8 §2):** the digest governs. Verifiers check the stated
digest against the renamed file directly. A re-paired sidecar under the `_1`
basename may be issued with the adoption wave; if issued, it supersedes and both
sidecars are retained. No content of the key is touched.

Not silently repaired before the erratum (supersession-only rule). Digest and
manifest remain the load-bearing checks.
