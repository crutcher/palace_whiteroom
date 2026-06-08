---
layer: L1
operator: axpy
rank: firm
# Firm-in-prose BLAS-1 leaf — fully-specified
# positive L0 source + syntactic-identity laws (the firm-on-positive-structure escape).
# The blocking depends-on is the rank-terminal POSITIVE L0 SOURCE (cites-evidence),
# which is what makes the `firm` rank well-founded (the set_subvector_zero precedent).
# The lowers-to edge points at the axpby-mutation-rotation theme, which covers axpy's
# sub-patterns as the β=1 specialisation (there is NO standalone axpy-mutation-rotation).
edges:
  depends-on:
    - target: palace/linalg/vector.cpp:702-712
      kind: cites-evidence        # free-function AXPY(double,Vector,Vector) + α==1.0 fast-path
    - target: palace/linalg/vector.cpp:715-723
      kind: cites-evidence        # AXPY(complex,ComplexVector,ComplexVector) overload
    - target: palace/linalg/vector.hpp:115-118
      kind: cites-evidence        # ComplexVector::AXPY / Add member decl
    - target: palace/linalg/vector.hpp:305-307
      kind: cites-evidence        # free-function template AXPY decl
    - target: L1-L0/axpby-mutation-rotation
      kind: lowers-to             # axpy's lowering = β=1 specialisation in the axpby theme
  reference:
    - L1/axpby
    - L1/axpbypcz
    - L1/scal
    - L2/linear_combination
    - concepts/axpy
    - concepts/scalar-promotion
---

# axpy

Mutation-lifted vector-scalar fused update: `y_new = α·x + y_old`. The canonical BLAS-1 primitive at L1.

## Context

