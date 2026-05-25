# GMRES (concept)

Generalized Minimum Residual method. See [the gmres slice](../spec/slices/gmres.md) for the L1 mathematical statement and the slice's progression up the layer stack.

## What GMRES is

A Krylov-subspace iterative method for solving $Ax = b$ where $A$ is a general nonsingular linear operator. At step $m$, GMRES produces the iterate $x_m \in x_0 + \mathcal{K}_m(A, r_0)$ that minimizes the 2-norm of the residual over that affine Krylov subspace.

The **minimum-residual property** is the defining feature: residual norms are monotone-non-increasing by construction, in contrast to CG (which minimizes a different functional and applies only to SPD systems) or BiCGStab (which minimizes nothing and has erratic residual behavior).

## Position in the vocabulary

GMRES sits one level above the Arnoldi process: GMRES = Arnoldi (to build an orthonormal Krylov basis) + a small least-squares problem (to pick the minimizing iterate within the basis). The least-squares solve is performed incrementally as the basis grows.

- **Builds on:** [orthogonalization](./orthogonalization.md) (used inside Arnoldi to grow the basis), [apply_linop](./apply_linop.md) (one matvec per step), [variant absorption](./variant-absorption.md) (preconditioner side, restart, flexibility).
- **Composes into:** outer nonlinear / time-stepping loops that call GMRES as their linear-solve subroutine.

## Variant axes

- **Preconditioner side.** Left ($M^{-1}A$), right ($AM^{-1}$), or none. Resolved at solve start via a [constructed operator](./constructed-operators.md) so the inner loop is variant-uniform.
- **Restart length.** Full GMRES ($m$ grows unboundedly) vs. restarted GMRES($k$) (restart every $k$ steps). Trades convergence quality for bounded memory.
- **Flexibility.** Fixed $M$ vs. per-step $M_j$ (FGMRES). Allows the preconditioner to itself be a nonlinear or iterative process.
- **Orthogonalization.** The Arnoldi-internal choice; see the [orthogonalization](./orthogonalization.md) concept and the [orthog](../spec/slices/orthog.md) slice.
