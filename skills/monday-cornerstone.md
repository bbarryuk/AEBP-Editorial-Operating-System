---
skill_name: aebp-monday-cornerstone
implementation: Claude skill, packaged and installed in Cowork
sync_status: PARTIALLY WIRED — see note at bottom
last_synced: 2026-07-14
---

# Skill: Monday Cornerstone

## Purpose

Builds the week's main blog post, its companion video page, the Google Business Profile post, and — as of 2026-07-14 — the cornerstone video's social distribution. This is the anchor content everything else that week (Thursday Tip) links back to. WWYD's Tuesday/Wednesday social slot was discontinued 2026-07-14 (underperforming per Brian's own FB/IG analytics review); Monday's social step below replaces it rather than adding to it — the goal is two solid weekly social touchpoints (Monday + Thursday), not three mediocre ones.

## Inputs

Week's assigned topic from the content calendar. AEBP-specific angle/observation (confirmed with Brian before drafting). Verified facts as needed from `knowledge/`.

## Outputs

- WordPress blog post (native Gutenberg blocks), with In Short box, Key Facts box, AEBP-specific section, comparison table where applicable, FAQ (5 questions), hero image
- Companion video page (custom `video` post type, category "Compliance & Legal")
- GBP post (published directly via the `gbp` MCP connector — though as of 2026-07-13 this is blocked by a `SERVICE_DISABLED` API error at the GCP project level; see `aebp-content-connector-gaps` memory, deliver copy as a fallback until Brian re-enables it)
- **Social distribution of the cornerstone video** (new step — see below)

## Step — Monday social distribution (added 2026-07-14)

Once the cornerstone video is rendered and uploaded to YouTube (same HeyGen pipeline WWYD used — see `reviews/video-review.md` for the render/transcript-literalness rules, they still apply), post it to social with a link back to the main blog post — not the video page — since the blog is the piece meant to rank and convert.

- **Facebook / Instagram — post live via the Meta MCP** (confirmed connected and authenticated 2026-07-14, `meta_health_check` passing). Use `meta_create_video_post` / `meta_publish_instagram_reel` as appropriate. **Confirm with Brian before the first live post of the week** — unlike WordPress drafts, a Meta post goes live immediately with no draft state, so this isn't a "draft and let Brian flip a status later" situation the way blog/video posts are.
- **LinkedIn / X / Nextdoor** — no connected posting MCP as of 2026-07-14; deliver copy for Brian to post manually, same as WWYD did for these platforms.
- **Copy structure:** short hook pulled from the video's own opening line, 2-3 sentences on what the post covers, link to the blog post (with UTM: `utm_source=<platform>&utm_medium=social&utm_campaign=<week>-cornerstone&utm_content=monday-video`). Link placement follows the same rule WWYD used — first comment on FB/IG/LinkedIn (caption links get reach-penalized), inline on X/Nextdoor.
- **Hashtags:** reuse WWYD's Wednesday counts as the working default (Instagram 10–14, Facebook 5–8, LinkedIn 4–6, X 3–4, Nextdoor none) until a Monday-specific pattern is validated over a few weeks.

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
