---
agent: abstractor
invoked_at: 2026-05-30T22:05:00Z
scope: L1>L0 theme sketch — reciprocal-elementwise-product-mutation-rotation (composite thin-theme; the two diagonal-preconditioner-apply L1 leaves landed c033)
status: pending
integrated_at: 2026-05-31T01:30:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  cycle-034 D1 — applied clean as the cycle's ONLY substantive book-touching landing. Created new firm L1>L0 composite theme `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` (757 lines on disk; sub-patterns A reciprocal + B elementwise-product; 40 citations clean per citecheck-bounds-scan; 43 in the report's pre-apply scan reflects prose-framing). Index dep-map row appended in `book/src/L1-L0/index.md` after `jacobi-smoother-mutation-rotation` and before `minres-iteration`. SUMMARY.md entry registered after `jacobi-smoother-mutation-rotation` per repaired META.md §Repair instruction. OQ ledger: 3 new (`reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch`, `safe-reciprocal-threshold-l1-candidacy`, `mfem-vector-reciprocal-upstream-body-investigation`) + 2 closed (`reciprocal-l1-l0-mutation-rotation-theme`, `elementwise-product-l1-l0-mutation-rotation-theme`). Build `cargo make book` exit 0, 88.60s, the new chapter renders; 2 non-fatal pulldown-cmark unclosed-HTML-tag WARNs on `<operator>`/`<complexoperator>` from C++-template-in-prose pattern (pre-existing artifact-wide pattern; siblings `<opertype>`/`<vectype>`/`<other>` produce identical WARNs in existing firm chapters — non-blocking, no repair). 4 KaTeX `Potential incomplete link` warnings in the new theme are part of the artifact-wide KaTeX false-positive class (74 total across the corpus including many long-firm files). retroactive-budget per-slice/global 0. Wave-conflict: none. The composite-vs-split decision (thin single theme co-housing two L1 leaves following the `ksp-solve-mutation-rotation` precedent) records cleanly without friction.
inputs:
  - book/src/L1/reciprocal.md (firm L1, landed c033)
  - book/src/L1/elementwise_product.md (firm L1, landed c033)
  - book/src/L1-L0/jacobi-smoother-mutation-rotation.md (firm c033; sub-pattern A forward-references these leaves as plain text)
  - book/src/L1-L0/dot-mutation-rotation.md (structural thin-theme precedent; 3 sub-patterns A/B/C)
  - book/src/L1-L0/ksp-solve-mutation-rotation.md (NOT present at L2-L1 path; instead consulted L1>L0 thin-theme siblings dot-/normalize-/scal-mutation-rotation)
  - palace/linalg/vector.cpp:248-261 (ComplexVector::Reciprocal definition — verified)
  - palace/linalg/jacobi.cpp:30-39 (real Apply elementwise-multiply consumer — verified)
  - palace/linalg/jacobi.cpp:41-69 (complex Apply elementwise-multiply consumer + dead-code transpose branch — verified)
  - palace/linalg/jacobi.cpp:99-104 (JacobiSmoother::Mult entry — verified)
  - palace/linalg/operator.cpp:478-487 / :489-507 / :545-568 (canonical BaseDiagonalOperator::Mult + MultHermitianTranspose — verified)
  - palace/linalg/vector.hpp:20 (using Vector = mfem::Vector alias — verified)
  - palace/linalg/vector.hpp:107-108 (ComplexVector::Reciprocal declaration — verified)
---

# CYCLE: L1>L0 theme sketch — reciprocal-elementwise-product-mutation-rotation

## Summary

Author the L1>L0 lowering theme for the two diagonal-preconditioner-apply L1 leaves landed in cycle-033: `reciprocal` (elementwise multiplicative-inverse) and `elementwise_product` (Hadamard pointwise product). Per the planner's recommendation and the `ksp-solve-mutation-rotation` thin-theme precedent, the two leaves are authored as **a single composite theme** with **sub-patterns A (reciprocal) + B (elementwise-product)** — they share the in-place-receiver-overwrite L0 mutation shape (both lower a fresh-value-returning L1 form into an in-place L0 `forall_switch` element-loop), differ only in the scalar kernel (complex closed-form inverse `s = 1/|z|²; XR *= s; XI *= -s` for `reciprocal` vs the single elementwise multiply `Y[i] = D[i]·X[i]` and the six-fused-MA complex multiply for `elementwise_product`), and are jointly consumed by the diagonal-preconditioner setup chain `assemble_diagonal → reciprocal → elementwise_product`. The rewrite is structural — destination-buffer reintroduction over an element-local pure map (sub-pattern A: receiver self-overwrite `*this = reciprocal(*this)`; sub-pattern B: output-arg `y = elementwise_product(a, b)` writing through `y`). One algebraic sub-rule: the complex `reciprocal` closed form `1/z = z̄/|z|²` (L1 reciprocal law 5) recognises the L0 kernel's three-line `s = 1/(XR²+XI²); XR *= s; XI *= -s` realisation. Conjugation sub-axis on `elementwise_product` (complex element-type only): the `BaseDiagonalOperator::MultHermitianTranspose` kernel (`palace/linalg/operator.cpp:545-568`, three sign flips at `:564-565`) realises `ā ⊙ b`. Status: `firm` — every sub-rule reads straight off the source.

## Proposed changes

```new:book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md
# reciprocal-elementwise-product-mutation-rotation

The mutation rotation for the two diagonal-preconditioner-apply L1 leaves —
elementwise multiplicative-inverse and Hadamard pointwise product. Lowers the
pure L1 forms [`reciprocal`](../L1/reciprocal.md) — `result = reciprocal(x)`,
the elementwise `1/x[i]` map — and [`elementwise_product`](../L1/elementwise_product.md)
— `result = elementwise_product(a, b)`, the Hadamard `a ⊙ b` — into Palace's
L0 in-place mutation surfaces: respectively the receiver-self-overwrite
`Reciprocal()` member-method pair (real `mfem::Vector::Reciprocal()` upstream
MFEM, complex `ComplexVector::Reciprocal()` at `palace/linalg/vector.cpp:248-261`),
and the output-arg `BaseDiagonalOperator::Mult(x, y)` / consumer-local `Apply(dinv, x, y)`
forall-switch elementwise-multiply kernel family. Narrated forward: each L1 pure
elementwise map dissolves into an L0 `forall_switch` element-loop that writes
through the destination buffer (`*this` receiver for sub-pattern A; the `y`
output argument for sub-pattern B). Sibling thin-theme to
[`dot-mutation-rotation`](./dot-mutation-rotation.md) (the BLAS-1 leaf-level
thin-theme; same one-theme-multiple-sub-patterns shape, but here the sub-patterns
are *different L1 operators* sharing a destination-binding rewrite class, where
the dot theme's sub-patterns were *different surface forms* of one operator).
The composite framing follows the planner's recommended thin-theme decomposition
(the two leaves co-occur in the same setup chain
`assemble_diagonal → reciprocal → elementwise_product`, both witnessed line-for-line
inside `JacobiSmoother::SetOperator` at `palace/linalg/jacobi.cpp:79-80,103`).

## Slug

`reciprocal-elementwise-product-mutation-rotation`

## L1 form (LHS)

Two pure-functional element-local maps, both reduction-free, both rank-local
(no MPI collective at any layer); they share the BLAS-1-leaf "Tensor[N] in,
Tensor[N] out" shape but differ in arity and per-element kernel.

### LHS — A: reciprocal

    reciprocal :: (x: Tensor[N]) -> Tensor[N]
    reciprocal(x)[i] = 1 / x[i]            -- ℝ: 1/x[i]
                     = x̄[i] / |x[i]|²       -- ℂ: closed-form (L1 reciprocal law 5)

Partial at `x[i] = 0`; precondition is `x[i] ≠ 0 ∀ i`
([`L1/reciprocal`](../L1/reciprocal.md) §Semantics; the consumer-side
enforcement `// Assumes A SPD (diag(A) > 0)` at `palace/linalg/jacobi.cpp:16`
discharges it operator-class-wide).

### LHS — B: elementwise-product

    elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]
    elementwise_product(a, b) = a ⊙ b      -- result[i] = a[i] · b[i]

