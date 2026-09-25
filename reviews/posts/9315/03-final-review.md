# Final Review — Post 9315

**What Overpricing a Rental Really Costs: The Vacancy Math**

**Content corrections verified. Hold pending technical/production clearance.**

Mode: Pre-Publish Audit, round 03. Reviewer: ChatGPT (GPT-6).
Reviewed: September 24, 2026, 23:17 PDT (September 25 UTC).
WordPress: draft, modified 2026-09-24 22:44:57 (source timezone unspecified).
Repository: `7507a7e8c83f400521672d6765c96cfccad27abb`, clean before review artifacts; matched GitHub main.
Standards: docs/01 v0.5, docs/02 v0.2, docs/03 v0.2, docs/07 v0.1, manifest v0.1.

## Prior finding dispositions

- 9315-F01 — CLOSED: condition assertion removed; current script matches approved wording in the September 25 anecdote log.
- 9315-F02 — CLOSED: repair-cost superlative removed; six extra weeks explicit in hypothetical; summary scoped to example; professional opinion labeled; excerpt and metadata softened. Both script copies match exactly.
- 9315-F03 — OPEN / requires_human preserved: video still in production, no finished recording/embed to verify, and rendered preview unavailable.

## Gated categories

### GATE-LEGAL-ACCURACY — PASS

### GATE-LOCAL-ACCURACY — PASS

### GATE-TECHNICAL-SEO — FAIL

**9315-F03 — Type B (carried forward)**

- **Finding:** “Video in production. It will be embedded here once it's live.”
- **Root Cause:** Still open after revision: snapshot remains draft and says video in production. No final video or render evidence was supplied; anonymous preview fetch failed again. Source block markers balance (31), but this does not prove editor validity or generated schema. Claude retains requires_human.
- **Fix:** Keep this page draft until recording/embed and final rendered checks are completed. Verify guide link at release and compare spoken recording with transcript before relabeling Video Script. Lack of raw JSON-LD is not proof that generated schema is absent.
- **Future Prevention:** Provide an authenticated preview and final video metadata in the companion handoff.

### GATE-COMPLIANCE-RISK — PASS

### GATE-ANECDOTE-INTEGRITY — PASS

### VIDEO-TRANSCRIPT-LITERAL — PASS

### VIDEO-CONSISTENCY — PASS

## Scored categories

All scores are estimates for reviewed content; passing scores do not override open gates.

- **SCORE-SEO: 91/100 — PASS**, threshold 90. Working: Configured metadata, descriptive title, image alt and useful resources. Holding back: Publication clearance still depends on the separate open technical/production gates; score evaluates reviewed content only.
- **SCORE-GEO: 95/100 — PASS**, threshold 95. Working: Compact summary and takeaways; hypothetical now has explicit six-week assumption. Holding back: No remaining below-threshold content issue identified; final rendered output remains outside verified scope.
- **SCORE-EEAT: 95/100 — PASS**, threshold 95. Working: Approved documented experience; unsupported condition and repair claims removed. Holding back: No remaining below-threshold content issue identified; final rendered output remains outside verified scope.
- **SCORE-READABILITY: 95/100 — PASS**, threshold 90. Working: Brief script with precise assumed delay, matching the article copy. Holding back: Some repeated pricing advice remains; optional tightening would improve economy.
- **SCORE-CONVERSION: 91/100 — PASS**, threshold 85. Working: Specific consultation CTA plus full written-guide destination. Holding back: No remaining below-threshold content issue identified; final rendered output remains outside verified scope.
- **SCORE-OVERALL: 95/100 — PASS**, threshold 95. Working: All requested script/content corrections verified; no new blocking regression found. Holding back: Publication clearance still depends on the separate open technical/production gates; score evaluates reviewed content only.

## Claim provenance

