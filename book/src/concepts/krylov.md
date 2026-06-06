---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/linalg/iterative.hpp:119-150
      kind: cites-evidence            # CgSolver class + `mutable VecType r, z, p;` workspace (:144)
    - target: palace/linalg/iterative.hpp:155-217
      kind: cites-evidence            # GmresSolver class + V/r/H/s,sn/cs workspace (:190-194) + Initialize/Update (:197-198)
    - target: palace/linalg/iterative.hpp:222-275
      kind: cites-evidence            # FgmresSolver class + `mutable std::vector<VecType> Z;` (:256)
  reference:
    - L4/krylov-step
    - concepts/solve-monad
    - concepts/convergence-test
    - concepts/state-stratification
    - concepts/op-params
    - concepts/sim-state
    - concepts/first-iteration-unrolling
    - concepts/prev-carry
---

# Krylov

> **Kind: `record`.** This page defines the *data shape* of the L4 `Krylov` record — its (slice-specific) field schemas, their types and meaning, the construction-vs-run-time stratum of each, and the L0 source home it mirrors. The *behaviour* over `Krylov` (how `krylov-step` reads and updates it) lives in the operator chapters that consume it — this page does not restate that algebra.

`Krylov` is the **ephemeral-intermediates** stratum of the L4 three-stratum solve typing: the solve-local workspace bundle, born at restart entry and discarded at restart exit or solve return. It is threaded through the kernel as a **plain value** (not as a monadic effect — its lifetime is strictly within a single restart cycle, which defeats encoding-as-state). It is the concrete record realising stratum (3) of [`state-stratification`](./state-stratification.md) — see that page for *why* the three-way split is load-bearing; this page enumerates the (slice-specific) field schemas.

Unlike the slice-uniform [`sim-state`](./sim-state.md), the `Krylov` schema is **slice-specific**: each Krylov method instantiates its own field set. The two settled schemas:

## Record definition — CG

The iterate-stratum fields below are all congruent solution-space vectors over one shape group — bound `(S: ...)` and used as `$S` per [`l4_calculus`](../semantics/index.md) §1.2.1 (the group `S` is the solution shape, not a rank-1 length axis):

```text
Krylov(CG) = {
  r  : Tensor[$S],   -- residual
  p  : Tensor[$S],   -- search direction
  z? : Tensor[$S],   -- preconditioned residual (present iff a preconditioner is set)
  α  : Scalar,      -- step length
  β  : Scalar       -- direction-update coefficient (the residual proxy read by convergence-test)
}
```

| Field | Type | Stratum | Meaning |
|-------|------|---------|---------|
| `r` | `Tensor[$S]` | run-time, iterate-stratum, solve-local | Residual vector. |
| `p` | `Tensor[$S]` | run-time, iterate-stratum, solve-local | Search (conjugate) direction. |
| `z?` | `Tensor[$S]` | run-time, iterate-stratum, solve-local | Preconditioned residual; present iff `OpParams.T` carries a preconditioner. |
| `α` | `Scalar` | run-time, scalar-stratum, solve-local | Step length for the iterate/residual update. |
| `β` | `Scalar` | run-time, scalar-stratum, solve-local | Direction-update coefficient; the residual proxy [`convergence-test`](./convergence-test.md) reads. |

(CG is non-restarted, so its "restart cycle" is the entire solve; the bundle is born once and discarded at solve return.)

## Record definition — GMRES / FGMRES

```text
Krylov(GMRES) = {
  V  : [Tensor[$S]],   -- Arnoldi basis (array of basis columns)
  Z? : [Tensor[$S]],   -- preconditioned basis (present iff OpParams.flexible — FGMRES)
  H  : DenseMatrix,   -- Hessenberg matrix (small-dense, scalar-stratum)
  s  : [Scalar],      -- least-squares RHS / rotated residual vector (small-dense)
  cs : [Scalar],      -- Givens cosines (small-dense)
  sn : [Scalar],      -- Givens sines (small-dense)
  β  : Scalar,        -- current residual proxy
  j  : Int            -- inner-iteration index within the restart cycle
}
```

| Field | Type | Stratum | Meaning |
|-------|------|---------|---------|
| `V` | `[Tensor[$S]]` | run-time, iterate-stratum, restart-local | Arnoldi basis columns. |
| `Z?` | `[Tensor[$S]]` | run-time, iterate-stratum, restart-local | Preconditioned basis; present iff `OpParams.flexible` (FGMRES). |
| `H` | `DenseMatrix` | run-time, scalar-stratum, restart-local | Upper-Hessenberg matrix from the Arnoldi recurrence. |
| `s` | `[Scalar]` | run-time, scalar-stratum, restart-local | Least-squares RHS / rotated residual; `s` provides the LS-residual proxy. |
| `cs` / `sn` | `[Scalar]` | run-time, scalar-stratum, restart-local | Givens rotation registers (cosines / sines). |
| `β` | `Scalar` | run-time, scalar-stratum, restart-local | Current residual proxy read by `convergence-test`. |
| `j` | `Int` | run-time, restart-local | Inner-iteration index within the current restart cycle. |

