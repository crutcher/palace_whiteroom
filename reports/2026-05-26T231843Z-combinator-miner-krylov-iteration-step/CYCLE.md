---
agent: combinator-miner
invoked_at: 2026-05-26T23:18:43Z
scope: Pattern proposal — krylov-step (state-update kernel + readout, threaded by an outer iterate_while)
status: integrated
integrated_at: 2026-05-26T23:51:01Z
integration_commit: c3312a6
integration_notes: |
  Applied as-is per repaired META.md (overall_status: ready). Single proposed-change block landed:
  modified book/src/L2/index.md to replace empty dep-map placeholder with markdown table (single row for `krylov-step`, 4-column L1-precedent format post-repair), Working Notes section carries provenance / consumed-by / pattern-instance / dependency-annotation overflow.
  No new chapter file — `krylov-step` is a rough-in awaiting harvester formalization (open question `krylov-step-harvester-deliverables`).
  Routed to `harvester` for formalization. Open questions `krylov-step-layer-placement` (cross-layer-cross-cutter) and `krylov-step-naming-and-borderline-cases` (harvester) promoted.
  Build: cargo make book clean.
skill_uptake:
  - skill: classify-variant-axis
    triggered: true
    decision: artifact_landed
    rationale: Six variant axes enumerated explicitly in `## Proposed combinator` → "Variant axes" subsection (preconditioner side, orthogonalization variant, polynomial-kind, first-iteration-unrolled vs branch-in-body, restart shape, in-place vs out-of-place); each axis tied to its absorption discipline. Skill not invoked by name during authoring but its artifact shape (enumerated, labelled axes) is present.
  - skill: verify-citation-range
    triggered: true
    decision: explained_non_applicable
    rationale: Five pattern-instance citations were range-checked inline by reading each `book/src/spec/slices/<slice>.md` range while drafting; skill invocation deferred to critic-phase per the same convention used by the pilot-1 axpy harvester report.
---

# REPORT: Combinator candidate — `krylov-step`

## Summary

Five Phase-1 slices (cg, gmres, chebyshev, arnoldi_step, polynomial_recurrence_step) all factor an iterative algorithm into the same two-piece shape: a **pure step kernel** mapping `(OpParams, IterState) -> {state: IterState', readout: StepOutputs}`, and an **outer driver** that folds the kernel with `iterate_while` (or `forM_/foldM`) until a convergence predicate fires. The kernel internally has a fixed primitive sequence — `apply_linop → (optional precondition / orthogonalize / project) → axpy-class iterate update → small scalar update (β / ρ / residual norm)` — shape-invariant across Krylov methods, polynomial smoothers, and Arnoldi-basis extension; variant axes (preconditioner side, orthogonalization variant, polynomial-kind, restart-vs-no-restart) are absorbed at construction time and do not change the kernel's primitive sequence. The pattern is *named* per-slice (`cg_step` / `cg_steady_step`, `pcg_step`, chebyshev `innerStep`, gmres `inner_loop` body, `arnoldi_step`) but no combinator names it as a first-class operator. This proposal adds a rough-in entry at L2 for `krylov-step` so harvester can later formalize it and downstream slices (MINRES, BiCGStab, LOBPCG, time-stepping) can cite-and-reuse rather than re-derive.

## Pattern instances

- **Instance 1 — CG step.** `book/src/spec/slices/cg.md:103-115` (L2 `step(s)`), `cg.md:172-188` (L4 `cg_step`), v0.5 split at `cg.md:393-425` (`cg_first_step`/`cg_steady_step`). Primitive sequence: `apply_linop A → axpy/axpby → dot → derived scalar norm`.
- **Instance 2 — GMRES inner Arnoldi step.** `book/src/spec/slices/gmres.md:459-471` (L4 `inner_loop` body): `apply_BA → orthogonalize → ls_update_column → it++ → convergence test`.
- **Instance 3 — Chebyshev inner-recurrence step.** `book/src/spec/slices/chebyshev.md:354-362` (L4 `innerStep`). Outer driver: `foldM ... [1..order-1]` (chebyshev.md:349-350) wrapped by `forM_ [1..pc_it]` (chebyshev.md:334).
- **Instance 4 — Arnoldi step kernel.** `book/src/spec/slices/arnoldi_step.md:99-105` (L1) and `arnoldi_step.md:285-298` (L4 `arnoldiStep`): `apply_linop T → orthogonalize → nrm2 → scal`.
- **Instance 5 — Polynomial recurrence sites catalog.** `book/src/spec/slices/polynomial_recurrence_step.md:119-160` tabulates three positive instances of the outer-driver-plus-step-kernel shape (Chebyshev-4th, Chebyshev-1st, GMRES-Givens-stream) — the slice's negative verdict is about Palace source not factoring it; the dataflow shape is unified in this slice's own table.

Five instances; well clear of the ≥3 soft bar.

## Proposed combinator

