# Revision Response 02 — Post 10342

Responds to: `reviews/posts/10342/01-review.json` (2026-11-07T02:08:08.221Z)  
Responder: Claude (Cowork) · 2026-11-07T02:25:00Z  
Repo: `3b3dbcb9ecfc3c6bb202026d73f5b37dabd1032c` (dirty: new response files only)  
WordPress: draft, https://dev.alleastbayproperties.com/?p=10342

**Summary:** All four findings addressed. Script and Key Takeaway fixed to match 10340; Berkeley guide link added. Page stays draft until the video is recorded, embedded and the script relabeled 'Video Transcript' after checking.

**requires_human_review:** true · **recommendation_to_brian:** proceed_to_gpt_final_review

## Dispositions

### 10342-F01 — accepted

**Rationale:** Same as 10340-F01.

**Change applied:** Video Script paragraph 4 replaced.

> Before: Now it's ten percent at a time, with the rest still banked for later.

> After: Once it takes effect, increases based on the adjustment are limited to ten percent in a twelve-month period. Our reading is that anything above that stays in the rent ceiling for later, but confirm the amount with the Rent Board.

### 10342-F02 — accepted

**Rationale:** Same as 10340-F02.

**Change applied:** Video Script paragraph 6 replaced.

> Before: And tenant associations can now form in self-managed buildings with five or more units.

> After: And tenants on self-managed parcels with five to nine units will be able to form a tenant association. Professionally managed parcels already qualified at any size, and an established association keeps its rights if the manager leaves.

### 10342-F03 — accepted

**Rationale:** Same root cause as F02.

**Change applied:** Key Takeaway rewritten with 'once Measure X takes effect', parcels and continuing rights. Intro also now says the result is unofficial and not yet in effect.

> Before: Tenant associations can now form in self-managed buildings of 5 or more units; professionally managed buildings were already covered at any size

> After: Once Measure X takes effect, the tenant-association threshold expands to self-managed parcels with 5 to 9 units; professionally managed parcels already qualify at any size, and established associations keep their rights if management ends

### 10342-F04 — accepted_with_modification

**Rationale:** Draft-until-video and transcript relabel accepted as standing process. Berkeley deep-dive link added now. Elections Code 9217 handled as in 10340-F06 (snapshot-less; Brian to confirm on leginfo). Rendered VideoObject/blocks can only be checked after the video is embedded.

**Change applied:** Added Berkeley Rent Control Compliance Guide to Laws & Resources. Page stays draft with 'Video Script' label until the render is checked against the script.

> Before: Video in production. It will appear here once it's published.

> After: (unchanged until the video exists)

## Operating System follow-ups

- Tenant-association 9→4 change and continuing-rights sentence visually verified by reviewer on official PDF p.18; already recorded in rent-caps.md by commit 382f8d8, no further change. (`knowledge/laws/rent-caps.md`)
- Save an Elections Code 9217 snapshot to knowledge/sources/state/statutes/ and re-verify civ-827/ccp-1013 against leginfo (inaccessible to both reviewers this round). (`knowledge/sources/README.md`)

## Still open

- Brian: confirm Civil Code 827, CCP 1013 and Elections Code 9217 on leginfo in a browser.
- Authenticated preview of rendered blocks and schema; featured image; video render, embed and transcript relabel.
- GBP copy is in `week2-monday-distribution.md` (sent in chat) if the final review wants to check consistency.
