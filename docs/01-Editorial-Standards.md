---
title: Editorial Standards
doc_type: normative
version: 0.3 (Working Draft)
status: drafted, validated against two real reviews (post 7996 Monday Cornerstone, post 8006 Thursday Tip)
owner: Brian
last_updated: 2026-07-08
purpose: Defines the editorial philosophy, audience, principles, and publish-readiness gates for all AEBP educational content.
used_by: [Claude, ChatGPT, human reviewer]
depends_on: [docs/02-Evidence-and-Sourcing.md]
referenced_by: [docs/03-Review-Format.md, reviews/*.md, skills/monday-cornerstone.md, skills/thursday-tip.md, skills/wwyd-social.md]
---

# Document 01 — Editorial Standards

## Purpose

This document defines the editorial standards for all educational content published by All East Bay Properties: blog posts, guides, FAQs, landing pages, video scripts, email newsletters, and social posts.

The objectives:

Publish the most accurate landlord education content available for the East Bay. Build long-term topical authority with Google and AI-powered search engines. Demonstrate expertise without overwhelming readers with legal jargon. Help landlords make informed decisions while recognizing that every situation is unique. Position All East Bay Properties as the trusted local authority for property management, leasing, and real estate services in Oakland, Berkeley, Emeryville, and the surrounding East Bay.

**Evidence and sourcing rules live in `docs/02-Evidence-and-Sourcing.md`, not here** — this document covers philosophy, principles, and the publish-readiness gate; that one covers what counts as sufficient proof for a claim.

## STD-PHILOSOPHY — Editorial Philosophy

Every piece of content educates first and sells second. Readers should leave every article with actionable knowledge regardless of whether they become clients. Sales are earned through demonstrated expertise, not promotional language. Content answers the reader's question completely before introducing company services.

## STD-AUDIENCE — Audience

Primary: DIY landlords, small portfolio investors, accidental landlords, out-of-state property owners, real estate investors considering East Bay rentals. Secondary: existing property management clients, prospective home sellers, rental applicants, investors researching the local market. Assume readers have little or no legal training.

## Editorial Principles

**STD-ACCURATE.** Legal statements verified per `docs/02-Evidence-and-Sourcing.md` whenever possible.

**STD-PRACTICAL.** Readers understand exactly what to do next. Avoid theory without application.

**STD-LOCAL.** Reflect Oakland, Berkeley, Emeryville, and Alameda County specifically wherever appropriate. Avoid generic "California landlord" examples when a local one would serve better.

**STD-EVERGREEN.** Avoid unnecessary references to current events or dates unless legally required. Write so the article stays valuable after publication with minimal updates.

**STD-HONEST.** No exaggerated claims. Never imply certainty where the law allows discretion. Words like *always*, *never*, *guaranteed*, *required* are used only when legally accurate (see `EVD-CONFIDENCE-LEVELS` in `docs/02`).

## STD-QUALITY-QUESTIONS — Quality Standards

Every article should answer: what is this, why does it matter, who does it apply to, what should the reader do, what mistakes should be avoided, and when should professional advice be sought instead.

## STD-READER-EXPERIENCE — Reader Experience

Content should be easy to scan, mobile-friendly, conversational, written around an 8th–10th grade reading level while preserving legal accuracy, free of unnecessary repetition, broken into short sections, and visually organized with headings, lists, tables, and callouts.

## STD-TRUST-SIGNALS — Trust Standards

Readers should always be able to tell the difference between California law, local ordinance, industry best practice, company recommendation, and opinion or interpretation. The article signals which is which, using the Confidence Levels defined in `docs/02-Evidence-and-Sourcing.md`.

## Review Categories

Categories split into two kinds, deliberately. A legal claim is either sourced and correct or it isn't — scoring it as "92% accurate" invents precision that doesn't exist. A readability judgment genuinely is a matter of degree, and a numeric rubric adds real signal there.

### Gated (pass/fail — no partial credit)

| ID | Category | Passes when |
|---|---|---|
| GATE-LEGAL-ACCURACY | Legal Accuracy | Every legal claim verified per `docs/02-Evidence-and-Sourcing.md`, confidence level labeled, nothing blocked per `EVD-BLOCK-PENDING-VERIFICATION` |
| GATE-LOCAL-ACCURACY | Local Accuracy | Local ordinance details verified against current source (`/knowledge`), city-specific examples used where relevant |
| GATE-TECHNICAL-SEO | Technical SEO / WordPress | Valid Gutenberg blocks (no classic/HTML dump), schema present where applicable, meta fields set, and required internal links present (at minimum: a link to the jurisdiction-specific deep-dive guide when this post only summarizes it, and a link to `/lets-talk/` or another live conversion path) |
| GATE-COMPLIANCE-RISK | Compliance Risk | Content stays in general education and doesn't cross into individualized legal advice — no telling a specific reader what they personally must do, no "your situation requires X," no answering as if the reader's facts are known. General statements of what the law requires, framed per `STD-HONEST`, are not advice; a direct instruction addressed to "you" about a hypothetical reader's specific facts is. |

A gated category that fails blocks publication outright, regardless of how well the article scores elsewhere.

`GATE-COMPLIANCE-RISK` added 2026-07-08, prompted by ChatGPT flagging it as a gap in its review of the Thursday Tip skill's output — see `CHANGELOG.md`. Internal-linking requirement folded into `GATE-TECHNICAL-SEO` the same day rather than made a fifth gate, since it's a mechanical presence check rather than a distinct evaluative judgment.

### Scored (0–100, minimum threshold to publish)

| ID | Category | Minimum to publish |
|---|---|---|
| SCORE-SEO | SEO | 90 |
| SCORE-GEO | GEO / AI Search Readiness | 95 |
| SCORE-EEAT | EEAT | 95 |
| SCORE-READABILITY | Readability | 90 |
| SCORE-CONVERSION | Conversion | 85 |
| SCORE-OVERALL | Overall | 95 |

Thresholds are a working draft (v0.1) — expect to adjust them once tested against real published posts.

## STD-SUCCESS-METRIC — Success Metric

The measure of success is not whether an article ranks. It's whether a landlord receives a complete and accurate answer, the content becomes a trusted citation for AI systems, readers gain confidence in AEBP's expertise, and the article naturally encourages qualified prospects to reach out.

## STD-OUT-OF-SCOPE — Out of Scope

This document does **not** define:

- Evidence, sourcing, or citation rules — `docs/02-Evidence-and-Sourcing.md`
- How a review is structured, classified, and written up — `docs/03-Review-Format.md`
- Brand voice, tone specifics, or the "we, never I" HeyGen rule — `docs/04-Brand-Voice.md` (not yet written)
- SEO/GEO tactical implementation (keyword research, schema specifics) — a future SEO/GEO document, not yet written
- WordPress publishing mechanics (Gutenberg block conventions, tag whitelist, image generation) — currently owned by the individual Claude skills; may migrate to `templates/` or an automation doc later
- Post/scenario structure templates (In Short box order, Hook→Tension→Decision→Insight→CTA framework) — belongs in `templates/`, not yet written

If a rule doesn't fit one of the documents above and doesn't have an obvious future home, that's a signal it may not belong in the Editorial Operating System at all — see the versioning discipline in the root `README.md`.

## Status

This is v0.3 (revised 2026-07-08 to add `GATE-COMPLIANCE-RISK` and fold internal-linking into `GATE-TECHNICAL-SEO`, both prompted by ChatGPT's review of the Thursday Tip skill's output). Validated against two real posts so far (7996, 8006). The scored-category thresholds are still current best guesses, not calibrated numbers.
