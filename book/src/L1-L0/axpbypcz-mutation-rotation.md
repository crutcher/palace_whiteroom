---
layer: L1-L0
theme: axpbypcz-mutation-rotation
rank: firm
# L1>L0 lowering-theme leaf. Firm mutation rotation: structural rewrites + a transparent
# γ==0 constant-folding sub-rule over fully-specified positive L0 source. The blocking
# depends-on edges are the rank-terminal positive L0 source (cites-evidence) the rewrite
# rests on. The firm L1 parent (axpbypcz) is recorded as `reference` see-also.
edges:
  depends-on:
    - target: palace/linalg/vector.cpp:745-758
      kind: cites-evidence        # real-real free-function body (with γ==0 branch)
    - target: palace/linalg/vector.cpp:749-751
      kind: cites-evidence        # γ==0 fast-path calling MFEM add(α,x,β,y,z)
    - target: palace/linalg/vector.cpp:755-756
      kind: cites-evidence        # γ≠0 slow-path AXPBY(...); z.Add(...)
    - target: palace/linalg/vector.hpp:313-316
      kind: cites-evidence        # free-function template AXPBYPCZ decl
  reference:
    - L1/axpbypcz
    - L1/axpby
    - L1/axpy
---

# axpbypcz-mutation-rotation

