# L3 — Global tensor-field operations

L2 algebraic decompositions re-expressed as global tensor-field / convolution-over-space operations: whole-tensor ops, no element loops. The **iteration rotation** layer.

## Context

Where the L2 algebra admits a global form, L3 captures it. Where no global form exists (Gauss-Seidel-flavored smoothers, certain triangular solves, sequentially-reordered preconditioners), the **obstruction** is recorded as a first-class output — negative L3 results are part of the deliverable.

## Semantics (overlay)

L3 expresses:
- Whole-tensor primitives (matvec, axpy, dot, nrm2 as field operations)
- Field transitions: state evolution over a single algorithmic step expressed as `state' = f(state, params)`
- Convolution-like patterns where applicable (stencil sweeps, restriction/prolongation)
- Sequential obstructions: explicit markers where global form is unavailable, with reason

## Operator dep-map

```
(empty — Phase B skeleton.)
```

## Working Notes

- This layer is the destination of the L2-L1 lowering pipeline output AND the source for L4-L3 lowering verification.
- `concepts/sequential-obstruction.md` is the canonical write-up of when L3 lifts fail.
