# Final Review 03 — Post 10268

Oakland and Berkeley Rent Increases for 2027: The New Numbers, and Which One Applies to Each Unit

**Recommendation: HOLD PENDING FIXES.** Most prior content findings are closed. Two Oakland content issues remain, plus technical/package clearance.

Review mode: Pre-Publish Audit. Reviewed 2026-10-31T04:10:44.820Z.
AEBP-Dev draft, site-local modified 2026-10-30 20:44:33; revision ID and GMT modified time unavailable.
Repository: adaad453c4c8f1057d3a49a6f8a12d54c24ff194; clean at review start, zero commits ahead of configured upstream; no remote fetch.
Standards: docs/01 v0.5; docs/02 v0.2 (including the October 30 source-snapshot rule); docs/03 v0.3; docs/07 v0.1; manifests v0.1.

## Prior dispositions checked against WordPress

Both revision responses validate against the active response schema, match their preceding review timestamps, and provide a disposition for every prior finding.

| Finding | Final-review status | Evidence |
|---|---|---|
| 10268-F01 | closed | Coverage/eligibility qualifiers, calendar-year limit and banking caveat are present in the live answers, tables and paired script. |
| 10268-F02 | closed | Combined CPI-plus-banking limit is explicit in the body, facts table and FAQ. |
| 10268-F03 | open / regression | New eligibility checks and tax attachment wording verified, but RAP Notice attachment duty was removed; restore it. |
| 10268-F04 | closed | Ownership restrictions and required exemption notice are both present; checked against civ-1947.12.txt §(d)(5)(A)-(B) and official DRE guidance. |
| 10268-F05 | closed | Cumulative notice test, mailing origin and conservative targets are present; checked against civ-827.txt §(b)(2)-(3), ccp-1013.txt §(a) and DRE guidance. |
| 10268-F06 | closed | October 30 anecdote-log entry documents the scheduling practices. Unconfirmed service/attachment promises were removed; CTA is narrowed. |
| 10268-F07 | partially closed / deferred | Viewing invitation corrected; authenticated rendered checks and companion production remain open. |
| 10268-F08 | closed for supplied draft | GBP draft in response reviewed: rate/coverage statements match the revised article. URL activation and posting approval remain future publication steps; no GBP posting performed. |
| 10268-F09 | new / open | New banking-expiration grandfather conflicts with current reviewed sources; remove or reconcile. |

## Gate results

| Gate | Result | Open findings |
|---|---|---|
| GATE-LEGAL-ACCURACY | FAIL | 10268-F03, 10268-F09 |
| GATE-LOCAL-ACCURACY | FAIL | 10268-F03, 10268-F09 |
| GATE-TECHNICAL-SEO | FAIL | 10268-F07 |
| GATE-COMPLIANCE-RISK | PASS | None identified within the reviewed scope |
| GATE-ANECDOTE-INTEGRITY | PASS | None identified within the reviewed scope |
| CORNERSTONE-STRUCTURE | PASS | None identified within the reviewed scope |
| CORNERSTONE-AEBP-VOICE | PASS | None identified within the reviewed scope |
| CORNERSTONE-COMPANION-VIDEO | FAIL | 10268-F07 |
| CORNERSTONE-GBP-CONSISTENCY | PASS | None identified within the reviewed scope |

A technical FAIL records an uncleared check, not proof of absent schema or invalid blocks. The schema has no blocked/deferred gate state. VIDEO-TRANSCRIPT-LITERAL passes for the correct “Video Script” label only; no final recording was available. GBP consistency is limited to the exact draft supplied in response 02; nothing was posted.

## Open findings

### 10268-F03 — Type A

**Finding:** Confirm the unit is registered with the Rent Adjustment Program when the increase is served, the first increase is at least 12 months after move-in, any prior increase was at least 12 months ago, and at least six months have passed since the tenant first received the RAP Notice.

