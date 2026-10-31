# Final Review 03 — Post 10269

Berkeley and Oakland Rent Increases for 2027 Explained (Video)

**Recommendation: HOLD PENDING FIXES.** Script-content checks pass. Completed-media and technical clearance remain open.

Review mode: Pre-Publish Audit. Reviewed 2026-10-31T04:10:44.820Z.
AEBP-Dev draft, site-local modified 2026-10-30 20:45:10; revision ID and GMT modified time unavailable.
Repository: adaad453c4c8f1057d3a49a6f8a12d54c24ff194; clean at review start, zero commits ahead of configured upstream; no remote fetch.
Standards: docs/01 v0.5; docs/02 v0.2 (including the October 30 source-snapshot rule); docs/03 v0.3; docs/07 v0.1; manifests v0.1.

## Prior dispositions checked against WordPress

Both revision responses validate against the active response schema, match their preceding review timestamps, and provide a disposition for every prior finding.

| Finding | Final-review status | Evidence |
|---|---|---|
| 10269-F01 | closed | Fully-covered-unit, first-eligibility and lease/compliance qualifiers are present. |
| 10269-F02 | closed | Takeaways give the complete date window and rolling basis. Spoken script supplies the 2027 through-July endpoint and rolling basis; acceptable in the 2027 context, though the response overstates that the spoken script includes August 1. |
| 10269-F03 | closed | Planning-target scenario and within-California mail condition are present; full cumulative/mailing caveats remain in takeaways and linked guide. |
| 10269-F04 | closed | New internal anecdote record supports retained practices; CTA narrowed to eligibility-date tracking. |
| 10269-F05 | open / requires_human | Recording, transcript and technical checks remain outstanding. Content-only script review is clear; page is not publication-ready. |

## Gate results

| Gate | Result | Open findings |
|---|---|---|
| GATE-LEGAL-ACCURACY | PASS | None identified within the reviewed scope |
| GATE-LOCAL-ACCURACY | PASS | None identified within the reviewed scope |
| GATE-TECHNICAL-SEO | FAIL | 10269-F05 |
| GATE-COMPLIANCE-RISK | PASS | None identified within the reviewed scope |
| GATE-ANECDOTE-INTEGRITY | PASS | None identified within the reviewed scope |
| VIDEO-TRANSCRIPT-LITERAL | PASS | None identified within the reviewed scope |
| CORNERSTONE-COMPANION-VIDEO | FAIL | 10269-F05 |
| VIDEO-CONSISTENCY | PASS | None identified within the reviewed scope |

A technical FAIL records an uncleared check, not proof of absent schema or invalid blocks. The schema has no blocked/deferred gate state. VIDEO-TRANSCRIPT-LITERAL passes for the correct “Video Script” label only; no final recording was available. GBP consistency is limited to the exact draft supplied in response 02; nothing was posted.

## Open findings

### 10269-F05 — Type A/B

**Finding:** 🎥 Video in production. The embed will appear here once it's published.

**Root cause:** The response correctly leaves this requires_human. There is still no completed embed or spoken recording/transcript to audit, and authenticated rendered-page/schema checks remain unavailable. The script text now matches the parent's exactly.

**Fix:** Keep the video page in draft. Insert the final recording, check the transcript against the audio, then change 'Video Script' to 'Video Transcript' for the verified transcript. Verify rendered VideoObject metadata and final parent/companion destinations before clearing the technical gate.

**Future prevention:** Preserve the requires_human production item until completed-media evidence and preview checks are supplied.

## Scored categories

Editorial estimates; not a computed rubric. Overall is an independent estimate.

