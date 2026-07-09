---
title: Monday Cornerstone Review Manifest
doc_type: normative
version: 0.1 (Working Draft)
status: drafted, validated against one real post (7996)
owner: Brian
last_updated: 2026-07-08
purpose: Content-type-specific review checks for the weekly Monday cornerstone post, its video companion, and its GBP post — extends docs/01, does not replace it.
used_by: [Claude, ChatGPT, human reviewer]
depends_on: [docs/01-Editorial-Standards.md, docs/03-Review-Format.md]
referenced_by: [skills/monday-cornerstone.md]
---

# Review Manifest — Monday Cornerstone

## Scope

Applies in addition to every `GATE-*` and `SCORE-*` category in `docs/01`, using the write-up format in `docs/03`. This manifest adds structural and package-level checks specific to the cornerstone format — it does not restate or override the base categories, and a QA Review or Pre-Publish Audit (see `docs/03` `REVIEW-MODE`) on a cornerstone post should run both.

## Structural checks (beyond docs/01)

- **CORNERSTONE-STRUCTURE** — post follows: answer-first intro paragraph → Key Facts box (table or callout) → body sections → AEBP-specific observation section (see `CORNERSTONE-AEBP-VOICE`) → "Before You [Act]" checklist → FAQ (5 questions minimum, `aebp-faq` block convention) → Sources section → closing CTA (`cta-primary` group). Missing any of these is a structural fail, logged as Type A per `docs/03` `FIND-TYPE` (violates a standard as currently written), not a style suggestion.
- **CORNERSTONE-AEBP-VOICE** — at least one first-person, AEBP-specific observation that only a practicing East Bay property manager would know (post 7996's "we manage 600+ units... this is the first cycle where the honest answer for one jurisdiction is no" is the validated example). A generic industry observation restated in AEBP's voice does not satisfy this — it has to be drawn from AEBP's own portfolio experience, not something any property management blog could have written with a find-and-replace.
- **CORNERSTONE-COMPANION-VIDEO** — the post's video companion page is a *separate* gate-checkable artifact, not covered by reviewing the blog post alone (see `CHANGELOG.md`, 2026-07-07 — missed once already on posts 7938/7958). Review both URLs independently against the full `docs/01` gate set. See also `reviews/video-review.md`.
- **CORNERSTONE-GBP-CONSISTENCY** — the GBP post's factual claims match the blog post's at time of publish. Not a citation requirement in itself (GBP posts don't carry inline citations), but a factual-drift check: if the blog post states one figure and the GBP post states another, that's a `GATE-LEGAL-ACCURACY` or `GATE-LOCAL-ACCURACY` fail on whichever one is wrong.

## Status

v0.1 — built 2026-07-08, validated against exactly one real post (7996). Re-run against the next Monday cornerstone post before calling this v1.0.
