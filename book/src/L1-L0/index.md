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
| [axpby-mutation-rotation](./axpby-mutation-rotation.md) | `L1/axpy` (+ `axpby` rough-in) | `palace/linalg/vector.{hpp,cpp}` | rough-in |
| [axpbypcz-mutation-rotation](./axpbypcz-mutation-rotation.md) | `L1/axpbypcz` (firm) | `palace/linalg/vector.{hpp,cpp}` | rough-in |
| [apply-linop-mutation-rotation](./apply-linop-mutation-rotation.md) | `L1/apply_linop` (firm) | `palace/linalg/operator.{hpp,cpp}`, `rap.cpp` | rough-in |
| [ksp-solve-mutation-rotation](./ksp-solve-mutation-rotation.md) | `L1/ksp_solve` (firm) | `palace/linalg/ksp.cpp`, `palace/linalg/iterative.{hpp,cpp}` | rough-in *(firmed cycle-008)* |
| [eigsolve-mutation-rotation](./eigsolve-mutation-rotation.md) | `L1/eigsolve` (rough-in) | `palace/linalg/{arpack,slepc,nleps}.cpp`, `palace/linalg/eps.hpp` | firm *(structural; partly-constructive on LinearSolveFailed)* |
| [eigsolve-convergence-reason-mapping](./eigsolve-convergence-reason-mapping.md) | `L1/eigsolve` (`EigStatus` sum-type) | `palace/linalg/slepc.cpp:{699,1182,1529}` (reason print-only) | partly-constructive *(SLEPc reason->EigStatus map; sub-theme of eigsolve-mutation-rotation)* |
| [chebyshev-smoother-mutation-rotation](./chebyshev-smoother-mutation-rotation.md) | `L1/chebyshev-smoother` (firm) | `palace/linalg/chebyshev.{hpp,cpp}` | firm *(structural; algebraic transpose-alias sub-rule)* |
| [orthogonalize-mutation-rotation](./orthogonalize-mutation-rotation.md) | `L1/orthogonalize` (firm) | `palace/linalg/orthog.hpp`, `palace/linalg/iterative.cpp` | firm *(structural; 3 variant loop-structures)* |
| [minres-iteration](./minres-iteration.md) | (speculative — `lanczos_step`, …) | (no Palace anchor — `MFEM_ABORT` at `ksp.cpp:53-57`) | obstruction |
| [bicgstab-iteration](./bicgstab-iteration.md) | (speculative — `bicgstab_step`, …) | (no Palace anchor — `MFEM_ABORT` at `ksp.cpp:53-57`) | obstruction |

## Working Notes

- Themes here are the bridge to source citations; every theme entry carries `palace/<file>.cpp:<lines>` evidence.
