---
agent: harvester
invoked_at: 2026-05-27T00:46:41Z
scope: L1 operator: axpbypcz
status: integrated
integrated_at: 2026-05-27T01:00:00Z
integration_commit: b8332b98300205740c4be4a9b1a2b30a2743dee3
integration_notes: Applied. New firm L1 operator with 12 algebraic laws including novel chained-collapse Law 12. Closes axpby-axpbypcz-next-harvest (both halves) and axpbypcz-l1-harvest.
inputs:
  - book/src/L1/axpby.md (precedent — fused-primitive structure)
  - reports/2026-05-27T001116Z-harvester-axpby-L1/CYCLE.md (cycle-003 axpby harvester report)
  - scaffolding/decisions/axpby-as-primitive.md (fused-primitive decision; mirrored here)
  - reference/palace/palace/linalg/vector.cpp:745-772 (AXPBYPCZ definitions, all three specialisations)
  - reference/palace/palace/linalg/vector.hpp:133-136 (ComplexVector::AXPBYPCZ member decl)
  - reference/palace/palace/linalg/vector.hpp:313-316 (linalg::AXPBYPCZ free-function template decl)
  - book/src/L1/index.md (L1 dep-map; append-after axpby row)
  - book/src/SUMMARY.md (append-after axpby line)
skill_uptake:
  - skill: verify-citation-range
    triggered: true
    decision: explained_non_applicable
    rationale: Citations verified inline by reading the cited ranges (vector.hpp:131-136, vector.hpp:309-316, vector.cpp:726-772 read directly via the Read tool); skill invocation deferred to critic-phase per cycle-003 axpby harvester precedent.
  - skill: classify-variant-axis
    triggered: true
    decision: artifact_landed
    rationale: Two variant axes (element-type real|complex; scalar-promotion sub-axis on complex element-type) landed in the Variant axes section, mirroring the axpby precedent. The L0 evidence is the three explicit specialisations at vector.cpp:745-772 (real-real-real, complex-complex-complex, and real-scalar-on-complex-vector overloads) — structurally identical to the axpby specialisation pattern.
  - skill: verify-refinement-surface
    triggered: true
    decision: explained_non_applicable
    rationale: Three proposed-changes blocks (new L1/axpbypcz.md, L1/index.md append-after axpby row, SUMMARY.md append-after axpby line) — surface well-formedness verified by inspection against the cycle-003 axpby harvester precedent.
---

# REPORT: Formalize axpbypcz at L1

## Summary

