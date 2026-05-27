---
agent: layer-intro-author
invoked_at: 2026-05-27T025354Z
scope: concepts/scalar-promotion (new concept page)
status: integrated
integrated_at: 2026-05-27T07:04:24Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied. New methodology concept page covering scalar-promotion across 4 L1 operators (axpy/axpby/axpbypcz/scal). Answers cycle-002 scalar-promotion-typing-rule (5 operators were past threshold). Retroactive L1 thinning is cycle-006+ follow-up.
---

# REPORT: concepts/scalar-promotion

## Summary

Authors a new cross-cutting concept page `book/src/concepts/scalar-promotion.md` covering the real→complex implicit scalar promotion typing rule. The rule currently appears as four repeated per-operator paragraphs across `axpy`, `axpby`, `axpbypcz`, and `scal` (the task brief named five operators including `dot`, but `dot` returns a scalar and has no input α to promote — the rule does not actually appear there; this is recorded as a correction in Open questions below). Concept page is purely additive: no retroactive edits to the four L1 entries (that backlink work is priority #11, cycle-006+).

The page collapses the duplicate prose into one canonical statement, ties the rule to Palace's explicit overload set (`vector.cpp:715-718`, `739-743`, `767-772`, and the `imag() == 0.0` branch at `vector.cpp:207-211` for `scal`), and explains why this is a *typing rule* (collapses to one L1 operator per promoted-case) rather than an operator variant. Also adds the concept to the index in `book/src/concepts/index.md`.

## Proposed changes

```edit:book/src/concepts/scalar-promotion.md
[old]: <file does not exist — create>
[new]:
# scalar-promotion

The implicit-coercion typing rule that lets a real-typed scalar argument enter a Palace L1 vector operator whose vector operands are complex-typed. Concretely: where a complex-vector operator nominally requires complex scalars, Palace's L0 surface also exposes a sibling overload taking real scalars against the same complex vectors, with the scalars promoted to complex (zero imaginary part) before the per-element kernel runs. At L1 this is a single operator, parameterised over scalar-vs-vector element types via the promotion lattice `real ⊑ complex` on scalars; no per-operator semantic branch.

## Rule statement

Given an L1 vector operator with shape `(scalars..., vectors...)` and a vector element type `T ∈ {real, complex}`:

- If `T = real`, scalar arguments must be `real`.
- If `T = complex`, scalar arguments may be either `complex` (no promotion) or `real` (promoted to complex with zero imaginary part).
- *Mixed* scalar tuples (some real, some complex, against complex vectors) are not exposed by Palace and are not part of the L1 signature — promote all-or-none.

The promotion is exact (zero imaginary part is representable exactly in IEEE-754 complex doubles). The L1 operator's algebraic laws are invariant under the promotion: every law that holds for a promoted-real-scalar call holds identically for the equivalent complex-scalar call with zero imaginary part.

## Where it applies in Palace

The rule is realised at L0 by a small set of dedicated overloads in `palace/linalg/vector.{hpp,cpp}`:

- `AXPY(double, ComplexVector, ComplexVector)` — `palace/linalg/vector.cpp:715-718`. Delegates to the member-form `y.AXPY(alpha, x)`, which the body specialises for `double alpha`.
- `AXPBY(double, ComplexVector, double, ComplexVector)` — `palace/linalg/vector.cpp:739-743`. Delegates to `y.AXPBY(alpha, x, beta)` with both scalars real.
- `AXPBYPCZ(double, ComplexVector, double, ComplexVector, double, ComplexVector)` — `palace/linalg/vector.cpp:767-772`. Delegates to `z.AXPBYPCZ(alpha, x, beta, y, gamma)` with all three scalars real.
- `ComplexVector::operator*=(std::complex<double> s)` — `palace/linalg/vector.cpp:203-227`. Branches on `s.imag() == 0.0` (line 207); the real-scalar path runs `Real() *= sr; Imag() *= sr` (two real `operator*=` calls). This is the `scal` site; the promotion is internal (the L0 caller passes `std::complex<double>` but Palace recognises the real special case), not a separate overload.

All four sites are direct evidence of the rule. The first three are overload-based (the L0 user calls the real-scalar entry point); the fourth is value-based (the L0 user calls the complex-scalar entry point with `imag == 0`). At L1 both shapes collapse to the same promotion lattice.

## Why it's a typing rule, not an operator variant

The promoted-real-scalar call and the explicit-complex-scalar call (with zero imaginary part) compute identical values element-for-element. Treating them as two L1 operators would force every algebraic law to be restated for both, every call site to disambiguate which overload it calls, and every L1>L0 lowering theme to carry the constant-folding optimisation (real-scalar fast-path) as an algebraic-sub-rule rather than as a transparent performance trick.

Treating them as one L1 operator (with the scalar's nominal type lifted by `real ⊑ complex`) collapses all of this. The L1 operator is well-typed against the promoted call because the promotion is exact (zero imaginary part); the L1>L0 lowering reintroduces the real-scalar fast path as a transparent constant-folding sub-rule (no algebraic content); and the four L1 operator entries each have one variant-axes paragraph that points here rather than restating the rule.

## Operators where it applies

- [`axpy`](../L1/axpy.md) — `axpy :: (α, x, y) → α·x + y`. Promotion of `α` against complex `x, y` via `AXPY(double, ComplexVector, ComplexVector)` (`vector.cpp:715-718`).
- [`axpby`](../L1/axpby.md) — `axpby :: (α, x, β, y) → α·x + β·y`. Promotion of `(α, β)` together against complex `x, y` via `AXPBY(double, ComplexVector, double, ComplexVector)` (`vector.cpp:739-743`).
- [`axpbypcz`](../L1/axpbypcz.md) — `axpbypcz :: (α, x, β, y, γ, z) → α·x + β·y + γ·z`. Promotion of `(α, β, γ)` together against complex `x, y, z` via `AXPBYPCZ(double, ComplexVector, double, ComplexVector, double, ComplexVector)` (`vector.cpp:767-772`).
- [`scal`](../L1/scal.md) — `scal :: (α, x) → α·x`. Internal promotion of `α` against complex `x` via the `s.imag() == 0.0` branch in `ComplexVector::operator*=` (`vector.cpp:207-211`).

## When it does NOT apply

- **Mixed scalar tuples against complex vectors**: e.g. `AXPBY(double, ComplexVector, std::complex<double>, ComplexVector)` — one real, one complex scalar against complex vectors. Palace exposes no such overload. At L1 this is a type error (the promotion rule is all-or-none across the scalar tuple).
- **Complex scalars against real vectors**: e.g. a hypothetical `AXPY(std::complex<double>, Vector, Vector)`. Palace exposes no such overload (it would lose information — the imaginary part has no destination in a real vector). At L1 this is a type error; the promotion lattice runs `real ⊑ complex` for scalars only, never the reverse.
- **Reductions returning complex from real inputs**: not a promotion site. `dot :: (x, y) → scalar` has no input scalar to promote — the scalar is the *output*. The return type is determined by the vector element type (real vectors → real scalar; complex vectors → complex scalar); the rule does not apply.
- **Norm-style reductions**: same as `dot` — `nrm2 :: x → ℝ⁺` returns a real scalar regardless of vector type. No input scalar; no promotion.

## See also

- [`complex-from-real-lift`](./complex-from-real-lift.md) — a *different* real↔complex lift at the **operator** level (real solver acting on complex vectors), not the scalar level. Distinct concept; both are real→complex coercions but they live at different axes.
- Open question `scalar-promotion-typing-rule` (in `scaffolding/open-questions.md`) — this concept page is the first concrete deposit toward closure of that question. Closure depends on the L1 calculus formally adopting the `real ⊑ complex` scalar lattice (not yet committed).
```

```edit:book/src/concepts/index.md
[old]: | [scal](./scal.md) | primitive |
[new]: | [scal](./scal.md) | primitive |
| [scalar-promotion](./scalar-promotion.md) | methodology |
```

## Supporting evidence

L1 operator entries that currently restate the rule per-operator (to be back-linked in cycle-006+):

- `book/src/L1/axpy.md` — Signature §, lines 25; Variant axes §, line 60. Cites `vector.cpp:715-718`.
- `book/src/L1/axpby.md` — Context §, line 13; Signature §, lines 34-36; Variant axes §, line 83; Evidence §, line 102. Cites `vector.cpp:739-743`.
- `book/src/L1/axpbypcz.md` — Context §, line 13; Signature §, lines 36-38; Variant axes §, line 100; Evidence §, line 121. Cites `vector.cpp:767-772`.
- `book/src/L1/scal.md` — Signature §, line 31; Variant axes §, line 79. Cites `vector.cpp:207-211`.

L0 evidence (verified against `reference/palace/palace/linalg/vector.cpp` at this report's invocation time):

- `vector.cpp:702-712` — real-scalar `AXPY` (no promotion; reference baseline).
- `vector.cpp:715-718` — promoted `AXPY(double, ComplexVector, ComplexVector)`.
- `vector.cpp:739-743` — promoted `AXPBY(double, ComplexVector, double, ComplexVector)`.
- `vector.cpp:767-772` — promoted `AXPBYPCZ(double, ComplexVector, ..., double, ComplexVector)`.
- `vector.cpp:203-227` — `ComplexVector::operator*=` with internal `si == 0.0` branch (line 207).

Citation count in the concept page: 9 unique pointers — 5 `vector.cpp` line ranges (`vector.cpp:715-718`, `739-743`, `767-772`, `203-227`, `207-211`) plus the four `L1/<op>.md` backlinks. Note: `203-227` and `207-211` are dual citations of the same `ComplexVector::operator*=` method — the wider range names the method body (§ "Where it applies"), the narrow range pinpoints the `s.imag() == 0.0` promotion branch (§ "Operators where it applies"); both are correct and intentionally distinguish "method body" from "promotion branch".

## Open questions / caveats

- **Task brief vs evidence mismatch (corrected)**: The cycle-005 dispatch brief named five operators (`axpy`, `dot`, `axpby`, `axpbypcz`, `scal`) where the rule appears. Per grep against `book/src/L1/*.md` at invocation time, `dot.md` does not contain a scalar-promotion paragraph (verified: no match for `promot` in `dot.md`). This is correct — `dot` returns a scalar; it has no input scalar to promote. The L1 dot entry's element-type rule is about the *return type* (real-vectors → real, complex-vectors → complex), which is a different typing concern from scalar promotion. The concept page lists four operators (`axpy`, `axpby`, `axpbypcz`, `scal`); `dot` is mentioned in the "When it does NOT apply" section as a non-promotion site (reductions). Cycle-006+ retroactive-thinning priority #11 should accordingly target four L1 entries, not five.
- **Cycle-006 back-linking**: this concept page is purely additive. The four L1 entries' duplicated paragraphs remain in place. Cycle-006 cycle-planner should slot priority #11 (retroactive-L1-context-thinning) to: (a) replace the per-operator promotion-rule paragraphs in `axpy.md`, `axpby.md`, `axpbypcz.md`, `scal.md` with one-line backlinks `see [scalar-promotion](../concepts/scalar-promotion.md)`; (b) leave the citation evidence in place (each operator's Evidence § keeps its own promoted-overload citation); (c) update the four operators' Variant axes § "scalar promotion (sub-axis)" bullets to short backlinks rather than full restatements. Estimated context savings: ~600 words across the four entries.
- **Concept-page index taxonomy**: classified as `methodology` (typing-rule, not an operator). Alternative classification `layer-pattern` (it's an L1-specific rule about how the type system collapses L0 overloads) was considered; `methodology` was picked because the rule transcends any single layer (it's a general principle of the promotion lattice). Either is defensible; if the integrator prefers `layer-pattern`, change line in `index.md`.
- **Lattice formalisation deferred**: the open question `scalar-promotion-typing-rule` calls for "lifting this into an L1 type-system rule rather than per-operator prose". This concept page is the *informal* statement of the rule (English + Palace evidence). Formal calculus-level adoption (the L4 typing judgement `Γ ⊢ α : real, Γ ⊢ x : Tensor[complex] ⇒ Γ ⊢ axpy(α, x, y) : Tensor[complex]`) is L4-calculus-design work, not L1-concept-page work. Closing the open question requires both this concept page (now landing) and the L4-calculus extension (future cycle).
