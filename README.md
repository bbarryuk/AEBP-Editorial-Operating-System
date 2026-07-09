# AEBP Editorial Operating System

The editorial brain for All East Bay Properties' content — the standards, facts, and templates every AI collaborator (Claude, ChatGPT, and whatever comes next) draws on so that a blog post, a Thursday Tip, a social caption, and a video script are all recognizably the product of the same company, written to the same bar, regardless of which model produced the first draft.

## Why this exists

Brian produces a lot of recurring content for AEBP — weekly cornerstone blog posts, Thursday Tips, social scenario posts, video scripts — using Claude (via packaged skills in Cowork) to draft and ChatGPT to review. Before this repository existed, the editorial rules for that content lived in two disconnected places: prose instructions inside Claude's skills, and a series of chat conversations with ChatGPT that weren't captured anywhere durable. That meant no single place either model could check to answer "is this actually how AEBP does things," and no way to update a rule once and have it apply everywhere it should.

This repo fixes that by being the **single source of truth**. It doesn't replace the Claude skills or ChatGPT's review process — it's what they both read from.

```
        AEBP Editorial Operating System
                      │
        ┌─────────────┼──────────────┬────────────────────┐
        │             │              │                    │
   Claude Writer  ChatGPT Reviewer  (future)          (future)
                                  WordPress Publisher  Social Adapter
```

## How each AI should use this repo