Conjugation sub-axis on the complex element-type
([`L1/elementwise_product`](../L1/elementwise_product.md) §Variant axes):

    elementwise_product_conj :: (a: ComplexTensor[N], b: ComplexTensor[N]) -> ComplexTensor[N]
    elementwise_product_conj(a, b) = ā ⊙ b

Both forms are commutative-up-to-conjugation, associative, with `𝟙` as identity,
`𝟘` as absorbing element, distributive over vector addition. Neither has an MPI
collective at any layer (the L1 forms are agnostic to data placement; ranks own
disjoint slices of `N`).

## L0 form (RHS)

The rewrite splits into two sub-patterns, one per L1 leaf. Each sub-pattern is
a destination-binding rewrite: an L1 pure-value return is reintroduced as an
in-place write through a designated destination (the receiver `*this` for
sub-pattern A; the `y` output argument for sub-pattern B). Both sub-patterns
are realised by `mfem::forall_switch` element-loops with per-element kernel
bodies that match the L1 closed forms verbatim.

### Sub-pattern A — `reciprocal` lowers to in-place receiver `Reciprocal()` member-method pair

The L1 value `result = reciprocal(x)` lowers to an in-place receiver mutation
`x.Reciprocal()` (the receiver `*this` becomes both the input source and the
output destination). There is **no free-function** `linalg::Reciprocal(x, y)`
overload, and **no two-arg out-of-place form** — the receiver-mutating member
method is the only L0 entry point.

#### A.1 — Real path (upstream MFEM, consumed via alias)

    using Vector = mfem::Vector;                   // palace/linalg/vector.hpp:20
    // ...
    dinv.Reciprocal();                             // palace/linalg/jacobi.cpp:80 (consumer)

The real path is **upstream MFEM**: `Vector` is the type alias to
`mfem::Vector` at `palace/linalg/vector.hpp:20`, and `Vector::Reciprocal()`
resolves to the upstream MFEM `mfem::Vector::Reciprocal()` method. Per
CLAUDE.md "Many symbols resolve into upstream libraries... Specialized agents
cite Palace source, not vendored upstream." The behaviour is taken as given —
elementwise `*x = 1/(*x)` in `ℝ` — and the lowering recognises the
`x.Reciprocal()` Palace consumer-call as the L0 surface form of the L1
`reciprocal(x)` operator. The four Palace consumer sites (cited under
**Verified-against**) all use this aliased form on a real `Vector` or on a
complex `ComplexVector` — the dispatch is by static C++ type.

#### A.2 — Complex path (Palace-defined, full closed-form)

    void ComplexVector::Reciprocal()              // palace/linalg/vector.cpp:248
    {
      const bool use_dev = UseDevice();
      const int N = Size();
      auto *XR = Real().ReadWrite(use_dev);
      auto *XI = Imag().ReadWrite(use_dev);
      mfem::forall_switch(use_dev, N,
                          [=] MFEM_HOST_DEVICE(int i)
                          {
                            const auto s = 1.0 / (XR[i] * XR[i] + XI[i] * XI[i]);
                            XR[i] *= s;
                            XI[i] *= -s;
                          });
    }

The L0 complex kernel is the full closed-form complex multiplicative-inverse
`1/(a + bi) = (a − bi)/(a² + b²)` realised via the intermediate squared modulus
`s = 1/|z|²`. Three lines per element:

1. `s = 1 / (XR² + XI²)` — compute the inverse-squared-modulus scalar (one
   division, one multiply, one add).
2. `XR[i] *= s` — write the real part `Re(1/z) = a · s = a/|z|²` in place.
3. `XI[i] *= -s` — write the imag part `Im(1/z) = -b · s = -b/|z|²` in place.

The kernel is element-local, reduction-free, rank-local, with **no zero-guard**
(`s = 1/0 = +∞` propagates as NaN/±∞ on a zero entry — the consumer-side
precondition `x[i] ≠ 0` is enforced at the call site, per the SPD assumption
at `palace/linalg/jacobi.cpp:16`).

The crucial L0 facts the L1 form erases:

- **Receiver-self-overwrite mutation.** The receiver `*this` is both the
  source (`Real().ReadWrite()` / `Imag().ReadWrite()` reads from the receiver's
  components) AND the destination (the same buffers are written back). The L1
  form takes `x` as a value and returns a fresh result; the L0 form mutates
  `*this` in place. There is no separate destination buffer — the L1>L0
  mutation rotation is the receiver-as-destination idiom (the same shape as
  the [`scal-mutation-rotation`](./scal-mutation-rotation.md) receiver-mutation
  `x *= α` and the [`normalize-mutation-rotation`](./normalize-mutation-rotation.md)
  receiver-rescale `x *= 1/norm`).
- **Intermediate `s` is a transparent factoring.** The scalar
  `s = 1/(XR² + XI²) = 1/|z|²` is computed once per element and reused for
  both component writes — algebraically identical to the unfused
  `XR = a/(a²+b²); XI = -b/(a²+b²)` form, with one fewer division per element.
  Transparent performance trick; L1 reciprocal law 5 holds either way.
- **No zero-guard.** The closed-form `(a-bi)/(a²+b²)` produces NaN/±∞ when
  `|z|² = 0`. L1 records this as **partiality** on the input (precondition
  `x[i] ≠ 0`), not as a runtime check in the kernel.
- **`forall_switch` device-uniform dispatch.** The host/device split is a
  transparent execution-model concern; the L1 form is the elementwise map,
  agnostic to where it runs.
- **No `linalg::Reciprocal(x, y)` two-arg form exists.** The L1 form is
  unconditionally out-of-place (pure functional); the L0 form is
  unconditionally in-place (receiver-mutating). The lowering's first job is
  to materialise a destination, then route the receiver through it.

Justification kind: **structural** (the receiver-self-overwrite binding is a
syntactic L1>L0 mutation rewrite) **+ algebraic** (the complex closed-form
`1/z = z̄/|z|²` recognition rule of L1 reciprocal law 5 against the three-line
`s, XR *= s, XI *= -s` body).

Citations:

- `palace/linalg/vector.hpp:20` — `using Vector = mfem::Vector;` — the
  real-path type alias; `Vector::Reciprocal()` resolves to upstream MFEM.
- `palace/linalg/vector.hpp:107` — `// Set all entries to their reciprocal.`
  — the complex method's doc-comment surface contract (one-line elementwise
  inverse).
- `palace/linalg/vector.hpp:108` — `void Reciprocal();` — the complex
  `ComplexVector::Reciprocal()` declaration; void return, no args, mutating.
- `palace/linalg/vector.cpp:248-261` — `ComplexVector::Reciprocal()`
  definition; the closed-form `s = 1/|z|²; XR *= s; XI *= -s` body realising
  L1 reciprocal law 5 verbatim. Lines `:250` device-flag query, `:251` size
  query, `:252-253` read-write component pointer setup, `:254-260`
  `forall_switch` kernel.
- `palace/linalg/jacobi.cpp:80` — `dinv.Reciprocal();` (real or complex `dinv`
  depending on the template instantiation `JacobiSmoother<OperType>`; the
  primary consumer site, immediately after `op.AssembleDiagonal(dinv)` at `:79`).
- `palace/linalg/chebyshev.cpp:178` — `dinv.Reciprocal();` (4th-kind
  Chebyshev consumer).
- `palace/linalg/chebyshev.cpp:241` — `dinv.Reciprocal();` (1st-kind
  Chebyshev consumer).
- `palace/fem/bilinearform.cpp:278` — `test_multiplicity.Reciprocal();`
  (FE-assembly multiplicity-averaging consumer; converts per-true-dof
  contribution count into averaging weight).

### Sub-pattern B — `elementwise_product` lowers to in-place `Mult(x, y)` / `Apply(dinv, x, y)` kernel cohort

The L1 value `y = elementwise_product(a, b)` lowers to an in-place
destination-arg mutation `y = a ⊙ b` writing through the output argument `y`.
Three closely-related L0 surface forms realise the same per-element kernel
across the operator-class wrapping and the consumer-local inline duplicate.

