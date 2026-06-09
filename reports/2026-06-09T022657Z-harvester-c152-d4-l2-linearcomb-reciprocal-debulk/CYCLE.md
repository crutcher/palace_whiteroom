---
agent: harvester
invoked_at: 2026-06-09T022657Z
scope: cycle-152 D/E/F de-bulk scale-out, dispatch D4 — E-class directive-date de-bulk
status: integrated
integrated_at: 2026-06-09T025046Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (staging row D4). E-class de-bulk of linear_combination/reciprocal (single 2026-06-01 date dropped per file) + fixed the reciprocal.md reference side of the stale prose-slug dot-l2-leaf-floor-vs-fold-only-design (3 sites retired, live ./index.md link kept). Companion to D2 — together fully discharge OQ reciprocal-stale-prose-slug-dot-l2-leaf-floor-ref. Baseline HELD EXACTLY; build EXIT 0; step-5b/5c/5d clean."
inputs:
  - book/src/L2/linear_combination.md (E-class — 2026-06-01 directive-date provenance)
  - book/src/L2/reciprocal.md (E-class date + stale prose slug dot-l2-leaf-floor-vs-fold-only-design)
  - skill finalization-debulk (incl. meta-150 E-class rephrase-to-drop-the-date rule)
  - exemplar book/src/L4/krylov_step.md
  - OQ reciprocal-stale-prose-slug-dot-l2-leaf-floor-ref (discharged from reciprocal side)
---

# CYCLE: Cycle-152 D4 — E-class directive-date de-bulk of `L2/linear_combination.md` + `L2/reciprocal.md`

## Summary

Applied the `finalization-debulk` skill (E-class directive-date rule + standard
process-accounting strip) to two L2 chapters. Both carried a single `2026-06-01`
directive-date provenance reference woven into structural-rationale prose; both were
rephrased to drop the date while keeping the static structural fact (the vocabulary-shift
redirect named directly, no date). `reciprocal.md` additionally carried a pre-existing stale
PROSE slug `dot-l2-leaf-floor-vs-fold-only-design` (3 occurrences, lines ~79/~254/~379)
pointing at the retired `L2/index.md §"Working Notes"` section (being stripped by the parallel
D2 dispatch this cycle); the prose was rephrased to state the leaf-vs-fold design-finality
fact directly without the dead cross-slug. No node/edge/rank/status/semantics moved; every
citation and live link preserved verbatim; graded-stack lint baseline HELD EXACTLY.

This was a DIRECT-EDIT de-bulk dispatch (per the batch-50 finalization-campaign convention,
not a proposed-changes dispatch). Edits applied to disk; recorded here.

## Per-file results

### `book/src/L2/linear_combination.md`

**E-class date stripped (1):** §Context line 39 —
`(vocabulary-shift redirect 2026-06-01, `CLAUDE.md` §Methodology invariants)`
→ `(the vocabulary-shift redirect, `CLAUDE.md` §Methodology invariants)`. Date dropped; the
governing redirect named directly; the static fact (L2 combinator is the family entry; arity
forms are specialization notes; same-named base-form floor is the retired rectangular pattern)
preserved verbatim.

No other process accounting found (no cycle-NNN / batch / wave / reports / verified_against
tags — confirmed by grep).

**Citations before/after — MATCH (10 palace pinpoint cites, all counts identical):**
`iterative.cpp:632` (1); `nleps.cpp:343-344` (2); `rap.cpp:764-787` (1); `vector.cpp:203-227`
(1); `vector.cpp:702-712` (1); `vector.cpp:726-730` (2); `vector.cpp:749-751` (2);
`vector.hpp:305-316` (1); `romoperator.cpp:188-189` (2); `timeoperator.cpp:217` (1). The
in-table bare-path cites (`vector.cpp:276-311` etc., `concepts/scalar-promotion.md:49`)
untouched. All 24 markdown links unchanged.

### `book/src/L2/reciprocal.md`

**E-class date stripped (1):** §"Downward to L1" line 331 —
`the degenerate smell the 2026-06-01 VOCABULARY-SHIFT REDIRECT names`
→ `the degenerate smell the vocabulary-shift redirect names`. Date dropped; static
identity-in-named-terms-is-a-smell fact preserved.

