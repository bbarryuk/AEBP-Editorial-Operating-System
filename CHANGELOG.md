# Changelog

All notable changes to the AEBP Editorial Operating System are recorded here. Versions are tagged when a document has actually been used on real content and held up — not on a fixed schedule.

## [Unreleased]

### Added
- `doc_type` frontmatter field (`normative`/`informative`) on `docs/01`, `docs/02`, and `knowledge/company/overview.md` — normative documents define requirements a draft can violate; informative documents provide context/facts and aren't themselves checkable rules.
- README section documenting normative/informative and listing three deliberately deferred ideas from this round of ChatGPT review: a `/tests` editorial regression suite, a glossary, and an `automation_ready` knowledge field — noted as planned rather than silently dropped.

### Considered and explicitly not done this round
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
