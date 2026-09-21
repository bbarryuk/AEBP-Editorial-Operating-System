---
skill_name: aebp-weekly-post-review
implementation: ChatGPT reusable review skill
sync_status: WIRED TO CURRENT REPO PROTOCOL
last_synced: 2026-09-20
---

# Skill: Weekly WordPress Post Review

## Purpose

Run AEBP's standard weekly editorial review loop for a WordPress post supplied by post ID. The skill reads the live draft from the AEBP-Dev WordPress connector, reviews it against the current AEBP Editorial Operating System in this repository, writes both human-readable Markdown and machine-readable JSON review artifacts into `reviews/posts/<post-id>/`, and supports repeated review rounds until blocking issues are resolved.

This skill is a thin execution layer. It must not restate or replace rules owned by `docs/`, `knowledge/`, `reviews/*-review.md`, or `automation/schemas/`. Always read the current files at run time.

## Trigger / user input

Typical invocation:

> Review post 9215

Required input:
- WordPress post ID

Optional input:
- Content type, if not inferable from the post or repo context
- Review mode; default is **Pre-Publish Audit** per `docs/03-Review-Format.md`
- Any explicit scope override from Brian (for example, defer rendered-page/schema checks)

Do not ask for information that can be derived from WordPress or the repo.

## Connected systems

- **WordPress:** AEBP-Dev connector, using the AEBP-Dev account.
- **Repository:** `bbarryuk/AEBP-Editorial-Operating-System`, default branch `main`.

The skill reviews and records findings. It does **not** edit or publish the WordPress post unless Brian separately and explicitly asks for that action.

## Run-time sources of truth

At the start of every run, read the current versions of:
1. `docs/01-Editorial-Standards.md`
2. `docs/02-Evidence-and-Sourcing.md`
3. `docs/03-Review-Format.md`
4. `docs/07-Editorial-Automation.md`
5. `automation/schemas/review.schema.json`
6. `automation/schemas/revision-response.schema.json`
7. The applicable content-type manifest in `reviews/`, if one exists
8. Relevant `knowledge/` files needed to check the post's factual/legal/local claims
9. Existing artifacts in `reviews/posts/<post-id>/`

Also inspect the current repository commit before writing artifacts. If the connector cannot expose local working-tree state, record only what is verifiable from GitHub and do not falsely claim a local tree is clean.

## WordPress retrieval

Use the AEBP-Dev connector and retrieve the actual current post, preferably with a complete snapshot:
- `wp_get_post_snapshot` with the supplied post ID and AEBP-Dev link
- Use `content_format: "full"` when markup, block structure, embeds, scripts, FAQ blocks, or schema-relevant structure matter
- A prose-only follow-up read may be used for easier editorial reading, but never instead of the full snapshot when doing a Pre-Publish Audit

Record the post ID, title, status, modified time if available, permalink, and any revision identifier if the connector returns one. Do not invent GMT values or revision IDs.

## Determine the review round

List `reviews/posts/<post-id>/` before creating anything.

Follow `docs/07` numbering and preserve history:
- First GPT review: `01-review.md` + `01-review.json`
- Claude response: `02-revision-response.md` + `02-revision-response.json`
- Next GPT review: `03-final-review.md` + `03-final-review.json`
- Further Claude response: `04-revision-response.*`
- Further GPT review: `05-final-review.*`
- Continue odd-numbered GPT reviews and even-numbered revision responses without overwriting prior artifacts.

If the latest artifact is a GPT review and there is no newer Claude revision-response artifact, do not create another redundant review unless Brian explicitly requests it. If the latest artifact is a Claude revision response, review the actual updated WordPress post and explicitly check every prior disposition against the live draft.

For a follow-up review, read the immediately preceding review and revision-response artifacts and verify:
- every prior finding has a disposition;
- accepted fixes are actually present in WordPress;
- rejected findings have a recorded rationale;
- `requires_human` items are not silently cleared;
- revisions did not create regressions elsewhere in the post or companion copy.

## Review scope

Default mode: **Pre-Publish Audit**.

Apply:
- every applicable `GATE-*` and `SCORE-*` from `docs/01`;
- the applicable manifest checks from `reviews/*-review.md`;
- `FIND-TYPE`, `FIND-STRUCTURE`, strengths, scoring presentation, and split fix lists from `docs/03`;
- evidence requirements from `docs/02`;
- structured artifact rules from `docs/07`.