**Claude** drafts content through packaged Cowork skills (see `/skills` for what's currently built). Before drafting, a skill should read the relevant files in `/docs` (standards) and `/knowledge` (facts) rather than relying on rules baked into the skill's own instructions — the skill is the *mechanism*, this repo is the *authority*. If a skill's behavior and this repo's standards disagree, this repo wins, and the skill should be updated to match.

**ChatGPT** reviews drafts against `/docs` (which categories are gated pass/fail vs. scored, and the minimum thresholds in `docs/01-Editorial-Standards.md`) and checks factual/legal claims against `/knowledge`. Until an automated pipeline exists, this happens by pasting the relevant doc(s) and the draft into a ChatGPT conversation.

**Anyone else** (a future model filling the Reviewer or Publisher role, or a human collaborator) should be able to clone this repo and understand how AEBP produces content without any conversation history — that's the actual test of whether a document belongs here.

## Repository structure

```
AEBP-Editorial-Operating-System/
├── README.md              — this file: entry point, philosophy, how to navigate
├── CHANGELOG.md           — what changed in each version
├── LICENSE                — usage terms (see note in that file)
│
├── docs/                  — BEHAVIOR: how to do things. Changes rarely.
│   ├── 01-Editorial-Standards.md
│   ├── 02-Evidence-and-Sourcing.md
│   ├── 03-Review-Format.md
│   └── 04-Brand-Voice.md              (coming next)
│
├── knowledge/              — FACTS: what is true right now. Changes often.
│   ├── company/
│   │   └── overview.md     — company facts, fees, service areas, credentials
│   ├── laws/                — rent caps, notice timing, and other verified legal reference
│   └── llms.txt             — verbatim mirror of alleastbayproperties.com/llms.txt
│
├── reviews/                 — content-type-specific review manifests that EXTEND docs/01,
│                              never replace it. One file per content type (cornerstone,
│                              thursday-tip, wwyd, social, email, video, schema). Built from
│                              real reviews as they happen, not invented in advance — most
│                              of these currently exist as placeholders for that reason.
│
├── tests/                   — editorial regression suite: real cases logged from real reviews
├── templates/              — (coming later) per-content-type structural templates
├── automation/              — (coming later) API workflows, JSON schemas, prompt chains
└── skills/                  — manifests describing each Claude skill: purpose, inputs,
                               outputs, which docs/knowledge files it depends on
```

Two folders carry the whole philosophy:

- **`docs/` is behavior.** How to review for legal accuracy. How to score SEO. What counts as an FAQ. These change rarely, and only when AEBP's actual editorial judgment changes.
- **`knowledge/` is facts.** The management fee percentage. Which cities are served. What a statute currently says. These change whenever the business or the law changes, independent of any editorial decision.

Keeping these separate means updating a fee doesn't require touching a standards document, and updating a standard doesn't require re-verifying every fact in the company profile.

## Knowledge documents carry metadata

Every file in `/knowledge` starts with YAML frontmatter:

```yaml
---
title: Company Overview
owner: Brian
last_verified: 2026-07-06
next_review: 2026-08-06
review_frequency: monthly
authority: Internal
confidence: Verified
review_method: Manual
source:
  - https://alleastbayproperties.com/llms.txt
---
```

`next_review` is what makes this maintainable at scale — eventually an automated check can simply find every knowledge document whose `next_review` date has passed and flag it, rather than someone needing to remember which facts might be stale. `review_frequency`/`authority`/`confidence`/`review_method` exist so that same future automation knows not just *when* to check a document but *how* — a `Manual`/monthly company-facts doc gets handled differently than something that could eventually be checked automatically against a live source.

## Documents declare their dependencies

Every file in `/docs` opens with a frontmatter block naming its `purpose`, who/what `used_by` it (Claude, ChatGPT, human reviewer, automation), what it `depends_on`, and what `referenced_by` it — a lightweight dependency graph. When a standard changes, this is how you find out what else needs to change with it, without searching the whole repo by hand.

## Rules carry stable IDs

Individual rules within `/docs` carry mnemonic IDs (`STD-HONEST`, `GATE-LEGAL-ACCURACY`, `EVD-SOURCE-HIERARCHY`) rather than section numbers, specifically so a review can cite "violates GATE-LEGAL-ACCURACY" durably — inserting a new rule later doesn't renumber anything, unlike sequential numbering would.

## Normative vs. informative documents

Every document declares a `doc_type` in its frontmatter:

- **Normative** — defines a requirement; a draft that violates it isn't ready to publish. `docs/01-Editorial-Standards.md` and `docs/02-Evidence-and-Sourcing.md` are normative.
- **Informative** — provides context, facts, or examples, but isn't itself a rule to check a draft against. `knowledge/company/overview.md` is informative.

Keeping these distinct matters once the repo has more documents: a reviewer (human or AI) should be able to tell at a glance whether a document is something to cite as a violation, or something to read for background.

## Planned, not yet built

A few things are intentionally deferred rather than forgotten:

- **A glossary** — canonical one-line definitions for recurring terms (Cornerstone, Thursday Tip, WWYD, GEO, EEAT, Confidence Level, Review Gate) so wording doesn't drift across documents. Worth doing once there are enough documents that drift has actually started, not preemptively.
- **`automation_ready` knowledge metadata** — flagged as a good future field once there's an actual automation step that would read it. Adding a field with undefined semantics now would create more confusion than it resolves.

`/tests` is no longer on this list — it's built and growing (`tests/legal/TEST-LEGAL-001` through `003`, plus a new `tests/editorial/` category started 2026-07-08 with `TEST-EDITORIAL-001` for non-legal content-integrity failures, logged from real reviews and incidents as they happened). `/reviews` is also now built, following the same "grow from real cases" discipline: most of its files are still placeholders for content types that haven't had a real review yet.

## Editorial standards are gated, not just scored

`docs/01-Editorial-Standards.md` splits review categories into two kinds:

- **Gated (pass/fail).** Legal Accuracy, Local Accuracy, Technical SEO/WordPress structure (including internal linking), Compliance Risk. These don't get a percentage — a legal claim is either sourced and correct, or it isn't. No partial credit.
- **Scored (0–100, with a minimum publish threshold).** SEO, GEO/AI Readiness, EEAT, Readability, Conversion. These are genuinely matters of degree, and a rubric adds real signal.

This split has been proposed for replacement twice now — once as a Critical/Major/Minor severity scale, once as a universal 10-gate pass/fail rubric — and held both times. See `docs/03-Review-Format.md`, "Round two, 2026-07-08," for the reasoning.

## Versioning

This repo versions like software, not like a manual. A document is a working draft (v0.1) until it's been used on real AEBP content and refined based on what that use revealed. It becomes stable (v1.0) once it's held up across multiple real posts, not because a fixed amount of writing time has passed.

```
v0.1  — Editorial Standards drafted, Company Overview knowledge doc live
v0.2+ — refined against real posts (Brand Voice, Legal Accuracy, SEO/GEO added)
v1.0  — validated across ~25 real posts, stable
v2.0  — automation: Claude API + ChatGPT API + GitHub-PR publishing pipeline
```

We are not building the v2.0 automation pipeline yet. The process gets validated by hand first; automation should only ever execute a process that's already been proven, not stand in for figuring the process out.

## Adding a new document

1. Decide: is this behavior (`docs/`) or fact (`knowledge/`)? If it's a fact, add YAML frontmatter with an honest `next_review` date.
2. Keep it focused — roughly 1,500–3,000 words. Smaller, single-purpose documents are easier for both AIs to load and easier for Brian to maintain than one large manual.
3. If it changes how a Claude skill should behave, update that skill's manifest in `/skills` so the dependency is visible, and flag to Brian that the actual Cowork skill may need updating too (this repo doesn't automatically change what's installed in Cowork).
4. Tag a version in `CHANGELOG.md` once the document has actually been used on real content, not before.
