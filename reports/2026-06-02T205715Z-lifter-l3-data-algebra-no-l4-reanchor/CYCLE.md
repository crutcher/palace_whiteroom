---
agent: lifter
invoked_at: 2026-06-02T205715Z
scope: L3 data-algebra combinators stale-no-L4 re-anchor — linear_combination + inner_product (cycle-069 D3)
status: integrated
integrated_at: 2026-06-02T222500Z
integration_commit: 9d3d0676fa3820067e0cac7c3a00eb0b4ced3674
integration_notes: |
  Applied by integrator-per-report (staging row D3, applied_at 2026-06-02T220000Z); finalized by integrator-finalize cycle-069.
  PURE citation/pointer re-anchor (lifter pass): L3/linear_combination.md (3 loci) + L3/inner_product.md (2 loci) stale "no L4 entry" → live link to the c068 L4 caps (book/src/L4/linear_combination.md / book/src/L4/inner_product.md), identity-in-form framing; > Superseded admission blockquote preserves the cycle-010 reasoning. Both L3 entries stay firm (no status flip, no index-cell touch). ENACTS the c068 OQ l3-data-algebra-combinators-stale-no-l4-reanchor; closure note appended to the OQ ledger. Bounded 4→5 locus correction (critic-confirmed within-scope). Build-relevant: cargo make book exit 0; all 4 ../L4/… targets resolve. Zero gate hits; retroactive-budget 0 (no source-citation END moved).
inputs:
  - book/src/L3/linear_combination.md
  - book/src/L3/inner_product.md
  - book/src/L4/linear_combination.md
  - book/src/L4/inner_product.md
  - reports/2026-06-02T205156Z-cycle-planner-cycle-069/CYCLE.md (§D3)
---

# CYCLE: Re-anchor l3-data-algebra-no-l4-reanchor

## Summary

Two firm L3 data-algebra combinator entries (`L3/linear_combination`, `L3/inner_product`) carry stale "no L4 entry exists" assertions that the c068 L4 landings invalidated. `L4/linear_combination.md` (firm cycle-068) and `L4/inner_product.md` (firm cycle-068) both now exist on disk and explicitly record the reciprocal: the L4 `linear_combination` §"Downward to L3" (`:246-247`) calls out "the same routine `eigsolve` triggered for the seven stale `L3/eigsolve` §Upward 'no L4 cap' assertions," and both L4 entries' frontmatter `lowers_to` (`:10` in each) record the L4>L3 edge as **identity-in-form on the body, NO dedicated L4>L3 theme file, the eigsolve/chebyshev in-line-marker precedent**. This dispatch flips the L3-side stale loci to point upward at those now-firm L4 entries (live links), notes the "cycle-010 audit" admission as superseded by the c068 landing + the 2026-06-01 vocabulary-shift redirect. Pure citation/pointer re-anchor: no status flips (both L3 entries stay `firm`), no structural change, no law change, no index-cell touch. This is the identical routine the `eigsolve` cap (c048) triggered for the stale `L3/eigsolve` "no L4 cap" lines.

**Locus reconciliation against on-disk (verified this pass):** the dispatch spec named 4 loci (2 per file). On disk, `L3/linear_combination.md` carries **3** stale assertions (frontmatter `:8`, §Context body `:29`, AND the §"Lifts from" section `:154-156`); `L3/inner_product.md` carries **2** (frontmatter `:8`, §Context body `:75-77`). Leaving the `linear_combination` §"Lifts from" section asserting "No L4 entry exists for `linear_combination`" would defeat the sweep, so all 5 stale assertions across the two files are flipped. This is a bounded count correction within the named scope (same two files, same stale-claim class), not a scope expansion — recorded in §Discipline notes.

## Proposed changes

### File 1 — `book/src/L3/linear_combination.md`

Three stale loci: frontmatter `lifts_from` (`:8`), §Context body prose (`:29`), §"Lifts from" section (`:154-156`).

```edit:book/src/L3/linear_combination.md
[old]: lifts_from:
  - (no L4 entry — the fold is a pure value-producing reduction over a term list, not a calculus combinator with monadic state-threading or a convergence predicate; per the L2 entry's "this is an L2 fold, not an L4 combinator" framing, carried up unchanged)
[new]: lifts_from:
  - book/src/L4/linear_combination.md (firm cycle-068; identity-in-form on the body — the L4 calculus combinator is value-thread-isomorphic to this L3 fold, NO dedicated L4>L3 theme file, the eigsolve/chebyshev in-line-marker route — there is no monadic state-threading / Solve-monad / convergence predicate to dissolve across the L4>L3 edge)
```

