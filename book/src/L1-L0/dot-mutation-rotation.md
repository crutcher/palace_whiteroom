# dot-mutation-rotation

> **Status: `stub`** — claim-free placeholder materialized 2026-05-28 (CLAUDE.md §Methodology invariants "Integration may materialize implied components as stubs"). Exists so converging forward-references resolve to a live home and the plan points at a real file. **No citations or semantic claims yet** — the next `abstractor` refines it in place (`stub` → `rough-in` → `firm`).

## What this will be

The L1>L0 lowering theme for the firm L1 [`dot`](../L1/dot.md) operator: how the pure inner-product `dot(x, y)` rewrites into the L0 `linalg::Dot` form — the local element-kernel + `MPI_Allreduce` two-step (single-rank-equivalent per scope), and the **receiver-vs-argument conjugation asymmetry** (method form `(*this).Dot(arg) = argᴴ·(*this)` vs free-function `linalg::Dot(comm, x, y) = xᴴ y`, which conjugates the first argument). Sibling to the firm `axpby` / `axpbypcz` mutation-rotation themes.

## Implied by

- OQ `l1-l0-dot-lowering-asymmetry` (the conjugation-asymmetry + MPI-collective deliverables).
- Plan (`scaffolding/priorities.md`) Backlog High-fan-out item **blas1-l1-l0-lowering-theme-gap**.
- The firm sibling themes [`axpby-mutation-rotation`](./axpby-mutation-rotation.md), [`axpbypcz-mutation-rotation`](./axpbypcz-mutation-rotation.md) (the BLAS-1 one-theme-per-operator pattern).
- The firm operator [`L1/dot`](../L1/dot.md).

## Refinement pending

- **Owner:** `abstractor`.
- **Plan:** Backlog High-fan-out `blas1-l1-l0-lowering-theme-gap`.
- **OQs:** `l1-l0-dot-lowering-asymmetry`.
- Self-verify every L0 citation before emitting (producer-citation self-verification convention).
