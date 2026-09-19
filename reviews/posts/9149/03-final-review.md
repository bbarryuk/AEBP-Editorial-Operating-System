# Final-review round — Post 9149

**HOLD pending fixes.** Reviewed current WordPress content and Claude's revision response against docs/01 v0.5, docs/02 v0.2, docs/03 v0.2, docs/07 v0.1 and cornerstone manifest v0.1. No WordPress changes.

## Resolved and strengths worth preserving

- 9149-01 closed: historical comparison limited to actual prior/current cycles.
- 9149-02 closed in substance: main body, checklist and FAQ distinguish local and state cap coverage; make remaining 'no rent cap' shorthand explicitly local.
- 9149-05 closed: brochure, housing fee and enrollment-amendment requirements added.
- 9149-07 and 9149-10 closed: documented letter anecdote replaces unverified operational history.
- FAQ 2 now distinguishes standard AGA from banking and identifies different city cycles.
- Sharing links and ordered-list attributes are present in current markup.
- Attorney referral and nonabsolute service CTA improve the draft.

## Remaining findings

### 9149-03 — Type A

**Finding:** “MAR = Base Rent + every lawful AGA applied since, via the city's MAR calculator”

**Root cause/evidence:** Partial fix: an additive percentage equation remains, and the named calculator has no link.

**Fix:** Remove the equation. Describe MAR as dependent on lawful rent history and applicable adjustments, and link the actual city calculator from https://www.ci.richmond.ca.us/3376/Rent-Increase.

**Future prevention:** Verify the current source and every repeated instance before closing the finding.

### 9149-04 — Type A

**Finding:** “More notice than the minimum is always safe; less is not.”

**Root cause/evidence:** Cumulative timing and mailing time are corrected, but the new absolute assurance exceeds what section 827 establishes.

**Fix:** Delete this sentence or say that longer notice does not cure an unlawful increase or defective service. Source: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827.

**Future prevention:** Verify the current source and every repeated instance before closing the finding.

### 9149-06 — Type A/B/C

**Finding:** “a $106/owner registration fee”

**Root cause/evidence:** FY 2026–27 Master Fee Schedule p14 lists current fees $110 registration, $220 initial inspection, $94 reinspection; $106/$211/$90 are previous fees. https://www.ci.richmond.ca.us/DocumentCenter/View/80176. Frequency is separately unresolved: the current Billing and RRIP pages conflict, and citing the repo's summary as enacted text does not resolve them.

**Fix:** Update all fee amounts and source to FY 2026–27. Resolve frequency against the enacted ordinance or department evidence, or omit that detail. The local knowledge file still contains both frequency versions; a July 2025 fee summary is not pre-amendment evidence for a January 2025 amendment.

**Future prevention:** Verify the current source and every repeated instance before closing the finding.

### 9149-08 — Type B

**Finding:** “<!-- wp:list {"ordered":true} -->”

**Root cause/evidence:** Ordered-list attribute and share links are now configured, contrary to the response's empty-link note. Other block attributes are also restored. Browser draft preview returned 404, so rendered schema, editor validity and image output remain unverified, not proven absent.

**Fix:** Verify with an authenticated preview/editor; ensure production share URLs use the final public domain. No site-wide share-template rebuild is justified by the superseded empty-link evidence.

**Future prevention:** Verify the current source and every repeated instance before closing the finding.

### 9149-09 — Type B

**Finding:** “No directly comparable citywide recurring inspection cycle identified”

**Root cause/evidence:** The weaker wording still puts an uncited research non-result into a factual comparison table.

**Fix:** Remove the comparison row or replace the Oakland cell with a sourced description of its actual inspection program.

**Future prevention:** Verify the current source and every repeated instance before closing the finding.

### 9149-11 — Type A

**Finding:** “applying Oakland's higher rate to a Richmond unit is an overcharge”

**Root cause/evidence:** Unqualified claim conflicts with the article's own eligible-banking exception, which can permit more than 1.5%.

**Fix:** Qualify: 'Applying 2.3% without sufficient lawful banking or another authorized basis can produce an unlawful increase.' Source: https://www.ci.richmond.ca.us/3376/Rent-Increase.

**Future prevention:** Verify the current source and every repeated instance before closing the finding.

## Gates

