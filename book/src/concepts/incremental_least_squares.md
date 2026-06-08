---
edges:
  reference:
    - L1/ls_update_column
    - concepts/givens
    - concepts/orthogonalization
---

# Incremental least-squares update

GMRES (and its flexible / restarted cousins) reduces to a sequence of least-squares problems

```
min_y  ‖β·e₁ − H̄_j · y‖₂      for j = 0, 1, 2, ...
```

where `H̄_j` is the `(j+2) × (j+1)` upper-Hessenberg matrix produced by Arnoldi. The naïve implementation re-factorises `H̄_j` at every step; the standard implementation maintains a *running QR factorisation* and exposes `β = |s[j+1]|` (the LS residual at step `j`) as a free byproduct of the update — no explicit `y` solve is needed to test convergence.

At L1 this is a single operation:

```
ls_update_column(K, j, h_new) -> K'
```

Its contract:
- input: a `Krylov` bundle carrying the previously-recorded rotation registers `(cs, sn)`, the RHS `s`, and the LS-problem residual proxy `β`;
- input: a freshly-orthogonalised Hessenberg column `h_new` of length `j+2`;
- output: a `Krylov'` where `h_new` has been triangularised in place into the upper-Hessenberg `H`, one new rotation `(cs[j], sn[j])` has been recorded, the RHS `s` has been advanced, and `K.beta = |s[j+1]|` is the LS residual.

What is *hidden* at L1:
- the Givens-rotation kernels (`GeneratePlaneRotation`, `ApplyPlaneRotation`) and their LAPACK-style scaled implementations;
- the bookkeeping that replays prior rotations on the new column before generating the new one;
- the LS residual being read off the RHS rather than computed by an explicit residual evaluation.

These are L2 mechanism. At L1 the role of the operation is "incremental triangularisation of the LS system, with the LS residual exposed as side-output."

## Why this is its own concept

Multiple iterative methods will reuse this pattern: GMRES, FGMRES, and (with a different basis-construction prefix) MINRES, LSQR, LSMR. The role — *incremental triangularisation maintaining residual as a free byproduct* — is shared even when the rotation kernels differ. Naming the role at L1 lets each method's L1 form stay shape-stable; the L2 form pins the specific kernel.

## Dependencies

- L2 realisation depends on [`givens`](./givens.md) (the scalar kernel pair: generate + apply).
- Closely coupled with `orthogonalization` (which produces the input column `h_new`) but neither concept subsumes the other.
