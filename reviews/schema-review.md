---
title: Schema Review Manifest
doc_type: normative
version: 0.1 (not yet built)
status: placeholder — schema.org markup practice not yet audited across published posts
owner: Brian
last_updated: 2026-07-08
purpose: Content-type-agnostic review checks for structured data (schema.org markup) on published posts — extends docs/01's GATE-TECHNICAL-SEO, does not replace it.
used_by: [Claude, ChatGPT, human reviewer]
depends_on: [docs/01-Editorial-Standards.md, docs/03-Review-Format.md]
referenced_by: []
---

# Review Manifest — Schema

## Status

Placeholder. `docs/01`'s `GATE-TECHNICAL-SEO` already says "schema present where applicable," but this repo hasn't yet audited what schema AEBP's WordPress setup (Yoast) actually emits by default versus what needs to be added manually — an FAQ block's `aebp-faq` markup may or may not produce valid `FAQPage` schema without additional work. Before this manifest can be built for real, that needs to be checked directly against a published post's rendered HTML, not assumed.

## Known open questions to resolve when this gets built

- Does the `aebp-faq` block pattern emit `FAQPage` schema automatically via Yoast, or does it need explicit JSON-LD?
- `Article` schema completeness (author, datePublished, dateModified) — Yoast default vs. AEBP-specific needs.
- Whether `LocalBusiness`/`RealEstateAgent` schema is set once site-wide or needs per-post attention.
