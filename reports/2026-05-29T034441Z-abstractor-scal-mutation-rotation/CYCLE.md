---
agent: abstractor
invoked_at: 2026-05-29T034441Z
scope: L1>L0 theme — scal-mutation-rotation (stub→firm)
status: integrated
integrated_at: 2026-05-29T06:05:00Z
integration_commit: 14cc0bd
integration_notes: "cycle-020 finalize (staging row #3). scal-mutation-rotation PROMOTED stub→firm (in-place scalar multiply x ← α·x; element-type + scalar-promotion variant axes; nleps.cpp:486-493 normalize site). Full-file replacement of the stub; L1-L0/index dep-map row inserted after nrm2 / before dot; SUMMARY :84 in-place de-stub. Post-repair citation drift nleps.cpp (491)→(493) + range 486-491→486-493 already fixed before apply; sibling-maturity correction landed (nrm2 firm, axpby/axpbypcz rough-in). BLAS-1 L1>L0 floor NOT yet closed (axpby/axpbypcz still rough-in) — blas1-l1-l0-lowering-theme-gap closing but not closed; meta-phase reconciles the scal constituent strike against the remainder. L1>L0 themes contribute to 12→15. retroactive-budget 0; clean build."
inputs:
  - book/src/L1/scal.md (firm L1 anchor)
  - book/src/L1-L0/scal-mutation-rotation.md (stub home, materialized 2026-05-28)
  - book/src/L1-L0/axpby-mutation-rotation.md (structural model)
  - reference/palace/linalg/vector.{hpp,cpp} (L0 sites, self-verified)
  - reference/palace/linalg/iterative.cpp, operator.cpp, nleps.cpp (call sites, self-verified)
  - reference/palace/test/unit/{test-orthog,test-lumpedportintegration}.cpp (tests, self-verified)
  - OQ scal-mutation-rotation-l1-l0-theme
---

# CYCLE: L1>L0 theme — scal-mutation-rotation (stub→firm)

## Summary

`scal` (`x ← α·x`) is the simplest BLAS-1 in-place mutation — an element-local,
reduction-free rescale of a vector by a scalar. The firm L1 operator
[`L1/scal`](../../book/src/L1/scal.md) is the pure form `scal(α, x) = α·x`; this
theme promotes the existing stub at `book/src/L1-L0/scal-mutation-rotation.md` to
`firm` by narrating forward how that pure form lowers into Palace's L0 in-place
mutation sites. Unlike `axpby`/`axpy`, `scal` has **no free-function form** and
**no scalar-value constant-folding** — the L0 surface is exactly two
receiver-mutating member overloads (`mfem::Vector::operator*=(double)` for real,
`ComplexVector::operator*=(std::complex<double>)` for complex) reached either
directly (`x *= α`) or through the fused `linalg::Normalize` construct
(`x *= 1.0/norm`, factoring at L1 as `scal(1/nrm2(x), x)`). The rewrite is
**structural** (re-bind the L1 result value into the in-place receiver buffer)
with one **algebraic** sub-note: the complex path's `s.imag() == 0.0` fast branch
is a transparent scalar-promotion shape-specialisation, algebraically exact, and
disappears at L1. I self-verified every cited L0 range against source via
`palace-codemap` `read_range` before emitting; tests give direct
empirical-match evidence on both the real (`test-orthog.cpp:193`) and the
real-α-on-complex promotion (`test-lumpedportintegration.cpp:394`) paths.

This is a sibling of the BLAS-1 mutation-rotation theme family —
`nrm2-mutation-rotation` (firm), `axpby-mutation-rotation` (rough-in), and
`axpbypcz-mutation-rotation` (rough-in) — and is the fourth member of the
BLAS-1 floor; promoting it to firm leaves `axpby`/`axpbypcz` still rough-in,
so the floor is not yet complete.

## Proposed changes

