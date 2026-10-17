# Follow-up Editorial Review — Post 10112

**Lighting, Sightlines and Access: Crime Prevention Through Environmental Design for East Bay Rentals**

Reviewed October 16, 2026 · Pre-Publish Audit · ChatGPT (Codex)

**Recommendation: HOLD PENDING FIXES / RELEASE VERIFICATION.** Original wording fixes are verified. Both posts are now scheduled; this review does not change that schedule.

## Snapshot and standards

Follow-up Pre-Publish Audit. Live WordPress snapshot modified 2026-10-16 17:24:17; status future, scheduled post_date 2026-10-19 00:00:00 (site-local; connector supplies no timezone/GMT). No revision ID returned. Current repo HEAD 5a07e8689a77605de017093c8b52652113bd3b89; clean before this review, zero commits ahead of locally recorded origin/main; no remote fetch. Standards and schemas unchanged from review 01 (git diff checked). Sources and legal verification from review 01 in this same conversation retained for unchanged claims; no new legal claims introduced. CLOSED: 10112-F01, 10112-F02, 10112-F03. 10112-F04: partially resolved, remains open pending release verification. NEW: 10112-F05, chapter links promised but companion contains plain timestamps. Response files predate the video swap and incorrectly describe the current posts as drafts without videos. Current package notes supersede that production detail. Local SRT Safer Rentals After Dark-caption.en_US.srt matches both transcript blocks after punctuation/whitespace normalization; chapter starts agree with SRT (0:00, 0:06, 0:28, 0:51, 1:12, 1:30). Local video exists; audio and complete visual playback not independently reviewed. Runtime 1:45 comes from package notes; 2 min is reasonable rounding, not independently measured. Both block-comment stacks balance, which does not establish editor validation. Browser inventory has no existing authenticated preview tabs; web-reader access to both future-post URLs and YouTube failed. Video private-until-launch status is documented in package notes, not independently confirmed through YouTube. Neither publication schedules nor WordPress content changed. Both 02-revision-response.json files fail the current response schema: unexpected top-level recommendation; missing summary, requires_human_review and recommendation_to_brian. Every original finding does have a disposition and the response timestamps match review 01. Because requires_human dispositions remain, requires_human_review must be true. Correct the machine-readable handoff without silently clearing those items. Proposed replacement fields: "summary": "Content fixes applied; video and transcript now added. Rendered preview, schema, mobile and public playback checks remain unresolved.", "requires_human_review": true, "recommendation_to_brian": "hold_for_brian_decision"; remove the unsupported recommendation key. Preserve historical responses; record the correction in a new response/addendum rather than silently rewriting prior history.

Standards: docs/01 v0.5; docs/02 v0.2; docs/03 v0.3; docs/07 v0.1; applicable manifest v0.1. JSON schema convention v1.0.0.

## Prior dispositions

- **10112-F01 — CLOSED:** Bottom Line, FAQ 5 and Key Facts now use voluntary self-audit/project-specific permitting wording.
- **10112-F02 — CLOSED:** owner checklist and companion takeaway explicitly refer to clear space beneath tree canopies; updated Instagram copy verified in package notes.
- **10112-F03 — CLOSED:** best-practice label appears in both transcripts and the supplied SRT.
- **10112-F04 — PARTIALLY RESOLVED, OPEN:** video and matching transcripts now exist; rendered release checks still pending.

Every prior finding received a disposition; none rejected. Human-required checks have not been silently cleared.

## Gates

- **GATE-LEGAL-ACCURACY: PASS**
- **GATE-LOCAL-ACCURACY: PASS**
- **GATE-TECHNICAL-SEO: FAIL** — 10112-F04, 10112-F05
- **GATE-COMPLIANCE-RISK: PASS**
- **GATE-ANECDOTE-INTEGRITY: PASS**
- **CORNERSTONE-STRUCTURE: PASS**
- **CORNERSTONE-AEBP-VOICE: PASS**
- **CORNERSTONE-COMPANION-VIDEO: PASS**
- **CORNERSTONE-GBP-CONSISTENCY: PASS**

Companion review PASS means separate review performed, not release clearance. GBP consistency is carried forward after checking the updated package notes.

## Open findings

### 10112-F04 — Type B

- **Finding:** `[lite_youtube videoid="eywhT2_YUsk" title="Rental Property Lighting: The Low-Cost Security Check East Bay Landlords Overlook"]`
- **Root cause:** PARTIALLY RESOLVED / still open. Live snapshots now contain the video embed and Video Transcript, superseding the response's statement that no video exists. Both transcripts match the local SRT word for word after punctuation normalization. Package notes record the YouTube video as private until October 19, 2026 at 07:00 UTC. Public playback, authenticated rendered preview, editor validation, generated schema and mobile presentation have not been verified. Draft/future URLs remain inaccessible to the web reader. No proof of a markup or schema defect is claimed.
- **Fix:** Keep the actual embed and checked transcript. Before scheduled release, verify authenticated desktop/mobile previews, WordPress block validation, generated Article/FAQ output for 10112 and applicable VideoObject output for 10113, internal-link destinations, and public video playback at the scheduled launch. Record results against this finding. If release checks cannot be completed, Brian should decide whether to defer the scheduled publication; this review did not change its schedule.
- **Future prevention:** Update production evidence when the video is added; do not reuse the earlier no-video status or infer rendered output from metadata.

### 10112-F05 — Type A

