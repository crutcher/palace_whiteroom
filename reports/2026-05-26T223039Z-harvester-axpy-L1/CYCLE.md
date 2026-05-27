---
agent: harvester
invoked_at: 2026-05-26T22:30:39Z
scope: L1 operator: axpy
status: pending
inputs:
  - book/src/concepts/axpy.md
  - book/src/L1/index.md
  - reference/palace/palace/linalg/vector.hpp
  - reference/palace/palace/linalg/vector.cpp
  - reference/palace/palace/linalg/operator.cpp
  - reference/palace/palace/linalg/rap.cpp
skill_uptake:
  - skill: verify-citation-range
    triggered: true
    decision: explained_non_applicable
    rationale: Citations verified inline by reading source ranges; skill invocation deferred until critic-phase mechanism stabilizes.
  - skill: classify-variant-axis
    triggered: true
    decision: artifact_landed
    rationale: Real-vs-complex element-type variant absorbed into a structured Variant axes section; see Operator content below.
integrated_at: 2026-05-26T22:50:00Z
integration_commit: TBD
integration_notes: |
  Applied both edits: created book/src/L1/axpy.md and populated L1 dep-map.
  Added axpy entry to SUMMARY.md under L1 layer.
  No safety-net gate hits.
  Book rebuilds cleanly.
---

# REPORT: Formalize axpy at L1

## Summary

`axpy` is the BLAS-1 vector-scalar fused update (`y ← α·x + y`) and the dominant primitive in every Palace solver loop touched so far (CG residual / iterate updates, GMRES basis-correction sums, operator-sum accumulation, Dirichlet residual correction in RAP). A cross-cutting concept entry already exists at `book/src/concepts/axpy.md`; the L1 dep-map is currently empty. This report promotes `axpy` into a firm L1 operator entry by creating `book/src/L1/axpy.md` (mutation-lifted pure-functional signature, semantics, algebraic laws, applicability) and registers it in the L1 dep-map. The L1 entry is the layer-specific firm form; the cross-cutting concept page stays in place as the narrative.

## Proposed changes

````edit:book/src/L1/axpy.md
# axpy

Mutation-lifted vector-scalar fused update: `y_new = α·x + y_old`. The canonical BLAS-1 primitive at L1.

## Context