```edit:book/src/L1-L0/scal-mutation-rotation.md
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
   formalizes the real⊑complex typing rule — resolving the former
   `scalar-promotion-typing-rule` OQ, closed cycle-005). A complex `α`
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

## Verified-against

L0 evidence ranges (all self-verified via codemap `read_range`,
2026-05-29T034441Z):

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

Test evidence (L0-equivalent semantic documentation; self-verified):

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

verified_against:
  - citation: palace/linalg/vector.hpp:98-99
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: ComplexVector::operator*=(std::complex<double> s) decl on line 99; comment "// Scale all entries by s." on line 98.
  - citation: palace/linalg/vector.cpp:203-227
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: operator*= definition; sr/si extracted; if(si==0.0){Real()*=sr;Imag()*=sr;} at 207-211; forall_switch complex kernel at 212-225 with the XR/XI cross-term. Matches theme exactly.
  - citation: palace/linalg/vector.hpp:262-270
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: Normalize<VecType> template; norm=Norml2; MFEM_ASSERT(norm>0.0); x *= 1.0/norm (line 268); return norm. Fused nrm2+scal construct confirmed.
  - citation: palace/linalg/iterative.cpp:632
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: w *= 1.0 / Hj[j + 1]; preceded by Hj[j+1]=linalg::Norml2(comm,w). GMRES Arnoldi basis-normalize, real scal.
  - citation: palace/linalg/iterative.cpp:811
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: w *= 1.0 / Hj[j + 1]; identical to 632 (second GMRES code path). Confirmed same source lines.
  - citation: palace/linalg/iterative.cpp:222
    verdict: supports (non-instance)
    audited_at: 2026-05-29T034441Z
    note: cs *= w; — cs is a scalar plane-rotation cosine (T d=sqrt(...); cs=dx2/d; ... cs*=w). Scalar-scalar *=, NOT a vector scal. Correctly recorded as a disambiguation non-instance.
  - citation: palace/linalg/operator.cpp:661
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: Normalize(comm, u); after SetRandom(comm,u), before the power-iteration while-loop.
  - citation: palace/linalg/operator.cpp:673
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: l = Normalize(comm, u); inside the while-loop after A.MultHermitianTranspose; returns eigenvalue estimate l.
  - citation: palace/linalg/nleps.cpp:486-493
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: c *= 1.0/norm_c (488), c2 *= 1.0/norm_c (489), v *= 1.0/norm_v (493); each preceded by a sqrt(abs(Dot(...))+squaredNorm()) norm. In-place scal on complex vectors, real promoted scalars.
  - citation: palace/test/unit/test-orthog.cpp:193
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: V[0] *= 1 / v0_norm; on real Vector, after CHECK_THAT(v0_norm, WithinRel(sqrt(mpi_size))...). Empirical-match sub-pattern A.
  - citation: palace/test/unit/test-orthog.cpp:208
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: V[1] *= 1 / v1_norm; second real-path normalize-by-hand, after the v1_norm assertion.
  - citation: palace/test/unit/test-lumpedportintegration.cpp:394
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: RHS *= 0.5; on ComplexVector RHS (RHS.UseDevice(true)). Real literal scalar against complex receiver — empirical-match for the si==0.0 promotion branch (sub-pattern B).

Coverage note: the cited call sites are illustrative, not exhaustive. The
two-overload recognition (real `mfem::Vector::operator*=(double)` vs complex
`ComplexVector::operator*=(std::complex<double>)`) plus the fused `Normalize`
template covers the observed corpus; additional `x *= α` sites exist under
`palace/models/` and `palace/fem/` (e.g. the `RHS *= 0.5` excitation-vector
rescale mirrored in `palace/models/spaceoperator.cpp`). Exhaustive corpus
indexing deferred to a future `lowering-verifier` audit, consistent with the
sibling `axpby-mutation-rotation` coverage note.

## Status

`firm` — the rewrite is a single structural buffer re-bind with one transparent
algebraic shape-sub-note (the complex `imag(s) == 0.0` branch), and every L0
range is direct from `palace/linalg/vector.{hpp,cpp}` + inlined call sites,
self-verified against source and corroborated by two empirical-match test sites
(real path `test-orthog.cpp:193`, complex-promotion path
`test-lumpedportintegration.cpp:394`). No constructive sub-part: nothing here is
reconstructed from negative anchors or literature — the `scal` L0 surface is
small, fully present, and positively cited. (Contrast the `partly-constructive`
`eigsolve-mutation-rotation`, whose `LinearSolveFailed` sub-part is negative-anchor
reconstructed.) The one named absence — no `linalg::Scal`/`linalg::Scale` symbol —
is a *positive* zero-hit corpus result (it confirms the receiver-only surface),
not a reconstruction.
```

```edit:book/src/L1-L0/index.md
| [nrm2-mutation-rotation](./nrm2-mutation-rotation.md) | `L1/nrm2` (firm) | `palace/linalg/vector.hpp`, `palace/utils/communication.hpp`, `palace/fem/errorindicator.hpp` | firm *(structural; 3 surface forms; abs-guard classified load-bearing defensive)* |
| [scal-mutation-rotation](./scal-mutation-rotation.md) | `L1/scal` (firm) | `palace/linalg/vector.{hpp,cpp}`, `palace/linalg/{iterative,operator,nleps}.cpp` | firm *(structural; 2 element-type overloads; transparent complex imag==0 shape branch)* |
```

