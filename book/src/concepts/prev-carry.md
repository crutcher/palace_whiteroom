---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/linalg/iterative.cpp:393-397
      kind: cites-evidence            # CG beta_prev backing: beta = (Br,r) recurrence value (:395-396)
    - target: palace/linalg/iterative.cpp:636-644
      kind: cites-evidence            # GMRES H_prev backing: sub-diagonal Hessenberg entry in the Arnoldi/plane-rotation sequence
  reference:
    - concepts/first-iteration-unrolling
    - L4/krylov-step
    - concepts/state-stratification
    - concepts/solve-result
    - concepts/krylov
    - concepts/step-outputs
---

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
