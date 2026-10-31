# Editorial Review — Post 10268

Oakland and Berkeley Rent Increases for 2027: The New Numbers, and Which One Applies to Each Unit

Recommendation: **HOLD PENDING FIXES**. Review mode: Pre-Publish Audit.
Snapshot: AEBP-Dev draft; site-local modified 2026-10-30 20:28:58. Revision ID / GMT timestamp unavailable.
Reviewed 2026-10-31T03:37:26.101Z. Repository commit c4534e57057f7ec5bebccc3578c4f5cbb18d875c; working tree clean before artifacts; zero commits ahead of configured upstream (no remote fetch).
Standards: docs/01 v0.5; docs/02 v0.2; docs/03 v0.3; docs/07 v0.1; applicable manifest v0.1.

## Gate results

| Gate | Result | Findings |
|---|---|---|
| GATE-LEGAL-ACCURACY | FAIL | 10268-F01, 10268-F02, 10268-F03, 10268-F04, 10268-F05 |
| GATE-LOCAL-ACCURACY | FAIL | 10268-F01, 10268-F02, 10268-F03 |
| GATE-TECHNICAL-SEO | FAIL | 10268-F07 |
| GATE-COMPLIANCE-RISK | PASS | No failure identified in available evidence |
| GATE-ANECDOTE-INTEGRITY | FAIL | 10268-F06 |
| CORNERSTONE-STRUCTURE | PASS | No failure identified in available evidence |
| CORNERSTONE-AEBP-VOICE | FAIL | 10268-F06 |
| CORNERSTONE-COMPANION-VIDEO | FAIL | 10268-F07 |
| CORNERSTONE-GBP-CONSISTENCY | FAIL | 10268-F08 |

FAIL for an inaccessible technical or package comparison means **not cleared**; it does not prove absent schema, broken URLs, invalid editor blocks or GBP factual drift. The binary schema has no separate blocked status. CORNERSTONE-STRUCTURE passes on the answer-first intro, facts table, body, practice section, eligibility list/calendar, five anchored FAQs, sources and CTA. The practice section's provenance remains a separate failure. On the video, VIDEO-TRANSCRIPT-LITERAL passes only for the accurate pre-recording label “Video Script”; no spoken transcript was audited.

## Findings

### 10268-F01 — Type A

**Finding:** In Berkeley it's January 1: tenancies that began in 2025 or earlier can take 2.5% on January 1, 2027, and tenancies that began in 2026 wait until January 1, 2028.

**Root cause:** The quick answer, FAQ 3, script and several tables omit the fully-covered-unit qualifier and make first eligibility sound automatic. The body later acknowledges lease and compliance restrictions. The AGA changes the rent ceiling; banking may make an actual increase different from 2.5%. The FAQ's 'on or after' wording also extends a 2027 figure beyond its verified year. Verified against the Berkeley AGA page: https://rentboard.berkeleyca.gov/rights-responsibilities/rent-levels/annual-general-adjustment

**Fix:** Replace the quoted sentence with: 'For fully rent-controlled Berkeley units, 2025 move-ins first become AGA-eligible on January 1, 2027; 2026 move-ins first become eligible on January 1, 2028, subject to the lease, proper notice and Rent Board compliance. The 2027 AGA is 2.5%; eligible banked AGAs can affect the actual increase.' Replace 'on or after January 1, 2027' in FAQ 1 with 'during calendar year 2027'. Apply the fully-covered-unit and eligibility qualifiers to FAQ 3, the script, tables and companion page.

**Future prevention:** Check coverage, eligibility, rent ceiling and actual increase separately; synchronize both scripts.

### 10268-F02 — Type A

**Finding:** A banked increase can add more, up to three times the current rate (6.9%).

**Root cause:** The wording can be read as allowing 6.9% of banking in addition to 2.3%. The limit applies to the total CPI-plus-banking increase. The FAQ is clearer but should be explicit. Source: https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases

**Fix:** Replace with: 'Eligible banked CPI amounts can be added, but the combined current CPI plus banking increase cannot exceed 6.9% this cycle.' Use that same total-limit wording in the Key Facts table and FAQ 4.

**Future prevention:** Write every banking limit as a total or an additional amount explicitly.

### 10268-F03 — Type A

**Finding:** Confirm the unit's last increase took effect at least 12 months earlier.

