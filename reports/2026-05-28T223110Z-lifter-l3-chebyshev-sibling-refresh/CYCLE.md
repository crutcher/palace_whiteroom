---
agent: lifter
invoked_at: 2026-05-28T22:31:10Z
scope: L3 prose sweep — chebyshev sibling forM_/foldM → iterate_while_pure refresh
status: integrated
integrated_at: 2026-05-28T230323Z
integration_commit: 80db8d6
integration_notes: |
  Applied cycle-017 (per-report position 4). 5-site sibling forM_/foldM ->
  iterate_while_pure/iterate_while_pure_L3 vocabulary refresh + 1 in-scope
  predicate-driven->convergence-predicate-driven disambiguation in
  book/src/L3/chebyshev.md; entry stays partial-obstruction. Post-apply re-grep
  returned ZERO residual forM_/foldM — the chebyshev forM_/foldM->iterate_while
  vocabulary-lag cohort (L4 body 015 + L4 prose 016 + L3 named-sentence 016 + L3
  siblings 017) is now FULLY TERMINATED. OQ
  l3-chebyshev-sibling-formm-foldm-prose-sweep resolved.
inputs:
  - book/src/L3/chebyshev.md
  - book/src/L4/chebyshev.md
  - book/src/L4/iterate-while.md
---

# CYCLE: Re-anchor L3 chebyshev sibling forM_/foldM mentions

## Summary

Companion prose sweep of `book/src/L3/chebyshev.md` closing OQ
`l3-chebyshev-sibling-formm-foldm-prose-sweep` (opened cycle-016). The cycle-014
re-anchor promoted L4 `chebyshev`'s two obstruction loops from the un-anchored
`forM_`/`foldM` rough-in sketch to firm nested `iterate_while_pure` folds with
step-count predicates (outer `pc_it` Richardson sweep `s.it <= op.pc_it`, inner
`k`-recurrence `c.k <= op.order - 1`), with the L3 image being the
`iterate_while_pure_L3` tail recursion. The cycle-016 lifter refreshed exactly
ONE named sentence in this L3 file (§"Value-threaded form (L3 rendering)" closing
paragraph, now `book/src/L3/chebyshev.md:236-241`). Five sibling mentions of the
superseded L4 `forM_`/`foldM` vocabulary remained. This dispatch is a pure
same-shape vocabulary refresh of all five — no L3 semantics, structure, or status
change (entry stays **partial-obstruction**). All five are present-tense
descriptions of the entry's own current rendering (the L4 form it lowers from, or
the L3 form's own loop structure); NONE is intentional historical-narrative
provenance, so all five refresh. No citations are introduced — the canonical
`iterate-while.md:193-195` / L4 §"L4 > L3" anchor was established by the cycle-016
sibling at `:236-241`; these are sibling mentions pointing at that established
phrasing.

## Proposed changes

```edit:book/src/L3/chebyshev.md
[old]: but differ in their iteration structure: `krylov-step`'s outer loop is a
predicate-driven `iterate_while` fold; `chebyshev`'s loops are bounded
`forM_`/`foldM` ranges (rendered at L3 as tail recursions over static index
ranges).
[new]: but differ in their iteration structure: `krylov-step`'s outer loop is a
convergence-predicate-driven `iterate_while` fold; `chebyshev`'s loops are two
nested **step-count-predicate** `iterate_while_pure` folds (outer `pc_it`
Richardson sweep `s.it <= op.pc_it`, inner `k`-recurrence `c.k <= op.order - 1`),
rendered at L3 as the `iterate_while_pure_L3` tail recursions over those static
ranges.
```

```edit:book/src/L3/chebyshev.md
[old]:   monad → explicit `(x, y)`-state threading; the `ChebOp` closure → positional
  operator-parameters value; the `Read`/`ReadWrite` capability typing on
  `ChebSim` → a documented mutation discipline; the `forM_`/`foldM` binds →
  tail recursions over static ranges) is **substantive at the wrapper**; the
[new]:   monad → explicit `(x, y)`-state threading; the `ChebOp` closure → positional
  operator-parameters value; the `Read`/`ReadWrite` capability typing on
  `ChebSim` → a documented mutation discipline; the two nested
  `iterate_while_pure` folds → `iterate_while_pure_L3` tail recursions over their
  step-count predicates) is **substantive at the wrapper**; the
```

```edit:book/src/L3/chebyshev.md
[old]: **body**; it does not erase the L3 loop-structure obstruction, which is a
property of the surrounding `forM_`/`foldM` ranges, not of the body.
[new]: **body**; it does not erase the L3 loop-structure obstruction, which is a
property of the surrounding two nested `iterate_while_pure` folds (the
`iterate_while_pure_L3` tail recursions over the `pc_it`/`k` step-count
predicates), not of the body.
```

```edit:book/src/L3/chebyshev.md
[old]:   E) ()` threads `(x, y)` through the `Solve (ChebSim E)` monad with `Read`/
  `ReadWrite` capability typing; the two sequential obstructions surface as
  `forM_` (outer) and `foldM` (inner) binds.
