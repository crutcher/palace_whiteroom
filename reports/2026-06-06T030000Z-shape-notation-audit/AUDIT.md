# Shape-notation audit: `Tensor[N]`-as-same-shape vs genuine rank-1

**Date:** 2026-06-06
**Scope:** READ-ONLY classification of `Tensor[N]` (and `Tensor[M]`, `Tensor[m]`, `Tensor[N, complex]`, `ComplexTensor[N]`, "share the length axis N" prose) across `book/src/`.
**Authoritative reference:** `book/src/design/l4_calculus.md` §1.2.1 (named shape groups).
**Excluded (handled separately):** the `linear_combination` cohort — `L4/L3/L2/linear_combination.md`, `L2-L1/linear-combination-fold-specialization.md`, and every `[(Scalar, Tensor[N])]` / `(Tensor[N], +)` term-list-monoid reference (these appear inside `L2/elementwise_product.md`, `L2/inner_product.md`, `L2/folds-intro.md`, `L2/index.md` discussing the fold cohort).
**No edits were made.**

## Core rule applied

- **FIX** = the op is shape-generic (element-local / whole-tensor / whole-tensor reduce) and the bare `Tensor[N]` is purely a *same-shape congruence stand-in* that accidentally pins operands to rank-1. Target: `Tensor[(S: ...)]` for the first binder, `Tensor[S]` for re-uses; or reuse `σ`. Lives at **L4 / L3 / L2** (the calculus layers).
- **KEEP** = `Tensor[N]` genuinely denotes a flat rank-1 dof-vector. Always KEEP at **L1 / L0** (Palace `Vector` IS rank-1). Also KEEP genuine rank-1 lists at any layer (eigenvalue list `Tensor[K]`, projection-coeff vector `Tensor[m]`).
- **BORDERLINE** = exact replacement form needs a human decision (multi-axis renderings, the `N`-vs-`M` rectangular operator case).

