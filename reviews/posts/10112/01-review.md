# Editorial Review — Post 10112

**Lighting, Sightlines and Access: Crime Prevention Through Environmental Design for East Bay Rentals**

Review mode: Pre-Publish Audit · Reviewed October 16, 2026 · Reviewer: ChatGPT (Codex)

**Recommendation: HOLD PENDING FIXES.** Blocking findings: 10112-F01, 10112-F02, 10112-F03, 10112-F04.

## Review context and limits

Snapshot: 2026-10-16 15:19:39 (WordPress returned local time without timezone); status draft; no revision ID or GMT supplied. Repository was clean and zero commits ahead of locally recorded origin/main before these artifacts; no remote fetch performed. Standards: docs/01 0.5, docs/02 0.2, docs/03 0.3, docs/07 0.1, manifest 0.1; schema_version 1.0.0 follows existing repository artifacts (schema has no embedded version constant). Pre-Publish Audit: full connector content/meta/terms/thumbnail inspected; block-comment nesting checked with no mismatches, but this is not editor validation. No WordPress edits. Both scripts match. Companion gate PASS means separate review performed, not companion approved; 10113 is held. GBP draft in October week3 package notes checked for consistency and matches the blog; other social/SMS copy not fully audited. No screenshot/layout or generated schema clearance. Source verification: Oakland residential checklist read; NBER 36% result and College of Policing 21% result corroborated through indexed source text (direct opens blocked). Civil Code 1941.3 and 1941.1 primary statutory text read via Justia mirrors; official legislature endpoint returned 403. Ann M. primary opinion accessed via Justia; existing internal security guide has identifiable case citations. DST first-Sunday rule confirmed in 15 USC 260a, November 1 date and 5:10 p.m. sunset corroborated by timeanddate; October 19 6:26 and October 31 6:11 corroborated by astronomy sources. Original sunset source unavailable to reader. Timeanddate's November 2026 Oakland table independently gives November 30 sunset as 4:50 p.m., one minute earlier than the cited provider's 4:51; this small provider/rounding difference does not affect the advice. Optional precision edit: use about 4:50 p.m. and cite https://www.timeanddate.com/sun/usa/oakland?month=11 (2026 table verified). Broader building/fire/accessibility code applicability not exhaustively reviewed; professional referral is appropriate. Main consultation and security-guide destinations loaded; package-theft/habitability and future companion targets require final browser verification.

## Gated categories

- **GATE-LEGAL-ACCURACY: FAIL** — 10112-F01, 10112-F03
- **GATE-LOCAL-ACCURACY: FAIL** — 10112-F02
- **GATE-TECHNICAL-SEO: FAIL** — 10112-F04
- **GATE-COMPLIANCE-RISK: PASS**
- **GATE-ANECDOTE-INTEGRITY: PASS**
- **CORNERSTONE-STRUCTURE: PASS**
- **CORNERSTONE-AEBP-VOICE: PASS**
- **CORNERSTONE-COMPANION-VIDEO: PASS**
- **CORNERSTONE-GBP-CONSISTENCY: PASS**

## Findings

### 10112-F01 — Type A/B

- **Finding:** “No law requires a CPTED review”
- **Root cause:** The conclusion turns a narrowly framed voluntary maintenance checklist into an unsupported universal legal exemption (STD-HONEST). Oakland expressly requires CPTED assessment for a particular vehicle-barrier obstruction-permit process. That does not establish a routine inspection duty for every rental, but defeats the blanket wording. Source: https://www.oaklandca.gov/Public-Safety-Streets/Transportation-Permits-Engineering/Obstruction-Permit
- **Fix:** Replace with: "Use this checklist as a voluntary maintenance self-audit. If you plan alterations or permit work, ask the city whether project-specific CPTED review or other conditions apply." In FAQ 5 replace the first sentence with: "Oakland's CPTED checklists are written for development projects; here, we use the residential checklist as a voluntary maintenance self-audit for an existing rental."
- **Future prevention:** Keep maintenance recommendations separate from claims that no law or permit condition applies.

