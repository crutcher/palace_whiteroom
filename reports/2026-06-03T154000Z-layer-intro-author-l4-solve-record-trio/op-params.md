# OpParams

> **Kind: `record`.** This page defines the *data shape* of the L4 `OpParams` record — its fields, their types and meaning, the construction-vs-run-time stratum of each, and the L0 source home it mirrors. The *behaviour* over `OpParams` (how `krylov-step` reads it through closed-over surfaces) lives in the operator chapters that consume it — this page does not restate that algebra.

`OpParams` is the **operator-internal-parameters** stratum of the L4 three-stratum solve typing: the readonly variant-selector + constructed-operator-surface closure that a Krylov-shaped solve captures **once at solve construction** and never re-inspects from the per-step kernel. It is the concrete record realising stratum (2) of [`state-stratification`](./state-stratification.md) — see that page for *why* the three-way split is load-bearing (lifetimes-visible + variant-absorption-mechanically-checkable); this page enumerates the record's fields.

## Record definition

`OpParams` is a `readonly` record, captured at the entry to the solve and fixed across the entire `Mult` call. It carries two kinds of field — **variant selectors** (small scalars/enums that select an algorithm variant) and **constructed-operator surfaces** (closures over the operators and the variant selectors, through which the kernel actually touches the parameters). The field set is **slice-specific**; the schema below is the common Krylov shape (GMRES-complete; CG omits the orthogonalization/restart fields).

```text
OpParams = {
  -- constructed-operator surfaces (the kernel touches OpParams ONLY through these)
  T          : ConstructedOp,        -- the apply surface (apply_BA: preconditioned operator)
  orthog?    : OrthogSurface,        -- present for GMRES/Arnoldi; absent for CG (no-op)
  scalars?   : ScalarSurface,        -- present for Chebyshev (polynomial-recurrence scalars); absent otherwise
  eps        : Convergence,          -- the stopping-predicate surface (build_convergence closure)

  -- variant selectors (closed over by the surfaces above; NOT read by the kernel body)
  pc_side    : PreconditionerSide,   -- LEFT | RIGHT
  gs_orthog  : Orthogonalization,    -- MGS | CGS | CGS2     (GMRES/Arnoldi only)
  flexible   : Bool,                 -- FGMRES vs GMRES (selects whether Krylov.Z is present)
  poly_kind? : PolynomialKind,       -- Chebyshev-4th | Chebyshev-1st  (Chebyshev only)
  restart    : RestartMode,          -- non-restarted | restarted-fixed-dim | restarted-adaptive

  -- termination knobs (close into eps; not read by the kernel body)
  max_dim    : Int,                  -- restart subspace dimension (GMRES only)
  max_it     : Int,
  rel_tol    : Scalar,
  abs_tol    : Scalar
}
```

| Field | Type | Stratum / lifetime | Meaning |
|-------|------|--------------------|---------|
| `T` | `ConstructedOp` | construction-time | The constructed apply surface (`apply_BA`); the only operator the kernel applies per step. Closes over `A`, `B`, `pc_side`. |
| `orthog?` | `OrthogSurface` | construction-time | Orthogonalization closure (closes over `gs_orthog`); present for GMRES/Arnoldi, absent (no-op) for CG. |
| `scalars?` | `ScalarSurface` | construction-time | Polynomial-recurrence scalar surface (closes over `poly_kind`); present for Chebyshev only. |
| `eps` | `Convergence` | construction-time | Stopping-predicate surface; closes over `rel_tol`, `abs_tol`, `max_it`, and the initial residual. See [`convergence-test`](./convergence-test.md). |
| `pc_side` | `PreconditionerSide` | construction-time (variant selector) | Left/right preconditioning; read only by `T`. |
| `gs_orthog` | `Orthogonalization` | construction-time (variant selector) | Gram–Schmidt variant; read only by `orthog?`. |
| `flexible` | `Bool` | construction-time (variant selector) | FGMRES vs GMRES; determines whether `Krylov.Z` is present (see [`krylov`](./krylov.md)). |
| `poly_kind?` | `PolynomialKind` | construction-time (variant selector) | Chebyshev kind; read only by `scalars?`. |
| `restart` | `RestartMode` | construction-time (variant selector) | Restart shape; consumed by the outer `solve_loop`, not the kernel. |
| `max_dim` | `Int` | construction-time (termination knob) | Restart subspace dimension (GMRES). |
| `max_it` | `Int` | construction-time (termination knob) | Iteration limit; closes into `eps`. |
| `rel_tol` / `abs_tol` | `Scalar` | construction-time (termination knob) | Convergence tolerances; close into `eps`. |