`σ` (e.g. the calculus doc's `axpy :: Scalar → Tensor[σ] → Tensor[σ] → Tensor[σ]`) is **already correct** — only the bare-`N` renderings leak. The book entries do NOT currently use `σ`; they use bare `Tensor[N]`.

---

## Group: elementwise leaves (BLAS-1, element-local, shape-generic)

These are element-local maps; `result[i] = f(args[i])`. Pure congruence — strongest FIX cohort.

| file:line | layer | current snippet | class | recommended replacement | rationale |
|---|---|---|---|---|---|
| `L2/axpy.md:36` | L2 | `axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` | FIX | `Scalar -> Tensor[(S: ...)] -> Tensor[S] -> Tensor[S]` | element-local `α·x+y`; matches doc's `Tensor[σ]` exemplar exactly |
| `L2/axpby.md:38` | L2 | `axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` | FIX | `... Tensor[(S: ...)] ... Tensor[S] -> Tensor[S]` | element-local `α·x+β·y` |
| `L2/axpbypcz.md:41` | L2 | `axpbypcz :: Scalar -> Tensor[N] -> ... -> Tensor[N]` | FIX | congruence group `S` across all three vector operands + result | element-local 3-term |
| `L2/scal.md:36` | L2 | `scal :: Scalar -> Tensor[N] -> Tensor[N]` | FIX | `Scalar -> Tensor[(S: ...)] -> Tensor[S]` | element-local scale; doc explicitly names `scal` rank-generic |
| `L2/reciprocal.md:94,100,103,354,73` | L2 | `reciprocal :: Tensor[N] -> Tensor[N]`; "single length axis `N`"; "`Tensor[N] -> Tensor[N]`" | FIX | `Tensor[(S: ...)] -> Tensor[S]`; drop "single length axis" → "the shared shape `S`" | element-local self-map; "single length axis N" is the exact leak the directive names |
| `L3/reciprocal.md:35,40,41,27,125,135` | L3 | `reciprocal :: Tensor[N] -> Tensor[N]`; "single length axis `N`" | FIX | same as L2 | identity-in-form to L2; whole-tensor field op |
| `L2/elementwise_product.md:89,95,97,98,106,203,392,58` | L2 | `elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]`; "sharing the length axis `N`" | FIX | `(a: Tensor[(S: ...)], b: Tensor[S]) -> Tensor[S]`; "sharing the shape group `S`" | Hadamard product, element-local; `:106` `ComplexTensor[N]` → `ComplexTensor[(S: ...)]`/`[S]` |
| `L3/elementwise_product.md:36,41,42,43,47,20,28,86,149` | L3 | `(a: Tensor[N], b: Tensor[N]) -> Tensor[N]`; "sharing the length axis `N`"; `d ∈ Tensor[N]` | FIX | same as L2 | identity-in-form to L2 |
| `L1/elementwise_product.md` (all) | L1 | `Tensor[N]` | **KEEP** | — | L1 dof-vector, faithful rank-1 |

Note: the elementwise leaves at L2/L3 also appear in the dep-map cells of `L2/index.md` / `L3/index.md` (below).

## Group: fused composite — normalize

| file:line | layer | current snippet | class | recommended replacement | rationale |
|---|---|---|---|---|---|
| `L2/normalize.md:36,45,52,54,145` | L2 | `normalize :: Tensor[N] -> (Scalar, Tensor[N])` | FIX | `Tensor[(S: ...)] -> (Scalar, Tensor[S])` | `nrm2 ∘ scal`, both shape-generic; result vector congruent to input |
| `L3/normalize.md:37,42,44,31,127,137` | L3 | `normalize :: Tensor[N] -> (Scalar, Tensor[N])`; "single length axis `N`" | FIX | same | identity-in-form to L2 |
| `L1/normalize.md:30,35,37,105` | L1 | `Tensor[N]` | **KEEP** | — | L1 dof-vector |

## Group: reduce-to-scalar (whole-tensor reductions)

`dot`/`nrm2`/`inner_product` reduce over the *entire* tensor → result `Scalar`. The reduction is shape-agnostic; `N` only asserts the two operands match.

| file:line | layer | current snippet | class | recommended replacement | rationale |
|---|---|---|---|---|---|
| `L4/dot.md:70,71,80,81,173,206` | L4 | `dot :: Tensor[N] -> Tensor[N] -> Scalar`; `tdot ...` | FIX | `Tensor[(S: ...)] -> Tensor[S] -> Scalar` | whole-tensor inner-product reduce |
| `L3/dot.md:44,45,111` | L3 | `dot :: Tensor[N] -> Tensor[N] -> Scalar` | FIX | same | |
| `L2/dot.md:31,32` | L2 | `dot :: (x: Tensor[N], y: Tensor[N]) -> Scalar` | FIX | `(x: Tensor[(S: ...)], y: Tensor[S]) -> Scalar` | |
| `L1/dot.md` | L1 | `Tensor[N]` | **KEEP** | — | L1 dof-vector |
| `L4/nrm2.md:69,76,160,194` | L4 | `nrm2 :: Tensor[N] -> Scalar` | FIX | `Tensor[(S: ...)] -> Scalar` | norm over whole tensor |
| `L3/nrm2.md:33,115,139` | L3 | `nrm2 :: Tensor[N] -> Scalar` | FIX | same | |
| `L2/nrm2.md:71` | L2 | `nrm2 :: Tensor[N] -> Scalar` | FIX | same | |
| `L1/nrm2.md` | L1 | `Tensor[N]` | **KEEP** | — | L1 dof-vector |
| `L4/inner_product.md:84,85,94,95,263,264,276` | L4 | `inner_product :: Tensor[N] -> Tensor[N] -> Scalar`; `inner_product_M :: Tensor[N] -> LinearOperator[N, N] -> Tensor[N] -> Scalar` | FIX (BORDERLINE on `_M`) | `inner_product :: Tensor[(S: ...)] -> Tensor[S] -> Scalar`; for `_M` see note | the weighted variant couples vector shape `S` to operator `LinearOperator[N,N]` — see BORDERLINE note below |
| `L3/inner_product.md:53,94,95,104,106,201,355,441` | L3 | `inner_product :: Tensor[N] -> Tensor[N] -> Scalar`; `_M` variant | FIX (BORDERLINE on `_M`) | same | |
| `L2/inner_product.md:144,145,154,156,358,433,521` | L2 | `inner_product :: (x: Tensor[N], y: Tensor[N]) -> Scalar`; `_M` variant | FIX (BORDERLINE on `_M`) | same; `:358,433,521` are term-list-monoid `(Tensor[N], +)` references — **EXCLUDED (linear_combination cohort)** | |
| `L2-L1/inner-product-fold-specialization.md:36,37,57,69,70,71,257` | L2-L1 | `inner_product :: (x: Tensor[N], y: Tensor[N]) -> Scalar`; "shared length axis `N`" | FIX (BORDERLINE on `_M`/`bilinear_form`) | vectors → `S`; `:19,23` are term-list references **EXCLUDED** | the aligned-pass precondition prose "`x, y : Tensor[N]` (shared length axis)" is the leak |
| `L1/dot.md`, `L1/nrm2.md`, `L1/...` | L1 | `Tensor[N]` | **KEEP** | — | |

## Group: reduce-to-matrix folds (gram)

| file:line | layer | current snippet | class | recommended replacement | rationale |
|---|---|---|---|---|---|
| `L2/gram.md:43,54,192` | L2 | `gram :: (dot: (Tensor[N], Tensor[N]) -> Scalar, X: Basis[N, k]) -> Matrix[k, k]` | FIX (dot-hook); KEEP (Basis/Matrix) | dot hook → `(Tensor[(S: ...)], Tensor[S]) -> Scalar`; leave `Basis[N, k]` / `Matrix[k, k]` | the `dot` hook's operands are shape-generic; `Basis[N, k]` is k columns of length-N dof-vectors (a genuine 2-D basis, separate `Matrix`/`Basis` notation, not the `Tensor[N]` leak) |
| `L2-L1/gram-fold-specialization.md:39,71,72,73` | L2-L1 | `gram :: (dot: (Tensor[N], Tensor[N]) -> ...`; `dot :: (x: Tensor[N], y: Tensor[N]) -> Scalar`; `bilinear_form :: (x: Tensor[M], M: LinearOperator[M, N], y: Tensor[N]) -> Scalar` | FIX (dot/tdot); BORDERLINE (bilinear_form) | dot/tdot → `S`; bilinear_form see BORDERLINE | |
| `L4/gram_reduce.md:82,104` | L4 | `[Tensor[N]]` — "the solution family xs" | FIX | `[Tensor[(S: ...)]]` (one group across the family) | family of congruent solution vectors; whole-tensor; reduces to `Matrix[k,k]` |

## Group: operator apply (apply_linop — rectangular)

| file:line | layer | current snippet | class | recommended replacement | rationale |
|---|---|---|---|---|---|
| `L3/apply_linop.md:37,44,45,30,59,69,73,146,193` | L3 | `apply_linop :: LinearOperator[M, N] -> Tensor[N] -> Tensor[M]` | BORDERLINE | likely `LinearOperator[(D: ...), (R: ...)] -> Tensor[D] -> Tensor[R]` (two groups: domain `D`, codomain `R`) | NOT pure congruence — domain `N` and codomain `M` are *distinct* shapes the operator maps between; the rank-1 implication is still accidental (an operator can map rank-k→rank-j), but the fix needs TWO named groups, not one. Human call on operator-shape notation |
| `L3/operator-apply-intro.md:16,17` | L3 | `(A: LinearOperator[M, N], x: Tensor[N]) -> Tensor[M]`; `(A: LinearOperator[N, N]) -> Tensor[N]` | BORDERLINE | same domain/codomain-group treatment | `assemble_diagonal` (`:17`) is square `N×N → Tensor[N]`: the output IS the diagonal as a vector congruent to the operator's axis — leans FIX but tied to operator-shape decision |
| `L1/apply_linop.md` | L1 | `Tensor[N]` / `Tensor[M]` | **KEEP** | — | L1 dof-vectors |

## Group: assemble_diagonal (operator-to-data, square)

| file:line | layer | current snippet | class | recommended replacement | rationale |
|---|---|---|---|---|---|
| `L3/assemble-diagonal.md:34,40,20,28,56,130,135` | L3 | `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]` | BORDERLINE | tie to the apply_linop operator-shape decision; if operator axes become groups, output is `Tensor[D]` (the diagonal over the square axis) | output diagonal is congruent to the operator's (square) axis; rank-1 implication accidental but coupled to operator notation. Lean FIX once operator-shape convention is set |
| `L2/assemble-diagonal.md:66,68,90,101,135,395` | L2 | `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]` | BORDERLINE | same | |
| `L1/assemble-diagonal.md` | L1 | `Tensor[N]` | **KEEP** | — | |

## Group: constructed-operator gates (jacobi, chebyshev)

| file:line | layer | current snippet | class | recommended replacement | rationale |
|---|---|---|---|---|---|
| `L3/jacobi-smoother.md:37,43,44,45,57,31,65,141` | L3 | `jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]`; `op.dinv : Tensor[N]` | FIX | `(op: JacobiSmoother[S], x: Tensor[(S: ...)]) -> Tensor[S]`; `op.dinv : Tensor[S]` | apply is ONE elementwise product `dinv ⊙ x` — element-local, shape-generic; `dinv` congruent to `x` |
| `L2/jacobi-smoother.md:95,104,111,114,137,456,48` | L2 | same | FIX | same | |
| `L1/jacobi-smoother.md` | L1 | `Tensor[N]` | **KEEP** | — | |
| `L3/chebyshev.md:129,140,141,146,183` | L3 | `op.dinv : Tensor[N]`; `x,y : Tensor[N]`; "fields `r, d, y : Tensor[N]`" | FIX | `Tensor[S]` (one group across `x`,`y`,`dinv`,`r`,`d`,`y'`) | smoother sweep is whole-tensor axpy/elementwise; all fields congruent |
| `L2/chebyshev-iteration.md:50,51,58,66` | L2 | `(op: ChebOp[N], x: Tensor[N], y: Tensor[N], ...) -> Tensor[N]` | FIX | `ChebOp[S]`, `Tensor[(S: ...)]`/`Tensor[S]` | same |
| `L3-L2/chebyshev-nested-recurrence.md:31,122` | L3-L2 | `(op: ChebOp[N], x, y, initial_guess) -> Tensor[N]` | FIX | `ChebOp[S] ... -> Tensor[S]` | same |
| `L1/chebyshev-smoother.md` | L1 | `Tensor[N]` | **KEEP** | — | |

## Group: krylov-step / ksp_solve (solver caps — iterate-stratum vectors)

The iterate-stratum fields (`x`, `r`, `p`, `z`, basis columns) are dof-vectors, but at the calculus layers they are threaded shape-generically. **`L4/krylov-step.md` is already partially converted** (its `CgState` record + `cg_converged` predicate use `Tensor[S]`/`LinOp<S>`), so the remaining `Tensor[N]` prose is an internal inconsistency.

| file:line | layer | current snippet | class | recommended replacement | rationale |
|---|---|---|---|---|---|
| `L4/krylov-step.md:129,130,131,177` | L4 | `x/r/p: Tensor[S]`; `cg_converged :: !CgConfig -> LinOp<S> -> Tensor[S] -> Tensor[S] -> Bool` | **already FIXED** | — (leave) | the converted exemplar — confirms the intended target form |
| `L4/krylov-step.md:76,77` | L4 | `Tensor[N]`-typed iterate-bundle fields (`V`,`Z`,...)`; `SimState ... x: Tensor[N]` | FIX | `Tensor[S]` (match the already-converted record) | inconsistent with lines 129-131; same iterate fields |
| `L3/krylov-step.md:58,92` | L3 | `s.x: Tensor[N]`; `apply_linop ... LinearOperator[N, N] -> Tensor[N] -> Tensor[N]` | FIX | iterate fields → `S`; apply_linop tie to operator-shape decision | |
| `L2/krylov-step.md:62,116` | L2 | "`Tensor[N]`-typed fields (`x`, `r`, ...)"; "`Tensor[N]`-typed vs `Scalar`-typed" | FIX | `Tensor[S]`-typed | |
| `L4/ksp_solve.md:79` | L4 | `SimState ... x: Tensor[N]` | FIX | `x: Tensor[S]` | |
| `L3/ksp_solve.md:60` | L3 | `s.x: Tensor[N]` | FIX | `Tensor[S]` | |
| `L2/ksp_solve.md:46,49,74` | L2 | `ksp_solve :: (K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) -> SolveResult[N]`; `x: Tensor[N]` | FIX (b/x); BORDERLINE (operator axis, SolveResult[N]) | `b`/`x` vectors → `S`; operator-axis tie to apply_linop decision | `SolveResult[N]` parameter is a result-shape tag, decide alongside operator notation |
| `L2-L1/ksp-solve-outer-driver-unfold.md:28,45,48` | L2-L1 | `ksp_solve :: (K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) -> SolveResult[N]`; `x: Tensor[N]` | FIX (b/x) | same | |
| `L3-L2/ksp-solve-outer-driver.md:45` | L3-L2 | `ksp_solve :: (..., b: Tensor[N]) -> SolveResult[N]` | FIX (b) | same | |
| `L4-L3/krylov-step-typed-wrapper-dissolution.md:210` | L4-L3 | `apply_linop : LinOp -> Tensor[N] -> Tensor[N]` (audit prose) | FIX | `Tensor[S]` | descriptive use in audit narration |
| `L3-L2/krylov-step-body-identity.md:109` | L3-L2 | `apply_linop :: LinearOperator[N, N] -> Tensor[N] -> Tensor[N]`; `axpy :: Scalar -> Tensor[N] -> ...` | FIX (axpy vectors); BORDERLINE (operator) | vectors → `S` | |
| `L2-L1/krylov-step-kernel-defusion.md:66-72` | L2-L1 | `apply_linop`/`axpy`/`axpby`/`axpbypcz`/`dot`/`nrm2`/`scal` all `Tensor[N]` | FIX (all the BLAS-1); BORDERLINE (apply_linop operator) | the whole defusion signature block → `S` | a single congruent block; the cleanest mass-FIX site |
| `concepts/krylov.md:35,36,37,45,46,47,57,58,70,71,78` | concept | `r,p,z?,V,Z? : Tensor[N]` / `[Tensor[N]]` | FIX | `Tensor[S]` / `[Tensor[S]]` | the `Krylov` record fields are iterate-stratum vectors; calculus-layer concept page |
| `concepts/sim-state.md:33,43` | concept | `x : Tensor[N]` (the current iterate) | FIX | `Tensor[S]` | matches the already-converted `L4/krylov-step` `SimState.x` intent |
| `L1/ksp_solve.md`, `L1/axpy.md`, etc. | L1 | `Tensor[N]` | **KEEP** | — | L1 dof-vectors |

## Group: orthogonalize / deflate (basis-using compositions)

| file:line | layer | current snippet | class | recommended replacement | rationale |
|---|---|---|---|---|---|
| `L2/orthogonalize.md:83,92,97,102,103,105` | L2 | `orthogonalize :: (op, w: Tensor[N], V: Basis[N, m]) -> { residual: Tensor[N], coeffs: Tensor[m] }`; `op.dot : (Tensor[N], Tensor[N]) -> Scalar` | FIX (`w`,`residual`,dot-hook); **KEEP (`coeffs: Tensor[m]`)**; KEEP (`Basis[N,m]`) | `w`/`residual` → `Tensor[(S: ...)]`/`Tensor[S]`; dot hook → `S`; leave `coeffs: Tensor[m]` | `w` and `residual` are congruent dof-vectors (FIX); **`coeffs` is a genuinely 1-D coefficient vector of length m (KEEP)**; `Basis[N,m]` is a 2-D basis (separate notation) |
| `L3/orthogonalize.md:129,133,138,141,173` | L3 | same shape | FIX (`w`/`residual`/dot); KEEP (`coeffs: Tensor[m]`) | same | `:141` `coeffs : Tensor[m]` KEEP |
| `L2-L1/orthogonalize-composition-lowering.md:32,61,82,83` | L2-L1 | `w/residual: Tensor[N]`; `coeffs/H: Tensor[m]`; `dot`/`axpy : Tensor[N]` | FIX (`w`/`residual`/dot/axpy); KEEP (`Tensor[m]`) | vectors → `S` | |
| `L3-L2/orthogonalize-variant-split.md:98` | L3-L2 | `w/residual: Tensor[N]`; `coeffs: Tensor[m]` | FIX (`w`/`residual`); KEEP (`Tensor[m]`) | |
| `L2/deflate.md:56,58,71,87,88,423` | L2 | `deflate :: (op, X: Basis[N, k], v: Tensor[N]) -> Tensor[N]`; `dot: (Tensor[N], Tensor[N]) -> Scalar` | FIX (`v`/result/dot-hook); KEEP (`Basis[N,k]`) | `v`/result → `Tensor[(S: ...)]`/`Tensor[S]`; dot hook → `S` | `v` and the deflated result are congruent dof-vectors |
| `L2-L1/deflate-composition-lowering.md:82,84` | L2-L1 | same | FIX (`v`/result/dot); KEEP (`Basis`) | |

## Group: divfree-projector (Nedelec field — distinct named axes already)

| file:line | layer | current snippet | class | recommended replacement | rationale |
|---|---|---|---|---|---|
| `L2/divfree-projector.md:89,106,109,113,134,251` | L2 | `divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Tensor[N_nd]) -> Tensor[N_nd]`; `Z_S : Tensor[N_h1] -> Tensor[N_h1]` | BORDERLINE | optionally `Tensor[(S_nd: ...)]` / `Tensor[(S_h1: ...)]` if rank-genericity wanted | `N_nd`/`N_h1` already distinguish two FE-space axes (Nedelec vs H1) and the prose treats them as field-space dimensions; the "accidental rank-1" risk is lower because the names are descriptive, but they ARE still flat-length stand-ins. Human call on whether FE-space fields get groups |
| `L2-L1/divfree-projector-leaf-identity.md:78,95,107,127` | L2-L1 | `Tensor[N_nd]` / `Field[N_nd]` | BORDERLINE | same | the `Tensor`/`Field` duality is already notational |
| `L1/divfree-projector.md` | L1 | `Tensor[N_nd]` | **KEEP** | — | L1 dof-vector |

## Group: eigsolve (eigenpair lists — genuine rank-1)

| file:line | layer | current snippet | class | recommended replacement | rationale |
|---|---|---|---|---|---|
| `L4/eigsolve.md:58` | L4 | `apply_shift_invert :: OpParams -> Tensor[N] -> Tensor[N]` | FIX | `Tensor[(S: ...)] -> Tensor[S]` | per-vector shift-invert apply — shape-generic operator action |
| `L4/eigsolve.md:68` | L4 | `pairs: [(λ: Complex, x: Tensor[N, complex])]`; `error: Tensor[K, real]` | BORDERLINE (`x`); **KEEP (`error: Tensor[K, real]`)** | `x` → `Tensor[(S: ...), complex]` or `ComplexTensor[(S: ...)]`; leave `Tensor[K, real]` | the eigenvector `x` is a congruent field-vector (FIX-leaning, but the trailing `complex` element-axis makes the exact rendering a judgment call); **`error: Tensor[K, real]` is a genuine length-K list of per-pair errors (KEEP)** |
| `L3/eigsolve.md:71,72` | L3 | `v: Tensor[N, complex]`; result `v': Tensor[N, complex]`; "Same length axis `N`" | BORDERLINE | `ComplexTensor[(S: ...)]` / `Tensor[(S: ...), complex]` | per-step shift-invert vector; congruence with element-type axis — exact form is a human call |
| `L2/eigsolve.md:68,84,85` | L2 | `apply_shift_invert :: (op, v: Tensor[N, complex]) -> Tensor[N, complex]` | BORDERLINE | same | |
| `L2-L1/eigsolve-spectral-transform-composition.md:49,84,85` | L2-L1 | `v: Tensor[N, complex]`; `apply_linop ... Tensor[N]`; `ksp_solve ... b: Tensor[N]` | FIX (apply_linop/ksp_solve vectors); BORDERLINE (`Tensor[N, complex]`) | vectors → `S` | |
| `L1/eigsolve.md:46,49,53` | L1 | `eigenvalues : Tensor[K, complex]`; `eigenvectors : Tensor[K, N, complex]`; `error : Tensor[K, real]` | **KEEP** | — | L1 + genuine list axes: `K` is the eigenpair count (rank-1 list); `eigenvectors` `[K, N]` is K dof-vectors |
| `L1-L0/eigsolve-mutation-rotation.md:42,43,46` | L1-L0 | same as L1/eigsolve | **KEEP** | — | L1-L0 layer; genuine list + dof axes |
| `feature/eigenmode.L1.md:40` | feature(L1) | `eigenvalues : Tensor[K, complex]`, `eigenvectors : Tensor[K, N, complex]` | **KEEP** | — | L1 feature surface; genuine list/dof axes |

