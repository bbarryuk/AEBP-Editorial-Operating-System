# Editorial Review — Post 10195

**How East Bay Landlords Can Talk With Tenants About Safety Without Promising More Than the Law Requires**

Recommendation: **HOLD PENDING FIXES**. Review mode: Pre-Publish Audit (draft content and metadata reviewed; rendered-page/schema clearance blocked).

Snapshot: draft; WordPress modified 2026-10-18 20:26:12 (timezone not supplied). Review date: October 18, 2026, America/Los_Angeles.

Standards: docs/01 v0.5; docs/02 v0.2; docs/03 v0.3; docs/07 v0.1; cornerstone manifest v0.1. Repository: `14e36e5f25f9b2290dee6b481bf983a1c7975e48`, dirty before review artifacts; existing anecdote-log change used and preserved.

## Gated categories

- **GATE-LEGAL-ACCURACY: FAIL** — 10195-F01, 10195-F02, 10195-F03, 10195-F04
- **GATE-LOCAL-ACCURACY: FAIL** — 10195-F07
- **GATE-TECHNICAL-SEO: FAIL** — 10195-F06
- **GATE-COMPLIANCE-RISK: PASS**
- **GATE-ANECDOTE-INTEGRITY: PASS**
- **CORNERSTONE-STRUCTURE: FAIL** — 10195-F05
- **CORNERSTONE-AEBP-VOICE: PASS**
- **CORNERSTONE-COMPANION-VIDEO: PASS**
- **CORNERSTONE-GBP-CONSISTENCY: PASS**

Compliance PASS concerns general-education framing only; it does not clear the legal errors. Production/preview failures are identified as such, not treated as proof that schema is absent.

## Findings and exact fixes

### 10195-F01 — Type A

**Finding:** A report is notice under Civil Code §1941.3, and what you do after notice is what courts look at.

**Root cause:** The Quick Answer extends a lock/window-security statute to every kind of security report. The body correctly narrows its Key Facts row, but the summary and shared script lose that boundary. Section 1941.3(b) concerns notice of a deficiency covered by subsection (a), not every light, stranger or theft report.

**Fix:** Quick Answer replacement: “A report of a deficiency covered by Civil Code §1941.3 can put the landlord on notice; the statute allows a reasonable time to correct it. Other security reports may raise duties under other law, so assess and document each one.” Replace the fourth paragraph of both Video Script blocks with: “Fourth, as a best practice, acknowledge security reports promptly, assess the urgency, arrange needed repairs and keep a record. A report about a required lock can give notice under California's lock statute; other reports may raise different duties.”

**Future prevention:** Preserve statutory subject matter and distinguish company response policy from statutory deadlines in summaries and scripts.

### 10195-F02 — Type A

**Finding:** Tenants can always call the police

**Root cause:** The heading, Key Facts, FAQ 4 and shared script omit the statute's abuse/crime/emergency and necessary-assistance conditions. This turns a scoped statutory protection into an unconditional statement. Source: Civil Code §1946.8(b)–(d).

**Fix:** Heading: “Protected calls for police or emergency help.” Key Facts and FAQ 4 replacement: “Civil Code §1946.8 protects calls made by or on behalf of someone facing abuse, crime or an emergency when the caller believes help is necessary. A lease cannot restrict those calls, and a landlord cannot penalize a tenant or resident for them. Documentation is not required to establish that belief.” Shared script replacement: “Third, don't discourage calls for help. California Civil Code section 1946.8 protects calls about abuse, crime or an emergency when the caller believes help is needed. A lease can't restrict those calls, and a landlord can't penalize a tenant or resident for them.”

**Future prevention:** Check every compressed legal restatement against the same statutory conditions, including companion takeaways.

### 10195-F03 — Type A/B

**Finding:** A single incident is rarely foreseeable.

**Root cause:** This unsupported frequency claim generalizes the heightened foreseeability analysis for hiring guards into all precautions. The package-theft row also says “Whatever you've promised in writing,” which omits duties independent of a contract. Ann M. balances foreseeability against the burden of the particular precaution; it does not establish a universal wait-for-repetition rule.