For legal, regulatory, rent-control, ordinance, statutory, agency, rate, deadline, or other time-sensitive factual claims, verify against current primary or authoritative sources where the Operating System requires verification. Do not rely on model memory when current verification is material.

When a claim cannot be verified:
- classify the issue accurately as Type B and/or Type C when appropriate;
- do not convert lack of evidence into a Type A factual-error claim;
- distinguish a blocked check from proof that the underlying feature or claim is absent.

For first-person AEBP experience claims, populate `claim_provenance` exactly as the schema requires. An AI reviewer must never assign `owner_verified`; use `unverified` unless the claim is documented or clearly hypothetical.

## Companion/package checks

If the applicable manifest requires a companion artifact, identify it from the WordPress post, existing repo artifacts, or connected WordPress data when possible.

For Monday cornerstone posts:
- review the blog post against the cornerstone manifest;
- flag that the companion video page is independently gate-checkable;
- if the companion post ID is identifiable and within the requested scope, inspect it using `reviews/video-review.md`;
- do not falsely imply the companion video or GBP copy was cleared if it was not actually reviewed.

## Creating the artifacts

Each GPT review round produces **both**:
- human-readable Markdown; and
- JSON conforming to `automation/schemas/review.schema.json`.

Write them to:
`reviews/posts/<post-id>/<NN>-review.*` for an initial review, or
`reviews/posts/<post-id>/<NN>-final-review.*` for subsequent GPT rounds.

The Markdown and JSON must describe the same findings, gate states, scores, strengths, fixes, provenance, review scope, and recommendation.

### Markdown requirements

Use the current `docs/03` format. Include:
- post ID/title and review context;
- recommendation;
- applicable gates;
- Type A/B/C findings using Finding / Root Cause / Fix / Future Prevention;
- scored categories with threshold status, what's working, and what's holding it back;
- Strengths Worth Preserving;
- Article fixes;
- Operating System improvements;
- provenance / review limits where relevant;
- a clear note about anything not actually verified.

For follow-up rounds, explicitly state which prior findings are closed, still open, deferred, rejected, or replaced by a regression/new finding.

### JSON requirements

Conform to the current schema; never hand-wave invalid fields.

Important:
- `schema_version` comes from the active review schema.
- `docs_versions` must reflect the versions actually read.
- `repo.commit` is the commit reviewed.
- `repo.state` must be truthful. If the environment cannot establish one of the schema's allowed local-state values, do not fabricate it; report the protocol limitation to Brian and treat it as a system/protocol issue requiring correction before claiming schema-valid output.
- `wordpress` references the post but does not duplicate its full body.
- Gate failures require findings.
- Every first-person AEBP experience claim goes in `claim_provenance`.
- Recommendation must be one of the schema enum values.

## GitHub write behavior

Before writing a path, check whether it already exists.
- Create a new numbered file; never overwrite a prior review round.
- Write the Markdown and JSON as the same review round.
- Use concise commit messages such as:
  - `Add post 9215 initial editorial review`
  - `Add post 9215 follow-up editorial review`

Do not change standards, knowledge, schemas, or manifests during a post review merely because an improvement is suggested. Record those changes under `operating_system_improvements`. Only edit Operating System source files when Brian separately asks for that change or it is explicitly part of the requested task.

## Iteration / handoff to Claude

When blockers exist:
1. Create the review artifacts.
2. Tell Brian the post is held pending fixes and identify the blocking finding IDs.
3. Claude should consume the JSON and respond using `automation/schemas/revision-response.schema.json`, with one disposition per finding.
4. On the next invocation for the same post ID, read Claude's response and the newly updated WordPress draft, verify all dispositions, detect regressions, and write the next odd-numbered review pair.
5. Continue until no blocking content issues remain or a human-required item stops the loop.

A PASS is not permission to publish. Brian still reads the final draft and makes the publication decision, per `docs/07 AUTO-HUMAN-GATE`.

## Completion message

At the end of each run, report:
- which WordPress revision/snapshot was reviewed;
- which repo commit and standards versions were used;
- the recommendation;
- blocking finding IDs, if any;
- exactly which Markdown/JSON files were written;
- whether a Claude revision-response is now expected, or whether the content review is clear for Brian's final human check.

Keep this status concise; the detailed record belongs in the repo artifacts.
