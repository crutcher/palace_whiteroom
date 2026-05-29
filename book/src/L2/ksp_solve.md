# ksp_solve

> **Status: `stub`** — claim-free placeholder materialized 2026-05-28 (CLAUDE.md §Methodology invariants "Integration may materialize implied components as stubs"). Exists so the plan and OQ resolve to a live home. **No citations or semantic claims yet** — the next `harvester` refines it in place (`stub` → `rough-in` → `firm`).

## What this will be

The L2 **outer-driver** framing of `ksp_solve` — the non-identity composition *above* the firm L1 operator [`L1/ksp_solve`](../L1/ksp_solve.md): the restart / convergence-test loop that wraps the [`krylov-step`](./krylov-step.md) kernel into a complete solve. This is the substantive L2 coverage gap (distinct from the L1 entry, which collapses the whole method body to `ksp_solve(solver, b) → x`); naming it as an L2 composition gives the per-solver pipelines a shared L2 wrapper.

## Implied by

- Plan (`scaffolding/priorities.md`) Backlog High-fan-out item **ksp-solve-l2-promotion-non-identity-substantive-gap**.
- OQ `ksp-solve-l2-promotion-non-identity-substantive-gap`.
- Firm [`L1/ksp_solve`](../L1/ksp_solve.md) + concept [`concepts/ksp_solve`](../concepts/ksp_solve.md); the L0 anchor [`L0/linalg-iterative-file`](../L0/linalg-iterative-file.md) (the three `Mult` bodies are `for`-loops over a `krylov-step` kernel wrapped by convergence + per-restart logic).

## Refinement pending

- **Owner:** `harvester`.
- **Plan:** Backlog High-fan-out `ksp-solve-l2-promotion-non-identity-substantive-gap`.
- **OQs:** `ksp-solve-l2-promotion-non-identity-substantive-gap`.
- Establishes the non-identity L2↔L1 relationship (the L3>L2 `krylov-step-body-identity` theme is identity; this outer-driver wrap is NOT).
