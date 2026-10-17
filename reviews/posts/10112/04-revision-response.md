# Revision Response 04 — Post 10112

Responds to: `reviews/posts/10112/03-final-review.json` (2026-10-17T00:35:08.023Z)  
Responder: Claude (Cowork) · 2026-10-17T00:50:00Z  
Repo: `386b0789839031ffc517f8d18d6b9fcdfbfc065b` (dirty: new response files)  
WordPress: scheduled (future) for 2026-10-19 00:00 site time, [https://dev.alleastbayproperties.com/?p=10112](https://dev.alleastbayproperties.com/?p=10112)

**Summary:** Content fixes applied and confirmed in 03 (F01-F03 closed); chapter-wording fix applied (F05). Video and verified transcript are now in place. Rendered preview, schema, mobile and public playback checks remain unresolved.

**requires_human_review:** true · **recommendation_to_brian:** hold_for_brian_decision

## Dispositions

### 10112-F04 — requires_human

**Rationale:** Partially resolved by Claude; release checks still open. Done 2026-10-16: real [lite_youtube videoid="eywhT2_YUsk"] embed in 10112 and 10113; SRT compared to the script (word-for-word, apostrophe style only) before relabeling both details blocks 'Video Transcript'; YouTube processed at 1:45, custom thumbnail set, scheduled private until 2026-10-19 07:00 UTC then public (confirmed via youtube_get_video: privacy private, publish_at 2026-10-19T07:00:00Z, embeddable true). Not done, and not marked PASS: authenticated desktop/mobile preview, block-editor validation, rendered Article/FAQ (10112) and VideoObject (10113) output, internal-link destinations on the rendered page, and public playback at launch. These need Brian's logged-in session or the post going live; the Rich Results Test can't read a scheduled post. Brian decides whether to run them before 00:00 Monday or to run them right after publish.

**Change applied:** Embed swap, transcript relabel, 'Prefer video?' line with length, video-page '(Video, 2 min)' title and Yoast title, chapter timestamps on 10113, _aebp_cb_* meta on 10112, featured image 10133 on 10113. No schema values or URLs fabricated.

> Before: 🎥 Video in production. It will appear here once it's live.

> After: [lite_youtube videoid="eywhT2_YUsk" title="Rental Property Lighting: The Low-Cost Security Check East Bay Landlords Overlook"]

### 10112-F05 — accepted

**Rationale:** Agreed. 10113 shows plain bold timestamps, not anchor links, so 'chapter links' overstated the page.

**Change applied:** 10112 'Prefer video?' line changed to 'chapter timestamps'. Post resaved; still scheduled for 2026-10-19.

> Before: visit the video page with chapter links and a full transcript.

> After: visit the video page with chapter timestamps and a full transcript.

## Operating System follow-ups

- Correction to 02-revision-response.json (kept unchanged as history): it carried an unsupported top-level 'recommendation' key and lacked summary / requires_human_review / recommendation_to_brian. This 04 response is schema-valid and supersedes it for machine-readable triage; 02's narrative described the pre-video state and is superseded by the video swap recorded here.
- Monday cornerstone skill template says 'video page with chapter links'; the video pages show plain timestamps. Either change the template wording to 'chapter timestamps' or add timestamp links on video pages, so 10112-F05 doesn't recur (weeks 1-2 video lines use the same wording). Target: `skills/monday-cornerstone (Claude skill) and docs/03-Review-Format.md`.

## Remaining before release (Brian)

1. Logged-in desktop and mobile preview of both posts: embed plays (private until launch), no block-validation warnings, tables readable on mobile.
2. After 00:00 Monday publish: Rich Results Test — Article/FAQ on 10112, Videos on 10113 only; public playback; internal links resolve; homepage (page 20) shows this video.
3. Record results against 10112-F04 / 10113-F02 (a short 05 note is enough).
