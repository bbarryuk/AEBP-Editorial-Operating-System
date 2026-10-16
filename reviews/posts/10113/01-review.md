# Editorial Review — Post 10113

**Rental Property Lighting and CPTED for East Bay Landlords (Video)**

Review mode: Pre-Publish Audit · Reviewed October 16, 2026 · Reviewer: ChatGPT (Codex)

**Recommendation: HOLD PENDING FIXES.** Blocking findings: 10113-F01, 10113-F02.

## Review context and limits

Snapshot: 2026-10-16 15:19:40 (WordPress returned local time without timezone); status draft; no revision ID or GMT supplied. Repository was clean and zero commits ahead of locally recorded origin/main before these artifacts; no remote fetch performed. Standards: docs/01 0.5, docs/02 0.2, docs/03 0.3, docs/07 0.1, manifest 0.1; schema_version 1.0.0 follows existing repository artifacts (schema has no embedded version constant). Pre-Publish Audit: full connector content/meta/terms/thumbnail inspected; block-comment nesting checked with no mismatches, but this is not editor validation. No WordPress edits. Both scripts match. Video Transcript literalness PASS applies to correct pre-recording Video Script label only; no recording exists to compare. No screenshot/layout or generated schema clearance. Source verification: Oakland residential checklist read; NBER 36% result and College of Policing 21% result corroborated through indexed source text (direct opens blocked). Civil Code 1941.3 and 1941.1 primary statutory text read via Justia mirrors; official legislature endpoint returned 403. Ann M. primary opinion accessed via Justia; existing internal security guide has identifiable case citations. DST first-Sunday rule confirmed in 15 USC 260a, November 1 date and 5:10 p.m. sunset corroborated by timeanddate; October 19 6:26 and October 31 6:11 corroborated by astronomy sources. Original sunset source unavailable to reader. Timeanddate's November 2026 Oakland table independently gives November 30 sunset as 4:50 p.m., one minute earlier than the cited provider's 4:51; this small provider/rounding difference does not affect the advice. Optional precision edit: use about 4:50 p.m. and cite https://www.timeanddate.com/sun/usa/oakland?month=11 (2026 table verified). Broader building/fire/accessibility code applicability not exhaustively reviewed; professional referral is appropriate. Main consultation and security-guide destinations loaded; package-theft/habitability and future companion targets require final browser verification.

## Gated categories

- **GATE-LEGAL-ACCURACY: FAIL** — 10113-F01
- **GATE-LOCAL-ACCURACY: PASS**
- **GATE-TECHNICAL-SEO: FAIL** — 10113-F02
- **GATE-COMPLIANCE-RISK: PASS**
- **GATE-ANECDOTE-INTEGRITY: PASS**
- **VIDEO-TRANSCRIPT-LITERAL: PASS**
- **VIDEO-CONSISTENCY: PASS**

## Findings

### 10113-F01 — Type A

- **Finding:** “Light entries, walkways, mail areas and parking from dusk to dawn”
- **Root cause:** The takeaway and spoken script omit the best-practice label used in the article's checklist. The standalone watch page needs to distinguish the recommendation from a legal lighting mandate (EVD-CONFIDENCE-LEVELS).
- **Fix:** Replace the script sentence with: "As a best practice, we recommend steady dusk-to-dawn lighting at entries, walkways, mail areas and parking." On the video page, replace the corresponding takeaway with: "Best practice: provide steady dusk-to-dawn lighting at entries, walkways, mail areas and parking."
- **Future prevention:** Carry labels through the blog, watch-page takeaways and both script copies.

### 10113-F02 — Type B

- **Finding:** “🎥 Video in production. It will appear here once it's live.”
- **Root cause:** The watch page promises video but still contains a production placeholder. No finished recording or VideoObject output was available to review. The draft could be read through the connector, but its rendered page was unavailable to the web reader. Metadata is present; this does not prove generated schema is absent.
- **Fix:** Keep this page in draft until its finished video is playable. Replace the placeholder with the actual embed; change "Video Script" to "Video Transcript" only after checking against the final recording. Verify the template, mobile player, generated VideoObject and final article link in an authenticated preview before clearing this finding.
- **Future prevention:** Treat production completion and rendered schema checks as explicit release prerequisites.

## Scored categories

All scores are editorial estimates, not computed measurements.

| Category | Estimate / threshold | Status | Working | Holding it back |
|---|---|---|---|---|
| SCORE-SEO | 91 / 90 | PASS | Clear watch-page title and populated metadata. | No playable video or verified rendered VideoObject yet. |
| SCORE-GEO | 92 / 95 | FAIL | Scannable takeaways and resources. | Lighting takeaway needs a best-practice label; final media is absent. |
| SCORE-EEAT | 93 / 95 | FAIL | Tenant-reporting statements match the October 16 internal record. | Recommendation labels need correction before recording. |
| SCORE-READABILITY | 95 / 90 | PASS | Short, conversational script; consistently uses we. | No material readability blocker; add the short best-practice label. |
| SCORE-CONVERSION | 93 / 85 | PASS | Read-the-guide link and relevant consultation CTA. | Article target needs verification at coordinated publication. |
| SCORE-OVERALL | 93 / 95 | FAIL | Coherent companion page and script matching the article. | Draft is still a production-stage watch page; labels and technical checks remain open. |

## Strengths Worth Preserving

- Correct Video Script label before recording.
- Script matches the parent and preserves documented AEBP practice.
- Takeaways, resources, read-the-guide link and CTA give the watch page independent value.

## Claim provenance

- **10113-C01 — documented:** “We manage 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay. Let's talk about how your building handles lighting, doors and repair reports.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt (retrieved October 16, generated October 8, 2026). Internal documented record, not AI-assigned owner verification. The tenant-reporting line is company practice, not a claim of routine night inspections.

- **10113-C02 — documented:** “At AEBP, our tenants see the property after dark every night. We mostly see it in daylight. So we ask them to report any light that's out or a door that won't latch. We can only fix what we know about. And once someone reports it, we do know about it.” Source: knowledge/company/anecdote-log.md — 2026-10-16 entry; same-day broken-lock policy additionally documented 2026-09-30. Internal documented record, not AI-assigned owner verification. The tenant-reporting line is company practice, not a claim of routine night inspections.

## Article fixes

- 10113-F01: Replace the script sentence with: "As a best practice, we recommend steady dusk-to-dawn lighting at entries, walkways, mail areas and parking." On the video page, replace the corresponding takeaway with: "Best practice: provide steady dusk-to-dawn lighting at entries, walkways, mail areas and parking."

- 10113-F02: Keep this page in draft until its finished video is playable. Replace the placeholder with the actual embed; change "Video Script" to "Video Transcript" only after checking against the final recording. Verify the template, mobile player, generated VideoObject and final article link in an authenticated preview before clearing this finding.

## Operating System improvements

- Add a sourced CPTED/security-lighting reference covering guideline dimensions, permit-specific assessment requirements and the limits of the lighting research; existing law knowledge files do not cover this topic. Proposed target: `knowledge/laws/security-lighting-cpted.md`. Type C follow-up; no standards changed.
- Define how technical gates distinguish unavailable draft previews from proven markup/schema defects, and how content-only clearance differs from production release. Proposed target: `docs/03-Review-Format.md`. Type C follow-up; no standards changed.

## Next review

Claude should record one disposition for every finding in `02-revision-response.md` and `02-revision-response.json`, then request a follow-up against the actual revised draft. Production or preview checks may remain explicitly unresolved; do not turn unavailable checks into PASS. Brian's final read remains required after review clearance.

