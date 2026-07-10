---
title: Video Companion Review Manifest
doc_type: normative
version: 0.1 (Working Draft — partial)
status: not yet built from a formal review; one real rule captured from a production incident
owner: Brian
last_updated: 2026-07-08
purpose: Content-type-specific review checks for video companion pages and transcripts — extends docs/01, does not replace it.
used_by: [Claude, ChatGPT, human reviewer]
depends_on: [docs/01-Editorial-Standards.md, docs/03-Review-Format.md]
referenced_by: []
---

# Review Manifest — Video Companion

## Status

Not yet built from a formal review — per this repo's own discipline (see root `README.md`, "Adding a new document"), manifests should grow from real cases, not invented ones. This file exists as a placeholder carrying the one rule already proven in production, so it isn't lost before the rest gets built.

## What's already known (validated 2026-07-07)

- **VIDEO-TRANSCRIPT-LITERAL** — a "Video Transcript" block must remain a verbatim transcription of what was actually spoken in the recording, even after the surrounding page's figures are updated (e.g., a rate change). Never insert updated information into the transcript itself — add a clarifying note *before* the video embed instead. Caught and reverted on post 5555 during the 2026-07-07 rate refresh (see `CHANGELOG.md`) after a subagent rewrote transcript sentences to include rates that were never actually spoken. **Corollary, validated 2026-07-09 (post 8017):** before the video is actually recorded, the details block should be labeled "Video Script," not "Video Transcript" — "Transcript" implies a verbatim record of something already spoken, which isn't true yet at draft stage. Relabel to "Video Transcript" only once the recording is final and the block has been checked against what was actually said.
- **CORNERSTONE-COMPANION-VIDEO** (see `reviews/monday-cornerstone-review.md`) — a video companion page is a separately gate-checkable artifact from its parent blog post, not covered by reviewing the blog post alone.
- **VIDEO-CONSISTENCY** — added 2026-07-09, prompted by ChatGPT's second-pass review of post 8015 / video 8017. Claude's first-round fixes corrected the parent blog post's legal/procedural framing (the withholding calculation, the law-vs-standard-form-vs-company-policy labeling, the unsourced "law requires this disbursement order" claim) but left the companion video's body, key-takeaways list, and script carrying the old, now-incorrect framing. A companion video is drafted from the same source facts as its blog post but is a separate set of blocks — a revision to one does not propagate to the other automatically. **Rule: whenever a parent blog post is revised after review, the companion video (body copy, key takeaways, resources, and script/transcript) must be rechecked line-by-line for the same claims, not just spot-checked.** This is a distinct failure mode from `GATE-ANECDOTE-INTEGRITY` or `GATE-LEGAL-ACCURACY` on a single asset — it's a drift check across paired assets.

## Not yet built

Full structural checks: script length, CTA placement, caption/SRT requirements, and the HeyGen "we, never I" voice rule referenced in `skills/thursday-tip.md`. Build once a real video script goes through a full review.
