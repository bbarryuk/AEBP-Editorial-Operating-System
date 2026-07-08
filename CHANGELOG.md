# Changelog

All notable changes to the AEBP Editorial Operating System are recorded here. Versions are tagged when a document has actually been used on real content and held up — not on a fixed schedule.

## [Unreleased]

### Fixed (same-day follow-up, 2026-07-07 evening)
- **Oakland RAP 2.3% figure upgraded from "calculated, pending confirmation" to "Confirmed."** A direct fetch of the City of Oakland's own [`Learn More About Allowable Rent Increases`](https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases) page (not found by the earlier WebSearch-only pass) states directly: *"Effective August 1, 2026, the new annual CPI rent increase is 2.3%."* The same page independently corroborates the AB 1482 8.8% figure too. Updated `knowledge/laws/rent-caps.md`, posts 7938 and 7958 (all "pending Oakland's official notice" language replaced with the confirmed citation), and `tests/legal/TEST-LEGAL-001.md`.
- **Berkeley 2026 AGA (1.0%) added and confirmed** via the [Berkeley Rent Board's own "2026 AGA Published" notice](https://rentboard.berkeleyca.gov/elected-rent-board/news/2026-aga-published-and-2025-security-deposit-interest-payment-due-soon) — new section in `knowledge/laws/rent-caps.md`, flagging Berkeley's different mechanics (calendar-year cycle, different CPI region and lookback window, different eligibility rules) so it doesn't get conflated with Oakland/AB 1482's Aug–Jul cycle in future posts.
- **Richmond 2026 AGA verification attempted, not completed.** Secondary sources suggest 1.5% (Sept 1, 2026–Aug 31, 2027), but a direct fetch of `ci.richmond.ca.us/3376/Rent-Increase` returned only stale 2019 content (likely JS-rendered, not captured by a static fetch). Logged as still-unconfirmed in `knowledge/laws/rent-caps.md` rather than guessing — do not cite a Richmond 2026 figure in published content until a primary source is found.

### Fixed
- **Post 7938** ("What Does a Property Manager Actually Do?") — the two GATE-LOCAL-ACCURACY / GATE-LEGAL-ACCURACY failures from the 2026-07-07 review are resolved. Added citations to the Key Facts table, a source note after the video transcript, the licensing paragraph, and FAQ #5; added a new "Sources" section (matches AEBP's existing house style on other legal posts). Both flagged figures were independently re-verified against primary sources rather than just cited on faith: AB 1482's 8.8% cap is confirmed via BLS News Release 26-739-SAN (San Francisco-Oakland-Hayward CPI, April 2026); Oakland's 2.3% RAP figure is a calculation from the City's published formula (60% of CPI, max 3%) and is explicitly labeled "pending Oakland's official notice" rather than asserted as confirmed — no independent search found an actual City of Oakland notice for the Aug 1, 2026 rate yet. All edits stayed within native Gutenberg blocks.
- **Post 7958** (the companion video page for 7938, same YouTube video, same transcript) — carried the identical uncited rent-cap and licensing claims in its own body copy and Key Takeaways list, independent of post 7938. Same review gates would have failed here too; not caught in the original review because only 7938 was reviewed. Fixed with the same citations, plus a link back to 7938's Sources section and two new entries in the existing "Resources Mentioned" list (BLS CPI release, DRE lookup already there). This is itself a small process gap worth remembering: a Monday cornerstone post and its video companion currently get reviewed and fixed as if they were one artifact, but they're two separate published URLs with independently gate-checkable claims.

### Added
- `knowledge/laws/rent-caps.md` — first file in `knowledge/laws/`. Documents AB 1482 (confirmed, statutory formula + BLS data) and Oakland RAP (calculated, pending city confirmation) rent-cap figures for Alameda/Contra Costa, with per-figure confidence levels and a currency-check date (re-verify after Aug 1, 2026). Exists so the next post citing these numbers has something to check against instead of repeating the citation gap that caused this round's review failure.
- `tests/legal/TEST-LEGAL-001.md` — first real entry in the `/tests` regression suite (previously documented in README but empty). Logged from the actual post-7938 review: both flagged claims turned out to be numerically correct, but still should have failed `EVD-CITATION-REQUIREMENT` as originally published — the case exists to catch a future standards revision that quietly stops requiring citations for claims a writer is confident about.
- `docs/03-Review-Format.md` (v0.1) — new normative document defining how a review gets classified and written up: `FIND-TYPE` (Type A Content Error / Type B Evidence Gap / Type C System Gap), root-cause structure (Finding → Root Cause → Fix → Future Prevention), a "Strengths Worth Preserving" section, separated Article-fixes vs. Operating-System-improvements lists, and a presentation layer for `SCORE-*` categories (still numeric per `docs/01`, now with explicit threshold-status and what's-working/what's-holding-it-back framing). Synthesized from ChatGPT's critique of the first real review, with one deliberate divergence — see below.
- Brand Voice renumbered from `docs/03` to `docs/04` in `docs/01`'s `STD-OUT-OF-SCOPE` section to make room for `docs/03-Review-Format.md`. The document itself still doesn't exist yet.

### Previously added
- `doc_type` frontmatter field (`normative`/`informative`) on `docs/01`, `docs/02`, and `knowledge/company/overview.md` — normative documents define requirements a draft can violate; informative documents provide context/facts and aren't themselves checkable rules.
- README section documenting normative/informative and listing three deliberately deferred ideas from this round of ChatGPT review: a `/tests` editorial regression suite, a glossary, and an `automation_ready` knowledge field — noted as planned rather than silently dropped.

### Considered and explicitly not done (across both rounds)
- A Critical/Major/Minor severity scale on every finding, as ChatGPT proposed this round — not adopted in `docs/03-Review-Format.md`. Reasoning: `docs/01` already establishes gated categories as pass/fail with no partial credit; a severity scale on top of a binary gate would quietly reintroduce partial credit ("it only failed a Minor"). The Type A/B/C classification already carries the same practical information (Type A always blocks, Type B blocks but is typically fast to fix, Type C often doesn't block this post but always creates follow-up work) without touching the gate's binary nature.
- Berkeley and Richmond rent-cap figures — referenced in AEBP's own published guides (1.0% and 1.62% respectively) but not independently re-verified this round, so not added to `knowledge/laws/rent-caps.md` as confirmed. Flagged in that file as unconfirmed rather than silently omitted.
- Sequential numeric rule IDs — kept mnemonic slugs (already decided last round; GPT concurred this round).
- `/tests` folder and example test cases — format is documented in README, but no files created; should grow from real review cases, not invented ones.
- Glossary — deferred until documents actually show definitional drift.
- `automation_ready` field — deferred until an automation step exists that would consume it.
- `docs/02-Evidence-and-Sourcing.md` — split out of `docs/01` §5–6 per ChatGPT's review. Adds `EVD-SOURCE-HIERARCHY` (8-level evidence priority), `EVD-CURRENCY-CHECK`, `EVD-UNCERTAINTY-HANDLING`, and `EVD-BLOCK-PENDING-VERIFICATION` — none of which existed before this pass.
- Mnemonic rule IDs across `docs/01` and `docs/02` (`STD-*`, `GATE-*`, `SCORE-*`, `EVD-*`) — deliberately non-sequential slugs rather than numbers, so inserting a new rule later doesn't require renumbering anything that cites an existing one.
- `STD-OUT-OF-SCOPE` section in `docs/01` — names what this doc does NOT cover and where that content belongs instead, to keep the standards doc from growing indefinitely.
- Dependency frontmatter (`purpose`/`used_by`/`depends_on`/`referenced_by`) on `docs/01` and `docs/02`.
- Extended knowledge frontmatter schema (`review_frequency`, `authority`, `confidence`, `review_method`) — applied to `knowledge/company/overview.md`, documented in `README.md`.
- `LICENSE.md` — CC BY-NC-ND 4.0 (Attribution-NonCommercial-NoDerivatives). Brian's decision: repo stays public for transparency/AI access, but competitors can't legally reuse or adapt the editorial methodology. Applies to content (`docs/`, `knowledge/`, `templates/`, `prompts/`, `skills/`); any future code in `automation/` will need its own license note.

### Changed
- All three `skills/*.md` manifests updated from `NOT YET WIRED` to `PARTIALLY WIRED` — the installed Cowork skills (`aebp-monday-cornerstone`, `aebp-thursday-tip`, `aebp-wwyd-social`) now read `knowledge/company/overview.md` and `docs/01-Editorial-Standards.md` (Evidence Standard, Confidence Levels, gated-vs-scored standards gate) at draft time, with an explicit inline fallback if this repo folder isn't connected in a given session. Post/scenario structure and tool-specific mechanics remain inline pending `templates/` and `docs/02+`.

## [0.1.0] — 2026-07-07

Initial foundation, built by Claude in Cowork per the plan worked out between Brian, Claude, and ChatGPT.

### Added
- `README.md` — vision, architecture, folder map, versioning philosophy, how Claude and ChatGPT should each use the repo
- `docs/01-Editorial-Standards.md` (v0.1) — editorial philosophy, audience, evidence standard, confidence levels, gated vs. scored review categories with draft minimum thresholds
- `knowledge/company/overview.md` — verified AEBP company facts, fees, service area, sourced from `llms.txt`, with `last_verified`/`next_review` metadata
- `knowledge/llms.txt` — point-in-time mirror of `alleastbayproperties.com/llms.txt` (fetched 2026-07-07) for offline/automation reference
- `skills/monday-cornerstone.md`, `skills/thursday-tip.md`, `skills/wwyd-social.md` — manifests for the three Claude skills already installed in Cowork, documenting purpose, inputs, outputs, and which standards/knowledge docs each depends on

### Known gaps (not yet built)
- `docs/02-Brand-Voice.md` and everything after it (Legal Accuracy, SEO/GEO, Content Structure, Conversion, WordPress, Scoring Rubric, Automation)
- `templates/`, `automation/` folders — intentionally empty; automation comes after the process is validated by hand
- The three installed Claude skills still encode standards inline rather than reading from `docs/` and `knowledge/` — this repo currently documents that gap rather than closing it (see `sync_status` in each `skills/*.md` manifest)
- No test yet against a real post — v0.1 status on the standards doc means exactly that: drafted, unvalidated

### Notes
- Repo is public on GitHub (`bbarryuk/AEBP-Editorial-Operating-System`), cloned locally into a OneDrive-synced folder. Git's own file-locking has shown friction with OneDrive's sync engine (a stale `.git/index.lock` couldn't be removed from within Cowork) — worth keeping an eye on, or moving the working clone outside OneDrive sync if it recurs.
