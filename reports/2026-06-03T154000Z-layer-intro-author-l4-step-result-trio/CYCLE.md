---
agent: layer-intro-author
invoked_at: 2026-06-03T154000Z
scope: record-definition cohort #2(a) — per-step result-side L4 records (StepOutputs, PrevCarry, Solve{...} return record)
status: pending
integrated_at: 2026-06-03T154500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (staging row 2/5). 3 record-definition concept pages (step-outputs/prev-carry/solve-result) + 3 alpha-position index/SUMMARY entries (REUSED D1's `record` legend). solve-result cross-links the Solve EFFECT to solve-monad.md, defines only the record FIELDS. record-definition data-shape pages (claim checks no-op). Build clean."
---

# CYCLE: concepts/ record-definition trio (step-outputs, prev-carry, solve-result)

## Summary

Authors THREE new cross-cutting record-definition concept pages (record-definition obligation, user directive 2026-06-03) — the per-step *result-side* L4 records of the [`krylov-step`](../../book/src/L4/krylov-step.md) kernel:

- **`book/src/concepts/step-outputs.md`** — `StepOutputs`, the demand-prunable per-step readout bundle (residual norm, LS residual, breakdown token).
- **`book/src/concepts/prev-carry.md`** — `PrevCarry`, the first-iteration-unrolling closure-threaded recurrence carry (CG `β_prev`, GMRES `H_{k,k-1}`).
- **`book/src/concepts/solve-result.md`** — the `Solve { sim, krylov, outputs[, carry] }` return-*record* shape, with the explicit effect-vs-record `Solve` disambiguation against `solve-monad`.

Each page defines the record **in itself**: fielded definition table (`field : type — meaning`, TS brace form), construction-vs-run-time stratum per field, the L0 source home of the backing C++ fields, and the list of signatures that name it. Discipline held: data-shape not algebra — the pages cross-link `state-stratification` / `solve-monad` / `first-iteration-unrolling` / `derived-view-hoisting` / `krylov-step` rather than restating their algebra.

The three pages are NEW files (full content below); the only edits to existing artifacts are alpha-position row inserts into `concepts/index.md` and `book/src/SUMMARY.md`. The `record` Kind value/legend line is authored by the parallel D1 dispatch — these three rows REUSE `record` and do NOT re-author the legend.

All 16 pinpoint citations across the three pages pass `citecheck --scan` (9 / 3 / 4, 0 failing). Key L0 anchors verified with `citecheck --anchor`:
- `palace/linalg/iterative.hpp:52-55` (anchor `final_res`) — ok, anchor at line 54.
- `palace/linalg/iterative.cpp:21-25` (anchor `CheckDot`) — ok, anchor at line 22.

## Proposed changes

### New file: book/src/concepts/step-outputs.md

Full content is on disk at `book/src/concepts/step-outputs.md` (authored this dispatch). Integrator: apply verbatim as a new file. Body reproduced here for the proposed-changes channel:

```file:book/src/concepts/step-outputs.md
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

## Status

`firm` — fields, types, per-field run-time stratum, and L0 backing sites are all positively cited; the record is the `outputs` field of the firm L4 `krylov-step` signature. The `BreakdownTag` enumeration is slice-specific and left open (the only constructed sub-part), but the record *shape* is firm.
```

### New file: book/src/concepts/prev-carry.md

Full content is on disk at `book/src/concepts/prev-carry.md`. Body reproduced for the proposed-changes channel:

```file:book/src/concepts/prev-carry.md
# prev-carry

`PrevCarry` is the **closure-threaded recurrence carry** that the [`first-iteration-unrolling`](./first-iteration-unrolling.md) rotation moves *out of* the steady-state iteration schema and threads through the loop driver as a closure argument. It appears only in **Form B** (first-iteration-unrolled) of the L4 [`krylov-step`](../L4/krylov-step.md) kernel. This page defines the data shape — what the carry holds, its type, its stratum, and its L0 backing — not the rotation that produces it (that is [`first-iteration-unrolling`](./first-iteration-unrolling.md)).

The defining property of `PrevCarry` is its **placement**: per [`first-iteration-unrolling`](./first-iteration-unrolling.md) §"The rotation", it is a *closure parameter of the loop driver*, **not** a *state field of the iteration*. The steady-state schema is one slot lighter for having moved the recurrence variable out into the carry; the `steady_step` body becomes branch-free because the `if it == 0` base-case branch is discharged by construction (`steady_step` is only ever called after `first_step` has produced a well-defined carry).

## Record definition

    PrevCarry = { <recurrence-variable> }   -- slice-specific single-slot (or small) carry

    -- CG / PCG:   PrevCarry = { beta_prev: Scalar }       -- β_{k-1} = (Br, r)_{k-1}
    -- GMRES:      PrevCarry = { H_prev: Scalar }           -- H_{k,k-1} (sub-diagonal Hessenberg entry)

| Field | Type | Meaning | Stratum |
|---|---|---|---|
| `beta_prev` (CG / PCG) | `Scalar` | The prior iteration's preconditioned residual inner product `β_{k-1} = (Br, r)_{k-1}`, used to form the CG direction-update coefficient `β_k / β_{k-1}` in `p_k = r_k + (β_k/β_{k-1})·p_{k-1}`. | run-time, **carry stratum** (threaded across steps, reborn per solve) |
| `H_prev` (GMRES) | `Scalar` | The prior Arnoldi step's sub-diagonal Hessenberg entry `H_{k,k-1}`; the carry the first-Arnoldi-step base case lacks. GMRES less commonly adopts Form B (its orthogonalization loop handles `k=0` as a zero-length loop). | run-time, **carry stratum** |

**Construction-vs-run-time stratum.** `PrevCarry` is **run-time** and occupies a distinct **carry stratum** — the "fourth stratum" pattern of [`state-stratification`](./state-stratification.md) §"a fourth stratum": *threaded across an inner loop within a single call but reborn at each top-level solve*. It is **not** construction-time (it is not captured in `OpParams`; it restarts from the base case each solve — leaving it in `OpParams` would persist it between calls and corrupt the next solve, the §"Common stratification mistakes" failure). It is **not** an ordinary per-step ephemeral either: an ordinary ephemeral has no cross-iteration data dependence, whereas `PrevCarry` carries a genuine `value_k ← f(value_{k-1})` recurrence. The carry's lifetime is exactly "one solve, all steps after the first."

## L0 source home

`PrevCarry` has **no L0 struct** — it is a *negative* artifact of the L4 first-iteration-unrolling rotation. Palace's source does **not** unroll the first iteration (per [`first-iteration-unrolling`](./first-iteration-unrolling.md) §"What is preserved": "The source code still contains the per-step branch"). In Palace's L0 form the recurrence variable is an **ordinary loop-local mutable** carried by the per-step `if it == 0` branch, not a separately-threaded carry:

- **CG `beta_prev`** — Palace's PCG loop computes `beta = (Br, r)` at the top of each step (`palace/linalg/iterative.cpp:395-396`) and the direction update `p = r + (beta / beta_prev) * p` uses the value from the previous iteration via an ordinary local; the iteration-zero special case (`p_0 = r_0`, no `β_{-1}`) is the in-loop branch the rotation hoists. The backing quantity is the preconditioned inner product `beta`, guarded by `CheckDot` (`iterative.cpp:396`).
- **GMRES `H_prev`** — the sub-diagonal Hessenberg entry built during the Arnoldi orthogonalization / plane-rotation sequence (`palace/linalg/iterative.cpp:636-644`).

So the L0 home is the **loop-local recurrence value**, not a struct field. `PrevCarry` exists at L4 purely to *type* the carry that the rotation extracts; it is the closure parameter that replaces the in-loop `_prev` slot. This is a deliberately *constructive* record (the L4 form may unroll where Palace did not) — see [`first-iteration-unrolling`](./first-iteration-unrolling.md) §Background.

## Distinct from neighbouring records

- **Not `Krylov`.** In Form A (branch-in-body), the recurrence variable lives *inside* the `Krylov` bundle as a `_prev` field; Form B's whole point is that it is **removed** from `Krylov` and re-typed as `PrevCarry`. The Form B `Krylov` schema is one slot lighter (see [`krylov-step`](../L4/krylov-step.md) §Semantics).
- **Not `StepOutputs`.** `StepOutputs` is the demand-prunable readout *consumed by the outer driver*; `PrevCarry` is *threaded back into the next step* as input. They are the two distinct result-side slots of Form B's return record `{ sim, krylov, carry, outputs }`.

## See also

- [`first-iteration-unrolling`](./first-iteration-unrolling.md) — the rotation that creates `PrevCarry`; the authoritative home for *why* and *when* the carry is extracted.
- [`krylov-step`](../L4/krylov-step.md) — Form B `first_step` / `steady_step` signatures that name `carry: PrevCarry`.
- [`state-stratification`](./state-stratification.md) — the carry / "fourth stratum" lifetime category `PrevCarry` belongs to.
- [`solve-result`](./solve-result.md) — the Form-B return record `{ sim, krylov, outputs, carry }` of which `PrevCarry` is the `carry` field.

## Signatures that name this record

- `first_step :: OpParams -> Krylov -> (SimState -> Solve { sim, krylov, carry: PrevCarry, outputs })`
- `steady_step :: OpParams -> Krylov -> (PrevCarry -> SimState -> Solve { sim, krylov, carry: PrevCarry', outputs })`

both in [`krylov-step`](../L4/krylov-step.md) §Signature (Form B).

## Status

`firm` — field, type, carry-stratum placement, and the negative L0 anchoring (Palace does not unroll; the carry is a reified rotation artifact) are all stated and cited; the record is the `carry` slot of the firm L4 `krylov-step` Form B signature and the canonical carry of the firm [`first-iteration-unrolling`](./first-iteration-unrolling.md) concept.
```

### New file: book/src/concepts/solve-result.md

Full content is on disk at `book/src/concepts/solve-result.md`. Body reproduced for the proposed-changes channel:

```file:book/src/concepts/solve-result.md
# solve-result

`Solve { sim, krylov, outputs[, carry] }` is the **return-record shape** of the L4 [`krylov-step`](../L4/krylov-step.md) kernel — the record of values one step hands back. This page defines that *record's fields* — the data shape. It is **distinct from the `Solve` monad effect**: the `Solve` monad (the `StateT SimState Identity` *effect* that threads `SimState`) is defined by [`solve-monad`](./solve-monad.md); this page defines the *fields the monadic action returns as its value*, not the threading discipline. The two share the name `Solve` because the L4 narrative writes the kernel result as `Solve { ... }` — the wrapping monad plus the record of returned values — but they answer different questions: `solve-monad` answers *how state is threaded*; `solve-result` answers *what record a step yields*.

## Record definition

    -- Form A (branch-in-body):
    StepReturn  = Solve { sim: SimState', krylov: Krylov', outputs: StepOutputs }

    -- Form B (first-iteration-unrolled): one additional field
    StepReturnB = Solve { sim: SimState', krylov: Krylov', outputs: StepOutputs, carry: PrevCarry' }

| Field | Type | Meaning | Stratum | Optionality |
|---|---|---|---|---|
| `sim` | `SimState'` | The next externally-visible state. **Discharged via the monad, not by structural projection** — the actual L4 mechanism is a `modify`-shaped `SimState` transition (typically the `it`-counter increment; the iterate `x` is folded at restart boundaries, not per step). Written as a record field only for the L4 narrative. | run-time; the monadic-effect product | always present |
| `krylov` | `Krylov'` | The next solve-local working bundle (basis, Hessenberg, scalars), returned as a **plain value** (its born-at-restart / discarded-at-restart lifetime defeats encoding as monadic state). | run-time; plain returned value | always present |
| `outputs` | `StepOutputs` | The demand-prunable per-step readout bundle (residual norm, LS residual, breakdown token) — see [`step-outputs`](./step-outputs.md). | run-time; plain returned value | always present |
| `carry` | `PrevCarry'` | The closure-threaded recurrence carry (`β_prev` for CG; `H_{k,k-1}` for GMRES) — see [`prev-carry`](./prev-carry.md). | run-time; carry stratum | **Form B only** |

**Construction-vs-run-time stratum.** Every field is **run-time** — the record is the *product of running one step*, so by definition it holds no construction-time data (the construction-time configuration lives in `OpParams`, which is an *input* to the kernel, never a field of its result). The structural distinction among the run-time fields is *how each is discharged*: `sim` is the **monadic-effect product** (returned through the `Solve` monad's `SimState` transition via `modify`), while `krylov` / `outputs` / `carry` are the **monadic action's plain return value** (the record's other fields). This split — one effectful field, the rest pure returned values — is exactly the [`solve-monad`](./solve-monad.md) rule of thumb: "if the action reads or writes `SimState`, it's in the monad; otherwise it's a pure function call / returned value."

## L0 source home

`Solve { ... }` has **no single L0 struct** — it is the L4 reification of one iteration's outputs, which Palace's C++ realises as **in-place mutations on the solver instance plus loop-local updates**, not as a returned record:

- **`sim`** mirrors the solve-statistics fields mutated in place on the `IterativeSolver` instance: `mutable bool converged; mutable double initial_res, final_res; mutable int final_it;` (`palace/linalg/iterative.hpp:53-55`), plus the iterate vector `x` written through the solver's `Mult` output argument. The L4 `sim` field un-mixes these persistent statistics into an explicit value-threaded `SimState'`.
- **`krylov`** mirrors the working bundle Palace holds as solver instance fields / loop locals (the basis `V`, Hessenberg `H`, rotation registers `cs`/`sn`, etc.); see [`state-stratification`](./state-stratification.md) §"Worked example — GMRES".
- **`outputs`** mirrors the per-step derived readouts computed inline (`res = √|beta|` at `iterative.cpp:395-397`; GMRES LS residual `beta = |s[j+1]|` at `iterative.cpp:642`; the `CheckDot` guard at `iterative.cpp:21-31`); see [`step-outputs`](./step-outputs.md) §"L0 source home".
- **`carry`** (Form B) is the reification of a loop-local recurrence value Palace carries through its in-loop `if it == 0` branch (Palace does not unroll); see [`prev-carry`](./prev-carry.md) §"L0 source home".

The L0 form expresses all four as **side-effects on shared mutable state** (the L1 mutation rotation turns these into the pure value-threaded record this page defines). The record-shaped return is the L4 surface; the L0 home is the bundle of mutated instance fields + loop locals.

## Distinct from the `Solve` monad

The single most important distinction this page draws: **`Solve` is overloaded between an effect and a record.**

- The **effect** `Solve a = StateT SimState Identity a` ([`solve-monad`](./solve-monad.md)) is *how `SimState` is threaded* across the loop. It is a type constructor parameterised by the returned-value type `a`.
- The **record** `Solve { sim, krylov, outputs[, carry] }` (this page) is the *shape of the value `a`* a single `krylov-step` yields — the `sim` field happens to be the effect's state product, the other fields are the plain `a`-value.

When you read `Solve { sim, krylov, outputs }` in the [`krylov-step`](../L4/krylov-step.md) signature, the `Solve` names the monad *and* the braces name the returned record; this page owns the *fields*, [`solve-monad`](./solve-monad.md) owns the *threading*.

## See also

- [`solve-monad`](./solve-monad.md) — the `Solve` **effect** (`StateT SimState Identity`); the threading discipline. The authoritative home for the monad; this page does not restate it.
- [`krylov-step`](../L4/krylov-step.md) — the kernel whose result is this record; §Signature names both Form A and Form B return shapes.
- [`step-outputs`](./step-outputs.md) — the `outputs` field.
- [`prev-carry`](./prev-carry.md) — the Form-B `carry` field.
- [`state-stratification`](./state-stratification.md) — the `SimState` / `Krylov` typing the `sim` / `krylov` fields instantiate.

## Signatures that name this record

- `krylov-step :: OpParams -> Krylov -> (SimState -> Solve { sim, krylov, outputs })` (Form A)
- `first_step` / `steady_step` returning `Solve { sim, krylov, carry, outputs }` (Form B)

both in [`krylov-step`](../L4/krylov-step.md) §Signature.

## Status

`firm` — the four fields, their types, their run-time discharge stratum (monadic-effect product vs. plain returned value), and the L0 mutated-state backing are all stated and cited; the record is the return shape of the firm L4 `krylov-step` signature. The effect-vs-record `Solve` distinction is drawn explicitly to forestall conflation with [`solve-monad`](./solve-monad.md).
```

### Edit: book/src/concepts/index.md — three alpha-position `record`-Kind rows

Insert `prev-carry` between `plane-rotation-stream` and `rotation`; `solve-result` between `solve-monad` and `solver-as-operator`; `step-outputs` between `state-stratification` and `tensor-field-lift`. Kind cell is `record` (legend line owned by parallel D1; not re-authored here).

```edit:book/src/concepts/index.md
[old]: | [plane-rotation-stream](./plane-rotation-stream.md) | layer-pattern |
| [rotation](./rotation.md) | methodology |
[new]: | [plane-rotation-stream](./plane-rotation-stream.md) | layer-pattern |
| [prev-carry](./prev-carry.md) | record |
| [rotation](./rotation.md) | methodology |
```

```edit:book/src/concepts/index.md
[old]: | [solve-monad](./solve-monad.md) | layer-pattern |
| [solver-as-operator](./solver-as-operator.md) | layer-pattern |
[new]: | [solve-monad](./solve-monad.md) | layer-pattern |
| [solve-result](./solve-result.md) | record |
| [solver-as-operator](./solver-as-operator.md) | layer-pattern |
```

```edit:book/src/concepts/index.md
[old]: | [state-stratification](./state-stratification.md) | layer-pattern |
| [tensor-field-lift](./tensor-field-lift.md) | layer-pattern |
[new]: | [state-stratification](./state-stratification.md) | layer-pattern |
| [step-outputs](./step-outputs.md) | record |
| [tensor-field-lift](./tensor-field-lift.md) | layer-pattern |
```

### Edit: book/src/SUMMARY.md — three alpha-position concepts-block entries

```edit:book/src/SUMMARY.md
[old]:   - [plane-rotation-stream](./concepts/plane-rotation-stream.md)
  - [rotation — methodology concept](./concepts/rotation.md)
[new]:   - [plane-rotation-stream](./concepts/plane-rotation-stream.md)
  - [prev-carry](./concepts/prev-carry.md)
  - [rotation — methodology concept](./concepts/rotation.md)
```

```edit:book/src/SUMMARY.md
[old]:   - [solve-monad](./concepts/solve-monad.md)
  - [solver-as-operator](./concepts/solver-as-operator.md)
[new]:   - [solve-monad](./concepts/solve-monad.md)
  - [solve-result](./concepts/solve-result.md)
  - [solver-as-operator](./concepts/solver-as-operator.md)
```

```edit:book/src/SUMMARY.md
[old]:   - [state-stratification](./concepts/state-stratification.md)
  - [tensor-field-lift](./concepts/tensor-field-lift.md)
[new]:   - [state-stratification](./concepts/state-stratification.md)
  - [step-outputs](./concepts/step-outputs.md)
  - [tensor-field-lift](./concepts/tensor-field-lift.md)
```

## Supporting evidence

- **Authoritative source for the three records' fields/stratification:** `book/src/L4/krylov-step.md:25,31-33,37-42,82` — the Form A / Form B signatures (`Solve { sim, krylov, outputs[, carry] }`), the per-field stratification narrative for `OpParams`/`Krylov`/`SimState`/`PrevCarry`/`StepOutputs`, and the demand-pruning Law 1.
- **Cross-linked concept pages (verbatim-aligned, not restated):** `book/src/concepts/state-stratification.md` (three-stratum + fourth carry stratum at §49-63), `book/src/concepts/solve-monad.md` (the `Solve a = StateT SimState Identity a` *effect* + the in-monad/out-of-monad rule of thumb at :35), `book/src/concepts/first-iteration-unrolling.md` (the rotation creating `PrevCarry`, :19-49), `book/src/concepts/derived-view-hoisting.md` (demand-pruning law underwriting `StepOutputs`).
- **L0 backing sites (citecheck-verified):**
  - `palace/linalg/iterative.hpp:52-55` — solve-statistics fields `converged` / `initial_res` / `final_res` / `final_it` (anchor `final_res` at line 54, verified).
  - `palace/linalg/iterative.cpp:21-31` — `CheckDot` partial-function guard (anchor `CheckDot` at line 22, verified).
  - `palace/linalg/iterative.cpp:395-397` — PCG residual `res = √|beta|`, `beta = (Br,r)`.
  - `palace/linalg/iterative.cpp:642-644` — GMRES LS residual `beta = |s[j+1]|`, `converged = (beta < eps)`.
  - `palace/linalg/iterative.cpp:484` — `final_res = res` (PCG statistic write).
  - `palace/linalg/iterative.cpp:636-644` — GMRES Givens / Hessenberg sequence (the `H_prev` backing).
- **citecheck:** `--scan` clean on all three pages (9 / 3 / 4 citations, 0 failing); `--anchor` on the two key L0 anchors both `[ok]`.

## Open questions / caveats

- **D1 Kind-legend dependency (coordination, not a defect).** These three rows use Kind value `record`; the `record` legend line in `concepts/index.md` §"Kind values" is authored by the parallel D1 dispatch. If D1 does not land in this cycle, the integrator should either (a) hold these row inserts until D1's legend lands, or (b) add the one-line `record` legend entry itself. The row inserts are otherwise parallel-safe (distinct anchors).
- **`OpParams` / `Krylov` / `SimState` record-definition homes (cohort #2(b), separate dispatch).** This cohort covers the *result-side* trio only. The *input/state-side* L4 records `OpParams`, `Krylov`, `SimState` are named across ≥2 chapters (krylov-step + state-stratification + solve-monad) and per the directive-2 ≥2-consumer bar warrant their own record-definition pages. They are partially defined by use in `state-stratification.md` but lack a dedicated record-definition home with the fielded `field : type — meaning` + stratum + L0-source schema. Flagged: `record-OpParams-needs-definition-home`, `record-Krylov-needs-definition-home`, `record-SimState-needs-definition-home`. (Appended to open-questions.md.)
- **`BreakdownTag` enumeration is open.** `StepOutputs.breakdown_token`'s `BreakdownTag` is a slice-specific enum left open on the page (only `CheckDot`'s positive-definite/finite guard is positively cited). If a future harvester enumerates the full breakdown-tag set per slice, the `step-outputs.md` enum line should be refined. Not blocking — the record *shape* is firm.