[new]:   E) ()` threads `(x, y)` through the `Solve (ChebSim E)` monad with `Read`/
  `ReadWrite` capability typing; the two sequential obstructions surface as two
  nested `iterate_while_pure` folds with step-count predicates (`iterate_while_pure`
  outer `pc_it` sweep, `iterate_while_pure` inner `k`-recurrence).
```

```edit:book/src/L3/chebyshev.md
[old]:   typing has demoted to a documented invariant; the closure-typed variant
  absorption has collapsed to one positional `op`; the `forM_`/`foldM` binds are
  tail recursions over static ranges. The kernel body's primitive sequence is
[new]:   typing has demoted to a documented invariant; the closure-typed variant
  absorption has collapsed to one positional `op`; the two nested
  `iterate_while_pure` folds are the `iterate_while_pure_L3` tail recursions over
  their step-count predicates. The kernel body's primitive sequence is
```

## Discipline notes

Pure structural rewrite — vocabulary refresh only, per `.claude/agents/lifter.md`
("structural rewrite, not authorship"). The theme/entry narrative, decomposition,
signature, and status are unchanged. Direction discipline preserved: every
refreshed sentence stays high→low — the §Upward and §"L3 vs L4 distinction" bullets
narrate the L4 form (`iterate_while_pure` folds) lowering FORWARD into the L3 form
(`iterate_while_pure_L3` tail recursions), matching the firm L4 `chebyshev`
§"L4 > L3" phrasing (`book/src/L4/chebyshev.md:427-436`) that the cycle-016 sibling
already adopted at `book/src/L3/chebyshev.md:236-241`.

Register matched to the canonical cycle-016 sibling paragraph
(`book/src/L3/chebyshev.md:236-241`): "two nested `iterate_while_pure` folds over
**step-count predicates** (`c.k <= op.order - 1` inner, `s.it <= op.pc_it` outer) —
the `iterate_while_pure_L3` tail-recursion lowering image". The five refreshes use
the same noun phrase and predicate forms.

Cross-reference to the promotion that motivated this sweep: cycle-014
integrator-finalize re-anchored L4 `chebyshev`'s `forM_`/`foldM` to nested
`iterate_while` folds with step-count predicates (commit `8ac1f37` lineage,
cycle-014 finalize per CLAUDE.md repo-status; L4 firm 3→4, rough-in cohort→0). The
cycle-016 lifter refreshed the one L3 named sentence; this closes the residual
sibling sweep.

No prose-correction (per the cycle-012 content-correction boundary) was needed —
all five sites were vocabulary-stale present-tense descriptions, not wrong claims.

### Historical-narrative judgment (per the watch clause)

Applied the same judgment the cycle-016 L4-side sweep used (which left 4
`forM_`/`foldM` mentions verbatim as superseded-vocabulary provenance, e.g. the
slice-provenance sentence at `book/src/L4/chebyshev.md:582-583` and the
§"L3 vs L4 distinction" / OQ-recap block at `:498-508`). In THIS L3 file there are
**no** such intentional-provenance mentions: a re-grep of `forM_\|foldM` returned
exactly the 5 sites, and each is a present-tense description of the entry's own
current rendering (the L4 form it lowers from, or the L3 form's own loop
structure). None sits in a "superseded"/"slice's rendering"/"had no dep-map row"
provenance frame. Therefore all 5 refresh; zero left verbatim.

## Supporting evidence

- `book/src/L4/chebyshev.md:427-436` — firm L4 §"L4 > L3": "the two
  `iterate_while_pure` folds become the L3 `iterate_while_pure_L3` tail recursions
  over their step-count predicates (`iterate-while.md:193-195`)". The phrasing the
  refresh matches.
- `book/src/L3/chebyshev.md:236-241` — the cycle-016 lifter's canonical refreshed
  paragraph (§"Value-threaded form (L3 rendering)"): "two nested
  [`iterate_while_pure`] folds over **step-count predicates** (`c.k <= op.order - 1`
  inner, `s.it <= op.pc_it` outer) — the `iterate_while_pure_L3` tail-recursion
  lowering image". Register source.
- `book/src/L4/iterate-while.md:193-195` — `iterate_while_pure_L3 :: α -> (α -> Bool)
  -> (α -> α) -> α` (self-verified: signature on `:193`, "The L3 form for
  `iterate_while_pure` is the textbook tail-recursive loop" on `:190`). Confirms the
  `iterate_while_pure_L3` term named in the refreshes is valid; no new citation
  introduced into the refreshed sentences (the established anchor lives in the
  cycle-016 sibling at `:236-241`).

## Open questions / caveats

- None. The firm L4 signature (`iterate_while_pure` folds with step-count
  predicates) does not contradict any assumption the L3 entry made — the L3 entry
  always described its loops as the tail-recursion image of the L4 folds; only the
  fold's NAME was stale (`forM_`/`foldM` → `iterate_while_pure`). No abstractor
  reread needed.
- Closes OQ `l3-chebyshev-sibling-formm-foldm-prose-sweep`.
- The pre-existing OQ for a dedicated thin L4>L3 chebyshev identity-theme
  (referenced at `book/src/L3/chebyshev.md:60-65` and L4 `:434-436`) is untouched by
  this dispatch — out of scope for a pure vocabulary refresh.
