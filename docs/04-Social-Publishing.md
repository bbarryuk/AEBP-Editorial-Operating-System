---
title: Social Publishing — Connector Status and Governance
doc_type: normative
version: 0.1
owner: Brian
last_updated: 2026-07-14
purpose: Single source of truth for which social platforms can be posted to directly via MCP, which are still copy-only, and the approval rule that applies to all of them. Referenced by any skill that produces social content (aebp-monday-cornerstone, aebp-thursday-tip) rather than duplicated in each.
used_by: [Claude, ChatGPT]
---

# Social Publishing

## Platform status (check this table before assuming a platform can be posted live — it changes as Brian connects new tools)

| Platform | Status | Tool(s) | Notes |
|---|---|---|---|
| Facebook | Live posting | Meta MCP — `meta_create_post`, `meta_create_video_post`, `meta_create_photo_post` | Confirmed connected and authenticated 2026-07-13 (`meta_health_check`). **No tool exists to create a fresh top-level comment on a Page post** — only `meta_reply_post_comment` (replies to an existing comment_id). Discovered 2026-07-16 when two "link in first comment" posts went live with no comment ever added. Fix used: put the link inline in the post text via `meta_update_post` instead of the first-comment pattern. Until a real comment-creation tool shows up, don't promise "link in first comment" for Facebook — put it inline. |
| Instagram | Live posting | Meta MCP — `meta_publish_instagram_reel`, `meta_publish_instagram_photo`, `meta_publish_instagram_carousel` | Same Meta connector as Facebook. |
| X (Twitter) | Live posting, text only | `x-write` MCP — `post_to_x` (also `reply_to_post`, `quote_post`, `repost`, `delete_post`) | Confirmed working 2026-07-14. **`post_to_x` takes an optional `media_ids` array, but no media/video upload tool is exposed** — there is currently no way to obtain a `media_id` to attach, so treat X posts as text-only until an upload tool shows up. Don't promise video/image attachment on X without re-checking this. |
| LinkedIn | Not yet connected | — | Brian is working on this (as of 2026-07-14). Once connected, re-check its actual capabilities (text only vs. media) the same way X's were checked — don't assume feature parity with Meta. |
| Nextdoor | No MCP, not expected | — | No API path exists for this the way it does for the others; plan on this staying copy-only indefinitely, per Brian. |

## The approval rule (applies to every live-posting tool above, no exceptions)

Unlike WordPress drafts, none of these tools have a draft/scheduled state — calling `meta_create_post`, `post_to_x`, or any future LinkedIn equivalent publishes immediately and publicly. **Always get Brian's explicit go-ahead on the specific post content before calling a live-posting tool.** This is different from WordPress, where leaving something in `draft` status is itself the safety mechanism — here the safety mechanism is asking first, every time, not just the first time a connector is set up.

Practically: draft the copy, show it to Brian, wait for confirmation, then post. Don't batch-post a week's content speculatively even if the copy was approved in principle earlier — confirm the specific post at the specific time.

## Which skills use this

- `skills/monday-cornerstone.md`, Step 8 (Monday social distribution) — Facebook/Instagram/X live via the tools above, LinkedIn once connected, Nextdoor as copy.
- `skills/thursday-tip.md`, social posts step — same platform split applies; update that skill's inline notes to point here rather than re-describing connector mechanics locally.

## Change log

- 2026-07-13: Meta (Facebook/Instagram) confirmed live.
- 2026-07-14: X confirmed live via `x-write` (text only — no media upload tool available).
- 2026-07-16: Discovered `post_to_x` silently truncates posts over 280 chars instead of erroring — always pre-count (URLs = 23 chars each, t.co) before posting. Discovered the Meta MCP has no Facebook top-level-comment tool — use inline links for Facebook instead of "link in first comment." Both posting workflows (Meta video/photo, X text) confirmed to require publicly-fetchable URLs — files only in OneDrive/dev-only locations aren't reachable by these tools; media must be uploaded to the live WordPress media library first.
