# Pre-Publish Audit — Post 10340

Berkeley Measure X Passed: What Changes for Landlords, and When

Recommendation: **Hold pending fixes.** Reviewed November 6, 2026. Both WordPress posts remain drafts.

## GATE-LEGAL-ACCURACY — FAIL

### 10340-F01 (A)

Quote: Now it's ten percent at a time, with the rest still banked for later.

Root cause: The script switches from future effect to present operation and loses the rolling 12-month limit. FAQ labels the carry-forward reading as interpretation but the script does not.

Fix: Once Measure X takes effect, AGA-based increases will be limited to 10% in a 12-month period. Our reading is that unused amounts remain in the rent ceiling for later; confirm the available amount with the Rent Board.

### 10340-F02 (A)

Quote: And tenant associations can now form in self-managed buildings with five or more units.

Root cause: Premature 'now'; the statutory test uses parcels, not individual buildings. Official PDF page 18 visually confirms both redline changes and preservation after a manager leaves.

Fix: Once the measure takes effect, tenants on self-managed parcels with five to nine rental units will become eligible to form an association under the ordinance. Professionally managed parcels already qualified at any size. An established association will also keep its rights if the management company leaves.

### 10340-F03 (A)

Quote: everything in this table except the 2027 AGA became law on November 3, 2026, pending certification.

Root cause: Election day, declaration/adoption and effective date are conflated. The table even includes the unannounced effective date as something supposedly enacted.

Fix: Voters approved these amendments in the November 3 election, according to unofficial results. They are not yet in effect; the operative date remains to be confirmed. The 2027 AGA is a separate Rent Board determination. Also replace 'Before November 3' with 'Before Measure X takes effect' in the AEBP observation.

### 10340-F04 (A)

Quote: The change only reaches self-managed buildings with 5 to 9 units.

Root cause: The threshold expansion is narrower than all changes to association rights; the survival provision also affects professionally managed parcels. See official ballot PDF page 18 and City Attorney analysis items 5–7.

Fix: The threshold expansion reaches self-managed parcels with five to nine rental units. Measure X also preserves an established association's rights if the property management company leaves. Rename the subsection 'Tenant associations: lower thresholds and continuing rights'.

### 10340-F05 (A)

Quote: the owner could serve one increase to about $2,811 (with 90 days' notice, since it's over 10%).

Root cause: The example includes the 2027 AGA, unavailable before January 1; framed as a pre-effective-date action it suggests notice could defeat the future cap. Eligibility for 2023 is not established merely by saying rent reached its ceiling in 2022.

Fix: Without Measure X's new cap, the hypothetical 2027 ceiling would be about $2,811. This is a comparison of rules, not a suggestion that serving notice before the measure takes effect permits that January increase. Assume the tenancy began before 2022, rent was $2,500 at the end of 2022, and the unit remained eligible for every listed AGA.

### 10340-F06 (A+B)

Quote: One side effect: the 90-day notice path mostly goes away

Root cause: The section needs the statutory aggregation/service assumptions and a source for mail timing; live LegInfo sections returned 403. Repo civ-827.txt confirms cumulative increases and longer contractual requirements, not an unconditional 30-day result.

Fix: For AGA-only increases that stay within 10% over the preceding 12 months, the ordinary statutory notice period is 30 days. Longer contractual or other applicable notice requirements still control. The November 25 mailing target assumes mailing within California and includes a conservative extra day. Before publication, verify Civil Code 827(b)-(c), CCP 1013(a), and Elections Code 9217 against an accessible official source and cite them.

## GATE-LOCAL-ACCURACY — FAIL

### 10340-F02 (A)

Quote: And tenant associations can now form in self-managed buildings with five or more units.

Root cause: Premature 'now'; the statutory test uses parcels, not individual buildings. Official PDF page 18 visually confirms both redline changes and preservation after a manager leaves.

Fix: Once the measure takes effect, tenants on self-managed parcels with five to nine rental units will become eligible to form an association under the ordinance. Professionally managed parcels already qualified at any size. An established association will also keep its rights if the management company leaves.