## Group: eliminate_bc / sparameter_reduce (L4 feature-surface)

| file:line | layer | current snippet | class | recommended replacement | rationale |
|---|---|---|---|---|---|
| `L4/eliminate_bc.md:87,88,113,116,118,37,366` | L4 | `eliminate_rhs :: LinearOperator[N, N] -> Tensor[N] -> Tensor[N] -> ... -> Tensor[N]`; `x_bc: Tensor[N]`; `b: Tensor[N]` | FIX (`x_bc`,`b`,result vectors); BORDERLINE (operator axis) | the three RHS-side vectors (`x_bc`, `b`, result) are congruent dof-vectors → `S`; operator `LinearOperator[N,N]` tie to apply_linop decision | RHS-side is whole-tensor subtract-the-forcing; congruent vectors |
| `L4/sparameter_reduce.md:76,97` | L4 | `[(Int, Tensor[N])]` — the driven solution family | FIX | `[(Int, Tensor[(S: ...)])]` (one group across the family) | family of congruent driven solution field-vectors; reduces to `Matrix[p,p]` |

## Group: dep-map / index tables (cells mirror the entry signatures)

These restate the per-op signatures inside `index.md` dep-map cells; classification follows the owning op above. FIX the calculus-layer cells whose op is FIX; the `[(Scalar, Tensor[N])]` cells are EXCLUDED (linear_combination).

