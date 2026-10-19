# Revision Response 04 — Post 10196

Responds to: `reviews/posts/10196/03-final-review.json` (2026-10-18T21:31:33-07:00)  
Responder: Claude (Cowork) · 2026-10-19T04:52:00Z  
Repo: `a9029ffeecf041942779ed04fe6983b31daecd9e` (dirty: new response files)  
WordPress: draft, https://dev.alleastbayproperties.com/?post_type=video&p=10196

**Summary:** Excerpt fixed (F04). Only the production hold (F03) remains, deferred to the video swap.

**requires_human_review:** true · **recommendation_to_brian:** hold_for_brian_decision

## Dispositions

### 10196-F04 — accepted

**Rationale:** Agreed: the excerpt is a separate field and was missed when F01/F02 were synced. Reviewer's replacement used verbatim. Checked 10195's excerpt too: it only names the statutes, with no unqualified claims, so it's unchanged.

**Change applied:** post_excerpt replaced on 10196 via wp_update_post (full resave).

> Before: Watch: why "secure building" and "safe neighborhood" are promises a landlord can't keep, what to put in writing for every tenant, why a lease can't discourage calls to the police, and how to treat a security report as notice.

> After: Watch: how East Bay landlords can describe security features without overpromising, explain protected calls for help, and respond to reports about locks, lighting and doors.

### 10196-F03 — requires_human

**Rationale:** Open until the video exists, same as 10112-F04. At the swap: real [lite_youtube] embed in both posts, SRT-derived chapter timestamps on 10196, 'Video Transcript' relabel only after checking the SRT against the audio, length added to the 10196 title/Yoast title and to the restored 'Prefer video?' line in 10195, thumbnail on 10196, _aebp_cb_* meta on 10195. Then Brian's logged-in preview (desktop/mobile, block validation) and, after publish, Rich Results (Article/FAQ on 10195, Videos on 10196 only), link checks and homepage (page 20). Both posts stay draft until then. No video ID, duration or timestamps invented.

> Before: 🎥 Video in production. It will appear here once it's live.

## Operating System follow-ups

- Revision checklist gap: when legal wording changes in a post body, also sync post_excerpt, Yoast metadesc and social/GBP copy. 10196-F04 was an excerpt that missed the sync. Consider adding 'excerpt + metadesc' to VIDEO-CONSISTENCY in reviews/video-review.md. Target: `reviews/video-review.md`.
