---
# Lowering theme (L1>L0). Theme rank = min(endpoint ranks); the L1 endpoint (`L1/scal`) is firm,
# the L0 endpoint is rank-terminal, so the theme is firm. This theme carries `cites-evidence`
# edges to the L0 complex `ComplexVector::operator*=` overload it lowers to; the real path is
# `mfem::Vector::operator*=(double)` — upstream MFEM, named in prose, not a Palace L0 edge.
rank: firm
edges:
  depends-on:
    - target: palace/linalg/vector.cpp:203-227
      kind: cites-evidence        # ComplexVector::operator*= definition; si==0.0 two-real-call branch (:207-211) + general complex forall_switch kernel (:212-225)
    - target: palace/linalg/vector.hpp:98-99
      kind: cites-evidence        # ComplexVector &operator*=(std::complex<double> s); decl + `// Scale all entries by s.` comment
---

# scal-mutation-rotation

The mutation rotation for the BLAS-1 vector-scalar rescale. Lowers the pure L1
form `scal(α, x) = α·x` (firm; see [`L1/scal`](../L1/scal.md)) into Palace's
in-place L0 receiver-mutating member call `x *= α` on the destination vector.
The simplest of the in-place mutation-rotation theme family — a sibling of
[`axpby-mutation-rotation`](./axpby-mutation-rotation.md),
[`axpbypcz-mutation-rotation`](./axpbypcz-mutation-rotation.md), and
[`nrm2-mutation-rotation`](./nrm2-mutation-rotation.md).

## Slug

`scal-mutation-rotation`

## L1 form (LHS)

The pure-functional rescale (firm; see [`L1/scal`](../L1/scal.md)) consumes the
scalar `α` and the *prior* value of `x` and produces a fresh post-update value.
There is one LHS shape — `scal` has no free-function form and no constant-folding
specialisations:

    x_new = scal(α, x_old)        -- x_new = α·x_old

`α` and `x` share element type (both real or both complex); a real `α` against a
complex `x` is promoted per [`concepts/scalar-promotion`](../concepts/scalar-promotion.md).
The L1 form carries no destination buffer — the prior `x` and the new `x` are
distinct values. The lowering below is where the in-place overwrite is
reintroduced.

## L0 form (RHS)

