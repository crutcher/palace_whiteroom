---
agent: harvester
invoked_at: 2026-06-09T022626Z
scope: cycle-152 D/E/F de-bulk scale-out — dispatch D3 (E-class directive-date provenance)
status: integrated
integrated_at: 2026-06-09T025046Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (staging row D3). E-class de-bulk of 3 firm L2 operator chapters correction_step/inner_product/normalize (directive-date provenance + process-pointers dropped from 4 prose fragments; static facts/laws/citations/edges/ranks conserved). c153 residual recorded: normalize.md still carries 3x the stale prose-slug dot-l2-leaf-floor-vs-fold-only-design (out of D3 scope). Baseline HELD EXACTLY; build EXIT 0; step-5b/5c/5d clean."
inputs:
  - skill finalization-debulk (incl. the 3 meta-150 sections; E-class directive-date rephrase rule)
  - c151 PILOT pattern
  - exemplar book/src/L4/krylov_step.md
  - files: book/src/L2/correction_step.md, book/src/L2/inner_product.md, book/src/L2/normalize.md
---

# CYCLE: c152-D3 — E-class directive-date de-bulk of three firm L2 operator chapters

## Summary

Edited the three firm L2 operator chapters in-place (de-bulk convention, NOT
proposed-changes — this is a finalization de-bulk dispatch, the meta-150 in-place
edit mode). Each carried `2026-0X-XX` directive-date provenance woven into prose
("the 2026-06-01 vocabulary-shift redirect", "collapsed into this note per the
2026-06-01 redirect", "per the 2026-06-01 VOCABULARY-SHIFT REDIRECT", "the 2026-05-31
`l2-floor-under-l3-leaf-cohort` directive"). Applied the E-class
rephrase-to-drop-the-date rule: drop the `2026-0X-XX` parenthetical, KEEP the static
structural fact by naming the redirect/concept directly without the date. No other
inline process accounting (cycle-tags, promotion-history, `reports/…` pointers,
`verified_against`/`## Verified-against` blocks) was present in these three files —
the date provenance was the only de-bulk target. All HARD SAFETY INVARIANTS held:
every `palace/…:N-M` citation preserved verbatim (before/after diff IDENTICAL), every
rank/status token preserved (all three are firm frontmatter-rank entries with no
`## Status` prose, correctly untouched), no node/edge/rank/status/semantics move, no
slug/anchor rename. Lint baseline held EXACTLY.

## Per-file record

### book/src/L2/correction_step.md (firm; frontmatter `rank: firm`)

- **Date references stripped/rephrased: 1.**
  - L48: `the 2026-06-01 vocabulary-shift redirect, METHODOLOGY-REDIRECT.md §1d`
    → `the combinator-as-entry vocabulary-shift`. Rephrase-to-drop-the-date: keeps the
    static structural fact (the combinator-as-entry vocabulary shift is why the
    smoothers are specializations, not mirrored floors) and drops both the date AND the
    `METHODOLOGY-REDIRECT.md §1d` process pointer. The §Context (L62) and §"L2 vs
    lower-layer distinction" (L396-397) already name "the vocabulary-shift redirect"
    date-free; this edit makes L48 consistent with those.
- **Citations before/after: 13 distinct (15 total occurrences) — MATCH** (diff IDENTICAL).
- **Rank/status: `firmness: firm` (L4) + `rank: firm` (L11) intact; no `## Status` prose
  (correct for firm frontmatter-rank entry).**

### book/src/L2/inner_product.md (firm; frontmatter `rank: firm`)

- **Date references stripped/rephrased: 1.**
  - L171: `collapsed into this note per the 2026-06-01 redirect`
    → `collapsed into this note per the vocabulary-shift redirect`. Rephrase-to-drop-the-date:
    keeps the static fact (the standalone `L2/dot.md` is collapsed into this combinator
    note) and names the redirect without the date.
- **Citations before/after: 26 distinct (46 total occurrences) — MATCH** (diff IDENTICAL).
- **Rank/status: `rank: firm` (L4) intact; no `## Status` prose (correct).** The
  member-granularity `tdot` "type-API-surface only" caveat (§"tdot") is a structural
  scope-of-evidence fact, NOT process/promotion-history accounting — KEPT verbatim.

### book/src/L2/normalize.md (firm; frontmatter `firmness: firm`)

- **Date references stripped/rephrased: 2.**
  - L137 (§"Downward to L1"): `recorded here as an in-line note rather than a dedicated
    L2-L1/ theme chapter (the degenerate identity-in-named-terms smell, per the 2026-06-01
    VOCABULARY-SHIFT REDIRECT; CLAUDE.md §Methodology invariants ⟢)`
    → `… per the vocabulary-shift redirect)`. Drops the date AND the
    `CLAUDE.md §Methodology invariants ⟢` process pointer; keeps the static fact (the
    degenerate identity-in-named-terms smell per the redirect).
  - L174 (§"L2 vs L1 distinction"): `… rests on a present adjacent L2 parent — per CLAUDE.md
    §Methodology invariants Identity-lowerings still require both L levels and the 2026-05-31
    l2-floor-under-l3-leaf-cohort directive.`
    → `… rests on a present adjacent L2 parent — the layer-coherence floor under an
    identity-in-form L3 leaf.` Drops the date and the directive-id/CLAUDE.md process pointer;
    keeps the static structural fact (this L2 entry is the layer-coherence floor under the
    firm identity-in-form L3 leaf).
- **Citations before/after: 9 distinct (19 total occurrences) — MATCH** (diff IDENTICAL).
- **Rank/status: `firmness: firm` (L4) intact; no `## Status` prose (correct).**
- **NOTE (left in place, not date-bearing):** L23-24 / L82 / L91 / L174-context retain
  the methodology-invariant *name* "Identity-lowerings still require both L levels" as a
  structural justification for the thin layer-coherence floor. These are date-free
  conceptual references (the structural rationale for the entry existing), not directive-date
  provenance — outside the E-class target. The dispatch's PRIMARY target (E-class date
  provenance) is fully discharged; the remaining methodology-invariant *name* references are
  static structural-justification facts, consistent with the finalization-debulk LIFT rule
  (coupling/justification concepts kept as static facts).