Formalizes `axpbypcz` — the fused three-scalar three-vector update `z_new = α·x + β·y + γ·z_old` — as a firm L1 operator. The L0 Palace surface fuses this operation at three entry points: the `ComplexVector::AXPBYPCZ` member (`vector.hpp:133-136`); the free-function template family `linalg::AXPBYPCZ` (`vector.hpp:313-316`); and three explicit specialisations at `vector.cpp:745-772` (real-real at 745-758 with a `γ == 0` branch delegating to MFEM's `add(α, x, β, y, z)`; complex-complex at 760-765 delegating to the member form; real-scalar-on-complex-vector at 767-772 delegating to the member form via implicit promotion). The fused-primitive decision is mirrored from the cycle-003 axpby decision (`scaffolding/decisions/axpby-as-primitive.md` § "Knock-on effects"): treat `axpbypcz` as a leaf at L1, record the subsumption chain `axpy ≺ axpby ≺ axpbypcz` as algebraic laws rather than dependencies. The L1 entry includes twelve algebraic laws (subsumption of `axpby`, subsumption of `axpy`, three identities for zero-scalars, one all-zero identity, trilinearity in the scalar triple `(α, β, γ)`, three distributivity laws over vector addition in each of `x`, `y`, `z`, scalar-vector absorption, and a chained-axpbypcz collapse on shared `(x, y)`), plus an explicit non-law section listing IEEE-754 reordering effects. Variant axes are element-type and scalar-promotion (same pattern as axpby).

## Proposed changes

````edit:book/src/L1/axpbypcz.md
# axpbypcz

Mutation-lifted fused three-scalar three-vector update: `z_new = α·x + β·y + γ·z_old`. The fused BLAS-1-extended primitive that subsumes `axpby` (γ=0), `axpy` (β=1, γ=0), and pure-scaling (α=0, β=0). At L1, the fused form is a leaf primitive; the decision against decomposing it as a composition of `axpby` + `axpy` (or chained `axpby` calls) mirrors the cycle-003 fused-primitive choice for `axpby` recorded in [`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md) (§ "Knock-on effects").

## Context

The L0 source-side forms are:

- `ComplexVector::AXPBYPCZ(std::complex<double> α, const ComplexVector &x, std::complex<double> β, const ComplexVector &y, std::complex<double> γ)` — member call mutating `*this` in place to `α·x + β·y + γ·(*this)` (`palace/linalg/vector.hpp:133-136`). The destination is the receiver; there is no output argument.
- `linalg::AXPBYPCZ<VecType, ScalarType>(ScalarType α, const VecType &x, ScalarType β, const VecType &y, ScalarType γ, VecType &z)` — free-function template (`palace/linalg/vector.hpp:313-316`) with three explicit specialisations:
  - `AXPBYPCZ(double, Vector, double, Vector, double, Vector)` (`palace/linalg/vector.cpp:745-758`): real-real path with a `γ == 0` branch. When `γ == 0` it delegates to MFEM's `add(α, x, β, y, z)` (the 5-argument out-of-place form that writes its last argument from the linear combination of its first four). When `γ ≠ 0` it splits into two calls: first `AXPBY(α, x, γ, z)` (in-place update `z = α·x + γ·z`), then `z.Add(β, y)` (in-place `z += β·y`). The split is not algebraically lossy — both branches compute the same `z_new = α·x + β·y + γ·z_old` — but it is the only L0 site in this family where the fused L1 form expands into multiple L0 calls.
  - `AXPBYPCZ(std::complex<double>, ComplexVector, std::complex<double>, ComplexVector, std::complex<double>, ComplexVector)` (`palace/linalg/vector.cpp:760-765`): delegates to `z.AXPBYPCZ(α, x, β, y, γ)`, i.e. the member form on `ComplexVector`.
  - `AXPBYPCZ(double, ComplexVector, double, ComplexVector, double, ComplexVector)` (`palace/linalg/vector.cpp:767-772`): real-scalar-on-complex-vector overload; promotes scalars implicitly and delegates to the same member form.

At L0, the in-place destination `z` is overwritten; the prior value of `z` is consumed by the update and inaccessible afterwards. The L1 form drops the destination-buffer mention: the operator consumes `α`, `x`, `β`, `y`, `γ`, and the pre-update value of `z`, and produces a fresh post-update value. The fusion (single-call combined update rather than a multi-pass form) is preserved at L1 because it has algebraic meaning — the law `axpbypcz(α, x, β, y, γ, z) = α·x + β·y + γ·z` is a primitive statement of the linear combination, not a derived shorthand.

This entry is the firm operator definition for `axpbypcz` at L1; it lands as a new firm row in `book/src/L1/index.md` (no prior rough-in row — this entry is a fresh promotion, motivated by the forward reference in `axpby.md` § "Dependencies" and open question `axpby-axpbypcz-next-harvest`). The L1>L0 lowering theme for `axpbypcz` (companion to `axpby-mutation-rotation`) is not authored in this report — that is abstractor work; see open question `axpbypcz-mutation-rotation-abstractor-target` below.

## Signature

```
axpbypcz :: (α: Scalar, x: Tensor[N], β: Scalar, y: Tensor[N], γ: Scalar, z: Tensor[N]) -> Tensor[N]
axpbypcz(α, x, β, y, γ, z) = α·x + β·y + γ·z
```

Shape contract (bunsen-style, named axes):

- `α` — scalar.
- `x` — `Tensor[N]` — read-only.
- `β` — scalar.
- `y` — `Tensor[N]` — read-only.
- `γ` — scalar.
- `z` — `Tensor[N]` — read-only (the *prior* value).
- result — `Tensor[N]` — same axis `N` as inputs.

`x`, `y`, and `z` must share the same length axis `N` and the same element type (all real or all complex). The scalars `α`, `β`, `γ` share each other's type and the vector element type, with one allowed promotion: real scalars may be passed against complex vectors and the scalars are promoted to complex (zero imaginary part). This mirrors Palace's `AXPBYPCZ(double, ComplexVector, double, ComplexVector, double, ComplexVector)` overload at `palace/linalg/vector.cpp:767-772`. Mixed real/complex scalar triples (some of α, β, γ real and others complex) are not exposed by Palace and are not part of the L1 signature — promote all or none.

The promotion rule is a typing concern, not a per-operator semantic difference; see open question `scalar-promotion-typing-rule` for the long-term plan to lift this into an L1 type-system rule rather than per-operator prose.

## Semantics

Element-wise: `result[i] = α·x[i] + β·y[i] + γ·z[i]` for `i ∈ [0, N)`. Reduction-free and element-local — every output element depends on exactly one input element from each of `x`, `y`, and `z`. No cross-element communication, no dependence on iteration order.

The operator is pure at L1: the prior `z` and the new `z` are distinct values. The L0 source overwrites the in-place destination buffer; that overwrite is an L1>L0 lowering concern (see open question `axpbypcz-mutation-rotation-abstractor-target`). At L1 the relationship is purely algebraic.

Special algebraic cases — `γ = 0` (recovers `axpby`), `β = 0, γ = 0` (recovers `axpy` with α=α), `β = 1, γ = 0` (recovers `axpy`), `α = 0` (drops `x`, gives `axpby(β, y, γ, z)`), all-zero (zero vector) — are not separate operators at L1. They are algebraic identities, recorded in the laws below. The L0 source has exactly one specialisation branch inside the `AXPBYPCZ` family: the real-real path at `vector.cpp:749-752` branches on `γ == 0` to dispatch either MFEM's `add(α, x, β, y, z)` (one-call) or the two-call split `AXPBY(α, x, γ, z); z.Add(β, y)`. This is a transparent performance trick — the `γ == 0` fast-path avoids the two-call split — and is recorded as such in the L1>L0 lowering theme (forthcoming).

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Subsumption of `axpby`**: `axpbypcz(α, x, β, y, 0, z) = axpby(α, x, β, y)` for any `z`. This is the load-bearing identity from the L0 `γ == 0` branch at `vector.cpp:749-751` — when `γ = 0` the L0 implementation calls MFEM's `add(α, x, β, y, z)` directly, which is the same kernel used by `AXPBY(α, x, β, y)` at `vector.cpp:729`. At L1 this restates as a subsumption law: `axpby` is a γ=0 specialisation of `axpbypcz`, not a dependency.

2. **Subsumption of `axpy`**: `axpbypcz(α, x, 1, y, 0, z) = axpy(α, x, y)` for any `z`. Composition of law 1 (γ=0 → axpby) and the axpby Law #1 (β=1 → axpy). Both `axpy` and `axpby` remain L1 leaves alongside `axpbypcz`; the subsumption chain `axpy ≺ axpby ≺ axpbypcz` is an algebraic-law statement, not a dependency statement.

3. **Identity in `α`**: `axpbypcz(0, x, β, y, γ, z) = β·y + γ·z = axpby(β, y, γ, z)` for any `x`. (Combines with law 1 to give the clean restatement: dropping the `x` term reduces to `axpby`.)

4. **Identity in `β`**: `axpbypcz(α, x, 0, y, γ, z) = α·x + γ·z = axpby(α, x, γ, z)` for any `y`.

5. **Identity in `γ`**: see law 1 (the γ=0 subsumption — `axpbypcz(α, x, β, y, 0, z) = axpby(α, x, β, y)`).

6. **All-zero identity**: `axpbypcz(0, x, 0, y, 0, z) = 0` (the zero vector of axis `N`) for any `x`, `y`, `z`.

7. **Trilinearity in the scalar triple `(α, β, γ)`**: for any scalars and held-fixed vector triple `(x, y, z)`:
   - Linear in `α` with `(x, β, y, γ, z)` held fixed: `axpbypcz(α₁ + α₂, x, β, y, γ, z) = axpbypcz(α₁, x, β, y, γ, z) + α₂·x`.
   - Symmetrically linear in `β` with `(α, x, y, γ, z)` held fixed.
   - Symmetrically linear in `γ` with `(α, x, β, y, z)` held fixed.
   - Combined: `axpbypcz(α, x, β, y, γ, z)` is linear separately in each of `α`, `β`, `γ`.

8. **Right distribution over vector addition in `x`**: `axpbypcz(α, x₁ + x₂, β, y, γ, z) = axpbypcz(α, x₁, β, y, γ, z) + α·x₂`. (The `+ α·x₂` is vector addition into the result.)

9. **Right distribution over vector addition in `y`**: `axpbypcz(α, x, β, y₁ + y₂, γ, z) = axpbypcz(α, x, β, y₁, γ, z) + β·y₂`.

10. **Right distribution over vector addition in `z`**: `axpbypcz(α, x, β, y, γ, z₁ + z₂) = axpbypcz(α, x, β, y, γ, z₁) + γ·z₂`.

11. **Scalar absorption**: `axpbypcz(α·κ, x, β, y, γ, z) = axpbypcz(α, κ·x, β, y, γ, z)` and symmetrically for the `β`/`y` and `γ`/`z` pairs — each scalar absorbs into its paired vector.

12. **Chained-`axpbypcz` collapse on shared `(x, y)`**: `axpbypcz(α₁, x, β₁, y, γ₁, axpbypcz(α₂, x, β₂, y, γ₂, z)) = axpbypcz(α₁ + γ₁·α₂, x, β₁ + γ₁·β₂, y, γ₁·γ₂, z)`. Two successive `axpbypcz` updates against the same `(x, y)` pair collapse to one with scalars `(α₁ + γ₁·α₂, β₁ + γ₁·β₂, γ₁·γ₂)`. This generalises the axpby chained-collapse law (axpby Law #9), which is the β₁ = β₂ = 0 case here (after re-labelling β-as-second-pair-scalar). It underwrites future L2 fusion of consecutive coefficient-update lines that share both an `x` and a `y` (e.g., GMRES/BiCGStab two-vector coefficient updates).

Laws that explicitly **do not** hold:

- **Commutativity in the vector arguments**: `axpbypcz(α, x, β, y, γ, z) ≠ axpbypcz(β, y, α, x, γ, z)` in general unless `α = β` — the operator is symmetric in the inputs only because `α·x + β·y + γ·z = β·y + α·x + γ·z` mathematically. The signature distinguishes argument slots by which scalar pairs with which vector; swapping scalar-vector pairs simultaneously preserves the value, but swapping vectors without swapping scalars does not. (Three-way permutation of the `(α, x), (β, y), (γ, z)` pair-triples preserves the value algebraically, but the signature has fixed argument positions.)
- **Associativity**: `axpbypcz` is six-ary (three scalar-vector pairs); "associativity" is not well-typed.
- **Floating-point associativity of the summation**: `α·x + β·y + γ·z` computed in IEEE-754 may differ from any reordering at the bit level when the magnitudes of the three partial sums differ enough to lose precision in one ordering. Palace's L0 form pins the ordering in the `γ == 0` fast-path (MFEM's `add(α, x, β, y, z)` kernel) but the `γ ≠ 0` slow-path uses a two-call split (`AXPBY(α, x, γ, z); z.Add(β, y)`) which computes the sum in a *different* order than the fused form would. **The L1 algebra is order-agnostic, but bit-identical reproduction of L0 output requires matching the L0 evaluation order, and the two L0 branches do not match each other.** This is recorded here, not erased.
- **Fusion identity with three separate `scal`+`add` passes**: `axpbypcz(α, x, β, y, γ, z) ≠ scal(α, x) + scal(β, y) + scal(γ, z)` in general at the bit level (the three-pass form rounds three times; the fused form rounds once or twice depending on the L0 branch) even though the values agree mathematically. The L0 form is fused for a reason; the L1 algebra preserves the fused statement. The lowering theme will record the fusion choice as load-bearing for performance, not for numerics.

## Dependencies

None at L1. `axpbypcz` is a leaf primitive — the harvester decision mirrors `scaffolding/decisions/axpby-as-primitive.md` § "Knock-on effects" ("The future `axpbypcz` harvester invocation can mirror this decision (fuse, don't decompose) for consistency"). Its sub-operations are three scalar multiplications and two element-wise additions, all at or below the L1 layer's resolution.

Subsumption (not dependency): `axpby(α, x, β, y) ≡ axpbypcz(α, x, β, y, 0, z)` and `axpy(α, x, y) ≡ axpbypcz(α, x, 1, y, 0, z)` (for any `z` — the result is independent of `z` when `γ = 0`). All three (`axpy`, `axpby`, `axpbypcz`) stay in the L1 dep-map as siblings; the subsumption chain is algebraic, not structural.

Future siblings (not dependencies): `scal` (pure scalar-vector multiply `(α, x) → α·x`) is the natural completion of this family — it appears as the two-zero reduction of `axpbypcz` (e.g., `axpbypcz(α, x, 0, _, 0, _) = α·x = scal(α, x)`). When `scal` lands, the zero-identity laws (3, 4) restate more cleanly. Until then, those identities are stated as "scalar-times-vector" without an L1 operator name.

## Variant axes

`axpbypcz` has two variant axes at L1, identical in structure to `axpby`'s:

- **element-type**: `real` | `complex`. The L0 source has separate template specialisations (real-real at `vector.cpp:745-758`; complex-complex at `vector.cpp:760-765`; real-scalar-on-complex-vector at `vector.cpp:767-772`; member form on `ComplexVector` at `vector.hpp:133-136`). At L1 these collapse to one operator parameterised by element type. The semantics are identical across element types — the per-element kernel is just `α·x[i] + β·y[i] + γ·z[i]` in the appropriate field.
- **scalar promotion** (sub-axis on the complex element-type): when `α`, `β`, `γ` are real but vectors are complex, Palace permits implicit promotion via the dedicated overload at `vector.cpp:767-772`. At L1 this is a typing-rule concern (subtype broadcasting), not a separate operator. Tracked at open question `scalar-promotion-typing-rule`.

**Internal control-flow axis at L0 (not an L1 variant axis)**: the real-real specialisation at `vector.cpp:749-752` branches on `γ == 0` to choose between a single-call fused dispatch and a two-call split. This is a transparent performance specialisation — algebraically equivalent — and not visible at L1. The L1>L0 lowering theme records it as a constant-folding sub-rule (the `γ == 0` algebraic-sub-rule, analogous to `axpy`'s `α == 1.0` sub-rule). The complex-complex and real-scalar-on-complex-vector specialisations do not have this branch — they uniformly delegate to the member form `z.AXPBYPCZ(α, x, β, y, γ)`, which presumably has its own internal branch or unified kernel (member-method body is in the corresponding `vector.cpp` definition, not surveyed in this report — recorded as a minor follow-up below).

No other variant axes — `axpbypcz` is unconditionally pure, element-local, and reduction-free across all variants.

## Status

`firm` — signature is canonical (matches three Palace L0 entry points exactly), evidence is direct from the Palace source, the algebraic laws listed are standard linear-combination facts extended from the axpby laws, and the fused-primitive choice mirrors the recorded decision for `axpby`.

## L1 vs L0 distinction

- **L0**: mutating member method (`ComplexVector::AXPBYPCZ(α, x, β, y, γ)` writes through `*this`) or free-function template (`linalg::AXPBYPCZ(α, x, β, y, γ, z)` writes through `z`). Three specialisations: real-real with a `γ == 0` branch (one-call fast-path via MFEM `add(α, x, β, y, z)` versus two-call split-path `AXPBY(α, x, γ, z); z.Add(β, y)`); complex-complex and real-scalar-on-complex-vector both delegating to the member form. No constant-folding branches on `α` or `β` individually (only on the `γ == 0` control-flow axis in the real-real specialisation). The evaluation order of the partial sums differs between the two real-real branches.
- **L1**: pure functional update. `z_new = axpbypcz(α, x, β, y, γ, z_old)`. No destination buffer in the signature. Algebraic laws apply directly. The L0 in-place mutation, the L0 fusion choice, and the L0 `γ == 0` control-flow branching are all L1>L0 lowering concerns. Floating-point evaluation-order non-associativity is recorded as an explicit non-law, classified as load-bearing for bit-reproduction but not for algorithmic correctness.

## Evidence

- `palace/linalg/vector.hpp:133-136` — `ComplexVector::AXPBYPCZ` member decl with comment `In-place addition (*this) = alpha * x + beta * y + gamma * (*this).`
- `palace/linalg/vector.hpp:313-316` — free-function template `AXPBYPCZ(ScalarType alpha, const VecType &x, ScalarType beta, const VecType &y, ScalarType gamma, VecType &z)` declared with comment `Addition z = alpha * x + beta * y + gamma * z.`
- `palace/linalg/vector.cpp:745-758` — `AXPBYPCZ(double, Vector, double, Vector, double, Vector)` specialisation with `γ == 0` branch: fast-path delegates to `add(alpha, x, beta, y, z)` (MFEM's 5-arg out-of-place form); slow-path splits into `AXPBY(alpha, x, gamma, z); z.Add(beta, y)`.
- `palace/linalg/vector.cpp:760-765` — `AXPBYPCZ(std::complex<double>, ComplexVector, std::complex<double>, ComplexVector, std::complex<double>, ComplexVector)` specialisation: delegates to member `z.AXPBYPCZ(alpha, x, beta, y, gamma)`.
- `palace/linalg/vector.cpp:767-772` — `AXPBYPCZ(double, ComplexVector, double, ComplexVector, double, ComplexVector)` specialisation: real-scalar-on-complex-vector overload; also delegates to the member form (implicit promotion).
- `palace/linalg/vector.cpp:729` — MFEM `add(α, x, β, y, y)` reference at the `AXPBY` real-real path (confirms the kernel reused by `axpbypcz`'s `γ == 0` fast-path which calls `add(α, x, β, y, z)`).
- Decision record: [`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md) § "Knock-on effects" — the explicit invitation for the `axpbypcz` harvester to mirror the fused-primitive choice.
- Cross-references: `book/src/L1/axpby.md` (the γ=0 specialisation; sibling L1 leaf), `book/src/L1/axpy.md` (the β=1, γ=0 specialisation; sibling L1 leaf), forthcoming `book/src/L1-L0/axpbypcz-mutation-rotation.md` (L1>L0 lowering theme; abstractor target).
````

````edit:book/src/L1/index.md
| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`axpy`](./axpy.md) | `(α, x, y) → α·x + y` | (leaf) | `firm` |
| [`dot`](./dot.md) | `(x, y) → ⟨x, y⟩` (hermitian for complex) | (leaf) | `firm` |
| [`nrm2`](./nrm2.md) | `(x) → √⟨x,x⟩` | `dot` | `firm` |
| [`axpby`](./axpby.md) | `(α, x, β, y) → α·x + β·y` | (leaf; subsumes `axpy`) | `firm` |
| [`axpbypcz`](./axpbypcz.md) | `(α, x, β, y, γ, z) → α·x + β·y + γ·z` | (leaf; subsumes `axpby` and `axpy`) | `firm` |
````