`axpy` lifts the BLAS-1 in-place fused update `y ← α·x + y` from two L0 idioms (receiver-mutating `y.Add(α, x)` / `y.AXPY(α, x)` and free-function-form `linalg::AXPY(α, x, y)`) to a single pure-functional operator. The L0 surface is detailed in [`L0/linalg-vector-file`](../L0/linalg-vector-file.md) (the `AXPY` family in `palace/linalg/vector.{hpp,cpp}`); the receiver-vs-output-arg idiom split is named in [`L0/output-arg-vs-receiver`](../L0/output-arg-vs-receiver.md); the real-vs-complex element-type axis is named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md); the real-real `α == 1.0` constant-folding branch is classified as transparent in [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

The L1 form drops the destination-buffer mention: the operator consumes `α`, `x`, and the pre-update value of `y`, and produces a fresh post-update value. Workspace, aliasing, and in-place overwrite are L0 concerns; they reappear (if at all) in the L1>L0 lowering theme, not in the L1 signature.

A cross-cutting prose treatment lives at [`concepts/axpy`](../concepts/axpy.md) — covering BLAS background, fusions (`α = 1`, `α = -1`), and roll-up usage across slices. The L1 entry here is the firm operator definition; the concept page is the narrative.

## Signature

```
axpy :: (α: Scalar, x: Tensor[N], y: Tensor[N]) -> Tensor[N]
axpy(α, x, y) = α·x + y
```

Shape contract (bunsen-style, named axes):

- `α` — scalar (real or complex, matching the vector element type).
- `x` — `Tensor[N]` — read-only.
- `y` — `Tensor[N]` — read-only (the *prior* value).
- result — `Tensor[N]` — same axis `N` as inputs.

`x` and `y` must share the same length axis `N` and the same element type (both real or both complex). When the vectors are complex, real `α` is promoted to complex per the [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) typing rule, realised at `palace/linalg/vector.cpp:715-718`.

## Semantics

Element-wise: `result[i] = α·x[i] + y[i]` for `i ∈ [0, N)`. Reduction-free and element-local — every output element depends on exactly one input element from each of `x` and `y`. No cross-element communication, no dependence on iteration order.

The operator is pure at L1: the prior `y` and the new `y` are distinct values. The L0 source overwrites the in-place destination buffer; the L1>L0 lowering theme is where that overwrite is reintroduced. At L1 the relationship is purely algebraic.

Special algebraic cases — `α = 0` (identity in the second argument), `α = 1` (vector add), `α = -1` (vector subtract), `x = 0` (identity in the first argument) — are not separate operators at L1. The L0 source sometimes specialises (Palace's `AXPY(double, Vector, Vector)` branches on `α == 1.0` to call `operator+=`); these are transparent performance tricks at L1 and disappear in the L1>L0 lowering.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Identity in `α`**: `axpy(0, x, y) = y` for any `x`.
2. **Identity in `x`**: `axpy(α, 0, y) = y` for any `α`, where `0` is the zero vector of axis `N`.
3. **Left distribution over vector addition in `y`**: `axpy(α, x, y₁ + y₂) = axpy(α, x, y₁) + y₂`. Both sides equal `α·x + y₁ + y₂`.
4. **Scalar linearity in α (additive collapse)**: `axpy(α, x, axpy(β, x, y)) = axpy(α + β, x, y)` — two successive axpy's against the same `x` collapse to one with summed scalar.
5. **Scalar absorption**: `axpy(α·β, x, y) = axpy(α, β·x, y)` — the scalar absorbs into either side.
6. **Vector linearity in x (additive expansion)**: `axpy(α, x₁ + x₂, y) = axpy(α, x₁, axpy(α, x₂, y))`. This law underwrites the L2 unfolding of GMRES basis-correction sums into axpy chains.

Laws that explicitly **do not** hold:

- **Commutativity in the vector arguments**: `axpy(α, x, y) ≠ axpy(α, y, x)`. The second argument `x` enters scaled by `α`; the third argument `y` does not. Swapping them changes the value.
- **Associativity** as a binary algebra: `axpy` is ternary; "associativity" is not even well-typed for it.

## Dependencies

None at L1. `axpy` is a leaf primitive — the canonical floor of the linear-algebra vocabulary at this layer. Its only sub-operations are scalar multiplication and element-wise addition, both at or below the L1 layer's resolution.

## Variant axes

`axpy` has one orthogonal variant axis at L1:

- **element-type**: `real` | `complex`. The L0 source has separate overloads (`AXPY(double, Vector, Vector)` at `palace/linalg/vector.cpp:702-712`; `AXPY(std::complex<double>, ComplexVector, ComplexVector)` at `palace/linalg/vector.cpp:715-723`; member-method form on `ComplexVector` at `vector.hpp:115-118`). At L1 these collapse to one operator parameterised by element type.
- **scalar promotion** (sub-axis): see [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) — real `α` against complex vectors via `vector.cpp:715-718`.

No other variant axes — `axpy` is unconditionally pure, element-local, and reduction-free across all variants.

## L1 vs L0 distinction

- **L0**: mutating member methods. `y.Add(α, x)` (real, MFEM); `y.AXPY(α, x)` (complex, Palace). Writes through `y`. May branch on `α == 1.0` (Palace `AXPY(double, Vector, Vector)` calls `y += x` rather than `y.Add(1.0, x)`).
- **L1**: pure functional update. `y_new = axpy(α, x, y_old)`. No destination buffer in the signature. Algebraic laws apply directly. The L0 in-place mutation and the L0 `α == 1` branch are both L1>L0 lowering concerns, not L1 concerns.

## Evidence

- `palace/linalg/vector.hpp:115-118` — `ComplexVector::AXPY` and `Add`/`Subtract` aliases declared, with comment `In-place addition (*this) += alpha * x.`
- `palace/linalg/vector.hpp:305-307` — free-function template `AXPY(ScalarType alpha, const VecType &x, VecType &y)` declared with comment `Addition y += alpha * x.`
- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` definition and the element-wise `forall_switch` kernels showing `YR[i] += ar*XR[i] − ai*XI[i]`.
- `palace/linalg/vector.cpp:702-712` — free-function `AXPY(double, Vector, Vector)` with the `α == 1.0` fast-path branch.
- `palace/linalg/operator.cpp:458-466` — `y.Add(a*c, z)` accumulating scaled operator outputs in `SumOperator::AddMult`.
- `palace/linalg/rap.cpp:73` — `b.Add(-1.0, ty)` in Dirichlet-boundary residual correction.
- `palace/linalg/rap.cpp:317` — `y.Add(a, ty)` in `ParOperator::AddMult`.