- **Slug**: `krylov-step`
- **Layer**: **L2**.
  - **Not L3.** L3 is the iteration-rotation layer; CG/GMRES/Chebyshev/Arnoldi all carry a sequential obstruction at L3 in the *outer loop*. The kernel body composes L3-native primitives (the L2→L3 rotation on the body is identity-in-form per cg.md:352-362, arnoldi_step.md:185-188). Putting `krylov-step` at L3 would conflate "kernel exists" with "kernel lifts to global tensor field" — distinct claims.
  - **Not L4.** L4 already has `iterate_while`, `solve-monad`, `state-stratification`, `derived-view-hoisting`, `first-iteration-unrolling` — the outer-driver and state-shape vocabulary. The combinator at L2 captures the **primitive-composition** shape consumed by L4's drivers. Each slice already renders an L2 form of its step body and an L4 form wrapping it in `Solve`/`StateT`; the combinator names the L2 layer of that pair.
- **Signature sketch.**

  ```
  type KrylovStep op_params iter_state step_outputs =
    op_params -> iter_state -> { state: iter_state, outputs: step_outputs }
  ```

  Internal body shape:
  ```
  step op s =
    let w     = apply_linop op.T s.<input_field>                                -- or apply_BA
    let s_aux = optionally(precondition / orthogonalize / project)(op, w, s)    -- variant-absorbed
    let s'    = axpy-class updates over s.{x, r, p, ...}                        -- shape-stable
    let scalar' = dot / nrm2 / recurrence-update on small scalar state
    let outputs = derived view (subject to §3.8 demand-pruning)
    { state: s' ⊕ scalar', outputs }
  ```

- **Algebraic intuition.**
  - Composition: `iterate_while` is the canonical composer at L4 (`iterate_while_with_prev` for unrolled forms; `forM_` × `foldM` for fixed-arity nested). `krylov-step` is the kernel of a fold whose carrier is `iter_state` — fold algebra, not categorical product/sum.
  - Identity element: none in general; `α=0` is breakdown, not identity.
  - Commutativity/associativity: not applicable — fixed primitive ordering by data dependency. What *is* invariant under reformulation is the primitive-count signature; reorderings within independent primitive groups (e.g., CGS batched `dot`s before all `axpy`s) are exact-arithmetic equivalent but differ in MPI-collective shape (load-bearing per CLAUDE.md §Optimization tricks).
  - Distributivity: the `output_extras` slot distributes over `iterate_while`'s trajectory — exactly the demand-pruned algebra of `derived-view-hoisting` (cg.md:330-339, chebyshev.md:421-436). The combinator's only non-trivial algebraic law, inherited from L4 §3.8.

- **Variant axes.**
  1. Preconditioner present/absent (CG↔PCG; GMRES via `apply_BA`).
  2. Orthogonalization variant (MGS/CGS/CGS2; arnoldi_step residual axis).
  3. Polynomial-kind (Chebyshev 4th/1st; scalar-coefficient generator plugs into `op_params`).
  4. First-iteration-unrolled vs branch-in-body (cg.md v0.4↔v0.5).
  5. Restart shape (non-restarted vs restarted; restart lives in the outer driver, kernel is restart-agnostic).
  6. In-place vs out-of-place buffer use (arnoldi `w` aliases `V[j+1]`; CG textually out-of-place; transparent-optimization-equivalent per CLAUDE.md scope).

## Proposed changes

````edit:book/src/L2/index.md
# L2 — Algebraic decompositions

The canonical algebraic decomposition: each operation written as composition of base tensor / operator / quadrature primitives, with HPC/SIMD optimization tricks **unfolded back into the base algebras**. The **fusion rotation** layer.

## Context

L2 is the layer where:
- Cache-blocked loops, SIMD intrinsics, manual unrolling are erased — they are below L2's level of abstraction.
- Kernel fusion across multiple algebraic operations is unfolded into composition.
- Packed sparse formats are de-packed to dense/symbolic algebraic operators.
- Batched specialized BLAS calls are written as compositions of base primitives.

**Load-bearing numerical tricks** (non-associative reduction orderings, fast-math, mixed-precision intermediates, deterministic-vs-atomic accumulation) are **preserved as explicit algebraic claims** with the property they buy called out.

## Semantics (overlay)

L2 vocabulary: tensors, linear operators, quadrature rules, basis transformations, primitive operations (axpy, dot, matvec, gemv, trsv, scal, nrm2, …). State threading via explicit value semantics.

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| `krylov-step` | `(op_params, iter_state) → {state: iter_state, outputs: step_outputs}` | `apply_linop`, `axpy`/`axpby`, `dot`, `nrm2`, `orthogonalization`, `apply_BA`, `derived-view-hoisting`, `first-iteration-unrolling`, `variant-absorption` | `rough-in` (proposed-by: combinator-miner:2026-05-26T231843Z) |

## Working Notes