| file:line | layer | content | class | rationale |
|---|---|---|---|---|
| `L3/index.md:42,43,45,52,53,54,60,61,69` | L3 | dep-map signatures for `dot`/`inner_product`/`nrm2`/`elementwise_product`/`normalize`/`reciprocal`/`apply_linop`/`assemble-diagonal`/`jacobi-smoother` | FIX (mirror owning entry; apply_linop/assemble-diagonal BORDERLINE) | keep cells consistent with fixed entries |
| `L2/index.md:95,102,113,114,121,123,124,125,132` | L2 | dep-map for `chebyshev`/`gram`(dot-hook)/`dot`/`nrm2`/`deflate`/`ksp_solve`/`orthogonalize`/`divfree` | FIX vectors/dot-hooks; KEEP `Basis`/`Matrix`/`Tensor[m]`; BORDERLINE operator/divfree | `:40,76` are term-list `(Tensor[N], +)` / fold-codomain refs — **EXCLUDED** |
| `L4/index.md:112,117,119,120` | L4 | dep-map for `dot`/`inner_product`/`nrm2`/`sparameter_reduce` | FIX (mirror owning entry) | |
| `L3/blas1-intro.md:25` | L3 | `inner_product` `Tensor[N] -> Tensor[N] -> Scalar` prose | FIX | reduce-to-scalar |
| `L2/folds-intro.md:28` | L2 | `(Tensor[N], +)` term-list monoid | EXCLUDED | linear_combination cohort |

