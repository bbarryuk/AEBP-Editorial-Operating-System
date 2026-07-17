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
- **Social distribution of the cornerstone video** (new step — see Step 8)

## Step 6 — Companion video page

Once the blog post exists, build its companion video page as a separate WordPress post using the custom `video` post type:
- Slug pattern: `/videos/{slug}/` (or the equivalent short slug matching the blog post's topic)
- Category: always ID 629 ("Compliance & Legal"), regardless of the blog post's own category
- Template: `_wp_page_template` meta set to `video-post-no-hero-with-sidebar`
- Structure: intro paragraph, the `[lite_youtube videoid="..." title="..."]` shortcode (as its own `wp:shortcode` block), "What This Video Covers" list, a body section restating the post's key points in the video's own words, "Key Takeaways" list, "Resources Mentioned" list (linking back to the blog post and any other relevant pages), a CTA block, and a `wp:details` block labeled **"Video Script"** (not "Video Transcript") containing the full spoken script.

**The blog post itself should also embed the video**, not just the separate video page — add a video section (shortcode + a `wp:details` "Video Transcript"/"Video Script" block, same labeling rule as below) positioned logically in the post body, matching the established site pattern. Don't treat the video page as the only place the video lives.

**Script vs. transcript labeling:** before the video is actually recorded, label the details block "Video Script" — it's the intended text, not a confirmed record of what was said. Once HeyGen's render is complete, cross-check the actual spoken audio (via the SRT sidecar or the render output) against the written script. If they match, relabel to "Video Transcript." If the actual recording diverged from the script in any way that changes a fact, update the written text to match what was actually said, not the other way around — this is the same `VIDEO-TRANSCRIPT-LITERAL` rule the video-review manifest enforces, and getting it backwards (editing a transcript to say something that wasn't actually spoken) is a harder mistake to catch later.

**If a parent blog post is revised after a review pass, recheck the companion video line-by-line for the same claims** — body copy, key takeaways, resources, and script/transcript are separate blocks from the blog post and don't update automatically when the blog post does. This is `VIDEO-CONSISTENCY` in `reviews/video-review.md`, added after this exact drift happened on a real post.

## Step 7 — GBP post

Publish via the `gbp` MCP connector once the blog post's real (bare, non-"dev.") production URL is live — GBP posts should link to `alleastbayproperties.com`, not the `dev.` subdomain used for drafting. As of 2026-07-13 the connected GBP MCP is blocked by a `SERVICE_DISABLED` Google My Business API error at the GCP project level (a console setting only Brian can toggle) — verify with a real `gbp_create_post` call each session rather than assuming it's fixed, and if it's still blocked, deliver the finished post copy (text + image URL + CTA link with UTM) for Brian to paste in manually instead of promising automated posting.

## Step 8 — Monday social distribution (added 2026-07-14, updated 2026-07-14 to add X)

Once the cornerstone video is rendered (HeyGen) and uploaded to YouTube, post it to social with a link back to the **main blog post** — not the video page — since the blog is the piece meant to rank and convert.

**See `docs/04-Social-Publishing.md` for current connector status and the approval rule — check it each session rather than trusting this list, since Brian is actively connecting new platforms (LinkedIn is next).** As of 2026-07-14: Facebook/Instagram post live via the Meta MCP, X posts live via `x-write` (text only — no media upload tool exists yet, so an X post can carry a link but not an attached video/image), LinkedIn is not yet connected, Nextdoor stays copy-only indefinitely.

- **Confirm the specific post content with Brian before calling any live-posting tool, every time** — these are direct-publish with no draft state, unlike the WordPress posts above. Don't post speculatively even if the general plan was approved earlier.
- **Copy structure:** a short hook pulled from the video's own opening line, 2-3 sentences on what the post covers, a link to the blog post with UTM tracking (`utm_source=<platform>&utm_medium=social&utm_campaign=<week>-cornerstone&utm_content=monday-video`). Link placement: first comment on Facebook/Instagram/LinkedIn (caption links get reach-penalized by those platforms' algorithms), inline in the post text on X/Nextdoor. On X, since there's no media attachment yet, write the post so the link itself carries the video/blog reference rather than reading as incomplete without an image.
- **Hashtags:** working default (not yet Monday-specific validated) — Instagram 10–14, Facebook 5–8, LinkedIn 4–6, X 3–4, Nextdoor none.

## Step 9 — Verify against the editorial repo before calling it done

Before treating the package as complete, re-check the finished post (and its companion video) against `docs/01-Editorial-Standards.md`'s gated categories (Legal Accuracy, Local Accuracy, Technical SEO, Compliance Risk, Anecdote Integrity) and, if a review has been requested, follow the format in `docs/03-Review-Format.md`. Don't skip this because the content "looks right" — several real incidents in this repo's history (fabricated anecdotes, gross-vs-net tax miscalculations, video/blog drift after a revision) all happened despite the draft reading as plausible on a first pass.

## Standards required

- `docs/01-Editorial-Standards.md` — answer-first structure, evidence standard, confidence levels, gated Legal/Local Accuracy, FAQ requirement
- `docs/02-Brand-Voice.md` — not yet written
- `docs/04-Social-Publishing.md` — connector status and the live-posting approval rule (Step 8)

## Documents referenced

- `knowledge/company/overview.md` — verified company facts, fees, service area
- `knowledge/llms.txt` — fallback/raw source

## Known tool-specific rules (currently live in the skill, not yet in `/docs`)

- `mwai_image` defaults to square; must explicitly request landscape
- `wp_create_post` more reliable than `create_posts` for large bodies; tags must be set in a separate call via `wp_add_post_terms` using term IDs (don't trust `tags_input` or a tag-whitelist doc against the live site)
- Video posts always use category ID 629 regardless of blog post category
- GBP posting mechanics (account/location IDs) are in Step 7 above; currently blocked at the API level, see that step
- HeyGen render/upload/YouTube pipeline mechanics (avatar verification, render polling, the render-to-YouTube local-file handoff) are the same ones documented in `skills/wwyd-social.md` — that file is discontinued as a content type but its tooling notes are still accurate and worth reading before a render
- `wp_alter_post`'s search string must byte-match the live content exactly — re-fetch via `wp_get_post_snapshot` before constructing it, and pass search/replace text as plain parameter values, not wrapped in CDATA (CDATA has been observed to silently strip `<!-- -->` HTML comment delimiters, causing false "no occurrences found" errors)

## Sync status: partially wired (as of 2026-07-14)

**Now reads from this repo:** verified company facts (`knowledge/company/overview.md`) and the Evidence Standard / Confidence Levels (`docs/02-Evidence-and-Sourcing.md`) at draft time, with an inline fallback only if the repo folder isn't connected that session. The skill also now runs a standards-gate check against `docs/01`'s gated-vs-scored categories before calling a draft done (Step 9).

**Still inline, not yet migrated:** the actual post structure (In Short box → Key Facts box → body → AEBP-specific section → comparison table → CTA → FAQ) and the Monday social distribution copy structure — both template-level detail with no home in the repo yet. Also still inline: WordPress/image/GBP/Meta/X/YouTube tool mechanics (these are legitimately skill-owned, not editorial standards, so no migration needed there) — except connector status and the approval rule, which now live in `docs/04-Social-Publishing.md`.

**Next migration candidate:** once `templates/cornerstone-blog.md` exists and has been validated against a real post, move the structure checklist there and have the skill read it the same way it now reads `docs/01`.
