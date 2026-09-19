# Post 9215 — editorial review

**Hold pending content fixes.** Structured-data/render checks are deferred to Brian near publication.

Responds to 02-revision-response.json. All seven dispositions present and response schema validated. Actual updated draft inspected: modified 2026-09-19 16:09:52 without explicit GMT. Five content findings fully closed; mandatory-offer correction in -04 verified, with a new regression recorded as -08. Brian explicitly deferred -07 to his pre-publication checks. Technical gate omitted from this scoped Editorial Review rather than falsely marked PASS. No rendered-page/schema clearance claimed. Shared scripts match exactly across 9215/9217. No WordPress changes. Repo was clean before these artifacts. Tool timestamp precedes response's stated timestamp; review order is established by numbered artifacts and actual snapshots, not inferred from that timestamp.

## Findings

### 9215-08 — Type A

> at a monthly rent no higher than the tenant's last month of the tenancy

**Root cause:** Claude removed the §827 qualification as unsupported, but §5-40.03(e)(2) expressly includes it. The definitions section alone does not state the complete rent rule.

**Fix:** Keep 'must offer' and restore 'subject to any notice provided in accordance with Civil Code §827.' Do not turn the return-rent provision into an unconditional ceiling. Source: https://ecode360.com/46994531, §5-40.03(e)(2).

**Prevention:** Check controlling provisions and every occurrence in body, summaries and companion script.

## Gates and estimated scores

- GATE-LEGAL-ACCURACY: PASS
- GATE-LOCAL-ACCURACY: FAIL
- GATE-COMPLIANCE-RISK: PASS
- GATE-ANECDOTE-INTEGRITY: PASS
- CORNERSTONE-STRUCTURE: PASS
- CORNERSTONE-AEBP-VOICE: PASS

- SCORE-SEO: 92 (minimum 90) — PASS. Specific title, SEO metadata, relevant internal links and live conversion destination. Rendered schema and page checks remain open.
- SCORE-GEO: 93 (minimum 95) — FAIL. Answer-first introduction, key facts, comparison tables and five FAQ answers. Restore the right-to-return qualification.
- SCORE-EEAT: 93 (minimum 95) — FAIL. Primary sources and documented company observation; hypothetical arithmetic explicitly labeled. Restore the right-to-return qualification.
- SCORE-READABILITY: 92 (minimum 90) — PASS. Clear sections, useful tables and an action checklist. Intro is dense and some points repeat through script and body.
- SCORE-CONVERSION: 90 (minimum 85) — PASS. Relevant Emeryville CTA and general education with attorney referral. Linked service page has broader rent-flexibility language worth separately reviewing.
- SCORE-OVERALL: 93 (minimum 95) — FAIL. Strong cornerstone structure and correctly updated central rate. Restore the right-to-return qualification.

## Preserve

- 9215-01, -02, -03, -05 and -06 resolved in actual updated post.
- 9215-04 mandatory-offer correction is present; unrelated removal of the rent qualification is tracked as 9215-08.
- Dated BLS citation is present; 8.8% remains verified.
- Structure, documented company observation and hypothetical arithmetic retained.

## Article fixes

- 9215-08: Keep 'must offer' and restore 'subject to any notice provided in accordance with Civil Code §827.' Do not turn the return-rent provision into an unconditional ceiling. Source: https://ecode360.com/46994531, §5-40.03(e)(2).
- 9215-07 is deferred to Brian's pre-publication structured-data/render check, per his instruction; not a blocker to continuing editorial work.
- Synchronize shared script changes resulting from 9217 review.

## Operating System follow-ups

- Retain the City-service exception and group-residential definition already present in the refreshed knowledge file when drafting shortened copy. This is application of existing reference material, not a missing-rule problem.
- Record the already cited license-calendar experience in the anecdote log with its internal source, so later reviews need not reconstruct provenance from published copy.
- Review the linked Emeryville service page separately: its 'Adjust rents to market rates annually' language could undermine this guide's careful explanation. This is outside the post-9215 clearance scope.

## Provenance

- 9215-C1: documented. “We've been headquartered in Emeryville since 2005” Source: knowledge/company/overview.md; https://alleastbayproperties.com/thursday-tip-emeryville-business-license/
- 9215-C2: documented. “license renewal sits on our own compliance calendar alongside the registration deadlines we track for Oakland, Berkeley, and Richmond” Source: https://alleastbayproperties.com/thursday-tip-emeryville-business-license/; knowledge/company/overview.md
- 9215-C3: documented. “we also checked the City's own Tenant Protection Resources page” Source: https://www.emeryville.org/Services/Housing/Tenant-Resources/Tenant-Protection-Resources
- 9215-C4: documented. “We're headquartered in Emeryville and have managed East Bay rentals since 2005 — including the license, notice, and City Clerk filings that sit underneath every Emeryville termination.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/thursday-tip-emeryville-business-license/
- 9215-C5: hypothetical_example. “Illustration (hypothetical arithmetic, not a client case)” Source: $3,000 rent illustration correctly shows arithmetic and requires checking current HUD FMR; no fabricated client event.