**Root cause:** Partially fixed, then regressed: registration, elapsed-time and tax-document checks were added, but the response explicitly removed the RAP Notice attachment bullet. The six-month prerequisite does not replace giving the required notice with every increase. Oakland's live allowable-increases page, RAP Notice Changes, confirms both duties. Snapshot checked: knowledge/sources/local/oakland/omc-8.22-art1-rent-adjustment.txt, §8.22.070H (notice requirements) and §8.22.060. Live source: https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases

**Fix:** Add a separate bullet: 'Include a copy of the City’s RAP Notice with every rent increase notice.' Keep the new registration, timing and tax-document bullets; the attachment is an additional requirement.

**Future prevention:** Do not delete independently applicable duties when adding a different notice prerequisite.

### 10268-F09 — Type B

**Finding:** Expire 5 years after accruing (10 years for amounts that accrued before Jan 1, 2026)

**Root cause:** New evidence conflict introduced in round 02. The table grants a 10-year window based on accrual date; the newly cited May 28, 2026 info sheet reportedly supports that interpretation, but its live URL returned 403. The reviewed ordinance snapshot, knowledge/sources/local/oakland/omc-8.22-art1-rent-adjustment.txt §8.22.070B.5.c, says five years without that accrual-date grandfather. The City's live page describes a pre-2026 notice-service exception instead. The 10-year entitlement is not cleared; this is a source-reconciliation finding, not an assertion that the inaccessible PDF says something it does not. EVD-UNCERTAINTY-HANDLING and EVD-BLOCK-PENDING-VERIFICATION apply.

**Fix:** Replace the table's entire banking-expiration row and the body's accrual-date sentence with: 'Banked CPI increases are subject to expiration and other eligibility limits. Check Oakland’s current banking rules before including older amounts.' Link 'current banking rules' to the City’s allowable-increases page. If retaining a specific grandfather rule instead, reconcile the current ordinance and City publications first and cite the controlling provision; do not retain the 10-year promise while the conflict is unresolved.

**Future prevention:** Reconcile a new agency summary against the saved ordinance before promoting a claim to verified. Correct the corresponding rent-caps.md assertion in a separately authorized reference update.

### 10268-F07 — Type B

**Finding:** 🎥 Companion video in production; the video and transcript will be added when ready.

**Root cause:** The premature viewing invitation is fixed. Generated BlogPosting/FAQPage, authenticated preview, editor validity and final paired URLs are still unverified. Deferral to the video-swap step does not clear the technical gate. Draft preview retrieval failed again; balanced comment nesting and populated metadata were verified but are narrower checks.

**Fix:** Keep the accurate production placeholder. Before publishing, verify the rendered article, applicable schema, editor blocks and final internal destinations in an authenticated preview. Restore the viewing invitation only after the companion recording and destination are ready.

**Future prevention:** Track content fixes and rendered-page clearance as separate tasks; never mark deferred checks complete.

## Scored categories

Editorial estimates; not a computed rubric. Overall is an independent estimate.

| Category | Estimate | Minimum | Status | Working | Holding it back |
|---|---:|---:|---|---|---|
| SCORE-SEO | 93 | 90 | PASS | Original answer-first structure retained; corrected eligibility, rolling cap, notice and documented company-practice details verified. | Remaining Oakland attachment omission, banking-source conflict, or technical/package checks as applicable. |
| SCORE-GEO | 93 | 95 | FAIL | Original answer-first structure retained; corrected eligibility, rolling cap, notice and documented company-practice details verified. | Remaining Oakland attachment omission, banking-source conflict, or technical/package checks as applicable. |
| SCORE-EEAT | 93 | 95 | FAIL | Original answer-first structure retained; corrected eligibility, rolling cap, notice and documented company-practice details verified. | Remaining Oakland attachment omission, banking-source conflict, or technical/package checks as applicable. |
| SCORE-READABILITY | 94 | 90 | PASS | Original answer-first structure retained; corrected eligibility, rolling cap, notice and documented company-practice details verified. | Remaining Oakland attachment omission, banking-source conflict, or technical/package checks as applicable. |
| SCORE-CONVERSION | 92 | 85 | PASS | Original answer-first structure retained; corrected eligibility, rolling cap, notice and documented company-practice details verified. | Remaining Oakland attachment omission, banking-source conflict, or technical/package checks as applicable. |
| SCORE-OVERALL | 92 | 95 | FAIL | Original answer-first structure retained; corrected eligibility, rolling cap, notice and documented company-practice details verified. | Remaining Oakland attachment omission, banking-source conflict, or technical/package checks as applicable. |

