# Follow-up Editorial Review — Post 10113

**Rental Property Lighting and CPTED for East Bay Landlords (Video, 2 min)**

Reviewed October 16, 2026 · Pre-Publish Audit · ChatGPT (Codex)

**Recommendation: HOLD PENDING FIXES / RELEASE VERIFICATION.** Original wording fixes are verified. Both posts are now scheduled; this review does not change that schedule.

## Snapshot and standards

Follow-up Pre-Publish Audit. Live WordPress snapshot modified 2026-10-16 17:28:07; status future, scheduled post_date 2026-10-19 00:00:00 (site-local; connector supplies no timezone/GMT). No revision ID returned. Current repo HEAD 5a07e8689a77605de017093c8b52652113bd3b89; clean before this review, zero commits ahead of locally recorded origin/main; no remote fetch. Standards and schemas unchanged from review 01 (git diff checked). Sources and legal verification from review 01 in this same conversation retained for unchanged claims; no new legal claims introduced. CLOSED: 10113-F01. 10113-F02: partially resolved, remains open pending release verification. No new substantive content findings. Response files predate the video swap and incorrectly describe the current posts as drafts without videos. Current package notes supersede that production detail. Local SRT Safer Rentals After Dark-caption.en_US.srt matches both transcript blocks after punctuation/whitespace normalization; chapter starts agree with SRT (0:00, 0:06, 0:28, 0:51, 1:12, 1:30). Local video exists; audio and complete visual playback not independently reviewed. Runtime 1:45 comes from package notes; 2 min is reasonable rounding, not independently measured. Both block-comment stacks balance, which does not establish editor validation. Browser inventory has no existing authenticated preview tabs; web-reader access to both future-post URLs and YouTube failed. Video private-until-launch status is documented in package notes, not independently confirmed through YouTube. Neither publication schedules nor WordPress content changed. Both 02-revision-response.json files fail the current response schema: unexpected top-level recommendation; missing summary, requires_human_review and recommendation_to_brian. Every original finding does have a disposition and the response timestamps match review 01. Because requires_human dispositions remain, requires_human_review must be true. Correct the machine-readable handoff without silently clearing those items. Proposed replacement fields: "summary": "Content fixes applied; video and transcript now added. Rendered preview, schema, mobile and public playback checks remain unresolved.", "requires_human_review": true, "recommendation_to_brian": "hold_for_brian_decision"; remove the unsupported recommendation key. Preserve historical responses; record the correction in a new response/addendum rather than silently rewriting prior history.

Standards: docs/01 v0.5; docs/02 v0.2; docs/03 v0.3; docs/07 v0.1; applicable manifest v0.1. JSON schema convention v1.0.0.

## Prior dispositions

- **10113-F01 — CLOSED:** best-practice label is in both the takeaway and transcript; canopy takeaway is clarified.
- **10113-F02 — PARTIALLY RESOLVED, OPEN:** actual embed and matching transcript are present; rendered release checks and public playback remain pending.

Every prior finding received a disposition; none rejected. Human-required checks have not been silently cleared.

## Gates

- **GATE-LEGAL-ACCURACY: PASS**
- **GATE-LOCAL-ACCURACY: PASS**
- **GATE-TECHNICAL-SEO: FAIL** — 10113-F02
- **GATE-COMPLIANCE-RISK: PASS**
- **GATE-ANECDOTE-INTEGRITY: PASS**
- **VIDEO-TRANSCRIPT-LITERAL: PASS**
- **VIDEO-CONSISTENCY: PASS**

Transcript literalness PASS is supported by supplied SRT comparison, not independent listening to the recording.

## Open findings

### 10113-F02 — Type B

- **Finding:** `[lite_youtube videoid="eywhT2_YUsk" title="Rental Property Lighting: The Low-Cost Security Check East Bay Landlords Overlook"]`
- **Root cause:** PARTIALLY RESOLVED / still open. Live snapshots now contain the video embed and Video Transcript, superseding the response's statement that no video exists. Both transcripts match the local SRT word for word after punctuation normalization. Package notes record the YouTube video as private until October 19, 2026 at 07:00 UTC. Public playback, authenticated rendered preview, editor validation, generated schema and mobile presentation have not been verified. Draft/future URLs remain inaccessible to the web reader. No proof of a markup or schema defect is claimed.
- **Fix:** Keep the actual embed and checked transcript. Before scheduled release, verify authenticated desktop/mobile previews, WordPress block validation, generated Article/FAQ output for 10112 and applicable VideoObject output for 10113, internal-link destinations, and public video playback at the scheduled launch. Record results against this finding. If release checks cannot be completed, Brian should decide whether to defer the scheduled publication; this review did not change its schedule.
- **Future prevention:** Update production evidence when the video is added; do not reuse the earlier no-video status or infer rendered output from metadata.