The L0 source-side form is the in-place call `y.Add(α, x)` (a member function on `mfem::Vector`) or `y.AXPY(α, x)` (a member function on Palace's `ComplexVector`, with `Add` as an alias). At L0 both forms mutate `y` in place. The L1 form drops the destination-buffer mention: the operator consumes `α`, `x`, and the pre-update value of `y`, and produces a fresh post-update value. Workspace, aliasing, and in-place overwrite are L0 concerns; they reappear (if at all) in the L1>L0 lowering theme, not in the L1 signature.

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

`x` and `y` must share the same length axis `N` and the same element type (both real or both complex; the scalar `α` may be promoted from real to complex against a complex vector pair, mirroring Palace's `AXPY(double, ComplexVector, ComplexVector)` overload at `palace/linalg/vector.cpp:715-718`).

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

- **element-type**: `real` | `complex`. The L0 source has separate overloads (`AXPY(double, Vector, Vector)` at `palace/linalg/vector.cpp:702-712`; `AXPY(std::complex<double>, ComplexVector, ComplexVector)` at `palace/linalg/vector.cpp:715-723`; the member-method form on `ComplexVector` at `vector.hpp:115-118`). At L1 these collapse to one operator parameterised by element type; the L1 signature `axpy :: (α: Scalar, x: Tensor[N], y: Tensor[N]) -> Tensor[N]` reads with the scalar/tensor element type bound consistently across `α`, `x`, `y`, and the result.

- **scalar promotion** (sub-axis of `element-type`): when the scalar is real but the vectors are complex, Palace permits implicit promotion (`AXPY(double, ComplexVector, ComplexVector)` overload). At L1 this is treated as a typing-rule concern (the scalar's element type may be a subtype of the vector's element type for the purposes of broadcasting); it does not create a separate operator. Future L1 refinements may formalise this via a typing rule rather than per-operator prose.

No other variant axes — the operator is unconditionally pure, element-local, and reduction-free regardless of element type.

## Status

`firm` — signature is canonical, evidence is uncontested across the Palace solver corpus, and the algebraic laws listed are standard BLAS-1 facts.

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
````

````edit:book/src/L1/index.md
## Operator dep-map

```
axpy           y_new = α·x + y_old  (leaf primitive; no L1 dependencies)
```
````

Replacement target in `book/src/L1/index.md`: the section currently reads

```
## Operator dep-map

`​`​`
(empty — Phase B skeleton.)
`​`​`
```

The edit replaces only the fenced placeholder content with the dep-map entry; the section heading and surrounding text stay intact.

## Operator content

### Slug and one-line

**`axpy`** — mutation-lifted vector-scalar fused update: `y_new = α·x + y_old`.

### Signature

```
axpy :: (α: Scalar, x: Tensor[N], y: Tensor[N]) -> Tensor[N]
```

Named axes: `N` is the shared length of `x` and `y`. The scalar `α` must match the vector element type (with promotion from real to complex permitted, matching Palace's `AXPY(double, ComplexVector, ComplexVector)` overload).

### Semantics

Element-local pure-functional update. `result[i] = α·x[i] + y[i]` for `i ∈ [0, N)`. Reduction-free, embarrassingly parallel, order-independent. The L0 source mutates the destination buffer `y` in place; the L1 form takes the *prior* `y` as input and produces a fresh value, so the operator is mathematically pure at this layer. In-place reuse of the output buffer for the input `y_old` is a concern of the L1>L0 lowering (an aliasing/COW theme), not of the L1 signature.

The special cases observed in the L0 source — `α = 1` becoming `operator+=`, `α = -1` becoming `Subtract` — are transparent performance tricks. At L1 they are the same operator with different constants.

### Algebraic laws

The laws below hold; absences are deliberate.

1. **Identity in `α`**: `axpy(0, x, y) = y`.
2. **Identity in `x`**: `axpy(α, 0, y) = y`.
3. **Left distribution over vector addition in `y`**: `axpy(α, x, y₁ + y₂) = axpy(α, x, y₁) + y₂`.
4. **Scalar linearity in α (additive collapse)**: `axpy(α, x, axpy(β, x, y)) = axpy(α + β, x, y)`.
5. **Scalar absorption**: `axpy(α·β, x, y) = axpy(α, β·x, y)`.
6. **Vector linearity in x (additive expansion)**: `axpy(α, x₁ + x₂, y) = axpy(α, x₁, axpy(α, x₂, y))`. Underwrites L2 unfolding of GMRES basis-correction sums.

Laws that do **not** hold:

- **Commutativity in the vector arguments**: `axpy(α, x, y) ≠ axpy(α, y, x)`. The second argument enters scaled, the third does not.

### Dependencies

None at L1. `axpy` is a leaf primitive at this layer.

### Variant axes

One axis: **element-type** = `real` | `complex` (with `scalar promotion` sub-axis for real-α-against-complex-vectors). Both variants collapse to one L1 operator; the L0 source has separate overloads. See the Variant axes section of the proposed L1 entry for details.

### Status

`firm`.

### Cross-reference

See [`concepts/axpy`](../concepts/axpy.md) for the cross-cutting prose treatment (BLAS background, fusions, role in higher-layer rotations across solver slices).

## Supporting evidence

Cited Palace ranges (paths relative to `reference/`):

- `palace/linalg/vector.hpp:115-118` — `ComplexVector::AXPY` declaration with `Add` and `Subtract` aliases. The header comment `In-place addition (*this) += alpha * x.` is the canonical statement of the L0 semantics this L1 entry lifts.
- `palace/linalg/vector.hpp:305-307` — free-function template `AXPY(ScalarType alpha, const VecType &x, VecType &y)` with header comment `Addition y += alpha * x.`
- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` implementation. Two element-wise `forall_switch` kernels (one for `ai == 0`, one general) computing `YR[i] += ar*XR[i] − ai*XI[i]` and the imaginary component analogue. Direct evidence of the element-local, reduction-free contract.
- `palace/linalg/vector.cpp:702-712` — free-function `AXPY(double, Vector, Vector)` showing the `α == 1.0` fast-path branch (`y += x` vs `y.Add(α, x)`) — evidence that the `α = 1` specialisation is a transparent performance trick, not a separate operator.
- `palace/linalg/vector.cpp:715-723` — free-function `AXPY` overloads for the complex case, dispatching to the member method.
- `palace/linalg/operator.cpp:458-466` — `SumOperator::AddMult` body: `for (op, c) in ops: op->Mult(x, z); y.Add(a*c, z);` — an axpy chain accumulating scaled operator-sum outputs.
- `palace/linalg/rap.cpp:73` — `b.Add(-1.0, ty)` — Dirichlet-boundary residual correction.
- `palace/linalg/rap.cpp:317` — `y.Add(a, ty)` in `ParOperator::AddMult` accumulation.

## Open questions / caveats

- The L1>L0 lowering theme for `axpy` (not authored here — abstractor's job) will need to cover three sub-patterns observed in the L0 corpus: (1) the bare `y.Add(α, x)` / `y.AXPY(α, x)` member call, (2) the `α == 1` specialisation to `operator+=` (`vector.cpp:704-706`), (3) the `α == -1` specialisation to `Subtract` (`vector.hpp:118`). All three lower from the same L1 `axpy`; the theme should note the per-constant L0 pattern-match rules.

- Palace also has `AXPBY` (`y = α·x + β·y`) and `AXPBYPCZ` (`z = α·x + β·y + γ·z`) (`palace/linalg/vector.hpp:130-136`, `:309-316`). These are L1-distinct operators (different signatures, different laws); they are not in scope for this report but are obvious next harvester targets. The `axpby` harvester should consider whether to treat it as a primitive or as `axpy ∘ scal` — Palace fuses them at L0 (e.g. `vector.cpp:319+`) but fusion is a performance trick, not algebra. Recommend drafting `axpby` as its own L1 primitive *and* recording the fusion-vs-decomposition trade-off in `scaffolding/decisions/`.

- The complex-scalar overload `AXPY(double, ComplexVector, ComplexVector)` (`vector.cpp:715-718`) raises the question of whether the L1 signature should treat scalar-promotion (real → complex) explicitly or as an implicit coercion at the L1 type layer. The current entry leans on prose. A future refinement may want to formalise this via a typing rule rather than a per-operator note.

- The L1 layer intro at `book/src/L1/index.md` may want a brief refresh after this lands — to mention that the dep-map is now populated and point readers to the first operator entry. Not in scope for this invocation (layer-intro-author's remit).
