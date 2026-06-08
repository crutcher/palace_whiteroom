---
edges:
  reference:
    - L1-L0/triangular-solve-obstruction   # the disposition: a general trsv has NO positive
                                            # Palace L0 site — it is an obstruction theme.
    - L1/back_solve                         # the one positively-anchored triangular component
                                            # Palace DOES implement (small-dense GMRES/FGMRES
                                            # restart back-substitution); the sibling of a general trsv.
---

# trsv

Base primitive: triangular solve `T · y = b` for a triangular matrix `T` and conforming vectors `b`, `y`. The BLAS-2 routine `?trsv`.

## Disposition: no L1 home — obstruction + a positively-anchored sibling

A **general** triangular solve (`trsv` / `trsm` / `SpTrSV`, sparse or dense, acting on the
length-`N` field) has **no positive Palace source site** and gets **no L1 operator** — this is
the settled disposition, documented by the L1>L0 obstruction theme
[`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md) (`obstruction`):
every triangular substitution that occurs in a Palace run lives inside opaque
library calls (HYPRE GS/SSOR relaxation selected by an integer enum, forward/back substitution
inside external MUMPS/SuperLU/STRUMPACK factorizations), and Palace-authored smoothers are
deliberately GS-free (Jacobi + Chebyshev only, citing Adams et al. 2003). Per CLAUDE.md §Scope an
unimplemented Palace component is not a direct implementation target, so no constructive `trsv`
L1 form is proposed.

The **one** triangular-solve component Palace *does* implement positively is the small-dense
GMRES/FGMRES restart-correction back-substitution — the firm L1 leaf
[`back_solve`](../L1/back_solve.md). It solves the dense upper-triangular `R · y = s` over
the small running-QR R-factor (coordinate space, dimension `j+1` ≤ `max_dim`, no collective), and
is the *small-dense-triangular* sibling of [`lu_solve`](../L1/lu_solve.md). It is **not** a
general `trsv` (which would act on the length-`N` field). This concept page is therefore a
non-node pointer to those two homes: the obstruction theme (the resolution for the general case)
and `back_solve` (the positively-anchored special case).

## Contract

- Reads `T` and `b`; writes `y` (or, by in-place convention, overwrites `b` with `y`).
- The triangle (upper/lower) and the diagonal (unit/non-unit) are parameters.
- Sequentially dependent: solving for `y[k]` requires `y[0..k-1]` (for lower triangular). At L3 this is an obstruction — `trsv` does not lift to a tensor-field operation without algorithmic change (e.g., level-set or block-Jacobi triangular preconditioning).
- Numerical: ill-conditioned or near-singular `T` produces large `y`; the caller is responsible for guarding against it.

## Role in higher-layer rotations

In GMRES, [`back_solve`](../L1/back_solve.md) is one `trsv` against the upper-triangular block of `H̄_j` (produced by replayed Givens rotations) with RHS `s[0..j]`. The size is `O(max_dim)`, which is small (default 30), so the primitive's serial cost is irrelevant.

## Palace mapping

- The GMRES/FGMRES restart back-substitution loop in `palace/linalg/iterative.cpp:652-660` (GMRES) / `:831-840` (FGMRES) — the positively-anchored small-dense case, firm at L1 as [`back_solve`](../L1/back_solve.md).
- The **general** `trsv` (sparse / large-field) has no Palace site: see the obstruction theme [`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md) for the exhaustive negative anchors (HYPRE-internal GS/SSOR, external direct-solver factorizations, the GS-free Palace smoother cohort).