## Strengths Worth Preserving

- The two current Video Script blocks match exactly.
- Internal anecdote log now documents scheduling practices; unconfirmed operational promises were removed.
- The 6.9% combined limit, AB 1482 ownership test and cumulative notice qualifications are corrected.
- Both drafts retain balanced Gutenberg comment nesting, populated SEO metadata and useful consultation paths.

## Claim provenance

- **10268-C01: documented** — “Every unit we manage has its own increase-eligibility date, and we track it in AppFolio, our property management software.” Source: knowledge/company/anecdote-log.md, 2026-10-30 rent-increase timing entry; knowledge/company/overview.md (600+ unit count and service area).
- **10268-C02: documented** — “Outside Berkeley, that date is the lease anniversary.” Source: knowledge/company/anecdote-log.md, 2026-10-30 rent-increase timing entry; knowledge/company/overview.md (600+ unit count and service area).
- **10268-C03: documented** — “In Berkeley, we raise rent on eligible units on January 1.” Source: knowledge/company/anecdote-log.md, 2026-10-30 rent-increase timing entry; knowledge/company/overview.md (600+ unit count and service area).
- **10268-C04: documented** — “So when a new Berkeley tenancy starts, we set its first eligibility date in AppFolio to the second January after move-in.” Source: knowledge/company/anecdote-log.md, 2026-10-30 rent-increase timing entry; knowledge/company/overview.md (600+ unit count and service area).
- **10268-C05: documented** — “Owners sometimes choose to skip a year, most often to keep a good tenant.” Source: knowledge/company/anecdote-log.md, 2026-10-30 rent-increase timing entry; knowledge/company/overview.md (600+ unit count and service area).
- **10268-C08: documented** — “We manage 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay, and track every unit's rent increase eligibility date.” Source: knowledge/company/anecdote-log.md, 2026-10-30 rent-increase timing entry; knowledge/company/overview.md (600+ unit count and service area).
- **10268-C09: documented** — “That's why, at AEBP, Berkeley is the one city where we raise rent on January 1.” Source: knowledge/company/anecdote-log.md, 2026-10-30 rent-increase timing entry; knowledge/company/overview.md (600+ unit count and service area).
- **10268-C10: documented** — “Outside Berkeley, we time increases to each unit's lease anniversary.” Source: knowledge/company/anecdote-log.md, 2026-10-30 rent-increase timing entry; knowledge/company/overview.md (600+ unit count and service area).
- **10268-C11: documented** — “AEBP takes increases on eligible Berkeley units on January 1 for that reason.” Source: knowledge/company/anecdote-log.md, 2026-10-30 rent-increase timing entry; knowledge/company/overview.md (600+ unit count and service area).

The October 30 internal record supports the retained scheduling and eligibility-date practices. “Documented” identifies that record; this AI review does not assign “owner_verified.” Removed notice-service and attachment-performance claims are closed as removed, not confirmed true. Repeated table/script wording shares the same documentary basis.

## Article fixes