The mutation rotation for the fused three-scalar three-vector update. Lowers
the pure L1 form `axpbypcz(α, x, β, y, γ, z_old) = α·x + β·y + γ·z_old` into
Palace's L0 free-function template and `ComplexVector` member-method forms.
Includes one algebraic sub-rule on `γ == 0` that mixes structural-rebind with
algebraic-constant-folding: when γ=0 the L1 form collapses to `axpby(α, x, β,
y)` and the L0 dispatch selects a 2-vector kernel (MFEM's 5-arg `add(α, x, β,
y, z)` in the real-real path; a γ=0-specialised kernel in the complex
member-form body).

## Slug

`axpbypcz-mutation-rotation`

## L1 form (LHS)

The pure-functional update consumes the prior value of `z` and produces a
fresh post-update value:

    z_new = axpbypcz(α, x, β, y, γ, z_old)
          = α·x + β·y + γ·z_old

where `α, β, γ : Scalar`, `x, y, z_old : Tensor[N]`, and `result : Tensor[N]`.
See [`L1/axpbypcz`](../L1/axpbypcz.md) for the firm operator entry, signature,
and algebraic laws.

## L0 form (RHS)

Four sub-patterns of the same rewrite, distinguished by the dispatch shape of
the L0 call. Plus one algebraic sub-rule on `γ == 0` that applies inside
sub-patterns A and C (the two paths that have a runtime γ==0 branch). The
complete `palace/**` call-site corpus (13 sites) is enumerated below; **every
call site passes a literal scalar in the γ slot** — all `0.0` except the two
real-real sites at `nleps.cpp:343-344` and `romoperator.cpp:188-189`, which use
`1.0`. Consequently sub-patterns **B and D are defined-not-used** (no observed
callers), and the only observed γ≠0 path is sub-pattern A's real-real slow-path.

### Sub-pattern A — free-function real-real

    linalg::AXPBYPCZ(alpha, x, beta, y, gamma, z);     // double α,β,γ; Vector x,y,z

The free-function template specialised on `double` scalars and `mfem::Vector`
vectors. Internally branches on `gamma == 0.0`: the γ==0 fast-path calls
MFEM's `add(alpha, x, beta, y, z)` (5-arg out-of-place; writes z from the
linear combination of the first four args); the γ≠0 slow-path splits into
`AXPBY(alpha, x, gamma, z); z.Add(beta, y)` (two in-place calls computing the
sum in a different order than the fused form would).

Justification kind: **structural** — re-bind the L1 output value into the L0
destination buffer `z`. The γ==0 / γ≠0 internal branch is a transparent
performance specialisation (algebraically equivalent — both compute `α·x +
β·y + γ·z_old`), classified by the γ==0 sub-rule below.

Citations:
- `palace/linalg/vector.hpp:313-316` — free-function template decl.
- `palace/linalg/vector.cpp:745-758` — real-real specialisation body with
  γ==0 branch.
- `palace/linalg/vector.cpp:749-751` — γ==0 fast-path calling MFEM `add(...)`.
- `palace/linalg/vector.cpp:755-756` — γ≠0 slow-path `AXPBY(...); z.Add(...)`.
- `palace/linalg/vector.cpp:729` — MFEM `add(alpha, x, beta, y, y)` kernel
  referenced (via the AXPBY real-real form) by the γ==0 fast-path (also reused
  by the L1 `axpby` operator).
- Call-site: `palace/models/timeoperator.cpp:139` — `linalg::AXPBYPCZ(-1.0,
  rhs1, dJ_coef(t), NegJ, 0.0, rhs1)` (γ=0; **uses aliasing** — z is also the
  first input; see Applicability conditions §1).
- Call-site: `palace/models/timeoperator.cpp:217` — `linalg::AXPBYPCZ(1.0,
  RHS2, dt, k1, 0.0, k2)` (γ=0; non-aliased).
- Call-site: `palace/models/timeoperator.cpp:273` — `linalg::AXPBYPCZ(1.0,
  b2, saved_gamma, x1, 0.0, x2)` (γ=0; non-aliased; `saved_gamma` is the β
  scalar, not γ).
- Call-site: `palace/linalg/nleps.cpp:343-344` — two paired calls
  `linalg::AXPBYPCZ(y(j).real(), X[j].Real(), -y(j).imag(), X[j].Imag(), 1.0,
  z.Real())` and the `.Imag()` sibling, computing the real and imaginary
  halves of a complex linear combination via real `Vector` halves
  (`X[j].Real()`/`.Imag()`, `z.Real()`/`.Imag()`) with `double` scalars and
  **γ=1.0** → real-real free-function (NOT the real-on-complex overload). This
  is the corpus's sole observed exercise of sub-pattern A's γ≠0 slow-path.
- Call-site: `palace/models/romoperator.cpp:188-189` — two paired calls
  `linalg::AXPBYPCZ(y(j).real(), V[j], y(j+1).real(), V[j+1], 1.0, u.Real())`
  and the `.Imag()` sibling. `V` is `std::vector<Vector>` (real), `u.Real()` a
  `Vector` half — real-real free-function, **γ=1.0** (confirmed by the odd-`n`
  companion `linalg::AXPY(y(j).real(), V[j], u.Real())` at romoperator.cpp:193-
  194 hitting the real-`Vector` AXPY overload). Second observed γ≠0 site.

### Sub-pattern B — free-function complex-complex

    linalg::AXPBYPCZ(alpha, x, beta, y, gamma, z);     // std::complex<double> α,β,γ; ComplexVector x,y,z

The free-function template specialised on `std::complex<double>` scalars and
`ComplexVector` vectors. The body is a one-line delegation to the member
form: `z.AXPBYPCZ(alpha, x, beta, y, gamma)`. No internal branch at this
layer — branching happens inside the member-form body (see sub-pattern C).

Justification kind: **structural** — pure trampoline; the destination
re-binding is performed by the member form.

Citations:
- `palace/linalg/vector.cpp:760-765` — complex-complex specialisation body
  (one-line delegation).
- **Defined-not-used.** No call site in the `palace/**` corpus uses the
  `std::complex<double>` α,β,γ overload (the complex call-site corpus uses the
  ComplexVector member form directly — sub-pattern C). Sub-pattern B is a
  recognition rule for *potential* call sites, by analogy with the
  `linalg::AXPY(std::complex<double>, ComplexVector, ComplexVector)`
  defined-not-used form documented in `axpby-mutation-rotation.md`
  Verified-against.

### Sub-pattern C — ComplexVector member form

    z.AXPBYPCZ(alpha, x, beta, y, gamma);              // std::complex<double> α,β,γ; ComplexVector x,y,z

The in-place mutating member method on `ComplexVector`. The destination is
the receiver `z`. The body is a one-line trampoline to a static
member-function (`ComplexVector::AXPBYPCZ` operating on raw real/imag halves
at `vector.cpp:388-455`) which carries the algebraic-branch logic:

- Outer branch on `gamma == 0.0` (at `vector.cpp:402`):
  - γ==0 path: destination buffer obtained via `Write(use_dev)` (the prior z
    is discarded — no read of `ZR`/`ZI`); kernel computes `ZR/I = α·XR/I +
    β·YR/I` (real/imag combined per the complex-multiply rules).
  - γ≠0 path: destination buffer obtained via `ReadWrite(use_dev)`; kernel
    computes `ZR/I = α·XR/I + β·YR/I + γ·ZR/I_prev`.
- Inner branch (both paths) on `ai == 0.0 && bi == 0.0` (real-α, real-β
  fast-path), and additionally on `gi == 0.0` (real-γ fast-path inside the
  γ≠0 outer branch): drops the imaginary-scalar cross-terms from the kernel.
  These inner branches are transparent performance specialisations on the
  scalar imaginary parts; they are not separate L1>L0 sub-patterns (no L1
  algebraic distinction; the L1 scalar-promotion variant axis in
  `axpbypcz.md` covers the typing concern).

Justification kind: **structural** — receiver-as-destination re-binding. The
γ==0 outer branch is the same γ==0 algebraic sub-rule as sub-pattern A
(see § γ==0 algebraic sub-rule below); the inner imaginary-scalar branches
are transparent.

Citations:
- `palace/linalg/vector.hpp:133-136` — member decl with comment
  `In-place addition (*this) = alpha * x + beta * y + gamma * (*this).`
- `palace/linalg/vector.cpp:381-386` — `ComplexVector::AXPBYPCZ` outer
  trampoline (delegates to static member-form on `Real()`/`Imag()` halves).
- `palace/linalg/vector.cpp:388-455` — static member-form body, with the
  γ==0 outer branch and the imaginary-scalar inner branches.
- `palace/linalg/vector.cpp:402-427` — the γ==0 branch block (`Write` access,
  no `γ·Z_prev` cross-terms; closes at 427, before the `else` at 428).
- Call-site: `palace/linalg/slepc.cpp:1986` — `ctx->y1.AXPBYPCZ(ctx->gamma/
  ctx->sigma, ctx->y2, -ctx->gamma/ctx->sigma, ctx->x1, 0.0)` (γ=0; the 5th
  argument is a literal `0.0` — `-gamma/sigma` is the β scalar in the 4th
  slot).
- Call-site: `palace/linalg/arpack.cpp:772` — `y2.AXPBYPCZ(sigma, x1, gamma,
  x2, 0.0)` (γ=0; the `gamma` variable is the β slot).
- Call-site: `palace/linalg/arpack.cpp:787` — `y2.AXPBYPCZ(sigma/gamma, y1,
  1.0, x1, 0.0)` (γ=0).
- Call-site: `palace/linalg/nleps.cpp:471` — `v.AXPBYPCZ(0.5,
  eigenvectors[i1], 0.5, eigenvectors[i2], 0.0)` (γ=0).
- Call-site: `palace/linalg/nleps.cpp:676` — `z.AXPBYPCZ(-delta_eig, w, -1.0,
  u, 0.0)` (γ=0; α=−Δλ, β=−1 literals — algebraic-but-not-fast-path-branched).
- Call-site: `palace/linalg/nleps.cpp:693` — `v_trial.AXPBYPCZ(1.0, v, alpha,
  du, 0.0)` (γ=0).

### Sub-pattern D — free-function real-on-complex

    linalg::AXPBYPCZ(alpha, x, beta, y, gamma, z);     // double α,β,γ; ComplexVector x,y,z

The free-function template specialised on `double` scalars and
`ComplexVector` vectors. The body is a one-line delegation to the member
form: `z.AXPBYPCZ(alpha, x, beta, y, gamma)` — the C++ overload resolution
promotes the `double` scalars to `std::complex<double>` at the call. No
internal branch at this layer — branching happens inside the member-form
body (see sub-pattern C).

Justification kind: **structural** — pure trampoline with implicit
scalar-promotion (covered by the L1 `axpbypcz` "scalar promotion" variant
sub-axis; not a separate L1 operator). The destination re-binding is
performed by the member form.

Citations:
- `palace/linalg/vector.cpp:767-772` — real-on-complex specialisation body
  (one-line delegation with implicit `double`→`std::complex<double>` promotion).
- **Defined-not-used.** No call site in the `palace/**` corpus exercises this
  overload (`double` scalars on `ComplexVector` x,y,z). The two sites
  previously attributed to sub-pattern D — `nleps.cpp:343-344` and
  `romoperator.cpp:188-189` — pass real `Vector` halves (`.Real()`/`.Imag()` /
  `std::vector<Vector>`), not `ComplexVector`s, so they dispatch to the
  **real-real free-function (sub-pattern A)**, not this overload. Sub-pattern D
  is a recognition rule for *potential* call sites (same status as sub-pattern
  B).

### γ==0 algebraic sub-rule (applies inside sub-patterns A and C)

When the recognition is `γ ≡ 0` (a literal `0.0` argument at the L0 call
site, or a compile-time-known γ=0 — observed exclusively as literal `0.0` in
the call-site corpus surveyed above), the L1 form collapses to an `axpby`
call by `axpbypcz` law #1 of [`L1/axpbypcz`](../L1/axpbypcz.md):

    axpbypcz(α, x, β, y, 0, z_old) = α·x + β·y = axpby(α, x, β, y)

The L0 dispatch then selects a structurally distinct 2-vector kernel:

- **Sub-pattern A (real-real)**: the γ==0 branch at `vector.cpp:749-751`
  calls MFEM's 5-arg `add(alpha, x, beta, y, z)` — the same kernel used by
  the L1 `axpby` operator's L0 real-real path (`axpby-mutation-rotation.md`,
  via the AXPBY real-real `add(alpha, x, beta, y, y)` at `vector.cpp:729`).
- **Sub-pattern C (complex member)**: the γ==0 branch at `vector.cpp:402-427`
  selects a `Write`-rather-than-`ReadWrite` access pattern on z and emits a
  kernel without the `γ·ZR/I_prev` cross-terms.

The sub-rule is **algebraic** (γ=0 turns the 3-vector form into a 2-vector
form, by law #1) *and* **structural** (z still gets a new value; the
mutation pattern is preserved — the buffer access mode shifts from
ReadWrite to Write in the complex form, and the kernel arity changes in the
real form, but the L1>L0 destination re-binding stays the same). This is
the first L1>L0 sub-rule in the spec that mixes the two justification
kinds. The recognition rule is **syntactic**: a literal `0.0` at the γ
slot of the call site is sufficient. A runtime-zero γ value lowers to the
γ≠0 path (the L0 branch is on the literal-compared-to-zero test, not on a
type-level zero).

The γ≠0 path of sub-pattern A is itself worth noting as a **load-bearing
numerical observation** (per `CLAUDE.md` "Optimization tricks vs. base
algebra"): the slow-path two-call split `AXPBY(α, x, γ, z); z.Add(β, y)`
(`vector.cpp:755-756`) computes the sum in a *different IEEE-754 evaluation
order* than the γ==0 fast-path's `add(α, x, β, y, z)` would, so bit-identical
reproduction across L0 branches is not guaranteed within the same operator
family. Per the corpus census this slow-path **is exercised** — at the two
real-real γ=1.0 sites (`nleps.cpp:343-344`, `romoperator.cpp:188-189`) — so
the cross-branch summation-order divergence is a **live, not merely potential,
reproduction concern**. This is recorded in `axpbypcz.md` § "Laws that
explicitly do not hold" and is not a defect of this lowering theme — it is a
property of the L0 source.

## Applicability conditions

For all four sub-patterns the rewrite preserves semantics when:

1. **No aliasing between `x`, `y`, and `z`** (with one exception, see
   below). Palace's L0 kernels read `x` and `y` element by element while
   writing `z[i]`; in the γ≠0 path, `z[i]` is also read (the prior z).
   If `x` aliases `z` and γ≠0, the L0 behaviour is well-defined (read-then-
   write at the same index, in-place per element), but the L1 form must
   carry the alias as a structural identity to match: `axpbypcz(α, z, β,
   y, γ, z_old) = α·z_old + β·y + γ·z_old = (α+γ)·z_old + β·y =
   axpby(α+γ, z_old, β, y)`. **Exception observed**:
   `timeoperator.cpp:139` reads `rhs1` and writes `rhs1` (z aliases x)
   with γ=0; under the γ==0 sub-rule this is equivalent to
   `axpby(-1.0, rhs1, dJ_coef, NegJ)` which then reads-and-writes rhs1
   in the L0 `add(α, x, β, y, z)` kernel — MFEM's kernel is defined to be
   alias-safe with the destination matching one of the inputs (verify
   against MFEM docs in a future cycle; flagged in Open questions).
2. **No observer of the prior `z` value after the call.** Same as
   `axpby-mutation-rotation` condition #2.
3. **Conforming shape and element type.** `x.Size() == y.Size() ==
   z.Size()`; all three real (`Vector`) or all three complex
   (`ComplexVector`); the real-on-complex overload at
   `vector.cpp:767-772` (sub-pattern D) promotes scalars implicitly per the
   L1 `axpbypcz` scalar-promotion variant sub-axis — though that overload is
   defined-not-used in the observed corpus (it is a recognition rule, not an
   exercised dispatch).
4. **`γ` is a runtime scalar (not a special form) — γ==0 recognition is
   syntactic.** The γ==0 sub-rule selection is a recognition step on the
   literal `0.0` (or a compile-time-known γ=0) at the L0 call site. A
   runtime γ value, even if it happens to equal zero at runtime, lowers
   to the γ≠0 path. This matches the L0 branch on `gamma == 0.0` — a
   value comparison, not a type-level zero. (Identical structure to
   `axpby-mutation-rotation` condition #4 on α.)
5. **No applicability conditions on α==0 or β==0.** Palace does *not*
   branch on `alpha == 0` or `beta == 0` at L0 — the algebraic
   identities `axpbypcz(0, x, β, y, γ, z) = axpby(β, y, γ, z)` and
   `axpbypcz(α, x, 0, y, γ, z) = axpby(α, x, γ, z)` (laws #3, #4 of
   `axpbypcz.md`) are **recognition-only** rewrites at L1, not L0
   sub-patterns. A future combinator-miner or lowering-verifier may
   choose to upgrade these to fully realised sub-patterns if a use-case
   warrants it; for now they are noted but not branched.

## Justification kind

- **Sub-pattern A** — `structural` (with the γ==0 algebraic sub-rule). The
  only observed γ≠0 path in the corpus.
- **Sub-pattern B** — `structural` (pure trampoline; defined-not-used).
- **Sub-pattern C** — `structural` (receiver-as-destination, with the
  same γ==0 algebraic sub-rule as A; the inner imaginary-scalar branches
  are transparent and not sub-patterns).
- **Sub-pattern D** — `structural` (pure trampoline with implicit
  scalar promotion; defined-not-used).
- **γ==0 algebraic sub-rule** — `algebraic` (law #1 of
  `axpbypcz.md`) *and* `structural` (destination still re-bound; kernel
  shape changes). The theme's first **mixed-justification** sub-rule.

The theme as a whole is `structural` with one mixed-justification
algebraic sub-rule. The call-site corpus is exhaustive (13 sites,
`search_text "AXPBYPCZ\("`): every site uses a literal γ; sub-patterns B and
D are defined-not-used; the only observed γ≠0 path is sub-pattern A's
real-real slow-path.

## Speculative L1 operators

None. `axpbypcz`, `axpby`, and `axpy` are all firm L1 operators
(`book/src/L1/axpbypcz.md`, `book/src/L1/axpby.md`, `book/src/L1/axpy.md`)
and this theme reaches into them as established vocabulary. The γ==0
sub-rule's RHS reference to `axpby(α, x, β, y)` invokes the firm
[`L1/axpby`](../L1/axpby.md) operator directly; no rough-in is needed.