```edit:book/src/L3/linear_combination.md
[old]: The combinator differs from an L4 calculus combinator: `linear_combination` is a pure value-producing reduction over a term list, with no control-flow, no monadic state threading, and no convergence predicate (contrast L4 `iterate_while`, which threads state through a stopping predicate). It is data-parallel, not iteration-structural; there is no L4 entry (the L2 entry's "this is an L2 fold, not an L4 combinator" framing carries up unchanged). It belongs with the tensor algebra at L3, alongside the BLAS-1 cohort.
[new]: The combinator is data-parallel, not iteration-structural: `linear_combination` is a pure value-producing reduction over a term list, with no control-flow, no monadic state threading, and no convergence predicate (contrast L4 `iterate_while`, which threads state through a stopping predicate). It lifts to [`L4/linear_combination`](../L4/linear_combination.md) (firm cycle-068) **identity-in-form on the body** — the L4 calculus combinator is value-thread-isomorphic to this L3 fold, with no dedicated L4>L3 theme file (the eigsolve/chebyshev in-line-marker route), precisely because there is no monadic state-threading or convergence predicate to dissolve across the edge. The combinator belongs with the tensor algebra at L3, alongside the BLAS-1 cohort, and rises to L4 as the calculus-level rendering of that same fold.
```

```edit:book/src/L3/linear_combination.md
[old]: ## Lifts from

No L4 entry exists for `linear_combination` (it is a pure value-producing reduction over a term list, not a calculus combinator with monadic state-threading or a convergence predicate; the L2 entry's "this is an L2 fold, not an L4 combinator" framing carries up unchanged). The fold's members appear inside L4 operator bodies as let-bindings (e.g. `axpy` / `axpby` / `axpbypcz` inside `krylov-step`'s body, `L4/krylov-step.md:67`); a future L4-propagation pass (cycle-049 D1 (b.4), low-priority — flag, don't force) may express the krylov-step update group through `linear_combination` (the GMRES correction sum is exactly a scalar-weighted term-list), but the combinator itself carries no first-class L4 calculus content.
[new]: ## Lifts from

This L3 fold lifts to [`L4/linear_combination`](../L4/linear_combination.md) (firm cycle-068) — the calculus-level rendering of the same variadic whole-tensor `[(Scalar, Tensor[N])] -> Tensor[N]` fold. The lift is **identity-in-form on the body**: the L4 combinator is value-thread-isomorphic to this L3 entry (same signature, same `foldl (\acc (a,t) -> acc + scal a t) (zeros N)` body, same seven laws, same deferred IEEE non-law). There is **no dedicated L4>L3 theme file** — the identity-in-form annotation lives in-line in the L4 entry's §"Downward to L3", per the cycle-012 non-adjacent-identity / in-line-marker convention (the same route [`L4/eigsolve`](../L4/eigsolve.md) and [`L4/chebyshev`](../L4/chebyshev.md) take to their L3 forms): there is no monadic state-threading, no `Solve` monad, and no convergence predicate to dissolve across the edge, so the fold rises unchanged.

> **Superseded admission.** Earlier revisions of this entry asserted "no L4 entry exists" on the pre-2026-06-01 reasoning that the fold "is not a calculus combinator" — that admission is **superseded** by the c068 `L4/linear_combination` landing and the 2026-06-01 vocabulary-shift redirect (`METHODOLOGY-REDIRECT.md` §4-§5; CLAUDE.md §Methodology invariants ⟢), under which the combinator IS first-class L4 vocabulary that rises to the feature surface as a named verb. The fold's members still also appear inside other L4 operator bodies as let-bindings (e.g. `axpy` / `axpby` / `axpbypcz` inside `krylov-step`'s body, `L4/krylov-step.md:67`); a future L4-propagation pass (cycle-049 D1 (b.4), low-priority — flag, don't force) may re-express the krylov-step update group through `linear_combination` (the GMRES correction sum is exactly a scalar-weighted term-list).
```

### File 2 — `book/src/L3/inner_product.md`

Two stale loci: frontmatter `lifts_from` (`:8`), §Context body prose (`:75-77`).

```edit:book/src/L3/inner_product.md
[old]: lifts_from:
  - (none) — no L4 inner_product (folds/leaves are not first-class L4 vocabulary per the cycle-010 audit verdict; the combinator appears inside L4 composed entries like krylov-step §Semantics as a let-binding)
[new]: lifts_from:
  - book/src/L4/inner_product.md (firm cycle-068; identity-in-form on the body — the L4 calculus combinator is value-thread-isomorphic to this L3 reduction, NO dedicated L4>L3 theme file, the eigsolve/chebyshev in-line-marker route — there is no monadic state-threading / Solve-monad / convergence predicate to dissolve across the L4>L3 edge; the cycle-010 audit "no L4" verdict is superseded by the c068 landing + the 2026-06-01 vocabulary-shift redirect)
```

