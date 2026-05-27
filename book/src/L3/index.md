# L3 — Global tensor-field operations

L2 algebraic decompositions re-expressed as global tensor-field / convolution-over-space operations: whole-tensor ops, no element loops. The **iteration rotation** layer.

## Context

Where the L2 algebra admits a global form, L3 captures it. Where no global form exists (Gauss-Seidel-flavored smoothers, certain triangular solves, sequentially-reordered preconditioners), the **obstruction** is recorded as a first-class output — negative L3 results are part of the deliverable.

## Semantics (overlay)

L3 expresses:
- Whole-tensor primitives (matvec, axpy, dot, nrm2 as field operations)
- Field transitions: state evolution over a single algorithmic step expressed as `state' = f(state, params)`
- Convolution-like patterns where applicable (stencil sweeps, restriction/prolongation)
- Sequential obstructions: explicit markers where global form is unavailable, with reason

## Operator dep-map

| Operator | Signature | Dependencies | Lowers to | Status |
|---|---|---|---|---|
| [`krylov-step`](./krylov-step.md) | Form A: `(op, K, s) -> (K', s', outputs)`. Form B: `krylov-step-first :: (op, K, s) -> (K', s', carry, outputs)` + `krylov-step-steady :: (op, K, s, carry) -> (K', s', carry', outputs)`. | L1 primitives (used as L3-native whole-tensor ops): `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`. Concepts: `sequential-obstruction`, `state-stratification`, `derived-view-hoisting`, `variant-absorption`, `first-iteration-unrolling`, `convergence-test`, `solve-monad`, `apply_BA`, `orthogonalization`. L4 lift via `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (identity-in-form on body). | L2 [`krylov-step`](../L2/krylov-step.md) via [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) (identity-in-form on body; surface adjustments consolidate `(K, s)` into `IterState`). | `firm` (harvested cycle-010T215300Z; first firm L3 operator; identity-lowering backfill per CLAUDE.md §Methodology invariants — supersedes cycle-006 "no L3 row needed" verdict) |

## Working Notes

- This layer is the destination of the L2-L1 lowering pipeline output AND the source for L4-L3 lowering verification.
- `concepts/sequential-obstruction.md` is the canonical write-up of when L3 lifts fail.
- **First firm L3 operator landed cycle-010**: `krylov-step` (identity-lowering backfill per CLAUDE.md §Methodology invariants new bullet **Identity-lowerings still require both L levels**, codified cycle-009 meta-phase). The L3 form is value-thread-isomorphic to the L4 body per the L4>L3 typed-wrapper-dissolution theme; the entry exists for layer-coherence reasons — each layer is coherent within itself, and the L3 reader must find `krylov-step` defined in L3 vocabulary. Supersedes cycle-006 audit verdict "no L3 row needed for krylov-step".
- **Cohort growth candidates** (per priority #20 cross-layer-cross-cutter audit, cycle-010+): other operators in the krylov-step chain (`apply_linop`, `dot`, `axpy`, `nrm2`, etc.) may also have identity-in-form rotations between adjacent layers that warrant L3 backfill. Audit deferred to a `cross-layer-cross-cutter`-scoped dispatch surveying the L4/L3/L2/L1 cohorts.
