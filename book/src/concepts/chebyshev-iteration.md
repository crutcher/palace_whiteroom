# Chebyshev iteration

A polynomial iteration for the linear system $A x = b$ (and the closely related polynomial smoother / polynomial preconditioner setting) that, given a containing interval $[\lambda_{\min}, \lambda_{\max}] \supseteq \mathrm{spec}(A)$ for a symmetric positive-definite operator $A$, applies a sequence of three-term recurrence updates such that after $k$ steps the residual polynomial $p_k(A) r_0$ achieves the minimax error reduction over $[\lambda_{\min}, \lambda_{\max}]$.

## What it computes

The iterate after $k$ steps satisfies $r_k = T_k(\hat A) \, r_0 / T_k(\hat 0)$ where $T_k$ is the Chebyshev polynomial of the first kind of degree $k$ and $\hat A$ is $A$ shifted-and-scaled to map $[\lambda_{\min}, \lambda_{\max}]$ to $[-1, 1]$. The error reduction factor is $2 \rho^k / (1 + \rho^{2k})$ with $\rho = (\sqrt{\kappa} - 1)/(\sqrt{\kappa} + 1)$ and $\kappa = \lambda_{\max}/\lambda_{\min}$.

## What distinguishes it from CG

CG also achieves a Chebyshev-like minimax bound, but discovers the Krylov subspace adaptively via inner products. Chebyshev iteration uses a *fixed* polynomial determined by the supplied interval — no inner products are required, only `axpy`/`apply_linop`. This is the key property:

- **Inner-product-free**: every step is `axpy` + `apply_linop`. No global reductions.
- **Communication-light**: ideal as a smoother in geometric/algebraic multigrid, especially on GPUs and distributed-memory systems where the dot-product reduction in CG is a synchronization bottleneck.
- **Requires spectral interval**: the user must supply $[\lambda_{\min}, \lambda_{\max}]$; this is typically obtained via a few steps of Lanczos or via theoretical bounds for structured operators.

## Common uses

- **Polynomial smoother** in multigrid (most common modern use): a few steps of degree-$k$ Chebyshev to smooth high-frequency error on each level, with the interval covering the high-end-of-spectrum to be smoothed.
- **Polynomial preconditioner**: apply $p(A)$ as a preconditioner for an outer Krylov method.
- **Standalone solver**: when the inner-product cost dominates and a good spectral bound is available.

## L1 ingredients

- Operator application `apply_linop(A, ·)`.
- Vector updates `axpy`, `scal`, optionally a saved-previous-iterate buffer for the three-term recurrence.
- The Chebyshev recurrence coefficients $(\alpha_k, \beta_k)$ derived from the interval — computed in closed form, no inner products.

## Relation to other concepts

- An inner-product-free counterpart to CG; see the `cg` slice for the inner-product-bearing alternative.
- A consumer of `apply_linop` and `axpy`; does NOT consume `dot` or `nrm2` (the latter only optionally for diagnostics).
- A common ingredient in multigrid smoother layers — see future multigrid slice.
- The spectral interval $[\lambda_{\min}, \lambda_{\max}]$ is typically obtained from a `lanczos-spectral-estimate` step (future concept) or from theory.