**Root cause:** Oakland's action list omits registration compliance, the first-increase wait and the six-month RAP-notice prerequisite. Having a tax certificate also differs from attaching the required document. Verified on the City's allowable-increases page and rent-registration FAQs.

**Fix:** Replace with: 'Confirm the unit is registered with RAP, the first increase is at least 12 months after move-in, any prior increase was at least 12 months ago, and at least six months have passed since the tenant first received the RAP Notice.' Replace 'have a current Business Tax Certificate or a payment plan for delinquent business taxes' with 'attach a current Business Tax Certificate or, for a CPI-only increase, a current signed City payment plan for delinquent business taxes'. Retain the current-certificate requirement for banking. Add an internal link to the existing Oakland rent-control deep dive.

**Future prevention:** Use a complete jurisdiction-specific eligibility checklist before calendar advice; source: https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases

### 10268-F04 — Type A

**Finding:** Single-family homes and condos are exempt from AB 1482 only if the tenant received the required written exemption notice.

**Root cause:** In an exemption summary, the notice-only description is incomplete: qualifying ownership also matters. A corporate owner cannot create this exemption just by delivering notice. Official DRE 2026 guide, printed p.39 (PDF p.45), summarizes the ownership and notice tests: https://www.dre.ca.gov/publications/ResourceGuidebook/2026_Landlord_Tenant_Guide.pdf

**Fix:** Replace with: 'The single-family-home/condo exemption also requires qualifying ownership: no REIT, corporation, or LLC with a corporate member, plus the required written exemption notice. Notice alone does not establish eligibility.' Cite Civil Code §1947.12(d)(5)(A)-(B), with the DRE guide as the accessible official corroboration.

**Future prevention:** Check exemption conditions as a conjunction; never reduce an exemption to its notice requirement.

### 10268-F05 — Type A

**Finding:** The same math works for any date: count back 30 days for personal service, or 35 if you mail the notice.

**Root cause:** The blanket instruction excludes the 90-day branch and the mailing-origin distinction. The FAQ also omits the cumulative 12-month test. The published November 25/December 1 targets are conservative, not late; do not 'correct' them as invalid. Official DRE 2026 guide, printed pp.44-46: https://www.dre.ca.gov/publications/ResourceGuidebook/2026_Landlord_Tenant_Guide.pdf

**Fix:** Replace with: 'For an otherwise lawful increase, use at least 30 days when the cumulative increase is 10% or less over the preceding 12 months; use 90 days above 10%, measured from the lowest rent in that period. First-class mailing within California adds five days; mailing from elsewhere can require longer. November 25 and December 1 are conservative planning targets for a January 1 increase that qualifies for 30-day notice.' Apply these qualifications to the Key Facts notice rows, calendar, FAQ 5 and script. Add the official DRE guide to Sources.

**Future prevention:** Test both notice branches and mailing origin; label conservative targets as planning targets.

### 10268-F07 — Type A/B

**Finding:** Watch the short video version, with chapter links and a full transcript.

**Root cause:** The draft itself says video in production, so this invitation promises unavailable assets. SEO metadata and balanced Gutenberg comments were checked, but draft previews and prospective article/video URLs were inaccessible to web retrieval. Generated schema, editor block validity, front-end appearance and paired destination availability remain unverified; no claim that schema is absent.

**Fix:** Until the video is ready, replace with: 'Companion video in production; the video and transcript will be added when ready.' Keep 'Video Script' until the recording is final. Before publication, insert the completed embed, verify its spoken content and transcript, and restore the video invitation only when the destination works. In an authenticated preview, verify BlogPosting/FAQPage output, block validity, paired URLs and internal links.

**Future prevention:** Separate draft-content review from rendered-page and media-production clearance.

### 10268-F06 — Type B

**Finding:** Every unit we manage has its own increase-eligibility date, and we track it in AppFolio, our property management software.

**Root cause:** The company overview supports 600+ units and AppFolio use, but no internal record read in this review documents these new operational claims: anniversary scheduling, January 1 scheduling, second-January setup, skipped-increase motives and service practices. The anecdote log does not contain them. This is unverified, not proof of fabrication.

