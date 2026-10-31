# Editorial Review — Post 10269

Berkeley and Oakland Rent Increases for 2027 Explained (Video)

Recommendation: **HOLD PENDING FIXES**. Review mode: Pre-Publish Audit.
Snapshot: AEBP-Dev draft; site-local modified 2026-10-30 20:28:59. Revision ID / GMT timestamp unavailable.
Reviewed 2026-10-31T03:37:26.101Z. Repository commit c4534e57057f7ec5bebccc3578c4f5cbb18d875c; working tree clean before artifacts; zero commits ahead of configured upstream (no remote fetch).
Standards: docs/01 v0.5; docs/02 v0.2; docs/03 v0.3; docs/07 v0.1; applicable manifest v0.1.

## Gate results

| Gate | Result | Findings |
|---|---|---|
| GATE-LEGAL-ACCURACY | FAIL | 10269-F01, 10269-F02, 10269-F03 |
| GATE-LOCAL-ACCURACY | FAIL | 10269-F01 |
| GATE-TECHNICAL-SEO | FAIL | 10269-F05 |
| GATE-COMPLIANCE-RISK | PASS | No failure identified in available evidence |
| GATE-ANECDOTE-INTEGRITY | FAIL | 10269-F04 |
| VIDEO-TRANSCRIPT-LITERAL | PASS | No failure identified in available evidence |
| CORNERSTONE-COMPANION-VIDEO | FAIL | 10269-F05 |
| VIDEO-CONSISTENCY | FAIL | 10269-F01, 10269-F02, 10269-F03 |

FAIL for an inaccessible technical or package comparison means **not cleared**; it does not prove absent schema, broken URLs, invalid editor blocks or GBP factual drift. The binary schema has no separate blocked status. CORNERSTONE-STRUCTURE passes on the answer-first intro, facts table, body, practice section, eligibility list/calendar, five anchored FAQs, sources and CTA. The practice section's provenance remains a separate failure. On the video, VIDEO-TRANSCRIPT-LITERAL passes only for the accurate pre-recording label “Video Script”; no spoken transcript was audited.

## Findings

### 10269-F01 — Type A

**Finding:** So a tenant who moved in any time in 2025 gets their first increase on January 1, 2027.

**Root cause:** The script makes eligibility sound automatic and applies Berkeley's fully-covered-unit rule to all Berkeley rentals. The page's introduction and takeaways repeat the broad claim; lease and compliance conditions are omitted. Source: https://rentboard.berkeleyca.gov/rights-responsibilities/rent-levels/annual-general-adjustment

**Fix:** Replace with: 'For fully rent-controlled Berkeley units, 2025 move-ins first become AGA-eligible on January 1, 2027; 2026 move-ins first become eligible in January 2028, subject to the lease, proper notice and Rent Board compliance.' Use the same qualifications in the introduction, takeaways and parent script.

**Future prevention:** Recheck page prose, takeaways and script together whenever the parent changes.

### 10269-F02 — Type A

**Finding:** Units covered only by state law can go up as much as eight point eight percent.

**Root cause:** The script does not state the August 2026-July 2027 window for this rate or its rolling-period limit; it can sound like a fresh increase allowance at each anniversary. The page should not imply every state-only unit can take the full amount regardless of earlier increases.

**Fix:** Replace with: 'For AB 1482-only units, the cap for increases effective August 1, 2026 through July 31, 2027 is 8.8% over a rolling 12 months, not an additional 8.8% after an earlier increase.' Use the same date window in Key Takeaways. The official Oakland allowable-increases page corroborates 8.8%; the DRE 2026 guide corroborates the rolling-period framework.

**Future prevention:** Include the effective window and rolling-period basis in every standalone rate summary.

### 10269-F03 — Type A

**Finding:** For a January 1 increase, mail the thirty-day notice by November 25, or deliver it in person by December 1.

**Root cause:** This standalone instruction omits when 30 days is enough and assumes within-California mailing. The targets provide adequate buffer for that scenario; the error is their universal framing. Official DRE 2026 guide, printed pp.44-46: https://www.dre.ca.gov/publications/ResourceGuidebook/2026_Landlord_Tenant_Guide.pdf

**Fix:** Replace with: 'For a lawful January 1 increase that qualifies for 30-day notice, our conservative targets are November 25 for first-class mailing within California, or December 1 for personal delivery. Larger cumulative increases or mailing from elsewhere need a different notice calculation.' Repeat this qualification in the takeaways and cite the DRE guide in Resources.

