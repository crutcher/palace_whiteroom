# Cycle-145 resume notes (post batch-47 finalization de-bulk campaign)

**SESSION RESTART REQUIRED before the next primary cycle.** Five `.claude/agents/` role-specs changed (the producer re-accretion discipline); the parent must restart the Claude Code session so the new agent definitions load before any producer dispatches. The restart also resets primary context (subsumes the retired `/compact` step — do NOT run a separate compaction).

## Agent-defs changed (why the restart is needed)

The **batch-47 FINALIZATION static-state-surface discipline** was codified into the five content-authoring producer role-specs, so they stop re-introducing the process/judgment accounting the de-bulk campaign removed:

- `.claude/agents/harvester.md` — new finalization blockquote after `# Role:`.
- `.claude/agents/abstractor.md` — new finalization blockquote.
- `.claude/agents/lifter.md` — new finalization blockquote (the pure-rewriting role — also proactively strips process accounting it encounters).
- `.claude/agents/combinator-miner.md` — new finalization blockquote (its proposed-changes).
- `.claude/agents/layer-intro-author.md` — new finalization blockquote (intros / dep-maps / concept pages / Synthesis libs; dep-map Status cells carry the bare static rank token, no cycle provenance; carve-out for `methodology/goal-flow.md` + `meta-reviews/*`).

Each points at the skill `skills/finalization-debulk/SKILL.md` (the strip/keep/lift discipline) and the exemplar `book/src/L4/krylov-step.md`. The rule in one line: **firmness lives in frontmatter `rank:`/`firmness:`; a firm frontmatter-rank entry has NO `## Status` prose; non-firm + no-frontmatter-rank entries keep a CONCISE static `## Status` token (the sole rank carrier); never re-introduce cycle-tags / verified_against / reports/ pointers / process narrative.**

## State the next planner should know

- **The batch-47 finalization de-bulk campaign is COMPLETE** (commits `95cd45e`→`d494a31` book waves; `96728d7` discharge record). All 284 target `book/src/**` files de-bulked (−103,753 words / −11.3%); graded-stack baseline held exactly through the waves; 0 genuine citation loss; build EXIT 0. Full record: `scaffolding/priorities.md` batch-47 head; memory `project_finalization_debulk_directive`.
- **Two follow-ups discharged this session (a)+(b):** (a) the producer re-accretion discipline (these role-spec changes) and (b) the lone `stub`-ranked `synthesis/data-algebra.md` reconciled to `navigational-container` (matching its 5 sibling synthesis chapters).
- **Graded-stack baseline MOVED (deliberate, by the data-algebra reconcile):** `stub 1→0`, rank-histogram `typed-no-rank 89→90`, `promotion_frontier 12→11`. The two hard invariants hold (`rank_violations 0`, `unresolved 0`); `typed 331`, `untyped 61`, `files 392`, `roots 45`, `detritus 123`, `true_detritus 51` UNCHANGED. **The next cycle's tripwire baseline is `promotion_frontier 11` (was 12).**
- **Still open (deferred):** the pre-existing `L2/index.md` fold-cohort KaTeX `\acc`-in-`$`-span render WARN (cosmetic, predates the campaign, table-cell so step-5c doesn't trip).
- **Forward direction:** batch-47 was the finalization de-bulk LEAD (a user-directed out-of-band campaign). With it complete, the maintenance floor is the standing surround; the forward direction is again the human's to set (the §CENTRAL ASK posture) unless the human directs new substantive work.

## FOUR MORE finalization directives landed AFTER these resume notes were first written (2026-06-08, all pushed)

These were user-directed out-of-band finalization passes (NOT numbered cycles), on top of the de-bulk:

1. **Code-identifier chapter naming** (`7678f72`; memory `project_code_identifier_chapter_naming`). Operator chapters → snake_case (`iterate-while`→`iterate_while`, `krylov-step`→`krylov_step`, `assemble-diagonal`, `bilinear-form`, `divfree-projector`, `eigenvalue-untransform`, `floquet-correction`, `ls-update-column`, `matrix-weighted-norm`, `incremental-least-squares`, `iterate-while-with-prev`); struct concept pages → PascalCase (`op-params`→`OpParams`, `sim-state`→`SimState`, `solve-result`→`SolveResult`, `step-outputs`→`StepOutputs`, `prev-carry`→`PrevCarry`). Depth = filenames + links + in-code identifiers. Descriptive theme/multi-word chapters (`*-mutation-rotation`, `*-dissolution`, `matrix-free-operator-apply`, `eigsolve-impl`, `nleps-deflated-eigensolve`, `sharding-decompose-reduce`) LEFT hyphenated. 23 files `git mv`'d, 212 files / 1775 edits, graph intact.
2. **Heading-metadata-hygiene** (`a7262d8`, `eb46266`; skill `heading-metadata-hygiene`). Section/chapter headings with status/classification tails → moved to structured `**Status:**`/`**Kind:**`/italic lines below the title; short distinguishing glosses (Sub-pattern A/B/C, etc.) KEPT for TOC navigability; `## Status` rank-carriers NEVER touched; anchor-referenced headings preserved. ~130 headings across ~55 files.
3. **Frontmatter NOT rendered → FIXED** (`833228a`). Root cause of "metadata rendered as section headers": mdBook had no frontmatter preprocessor, so YAML frontmatter (incl. `#`-comment lines → `<h1>`) rendered on every page. Added `book/strip-frontmatter.py` (registered in `book.toml`, runs before mermaid/katex/links; mdBook v0.5.1 chapter list is `items`). **NEW BUILD INVARIANT:** no rendered page may contain its own frontmatter — a candidate `integrator-finalize` step-5d post-build guard (analog of the KaTeX step-5c), for the next meta-phase to codify.

## What the NEXT meta-phase should codify (these landed out-of-band; fold into CLAUDE.md + role-specs properly)

- The 2 finalization skills (`finalization-debulk`, `heading-metadata-hygiene`) + the producer re-accretion discipline + the **legal-identifier chapter-naming convention** (add "new operator/struct chapters use legal-identifier filenames; descriptive themes stay hyphenated" to `harvester`/`abstractor`/`layer-intro-author`).
- The frontmatter-render fix as a build invariant (step-5d guard candidate).
- The `## Status`-as-sole-rank-carrier subtlety (no-frontmatter-rank files) — already in the skills; ensure role-specs and the graded-stack-scheme doc note it.
- Carry the deferred pre-existing `L2/index.md` fold-cohort KaTeX `\acc`-in-`$`-span WARN (cosmetic).
- Decide the `feature/*.L4.md` H1 convention-tails (`— L4 composition-root (output product)`) — left intentionally uniform; normalize Part-wide or keep.
