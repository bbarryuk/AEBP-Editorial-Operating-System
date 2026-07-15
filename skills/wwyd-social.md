---
skill_name: aebp-wwyd-social
implementation: Claude skill, packaged and installed in Cowork
sync_status: DISCONTINUED — see note below
last_synced: 2026-07-13
discontinued: 2026-07-14
---

## Discontinued 2026-07-14

Brian reviewed FB/IG performance data via a newly connected Meta MCP and found Tuesday/Wednesday WWYD content was underperforming — "falling flat" relative to the rest of the weekly cadence. Decision: drop Tue/Wed WWYD packages entirely rather than keep iterating on the format. Monday's cornerstone now gets its own social distribution step instead (see `skills/monday-cornerstone.md`), and Thursday Tip is unchanged. This file is kept for reference (the framework, the render pipeline, the connector-gap notes are all real work product) but should not be used to build new content unless Brian explicitly revives WWYD. If reviving it, re-check everything below against current tooling before trusting it — connector states and avatar IDs recorded here will have gone stale.

**Also unresolved when this was paused:** the Nextdoor comments on the final WWYD post (July 14 spending-approval scenario) pointed out the illustrative $600 water-heater-replacement figure was unrealistic — real replacement cost is closer to $2,200. The scenario's dollar figures were meant to be illustrative, but this is a case where "illustrative" collided with a fact enough people already know firsthand, which undercut credibility even though engagement (comments) was otherwise healthy. Worth a general lesson for any future scenario writing (WWYD or otherwise): run illustrative repair/cost figures through a plausibility check against real prices, not just against the arithmetic the scenario needs (here, "$100 over a $500 threshold" only worked narratively at $600 — the actual cost didn't need to be that low, the *gap over threshold* did, and that constraint could have been hit with realistic numbers instead).

# Skill: WWYD Social

## Purpose

Builds the full weekly WWYD pair: the Tuesday scenario post (video + social + SMS) and the Wednesday resolution post (social + SMS), using the Hook→Tension→Decision→Insight→CTA framework. As of 2026-07-13, video is a standard part of Tuesday's package, not an optional extra — see Step 4.

## Inputs

That week's WWYD scenario — pulled from the content calendar if one exists there, otherwise proposed by drawing on that week's Monday cornerstone post (the richest source of fresh, on-topic dilemma material) and confirmed with Brian before drafting proceeds.

## Outputs

- Tuesday: HeyGen video short (vertical, ~45-60s) + YouTube upload (title/description/tags) + Hook→Tension→Decision social copy per platform, no resolution, no blog link + SMS
- Wednesday: Hook→Insight→Twist→CTA, blog link in first comment (FB/IG/LinkedIn) or inline (X/Nextdoor) + SMS

## Link target — promote this week's new content, not the best topical match

**Rule, added 2026-07-08 after Brian caught a real instance of this:** the Wednesday resolution's CTA link exists to drive traffic to *that week's* new content — normally the Monday cornerstone post, occasionally another piece of new content published that week — not to whichever existing post is the closest topical match to the scenario. A WWYD scenario about a 3-Day Notice will often have a more precise legal-topic match sitting in the archive (e.g., a dedicated eviction-notice-requirements guide) — that archival post is still the right place to *source* the legal facts in the resolution, but it is the wrong CTA destination. Promotion goal and citation accuracy are two separate decisions:

- **Citation** (which post/source backs the legal claim) — pick whatever is most accurate, archival or not.
- **CTA link** (where the "full breakdown" / "learn more" click actually goes) — always this week's new post, bridged to the scenario with a sentence connecting the two (e.g., "this is exactly the kind of thing a property manager tracks for you — see what that role actually covers: [this week's post]") rather than forcing an unrelated non-sequitur.