**Future prevention:** Carry the notice scenario's conditions into short-form scripts.

### 10269-F05 — Type A/B

**Finding:** 🎥 Video in production. The embed will appear here once it's published.

**Root cause:** The video page is not production-complete. 'Video Script' is correctly labeled, but there is no finished recording to compare or transcript to verify. Metadata and balanced block comments were inspected; inaccessible draft previews prevent verification of rendered schema, editor validity and final URLs.

**Fix:** Keep this post in draft until the recording is embedded and checked against the script. Keep 'Video Script' until a verbatim transcript is available; then use 'Video Transcript' with the checked spoken text. Verify rendered VideoObject metadata against the final video and confirm the parent article link in an authenticated preview.

**Future prevention:** Require a separate completed-media and rendered-page check before clearing the video page.

### 10269-F04 — Type B

**Finding:** That's why, at AEBP, Berkeley is the one city where we raise rent on January 1.

**Root cause:** The cited company records support the portfolio count, but not the new January 1 and anniversary policies or unit-level tracking practices. No relevant confirmation appeared in the anecdote log.

**Fix:** Retain only after Brian confirms the practice in an identifiable internal record. Pending confirmation, replace with: 'For eligible fully covered Berkeley units, January 1 can avoid waiting until a later lease anniversary.' Replace 'Outside Berkeley, we time increases to each unit’s lease anniversary' with 'Outside Berkeley, check the lease and the local eligibility rules before choosing an increase date.' Remove unconfirmed tracking claims from the CTA; retain the documented 600+ unit count.

**Future prevention:** Use documented operational facts or clearly framed professional analysis.

## Scored categories

All scores are editorial estimates, not computed rubric results. Overall is an independent estimate, not an asserted weighted average.

| Category | Estimate | Minimum | Status | Working | Holding it back |
|---|---:|---:|---|---|---|
| SCORE-SEO | 90 | 90 | PASS | Specific topic and populated metadata; parent and Berkeley guide links. | Final video and rendered technical checks pending. |
| SCORE-GEO | 87 | 95 | FAIL | Concise takeaways and authoritative resources. | Coverage, rolling cap and notice conditions missing from standalone summaries. |
| SCORE-EEAT | 87 | 95 | FAIL | Links to city sources and documented business scale. | Unverified practices; recording unavailable. |
| SCORE-READABILITY | 94 | 90 | PASS | Short accessible script; useful November move-in example. | A few qualifiers are needed to prevent misleading certainty. |
| SCORE-CONVERSION | 90 | 85 | PASS | Clear parent-guide and consultation paths. | Video itself remains unavailable and tracking claim unverified. |
| SCORE-OVERALL | 88 | 95 | FAIL | Coherent companion to the written guide. | Content fixes and production/technical clearance required. |

## Strengths Worth Preserving

- Correct effective-date distinction between Berkeley's calendar year and Oakland/AB 1482's August-July cycle.
- Berkeley new-tenancy delay and 2027 2.5% AGA independently corroborated.
- Hypothetical unit examples identified as examples; Video Script correctly labeled before recording.
- Useful November move-in comparison and specific consultation path.

## Claim provenance

- **10269-C01: unverified** — “We manage 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay, and track every unit's increase date and rate for its jurisdiction.” Portfolio count and service area documented; operational tracking unverified.
- **10269-C02: unverified** — “That's why, at AEBP, Berkeley is the one city where we raise rent on January 1.” No confirming operational record identified in the reviewed company sources.
- **10269-C03: unverified** — “Outside Berkeley, we time increases to each unit's lease anniversary.” No confirming operational record identified in the reviewed company sources.

Repeated scheduling/tracking claims in the comparison table, FAQ and embedded parent script share the dispositions above; no repetition is separately verified. Company scale (600+ units), service area and AppFolio use are supported by knowledge/company/overview.md and knowledge/llms.txt. No AI owner_verified classification assigned.

## Article fixes