## L1 / L0 confirmation (all KEEP)

Spot-checked and confirmed KEEP (faithful flat rank-1 Palace `Vector`):
`L1/axpy.md`, `L1/dot.md`, `L1/elementwise_product.md`, `L1/normalize.md`, `L1/apply_linop.md`, and all other `L1/*`, `L1-L0/*`. `L0/mfem-vector-types.md:26` explicitly states "At L1 the element-type axis collapses to a single `Tensor[N]`" describing the flat Palace vector — correct, KEEP. No L1/L0 occurrence should change.

---

## Summary

### FIX occurrences by file (calculus layers L4/L3/L2 + L2-L1/L3-L2/L4-L3 + calculus concept pages; linear_combination cohort excluded; counts are the leaking lines, BORDERLINE counted where the leading-`N` vector is clearly a congruence stand-in)

**L4 (7 files):**
- `L4/dot.md` — 6
- `L4/inner_product.md` — 7 (1 `_M` BORDERLINE)
- `L4/nrm2.md` — 4
- `L4/eliminate_bc.md` — 6 (operator BORDERLINE)
- `L4/gram_reduce.md` — 2
- `L4/sparameter_reduce.md` — 2
- `L4/krylov-step.md` — 2 (lines 76-77; rest already fixed)
- `L4/ksp_solve.md` — 1
- `L4/eigsolve.md` — 1 FIX (`:58`) + 1 BORDERLINE (`:68` eigenvector); `error: Tensor[K]` KEEP
- `L4/index.md` — 4 (dep-map cells)

