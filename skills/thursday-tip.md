---
skill_name: aebp-thursday-tip
implementation: Claude skill, packaged and installed in Cowork
sync_status: PARTIALLY WIRED — see note at bottom
last_synced: 2026-07-07
---

# Skill: Thursday Tip

## Purpose

Builds the weekly Thursday Tip package — a WordPress blog post, Mailchimp email HTML, HeyGen video script, and social posts — as a distillation of that week's already-published Monday cornerstone post.

## Inputs

That week's published cornerstone blog post (prerequisite — this skill doesn't originate a topic). Brian's approval of the proposed tip angle before drafting proceeds.

## Outputs

- WordPress draft post (native Gutenberg blocks): hook/rule/consequence, AEBP micro-case-study, pull quote, action steps, takeaway, link back to the cornerstone post
- Mailchimp email HTML (delivered as a file for manual paste — the connected Mailchimp MCP can't create campaign drafts directly)
- HeyGen video script (locked avatar/voice/format specs)
- Social posts for 5 platforms, graphic + video versions

## Standards required

- `docs/01-Editorial-Standards.md` — evidence standard and confidence levels apply directly to the micro-case-study (real figures or clearly hypothetical, never fabricated as a specific client story)
- `docs/02-Brand-Voice.md` — not yet written; HeyGen script "we," never "I," is a brand-voice rule currently living only in the skill

## Documents referenced

- `knowledge/company/overview.md` — for any AEBP fact used in the micro-case-study or takeaway
- Tag whitelist (currently only in the skill body — should move to a `knowledge/website/tags.md` once that file exists)

## Sync status: partially wired (as of 2026-07-07)

**Now reads from this repo:** `knowledge/company/overview.md` for facts used in the micro-case-study, and `docs/01-Editorial-Standards.md` §5–6/§10 for the Evidence Standard, Confidence Levels, and the pass/fail Legal Accuracy gate — with an inline fallback if the repo isn't connected that session.

**Still inline, not yet migrated:** the tag whitelist, HeyGen script structure and "we, never I" rule, Adobe Express/Mailchimp mechanics. The tag whitelist should move to `knowledge/website/tags.md` once that file exists; the brand-voice rules belong in `docs/02-Brand-Voice.md` once it's written.
