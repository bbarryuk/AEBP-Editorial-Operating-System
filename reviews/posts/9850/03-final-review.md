# Follow-up Editorial Review — Post 9850

**Landlord Security Responsibilities in California: What You're Liable For (and What You're Not)**

**Recommendation: HOLD PENDING FIXES.** All prior content findings are closed; only the technical/video verification hold remains.

Mode: Pre-Publish Audit, with rendered checks blocked. Reviewed 2026-10-01T03:28:31Z (September 30 Pacific).

WordPress: draft; modified 2026-09-30 19:45:22 (timezone unspecified), revision ID/GMT timestamp unavailable. [Dev draft](https://dev.alleastbayproperties.com/?post_type=video&p=9850).

Repository: `9b2dd5c60c5e3558b0b6e44fdebd6f80051ac3a8`, clean before artifact creation. Standards: 01 v0.5 / 02 v0.2 / 03 v0.3 / 07 v0.1; manifest v0.1.

## Verification of Claude’s responses

| Finding | Final-review status | Evidence |
|---|---|---|
| 9850-F01 | CLOSED | Knowledge/notice and causation corrections verified, including metadata. |
| 9850-F02 | CLOSED | Qualified standalone summary and explicit exceptions in spoken script verified. |
| 9850-F03 | CLOSED | Hook, guard test, frequency claim, protected-tenant takeaway, citations and risk-reduction wording fixed. |
| 9850-F04 | OPEN / REQUIRES HUMAN | Preview/editor, recording, schema and parent-guide launch destination pending. |

All prior findings received a disposition. Closed means checked against the current WordPress draft. No requires_human item was cleared without evidence.

## Gates

- **GATE-LEGAL-ACCURACY: PASS**
- **GATE-LOCAL-ACCURACY: PASS**
- **GATE-TECHNICAL-SEO: FAIL** — 9850-F04
- **GATE-COMPLIANCE-RISK: PASS**
- **GATE-ANECDOTE-INTEGRITY: PASS**
- **VIDEO-TRANSCRIPT-LITERAL: PASS**
- **VIDEO-CONSISTENCY: PASS**

The technical FAIL records unverified requirements, not a demonstrated absent-schema defect. Companion/consistency PASS is not publication approval.

## Remaining findings

### 9850-F04 — Type B

**Finding:** “🎥 Video in production. It will appear here once it's live.”

**Root cause:** Still open; Claude correctly marked requires_human. Both current draft URLs were rechecked and return the theme’s Page not found page without an authenticated preview session. Stored block delimiters and JSON attributes pass basic checks, but this does not verify editor validity, rendered layout, canonical or applicable schema. Recording/player remains in production. This is a verification hold, not evidence of missing schema.

**Fix (not applied):** Retain the accurate production placeholder and 'Video Script' label while drafting. No text replacement clears this check: inspect an authenticated WordPress preview and editor, check applicable rendered schema and layout, and validate the actual video/player and parent-guide destination when ready. Do not invent a video URL or upload date. A post-publication check supplements rather than replaces pre-publication evidence.

**Future prevention:** Check the short answer, tables, FAQs, metadata and both copies of the video script against the same qualified rule before recording or publishing.

## Scored categories

Estimates, not calibrated measurements. Thresholds remain unchanged.

| Category | Score | Threshold | Status | What works | What holds it back |
|---|---:|---:|---|---|---|
| SCORE-SEO | 88 | 90 | FAIL | Clear search intent, distinct title and description, contextual internal links. | Rendered technical SEO, editor validity and launch destination remain unverified. |
| SCORE-GEO | 94 | 95 | FAIL | Scannable summary and takeaways plus link to the full guide. | Content qualifications corrected; final emitted schema and video integration remain unverified. |
| SCORE-EEAT | 96 | 95 | PASS | Named author, documented AEBP process and identifiable legal authorities. | No remaining content evidence blocker found; completed recording and technical inspection still pending. |
| SCORE-READABILITY | 94 | 90 | PASS | Plain language, short sections and useful practical organization. | Some legal vocabulary remains necessary; no readability blocker. |
| SCORE-CONVERSION | 91 | 85 | PASS | Relevant CTA, verified consultation destination and documented maintenance service. | Final recording/player is unfinished; existing consultation path was verified in the initial pass. |
| SCORE-OVERALL | 94 | 95 | FAIL | Strong structure and documented practitioner contribution. | Content fixes clear; full pre-publication audit still held for technical/video evidence. |

## Strengths Worth Preserving

- Actual knowledge and received notice are now distinguished from automatic liability for a later crime.
- Guard-duty summaries allow other serious warning signs, and camera wording stays within §1941.3.
- AEBP same-day vendor dispatch and the revised risk/retention opinion are documented; provenance remains PASS.
- All three prior content findings are closed; the script matches the parent post and correctly remains labeled Video Script.

## Claim provenance

- **9850-C01: documented** — “AEBP manages 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay, with a 24/7 bilingual maintenance line.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt. Company facts supported by current web reference.

- **9850-C02: documented** — “At AEBP, we treat a broken entry or lobby lock as an emergency, with a vendor sent the same day.” Source: knowledge/company/anecdote-log.md — 2026-09-30 entry; October/2026-10-05-week1-package-notes.md (OneDrive). Exact script policy documented; do not expand into a performance statistic.

- **9850-C03: documented** — “In our view, working locks, good lighting and secure mail can help reduce risk and support tenant retention.” Source: knowledge/company/anecdote-log.md — 2026-09-30 entry; October/2026-10-05-week1-package-notes.md (OneDrive). Revised professional opinion matches the amended September 30 anecdote-log entry; no promise of immunity or measured retention benefit.

## Article fixes

- 9850-F04: Retain the accurate production placeholder and 'Video Script' label while drafting. No text replacement clears this check: inspect an authenticated WordPress preview and editor, check applicable rendered schema and layout, and validate the actual video/player and parent-guide destination when ready. Do not invent a video URL or upload date. A post-publication check supplements rather than replaces pre-publication evidence.

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

Snapshot post_modified: 2026-09-30 19:45:22; connector did not identify its timezone or return revision_id/modified_gmt. Those fields remain null. Review date September 30 Pacific / October 1 UTC.

Disposition verification:
9850-F01 — CLOSED — Knowledge/notice and causation corrections verified, including metadata.
9850-F02 — CLOSED — Qualified standalone summary and explicit exceptions in spoken script verified.
9850-F03 — CLOSED — Hook, guard test, frequency claim, protected-tenant takeaway, citations and risk-reduction wording fixed.
9850-F04 — OPEN / REQUIRES HUMAN — Preview/editor, recording, schema and parent-guide launch destination pending.

Current docs/01 v0.5, docs/02 v0.2, docs/03 v0.3, docs/07 v0.1, both manifests v0.1 and schemas were read. Git comparison shows normative files unchanged from the initial audit; the anecdote log now records the revised risk wording. Repo was clean before review artifact creation and 0/0 against locally stored origin/main; no fresh fetch claimed. Global-ignore permission warning did not prevent status.

Full body, excerpt, metadata, terms, author and thumbnail were examined. Basic checks: all block comment pairs balance and all attribute JSON parses (43 attribute objects in 9849; 8 in 9850). These checks do not establish Gutenberg editor validity. Both current public dev permalinks return the theme’s Page not found page. No logged-in preview, responsive-layout or emitted-schema clearance is claimed.

Scripts are identical across the two WordPress drafts; package notes carry the same revised script. GBP/social/SMS/YouTube draft copy was re-read for factual consistency after revisions; no live posting or full platform-specific publishing audit occurred. Existing production references and Oakland checklist were verified in the initial pass in this same task; the parent-guide launch URL and actual video remain pending.

VIDEO-TRANSCRIPT-LITERAL PASS refers to correct pre-recording Script labeling. VIDEO-CONSISTENCY PASS confirms matching scripts and shared claims; blog-only FAQ/checklist findings do not create a video content defect.

Sources rechecked for revisions: California Legislative Information §§1941.3, 1941.5, 1941.6; Ann M. and Castaneda judicial opinions via Justia. Initial-source verification retained for unchanged claims. No comprehensive case subsequent-history research is claimed.

Technical findings remain requires_human and are not silently cleared. Under the current binary schema, recommendation remains hold_pending_fixes. No WordPress, response, standards or knowledge files were edited.

No further video prose rewrite is required by this review. Supply verification evidence for 9850-F04 in the next response; correct the response content-type bookkeeping separately. Brian still reads the finished draft and recording before publication.