- **9315-C01 — documented:** “We've watched this happen. In one turnover we handled, the unit went through several price cuts over a period of months and leased close to where comparable units had been renting all along.” Approval and reuse constraints documented in the repository. Wording matches; distinctive private case figures absent. AI reviewer does not assign owner_verified. Source: knowledge/company/anecdote-log.md, 2026-09-25 entry.
- **9315-C03 — hypothetical_example:** “Say a unit is worth $2,500 a month.” The page calls it illustrative; make six extra weeks explicit in the spoken calculation. Source: Explicit hypothetical in draft.

## Strengths Worth Preserving

- Script is correctly labeled before recording.
- The two script copies match at review time.
- Core $575 weekly and $3,450 six-week arithmetic agrees with the article.
- Resources and consultation CTA offer useful next steps.
- Revisions preserve the hypothetical/real-case distinction and remove the unsupported condition detail.
- Both live script copies are identical; no blocking content regression identified.

## Article fixes / remaining clearance

- 9315-F03: Keep this page draft until recording/embed and final rendered checks are completed. Verify guide link at release and compare spoken recording with transcript before relabeling Video Script. Lack of raw JSON-LD is not proof that generated schema is absent.

## Operating System improvements

- Industry benchmark reference now exists and the approved anecdote is logged. Older fees/vacancy-tip shorthand remains a separate audit, not a blocker for this corrected draft. Target: `knowledge/company/industry-vacancy-benchmarks.md`.
- Review schema still lacks a canonical version constant: initial GPT review uses 1.0.0 and Claude response uses 0.1.0. Both validate structurally; this final review retains 1.0.0 for continuity without claiming it is declared by the schema. Target: `automation/schemas/review.schema.json`.
- Clarify the revision-response summary: its sentence can be read as saying preview checks were approved, but F06 explicitly remains requires_human. The appended anecdote approval supersedes older pending-approval prose only for the anecdote. Target: `reviews/posts/9313/02-revision-response.json`.

## Evidence and limits

Final review round 03. Reviewed live WordPress snapshot modified 2026-09-24 22:44:57; timezone not supplied, no revision ID or GMT timestamp returned. Repository HEAD matches GitHub main; clean before these artifacts (global-ignore permission warning noted). Standards/manifests/schemas unchanged from initial review, confirmed by repository diff; new benchmark reference and anecdote entry read. Both revision-response JSON files validate and address every prior numbered finding; no rejected or unanswered findings. 9315-F01 — CLOSED: condition assertion removed; current script matches approved wording in the September 25 anecdote log. 9315-F02 — CLOSED: repair-cost superlative removed; six extra weeks explicit in hypothetical; summary scoped to example; professional opinion labeled; excerpt and metadata softened. Both script copies match exactly. 9315-F03 — OPEN / requires_human preserved: video still in production, no finished recording/embed to verify, and rendered preview unavailable. Content scores are estimates, not a calibrated computation; all meet thresholds. Overall recommendation remains hold_pending_fixes only because technical/production clearance remains open, not because another substantive rewrite is required. No new blocking content issue identified. Primary legal and industry sources rechecked this round; original math and documented portfolio figures remain unchanged. Article block markers 82; video 31; all balanced; scripts equal. GBP package draft unchanged and consistent with the hypothetical; live GBP/recording not reviewed. Internal link presence checked; initial round's destination checks retained, not represented as a fresh full live-link audit. Anonymous article/video previews failed again. No claim that generated schema is absent. No WordPress edits, publishing, commits or pushes. Next step is recorded preview/production evidence and Brian's final read; another Claude prose-revision cycle is not needed unless those checks uncover defects.

Sources rechecked:

- [Berkeley AGA](https://rentboard.berkeleyca.gov/rights-responsibilities/rent-levels/annual-general-adjustment)
- [Oakland allowable increases](https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases)
- [Civil Code 1954.53](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1954.53)
- [PM Trends co-author's source](https://www.peterlohmann.com/blog/pm-trends-report-2026)
- [Apartment List seasonality research](https://www.apartmentlist.com/research/the-rental-markets-peak-season-is-becoming-less-pronounced)

## Recommendation

`hold_pending_fixes` — technical/production clearance only. Brian's anecdote approval is documented and does not need to be requested again. Record the remaining preview and video results, then perform Brian's final publication read.

