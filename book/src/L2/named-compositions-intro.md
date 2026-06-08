---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L2/deflate
    - L2/eigsolve
    - L2/incremental_least_squares
    - L2/ksp_solve
    - L2/orthogonalize
---

# L2 named compositions

A single Palace runtime-dispatched entry point unfolds into a **canonical pipeline** of
L1 leaves (or, one tier up, of other L2 compositions) under a **named L2 surface** — the
opaque parameter that selected a variant is turned into the visible per-variant sequencing.

- [`orthogonalize`](./orthogonalize.md) — the Gram-Schmidt `project ▷ subtract` composition
  (`dot` ▷ `axpy`); names the `gs_orthog ∈ {MGS, CGS, CGS2}` parameter as the
  collective-shape residual axis. First named-composition exemplar.
- [`incremental_least_squares`](./incremental_least_squares.md) — the GMRES / FGMRES
  running-QR / Givens-stream small-dense LS update (`replay ▷ generate ▷ apply ▷ apply_rhs`
  ▷ back-solve); FIXED sub-step sequence (replay-before-generate non-commutative).
- [`ksp_solve`](./ksp_solve.md) — the **outer-driver** wrap: the restart / convergence-test
  `iterate_while` fold of the `krylov_step` kernel into a complete solve. Composes one tier
  up (over `krylov_step`, not its L1 primitives); establishes the non-identity L2↔L1 hop.
- [`eigsolve`](./eigsolve.md) — the shift-invert spectral-transform application
  `apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)`; the per-step body the opaque-library
  eigen-iteration folds (the fold stays library-owned — load-bearing for the L3
  `partial-obstruction`).
- [`deflate`](./deflate.md) — the oblique / Galerkin complementary projector
  `I − X(XᴴX)⁻¹Xᴴ`; the `coords ▷ schur-solve ▷ back-project` composition over `gram` +
  `lu_solve` + `linear_combination` + `dot`. **Over-unification guard:** NOT the same as
  `orthogonalize` (which is `deflate` at `gram = I`) — the `(XᴴX)⁻¹` Gram solve is
  load-bearing.

Four `firm`; [`deflate`](./deflate.md) is `partly-constructive` (firm Schur-form pipeline +
a constructive bare-Galerkin core with a stated positive-source promotion condition).
Chapters are alphabetical.