*Edit-mode for `book/src/L1/index.md`*: **append-after** the existing `axpby` row in the operator dep-map table — append one row. No other change to the file. The block above shows the full updated dep-map table for context; the integrator may apply as a single-row insert after the axpby row.

````edit:book/src/SUMMARY.md
- [axpbypcz](./L1/axpbypcz.md)
````

*Edit-mode for `book/src/SUMMARY.md`*: **append-after** the existing `- [axpby](./L1/axpby.md)` line under the `# L1 — Mutation-Lifted Forms` Part. One-line insert.

## Supporting evidence

- **L0 source (verified by direct read):**
  - `palace/linalg/vector.hpp:131` — `ComplexVector::AXPBY` member (sister operator, for chain context).
  - `palace/linalg/vector.hpp:133-136` — `ComplexVector::AXPBYPCZ` member decl.
  - `palace/linalg/vector.hpp:309-311` — `linalg::AXPBY` template decl.
  - `palace/linalg/vector.hpp:313-316` — `linalg::AXPBYPCZ` template decl.
  - `palace/linalg/vector.cpp:745-758` — `AXPBYPCZ(double, ...)` specialisation with `γ == 0` branch; fast-path `add(α, x, β, y, z)`, slow-path `AXPBY(α, x, γ, z); z.Add(β, y)`.
  - `palace/linalg/vector.cpp:760-765` — `AXPBYPCZ(std::complex<double>, ...)` complex-complex specialisation; delegates to member.
  - `palace/linalg/vector.cpp:767-772` — `AXPBYPCZ(double, ComplexVector, ...)` real-scalar-on-complex-vector specialisation; delegates to member.
