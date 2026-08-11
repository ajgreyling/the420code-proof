# PROV-CCC.4 — The Floor Poured: Export Digests, the Analog Archive, and the Escrow Protocol

**The 420 Code · Studio G, Strand, Cape Town**
**Record date: 2026-08-10 (late evening).**
**References: PROV-CCC.1 (e4f45c70…d9cd84), PROV-CCC.2 (59f650df…cf58b39f), PROV-CCC.3 (82a84b44…371c24e) — never edited.**
**Status: canonical text for hashing. Amendments go to PROV-CCC.5.**

---

## 1 — Slots T1 and T2: filled

The author supplied two platform data exports, one per account, made minutes apart late on 10 August. Each was inspected mechanically; the target conversation was located by content and extracted verbatim as a standalone JSON artifact. **The record's floor is now artifact, not testimony**, exactly as the reviewer demanded.

**T1 — the production thread** (this record's Stages 1–10; the thread that produced AP44 and WP-CCC.1):
- Conversation UUID `9d47f86b-ab95-4a58-9821-978fe6c1bcc2`; **created 2026-08-10 17:27:29; export snapshot at 21:08:55**; 31 messages at snapshot.
- Extracted artifact: `T1_production_thread_conversation.json` — **SHA-256 9066410d4f8daa8f50cfbfe93aaba2e63426e4c067ad7b1dcf8ea5563a11ba10**
- Source export (escrow only): `data-23ef5494-…-batch-0000.zip` — SHA-256 7b3c7abf80983af01e7ac827b35e27bae885632a729a698f02ec310ac80bcec7
- **Snapshot caveat:** the export precedes the session's final exchanges (the transcript upload, PROV-CCC.3–4, AP44 v0.5, WP rev 1.3). A post-session export fills slot **T1-final** in PROV-CCC.5. Everything after the snapshot is meanwhile evidenced by the artifacts themselves and their digests.

**T2 — the reviewer thread:**
- Conversation UUID `0a07d72e-0bdc-407f-9b9f-f5caee6a7835`; **created 2026-08-10 17:32:27; export snapshot at 20:51:48**; 18 messages.
- Extracted artifact: `T2_reviewer_thread_conversation.json` — **SHA-256 19930ed96c4832704f82c8d7e65df161485c2ad37771fe4d7cccc1fa67b30515**
- Source export (escrow only): `data-bd55f3ff-…-batch-0000.zip` — SHA-256 b71e35b50cf120c46eca7c5d904a1f2587a8869e567a9b8b8de061be90323300

**Clock ordering, now established by artifact.** PROV-CCC.3 §2 stated the ordering of the two openings was not established. The export metadata establishes it: **the production thread opened at 17:27:29, the reviewer thread at 17:32:27 — four minutes and fifty-eight seconds later.** Both threads received the same opening message; the parallel design stands as recorded; CCC.3's statement was accurate when made and is improved, not corrected, here.

## 2 — Slot M1a: the analog archive, first tranche

Three photographs of the bedroom mirror, taken 2026-08-10 at 23:16, supplied and hashed:

- `WhatsApp_Image_2026-08-10_at_23_16_55.jpeg` — SHA-256 676f638e16250b51c974ea5368fdbae7f60200af14d05fa7df5e9be123fc78be
- `WhatsApp_Image_2026-08-10_at_23_16_56.jpeg` — SHA-256 6ea15ee0d0f57e7cabb226ee68b0992deac0ecbc7640081f2f5397b8b2c27462
- `WhatsApp_Image_2026-08-10_at_23_16_56__1_.jpeg` — SHA-256 6559f19fdccf0354aff8cd8b4e6f0ff64a995979b9c0e9f48947077dd0092acb

**Legibility note, stated conservatively.** The marker writing is partially legible (mirror-reversed in places, overwritten in others). Legible without strain, and corroborating the testimony of PROV-CCC.2 §2: the decomposition **"6 faces / 3 AS / + 1 R"** — the ten-vertex reading; the line **"leakage = +1×ε"**; repeated **coupling-cost** phrasing ("coupling cost", "cost relative to faces", "each B force carries a cost"); **"Defrag/Defragmentation"** language in several places — direct physical corroboration of the seven-channel picture (one visible plus six defragmentation channels, ≈ 20 July) that the reviewer thread's Exchange 1 dates and describes; and fraction sketches (1/21 beside "Persistent", 10/10, 1/2, sf/20) consistent with the wrong turns the testimony names. The photographs show the thinking including its errors, uncleaned — which is their entire evidentiary value. **Slot M1b** (the systematic morning set, all rooms, raking light, a date-bearing object per room) remains open for PROV-CCC.5.

## 3 — Escrow protocol and a required author ruling

**The raw export zips must never be published.** They contain, beyond the two target conversations: account memories, login history, project files, and in one case an unrelated conversation. They go to **private escrow only** — the author retains them; the independent verifier holds private copies; their digests (above) are public so escrow integrity is checkable without disclosure.

**Public artifacts** are the two extracted conversation files. One flag before they go public, requiring the author's explicit ruling: **T1 contains a personal message** (the production thread's Exchange 10, on the author's emotional state). Options, both honest: (a) publish T1 as-is; (b) publish a redacted public variant with the redaction openly marked, the unredacted file remaining in escrow under the digest above — so the redaction itself is verifiable. Neither option touches the physics record. Until the ruling, T1's extracted file travels to the verifier privately; its digest is public now either way.

## 4 — Author-supplied items still owed to the archive

Superseded drafts v0.1–v0.4 of AP44 (the author's downloaded copies — the build environment retained only the current version); the reviewer thread's execution file `Appendix_C_Execution_The_Leakage_Discriminator_v0_1.md`; the reviewer thread's reconstructed transcript as a saved file. Digests on the author's copies, to PROV-CCC.5.

## 5 — Standing

With T1, T2, and M1a filled: every stage of the session record is now backed by a hashed artifact; the pre-session analog period is backed by testimony, the reviewer thread's contemporaneous references, and a growing photographic archive. The remaining openings are named (T1-final, M1b, §4's items), each with its slot. The first repository commit anchors all of it externally.

*This work is published for free, forever.*