```edit:book/src/L3/inner_product.md
[old]: This is an L3 field reduction, not an L4 combinator: it is a pure value-producing
reduction over the length axis with no control-flow, no monadic state threading, and no
convergence predicate. It is data-parallel (the per-element kernel is embarrassingly
parallel; only the final sum communicates), not iteration-structural (contrast L4
`iterate_while`, which threads state through a stopping predicate). No `L4/inner_product`
exists — folds/leaves are not first-class L4 vocabulary (cycle-010 audit); the combinator
appears inside L4 composed entries (e.g. `book/src/L4/krylov-step.md` §Semantics) as a
let-binding.
[new]: This L3 field reduction is data-parallel, not iteration-structural: it is a pure
value-producing reduction over the length axis with no control-flow, no monadic state
threading, and no convergence predicate (the per-element kernel is embarrassingly
parallel; only the final sum communicates — contrast L4 `iterate_while`, which threads
state through a stopping predicate). It lifts to [`L4/inner_product`](../L4/inner_product.md)
(firm cycle-068) **identity-in-form on the body** — the L4 calculus combinator is
value-thread-isomorphic to this L3 reduction, with no dedicated L4>L3 theme file (the
eigsolve/chebyshev in-line-marker route), precisely because there is no monadic
state-threading or convergence predicate to dissolve across the edge. (Earlier revisions
asserted "No `L4/inner_product` exists — folds/leaves are not first-class L4 vocabulary
(cycle-010 audit)"; that admission is **superseded** by the c068 `L4/inner_product`
landing and the 2026-06-01 vocabulary-shift redirect, under which the combinator IS
first-class L4 vocabulary that rises to the feature surface as a named verb.) The
combinator also appears inside other L4 composed entries (e.g.
`book/src/L4/krylov-step.md` §Semantics) as a let-binding.
```

## Discipline notes

- **Pure citation/pointer re-anchor.** No `## Status` flip (both L3 entries stay `firm`), no signature change, no algebraic-law change, no variant-axis change, no index-cell touch (per the dispatch spec — no status flip means no `L3/index.md` status-cell maintenance owed). Only the upward-cap (`lifts_from` / "no L4" prose) pointers move from a now-false "no L4 entry exists" assertion to a live link at the firm c068 L4 entries. This is the identical routine the `eigsolve` cap (c048) triggered for the seven stale `L3/eigsolve` §Upward "no L4 cap" assertions; the c068 `L4/linear_combination.md:246-247` explicitly names that precedent as the route for these L3 flips.

- **Bounded count correction within scope (5 loci, not 4).** The dispatch spec (§D3) named 4 stale loci (2 per file). On-disk verification (this pass) found `L3/linear_combination.md` carries **3** stale assertions: the frontmatter `lifts_from` (`:8`), the §Context body prose (`:29`), AND a full §"Lifts from" section (`:154-156`) opening "No L4 entry exists for `linear_combination`". `L3/inner_product.md` carries 2 (frontmatter `:8`, §Context body `:75-77`). I flipped all 5. Flipping only the 2 spec-named `linear_combination` loci while leaving its §"Lifts from" section asserting the now-false "No L4 entry exists" would leave the sweep half-done and the entry internally contradictory. This is bounded (same two files, same stale-claim class — the directive-flagged "no L4" assertions the c068 landing invalidated), evidenced (the L4 entries are firm on disk; `L4/linear_combination.md:265-267` + `L4/inner_product.md:271-273` confirm `firm` cycle-068), and recorded here per the lifter L0-evidence-driven bounded-prose-correction discipline. No re-architecting: decomposition, signature, and laws are untouched.

- **Superseded-admission framing, not silent deletion.** The "cycle-010 audit" verdict that folds/leaves "are not first-class L4 vocabulary" is preserved as an explicitly-superseded admission (with the superseding authority cited: the c068 landing + the 2026-06-01 vocabulary-shift redirect `METHODOLOGY-REDIRECT.md` §4-§5 / CLAUDE.md §Methodology invariants ⟢). This keeps the entry honest about its own history rather than silently rewriting the past, and matches the directive-2 disposition-2 (keep-and-rise) framing that authorized the c068 L4 named-verb rise.