**The whole record is construction-time / readonly.** There are no run-time-mutated fields — that is the defining property of the stratum. The `readonly` annotation is the typing invariant that *forbids* the per-step kernel from re-inspecting the variant selectors; variant absorption (see [`variant-absorption`](./variant-absorption.md)) is structural precisely because the kernel can only touch `OpParams` through the closed-over surfaces (`T`, `orthog?`, `scalars?`, `eps`), never through the raw selector fields.

## L0 source home

`OpParams` mirrors the **immutable instance fields** of Palace's `IterativeSolver` class hierarchy (`palace/linalg/iterative.hpp:26-115`) and its `GmresSolver` subclass (`palace/linalg/iterative.hpp:155-217`) — the configuration the solver is set up with before `Mult` runs:

- Termination knobs on the base class: `rel_tol, abs_tol` (`iterative.hpp:42`), `max_it` (`iterative.hpp:45`).
- Operator + preconditioner handles (not owned): `const OperType *A` (`iterative.hpp:49`), `const Solver<OperType> *B` (`iterative.hpp:50`) — closed over by the `T` surface.
- GMRES variant selectors: `max_dim` (`iterative.hpp:180`), `Orthogonalization gs_orthog` (`iterative.hpp:184`), `PreconditionerSide pc_side` (`iterative.hpp:187`).

These are exactly the fields [`state-stratification`](./state-stratification.md) §"Worked example — GMRES" maps to `OpParams` ("instance fields (configuration) ↔ OpParams"). The L0 layout stores them as plain instance fields alongside the run-time workspace and statistics; the L4 `OpParams` record un-mixes the construction-time configuration from the run-time strata (see [`krylov`](./krylov.md) for the ephemeral workspace and [`sim-state`](./sim-state.md) for the solve statistics). The `mutable` keyword on the L0 statistics/workspace fields is itself the L0 signal of the stratum boundary: the non-`mutable` fields above are the `OpParams` stratum.

## Used by

- [`krylov-step`](../L4/krylov-step.md) — the per-step kernel reads `OpParams` only through `op.T`, `op.orthog?`, `op.scalars?`, `op.eps` (`L4/krylov-step.md:37`); it never branches on the raw selector fields.
- [`solve-monad`](./solve-monad.md) — the outer driver closes the constructed-operator surfaces over the `OpParams` selectors at construction.

## See also

- [`state-stratification`](./state-stratification.md) — the three-stratum typing this record's stratum (2) belongs to (do not duplicate; this page is the field schema, that page is the conceptual typing).
- [`sim-state`](./sim-state.md) — stratum (1), the run-time externally-visible record.
- [`krylov`](./krylov.md) — stratum (3), the ephemeral workspace record.
- [`variant-absorption`](./variant-absorption.md) — why the `readonly` typing makes variant absorption structural.
- [`constructed-operators`](./constructed-operators.md) / [`constructed-operator-factory`](./constructed-operator-factory.md) — where the variant selectors are closed over into the `T` / `orthog?` / `scalars?` surfaces.

## Status

`firm` — the field schema is the construction-time stratum of the three-stratum typing, every field is backed by a cited `IterativeSolver`/`GmresSolver` instance-field declaration, and the construction-vs-run-time stratum of each field is the defining readonly property. The record-definition obligation (one home defining the record in itself) is met: this is the cross-cutting home for `OpParams`, referenced by ≥2 consumers (`L4/krylov-step.md`, `concepts/solve-monad.md`, `concepts/state-stratification.md`).
