# Pre-Publish Audit — Post 10342

Berkeley Measure X Explained for Landlords (Video)

Recommendation: **Hold pending fixes.** Reviewed November 6, 2026. Both WordPress posts remain drafts.

## GATE-LEGAL-ACCURACY — FAIL

### 10342-F01 (A)

Quote: Now it's ten percent at a time, with the rest still banked for later.

Root cause: The script switches from future effect to present operation and loses the rolling 12-month limit. FAQ labels the carry-forward reading as interpretation but the script does not.

Fix: Once Measure X takes effect, AGA-based increases will be limited to 10% in a 12-month period. Our reading is that unused amounts remain in the rent ceiling for later; confirm the available amount with the Rent Board.

### 10342-F02 (A)

Quote: And tenant associations can now form in self-managed buildings with five or more units.

Root cause: Premature 'now'; the statutory test uses parcels, not individual buildings. Official PDF page 18 visually confirms both redline changes and preservation after a manager leaves.

Fix: Once the measure takes effect, tenants on self-managed parcels with five to nine rental units will become eligible to form an association under the ordinance. Professionally managed parcels already qualified at any size. An established association will also keep its rights if the management company leaves.

### 10342-F03 (A)

Quote: Tenant associations can now form in self-managed buildings of 5 or more units; professionally managed buildings were already covered at any size

Root cause: The key takeaway repeats the premature effective-date wording and uses building rather than parcel.

Fix: Once effective, the threshold expands to self-managed parcels with five to nine units. Professionally managed parcels already qualify at any size, and established associations will retain their rights after management ends.

## GATE-LOCAL-ACCURACY — FAIL

### 10342-F02 (A)

Quote: And tenant associations can now form in self-managed buildings with five or more units.

Root cause: Premature 'now'; the statutory test uses parcels, not individual buildings. Official PDF page 18 visually confirms both redline changes and preservation after a manager leaves.

Fix: Once the measure takes effect, tenants on self-managed parcels with five to nine rental units will become eligible to form an association under the ordinance. Professionally managed parcels already qualified at any size. An established association will also keep its rights if the management company leaves.

## GATE-TECHNICAL-SEO — FAIL

### 10342-F04 (A+B)

Quote: Video in production. It will appear here once it's published.

Root cause: The draft has no finished video; no rendered VideoObject, block validity or playback could be confirmed. Statutory effective-date claim's official source was inaccessible (403).

Fix: Keep this page in draft until the final video is embedded and checked. Match the recorded words to the script, then label the checked recording text 'Video Transcript'. Verify rendered VideoObject and Gutenberg blocks, and add a contextual link to the Berkeley rent-control deep-dive guide. Verify Elections Code 9217 against an accessible official source before publishing.

## GATE-COMPLIANCE-RISK — PASS

## GATE-ANECDOTE-INTEGRITY — PASS

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

- 10342-F01
- 10342-F02
- 10342-F03
- 10342-F04

## Operating System improvements

Commit the pending reference corrections and TEST-LEGAL-009; retain visual verification and continuing-association-rights notes.

## Verification limits

Remote main at review: 9e490e00d109ff0e280a777ee4b617751605a82f; local HEAD differs and has pending knowledge/test content. No local worktree/push state could be verified because git status reports 'must be run in a work tree'; dirty denotes known pending reference differences. Reviewed WP modified local fields 2026-11-06 17:52:50 / 17:53:41; timezone not supplied. Draft URLs inaccessible to anonymous rendering; schema/render checks remain pending. GBP copy not supplied and consistency not assessed. Primary sources: official Measure X PDF (visual page 18); City Attorney analysis pp.6–7; AGA page and history list; County unofficial result 67.51% (17,270/25,580), so 68% is acceptable rounded but add as-of date and official county link. 2024 BB effective date confirmed on Rent Board site; live statutory URLs were 403, not claimed verified.
