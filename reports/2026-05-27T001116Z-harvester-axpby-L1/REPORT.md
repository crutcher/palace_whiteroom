---
agent: harvester
invoked_at: 2026-05-27T00:11:16Z
scope: L1 operator: axpby (rough-in → firm)
status: pending
inputs:
  - book/src/L1/index.md (dep-map; axpby currently rough-in plain text)
  - book/src/L1/axpy.md (firm L1 operator, pilot-1 — format reference + subsumption target)
  - book/src/L1/dot.md (firm L1 operator, cycle-002 — format reference)
  - book/src/L1-L0/axpby-mutation-rotation.md (cycle-002 abstractor's L1>L0 theme that motivated this rough-in)
  - reports/2026-05-26T231843Z-abstractor-axpby-mutation-L1-L0/REPORT.md (rough-in source)
  - reports/2026-05-26T231843Z-harvester-dot-L1/REPORT.md (format reference)
  - scaffolding/open-questions.md (axpby-axpy-scal-decomposition-decision, axpby-axpbypcz-next-harvest, scalar-promotion-typing-rule)
  - scaffolding/decisions/axpby-as-primitive.md (NEW — captures the fused-primitive decision)
  - reference/palace/palace/linalg/vector.hpp:115-128 (ComplexVector AXPY/Add/Subtract/+=/-= decls)
  - reference/palace/palace/linalg/vector.hpp:130-136 (ComplexVector AXPBY, AXPBYPCZ member decls)
  - reference/palace/palace/linalg/vector.hpp:305-316 (free-function templates AXPY/AXPBY/AXPBYPCZ)
  - reference/palace/palace/linalg/vector.cpp:726-743 (AXPBY family: three explicit template specialisations)
  - reference/palace/palace/linalg/vector.cpp:745-758 (AXPBYPCZ real-path dispatch with γ==0 branch to AXPBY)
skill_uptake:
  - skill: verify-citation-range
    triggered: true
    decision: explained_non_applicable
    rationale: Citations verified inline by reading the cited ranges (vector.hpp:130-136, vector.cpp:726-743 read directly); skill invocation deferred to critic-phase per the established pilot-1 / cycle-002 harvester precedent.
  - skill: classify-variant-axis
    triggered: true
    decision: artifact_landed
    rationale: Two variant axes (element-type real|complex; scalar-promotion sub-axis when α/β are real but vectors complex) landed in the Variant axes section. The scalar-promotion sub-axis explicitly references open question `scalar-promotion-typing-rule` and points at the L0 evidence — Palace's `AXPBY(double, ComplexVector, double, ComplexVector)` overload at `vector.cpp:740-742`.
  - skill: verify-refinement-surface
    triggered: true
    decision: explained_non_applicable
    rationale: Three proposed-changes blocks (new L1/axpby.md, L1/index.md rough-in→firm row replacement, SUMMARY.md targeted insertion) — surface well-formedness verified by inspection against the cycle-002 dot harvester precedent.
integrated_at: 2026-05-27T00:23:54Z
integration_commit: TBD-AT-COMMIT-TIME
integration_notes: Applied as proposed (L1/index.md rough-in row replaced in-place with firm row; SUMMARY.md insertion auto-merged with sister nrm2 SUMMARY edit; decision file scaffolding/decisions/axpby-as-primitive.md git-added; open question axpby-axpy-scal-decomposition-decision marked answered).
---

# REPORT: Formalize axpby at L1

## Summary

Formalizes `axpby` — the fused two-scalar two-vector update `y_new = α·x + β·y_old` — as a firm L1 operator, promoting the rough-in row added to `book/src/L1/index.md` by cycle-002's abstractor (`axpby-mutation-rotation` theme). The Palace L0 surface fuses this operation at three entry points: the `ComplexVector::AXPBY` member (`vector.hpp:131`); the free-function template family `linalg::AXPBY` (`vector.hpp:311`, with three explicit specialisations at `vector.cpp:726-743` for real-real, complex-complex, and real-scalar-on-complex-vector dispatch); and the real-path delegation to MFEM's `add(α, x, β, y, y)` in-place 5-argument form (`vector.cpp:729`). The pre-existing open question `axpby-axpy-scal-decomposition-decision` is resolved in favour of treating `axpby` as a **fused primitive** (rather than decomposing as `axpy ∘ scal`); the decision is recorded in the new `scaffolding/decisions/axpby-as-primitive.md`. The L1 entry includes nine algebraic laws (subsumption of `axpy`, two zero-identities, the reduction-to-`scal` identity, β=1 reduction, bilinearity in (α, β), one distributivity in `x`, one distributivity in `y`, and the chained-`axpby` collapse law), plus an explicit non-law section listing IEEE-754 reordering effects. Variant axes are element-type and scalar-promotion (the latter cross-referencing open question `scalar-promotion-typing-rule`).

## Proposed changes

````edit:book/src/L1/axpby.md
# axpby

Mutation-lifted fused two-scalar two-vector update: `y_new = α·x + β·y_old`. The fused BLAS-1 primitive that subsumes both `axpy` (β=1) and pure-scaling (α=0). At L1, the fused form is a leaf primitive; the decision against decomposing it as `axpy ∘ scal` is recorded in [`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md).

## Context

The L0 source-side forms are:

- `ComplexVector::AXPBY(std::complex<double> α, const ComplexVector &x, std::complex<double> β)` — member call mutating `*this` in place to `α·x + β·(*this)` (`palace/linalg/vector.hpp:130-131`). The destination is the receiver; there is no output argument.
- `linalg::AXPBY<VecType, ScalarType>(ScalarType α, const VecType &x, ScalarType β, VecType &y)` — free-function template (`palace/linalg/vector.hpp:309-311`) with three explicit specialisations:
  - `AXPBY(double, Vector, double, Vector)` (`palace/linalg/vector.cpp:726-730`) delegates to MFEM's `add(α, x, β, y, y)` — MFEM's 5-argument in-place additive combine which writes its last argument from the linear combination of its first four.
  - `AXPBY(std::complex<double>, ComplexVector, std::complex<double>, ComplexVector)` (`palace/linalg/vector.cpp:732-737`) delegates to `y.AXPBY(α, x, β)`, i.e. the member form.
  - `AXPBY(double, ComplexVector, double, ComplexVector)` (`palace/linalg/vector.cpp:739-743`) — real-scalar overload on complex vectors; promotes scalars implicitly and delegates to the same member form.

At L0, the in-place destination `y` is overwritten; the prior value of `y` is consumed by the update and inaccessible afterwards. The L1 form drops the destination-buffer mention: the operator consumes `α`, `x`, `β`, and the pre-update value of `y`, and produces a fresh post-update value. The fusion (single-call combined update rather than the two-pass `y *= β; y += α·x`) is preserved at L1 because it has algebraic meaning — the law `axpby(α, x, β, y) = α·x + β·y` is a primitive statement of the linear combination, not a derived shorthand.

This entry is the firm operator definition for `axpby` at L1; it supersedes the rough-in row in `book/src/L1/index.md` (originally proposed by the cycle-002 abstractor `axpby-mutation-rotation` theme — see [`L1-L0/axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md)). The lowering theme remains the L1>L0 narrative; this entry is the L1 algebra. No `concepts/axpby.md`-style cross-cutting prose exists yet for `axpby` (the existing `concepts/axpy.md` covers `axpy` only); if one is authored, it should cross-reference this entry.

