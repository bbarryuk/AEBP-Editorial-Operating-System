---
skill_name: aebp-monday-cornerstone
implementation: Claude skill, packaged and installed in Cowork
sync_status: PARTIALLY WIRED — see note at bottom
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

## Sync status: partially wired (as of 2026-07-07)

**Now reads from this repo:** verified company facts (`knowledge/company/overview.md`) and the Evidence Standard / Confidence Levels (`docs/02-Evidence-and-Sourcing.md`) at draft time, with an inline fallback only if the repo folder isn't connected that session. The skill also now runs a standards-gate check against §10's gated-vs-scored categories before calling a draft done.

**Still inline, not yet migrated:** the actual post structure (In Short box → Key Facts box → body → AEBP-specific section → comparison table → CTA → FAQ) — this is template-level detail with no home in the repo yet. It belongs in `templates/cornerstone-blog.md`, which doesn't exist. Also still inline: WordPress/image/GBP tool mechanics (these are legitimately skill-owned, not editorial standards, so no migration needed there).

**Next migration candidate:** once `templates/cornerstone-blog.md` exists and has been validated against a real post, move the structure checklist there and have the skill read it the same way it now reads `docs/01`.