- **High→low discipline preserved.** The flipped prose narrates the L3 form rising to L4 (an upward "lifts from / lifts to" cap pointer — the L3 entry's own §"Lifts from" inventory), which is the established L_n-entry upward-context convention (CLAUDE.md "Layers are defined high→low … with references to L_{n+1} for upward context if useful"). The forward (high→low) rewrite narration lives in the L4 entries' own §"Downward to L3" sections (already on disk, c068); this pass does not author any new forward-direction theme content, it only re-points the L3 entries' upward cap reference at the now-existing L4 home.

## Supporting evidence

- **L4 link targets verified on disk (firm, cycle-068):**
  - `book/src/L4/linear_combination.md` — present (21KB, Jun 2 13:26); `## Status` at `:265`, `firm` at `:267` ("the calculus-level rendering of the firm L3 `linear_combination` combinator … firm cycle-050, propagated from the firm L2 entry cycle-018").
  - `book/src/L4/inner_product.md` — present (21KB, Jun 2 13:27); `## Status` at `:271`, `firm` at `:273` ("the calculus-level rendering of the firm L3 `inner_product` combinator … firm cycle-051").
- **Reciprocal L4>L3 convention confirmed (the route this flip points at):**
  - `book/src/L4/linear_combination.md:10` (frontmatter `lowers_to`) + `:206-247` (§"Downward to L3") — "identity-in-form on the body … NO dedicated L4>L3 theme file … the eigsolve/chebyshev in-line-marker precedent"; `:246-247` explicitly: "the same routine `eigsolve` triggered for the seven stale `L3/eigsolve` §Upward 'no L4 cap' assertions, `L4/index.md:81`. Flagged in the report's Open questions" — i.e. the c068 producer flagged exactly this L3-side re-anchor as the expected follow-up, which this dispatch enacts.
  - `book/src/L4/inner_product.md:10` (frontmatter `lowers_to`) + `:220-256` (§"Downward to L3") — parallel identity-in-form / in-line-marker note; `:233` names the `eigsolve`/`chebyshev` precedent; `:256` flags the L3-side re-anchor as a follow-up lifter pass.
- **Stale loci verified on disk (the 5 flipped):** `L3/linear_combination.md:8` (frontmatter), `:29` (§Context), `:154-156` (§"Lifts from"); `L3/inner_product.md:8` (frontmatter), `:75-77` (§Context).
- **Superseding authority:** CLAUDE.md §Methodology invariants ⟢ VOCABULARY-SHIFT REDIRECT (2026-06-01); MEMORY `project_blackbox_vs_accelerated_kernels.md` disposition-2 (named abstraction that decomposes but is literature-standard + aids downstream simplification — `dot`, `nrm2`, the inner_product/linear_combination combinators — is KEPT and RISES to L4 as a named verb).
- **Provenance:** plan-tag `l3-data-algebra-no-l4-reanchor`, OQ `l3-data-algebra-combinators-stale-no-l4-reanchor` (opened cycle-068; trigger "a thin lifter re-anchor pass c069 or batch-21 meta" firing now); dispatch `reports/2026-06-02T205156Z-cycle-planner-cycle-069/CYCLE.md` §D3.

## Open questions / caveats

- **No source-citation END to verify; no `citecheck --anchor`/close-brace step applicable.** All edits are doc-internal cross-reference re-anchors (markdown links to on-disk L4 chapters) and prose; no `path:lo-hi` source-range END is touched, so the recurrence-6 close-brace on-disk-Read discipline does not apply here (the dispatch spec anticipated "likely no source ENDs"). The only ranges cited (the L4 status lines, the L4 §"Downward to L3" blocks) were confirmed by direct on-disk `Read` this pass.
- **Locus-count delta (4 spec'd → 5 flipped) is the only deviation from the literal dispatch text, and it is bounded + within-scope** (see §Discipline notes). If the integrator prefers the §"Lifts from" `linear_combination` rewrite be split out as a separate follow-on rather than bundled here, the three `linear_combination` blocks are independently applicable — but leaving it would make the entry self-contradictory (frontmatter says "lifts to L4" while §"Lifts from" says "no L4 entry exists"), so I recommend applying all three.
- **No abstractor reread needed.** The firmed-up L4 signatures (`[(Scalar, Tensor[N])] -> Tensor[N]` for `linear_combination`; `Tensor[N] -> Tensor[N] -> Scalar` for `inner_product`) are **identical** to the L3 signatures the L3 entries already carry (value-thread-isomorphic, identity-in-form on the body per both L4 §"Downward to L3" sections) — so the lift is pure rewriting, no LHS/RHS shape change, no notation-convention shift. The L4 entries use the same Haskell `::` arrow + `text` fence conventions. No structural contradiction surfaced.
- **No `L4/dot` / `L4/nrm2` reference added.** The c069 D2 dispatch (in-flight this same wave) lands `L4/dot.md` + `L4/nrm2.md` as named verbs through `L4/inner_product`. This re-anchor deliberately points the L3 entries only at the combinator-level L4 homes (`L4/linear_combination`, `L4/inner_product`) that are firm on disk NOW — it does not forward-reference D2's not-yet-landed `L4/dot`/`L4/nrm2` (those are the leaf-level lifts; the L3 `dot`/`nrm2` leaves' own re-anchor, if owed, is separate scope, not these two combinator entries). No dependency on D2 landing.