## Signature

```
axpby :: (α: Scalar, x: Tensor[N], β: Scalar, y: Tensor[N]) -> Tensor[N]
axpby(α, x, β, y) = α·x + β·y
```

Shape contract (bunsen-style, named axes):

- `α` — scalar.
- `x` — `Tensor[N]` — read-only.
- `β` — scalar.
- `y` — `Tensor[N]` — read-only (the *prior* value).
- result — `Tensor[N]` — same axis `N` as inputs.

`x` and `y` must share the same length axis `N` and the same element type (both real or both complex). The scalars `α` and `β` share each other's type and the vector element type, with one allowed promotion: real scalars may be passed against complex vectors and the scalars are promoted to complex (zero imaginary part). This mirrors Palace's `AXPBY(double, ComplexVector, double, ComplexVector)` overload at `palace/linalg/vector.cpp:739-743`. Mixed real/complex scalar pairs (one of α, β real and the other complex) are not exposed by Palace and are not part of the L1 signature — promote both or neither.

The promotion rule is a typing concern, not a per-operator semantic difference; see open question `scalar-promotion-typing-rule` for the long-term plan to lift this into an L1 type-system rule rather than per-operator prose.

## Semantics

Element-wise: `result[i] = α·x[i] + β·y[i]` for `i ∈ [0, N)`. Reduction-free and element-local — every output element depends on exactly one input element from each of `x` and `y`. No cross-element communication, no dependence on iteration order.

