# Post 9215 — protocol review

**Recommendation: hold pending fixes.** Reviewed September 19, 2026 against docs/01 v0.5, docs/02 v0.2, docs/03 v0.2 and docs/07 v0.1; cornerstone manifest v0.1. WordPress status: draft on AEBP-Dev.

This is the first recorded review for 9215, so the artifacts use round 01. No previous review-response pair was found. WordPress was not changed.

## Gates

- GATE-LEGAL-ACCURACY: **FAIL**
- GATE-LOCAL-ACCURACY: **FAIL**
- GATE-TECHNICAL-SEO: **FAIL**
- GATE-COMPLIANCE-RISK: **PASS**
- GATE-ANECDOTE-INTEGRITY: **PASS**
- CORNERSTONE-STRUCTURE: **PASS**
- CORNERSTONE-AEBP-VOICE: **PASS**

## Findings

### 9215-01 — Type A

> A unit that is exempt from AB 1482 has no rent-increase cap at all

**Root cause:** Exemption from one statute is treated as exemption from all rent restrictions, immediately after listing deed-restricted affordable housing.

**Fix:** Replace with 'An exempt unit is not subject to AB 1482’s cap; affordability restrictions, agreements, and other applicable limits still need checking.' Assess local termination coverage separately. Source: Civil Code §1947.12(d)(1), https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12.

**Future prevention:** Preserve the distinction between state-cap exemption, other rent restrictions, and local just-cause coverage in every summary.

### 9215-02 — Type A

> Miss a precondition and the notice can be invalidated.

**Root cause:** The five-step sequence and consequences omit the express City-service exception in §5-40.06(b). 'City-required form' also overstates §5-40.08.

**Fix:** Explain that City filing is mandatory, but failure of City service alone does not invalidate the termination notice under §5-40.06(b). Describe a notice substantially in the City's prescribed form with all required content. Correct intro, five steps, consequences, checklist and script. Source: https://ecode360.com/46994531

**Future prevention:** Compare procedural instructions with the remedies section; retain exceptions when compressing into a script.

### 9215-03 — Type A

> Small landlord — 4 or fewer covered units

**Root cause:** The tier definition drops the group-residential-facility exception; quick answer, facts, FAQ and script also lose the Emeryville-only unit count.

**Fix:** Count covered units in Emeryville; include group residential facilities of any size in the small-landlord definition. Apply consistently across table, FAQ, intro and script. Source: §5-40.02(e), https://ecode360.com/46994531

**Future prevention:** Carry the full defined term into condensed tables and companion copy.

### 9215-04 — Type A

> the tenant may be offered it

**Root cause:** A conditional obligation reads as landlord discretion.

**Fix:** Use 'the landlord must offer it' when the stated right-to-return conditions are met; retain the two-year, current-address and written-acceptance qualifications. Source: §5-40.02(j), https://ecode360.com/46994531

**Future prevention:** Check must/may wording against the controlling provision.

### 9215-05 — Type A

> hotels and motels

**Root cause:** The local-exemptions paragraph and FAQ omit the occupancy limit, making the exemption categorical.

**Fix:** Qualify hotels, motels and short-term rentals by the maximum 30-consecutive-day occupancy condition and anti-evasion rule. Use 'covered tenancies' in broad day-one/any-termination statements. Source: §5-40.02(b)(1), https://ecode360.com/46994531

**Future prevention:** Do not turn conditional coverage exemptions into property-type labels.

### 9215-06 — Type A

> generally 30 days if it totals 10% or less, 90 days if more

**Root cause:** The action checklist repeats base notice periods without allowing for service by mail.

**Fix:** Add that mailed notices require the applicable additional time under CCP §1013, and that longer governing notice requirements control. Update body and checklist. Source: Civil Code §827(b)–(c), https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827.

**Future prevention:** Review service method whenever publishing a notice-period checklist.

### 9215-07 — Type B

