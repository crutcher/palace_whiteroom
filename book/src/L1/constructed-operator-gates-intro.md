# L1 — Constructed-operator gates

The **constructed-operator absorption** motif (index motif 4): forms whose primary argument is a structured opaque value — a `Solver[A]`, `EigSolver`, `ChebSmoother`, `JacobiSmoother`, `DivFreeProjector`, or `FloquetCorrector` — whose per-method body, preconditioner, tolerances, and iteration cap are bound at construction. The L1 signature is variant-free; the per-method body unfolds at L2 (`krylov-step`). Results are structured values, not L0 in-place destinations + side-effect loggers + mutating counters.

The six gates, in increasing internal richness: `jacobi-smoother` (thinnest — one elementwise product, no sweep), `chebyshev-smoother` (fixed-degree polynomial action), `ksp_solve` (solve-to-convergence), `eigsolve` (composes `ksp_solve` for spectral-transform modes — first two-layer constructed-operator absorption), `divfree-projector` and `floquet-correction` (the `nested-constructed-operator-gate` shape — the closure carries another `Solver[·]` as a sub-field).

Chapters are listed alphabetically.