**L3 (12 files):**
- `L3/elementwise_product.md` — 9
- `L3/reciprocal.md` — 6
- `L3/normalize.md` — 7
- `L3/jacobi-smoother.md` — 8
- `L3/chebyshev.md` — 5
- `L3/dot.md` — 3
- `L3/nrm2.md` — 3
- `L3/inner_product.md` — 8 (`_M` BORDERLINE)
- `L3/krylov-step.md` — 2 (1 apply_linop BORDERLINE)
- `L3/eigsolve.md` — 2 (BORDERLINE, complex)
- `L3/orthogonalize.md` — 4 FIX (`coeffs` KEEP)
- `L3/blas1-intro.md` — 1
- `L3/index.md` — ~9 (dep-map cells)
- `L3/apply_linop.md` — 9 (BORDERLINE — operator domain/codomain)
- `L3/assemble-diagonal.md` — 7 (BORDERLINE)
- `L3/operator-apply-intro.md` — 2 (BORDERLINE)

**L2 (16 files):**
- `L2/elementwise_product.md` — ~6 FIX (excl. term-list lines)
- `L2/reciprocal.md` — 6
- `L2/normalize.md` — 5
- `L2/jacobi-smoother.md` — 7
- `L2/chebyshev-iteration.md` — 4
- `L2/dot.md` — 2
- `L2/nrm2.md` — 1
- `L2/inner_product.md` — ~4 FIX (excl. term-list lines; `_M` BORDERLINE)
- `L2/gram.md` — 3 (dot-hook FIX; Basis/Matrix KEEP)
- `L2/orthogonalize.md` — ~5 FIX (`coeffs`/`Basis` KEEP)
- `L2/deflate.md` — ~5 FIX (`Basis` KEEP)
- `L2/scal.md` — 2
- `L2/axpy.md` — 2
- `L2/axpby.md` — 1
- `L2/axpbypcz.md` — 2
- `L2/krylov-step.md` — 2
- `L2/ksp_solve.md` — 3 (operator/SolveResult BORDERLINE)
- `L2/eigsolve.md` — 3 (BORDERLINE, complex)
- `L2/assemble-diagonal.md` — 6 (BORDERLINE)
- `L2/divfree-projector.md` — 6 (BORDERLINE, FE-space axes)
- `L2/index.md` — ~12 FIX (dep-map cells; excl. term-list)

