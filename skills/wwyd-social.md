---
skill_name: aebp-wwyd-social
implementation: Claude skill, packaged and installed in Cowork
sync_status: NOT YET WIRED — see note at bottom
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

- None from `/knowledge` yet directly — scenarios are drawn from the content calendar, not company facts. Worth revisiting once `knowledge/laws/` exists, since several past scenarios have hinged on specific statutory details (e.g. grace period clocks) that should be checked against a maintained source rather than memory.

## Sync status: not yet wired

Same caveat as the other two skills: this manifest documents current behavior; the skill doesn't read this repo yet. Rewiring is a follow-up task.
