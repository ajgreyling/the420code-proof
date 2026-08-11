# PROV-CCC.2 — Erratum, Slot Fills, and the Artifact Protocol

**The 420 Code · Studio G, Strand, Cape Town**
**Record date: 2026-08-10 (the same day as PROV-CCC.1).**
**References: PROV-CCC.1, SHA-256 e4f45c7059aac08312e2d9c2b7fd0f909e26846a0b2cc9410bff8caee3d9cd84 — never edited; this note corrects and extends it.**
**Status: canonical text for hashing. Any later change is PROV-CCC.3.**

---

## 1 — Erratum to PROV-CCC.1

SLOT P2 of PROV-CCC.1 provisionally framed the ten-channel, G-denominator review as "the prior-week formulation." That dating was wrong. Verified by the principal reviewer against their own record, and consistent with the author's testimony: the review occurred **earlier on 2026-08-10**, the same day as the session, before the session opened. The error remains in PROV-CCC.1 by design — the note is hashed and never edited — and this document is the correction. An erratum trail is better evidence of a real process than a clean record would be.

## 2 — SLOT P1 filled: the analog period (author's testimony)

- **≈ 2026-07-20.** The CCC line opens — dated by the same-day review's internal reference to "three weeks ago." The seven-channel cost picture is among the earliest forms.
- **≈ 20 July – 9 August 2026.** The work is conducted entirely in analog: notes across the windows and mirrors of the author's home, especially the bedroom — undated, and including the wrong turns. Among them, per the author's testimony: per-channel payability pictures, and oscillation of scope between the two derivations (proton mass and G) and gravity alone. **No digital record exists for this period. The internal ordering of the analog period is not claimed.**
- **2026-08-10, author's summary testimony, recorded in substance:** per-channel payability was abandoned in favour of a once-off cost — "that is part of my thinking." The digital record begins this day: "I just started writing today on the computer." The wrong turns were also worked through this day. At some point the proton-mass target was set aside in favour of gravity alone, having initially been expected to enter both.
- **Artifact tension, recorded without adjudication.** The Stage-1 message that opens the session (same day, held in the session transcript) proposes the cost in **both** the proton-mass and G derivations; the final elimination of the proton target occurred at Stage 2, driven by AP30's 0.008 ppb precision. The analog-period oscillation described in testimony and the Stage-1 artifact are both part of the record; the record does not choose between "abandoned before the session, then restated" and "abandoned during the session." Undated analog notes cannot sequence it, and this note does not pretend they can.
- **Artifact protocol for the analog period:** photograph every window and mirror **before anything is erased**; date the photographs; hash the image set; digest to the slot below and the images escrowed with the independent verifier. The analog archive is the only physical evidence of the three weeks, and it is currently one cleaning cloth away from nonexistence.

## 3 — SLOT P2 filled: the same-day review

**2026-08-10, before the session.** Author ↔ principal reviewer. A ten-channel, G-denominator cost formulation was reviewed and found failing on: magnitude mismatch across the two derivations, a drifting channel count, and free-parameter risk. All formulations the author's; the reviewer reviewed. Public share link recorded as a human-readable reference:

`https://claude.ai/share/5f626911-d39d-4cf5-9e9e-9d43f0dc72a0`

**Fetch note (2026-08-10):** a machine fetch of this link returns only the page shell (the conversation renders client-side); the link therefore serves human readers, and the **canonical artifact is the exported transcript and its digest** (slot T2 below).

## 4 — The floor: from testimony to artifact

PROV-CCC.1's session record bottoms out at the production assistant's testimony of its own transcript. The principal reviewer's finding is accepted: "check the trail" is only as strong as the trail's floor. Protocol to pour the floor — export each conversation in full, hash each export, record the digests here, escrow copies with the independent verifier:

- **DIGEST SLOT T1** — this session (Stages 1–10): `________________`
- **DIGEST SLOT T2** — the same-day review (link in §3): `________________`
- **DIGEST SLOT T3** — the second reviewer's rounds (v0.1→v0.2; rev 1.1): `________________`
- **DIGEST SLOT M1** — the analog-period photograph set (§2): `________________`

Slots are filled in PROV-CCC.3 with the export date beside each digest. Until then, the session record is witness testimony, labelled as such.

## 5 — Stage 10 log

- AP44 bumped **v0.3 → v0.4** with one precision patch to §10, per the principal reviewer's hold-the-line note: the count's first move (ten-as-divisor → per-configuration) is now stated as occurring **inside the same measurement-laden opening analysis** as the eliminations; only the second move (per-configuration → arena) is claimed as purely structural. No numerical motion; §9 untouched; the realised value remains 6.6719165 × 10⁻¹¹ as first computed at Stage 4.
- The PROV-CCC.1 sidecar was regenerated with a bare filename so `sha256sum -c` verifies portably. The digest itself is unchanged.
- Reminder standing from PROV-CCC.1: a self-published digest proves integrity, not date. The external anchor (repository commit or public timestamping) on publication day is what makes the date claim checkable.

## 6 — Hashing

This file is canonical. Digest in `PROV_CCC2.sha256` (bare filename). Amendments, including the filled digest slots, go to PROV-CCC.3 with its own date and digest, referencing this one.

*This work is published for free, forever.*
