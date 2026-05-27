# L2 — Algebraic decompositions

The canonical algebraic decomposition: each operation written as composition of base tensor / operator / quadrature primitives, with HPC/SIMD optimization tricks **unfolded back into the base algebras**. The **fusion rotation** layer.

## Context

L2 is the layer where:
- Cache-blocked loops, SIMD intrinsics, manual unrolling are erased — they are below L2's level of abstraction.
- Kernel fusion across multiple algebraic operations is unfolded into composition.
- Packed sparse formats are de-packed to dense/symbolic algebraic operators.
- Batched specialized BLAS calls are written as compositions of base primitives.

**Load-bearing numerical tricks** (non-associative reduction orderings, fast-math, mixed-precision intermediates, deterministic-vs-atomic accumulation) are **preserved as explicit algebraic claims** with the property they buy called out.

## Semantics (overlay)

L2 vocabulary: tensors, linear operators, quadrature rules, basis transformations, primitive operations (axpy, dot, matvec, gemv, trsv, scal, nrm2, …). State threading via explicit value semantics.

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| `krylov-step` | `(op_params, iter_state) → {state: iter_state, outputs: step_outputs}` | `apply_linop`, `axpy`/`axpby`, `dot`, `nrm2`, `orthogonalization`, `apply_BA`, `derived-view-hoisting`, `first-iteration-unrolling`, `variant-absorption` | `rough-in` (proposed-by: combinator-miner:2026-05-26T231843Z) |

## Working Notes

- This is the layer most populated by `combinator-miner` output — patterns recurring across the slice corpus are L2 candidates.
- `krylov-step` is a rough-in awaiting harvester formalization. Pattern is well-attested across five slices; harvester should pin the signature, variant-axis dispatch sites, and the algebraic-laws section (essentially: no internal algebraic laws — kernel of a fold; only law is L4 §3.8 demand-pruning over `output_extras`).
- **`krylov-step` provenance and consumers** (per combinator-miner:2026-05-26T231843Z):
  - **Consumed-by**: L4 `iterate_while` + `solve-monad` (outer driver; `cg.md §L4`, `gmres.md §L4`, `chebyshev.md §L4`, `arnoldi_step.md §L4`).
  - **Pattern instances** (five, well clear of ≥3 soft bar):
    - `spec/slices/cg.md:103-115`, `:172-188`, `:393-425`
    - `spec/slices/gmres.md:459-471`
    - `spec/slices/chebyshev.md:354-362`
    - `spec/slices/arnoldi_step.md:99-105`, `:285-298`
    - `spec/slices/polynomial_recurrence_step.md:119-160` (catalog of three instances)
  - **Dependency annotations** (carried from the original tree-style rough-in):
    - `orthogonalization` — variant axis.
    - `apply_BA` — preconditioner-side variant axis.
    - `derived-view-hoisting` — `output_extras` slot.
    - `first-iteration-unrolling` — orthogonal variant axis.
    - `variant-absorption` — absorption discipline applied to the step.
