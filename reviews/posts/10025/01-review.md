# Pre-Publish Audit — 10025

**How to Stop Package Theft in an Apartment Building (Video)**

Recommendation: **HOLD PENDING FIXES**. Intended publication: Monday, October 12, 2026. Reviewed October 9 Pacific.

WordPress: draft; modified 2026-10-09 18:01:22 (timezone unspecified); [draft](https://dev.alleastbayproperties.com/?post_type=video&p=10025).

Repository: `e035aa64a04a568d7a166172b7fcc87afee5c1e0`, clean before review files; local HEAD matched GitHub main. Standards: docs/01 v0.5; docs/02 v0.2; docs/03 v0.3; docs/07 v0.1; applicable manifests v0.1.

## Gated categories

### GATE-LEGAL-ACCURACY — FAIL

**10025-F01 — Type A + B**

- **Finding:** Cameras record package theft. Controlling where packages land is what prevents it.
- **Root cause:** STD-HONEST / EVD-CITATION-REQUIREMENT: the intro, coverage list, takeaway and script repeat an unsupported absolute prevention contrast. The parent table concedes camera deterrence and shared-code risk. This is procedural certainty, not individualized legal advice. See 10023-F01.
- **Fix (replacement wording / exact completion requirement):**

> Replace the intro with: "Controlling access to deliveries can reduce opportunities for package theft. Cameras can document incidents and may deter theft. This video explains practical options for older East Bay apartment buildings."
> Replace "Why cameras don't stop package theft" with "Why cameras work best alongside controlled access".
> Replace the first takeaway with: "Start with the delivery area and who can reach it; use cameras as one layer of protection."
> Use the exact revised opening proposed in 10023-F01 for both Video Script blocks. Remove any "rarely prevent it" or assured-prevention phrasing from the companion copy.

- **Future prevention:** Check every video surface after article revisions, including intro, bullet lists and script.

### GATE-LOCAL-ACCURACY — PASS

Local context and reported carrier-robbery claim supported. No city-specific ordinance or current local vendor price is asserted in this video copy.

### GATE-TECHNICAL-SEO — FAIL

**10025-F03 — Type B**

- **Finding:** 🎥 Video in production. It will appear here once it's live.
- **Root cause:** GATE-TECHNICAL-SEO: no finished recording, YouTube embed or verified literal transcript is present. This is a production dependency rather than a claim the draft was supposed to be finished. Draft preview returned HTTP 404; emitted schema, canonical, responsive rendering and editor validation remain unverified. Category 629, required template, image and SEO metadata are present.
- **Fix (replacement wording / exact completion requirement):**

> Keep the accurate in-production notice while drafting. At launch replace it with the finished video's actual lite_youtube shortcode in a native wp:shortcode block. Retain "Video Script" until checked against the recording/SRT; then use "Video Transcript" only if it is literal. Verify the real companion URL, parent link, emitted VideoObject where applicable, canonical and responsive page before clearing this finding. No final shortcode can be supplied truthfully until a real video ID exists.

- **Future prevention:** Track recording, embed and rendered-page verification as launch requirements separate from script review.

### GATE-COMPLIANCE-RISK — PASS

General education, not an assessment of an identified reader's legal situation.

### GATE-ANECDOTE-INTEGRITY — PASS

Claims documented in the Oct 9 anecdote log and company sources; see provenance below.

### VIDEO-TRANSCRIPT-LITERAL — PASS

Pass for draft labeling: Video Script is accurate before recording. The actual recording/transcript check remains pending under the technical finding.

### VIDEO-CONSISTENCY — FAIL

**10025-F02 — Type A + B**

- **Finding:** A keypad package room with a changeable code fits most older buildings.
- **Root cause:** VIDEO-CONSISTENCY / EVD-CITATION-REQUIREMENT: the takeaway turns the article's labeled professional judgment into an unqualified claim about most buildings. Also, the script says not to buzz in anyone who says they have a delivery while the page correctly qualifies this as unexpected deliveries. Both scripts match each other, but these page-to-script shifts need correction.
- **Fix (replacement wording / exact completion requirement):**

> Replace the keypad takeaway with: "Professional opinion: consider a keypad package room where the layout, carrier access and applicable requirements allow it."
> Replace the door takeaway with: "Strongly recommended best practice: check entry locks and make sure any existing door closer works reliably."
> In both scripts replace "remind them not to buzz in anyone who says they have a delivery" with "remind them not to buzz in unexpected or unverified visitors, even if they claim to have a delivery".

- **Future prevention:** Compare body, takeaways and spoken script for lost qualifications; textual identity of two scripts is only one consistency check.

## Scored categories

All values are editorial estimates, not a computed rubric. A passing score cannot override a failed gate.

| Category | Estimate / threshold | Result | What works | What holds it back |
|---|---:|---|---|---|
| SCORE-SEO | 90 / 90 | PASS | Companion title/slug, metadata and links to the full guide. | Actual video, output schema and final production route pending. |
| SCORE-GEO | 89 / 95 | FAIL | Scannable coverage and takeaway lists. | Prevention absolutes and lost qualifications make standalone extraction misleading. |
| SCORE-EEAT | 92 / 95 | FAIL | Documented post-office conversation and complaint frequency, linked resources. | Unsupported camera/prevention contrast and 'fits most' generalization. |
| SCORE-READABILITY | 94 / 90 | PASS | Concise 217-word script with a clear walkthrough and practical steps. | Align visitor wording and soften the opening without adding legal jargon. |
| SCORE-CONVERSION | 90 / 85 | PASS | Full-guide link and live consultation CTA. | Recording not available yet; replace production notice only when ready. |
| SCORE-OVERALL | 90 / 95 | FAIL | Useful companion draft, correct template and honest Script label. | Needs the shared claim corrections and a completed, verifiable recording/page. |

## Strengths Worth Preserving

- Script matches the parent's script exactly; no existing cross-post text drift.
- Correct pre-recording Video Script label preserves transcript integrity.
- Category 629 and video-post-no-hero-with-sidebar template are set.
- AEBP experience claims are documented and the copy remains general education.
- Distinct coverage/takeaway/resource lists support readers alongside a future video.

## Claim provenance

- **10025-C01 — documented:** “At AEBP, package theft is one of the most common complaints we hear from tenants.” Source: knowledge/company/anecdote-log.md, 2026-10-09 entry. Documented complaint-frequency wording, not a #1 ranking.
- **10025-C02 — documented:** “When we asked our local post office what owners can do, the best advice they had was a PO box.” Source: knowledge/company/anecdote-log.md, 2026-10-09 entry. Reported conversation, not national USPS policy. Blog section/FAQ and script variants covered.
- **10025-C03 — documented:** “AEBP manages 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay, with a 24/7 bilingual maintenance line.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt. Live company source rechecked after cached overview's review date.

## Article fixes

- 10025-F01: Replace the intro with: "Controlling access to deliveries can reduce opportunities for package theft. Cameras can document incidents and may deter theft. This video explains practical options for older East Bay apartment buildings."
  Replace "Why cameras don't stop package theft" with "Why cameras work best alongside controlled access".
  Replace the first takeaway with: "Start with the delivery area and who can reach it; use cameras as one layer of protection."
  Use the exact revised opening proposed in 10023-F01 for both Video Script blocks. Remove any "rarely prevent it" or assured-prevention phrasing from the companion copy.

- 10025-F02: Replace the keypad takeaway with: "Professional opinion: consider a keypad package room where the layout, carrier access and applicable requirements allow it."
  Replace the door takeaway with: "Strongly recommended best practice: check entry locks and make sure any existing door closer works reliably."
  In both scripts replace "remind them not to buzz in anyone who says they have a delivery" with "remind them not to buzz in unexpected or unverified visitors, even if they claim to have a delivery".

- 10025-F03: Keep the accurate in-production notice while drafting. At launch replace it with the finished video's actual lite_youtube shortcode in a native wp:shortcode block. Retain "Video Script" until checked against the recording/SRT; then use "Video Transcript" only if it is literal. Verify the real companion URL, parent link, emitted VideoObject where applicable, canonical and responsive page before clearing this finding. No final shortcode can be supplied truthfully until a real video ID exists.

## Operating System improvements

- Add a narrowly sourced package-theft/security knowledge note separating lock duties, closer best practice, deposit acceptance duties and property-specific storage requirements. Do not infer statutory absence from one section. Suggested location: `knowledge/laws/package-theft-and-building-access.md`.
- Add a regression case preserving 'believed/apparent' when a reported incident is summarized in a Key Facts table. Suggested location: `tests/editorial/`.
- Define draft-stage versus launch-stage technical checks for unrecorded companion videos while retaining the final publication gate. Suggested location: `reviews/video-review.md`.
- Declare the JSON schema release version explicitly; 1.0.0 currently follows existing artifacts rather than an explicit schema-version constant. Suggested location: `automation/schemas/review.schema.json`.

## Evidence and review limits

WordPress post_modified as returned: 2026-10-09 18:01:22; timezone not supplied.

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

## Recommendation

Hold pending the findings above. Claude's next artifact is `02-revision-response.md` and `02-revision-response.json`, with one disposition per finding. Finish production checks before requesting publication clearance. Brian's final read remains required.

