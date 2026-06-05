---
agent: layer-intro-author
invoked_at: 2026-06-05T201831Z
scope: cycle-106 D2 — WAVE-3 op-chapter typed-edge migration (solve_family + fold_solve)
status: integrated
integrated_at: 2026-06-05T223000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-106 D2, applied clean. L4/solve_family + L4/fold_solve migrated to typed edges → sim-state rescued, op-params inbound climbed (5 sources); fold_solve→solve_family a deliberate reference contrast-sibling (no liveness). Cleared the residual unresolved_depends_on_targets entry (the 21st, the rest by D5). Build EXIT 0; rank_violations 0. OQs record-TimeState-needs-definition-home + fold_solve-sibling-reference-carries-no-liveness promoted. Pre-existing variant_axes mid-scalar-colon strict-YAML artifact retained verbatim (non-blocking). Non-blocking report-narration AMBIG citecheck (fold_solve.md:161 bare basename) recorded, not an artifact defect."
---

# CYCLE: WAVE-3 op-chapter `uses-record` typing — `L4/solve_family` + `L4/fold_solve`

## Summary

The cycle-106 LEAD §(f) WAVE-3 duty for two of the six internal solve/BC record
pages' reachers. Migrate `book/src/L4/solve_family.md` and `book/src/L4/fold_solve.md`
off their pre-scheme frontmatter (`consumes:` / `lowers_to:` lists) into a typed
graded-stack `edges:` block (`graded-stack-scheme.md` §2/§5/§6), and ADD the
`uses-record` `depends-on` edges that root-reach the internal record pages:

- `L4/solve_family` → `concepts/op-params`, `concepts/sim-state`
- `L4/fold_solve`  → `concepts/op-params`

Both chapters are already `firm` and already root-reachable today
(`solve_family ← electrostatic/magnetostatic`, `fold_solve ← lifecycle/transient` —
confirmed in the baseline `--show-inbound` below), so the `uses-record` edges land
the records immediately. **`concepts/sim-state` is rescued from GC-garbage**: it is a
`[garbage?]` detritus node in the baseline (no inbound `depends-on`) and gains its
first inbound edge from `L4/solve_family` here; `concepts/op-params` gains two new
inbound edges (previously only `feature/transient.L4`).

This is typed-edge migration on already-firm chapters — NOT new operator algebra. No
operator semantics change beyond the §(f) record-edge additions. The migration of the
prose maturity word is `firmness: firm` → `rank: firm` (the §1-table token the linter
reads); the descriptive frontmatter (`layer` / `operator` / `variant_axes`) is
preserved verbatim, and the rich `consumes:` / `lowers_to:` annotations are carried
forward as edge `kind:` documentation comments.

**Well-foundedness:** both chapters are `rank: firm` (3); every `depends-on` target is
`firm` — the `ksp_solve` / `iterate-while` vocabulary caps are firm, the
`op-params` / `sim-state` record pages are `rank: firm` on firm L0 cites, and the
lowering-theme endpoints are `depends-on` per §5. So `rank(u) ≤ rank(v)` holds
firm/firm on every new and migrated `depends-on` edge — zero rank violations.

## Edge-classification rationale (deliberate, per §2)

For each chapter, every dependency is classified `depends-on` (blocking; constrains
rank + carries liveness) vs `reference` (navigational see-also; constrains nothing):

**`solve_family`:**
- `depends-on` — `L4/ksp_solve` (the firm cap the family `map`s over — a genuine
  blocking vocabulary constituent), `L4/iterate-while` (the §3.7 family whose pure-map
  degenerate the combinator IS — blocking), the lowering theme
  `L4-L3/solve-family-map-dissolution` (a lowering edge is `depends-on` on both
  endpoints, §5; `kind: lowers-to`), and the NEW `uses-record` edges to
  `concepts/op-params` + `concepts/sim-state` (the records the signature
  `solve_family :: OpParams -> [Inputs] -> [SimState]` names — `[SimState]` is the
  collected solution family, each element one `ksp_solve` terminal `SimState`).