### 10112-F02 — Type A

- **Finding:** “Trim shrubs near paths and windows to about 2 feet, and tree canopies to about 6 feet”
- **Root cause:** The owner checklist drops the word clearance, making the six-foot figure read as tree height rather than the open space beneath the canopy. Other passages and the script state the distinction better. STD-PRACTICAL / GATE-LOCAL-ACCURACY. Source: https://www.oaklandca.gov/files/assets/city/v/1/planning-amp-building/documents/sp/design-standards/cpted-residential.pdf
- **Fix:** Replace with: "Keep shrubs near paths and windows about 2 feet high, and maintain about 6 feet of clear space beneath tree canopies, following Oakland's CPTED guideline."
- **Future prevention:** Preserve the measured dimension when shortening guidance; use the same correction in the package's Instagram checklist.

### 10112-F03 — Type A

- **Finding:** “Entries, walkways, mail areas and parking should be lit from dusk to dawn.”
- **Root cause:** The standalone spoken script omits the best-practice label that distinguishes recommendations from law in the article. EVD-CONFIDENCE-LEVELS applies to the script as well as the body.
- **Fix:** Replace the script sentence with: "As a best practice, we recommend steady dusk-to-dawn lighting at entries, walkways, mail areas and parking." On the video page, replace the corresponding takeaway with: "Best practice: provide steady dusk-to-dawn lighting at entries, walkways, mail areas and parking."
- **Future prevention:** Check confidence labels in both copies of the script and in standalone takeaways.

### 10112-F04 — Type B

- **Finding:** “🎥 Video in production. It will appear here once it's live.”
- **Root cause:** Pre-publish technical verification is incomplete. The full snapshot has nested Gutenberg blocks, metadata, image and FAQ hooks, but no finished video. The unauthenticated draft preview returned a 404; actual editor block validity, rendered FAQ/Article schema, reusable block 7266 and responsive presentation could not be verified. This is an access/production hold, not evidence that generated schema is missing.
- **Fix:** Retain "Video Script" until recording is final. At release, replace the production placeholder with the actual playable video embed and use "Video Transcript" only for checked verbatim speech. Verify the authenticated preview, editor block validity, generated schema and final internal links before clearing this finding; no fabricated video URL or schema values should be inserted.
- **Future prevention:** Distinguish draft-content approval from completed-media and rendered-page release checks.

## Scored categories

All scores are editorial estimates, not computed measurements.

| Category | Estimate / threshold | Status | Working | Holding it back |
|---|---|---|---|---|
| SCORE-SEO | 92 / 90 | PASS | Specific search intent and complete Yoast fields. | Rendered output and final media remain unverified. |
| SCORE-GEO | 93 / 95 | FAIL | Answer-first summary, sourced facts table and five FAQs. | Blanket legal wording and compressed canopy instruction weaken standalone answers. |
| SCORE-EEAT | 93 / 95 | FAIL | Documented tenant-reporting practice and careful limits on crime-reduction evidence. | Unqualified no-law statement and script recommendation label need correction. |
| SCORE-READABILITY | 91 / 90 | PASS | Actionable walk-through and controls tables. | Six-foot checklist instruction is ambiguous; Quick Answer is long. |
| SCORE-CONVERSION | 94 / 85 | PASS | Relevant CTA with a live consultation destination. | No material copy blocker; rendered CTA remains unchecked. |
| SCORE-OVERALL | 92 / 95 | FAIL | Useful local maintenance guide with verified company experience. | Legal/local wording fixes and technical release checks remain open. |

## Strengths Worth Preserving

- AEBP observations are documented, including the newsletter actually being sent.
- Relative costs are explicitly professional opinion rather than invented quotes.
- Crime research is not turned into a promise that an individual building is safe.
- Complete cornerstone structure, five FAQs, contextual internal links and focused CTA.

## Claim provenance

