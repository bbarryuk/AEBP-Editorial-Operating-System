---
title: "TEST-LEGAL-003 — Correct-but-uncited claim caught in social content, not a blog post"
doc_type: informative
owner: Brian
last_verified: 2026-07-08
source_case: WWYD Week 2 Wednesday resolution package (social/video content, not a WordPress post) — drafted 2026-07-08, gate-checked same day once the repo became reachable from the new `C:\Users\brian\repos\AEBP-Editorial-Operating-System` path
---

# TEST-LEGAL-003

Third real entry in the `/tests/legal/` regression suite (see `TEST-LEGAL-001.md` and `TEST-LEGAL-002.md`). Logged from an actual case, not invented.

## Excerpt

From the Facebook/Instagram, X, LinkedIn, Nextdoor, SMS, and HeyGen-script versions of the Wednesday resolution (all six channels carried the same underlying claim):

> "Accepting even a partial payment after you've served the notice can void it and reset the clock to zero."

## Rule IDs triggered

- `GATE-LEGAL-ACCURACY` — **FAIL as originally drafted** (Type B, Evidence Gap)
- `EVD-CITATION-REQUIREMENT` — the claim was reused faithfully from published WordPress post 6614 ("California Eviction Notice Requirements (2026)"), but neither that post nor the new social draft cited an actual source for it.
- `EVD-SOURCE-HIERARCHY` — no `knowledge/laws/` file existed yet to check this claim against at all (Type C, System Gap, compounding the Type B).

## Why this one is instructive

Two things make this case distinct from `TEST-LEGAL-001` (same underlying pattern — a correct claim with no citation):

1. **It's the first case caught in social/video content, not a WordPress blog post.** Every prior real case in this suite came from a long-form article review. This one confirms `GATE-LEGAL-ACCURACY` and `EVD-CITATION-REQUIREMENT` apply with the same force to a Facebook caption, an SMS, and a HeyGen video script as to a blog post — the content type doesn't lower the bar, even though social copy has no visible citation UI (no footnote, no linked source) the way a blog post does. The fix here was to source the claim properly in the *repo* (`knowledge/laws/eviction-notice-timing.md`) and note it in the content package's internal posting notes, even though the public-facing caption itself will never show a citation. The standard is "can this be verified by someone checking the system," not "does the reader see a footnote."
2. **The gap was caught the same day it was created**, immediately after the repo became reachable again (it had been unreachable due to the OneDrive git-lock issue at the time of drafting, so the skill's own inline fallback path was used instead of reading `knowledge/` directly). This is a useful case for `EVD-BLOCK-PENDING-VERIFICATION`: the content wasn't held back from being drafted while the repo was unreachable (correctly — the skill's fallback path exists for exactly this situation), but it also wasn't treated as fully verified until the gate-check happened once the repo came back. Drafting under a fallback and treating that draft as gate-checked are two different states, and this case shows why keeping them distinct matters.

The claim itself turned out to be correct and, once searched for properly, has real backing: *Woodman Partners v. Sofa U Love* (2001) 94 Cal.App.4th 766 establishes that a residential landlord must give a proper nonwaiver notice *before* accepting a partial payment for the acceptance not to waive a previously served notice — a nonwaiver notice given only after the fact doesn't cure it. There's also a scope limit worth preserving: this waiver rule is residential-only; Civil Code §1161.1(c) creates a different, more permissive rule for commercial tenancies. Both details are now captured in `knowledge/laws/eviction-notice-timing.md`.

## Expected verdict

`GATE-LEGAL-ACCURACY` should **FAIL** as originally drafted (claim correct, but uncited anywhere the system could check it — the only "source" was an equally uncited sentence in post 6614). After the fix — creating `knowledge/laws/eviction-notice-timing.md` with the *Woodman Partners* citation and the residential/commercial scope limit, and noting the citation in the content package's posting notes — the gate should **PASS**. No change to the public-facing social copy was required, since none of it overstated the claim.

## What this should catch in the future

If a future skill (Monday cornerstone, Thursday Tip, or a new content type) is reviewed with an implicit assumption that `GATE-LEGAL-ACCURACY` only applies to WordPress posts because that's where the citation UI naturally lives, re-run this case — the gate applies to every content type this Operating System produces, including channels with no visible footnote mechanism at all. Also worth re-checking: any content drafted while this repo was unreachable (OneDrive lock, or any future connectivity gap) should get an explicit gate-check pass once the repo is reachable again, rather than being treated as already-verified just because a skill's inline fallback let drafting proceed.
