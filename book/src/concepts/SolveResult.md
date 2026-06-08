---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/linalg/iterative.hpp:26-115
      kind: cites-evidence            # `sim` backing: mutable solve-statistics fields (:52-54) mutated in place on the solver instance
    - target: palace/linalg/iterative.cpp:393-397
      kind: cites-evidence            # `outputs` backing: per-step derived readouts computed inline (residual proxy)
    - target: palace/linalg/iterative.cpp:640-644
      kind: cites-evidence            # `outputs` backing: GMRES LS-residual readout
    - target: palace/linalg/iterative.cpp:21-31
      kind: cites-evidence            # `outputs` backing: CheckDot guard
  reference:
    - concepts/solve-monad
    - L4/krylov_step
    - concepts/StepOutputs
    - concepts/PrevCarry
    - concepts/state-stratification
    - concepts/SimState
    - concepts/krylov
---

# SolveResult

`Solve { sim, krylov, outputs[, carry] }` is the **return-record shape** of the L4 [`krylov_step`](../L4/krylov_step.md) kernel — the record of values one step hands back. This page defines that *record's fields* — the data shape. It is **distinct from the `Solve` monad effect**: the `Solve` monad (the `StateT SimState Identity` *effect* that threads `SimState`) is defined by [`solve-monad`](./solve-monad.md); this page defines the *fields the monadic action returns as its value*, not the threading discipline. The two share the name `Solve` because the L4 narrative writes the kernel result as `Solve { ... }` — the wrapping monad plus the record of returned values — but they answer different questions: `solve-monad` answers *how state is threaded*; `SolveResult` answers *what record a step yields*.

## Record definition

    -- Form A (branch-in-body):
    StepReturn  = Solve { sim: SimState', krylov: Krylov', outputs: StepOutputs }

    -- Form B (first-iteration-unrolled): one additional field
    StepReturnB = Solve { sim: SimState', krylov: Krylov', outputs: StepOutputs, carry: PrevCarry' }

| Field | Type | Meaning | Stratum | Optionality |
|---|---|---|---|---|
| `sim` | `SimState'` | The next externally-visible state. **Discharged via the monad, not by structural projection** — the actual L4 mechanism is a `modify`-shaped `SimState` transition (typically the `it`-counter increment; the iterate `x` is folded at restart boundaries, not per step). Written as a record field only for the L4 narrative. | run-time; the monadic-effect product | always present |
| `krylov` | `Krylov'` | The next solve-local working bundle (basis, Hessenberg, scalars), returned as a **plain value** (its born-at-restart / discarded-at-restart lifetime defeats encoding as monadic state). | run-time; plain returned value | always present |
| `outputs` | `StepOutputs` | The demand-prunable per-step readout bundle (residual norm, LS residual, breakdown token) — see [`StepOutputs`](./StepOutputs.md). | run-time; plain returned value | always present |
| `carry` | `PrevCarry'` | The closure-threaded recurrence carry (`β_prev` for CG; `H_{k,k-1}` for GMRES) — see [`PrevCarry`](./PrevCarry.md). | run-time; carry stratum | **Form B only** |

**Construction-vs-run-time stratum.** Every field is **run-time** — the record is the *product of running one step*, so by definition it holds no construction-time data (the construction-time configuration lives in `OpParams`, which is an *input* to the kernel, never a field of its result). The structural distinction among the run-time fields is *how each is discharged*: `sim` is the **monadic-effect product** (returned through the `Solve` monad's `SimState` transition via `modify`), while `krylov` / `outputs` / `carry` are the **monadic action's plain return value** (the record's other fields). This split — one effectful field, the rest pure returned values — is exactly the [`solve-monad`](./solve-monad.md) rule of thumb: "if the action reads or writes `SimState`, it's in the monad; otherwise it's a pure function call / returned value."

## L0 source home

`Solve { ... }` has **no single L0 struct** — it is the L4 reification of one iteration's outputs, which Palace's C++ realises as **in-place mutations on the solver instance plus loop-local updates**, not as a returned record:

- **`sim`** mirrors the solve-statistics fields mutated in place on the `IterativeSolver` instance: `mutable bool converged; mutable double initial_res, final_res; mutable int final_it;` (`palace/linalg/iterative.hpp:53-55`), plus the iterate vector `x` written through the solver's `Mult` output argument. The L4 `sim` field un-mixes these persistent statistics into an explicit value-threaded `SimState'`.
- **`krylov`** mirrors the working bundle Palace holds as solver instance fields / loop locals (the basis `V`, Hessenberg `H`, rotation registers `cs`/`sn`, etc.); see [`state-stratification`](./state-stratification.md) §"Worked example — GMRES".
- **`outputs`** mirrors the per-step derived readouts computed inline (`res = √|beta|` at `iterative.cpp:395-397`; GMRES LS residual `beta = |s[j+1]|` at `iterative.cpp:642`; the `CheckDot` guard at `iterative.cpp:21-31`); see [`StepOutputs`](./StepOutputs.md) §"L0 source home".
- **`carry`** (Form B) is the reification of a loop-local recurrence value Palace carries through its in-loop `if it == 0` branch (Palace does not unroll); see [`PrevCarry`](./PrevCarry.md) §"L0 source home".

The L0 form expresses all four as **side-effects on shared mutable state** (the L1 mutation rotation turns these into the pure value-threaded record this page defines). The record-shaped return is the L4 surface; the L0 home is the bundle of mutated instance fields + loop locals.

## Distinct from the `Solve` monad

The single most important distinction this page draws: **`Solve` is overloaded between an effect and a record.**

- The **effect** `Solve a = StateT SimState Identity a` ([`solve-monad`](./solve-monad.md)) is *how `SimState` is threaded* across the loop. It is a type constructor parameterised by the returned-value type `a`.
- The **record** `Solve { sim, krylov, outputs[, carry] }` (this page) is the *shape of the value `a`* a single `krylov_step` yields — the `sim` field happens to be the effect's state product, the other fields are the plain `a`-value.

When you read `Solve { sim, krylov, outputs }` in the [`krylov_step`](../L4/krylov_step.md) signature, the `Solve` names the monad *and* the braces name the returned record; this page owns the *fields*, [`solve-monad`](./solve-monad.md) owns the *threading*.

## See also

- [`solve-monad`](./solve-monad.md) — the `Solve` **effect** (`StateT SimState Identity`); the threading discipline. The authoritative home for the monad; this page does not restate it.
- [`krylov_step`](../L4/krylov_step.md) — the kernel whose result is this record; §Signature names both Form A and Form B return shapes.
- [`StepOutputs`](./StepOutputs.md) — the `outputs` field.
- [`PrevCarry`](./PrevCarry.md) — the Form-B `carry` field.
- [`state-stratification`](./state-stratification.md) — the `SimState` / `Krylov` typing the `sim` / `krylov` fields instantiate.

## Signatures that name this record

- `krylov_step :: OpParams -> Krylov -> (SimState -> Solve { sim, krylov, outputs })` (Form A)
- `first_step` / `steady_step` returning `Solve { sim, krylov, carry, outputs }` (Form B)

both in [`krylov_step`](../L4/krylov_step.md) §Signature.
