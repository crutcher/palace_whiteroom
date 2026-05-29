# nrm2-mutation-rotation

> **Status: `stub`** — claim-free placeholder materialized 2026-05-28 (CLAUDE.md §Methodology invariants "Integration may materialize implied components as stubs"). Exists so converging forward-references resolve to a live home and the plan points at a real file. **No citations or semantic claims yet** — the next `abstractor` refines it in place (`stub` → `rough-in` → `firm`).

## What this will be

The L1>L0 lowering theme for the firm L1 [`nrm2`](../L1/nrm2.md) operator: how `nrm2(x)` rewrites into the L0 `linalg::Norml2` form — the `Dot` + `MPI_Allreduce` + `sqrt` chain (inheriting the [`dot`](./dot-mutation-rotation.md) lowering's MPI-collective theme), the `std::abs` defensive guard against round-off-induced sub-zero self-dot, and the method-form / free-function / `ErrorIndicator` wrapper surface as transparent caller-side conveniences. Notes the B-weighted overload's existence as a separate L0 symbol with a different L1 referent ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)).

## Implied by

- OQs `nrm2-lowering-theme-deliverables`, `nrm2-std-abs-defensive-guard-classification`.
- Plan (`scaffolding/priorities.md`) Backlog High-fan-out item **blas1-l1-l0-lowering-theme-gap**.
- In-file references in [`L1/nrm2`](../L1/nrm2.md) and [`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md) to the not-yet-authored nrm2 lowering.
- The firm sibling BLAS-1 mutation-rotation themes.

## Refinement pending

- **Owner:** `abstractor`.
- **Plan:** Backlog High-fan-out `blas1-l1-l0-lowering-theme-gap`.
- **OQs:** `nrm2-lowering-theme-deliverables`, `nrm2-std-abs-defensive-guard-classification`.
- Self-verify every L0 citation before emitting.
