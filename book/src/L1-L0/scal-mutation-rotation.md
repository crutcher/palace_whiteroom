# scal-mutation-rotation

> **Status: `stub`** — claim-free placeholder materialized 2026-05-28 (CLAUDE.md §Methodology invariants "Integration may materialize implied components as stubs"). Exists so converging forward-references resolve to a live home and the plan points at a real file. **No citations or semantic claims yet** — the next `abstractor` refines it in place (`stub` → `rough-in` → `firm`).

## What this will be

The L1>L0 lowering theme for the firm L1 [`scal`](../L1/scal.md) operator: how the pure rescale `scal(α, x)` rewrites into the L0 in-place `x *= α` mutation, the real-imag-shape branch on the complex path, and the call-site fusion with `nrm2` inside `linalg::Normalize` (a transparent fusion the L1 form factors as `scal(1/nrm2(x), x)`). Sibling to the firm `axpby` / `axpbypcz` mutation-rotation themes.

## Implied by

- OQ `scal-mutation-rotation-l1-l0-theme`.
- Plan (`scaffolding/priorities.md`) Backlog High-fan-out item **blas1-l1-l0-lowering-theme-gap**.
- In-file reference in [`L1/scal`](../L1/scal.md) (the L0 in-place mutation, real-imag branch, and `Normalize` fusion are flagged as L1>L0 lowering concerns).
- The firm sibling BLAS-1 mutation-rotation themes.

## Refinement pending

- **Owner:** `abstractor`.
- **Plan:** Backlog High-fan-out `blas1-l1-l0-lowering-theme-gap`.
- **OQs:** `scal-mutation-rotation-l1-l0-theme`.
- Self-verify every L0 citation before emitting.
