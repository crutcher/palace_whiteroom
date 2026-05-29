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

L2 vocabulary: tensors, linear operators, quadrature rules, basis transformations, primitive operations (axpy, dot, matvec, gemv, trsv, scal, nrm2, …). State threading via explicit value semantics. Compositions of L1 primitives into method-step shapes are first-class at L2.

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`krylov-step`](./krylov-step.md) | `(op: OpParams, s: IterState) → { state: IterState', outputs: StepOutputs }` | L1: `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`. L2-composition: `apply_BA`, `orthogonalization`. Concepts: `derived-view-hoisting`, `variant-absorption`, `first-iteration-unrolling`, `sequential-obstruction`, `solve-monad`, `state-stratification`, `solver-as-operator`. | `firm` (harvested cycle-005; promoted from rough-in proposed-by combinator-miner:2026-05-26T231843Z) |
| [`chebyshev-iteration`](./chebyshev-iteration.md) | `(op: ChebOp[N], x: Tensor[N], y: Tensor[N], initial_guess: Bool) → Tensor[N]` | L1: `apply_linop`, `axpy`, `axpby`, `scal`. Concepts: `elementwise-product`, `variant-absorption`, `sequential-obstruction`, `first-iteration-unrolling`. L1 sibling: `chebyshev-smoother`. L2 sibling: `krylov-step`. | `firm` (harvested cycle-012; the concrete L2 entry behind `krylov-step` variant-axis 3; test-coverage caveat, firm ratified) |
| [`linear_combination`](./linear_combination.md) | `[(Scalar, Tensor[N])] -> Tensor[N]` (≡ `foldl (\acc (a,t) -> acc + a·t) zeros pairs`) | L1 fixed-arity specializations: `scal` (arity 1), `axpy` (arity 2, coeff 1 fixed), `axpby` (arity 2), `axpbypcz` (arity 3). Concepts: `scalar-promotion` (element-type axis, concept-page-level sibling of this arity-axis unification; inherited with its open upstream dependency — OQ `scalar-promotion-typing-rule`, not yet committed). Sibling fold (do NOT merge): `dot` (reduce-to-scalar inner product). | `firm` (harvested cycle-018; promoted from rough-in proposed-by combinator-miner:2026-05-28T223022Z; constructive prong (b) of OQ blas1-variadic-linear-combination-fold-unification) |
| [`inner_product`](./inner_product.md) | `(x: Tensor[N], y: Tensor[N]) -> Scalar` (≡ `foldl (+) zero (zipWith kernel x y)`); M-weighted member `inner_product_M(x, M, y) = xᴴ M y` (arg-1-conjugated convention, pinned — matches the L1 `dot`/`bilinear-form` leaves; Palace's free-function `Dot(comm,x,y) = yᴴ x` conjugates arg-2, the deliberate L1 re-order — see entry §"Conjugation convention (pinned)"); plain ≡ `M = I` | L1 leaves it fuses up from: `dot` (Hermitian), `tdot` (unconjugated; firm but type-API-surface only — zero Palace call sites), `bilinear-form` (M-weighted member, rough-in). L2-composition for the weighted member: `apply_linop` (M applied to the linear/arg-1 operand). Concepts: `dot` (cross-cutting prose). **Sibling fold (do NOT merge):** `linear_combination` (reduce-to-`Tensor[N]`; folds the term axis, keeps `N`; different homomorphism). Consumer (NOT an instance): `nrm2` / `matrix-weighted-norm` = `√ ∘ inner_product` at `y=x`. | `firm` (harvested cycle-019; promoted from rough-in proposed-by combinator-miner:2026-05-28T231046Z; family-mode characterized combinator-miner:2026-05-29T023000Z; conjugation pinned per OQ inner-product-harvester-formalization-and-conjugation-pinning) |
| [`orthogonalize`](./orthogonalize.md) | `(op: OrthogOp, w: Tensor[N], V: Basis[N, m]) → { residual: Tensor[N], coeffs: Tensor[m] }` | L1 leaf it lifts: `orthogonalize` (firm). L1 primitives the stages compose: `dot` (project), `axpy` (subtract). Concepts: `orthogonalization`, `variant-absorption` (`:131`, residual-axis disclosure), `sequential-obstruction`. Consumers: `krylov-step` (level-(b) `op.orthog`), ROM basis-extension. Sibling fold (constituent, not parent): `inner_product` (rough-in). | `firm` (harvested cycle-019; promoted from stub; the `l2-named-composition-lifts` backlog item / OQ orthogonalize-as-future-L2-firstclass-entry) |

## Working Notes

- This is the layer most populated by `combinator-miner` output — patterns recurring across the slice corpus are L2 candidates.
- `krylov-step` was promoted from rough-in to firm in cycle-005 (harvester invocation 2026-05-27T025354Z). The firm chapter is at [`krylov-step.md`](./krylov-step.md); the rough-in's six variant axes and pattern-instance list survived intact (no axes added, none merged or split). One non-trivial algebraic law was authored (the demand-pruning law over `outputs` extras, inherited from `derived-view-hoisting`); the kernel's non-laws (commutativity, associativity, fold-merge, step-composition, linearity, bit-determinism-across-variants) are catalogued explicitly to prevent decoration drift.
- **Pattern provenance and consumers** (carried from the rough-in; combinator-miner:2026-05-26T231843Z):
  - **Consumed-by**: L4 `iterate_while` + `solve-monad` outer driver (cg.md §L4, gmres.md §L4, `book/src/L4/chebyshev.md` §Semantics (firm cycle-015; absorbed the former chebyshev §L4), arnoldi_step.md §L4).
  - **Pattern instances** (five, well clear of ≥3 soft bar):
    - `spec/slices/cg.md:103-115`, `:172-188`, `:393-425`
    - `spec/slices/gmres.md:459-471`
    - `book/src/L4/chebyshev.md` §Semantics `innerStep` (firm cycle-015; absorbed the former `spec/slices/chebyshev.md:354-362`)
    - `spec/slices/arnoldi_step.md:99-105`, `:285-298`
    - `spec/slices/polynomial_recurrence_step.md:119-160` (catalog of three instances)
- **Cycle-004 obstruction-theme guidance**: the MINRES and BiCGStab L1>L0 themes (`book/src/L1-L0/minres-iteration.md`, `book/src/L1-L0/bicgstab-iteration.md`) sketch five speculative L1 operators (`lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min`, `bicgstab_step`, `omega_update`, `stabilisation_update`). The cycle-005 harvester decision is to **not** promote any to firm L1: each is a *step-body specialisation* of `krylov-step` rather than an orthogonal axis that would simplify `krylov-step`'s L2 semantics. The decision is recorded at `scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md` (proposed for integrator wiring).
- The cycle-005 firm-up did **not** introduce a new L2 entry for `orthogonalize` as a first-class L2 composition, even though `krylov-step` depends on it as a level-(b)-absorbed surface — that remains a candidate for a future harvester invocation. Same for `incremental-least-squares` (GMRES outer driver's small-dense kernel; currently lives as a concept page only).
