---
skill_name: aebp-monday-cornerstone
implementation: Claude skill, packaged and installed in Cowork
sync_status: NOT YET WIRED — see note at bottom
last_synced: 2026-07-07
---

# Skill: Monday Cornerstone

## Purpose

Builds the week's main blog post, its companion video page, and the Google Business Profile post — the anchor content everything else that week (WWYD social, Thursday Tip) links back to.

## Inputs

Week's assigned topic from the content calendar. AEBP-specific angle/observation (confirmed with Brian before drafting). Verified facts as needed from `knowledge/`.

## Outputs

- WordPress blog post (native Gutenberg blocks), with In Short box, Key Facts box, AEBP-specific section, comparison table where applicable, FAQ (5 questions), hero image
- Companion video page (custom `video` post type, category "Compliance & Legal")
- GBP post (published directly via the `gbp` MCP connector)

## Standards required

- `docs/01-Editorial-Standards.md` — answer-first structure, evidence standard, confidence levels, gated Legal/Local Accuracy, FAQ requirement
- `docs/02-Brand-Voice.md` — not yet written

## Documents referenced

- `knowledge/company/overview.md` — verified company facts, fees, service area
- `knowledge/llms.txt` — fallback/raw source

## Known tool-specific rules (currently live in the skill, not yet in `/docs`)

- `mwai_image` defaults to square; must explicitly request landscape
- `wp_create_post` more reliable than `create_posts` for large bodies; tags must be set in a separate call
- Video posts always use category ID 629 regardless of blog post category
- GBP posting is live (account/location IDs in the skill); local MCP server's OAuth token needs periodic re-auth (see `gbp-token-expiry-check` scheduled task)

## Sync status: not yet wired

As of 2026-07-07, this manifest documents what the installed `aebp-monday-cornerstone` Cowork skill does — it does **not** yet mean the skill reads this repo at draft time. The skill's own `SKILL.md` currently still encodes the standards inline (that's the duplication this repo exists to eliminate). Rewiring the skill to reference `docs/01-Editorial-Standards.md` and `knowledge/company/overview.md` directly, instead of repeating those rules, is a follow-up task — flag it to Brian before assuming it's done.
