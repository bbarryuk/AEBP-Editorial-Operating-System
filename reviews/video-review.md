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

- **VIDEO-TRANSCRIPT-LITERAL** — a "Video Transcript" block must remain a verbatim transcription of what was actually spoken in the recording, even after the surrounding page's figures are updated (e.g., a rate change). Never insert updated information into the transcript itself — add a clarifying note *before* the video embed instead. Caught and reverted on post 5555 during the 2026-07-07 rate refresh (see `CHANGELOG.md`) after a subagent rewrote transcript sentences to include rates that were never actually spoken.
- **CORNERSTONE-COMPANION-VIDEO** (see `reviews/monday-cornerstone-review.md`) — a video companion page is a separately gate-checkable artifact from its parent blog post, not covered by reviewing the blog post alone.

## Not yet built

Full structural checks: script length, CTA placement, caption/SRT requirements, and the HeyGen "we, never I" voice rule referenced in `skills/thursday-tip.md`. Build once a real video script goes through a full review.
