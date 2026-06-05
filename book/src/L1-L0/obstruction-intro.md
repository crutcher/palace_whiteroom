---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1-L0/bicgstab-iteration
    - L1-L0/fe-assemble-libceed-boundary-obstruction
    - L1-L0/minres-iteration
    - L1-L0/triangular-solve-obstruction
---

# L1 > L0 — Obstruction themes

Claim-free obstruction documentation: themes where the L1 form has **no positive Palace L0 realisation**, with negative-anchor citations cataloguing the boundary so future producers don't re-localize. Two sub-kinds (per CLAUDE.md §Methodology invariants):

- **`enum-only-stub`** — Palace names the functionality in its configuration surface but the method body is `MFEM_ABORT` / `// TODO`: `minres-iteration`, `bicgstab-iteration` (both route to `MFEM_ABORT` at `palace/linalg/ksp.cpp:53-57`). Promotion route: a future Palace upstream change fills the body.
- **`opaque-library-ownership`** — the functionality is available to Palace only through a library boundary, never as a standalone Palace callable: `triangular-solve-obstruction` (HYPRE GS/SSOR relax-types + external direct-solver wrappers) and `fe-assemble-libceed-boundary-obstruction` (the libCEED element-local quadrature kernel below the firm `fe_assemble` fold). Promotion route: none conventional — the theme's value is documenting the boundary.

Themes are listed alphabetically.
