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

```
(empty — Phase B skeleton.)
```

## Working Notes

- This is the layer most populated by `combinator-miner` output — patterns recurring across the slice corpus are L2 candidates.
