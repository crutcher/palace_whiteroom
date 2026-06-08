---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/chebyshev-smoother
    - L1/divfree_projector
    - L1/eigsolve
    - L1/floquet_correction
    - L1/jacobi-smoother
    - L1/ksp_solve
---

# L1 — Constructed-operator gates

The **constructed-operator absorption** motif (index motif 4): forms whose primary argument is a structured opaque value — a `Solver[A]`, `EigSolver`, `ChebSmoother`, `JacobiSmoother`, `DivFreeProjector`, or `FloquetCorrector` — whose per-method body, preconditioner, tolerances, and iteration cap are bound at construction. The L1 signature is variant-free; the per-method body unfolds at L2 (`krylov_step`). Results are structured values, not L0 in-place destinations + side-effect loggers + mutating counters.

The six gates, in increasing internal richness: `jacobi-smoother` (thinnest — one elementwise product, no sweep), `chebyshev-smoother` (fixed-degree polynomial action), `ksp_solve` (solve-to-convergence), `eigsolve` (composes `ksp_solve` for spectral-transform modes — first two-layer constructed-operator absorption), `divfree_projector` and `floquet_correction` (the `nested-constructed-operator-gate` shape — the closure carries another `Solver[·]` as a sub-field).

Chapters are listed alphabetically.
