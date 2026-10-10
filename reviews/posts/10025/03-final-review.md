# Follow-up Pre-Publish Audit — Post 10025

**How to Stop Package Theft in an Apartment Building (Video)**

**Copy fixes verified. Hold publication for production checks only.**

Reviewed October 9, 2026 Pacific for Monday October 12. WordPress modified 2026-10-09 18:21:32 (timezone unspecified), status draft. Repository `8d19435b130d5846c7157516279476b168f0948b`, clean before artifacts. Standards: docs/01 v0.5, docs/02 v0.2, docs/03 v0.3, docs/07 v0.1, applicable manifest v0.1. Reviewer: ChatGPT / Codex.

## Prior findings and dispositions

| Finding | Result | Verified evidence |
|---|---|---|
| 10025-F01 | CLOSED | Intro, coverage list, first takeaway, excerpt, metadescription and script use qualified prevention wording. |
| 10025-F02 | CLOSED | Professional-opinion/closer labels and layout caveat present; both scripts now refer to unexpected or unverified visitors. |
| 10025-F03 | OPEN FOR LAUNCH | Accurate placeholder/Script label retained; no recording/embed or rendered-page verification available. Requires_human retained. |

## Gates

- **GATE-LEGAL-ACCURACY — PASS**
- **GATE-LOCAL-ACCURACY — PASS**
- **GATE-TECHNICAL-SEO — FAIL** — 10025-F03
- **GATE-COMPLIANCE-RISK — PASS**
- **GATE-ANECDOTE-INTEGRITY — PASS**
- **VIDEO-TRANSCRIPT-LITERAL — PASS**
- **VIDEO-CONSISTENCY — PASS**

Passes for companion scope and draft Script labeling do not imply a finished video exists. GBP consistency checks shared claims only. Technical FAIL means not yet verified for launch, not that emitted schema is proven absent.

## Remaining finding: 10025-F03 — Type B

- **Finding:** “🎥 Video in production. It will appear here once it's live.”
- **Root cause:** Remaining production/verification dependency, not a current copy defect. The revised draft-stage wording is truthful. No finished recording or lite_youtube embed is present. Both unauthenticated draft preview URLs were retried this round and returned HTTP 404. Emitted schema/canonical, responsive rendering, editor round-trip validation and actual recording/transcript agreement cannot yet be cleared. Claude correctly retained requires_human; this review does not silently resolve it.
- **Fix:** Keep "Video Script" and the accurate in-production notice until the recording exists. At launch replace the placeholder with the real video embed in a native wp:shortcode block; no ID may be invented. Check the recording/SRT before using "Video Transcript". On the blog, use "Prefer video? Watch the companion video below or visit the video page." with the actual link; mention chapters only when supplied. Check both rendered pages, applicable emitted schema, canonicals, internal links and mobile layout, then perform Brian’s final read.
- **Future prevention:** Keep draft-copy clearance separate from final launch clearance. Record actual rendered-page evidence before changing this gate to PASS.

## Scored categories

Editorial estimates; passing content scores do not override the open technical gate.

| Category | Estimate / threshold | Result | What works | What holds it back |
|---|---:|---|---|---|
| SCORE-SEO | 93 / 90 | PASS | Companion metadata, topic-specific title and clear full-guide link. | Rendered canonical and production routes await launch verification. |
| SCORE-GEO | 95 / 95 | PASS | Coverage/takeaways now retain risk-reduction and best-practice qualifications. | Emitted structured data remains unverified. |
| SCORE-EEAT | 95 / 95 | PASS | Documented AEBP observations and professionally labeled recommendations; no invented success story. | No new content evidence gap found; final media verification remains pending. |
| SCORE-READABILITY | 95 / 90 | PASS | Coherent revised script, consistent visitor wording and matched 241-word copies. | Final runtime is unknown until render; package notes undercount the script. |
| SCORE-CONVERSION | 91 / 85 | PASS | Full-guide link and consultation CTA provide a clear next step. | Finished video is still unavailable. |
| SCORE-OVERALL | 95 / 95 | PASS | Both substantive copy findings resolved; script and page qualifications aligned. | Publication remains held solely for the technical/production finding; this estimated content score is not publication authorization. |

## Strengths Worth Preserving

- Script matches the parent's script exactly; no existing cross-post text drift.
- Correct pre-recording Video Script label preserves transcript integrity.
- Category 629 and video-post-no-hero-with-sidebar template are set.
- AEBP experience claims are documented and the copy remains general education.
- Distinct coverage/takeaway/resource lists support readers alongside a future video.
- Risk reduction, statute scope, professional opinion and draft-stage video status are now stated accurately.
- Both revised Video Script blocks match exactly at 241 words by whitespace count.

## Claim provenance

- **10025-C01 — documented:** At AEBP, package theft is one of the most common complaints we hear from tenants. Source: knowledge/company/anecdote-log.md, 2026-10-09 entry. Documented complaint-frequency wording, not a #1 ranking.
- **10025-C02 — documented:** When we asked our local post office what owners can do, the best advice they had was a PO box. Source: knowledge/company/anecdote-log.md, 2026-10-09 entry. Reported conversation, not national USPS policy. Blog section/FAQ and script variants covered.
- **10025-C03 — documented:** AEBP manages 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay, with a 24/7 bilingual maintenance line. Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt. Live company source rechecked after cached overview's review date.

