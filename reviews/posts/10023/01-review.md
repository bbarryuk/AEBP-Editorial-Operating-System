# Pre-Publish Audit — 10023

**How to Stop Package Theft in an Apartment Building: What Actually Works in Older East Bay Buildings**

Recommendation: **HOLD PENDING FIXES**. Intended publication: Monday, October 12, 2026. Reviewed October 9 Pacific.

WordPress: draft; modified 2026-10-09 18:01:16 (timezone unspecified); [draft](https://dev.alleastbayproperties.com/?p=10023).

Repository: `e035aa64a04a568d7a166172b7fcc87afee5c1e0`, clean before review files; local HEAD matched GitHub main. Standards: docs/01 v0.5; docs/02 v0.2; docs/03 v0.3; docs/07 v0.1; applicable manifests v0.1.

## Gated categories

### GATE-LEGAL-ACCURACY — FAIL

**10023-F01 — Type A + B**

- **Finding:** Cameras record theft; a controlled drop point prevents it.
- **Root cause:** STD-HONEST / EVD-CITATION-REQUIREMENT: the hook converts a reasonable risk-reduction recommendation into an assured outcome and contrasts it with categorical claims that cameras do not prevent theft. The table itself acknowledges deterrence and shared-code risk. Security.org supports layered precautions, not zero theft or the unsourced claim that footage rarely recovers packages. The conclusion/FAQ also overstate low cost without property quotes. No AEBP comparative performance example is documented.
- **Fix (replacement wording / exact completion requirement):**

> Replace the Quick Answer opening with: "To reduce package theft in an apartment building, start with where deliveries are left and who can reach them. Cameras can document incidents and may deter theft; controlled access can reduce opportunities to take packages. No option eliminates the risk."
> Replace the shared script opening with: "How can you reduce package theft in an apartment building? Start with where deliveries are left and who can reach them. Cameras can document incidents and may deter theft, but they work best alongside a controlled delivery area."
> Replace "Doesn't stop the theft, and footage rarely gets a package back" with "Does not physically secure packages; deterrence and recovery are not guaranteed."
> Replace the More cameras paragraph with: "Camera footage can help document an incident. Strongly recommended best practice: use cameras alongside controlled access and prompt pickup, rather than relying on footage alone."
> Replace "you can make your building a much harder target for very little money" with "you can start by checking existing doors and delivery arrangements before pricing improvements."
> Replace FAQ 1's final sentence with: "A written policy and repairs to existing hardware may be lower-cost starting points; a new package room needs a property-specific quote."
> Apply the same prevention wording to the excerpt, script on both pages, and GBP/social/SMS lead-ins before distribution.

- **Future prevention:** Review titles, excerpts, FAQs and distribution copy for absolute outcome claims; retain the anecdote log's explicit lack of a proven keypad-versus-camera case.

**10023-F02 — Type A**

- **Finding:** Confirm every common-area entry door closes, latches and locks on its own (Civil Code §1941.3)
- **Root cause:** GATE-LEGAL-ACCURACY / STD-TRUST-SIGNALS: the citation makes automatic closing/latching a universal statutory duty. Section 1941.3(a)(3) addresses code-compliant locking mechanisms on specified exterior common-area doors; it does not itself impose that blanket closer requirement. The section has scope limits/exceptions, including designated historic buildings, material for an older-building article. The Step One compliance-fix sentence repeats the conflation. Statutory text inspected at https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1941-3/; the official Legislature endpoint returned 403.
- **Fix (replacement wording / exact completion requirement):**

> Replace the checklist item with: "Check required common-area entry locks. Strongly recommended best practice: test any existing door closer and confirm the door latches reliably."
> Replace the Step One closing paragraph with: "Required by law: for covered multifamily buildings, Civil Code §1941.3(a)(3) addresses locking mechanisms on exterior doors serving common areas with access to dwelling units, subject to the section's scope and exceptions. Strongly recommended best practice: keep existing closers working so doors latch reliably. Before changing doors or converting a closet into package storage, have a qualified professional check applicable fire, egress and accessibility requirements. See our landlord security duties guide for the broader rules."
> Retain the statute and security-guide links.

- **Future prevention:** Separate the statutory hardware duty from operational closer recommendations, and review retrofit advice against scope and fire/egress requirements.

**10023-F03 — Type B**

- **Finding:** No California statute requires a package room or lockers
- **Root cause:** EVD-CITATION-REQUIREMENT: absence of package storage from §1941.3's list supports a statement about that section, not a conclusion about every California statute or every property's requirements. This is an unsupported breadth issue, not evidence that a general locker mandate exists. The same assertion occurs in Quick Answer, Key Facts, conclusion and FAQ 2. Source: https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1941-3/.
- **Fix (replacement wording / exact completion requirement):**

> Replace the Quick Answer sentence with: "Civil Code §1941.3 does not itself require a package room or lockers; separate property-specific requirements and commitments may still matter."
> Replace the Key Facts answer with: "Not under Civil Code §1941.3 itself. That section addresses specified locks, not package storage."
> Replace FAQ 2's first two sentences with: "Civil Code §1941.3 does not itself require either. That does not settle every building's obligations: check applicable local requirements, approvals and lease commitments."
> Replace the conclusion's opening with: "No setup eliminates every theft, and Civil Code §1941.3 does not itself require a package room."

- **Future prevention:** Narrow negative legal claims to the authority actually checked; do not infer all-law absence from one statutory list.

### GATE-LOCAL-ACCURACY — FAIL

**10023-F04 — Type A**

- **Finding:** thieves have used a carrier key to enter a Berkeley apartment building and open its mailboxes.
- **Root cause:** GATE-LOCAL-ACCURACY: the body correctly attributes the master-key theory to the building manager, but the Key Facts row turns it into a confirmed identification. NBC's October 2022 report describes apparent postal-key use and the manager's belief. Verified by direct retrieval after the browser search tool returned 403. https://www.nbcbayarea.com/news/local/east-bay/berkeley-mail-thieves/3027839/
- **Fix (replacement wording / exact completion requirement):**

> Replace the Postal keys fact cell with: "An Oakland carrier's postal keys were stolen in May 2024. In a separate Berkeley incident reported in October 2022, thieves entered with a key that the building manager believed was a carrier master key." Keep both NBC citations.

- **Future prevention:** Preserve attribution and uncertainty when compressing reporting into tables and answer boxes.

**10023-F05 — Type B**

- **Finding:** Low (Amazon's install partners describe it as no cost to the property; confirm current terms)
- **Root cause:** GATE-LOCAL-ACCURACY / EVD-CURRENCY-CHECK: ASK4's cited June 26, 2026 article explicitly discusses the UK market. Its no-cost offer does not establish East Bay eligibility or pricing. Attribution and 'confirm current terms' help, but the table still assigns a local cost tier from a different market. This is an evidence gap, not proof Amazon charges US properties. Direct source read: https://www.ask4.com/resources/blog/amazon-key-for-business-smarter-amazon-deliveries-for-your-building . Amazon's own technical explanation supports verified temporary access, not the current local price: https://aws.amazon.com/blogs/iot/building-a-virtual-fob-with-amazon-key-for-business-and-aws-iot/
- **Fix (replacement wording / exact completion requirement):**

> Replace the carrier-access cost cell with: "Confirm current U.S. property eligibility, installation costs and ongoing fees directly with the provider."
> Replace the source-list entry with: "Amazon Key delivery-access mechanism: Amazon's explanation of verified, time-limited building access. Confirm current local availability and terms directly with Amazon." Link to Amazon's own explanation. Keep the cost unquantified unless a current U.S. offer is verified.

- **Future prevention:** Check source country, product variant, date and eligibility before importing vendor prices into local comparisons.

### GATE-TECHNICAL-SEO — FAIL

**10023-F06 — Type A + B**

- **Finding:** Watch the video version, with chapter links and a full transcript.
- **Root cause:** GATE-TECHNICAL-SEO: the copy promises a finished asset, but both pages have an in-production placeholder and a Video Script, with no embed or chapter links. Draft-stage incompleteness is expected, but cannot receive publication clearance. Unauthenticated preview retrieval returned HTTP 404; the browser automation runtime also failed, so emitted schema, canonical, editor validation and responsive layout remain unverified, not proven missing. Metadata presence alone does not verify schema.
- **Fix (replacement wording / exact completion requirement):**

> For the current draft replace the lead-in with: "Video companion in production. The planned script appears below."
> For launch, replace it with: "Prefer video? Watch the companion video below or visit the video page." Restore "chapter links" only if actual chapters are supplied.
> Replace the production placeholder with the actual finished video's native wp:shortcode block after its real ID exists; do not invent an ID. Cross-check the recording/SRT before changing "Video Script" to "Video Transcript". Verify the rendered pages, canonical, emitted schema, image and mobile tables before clearing the technical gate.

- **Future prevention:** Use separate draft-content and launch checks; never treat unavailable previews or unrecorded scripts as verified rendered output.

### GATE-COMPLIANCE-RISK — PASS

General education, not an assessment of an identified reader's legal situation.

### GATE-ANECDOTE-INTEGRITY — PASS

Claims documented in the Oct 9 anecdote log and company sources; see provenance below.

### CORNERSTONE-STRUCTURE — PASS

Required source-level structure / documented practitioner content present. See strengths and limits.

### CORNERSTONE-AEBP-VOICE — PASS

Required source-level structure / documented practitioner content present. See strengths and limits.

### CORNERSTONE-COMPANION-VIDEO — PASS

10025 independently reviewed; this passes scope completion, not its publication readiness.

### CORNERSTONE-GBP-CONSISTENCY — PASS

GBP copy matches parent factual framing. The shared prevention overclaim must still be corrected under 10023-F01; no social-publishing clearance is implied.

## Scored categories

All values are editorial estimates, not a computed rubric. A passing score cannot override a failed gate.

| Category | Estimate / threshold | Result | What works | What holds it back |
|---|---:|---|---|---|
| SCORE-SEO | 92 / 90 | PASS | Clear owner-improvement intent, descriptive slug/meta and separation from liability guide. | Some promise wording needs qualification; rendered canonical remains unverified. |
| SCORE-GEO | 89 / 95 | FAIL | Answer-first box, facts table, five explicit FAQs and named sources. | Absolute prevention and legal claims could be extracted without the later caveats. |
| SCORE-EEAT | 92 / 95 | FAIL | Documented practitioner observations, candid no-locker disclosure, dated reporting. | Scope overreach in lock/storage law, uncertain key identity and UK pricing evidence. |
| SCORE-READABILITY | 92 / 90 | PASS | Practical route audit, comparison table and owner checklist. | Repeated cameras-versus-prevention slogan; six-column table needs mobile check. |
| SCORE-CONVERSION | 90 / 85 | PASS | Relevant package-complaint CTA and live consultation path. | Current text promises a video/transcript that is not yet available. |
| SCORE-OVERALL | 90 / 95 | FAIL | Well-targeted Monday cornerstone with useful original context. | Content findings and launch verification remain unresolved; overall is an editorial estimate, not an arithmetic rubric. |

## Strengths Worth Preserving

- Matches the October plan's owner-side prevention intent and avoids duplicating the liability guide.
- Required structure present: answer-first, facts, body, documented AEBP observation, before-holiday checklist, five aebp-faq questions, sources, closing cta-primary.
- All three new AEBP observations are documented in the Oct 9 anecdote log; no invented keypad-performance example.
- Comparison table acknowledges shared codes, oversize parcels, outages and carrier limitations; relative costs avoid recycled unsupported 2014 prices.
- Useful links to live liability/security guides and consultation path; native Gutenberg source structure and descriptive image alt present.

## Claim provenance

- **10023-C01 — documented:** “At AEBP, package theft is one of the most common complaints we hear from tenants.” Source: knowledge/company/anecdote-log.md, 2026-10-09 entry. Documented complaint-frequency wording, not a #1 ranking.
- **10023-C02 — documented:** “When we asked our local post office what owners can do, the best advice they had was a PO box.” Source: knowledge/company/anecdote-log.md, 2026-10-09 entry. Reported conversation, not national USPS policy. Blog section/FAQ and script variants covered.
- **10023-C03 — documented:** “We manage 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt. Live company source rechecked after cached overview's review date.
- **10023-C04 — documented:** “None of the buildings we currently manage use smart package lockers” Source: knowledge/company/anecdote-log.md, 2026-10-09 entry. Confirmed company fact; no locker-performance experience is implied.
- **10023-C05 — documented:** “We took two lessons from that conversation.” Source: knowledge/company/anecdote-log.md, 2026-10-09 entry. Professional interpretation following a documented conversation; does not establish a successful AEBP intervention.

## Article fixes

- 10023-F01: Replace the Quick Answer opening with: "To reduce package theft in an apartment building, start with where deliveries are left and who can reach them. Cameras can document incidents and may deter theft; controlled access can reduce opportunities to take packages. No option eliminates the risk."
  Replace the shared script opening with: "How can you reduce package theft in an apartment building? Start with where deliveries are left and who can reach them. Cameras can document incidents and may deter theft, but they work best alongside a controlled delivery area."
  Replace "Doesn't stop the theft, and footage rarely gets a package back" with "Does not physically secure packages; deterrence and recovery are not guaranteed."
  Replace the More cameras paragraph with: "Camera footage can help document an incident. Strongly recommended best practice: use cameras alongside controlled access and prompt pickup, rather than relying on footage alone."
  Replace "you can make your building a much harder target for very little money" with "you can start by checking existing doors and delivery arrangements before pricing improvements."
  Replace FAQ 1's final sentence with: "A written policy and repairs to existing hardware may be lower-cost starting points; a new package room needs a property-specific quote."
  Apply the same prevention wording to the excerpt, script on both pages, and GBP/social/SMS lead-ins before distribution.

- 10023-F02: Replace the checklist item with: "Check required common-area entry locks. Strongly recommended best practice: test any existing door closer and confirm the door latches reliably."
  Replace the Step One closing paragraph with: "Required by law: for covered multifamily buildings, Civil Code §1941.3(a)(3) addresses locking mechanisms on exterior doors serving common areas with access to dwelling units, subject to the section's scope and exceptions. Strongly recommended best practice: keep existing closers working so doors latch reliably. Before changing doors or converting a closet into package storage, have a qualified professional check applicable fire, egress and accessibility requirements. See our landlord security duties guide for the broader rules."
  Retain the statute and security-guide links.

- 10023-F03: Replace the Quick Answer sentence with: "Civil Code §1941.3 does not itself require a package room or lockers; separate property-specific requirements and commitments may still matter."
  Replace the Key Facts answer with: "Not under Civil Code §1941.3 itself. That section addresses specified locks, not package storage."
  Replace FAQ 2's first two sentences with: "Civil Code §1941.3 does not itself require either. That does not settle every building's obligations: check applicable local requirements, approvals and lease commitments."
  Replace the conclusion's opening with: "No setup eliminates every theft, and Civil Code §1941.3 does not itself require a package room."

- 10023-F04: Replace the Postal keys fact cell with: "An Oakland carrier's postal keys were stolen in May 2024. In a separate Berkeley incident reported in October 2022, thieves entered with a key that the building manager believed was a carrier master key." Keep both NBC citations.

- 10023-F05: Replace the carrier-access cost cell with: "Confirm current U.S. property eligibility, installation costs and ongoing fees directly with the provider."
  Replace the source-list entry with: "Amazon Key delivery-access mechanism: Amazon's explanation of verified, time-limited building access. Confirm current local availability and terms directly with Amazon." Link to Amazon's own explanation. Keep the cost unquantified unless a current U.S. offer is verified.

- 10023-F06: For the current draft replace the lead-in with: "Video companion in production. The planned script appears below."
  For launch, replace it with: "Prefer video? Watch the companion video below or visit the video page." Restore "chapter links" only if actual chapters are supplied.
  Replace the production placeholder with the actual finished video's native wp:shortcode block after its real ID exists; do not invent an ID. Cross-check the recording/SRT before changing "Video Script" to "Video Transcript". Verify the rendered pages, canonical, emitted schema, image and mobile tables before clearing the technical gate.

## Operating System improvements

- Add a narrowly sourced package-theft/security knowledge note separating lock duties, closer best practice, deposit acceptance duties and property-specific storage requirements. Do not infer statutory absence from one section. Suggested location: `knowledge/laws/package-theft-and-building-access.md`.
- Add a regression case preserving 'believed/apparent' when a reported incident is summarized in a Key Facts table. Suggested location: `tests/editorial/`.
- Define draft-stage versus launch-stage technical checks for unrecorded companion videos while retaining the final publication gate. Suggested location: `reviews/video-review.md`.
- Declare the JSON schema release version explicitly; 1.0.0 currently follows existing artifacts rather than an explicit schema-version constant. Suggested location: `automation/schemas/review.schema.json`.

## Evidence and review limits

WordPress post_modified as returned: 2026-10-09 18:01:16; timezone not supplied.

Reviewed October 9, 2026 Pacific (October 10 UTC), for Monday October 12. Pre-Publish Audit with rendered-page and recording checks blocked. Full AEBP-Dev snapshots read; no revision ID or GMT-modified timestamp returned. Local repository access initially failed in sandbox; read-only escalated checks succeeded. Local HEAD and GitHub main both e035aa64a04a568d7a166172b7fcc87afee5c1e0; pre-write working tree clean, HEAD...origin/main 0/0 against the locally stored ref, and GitHub main independently matched. No AGENTS.md found in repo or checked repo ancestors. Neither review directory existed.

Standards: docs/01 v0.5, docs/02 v0.2, docs/03 v0.3, docs/07 v0.1; Monday and video manifests v0.1. Weekly-review workflow and both schemas read. schema_version 1.0.0 follows existing review artifacts; exact schema fixed by repo commit.

Native block comment nesting and attribute JSON inspected: no detected imbalance/JSON parse errors. This is not a Gutenberg editor round-trip validation. Both scripts are identical, 217 words by whitespace count; package notes say approximately 205, a nonblocking planning discrepancy. Both correctly say Video Script. No video embed is present. Both unauthenticated draft permalinks returned HTTP 404, and browser UI runtime failed. Emitted schema, canonical, mobile layout and editor validation remain unverified rather than absent. Meta fields, terms, image ID/alt, author and video template read. Local 1200x675 hero crop visually inspected: suitable older-lobby illustration with open keypad door; WordPress uses media 10024, reported in package notes as 1536x1024, so the local crop is not proof of the site's rendered crop. Optional alt improvement: 'Older East Bay apartment lobby with wall mailboxes and an open package-room door fitted with a keypad.'

Live production consultation, liability-guide and landlord-security-guide links opened successfully. Future parent/companion production routes need launch verification. No full review of post 2804 performed. Both posts remain drafts with Oct 9 stored dates, not scheduled for Oct 12. Scheduling is a future publishing action, not an editorial error.

Security.org figures (one in four lifetime experience, $222, 3.5x recent-period comparison, n=3,307 October 2025) match the cited survey; do not present 'most recent three months' as an October 2026 observation. Prefer 'the three-month period covered by the October 2025 survey.' USPS FY2022/lock-replacement figures, OIG May 19, 2026 report and PO-box street-addressing explanation verified. NBC pages verified by direct retrieval after web-tool 403 failures; Berkeley key identity remains attributed. ASK4 direct retrieval shows UK context. Official Legislature endpoints returned 403; legal comparison uses accessible statutory mirrors, not a claim that current official-site verification succeeded. Sections 1846/1852 state the care distinctions cited; §1814 supports consensual deposit creation. As a nonblocking clarity improvement, say package acceptance 'can create a duty of care' and label a written acceptance policy as best practice, not a statute. Do not imply no separate fee alone settles the legal classification; retain attorney qualification.

GBP draft in Week 2 package notes repeats the blog's prevention claim, so substantive correction in 10023-F01 must propagate. Other social/SMS copy was spot-checked for that shared claim only, not cleared through separate channel audits. No WordPress content, standards, knowledge files, schedules or social posts changed. Claude should supply 02-revision-response.md/json for each reviewed post with one disposition per finding; production-dependent items can remain requires_human until completed. Brian still reads the final drafts before publication.

Sources inspected:
Editorial standards: https://github.com/bbarryuk/AEBP-Editorial-Operating-System/blob/e035aa64a04a568d7a166172b7fcc87afee5c1e0/docs/01-Editorial-Standards.md
Confirmed Oct 9 anecdotes: https://github.com/bbarryuk/AEBP-Editorial-Operating-System/blob/e035aa64a04a568d7a166172b7fcc87afee5c1e0/knowledge/company/anecdote-log.md
Civil Code 1941.3 (statutory mirror; official endpoint blocked): https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1941-3/
Civil Code 1846 (statutory mirror): https://law.justia.com/codes/california/code-civ/division-3/part-4/title-3/chapter-2/article-2/section-1846/
Civil Code 1852 (statutory mirror): https://california.public.law/codes/ca_civ_code_section_1852
Security.org survey: https://www.security.org/package-theft/annual-report/
NBC Berkeley incident: https://www.nbcbayarea.com/news/local/east-bay/berkeley-mail-thieves/3027839/
NBC Oakland incident: https://www.nbcbayarea.com/news/local/usps-150k-reward-postal-worker-robbed-oakland/3528206/
USPS crime-prevention release: https://about.usps.com/newsroom/national-releases/2023/0512-usps-postal-inspection-service-roll-out-expanded-measures-to-crack-down-on-mail-theft.htm
USPS OIG 25-137-R26: https://www.oversight.gov/reports/audit/follow-us-postal-services-and-us-postal-inspection-services-response-mail-theft
USPS street addressing: https://postalpro.usps.com/mailing/competitivepoboxes
ASK4 UK-oriented offer: https://www.ask4.com/resources/blog/amazon-key-for-business-smarter-amazon-deliveries-for-your-building
Amazon delivery access explanation: https://aws.amazon.com/blogs/iot/building-a-virtual-fob-with-amazon-key-for-business-and-aws-iot/
Current company facts: https://alleastbayproperties.com/llms.txt

Gate interpretation: CORNERSTONE-COMPANION-VIDEO passes because the companion was independently reviewed, not because it is publish-ready. GBP consistency passes only the drift check: it matches the parent; its shared overclaim is already included in 10023-F01. GATE-LEGAL-ACCURACY applies docs/02 evidence rules to material procedural claims as well as statutory claims. Compliance Risk passes the general-education test and is not used as a duplicate gate for inaccurate law. CORNERSTONE-STRUCTURE passes functional section order; a social-share bar preceding the answer does not defeat answer-first prose.

## Recommendation

Hold pending the findings above. Claude's next artifact is `02-revision-response.md` and `02-revision-response.json`, with one disposition per finding. Finish production checks before requesting publication clearance. Brian's final read remains required.

