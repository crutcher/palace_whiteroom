# L1 > L0 — Lowering layer

The transformation from L1 (mutation-lifted forms) to L0 (cited Palace source ranges). Batched by **themes**.

## Context

L0 is the ground truth: cited Palace C++ source. L1 is its pure-functional lift. This lowering describes how a pure-functional L1 form is the abstract view of the C++ source pattern at L0.

Many themes here capture **how Palace expresses common patterns**:
- In-place axpy as `x.Add(α, y)` → vector-method-call shape
- Operator application as `A.Mult(x, y)` → matrix-method-call shape (output-arg convention)
- Workspace buffer reuse → mention-and-erase patterns

## Theme list

| theme | L1 anchor | L0 anchor | status |
|---|---|---|---|
| [axpby-mutation-rotation](./axpby-mutation-rotation.md) | `L1/axpy` (+ `axpby`/`axpbypcz` fwd-ref) | `palace/linalg/vector.{hpp,cpp}`, `operator.cpp`, `rap.cpp` | firm *(structural; 3 sub-patterns A/B/C; `α==1`/`α==-1` algebraic sub-rules; complex-α + Subtract forms defined-not-used)* |
| [axpbypcz-mutation-rotation](./axpbypcz-mutation-rotation.md) | `L1/axpbypcz` (firm) | `palace/linalg/vector.{hpp,cpp}`, `arpack.cpp`, `slepc.cpp`, `nleps.cpp`; `palace/models/{timeoperator,romoperator}.cpp` | firm *(structural; 4 sub-patterns A/B/C/D; mixed-justification γ==0 algebraic sub-rule; B+D defined-not-used; sole γ≠0 path is A's real-real slow-path)* |
| [apply-linop-mutation-rotation](./apply-linop-mutation-rotation.md) | `L1/apply_linop` (firm) | `palace/linalg/operator.{hpp,cpp}`, `rap.cpp` | rough-in |
| [ksp-solve-mutation-rotation](./ksp-solve-mutation-rotation.md) | `L1/ksp_solve` (firm) | `palace/linalg/ksp.cpp`, `palace/linalg/iterative.{hpp,cpp}` | rough-in *(firmed cycle-008)* |
| [eigsolve-mutation-rotation](./eigsolve-mutation-rotation.md) | `L1/eigsolve` (rough-in) | `palace/linalg/{arpack,slepc,nleps}.cpp`, `palace/linalg/eps.hpp` | firm *(structural; partly-constructive on LinearSolveFailed)* |
| [eigsolve-convergence-reason-mapping](./eigsolve-convergence-reason-mapping.md) | `L1/eigsolve` (`EigStatus` sum-type) | `palace/linalg/slepc.cpp:{699,1182,1529}` (reason print-only) | partly-constructive *(SLEPc reason->EigStatus map; sub-theme of eigsolve-mutation-rotation)* |
| [chebyshev-smoother-mutation-rotation](./chebyshev-smoother-mutation-rotation.md) | `L1/chebyshev-smoother` (firm) | `palace/linalg/chebyshev.{hpp,cpp}` | firm *(structural; algebraic transpose-alias sub-rule)* |
| [divfree-projector-mutation-rotation](./divfree-projector-mutation-rotation.md) | `L1/divfree-projector` (firm) | `palace/linalg/divfree.{hpp,cpp}`, `palace/fem/integ/mixedvecgrad.cpp` | firm *(structural; 4 sub-patterns; algebraic sign sub-note, positively anchored)* |
| [orthogonalize-mutation-rotation](./orthogonalize-mutation-rotation.md) | `L1/orthogonalize` (firm) | `palace/linalg/orthog.hpp`, `palace/linalg/iterative.cpp` | firm *(structural; 3 variant loop-structures)* |
| [nrm2-mutation-rotation](./nrm2-mutation-rotation.md) | `L1/nrm2` (firm) | `palace/linalg/vector.hpp`, `palace/utils/communication.hpp`, `palace/fem/errorindicator.hpp` | firm *(structural; 3 surface forms; abs-guard classified load-bearing defensive)* |
| [scal-mutation-rotation](./scal-mutation-rotation.md) | `L1/scal` (firm) | `palace/linalg/vector.{hpp,cpp}`, `palace/linalg/{iterative,operator,nleps}.cpp` | firm *(structural; 2 element-type overloads; transparent complex imag==0 shape branch)* |
| [dot-mutation-rotation](./dot-mutation-rotation.md) | `L1/dot` (firm) | `palace/linalg/vector.{hpp,cpp}`, `palace/utils/communication.hpp` | firm *(structural; 3 surface forms; conjugate-pair re-order `xᴴ y = conj(yᴴ x)`; tdot type-API-surface-only)* |
| [matrix-weighted-norm-mutation-rotation](./matrix-weighted-norm-mutation-rotation.md) | `L1/matrix-weighted-norm` (rough-in) | `palace/linalg/operator.{hpp,cpp}`, `palace/linalg/{arpack,slepc,nleps}.cpp` | firm *(structural; 2 element-type sub-patterns A real/B complex + Normalize consumer C; reuses apply_linop A `B.Mult(x,Bx)` + dot A `Dot(comm,Bx,x)` + scal; caller-owned destination workspace Bx; SPD `MFEM_ASSERT(dot>0)` load-bearing defensive guard + complex Hermiticity witness; B=I collapses to nrm2)* |
| [nleps-deflated-residual-mutation-rotation](./nleps-deflated-residual-mutation-rotation.md) | `L1/nleps_deflated_residual` (firm) | `palace/linalg/nleps.cpp:547-577` (+ `:329-347` MatVecMult, `:587`/`:702` call sites) | firm *(structural; 3 sub-patterns A/B/C; load-bearing Mult+AddMult→single-pencil-apply collapse; reuses dot Sub-pattern A; reuses lin-comb fold L2>L1)* |
| [apply-nonlinear-pencil-mutation-rotation](./apply-nonlinear-pencil-mutation-rotation.md) | `L1/apply_nonlinear_pencil` (firm) | `palace/linalg/nleps.cpp:807-821` (+ `:496-499`/`:556-559`/`:655`/`:729` BuildParSumOperator sites; `:177-181` A2-closure; `rap.cpp:832-841` BuildParSumOperator) | firm *(structural; 3 sub-patterns A term-by-term/B BuildParSumOperator-dual/C A2-closure-at-\|Im λ\|; load-bearing build-form accumulation-order non-law; reuses apply_linop laws 3/5)* |
| [assemble-diagonal-mutation-rotation](./assemble-diagonal-mutation-rotation.md) | `L1/assemble-diagonal` (firm) | `palace/linalg/operator.{hpp,cpp}`, `hypre.{hpp,cpp}`, `rap.{hpp,cpp}`, `fem/libceed/operator.{hpp,cpp}` | firm *(structural; 4 representation sub-patterns + abort; load-bearing approximate-matrix-free non-law, positively anchored)* |
| [lu-solve-mutation-rotation](./lu-solve-mutation-rotation.md) | `L1/lu_solve` (firm) | `palace/linalg/nleps.cpp`, `palace/models/romoperator.{cpp,hpp}` (inline Eigen — no `lu.cpp`) | firm *(structural; 2 sub-patterns A NLEPS full-pivot-LU / B ROM full-pivot-QR; load-bearing factorization-kernel axis incl. rejected LDLT, positively anchored; in-place RHS overwrite)* |
| [nleps-deflated-solve-mutation-rotation](./nleps-deflated-solve-mutation-rotation.md) | `L1/nleps_deflated_solve` (firm) | `palace/linalg/nleps.cpp:504-537` (+ `:329-347` MatVecMult, `:542`/`:682`/`:735` call sites) | firm *(structural; 3 sub-patterns A big-space `ksp_solve` / B coordinate Gram+Schur-complement+`lu_solve` / C back-projection `lin-comb`∘`lu_solve`+`axpy`; load-bearing block-elimination double-`S⁻¹` structure, never-bare-Gram-solve; reuses lu-solve/dot Sub-pattern A)* |
| [nleps-jacobian-action-mutation-rotation](./nleps-jacobian-action-mutation-rotation.md) | `L1/nleps_jacobian_action` (firm) | `palace/linalg/nleps.cpp:649-669` (+ `:329-347` MatVecMult, `:412` δ=√ε, `:673-676` consumer) | firm *(structural; 3 sub-patterns A divided-difference derivative-pencil apply / B double-`S⁻¹` back-projection for `S⁻²` / C two-`AddMult` product-rule `+T'·XS⁻¹v₂ −T·XS⁻²v₂`; load-bearing divided-difference `A2'` quasi-Newton non-law + big-space-only-output contract; reuses apply-nonlinear-pencil B / lu-solve A / lin-comb fold L2>L1)* |
| [nleps-eigenvalue-correction-mutation-rotation](./nleps-eigenvalue-correction-mutation-rotation.md) | `L1/nleps_eigenvalue_correction` (firm) | `palace/linalg/nleps.cpp:672-677` (+ `:587`/`:657`/`:542-545` producers, `:682` consumer, `:691`/`:708` line-search) | firm *(structural; 3 sub-patterns A projected Newton ratio `−num/den` over `dot` / B big-space RHS `axpby` (`AXPBYPCZ` γ=0) `−δλ·w−u` / C coordinate RHS `scal` `−u2`; load-bearing big/coordinate RHS asymmetry — `δλ` couples into `z` only; `⟨w0,w⟩=0` near-singularity + undamped-`δλ` non-laws; reuses dot Sub-pattern A / axpbypcz γ=0)* |
| [minres-iteration](./minres-iteration.md) | (speculative — `lanczos_step`, …) | (no Palace anchor — `MFEM_ABORT` at `ksp.cpp:53-57`) | obstruction |
| [bicgstab-iteration](./bicgstab-iteration.md) | (speculative — `bicgstab_step`, …) | (no Palace anchor — `MFEM_ABORT` at `ksp.cpp:53-57`) | obstruction |

## Working Notes

- Themes here are the bridge to source citations; every theme entry carries `palace/<file>.cpp:<lines>` evidence.
