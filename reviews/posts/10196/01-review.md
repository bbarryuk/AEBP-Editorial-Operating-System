# Editorial Review — Post 10196

**How to Talk With Tenants About Safety Without Overpromising (Video)**

Recommendation: **HOLD PENDING FIXES**. Review mode: Pre-Publish Audit (draft content and metadata reviewed; rendered-page/schema clearance blocked).

Snapshot: draft; WordPress modified 2026-10-18 20:26:14 (timezone not supplied). Review date: October 18, 2026, America/Los_Angeles.

Standards: docs/01 v0.5; docs/02 v0.2; docs/03 v0.3; docs/07 v0.1; video manifest v0.1. Repository: `14e36e5f25f9b2290dee6b481bf983a1c7975e48`, dirty before review artifacts; existing anecdote-log change used and preserved.

## Gated categories

- **GATE-LEGAL-ACCURACY: FAIL** — 10196-F01, 10196-F02
- **GATE-LOCAL-ACCURACY: PASS**
- **GATE-TECHNICAL-SEO: FAIL** — 10196-F03
- **GATE-COMPLIANCE-RISK: PASS**
- **GATE-ANECDOTE-INTEGRITY: PASS**
- **VIDEO-TRANSCRIPT-LITERAL: PASS**
- **VIDEO-CONSISTENCY: PASS**

Compliance PASS concerns general-education framing only; it does not clear the legal errors. Production/preview failures are identified as such, not treated as proof that schema is absent.

## Findings and exact fixes

### 10196-F01 — Type A

**Finding:** Under California Civil Code section 1946.8, a lease can't limit a tenant's right to call for help, and a landlord can't penalize them for it.

**Root cause:** The script and legal takeaway omit the statutory conditions for protected calls; see §1946.8(b)–(d) and parent finding 10195-F02.

**Fix:** Script replacement: “Third, don't discourage calls for help. California Civil Code section 1946.8 protects calls about abuse, crime or an emergency when the caller believes help is needed. A lease can't restrict those calls, and a landlord can't penalize a tenant or resident for them.” Key takeaway replacement: “Civil Code §1946.8 protects calls about abuse, crime or an emergency when the caller believes assistance is necessary; lease restrictions and landlord penalties for protected calls are prohibited.”

**Future prevention:** Apply 10195-F02 to both scripts and the video key takeaways.

### 10196-F02 — Type A

**Finding:** A security report is notice: reply the same day, fix it, log it and watch for patterns

**Root cause:** The legal-resource context makes an unlimited notice statement and a same-day response instruction sound statutory. Same-day handling is documented AEBP policy for broken entry/lobby locks, not a universal legal repair deadline. Distinguish it from general best practice and §1941.3.

**Fix:** Key takeaway replacement: “Best practice: acknowledge security reports promptly, assess urgency, arrange needed repairs and document follow-up. Reports of covered lock deficiencies can provide notice under Civil Code §1941.3.” Fourth script paragraph: “Fourth, as a best practice, acknowledge security reports promptly, assess the urgency, arrange needed repairs and keep a record. A report about a required lock can give notice under California's lock statute; other reports may raise different duties.”

**Future prevention:** Preserve the documented AEBP same-day policy in its own paragraph; label the general workflow as best practice.

### 10196-F03 — Type A/B

**Finding:** 🎥 Video in production. It will appear here once it's live.

**Root cause:** A draft placeholder is appropriate while producing the video but does not satisfy publication readiness for a watch page. No recording is available to verify, and the browser preview returned a site 404. Generated VideoObject/schema and final rendering are unverified, not proved absent.

**Fix:** Keep this page in draft until the actual recording is embedded. Replace the placeholder with that playable embed; add chapter timestamps from the recording and use “Video Transcript” only after checking the text against the final audio. Verify authenticated rendering, schema, thumbnail, duration and the published parent link. Real video-dependent values cannot be invented in this review.

**Future prevention:** Require a production-completion check after the script review; maintain VIDEO-TRANSCRIPT-LITERAL.

## Scored categories

All scores are editorial estimates.

| Category | Estimate / minimum | Status | What's working | What's holding it back |
|---|---:|---|---|---|
| SCORE-SEO | 88 / 90 | FAIL | Focused query, populated Yoast fields and relevant internal links. | Final rendering/schema and video production unverified. |
| SCORE-GEO | 89 / 95 | FAIL | Answer-first structure and extractable facts/takeaways. | Compressed legal statements omit conditions; blog checklist absent or video not produced. |
| SCORE-EEAT | 92 / 95 | FAIL | Documented practitioner process and identifiable primary legal texts. | Overbroad legal phrasing limits reliability despite strong provenance. |
| SCORE-READABILITY | 96 / 90 | PASS | Plain language with scannable sections and short script. | Some legal shortcuts need precise wording without adding unnecessary complexity. |
| SCORE-CONVERSION | 89 / 85 | PASS | Relevant property-management CTA with live consultation destination. | Video promise cannot yet be fulfilled; final cross-links need checking. |
| SCORE-OVERALL | 90 / 95 | FAIL | Clear educational purpose and documented AEBP examples. | Blocking legal and production findings remain. |

## Strengths Worth Preserving

- The features-versus-outcomes framing gives readers usable replacement language.
- AEBP welcome-sheet, lock-triage and lease practices are documented; no invented incident is needed.
- O’Hara is presented as claims allowed to proceed, not a final damages verdict.
- The script is correctly labeled as a script while recording is pending.