## Scores

Editorial estimates; passing scores do not override the technical gate.

| Category | Estimate / threshold | Status | Working | Holding it back |
|---|---|---|---|---|
| SCORE-SEO | 94 / 90 | PASS | Clear watch-page title and populated metadata. | Rendered output and public video playback remain unverified. |
| SCORE-GEO | 96 / 95 | PASS | Scannable takeaways and resources. | No remaining scored-content blocker identified; technical release checks are separate. |
| SCORE-EEAT | 96 / 95 | PASS | Tenant-reporting statements match the October 16 internal record. | No remaining scored-content blocker identified; technical release checks are separate. |
| SCORE-READABILITY | 95 / 90 | PASS | Short, conversational script; consistently uses we. | No remaining scored-content blocker identified; technical release checks are separate. |
| SCORE-CONVERSION | 95 / 85 | PASS | Read-the-guide link and relevant consultation CTA. | No remaining scored-content blocker identified; technical release checks are separate. |
| SCORE-OVERALL | 95 / 95 | PASS | Coherent companion page and script matching the article. | Content scores meet thresholds; technical release gate still fails independently. |

## Strengths Worth Preserving

- Correct Video Script label before recording.
- Script matches the parent and preserves documented AEBP practice.
- Takeaways, resources, read-the-guide link and CTA give the watch page independent value.
- All original wording findings are fixed in live WordPress; both transcripts match each other and the supplied SRT.
- Actual video embeds and production metadata replace the earlier placeholders.

## Claim provenance

Unchanged claims remain documented; none assigned owner_verified by the AI reviewer.

- **10113-C01: documented.** “We manage 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay. Let's talk about how your building handles lighting, doors and repair reports.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt (retrieved October 16, generated October 8, 2026)

- **10113-C02: documented.** “At AEBP, our tenants see the property after dark every night. We mostly see it in daylight. So we ask them to report any light that's out or a door that won't latch. We can only fix what we know about. And once someone reports it, we do know about it.” Source: knowledge/company/anecdote-log.md — 2026-10-16 entry; same-day broken-lock policy additionally documented 2026-09-30

## Article fixes

- 10113-F02: Keep the actual embed and checked transcript. Before scheduled release, verify authenticated desktop/mobile previews, WordPress block validation, generated Article/FAQ output for 10112 and applicable VideoObject output for 10113, internal-link destinations, and public video playback at the scheduled launch. Record results against this finding. If release checks cannot be completed, Brian should decide whether to defer the scheduled publication; this review did not change its schedule.

## Operating System improvements

- Add a sourced CPTED/security-lighting reference covering guideline dimensions, permit-specific assessment requirements and the limits of the lighting research; existing law knowledge files do not cover this topic. Target: `knowledge/laws/security-lighting-cpted.md`.

- Define how technical gates distinguish unavailable draft previews from proven markup/schema defects, and how content-only clearance differs from production release. Target: `docs/03-Review-Format.md`.

- Both 02-revision-response.json files fail the current response schema: unexpected top-level recommendation; missing summary, requires_human_review and recommendation_to_brian. Every original finding does have a disposition and the response timestamps match review 01. Because requires_human dispositions remain, requires_human_review must be true. Correct the machine-readable handoff without silently clearing those items. Proposed replacement fields: "summary": "Content fixes applied; video and transcript now added. Rendered preview, schema, mobile and public playback checks remain unresolved.", "requires_human_review": true, "recommendation_to_brian": "hold_for_brian_decision"; remove the unsupported recommendation key. Preserve historical responses; record the correction in a new response/addendum rather than silently rewriting prior history. Target: `reviews/posts/10113/02-revision-response.json`.

## Next step

Provide a schema-valid 04 revision response covering the remaining findings and completed release checks. Preserve 01/02 history. Brian still makes the final publication decision; both WordPress posts currently show scheduled publication for October 19 at 00:00 site-local time.