**The whole record is run-time and restart-local** — that is the defining property of the ephemeral stratum, distinct from the construction-time [`op-params`](./op-params.md) and the solve-persistent [`sim-state`](./sim-state.md). `Krylov` is **mixed-stratum** internally: it carries both `Tensor[$S]`-typed iterate-bundle fields (`V`, `Z`, `r`, `p`) and small-dense scalar-stratum fields (`H`, `s`, `cs`, `sn`, `β`, `α`). On a restarted solver the bundle is **reborn at each restart** (the `Krylov` at restart `r+1` is a fresh bundle, not the prior bundle with `j` reset) — the lifetime that forbids `Krylov` from living in `SimState`.

When [`first-iteration-unrolling`](./first-iteration-unrolling.md) Form B is applied, the recurrence-carry field (CG's `β_prev`; GMRES's `H_{k,k-1}`) is *removed* from the `Krylov` schema and threaded as a `PrevCarry` closure argument instead — so Form B's `Krylov` is one slot lighter.

## L0 source home

The `Krylov` schema mirrors the **`mutable` "Temporary workspace for solve"** instance fields of Palace's `CgSolver` / `GmresSolver` / `FgmresSolver` classes (`palace/linalg/iterative.hpp`):

- **CG** (`CgSolver`, `iterative.hpp:119-150`): `mutable VecType r, z, p;` (`iterative.hpp:144`) ↔ `Krylov(CG)` fields `r`, `z?`, `p`. (The scalars `α`, `β` are local variables within `CgSolver::Mult`, not instance fields.)
- **GMRES** (`GmresSolver`, `iterative.hpp:155-217`): the workspace block at `iterative.hpp:190-194` — `mutable std::vector<VecType> V;` (`:190`), `mutable VecType r;` (`:191`), `mutable std::vector<ScalarType> H;` (`:192`), `mutable std::vector<ScalarType> s, sn;` (`:193`), `mutable std::vector<RealType> cs;` (`:194`) ↔ `Krylov(GMRES)` fields `V`, `H`, `s`, `sn`, `cs`.
- **FGMRES** (`FgmresSolver`, `iterative.hpp:222-275`): adds `mutable std::vector<VecType> Z;` (`iterative.hpp:256`) ↔ `Krylov.Z?`, present exactly because `OpParams.flexible` is true. The lazy `Initialize()` / `Update(int j)` methods (declared `iterative.hpp:197-198` for GMRES, overridden in FGMRES) allocate/grow this workspace — the L0 realisation of the "born at restart, grown per inner iteration" lifetime.

This is the mapping [`state-stratification`](./state-stratification.md) §"Worked example — GMRES" records ("lazy `Initialize`/`Update` workspace ↔ Krylov"). The L0 `mutable` keyword on a `const Mult` method marks these as solve-scratch (run-time, reborn each solve/restart) — the stratum boundary separating `Krylov` from the non-`mutable` configuration ([`op-params`](./op-params.md)) and the `mutable` *statistics* ([`sim-state`](./sim-state.md), which persist as the return value rather than being reborn).

## Used by

- [`krylov-step`](../L4/krylov-step.md) — the kernel threads `Krylov` as a plain value, updates it purely (`K' = krylov_update K_aux op w`), and derives `outputs` from it (`L4/krylov-step.md:38`); the slice-specific schemas are named at `L4/krylov-step.md:50`.
- [`solve-monad`](./solve-monad.md) — `restart_cycle` builds a fresh `Krylov`, folds `inner_loop` over the kernel, then folds the correction into `SimState.x`.
- [`convergence-test`](./convergence-test.md) — reads the residual proxy (`Krylov.β` / `Krylov.s`).

## See also

- [`state-stratification`](./state-stratification.md) — the three-stratum typing this record's stratum (3) belongs to (do not duplicate; this page is the field schema, that page is the conceptual typing). Note the *fourth* (scalar-recurrence) stratum it documents for Chebyshev is distinct from `Krylov` and is not enumerated here.
- [`op-params`](./op-params.md) — stratum (2), the construction-time readonly configuration record.
- [`sim-state`](./sim-state.md) — stratum (1), the solve-persistent externally-visible record.
- [`first-iteration-unrolling`](./first-iteration-unrolling.md) — the rotation that moves a recurrence-carry field out of `Krylov` into a `PrevCarry` closure argument.

## Status

`firm` — both slice-specific schemas (CG, GMRES/FGMRES) are settled and match `L4/krylov-step.md:50`; every field is backed by a cited `CgSolver` / `GmresSolver` / `FgmresSolver` `mutable`-workspace instance-field declaration; the run-time restart-local stratum (and the mixed iterate/scalar internal split) is the defining property vs. the other two strata. The record-definition obligation is met: this is the cross-cutting home for `Krylov`, referenced by ≥2 consumers (`L4/krylov-step.md`, `concepts/solve-monad.md`, `concepts/state-stratification.md`, `concepts/convergence-test.md`).
