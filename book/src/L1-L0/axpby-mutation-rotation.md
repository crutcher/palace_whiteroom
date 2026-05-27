# axpby-mutation-rotation

The mutation rotation for BLAS-1 axpy-shaped vector updates. Lowers the pure L1
forms `axpy(α, x, y) = α·x + y` and (speculative) `axpby(α, x, β, y) = α·x + β·y`
into Palace's in-place L0 member-call forms on the destination vector.

## Slug

`axpby-mutation-rotation`

## L1 form (LHS)

The pure-functional update consumes the prior value of `y` and produces a fresh
post-update value. Two LHS shapes appear:

- **axpy** (firm; see [`L1/axpy`](../L1/axpy.md)):

      y_new = axpy(α, x, y_old)        -- y_new = α·x + y_old

- **axpby** (rough-in; harvester promotion pending — see open question
  `axpby-axpbypcz-next-harvest`):

      y_new = axpby(α, x, β, y_old)    -- y_new = α·x + β·y_old

  Palace's L0 `AXPBYPCZ(α, x, β, y, γ, z) = α·x + β·y + γ·z` (member form at
  `vector.cpp:739-743`, free-function template at `vector.cpp:745-758`) is the
  three-vector generalisation; harvester will firm it up as `axpbypcz` and
  decide whether to expose it as a primitive or a fusion of `axpby + axpy`.

## L0 form (RHS)

Three sub-patterns of the same rewrite, distinguished by constant-folding on the
scalar argument. All three are in-place mutating member calls on the destination
vector; the destination is named on the LHS of the call, not in an output
argument.

### Sub-pattern A — bare axpy (general α)

    y.Add(alpha, x);                       // mfem::Vector member
    y.AXPY(alpha, x);                      // ComplexVector member (alias: Add)
    linalg::AXPY(alpha, x, y);             // free-function template

The textbook in-place axpy. Palace dispatches the free-function template to
either the MFEM `Vector::Add` (real path, with the α==1 branch below) or
`ComplexVector::AXPY` (complex path, no branch).

Justification kind: **structural** — the rewrite is purely about re-binding the
L1 output value into the L0 destination buffer.