- 10268-F03: Add a separate bullet: 'Include a copy of the City’s RAP Notice with every rent increase notice.' Keep the new registration, timing and tax-document bullets; the attachment is an additional requirement.
- 10268-F09: Replace the table's entire banking-expiration row and the body's accrual-date sentence with: 'Banked CPI increases are subject to expiration and other eligibility limits. Check Oakland’s current banking rules before including older amounts.' Link 'current banking rules' to the City’s allowable-increases page. If retaining a specific grandfather rule instead, reconcile the current ordinance and City publications first and cite the controlling provision; do not retain the 10-year promise while the conflict is unresolved.
- 10268-F07: Keep the accurate production placeholder. Before publishing, verify the rendered article, applicable schema, editor blocks and final internal destinations in an authenticated preview. Restore the viewing invitation only after the companion recording and destination are ready.

## Operating System improvements

- Reconcile rent-caps.md's new pre-2026-accrual ten-year banking claim against OMC §8.22.070B.5.c and current City guidance. Do not silently treat the conflicting summary as controlling. Target: knowledge/laws/rent-caps.md.
- Add regression coverage for preserving the RAP Notice attachment duty while adding the six-month prerequisite. Target: tests/legal.

## Evidence and limits

- [Oakland current allowable-increases guidance](https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases) re-read: RAP Notice attachment requirement and current banking guidance.
- knowledge/sources/local/oakland/omc-8.22-art1-rent-adjustment.txt: §8.22.070B.5.c and H, plus §8.22.060. Live Municode unavailable. The new ten-year accrual-date exception does not appear in that reviewed ordinance text.
- [Berkeley current AGA guidance](https://rentboard.berkeleyca.gov/rights-responsibilities/rent-levels/annual-general-adjustment) re-read: current rate, delay and compliance restrictions.
- knowledge/sources/state/statutes/civ-1947.12.txt: (a)(1)-(2), (d)(5), (g)(3); civ-827.txt: (b)(2)-(3); ccp-1013.txt: (a). Live Leginfo URLs attempted and blocked.
- [Official DRE 2026 guide](https://www.dre.ca.gov/publications/ResourceGuidebook/2026_Landlord_Tenant_Guide.pdf) corroborates exemption and notice checks.
- The May 28 Oakland info-sheet URL returned 403. The response's reported text was not silently treated as verified when it conflicted with available sources.
- Both full current drafts have balanced Gutenberg comment nesting, populated Yoast metadata, and byte-identical Video Script blocks. Those checks do not validate generated schema or WordPress editor serialization.
- Draft previews were inaccessible again. Rendered BlogPosting/FAQPage/VideoObject, final media and destination activation remain open. Media-dependent requirements apply when that media is present and applicable.
- Measure X remains a pre-election proposal in the reviewed context. Recheck outcome and operative rules if publication moves past the vote.

Final review round 03 follows 02-revision-response.json and checks every prior disposition against the live full AEBP-Dev snapshot, site-local post_modified 2026-10-30 20:44:33. Revision ID and modified_gmt not returned. Repo clean and zero commits ahead of configured upstream at start; no remote fetch. Docs/02 v0.2 now includes EVD-SOURCE-SNAPSHOTS (updated October 30); reviewed matching statute/ordinance snapshots and attempted live URLs. Leginfo §§827,1947.12,1013, Oakland Municode and the May 28 info sheet were inaccessible; official Berkeley/Oakland agency pages and DRE 2026 guide corroborate available checks. Failure to retrieve is not proof of absence. Draft previews inaccessible; generated schema and editor block validity not cleared. No WordPress edits/publishing. Closed F01,F02,F04,F05,F06,F08; F03 reopened after RAP attachment regression; F07 technical portion deferred; F09 new banking-source conflict. C06/C07 removed from article, not verified true. Supplied GBP text compared, not posted. Next response: 04-revision-response.md/json, then 05-final-review.

## Handoff

Respond to these open findings in reviews/posts/10268/04-revision-response.md and .json. Retain the requires_human production item until evidence is available; do not close it by deferring it again. Re-review the updated WordPress content for round 05. Brian retains the final publication decision.