**Fix:** Replace the sentence with: “Do not wait for a second incident before assessing a known hazard. The duty depends on the foreseeable risk and the burden of the proposed precaution; hiring guards involves a higher foreseeability threshold than simpler measures.” Replace the package-theft ‘Usually your job’ cell with: “Honor written commitments and assess reasonable measures for known risks in common areas you control.”

**Future prevention:** Keep guard-specific holdings separate from basic maintenance and warning duties; do not frame contracts as the sole source of duty.

### 10195-F04 — Type A/B

**Finding:** What to leave out: crime statistics you've pulled together yourself, a description of the neighborhood, and any claim about how often something happens at the building.

**Root cause:** Advice meant to prevent unsupported marketing claims can read as advice to withhold known incident history, undercutting the article's O’Hara discussion. The later absolute “No statute requires a general crime bulletin” is not established by a cited authority or bounded jurisdictional review.

**Fix:** Replace the quoted sentence with: “Leave out unsupported safety ratings, speculative crime statistics and promises about outcomes. This does not mean withholding known material safety information: seek legal guidance about warnings or disclosures when specific incidents or hazards are known.” Replace “No statute requires a general crime bulletin.” with: “Whether an incident calls for a warning depends on the facts and applicable duties; ask an attorney about a specific incident or known hazard.”

**Future prevention:** Review advice about omissions against the article's disclosure duties; avoid universal negative legal claims without support.

### 10195-F05 — Type A

**Finding:** Bottom Line

**Root cause:** The required CORNERSTONE-STRUCTURE ‘Before You [Act]’ checklist is absent between the AEBP observation and FAQ. A prose conclusion and earlier tables do not meet the current explicit checklist requirement.

**Fix:** Insert after Bottom Line, before FAQ:
## Before You Talk With Tenants About Safety
- Check that each listed security feature exists and works.
- Replace unsupported safety promises with factual descriptions.
- Give tenants current maintenance and police contact information.
- Log reports, assess urgency and document follow-up.
- Ask counsel about known hazards, incident warnings and protected lock-change requests.

**Future prevention:** Run the cornerstone structural manifest before creating WordPress drafts.

### 10195-F06 — Type A/B

**Finding:** Prefer video? Watch the video version, with chapter timestamps and a full transcript.

**Root cause:** The same draft says the video is in production; no playable video or chapter timestamps are present. Browser preview returned a site 404, so editor validity, actual layout and generated schema could not be verified. Metadata and balanced block comments do not prove those checks pass.

**Fix:** Until production is complete, replace the invitation with: “The companion video is in production.” For publication, replace the production placeholder with the actual playable embed, add real chapter times and a recording-checked transcript, and verify the authenticated preview, generated schema and destination links. No embed ID or transcript text can be supplied before the recording exists.

**Future prevention:** Separate draft-content review from production-readiness sign-off; never infer missing generated schema from raw post content.

### 10195-F07 — Type B

**Finding:** Emeryville: press 5 for dispatch or a police report

**Root cause:** The 510-596-3700 number is corroborated by the city's police page. The specific menu option could not be independently verified: the cited DA PDF and Community Outreach page were unavailable. This is a limited verification gap, not evidence the option is wrong.

**Fix:** Remove only the unverified parenthetical. Use: “Oakland 510-777-3333, Berkeley 510-981-5900, Emeryville 510-596-3700.” Alternatively retain the parenthetical after verifying the current official routing instruction.

**Future prevention:** Store current phone-routing evidence separately from verified base numbers.

## Scored categories

All scores are editorial estimates.

| Category | Estimate / minimum | Status | What's working | What's holding it back |
|---|---:|---|---|---|
| SCORE-SEO | 92 / 90 | PASS | Focused query, populated Yoast fields and relevant internal links. | Final rendering/schema and video production unverified. |
| SCORE-GEO | 90 / 95 | FAIL | Answer-first structure and extractable facts/takeaways. | Compressed legal statements omit conditions; blog checklist absent or video not produced. |
| SCORE-EEAT | 92 / 95 | FAIL | Documented practitioner process and identifiable primary legal texts. | Overbroad legal phrasing limits reliability despite strong provenance. |
| SCORE-READABILITY | 93 / 90 | PASS | Plain language with scannable sections and short script. | Some legal shortcuts need precise wording without adding unnecessary complexity. |
| SCORE-CONVERSION | 90 / 85 | PASS | Relevant property-management CTA with live consultation destination. | Video promise cannot yet be fulfilled; final cross-links need checking. |
| SCORE-OVERALL | 91 / 95 | FAIL | Clear educational purpose and documented AEBP examples. | Blocking legal and production findings remain. |