#### B.1 — Canonical operator-action form: `BaseDiagonalOperator::Mult`

    template <>
    void BaseDiagonalOperator<Operator>::Mult(const Vector &x, Vector &y) const
    {                                              // palace/linalg/operator.cpp:478-487
      const bool use_dev = x.UseDevice() || y.UseDevice();
      const int N = this->height;
      const auto *D = d.Read(use_dev);
      const auto *X = x.Read(use_dev);
      auto *Y = y.Write(use_dev);
      mfem::forall_switch(use_dev, N, [=] MFEM_HOST_DEVICE(int i) { Y[i] = D[i] * X[i]; });
    }

The real canonical site: one elementwise multiply per element,
`Y[i] = D[i] * X[i]` at `:486`, writing through the output argument `y`. The
operator's diagonal vector `d` (a `BaseDiagonalOperator` member) is the
implicit second operand — this is the L0 surface where "the operator IS its
diagonal vector" wrapping holds (L1 `elementwise_product` law 9:
`apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`).

The complex canonical site (`palace/linalg/operator.cpp:489-507`) is the standard complex
multiplication `(d_R + i·d_I)(x_R + i·x_I) = (d_R·x_R − d_I·x_I) + i·(d_I·x_R + d_R·x_I)`:

    YR[i] = DR[i] * XR[i] - DI[i] * XI[i];        // palace/linalg/operator.cpp:504
    YI[i] = DI[i] * XR[i] + DR[i] * XI[i];        // palace/linalg/operator.cpp:505

Six fused multiply-adds per element across `(YR, YI, DR, DI, XR, XI)`. Reads
through `Real().Read()` / `Imag().Read()` of `d` and `x`; writes through
`Real().Write()` / `Imag().Write()` of `y`.

#### B.2 — Conjugate variant (complex element-type only): `MultHermitianTranspose`

    template <>
    void DiagonalOperatorHelper<BaseDiagonalOperator<ComplexOperator>,
                                ComplexOperator>::MultHermitianTranspose(
                                    const ComplexVector &x, ComplexVector &y) const
    {                                              // palace/linalg/operator.cpp:545-568
      // ... read pointer setup ...
      mfem::forall_switch(use_dev, N,
                          [=] MFEM_HOST_DEVICE(int i)
                          {
                            YR[i] = DR[i] * XR[i] + DI[i] * XI[i];
                            YI[i] = -DI[i] * XR[i] + DR[i] * XI[i];
                          });
    }

The conjugate-variant kernel realises `d̄ ⊙ x` algebraically via three sign
flips on the cross-terms (sign-flip on `DI*XI` in the real part; sign-flip on
`DI*XR` in the imag part — net effect is conjugation of `d`):

    (d_R − i·d_I)(x_R + i·x_I) = (d_R·x_R + d_I·x_I) + i·(−d_I·x_R + d_R·x_I)

This is the L0 realisation of L1 `elementwise_product`'s conjugation sub-axis
on the complex side. The real-element-type conjugation is identity (no sign
flips needed); `BaseDiagonalOperator<Operator>::MultTranspose` aliases to
`Mult` (`palace/linalg/operator.hpp:279`), so the real conjugation kernel does not duplicate
into a separate body.

#### B.3 — Consumer-duplicate form: `Apply(dinv, x, y)` namespace-local helper (`jacobi.cpp:30-69`)

    template <bool Transpose = false>
    inline void Apply(const Vector &dinv, const Vector &x, Vector &y)
    {                                              // palace/linalg/jacobi.cpp:30-39
      const bool use_dev = dinv.UseDevice() || x.UseDevice() || y.UseDevice();
      const int N = dinv.Size();
      const auto *DI = dinv.Read(use_dev);
      const auto *X = x.Read(use_dev);
      auto *Y = y.Write(use_dev);
      mfem::forall_switch(use_dev, N, [=] MFEM_HOST_DEVICE(int i) { Y[i] = DI[i] * X[i]; });
    }

The real-path `Apply` helper is **line-for-line identical** to
`palace/linalg/operator.cpp:486` modulo the variable rename `D → DI` — same single multiply
`Y[i] = DI[i] * X[i]` at `:38`. It is a **consumer-local duplicate** of the
canonical kernel: the Jacobi smoother bypasses `BaseDiagonalOperator::Mult`
and inlines the kernel directly (avoiding the operator-class wrapping for the
preconditioner-apply hot path). Cross-witness for the canonical real form.

The complex-path `Apply` helper (`jacobi.cpp:41-69`) carries two branches —
forward (`Transpose=false`) and transpose (`Transpose=true`):

    if constexpr (!Transpose) {                    // jacobi.cpp:52-60 (forward; LIVE)
      mfem::forall_switch(use_dev, N,
                          [=] MFEM_HOST_DEVICE(int i)
                          {
                            YR[i] = DIR[i] * XR[i] - DII[i] * XI[i];
                            YI[i] = DII[i] * XR[i] + DIR[i] * XI[i];
                          });
    } else {                                       // jacobi.cpp:61-69 (transpose; DEAD CODE)
      mfem::forall_switch(use_dev, N,
                          [=] MFEM_HOST_DEVICE(int i)
                          {
                            YR[i] = DIR[i] * XR[i] + DII[i] * XI[i];
                            YI[i] = -DII[i] * XR[i] + DIR[i] * XI[i];
                          });
    }

- Forward branch (`:52-60`): line-for-line identical to the canonical
  `BaseDiagonalOperator<ComplexOperator>::Mult` at `palace/linalg/operator.cpp:504-505`
  modulo the `DI → DIR, DII` Real/Imag-component variable rename.
  Cross-witness for the canonical complex straight form. Live (called by
  `JacobiSmoother::Mult`).
- Transpose branch (`:61-69`): line-for-line identical to the canonical
  `MultHermitianTranspose` at `palace/linalg/operator.cpp:564-565` (same three sign
  flips). **Dead code** under Palace's symmetric wiring —
  `JacobiSmoother::MultTranspose` aliases to `Mult` (`jacobi.hpp:43`,
  one-liner `{ Mult(x, y); }`), not to `Apply<Transpose=true>`. The L0
  conjugate kernel is *defined* but *never instantiated* in the consumer.
  Recognition rule for potential non-symmetric sites; same defined-not-used
  status as the chebyshev sibling's complex transpose kernels
  (`palace/linalg/chebyshev.cpp:101-110, :150-159`) recorded in the
  `chebyshev-smoother-mutation-rotation` theme and as the dead-code caveat
  in [`jacobi-smoother-mutation-rotation`](./jacobi-smoother-mutation-rotation.md)
  sub-pattern B.

The crucial L0 facts the L1 form erases:

- **Output-arg destination mutation.** `y` is the output argument; the kernel
  writes through it via `auto *Y = y.Write(use_dev);` then `Y[i] = D[i] * X[i]`
  (real) or the six-FMA complex pair. The L1 form returns a fresh value. The
  output-arg idiom is shared with
  [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md),
  [`chebyshev-smoother-mutation-rotation`](./chebyshev-smoother-mutation-rotation.md),
  and [`jacobi-smoother-mutation-rotation`](./jacobi-smoother-mutation-rotation.md)
  sub-pattern B.
- **Operator-class wrapping vs. free binary.** The canonical L0 site (B.1)
  binds one of the two operands as a `BaseDiagonalOperator` member `d`; the
  consumer-duplicate site (B.3) takes both operands as explicit arguments
  `(dinv, x)`. At L1 both collapse to the free binary
  `elementwise_product(a, b)`; the operator-wrapping is recovered as L1
  `elementwise_product` law 9 (`apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`).
  No free-function `linalg::ElementwiseProduct` exists.
- **Conjugation as a structural axis, not a value branch.** The complex side
  carries `MultHermitianTranspose` (`palace/linalg/operator.cpp:545-568`) and the consumer
  `Apply<Transpose=true>` (`jacobi.cpp:61-69`) as separate kernel templates,
  not as a runtime branch on `imag(d) == 0`. The L1 conjugation sub-axis maps
  one-to-one onto the kernel-template choice.
