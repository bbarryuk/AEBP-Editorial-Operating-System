# Editorial Review — Post 9849

**Landlord Security Duties in California: What You're Liable For (and What You're Not)**

Recommendation: **HOLD PENDING FIXES**. Review mode: Pre-Publish Audit (rendered checks blocked).

Reviewed September 30, 2026 Pacific (2026-10-01T02:29:26Z). WordPress status: draft; modified: 2026-09-30 19:15:19, timezone unspecified. Revision ID and GMT modification time were not returned. [Dev draft](https://dev.alleastbayproperties.com/?p=9849).

Standards: docs/01 v0.5; docs/02 v0.2; docs/03 v0.3; docs/07 v0.1; cornerstone manifest v0.1. Repository: `b26e98e1871d47f82ef0dc41f3c3841c8af031cd`, clean before artifact creation, 0/0 against local origin/main.

## Gated categories

- **GATE-LEGAL-ACCURACY: FAIL** — 9849-F01, 9849-F02, 9849-F03, 9849-F04, 9849-F05
- **GATE-LOCAL-ACCURACY: PASS**
- **GATE-TECHNICAL-SEO: FAIL** — 9849-F06
- **GATE-COMPLIANCE-RISK: PASS**
- **GATE-ANECDOTE-INTEGRITY: PASS**
- **CORNERSTONE-STRUCTURE: PASS**
- **CORNERSTONE-AEBP-VOICE: PASS**
- **CORNERSTONE-COMPANION-VIDEO: PASS**
- **CORNERSTONE-GBP-CONSISTENCY: PASS**

Technical FAIL is a verification hold, not proof of absent schema. Companion/consistency PASS means the paired asset was checked; it does not mean either asset is cleared to publish.

## Findings

### 9849-F01 — Type A

**Finding:** “The tenant must tell you. You're liable if you don't fix it within a reasonable time after notice.”

**Root Cause:** The Key Facts row, lock section, comparison table and script compress §1941.3(b) into tenant-report-only notice. The table also excludes 'A lock the tenant broke or never reported'; that conflates repair responsibility, cost allocation, actual knowledge and tort liability. See Civil Code §1941.3(b), (d): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.3.

**Fix (proposed, not applied):** Under Civil Code §1941.3(b), a landlord can be liable for a violation if a covered defect remains uncorrected beyond a reasonable time after the landlord or agent actually knows about it or receives notice. A tenant report is one way to establish notice. Liability for injuries from a crime also requires the other elements of the claim, including causation.
Replace 'A lock the tenant broke or never reported' with 'Tenant-caused damage may affect who pays; it does not by itself settle the landlord’s repair or safety duties.' Replace both scripts’ notice opening with: Once you know a required lock is defective—whether through a tenant report or your own observation—act promptly and document the repair. Notice alone does not establish liability for a later crime.

**Future Prevention:** Check the short answer, tables, FAQs, metadata and both copies of the video script against the same qualified rule before recording or publishing.

### 9849-F02 — Type A

**Finding:** “Bigger measures like security guards generally aren't owed unless similar violent incidents have already happened on the premises.”

**Root Cause:** The quick answer makes prior on-site incidents sound like a prerequisite. Castaneda also recognizes other sufficiently serious indications and immediately proximate incidents. The no-liability examples, camera table ('Nothing statewide') and FAQ ('No California statute requires it') similarly turn limited authorities into broad exclusions. A working lock, no incident history or an intra-unit dispute does not alone resolve duty, breach and causation. Sources: Castaneda and Ann M. in the source ledger.

**Fix (proposed, not applied):** Replace the quick-answer guard sentence with: 'A duty to hire guards generally requires heightened foreseeability, which can arise from prior similar incidents or other sufficiently serious warning signs.' Replace the opening paragraph under 'What Landlords Generally Aren’t Responsible For' with: 'A crime does not automatically make a landlord liable. Duty depends on foreseeable risk and the burden of the proposed precaution; liability also requires breach and a causal link to the injury. A working lock, no prior on-site incident, or an incident inside a unit does not alone decide the claim.' Replace the camera table’s 'Nothing statewide' and FAQ opening with: 'Civil Code §1941.3 does not itself require cameras. Other applicable requirements, promises and property-specific negligence duties need separate assessment.' Replace the guards table’s exclusion with: 'No automatic duty to provide patrols; assess heightened foreseeability and the burden of the precaution.' Replace the script opening 'In California, usually not' with 'A crime alone does not make a California landlord liable.' Replace 'protect you from liability and help keep good tenants' in the script with 'can help reduce risk and support tenant retention.'

**Future Prevention:** Check the short answer, tables, FAQs, metadata and both copies of the video script against the same qualified rule before recording or publishing.

### 9849-F03 — Type A

**Finding:** “Every main unit entry door has a working deadbolt with at least a 13/16-inch throw.”

**Root Cause:** The checklist and standalone quick answer/script drop qualifications correctly included in the body. Section 1941.3(a)(1) covers main swinging doors, contains existing-hardware and approved-device provisions, and does not apply to horizontal sliding doors; window coverage also has exceptions.

**Fix (proposed, not applied):** Replace the quick-answer lock sentence and the script lock list with: 'Subject to statutory exceptions, Civil Code §1941.3 requires deadbolts on main swinging unit-entry doors, security or locking devices on covered openable windows, and code-compliant locks on exterior common-area doors with access to units in multifamily buildings.' Replace the first checklist item with: 'Check each covered main swinging unit-entry door for a compliant deadbolt or statutory alternative; apply the existing-hardware rules before requiring replacement.' Label the self-closing-door and lighting checklist items 'Recommended safety checks' so they do not appear to be verbatim §1941.3 mandates.

**Future Prevention:** Check the short answer, tables, FAQs, metadata and both copies of the video script against the same qualified rule before recording or publishing.

### 9849-F04 — Type A

**Finding:** “One big exception: a tenant protected from domestic violence or abuse can ask you to change the locks, and you have 24 hours after receiving qualifying documentation (Civil Code §1941.5 and §1941.6).”

**Root Cause:** The FAQ and Key Facts row merge distinct eligibility/documentation paths. Most importantly, excluding a co-tenant under §1941.6 requires a qualifying exclusion order; 'qualifying documentation' alone gives the owner no usable distinction. The reimbursement sentence omits its starting event. Sources: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.5. and https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.6.

**Fix (proposed, not applied):** Replace the FAQ’s exception and reimbursement sentences with: 'On a written request with qualifying documentation, the landlord must change covered locks at the landlord’s expense within 24 hours. Section 1941.5 applies when the alleged abuser is not a tenant of the same unit and allows several forms of documentation, including a qualifying tenant statement. Section 1941.6 applies to a co-tenant and requires a qualifying court order excluding that person from the dwelling. If the landlord misses the deadline, statutory self-change rights apply; for covered leases, reimbursement is due within 21 days after the tenant changes the locks. The tenant must use suitable replacement locks, notify the landlord within 24 hours of the change, and provide a key as the statute specifies.' Replace the Key Facts rule with: 'Written request plus the documentation required by the applicable section; 24 hours, at landlord expense. A co-tenant case under §1941.6 requires a qualifying exclusion order.'

**Future Prevention:** Check the short answer, tables, FAQs, metadata and both copies of the video script against the same qualified rule before recording or publishing.

### 9849-F05 — Type A

**Finding:** “There were no prior similar violent incidents on the premises, only general neighborhood crime.”

**Root Cause:** Ann M. records evidence of earlier crimes on the premises but no evidence the owner knew of those alleged acts; 'only general neighborhood crime' misstates the record. The case also treated the earlier offenses as insufficiently similar. Source: Ann M., 6 Cal.4th 670–671, 679–680.

**Fix (proposed, not applied):** Replace the Ann M. 'What happened' cell with: 'An employee was assaulted at a shopping center. The record included earlier on-site crimes, but no evidence the owner knew of those alleged acts; the earlier crimes also did not establish foreseeability of this assault sufficient to require guards.'

**Future Prevention:** Check the short answer, tables, FAQs, metadata and both copies of the video script against the same qualified rule before recording or publishing.

### 9849-F06 — Type B

**Finding:** “🎥 Video in production. It will appear here once it's live.”

**Root Cause:** The connector exposes draft markup and metadata, but the public draft permalink returned Page not found in the browser. Therefore rendered H1/canonical/schema, responsive tables, image rendering and Gutenberg editor validation remain unverified. Balanced block comments are not proof of editor validity. Video production is explicitly unfinished, not concealed. No evidence that schema is absent.

**Fix (proposed, not applied):** Retain 'Video in production. It will appear here once it’s live.' while drafting. No text replacement can clear the access check: review an authenticated preview or the final rendered page, validate the blocks in WordPress, then inspect applicable Article/FAQ schema and the completed video integration before full technical clearance.

**Future Prevention:** Check the short answer, tables, FAQs, metadata and both copies of the video script against the same qualified rule before recording or publishing.

## Scored categories

All scores are editorial estimates, not calibrated measurements.

| Category | Estimate | Threshold | Status | What works | What holds it back |
|---|---:|---:|---|---|---|
| SCORE-SEO | 88 | 90 | FAIL | Clear search intent, distinct title and description, contextual internal links. | Rendered technical checks and final destination verification remain open. |
| SCORE-GEO | 87 | 95 | FAIL | Answer-first structure, comparison tables and five concise FAQs. | Extractable short answers overstate legal rules; schema output not verified. |
| SCORE-EEAT | 89 | 95 | FAIL | Named author, documented AEBP process and identifiable legal authorities. | Notice and liability scope need correction; video needs direct supporting resources. |
| SCORE-READABILITY | 92 | 90 | PASS | Plain language, short sections and useful practical organization. | Some repeated summaries and oversimplified legal phrasing; blog table responsiveness unverified. |
| SCORE-CONVERSION | 90 | 85 | PASS | Relevant CTA, verified consultation destination and documented maintenance service. | Video is unfinished; avoid implying protection from liability is assured. |
| SCORE-OVERALL | 88 | 95 | FAIL | Strong structure and documented practitioner contribution. | Legal blockers and technical verification hold prevent clearance. |

## Strengths Worth Preserving

- Same-day emergency vendor dispatch is documented in the September 30 anecdote log; no invented building anecdote is needed.
- Company policy and professional opinion are distinguished from law in the long-form article; preserve those distinctions in both scripts.
- Answer-first summary, practical responsibility table, five FAQs, sources and a relevant closing CTA form a useful owner guide.
- Oakland’s actual CPTED checklist and relevant existing AEBP guides provide useful local context.

## Claim provenance

- **9849-C01: documented** — “when a tenant reports a broken entry door lock or a lobby door that won't lock, we treat it as an emergency on our 24/7 maintenance line, not a routine work order, and send a vendor the same day.” Source: knowledge/company/anecdote-log.md — 2026-09-30 entry; October/2026-10-05-week1-package-notes.md (OneDrive). Documented company process. Same-day dispatch is not a promise of same-day completed repair.

- **9849-C02: documented** — “How fast is "reasonable" for an entry lock (we treat it as same-day)” Source: knowledge/company/anecdote-log.md — 2026-09-30 entry; October/2026-10-05-week1-package-notes.md (OneDrive). Same policy repeated in table; retain distinction between dispatch and completed repair.

- **9849-C03: documented** — “Professional opinion, from managing 600+ East Bay units:” Source: knowledge/company/anecdote-log.md — 2026-09-30 entry; October/2026-10-05-week1-package-notes.md (OneDrive); knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt. Documented professional view and portfolio basis, not an observed building case or measured retention result.

- **9849-C04: documented** — “We manage 600+ East Bay rental units with a 24/7 bilingual maintenance line.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt. Live reference checked for portfolio count, service area and maintenance line; unrelated stale financial metrics were not used.

- **9849-C05: documented** — “At AEBP, we treat a broken entry or lobby lock as an emergency, with a vendor sent the same day.” Source: knowledge/company/anecdote-log.md — 2026-09-30 entry; October/2026-10-05-week1-package-notes.md (OneDrive). Exact script policy documented; do not expand into a performance statistic.

- **9849-C06: documented** — “In our view, working locks, good lighting and secure mail protect you from liability and help keep good tenants.” Source: knowledge/company/anecdote-log.md — 2026-09-30 entry; October/2026-10-05-week1-package-notes.md (OneDrive). The underlying opinion is documented. Provenance does not validate the legal breadth of 'protect you from liability'; replacement proposed in legal finding.

## Article fixes

- 9849-F01: Under Civil Code §1941.3(b), a landlord can be liable for a violation if a covered defect remains uncorrected beyond a reasonable time after the landlord or agent actually knows about it or receives notice. A tenant report is one way to establish notice. Liability for injuries from a crime also requires the other elements of the claim, including causation.
Replace 'A lock the tenant broke or never reported' with 'Tenant-caused damage may affect who pays; it does not by itself settle the landlord’s repair or safety duties.' Replace both scripts’ notice opening with: Once you know a required lock is defective—whether through a tenant report or your own observation—act promptly and document the repair. Notice alone does not establish liability for a later crime.

- 9849-F02: Replace the quick-answer guard sentence with: 'A duty to hire guards generally requires heightened foreseeability, which can arise from prior similar incidents or other sufficiently serious warning signs.' Replace the opening paragraph under 'What Landlords Generally Aren’t Responsible For' with: 'A crime does not automatically make a landlord liable. Duty depends on foreseeable risk and the burden of the proposed precaution; liability also requires breach and a causal link to the injury. A working lock, no prior on-site incident, or an incident inside a unit does not alone decide the claim.' Replace the camera table’s 'Nothing statewide' and FAQ opening with: 'Civil Code §1941.3 does not itself require cameras. Other applicable requirements, promises and property-specific negligence duties need separate assessment.' Replace the guards table’s exclusion with: 'No automatic duty to provide patrols; assess heightened foreseeability and the burden of the precaution.' Replace the script opening 'In California, usually not' with 'A crime alone does not make a California landlord liable.' Replace 'protect you from liability and help keep good tenants' in the script with 'can help reduce risk and support tenant retention.'

- 9849-F03: Replace the quick-answer lock sentence and the script lock list with: 'Subject to statutory exceptions, Civil Code §1941.3 requires deadbolts on main swinging unit-entry doors, security or locking devices on covered openable windows, and code-compliant locks on exterior common-area doors with access to units in multifamily buildings.' Replace the first checklist item with: 'Check each covered main swinging unit-entry door for a compliant deadbolt or statutory alternative; apply the existing-hardware rules before requiring replacement.' Label the self-closing-door and lighting checklist items 'Recommended safety checks' so they do not appear to be verbatim §1941.3 mandates.

- 9849-F04: Replace the FAQ’s exception and reimbursement sentences with: 'On a written request with qualifying documentation, the landlord must change covered locks at the landlord’s expense within 24 hours. Section 1941.5 applies when the alleged abuser is not a tenant of the same unit and allows several forms of documentation, including a qualifying tenant statement. Section 1941.6 applies to a co-tenant and requires a qualifying court order excluding that person from the dwelling. If the landlord misses the deadline, statutory self-change rights apply; for covered leases, reimbursement is due within 21 days after the tenant changes the locks. The tenant must use suitable replacement locks, notify the landlord within 24 hours of the change, and provide a key as the statute specifies.' Replace the Key Facts rule with: 'Written request plus the documentation required by the applicable section; 24 hours, at landlord expense. A co-tenant case under §1941.6 requires a qualifying exclusion order.'

- 9849-F05: Replace the Ann M. 'What happened' cell with: 'An employee was assaulted at a shopping center. The record included earlier on-site crimes, but no evidence the owner knew of those alleged acts; the earlier crimes also did not establish foreseeability of this assault sufficient to require guards.'

- 9849-F06: Retain 'Video in production. It will appear here once it’s live.' while drafting. No text replacement can clear the access check: review an authenticated preview or the final rendered page, validate the blocks in WordPress, then inspect applicable Article/FAQ schema and the completed video integration before full technical clearance.

## Operating System improvements

- Type C follow-up (not an additional content blocker): Add a focused security-duty reference covering actual/received notice, duty versus causation, qualified lock coverage, co-tenant exclusion orders and the guard-duty foreseeability test. Independently checked sources support this review; absence of a local reference is not an extra publication blocker. Target: `knowledge/laws/landlord-security-duties.md`.

- Type C follow-up (not an additional content blocker): Declare the schema release version explicitly; 1.0.0 currently comes from established review artifacts rather than a version in the schema itself. Target: `automation/schemas/review.schema.json`.

- Type C follow-up (not an additional content blocker): Add an explicit deferred/blocked verification representation for pre-recording drafts so FAIL can distinguish confirmed defects from an inaccessible preview without relying only on notes. Target: `docs/07-Editorial-Automation.md`.

## Sources checked

- [Civil Code §1941.3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.3.)
- [Civil Code §1941.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.5.)
- [Civil Code §1941.6](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.6.)
- [Ann M. v. Pacific Plaza](https://law.justia.com/cases/california/supreme-court/4th/6/666.html)
- [Castaneda v. Olsher](https://law.justia.com/cases/california/supreme-court/2007/s138104.html)
- [Kwaitkowski v. Superior Trading](https://law.justia.com/cases/california/court-of-appeal/3d/123/324.html)
- [O’Hara v. Western Seven Trees](https://law.justia.com/cases/california/court-of-appeal/3d/75/798.html)
- [Oakland residential CPTED checklist](https://www.oaklandca.gov/files/assets/city/v/1/planning-amp-building/documents/sp/design-standards/cpted-residential.pdf)
- [AEBP company reference](https://alleastbayproperties.com/llms.txt)

Court opinions were read as primary judicial texts hosted by Justia. Statutory findings were checked against California Legislative Information. No citation implies a comprehensive subsequent-history check.

## Scope, limits and handoff

Reviewed full AEBP-Dev snapshot; post_modified as returned: 2026-09-30 19:15:19 (timezone not supplied). No revision ID or modified_gmt was returned; both remain null. Reviewed September 30, 2026 Pacific / October 1 UTC.

Repository was clean before these artifacts, HEAD b26e98e1871d47f82ef0dc41f3c3841c8af031cd; origin/main...HEAD was 0/0 against the locally stored remote ref (no fetch claimed). Git emitted a global-ignore permission warning, but status completed.

Pre-Publish Audit ran with rendered checks blocked: both draft permalinks returned the theme’s Page not found page in an unauthenticated browser. Full WordPress content/meta/terms/author/thumbnail read. Block comment nesting balanced and attribute JSON inspected; editor validation, responsive layout, canonical and emitted schema remain unverified. Schema metadata presence is not schema-output verification. Featured image alt exists; image visual suitability not verified.

Production repair-timelines, package-theft, repair-documentation and consultation links opened successfully. Parent-guide production URL was not verifiable; validate at launch. Oakland page was verified in browser after web fetch returned 403; its residential checklist PDF was read. This is not evidence of a broken Oakland link.

General education and conditional advice pass Compliance Risk; inaccurate legal generalizations are recorded under Legal Accuracy rather than duplicating them as personalized advice.

Cornerstone sequence is present, including five FAQs and a functionally equivalent self-audit checklist. Same-day dispatch policy supplies the documented practitioner observation. Companion check PASS means independently reviewed in 9850/01-review, not approved for publication. GBP-consistency PASS applies only to the saved draft in 2026-10-05-week1-package-notes.md, not a live GBP post. Its positive 'a reported broken lock puts you on notice' claim does not say that only tenant reports count. Recheck all package copy after revisions.

Schema file has no explicit release-version declaration. schema_version 1.0.0 follows existing review artifacts, with the exact schema fixed by repository commit; this provenance gap is logged below.

Nonblocking editorial suggestions: replace relative 'later this month' and October 12 promises in the blog with evergreen links when available; tighten repetitive 'usually not' phrasing through the legal replacements. No standards, company records or WordPress content changed.

Next: Claude supplies 02-revision-response.md/json with one disposition per finding and applies accepted revisions to both assets and package copy. Brian still reads the final drafts before publication.