**Fix:** Retain the operational wording only after Brian confirms it in a cited internal record. Pending confirmation, replace the opening practice assertion with: 'Track each unit’s increase eligibility separately, including lease restrictions and local requirements.' Replace 'In Berkeley, we raise rent on January 1' with 'For an eligible fully covered Berkeley tenancy, January 1 may be the earliest available AGA date.' Remove unconfirmed AppFolio setup, universal anniversary, owner-motive and service-performance assertions from prose, comparison table and scripts. If using this fallback, supply a real documented observation to retain CORNERSTONE-AEBP-VOICE.

**Future prevention:** Document new company-practice assertions before review; do not infer confirmation from plausibility.

### 10268-F08 — Type B

**Finding:** The 2027 numbers are set: 2.5% in Berkeley, 2.3% in Oakland through July, and 8.8% under AB 1482 through July.

**Root cause:** This package-level check requires actual GBP copy; no GBP draft was supplied or found in the requested WordPress assets. This is an unavailable comparison, not evidence of factual drift.

**Fix:** Use this scoped GBP draft for comparison: 'Planning a 2027 rent increase? Berkeley’s 2027 AGA is 2.5%; Oakland’s annual CPI allowance is 2.3% through July 31, 2027. Eligibility, banking and notice requirements vary. Read our guide before choosing an effective date.' Supply the actual approved GBP copy for comparison before package clearance; do not publish this proposal automatically.

**Future prevention:** Include companion GBP copy in the package handed to review.

## Scored categories

All scores are editorial estimates, not computed rubric results. Overall is an independent estimate, not an asserted weighted average.

| Category | Estimate | Minimum | Status | Working | Holding it back |
|---|---:|---:|---|---|---|
| SCORE-SEO | 92 | 90 | PASS | Clear 2027 search intent, focus keyword, title and description populated; useful related articles. | Rendered schema and destination checks remain open. |
| SCORE-GEO | 90 | 95 | FAIL | Answer-first summary, comparative tables, five anchored FAQs and identifiable sources. | Standalone answers overgeneralize coverage and eligibility; notice and banking ambiguity. |
| SCORE-EEAT | 88 | 95 | FAIL | Primary agency sources; documented portfolio scale; practical operational detail. | New practice claims lack provenance and eligibility guidance is incomplete. |
| SCORE-READABILITY | 93 | 90 | PASS | Move-in table and timing examples make a complicated rule usable. | Repeated script and repeated January 1 explanations lengthen the page; absolute language conflicts with later caveats. |
| SCORE-CONVERSION | 91 | 85 | PASS | Relevant property consultation CTA and live contact destination. | Operational promises require confirmation. |
| SCORE-OVERALL | 90 | 95 | FAIL | Strong practical calendar and effective-date approach. | Blocking content/provenance findings and incomplete technical audit. |

## Strengths Worth Preserving

- Correct effective-date distinction between Berkeley's calendar year and Oakland/AB 1482's August-July cycle.
- Berkeley new-tenancy delay and 2027 2.5% AGA independently corroborated.
- Hypothetical unit examples identified as examples; Video Script correctly labeled before recording.
- Useful November move-in comparison and specific consultation path.

## Claim provenance

- **10268-C01: unverified** — “Every unit we manage has its own increase-eligibility date, and we track it in AppFolio, our property management software.” No confirming operational record identified in the reviewed company sources.
- **10268-C02: unverified** — “Outside Berkeley, that date is the lease anniversary.” No confirming operational record identified in the reviewed company sources.
- **10268-C03: unverified** — “In Berkeley, we raise rent on January 1.” No confirming operational record identified in the reviewed company sources.
- **10268-C04: unverified** — “So when a new Berkeley tenancy starts, we set its first eligibility date in AppFolio to the second January after move-in.” No confirming operational record identified in the reviewed company sources.
- **10268-C05: unverified** — “Owners sometimes choose to skip a year, most often to keep a good tenant.” No confirming operational record identified in the reviewed company sources.
- **10268-C06: unverified** — “Served on schedule with proof of service” No confirming operational record identified in the reviewed company sources.
- **10268-C07: unverified** — “Included with every Oakland increase” No confirming operational record identified in the reviewed company sources.
- **10268-C08: unverified** — “We manage 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay, and track every unit's increase date and rate for its jurisdiction.” 600+ units and service area are documented in overview.md; unit-by-unit tracking is unverified, so the compound claim is not cleared.
- **10268-C09: unverified** — “That's why, at AEBP, Berkeley is the one city where we raise rent on January 1.” No confirming operational record identified in the reviewed company sources.
- **10268-C10: unverified** — “Outside Berkeley, we time increases to each unit's lease anniversary.” No confirming operational record identified in the reviewed company sources.
- **10268-C11: unverified** — “AEBP takes Berkeley increases on January 1 for that reason.” No confirming operational record identified in the reviewed company sources.

