---
edges:
  reference:
    - concepts/givens_apply
    - concepts/givens_generate
    - concepts/sequential-obstruction
    - L2/incremental_least_squares
    - L2/krylov_step
---

# Plane-rotation stream

A **plane-rotation stream** is the sequential per-step generation and application of Givens rotations against an incrementally-arriving upper-Hessenberg (or upper-bidiagonal) column, with the rotation stream itself stored as paired $(c, s)$ arrays rather than as an explicit unitary factor.

## Shape

For each step $k = 0, 1, 2, \ldots$ producing a column $H[\cdot, k]$ of length $k+2$ (or a bidiagonal column of length 2):

1. **Replay**: apply stored rotations $(c_0, s_0), \ldots, (c_{k-1}, s_{k-1})$ to entries $H[0..k, k]$ in order — using [`givens_apply`](./givens_apply.md).
2. **Generate**: produce $(c_k, s_k)$ from the resulting $(H[k, k], H[k+1, k])$ pair — using [`givens_generate`](./givens_generate.md).
3. **Apply-to-self**: apply $(c_k, s_k)$ to $(H[k, k], H[k+1, k])$, zeroing the sub-diagonal.
4. **Propagate**: apply $(c_k, s_k)$ to the running RHS pair $(\bar{g}[k], \bar{g}[k+1])$.
5. **Read**: the new RHS tail $|\bar{g}[k+1]|$ is the least-squares residual norm at step $k+1$.

The stream's combined effect is to maintain $R_k = \text{upper-tri}(H[0..k, 0..k])$ and $\bar{g}_k$ such that the least-squares problem $\min_y \|\bar{H}_k y - \beta e_1\|$ has solution $y_k = R_k^{-1} \bar{g}_k[0..k]$ with residual $|\bar{g}_k[k]|$ — all without forming or storing the orthogonal factor explicitly.

## Background

The stream pattern is the standard implementation technique for least-squares-on-Krylov solvers (Saad 2003, §6.5.3 for GMRES; Paige & Saunders 1975 for MINRES; Paige & Saunders 1982 for LSQR). It is preferred over forming $Q_m$ explicitly because (a) the storage is $O(m)$ rather than $O(m(m+1)/2)$, (b) the application cost per step is $O(k)$ which matches the Arnoldi cost, and (c) the residual norm is available cheaply at every step without solving the least-squares system.

## Sequential character

The replay step (1) is a length-$k$ chain of 2-vector updates, each reading the output of the previous. This is a [`sequential-obstruction`](./sequential-obstruction.md) candidate when lifting to L3; the chain has no obvious global tensor form. The generate (2), apply-to-self (3), propagate (4), and read (5) steps are pointwise.

## Variants the stream is invariant to

The stream pattern does not depend on:

- The orthogonalization scheme producing the column (MGS, CGS2, householder-Arnoldi all produce a column with non-zero sub-diagonal that the stream then reduces).
- Whether the underlying solver is preconditioned, flexibly preconditioned, or unpreconditioned.
- Whether the Krylov space is restarted (the stream re-initializes per restart cycle).

This invariance is what makes the stream a candidate shared concept across GMRES, FGMRES, MINRES, and LSQR slices.

## Used in

- [`incremental_least_squares`](../L2/incremental_least_squares.md) — primary (canonical) firm dissection of the stream as it appears in GMRES/FGMRES.
- [`krylov_step` (GMRES instance)](../L2/krylov_step.md) — consumer (per-step driver and back-solve).
