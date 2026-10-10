# Revision Response — Post 10025

Responds to: `reviews/posts/10025/01-review.json` (2026-10-09T18:12:23-07:00)  
Responder: Claude (Cowork) · 2026-10-10T01:25:00Z  
Repo: `f9ef98d37ed93d2ebbdddb7b2462a3349073ec59` (dirty: new response files)  
WordPress: draft, [https://dev.alleastbayproperties.com/?post_type=video&p=10025](https://dev.alleastbayproperties.com/?post_type=video&p=10025)

**Recommendation to Brian:** hold_for_brian_decision

## Dispositions

### 10025-F01 — accepted

**Rationale:** Same root cause as 10023-F01.

**Change applied:** Intro, first 'What This Video Covers' bullet and first takeaway replaced verbatim; script opening replaced with the 10023-F01 wording in both posts. Excerpt and Yoast metadesc rewritten ('Watch: practical ways to reduce package theft...'). Fixed a resulting 'Start... Start' repetition by changing script paragraph 2 to 'First, walk the route...' in both posts.

> Before: Cameras record package theft. Controlling where packages land is what prevents it.

> After: Controlling access to deliveries can reduce opportunities for package theft. Cameras can document incidents and may deter theft.

### 10025-F02 — accepted

**Rationale:** Agreed: the takeaway dropped the professional-opinion label, and the script's 'anyone who says they have a delivery' lost the page's 'unexpected' qualifier.

**Change applied:** Keypad and door takeaways replaced verbatim. Buzz-in line replaced in both scripts. Script keypad sentence now 'In our view... where the layout allows' in both posts and the package notes.

> Before: A keypad package room with a changeable code fits most older buildings.

> After: Professional opinion: consider a keypad package room where the layout, carrier access and applicable requirements allow it.

### 10025-F03 — requires_human

**Rationale:** Production dependency, not a content defect. Needs the HeyGen render, YouTube ID, SRT cross-check, and rendered-page/VideoObject/canonical/mobile verification from a logged-in preview or post-publish check.

## Operating system follow-ups

- Accepted, not built this pass: knowledge/laws/package-theft-and-building-access.md separating §1941.3 lock duties, closer best practice, depositary duties (§§1814/1846/1852) and property-specific storage requirements, without inferring statutory absence from one section. Should exist before the Oct 15 Thursday Tip reuses these rules. (`knowledge/laws/package-theft-and-building-access.md`)
- Agreed, deferred to Brian/ChatGPT: regression test preserving 'believed/apparent' attribution when reporting is compressed into Key Facts tables; draft-stage vs launch-stage technical checks for unrecorded companion videos in reviews/video-review.md; explicit schema version constant in review.schema.json. (`tests/editorial/; reviews/video-review.md; automation/schemas/review.schema.json`)
- New: post 2804 was refreshed this week but has no review folder. Recommend a GPT Pre-Publish Audit of 2804 before Oct 12, since it is already published on dev. (`reviews/posts/2804/`)

## Summary

All three findings answered. F01-F02 fixed on the video page and in both scripts; F03 waits on the recording and a rendered-page check. Nothing published.

Requires human review: yes (launch-stage video checks, plus Brian's final read).