> Emeryville Rental Laws 2026: What Landlords Need to Know (It's Not as Simple as No Rent Control)

**Root cause:** The saved draft is readable through WordPress, but the browser preview returns Page not found. Rendered content and emitted schema cannot be inspected from that response.

**Fix:** Provide an authenticated working preview or rendered-page evidence, then verify article/FAQ schema, on-page FAQ agreement, responsive tables, sharing links and reusable block output. This is an evidence gap, not proof that schema is missing. Do not publish merely to obtain a preview.

**Future prevention:** Include usable preview evidence with a final-review handoff.

## Strengths to preserve

- 8.8% for August 1, 2026–July 31, 2027 is verified: April 2026 regional CPI 3.8% plus 5%. Preserve it.
- Oakland 2.3%, Berkeley 1.0%, Richmond 1.5% match current official city/Rent Board sources.
- Required cornerstone sequence is present, including AEBP observation, action checklist, five FAQ questions, sources and closing CTA.
- Company calendar practice has an identifiable internal published source; illustration is explicitly hypothetical.
- Script is labeled Video Script, not a transcript of an unrecorded video.
- Source notes distinguish City FAQ guidance from ordinance authority; contested individual cases are referred to counsel.
- Native block attributes parse as JSON; social-link escaping is normal JSON escaping, not a demonstrated defect.

The central rate is supported by the [dated BLS release](https://www.bls.gov/regions/west/news-release/2026/consumerpriceindex_sanfrancisco_20260512.htm). The local corrections reference [Emeryville Chapter 5-40](https://ecode360.com/46994531).

## Estimated scores

| Category | Score | Minimum | Result |
|---|---:|---:|---|
| SCORE-SEO | 92 | 90 | PASS |
| SCORE-GEO | 88 | 95 | FAIL |
| SCORE-EEAT | 88 | 95 | FAIL |
| SCORE-READABILITY | 92 | 90 | PASS |
| SCORE-CONVERSION | 90 | 85 | PASS |
| SCORE-OVERALL | 88 | 95 | FAIL |

- **SCORE-SEO:** Specific title, SEO metadata, relevant internal links and live conversion destination. Rendered schema and page checks remain open.
- **SCORE-GEO:** Answer-first introduction, key facts, comparison tables and five FAQ answers. Compressed answers repeat incomplete legal definitions.
- **SCORE-EEAT:** Primary sources and documented company observation; hypothetical arithmetic explicitly labeled. Legal exceptions omitted; replace rolling BLS link with dated release.
- **SCORE-READABILITY:** Clear sections, useful tables and an action checklist. Intro is dense and some points repeat through script and body.
- **SCORE-CONVERSION:** Relevant Emeryville CTA and general education with attorney referral. Linked service page has broader rent-flexibility language worth separately reviewing.
- **SCORE-OVERALL:** Strong cornerstone structure and correctly updated central rate. Open legal/local findings and incomplete rendered-page verification prevent clearance.

## Article fix list

- 9215-01: Replace with 'An exempt unit is not subject to AB 1482’s cap; affordability restrictions, agreements, and other applicable limits still need checking.' Assess local termination coverage separately. Source: Civil Code §1947.12(d)(1), https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12.
- 9215-02: Explain that City filing is mandatory, but failure of City service alone does not invalidate the termination notice under §5-40.06(b). Describe a notice substantially in the City's prescribed form with all required content. Correct intro, five steps, consequences, checklist and script. Source: https://ecode360.com/46994531
- 9215-03: Count covered units in Emeryville; include group residential facilities of any size in the small-landlord definition. Apply consistently across table, FAQ, intro and script. Source: §5-40.02(e), https://ecode360.com/46994531
- 9215-04: Use 'the landlord must offer it' when the stated right-to-return conditions are met; retain the two-year, current-address and written-acceptance qualifications. Source: §5-40.02(j), https://ecode360.com/46994531
- 9215-05: Qualify hotels, motels and short-term rentals by the maximum 30-consecutive-day occupancy condition and anti-evasion rule. Use 'covered tenancies' in broad day-one/any-termination statements. Source: §5-40.02(b)(1), https://ecode360.com/46994531
- 9215-06: Add that mailed notices require the applicable additional time under CCP §1013, and that longer governing notice requirements control. Update body and checklist. Source: Civil Code §827(b)–(c), https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827.
- 9215-07: Provide an authenticated working preview or rendered-page evidence, then verify article/FAQ schema, on-page FAQ agreement, responsive tables, sharing links and reusable block output. This is an evidence gap, not proof that schema is missing. Do not publish merely to obtain a preview.
- Source durability: replace the rolling BLS URL with https://www.bls.gov/regions/west/news-release/2026/consumerpriceindex_sanfrancisco_20260512.htm, which verifies the April 2026 figure.
- Keep tax attribution precise: the City FAQ describes the 0.10%/$25 schedule for 'most businesses'; retain confirmation language rather than call the FAQ an independently verified residential-specific rate schedule.
- Before the full cornerstone package ships, review the separate video companion and GBP copy independently. They were not supplied/identified in this post-only review.

## Operating System follow-ups

- Retain the City-service exception and group-residential definition already present in the refreshed knowledge file when drafting shortened copy. This is application of existing reference material, not a missing-rule problem.
- Record the already cited license-calendar experience in the anecdote log with its internal source, so later reviews need not reconstruct provenance from published copy.
- Review the linked Emeryville service page separately: its 'Adjust rents to market rates annually' language could undermine this guide's careful explanation. This is outside the post-9215 clearance scope.

## Provenance and review limits

- **9215-C1: documented.** “We've been headquartered in Emeryville since 2005” Source: knowledge/company/overview.md; https://alleastbayproperties.com/thursday-tip-emeryville-business-license/. Published internal citation supports headquarters/history; no new owner_verified label inferred.
- **9215-C2: documented.** “license renewal sits on our own compliance calendar alongside the registration deadlines we track for Oakland, Berkeley, and Richmond” Source: https://alleastbayproperties.com/thursday-tip-emeryville-business-license/; knowledge/company/overview.md. Existing internal published record supports the calendar practice; draft cites Brian confirmation. Script's shorter version is covered here.
- **9215-C3: documented.** “we also checked the City's own Tenant Protection Resources page” Source: https://www.emeryville.org/Services/Housing/Tenant-Resources/Tenant-Protection-Resources. Reviewer independently checked on September 19, 2026: page still shows the 6.3% 2025–26 period. Same research observation repeated in body and script.
- **9215-C4: documented.** “We're headquartered in Emeryville and have managed East Bay rentals since 2005 — including the license, notice, and City Clerk filings that sit underneath every Emeryville termination.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/thursday-tip-emeryville-business-license/. Read as general compliance-service description, supported by internal service record, not as an assertion of a particular eviction/client result. Legal coverage qualification is addressed in 9215-05.
- **9215-C5: hypothetical_example.** “Illustration (hypothetical arithmetic, not a client case)” $3,000 rent illustration correctly shows arithmetic and requires checking current HUD FMR; no fabricated client event.

First recorded protocol review for 9215: no earlier review/revision-response found in the repository, so numbered 01 despite the request for a final review. Reviewed latest WordPress snapshot on AEBP-Dev, not production. Snapshot reports post_modified 2026-09-19 15:50:50 without explicit GMT, so modified_gmt is null rather than guessed; revision ID not returned. Repo was clean and aligned with origin/main before writing these artifacts. No WordPress edits or publishing performed. Embedded script reviewed as part of the post; separate companion video and GBP are not cleared. Preview https://dev.alleastbayproperties.com/?p=9215&preview=true returned Page not found. Metadata and native block attributes inspected, but no editor round-trip or emitted schema verification claimed. BMR percentages corroborated by official City indexed program text; direct program/PDF retrieval was blocked, so this was not a full current PDF audit. Scores are editorial estimates, not measured search results or an arithmetic average. Claude should answer every finding in 02-revision-response.json; next review must inspect the actual updated post.

