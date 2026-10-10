# Follow-up Pre-Publish Audit — Post 10023

**How to Stop Package Theft in an Apartment Building: What Actually Works in Older East Bay Buildings**

**Copy fixes verified. Hold publication for production checks only.**

Reviewed October 9, 2026 Pacific for Monday October 12. WordPress modified 2026-10-09 18:21:30 (timezone unspecified), status draft. Repository `8d19435b130d5846c7157516279476b168f0948b`, clean before artifacts. Standards: docs/01 v0.5, docs/02 v0.2, docs/03 v0.3, docs/07 v0.1, applicable manifest v0.1. Reviewer: ChatGPT / Codex.

## Prior findings and dispositions

| Finding | Result | Verified evidence |
|---|---|---|
| 10023-F01 | CLOSED | Risk-reduction wording verified in Quick Answer, camera table/bullet, excerpt, conclusion, FAQ and both scripts. Revised package notes/GBP/social/SMS no longer use the flagged prevention claims. |
| 10023-F02 | CLOSED | Statutory lock provision and closer best practice separated in Step One/checklist; retrofit caveat and security-guide link present. |
| 10023-F03 | CLOSED | Quick Answer, Key Facts, FAQ 2 and conclusion now limit the negative mandate statement to §1941.3 itself. |
| 10023-F04 | CLOSED | Key Facts now attributes Berkeley master-key belief to the building manager; both NBC links retained. |
| 10023-F05 | CLOSED | US terms must be confirmed; UK price tier and ASK4 link removed from WordPress; Amazon's own mechanism explanation linked. |
| 10023-F06 | PARTIALLY CLOSED / OPEN FOR LAUNCH | False transcript/chapters promise removed. Keeping Prefer video? is acceptable. Finished video and rendered verification remain requires_human. |

## Gates

- **GATE-LEGAL-ACCURACY — PASS**
- **GATE-LOCAL-ACCURACY — PASS**
- **GATE-TECHNICAL-SEO — FAIL** — 10023-F06
- **GATE-COMPLIANCE-RISK — PASS**
- **GATE-ANECDOTE-INTEGRITY — PASS**
- **CORNERSTONE-STRUCTURE — PASS**
- **CORNERSTONE-AEBP-VOICE — PASS**
- **CORNERSTONE-COMPANION-VIDEO — PASS**
- **CORNERSTONE-GBP-CONSISTENCY — PASS**

Passes for companion scope and draft Script labeling do not imply a finished video exists. GBP consistency checks shared claims only. Technical FAIL means not yet verified for launch, not that emitted schema is proven absent.

## Remaining finding: 10023-F06 — Type B

- **Finding:** “🎥 Video in production. It will appear here once it's live.”
- **Root cause:** Remaining production/verification dependency, not a current copy defect. The revised draft-stage wording is truthful. No finished recording or lite_youtube embed is present. Both unauthenticated draft preview URLs were retried this round and returned HTTP 404. Emitted schema/canonical, responsive rendering, editor round-trip validation and actual recording/transcript agreement cannot yet be cleared. Claude correctly retained requires_human; this review does not silently resolve it.
- **Fix:** Keep "Video Script" and the accurate in-production notice until the recording exists. At launch replace the placeholder with the real video embed in a native wp:shortcode block; no ID may be invented. Check the recording/SRT before using "Video Transcript". On the blog, use "Prefer video? Watch the companion video below or visit the video page." with the actual link; mention chapters only when supplied. Check both rendered pages, applicable emitted schema, canonicals, internal links and mobile layout, then perform Brian’s final read.
- **Future prevention:** Keep draft-copy clearance separate from final launch clearance. Record actual rendered-page evidence before changing this gate to PASS.

## Scored categories

Editorial estimates; passing content scores do not override the open technical gate.

