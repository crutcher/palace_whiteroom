---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/linalg/iterative.cpp:393-397
      kind: cites-evidence            # PCG residual proxy: beta = (Br,r) (:395), CheckDot (:396), res = sqrt|beta| (:397)
    - target: palace/linalg/iterative.cpp:640-644
      kind: cites-evidence            # GMRES LS-residual estimate: beta = |s[j+1]| (:642), CheckDot (:643), converged test (:644)
    - target: palace/linalg/iterative.cpp:21-31
      kind: cites-evidence            # CheckDot guard backing the breakdown_token slot
    - target: palace/linalg/iterative.hpp:26-115
      kind: cites-evidence            # persistent home of the readouts: mutable final_res statistic (:54)
  reference:
    - L4/krylov-step
    - concepts/derived-view-hoisting
    - concepts/solve-monad
    - concepts/state-stratification
    - concepts/solve-result
    - concepts/sim-state
    - concepts/krylov
---

# step-outputs

`StepOutputs` is the **demand-prunable per-step readout bundle** returned by the L4 [`krylov-step`](../L4/krylov-step.md) kernel alongside the next `SimState` and `Krylov` values. It is a *record definition*: this page defines the data shape — its fields, their types, their meaning, and the L0 source the fields mirror — not the algebra of the operator that produces it (that lives in [`krylov-step`](../L4/krylov-step.md) and its [`derived-view-hoisting`](./derived-view-hoisting.md) demand-pruning law).

It is a **result-side** record: it carries the *observations a step makes about itself* — the residual proxy, the least-squares residual estimate, and any breakdown signal — so that the outer driver (`iterate_while`'s predicate, `solve_loop`'s `Outcome` classifier) can read them without inspecting `Krylov` internals. Every field is **derived** from the post-step `Krylov` bundle by a pure function and is **demand-prunable**: if no downstream consumer reads a field, the kernel is free to skip computing it (the [`derived-view-hoisting`](./derived-view-hoisting.md) Law 1 distributivity-over-trajectory). The record exists precisely to make that pruning structural — the derived views are typed separately from the `Krylov` state they are derived from.

## Record definition

    StepOutputs = {
      residual_norm:    Scalar,            -- ‖r‖ proxy for this step (CG: √|(Br,r)|; non-restarted)
      ls_residual?:     Scalar,            -- GMRES/FGMRES least-squares residual estimate |s[j+1]|
      breakdown_token?: BreakdownTag       -- partiality signal: a guarded-quantity validity tag
    }

    BreakdownTag = Ok | NotPositiveDefinite | NotFinite | ...   -- slice-specific

| Field | Type | Meaning | Stratum | Optionality |
|---|---|---|---|---|
| `residual_norm` | `Scalar` | The step's residual-norm proxy — a pure derived view `g(krylov')` of the post-step bundle. For CG, `√|β|` where `β = (Br, r)`. | run-time (per-step derived) | always present |
| `ls_residual` | `Scalar` | The GMRES / FGMRES least-squares residual estimate `|s[j+1]|`, read off the rotated RHS vector after the Givens update — the cheap LS proxy that avoids forming the true residual each inner step. | run-time (per-step derived) | present only for restarted-LS Krylov methods (GMRES, FGMRES); absent for CG / Chebyshev |
| `breakdown_token` | `BreakdownTag` | The materialised result of a guarded-quantity validity check (`CheckDot`-style): whether a dot product expected positive-definite came back finite and non-negative. Routes partiality to the wrapper rather than aborting in the kernel body. | run-time (per-step derived) | present only for breakdown-guarding kernels (CG positive-definiteness guard, GMRES residual-validity guard) |

**Construction-vs-run-time stratum.** Every `StepOutputs` field is **run-time, per-step, derived** — none is captured at solve construction. The record is reborn each step (a fresh value, like `Krylov'`), and each field is a pure function of the post-step `Krylov` bundle. There are no construction-time fields: the *which fields are present* question is fixed at construction by the slice's variant profile (a CG `StepOutputs` has no `ls_residual` slot at all), but the *values* are all run-time.

## L0 source home

`StepOutputs` does not exist as a single named C++ struct in Palace — it is the L4 *reification* of three readout quantities that Palace computes inline inside each iterative-solver loop body and either stores in solve-statistics fields or consumes immediately. The backing source sites:

- **`residual_norm`** — Palace's PCG loop computes `res = std::sqrt(std::abs(beta))` from `beta = (Br, r)` each step (`palace/linalg/iterative.cpp:395-397`); the value flows into the persisted `final_res` statistic at loop exit (`iterative.cpp:484`). The persisted home is the solve-statistics field `mutable double final_res` (`palace/linalg/iterative.hpp:54`).
- **`ls_residual`** — GMRES computes `beta = std::abs(s[j + 1])` after the Givens plane-rotation update of the LS RHS (`palace/linalg/iterative.cpp:642`); this is the cheap LS residual estimate the convergence test reads (`converged = (beta < eps)`, `iterative.cpp:644`).
- **`breakdown_token`** — the `CheckDot` partial-function guard (`palace/linalg/iterative.cpp:21-31`; a templated `MFEM_ASSERT(std::isfinite(dot) && dot >= 0.0, ...)`) is invoked at each guarded dot site (e.g. `iterative.cpp:396` PCG, `iterative.cpp:643` GMRES). At L0 the guard *aborts* on failure; at L4 the failure is reified as a `breakdown_token` slot routed to the outer driver (see [`krylov-step`](../L4/krylov-step.md) §Semantics, "Breakdown signals propagate through `outputs`").

The L0 form **mixes** these three readouts into the loop body and the persistent solve-statistics fields (`converged` / `initial_res` / `final_res` / `final_it`, `iterative.hpp:53-55`); the L4 `StepOutputs` record *un-mixes* the per-step derived observations from the persistent `SimState` statistics, which is what makes the demand-pruning law statable.

## Distinct from neighbouring records

- **Not `SimState`.** `SimState` is the externally-visible persistent state ([`state-stratification`](./state-stratification.md): `x`, `it`, `converged`, `final_res`, `initial_res`); it persists across the whole solve. `StepOutputs` is per-step ephemeral and derived — it is the *observation* feeding the eventual `SimState.final_res` / `SimState.converged` statistics, not those statistics themselves.
- **Not `Krylov`.** `Krylov` is the solve-local working bundle (basis, Hessenberg, scalars). `StepOutputs` fields are *pure derived views of* `Krylov'`, typed separately so they can be pruned.

## See also

- [`krylov-step`](../L4/krylov-step.md) — the L4 kernel returning `{ sim, krylov, outputs }`; defines the behaviour producing this record.
- [`derived-view-hoisting`](./derived-view-hoisting.md) — the demand-pruning law (Law 1) that the `StepOutputs` typing makes structural.
- [`solve-monad`](./solve-monad.md) — the outer driver whose `Outcome` classifier reads `outputs.breakdown_token` / `outputs.residual_norm`.
- [`state-stratification`](./state-stratification.md) — the three-stratum split `StepOutputs` is *not* part of (it is a fourth, result-side bundle).
- [`solve-result`](./solve-result.md) — the enclosing return record `{ sim, krylov, outputs[, carry] }` of which `StepOutputs` is the `outputs` field.

## Signatures that name this record

- `krylov-step :: OpParams -> Krylov -> (SimState -> Solve { sim, krylov, outputs: StepOutputs })` (Form A) and the Form B `first_step` / `steady_step` pair — [`krylov-step`](../L4/krylov-step.md) §Signature.
