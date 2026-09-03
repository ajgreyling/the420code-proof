# Receipt — AP47 lock attestation, 2026-09-03

**From AJ's hand:** `AP47_AJ_bundle_v2_LOCKED_2026-09-03.zip` (Downloads), delivered by Studio G with
`AP47_LOCK_DECLARATION.md`, attesting a lock the declaration dates to 1 September 2026.

## What actually authorizes this lock

Not the declaration on its own. `AP47_LOCK_DECLARATION.md` is Studio G's account of a private
session this repo has no independent access to — real evidence of intent, but third-party
attestation, not the author's own word given directly to the verifier. Per this repo's standing
rule (the same one that held AP47 at "pending lock" through the 3 September freeze anchor), a
third party's account of the author's word does not substitute for the author's word.

**What actually closes it:** AJ Greyling, asked directly and plainly whether the walk described in
the declaration matches his own memory and whether he personally stands behind locking AP47,
answered: **"yes lock."** That direct confirmation, not the declaration's own say-so, is the
event this anchor is dated to and authorized by.

## Verified before acting on it

- `SHA256SUMS.txt` (v2 bundle): all entries verified `OK`.
- **AP47_The_Flip_FINAL_v3's hash is byte-identical to the version received and independently
  verified on 1 September and 3 September** (md `6e7fe6486a16…`, docx `070b0d81b51e…`) — the paper
  itself has not changed. Only the attestation and status documents are new.
- **A factual error found and corrected, not silently accepted:** `POST_LOCK_STATUS_ANNEX.md` cites
  "AP45 FINAL v1.6" (`2e95321d…`) and "AP46 FINAL v1.4" (`0a510d26…`) as what was locked 2 September.
  Those hashes are real but wrong — they're superseded drafts. What was actually locked, verified
  and anchored by this repo on 2 September, is **AP45 FINAL v1.7** (`f4453adb…`) and **AP46 FINAL
  v1.5** (`b1102a43…`), per `FREEZE_REGISTER_AP45_AP46_2026-09-02.md`'s own text and this repo's own
  `ap45-ap46-locked-2026-09-02` tag. The annex's citation error does not touch AP47's own lock — the
  paper it describes as locked (FINAL v3) is correctly hashed throughout — but it is flagged here
  because an attestation bundle getting a checkable detail wrong, on a detail unrelated to what it
  is asking to be trusted on, is exactly the kind of thing this repo's discipline exists to catch,
  not wave through.

## What is anchored

Artist's Proof 47, "The Flip," FINAL v3 (md `6e7fe6486a16…`, docx `070b0d81b51e…`) — **LOCKED**, at
the author's own direct confirmation, 2026-09-03. Kill switches KS-FLIP.1–4 now armed from this
lock; KS-30.2 remains inherited, live in its parent (AP30); KS-NPP.1 remains fired, shown forever,
not repaired by this or any paper.

Stored under `lock-2026-09-03-ap47/`: the lock declaration, the post-lock status annex (with the
correction above standing beside it, per house rule — nothing edited, only corrected in the open),
and the v2 README.

## Effect on prior anchors

`ap47-freeze-anchor-2026-09-03` (the receipt/provenance anchor made earlier the same day) is not
superseded or removed — it stands as the record of when the bundle was first received and
independently verified. This lock anchor is the separate, later step the freeze anchor's own commit
message said would follow "once he's walked it."