## Claim provenance

- **10196-C01 — documented:** “At AEBP, every new tenant gets a welcome sheet with our 24/7 maintenance line, and a broken entry lock is an emergency, with a vendor sent the same day.” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; local working copy). Documented internal record; not AI owner verification.

- **10196-C02 — documented:** “Our lease asks tenants to research the neighborhood themselves. We describe the building, and how to reach us.” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; local working copy). Documented lease practice; final sentence is professional framing, not an independently verified universal listing-language policy.

- **10196-C03 — documented:** “We manage 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt. Documented internal record; not AI owner verification.

## Article fixes

- 10196-F01: The script and legal takeaway omit the statutory conditions for protected calls; see §1946.8(b)–(d) and parent finding 10195-F02.
- 10196-F02: The legal-resource context makes an unlimited notice statement and a same-day response instruction sound statutory
- 10196-F03: A draft placeholder is appropriate while producing the video but does not satisfy publication readiness for a watch page

## Operating System improvements

- Add a maintained security-duty reference separating lock-statute notice, guard foreseeability, general reasonable-care duties, protected police calls and incident warnings. Sources are available, so this system gap does not independently block these posts. Target: `knowledge/laws/landlord-security-duties.md`. Type C follow-up: yes.

- Add an explicit blocked/not-verified representation for rendered-page checks; the current PASS/FAIL schema forces incomplete checks into FAIL with explanatory evidence-gap text. Target: `automation/schemas/review.schema.json`. Type C follow-up: yes.

- Refresh the overdue company overview separately. Relevant 600+ units and maintenance facts were cross-checked this session; do not change the existing anecdote-log work during this review. Target: `knowledge/company/overview.md`. Type C follow-up: no.

## Evidence and review limits

Reviewed 2026-10-18 America/Los_Angeles. Full AEBP-Dev snapshots read, including content, metadata, terms, thumbnail and author. Post-modified values below are exactly as returned, with no timezone supplied; no revision ID or modified_gmt was returned. Repo HEAD 14e36e5f25f9b2290dee6b481bf983a1c7975e48; initially dirty because knowledge/company/anecdote-log.md has an existing uncommitted change (the current welcome-sheet entry was used); zero commits ahead of locally recorded origin/main, no remote fetch. Schema version 1.0.0 follows existing review artifacts; schema itself has no version constant. No WordPress edits. Native block comments balanced on both posts; this is not Gutenberg editor validation. Authenticated preview was unavailable: both attempted browser previews returned site 404 pages; layout, mobile appearance, rendered FAQ/VideoObject schema and canonical/indexing are not cleared. Featured media 10194 and descriptive alt present, image appearance not inspected. Main security guide and conversion destination loaded; package-theft destination fetch failed, not proof of a broken link; future parent/companion production links need final verification. Statutory text was read from Justia/Public.Law mirrors after official LegInfo endpoints returned 403; mirrors are not an independently certified current-law check. Case opinions read in full opinion reproductions; no exhaustive subsequent-case-treatment audit. O’Hara pleading-stage qualification is appropriately preserved. 1941.5/1941.6 24-hour duty is supportable for qualifying documented requests; this post does not enumerate all eligibility conditions. Megan's Law summary preserves other-law duties in FAQ 3. Local numbers verified from municipal pages/indexed municipal text; press-5 routing not independently verified. Fair Housing Institute list corroborates ‘safe neighborhood’ avoidance as industry guidance, not a statutory word ban. Live llms.txt corroborates 600+ units and maintenance service. Local October newsletter and week4 package notes inspected; no private lease details copied. Scores are editorial estimates, not a measured rubric. WordPress post_modified: 2026-10-18 20:26:14. VIDEO-TRANSCRIPT-LITERAL passes draft labeling only: the block correctly says Video Script. No audio was available. VIDEO-CONSISTENCY passes because the scripts match; their shared errors remain legal failures. Apply parent revisions to this page's body, takeaways and script before recording.

Sources inspected (October 18, 2026):

- [Civil Code 1941.3](https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1941-3/)
- [Civil Code 1946.8](https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1946-8/)
- [Civil Code 1941.5](https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1941-5/)
- [Civil Code 1941.6](https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1941-6/)
- [Civil Code 2079.10a](https://california.public.law/codes/ca_civ_code_section_2079.10a)
- [O’Hara (full opinion)](https://law.justia.com/cases/california/court-of-appeal/3d/75/798.html)
- [Ann M. (full opinion)](https://law.justia.com/cases/california/supreme-court/4th/6/666.html)
- [Kwaitkowski (full opinion)](https://law.justia.com/cases/california/court-of-appeal/3d/123/324.html)
- [Oakland police](https://www.oaklandca.gov/Public-Safety-Streets/Police)
- [Berkeley police reporting](https://berkeleyca.gov/safety-health/police/report-crime)
- [Emeryville police](https://www.emeryville.org/Government/Departments/Police)
- [Fair Housing Institute word list](https://www.fairhousinginstitute.com/wp-content/uploads/2020/06/Fair-Housing-Advertising-Words-Phrases-List-1.pdf)
- [Current company reference](https://alleastbayproperties.com/llms.txt)

## Handoff

Claude should provide `02-revision-response.md` and `02-revision-response.json` with a disposition for every finding, then request review of the updated drafts. Production and preview checks remain open until actually verified. Brian's final read is still required; no publication was performed.