- **Precedent (cycle-003):** `reports/2026-05-27T001116Z-harvester-axpby-L1/CYCLE.md` — same fused-primitive structure, nine algebraic laws, two variant axes. This `axpbypcz` report extends the pattern to three scalar-vector pairs, adds two subsumption laws (axpby and axpy) at the top, and generalises the chained-collapse law from 2-pair to 3-pair form.
- **Decision record (mirrored):** `scaffolding/decisions/axpby-as-primitive.md` § "Knock-on effects" explicitly invites this harvester to mirror the fused-primitive choice. No new decision file authored for `axpbypcz` — the existing record covers both via the explicit forward-statement.
- **Cycle-003 lowering-verifier anchor:** The lowering-verifier audit (cycle-003) confirmed the evidence anchor at `vector.cpp:756` (the `z.Add(beta, y)` line in the `γ ≠ 0` slow-path). This is the load-bearing detail that distinguishes the L0 `γ == 0` fast-path from the slow-path — recorded here as the "internal control-flow axis at L0" note in the Variant axes section.

## Open questions / caveats

1. **L1>L0 lowering theme not yet authored.** A companion theme `axpbypcz-mutation-rotation` (analogous to the existing `axpby-mutation-rotation`) is the next abstractor target — it must address: (a) the `γ == 0` algebraic-sub-rule (analogous to `axpy`'s `α == 1.0` sub-rule and the structural fact that `axpby-mutation-rotation` lacks this) — this is the *first* place in the L1>L0 lowering corpus where a Palace specialisation requires algebraic constant-folding to recognise; (b) the two distinct L0 evaluation orders in the real-real specialisation (one-call vs two-call); (c) the in-place destination rebinding (same as `axpby`). Tracked as open question `axpbypcz-mutation-rotation-abstractor-target` (new; harvester appendable to `scaffolding/open-questions.md`). The L1 algebra is firm independent of this — the lowering can proceed in a future cycle.

2. **`ComplexVector::AXPBYPCZ` member-method body not surveyed.** The complex-complex and real-scalar-on-complex-vector specialisations at `vector.cpp:760-772` both delegate to `z.AXPBYPCZ(α, x, β, y, γ)` (the member form), but the member-method body itself was not read in this invocation. Whether the member form has its own `γ == 0` constant-folding branch or uses a unified kernel is unresolved. This is a minor follow-up — the L1 algebra is unchanged either way (both branches compute the same value) — but the lowering-verifier audit for `axpbypcz` should survey the member-method body to document the complete L0 dispatch tree. Recorded as open question `axpbypcz-member-method-body-survey`.

3. **`scal` is referenced but not yet a primitive.** Laws 3 and 4 ("Identity in α", "Identity in β") restate as `axpby(β, y, γ, z)` and `axpby(α, x, γ, z)` respectively — both forms in the existing L1 vocabulary. But the two-zero cases (`axpbypcz(0, x, 0, y, γ, z) = γ·z`, `axpbypcz(0, x, β, y, 0, z) = β·y`, `axpbypcz(α, x, 0, y, 0, z) = α·x`) reduce to scalar-times-vector — until `scal` lands as an L1 primitive, these are stated as `γ·z`, `β·y`, `α·x` without an L1 operator name. Forward-reference to a future `scal` harvest is recorded; no action needed by integrator.

4. **Open question `axpby-axpbypcz-next-harvest` now fully closed.** Pilot-1 / cycle-002 opened this question with two halves (axpby + axpbypcz). Cycle-003 closed the axpby half; this report closes the axpbypcz half. Recommend the integrator mark the question `answered` in `scaffolding/open-questions.md` with `answered_in: <this commit>; answered_at: cycle-004`.

5. **L1 dep-map row count: 5.** After this report lands, the L1 dep-map has five firm operators (`axpy`, `dot`, `nrm2`, `axpby`, `axpbypcz`). Pilot-1's open question `l1-index-refresh` set "≥3 L1 operators" as the threshold for an intro refresh; cycle-003 noted the trigger was met at 4 operators. The L1 layer-intro refresh is now well past its trigger — five operators, three of which (`axpy`, `axpby`, `axpbypcz`) form an explicit subsumption chain that the intro could/should narrate. Recommend cycle-planner schedule a `layer-intro-author` invocation for the L1 Part overview in the next cycle. (Out of scope for harvester — flagging per role discipline.)

6. **`scalar-promotion-typing-rule` cross-operator pattern now at 4 operators.** This entry, like `axpy`, `dot`, and `axpby` before it, states the real-scalar-on-complex-vector promotion rule in per-operator prose (Signature section). Four operators now stating the same rule — well past the "three operators" threshold flagged by cycle-003. Recommend cycle-planner promote `scalar-promotion-typing-rule` to high priority for a dedicated lift into an L1 type-system rule.

7. **Chained-collapse law (Law 12) is novel — first appearance of a 3-pair collapse identity.** The axpby chained-collapse (axpby Law #9) is `(α₁ + β₁·α₂, β₁·β₂)`; this report's Law 12 generalises to `(α₁ + γ₁·α₂, β₁ + γ₁·β₂, γ₁·γ₂)`. The pattern (`outer_scalar + outer_self_scalar · inner_scalar` for each non-self-scalar slot; `outer_self_scalar · inner_self_scalar` for the self-slot) is a candidate combinator-mining target for a "fused-update chained-collapse" L1 → L2 pattern. Not in scope for this report; flagged for a future combinator-miner invocation.

8. **No new decision file authored.** The fused-primitive choice for `axpbypcz` is governed by the existing `scaffolding/decisions/axpby-as-primitive.md` § "Knock-on effects" forward-statement. Authoring a parallel `axpbypcz-as-primitive.md` would duplicate prose without adding signal. If a future cycle finds the existing forward-statement insufficient, a dedicated decision file can be added then — but the bar for that is "the existing forward-statement was contested or proved insufficient," which has not occurred.
