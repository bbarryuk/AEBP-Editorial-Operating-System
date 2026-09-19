# Pre-Publish Audit — WordPress post 9149

**Richmond Rent Control 2026: What Landlords Must Know About the Richmond Fair Rent Act**

**Recommendation: HOLD pending fixes.** Reviewed September 7, 2026 (Pacific), against Editorial Standards v0.5, Evidence v0.2, Review Format v0.2, and the new Automation Protocol v0.1. WordPress remains a draft and was not edited.

## Gates

| Gate | Result |
|---|---|
| GATE-LEGAL-ACCURACY | FAIL |
| GATE-LOCAL-ACCURACY | FAIL |
| GATE-TECHNICAL-SEO | FAIL |
| GATE-COMPLIANCE-RISK | PASS |
| GATE-ANECDOTE-INTEGRITY | FAIL |
| CORNERSTONE-STRUCTURE | PASS |
| CORNERSTONE-AEBP-VOICE | FAIL |

Companion video and GBP were not identified in the supplied post data and remain unaudited. Technical review covers the retrieved markup and metadata; editor validity, rendered schema and visual presentation remain unverified.

## Findings

### 9149-01 — Type A

**Finding:** “the first time in years the two have swapped places”

**Root cause / evidence:** Historical comparison was inferred from the prior cycle. Richmond's 2024 AGA was 1.4%, below Oakland's 2.3%. Sources: [Source](https://www.ci.richmond.ca.us/3376/Rent-Increase) and [Source](https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases)

**Fix:** Replace all longstanding-higher/first-time claims with a comparison limited to 2025–26 versus 2026–27. Keep the practical warning to check each city's current rate.

**Future prevention:** Verify both historical series before writing trend-based hooks.

### 9149-02 — Type A

**Finding:** “A single-family rental in Richmond doesn't get a rent cap”

**Root cause / evidence:** The draft generalizes a local exemption to all law; the checklist and FAQ repeat this. Civil Code 1947.12 can apply to locally exempt housing. Source: [Source](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12.)

**Fix:** Use 'not subject to Richmond's local rent cap'; add a separate AB 1482 eligibility check, including ownership and exemption-notice conditions for separately alienable homes and the rolling 15-year construction exemption.

**Future prevention:** Record the local-versus-state distinction in Richmond coverage knowledge.

### 9149-03 — Type A

**Finding:** “Base Rent + AGA = Maximum Allowable Rent”

**Root cause / evidence:** This treats a percentage as a dollar amount and omits accumulated lawful adjustments. The body also implies today's AGA alone applied to original Base Rent establishes MAR. Source: [Source](https://www.ci.richmond.ca.us/3376/Rent-Increase)

**Fix:** Replace the formula with an explanation that MAR depends on lawful rent history and applicable adjustments; link the city's MAR calculator. Distinguish the ordinary current AGA from available banking.

**Future prevention:** Require a worked, verified calculation before publishing rent formulas.

### 9149-04 — Type A

**Finding:** “30 days for an increase of 10% or less, 90 days for anything larger”

**Root cause / evidence:** The summary omits the cumulative prior-12-month test and additional mailing time, and reads as universal despite statutory exceptions. Source: [Source](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827.)

**Fix:** Say generally at least 30/90 days based on cumulative increases over the preceding 12 months, account for service by mail and applicable exceptions, and link section 827 directly. More notice does not authorize an otherwise unlawful increase.

**Future prevention:** Add a notice-summary regression check for aggregation and service method.

### 9149-05 — Type A

**Finding:** “Run through this before serving any AGA increase notice:”

**Root cause / evidence:** The action checklist omits the Rent Program brochure and annual Rental Housing Fee compliance, although both appear in current city instructions. Source: [Source](https://www.ci.richmond.ca.us/3376/Rent-Increase)

**Fix:** Add brochure service and paid Rental Housing Fee checks; clarify that enrollment must be amended when ownership/contact/agent/status changes, despite not being an annual renewal.

**Future prevention:** Maintain a current source-linked AGA notice checklist.

### 9149-06 — Type B/C

**Finding:** “a $106/owner annual registration fee”

**Root cause / evidence:** The city's Billing page distinguishes annual registration for 3+ units from every three years for 1–2; its RRIP update page says yearly for participants. The knowledge file also contains both versions. Sources: [Source](https://www.ci.richmond.ca.us/4832/Billing) and [Source](https://www.ci.richmond.ca.us/2101/Rental-Inspection-Program)

**Fix:** Resolve using the enacted amendment/current fee schedule or department confirmation. Until resolved, omit the universal frequency assertion or explicitly disclose the conflict. Re-verify FY 2025–26 tax/fee amounts for the 2026–27 publication; don't infer a new fee from a stale page.

**Future prevention:** Reconcile the contradictory RRIP entries and track fee verification by fiscal year.

### 9149-07 — Type B

**Finding:** “We're checking the rate against the current cycle on every Richmond notice we prepare”

**Root cause / evidence:** No confirming entry supports this operational claim or the earlier 'mistake we watched for' in knowledge/company/anecdote-log.md. Absence of a record is not proof of fabrication.

**Fix:** Provide Brian's confirmation in a durable record, or replace this observation with the already documented Richmond post-purchase business-license reminder letter (2026-08-26). Do not embellish that incident.

**Future prevention:** Require claim-provenance references during drafting.

### 9149-08 — Type A/B

**Finding:** “<!-- wp:list -->
<ol class="wp-block-list">”

**Root cause / evidence:** The ordered list lacks its ordered attribute; several blocks have HTML classes/anchors not represented in their block attributes. Share links are empty self-closing social-link blocks. Raw markup alone cannot establish editor validity; rendered schema is unverified.

**Fix:** Re-save through valid Gutenberg blocks and inspect editor validation and preview. Configure or remove empty share links. Verify emitted Article/FAQ schema and featured image; meta keyword/about fields alone are not proof of JSON-LD. Preserve the two working internal links.

**Future prevention:** Require editor validation and rendered schema evidence, not just wp comments.

### 9149-09 — Type B

**Finding:** “No equivalent city-run rental inspection program”

**Root cause / evidence:** A broad negative comparison has no supporting Oakland inspection-program source in the article or this review.

**Fix:** Narrow to the specific recurring RRIP model and verify against Oakland's inspection programs, or remove this row.

**Future prevention:** Source negative comparative claims independently.

## Scores — editorial estimates

| Category | Estimate / minimum | Result | Working | Holding it back |
|---|---|---|---|---|
| SCORE-SEO | 91 / 90 | PASS | Clear Richmond keyword, title, excerpt, metadata and live internal links. | Repetitive framing; technical release gate remains separate. |
| SCORE-GEO | 83 / 95 | FAIL | Answer-first layout, tables and five labeled FAQs. | Standalone FAQ answers overgeneralize coverage and the AGA ceiling; calculation language is unreliable. |
| SCORE-EEAT | 79 / 95 | FAIL | Named author and official source list. | Unverified operational claims and incorrect historical narrative. |
| SCORE-READABILITY | 89 / 90 | FAIL | Scannable sections and practical checklist. | Rate reversal repeated across intro, body, observation and conclusion; dense quick answer. |
| SCORE-CONVERSION | 88 / 85 | PASS | Relevant closing CTA and live consultation destination. | No clear advice on when to consult a housing attorney for contested exemptions or termination. |
| SCORE-OVERALL | 84 / 95 | FAIL | Useful city-specific cornerstone structure. | Multiple blocking factual, provenance and technical findings. Holistic estimate, not an arithmetic rubric. |

## Strengths worth preserving

- Required cornerstone sections are present, including five FAQ details blocks and closing CTA.
- Current 1.5% Richmond AGA, Oakland 2.3%, distinct cycles and 6.5% Richmond banking ceiling are supported by current official pages.
- Relocation amounts match the city's still-published 2025 table; the city explicitly confirms the 2026 publication delay. This is not an automatic stale-number failure. Source: [Source](https://www.ci.richmond.ca.us/4824/Richmond-Relocation-Ordinance)
- Eight just-cause grounds and two-business-day filing are supported by the city's Termination of Tenancy page.
- Comparison-guide and consultation links resolve to the intended live pages.

## Claim provenance

- **9149-C1: documented.** “We manage properties in both Oakland and Richmond” knowledge/company/overview.md; knowledge/company/anecdote-log.md (Richmond client entry) Supports service footprint; does not verify the new notice-preparation narrative.
- **9149-C2: unverified.** “the multi-city mistake we watched for was an owner defaulting to Oakland's lower number”  
- **9149-C3: unverified.** “"Richmond runs a bit hotter" became a safe assumption to work from”  
- **9149-C4: unverified.** “We're checking the rate against the current cycle on every Richmond notice we prepare”  
- **9149-C5: unverified.** “We track Richmond's registration, inspection, and relocation requirements alongside Oakland's, Berkeley's, and Emeryville's for 600+ units across the East Bay, so nothing gets applied on the wrong city's clock.” knowledge/company/overview.md supports the 600+ portfolio size and compliance service, not the complete process/outcome assertion. Remove the absolute 'nothing' assurance under STD-HONEST; confirm the operational wording. Company overview review date is overdue.

## Article fixes

- 9149-01: Replace all longstanding-higher/first-time claims with a comparison limited to 2025–26 versus 2026–27. Keep the practical warning to check each city's current rate.
- 9149-02: Use 'not subject to Richmond's local rent cap'; add a separate AB 1482 eligibility check, including ownership and exemption-notice conditions for separately alienable homes and the rolling 15-year construction exemption.
- 9149-03: Replace the formula with an explanation that MAR depends on lawful rent history and applicable adjustments; link the city's MAR calculator. Distinguish the ordinary current AGA from available banking.
- 9149-04: Say generally at least 30/90 days based on cumulative increases over the preceding 12 months, account for service by mail and applicable exceptions, and link section 827 directly. More notice does not authorize an otherwise unlawful increase.
- 9149-05: Add brochure service and paid Rental Housing Fee checks; clarify that enrollment must be amended when ownership/contact/agent/status changes, despite not being an annual renewal.
- 9149-06: Resolve using the enacted amendment/current fee schedule or department confirmation. Until resolved, omit the universal frequency assertion or explicitly disclose the conflict. Re-verify FY 2025–26 tax/fee amounts for the 2026–27 publication; don't infer a new fee from a stale page.
- 9149-07: Provide Brian's confirmation in a durable record, or replace this observation with the already documented Richmond post-purchase business-license reminder letter (2026-08-26). Do not embellish that incident.
- 9149-08: Re-save through valid Gutenberg blocks and inspect editor validation and preview. Configure or remove empty share links. Verify emitted Article/FAQ schema and featured image; meta keyword/about fields alone are not proof of JSON-LD. Preserve the two working internal links.
- 9149-09: Narrow to the specific recurring RRIP model and verify against Oakland's inspection programs, or remove this row.
- Qualify FAQ 2's 'maximum' as the standard AGA and acknowledge eligible banking; Oakland's cycle is not exactly the same period.
- Replace 'so nothing gets applied on the wrong city's clock' with a nonabsolute service description; add when to seek a housing attorney for a proposed termination or disputed coverage.
- Check the separate companion video and GBP copy before approving the entire cornerstone package. They were not supplied or identified in this post snapshot.

## Operating System improvements

- Reconcile conflicting RRIP frequency statements and refresh fiscal-year fee evidence. Target: knowledge/laws/richmond-rent-program.md.
- Add historical comparison and local-exemption-versus-state-cap regression cases. Target: tests/legal/.
- Attach confirming records to every new AEBP observation; reuse the existing Richmond letter record without embellishment. Target: knowledge/company/anecdote-log.md.
- Clarify schema handling of unperformed companion checks and technical checks; schema has only PASS/FAIL. Do not silently equate inaccessible with absent. Target: automation/schemas/review.schema.json.
- Record current reproducible Richmond page evidence, preserving the older tooling-discrepancy history; update company-fact currency. Target: knowledge/laws/richmond-rent-program.md.

## Review limitations and handoff

Review only; no WordPress changes. Source snapshot post_modified=2026-09-07 22:31:08; timezone not supplied, so not relabeled as GMT. REST get_posts failed response-schema validation; connectivity ping succeeded. No rendered draft/editor/schema inspection completed. Technical FAIL includes observed markup concerns plus unverified release requirements, not a claim that schema/featured image is absent. Video and GBP artifacts remain unaudited; no package clearance. Root causes are review inferences. Repo state recorded before adding these review artifacts; HEAD matched local origin/main, without fetching remote.

The structured companion is 01-review.json. The next revision response should address each unique finding ID, including 9149-10, under docs/07's disposition protocol. No standards or knowledge files were changed as part of this review.