## Verification

- **Date-provenance remaining:** `grep -nE '2026-0[0-9]-[0-9]{2}'` over all three files →
  0 matches each (confirmed). No date is genuinely load-bearing in any of the three (all
  were directive-attribution provenance, not factual dates).
- **Citations:** sorted `uniq -c` citation lists captured before and after; `diff` →
  CITATIONS IDENTICAL (match) for all three files combined.
- **Rank/status tokens:** all three are firm frontmatter-rank entries (`firmness: firm`
  and/or `rank: firm`); none carries a `## Status` prose section (correct — firm
  frontmatter-rank gets no Status prose); none touched.
- **Lint baseline (HOLD — exact):**
  `python3 tools/graded-stack-lint/graded_stack_lint.py --book-src book/src`
  → files scanned 392, typed nodes 331, untyped 61 (warning), 0 rank violation(s),
  0 unresolved depends-on targets (no unresolved line emitted), promotion frontier 11,
  123 detritus (51 true-detritus / 72 reference-reachable §2g).
  Matches the stated baseline `files=392, typed=331, untyped=61, rank_violations=0,
  unresolved_depends_on_targets=0, promotion_frontier=11, detritus=123, true_detritus=51`
  EXACTLY.

## Open questions / caveats

- None blocking. The de-bulk was clean: pure E-class date-provenance rephrase, no
  semantics/laws/citations/edges/ranks moved. The three files are now date-provenance-free
  while retaining every static structural fact, citation, law, and coupling/justification
  concept.