- **10112-C01 — documented:** “At AEBP, our tenants see the property after dark every night. We mostly see it in daylight. So we ask them to report any light that's out or a door that won't latch. We can only fix what we know about. And once someone reports it, we do know about it.” Source: knowledge/company/anecdote-log.md — 2026-10-16 entry; same-day broken-lock policy additionally documented 2026-09-30. Internal documented record, not AI-assigned owner verification. The tenant-reporting line is company practice, not a claim of routine night inspections.

- **10112-C02 — documented:** “Our tenants see the property after dark every night; we mostly see it in daylight. So we rely on them to tell us what's wrong. Our October tenant newsletter asks residents to submit a maintenance request whenever an exterior light is out, flickering or on a timer that's no longer set right, and to report any front door, gate or lobby door that isn't latching on its own. The line we use with tenants: we can only fix what we know about.” Source: knowledge/company/anecdote-log.md — 2026-10-16 entry; same-day broken-lock policy additionally documented 2026-09-30. Internal documented record, not AI-assigned owner verification. The tenant-reporting line is company practice, not a claim of routine night inspections.

- **10112-C03 — documented:** “Two things follow from that. First, a tenant report is notice. Once someone tells us an entry light is out or a lobby door won't latch, we know about it, and the clock is running. That's why we treat a broken entry or lobby lock as an emergency, with a vendor sent the same day. Company policy. Second, making it easy for tenants to report is part of the security plan, not just customer service. If tenants don't know how to report a dark walkway, or don't think anyone will act on it, the problem stays invisible to the owner.” Source: knowledge/company/anecdote-log.md — 2026-10-16 entry; same-day broken-lock policy additionally documented 2026-09-30. Internal documented record, not AI-assigned owner verification. The tenant-reporting line is company practice, not a claim of routine night inspections.

- **10112-C04 — documented:** “We manage 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay, with a 24/7 bilingual maintenance line for tenants to report problems. Let's talk about how your building handles lighting, doors and repair reports.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt (retrieved October 16, generated October 8, 2026). Internal documented record, not AI-assigned owner verification. The tenant-reporting line is company practice, not a claim of routine night inspections.

## Article fixes

- 10112-F01: Replace with: "Use this checklist as a voluntary maintenance self-audit. If you plan alterations or permit work, ask the city whether project-specific CPTED review or other conditions apply." In FAQ 5 replace the first sentence with: "Oakland's CPTED checklists are written for development projects; here, we use the residential checklist as a voluntary maintenance self-audit for an existing rental."

- 10112-F02: Replace with: "Keep shrubs near paths and windows about 2 feet high, and maintain about 6 feet of clear space beneath tree canopies, following Oakland's CPTED guideline."

- 10112-F03: Replace the script sentence with: "As a best practice, we recommend steady dusk-to-dawn lighting at entries, walkways, mail areas and parking." On the video page, replace the corresponding takeaway with: "Best practice: provide steady dusk-to-dawn lighting at entries, walkways, mail areas and parking."

- 10112-F04: Retain "Video Script" until recording is final. At release, replace the production placeholder with the actual playable video embed and use "Video Transcript" only for checked verbatim speech. Verify the authenticated preview, editor block validity, generated schema and final internal links before clearing this finding; no fabricated video URL or schema values should be inserted.

## Operating System improvements

- Add a sourced CPTED/security-lighting reference covering guideline dimensions, permit-specific assessment requirements and the limits of the lighting research; existing law knowledge files do not cover this topic. Proposed target: `knowledge/laws/security-lighting-cpted.md`. Type C follow-up; no standards changed.
- Define how technical gates distinguish unavailable draft previews from proven markup/schema defects, and how content-only clearance differs from production release. Proposed target: `docs/03-Review-Format.md`. Type C follow-up; no standards changed.

## Next review

Claude should record one disposition for every finding in `02-revision-response.md` and `02-revision-response.json`, then request a follow-up against the actual revised draft. Production or preview checks may remain explicitly unresolved; do not turn unavailable checks into PASS. Brian's final read remains required after review clearance.