- **Per-element kernel uniformity.** Both canonical and consumer-duplicate
  kernels are uniform `forall_switch` multiplies — no constant-folding fast
  paths (unlike `axpy`'s `α == 1.0` skip or `scal`'s `imag(s) == 0.0`
  complex-shape specialisation). Special algebraic cases (`a = 𝟙`, `a = 𝟘`,
  `a = -1`) are absorbed into algebraic laws, not into runtime branches
  ([`L1/elementwise_product`](../L1/elementwise_product.md) §Variant axes
  non-axes).
- **Element-type variant axis absorbed via template instantiation.** Real
  and complex `BaseDiagonalOperator::Mult` are separate template
  specialisations; real and complex `Apply` are separate namespace-local
  helper overloads. At L1 both collapse to the same `a ⊙ b` action with the
  per-element kernel parameterised by element type.
- **No workspace, no aliasing requirement explicitly enforced.** The kernel
  reads `D[i]` and `X[i]` and writes `Y[i]` at the same index — the loop is
  embarrassingly parallel under the non-aliasing precondition (`y` distinct
  from `a` and `b`). The L0 source provides no `MFEM_ASSERT` against
  aliasing; the L1 form takes operands as values and returns a fresh result,
  so the L0 caller must guarantee distinct buffers (the standard BLAS
  contract; same as
  [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md)).

Justification kind: **structural** — destination-arg `y` re-bind via the
`forall_switch` per-element multiply. The element-type and conjugation
variant axes are absorbed by L0 template instantiation. The
canonical-vs-consumer-duplicate equivalence (B.1 ↔ B.3) is byte-level
identity modulo variable rename.

Citations:

- `palace/linalg/operator.cpp:478-487` — real canonical
  `BaseDiagonalOperator<Operator>::Mult`; per-element body
  `Y[i] = D[i] * X[i]` at `:486` in a `forall_switch` over `N`.
- `palace/linalg/operator.cpp:489-507` — complex canonical
  `BaseDiagonalOperator<ComplexOperator>::Mult`; per-element complex multiply
  body at `:504-505`: `YR[i] = DR[i] * XR[i] - DI[i] * XI[i]; YI[i] = DI[i] * XR[i] + DR[i] * XI[i]`.
- `palace/linalg/operator.cpp:545-568` — complex conjugate-variant canonical
  `DiagonalOperatorHelper<...>::MultHermitianTranspose`; three sign flips
  at `:564-565`: `YR[i] = DR[i] * XR[i] + DI[i] * XI[i]; YI[i] = -DI[i] * XR[i] + DR[i] * XI[i]`.
- `palace/linalg/jacobi.cpp:30-39` — real consumer-duplicate
  `Apply<Transpose>(dinv, x, y)`; per-element body `Y[i] = DI[i] * X[i]` at
  `:38` (line-for-line identical to `palace/linalg/operator.cpp:486` modulo variable
  rename `D → DI`). Cross-witness for the canonical real form.
- `palace/linalg/jacobi.cpp:41-69` — complex consumer-duplicate `Apply`;
  forward branch `:52-60` line-for-line identical to `palace/linalg/operator.cpp:504-505`;
  transpose branch `:61-69` line-for-line identical to
  `palace/linalg/operator.cpp:564-565`. Dead-code transpose branch under Palace's
  symmetric wiring (recognition rule).
- `palace/linalg/jacobi.cpp:99-104` — `JacobiSmoother<OperType>::Mult(x, y) const`
  entry; line `:103` dispatches `Apply(dinv, x, y)` — the only call into
  the consumer-duplicate kernel.

## Applicability conditions

The rewrite preserves semantics when:

1. **No aliasing.**
   - Sub-pattern A: the receiver-self-overwrite `*this = reciprocal(*this)`
     is correct because each element write `XR[i] *= s, XI[i] *= -s` reads
     `XR[i], XI[i]` first (into the local `s` and into the multiply RHS)
     before writing — the receiver-as-source-and-destination is safe
     element-locally. No aliasing concern (the receiver IS the destination,
     intentionally).
   - Sub-pattern B: `y` MUST be distinct from `a` and `b`. The kernel reads
     `D[i]` and `X[i]` then writes `Y[i]` at the same index; under aliasing
     (e.g. `&y == &a`) the read of `A[i]` after the write of `Y[i]` would be
     undefined. The L1 form takes `a, b` as values and returns a fresh `y`,
     so the L0 caller must guarantee distinct buffers (standard BLAS shape).
2. **Element-type conformance.**
   - Sub-pattern A: real `Vector` lowers to upstream MFEM
     `mfem::Vector::Reciprocal()`; complex `ComplexVector` lowers to the
     Palace-defined `ComplexVector::Reciprocal()` at `vector.cpp:248-261`.
     Dispatch is by static C++ type at the call site.
   - Sub-pattern B: real `(Vector, Vector, Vector)` lowers to the real
     template specialisation; complex `(ComplexVector, ComplexVector, ComplexVector)`
     lowers to the complex specialisation. Mixed-type operands are
     ill-typed (no implicit conversion).
3. **Conjugation key matches the algorithm's intent (sub-pattern B,
   complex element-type only).** Selecting `elementwise_product` (straight)
   vs. `elementwise_product_conj` (conjugate-`a`) is value-bearing for
   complex element-type — the two kernels differ in three cross-term signs.
   The lowering chooses `Mult` / `Apply<false>` for straight,
   `MultHermitianTranspose` for conjugate. Real element-type makes the
   conjugation a no-op (`MultTranspose` aliases `Mult` per
   `palace/linalg/operator.hpp:279`).
4. **Nonzero-input precondition (sub-pattern A).** `reciprocal` is partial
   at `x[i] = 0`; the L0 kernel produces NaN/±∞ on a zero entry rather than
   clean-erroring. The consumer-side precondition (e.g.
   `palace/linalg/jacobi.cpp:16` `// Assumes A SPD (diag(A) > 0)` — the
   operator-class-level Jacobi SPD assumption) discharges this. All four
   consumer sites of `Reciprocal()` operate under preconditions that
   exclude zero entries.
5. **Single-machine scope.** Neither sub-pattern touches MPI — both are
   rank-local element-loops over disjoint slices of the length axis. MPI
   distribution is out of scope per CLAUDE.md §Scope; the
   single-rank/multi-rank dichotomy is invisible at this lowering.
6. **The L1 receiver-vs-output-arg shape mismatch is reconciled by the
   lowering.** Sub-pattern A's L0 form has no separate destination — it
   mutates `*this`. Sub-pattern B's L0 form has an explicit `y` output
   argument. The L1 forms are both pure-functional. The lowering's job is to
   materialise the destination buffer (the receiver `*this` in A; the `y`
   argument in B) into which the L1 fresh-return is written. No L1 algebraic
   law is sensitive to which destination idiom is used.

## Justification kind

- **Sub-pattern A** — `structural + algebraic`. Structural: receiver-self-
  overwrite mutation binding of the L1 fresh-return. Algebraic: the complex
  closed-form `1/z = z̄/|z|²` (L1 reciprocal law 5) is the algebraic
  recognition rule against the three-line `s, XR *= s, XI *= -s` kernel
  body (`vector.cpp:257-259`).
- **Sub-pattern B** — `structural`. Destination-arg `y` re-bind via the
  per-element multiply kernel; canonical-vs-consumer-duplicate equivalence
  is byte-level identity modulo variable rename. The conjugation sub-axis
  is structural (kernel-template choice), not algebraic.

The theme as a whole is `structural` with one algebraic sub-rule (the
complex-reciprocal closed-form recognition in sub-pattern A). Both
sub-patterns read straight off positively-cited source with no literature
inference and no negative-anchor reconstruction.

## Speculative L1 operators

**None.** This theme lowers two already-firm L1 leaves
([`L1/reciprocal`](../L1/reciprocal.md) and
[`L1/elementwise_product`](../L1/elementwise_product.md), both landed
cycle-033); it proposes no new L1 vocabulary. A speculative
`safe_reciprocal(x, ε)` operator with threshold zero-guard is named in
[`L1/reciprocal`](../L1/reciprocal.md) §Variant axes (non-axes) as a future
candidate but is not part of this theme — Palace has no zero-guarded
kernel, so no L0 anchor exists. Open question
`safe-reciprocal-threshold-l1-candidacy` (filed below) tracks it.

## Verified-against

