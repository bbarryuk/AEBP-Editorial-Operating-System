# Pre-Publish Audit — 10516

**Leak Calls in Rainy Season Explained for Landlords (Video)** · November 20, 2026 · ChatGPT GPT-6 · **HOLD PENDING FIXES**

Reviewed against docs/01 v0.5, docs/02 v0.2, docs/03 v0.3 and docs/07 v0.1. Companion post: 10515.

## Gated categories

### GATE-LEGAL-ACCURACY — FAIL
- **10516-F02 (A)** Quote: "the repair clock starts when you get notice". Root cause: Civil Code 1942(a) is specific to notice of untenantable conditions; phrasing sweeps in all reports. **Fix:** Replace 'the repair clock starts when you get notice' with 'Once you receive notice of a condition affecting habitability, respond within a reasonable time for the circumstances; document and investigate every leak report.'
- **10516-F03 (A)** Quote: "Emergency entry without notice (§1954)". Root cause: Operational emergency classification is not by itself a legal determination that emergency entry is warranted. **Fix:** Replace 'Emergency entry without notice (§1954)' with 'Emergency entry without advance notice only where circumstances constitute an actual emergency under §1954; otherwise use statutory notice or applicable consent.'

### GATE-LOCAL-ACCURACY — PASS


### GATE-TECHNICAL-SEO — FAIL
- **10516-F07 (B)** Quote: "Video in production. Check back soon.". Root cause: Video embed, chapter links and finished transcript not yet present. **Fix:** Keep draft pending final embed and script-to-recording verification.

### GATE-COMPLIANCE-RISK — PASS


### GATE-ANECDOTE-INTEGRITY — PASS

The November 20 anecdote-log entry documents Brian's confirmation of four weather-related maintenance requests in Nov 16–20 versus zero in the four prior comparable weekday periods (including the exclusions), the wind-driven window/slider observation, and AEBP's same-day active-leak vendor policy. **Original findings 10516-F04 and 10516-F05 withdrawn.** Source: `knowledge/company/anecdote-log.md (2026-11-20 entry; commit 267c3e715cc182992f59a391da01584514dd8dfb)`.

## Scored categories (estimates)
- SCORE-SEO: 85/100 (threshold 90, FAIL). Clear searchable heading and internal links; gap: Unfinished video/schema/metadata not fully checked.
- SCORE-GEO: 90/100 (threshold 95, FAIL). Direct answers and practical steps; gap: Qualify statutory and operational claims.
- SCORE-EEAT: 95/100 (threshold 95, PASS). The claims are documented by Brian in the anecdote log; remaining legal and production issues are evaluated separately.
- SCORE-READABILITY: 94/100 (threshold 90, PASS). Clear triage categories and scannable sections; gap: Some overgeneralized legal phrasing.
- SCORE-CONVERSION: 92/100 (threshold 85, PASS). Relevant CTA and correct maintenance number; gap: Avoid unconditional guarantees.
- SCORE-OVERALL: 88/100 (threshold 95, FAIL). Useful local landlord topic; gap: Publication blockers remain.

## Strengths worth preserving
- Practical three-tier triage and seasonal checklist
- Cross-linking of educational article and video
- Citations to relevant California codes and clear AEBP contact path

## Article fixes
- 10516-F02: Replace 'the repair clock starts when you get notice' with 'Once you receive notice of a condition affecting habitability, respond within a reasonable time for the circumstances; document and investigate every leak report.'
- 10516-F03: Replace 'Emergency entry without notice (§1954)' with 'Emergency entry without advance notice only where circumstances constitute an actual emergency under §1954; otherwise use statutory notice or applicable consent.'
- Do not publish a video page without final embed and matching transcript/chapters.

## Operating System improvements
- Anecdote evidence is now recorded in knowledge/company/anecdote-log.md. Refresh knowledge/company/overview.md on its regular review cycle.

## Verification limit
Official Legislative Information URLs returned HTTP 403. Statutory text was cross-checked with 2026 FindLaw and California DRE guidance; live official-source verification remains outstanding. The date/volume claims are now directly owner-confirmed in the anecdote log, although an underlying maintenance export was not separately reviewed.

## Recommendation
**Hold pending fixes.** Re-review both the article and the video script/page together following Claude revisions. Human final read remains required.

## Addendum — Anecdote evidence confirmed (November 20, 2026)

The missing anecdote entry was found in `knowledge/company/anecdote-log.md (2026-11-20 entry; commit 267c3e715cc182992f59a391da01584514dd8dfb)`. Findings 10516-F04 and 10516-F05 are **withdrawn**, GATE-ANECDOTE-INTEGRITY is **PASS**, and the documented numbers and same-day company policy should be preserved without unsupported generalization. Remaining legal/technical findings and HOLD recommendation are unchanged.