## Strengths Worth Preserving

- The features-versus-outcomes framing gives readers usable replacement language.
- AEBP welcome-sheet, lock-triage and lease practices are documented; no invented incident is needed.
- O’Hara is presented as claims allowed to proceed, not a final damages verdict.
- The script is correctly labeled as a script while recording is pending.

## Claim provenance

- **10195-C01 — documented:** “every new AEBP tenant gets a short welcome sheet on top of the lease documents.” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; local working copy). Documented internal record; not AI owner verification.

- **10195-C02 — documented:** “routine repairs go through the tenant portal as a work order, and urgent problems go to our 24/7 maintenance line at (510) 450-3815” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; local working copy). Documented internal record; not AI owner verification.

- **10195-C03 — documented:** “a broken entry or lobby lock counts as urgent, and we send a vendor the same day.” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; local working copy). Documented internal record; not AI owner verification.

- **10195-C04 — documented:** “The lease itself is the California Association of REALTORS® residential lease form.” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; local working copy). Documented internal record; not AI owner verification.

- **10195-C05 — documented:** “The package includes C.A.R.'s Fair Housing and Discrimination Advisory too” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; local working copy); 10-October/week4/2026-10-26-week4-package-notes.md. Documented internal record; not AI owner verification.

- **10195-C06 — documented:** “Our October issue went to every resident.” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; local working copy). Documented internal record; not AI owner verification.

- **10195-C07 — documented:** “It asked them to report lights that are out and doors that won't latch, because "we can only fix what we know about."” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; local working copy); 10-October/October-Tenant-Newsletter.md. Documented internal record; not AI owner verification.

- **10195-C08 — documented:** “It listed the Oakland, Berkeley and Emeryville non-emergency police numbers and asked residents to "let us know too so we can follow up on the property side."” Source: 10-October/October-Tenant-Newsletter.md. Documented internal record; not AI owner verification.

- **10195-C09 — documented:** “We manage 600+ East Bay rental units with a 24/7 bilingual maintenance line.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt. Documented internal record; not AI owner verification.

- **10195-C10 — documented:** “At AEBP, every new tenant gets a welcome sheet with our 24/7 maintenance line, and a broken entry lock is an emergency, with a vendor sent the same day. Our lease asks tenants to research the neighborhood themselves. We describe the building, and how to reach us.” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; local working copy). Shared script condenses documented practices. Final sentence is present-tense professional framing, not proof of an unrecorded listing-language policy.

- **10195-C11 — documented:** “Together they set the division we try to follow in conversation as well: tenants research the neighborhood, and we describe the building and how to reach us.” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; local working copy). Professional framing of documented materials; do not strengthen into a claimed universal AEBP no-safe/no-secure policy.

## Article fixes

- 10195-F01: The Quick Answer extends a lock/window-security statute to every kind of security report
- 10195-F02: The heading, Key Facts, FAQ 4 and shared script omit the statute's abuse/crime/emergency and necessary-assistance conditions
- 10195-F03: This unsupported frequency claim generalizes the heightened foreseeability analysis for hiring guards into all precautions
- 10195-F04: Advice meant to prevent unsupported marketing claims can read as advice to withhold known incident history, undercutting the article's O’Hara discussion
- 10195-F05: The required CORNERSTONE-STRUCTURE ‘Before You [Act]’ checklist is absent between the AEBP observation and FAQ
- 10195-F06: The same draft says the video is in production; no playable video or chapter timestamps are present
- 10195-F07: The 510-596-3700 number is corroborated by the city's police page

## Operating System improvements

- Add a maintained security-duty reference separating lock-statute notice, guard foreseeability, general reasonable-care duties, protected police calls and incident warnings. Sources are available, so this system gap does not independently block these posts. Target: `knowledge/laws/landlord-security-duties.md`. Type C follow-up: yes.