| Category | Estimate | Minimum | Status | Working | Holding it back |
|---|---:|---:|---|---|---|
| SCORE-SEO | 92 | 90 | PASS | Standalone eligibility and notice qualifications verified; both scripts identical; practices now documented. | No remaining script-content blocker; production and rendered-page checks prevent whole-page clearance. |
| SCORE-GEO | 95 | 95 | PASS | Standalone eligibility and notice qualifications verified; both scripts identical; practices now documented. | No remaining script-content blocker; production and rendered-page checks prevent whole-page clearance. |
| SCORE-EEAT | 95 | 95 | PASS | Standalone eligibility and notice qualifications verified; both scripts identical; practices now documented. | No remaining script-content blocker; production and rendered-page checks prevent whole-page clearance. |
| SCORE-READABILITY | 95 | 90 | PASS | Standalone eligibility and notice qualifications verified; both scripts identical; practices now documented. | No remaining script-content blocker; production and rendered-page checks prevent whole-page clearance. |
| SCORE-CONVERSION | 92 | 85 | PASS | Standalone eligibility and notice qualifications verified; both scripts identical; practices now documented. | No remaining script-content blocker; production and rendered-page checks prevent whole-page clearance. |
| SCORE-OVERALL | 94 | 95 | FAIL | Standalone eligibility and notice qualifications verified; both scripts identical; practices now documented. | No remaining script-content blocker; production and rendered-page checks prevent whole-page clearance. |

## Strengths Worth Preserving

- The two current Video Script blocks match exactly.
- Internal anecdote log now documents scheduling practices; unconfirmed operational promises were removed.
- The 6.9% combined limit, AB 1482 ownership test and cumulative notice qualifications are corrected.
- Both drafts retain balanced Gutenberg comment nesting, populated SEO metadata and useful consultation paths.

## Claim provenance

- **10269-C01: documented** — “We manage 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay, and track every unit's rent increase eligibility date.” Source: knowledge/company/anecdote-log.md, 2026-10-30 rent-increase timing entry; knowledge/company/overview.md (600+ unit count and service area).
- **10269-C02: documented** — “That's why, at AEBP, Berkeley is the one city where we raise rent on January 1.” Source: knowledge/company/anecdote-log.md, 2026-10-30 rent-increase timing entry; knowledge/company/overview.md (600+ unit count and service area).
- **10269-C03: documented** — “Outside Berkeley, we time increases to each unit's lease anniversary.” Source: knowledge/company/anecdote-log.md, 2026-10-30 rent-increase timing entry; knowledge/company/overview.md (600+ unit count and service area).

The October 30 internal record supports the retained scheduling and eligibility-date practices. “Documented” identifies that record; this AI review does not assign “owner_verified.” Removed notice-service and attachment-performance claims are closed as removed, not confirmed true. Repeated table/script wording shares the same documentary basis.

## Article fixes

- 10269-F05: Keep the video page in draft. Insert the final recording, check the transcript against the audio, then change 'Video Script' to 'Video Transcript' for the verified transcript. Verify rendered VideoObject metadata and final parent/companion destinations before clearing the technical gate.

## Operating System improvements

No additional source-file changes proposed for this video review. The parent review records the banking-reference conflict.

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

Final review round 03 follows 02-revision-response.json and checks every prior disposition against the live full AEBP-Dev snapshot, site-local post_modified 2026-10-30 20:45:10. Revision ID and modified_gmt not returned. Repo clean and zero commits ahead of configured upstream at start; no remote fetch. Docs/02 v0.2 now includes EVD-SOURCE-SNAPSHOTS (updated October 30); reviewed matching statute/ordinance snapshots and attempted live URLs. Leginfo §§827,1947.12,1013, Oakland Municode and the May 28 info sheet were inaccessible; official Berkeley/Oakland agency pages and DRE 2026 guide corroborate available checks. Failure to retrieve is not proof of absence. Draft previews inaccessible; generated schema and editor block validity not cleared. No WordPress edits/publishing. F01-F04 closed; F05 remains requires_human. Script content clear in reviewed context; video-page production remains held. Next response: 04-revision-response.md/json, then 05-final-review.

## Handoff

Respond to these open findings in reviews/posts/10269/04-revision-response.md and .json. Retain the requires_human production item until evidence is available; do not close it by deferring it again. Re-review the updated WordPress content for round 05. Brian retains the final publication decision.

