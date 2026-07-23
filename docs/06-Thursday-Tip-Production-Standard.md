---
title: Thursday Tip Production Standard — Graphic, Email Template, WordPress Structure
doc_type: normative
version: 0.1
owner: Brian
last_updated: 2026-07-22
purpose: The real, verified Thursday Tip production pipeline, reconstructed against actual published examples after the aebp-thursday-tip skill was found to be drafting from a generic structure that didn't match the site. Referenced by the aebp-thursday-tip skill.
used_by: [Claude, ChatGPT]
---

# Thursday Tip Production Standard

## Why this file exists

On 2026-07-22, the Thursday Tip WordPress post, Mailchimp email, and social package were drafted using a plausible-but-invented structure — generic headings, a from-scratch email layout, and category/tag guesses — instead of the site's actual established pattern. Brian corrected this by pointing to real examples: 4 published Thursday Tip posts (7867, 7928, 8006, 8219), 4 example graphics, and the real Mailchimp "Code Your Own" template (`MC-Tip-Email-Template.html`). This file documents the verified pattern so future weeks build from it directly instead of re-deriving it from scratch each time.

**The pipeline has three deliverables that must be built in this order**, because each depends on the one before it:

1. **Graphic text spec** — drafted first. The same graphic gets used in both the email and (as the featured image) the WordPress post.
2. **Mailchimp email** — built from the real template file, using the graphic once Brian has made it.
3. **WordPress post** — built to match the real site structure below.

Brian builds the actual graphic himself (in his own graphic tool) from the text spec — that step isn't automatable here. Same for the final Mailchimp paste and send.

## Step 1: Graphic text spec

The graphic is a single branded card: eyebrow badge, headline, body paragraph, pull quote, series label + date. It's used twice — as the email's hero image, and as the WordPress post's featured image (`PM-Tip-{DD}{Month}{YYYY}.webp`, e.g. `PM-Tip-23July2026.webp`).

Fields to deliver, every week:

- **Eyebrow badge:** always "2026 Landlord Tip" (fixed, confirmed across all 4 examples).
- **Headline:** short, punchy, often a question ("Do You Have 3 Months' Reserve Per Property?") or a direct claim ("Your deposit clock starts when they leave — not when the lease ends").
- **Body paragraph:** **keep to ~200–220 characters.** One of the 4 real examples ran long and got visibly cut off mid-sentence in the actual graphic ("...catches an") — the template has no overflow handling, so this is a hard budget, not a style preference.
- **Pull quote:** the same pull-quote used in the blog post and email, no attribution, bold italic in the graphic.
- **Series label + date:** e.g. "Owner ROI Series · July 23, 2026." **There is no formal list of series names** — known ones so far are "Owner ROI Series" and "Move-Out Series." Ask Brian for the right one each week rather than inventing a new one; add it to this list once confirmed.

## Step 2: Mailchimp email

Built from `MC-Tip-Email-Template.html` (Brian's real "Code Your Own" template — get the current copy from him if it's not already in this repo). Do not build the email from scratch; populate a copy of this template.

The template has exactly 6 weekly-edit points, each marked `<!-- ✏️ UPDATE: ... -->` in the HTML:

1. Header meta — date (auto via Mailchimp merge tag, don't touch) + series tag (`<span class="header-tag">`).
2. Greeting blurb — one sentence naming this week's topic, using Mailchimp's `*|FNAME|*` merge tag.
3. Section 1 "2026 Landlord Tip" — `.tip-card` body copy (2 short paragraphs), an optional `.city-table` (remove entirely if the topic has no per-city/tiered data — don't force one in), and an optional `.warning-note` callout.
4. Section 2 "This Week's Thursday Tip" — `.weekly-tip-text` (the main pull-quote/takeaway line) + `.tip-footnote` (one supporting sentence).
5. Section 3 "Want to Learn More" — `.learn-card-headline`, `.learn-card-desc`, the CTA button URL (UTM-tagged, `utm_source=mailchimp&utm_medium=email&utm_campaign=<week>-thursdaytip&utm_content=cta-button`), and `.series-note`.
6. The `<!-- #### IMAGE PLACEHOLDER #### -->` block — empty in the raw template. Populate it with the `.graphic-block`/`.graphic-caption` markup (CSS classes already defined) and a placeholder `src` — Brian swaps in the real Mailchimp-hosted image URL after he uploads the graphic from Step 1.

Deliver the fully populated HTML as a file, same as before — the connected Mailchimp MCP can't create campaign drafts, so this is always a manual paste into "Code Your Own." **Always include Subject Line + Preview Text** alongside the file.

## Step 3: WordPress post — verified structure

Reconstructed from posts 7867, 7928, 8006 (8219 is a one-off deviation — flatter markup, no group wrappers — treat it as a regression, not a variant to follow).

**Fixed elements, every post:**

- Title: `Thursday Tip: [The/Your + specific hook]`.
- Author: Jason Crouch (user ID 1).
- Category: **"Landlord Tips & Compliance Insights" (term_id 716)** — not any other category. Set as Yoast primary category too.
- Tags: "Property Management" (167) always, plus topic-relevant tags — "California Rental Law" (649) for legal/compliance angles, "Security Deposits" (201) for deposit topics, "Move-In & Move-Out" (708) for turnover topics.
- Featured image: `PM-Tip-{DD}{Month}{YYYY}.webp`, same file as the email graphic.
- Manually written excerpt, 💡-prefixed, 1–2 sentences (don't leave it to auto-generate from body text — 2 of the 4 real posts skipped this and it shows).

**Section order (each section is its own `wp:group` with `className: "container"`, `padding: preset|spacing|10`, containing one `H3` with an `anchor` id):**

1. **Hook section** — 💡-prefixed H3, then 1–3 short paragraphs delivering the specific rule/stat/surprising fact.
2. **"What We See at AEBP" section** — H3 with anchor `h-what-we-see-at-aebp` (keep this exact anchor id even if the visible heading text varies) — the AEBP-voice grounding paragraph (operational observation, not a named-client anecdote, per `GATE-ANECDOTE-INTEGRITY`). Optionally followed by a comparison/reference table (`wp:table`, class `is-style-stripes`, background `#0693e333`, `borderColor: accent-5`) if the topic has clear tiered/comparative data — don't force one if it doesn't. Optionally followed by a no-attribution pull-quote (`wp:quote`, italicized text).
3. **Action-steps section** — task-specific H3 (e.g. "What to do this week," "Before you call the switch finished"), then an **ordered list** (`<ol>`, not `<ul>`) — matches the real pattern in 7867/7928/8006, each item usually bold-lead-in + detail.
4. **"💡 This week's takeaway" section** — H3 anchor `h-this-week-s-takeaway`, one bolded-lead-sentence paragraph.
5. **"📘 Learn more" section** — H3 anchor `h-learn-more`, one context sentence, then arrow-formatted relative links: `→ [Title](relative-url) — description`, one per line via `<br>`, linking back to cornerstone/related long-form posts.
6. **Closing boilerplate** — outside any group, italicized paragraph, near-verbatim: *"This tip is part of our ongoing education series for Bay Area landlords focused on compliance, risk reduction, and smarter property management. 📋 **Browse all Thursday Landlord Tips →**"* linking to `https://alleastbayproperties.com/landlord-tips/` (absolute URL, not the category archive).

## Change log

- 2026-07-22: Created after Brian flagged that the WordPress post, email, and skill were all drafting from an invented structure instead of the site's real one. Verified against posts 7867/7928/8006/8219, the real `MC-Tip-Email-Template.html`, and 4 example graphics. Post 8614 (week 4, "who holds the deposit") and its email were corrected to match.