- **Finding:** `visit the video page with chapter links and a full transcript.`
- **Root cause:** New video-swap wording promises clickable chapter links, but 10113's six chapter entries contain bold timestamp text only, with no anchors. This is a small factual UI-description regression (STD-ACCURATE), not a problem with the chapter timing.
- **Fix:** Replace "visit the video page with chapter links and a full transcript" with "visit the video page with chapter timestamps and a full transcript". Alternatively, implement and verify the actual timestamp links.
- **Future prevention:** Compare feature descriptions with the companion page's actual markup during video swaps.

## Scores

Editorial estimates; passing scores do not override the technical gate.

| Category | Estimate / threshold | Status | Working | Holding it back |
|---|---|---|---|---|
| SCORE-SEO | 94 / 90 | PASS | Specific search intent and complete Yoast fields. | Rendered output and public video playback remain unverified. |
| SCORE-GEO | 96 / 95 | PASS | Answer-first summary, sourced facts table and five FAQs. | No remaining scored-content blocker identified; technical release checks are separate. |
| SCORE-EEAT | 96 / 95 | PASS | Documented tenant-reporting practice and careful limits on crime-reduction evidence. | No remaining scored-content blocker identified; technical release checks are separate. |
| SCORE-READABILITY | 93 / 90 | PASS | Actionable walk-through and controls tables. | Long Quick Answer and minor chapter-links wording correction; no remaining original prose blocker. |
| SCORE-CONVERSION | 95 / 85 | PASS | Relevant CTA with a live consultation destination. | No remaining scored-content blocker identified; technical release checks are separate. |
| SCORE-OVERALL | 95 / 95 | PASS | Useful local maintenance guide with verified company experience. | Content scores meet thresholds; technical release gate still fails independently. |

## Strengths Worth Preserving

- AEBP observations are documented, including the newsletter actually being sent.
- Relative costs are explicitly professional opinion rather than invented quotes.
- Crime research is not turned into a promise that an individual building is safe.
- Complete cornerstone structure, five FAQs, contextual internal links and focused CTA.
- All original wording findings are fixed in live WordPress; both transcripts match each other and the supplied SRT.
- Actual video embeds and production metadata replace the earlier placeholders.

## Claim provenance

Unchanged claims remain documented; none assigned owner_verified by the AI reviewer.

- **10112-C01: documented.** “At AEBP, our tenants see the property after dark every night. We mostly see it in daylight. So we ask them to report any light that's out or a door that won't latch. We can only fix what we know about. And once someone reports it, we do know about it.” Source: knowledge/company/anecdote-log.md — 2026-10-16 entry; same-day broken-lock policy additionally documented 2026-09-30

- **10112-C02: documented.** “Our tenants see the property after dark every night; we mostly see it in daylight. So we rely on them to tell us what's wrong. Our October tenant newsletter asks residents to submit a maintenance request whenever an exterior light is out, flickering or on a timer that's no longer set right, and to report any front door, gate or lobby door that isn't latching on its own. The line we use with tenants: we can only fix what we know about.” Source: knowledge/company/anecdote-log.md — 2026-10-16 entry; same-day broken-lock policy additionally documented 2026-09-30

- **10112-C03: documented.** “Two things follow from that. First, a tenant report is notice. Once someone tells us an entry light is out or a lobby door won't latch, we know about it, and the clock is running. That's why we treat a broken entry or lobby lock as an emergency, with a vendor sent the same day. Company policy. Second, making it easy for tenants to report is part of the security plan, not just customer service. If tenants don't know how to report a dark walkway, or don't think anyone will act on it, the problem stays invisible to the owner.” Source: knowledge/company/anecdote-log.md — 2026-10-16 entry; same-day broken-lock policy additionally documented 2026-09-30

- **10112-C04: documented.** “We manage 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay, with a 24/7 bilingual maintenance line for tenants to report problems. Let's talk about how your building handles lighting, doors and repair reports.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt (retrieved October 16, generated October 8, 2026)

## Article fixes

- 10112-F04: Keep the actual embed and checked transcript. Before scheduled release, verify authenticated desktop/mobile previews, WordPress block validation, generated Article/FAQ output for 10112 and applicable VideoObject output for 10113, internal-link destinations, and public video playback at the scheduled launch. Record results against this finding. If release checks cannot be completed, Brian should decide whether to defer the scheduled publication; this review did not change its schedule.

- 10112-F05: Replace "visit the video page with chapter links and a full transcript" with "visit the video page with chapter timestamps and a full transcript". Alternatively, implement and verify the actual timestamp links.

## Operating System improvements

- Add a sourced CPTED/security-lighting reference covering guideline dimensions, permit-specific assessment requirements and the limits of the lighting research; existing law knowledge files do not cover this topic. Target: `knowledge/laws/security-lighting-cpted.md`.

- Define how technical gates distinguish unavailable draft previews from proven markup/schema defects, and how content-only clearance differs from production release. Target: `docs/03-Review-Format.md`.

- Both 02-revision-response.json files fail the current response schema: unexpected top-level recommendation; missing summary, requires_human_review and recommendation_to_brian. Every original finding does have a disposition and the response timestamps match review 01. Because requires_human dispositions remain, requires_human_review must be true. Correct the machine-readable handoff without silently clearing those items. Proposed replacement fields: "summary": "Content fixes applied; video and transcript now added. Rendered preview, schema, mobile and public playback checks remain unresolved.", "requires_human_review": true, "recommendation_to_brian": "hold_for_brian_decision"; remove the unsupported recommendation key. Preserve historical responses; record the correction in a new response/addendum rather than silently rewriting prior history. Target: `reviews/posts/10112/02-revision-response.json`.

## Next step

Provide a schema-valid 04 revision response covering the remaining findings and completed release checks. Preserve 01/02 history. Brian still makes the final publication decision; both WordPress posts currently show scheduled publication for October 19 at 00:00 site-local time.