L0 evidence ranges (self-verified via `tools/citecheck/citecheck.py --anchor`
this invocation against `reference/palace/palace/linalg/{vector,jacobi,operator}.{hpp,cpp}`):

### Sub-pattern A — `reciprocal` L0 anchors

- `palace/linalg/vector.hpp:20` — `using Vector = mfem::Vector;` — the
  real-path type alias. Self-verified.
- `palace/linalg/vector.hpp:107` — `// Set all entries to their reciprocal.`
  — complex method doc-comment. Self-verified.
- `palace/linalg/vector.hpp:108` — `void Reciprocal();` — complex method
  declaration (void return, no args, mutating). Self-verified.
- `palace/linalg/vector.cpp:248-261` — `ComplexVector::Reciprocal()` body:
  signature `:248`, `use_dev` flag `:250`, `N = Size()` `:251`,
  `XR = Real().ReadWrite(use_dev)` `:252`, `XI = Imag().ReadWrite(use_dev)`
  `:253`, `forall_switch` kernel `:254-260` (`s = 1/(XR² + XI²)` at `:257`,
  `XR *= s` at `:258`, `XI *= -s` at `:259`). Self-verified — anchor lit
  'ComplexVector::Reciprocal' at line 248 within range 248-261.
- `palace/linalg/jacobi.cpp:80` — primary consumer: `dinv.Reciprocal();`
  inside `JacobiSmoother<OperType>::SetOperator`, immediately after
  `op.AssembleDiagonal(dinv)` at `:79`. Self-verified (the `SetOperator`
  body at `:74-97` is verified in
  `book/src/L1-L0/jacobi-smoother-mutation-rotation.md` Sub-pattern A; the
  `Reciprocal()` call lives on line 80 of that body).
- `palace/linalg/jacobi.cpp:16` — consumer-precondition source:
  `// Assumes A SPD (diag(A) > 0) to use Hermitian eigenvalue solver.`
  inside the `GetLambdaMax` helper; the operator-class-level Jacobi
  precondition that discharges the `x[i] ≠ 0` L1 reciprocal partiality.
- `palace/linalg/chebyshev.cpp:178` — second consumer: `dinv.Reciprocal();`
  inside `ChebyshevSmoother<OperType>::SetOperator` (4th-kind Chebyshev).
- `palace/linalg/chebyshev.cpp:241` — third consumer: `dinv.Reciprocal();`
  inside `ChebyshevSmoother1stKind<OperType>::SetOperator` (1st-kind
  Chebyshev).
- `palace/fem/bilinearform.cpp:278` — fourth consumer (non-preconditioner):
  `test_multiplicity.Reciprocal();` — FE-assembly multiplicity-averaging
  step (`1/c[i]` for `SetDofMultiplicity`).

### Sub-pattern B — `elementwise_product` L0 anchors

- `palace/linalg/operator.cpp:478-487` — real canonical
  `BaseDiagonalOperator<Operator>::Mult`; per-element body
  `Y[i] = D[i] * X[i]` at `:486`. Self-verified — anchor lit
  'BaseDiagonalOperator<Operator>::Mult' at line 479 within range 478-487.
- `palace/linalg/operator.cpp:489-507` — complex canonical
  `BaseDiagonalOperator<ComplexOperator>::Mult`; complex multiply body at
  `:504-505`. Self-verified — anchor lit
  'BaseDiagonalOperator<ComplexOperator>::Mult' at line 490 within range
  489-507.
- `palace/linalg/operator.cpp:545-568` — complex conjugate-variant
  `DiagonalOperatorHelper<...>::MultHermitianTranspose`; three sign flips at
  `:564-565`. Self-verified — anchor lit 'MultHermitianTranspose' at line
  548 within range 545-568.
- `palace/linalg/operator.hpp:279` — real `BaseDiagonalOperator<Operator>::MultTranspose`
  aliases to `Mult` (no conjugation-variant body on the real side).
  (Localizing-evidence; not load-bearing-anchor.)
- `palace/linalg/jacobi.cpp:30-39` — real consumer-duplicate
  `Apply<Transpose>(dinv, x, y)`; per-element body `Y[i] = DI[i] * X[i]` at
  `:38`. Self-verified — anchor lit 'Apply(const Vector' at line 31 within
  range 30-39.
- `palace/linalg/jacobi.cpp:41-69` — complex consumer-duplicate `Apply`;
  forward branch `:52-60` straight multiply; transpose branch `:61-69`
  conjugate multiply (dead code under symmetric wiring). Self-verified —
  anchor lit 'Apply(const ComplexVector' at line 42 within range 41-69.
- `palace/linalg/jacobi.cpp:99-104` — `JacobiSmoother::Mult(x, y) const`
  entry; line `:103` `Apply(dinv, x, y)` dispatch. Self-verified — anchor
  lit 'Apply(dinv, x, y)' at line 103 within range 99-104.
- `palace/linalg/jacobi.hpp:43` — `void MultTranspose(...) const override
  { Mult(x, y); }` — the symmetric self-alias that strands
  `Apply<Transpose=true>` (jacobi.cpp:61-69) as dead code. (Recognition-rule
  citation for the dead-code transpose branch.)

### L1 anchors

- `book/src/L1/reciprocal.md` — the firm L1 operator sub-pattern A lowers
  from (landed cycle-033). Closed-form complex law 5 + partiality
  precondition.
- `book/src/L1/elementwise_product.md` — the firm L1 operator sub-pattern B
  lowers from (landed cycle-033). Conjugation sub-axis at §Variant axes;
  diagonal-operator-action identity at law 9.

### L1>L0 sibling precedents (structural template)

- `book/src/L1-L0/dot-mutation-rotation.md` — the structural thin-theme
  precedent: a single theme with multiple sub-patterns realising the same
  L1 operator's L0 expansion. Here the sub-patterns realise *two distinct
  L1 operators* sharing a destination-binding rewrite class, so the
  shape is slightly different — but the per-sub-pattern citation density
  and the structural justification pattern are the same.
- `book/src/L1-L0/scal-mutation-rotation.md` — sibling receiver-mutation
  thin-theme precedent for sub-pattern A's receiver-self-overwrite shape
  (`x *= α` vs `x = reciprocal(x)`).
- `book/src/L1-L0/normalize-mutation-rotation.md` — sibling receiver-
  mutation thin-theme precedent (sub-pattern A category) — `x *= 1/norm`
  rescale via the same receiver-as-destination idiom.
- `book/src/L1-L0/apply-linop-mutation-rotation.md` — sibling output-arg
  thin-theme precedent for sub-pattern B's destination-arg shape
  (`A.Mult(x, y)` vs `BaseDiagonalOperator::Mult(x, y)`).
- `book/src/L1-L0/jacobi-smoother-mutation-rotation.md` — the cycle-033
  parent theme: its sub-pattern A forward-references both leaves; its
  sub-pattern B forward-references the consumer-duplicate
  `Apply(dinv, x, y)` kernel. This thin-theme is what those references
  resolve to.
- `book/src/L1-L0/assemble-diagonal-mutation-rotation.md` — the
  diagonal-extraction L1>L0 theme; the first link in the
  `assemble_diagonal → reciprocal → elementwise_product`
  diagonal-preconditioner setup chain. This theme is the second and third
  links.
- `book/src/L1-L0/chebyshev-smoother-mutation-rotation.md` — sibling
  constructed-operator theme that also exercises the
  `assemble_diagonal → reciprocal` chain (`palace/linalg/chebyshev.cpp:177-178,240-241`).

## Variant axes

The theme exposes three variant axes at the L1>L0 edge:

- **Sub-pattern selection**: `A: reciprocal` | `B: elementwise-product`.
  Not a variant within a single operator but the composite-theme
  decomposition — the two L1 leaves are co-housed in this thin-theme.
  Distinguished by L1 operator name (and L0 entry surface:
  receiver-self-overwrite for A vs. output-arg-write for B).
