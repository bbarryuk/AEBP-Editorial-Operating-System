# Revision Response — Post 9850

Responds to: `reviews/posts/9850/01-review.json` (2026-10-01T02:29:26Z)  
Responder: Claude (Cowork) · 2026-10-01T02:47:00Z  
Repo: `b26e98e1871d47f82ef0dc41f3c3841c8af031cd` (dirty: new review/response files; `skills/weekly-post-review.md` shows a pre-existing diff not made by Claude)  
WordPress: draft, [https://dev.alleastbayproperties.com/?post_type=video&p=9850](https://dev.alleastbayproperties.com/?post_type=video&p=9850)

**Recommendation to Brian:** hold_for_brian_decision

## Dispositions

### 9850-F01 — accepted

**Rationale:** Same §1941.3(b) actual-notice issue as 9849-F01, verified against the statute text.

**Change applied:** Coverage bullet, Short Version (new §1941.3(b) paragraph with causation), takeaway 2 and script paragraph 3 rewritten. Yoast meta description replaced with GPT's proposed text.

> Before: The liability window opens when a tenant reports a broken lock. Fix it fast and log it.

> After: Once you know a required lock is defective, whether through a tenant report or your own observation, act promptly and document the repair. Notice alone doesn't establish liability for a later crime.

### 9850-F02 — accepted

**Rationale:** Standalone page lacked §1941.3's scope qualifications.

**Change applied:** Short Version first paragraph replaced with the qualified statute summary plus 'The full guide explains the sliding-door, window, existing-hardware and other exceptions.' Script lock list now opens 'With some exceptions.'

> Before: California law requires a working deadbolt on each main entry door, locks on windows that open, and locking exterior doors into common areas of multifamily buildings.

> After: Subject to statutory exceptions, Civil Code §1941.3 requires deadbolts on main swinging unit-entry doors, security or locking devices on covered windows that open, and code-compliant locks on exterior doors into common areas with access to units in multifamily buildings.

### 9850-F03 — accepted

**Rationale:** Agreed on all four parts: generalized outcome hook, guard-duty test applied to foreseeability overall, unsupported frequency claim, and missing co-tenant distinction/citations.

**Change applied:** Intro paragraph and excerpt now open with GPT's 'A crime alone does not make a California landlord liable…' text; neighborhood/guard sentence replaced (citing Ann M. and Castaneda; less burdensome precautions assessed separately); 'Low-cost fixes…' takeaway replaced; protected-tenant takeaway replaced with the §1941.6 court-order distinction; Resources now link §1941.5, §1941.6, Ann M. and Castaneda; script AEBP line changed to 'can help reduce risk and support tenant retention.'

> Before: Low-cost fixes to known problems are where landlords most often get caught.

> After: Address known defects promptly; the burden of a precaution matters when courts assess duty.

### 9850-F04 — requires_human

**Rationale:** Verification hold, not a text defect. 'Video Script' label kept until the render is checked word for word; placeholder stays until a real YouTube ID exists. Rendered page, Gutenberg validity and VideoObject output need Brian's logged-in preview now and a post-publish check later. No video URL or upload date invented.

## Operating System follow-ups

- **knowledge/laws/landlord-security-duties.md:** Accepted, not built this pass: add knowledge/laws/landlord-security-duties.md covering actual/received notice under §1941.3(b), §1941.3(d) duty-of-care carve-out, duty vs. causation, qualified lock coverage (sliding-door, window, existing-hardware, approved-device exceptions), §1941.5 vs. §1941.6 documentation paths, and the Ann M./Castaneda guard-duty foreseeability test. Recommend building it before the Oct 8 Thursday Tip and Week 4 drafts, which reuse these rules.
- **automation/schemas/review.schema.json; docs/07-Editorial-Automation.md:** Agreed, deferred to Brian/ChatGPT: explicit schema release version in review.schema.json, and a deferred/blocked verification state in docs/07 so an inaccessible draft preview is distinguishable from a confirmed defect.

## Summary

All four findings answered. F01–F03 fixed (summary, takeaways, resources, excerpt, meta description, script); F04 is a rendered-preview/video verification hold. Nothing published.

## Verification of edits

- Full content replaced via `wp_update_post`; returned content length matched the locally built file byte-for-byte.
- Script text is identical in 9849, 9850 and the package notes (`VIDEO-CONSISTENCY`).
- Package copy (GBP, social, SMS, YouTube, homepage lead-in) rechecked against the revised rules; tenant-report-only 'on notice' and 'usually not' framing removed.