**Lowering layers:**
- `L2-L1/inner-product-fold-specialization.md` — ~7 FIX (excl. term-list)
- `L2-L1/gram-fold-specialization.md` — 3 (bilinear_form BORDERLINE)
- `L2-L1/orthogonalize-composition-lowering.md` — 4 FIX (`Tensor[m]` KEEP)
- `L2-L1/deflate-composition-lowering.md` — 2 FIX (`Basis` KEEP)
- `L2-L1/krylov-step-kernel-defusion.md` — 7 (operator BORDERLINE)
- `L2-L1/ksp-solve-outer-driver-unfold.md` — 3 FIX vectors
- `L2-L1/eigsolve-spectral-transform-composition.md` — 3 (complex BORDERLINE on `v`)
- `L2-L1/divfree-projector-leaf-identity.md` — 4 BORDERLINE
- `L3-L2/chebyshev-nested-recurrence.md` — 2
- `L3-L2/krylov-step-body-identity.md` — 1 FIX vectors (operator BORDERLINE)
- `L3-L2/orthogonalize-variant-split.md` — 1 FIX (`coeffs` KEEP)
- `L3-L2/ksp-solve-outer-driver.md` — 1 FIX (`b`)
- `L4-L3/krylov-step-typed-wrapper-dissolution.md` — 1 FIX