| Category | Estimate / threshold | Result | What works | What holds it back |
|---|---:|---|---|---|
| SCORE-SEO | 94 / 90 | PASS | Clear owner-side intent, useful internal links, descriptive metadata and distinct liability-guide scope. | Rendered canonical and production routes await launch verification. |
| SCORE-GEO | 96 / 95 | PASS | Answer-first structure, five FAQs and fact table now retain legal scope, reporting attribution and survey period. | Emitted structured data remains unverified. |
| SCORE-EEAT | 96 / 95 | PASS | Documented AEBP experience, narrower legal claims, explicit professional judgment and removed UK pricing claim. | No new content evidence gap found; final media verification remains pending. |
| SCORE-READABILITY | 94 / 90 | PASS | Actionable route audit, checklist and comparison table; misleading slogan removed. | Six-column table still needs a mobile rendering check; duplicate production notice can optionally be shortened. |
| SCORE-CONVERSION | 92 / 85 | PASS | Relevant package-complaint CTA, live conversion path verified earlier this session, truthful draft-stage video notice. | Finished video is still unavailable. |
| SCORE-OVERALL | 95 / 95 | PASS | All substantive prior copy findings resolved; complete required cornerstone structure. | Publication remains held solely for the technical/production finding; this estimated content score is not publication authorization. |

## Strengths Worth Preserving

- Matches the October plan's owner-side prevention intent and avoids duplicating the liability guide.
- Required structure present: answer-first, facts, body, documented AEBP observation, before-holiday checklist, five aebp-faq questions, sources, closing cta-primary.
- All three new AEBP observations are documented in the Oct 9 anecdote log; no invented keypad-performance example.
- Comparison table acknowledges shared codes, oversize parcels, outages and carrier limitations; relative costs avoid recycled unsupported 2014 prices.
- Useful links to live liability/security guides and consultation path; native Gutenberg source structure and descriptive image alt present.
- Risk reduction, statute scope, professional opinion and draft-stage video status are now stated accurately.
- Both revised Video Script blocks match exactly at 241 words by whitespace count.

## Claim provenance

- **10023-C01 — documented:** At AEBP, package theft is one of the most common complaints we hear from tenants. Source: knowledge/company/anecdote-log.md, 2026-10-09 entry. Documented complaint-frequency wording, not a #1 ranking.
- **10023-C02 — documented:** When we asked our local post office what owners can do, the best advice they had was a PO box. Source: knowledge/company/anecdote-log.md, 2026-10-09 entry. Reported conversation, not national USPS policy. Blog section/FAQ and script variants covered.
- **10023-C03 — documented:** We manage 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay. Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt. Live company source rechecked after cached overview's review date.
- **10023-C04 — documented:** None of the buildings we currently manage use smart package lockers Source: knowledge/company/anecdote-log.md, 2026-10-09 entry. Confirmed company fact; no locker-performance experience is implied.
- **10023-C05 — documented:** We took two lessons from that conversation. Source: knowledge/company/anecdote-log.md, 2026-10-09 entry. Professional interpretation following a documented conversation; does not establish a successful AEBP intervention.

## Article fixes

- 10023-F06: Keep "Video Script" and the accurate in-production notice until the recording exists. At launch replace the placeholder with the real video embed in a native wp:shortcode block; no ID may be invented. Check the recording/SRT before using "Video Transcript". On the blog, use "Prefer video? Watch the companion video below or visit the video page." with the actual link; mention chapters only when supplied. Check both rendered pages, applicable emitted schema, canonicals, internal links and mobile layout, then perform Brian’s final read.

## Operating System improvements

- Add a narrowly sourced package-theft/security knowledge note separating lock duties, closer best practice, deposit acceptance duties and property-specific storage requirements. Do not infer statutory absence from one section. Target: `knowledge/laws/package-theft-and-building-access.md`. Deferred; not a new content blocker.
- Add a regression case preserving 'believed/apparent' when a reported incident is summarized in a Key Facts table. Target: `tests/editorial/`. Deferred; not a new content blocker.
- Define draft-stage versus launch-stage technical checks for unrecorded companion videos while retaining the final publication gate. Target: `reviews/video-review.md`. Deferred; not a new content blocker.
- Declare the JSON schema release version explicitly; 1.0.0 currently follows existing artifacts rather than an explicit schema-version constant. Target: `automation/schemas/review.schema.json`. Deferred; not a new content blocker.

## Review context and limits

