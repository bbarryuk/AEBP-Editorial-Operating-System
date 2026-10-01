# Follow-up Editorial Review — Post 9849

**Landlord Security Duties in California: What You're Liable For (and What You're Not)**

**Recommendation: HOLD PENDING FIXES.** Three content findings remain, plus the technical verification hold.

Mode: Pre-Publish Audit, with rendered checks blocked. Reviewed 2026-10-01T03:28:31Z (September 30 Pacific).

WordPress: draft; modified 2026-09-30 19:44:45 (timezone unspecified), revision ID/GMT timestamp unavailable. [Dev draft](https://dev.alleastbayproperties.com/?p=9849).

Repository: `9b2dd5c60c5e3558b0b6e44fdebd6f80051ac3a8`, clean before artifact creation. Standards: 01 v0.5 / 02 v0.2 / 03 v0.3 / 07 v0.1; manifest v0.1.

## Verification of Claude’s responses

| Finding | Final-review status | Evidence |
|---|---|---|
| 9849-F01 | CLOSED | Actual and received notice present in Key Facts, body, table, script and package; causation distinguished. |
| 9849-F02 | PARTIALLY RESOLVED / OPEN | Guard/camera scope corrected; unsupported claim-strength predictions remain in body and FAQ 1. |
| 9849-F03 | CLOSED; NEW REGRESSION SEPARATE | Exceptions and alternatives improved. Spoken 'With some exceptions' is adequate concise qualification; new checklist mandate is F07. |
| 9849-F04 | PARTIALLY RESOLVED / OPEN | Co-tenant order and reimbursement trigger corrected; non-co-tenant path still uses restrained-person terminology. |
| 9849-F05 | CLOSED | Ann M. earlier crimes and lack of owner knowledge now accurately summarized. |
| 9849-F06 | OPEN / REQUIRES HUMAN | Rendered preview/editor/schema/video evidence still unavailable. |
| 9849-F07 | NEW REGRESSION | Written internal procedure incorrectly classified as statutory mandate. |

All prior findings received a disposition. Closed means checked against the current WordPress draft. No requires_human item was cleared without evidence.

## Gates

- **GATE-LEGAL-ACCURACY: FAIL** — 9849-F02, 9849-F04, 9849-F07
- **GATE-LOCAL-ACCURACY: PASS**
- **GATE-TECHNICAL-SEO: FAIL** — 9849-F06
- **GATE-COMPLIANCE-RISK: PASS**
- **GATE-ANECDOTE-INTEGRITY: PASS**
- **CORNERSTONE-STRUCTURE: PASS**
- **CORNERSTONE-AEBP-VOICE: PASS**
- **CORNERSTONE-COMPANION-VIDEO: PASS**
- **CORNERSTONE-GBP-CONSISTENCY: PASS**

The technical FAIL records unverified requirements, not a demonstrated absent-schema defect. Companion/consistency PASS is not publication approval.

## Remaining findings

### 9849-F02 — Type A / B

**Finding:** “A working lock, no prior incident on the property, or an incident inside a unit makes a claim harder, but none of them alone decides it.”

**Root cause:** Partially resolved. Guard/camera scope and causation are fixed, but the retained claim-strength prediction remains unsupported. Ann M. and Castaneda analyze particular precautions and facts; neither establishes this general rule for incidents inside units or properties with working locks. FAQ 1 repeats 'makes a claim much harder'.

**Fix (not applied):** Replace the quoted sentence with: 'A working lock, no prior incident on the property, or an incident inside a unit does not by itself decide liability; the relevant risk, available precautions and causal connection still matter.' Replace FAQ 1’s final sentence with: 'A working, properly maintained lock does not by itself resolve liability; the claim still depends on the relevant duty, breach and causal connection.'

**Future prevention:** Check revised summaries, FAQs and checklist labels against the operative source; distinguish implementation recommendations from statutory requirements.

### 9849-F04 — Type A

**Finding:** “Civil Code §1941.5 covers cases where the restrained person isn't a tenant of the unit, and accepts several kinds of documentation, including a signed statement from the tenant.”

**Root cause:** Partially resolved. Written request, co-tenant exclusion order and reimbursement trigger are fixed. Section 1941.5(a) concerns a person alleged to have committed abuse or violence, not necessarily someone restrained by court order. Its eligibility definition also includes qualifying household/immediate-family victims. The self-change subdivision’s lease-date qualification applies to that subdivision, not just reimbursement; the summary omits workmanship/quality safeguards. Source: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.5.

**Fix (not applied):** Replace the quoted sentence with: 'Civil Code §1941.5 applies when the person alleged to have committed abuse or violence is not a tenant of the same unit. It accepts several forms of qualifying documentation, including a signed statement from the eligible tenant; a restraining order is not required in every case.' Replace 'The big exception is a tenant protected from domestic violence or abuse' with: 'Special lock-change rights cover eligible victims of abuse or violence and, under §1941.5, certain tenants whose household or immediate family member is a victim.' Replace the final self-change sentence with: 'For leases executed on or after January 1, 2011, if the landlord misses the deadline, the tenant may change the locks in a workmanlike manner using locks of similar or better quality, must notify the landlord within 24 hours and provide a key by an agreed reasonable method, and must be reimbursed within 21 days after the change.'

**Future prevention:** Check revised summaries, FAQs and checklist labels against the operative source; distinguish implementation recommendations from statutory requirements.

### 9849-F07 — Type A

**Finding:** “You have a written process for 24-hour lock changes when a protected tenant asks.”

**Root cause:** New regression: this now sits under 'Required by §1941.5/§1941.6'. Those sections require a qualifying written tenant request and timely lock change, not a landlord’s written internal procedure. The adjacent 'best practice, not statutory mandates' label is also broader than necessary: other law/code duties can apply even when §1941.3 does not specifically prescribe an item. Sources: Civil Code §§1941.3, 1941.5 and 1941.6.

**Fix (not applied):** Under 'Required by §1941.5/§1941.6', replace the item with: 'When the applicable written request and documentation requirements are met, change covered locks at landlord expense within 24 hours and provide the tenant a key.' Under the recommendations, add: 'Keep a written procedure for identifying qualifying requests and meeting the deadline.' Replace 'Recommended safety checks (best practice, not statutory mandates)' with: 'Additional safety and operating checks (other legal or code duties may also apply).'

**Future prevention:** Check revised summaries, FAQs and checklist labels against the operative source; distinguish implementation recommendations from statutory requirements.

### 9849-F06 — Type B

**Finding:** “🎥 Video in production. It will appear here once it's live.”

**Root cause:** Still open; Claude correctly marked requires_human. Both current draft URLs were rechecked and return the theme’s Page not found page without an authenticated preview session. Stored block delimiters and JSON attributes pass basic checks, but this does not verify editor validity, rendered layout, canonical or applicable schema. Recording/player remains in production. This is a verification hold, not evidence of missing schema.

**Fix (not applied):** Retain the accurate production placeholder and 'Video Script' label while drafting. No text replacement clears this check: inspect an authenticated WordPress preview and editor, check applicable rendered schema and layout, and validate the actual video/player and parent-guide destination when ready. Do not invent a video URL or upload date. A post-publication check supplements rather than replaces pre-publication evidence.

**Future prevention:** Check the short answer, tables, FAQs, metadata and both copies of the video script against the same qualified rule before recording or publishing.

## Scored categories

Estimates, not calibrated measurements. Thresholds remain unchanged.

| Category | Score | Threshold | Status | What works | What holds it back |
|---|---:|---:|---|---|---|
| SCORE-SEO | 88 | 90 | FAIL | Clear search intent, distinct title and description, contextual internal links. | Rendered technical SEO, editor validity and launch destination remain unverified. |
| SCORE-GEO | 92 | 95 | FAIL | Answer-first structure, comparison tables and five concise FAQs. | Three remaining legal wording issues affect extractable summaries; emitted schema unverified. |
| SCORE-EEAT | 93 | 95 | FAIL | Named author, documented AEBP process and identifiable legal authorities. | Residual claim-strength prediction, restrained-person label and false procedure mandate. |
| SCORE-READABILITY | 92 | 90 | PASS | Plain language, short sections and useful practical organization. | Dense FAQ 4 and repetitive introductory summaries; keep remaining fixes concise. |
| SCORE-CONVERSION | 91 | 85 | PASS | Relevant CTA, verified consultation destination and documented maintenance service. | Final recording/player is unfinished; existing consultation path was verified in the initial pass. |
| SCORE-OVERALL | 92 | 95 | FAIL | Strong structure and documented practitioner contribution. | Remaining legal findings plus carried-forward technical verification hold. |

## Strengths Worth Preserving

- Actual knowledge and received notice are now distinguished from automatic liability for a later crime.
- Guard-duty summaries allow other serious warning signs, and camera wording stays within §1941.3.
- AEBP same-day vendor dispatch and the revised risk/retention opinion are documented; provenance remains PASS.
- Answer-first structure, responsibility tables, five FAQs and a relevant CTA remain intact.

## Claim provenance

- **9849-C01: documented** — “when a tenant reports a broken entry door lock or a lobby door that won't lock, we treat it as an emergency on our 24/7 maintenance line, not a routine work order, and send a vendor the same day.” Source: knowledge/company/anecdote-log.md — 2026-09-30 entry; October/2026-10-05-week1-package-notes.md (OneDrive). Documented company process. Same-day dispatch is not a promise of same-day completed repair.

- **9849-C02: documented** — “How fast is "reasonable" for an entry lock (we treat it as same-day)” Source: knowledge/company/anecdote-log.md — 2026-09-30 entry; October/2026-10-05-week1-package-notes.md (OneDrive). Same policy repeated in table; retain distinction between dispatch and completed repair.

- **9849-C03: documented** — “Professional opinion, from managing 600+ East Bay units:” Source: knowledge/company/anecdote-log.md — 2026-09-30 entry; October/2026-10-05-week1-package-notes.md (OneDrive); knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt. Documented professional view and portfolio basis, not an observed building case or measured retention result.

- **9849-C04: documented** — “We manage 600+ East Bay rental units with a 24/7 bilingual maintenance line.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt. Live reference checked for portfolio count, service area and maintenance line; unrelated stale financial metrics were not used.

- **9849-C05: documented** — “At AEBP, we treat a broken entry or lobby lock as an emergency, with a vendor sent the same day.” Source: knowledge/company/anecdote-log.md — 2026-09-30 entry; October/2026-10-05-week1-package-notes.md (OneDrive). Exact script policy documented; do not expand into a performance statistic.

- **9849-C06: documented** — “In our view, working locks, good lighting and secure mail can help reduce risk and support tenant retention.” Source: knowledge/company/anecdote-log.md — 2026-09-30 entry; October/2026-10-05-week1-package-notes.md (OneDrive). Revised professional opinion matches the amended September 30 anecdote-log entry; no promise of immunity or measured retention benefit.

## Article fixes

- 9849-F02: Replace the quoted sentence with: 'A working lock, no prior incident on the property, or an incident inside a unit does not by itself decide liability; the relevant risk, available precautions and causal connection still matter.' Replace FAQ 1’s final sentence with: 'A working, properly maintained lock does not by itself resolve liability; the claim still depends on the relevant duty, breach and causal connection.'

- 9849-F04: Replace the quoted sentence with: 'Civil Code §1941.5 applies when the person alleged to have committed abuse or violence is not a tenant of the same unit. It accepts several forms of qualifying documentation, including a signed statement from the eligible tenant; a restraining order is not required in every case.' Replace 'The big exception is a tenant protected from domestic violence or abuse' with: 'Special lock-change rights cover eligible victims of abuse or violence and, under §1941.5, certain tenants whose household or immediate family member is a victim.' Replace the final self-change sentence with: 'For leases executed on or after January 1, 2011, if the landlord misses the deadline, the tenant may change the locks in a workmanlike manner using locks of similar or better quality, must notify the landlord within 24 hours and provide a key by an agreed reasonable method, and must be reimbursed within 21 days after the change.'

- 9849-F07: Under 'Required by §1941.5/§1941.6', replace the item with: 'When the applicable written request and documentation requirements are met, change covered locks at landlord expense within 24 hours and provide the tenant a key.' Under the recommendations, add: 'Keep a written procedure for identifying qualifying requests and meeting the deadline.' Replace 'Recommended safety checks (best practice, not statutory mandates)' with: 'Additional safety and operating checks (other legal or code duties may also apply).'

- 9849-F06: Retain the accurate production placeholder and 'Video Script' label while drafting. No text replacement clears this check: inspect an authenticated WordPress preview and editor, check applicable rendered schema and layout, and validate the actual video/player and parent-guide destination when ready. Do not invent a video URL or upload date. A post-publication check supplements rather than replaces pre-publication evidence.

## Operating System improvements

- Type C follow-up: Add a focused security-duty reference covering actual/received notice, duty versus causation, qualified lock coverage, co-tenant exclusion orders and the guard-duty foreseeability test. Independently checked sources support this review; absence of a local reference is not an extra publication blocker. Target: `knowledge/laws/landlord-security-duties.md`.

- Type C follow-up: Declare the schema release version explicitly; 1.0.0 currently comes from established review artifacts rather than a version in the schema itself. Target: `automation/schemas/review.schema.json`.

- Type C follow-up: Add an explicit deferred/blocked verification representation for pre-recording drafts so FAIL can distinguish confirmed defects from an inaccessible preview without relying only on notes. Target: `docs/07-Editorial-Automation.md`.

- Type C follow-up: Revision-response 9850 has content_type 'cornerstone' although the post and initial review are 'video'. Correct that metadata to 'video' and add a cross-artifact content-type check. Both responses also use schema_version 0.1.0 while prior reviews use 1.0.0; neither schema declares its release version, so this is a protocol ambiguity rather than a proven JSON-schema violation. Do not rewrite historical artifacts silently. Target: `reviews/posts/9850/02-revision-response.json`.

## Sources

- [Civil Code §1941.3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.3.)
- [Civil Code §1941.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.5.)
- [Civil Code §1941.6](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.6.)
- [Ann M.](https://law.justia.com/cases/california/supreme-court/4th/6/666.html)
- [Castaneda](https://law.justia.com/cases/california/supreme-court/2007/s138104.html)

## Scope and handoff

Follow-up to 01-review and Claude’s 02-revision-response (2026-10-01T02:47:00Z). Every prior finding has exactly one response; no missing or extra dispositions. Each accepted edit was checked against a fresh full AEBP-Dev snapshot rather than assumed from Claude’s summary.

Snapshot post_modified: 2026-09-30 19:44:45; connector did not identify its timezone or return revision_id/modified_gmt. Those fields remain null. Review date September 30 Pacific / October 1 UTC.

Disposition verification:
9849-F01 — CLOSED — Actual and received notice present in Key Facts, body, table, script and package; causation distinguished.
9849-F02 — PARTIALLY RESOLVED / OPEN — Guard/camera scope corrected; unsupported claim-strength predictions remain in body and FAQ 1.
9849-F03 — CLOSED; NEW REGRESSION SEPARATE — Exceptions and alternatives improved. Spoken 'With some exceptions' is adequate concise qualification; new checklist mandate is F07.
9849-F04 — PARTIALLY RESOLVED / OPEN — Co-tenant order and reimbursement trigger corrected; non-co-tenant path still uses restrained-person terminology.
9849-F05 — CLOSED — Ann M. earlier crimes and lack of owner knowledge now accurately summarized.
9849-F06 — OPEN / REQUIRES HUMAN — Rendered preview/editor/schema/video evidence still unavailable.
9849-F07 — NEW REGRESSION — Written internal procedure incorrectly classified as statutory mandate.

Current docs/01 v0.5, docs/02 v0.2, docs/03 v0.3, docs/07 v0.1, both manifests v0.1 and schemas were read. Git comparison shows normative files unchanged from the initial audit; the anecdote log now records the revised risk wording. Repo was clean before review artifact creation and 0/0 against locally stored origin/main; no fresh fetch claimed. Global-ignore permission warning did not prevent status.

Full body, excerpt, metadata, terms, author and thumbnail were examined. Basic checks: all block comment pairs balance and all attribute JSON parses (43 attribute objects in 9849; 8 in 9850). These checks do not establish Gutenberg editor validity. Both current public dev permalinks return the theme’s Page not found page. No logged-in preview, responsive-layout or emitted-schema clearance is claimed.

Scripts are identical across the two WordPress drafts; package notes carry the same revised script. GBP/social/SMS/YouTube draft copy was re-read for factual consistency after revisions; no live posting or full platform-specific publishing audit occurred. Existing production references and Oakland checklist were verified in the initial pass in this same task; the parent-guide launch URL and actual video remain pending.

CORNERSTONE-STRUCTURE and AEBP-VOICE PASS: required sequence and documented practitioner policy retained. COMPANION-VIDEO PASS means independently audited in 9850/03-final-review, not publication approval. GBP-CONSISTENCY PASS refers to the saved revised package copy only.

Sources rechecked for revisions: California Legislative Information §§1941.3, 1941.5, 1941.6; Ann M. and Castaneda judicial opinions via Justia. Initial-source verification retained for unchanged claims. No comprehensive case subsequent-history research is claimed.

Technical findings remain requires_human and are not silently cleared. Under the current binary schema, recommendation remains hold_pending_fixes. No WordPress, response, standards or knowledge files were edited.

Next: Claude should answer 9849-F02, F04, F06 and new F07 in 04-revision-response, apply the three content fixes, and keep the technical hold explicit.