- **element-type**: `real` | `complex`. Both sub-patterns carry this axis.
  - A: real path is upstream MFEM
    (`mfem::Vector::Reciprocal()` via `using Vector` alias `vector.hpp:20`);
    complex path is Palace-defined `ComplexVector::Reciprocal()`
    (`vector.cpp:248-261`).
  - B: real path is `BaseDiagonalOperator<Operator>::Mult`
    (`palace/linalg/operator.cpp:478-487`) + consumer-duplicate `Apply` over `Vector`
    (`jacobi.cpp:30-39`); complex path is
    `BaseDiagonalOperator<ComplexOperator>::Mult`
    (`palace/linalg/operator.cpp:489-507`) + consumer-duplicate `Apply` over
    `ComplexVector` (`jacobi.cpp:41-69`).
- **conjugation** (sub-axis on sub-pattern B, complex element-type only):
  `straight (a ⊙ b)` | `conjugate-first-operand (ā ⊙ b)`. Realised by the
  kernel-template choice `Mult` vs. `MultHermitianTranspose`
  (`palace/linalg/operator.cpp:489-507` vs. `:545-568`); the consumer-duplicate `Apply`
  carries both forms as `Transpose=false` / `Transpose=true` branches
  (`jacobi.cpp:52-60` / `:61-69`). The conjugate consumer-duplicate branch
  is **dead code** under Palace's symmetric wiring
  (`MultTranspose → Mult` self-alias at `jacobi.hpp:43`); the canonical
  `MultHermitianTranspose` is live (called whenever a diagonal operator's
  Hermitian-transpose action is needed).

No other variant axes — both sub-patterns are unconditionally per-element,
reduction-free, single-`forall_switch`-pass, with no fast paths,
constant-folding branches, or masking.

Non-axes (recorded for disambiguation):

- **zero-guard policy on sub-pattern A**: there is **no** zero-guarded vs.
  unguarded variant of `reciprocal` — the L0 source unconditionally divides
  by `|z|²`; the partiality `reciprocal(0) = undefined` is recorded as a
  precondition on the input, not a variant axis.
- **operator-action vs. free-binary on sub-pattern B**: not an axis at L1
  — the L0 canonical site wraps one operand as a `BaseDiagonalOperator`
  member, the consumer-duplicate site takes both operands as explicit args.
  At L1 both lower from the free-binary `elementwise_product(a, b)`; the
  operator-action form is recovered via L1 `elementwise_product` law 9.
- **in-place vs. out-of-place**: both sub-patterns are unconditionally
  in-place at L0 (A via receiver self-overwrite, B via output-arg write).
  The L1 forms are unconditionally out-of-place. The in-place/out-of-place
  choice is the very rewrite this theme captures, not an L1 axis.

## Status

`firm` — the rewrite is the structural expansion of two L1 pure-functional
leaves into their L0 in-place mutation surfaces, exhaustively pinned by
direct, self-verified evidence (the complex `Reciprocal` body
`vector.cpp:248-261`; the real and complex canonical
`BaseDiagonalOperator::Mult` bodies `palace/linalg/operator.cpp:478-487` and
`:489-507`; the canonical conjugate-variant body
`MultHermitianTranspose` at `:545-568`; the consumer-duplicate `Apply`
bodies `jacobi.cpp:30-39` real and `:41-69` complex including the
dead-code transpose branch; the consumer-call sites
`jacobi.cpp:79-80,103,178,241` and `bilinearform.cpp:278`). The
canonical-vs-consumer-duplicate kernel equivalence (B.1 ↔ B.3 forward
branch) is byte-level identity modulo variable rename. Both sub-patterns
read straight off positively-cited source with no literature inference and
no negative-anchor reconstruction, so `firm` rather than
`partly-constructive`.

The two L1 anchors are themselves firm (landed cycle-033) — the L1 algebraic
laws this theme references (reciprocal law 5 for sub-pattern A's complex
closed-form; elementwise_product laws 1/2/3/4/5/9 + the conjugation sub-axis
for sub-pattern B) are all anchored in those entries with positive source
citations.

Per the firm-on-positive-structure precedent
([`apply_linop`](../L1/apply_linop.md) /
[`apply_nonlinear_pencil`](../L1/apply_nonlinear_pencil.md) /
[`jacobi-smoother`](../L1/jacobi-smoother.md) /
[`chebyshev-smoother`](../L1/chebyshev-smoother.md)), the absence of a
dedicated test for either operator under `reference/palace/test/unit/`
(no `test-reciprocal.cpp`, no `test-elementwise-product.cpp`, no
`test-diagonal-operator.cpp`) does not gate `firm`: every sub-pattern is a
syntactic identity on fully-specified positive source. Behaviour is
exercised indirectly through the diagonal-preconditioner consumer chain
(Jacobi/Chebyshev smoothers in the multigrid integration coverage) and via
the FE-assembly multiplicity-averaging consumer
(`bilinearform.cpp:278`).

**Caveats (not status reductions):**

- **Dead-code complex transpose consumer branch.** The
  `Apply<Transpose=true>` kernel at `palace/linalg/jacobi.cpp:61-69` is
  unreachable under Palace's symmetric `MultTranspose → Mult` wiring
  (`jacobi.hpp:43` one-liner self-alias). The L0 body is byte-identical to
  the canonical `MultHermitianTranspose` at `palace/linalg/operator.cpp:564-565` modulo
  variable rename, so the conjugate variant axis IS live at the canonical
  site even though one consumer's copy of it is not. Recorded as a
  recognition rule for potential non-symmetric sites; same status as the
  chebyshev sibling's dead-code transpose kernels
  (`palace/linalg/chebyshev.cpp:101-110, :150-159`) and the dead-code
  caveat in [`jacobi-smoother-mutation-rotation`](./jacobi-smoother-mutation-rotation.md)
  sub-pattern B. The cycle-034 D2 `lowering-verifier`-on-jacobi-smoother
  audit (running in parallel with this dispatch) is auditing the
  dead-code kernels system-wide; any harden-or-prune outcome from that
  audit will refine this caveat in a follow-up cycle.
- **Real-path upstream-MFEM body (sub-pattern A).** `Vector::Reciprocal()`
  resolves to upstream `mfem::Vector::Reciprocal()`; per CLAUDE.md
  "Many symbols resolve into upstream libraries... Specialized agents cite
  Palace source, not vendored upstream." the real-path body behaviour is
  taken as given (elementwise `1/x[i]` in ℝ). Any deeper upstream-MFEM
  behavioural question (NaN policy specifics, device-kernel
  implementation) is logged as an open question, not reconstructed.
- **No constant-folding branches in either sub-pattern.** Special algebraic
  cases (`a = 𝟙`, `a = 𝟘`, `x = 𝟙`, etc.) are absorbed into L1 algebraic
  laws, not realised as runtime branches in the L0 source. The kernels are
  uniform `forall_switch` per-element passes.
- **No MPI collective at any layer.** Both sub-patterns are rank-local
  element-loops; the L1 forms are agnostic to data placement. MPI
  distribution is out of scope per CLAUDE.md §Scope.
- A `lowering-verifier` exhaustiveness audit (both sub-patterns × both
  element-types × the conjugation sub-axis × all four consumer sites for
  sub-pattern A and the consumer cohort for sub-pattern B) is the standard
  follow-up, not a status reduction.

## Open questions / caveats

- **Composite-vs-split decision recorded.** The theme is authored as a
  single composite thin-theme covering both L1 leaves (sub-pattern A +
  sub-pattern B) per the planner's recommendation. The decision rests on
  three factors: (1) the two leaves share the in-place-mutation rewrite
  class (destination-binding of an L1 pure-functional return); (2) they
  co-occur line-for-line in `JacobiSmoother::SetOperator` (`jacobi.cpp:79-80`)
  and `JacobiSmoother::Mult` (`jacobi.cpp:103`), so a single theme cohabits
  with the diagonal-preconditioner setup-chain narrative; (3) splitting
  into two themes would duplicate the BLAS-1-leaf shape boilerplate
  (applicability, single-rank scope, firm-on-positive-structure status
  argument) verbatim. The shared mutation-rewrite class is the
  load-bearing factor, the same shape choice
  [`ksp-solve-mutation-rotation`](./ksp-solve-mutation-rotation.md) made
  for the L2>L1 thin-theme co-authoring precedent. No friction surfaced
  during authoring — sub-patterns are independently citable and the
  composite reads cleanly. A future split into two themes would not change
  any L0 anchor or any L1 algebraic-law citation; it would only re-split
  the theme prose.