- Add an explicit blocked/not-verified representation for rendered-page checks; the current PASS/FAIL schema forces incomplete checks into FAIL with explanatory evidence-gap text. Target: `automation/schemas/review.schema.json`. Type C follow-up: yes.

- Refresh the overdue company overview separately. Relevant 600+ units and maintenance facts were cross-checked this session; do not change the existing anecdote-log work during this review. Target: `knowledge/company/overview.md`. Type C follow-up: no.

## Evidence and review limits

Reviewed 2026-10-18 America/Los_Angeles. Full AEBP-Dev snapshots read, including content, metadata, terms, thumbnail and author. Post-modified values below are exactly as returned, with no timezone supplied; no revision ID or modified_gmt was returned. Repo HEAD 14e36e5f25f9b2290dee6b481bf983a1c7975e48; initially dirty because knowledge/company/anecdote-log.md has an existing uncommitted change (the current welcome-sheet entry was used); zero commits ahead of locally recorded origin/main, no remote fetch. Schema version 1.0.0 follows existing review artifacts; schema itself has no version constant. No WordPress edits. Native block comments balanced on both posts; this is not Gutenberg editor validation. Authenticated preview was unavailable: both attempted browser previews returned site 404 pages; layout, mobile appearance, rendered FAQ/VideoObject schema and canonical/indexing are not cleared. Featured media 10194 and descriptive alt present, image appearance not inspected. Main security guide and conversion destination loaded; package-theft destination fetch failed, not proof of a broken link; future parent/companion production links need final verification. Statutory text was read from Justia/Public.Law mirrors after official LegInfo endpoints returned 403; mirrors are not an independently certified current-law check. Case opinions read in full opinion reproductions; no exhaustive subsequent-case-treatment audit. O’Hara pleading-stage qualification is appropriately preserved. 1941.5/1941.6 24-hour duty is supportable for qualifying documented requests; this post does not enumerate all eligibility conditions. Megan's Law summary preserves other-law duties in FAQ 3. Local numbers verified from municipal pages/indexed municipal text; press-5 routing not independently verified. Fair Housing Institute list corroborates ‘safe neighborhood’ avoidance as industry guidance, not a statutory word ban. Live llms.txt corroborates 600+ units and maintenance service. Local October newsletter and week4 package notes inspected; no private lease details copied. Scores are editorial estimates, not a measured rubric. WordPress post_modified: 2026-10-18 20:26:12. Companion PASS means 10196 was independently reviewed, not approved. GBP copy located in week4 package notes matches the blog's central message; PASS is consistency only, not independent clearance of every social caption. Optional GBP precision: include ‘while knowing about earlier assaults’ in its case summary. LinkedIn and all other distribution copy are outside this two-post approval scope.

Sources inspected (October 18, 2026):

- [Civil Code 1941.3](https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1941-3/)
- [Civil Code 1946.8](https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1946-8/)
- [Civil Code 1941.5](https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1941-5/)
- [Civil Code 1941.6](https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1941-6/)
- [Civil Code 2079.10a](https://california.public.law/codes/ca_civ_code_section_2079.10a)
- [O’Hara (full opinion)](https://law.justia.com/cases/california/court-of-appeal/3d/75/798.html)
- [Ann M. (full opinion)](https://law.justia.com/cases/california/supreme-court/4th/6/666.html)
- [Kwaitkowski (full opinion)](https://law.justia.com/cases/california/court-of-appeal/3d/123/324.html)
- [Oakland police](https://www.oaklandca.gov/Public-Safety-Streets/Police)
- [Berkeley police reporting](https://berkeleyca.gov/safety-health/police/report-crime)
- [Emeryville police](https://www.emeryville.org/Government/Departments/Police)
- [Fair Housing Institute word list](https://www.fairhousinginstitute.com/wp-content/uploads/2020/06/Fair-Housing-Advertising-Words-Phrases-List-1.pdf)
- [Current company reference](https://alleastbayproperties.com/llms.txt)

## Handoff

Claude should provide `02-revision-response.md` and `02-revision-response.json` with a disposition for every finding, then request review of the updated drafts. Production and preview checks remain open until actually verified. Brian's final read is still required; no publication was performed.

