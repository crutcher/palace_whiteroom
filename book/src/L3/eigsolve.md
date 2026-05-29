# eigsolve

> **Status: `stub`** — claim-free placeholder materialized cycle-023 (CLAUDE.md §Methodology invariants "Integration may materialize implied components as stubs"). Exists so converging forward-references resolve to a live home and the plan points at a real file. **No citations or semantic claims yet** — the cycle-024 L3 backfill refines it in place (`stub` → `rough-in` → … the predicted terminal status is `partial-obstruction`).

## What this will be

The L3 (iteration-rotation) view of `eigsolve`. **Predicted `partial-obstruction`** (per the firm L2 [`eigsolve`](../L2/eigsolve.md) §"Lifts to"): the per-step body — the named shift-invert spectral-transform composition `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)` — lifts cleanly to a global tensor-field expression (it is the `apply_linop ▷ ksp_solve` composition, which has a clean L3 per-step form, identity-in-form to the firm L2 body). **But the eigen-iteration loop does not lift:** unlike [`ksp_solve`](./ksp_solve.md) (whose L3 lift renders the Palace-authored convergence-test loop as an explicit value-threaded tail recursion), `eigsolve` has **no Palace-authored loop to render** — the eigen-iteration (Krylov-Schur restart, Arnoldi/Lanczos basis extension, Rayleigh-Ritz extraction, convergence test) is entirely inside SLEPc `EPSSolve` / ARPACK RCI. The loop is therefore a witnessed `sequential-obstruction` rooted in opaque-library-ownership, with no removable recurrence to rotate. The status reflects the **loop structure, not the body** (the L3 `partial-obstruction` definition per CLAUDE.md §Methodology invariants). The refining dispatch authors the body-lifts / loop-obstruction split, the in-line identity-in-form annotation to the L2 body, and the `sequential-obstruction` citation.

## Implied by

- [`L2/eigsolve`](../L2/eigsolve.md) (firm, cycle-023) — §"Lifts to" + `lowers_to:` frontmatter both name `L3/eigsolve.md` as the iteration-rotation lift target; the firm L2 entry is chain-step-2 of the eigsolve prerequisite chain (L1-firm → L2-firm → **L3-backfill**), and its existence unblocks this L3 entry.
- The eigsolve prerequisite chain (L1 `eigsolve` firm cycle-022 → L2 `eigsolve` firm cycle-023 → L3 backfill cycle-024) — this stub is the chain's step-3 home.
- OQ `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog` (cycle-021 cross-layer-cross-cutter prediction) + the cycle-022/023 eigsolve-chain OQs predicting the L3 lands `partial-obstruction` (or full sequential-obstruction) because the eigen-iteration is opaque-library-owned.

## Refinement pending (cycle-024 L3 backfill)

- **Owner:** `harvester` (or `lowering-verifier` to confirm the obstruction).
- **Predicted terminal status:** `partial-obstruction` (body lifts identity-in-form to the firm L2 [`eigsolve`](../L2/eigsolve.md) body; the eigen-iteration loop is a `sequential-obstruction` rooted in opaque-library-ownership, no Palace-authored kernel/driver pair to rotate).
- **Companion theme:** `L3-L2/eigsolve-*` (the L3>L2 lowering theme) is also pending; the L2>L1 `L2-L1/eigsolve-spectral-transform-composition` theme is separately pending.
- **OQs:** `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog` + the cycle-023 eigsolve-chain OQs.
