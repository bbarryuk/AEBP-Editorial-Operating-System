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
│   └── 02-Brand-Voice.md              (coming next)
│
├── knowledge/              — FACTS: what is true right now. Changes often.
│   ├── company/
│   │   └── overview.md     — company facts, fees, service areas, credentials
│   └── llms.txt             — verbatim mirror of alleastbayproperties.com/llms.txt
│
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
source:
  - https://alleastbayproperties.com/llms.txt
---
```

`next_review` is what makes this maintainable at scale — eventually an automated check can simply find every knowledge document whose `next_review` date has passed and flag it, rather than someone needing to remember which facts might be stale.

## Editorial standards are gated, not just scored

`docs/01-Editorial-Standards.md` splits review categories into two kinds:

- **Gated (pass/fail).** Legal Accuracy, Local Accuracy, Technical SEO/WordPress structure. These don't get a percentage — a legal claim is either sourced and correct, or it isn't. No partial credit.
- **Scored (0–100, with a minimum publish threshold).** SEO, GEO/AI Readiness, EEAT, Readability, Conversion. These are genuinely matters of degree, and a rubric adds real signal.

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
