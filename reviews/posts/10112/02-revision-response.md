# Revision Response — Post 10112

Responds to: `reviews/posts/10112/01-review.json` (2026-10-16T22:31:40.271Z)  
Responder: Claude (Cowork) · 2026-10-16T22:45:00Z  
Repo: `c4a82301f826d60cf164ac46449dd2e996e8d69a` (dirty: new response files)  
WordPress: draft, [https://dev.alleastbayproperties.com/?p=10112](https://dev.alleastbayproperties.com/?p=10112)

**Recommendation:** rereview_content_findings; hold release for video

## Dispositions

### 10112-F01 — accepted

**Rationale:** Agreed. The Oakland obstruction-permit CPTED assessment shows the blanket 'no law' wording overstates the point, even though it creates no routine duty for an existing rental.

**Change applied:** Bottom Line and FAQ 5 replaced with GPT's wording (voluntary maintenance self-audit; ask the city about project-specific CPTED review for alterations or permit work). Also narrowed the Key Facts label from 'Local guideline, not a code requirement for existing buildings' to 'Local guideline; used here as a voluntary self-audit', which made the same blanket claim. No other 'no law' wording in the post, video page or package copy.

> Before: No law requires a CPTED review, but a lighting or door problem you've been told about and haven't fixed is the kind of thing that can matter later.

> After: Use Oakland's checklist as a voluntary maintenance self-audit. If you plan alterations or permit work, ask the city whether project-specific CPTED review or other conditions apply. Either way, a lighting or door problem you've been told about and haven't fixed is the kind of thing that can matter later.

### 10112-F02 — accepted

**Rationale:** Agreed; the shortened checklist line dropped 'clearance' and could be read as a tree height.

**Change applied:** Owner checklist item replaced verbatim. Same fix applied to the video-page takeaway ('about 6 feet of clear space beneath tree canopies') and the Instagram caption in the package notes. Quick Answer, Key Facts, walk-through table and Oakland list already said 'clearance' and are unchanged.

> Before: Trim shrubs near paths and windows to about 2 feet, and tree canopies to about 6 feet

> After: Keep shrubs near paths and windows about 2 feet high, and maintain about 6 feet of clear space beneath tree canopies, following Oakland's CPTED guideline

### 10112-F03 — accepted

**Rationale:** Agreed; the spoken script needs the same confidence label as the body.

**Change applied:** Script sentence replaced in both copies (10112 and 10113) and in the HeyGen script in the package notes; video-page takeaway replaced per 10113-F01. Script is still unrecorded.

> Before: Entries, walkways, mail areas and parking should be lit from dusk to dawn.

> After: As a best practice, we recommend steady dusk-to-dawn lighting at entries, walkways, mail areas and parking.

### 10112-F04 — requires_human

**Rationale:** Accepted as a release prerequisite; not resolvable in a content pass. No video exists yet, and the draft preview needs an authenticated session. Nothing fabricated: placeholder and 'Video Script' label kept. At the video swap: embed the real [lite_youtube] shortcode, compare SRT to script before relabeling to 'Video Transcript', set the length in the 'Prefer video?' line and video-page title, then check the authenticated preview, block validity, rendered schema and links.

**Change applied:** None yet. Optional precision note also applied: Nov 30 sunset changed from '4:51' / 'before 4:51' to 'about 4:50 p.m.' in Key Facts and the controls section (cited source gives 4:50:30).

## Operating System follow-ups

- Accepted, not built this pass: knowledge/laws/security-lighting-cpted.md covering Oakland's checklist dimensions (2 ft landscaping / 6 ft canopy clearance), permit-specific CPTED assessment (e.g., Oakland obstruction permits for vehicle barriers), §1941.1(a)(5) wording, and the limits of the NBER/Welsh-Farrington lighting research. Should exist before the Oct 22 Thursday Tip reuses these facts. Target: `knowledge/laws/security-lighting-cpted.md`. Type C follow-up.
- Accepted as a proposal for Brian: docs/03 should say how a technical gate records 'preview unavailable / media not yet produced' separately from a proven markup or schema defect, and distinguish content clearance from production release. Target: `docs/03-Review-Format.md`. Type C follow-up.

## Next review

Request a follow-up (03) against the revised draft for the content findings. The video/preview finding stays open until the HeyGen render and YouTube upload; it should not be marked PASS before then. Brian's final read is still required.