- **Dead-code complex transpose branch (`jacobi.cpp:61-69`).** Recorded as
  a recognition rule in sub-pattern B and as a status caveat above; flagged
  for the cycle-034 D2 `lowering-verifier`-on-jacobi-smoother audit. The
  canonical `MultHermitianTranspose` at `palace/linalg/operator.cpp:545-568` is live; only
  the consumer-duplicate copy is dead. (Filing OQ
  `reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch`.)
- **`safe_reciprocal(x, ε)` L1 candidacy.** A speculative zero-guarded
  reciprocal operator (returning `0` or `1/ε` for `|x[i]| < ε`) is named in
  [`L1/reciprocal`](../L1/reciprocal.md) §Variant axes as a future
  candidate. Palace has no zero-guarded kernel, so no L0 anchor exists.
  Filing OQ `safe-reciprocal-threshold-l1-candidacy` to track.
- **Upstream `mfem::Vector::Reciprocal()` body.** The real-path body lives
  in upstream MFEM, not in Palace. The behaviour is documented (elementwise
  `1/x[i]`); any deeper question (NaN-on-zero specifics, device-kernel
  realisation) is logged for upstream investigation. Filing OQ
  `mfem-vector-reciprocal-upstream-body-investigation`.
- **L2 unification: `diagonal_preconditioner_apply` combinator.** The
  composition `elementwise_product(reciprocal(assemble_diagonal(A)), x)` is
  the L1 expression of the diagonal-preconditioner action. An L2
  `diagonal_preconditioner_apply` combinator could absorb the three-step
  chain into a single fold, parameterised by the operator `A`. Both the
  `jacobi_smoother` apply and the per-step `chebyshev_smoother` inner step
  realise this L1 composition (line-for-line in `JacobiSmoother::Mult` at
  `jacobi.cpp:103` via the local `Apply` helper; ditto inside
  `chebyshev.cpp`'s polynomial sweep). The unification is a candidate but
  not pursued in this theme; recorded for future
  `same-layer-cross-cutter` or `combinator-miner` attention.
- **`assemble_diagonal → reciprocal → elementwise_product` setup-chain
  identity.** All three preconditioner sub-cases (Jacobi, Chebyshev 4th-kind,
  Chebyshev 1st-kind) carry the **identical** `op.AssembleDiagonal(dinv); dinv.Reciprocal();`
  prefix (`jacobi.cpp:79-80`; `chebyshev.cpp:177-178,240-241`). The L2>L1
  unification of this prefix is the same fan-out target as the previous
  bullet's combinator candidate. (No new OQ — covered by the existing
  `polynomial_smoother` combinator candidate in
  [`jacobi-smoother-mutation-rotation`](./jacobi-smoother-mutation-rotation.md)
  §Open questions.)
- **MPI / `MPI_Comm` placeholder.** Both sub-patterns are rank-local; the
  `MPI_Comm` argument never appears in either operator's L0 surface. Under
  MPI the disjoint-slice-per-rank decomposition is the standard parallel
  shape (every element write is rank-local; no boundary exchange). Per
  CLAUDE.md §Scope, MPI distribution is out of scope; flagged once here.
```

```edit:book/src/L1-L0/index.md
[after the `jacobi-smoother-mutation-rotation` row at line 42, before the `minres-iteration` row, append a new row:

| [reciprocal-elementwise-product-mutation-rotation](./reciprocal-elementwise-product-mutation-rotation.md) | `L1/reciprocal` (firm c033) + `L1/elementwise_product` (firm c033) | `palace/linalg/vector.{hpp,cpp}`, `palace/linalg/operator.cpp`, `palace/linalg/jacobi.cpp`, `palace/fem/bilinearform.cpp` | firm *(structural + complex-reciprocal closed-form algebraic sub-rule; 2 composite sub-patterns A reciprocal receiver-self-overwrite / B elementwise-product output-arg via canonical `BaseDiagonalOperator::Mult` + consumer-duplicate `Apply(dinv, x, y)`; element-type axis (real upstream-MFEM-aliased + complex Palace-defined) + complex conjugation sub-axis on B (canonical `MultHermitianTranspose` live, consumer-duplicate `Apply<Transpose=true>` dead-code under `MultTranspose→Mult` symmetric wiring); closes c033 OQs `reciprocal-l1-l0-mutation-rotation-theme` + `elementwise-product-l1-l0-mutation-rotation-theme`; thin-theme composite per `ksp-solve-mutation-rotation` precedent — shared in-place-mutation rewrite class + co-occurrence in `JacobiSmoother::SetOperator`)* |
]
```

```edit:book/src/SUMMARY.md
[under the `# L1 > L0 — Lowering` Part (existing ordering is integration-cycle-chronological, NOT alphabetical), insert a new chapter row immediately after the `jacobi-smoother-mutation-rotation` row at line 105 and before the `divfree-projector-mutation-rotation` row at line 106 — this mirrors the `index.md` insertion position (which itself sits after the `jacobi-smoother-mutation-rotation` index row at line 42) and keeps the SUMMARY.md and index.md insertion points co-located alongside the closest semantic sibling (the jacobi-smoother lowering, which this theme co-occurs with via `JacobiSmoother::SetOperator`):

- [reciprocal-elementwise-product-mutation-rotation](./L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
]
```

```edit:scaffolding/open-questions.md
[append three new OQ entries at the active block tail (under cycle-034 D1):

- `reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch` — OPEN — the consumer-duplicate `Apply<Transpose=true>` kernel at `palace/linalg/jacobi.cpp:61-69` is unreachable under Palace's symmetric `MultTranspose → Mult` self-alias wiring (`palace/linalg/jacobi.hpp:43`); the canonical `MultHermitianTranspose` at `palace/linalg/operator.cpp:545-568` is live. Recorded as a recognition rule in `reciprocal-elementwise-product-mutation-rotation` sub-pattern B and as a status caveat. Same defined-not-used status as the chebyshev sibling's dead-code transpose kernels (`chebyshev.cpp:101-110, :150-159`); flagged for the cycle-034 D2 `lowering-verifier`-on-jacobi-smoother audit (running in parallel with this dispatch) — any harden-or-prune outcome from that audit will refine this OQ. *Trigger:* the D2 audit's exhaustiveness verdict.

- `safe-reciprocal-threshold-l1-candidacy` — OPEN — speculative `safe_reciprocal(x, ε)` L1 operator (threshold zero-guard: returns `0` or `1/ε` for `|x[i]| < ε`) is named in [`L1/reciprocal`](../book/src/L1/reciprocal.md) §Variant axes (non-axes) as a future candidate. Palace has no zero-guarded reciprocal kernel — the complex `ComplexVector::Reciprocal()` at `palace/linalg/vector.cpp:248-261` unconditionally divides by `|z|²`. No L0 anchor exists; promotion would require either an upstream Palace zero-guarded kernel addition OR a literature-anchored algorithmic motivation that doesn't depend on Palace surface. Backlog candidate. *Trigger:* a consumer-side need (e.g., a preconditioner setup that can't enforce `diag(A) > 0`) or an upstream Palace addition.

- `mfem-vector-reciprocal-upstream-body-investigation` — OPEN — the real-path sub-pattern A of `reciprocal-elementwise-product-mutation-rotation` lowers to upstream `mfem::Vector::Reciprocal()` via the `using Vector = mfem::Vector` alias at `palace/linalg/vector.hpp:20`. Per CLAUDE.md "Many symbols resolve into upstream libraries... Specialized agents cite Palace source, not vendored upstream." the body is treated as given (elementwise `1/x[i]` in ℝ). Deeper questions — NaN-on-zero policy specifics, device-kernel implementation, whether the upstream method clamps or guards — are logged here for upstream investigation rather than reconstructed inside the theme. Low priority. *Trigger:* a consumer site that depends on a specific upstream behaviour the doc-comment doesn't pin down.

Resolution of motivating OQs:

- `reciprocal-l1-l0-mutation-rotation-theme` — RESOLVED cycle-034 — closed by the composite theme `reciprocal-elementwise-product-mutation-rotation` sub-pattern A.
- `elementwise-product-l1-l0-mutation-rotation-theme` — RESOLVED cycle-034 — closed by the composite theme `reciprocal-elementwise-product-mutation-rotation` sub-pattern B.
]
```

## Speculative operators proposed

**None.** Both L1 anchors ([`L1/reciprocal`](../L1/reciprocal.md) and
[`L1/elementwise_product`](../L1/elementwise_product.md)) are already firm
(landed cycle-033). This theme lowers existing firm L1 vocabulary; no new
L1 operators are proposed. A speculative `safe_reciprocal(x, ε)` is named in
[`L1/reciprocal`](../L1/reciprocal.md) §Variant axes as a future candidate
but is **not** part of this theme — Palace has no zero-guarded kernel, so
no L0 anchor exists. The open question `safe-reciprocal-threshold-l1-candidacy`
tracks the future candidacy without committing this theme to it.

## Supporting evidence

### L0 source ranges (cited in the theme; self-verified this dispatch)

- `palace/linalg/vector.hpp:20` — `using Vector = mfem::Vector;` (real-path
  alias).
- `palace/linalg/vector.hpp:107-108` — `ComplexVector::Reciprocal()`
  declaration + doc-comment.
- `palace/linalg/vector.cpp:248-261` — `ComplexVector::Reciprocal()` body
  (the full `s = 1/|z|²; XR *= s; XI *= -s` realisation of the closed-form
  `1/z = z̄/|z|²` at `:257-259`).
- `palace/linalg/operator.cpp:478-487` — real canonical
  `BaseDiagonalOperator<Operator>::Mult` (`Y[i] = D[i] * X[i]` at `:486`).
- `palace/linalg/operator.cpp:489-507` — complex canonical
  `BaseDiagonalOperator<ComplexOperator>::Mult` (six-FMA complex multiply at
  `:504-505`).
- `palace/linalg/operator.cpp:545-568` — complex canonical
  `MultHermitianTranspose` (three sign flips at `:564-565`).
- `palace/linalg/jacobi.cpp:16` — `// Assumes A SPD (diag(A) > 0)` —
  consumer-side precondition discharging the sub-pattern A `x[i] ≠ 0`
  partiality.