**Calculus concept pages:**
- `concepts/krylov.md` — 11 FIX (iterate-stratum record fields)
- `concepts/sim-state.md` — 2 FIX (`SimState.x`)

### KEEP (do not change)
- **All `L1/*`, `L1-L0/*`, `L0/*`** occurrences (Palace `Vector` is faithful flat rank-1).
- **`Tensor[K, ...]`** eigenpair/error lists (`L1/eigsolve.md`, `L1-L0/eigsolve-mutation-rotation.md`, `feature/eigenmode.L1.md`, and the `error: Tensor[K, real]` field in `L4/eigsolve.md`) — genuine length-K lists.
- **`Tensor[m]`** projection-coefficient vectors in `orthogonalize` (all layers) — genuinely 1-D coefficient vectors.
- **`Basis[N, k/m]`, `Matrix[k, k]`, `Coords[...]`** — distinct 2-D/list notations, not the `Tensor[N]` leak.

### BORDERLINE (need human judgment)
1. **`apply_linop` / `eliminate_bc` / `ksp_solve` operator axes** (`LinearOperator[M, N]`, `LinearOperator[N, N]`): the domain/codomain are *distinct* shapes; fixing needs a TWO-named-group convention (`LinearOperator[(D: ...), (R: ...)]`) or a decision to leave operator-shape notation as-is. The vector operands of these ops are clear FIX; only the operator-shape spelling is the open question. This decision then settles `assemble-diagonal`, `gram` (`bilinear_form`), `SolveResult[N]`.
2. **`inner_product_M` / `bilinear_form`** weighted variants: couple a vector shape to `LinearOperator[N,N]` — depends on (1).
3. **Complex multi-axis renderings** `Tensor[N, complex]` / `ComplexTensor[N]` (eigsolve `v`/eigenvector, elementwise_product_conj): the leading `N` is a congruence stand-in (FIX intent) but the exact form — `Tensor[(S: ...), complex]` vs `ComplexTensor[(S: ...)]` — is a notation call.
4. **`divfree-projector` FE-space axes** `N_nd` / `N_h1`: descriptive named axes for Nedelec/H1 spaces; lower accidental-rank-1 risk, but still flat-length stand-ins. Decide whether FE-space fields adopt named groups.

### Recommended edit order
1. **`book/src/design/l4_calculus.md`** is already authoritative — no change; it is the spec.
2. **L4 first (the backend-lowering target + the partially-converted exemplar):** finish `L4/krylov-step.md` (lines 76-77 to match its own already-converted record), then `L4/dot.md`, `L4/nrm2.md`, `L4/inner_product.md`, `L4/gram_reduce.md`, `L4/sparameter_reduce.md`, `L4/eliminate_bc.md`, `L4/ksp_solve.md`, `L4/eigsolve.md`, `L4/index.md` cells.
3. **Pure elementwise + reduce leaves at L2/L3** (lowest risk, highest volume, exact `σ`/`(S: ...)` template): `scal`, `axpy`, `axpby`, `axpbypcz`, `reciprocal`, `elementwise_product`, `normalize`, `dot`, `nrm2`, `inner_product` (vector operands only) — at both L2 and L3, plus their `index.md` dep-map cells and `L3/blas1-intro.md`.
4. **Constructed-operator gates** `jacobi-smoother`, `chebyshev` (L2/L3) + `L3-L2/chebyshev-nested-recurrence.md`.
5. **Composition compositions** `orthogonalize`, `deflate`, `gram` (vector operands + dot-hook; KEEP `coeffs`/`Basis`/`Matrix`) at L2/L3 + their lowering themes.
6. **Solver-cap iterate vectors** `krylov-step` / `ksp_solve` (L2/L3) + `concepts/krylov.md` + `concepts/sim-state.md` + the krylov lowering themes (`L2-L1/krylov-step-kernel-defusion.md`, `L3-L2/krylov-step-body-identity.md`, `L4-L3/krylov-step-typed-wrapper-dissolution.md`) — vector operands; defer the apply_linop operator-axis spelling to the BORDERLINE decision.
7. **Resolve BORDERLINE (1) operator-shape notation** with the human, then sweep `apply_linop`, `assemble-diagonal`, `eliminate_bc` operator axes, `inner_product_M`/`bilinear_form`, `SolveResult[N]`, and the complex/FE-space renderings (eigsolve, divfree).
8. **Never touch L1 / L0** — confirmed KEEP throughout.
