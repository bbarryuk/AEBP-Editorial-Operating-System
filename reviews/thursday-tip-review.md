---
title: Thursday Tip Review Manifest
doc_type: normative
version: 0.1 (Working Draft)
status: drafted, prompted by ChatGPT's informal (non-OpSys) review of post 8006
owner: Brian
last_updated: 2026-07-08
purpose: Content-type-specific review checks for the weekly Thursday Tip package (blog post, email, video script, social) — extends docs/01, does not replace it.
used_by: [Claude, ChatGPT, human reviewer]
depends_on: [docs/01-Editorial-Standards.md, docs/03-Review-Format.md]
referenced_by: [skills/thursday-tip.md]
---

# Review Manifest — Thursday Tip

## Scope

Applies in addition to every `GATE-*` and `SCORE-*` category in `docs/01`. This manifest exists because a Thursday Tip's job is narrower and more specific than a cornerstone post's, and generic application of `docs/01` alone doesn't catch Thursday-Tip-specific failure modes — which is exactly what happened when post 8006 got reviewed with no manifest at all and no stated mode (see `docs/03` `REVIEW-MODE`, added the same day this manifest was, in direct response).

## Structural checks (beyond docs/01)

- **TIP-NARROW-QUESTION** — the post answers exactly one narrow, specific question, not a broad topic. "What counts as an emergency repair?" passes; "What do landlords need to know about repairs?" fails — that's cornerstone scope, not Thursday Tip scope. If a draft is trying to cover more than one question, it's the wrong format, not a length problem.
- **TIP-MICRO-CASE-STUDY** — the tip is framed as a brand-specific micro-case-study (a situation AEBP actually encountered, or a scenario grounded in AEBP's own portfolio and service area), not generic landlord advice restated in AEBP's voice. A tip that could have been published by any property management company's blog with a find-and-replace of the company name fails this check.
- **TIP-EXTRACTABLE-STRUCTURE** — answer-first: the direct answer appears in the first 1–2 sentences, followed by supporting structure (Key Facts box, table, or checklist) an AI answer engine or a skimming reader can extract without reading the full post.
- **TIP-FRESHNESS-JUSTIFIED** — if the post claims 2026-specific relevance ("new for 2026," "as of 2026," a year in the title), it states *what actually changed* to justify that claim — a rate, a rule, a deadline. A "2026" claim with no stated change is a `GATE-LEGAL-ACCURACY`-adjacent fail: not because the underlying content is wrong, but because the freshness claim itself is unverifiable as written.

These four checks come directly from AEBP's standing content framework (Brian's AI-era SEO guidance, applied site-wide) — they're captured here first because this is where the gap surfaced, but `TIP-EXTRACTABLE-STRUCTURE` and `TIP-FRESHNESS-JUSTIFIED` apply just as much to cornerstone posts and probably belong in `docs/01` directly once validated across more than one content type. Logged as a `docs/03` `FIND-TYPE` Type C system-gap follow-up, not resolved in this pass.

## Status

v0.1 — built 2026-07-08 in direct response to ChatGPT's informal review of post 8006. Re-run against the next Thursday Tip before calling this v1.0.