- `palace/linalg/jacobi.cpp:30-39` — real consumer-duplicate `Apply`
  (`Y[i] = DI[i] * X[i]` at `:38`).
- `palace/linalg/jacobi.cpp:41-69` — complex consumer-duplicate `Apply`
  with dead-code transpose branch `:61-69`.
- `palace/linalg/jacobi.cpp:74-97` — `JacobiSmoother::SetOperator` setup
  chain (`AssembleDiagonal(dinv)` at `:79`, `dinv.Reciprocal()` at `:80`).
- `palace/linalg/jacobi.cpp:99-104` — `JacobiSmoother::Mult` entry
  (`Apply(dinv, x, y)` dispatch at `:103`).
- `palace/linalg/jacobi.hpp:43` — `MultTranspose → Mult` symmetric
  self-alias (strands the consumer transpose branch as dead code).
- `palace/linalg/chebyshev.cpp:178` — second consumer of
  `dinv.Reciprocal()` (4th-kind Chebyshev).
- `palace/linalg/chebyshev.cpp:241` — third consumer (1st-kind Chebyshev).
- `palace/fem/bilinearform.cpp:278` — fourth consumer
  (multiplicity-averaging, non-preconditioner).

### Producer self-verification

- `tools/citecheck/citecheck.py --anchor 'ComplexVector::Reciprocal' palace/linalg/vector.cpp:248-261` → ok, anchor at line 248.
- `tools/citecheck/citecheck.py --anchor 'Apply(const Vector' palace/linalg/jacobi.cpp:30-39` → ok, anchor at line 31.
- `tools/citecheck/citecheck.py --anchor 'Apply(const ComplexVector' palace/linalg/jacobi.cpp:41-69` → ok, anchor at line 42.
- `tools/citecheck/citecheck.py --anchor 'Apply(dinv, x, y)' palace/linalg/jacobi.cpp:99-104` → ok, anchor at line 103.
- `tools/citecheck/citecheck.py --anchor 'BaseDiagonalOperator<Operator>::Mult' palace/linalg/operator.cpp:478-487` → ok, anchor at line 479.
- `tools/citecheck/citecheck.py --anchor 'BaseDiagonalOperator<ComplexOperator>::Mult' palace/linalg/operator.cpp:489-507` → ok, anchor at line 490.
- `tools/citecheck/citecheck.py --anchor 'MultHermitianTranspose' palace/linalg/operator.cpp:545-568` → ok, anchor at line 548.
- `tools/citecheck/citecheck.py --anchor 'JacobiSmoother<OperType>::SetOperator' palace/linalg/jacobi.cpp:74-97` → ok, anchor at line 75.
- `tools/citecheck/citecheck.py --anchor 'Reciprocal' palace/linalg/vector.hpp:107-108` → ok, anchor at line 108.

All load-bearing pinpoint citations passed `citecheck`'s `--anchor` self-verification this dispatch.

### Cross-theme cohabitation evidence

- `book/src/L1-L0/jacobi-smoother-mutation-rotation.md` sub-pattern A
  (`palace/linalg/jacobi.cpp:74-97`) is the cycle-033 parent theme that
  forward-references both leaves; the `op.AssembleDiagonal(dinv)` +
  `dinv.Reciprocal()` setup at `:79-80` and the `Apply(dinv, x, y)` apply
  dispatch at `:103` are the exact L0 ground this thin-theme's
  sub-patterns A and B lower to.
- `book/src/L1-L0/assemble-diagonal-mutation-rotation.md` is the
  diagonal-extraction L1>L0 theme (the first link in the
  `assemble_diagonal → reciprocal → elementwise_product`
  diagonal-preconditioner setup chain). The current theme is the second
  and third links.
- `book/src/L1-L0/chebyshev-smoother-mutation-rotation.md` is the sibling
  constructed-operator theme that exercises the same setup chain at
  `palace/linalg/chebyshev.cpp:177-178,240-241`.

## Open questions / caveats

(Three new OQs filed via the proposed-changes block above:
`reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch`,
`safe-reciprocal-threshold-l1-candidacy`,
`mfem-vector-reciprocal-upstream-body-investigation`. Two existing OQs
resolved: `reciprocal-l1-l0-mutation-rotation-theme` and
`elementwise-product-l1-l0-mutation-rotation-theme`.)

- **Composite-vs-split decision.** Authored as composite per planner
  recommendation. No authoring friction surfaced — sub-patterns are
  independently citable and the composite reads cleanly. The shared
  in-place-mutation rewrite class and the co-occurrence in
  `JacobiSmoother::SetOperator` (`jacobi.cpp:79-80`) are the load-bearing
  factors; splitting would duplicate the BLAS-1-leaf boilerplate verbatim
  for negligible structural gain.

- **Dead-code consumer transpose branch.** The consumer-duplicate
  `Apply<Transpose=true>` at `jacobi.cpp:61-69` is unreachable; the
  canonical `MultHermitianTranspose` at `palace/linalg/operator.cpp:545-568` IS live.
  Recorded as a recognition rule in sub-pattern B and flagged for the
  cycle-034 D2 `lowering-verifier`-on-jacobi-smoother audit. The new OQ
  `reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch`
  tracks the harden-or-prune outcome.

- **L2 unification candidate: `diagonal_preconditioner_apply` combinator.**
  The composition
  `elementwise_product(reciprocal(assemble_diagonal(A)), x)` is realised
  line-for-line in `JacobiSmoother::SetOperator` + `Mult` (`jacobi.cpp:79-80,103`)
  and via the polynomial sweep in `ChebyshevSmoother`. The L2 unification
  is a candidate but out of scope here — recorded as a future
  `same-layer-cross-cutter` / `combinator-miner` target. Subsumed by the
  existing `polynomial_smoother` combinator candidate in
  `jacobi-smoother-mutation-rotation` §Open questions.

- **Upstream MFEM real-path body opacity.** The real `Vector::Reciprocal()`
  resolves to upstream MFEM and is treated as given per CLAUDE.md.
  Deeper-behaviour questions are filed as
  `mfem-vector-reciprocal-upstream-body-investigation`; not a status
  reduction.
