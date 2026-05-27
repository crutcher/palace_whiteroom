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