If the scenario and the current week's new post don't have an obvious natural bridge, write one deliberately rather than defaulting to the topically-closer archival link — that default is the mistake this rule exists to prevent. See `tests/legal/TEST-LEGAL-003.md`'s sibling case (not itself a legal-accuracy issue, so not logged there) for the real instance that prompted this: Week 2's Wednesday resolution originally linked to post 6614 (an eviction-notice guide) instead of post 7938 (that week's actual new cornerstone post, "What Does a Property Manager Actually Do?").

## Step 4 — Video short + YouTube upload (standard as of 2026-07-13, was previously optional)

HeyGen MCP is connected and functional as of 2026-07-13 (confirmed live via `get_current_user`, `creator` plan, `add_on_credits` available) — video render no longer has to be a manual step or skipped. Every Tuesday scenario gets a vertical short:

- **Format:** 9:16, ~45-60s, 1080p, burned-in captions + SRT sidecar, mp4, voice speed 0.95.
- **Avatar:** dedicated WWYD avatar — confirm current ID before each render rather than trusting a prior session's value; avatar IDs recorded in chat can go stale or belong to a different HeyGen login than the one actually connected (`get_current_user` returns the authenticated account's email — cross-check against that). If the intended avatar isn't found via `get_avatar_look`, fall back to Henry (`69e0fe7567c84a46954a6b4a55fd5290`, digital twin, native portrait, default voice `4f0b1c9da53e47d7a045c238b87303c2`) rather than blocking the week's content, and flag the mismatch to Brian.
- **Script:** same Hook→Tension→Decision beats as the social copy, spoken version, no resolution/Insight — matches Tuesday's "open loop" rule.
- **YouTube upload:** title, description (no post-specific blog link yet — same no-link-on-Tuesday rule as social; a general homepage link with UTM is fine), tags (keep simple/short — multi-word unusual phrases have tripped YouTube's `invalidTags` check before, e.g. "spending approval clause"; prefer 1-2 word tags), `#Shorts` in title or description for Shorts surfacing. Category matches other AEBP video content. Upload as private/unlisted — Brian decides when to flip public, same publishing governance as every other content type.
- **Known gap, confirmed 2026-07-13: the render-to-YouTube handoff isn't automatic yet.** `youtube_upload_video` needs a local file path, but HeyGen only returns signed URLs on `files2.heygen.ai`, which this sandbox's outbound proxy blocks (`curl` confirmed `blocked-by-allowlist`, 403; `web_fetch` separately rejects the long signed URL). Until fixed, give Brian the HeyGen video page link once the render completes — he downloads and re-attaches the mp4, same hand-off he already does for Monday cornerstone videos — then the upload proceeds normally.
- **Captions:** the render includes burned-in captions automatically; the sidecar SRT this generates is for reference/QA (confirm the spoken script matches what HeyGen actually rendered before calling it final, per `VIDEO-TRANSCRIPT-LITERAL` in `reviews/video-review.md`) — YouTube's separate caption-track upload is still a manual step (no MCP tool for it, confirmed 2026-07-08).

## Standards required

- `docs/01-Editorial-Standards.md` — confidence levels apply to any legal/regulatory detail referenced in a scenario (notice periods, grace periods, deposit rules); frame scenarios as illustrative, never as a specific real client case

## Documents referenced

- `knowledge/company/overview.md` and `docs/02-Evidence-and-Sourcing.md` (EVD-CONFIDENCE-LEVELS) — now read at draft time for any legal/regulatory detail in a scenario.
- `knowledge/laws/eviction-notice-timing.md` — added 2026-07-08, closing the gap this file previously flagged. Covers grace-period-is-a-lease-term, CCP §§1161–1162 day-count rules, and the residential partial-payment waiver rule (*Woodman Partners v. Sofa U Love* (2001) 94 Cal.App.4th 766). Check this file for any future scenario touching notice timing, day-counting, or partial-payment acceptance rather than re-deriving from memory or the content calendar. Still carries one open Type C flag internally (the "no statutory serving deadline" claim needs a stronger case citation before it's more than professional-opinion confidence) — see the file's own "Type C flag" section.
- `knowledge/laws/rent-caps.md` — for any scenario touching AB 1482, Oakland RAP, Berkeley AGA, or Richmond AGA figures.

## Sync status: partially wired (as of 2026-07-13)

**Now reads from this repo:** `knowledge/company/overview.md`, `knowledge/laws/eviction-notice-timing.md`, `knowledge/laws/rent-caps.md`, and the Confidence Levels section of `docs/01`, with a fallback to the content calendar/existing posts if the repo isn't connected.

**Still inline, not yet migrated:** the Hook→Tension→Decision→Insight→CTA framework, platform-specific rules (hashtag counts — only formally defined for Wednesday so far, Tuesday's are still an inline default pending confirmation — link placement, SMS timing), and the Step 4 video/YouTube spec table — these are template/behavior content with no home in `/docs` yet. A future `docs/05-Content-Structure.md` or a `templates/` entry is the natural destination once validated.

**Open item:** the WWYD-dedicated HeyGen avatar ID Brian referenced in chat (2026-07-13) did not resolve against the connected HeyGen account — used Henry as a fallback for that week. Needs the correct ID confirmed and recorded here before the next render.