## GATE-TECHNICAL-SEO — FAIL

### 10340-F07 (A+B)

Quote: Bottom Line

Root cause: CORNERSTONE-STRUCTURE requires a Before You Act checklist. Technical gate also requires a Berkeley deep-dive link, absent in the draft; rendered schema and blocks could not be checked through anonymous draft URLs.

Fix: Before You Serve a Berkeley Rent Increase: Confirm coverage and tenancy eligibility; verify the registered ceiling, unused AGAs and prior 12-month increases; confirm Measure X's effective date; check registration, deposit interest, repair orders and lease limits; calculate notice and service time. Add a contextual link to the site's Berkeley rent-control deep-dive guide after resolving its live URL. Replace the video teaser's 'with chapter links and a full transcript' with 'with the draft script below' until production is complete. Validate rendered blocks, schema and media in authenticated preview.

## GATE-COMPLIANCE-RISK — PASS

## GATE-ANECDOTE-INTEGRITY — PASS

## CORNERSTONE-STRUCTURE — FAIL

### 10340-F07 (A+B)

Quote: Bottom Line

Root cause: CORNERSTONE-STRUCTURE requires a Before You Act checklist. Technical gate also requires a Berkeley deep-dive link, absent in the draft; rendered schema and blocks could not be checked through anonymous draft URLs.

Fix: Before You Serve a Berkeley Rent Increase: Confirm coverage and tenancy eligibility; verify the registered ceiling, unused AGAs and prior 12-month increases; confirm Measure X's effective date; check registration, deposit interest, repair orders and lease limits; calculate notice and service time. Add a contextual link to the site's Berkeley rent-control deep-dive guide after resolving its live URL. Replace the video teaser's 'with chapter links and a full transcript' with 'with the draft script below' until production is complete. Validate rendered blocks, schema and media in authenticated preview.

## CORNERSTONE-AEBP-VOICE — PASS

## CORNERSTONE-COMPANION-VIDEO — PASS

## Scores (estimates)

| Category | Score | Minimum | Result |
|---|---:|---:|---|
| SCORE-SEO | 91 | 90 | PASS |
| SCORE-GEO | 92 | 95 | FAIL |
| SCORE-EEAT | 93 | 95 | FAIL |
| SCORE-READABILITY | 92 | 90 | PASS |
| SCORE-CONVERSION | 90 | 85 | PASS |
| SCORE-OVERALL | 92 | 95 | FAIL |

Working: local focus, answer-first copy, source links, practical CTA. Holding back: findings above and pending rendered checks.

## Strengths worth preserving

- Both tenant-association numeric redlines verified visually in official ballot PDF, printed p.18.
- 2027 AGA and historical figures match Rent Board publications; banking arithmetic correct.
- Removed unsupported AEBP claims remain absent; table's retained tracking/registration claims are documented.
- Golden Duplex notice and lower-state-limit language from superseded drafts are absent.

## Article fixes

- 10340-F01
- 10340-F02
- 10340-F03
- 10340-F04
- 10340-F05
- 10340-F06
- 10340-F07

## Operating System improvements

Commit the pending reference corrections and TEST-LEGAL-009; retain visual verification and continuing-association-rights notes.

## Verification limits

Remote main at review: 9e490e00d109ff0e280a777ee4b617751605a82f; local HEAD differs and has pending knowledge/test content. No local worktree/push state could be verified because git status reports 'must be run in a work tree'; dirty denotes known pending reference differences. Reviewed WP modified local fields 2026-11-06 17:52:50 / 17:53:41; timezone not supplied. Draft URLs inaccessible to anonymous rendering; schema/render checks remain pending. GBP copy not supplied and consistency not assessed. Primary sources: official Measure X PDF (visual page 18); City Attorney analysis pp.6–7; AGA page and history list; County unofficial result 67.51% (17,270/25,580), so 68% is acceptable rounded but add as-of date and official county link. 2024 BB effective date confirmed on Rent Board site; live statutory URLs were 403, not claimed verified.