The operator is pure at L1: the prior `y` and the new `y` are distinct values. The L0 source overwrites the in-place destination buffer; that overwrite is an L1>L0 lowering concern (see [`L1-L0/axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md)). At L1 the relationship is purely algebraic.

Special algebraic cases — `α = 0` (pure scaling of `y`), `β = 0` (pure scaling of `x`, discards `y`), `α = 1, β = 1` (vector add), `β = 1` (recovers `axpy`), `α = -1, β = 1` (vector subtract) — are not separate operators at L1. They are algebraic identities, recorded in the laws below. The L0 source has no specialisation branches inside the `AXPBY` family (unlike the real-path `AXPY` at `vector.cpp:704-706`, which branches on `α == 1.0`); the AXPBY surface is uniformly a single delegation, so there are no L0 sub-patterns to recognise — the L1>L0 lowering for `axpby` is structural (re-bind destination), not algebraic.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Subsumption of `axpy`**: `axpby(α, x, 1, y) = axpy(α, x, y) = α·x + y`. This is the load-bearing identity from `scaffolding/decisions/axpby-as-primitive.md`: `axpy` is a β=1 specialisation of `axpby`, not a dependency.
2. **Identity in `α`**: `axpby(0, x, β, y) = β·y` for any `x`. (When a future `scal :: (β, y) → β·y` primitive lands at L1, this restates as `axpby(0, x, β, y) = scal(β, y)`. Until then, the right-hand side is stated as the scalar-times-vector operation `β·y`.)
3. **Identity in `β`**: `axpby(α, x, 0, y) = α·x` for any `y`. (Likewise restates as `scal(α, x)` once `scal` lands.)
4. **Identities in both**: `axpby(0, x, 0, y) = 0` (the zero vector of axis `N`).
5. **Bilinearity in the scalar pair `(α, β)`**: for scalars `α₁, α₂, β`:
   - `axpby(α₁ + α₂, x, β, y) = axpby(α₁, x, β, y) + axpby(α₂, x, 0, y) - β·y + β·y = α₁·x + α₂·x + β·y` (i.e., the result is linear in `α` with `(x, β, y)` held fixed).
   - Symmetrically linear in `β` with `(α, x, y)` held fixed.
   - Combined: `axpby(α, x, β, y)` is linear separately in each of `α` and `β`.
6. **Right distribution over vector addition in `x`**: `axpby(α, x₁ + x₂, β, y) = axpby(α, x₁, β, y) + axpby(α, x₂, 0, y) = α·x₁ + α·x₂ + β·y`. (The `axpby(α, x₂, 0, y)` term is `α·x₂` per law 3; the `+` is vector addition.)
7. **Right distribution over vector addition in `y`**: `axpby(α, x, β, y₁ + y₂) = axpby(α, x, β, y₁) + β·y₂ = α·x + β·y₁ + β·y₂`.
8. **Scalar absorption**: `axpby(α·γ, x, β, y) = axpby(α, γ·x, β, y) = axpby(α, x, β·γ, γ⁻¹·y)` (the latter only for invertible scalar `γ`) — the scalars absorb into their paired vector.
9. **Chained-`axpby` collapse on shared `x`**: `axpby(α₁, x, β₁, axpby(α₂, x, β₂, y)) = axpby(α₁ + β₁·α₂, x, β₁·β₂, y)`. Two successive `axpby` updates against the same `x` collapse to one with scalars `(α₁ + β₁·α₂, β₁·β₂)`. This generalises law 4 of `axpy` (`axpy(α, x, axpy(β, x, y)) = axpy(α+β, x, y)`, which is the β₁ = β₂ = 1 case) and underwrites the L2 fusion of consecutive coefficient-update lines in Krylov solvers.

Laws that explicitly **do not** hold:

- **Commutativity in the vector arguments**: `axpby(α, x, β, y) ≠ axpby(β, y, α, x)` in general unless `α = β` — but even then the result is symmetric in the inputs only because the operator is structurally `α·x + β·y`. The signature distinguishes "the `x` argument" from "the `y` argument" by which slot pairs with which scalar; swapping both pairs simultaneously preserves the value (because `α·x + β·y = β·y + α·x`), but swapping vectors without swapping scalars does not.
- **Associativity**: `axpby` is quaternary; "associativity" is not well-typed.
- **Floating-point associativity of the summation**: `α·x + β·y` computed in IEEE-754 may differ from `β·y + α·x` at the bit level when the magnitudes of `α·x` and `β·y` differ enough to lose precision in one ordering. Palace's L0 form pins the ordering via MFEM's `add(α, x, β, y, y)` kernel — the L1 algebra is order-agnostic, but bit-identical reproduction of L0 output requires matching the L0 evaluation order. This is recorded here, not erased.
- **Fusion identity with `scal + axpy`**: `axpby(α, x, β, y) ≠ scal(β, axpy(α/β, x, y))` in general at the bit level (the two-pass form rounds twice; the fused form rounds once) even though the values agree mathematically. The L0 form is fused for a reason; the L1 algebra preserves the fused statement. The lowering theme records the fusion choice as load-bearing for performance, not for numerics.

## Dependencies

None at L1. `axpby` is a leaf primitive — the harvester decision (`scaffolding/decisions/axpby-as-primitive.md`) is explicit on this point. Its sub-operations are two scalar multiplications and one element-wise addition, all at or below the L1 layer's resolution.

Subsumption (not dependency): `axpy(α, x, y) ≡ axpby(α, x, 1, y)` — both stay in the L1 dep-map as siblings; the L1>L0 lowering theme `axpby-mutation-rotation` covers `axpy`'s sub-patterns A/B/C as the β=1 specialisation of `axpby`'s lowering (per the abstractor's "Subsumption relation" paragraph).

Future siblings (not dependencies): `axpbypcz` (the three-vector generalisation `z = α·x + β·y + γ·z`) is the next harvester target — see open question `axpby-axpbypcz-next-harvest`. The real-path `AXPBYPCZ` at `vector.cpp:749-752` branches on `γ == 0` and delegates to `AXPBY`, confirming the subsumption chain `axpy ≺ axpby ≺ axpbypcz` at L1 (each generalises the prior by one more scalar-vector pair).

## Variant axes

`axpby` has two variant axes at L1:

- **element-type**: `real` | `complex`. The L0 source has separate template specialisations (real-real at `vector.cpp:726-730`; complex-complex at `vector.cpp:732-737`; real-scalar-on-complex-vector at `vector.cpp:739-743`; member form on `ComplexVector` at `vector.hpp:130-131`). At L1 these collapse to one operator parameterised by element type. The semantics are identical across element types — the per-element kernel is just `α·x[i] + β·y[i]` in the appropriate field.
- **scalar promotion** (sub-axis on the complex element-type): when `α` and `β` are real but vectors are complex, Palace permits implicit promotion via the dedicated overload at `vector.cpp:739-743`. At L1 this is a typing-rule concern (subtype broadcasting), not a separate operator. The long-term plan is to formalise this as an L1 type-system rule rather than per-operator prose — tracked at open question `scalar-promotion-typing-rule`.

No other variant axes — `axpby` is unconditionally pure, element-local, and reduction-free across all variants. Unlike `axpy` (which has the real-path `α == 1.0` constant-folding specialisation at L0), `axpby` has no L0 constant-folding branches — the AXPBY surface uniformly delegates without inspecting scalar values. Consequently, the L1>L0 lowering for `axpby` does not need an algebraic-sub-rule mechanism; it is purely structural.

## Status

`firm` — signature is canonical (matches three Palace L0 entry points exactly), evidence is direct from the Palace source, the algebraic laws listed are standard linear-combination facts, and the decomposition decision is recorded in `scaffolding/decisions/axpby-as-primitive.md`.

## L1 vs L0 distinction

- **L0**: mutating member method (`ComplexVector::AXPBY(α, x, β)` writes through `*this`) or free-function template (`linalg::AXPBY(α, x, β, y)` writes through `y`). Delegates to MFEM's `add(α, x, β, y, y)` for the real-real path or to the member form for the complex paths. No constant-folding branches on `α` or `β`. The evaluation order of `α·x` and `β·y` is pinned by the underlying kernel.
- **L1**: pure functional update. `y_new = axpby(α, x, β, y_old)`. No destination buffer in the signature. Algebraic laws apply directly. The L0 in-place mutation and the L0 fusion choice are both L1>L0 lowering concerns. Floating-point evaluation-order non-associativity is recorded as an explicit non-law, classified as load-bearing for bit-reproduction but not for algorithmic correctness.

## Evidence

- `palace/linalg/vector.hpp:130-131` — `ComplexVector::AXPBY` member decl with comment `In-place addition (*this) = alpha * x + beta * (*this).`
- `palace/linalg/vector.hpp:309-311` — free-function template `AXPBY(ScalarType alpha, const VecType &x, ScalarType beta, VecType &y)` declared with comment `Addition y = alpha * x + beta * y.`
- `palace/linalg/vector.cpp:726-730` — `AXPBY(double, Vector, double, Vector)` specialisation: delegates to `add(alpha, x, beta, y, y)` (MFEM's 5-arg in-place linear combine).
- `palace/linalg/vector.cpp:732-737` — `AXPBY(std::complex<double>, ComplexVector, std::complex<double>, ComplexVector)` specialisation: delegates to member `y.AXPBY(alpha, x, beta)`.
- `palace/linalg/vector.cpp:739-743` — `AXPBY(double, ComplexVector, double, ComplexVector)` specialisation: real-scalar-on-complex-vector overload; also delegates to the member form (implicit promotion).
- `palace/linalg/vector.cpp:745-758` — `AXPBYPCZ(double, ...)` real-path with `γ == 0` branch to `add(alpha, x, beta, y, z)` (confirms the subsumption `axpbypcz(α, x, β, y, 0, z) = axpby(α, x, β, y)` at L0).
- `palace/linalg/vector.hpp:133-136` — `ComplexVector::AXPBYPCZ` member decl (forward reference for the next harvester target).
- `palace/linalg/vector.hpp:313-316` — free-function template `AXPBYPCZ` decl (forward reference).
- Decision record: [`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md) — fused-primitive choice rationale.
- Cross-references: `book/src/L1-L0/axpby-mutation-rotation.md` (L1>L0 lowering theme, cycle-002), `book/src/L1/axpy.md` (the β=1 specialisation; sibling L1 leaf).
````

````edit:book/src/L1/index.md
[Row replacement in the operator dep-map. Find the existing rough-in row:

| `axpby` | `(α, x, β, y) → α·x + β·y` | (leaf; subsumes `axpy`) | `rough-in, proposed-by: abstractor:2026-05-26T231843Z-abstractor-axpby-mutation-L1-L0` |

Replace it (in-place; same table position) with:

| [`axpby`](./axpby.md) | `(α, x, β, y) → α·x + β·y` | (leaf; subsumes `axpy`) | `firm` |

No other rows or sections in `book/src/L1/index.md` should change.]
````

````append-after:book/src/SUMMARY.md
# Anchor line (must exist in SUMMARY.md, under the "L1 — Mutation-Lifted Forms" Part):
- [dot](./L1/dot.md)

# Insert immediately after the anchor line above:
- [axpby](./L1/axpby.md)
````

(Integrator hint: this is a targeted insertion, NOT a full-file replacement. `SUMMARY.md` is ~117 lines covering many Parts; only the single new line `- [axpby](./L1/axpby.md)` should be added, positioned directly after the existing `- [dot](./L1/dot.md)` line under the "L1 — Mutation-Lifted Forms" Part heading. All other content in `SUMMARY.md` must be preserved verbatim. Note: cycle-003 dispatch 1 — the `nrm2` harvester — also targets the same anchor; the integrator should merge both additions, placing both `- [axpby](./L1/axpby.md)` and `- [nrm2](./L1/nrm2.md)` after the `- [dot](./L1/dot.md)` line, in whichever order is consistent with the dep-map row order in `L1/index.md`.)

## Operator content

See the `book/src/L1/axpby.md` content in the proposed-changes block above.

## Supporting evidence

- L0 source-side citations: every claim in the operator entry is cited to a `(file:start-end)` range in `reference/palace/`. The eight evidence citations span the three L0 entry points (member `ComplexVector::AXPBY`; free-function template `linalg::AXPBY` with three specialisations; the MFEM `add(α, x, β, y, y)` delegation for the real-real path).
- Cross-cycle context:
  - The cycle-002 abstractor REPORT (`reports/2026-05-26T231843Z-abstractor-axpby-mutation-L1-L0/REPORT.md`) sketched the L1>L0 theme assuming the fused L1 form and explicitly deferred the primitive-vs-decomposed choice to harvester via open question `axpby-axpby-scal-decomposition-decision`. This report resolves that question.
  - The cycle-002 dot harvester REPORT (`reports/2026-05-26T231843Z-harvester-dot-L1/REPORT.md`) is the format reference for this report's structure (frontmatter inputs/skill_uptake, proposed-changes block style, four-backtick fences, append-after SUMMARY pattern).
  - The pilot-1 axpy harvester REPORT (`reports/2026-05-26T223039Z-harvester-axpy-L1/`) established the L1 entry format that `axpy.md` and now `axpby.md` follow; the subsumption law (Law 1) explicitly preserves the `axpy` entry's place in the L1 dep-map.
- Decision record (new this cycle): `scaffolding/decisions/axpby-as-primitive.md` captures the fused-primitive choice with rationale (algebraic, engineering, and trade-offs accepted).
- Open-question status: `axpby-axpby-scal-decomposition-decision` should be marked `answered` by the integrator (answered_in: this commit; answered_at: cycle-003). The `axpby-axpbypcz-next-harvest` question remains open — the `axpby` half is now done; the `axpbypcz` half is the next harvester target.

## Open questions / caveats

1. **Decision recorded outside operator entry.** The fused-primitive vs. decomposed choice is captured in `scaffolding/decisions/axpby-as-primitive.md` (a new decision-log entry) rather than inline in `book/src/L1/axpby.md`. The operator entry references the decision in two places (chapeau paragraph and Dependencies section); readers wanting the rationale follow the link. This matches the precedent of `scaffolding/decisions/integration-plan-architecture.md` — decisions live in scaffolding, operators in `book/`.

2. **`scal` is referenced but not yet a primitive.** Laws 2 and 3 ("Identity in `α`", "Identity in `β`") state right-hand sides as `β·y` and `α·x` respectively, with parenthetical notes that they will restate as `scal(β, y)` and `scal(α, x)` once `scal` lands as a separate L1 primitive. This forward reference is recorded; no action needed by integrator. A future cycle harvesting `scal` should revisit these two laws (one-line cosmetic update; the algebra is unchanged).

3. **`axpbypcz` is the next harvester target.** Open question `axpby-axpbypcz-next-harvest` had two halves; this report closes the `axpby` half. The `axpbypcz` half (Palace's three-vector generalisation `z = α·x + β·y + γ·z` at `vector.hpp:133-136` and `vector.cpp:745-772`) should land in a future cycle. The L0 evidence at `vector.cpp:749-752` shows the real-path `AXPBYPCZ` branches on `γ == 0` and delegates to `AXPBY`, so `axpbypcz` will subsume `axpby` (which subsumes `axpy`) — a three-level chain. Recommend the next harvester invocation mirror the fused-primitive decision for `axpbypcz` for consistency. A new abstractor sketch of `axpbypcz-mutation-rotation` (companion theme to the existing `axpby-mutation-rotation`) is also pending; cycle-planner may want to schedule both together.

4. **`scalar-promotion-typing-rule` continues to surface per-operator.** This entry, like `axpy` and `dot` before it, states the real-scalar-on-complex-vector promotion rule in per-operator prose (Signature section). The cross-operator pattern is now visible: every L1 operator that takes scalar arguments will need this clause until the L1 type-system rule lands. Recommend cycle-planner consider promoting `scalar-promotion-typing-rule` to a higher priority — three operators now stating the same rule is the threshold for lifting it into a typing-rule layer.

5. **L1 layer-intro refresh approaching the trigger.** Pilot-1's open question `l1-index-refresh` set "≥3 L1 operators" as the threshold for an intro refresh. After this report lands, the L1 dep-map has three firm operators (`axpy`, `dot`, `axpby`). The trigger is met. Recommend cycle-planner schedule a `layer-intro-author` invocation for the L1 Part overview in the next cycle. (Out of scope for harvester — flagging per role discipline.)

6. **Lowering-verifier audit remains pending.** Open question `axpby-lowering-verifier-audit` (opened by cycle-002 abstractor) asks for a corpus-wide audit of the three sub-pattern recognition rules in the `axpby-mutation-rotation` theme. That theme remains `rough-in` at L1-L0 pending the audit. This report does not move that status forward — it only addresses the L1 algebra. The lowering-verifier dispatch can now proceed with the L1 `axpby` algebra fixed, which gives the verifier a stable target.

7. **No `concepts/axpby.md` exists.** Unlike `axpy` and `dot`, `axpby` has no concept-page cross-reference. If a future cycle authors one, it should cross-reference this L1 entry rather than duplicate the algebraic-laws content; the same-layer-cross-cutter precedent set by the cycle-002 dot harvester REPORT applies.
