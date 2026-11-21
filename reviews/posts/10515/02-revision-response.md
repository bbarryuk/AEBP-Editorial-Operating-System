# Revision Response 02 — Post 10515

Responds to: `reviews/posts/10515/review.json` (2026-11-20T20:00:00-08:00)  
Responder: Claude (Cowork) · 2026-11-21T04:15:00Z  
Repo: `cd58ae46a7b6d12d6de5045c461f9f6d6f79a443` (dirty: new response files and anecdote-log wording update)  
WordPress: draft, https://dev.alleastbayproperties.com/?p=10515

**Summary:** All active findings accepted (F01 as written; F02, F03, F06 and F07 with shorter wording than proposed). F04 and F05 were withdrawn by the reviewer after locating the 2026-11-20 anecdote-log entry; the AEBP count, window/slider observation and same-day policy are unchanged. The shared Video Script was also edited on paired page 10516 (F02 wording and a date-neutral holiday line, since the video usually publishes later in the week than the post). Statute text still needs a live leginfo check because the reviewer's fetch returned 403.

**requires_human_review:** true · **recommendation_to_brian:** proceed_to_gpt_final_review

**Withdrawn by reviewer:** F04, F05 (anecdote integrity; see `knowledge/company/anecdote-log.md`, 2026-11-20 entry). No change made; the documented claims are preserved as written.

## Dispositions

### 10515-F01 — accepted

**Rationale:** Correct. 'Last week' goes stale the moment the post is read after Nov 27. The anecdote log's reuse limits already say to cite the dates.

**Change applied:** What We See at AEBP, first paragraph. Anecdote-log 'Published as' line updated to match.

> Before: Last week (November 16–20), our portfolio of 600+ East Bay units logged

> After: During November 16–20, 2026, our portfolio of 600+ East Bay units logged

### 10515-F02 — accepted_with_modification

**Rationale:** Correct on scope: Civ. 1942(a) runs from notice of 'dilapidations rendering the premises untenantable,' not any report. A rain leak is usually that kind of condition under 1941.1(a)(1), so the post now ties notice to habitability instead of using the reviewer's longer replacement, which would have read awkwardly in a Quick Answer. The 'document and investigate every leak report' advice was kept, in the law-section bullet.

**Change applied:** Quick Answer last sentence; Key Facts 'When does the repair clock start?' row; law-section 'Notice' bullet (now adds 'Document and investigate every leak report either way'); FAQ 4 (now 'It can' and scoped to untenantable conditions); Video Script paragraph 5 on both drafts.

> Before: and the repair clock starts when you get notice, holiday weekend or not.

> After: and once you have notice of a leak that affects habitability, the law expects a repair within a reasonable time for the circumstances, holiday weekend or not.

### 10515-F03 — accepted_with_modification

**Rationale:** Correct: the tier label is AEBP's operational classification, and 1954(a)(1)/(e)(1) emergency entry depends on an actual emergency. Shortened the reviewer's wording to fit a table cell. The Quick Answer, FAQ 3 and script already said 'in an emergency' / 'to respond to an emergency' and were left as is.

**Change applied:** Triage table, Emergency row, Entry rule column.

> Before: Emergency entry without notice (§1954)

> After: Entry without advance notice only if it's an actual emergency (§1954); otherwise written notice or the tenant's consent

### 10515-F06 — accepted_with_modification

**Rationale:** Correct that 'always move up a tier' overstates it. Kept the reviewer's substance (electrical as a potential immediate safety hazard, prompt inspection for suspected mold, escalate on actual risk) in shorter sentences.

**Change applied:** Paragraph after the triage table.

> Before: Two kinds of calls should always move up a tier: anything involving electrical, and anything where the tenant mentions a musty smell or spots on the wall.

> After: Two kinds of calls deserve extra care. Treat water near outlets, light fixtures or wiring as a potential immediate safety hazard. And when a tenant mentions a musty smell or spots on the wall, inspect promptly for mold. Escalate based on the actual risk.

### 10515-F07 — accepted_with_modification

**Rationale:** Correct: the video page has no embed, chapters or transcript yet. Kept the 'Prefer video?' label because the site pattern restores the link at the video swap step; the swap will put back 'Watch the N-minute video version, with chapter links and a full transcript.'

**Change applied:** 'Prefer video?' paragraph above the video placeholder.

> Before: Prefer video? Watch the video version, with chapter links and a full transcript.

> After: Prefer video? A companion video is in production. The written guide is below.

## Also changed (shared Video Script, both drafts)

> Before: The repair clock starts when your tenant tells you, and a phone call or a text counts.

> After: Once your tenant tells you about a leak like that, and a phone call or a text counts, the law expects a repair within a reasonable time.

> Before: It's Thanksgiving week, so before the long weekend, make sure your tenants have your after-hours number, and you know which vendor will pick up on Thursday.

> After: Holiday weekends are the hard part, so make sure your tenants have your after-hours number, and you know which vendor will pick up when the office is closed.

## Operating System follow-ups

- Civil Code §1941.7 and Health & Safety Code §17920.3 are cited in 10515 but have no snapshot in knowledge/sources/state/statutes (verified this round from SB 655 bill text and secondary sources). Add snapshots when leginfo is reachable.
- Reviewer's leginfo fetch returned 403. Brian to spot-check §§1941.1, 1942, 1954, 1941.7 and HSC 17920.3 on leginfo before publish, as on the Measure X post.
- Thanksgiving alignment (article-fixes item 5): the post publishes Monday Nov 23, so the 'Before the Long Weekend' section is aligned and unchanged. The Video Script's holiday line was made date-neutral because the video typically publishes later in the week. If the post's publish date slips past Nov 26, retitle that section.