A single rewrite — re-bind the L1 output value into the in-place receiver buffer
— reaching one of two element-type-distinguished member overloads. There is no
free-function `linalg::Scal` / `linalg::Scale` symbol (the corpus grep returns
zero hits; the absence is named in
[`L0/linalg-free-functions`](../L0/linalg-free-functions.md)), and there are no
scalar-value constant-folding branches (unlike `axpy`'s `α == 1.0` fast path),
so the three-sub-pattern shape of `axpby-mutation-rotation` collapses here to a
single structural pattern with one shape-specialisation sub-note on the complex
path.

### Sub-pattern A — bare in-place rescale (real path)

    x *= alpha;                            // mfem::Vector::operator*=(double) — MFEM

The textbook in-place real scale. The receiver is the destination buffer; the
scalar is a runtime `double`. Reached directly at GMRES Arnoldi
basis-normalisation `w *= 1.0 / Hj[j + 1];` and inside `linalg::Normalize`
(`x *= 1.0 / norm;`).

Justification kind: **structural** — the rewrite re-binds the L1 result `α·x`
into the L0 receiver buffer `x`; there is no algebraic restatement.

Citations:
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template:
  `auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, ...); x *= 1.0 / norm; return norm;`
  (the `x *= 1.0/norm;` rescale is on line 268). The only Palace-side `scal`
  use that returns the discarded scalar (the norm).
- `palace/linalg/iterative.cpp:632` — GMRES Arnoldi basis-normalisation
  `w *= 1.0 / Hj[j + 1];` (real `scal`; `w *= 1.0/nrm2`).
- `palace/linalg/iterative.cpp:811` — second analogous GMRES code path,
  identical `w *= 1.0 / Hj[j + 1];`.

### Sub-pattern B — in-place rescale (complex path)

    x *= s;                                // ComplexVector::operator*=(std::complex<double>) — Palace

The complex-receiver scale. The definition at `vector.cpp:203-227` branches on
`s.imag() == 0.0`:

- **`si == 0.0`** (real scalar against a complex vector — the scalar-promotion
  case): two real `operator*=` calls, `Real() *= sr; Imag() *= sr;`
  (`vector.cpp:207-211`). Algebraically `(sr + 0i)·x = sr·x` exactly, so the
  cross-term elision is equivalent — a **transparent** shape-specialisation.
- **`si != 0.0`** (general complex scalar): the `forall_switch` kernel
  (`vector.cpp:212-225`) computing `XR[i] = sr·XR[i] − si·XI[i]`,
  `XI[i] = si·XR[i] + sr·XI[i]` — the standard complex-multiply applied
  element-wise.

Justification kind: **structural** for the buffer re-bind, with one
**algebraic** sub-note: the `s.imag() == 0.0` branch is justified by
`(sr + 0i)·x = sr·x` and is a transparent constant-shape trick (a complex-scalar
*shape* specialisation on `imag(s)`, **not** a scalar-*value* specialisation on
`α`). It disappears at L1 — both branches realise the same `scal(α, x)` form.

Citations:
- `palace/linalg/vector.hpp:98-99` — declaration
  `ComplexVector &operator*=(std::complex<double> s);` with the preceding comment
  `// Scale all entries by s.`
- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=` definition;
  lines 207-211 the `si == 0.0` two-real-call branch; lines 212-225 the general
  complex `forall_switch` kernel.

## Applicability conditions

For both sub-patterns the rewrite preserves semantics when:

1. **No observer of the prior `x` value after the call.** The L0 `x *= α`
   overwrites `x` in place, destroying the prior value. If a downstream operation
   reads `x_old` after the rescale site, the rewrite is invalid — at L1 `x_old`
   would still be in scope. In Palace this is upheld by lexical sequencing: every
   site reads the prior `x` (e.g. to compute `1/nrm2(x)`) strictly before the
   `*=` call. **Self-aliasing of `x` is not a hazard for `scal`** (unlike
   `axpy`): the operation is element-local — `x[i]` depends only on `x[i]` —
   so there is no separate read buffer to alias against. This is the structural
   reason the `scal` lowering is simpler than `axpby`'s (which carries an
   explicit no-`x`/`y`-aliasing condition).
2. **Conforming element type with promotion.** `α` and `x` share element type;
   a real `α` against a complex `x` is promoted via the internal
   `s.imag() == 0.0` branch at `vector.cpp:207-211` (see
   [`concepts/scalar-promotion`](../concepts/scalar-promotion.md), which
   formalizes the real⊑complex typing rule). A complex `α`
   against a real `x` has no L0 overload and does not occur in the corpus.
3. **`α` is a runtime scalar.** There is no sub-pattern selection on the value
   of `α` — `scal` has no `α == 0` / `α == 1` / `α == -1` constant-folding
   branches at L0 (the special algebraic cases are L1 laws, not L0 fast paths).
   The only L0 branch is the complex-path `imag(s) == 0.0` shape branch inside
   sub-pattern B, which is a transparent trick within that one overload, not a
   distinct sub-pattern.

## Justification kind

- **Sub-pattern A** (real) — `structural`. Re-bind the L1 output value into the
  L0 receiver buffer.
- **Sub-pattern B** (complex) — `structural` buffer re-bind plus one
  `algebraic` sub-note: `(sr + 0i)·x = sr·x` grounds the transparent
  `imag(s) == 0.0` shape branch.

The theme as a whole is `structural`. There are no scalar-value algebraic
sub-rules (contrast `axpby-mutation-rotation`'s B/C `α == 1` / `α == -1`
specialisations) because `scal`'s L0 surface has no scalar-value constant
folding. A future `lowering-verifier` audit should confirm the two-overload
recognition matches the L0 corpus exhaustively (the cited call sites are
illustrative, not exhaustive — see Coverage note below).

## Speculative L1 operators

None. `scal` is a firm L1 leaf primitive (see [`L1/scal`](../L1/scal.md)); this
theme introduces no new rough-in operators. The fused `linalg::Normalize`
construct (`x *= 1.0/norm; return norm;`) factors at L1 as the composition
`scal(1/nrm2(x), x)` paired with the returned norm; whether to harvest a fused
`normalize` L1 primitive is an existing open question (registered OQ
`normalize-as-fused-l1-primitive`, a constituent of the
`normalize-l1-primitive-harvest` plan item; also discussed in prose at
[`L1/scal`](../L1/scal.md) §Dependencies), not a speculative operator of this
theme.

## Evidence

L0 evidence ranges:

- `palace/linalg/vector.hpp:98-99` — `ComplexVector::operator*=(std::complex<double>)`
  declaration + `// Scale all entries by s.` comment.
- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=` definition;
  `si == 0.0` two-real-call branch at 207-211, general complex kernel at 212-225.
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template;
  `x *= 1.0 / norm;` rescale at line 268.
- `palace/linalg/iterative.cpp:632` — GMRES Arnoldi `w *= 1.0 / Hj[j + 1];`.
- `palace/linalg/iterative.cpp:811` — second GMRES path, identical `w *= ...`.
- `palace/linalg/iterative.cpp:222` — `cs *= w;` — a *scalar-scalar* `*=`
  (plane-rotation cosine), **not** a vector `scal`. Cited as a *non-instance*
  for disambiguation (syntactic `*=` match that the recognition rule must reject).
- `palace/linalg/operator.cpp:661` — `Normalize(comm, u);` call site
  (fixed-point power-iteration spectral-radius estimate).
- `palace/linalg/operator.cpp:673` — `l = Normalize(comm, u);` call site
  (same loop, returns the eigenvalue estimate).
- `palace/linalg/nleps.cpp:486-493` — eigenvector / c-vector normalisation:
  `c *= 1.0 / norm_c;` (488), `c2 *= 1.0 / norm_c;` (489), `v *= 1.0 / norm_v;`
  (493) — in-place `scal` sites on complex vectors with real promoted scalars.

L1 anchor:

- `book/src/L1/scal.md` — the firm L1 operator that both sub-patterns lower from
  (signature `scal :: (α: Scalar, x: Tensor[N]) -> Tensor[N]`, nine algebraic
  laws).

Test evidence (L0-equivalent semantic documentation):

- `palace/test/unit/test-orthog.cpp:193` — `V[0] *= 1 / v0_norm;` on a real
  `Vector`, immediately after a `CHECK_THAT(v0_norm, ...)` assertion on the norm.
  Direct **empirical-match** for sub-pattern A: the textbook `scal(1/nrm2, x)`
  normalize step on the real path, with the norm asserted before the rescale.
- `palace/test/unit/test-orthog.cpp:208` — `V[1] *= 1 / v1_norm;`, second
  analogous real-path normalize-by-hand instance.
- `palace/test/unit/test-lumpedportintegration.cpp:394` — `RHS *= 0.5;` on a
  `ComplexVector` with a real literal scalar. Direct **empirical-match** for
  sub-pattern B's `s.imag() == 0.0` promotion branch (real `0.5` promoted against
  a complex receiver). A second instance is at
  `test-lumpedportintegration.cpp:746`.

Coverage note: the cited call sites are illustrative, not exhaustive. The
two-overload recognition (real `mfem::Vector::operator*=(double)` vs complex
`ComplexVector::operator*=(std::complex<double>)`) plus the fused `Normalize`
template covers the observed corpus; additional `x *= α` sites exist under
`palace/models/` and `palace/fem/` (e.g. the `RHS *= 0.5` excitation-vector
rescale mirrored in `palace/models/spaceoperator.cpp`).
