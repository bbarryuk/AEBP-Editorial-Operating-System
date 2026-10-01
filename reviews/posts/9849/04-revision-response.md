# Revision Response 2 — Post 9849

Responds to: `reviews/posts/9849/03-final-review.json` (2026-10-01T03:28:31Z)  
Responder: Claude (Cowork) · 2026-10-01T03:40:00Z  
Repo: `9b2dd5c60c5e3558b0b6e44fdebd6f80051ac3a8` (dirty: new response files)  
WordPress: draft, [https://dev.alleastbayproperties.com/?p=9849](https://dev.alleastbayproperties.com/?p=9849)

**Recommendation to Brian:** hold_for_brian_decision

## Dispositions

### 9849-F02 — accepted

**Rationale:** Agreed: 'makes a claim harder' / 'much harder' is a claim-strength prediction neither Ann M. nor Castaneda supports as a general rule. GPT's replacements say only what the authorities support.

**Change applied:** Body sentence in 'What Landlords Generally Aren't Responsible For' and FAQ 1's last sentence replaced with GPT's proposed text verbatim.

> Before: A working lock, no prior incident on the property, or an incident inside a unit makes a claim harder, but none of them alone decides it.

> After: A working lock, no prior incident on the property, or an incident inside a unit does not by itself decide liability; the relevant risk, available precautions and causal connection still matter.

### 9849-F04 — accepted_with_modification

**Rationale:** Verified against §1941.5 text: the statute refers to a person 'alleged to have committed abuse or violence' (not a 'restrained person'); 'eligible tenant' includes a tenant whose immediate family or household member is a victim; the self-change remedy (subdivision (c)(3)) applies to leases executed on or after Jan. 1, 2011 and requires a workmanlike change with locks of similar or better quality. Modification: GPT's self-change sentence is §1941.5-specific, so it is prefixed 'Under §1941.5' and followed by '§1941.6 has a similar self-change remedy' rather than presented as one rule for both sections.

**Change applied:** FAQ 4 rewritten: eligibility sentence (incl. household/immediate-family victims under §1941.5), §1941.5 'person alleged to have committed abuse or violence … not a tenant of the same unit' with tenant-statement documentation and 'a restraining order is not required in every case,' §1941.6 co-tenant court order retained, and the self-change sentence with the 2011 lease date, workmanlike/similar-or-better-quality condition, 24-hour notice, key by agreed reasonable method and 21-day reimbursement. Key Facts row unchanged ('restrained person' there refers only to §1941.6, which uses that term).

> Before: Civil Code §1941.5 covers cases where the restrained person isn't a tenant of the unit, and accepts several kinds of documentation, including a signed statement from the tenant.

> After: Civil Code §1941.5 applies when the person alleged to have committed abuse or violence is not a tenant of the same unit. It accepts several forms of qualifying documentation, including a signed statement from the eligible tenant; a restraining order is not required in every case.

### 9849-F07 — accepted

**Rationale:** Correct regression: §1941.5/§1941.6 require a timely lock change on a qualifying written request, not a landlord's internal written procedure. The 'not statutory mandates' label was also broader than accurate, since other law or code duties can apply.

**Change applied:** Under 'Required by §1941.5/§1941.6' the item now states the statutory duty (GPT's text). The written-procedure item moved to the additional checks list. The additional-checks heading now reads 'Additional safety and operating checks (other legal or code duties may also apply).'

> Before: You have a written process for 24-hour lock changes when a protected tenant asks.

> After: When the applicable written request and documentation requirements are met, change covered locks at landlord expense within 24 hours and provide the tenant a key.

### 9849-F06 — requires_human

**Rationale:** Unchanged verification hold. No new evidence this round: the logged-in preview/editor check, rendered layout and schema, and the actual video/player are still pending with Brian. Placeholder and 'Video Script' label retained; nothing invented.

## Verification of edits

- Six `wp_alter_post` replacements each matched exactly once against the live draft; a full `wp_update_post` resave followed so SEO/schema caches refresh.
- The local build and markdown copy were updated with the same text.
- `VIDEO-CONSISTENCY`: no change to the script or 9850 was needed; none of the edited passages appear in either.

## Operating System follow-ups

- **knowledge/laws/landlord-security-duties.md:** Still accepted, not built: knowledge/laws/landlord-security-duties.md (actual/received notice, §1941.3(d), duty vs. causation, qualified lock coverage, §1941.5 eligibility incl. household/immediate-family victims and 'alleged' abuser wording vs. §1941.6 co-tenant exclusion order, self-change conditions, guard-duty foreseeability). Recommended before the Oct 8 Tip.
- **automation/schemas/; docs/07-Editorial-Automation.md:** Agreed, deferred to Brian/ChatGPT: explicit schema release version in review.schema.json and revision-response.schema.json, and a deferred/blocked verification state in docs/07. Revision responses keep schema_version 0.1.0 to match the 9313 precedent until a version is declared.

## Summary

All four open findings answered. F02, F04 and F07 fixed in the draft via targeted edits (verified by single-match replacements, followed by a full resave). These edits touch blog-only sections (body, FAQ 1, FAQ 4, self-audit), so the shared video script and package copy didn't need changes. F06 remains a verification hold for Brian's logged-in preview and the video. Nothing published.
