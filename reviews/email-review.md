---
title: Email Review Manifest
doc_type: normative
version: 0.1 (not yet built)
status: placeholder — no Mailchimp email has been through a formal review yet
owner: Brian
last_updated: 2026-07-08
purpose: Content-type-specific review checks for the weekly Thursday Tip email (Mailchimp HTML) — extends docs/01, does not replace it.
used_by: [Claude, ChatGPT, human reviewer]
depends_on: [docs/01-Editorial-Standards.md, docs/03-Review-Format.md]
referenced_by: [skills/thursday-tip.md]
---

# Review Manifest — Email

## Status

Placeholder. No email has gone through a formal `docs/03` review yet — build this from the first real case.

## Known constraint worth capturing now

The connected Mailchimp MCP cannot create actual campaign drafts (confirmed via its own `get_capabilities` tool) — the working process is delivering populated HTML for manual paste into Mailchimp's "Code Your Own" editor, not a temporary gap expected to close. Any review checklist built here should assume that hand-off point, not assume direct campaign creation.

## Known open questions to resolve when this gets built

- Subject line / preview text requirements (length limits, whether they need their own citation-free "hook" standard separate from the blog post's).
- Whether `GATE-COMPLIANCE-RISK` (docs/01) needs an email-specific reading, given emails address "you" more directly than a blog post does.
