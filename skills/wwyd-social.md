---
skill_name: aebp-wwyd-social
implementation: Claude skill, packaged and installed in Cowork
sync_status: PARTIALLY WIRED — see note at bottom
last_synced: 2026-07-08
---

# Skill: WWYD Social

## Purpose

Builds the linked Tuesday scenario post and Wednesday resolution post across Facebook, Instagram, LinkedIn, X, Nextdoor, and SMS, using the Hook→Tension→Decision→Insight→CTA framework.

## Inputs

That week's WWYD scenario from the content calendar (usually specified alongside the week's blog topic).

## Outputs

- Tuesday: Hook→Tension→Decision only, per platform, no resolution, no blog link
- Wednesday: Hook→Insight→Twist→CTA, blog link in first comment (FB/IG/LinkedIn) or inline (X/Nextdoor)
- SMS for both days (never Thursday)

## Link target — promote this week's new content, not the best topical match

**Rule, added 2026-07-08 after Brian caught a real instance of this:** the Wednesday resolution's CTA link exists to drive traffic to *that week's* new content — normally the Monday cornerstone post, occasionally another piece of new content published that week — not to whichever existing post is the closest topical match to the scenario. A WWYD scenario about a 3-Day Notice will often have a more precise legal-topic match sitting in the archive (e.g., a dedicated eviction-notice-requirements guide) — that archival post is still the right place to *source* the legal facts in the resolution, but it is the wrong CTA destination. Promotion goal and citation accuracy are two separate decisions:

- **Citation** (which post/source backs the legal claim) — pick whatever is most accurate, archival or not.
- **CTA link** (where the "full breakdown" / "learn more" click actually goes) — always this week's new post, bridged to the scenario with a sentence connecting the two (e.g., "this is exactly the kind of thing a property manager tracks for you — see what that role actually covers: [this week's post]") rather than forcing an unrelated non-sequitur.

If the scenario and the current week's new post don't have an obvious natural bridge, write one deliberately rather than defaulting to the topically-closer archival link — that default is the mistake this rule exists to prevent. See `tests/legal/TEST-LEGAL-003.md`'s sibling case (not itself a legal-accuracy issue, so not logged there) for the real instance that prompted this: Week 2's Wednesday resolution originally linked to post 6614 (an eviction-notice guide) instead of post 7938 (that week's actual new cornerstone post, "What Does a Property Manager Actually Do?").

## Standards required

- `docs/01-Editorial-Standards.md` — confidence levels apply to any legal/regulatory detail referenced in a scenario (notice periods, grace periods, deposit rules); frame scenarios as illustrative, never as a specific real client case

## Documents referenced

- `knowledge/company/overview.md` and `docs/02-Evidence-and-Sourcing.md` (EVD-CONFIDENCE-LEVELS) — now read at draft time for any legal/regulatory detail in a scenario.
- `knowledge/laws/eviction-notice-timing.md` — added 2026-07-08, closing the gap this file previously flagged. Covers grace-period-is-a-lease-term, CCP §§1161–1162 day-count rules, and the residential partial-payment waiver rule (*Woodman Partners v. Sofa U Love* (2001) 94 Cal.App.4th 766). Check this file for any future scenario touching notice timing, day-counting, or partial-payment acceptance rather than re-deriving from memory or the content calendar. Still carries one open Type C flag internally (the "no statutory serving deadline" claim needs a stronger case citation before it's more than professional-opinion confidence) — see the file's own "Type C flag" section.
- `knowledge/laws/rent-caps.md` — for any scenario touching AB 1482, Oakland RAP, Berkeley AGA, or Richmond AGA figures.

## Sync status: partially wired (as of 2026-07-08)

**Now reads from this repo:** `knowledge/company/overview.md`, `knowledge/laws/eviction-notice-timing.md`, `knowledge/laws/rent-caps.md`, and the Confidence Levels section of `docs/01`, with a fallback to the content calendar/existing posts if the repo isn't connected.

**Still inline, not yet migrated:** the Hook→Tension→Decision→Insight→CTA framework and platform-specific rules (hashtag counts, link placement, SMS timing) — these are template/behavior content with no home in `/docs` yet. A future `docs/05-Content-Structure.md` or a `templates/` entry is the natural destination once validated.
