---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/linalg/iterative.hpp:26-115
      kind: cites-evidence            # IterativeSolver base: mutable converged/initial_res,final_res/final_it (:52-54); accessor surface (:97-108)
    - target: palace/linalg/iterative.hpp:140-150
      kind: cites-evidence            # CgSolver::Mult iterate output arg `x` (:149)
    - target: palace/linalg/iterative.hpp:214-217
      kind: cites-evidence            # GmresSolver::Mult iterate output arg `x` (:216)
  reference:
    - L4/krylov_step
    - concepts/solve-monad
    - concepts/state-stratification
    - concepts/convergence-test
    - concepts/OpParams
    - concepts/krylov
---

# SimState

> **Kind: `record`.** This page defines the *data shape* of the L4 `SimState` record — its fields, their types and meaning, the construction-vs-run-time stratum of each, and the L0 source home it mirrors. The *behaviour* over `SimState` (how `krylov_step` threads it through the `Solve` monad) lives in the operator chapters that consume it — this page does not restate that algebra.

`SimState` is the **SimState** stratum of the L4 three-stratum solve typing: the externally-visible quantities a Krylov-shaped solve evolves and reports, threaded by the `Solve` state monad and returned to the caller. It is the concrete record realising stratum (1) of [`state-stratification`](./state-stratification.md) — see that page for *why* the three-way split is load-bearing; this page enumerates the record's fields.

## Record definition

`SimState` is the value threaded by `Solve a = StateT SimState Identity a` (see [`solve-monad`](./solve-monad.md)). It is `readonly` from the *caller's* perspective (the solve produces a new `SimState` value rather than mutating in place), but its fields are **run-time-evolved** within the solve — the defining property that distinguishes it from the construction-time [`OpParams`](./OpParams.md).

The iterate `x` is the solution-space vector, named with the shape group `S` per [`l4_calculus`](../semantics/index.md) §1.2.1 (not a rank-1 length axis):

```text
SimState = {
  x           : Tensor[(S: ...)],   -- the current iterate (the solve's primary product)
  it          : Int,         -- iteration count
  converged   : Bool,        -- convergence flag
  final_res   : Scalar,      -- final (absolute) residual, possibly an estimate
  initial_res : Scalar       -- initial (absolute) residual, captured at solve entry
}
```

| Field | Type | Stratum / lifetime | Meaning |
|-------|------|--------------------|---------|
| `x` | `Tensor[$S]` | run-time, persists across the `Mult` call | The current iterate; the solve's primary product. Updated at restart-cycle boundaries (folding the correction `K.V · K.y`), **not** per step — see [`krylov_step`](../L4/krylov_step.md). |
| `it` | `Int` | run-time, persists across the `Mult` call | Iteration counter; the per-step `modify (\s -> s { it = s.it + 1 })` is typically the kernel's *sole* monadic effect. |
| `converged` | `Bool` | run-time, written at solve exit | Convergence flag; set by the convergence test, read by the caller. |
| `final_res` | `Scalar` | run-time, written at solve exit | Final absolute residual (may be an estimate of the true residual, not a recomputed one). |
| `initial_res` | `Scalar` | run-time, captured at solve entry | Initial absolute residual; closed into the [`convergence-test`](./convergence-test.md) surface as the relative-tolerance baseline. |

**Every field is run-time.** `SimState` carries no construction-time configuration — the configuration lives in [`OpParams`](./OpParams.md), and the per-restart workspace lives in [`krylov`](./krylov.md). The schema is **uniform across slices** (CG, GMRES, FGMRES, Chebyshev all use this exact five-field shape) — unlike `OpParams`/`Krylov`, `SimState` is **not** slice-specific. This uniformity is what lets the `Solve` monad's effect domain be exactly `SimState`: the monadic coordination does not vary by algorithm.

A common stratification mistake (per [`state-stratification`](./state-stratification.md) §"Common stratification mistakes") is putting ephemeral workspace into `SimState` because L0 stored it as an instance field; the L4 typing keeps `SimState` to exactly the caller-observable five fields.

## L0 source home

`SimState` mirrors the **`mutable` solve-statistics fields** of Palace's `IterativeSolver` base class (`palace/linalg/iterative.hpp:26-115`) plus the iterate vector `x` passed by reference to `Mult`:

- `mutable bool converged` (`iterative.hpp:53`) ↔ `SimState.converged`.
- `mutable double initial_res, final_res` (`iterative.hpp:54`) ↔ `SimState.initial_res`, `SimState.final_res`.
- `mutable int final_it` (`iterative.hpp:55`) ↔ `SimState.it`.
- The iterate `x` is the output argument of `void Mult(const VecType &b, VecType &x) const` (`CgSolver::Mult` declared at `iterative.hpp:149`; `GmresSolver::Mult` at `iterative.hpp:216`) — written in place at L0, returned as a fresh `SimState.x` value at L4.

The accessor surface confirms these five are exactly the externally-observable quantities: `GetConverged()`, `GetInitialRes()`, `GetFinalRes()`, `GetNumIterations()` (`iterative.hpp:97-108`) expose precisely `converged`, `initial_res`, `final_res`, `final_it` — the L0 read-side of the `SimState` record. The L0 `mutable` keyword marks these as written-during-`const`-`Mult` (i.e. run-time-evolved), which is exactly the stratum boundary: `mutable` statistics ↔ `SimState`; non-`mutable` configuration ↔ [`OpParams`](./OpParams.md); lazy `Initialize`/`Update` workspace ↔ [`krylov`](./krylov.md). This is the mapping [`state-stratification`](./state-stratification.md) §"Worked example — GMRES" records ("the externally-observable `final_res` / `converged` flags ↔ SimState").

## Used by

- [`krylov_step`](../L4/krylov_step.md) — the kernel's monadic effect *is* the `SimState` transition (`L4/krylov_step.md:39`); the per-step effect is the `it` increment, the `x` update is the restart-boundary operation.
- [`solve-monad`](./solve-monad.md) — `Solve a = StateT SimState Identity a`; `SimState` is the monad's state type.
- [`convergence-test`](./convergence-test.md) — reads `initial_res` (baseline) and writes `converged` / `final_res`.

## See also

- [`state-stratification`](./state-stratification.md) — the three-stratum typing this record's stratum (1) belongs to (do not duplicate; this page is the field schema, that page is the conceptual typing).
- [`OpParams`](./OpParams.md) — stratum (2), the construction-time readonly configuration record.
- [`krylov`](./krylov.md) — stratum (3), the ephemeral per-restart workspace record.
- [`solve-monad`](./solve-monad.md) — the monad that threads `SimState`.