Follow-up Pre-Publish Audit for Monday October 12, reviewed October 9 Pacific. Read 01-review.md/json and 02-revision-response.md/json and independently retrieved fresh full AEBP-Dev snapshots. Current WordPress post_modified: 2026-10-09 18:21:30, timezone not supplied; no revision ID or modified_gmt returned. Content review clear; publication recommendation remains hold_pending_fixes for 10023-F06 only. No new blocking copy findings.

Prior finding verification:
10023-F01 — CLOSED — Risk-reduction wording verified in Quick Answer, camera table/bullet, excerpt, conclusion, FAQ and both scripts. Revised package notes/GBP/social/SMS no longer use the flagged prevention claims.
10023-F02 — CLOSED — Statutory lock provision and closer best practice separated in Step One/checklist; retrofit caveat and security-guide link present.
10023-F03 — CLOSED — Quick Answer, Key Facts, FAQ 2 and conclusion now limit the negative mandate statement to §1941.3 itself.
10023-F04 — CLOSED — Key Facts now attributes Berkeley master-key belief to the building manager; both NBC links retained.
10023-F05 — CLOSED — US terms must be confirmed; UK price tier and ASK4 link removed from WordPress; Amazon's own mechanism explanation linked.
10023-F06 — PARTIALLY CLOSED / OPEN FOR LAUNCH — False transcript/chapters promise removed. Keeping Prefer video? is acceptable. Finished video and rendered verification remain requires_human.

Both response JSON files validate against revision-response.schema.json, answer every prior finding exactly once and reference the correct original-review timestamp. No rejected or unanswered findings. The requires_human items are explicitly preserved.

Local repository clean before new artifacts; HEAD 8d19435b130d5846c7157516279476b168f0948b; HEAD...origin/main 0/0 against local tracking ref. No remote fetch or new GitHub-main verification claimed this round. Diff from the initial reviewed commit e035aa64a04a568d7a166172b7fcc87afee5c1e0 shows no changes in docs, skills, schemas, relevant manifests or knowledge; the standards and evidence read and verified earlier in this same conversation remain applicable. Legal/source checks from round 01 are reused for unchanged claims and the exact narrower replacements; no new legal claim was introduced. Official Legislature-site access was blocked in round 01; statutory mirrors were used as recorded there. Schema version 1.0.0 follows existing artifacts; explicit version-declaration improvement remains deferred.

Native block-comment nesting and attribute JSON rechecked without detected errors. Full page source, headings, FAQs, resource links, CTA, terms, metadata, hero alt and video template reviewed. This does not prove Gutenberg editor validation or emitted schema. Both scripts are identical, 241 words by whitespace count. No lite_youtube embed. Both unauthenticated draft previews returned HTTP 404 on this round's retry; authenticated rendering, schema/canonical and mobile checks remain open. Updated media 10024 alt accurately describes an open keypad door. No video transcript verification claimed.

Reviewed revised Week 2 package notes for shared-claim propagation, including HeyGen script, YouTube description, future lead-in, GBP, Facebook, Instagram, X, LinkedIn, Nextdoor and SMS. This is claim-consistency review, not channel-specific publishing clearance. Nonblocking housekeeping: notes still call the revised script '~215 words, ~80 sec'; source count is 241 and runtime should come from the render. Historical source list still lists ASK4 despite its removal from the article: label it reviewed/not used, or replace with the Amazon source. No need for a further copy-revision loop for these housekeeping items.

All first-person experience provenance remains documented in the Oct 9 anecdote log/company sources; no owner_verified inference. The newly labeled 'In our view' recommendation is professional opinion, not a claimed AEBP success case. No new anecdote introduced.

Post 2804 changes mentioned by Claude are outside this two-post review and are not cleared here. A separate review can be commissioned; the response's suggestion is not authority to expand the current task. Proposed knowledge/standards/schema improvements remain recommendations, not prerequisites for shipping this corrected copy. No standards, knowledge, WordPress content or schedules changed in this review.

Both posts remain draft with Oct 9 stored dates, not scheduled for Oct 12. Next action is video production and authenticated preview/launch verification, then Brian's final read. An additional prose rewrite response is not needed now. When the production evidence is ready, record it in the next response round and perform the final launch review. No publication authorization is granted.

## Recommendation

**Hold pending production/technical completion only.** No further copy rewrite requested. Complete the recording, verify the actual transcript and rendered pages, then obtain Brian's final read.

