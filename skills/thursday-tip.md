---
skill_name: aebp-thursday-tip
implementation: Claude skill, packaged and installed in Cowork
sync_status: PARTIALLY WIRED — see note at bottom
last_synced: 2026-07-08
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
- Social posts for 5 platforms, graphic + video versions — **see `docs/04-Social-Publishing.md` for current connector status.** As of 2026-07-14, Facebook/Instagram and X can be posted live (Meta MCP and `x-write` respectively — X is text-only, no media upload tool yet); LinkedIn isn't connected yet, Nextdoor stays copy-only. Same rule as everywhere else these connectors are used: confirm the specific post with Brian before calling a live-posting tool, every time — these publish immediately with no draft state.

## Standards required

- `docs/01-Editorial-Standards.md` — evidence standard and confidence levels apply directly to the micro-case-study (real figures or clearly hypothetical, never fabricated as a specific client story). Specifically `GATE-ANECDOTE-INTEGRITY` — before drafting the "AEBP observation" this skill's Step 1 requires, confirm a real example exists (ask Brian) or fall back to a sourced general fact / explicitly-flagged hypothetical instead. Added 2026-07-08 after this exact skill produced a fabricated anecdote in post 8006 and its HeyGen script; see `docs/02-Evidence-and-Sourcing.md`'s `EVD-ANECDOTE-INTEGRITY` and `tests/editorial/TEST-EDITORIAL-001.md`.
- `docs/02-Brand-Voice.md` — not yet written; HeyGen script "we," never "I," is a brand-voice rule currently living only in the skill

## Documents referenced

- `knowledge/company/overview.md` — for any AEBP fact used in the micro-case-study or takeaway
- Tag whitelist (currently only in the skill body — should move to a `knowledge/website/tags.md` once that file exists)

## Sync status: partially wired (as of 2026-07-07)

**Now reads from this repo:** `knowledge/company/overview.md` for facts used in the micro-case-study, and `docs/02-Evidence-and-Sourcing.md`, and `docs/01-Editorial-Standards.md`'s `GATE-LEGAL-ACCURACY` for the Evidence Standard, Confidence Levels, and the pass/fail Legal Accuracy gate — with an inline fallback if the repo isn't connected that session. As of 2026-07-08, also `GATE-ANECDOTE-INTEGRITY` / `EVD-ANECDOTE-INTEGRITY` — the micro-case-study step must not proceed with an invented "we've done X" claim.

**Still inline, not yet migrated:** the tag whitelist, HeyGen script structure and "we, never I" rule, Adobe Express/Mailchimp mechanics. The tag whitelist should move to `knowledge/website/tags.md` once that file exists; the brand-voice rules belong in `docs/02-Brand-Voice.md` once it's written.