In-place de-stub of `book/src/SUMMARY.md` line 84 — drop the ` (stub)` label,
do NOT append (a bare append would duplicate the entry or leave the stale
`(stub)` label). Replace the existing line:

```text
- [scal-mutation-rotation (stub)](./L1-L0/scal-mutation-rotation.md)
```

with:

```text
- [scal-mutation-rotation](./L1-L0/scal-mutation-rotation.md)
```

## Speculative operators proposed

None. `scal` is a firm L1 leaf primitive; this theme introduces no rough-in
operators. (The fused `normalize` primitive question is pre-existing and recorded
at `L1/scal` §Dependencies — it is not a speculative operator of this theme.)

## Supporting evidence

All ranges self-verified against `reference/palace/` source via `palace-codemap`
`read_range` at 2026-05-29T034441Z. The `scal` L0 surface is exactly two
receiver-mutating member overloads (no free-function form — `linalg::Scal` /
`linalg::Scale` grep returns zero hits, confirming the named absence at
`L0/linalg-free-functions`), reached either directly (`x *= α`) or via the
`linalg::Normalize` template (`x *= 1.0/norm; return norm;`, factoring at L1 as
`scal(1/nrm2(x), x)`). The complex overload's `s.imag() == 0.0` branch is a
transparent scalar-promotion shape-specialisation. See the Verified-against
block above for the full per-citation audit table.

## Open questions / caveats

- **Scalar promotion (real⊑complex)** — the real-α-on-complex-vector
  promotion is realised here at the value level by the `s.imag() == 0.0` branch
  (`vector.cpp:207-211`), distinct from `axpy`'s overload-based promotion. This
  theme's sub-pattern B documents the in-place site; the typing rule itself is
  already formalized in [`concepts/scalar-promotion`](../concepts/scalar-promotion.md)
  (the former `scalar-promotion-typing-rule` OQ, resolved cycle-005 — no live OQ
  remains). Recorded here for cross-reference only.
- **`normalize-as-fused-l1-primitive`** (existing registered OQ, constituent of
  the `normalize-l1-primitive-harvest` plan item; also discussed in prose at
  `L1/scal` §Dependencies) — `linalg::Normalize` is the dominant `scal` call
  shape in the corpus (GMRES, power-iteration, nonlinear-EVP). This theme factors
  it as
  `scal(1/nrm2(x), x)` + returned norm; whether to harvest a fused `normalize`
  L1 primitive is unchanged by this theme. Flagging for the planner: a fused
  `normalize` would unify the GMRES Arnoldi, `operator.cpp` power-iteration, and
  `nleps.cpp` eigenvector-normalisation sites under one L1 form, which would
  simplify those higher abstractions (the CLAUDE.md "promote to firm only when it
  simplifies higher forms" bar plausibly applies).
- **Coverage exhaustiveness** — consistent with the sibling
  `axpby-mutation-rotation`, the cited call sites are illustrative; a
  `lowering-verifier` audit should confirm the two-overload + `Normalize`
  recognition matches the L0 corpus exhaustively (additional `x *= α` sites under
  `palace/models/`, `palace/fem/`). Not blocking the `firm` status — the
  recognition rules themselves are small, complete, and positively anchored.
- **Lifting note (working-note only; not in theme content per high→low
  discipline)** — the reverse direction (L0 `x *= α` lifting into L1 `scal`)
  requires the no-observer-of-prior-`x` applicability condition to hold; because
  `scal` is element-local there is no aliasing precondition to lift (the simplest
  case in the BLAS-1 family). This note is recorded here in the CYCLE.md working
  notes only; the formal theme chapter stays high→low (L1 form → L0 sites).
- The constituent OQ `scal-mutation-rotation-l1-l0-theme` is **closed** by this
  theme (stub→firm). It is **not** a standalone ledger entry — it is a rolled-up
  constituent inside the migrated plan item `blas1-l1-l0-lowering-theme-gap`
  (`scaffolding/open-questions.md:25`). The integrator should strike this slug
  from that constituent list at line 25 (and check whether the parent
  `blas1-l1-l0-lowering-theme-gap` plan item warrants status movement now that
  `nrm2` and `scal` are firm while `dot` remains a stub), not edit a standalone
  OQ row.