- 10269-F01: Replace with: 'For fully rent-controlled Berkeley units, 2025 move-ins first become AGA-eligible on January 1, 2027; 2026 move-ins first become eligible in January 2028, subject to the lease, proper notice and Rent Board compliance.' Use the same qualifications in the introduction, takeaways and parent script.
- 10269-F02: Replace with: 'For AB 1482-only units, the cap for increases effective August 1, 2026 through July 31, 2027 is 8.8% over a rolling 12 months, not an additional 8.8% after an earlier increase.' Use the same date window in Key Takeaways. The official Oakland allowable-increases page corroborates 8.8%; the DRE 2026 guide corroborates the rolling-period framework.
- 10269-F03: Replace with: 'For a lawful January 1 increase that qualifies for 30-day notice, our conservative targets are November 25 for first-class mailing within California, or December 1 for personal delivery. Larger cumulative increases or mailing from elsewhere need a different notice calculation.' Repeat this qualification in the takeaways and cite the DRE guide in Resources.
- 10269-F05: Keep this post in draft until the recording is embedded and checked against the script. Keep 'Video Script' until a verbatim transcript is available; then use 'Video Transcript' with the checked spoken text. Verify rendered VideoObject metadata against the final video and confirm the parent article link in an authenticated preview.
- 10269-F04: Retain only after Brian confirms the practice in an identifiable internal record. Pending confirmation, replace with: 'For eligible fully covered Berkeley units, January 1 can avoid waiting until a later lease anniversary.' Replace 'Outside Berkeley, we time increases to each unit’s lease anniversary' with 'Outside Berkeley, check the lease and the local eligibility rules before choosing an increase date.' Remove unconfirmed tracking claims from the CTA; retain the documented 600+ unit count.

## Operating System improvements

- Refresh Berkeley 2027 rate and election-dependent Measure X notes in the existing rent-cap reference after primary-source verification; do not alter standards as part of this review. Target: knowledge/laws/rent-caps.md.
- If Brian confirms the scheduling and tracking practices, record their exact scope and reuse limits. Target: knowledge/company/anecdote-log.md.

## Evidence and review limits

- [Berkeley AGA and eligibility](https://rentboard.berkeleyca.gov/rights-responsibilities/rent-levels/annual-general-adjustment) — verified 2.5% for 2027 and new-tenancy delay; compliance exceptions checked.
- [Oakland allowable increases](https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases) — verified 2.3% cycle, 8.8% state-cap corroboration, banking total and prerequisites.
- [Official DRE 2026 landlord/tenant guide](https://www.dre.ca.gov/publications/ResourceGuidebook/2026_Landlord_Tenant_Guide.pdf) — printed pp.39 and 44–46 for exemption and notice qualifications. Official statute URLs returned 403.
- [Berkeley official November 2026 impartial analyses](https://berkeleyca.gov/sites/default/files/Nov%202026%20Impartial%20Analyses.pdf) — Measure X analyzed on PDF pp.6–7. Pending proposal as of this review; election outcome and operative law must be rechecked if publication occurs after the vote.

Reviewed current AEBP-Dev full snapshots; no revision identifier or GMT modified time returned. Source post_modified values (site-local, timezone not supplied): 10268 = 2026-10-30 20:28:58; 10269 = 2026-10-30 20:28:59. Repo clean and zero commits ahead of the configured upstream at start; no fetch performed, so remote freshness is not independently established. Standards: docs/01 v0.5, /02 v0.2, /03 v0.3, /07 v0.1; manifests v0.1. Schema version 1.0.0 follows existing review artifacts; the schema does not declare a version constant. Draft previews and prospective production URLs could not be retrieved; generated schema is unverified, not proven missing. Gutenberg comment nesting is balanced in both snapshots, not a substitute for WordPress editor validation. SEO fields are populated. Live Berkeley guide, rent-cap update, banking tip, exemption-notice tip, month-to-month guide and /lets-talk/ retrieved successfully. GBP copy not supplied/reviewed. Official Leginfo sections 827 and 1947.12 returned 403; accessible official DRE 2026 guidance used instead. No WordPress edits or publication performed. Claude should produce 02-revision-response.md/json for every finding, then request re-review.

The November 25 / December 1 targets are conservative for the described within-California 30-day scenario; no finding claims they are too late. Calendar review must not imply they cover a 90-day scenario. Month-count examples assume first-of-month starts; add that label if presenting exact elapsed-month counts.

## Handoff

Claude should return reviews/posts/10269/02-revision-response.md and .json, with one disposition per finding ID above. Preserve this review round. After fixes, re-read both current WordPress drafts and verify all dispositions. Brian's final read-through remains required.