Citations:
- `palace/linalg/vector.hpp:116-117` — `ComplexVector::AXPY` / `Add` decls.
- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` definition.
- `palace/linalg/vector.cpp:710` — real path `y.Add(alpha, x)` (α≠1 branch).
- `palace/linalg/vector.cpp:715-723` — complex AXPY dispatches.
- `palace/linalg/operator.cpp:464` — `y.Add(a*c, z)` in `SumOperator::AddMult`.
- `palace/linalg/rap.cpp:317` — `y.Add(a, ty)` in `ParOperator::AddMult`.

### Sub-pattern B — `α == 1` specialisation

    y += x;                                // operator+=
    y.Add(x);                              // MFEM Vector::Add(const Vector&)
    linalg::AXPY(1.0, x, y);               // free-function takes the α==1 branch

Algebraic specialisation: `axpy(1, x, y) = y + x`. Palace's real-path
`AXPY(double, Vector, Vector)` branches on `alpha == 1.0` to call `y += x`
rather than `y.Add(1.0, x)` (transparent performance trick — saves one
multiply per element). The complex path does not branch.

Justification kind: **algebraic** — the law `axpy(1, x, y) = y + x` justifies
the specialisation; the L0 branch is a transparent constant-folding trick.

Citations:
- `palace/linalg/vector.cpp:704-706` — `if (alpha == 1.0) { y += x; }`.
- `palace/linalg/vector.hpp:119-123` — `ComplexVector::operator+=` defined as
  `AXPY(1.0, x)`.

### Sub-pattern C — `α == -1` specialisation

    y.Subtract(alpha, x);                  // ComplexVector::Subtract(α, x) ≡ AXPY(-α, x)
    y -= x;                                // operator-=, equivalent to AXPY(-1, x)
    b.Add(-1.0, ty);                       // bare member call with literal -1.0
    linalg::AXPY(-1.0, x, y);              // free function with negated literal

Algebraic specialisation: `axpy(-1, x, y) = y - x`. Palace does not branch on
`α == -1.0` in the real free-function path — callers either pass literal
`-1.0` to `y.Add` (rap.cpp:73) or use one of the operator forms.
`ComplexVector::Subtract(α, x)` (`vector.hpp:118`) is defined as
`AXPY(-α, x)`, so it is a sub-pattern even for non-unit α.

Justification kind: **algebraic** — the laws `axpy(-1, x, y) = y - x` and
`axpy(-α, x, y) = subtract(α, x, y)` ground the rewrites; recognition is by
syntactic match on the negated literal or the `Subtract` / `operator-=`
member name.

Citations:
- `palace/linalg/vector.hpp:118` — `Subtract(α, x) { AXPY(-α, x); }`.
- `palace/linalg/vector.hpp:124-128` — `ComplexVector::operator-=` as
  `AXPY(-1.0, x)`.
- `palace/linalg/rap.cpp:73` — `b.Add(-1.0, ty)` in Dirichlet residual
  correction (real path; literal -1.0 passed to `mfem::Vector::Add`).

## Applicability conditions

For all three sub-patterns the rewrite preserves semantics when:

1. **No aliasing between `x` and `y`.** Palace's L0 kernels read `x` element by
   element while writing `y[i]`; if `x` and `y` alias, the L0 behaviour is
   `y[i] = α·y[i] + y_prev[i]`, which is not `axpy`. The L1 form takes the
   pre-update `y` as a separate value, so the lowering must guarantee
   non-aliased buffers. (Palace never aliases axpy arguments in observed
   sites; this is an applicability condition, not a known failure.)
2. **No observer of the prior `y` value after the call.** The L0 call destroys
   the prior `y`. If a downstream operation reads the prior `y_old` after the
   `y.Add(α, x)` site, the rewrite is invalid — at L1 `y_old` would still be
   in scope. In Palace this is upheld by lexical sequencing: every site
   reads prior `y` only before the `Add` call.
3. **Conforming shape and element type.** `x.Size() == y.Size()`, and either
   both real (`Vector`) or both complex (`ComplexVector`), with the standard
   real→complex scalar promotion rule (see open question
   `scalar-promotion-typing-rule`).
4. **`α` is a runtime scalar (not a special form).** The sub-pattern selection
   is a recognition step on the literal or compile-time-known value of `α`,
   not a runtime check. A runtime α value lowers to sub-pattern A; only
   literal `1.0` or `-1.0` (or the named operator forms `+=` / `-=` /
   `Subtract`) match B and C. The free-function template's real path performs
   a runtime branch on `α == 1.0`; that is a transparent performance trick
   inside sub-pattern A's L0 form, not a fourth sub-pattern.

## Justification kind

- **Sub-pattern A** — `structural`. Re-bind the L1 output value into the L0
  destination buffer.
- **Sub-pattern B** — `algebraic`. `axpy(1, x, y) = y + x`.
- **Sub-pattern C** — `algebraic`. `axpy(-1, x, y) = y - x` and `Subtract(α,
  x) ≡ AXPY(-α, x)`.

The theme as a whole is `structural` with three algebraic sub-rules. A
`lowering-verifier` audit in a later cycle should confirm sub-rule recognition
matches the L0 corpus exhaustively.

## Speculative L1 operators

- `axpby` — rough-in. Signature `(α, x, β, y_old) → α·x + β·y_old`. See
  this report's Speculative operators proposed section.

(The theme does not propose `axpbypcz` here. That is a separate currently-open
harvester question — `axpby-axpbypcz-next-harvest`. Bundling `axpbypcz`
would violate one-theme-per-invocation. A follow-up theme
`axpbypcz-mutation-rotation` should be sketched once `axpbypcz` is
harvested.)

## Verified-against

L0 evidence ranges:

- `palace/linalg/vector.hpp:115-118` — ComplexVector member decls (AXPY,
  Add, Subtract).
- `palace/linalg/vector.hpp:119-128` — operator+= / operator-= bodies.
- `palace/linalg/vector.cpp:276-311` — ComplexVector::AXPY definition.
- `palace/linalg/vector.cpp:701-712` — free-function `AXPY(double, Vector,
  Vector)` with α==1 branch.
- `palace/linalg/vector.cpp:714-723` — free-function complex AXPY dispatches.
- `palace/linalg/operator.cpp:458-466` — `SumOperator::AddMult` uses
  `y.Add(a*c, z)`.
- `palace/linalg/rap.cpp:73` — `b.Add(-1.0, ty)`.
- `palace/linalg/rap.cpp:317` — `y.Add(a, ty)`.

L1 anchor:

- `book/src/L1/axpy.md` — the firm L1 operator that sub-patterns A/B/C all
  lower from.

verified_against:
  - citation: palace/linalg/vector.hpp:115-118
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: ComplexVector member decls AXPY/Add/Subtract; Subtract inline body literally AXPY(-alpha, x).
  - citation: palace/linalg/vector.hpp:119-128
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: operator+= calls AXPY(1.0, x); operator-= calls AXPY(-1.0, x). Both defined-not-used in palace/**.
  - citation: palace/linalg/vector.cpp:276-311
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: ComplexVector::AXPY definition; forall_switch kernel with ai==0 branch; no alpha==1 branch on complex path (matches theme claim).
  - citation: palace/linalg/vector.cpp:701-712
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: Free-function template real-Vector specialisation with verbatim if(alpha==1.0){y+=x;}else{y.Add(alpha,x);} branch.
  - citation: palace/linalg/vector.cpp:714-718
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: Free-function real-alpha-on-ComplexVector specialisation dispatches to ComplexVector::AXPY member; no branch. Used by romoperator.cpp:193-194.
  - citation: palace/linalg/vector.cpp:720-724
    verdict: supports (defined-not-used)
    audited_at: 2026-05-27T00:11:16Z
    note: Free-function complex-alpha-on-ComplexVector specialisation dispatches to ComplexVector::AXPY member; no branch. Defined-not-used — corpus grep of linalg::AXPY returns 5 sites, all pass double alpha. No caller passes std::complex<double>.
  - citation: palace/linalg/operator.cpp:458-466
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: SumOperator::AddMult uses y.Add(a*c, z) inside ops-loop; transpose sibling at 468-475 is same pattern, uncited.
  - citation: palace/linalg/rap.cpp:73
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: b.Add(-1.0, ty); literal -1.0 confirmed sub-pattern-C.
  - citation: palace/linalg/rap.cpp:317
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: y.Add(a, ty); runtime alpha=a; transpose sibling y.Add(a, tx) at rap.cpp:360, uncited.

Coverage note (lowering-verifier audit, 2026-05-27): the corpus contains
~25 additional axpy-shaped sites beyond those cited (under
palace/linalg/{orthog,iterative,chebyshev,floquetcorrection,nleps},
palace/models/{romoperator,waveportoperator,materialoperator}, palace/fem,
palace/drivers/drivensolver). Theme content as written is correct; the
cited set is illustrative not exhaustive. The ComplexVector::Subtract(α, x),
ComplexVector::operator-=, and the free-function
`linalg::AXPY(std::complex<double>, ComplexVector, ComplexVector)`
specialisation (vector.cpp:720-724) are all defined-not-used in palace/**
(definitions exist; no caller sites). Treat these three L0 forms as
recognition rules for *potential* call sites rather than observed ones.
Exhaustive corpus indexing deferred to a future cycle.

## Status

`rough-in` — sub-pattern recognition rules sketched; full sub-rule
verification against the L0 corpus deferred to `lowering-verifier`. The
`axpby` rough-in operator awaits harvester promotion. The optional
`axpbypcz` companion theme is deferred to a separate cycle.