**Stale-slug fix (3 occurrences, dead PROSE token — NOT a live link):** the bare backtick
slug `dot-l2-leaf-floor-vs-fold-only-design` and its `L2/index.md §"Working Notes"` referent
(retired by D2 this cycle) rephrased in three places, keeping the load-bearing
"NOT-a-fold-member / design-final" structural content and dropping only the dead cross-slug:
  1. §"No fold-parent" `## Consequence — design-finality` (line ~77) — recast "the
     **leaf-vs-fold design fork** (`book/src/L2/index.md` §"Working Notes",
     `dot-l2-leaf-floor-vs-fold-only-design`) concerns whether …" as "The leaf-vs-fold design
     question for the per-leaf L2 floors `dot` / `scal` is whether …"; kept the full
     design-finality argument (no fold-parent subsumes a nonlinear elementwise self-map →
     `reciprocal` can only ever be a same-named standalone leaf).
  2. §Dependencies "Fold-parent: NONE" (line ~253) — "The leaf-vs-fold design fork
     (`book/src/L2/index.md` §"Working Notes") does not apply" → "The leaf-vs-fold design
     question does not apply to this floor".
  3. §Evidence (line ~378) — `[`book/src/L2/index.md`](./index.md) §"Identity-in-form BLAS-1
     floors" + §"Working Notes" (the `dot-l2-leaf-floor-vs-fold-only-design` fork)` →
     `[`book/src/L2/index.md`](./index.md) §"Identity-in-form BLAS-1 floors"` + "places it
     outside the leaf-vs-fold design question". The live `[..](./index.md)` link KEPT
     (distinguished from the dead prose slug); only the retired §"Working Notes" sub-anchor
     and dead slug dropped.

This discharges OQ `reciprocal-stale-prose-slug-dot-l2-leaf-floor-ref` from the reciprocal
side (D2 retires the `L2/index.md` §"Working Notes" section itself).

No other process accounting found (no cycle/batch/wave/reports/verified_against tags).

**Citations before/after — MATCH (11 palace pinpoint cites, all counts identical):**
`bilinearform.cpp:278` (2); `chebyshev.cpp:178` (2); `jacobi.cpp:16` (1); `jacobi.cpp:80` (2);
`jacobi.cpp:92` (1); `vector.cpp:248-261` (2); `vector.cpp:253-260` (1); `vector.cpp:257` (1);
`vector.cpp:257-259` (5); `vector.hpp:107-108` (1); `vector.hpp:20` (2). All 39 markdown links
unchanged — including every `inner_product.md#…` / `linear_combination.md#…` / `index.md`
anchor link (the dead-slug fix touched PROSE only, no `[link](...)` rename).

## Safety-invariant verification

- **Citations preserved verbatim:** both files — palace pinpoint-cite multiset identical
  before/after; markdown-link multiset identical before/after. CONFIRMED.
- **Rank/status tokens preserved:** `linear_combination` `rank: firm` frontmatter untouched;
  `reciprocal` `firmness: firm` frontmatter untouched. No `## Status` section in either file
  (both are firm-frontmatter entries — correct static-state shape already). CONFIRMED.
- **No node/edge/rank/status/semantics move:** edits are prose-only. CONFIRMED.
- **No live link renamed:** the stale slug was a bare PROSE backtick token, not a markdown
  link; the live `[..](./index.md)` link kept. CONFIRMED.
- **Laws / structural-facts preserved:** all 7 linear_combination laws + non-laws; all 8
  reciprocal laws + non-laws; the design-finality / NOT-a-fold-member content; untouched.

- **0 `2026-0X-XX` date-provenance remaining** in both files (grep-confirmed empty).
- **Stale `dot-l2-leaf-floor-vs-fold-only-design` prose slug retired** in reciprocal.md
  (grep-confirmed empty); `Working Notes` reference also gone (grep-confirmed empty).

## Lint baseline — HELD EXACTLY

`python3 tools/graded-stack-lint/graded_stack_lint.py --book-src book/src`:

```
files=392, typed=331, untyped=61, rank_violations=0,
unresolved_depends_on_targets=0, promotion_frontier=11,
detritus=123, true_detritus=51
```

Matches the prompt's required baseline on every field, before and after.

## Open questions / caveats

- OQ `reciprocal-stale-prose-slug-dot-l2-leaf-floor-ref` is discharged from the reciprocal
  side by this dispatch; the `L2/index.md` §"Working Notes" retirement (D2 this cycle) closes
  it on the index side.
- No new open questions.
