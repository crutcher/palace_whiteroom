---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L4/eigsolve
    - L4/fold_solve
    - L4/frequency_sweep
    - L4/ksp_solve
    - L4/preconditioning-framework
    - L4/solve_family
---

# L4 — Outer-driver caps & coordination combinators

The outer-coordination vocabulary at L4: the `Solve = StateT SimState Identity` outer-driver caps that wrap a single solve, and the map/fold coordination combinators that sit one shell further out and drive a *family* of solves. These compose strictly above the iteration-structural kernels (the `iterate_while` family) — the kernels fold per-step; these caps and shells coordinate the restart / convergence structure and the family iteration around them.

- **Caps** — [`ksp_solve`](./ksp_solve.md) (the preconditioned-Krylov outer-driver cap, assembling the `solve_loop` / `restart_cycle` / `Outcome` vocabulary and folding `krylov_step`) and [`eigsolve`](./eigsolve.md) (the generalized-eigenproblem cap, a role-naming `EigOutcome`-wrapper over an opaque-library obstruction marker — the eigen-iteration is library-owned, so the cap marks the `sequential-obstruction` rather than rendering a Palace loop).
- **Coordination combinators** — the two children of the strawman §3.7 `iterate_while` family (a map is the degenerate fold whose step ignores the accumulator; there is no third parent above them):
  - [`solve_family`](./solve_family.md) — the fixed-operator **map** over an RHS family (`SetOperators` hoisted outside the loop; electrostatic + magnetostatic).
  - [`frequency_sweep`](./frequency_sweep.md) — the operator-varying **map** over a frequency family (the operator rebuilt INSIDE the map; the driven uniform sweep).
  - [`fold_solve`](./fold_solve.md) — the state-threaded **fold** over a time/sweep schedule (each step's input is the prior step's output; transient + driven-PROM SweepAdaptive).

The `Solve`-monad outer-driver vocabulary anchors (`solve_loop`, `restart_cycle`, `Outcome`, `EigOutcome`) that the caps consume have no standalone chapters — they live in the [Overview](./index.md) dep-map. Chapters are alphabetical within this group.