Repeated scheduling/tracking claims in the comparison table, FAQ and embedded parent script share the dispositions above; no repetition is separately verified. Company scale (600+ units), service area and AppFolio use are supported by knowledge/company/overview.md and knowledge/llms.txt. No AI owner_verified classification assigned.

## Article fixes

- 10268-F01: Replace the quoted sentence with: 'For fully rent-controlled Berkeley units, 2025 move-ins first become AGA-eligible on January 1, 2027; 2026 move-ins first become eligible on January 1, 2028, subject to the lease, proper notice and Rent Board compliance. The 2027 AGA is 2.5%; eligible banked AGAs can affect the actual increase.' Replace 'on or after January 1, 2027' in FAQ 1 with 'during calendar year 2027'. Apply the fully-covered-unit and eligibility qualifiers to FAQ 3, the script, tables and companion page.
- 10268-F02: Replace with: 'Eligible banked CPI amounts can be added, but the combined current CPI plus banking increase cannot exceed 6.9% this cycle.' Use that same total-limit wording in the Key Facts table and FAQ 4.
- 10268-F03: Replace with: 'Confirm the unit is registered with RAP, the first increase is at least 12 months after move-in, any prior increase was at least 12 months ago, and at least six months have passed since the tenant first received the RAP Notice.' Replace 'have a current Business Tax Certificate or a payment plan for delinquent business taxes' with 'attach a current Business Tax Certificate or, for a CPI-only increase, a current signed City payment plan for delinquent business taxes'. Retain the current-certificate requirement for banking. Add an internal link to the existing Oakland rent-control deep dive.
- 10268-F04: Replace with: 'The single-family-home/condo exemption also requires qualifying ownership: no REIT, corporation, or LLC with a corporate member, plus the required written exemption notice. Notice alone does not establish eligibility.' Cite Civil Code §1947.12(d)(5)(A)-(B), with the DRE guide as the accessible official corroboration.
- 10268-F05: Replace with: 'For an otherwise lawful increase, use at least 30 days when the cumulative increase is 10% or less over the preceding 12 months; use 90 days above 10%, measured from the lowest rent in that period. First-class mailing within California adds five days; mailing from elsewhere can require longer. November 25 and December 1 are conservative planning targets for a January 1 increase that qualifies for 30-day notice.' Apply these qualifications to the Key Facts notice rows, calendar, FAQ 5 and script. Add the official DRE guide to Sources.
- 10268-F07: Until the video is ready, replace with: 'Companion video in production; the video and transcript will be added when ready.' Keep 'Video Script' until the recording is final. Before publication, insert the completed embed, verify its spoken content and transcript, and restore the video invitation only when the destination works. In an authenticated preview, verify BlogPosting/FAQPage output, block validity, paired URLs and internal links.
- 10268-F06: Retain the operational wording only after Brian confirms it in a cited internal record. Pending confirmation, replace the opening practice assertion with: 'Track each unit’s increase eligibility separately, including lease restrictions and local requirements.' Replace 'In Berkeley, we raise rent on January 1' with 'For an eligible fully covered Berkeley tenancy, January 1 may be the earliest available AGA date.' Remove unconfirmed AppFolio setup, universal anniversary, owner-motive and service-performance assertions from prose, comparison table and scripts. If using this fallback, supply a real documented observation to retain CORNERSTONE-AEBP-VOICE.
- 10268-F08: Use this scoped GBP draft for comparison: 'Planning a 2027 rent increase? Berkeley’s 2027 AGA is 2.5%; Oakland’s annual CPI allowance is 2.3% through July 31, 2027. Eligibility, banking and notice requirements vary. Read our guide before choosing an effective date.' Supply the actual approved GBP copy for comparison before package clearance; do not publish this proposal automatically.

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

Claude should return reviews/posts/10268/02-revision-response.md and .json, with one disposition per finding ID above. Preserve this review round. After fixes, re-read both current WordPress drafts and verify all dispositions. Brian's final read-through remains required.