- `reference` — `concepts/state-stratification`, `concepts/solve-monad`,
  `concepts/derived-view-hoisting`, `concepts/variant-absorption` (concept-narrative
  see-also pointers — the chapter's §Dependencies lists them as "L4 concept
  references", navigational not blocking).

**`fold_solve`:**
- `depends-on` — `L4/iterate-while` (the §3.7 family whose non-degenerate
  carry-threading member the fold IS — blocking), the lowering theme
  `L4-L3/fold-solve-time-step-dissolution` (`kind: lowers-to`), and the NEW
  `uses-record` edge to `concepts/op-params` (the signature
  `fold_solve :: OpParams -> TimeState -> [Time] -> TimeState` names `OpParams`).
- `reference` — `L4/solve_family` (the **contrast-sibling** map — the chapter's
  §Dependencies is explicit: "L4 contrast-sibling (**not consumed**, referenced for the
  map/fold distinction)" — so a `reference`, never `depends-on`),
  `concepts/state-stratification`, `concepts/sequential-obstruction`,
  `concepts/derived-view-hoisting` (concept-narrative see-also pointers).

Note: `fold_solve`'s `TimeState` / `time_step_op` are speculative rough-in
sub-component records named in prose but with **no definition home** (no
`concepts/time-state.md`); per §(f) the WAVE-3 record set for `fold_solve` is
`op-params` only (`TimeState` is not one of the six rescued record pages and has no
page to point at). This is flagged in Open questions, not forced into an edge.

## Proposed changes

```edit:book/src/L4/solve_family.md
[old]:
---
layer: L4
operator: solve_family
firmness: firm
consumes:
  - book/src/L4/ksp_solve.md (the firm outer-driver cap mapped over the family — the per-element solve)
  - book/src/L4/iterate-while.md (the pure-map degenerate of the strawman §3.7 iterate_while family)
  - book/src/concepts/state-stratification.md (op is the shared readonly operator stratum captured once; each element's SimState independent)
lowers_to:
  - book/src/L4-L3/solve-family-map-dissolution.md (the L4>L3 dissolution to the L3 explicit std::vector<Vector>-accumulating outer sweep — the authoritative L3-form home; NO standalone L3/solve_family entry, per the cycle-057 D1 NO-ENTRY warrant: the family loop carries no sequential-obstruction, so the L3 form is fully + concisely expressed by the dissolution theme's §"L3 form (RHS)" — a separate L3 chapter would mirror it)
variant_axes:
  - operator-capture (fixed: this combinator, op captured once / SetOperators hoisted outside the map | per-element: the batch-17 superset map_solve_over_(operator,rhs)_family, op rebuilt per family-element / SetOperators inside the map — driven)
  - family-index-domain (terminal-boundary / surface-current-boundary / frequency — absorbed into [Inputs]; does not shape the combinator)
  - element-type (real / complex — absorbed into OpParams / Inputs as at the ksp_solve cap)
  - collection-shape (pre-sized vector / append — transparent; the trajectory/map result IS the family, indexing is a lowering concern)
---
[new]:
---
layer: L4
operator: solve_family
firmness: firm
rank: firm
edges:
  depends-on:
    - target: L4/ksp_solve
      kind: folds                     # the firm outer-driver cap mapped over the family — the per-element solve
    - target: L4/iterate-while
      kind: folds                     # the pure-map degenerate of the strawman §3.7 iterate_while family
    - target: concepts/op-params
      kind: uses-record               # signature: solve_family :: OpParams -> [Inputs] -> [SimState] — op captured once, readonly
    - target: concepts/sim-state
      kind: uses-record               # [SimState] = collected solution family; each element one ksp_solve terminal SimState
    - target: L4-L3/solve-family-map-dissolution
      kind: lowers-to                 # the L4>L3 dissolution to the L3 explicit std::vector<Vector>-accumulating outer sweep (authoritative L3-form home; NO standalone L3/solve_family entry — cycle-057 D1 NO-ENTRY warrant)
  reference:
    - concepts/state-stratification   # op is the shared readonly operator stratum captured once; each element's SimState independent
    - concepts/solve-monad            # the Solve = StateT SimState Identity effect each per-element ksp_solve discharges
    - concepts/derived-view-hoisting  # the §3.8 demand-pruning governing per-element materialization
    - concepts/variant-absorption     # the operator-capture axis + family-index/element-type absorption
variant_axes:
  - operator-capture (fixed: this combinator, op captured once / SetOperators hoisted outside the map | per-element: the batch-17 superset map_solve_over_(operator,rhs)_family, op rebuilt per family-element / SetOperators inside the map — driven)
  - family-index-domain (terminal-boundary / surface-current-boundary / frequency — absorbed into [Inputs]; does not shape the combinator)
  - element-type (real / complex — absorbed into OpParams / Inputs as at the ksp_solve cap)
  - collection-shape (pre-sized vector / append — transparent; the trajectory/map result IS the family, indexing is a lowering concern)
---
```

```edit:book/src/L4/fold_solve.md
[old]:
---
layer: L4
operator: fold_solve
firmness: firm
consumes:
  - book/src/L4/iterate-while.md (the strawman §3.7 family whose carry-threading non-degenerate form fold_solve IS — the shared parent of solve_family's map + this fold; NO third parent abstraction)
  - book/src/concepts/state-stratification.md (op captured once at TimeOperator construction / readonly; TimeState the persistent per-step-threaded carry stratum)
  - book/src/concepts/sequential-obstruction.md (the fold spine cannot reorder — each step's input is the prior step's output; AND the per-step body is an opaque library step)
lowers_to:
  - book/src/L4-L3/fold-solve-time-step-dissolution.md (the L4>L3 dissolution to the L3 explicit for-loop threading the field-state in place, with the per-step body a role-naming wrapper over the opaque MFEM ODESolver step — authored by cycle-058 D2 abstractor this same cycle; canonical slug fold-solve-time-step-dissolution)
variant_axes:
  - schedule-source (fixed-list: the carry consumes a precomputed [Time] schedule, foldl over a uniform list — transient | state-generated: the carry GENERATES the next input + the loop bound from accumulated state, an error-terminated march — TWO witnesses: driven-PROM SweepAdaptive (greedy frequency-sampling) + the AMR Solve→Estimate→Mark→Refine loop (basesolver.cpp:190, error-indicator-terminated). THE load-bearing axis; the fixed-list form is the default surface, the state-generated form the recorded generalization, now twice-witnessed)
  - per-step-operator (opaque-library: the step bottoms out in a library integrator/sampler the L4 entry quantifies over — MFEM ODESolver for transient, RomOperator greedy sampler for SweepAdaptive; absorbed into the op : OpParams stratum)
  - carry-shape (single field-state TimeState — transient | field-state + growing reduced basis + error history — SweepAdaptive; absorbed into the carry type, does not shape the spine)
  - element-type (real — transient | complex — driven-PROM; absorbed into OpParams / the carry, as at the ksp_solve cap)
---
[new]:
---
layer: L4
operator: fold_solve
firmness: firm
rank: firm
edges:
  depends-on:
    - target: L4/iterate-while
      kind: folds                     # the strawman §3.7 family whose carry-threading non-degenerate form fold_solve IS — the shared parent of solve_family's map + this fold; NO third parent abstraction
    - target: concepts/op-params
      kind: uses-record               # signature: fold_solve :: OpParams -> TimeState -> [Time] -> TimeState — op captured once at TimeOperator construction, readonly
    - target: L4-L3/fold-solve-time-step-dissolution
      kind: lowers-to                 # the L4>L3 dissolution to the L3 explicit for-loop threading the field-state in place, the per-step body a role-naming wrapper over the opaque MFEM ODESolver step (canonical slug fold-solve-time-step-dissolution)
  reference:
    - L4/solve_family                 # the independent-MAP contrast-sibling (NOT consumed; referenced for the map/fold distinction)
    - concepts/state-stratification   # op captured once at TimeOperator construction / readonly; TimeState the persistent per-step-threaded carry stratum
    - concepts/sequential-obstruction # the fold spine cannot reorder — each step's input is the prior step's output; AND the per-step body is an opaque library step
    - concepts/derived-view-hoisting  # the §3.8 demand-pruning governing whether the intermediate-state trajectory materializes
variant_axes:
  - schedule-source (fixed-list: the carry consumes a precomputed [Time] schedule, foldl over a uniform list — transient | state-generated: the carry GENERATES the next input + the loop bound from accumulated state, an error-terminated march — TWO witnesses: driven-PROM SweepAdaptive (greedy frequency-sampling) + the AMR Solve→Estimate→Mark→Refine loop (basesolver.cpp:190, error-indicator-terminated). THE load-bearing axis; the fixed-list form is the default surface, the state-generated form the recorded generalization, now twice-witnessed)
  - per-step-operator (opaque-library: the step bottoms out in a library integrator/sampler the L4 entry quantifies over — MFEM ODESolver for transient, RomOperator greedy sampler for SweepAdaptive; absorbed into the op : OpParams stratum)
  - carry-shape (single field-state TimeState — transient | field-state + growing reduced basis + error history — SweepAdaptive; absorbed into the carry type, does not shape the spine)
  - element-type (real — transient | complex — driven-PROM; absorbed into OpParams / the carry, as at the ksp_solve cap)
---
```

## Supporting evidence

### Scheme conformance (per `graded-stack-scheme.md` §2/§5/§6)

- **`rank:` token (§1).** Both chapters carry on-disk `firmness: firm` and a prose
  `## Status` line reading `firm` (`solve_family.md:142`, `fold_solve.md:161`). Mapped
  via the §1 table to `rank: firm` (numeric 3). The `firmness:` line is preserved
  (human-facing label) alongside the new linter-read `rank:` token (§6 step 1).
- **`edges:` block (§2).** Both use the **block-mapping edge form**
  (`- target: …` / `  kind: …`) so the batch-33 linter GC-traverses the `uses-record`
  edges (§(f)). Targets are repo-relative slugs without `book/src/` prefix or `.md`
  suffix (§2). The `kind:` annotations are documentation the linters ignore.
- **Lowering edge (§5).** The `lowers_to:` theme becomes a `depends-on` with
  `kind: lowers-to` on the source endpoint — the lowering edge is `depends-on` on both
  endpoints; the theme page already lists the L4 source as its own `depends-on`
  (confirmed in baseline `--show-inbound`:
  `L4-L3/solve-family-map-dissolution <- L4/solve_family`,
  `L4-L3/fold-solve-time-step-dissolution <- L4/fold_solve`).
- **No feature-root edge.** Neither chapter links to a feature column as a dependency,
  so no `reference`-to-root reclassification is needed here.

### Baseline `--show-inbound` (BEFORE edits)

```
  concepts/op-params  <-  feature/transient.L4
    [garbage?] concepts/sim-state
```

`concepts/op-params` has a single inbound edge; `concepts/sim-state` is a `[garbage?]`
detritus node (no inbound `depends-on`). Both chapters are themselves already
root-reachable (from the baseline run):

```
  L4/solve_family  <-  L4-L3/solve-family-map-dissolution, L4/gram_reduce, feature/electrostatic.L4, feature/magnetostatic.L4
  L4/fold_solve    <-  L3/fold_solve, feature/lifecycle.L1, feature/lifecycle.L4, feature/transient.L1, feature/transient.L4
```

So the `uses-record` edges land the two records on a live path immediately
(column → composes → op → uses-record → record).

### Expected `--show-inbound` AFTER edits (integrator-verifiable)

```
  concepts/op-params  <-  L4/fold_solve, L4/solve_family, feature/transient.L4
  concepts/sim-state  <-  L4/solve_family
```

`concepts/sim-state` is rescued from `[garbage?]` (gains its first inbound edge);
`concepts/op-params` gains two new inbound edges. Baseline overall result
`0 rank violation(s) / 163 detritus / 77 untyped` should move to **0 rank violations
HELD** (both edges firm/firm), detritus −1 (sim-state rescued; op-params was already
non-detritus), and untyped unchanged (these two chapters carried pre-scheme
`consumes:`/`lowers_to:` frontmatter — they were not in the "no frontmatter" untyped
set, so the count of `77 untyped` is governed by the OTHER WAVE-3 chapters / record
reachers, not these two). The other four WAVE-3 record reachers
(`ksp_solve` → sim-state, `krylov-step` → 6 records, `eliminate_bc` → dofset) are the
co-dispatched D1/D3 scope, not this report's.

## Open questions / caveats

- **`record-TimeState-needs-definition-home`** (re-surfaced; §(f) / record-definition
  obligation). `fold_solve`'s signature names `TimeState` (the persistent field-state
  carry — the `(E, B)` bundle) and the prose names `time_step_op` as a speculative
  rough-in sub-component, but there is **no `concepts/time-state.md` definition home** —
  `TimeState` is defined only by how the fold threads it. It is named by `fold_solve`
  alone among firm chapters today (single-consumer → an in-chapter `## Record
  definition` section would be the home, not a standalone page), but if a transient
  feature-column or a future per-step consumer also names it the ≥2-consumer bar trips
  and it needs a `concepts/time-state.md` page. Flagged so the WAVE-3 record set is not
  silently read as complete — `TimeState` is NOT one of the six rescued record pages
  and has no page to `uses-record`-edge to. (Not blocking this migration; the
  `op-params` edge is the only WAVE-3 record edge `fold_solve` carries.)
- **`fold_solve` sibling-`reference` to `solve_family`.** Classified `reference` (not
  `depends-on`) because the chapter's §Dependencies is explicit that `solve_family` is
  the contrast-sibling "not consumed, referenced for the map/fold distinction". This is
  the correct deliberate classification (a `depends-on` here would wrongly couple the
  two combinators' ranks), but note it means the map/fold sibling relationship carries
  no liveness — which is fine (both are independently root-reachable).
- Did not touch the prose bodies of either chapter (no operator-algebra change). The
  rich `consumes:`/`lowers_to:` descriptive text is preserved as edge `kind:` /
  trailing-comment documentation; nothing semantic was dropped.