## Article fixes

- 10025-F03: Keep "Video Script" and the accurate in-production notice until the recording exists. At launch replace the placeholder with the real video embed in a native wp:shortcode block; no ID may be invented. Check the recording/SRT before using "Video Transcript". On the blog, use "Prefer video? Watch the companion video below or visit the video page." with the actual link; mention chapters only when supplied. Check both rendered pages, applicable emitted schema, canonicals, internal links and mobile layout, then perform Brian’s final read.

## Operating System improvements

- Add a narrowly sourced package-theft/security knowledge note separating lock duties, closer best practice, deposit acceptance duties and property-specific storage requirements. Do not infer statutory absence from one section. Target: `knowledge/laws/package-theft-and-building-access.md`. Deferred; not a new content blocker.
- Add a regression case preserving 'believed/apparent' when a reported incident is summarized in a Key Facts table. Target: `tests/editorial/`. Deferred; not a new content blocker.
- Define draft-stage versus launch-stage technical checks for unrecorded companion videos while retaining the final publication gate. Target: `reviews/video-review.md`. Deferred; not a new content blocker.
- Declare the JSON schema release version explicitly; 1.0.0 currently follows existing artifacts rather than an explicit schema-version constant. Target: `automation/schemas/review.schema.json`. Deferred; not a new content blocker.

## Review context and limits

Follow-up Pre-Publish Audit for Monday October 12, reviewed October 9 Pacific. Read 01-review.md/json and 02-revision-response.md/json and independently retrieved fresh full AEBP-Dev snapshots. Current WordPress post_modified: 2026-10-09 18:21:32, timezone not supplied; no revision ID or modified_gmt returned. Content review clear; publication recommendation remains hold_pending_fixes for 10025-F03 only. No new blocking copy findings.

Prior finding verification:
10025-F01 — CLOSED — Intro, coverage list, first takeaway, excerpt, metadescription and script use qualified prevention wording.
10025-F02 — CLOSED — Professional-opinion/closer labels and layout caveat present; both scripts now refer to unexpected or unverified visitors.
10025-F03 — OPEN FOR LAUNCH — Accurate placeholder/Script label retained; no recording/embed or rendered-page verification available. Requires_human retained.

Both response JSON files validate against revision-response.schema.json, answer every prior finding exactly once and reference the correct original-review timestamp. No rejected or unanswered findings. The requires_human items are explicitly preserved.

Local repository clean before new artifacts; HEAD 8d19435b130d5846c7157516279476b168f0948b; HEAD...origin/main 0/0 against local tracking ref. No remote fetch or new GitHub-main verification claimed this round. Diff from the initial reviewed commit e035aa64a04a568d7a166172b7fcc87afee5c1e0 shows no changes in docs, skills, schemas, relevant manifests or knowledge; the standards and evidence read and verified earlier in this same conversation remain applicable. Legal/source checks from round 01 are reused for unchanged claims and the exact narrower replacements; no new legal claim was introduced. Official Legislature-site access was blocked in round 01; statutory mirrors were used as recorded there. Schema version 1.0.0 follows existing artifacts; explicit version-declaration improvement remains deferred.

Native block-comment nesting and attribute JSON rechecked without detected errors. Full page source, headings, FAQs, resource links, CTA, terms, metadata, hero alt and video template reviewed. This does not prove Gutenberg editor validation or emitted schema. Both scripts are identical, 241 words by whitespace count. No lite_youtube embed. Both unauthenticated draft previews returned HTTP 404 on this round's retry; authenticated rendering, schema/canonical and mobile checks remain open. Updated media 10024 alt accurately describes an open keypad door. No video transcript verification claimed.

Reviewed revised Week 2 package notes for shared-claim propagation, including HeyGen script, YouTube description, future lead-in, GBP, Facebook, Instagram, X, LinkedIn, Nextdoor and SMS. This is claim-consistency review, not channel-specific publishing clearance. Nonblocking housekeeping: notes still call the revised script '~215 words, ~80 sec'; source count is 241 and runtime should come from the render. Historical source list still lists ASK4 despite its removal from the article: label it reviewed/not used, or replace with the Amazon source. No need for a further copy-revision loop for these housekeeping items.

All first-person experience provenance remains documented in the Oct 9 anecdote log/company sources; no owner_verified inference. The newly labeled 'In our view' recommendation is professional opinion, not a claimed AEBP success case. No new anecdote introduced.

Post 2804 changes mentioned by Claude are outside this two-post review and are not cleared here. A separate review can be commissioned; the response's suggestion is not authority to expand the current task. Proposed knowledge/standards/schema improvements remain recommendations, not prerequisites for shipping this corrected copy. No standards, knowledge, WordPress content or schedules changed in this review.

Both posts remain draft with Oct 9 stored dates, not scheduled for Oct 12. Next action is video production and authenticated preview/launch verification, then Brian's final read. An additional prose rewrite response is not needed now. When the production evidence is ready, record it in the next response round and perform the final launch review. No publication authorization is granted.

## Recommendation

**Hold pending production/technical completion only.** No further copy rewrite requested. Complete the recording, verify the actual transcript and rendered pages, then obtain Brian's final read.

