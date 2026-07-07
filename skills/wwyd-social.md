---
skill_name: aebp-wwyd-social
implementation: Claude skill, packaged and installed in Cowork
sync_status: PARTIALLY WIRED — see note at bottom
last_synced: 2026-07-07
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

## Standards required

- `docs/01-Editorial-Standards.md` — confidence levels apply to any legal/regulatory detail referenced in a scenario (notice periods, grace periods, deposit rules); frame scenarios as illustrative, never as a specific real client case

## Documents referenced

- `knowledge/company/overview.md` and `docs/01-Editorial-Standards.md` §6 (Confidence Levels) — now read at draft time for any legal/regulatory detail in a scenario.
- Still no `knowledge/laws/` — several past scenarios hinge on statutory details (e.g. grace period clocks) that should eventually be checked against a maintained laws file rather than the content calendar or memory. Worth prioritizing once the laws knowledge folder exists, especially given the pending Aug 1 rent-cap changes flagged in `knowledge/llms.txt`.

## Sync status: partially wired (as of 2026-07-07)

**Now reads from this repo:** `knowledge/company/overview.md` and the Confidence Levels section of `docs/01`, with a fallback to the content calendar/existing posts if the repo isn't connected.

**Still inline, not yet migrated:** the Hook→Tension→Decision→Insight→CTA framework and platform-specific rules (hashtag counts, link placement, SMS timing) — these are template/behavior content with no home in `/docs` yet. A future `docs/05-Content-Structure.md` or a `templates/` entry is the natural destination once validated.
