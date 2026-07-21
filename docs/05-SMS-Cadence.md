---
title: SMS Cadence — Mailchimp Mechanics, Weekly Templates, and Governance
doc_type: normative
version: 0.1
owner: Brian
last_updated: 2026-07-20
purpose: Single source of truth for AEBP's weekly SMS touchpoints — when they go out, what they say, and the Mailchimp-specific mechanics that shape the copy. Referenced by any skill that produces SMS content (aebp-monday-cornerstone, aebp-thursday-tip) rather than duplicated in each.
used_by: [Claude, ChatGPT]
---

# SMS Cadence

## Why this file exists

WWYD's Tuesday/Wednesday pair was the only SMS touchpoint AEBP had. When WWYD was discontinued (2026-07-14, underperforming per Brian's own FB/IG analytics review), SMS was cut along with it — not a deliberate decision, just a side effect. Brian flagged the gap on 2026-07-20 and asked for a replacement. Rather than reviving a standalone SMS effort, this follows the same discipline already applied to social that week: attach the touchpoint to an anchor content piece that already exists, don't invent new content to fill a slot.

## The cadence: two texts a week, tied to the two anchor posts

- **Monday — Cornerstone Alert.** Same day the cornerstone blog post goes live. Teases the post, no resolution, just enough to earn the click.
- **Thursday — Tip SMS.** A one-line compression of that week's already-distilled Thursday Tip post. Since the Thursday Tip skill already produces a distilled, single-idea version of the week's content, the SMS is a further compression of something that exists — not new drafting.

No Tuesday/Wednesday SMS — that was WWYD-specific and doesn't carry over.

## Mailchimp mechanics (confirmed 2026-07-20 against a real draft in Brian's account)

- **Mailchimp auto-appends "Text STOP to opt out."** Do not add a manual STOP/opt-out line to the drafted copy — it would double up. This satisfies the TCPA requirement automatically; it isn't optional courtesy copy, it's the compliance mechanism, and Mailchimp is already handling it.
- **Mailchimp's built-in link shortener preserves UTM parameters.** A full UTM'd URL pasted into the SMS composer gets shortened to an `AEBP.mssg.io/...`-style link, but the underlying destination (visible on hover, per the composer's own status bar) still carries the full query string. Paste the full UTM URL as normal — don't hand-shorten it or strip the UTM params to save characters; Mailchimp does that work.
- **Segment length:** budget for 2 SMS segments (up to ~306 characters including the shortened link and the auto-appended STOP footer) as the normal case for a message with a link. Don't force it into a single 160-character segment at the cost of clarity — 2 segments is standard here, not a failure.
- **Audience/list segment:** which Mailchimp SMS list/segment these send to hasn't been confirmed in this repo yet — check with Brian before the first real send rather than assuming it matches the email list.

## Templates

### Monday Cornerstone Alert

Structure: one-line hook naming the topic, one sentence on what the guide actually covers (the two or three most concrete things, not a vague teaser), the link.

Example (Week 4, "Switching Property Managers"):

> AEBP Landlord Update: Switching property managers this year? New guide covers the tenant notice CA law requires + the deposit handoff most owners miss. Read here: [full UTM URL]

UTM pattern: `utm_source=sms&utm_medium=text&utm_campaign=<month><year>-week<N>&utm_content=monday-alert`

### Thursday Tip SMS

Structure: the single practical takeaway in one line (pulled from the Thursday Tip post's own hook — don't re-derive it from the cornerstone post directly), the link back to the Thursday Tip post.

Template:

> AEBP Landlord Tip: [one-line practical takeaway]. Full tip: [full UTM URL]

UTM pattern: `utm_source=sms&utm_medium=text&utm_campaign=<month><year>-week<N>&utm_content=thursday-tip`

## Governance

Same approval rule as every other content type in this system: draft the copy, confirm the specific message with Brian before it actually sends. Mailchimp's own compose/review flow is a natural gate here (Brian sends manually), but that doesn't substitute for confirming wording — a reviewed draft can still say the wrong thing.

## Which skills use this

- `skills/monday-cornerstone.md` — Monday Cornerstone Alert, alongside the existing Step 8 (Monday social distribution).
- `skills/thursday-tip.md` — Thursday Tip SMS, alongside the existing Step 5 (social posts).

Both skill files are a read-only cache in Cowork sessions and can't be edited directly from a session — Brian adds the cross-reference to each skill himself via Settings → Capabilities; this file is what they'd point to.

## Change log

- 2026-07-20: Created. WWYD's SMS touchpoint (Tuesday/Wednesday, scenario + resolution, no link on Tuesday) is the precedent for "SMS as plain text, not HTML" and "confirm before send," but the two-text weekly cadence above is new — it replaces WWYD's SMS rather than extending it. Mailchimp mechanics (STOP auto-append, UTM-preserving shortener) confirmed against a real compose-screen screenshot in Brian's account.