- This is the layer most populated by `combinator-miner` output — patterns recurring across the slice corpus are L2 candidates.
- `krylov-step` is a rough-in awaiting harvester formalization. Pattern is well-attested across five slices; harvester should pin the signature, variant-axis dispatch sites, and the algebraic-laws section (essentially: no internal algebraic laws — kernel of a fold; only law is L4 §3.8 demand-pruning over `output_extras`).
- **`krylov-step` provenance and consumers** (per combinator-miner:2026-05-26T231843Z):
  - **Consumed-by**: L4 `iterate_while` + `solve-monad` (outer driver; `cg.md §L4`, `gmres.md §L4`, `chebyshev.md §L4`, `arnoldi_step.md §L4`).
  - **Pattern instances** (five, well clear of ≥3 soft bar):
    - `spec/slices/cg.md:103-115`, `:172-188`, `:393-425`
    - `spec/slices/gmres.md:459-471`
    - `spec/slices/chebyshev.md:354-362`
    - `spec/slices/arnoldi_step.md:99-105`, `:285-298`
    - `spec/slices/polynomial_recurrence_step.md:119-160` (catalog of three instances)
  - **Dependency annotations** (carried from the original tree-style rough-in):
    - `orthogonalization` — variant axis.
    - `apply_BA` — preconditioner-side variant axis.
    - `derived-view-hoisting` — `output_extras` slot.
    - `first-iteration-unrolling` — orthogonal variant axis.
    - `variant-absorption` — absorption discipline applied to the step.
````

## Supporting evidence

Step-kernel instances:
- `book/src/spec/slices/cg.md:103-115`, `:172-188`, `:228-257`, `:393-425`
- `book/src/spec/slices/gmres.md:459-471`
- `book/src/spec/slices/chebyshev.md:354-362`
- `book/src/spec/slices/arnoldi_step.md:99-105`, `:285-298`
- `book/src/spec/slices/polynomial_recurrence_step.md:119-160`

Outer-driver consumers:
- `book/src/spec/slices/cg.md:208-220`, `:430-446`
- `book/src/spec/slices/gmres.md:430-454`
- `book/src/spec/slices/chebyshev.md:330-353`

Cross-referenced concepts (do not duplicate):
- `book/src/concepts/apply_linop.md`, `axpy.md`, `dot.md`, `nrm2.md`, `scal.md`
- `book/src/concepts/orthogonalization.md`, `apply_BA.md`
- `book/src/concepts/derived-view-hoisting.md`, `first-iteration-unrolling.md`
- `book/src/concepts/solve-monad.md`, `sequential-obstruction.md`
- `book/src/concepts/variant-absorption.md`

Tests:
- `reference/palace/test/unit/test-orthog.cpp:80-170`, `:234-280` — exercises the orthogonalize variant axis.
- Per cg.md:288, gmres.md:128, chebyshev.md:99-100: no direct unit tests on CG/GMRES/Chebyshev step kernels (integration tests only) — recorded coverage gap, not introduced by this rough-in.

## Open questions / caveats

1. **Layer placement may be revisited at L4.** Named step-functions live in L4 prose; the L2 form is the primitive composition. Cross-layer-cross-cutter should examine whether `krylov-step` deserves L2, L4, or both with a lowering edge. My read: L2 captures primitive composition, L4 captures typed wrapping; complementary.
2. **Same-layer-cross-cutter check.** `apply_BA` is a sub-primitive of `krylov-step`, not a substitute; `krylov-step` names the *fold-kernel role* consumed by `iterate_while`. Worth same-layer-cross-cutter scrutiny.
3. **GMRES-Givens-stream as a special case?** polynomial_recurrence_step.md:147-155 frames it as a step-kernel instance, but its primitive sequence is `givens_apply`/`givens_generate` rather than `apply_linop`+`axpy`+`dot`. Strict reading excludes; broad reading includes. Defer to harvester.
4. **Negative-result interaction with `polynomial_recurrence_step`.** That slice answers "Palace does not have a shared `polynomial_recurrence_step` kernel" at the source level. The open question (polynomial_recurrence_step.md:194-196) about a methodology-level concept is answered affirmatively here: `krylov-step` is the methodology-level concept; no single Palace-source citation, but five Palace-spec-corpus citations. Harvester should make the no-source-citation status explicit.
5. **Naming.** "krylov-step" stretches to cover Chebyshev (not strictly Krylov-subspace per Saad 2003); alternatives `iterative-step-kernel`, `fold-step`, `solver-step` all less precise. Harvester may rename.
6. **Methodology compound.** Value compounds across future slices (MINRES, BiCGStab, LOBPCG, time-stepping) — each writes "this is `krylov-step` over `<state>` with `<variant-axes>` and `<output_extras>`" rather than re-derive. Harvester deliverable could include a slice-template.

---

## Parent-session annotation

This CYCLE.md was persisted by the parent session because the combinator-miner subagent's `Write` call was intercepted by the content-pattern filter ("Subagents should return findings as text, not write report files."). Body content above is the combinator-miner's substantive output verbatim. Same finding as the harvester and abstractor reports.