- GATE-LEGAL-ACCURACY: **FAIL**
- GATE-LOCAL-ACCURACY: **FAIL**
- GATE-TECHNICAL-SEO: **FAIL**
- GATE-COMPLIANCE-RISK: **PASS**
- GATE-ANECDOTE-INTEGRITY: **PASS**
- CORNERSTONE-STRUCTURE: **PASS**
- CORNERSTONE-AEBP-VOICE: **PASS**

## Scores (estimates)

| Category | Score / threshold | Status | Working | Holding back |
|---|---|---|---|---|
| SCORE-SEO | 92/90 | PASS | Clear Richmond keyword, title, excerpt, metadata and live internal links. | Technical clearance outstanding. |
| SCORE-GEO | 90/95 | FAIL | Answer-first layout, tables and five labeled FAQs. | Formula and unqualified overcharge wording. |
| SCORE-EEAT | 91/95 | FAIL | Named author and official source list. | Outdated fees and conflicting fee frequency. |
| SCORE-READABILITY | 90/90 | PASS | Scannable sections and practical checklist. | Long intro and repeated comparison. |
| SCORE-CONVERSION | 90/85 | PASS | Relevant closing CTA and live consultation destination. | No material shortfall; attorney referral added. |
| SCORE-OVERALL | 90/95 | FAIL | Useful city-specific cornerstone structure. | Holistic estimate; legal/local and technical gates remain blocked. |

## Article fixes

- 9149-03: Remove the equation. Describe MAR as dependent on lawful rent history and applicable adjustments, and link the actual city calculator from https://www.ci.richmond.ca.us/3376/Rent-Increase.
- 9149-04: Delete this sentence or say that longer notice does not cure an unlawful increase or defective service. Source: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827.
- 9149-06: Update all fee amounts and source to FY 2026–27. Resolve frequency against the enacted ordinance or department evidence, or omit that detail. The local knowledge file still contains both frequency versions; a July 2025 fee summary is not pre-amendment evidence for a January 2025 amendment.
- 9149-08: Verify with an authenticated preview/editor; ensure production share URLs use the final public domain. No site-wide share-template rebuild is justified by the superseded empty-link evidence.
- 9149-09: Remove the comparison row or replace the Oakland cell with a sourced description of its actual inspection program.
- 9149-11: Qualify: 'Applying 2.3% without sufficient lawful banking or another authorized basis can produce an unlawful increase.' Source: https://www.ci.richmond.ca.us/3376/Rent-Increase.
- Add direct links for Civil Code 827, 1947.12 and the actual MAR calculator.
- Scope FAQ 3 tenancy registration to rent-controlled units, consistent with the main body.
- Companion video/GBP remain unaudited; no package clearance.

## Operating System improvements

- Refresh RRIP amounts from FY 2026–27 Master Fee Schedule p14; reconcile frequency against primary evidence. Claude recorded this follow-up but the knowledge file is unchanged locally.
- Record actual current WordPress evidence; revision-response assertions about empty share blocks are now superseded.

## Provenance and limits

- 9149-C1: documented — knowledge/company/overview.md and knowledge/company/anecdote-log.md. 
- 9149-C4: documented — knowledge/company/anecdote-log.md, 2026-08-26 Richmond letter entry. Replaces former C4. Reuse of a documented anecdote does not require another owner confirmation.
- 9149-C5: documented — knowledge/company/overview.md: portfolio, service area, compliance service. General service description supported; absolute outcome assurance removed. Internal fact review date remains overdue.

Responds to 02-revision-response.json. All ten original findings have dispositions. Closed: 9149-01,02,05,07,10. Partial/open: 9149-03,04,06,08,09. Additional clarification: 9149-11. No WordPress edits or publishing. Raw post_modified=2026-09-07 23:52:55, timezone unspecified; modified_gmt remains null. Browser preview returned 404 in this unauthenticated session, so no rendered/schema clearance. Fee figures verified from extracted PDF text p14 including previous/current headings; PDF screenshot attempt failed. Scanned enacted amendment did not yield readable evidence, so frequency is not settled. HEAD unchanged at 3f9473; review files untracked; local knowledge file still contradictory. Standards and knowledge files were not changed by this review. Root causes are review inferences.

Next protocol artifact: 04-revision-response.json addressing the six remaining findings. Keep earlier rounds as history.

