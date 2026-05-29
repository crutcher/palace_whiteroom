---
agent: abstractor
invoked_at: 2026-05-29T10:55:00Z
scope: L1>L0 theme sketch — apply-nonlinear-pencil-mutation-rotation
status: pending
integrated_at: 2026-05-29T140000Z
integration_commit: INTEGRATION_COMMIT_SHA
integration_notes: "Applied cycle-024 (staging row 4). Firm L1>L0 theme apply-nonlinear-pencil-mutation-rotation landed (last NLEPS L1>L0 leaf); NLEPS L1>L0 cohort COMPLETE. New chapter + L1-L0/index.md dep-map row + SUMMARY.md. Citation nleps.cpp:810-811 kept verbatim per dispatch (no :809-810 shift). No gate hits."
inputs:
  - book/src/L1/apply_nonlinear_pencil.md (firm L1 operator, cycle-021/022)
  - book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md (sibling firm theme, cycle-023 — structure/citation precedent)
  - book/src/L1-L0/lu-solve-mutation-rotation.md (sibling firm theme, cycle-023 — structure/citation precedent)
  - palace/linalg/nleps.cpp:807-821 (positive site: QuasiNewtonSolver::GetResidualNorm)
  - palace/linalg/nleps.cpp:496-499, :556-559, :655, :729 (four corroborating BuildParSumOperator sites)
  - palace/linalg/nleps.cpp:177-181 (SetExtraSystemMatrix — A2 closure type)
  - palace/linalg/eps.hpp:69-74 (nonlinear SetOperators overload — pencil shape)
  - palace/linalg/rap.cpp:832-841 (BuildParSumOperator signature)
---

# CYCLE: L1>L0 theme sketch — apply-nonlinear-pencil-mutation-rotation

## Summary

The firm L1 `apply_nonlinear_pencil` operator (`book/src/L1/apply_nonlinear_pencil.md`) is the
last plain-text-forward-referenced NLEPS L1>L0 leaf — its three firm siblings
(`nleps_deflated_residual`, `lu_solve`, plus the BLAS-1 floor) already reference its lowering as
"no L1>L0 theme yet — plain-text reference." This theme provides it. The L1 form
`r = apply_nonlinear_pencil(T, λ, v) = T(λ)·v` for the operator pencil
`T(λ) = K + λC + λ²M + A2(|Im λ|)` lowers into **two algebraically-identical L0 build forms**:
(A) the term-by-term in-place accumulation `opK->Mult; opC->AddMult; opM->AddMult; A2->AddMult`
into a destination buffer `r` (the clean positive site `QuasiNewtonSolver::GetResidualNorm`,
`palace/linalg/nleps.cpp:807-821`), and (B) a `BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM,
A2})` materialization of the coefficient-weighted operator sum followed by a single `Mult` (the
four in-`Solve` sites `:496-499`, `:556-559`, `:655`, `:729`). The two forms are equal by the
operator-sum-distributes law (`apply_linop` law 5: `(ΣcᵢAᵢ)·v = Σcᵢ(Aᵢ·v)`); the L1 names the
apply. The rewrite is **structural**, decomposing into three sub-patterns — (A) term-by-term
`Mult`/`AddMult` ↔ sum-of-applies, (B) `BuildParSumOperator`+`Mult` ↔ operator-sum-then-apply
(the build-form duality, transparent), (C) the `A2(|Im λ|)` closure-evaluation-and-apply (the
nonlinear leaf, with the `|Im λ|` real-projection contract and the `A2`-caching transparent
trick). No new L1 vocabulary; every constituent is already firm (`apply_linop`, `axpby`,
`axpbypcz`). Status `firm`, on the firm-on-positive-structure precedent inherited from the
operator it lowers — the laws are syntactic identities on a fully-specified read closure, so the
NLEPS test-coverage absence does not gate the firm decision.

All L0 citations below were **self-verified** this invocation via `palace-codemap` `read_range`
(not from memory or the L1 entry's text) — inline-anchor-drift is a live friction this batch; the
verified line map is in §Supporting evidence.

## Proposed changes

```new:book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md
---
status: firm
layer: L1>L0
theme: apply-nonlinear-pencil-mutation-rotation
l1_anchor: book/src/L1/apply_nonlinear_pencil.md
l0_anchor: palace/linalg/nleps.cpp:807-821
justification: structural
---

# apply-nonlinear-pencil-mutation-rotation

How the firm L1 [`apply_nonlinear_pencil`](../L1/apply_nonlinear_pencil.md) form lowers into its
L0 source: the nonlinear-pencil residual apply `r = T(λ)·v` for the operator pencil
`T(λ) = K + λC + λ²M + A2(|Im λ|)` inside Palace's `QuasiNewtonSolver` NEP loop
(`palace/linalg/nleps.cpp`). This is the **interior pencil-apply atom** that
[`nleps-deflated-residual-mutation-rotation`](./nleps-deflated-residual-mutation-rotation.md)
extends with deflation, and the per-step operator-cost unit that the
[`eigsolve`](../L1/eigsolve.md) `direct_newton` orchestration is composed of. It is to the NEP
Newton loop what [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md) is to the
linear Krylov loop.

## Slug

`apply-nonlinear-pencil-mutation-rotation`

## Status

`firm` — the rewrite is read from a **positive** source site (`QuasiNewtonSolver::GetResidualNorm`,
`palace/linalg/nleps.cpp:807-821`) and corroborated at four further positive sites
(`:496-499` in-`Solve` setup, `:556-559` deflated-residual `k==0` core, `:655` Jacobian build,
`:729` lagged system-operator refresh). Both L0 build forms — the term-by-term `Mult`+`AddMult`
accumulation (`:812-819`) and the `BuildParSumOperator`+`Mult` materialization (`:498-499`,
`:557-559`) — are directly cited; the `BuildParSumOperator` signature
(`palace/linalg/rap.cpp:832-841`) and the `A2`-closure type (`SetExtraSystemMatrix`,
`palace/linalg/nleps.cpp:177-181`) ground the structure. The rewrite is a **structural** syntactic
expansion — no sub-part is materialized from negative anchors, so there is no
`partly-constructive` caveat. This matches the firm-on-positive-structure status of the operator
this theme lowers (`book/src/L1/apply_nonlinear_pencil.md:98`) and the sibling deflated-residual
theme (`book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md:23-35`): every law is a
syntactic identity on a fully-specified positive source closure (linearity in `v`, term
decomposition, build-form duality), so the NLEPS test-coverage absence (`search_text` for
`QuasiNewton|nleps|funcA2|GetResidualNorm` over `test/unit/**` returns zero hits) does not gate
the firm decision — the laws do not depend on convergence behaviour. A `lowering-verifier` audit
attaching the `verified_against:` block (per the sibling-theme convention) confirming surface-form
recognition is exhaustive is the standard follow-up, not a status reduction.

## L1 form (LHS)

The pure-functional L1 operator — no destination buffer, no `A2`-caching, no build-form choice in
the signature (`book/src/L1/apply_nonlinear_pencil.md:21-26`):

```text
apply_nonlinear_pencil
  :: (T: NonlinearPencil[N], λ: Complex, v: Tensor[N]) -> Tensor[N]

apply_nonlinear_pencil(T, λ, v) = T(λ) · v
                                = K·v + λ·(C·v) + λ²·(M·v) + (A2(|Im λ|))·v
```

`T` binds four operators over a shared square axis `N`: `T.K : LinearOperator[N, N]` (stiffness /
curl-curl), `T.M : LinearOperator[N, N]` (mass), `T.C : Maybe LinearOperator[N, N]` (damping —
`Nothing` drops the `λ·(C·v)` term), and the opaque nonlinear closure
`T.A2 : Real -> LinearOperator[N, N]`. The polynomial coefficients are the full complex `λ` and
`λ²`; the closure is evaluated at the **real** argument `|Im λ|` (the frequency convention —
`book/src/L1/apply_nonlinear_pencil.md:51`, semantics point 1). Element type is **complex-only**.
The destination buffer, the `A2`-caching, the term-vs-sum build-form choice, and the in-place
accumulation order are **not** in the L1 signature — they are exactly what this lowering exposes.

## L0 form (RHS)

The L1 pencil apply lowers into **two algebraically-identical L0 build forms**, both witnessed in
`QuasiNewtonSolver` (`palace/linalg/nleps.cpp`). They share the same `{1, λ, λ², 1}` coefficient
vector over `{opK, opC, opM, A2(|Im λ|)}`; they differ in whether the operator-sum is materialized
(form B) or never built (form A).

**Form A — term-by-term in-place accumulation** (the clean positive site,
`QuasiNewtonSolver::GetResidualNorm`, `palace/linalg/nleps.cpp:807-821`):

```text
// nleps.cpp:810-811 — the source's own statement:
//   "Compute the i-th eigenpair residual: || P(λ) x ||₂ = || (K + λ C + λ² M + A2(λ)) x ||₂"
double QuasiNewtonSolver::GetResidualNorm(std::complex<double> l, const ComplexVector &x,
                                          ComplexVector &r) const
{                                                                       // :809
  opK->Mult(x, r);                                                      // :812  r  := K·x
  if (opC)                                                             // :813
  {                                                                    // :814
    opC->AddMult(x, r, l);                                            // :815  r  += l · (C·x)
  }                                                                    // :816
  opM->AddMult(x, r, l * l);                                          // :817  r  += l² · (M·x)
  auto A2 = (*funcA2)(std::abs(l.imag()));                           // :818  build A2 at |Im l|
  A2->AddMult(x, r, 1.0);                                            // :819  r  += 1.0 · (A2·x)
  return linalg::Norml2(comm, r);                                    // :820  ‖r‖₂  (the fused norm)
}                                                                     // :821
```

**Form B — `BuildParSumOperator` materialization then single `Mult`** (the four in-`Solve` sites;
the deflated-residual core shown, `palace/linalg/nleps.cpp:556-559`):

```text
auto A2_out = (*funcA2)(std::abs(lam.imag()));                       // :556  build A2 at |Im lam|
auto A = BuildParSumOperator({1.0 + 0.0i, lam, lam * lam, 1.0 + 0.0i}, // :557  the {1,λ,λ²,1}
                             {opK, opC, opM, A2_out.get()}, true);     // :558  coeff-weighted sum op
A->Mult(vv, rr);                                                      // :559  rr := T(λ)·vv  (one apply)
```

`BuildParSumOperator` (`palace/linalg/rap.cpp:832-841`) takes a length-`N` coefficient array, a
length-`N` operator-pointer array (a `nullptr` entry — e.g. absent `opC` — is skipped), and a
`bool set_essential`; it returns a single `ComplexParOperator` whose `Mult` applies the
coefficient-weighted sum. The two forms compute the identical vector
`r = K·v + λ·(C·v) + λ²·(M·v) + A2(|Im λ|)·v`.

## Rewrite — forward (L1 → L0)

The pure `r = apply_nonlinear_pencil(T, λ, v)` rewrites to either L0 build form, applied with a
destination buffer `r` (in place of the returned value) and an optional `A2`-operator cache. The
rewrite proceeds via the three sub-patterns below.

The L0-only material the L1 signature drops:

- **Destination buffer.** `r` (a `ComplexVector &`) is an output reference overwritten in place —
  `opK->Mult(x, r)` writes it, the three `AddMult` calls accumulate into it (`:812-819`); the
  `BuildParSumOperator` form writes it with one `A->Mult(vv, rr)` (`:559`). The L1 form returns the
  value. Buffer reuse across the Newton/line-search iterations is a transparent L1>L0 trick.
- **`A2` carry-back / caching.** `A2 = (*funcA2)(|Im λ|)` (`:818`) is re-evaluated per call in
  `GetResidualNorm`, but the `compute_residual` form returns the built `A2_out` by reference
  (`:556`, the `A2_out` parameter) so the caller can skip re-assembly at the same `λ` across a line
  search. Pure-functional re-evaluation at L1; an L0 caching concern only
  (`book/src/L1/apply_nonlinear_pencil.md:72`, the `A2`-recompute bit-non-idempotence non-law).
- **The build-form choice.** Whether to materialize the operator-sum (form B) or accumulate
  term-by-term (form A) is an L0 decision absorbed at L1 by Sub-pattern B's duality.

### Sub-pattern A — term-by-term `Mult`+`AddMult` ↔ sum-of-applies

The `GetResidualNorm` form never builds the sum operator; it accumulates the four terms directly
into the destination (`:812-819`):

```text
opK->Mult(x, r);            // :812   r := K·x
opC->AddMult(x, r, l);      // :815   r += l·(C·x)     (only when opC present)
opM->AddMult(x, r, l*l);    // :817   r += l²·(M·x)
A2->AddMult(x, r, 1.0);     // :819   r += 1.0·(A2·x)
```

This is exactly `apply_nonlinear_pencil`'s **term-decomposition law** (its law 3,
`book/src/L1/apply_nonlinear_pencil.md:63`):

```text
T(λ)·v = apply_linop(K, v) + λ·apply_linop(C, v) + λ²·apply_linop(M, v) + apply_linop(A2(|Im λ|), v)
```

Each `op->Mult` / `op->AddMult` is an [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md)
in accumulate-mode: the L0 `AddMult(x, r, c)` is the fused `r ← r + c·(op·x)` form, which is
`axpby(c, apply_linop(op, x), 1, r)` per `apply_linop`'s accumulate-mode treatment (so the term
accumulation transitively reuses [`axpby-mutation-rotation`](./axpby-mutation-rotation.md) /
[`axpbypcz-mutation-rotation`](./axpbypcz-mutation-rotation.md)). The leading `opK->Mult(x, r)`
is the write-mode `apply_linop` that initializes `r`; the three `AddMult` calls accumulate. The
**damping term is conditional** — `if (opC)` (`:813`) guards the `λ·(C·x)` accumulation, realizing
the `T.C = Maybe LinearOperator` axis (when `Nothing`, the term is dropped).

Justification kind: **structural** — the rewrite is the syntactic recognition that the
`Mult` + three-`AddMult` chain on the four bound operators is the unfolded sum-of-applies of the
fixed-`λ` linear operator `T(λ)`.

Citations:
- `palace/linalg/nleps.cpp:810-811` — the source's own residual statement
  (`|| (K + λ C + λ² M + A2(λ)) x ||₂`).
- `palace/linalg/nleps.cpp:812` — `opK->Mult(x, r)`: `r := K·x` (write-mode init).
- `palace/linalg/nleps.cpp:813-816` — `if (opC) { opC->AddMult(x, r, l); }`: the conditional
  `λ·(C·x)` accumulation (the `Maybe C` damping axis).
- `palace/linalg/nleps.cpp:817` — `opM->AddMult(x, r, l * l)`: `r += λ²·(M·x)`.
- `palace/linalg/nleps.cpp:818` — `auto A2 = (*funcA2)(std::abs(l.imag()))`: the closure built at
  `|Im λ|` (Sub-pattern C).
- `palace/linalg/nleps.cpp:819` — `A2->AddMult(x, r, 1.0)`: `r += 1.0·(A2·x)` (the nonlinear term).
- `book/src/L1/apply_nonlinear_pencil.md:63` — law 3 (term decomposition / sum-of-applies).

### Sub-pattern B — `BuildParSumOperator`+`Mult` ↔ operator-sum-then-apply (the build-form duality)

The four in-`Solve` sites instead **materialize** the coefficient-weighted operator sum and apply
it once (`:557-559`):

```text
auto A = BuildParSumOperator({1.0 + 0.0i, lam, lam * lam, 1.0 + 0.0i},  // :557
                             {opK, opC, opM, A2_out.get()}, true);       // :558
A->Mult(vv, rr);                                                        // :559   rr := T(λ)·vv
```

`A` is the single `ComplexParOperator` realizing `T(λ) = 1·K + λ·C + λ²·M + 1·A2(|Im λ|)`; its
`Mult` is one apply. Sub-pattern A (sum-of-applies) and Sub-pattern B (operator-sum-then-apply) are
equal by the **operator-sum-distributes** law of `apply_linop` (its law 5):

```text
(ΣᵢcᵢAᵢ)·v  =  Σᵢcᵢ(Aᵢ·v),
```

i.e. `apply_linop(BuildParSumOperator(c, ops), v) = Σᵢ cᵢ·apply_linop(opsᵢ, v)`. This is the
**build-form variant axis** collapsed at L1 (`book/src/L1/apply_nonlinear_pencil.md:94`): the L1
form sees one apply; the term-vs-sum choice is an L0 / transparent-performance concern. The
coefficient vector `{1, λ, λ², 1}` and operator list `{opK, opC, opM, A2}` are the **same five-site
shared shape** — built identically at the in-`Solve` linear-solver setup (`:498-499`), the
deflated-residual core (`:557-558`), and the lagged system-operator refresh (`:729`); the Jacobian
(`:655`) reuses the same construction with coefficient vector `{0, 1, 2λ, 1}` and the `A2'`
derivative closure (the **purpose / coefficient-vector** variant axis,
`book/src/L1/apply_nonlinear_pencil.md:89`; law 4 coefficient-vector-linearity makes this a
substitution, not a new operator).

The two build forms are algebraically identical but **not bit-identical**: the term-by-term
accumulation orders the four operator contributions differently from the materialized-sum apply,
and the matrix-free `A2` term inherits reduction-tree non-associativity from `apply_linop`
(`book/src/L1/apply_nonlinear_pencil.md:71`, the recorded non-law). The mathematical law-3 identity
holds; its floating-point realization is exact modulo accumulation-order noise — load-bearing per
the CLAUDE.md trick taxonomy, recorded not erased.

Justification kind: **structural** (with a load-bearing accumulation-order note) — the rewrite is
the syntactic recognition that the `BuildParSumOperator`+`Mult` pair is the operator-sum-then-apply
dual of the term-by-term sum-of-applies, equal by `apply_linop` law 5.

Citations:
- `palace/linalg/nleps.cpp:557-558` — `BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM,
  A2_out.get()}, true)`: the materialized coefficient-weighted sum (the deflated-residual core).
- `palace/linalg/nleps.cpp:559` — `A->Mult(vv, rr)`: `rr := T(λ)·vv` (the single apply).
- `palace/linalg/nleps.cpp:498-499` — `opA = BuildParSumOperator({1, eig, eig*eig, 1}, {opK, opC,
  opM, opA2.get()}, true)`: the in-`Solve` linear-solver setup (second build site, same shape).
- `palace/linalg/nleps.cpp:729` — the lagged system-operator refresh: the same `{1, λ, λ², 1}`
  pencil rebuilt into `opA` at the committed `λ` (`eig_opInv`).
- `palace/linalg/nleps.cpp:655` — `opJ = BuildParSumOperator({0, 1, 2·eig, 1}, {opK, opC, opM,
  opAJ.get()}, true)`: the Jacobian build (same construction, `{0, 1, 2λ, 1}` coefficient vector;
  law 4 / law 5 — the purpose variant axis).
- `palace/linalg/rap.cpp:832-841` — `BuildParSumOperator(coeff: array<complex,N>, ops:
  array<ComplexParOperator*,N>, set_essential: bool)`: the construction signature (a `nullptr`
  operator entry is skipped — `std::find_if(... p != nullptr ...)`, `:837`).
- `book/src/L1/apply_nonlinear_pencil.md:94` — the L0-build-form collapsed variant axis (term-by-
  term `AddMult` vs `BuildParSumOperator`+`Mult`).
- `book/src/L1/apply_nonlinear_pencil.md:71` — the two-build-form bit-difference non-law.

### Sub-pattern C — `A2(|Im λ|)` closure evaluation + apply (the nonlinear leaf)

Both build forms evaluate the opaque nonlinear closure at the **real** argument `|Im λ|` and apply
the freshly-built operator as the fourth term:

```text
auto A2 = (*funcA2)(std::abs(l.imag()));   // :818  (Form A)  — closure at |Im λ|
A2->AddMult(x, r, 1.0);                    // :819             — r += A2·x
// or, in Form B:
A2_out = (*funcA2)(std::abs(lam.imag()));  // :556  (Form B)  — closure at |Im λ|, carried back
//   ...folded into BuildParSumOperator as the 4th operand (:558), applied by A->Mult (:559).
```

The closure `funcA2` has type `std::function<std::unique_ptr<ComplexOperator>(double)>` —
**a single real argument** (`SetExtraSystemMatrix`, `palace/linalg/nleps.cpp:177-181`). The
evaluation point is `std::abs(l.imag()) = |Im λ|`, the angular frequency at which the
frequency-dependent material/boundary operator is assembled. This is **not** an algebraic identity
recoverable from a "uniform `λ`" form — the polynomial terms take the full complex `λ`/`λ²` while
`A2` takes the lossy real projection `|Im λ|`; the asymmetry is part of the operator's contract
(`book/src/L1/apply_nonlinear_pencil.md:51`, semantics point 1), pinned in the closure type
`Real -> LinearOperator` and the evaluation point, not absorbed.

The closure is a **genuine black box** at L1 — `apply_nonlinear_pencil` sees a function and an
evaluation point, not inside it. At L0 the closure's realisation is one of several
(frequency-dependent re-assembly, or a `NewtonInterpolationOperator` Newton-polynomial
interpolation, `palace/linalg/nleps.hpp:232-283`) — the **A2-representation** variant axis,
collapsed at L1 to the single opaque `Real -> LinearOperator[N, N]`
(`book/src/L1/apply_nonlinear_pencil.md:93`). The cost of building `A2(|Im λ|)` is real and is why
`compute_residual` carries `A2_out` back to the caller for reuse across a line search (`:556` — the
`A2_out` reference parameter); the *value* is identical (transparent trick), but rebuilding a
matrix-free / re-assembled `A2` is not guaranteed bit-reproducible
(`book/src/L1/apply_nonlinear_pencil.md:72`, the `A2`-recompute bit-non-idempotence non-law).

Justification kind: **structural** — `:818`/`:556` are syntactic closure evaluations at `|Im λ|`;
`:819` is the accumulate-mode `apply_linop` of the built operator. The `|Im λ|` real-projection
contract and the `A2`-caching trick are the load-bearing notes, recorded not erased.

Citations:
- `palace/linalg/nleps.cpp:818` — `auto A2 = (*funcA2)(std::abs(l.imag()))`: the closure built at
  `|Im λ|` (Form A).
- `palace/linalg/nleps.cpp:556` — `A2_out = (*funcA2)(std::abs(lam.imag()))`: the closure built at
  `|Im λ|` and carried back for caching (Form B).
- `palace/linalg/nleps.cpp:177-181` — `QuasiNewtonSolver::SetExtraSystemMatrix(std::function<
  std::unique_ptr<ComplexOperator>(double)> A2) { funcA2 = A2; }`: the real-argument closure type
  (the operative closure the solver evaluates).
- `palace/linalg/nleps.hpp:232-283` — `Interpolation` (`:232`) / `NewtonInterpolationOperator`
  (`:246`): one concrete `A2`-representation (the collapsed A2-representation axis).
- `book/src/L1/apply_nonlinear_pencil.md:51` — semantics point 1 (the `|Im λ|` frequency-argument
  asymmetry).

## Applicability conditions

- The pencil `T(λ)` is bound as `{1, λ, λ², 1}` over `{opK, opC, opM, A2(|Im λ|)}`; the
  `with-C` / `without-C` damping axis is absorbed by the `Maybe C` pencil argument (`if (opC)` at
  `:813`; the two `SetOperators` overloads `:191`/`:221`).
- Element type is **complex-only** (the pencil operators are `ComplexOperator`, the carriers
  `ComplexVector`). No real specialization.
- The closure `A2` is evaluated at the **real** argument `|Im λ|`, not the complex `λ` (semantics
  point 1). The polynomial coefficients use the full complex `λ`/`λ²`. A lowering must preserve
  this asymmetry.
- Single-rank scope (CLAUDE.md "Scope"): the per-operator `Mult`/`AddMult` and the
  `BuildParSumOperator` apply are local operator actions; any `Mpi::GlobalSum` lives inside the
  downstream `Norml2` (the fused norm at `:820`), not in the apply itself.
- **Build-form choice is free in value, load-bearing in floating-point.** Form A (term-by-term)
  and form B (`BuildParSumOperator`+`Mult`) are value-identical (law 5) but bit-differ in
  accumulation order. A lowering may pick either; it must record which to reproduce that call's
  floating-point behaviour (the recorded non-law).

## Justification kind

**Structural** — the rewrite is the syntactic expansion of one pure L1 pencil apply into the L0
destination-buffer composition, in two algebraically-identical build forms. Three structural
recognitions carry the theme: (A) the `Mult` + three-`AddMult` chain is the unfolded
sum-of-applies (law 3) of the fixed-`λ` linear operator; (B) the `BuildParSumOperator`+`Mult` pair
is its operator-sum-then-apply dual (law 5 / build-form variant axis); (C) `:818`/`:556` are
closure evaluations at `|Im λ|` with the apply as the fourth term. The one load-bearing
non-structural note is the form-A-vs-form-B accumulation-order bit-difference (Sub-pattern B),
recorded per the trick taxonomy.

## Speculative L1 operators

**None.** Every constituent is **already firm L1 vocabulary**: `apply_linop` (firm — each pencil
term is an `apply_linop`), `axpby` / `axpbypcz` (firm — the `AddMult` accumulate-mode form),
`nrm2` (firm — the adjacent fused norm at `:820`, not part of the apply). This theme proposes no
new rough-in operators — it composes existing firm leaves and inherits the sibling lowering
themes. The opaque `A2 : Real -> LinearOperator[N, N]` closure is an **opaque leaf** at L1 (its
internal assembly is below L1 resolution); whether the `A2'` finite-difference build (the Jacobian
derivative pencil, `:653-655`) deserves a small `divided_difference_operator` primitive is a
deferred upstream decision (see the parent's Open questions), **not** a speculative operator of
this theme.

## Verified-against

L0 evidence ranges (self-verified via `palace-codemap` `read_range` / `get_symbol_def` this
invocation — producer-citation self-verification, `verify-citation-range`):

- `palace/linalg/nleps.cpp:807-821` — `QuasiNewtonSolver::GetResidualNorm` (Form A, the clean
  positive site): signature `:807-808`, comment `:810-811`, `opK->Mult(x, r)` `:812`, `if (opC) {
  opC->AddMult(x, r, l); }` `:813-816`, `opM->AddMult(x, r, l*l)` `:817`, `auto A2 =
  (*funcA2)(std::abs(l.imag()))` `:818`, `A2->AddMult(x, r, 1.0)` `:819`, `return
  linalg::Norml2(comm, r)` `:820`. **Self-verified** (`read_range` 806-821).
- `palace/linalg/nleps.cpp:496-499` — in-`Solve` linear-solver setup: `opA2 = (*funcA2)(std::abs(
  eig.imag()))` `:497`, `opA = BuildParSumOperator({1, eig, eig*eig, 1}, {opK, opC, opM,
  opA2.get()}, true)` `:498-499`. **Self-verified** (`read_range` 494-500).
- `palace/linalg/nleps.cpp:556-559` — `compute_residual` core (Form B): `A2_out =
  (*funcA2)(std::abs(lam.imag()))` `:556`, `auto A = BuildParSumOperator({1, lam, lam*lam, 1},
  {opK, opC, opM, A2_out.get()}, true)` `:557-558`, `A->Mult(vv, rr)` `:559`. **Self-verified**
  (`read_range` 547-560).
- `palace/linalg/nleps.cpp:655` — Jacobian build: `auto opJ = BuildParSumOperator({0, 1, 2*eig,
  1}, {opK, opC, opM, opAJ.get()}, true)` `:655-656`, `opJ->Mult(v, w)` `:657`; the `A2'`
  finite-difference closure `opA2p`/`opAJ` at `:650-654`. **Self-verified** (`read_range` 650-658).
- `palace/linalg/nleps.cpp:729` — lagged system-operator refresh: `opA = BuildParSumOperator({1,
  eig_opInv, eig_opInv*eig_opInv, 1}, {opK, opC, opM, opA2.get()}, true)` (`opA =` at `:728`,
  args at `:729-730`); `opA2 = (*funcA2)(std::abs(eig_opInv.imag()))` `:727`. **Self-verified**
  (`read_range` 725-733).
- `palace/linalg/nleps.cpp:177-181` — `QuasiNewtonSolver::SetExtraSystemMatrix(std::function<
  std::unique_ptr<ComplexOperator>(double)> A2) { funcA2 = A2; }`: the real-argument closure type.
  **Self-verified** (`read_range` 176-182).
- `palace/linalg/nleps.cpp:191`, `:221` — the two `SetOperators` overloads (`without-C` at `:191`,
  `with-C` at `:221`): the damping-present axis. **Self-verified** (`read_range` 189-225).
- `palace/linalg/nleps.hpp:146` — class comment "Quasi-Newton nonlinear eigenvalue solver for
  (K + λ C + λ² M + A2(λ)) x = 0" (preceding `class QuasiNewtonSolver` at `:147`). **Self-verified**
  (`read_range` 144-148).
- `palace/linalg/rap.cpp:832-841` — `BuildParSumOperator(coeff: array<complex,N>, ops:
  array<ComplexParOperator*,N>, set_essential: bool)`: the construction signature; a `nullptr`
  operator entry is skipped (`std::find_if(... p != nullptr ...)`, `:837`). **Self-verified**
  (`get_symbol_def BuildParSumOperator` → rap.cpp:832-912 + `read_range` 832-842).
- `palace/linalg/eps.hpp:69-74` — the nonlinear `SetOperators(K, M, A2, type)` virtual: corroborates
  the pencil shape + complex-only element type; note this overload's `A2` is a *complex-argument*
  closure (`std::function<const ComplexOperator &(std::complex<double>)>`), distinct from the
  operative real-argument `SetExtraSystemMatrix` closure. **Self-verified** (`read_range` 57-74).

L1 / cross-theme anchors:

- `book/src/L1/apply_nonlinear_pencil.md` — the firm L1 operator this theme lowers: signature
  (`:21-26`), term-decomposition law 3 (`:63`), `|Im λ|` semantics point 1 (`:51`), the L0-build-
  form collapsed axis (`:94`), the two-build-form bit-difference non-law (`:71`), the
  `A2`-recompute bit-non-idempotence non-law (`:72`), and the firm-on-positive-structure status
  (`:98`).
- `book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md` — the deflation **extension** of
  this theme (its Sub-pattern A is the linearity-collapse of the `vv` + `XSvv2` corrected-vector
  apply; the `k==0` degeneration is exactly this bare-pencil apply).
- `book/src/L1-L0/apply-linop-mutation-rotation.md` — the per-term operator action (each pencil
  term is an `apply_linop`; the `AddMult` accumulate-mode is the bridge).
- `book/src/L1-L0/axpby-mutation-rotation.md` / `axpbypcz-mutation-rotation.md` — the
  `AddMult(x, r, c) = axpby(c, op·x, 1, r)` accumulate-mode fusion (transitive).
- No dedicated unit test (NLEPS test-coverage absence inherited from `apply_nonlinear_pencil` /
  `eigsolve`); the firm decision rests on exhaustive positive structural citation.
```

```edit:book/src/L1-L0/index.md
| [nleps-deflated-residual-mutation-rotation](./nleps-deflated-residual-mutation-rotation.md) | `L1/nleps_deflated_residual` (firm) | `palace/linalg/nleps.cpp:547-577` (+ `:329-347` MatVecMult, `:587`/`:702` call sites) | firm *(structural; 3 sub-patterns A/B/C; load-bearing Mult+AddMult→single-pencil-apply collapse; reuses dot Sub-pattern A; reuses lin-comb fold L2>L1)* |
| [apply-nonlinear-pencil-mutation-rotation](./apply-nonlinear-pencil-mutation-rotation.md) | `L1/apply_nonlinear_pencil` (firm) | `palace/linalg/nleps.cpp:807-821` (+ `:496-499`/`:556-559`/`:655`/`:729` BuildParSumOperator sites; `:177-181` A2-closure; `rap.cpp:832-841` BuildParSumOperator) | firm *(structural; 3 sub-patterns A term-by-term/B BuildParSumOperator-dual/C A2-closure-at-\|Im λ\|; load-bearing build-form accumulation-order non-law; reuses apply_linop laws 3/5)* |
```

```edit:book/src/SUMMARY.md
- [lu-solve-mutation-rotation](./L1-L0/lu-solve-mutation-rotation.md)
- [apply-nonlinear-pencil-mutation-rotation](./L1-L0/apply-nonlinear-pencil-mutation-rotation.md)
```

## Speculative operators proposed

**None.** This theme composes existing firm L1 vocabulary only:
- `apply_linop` (firm) — each of the (up to) four pencil terms is an `apply_linop`; its law 3
  (term decomposition) is Sub-pattern A and its law 5 (operator-sum-distributes) is Sub-pattern B.
- `axpby` / `axpbypcz` (firm) — the `AddMult(x, r, c) = r ← r + c·(op·x)` accumulate-mode fusion.
- `nrm2` (firm) — adjacent (the fused norm at `:820`), not part of the apply.

No harvester promotion is needed. The only candidate-for-future-vocabulary the theme *touches* is
a `divided_difference_operator` for the Jacobian's `A2'` finite-difference build (`:653-655`) — but
that is explicitly an **upstream Jacobian-pencil decision deferred by the parent's open questions**,
not an operator of this bare-pencil-apply theme.

## Supporting evidence

Self-verified L0 line map (`palace-codemap` `read_range`, this invocation — confirming no
inline-anchor drift from the L1 entry's cited ranges):

| construct | cited | verified-on-disk | match |
|---|---|---|---|
| `GetResidualNorm` sig | `:807-808` | 807-808 | ✓ |
| `opK->Mult(x, r)` | `:812` | 812 | ✓ |
| `if (opC) { opC->AddMult(x, r, l); }` | `:813-816` | 813-816 | ✓ |
| `opM->AddMult(x, r, l*l)` | `:817` | 817 | ✓ |
| `auto A2 = (*funcA2)(std::abs(l.imag()))` | `:818` | 818 | ✓ |
| `A2->AddMult(x, r, 1.0)` | `:819` | 819 | ✓ |
| `return linalg::Norml2(comm, r)` | `:820` | 820 | ✓ |
| in-`Solve` `opA2 = (*funcA2)(...)` | `:497` | 497 | ✓ |
| in-`Solve` `BuildParSumOperator(...)` | `:498-499` | 498-499 | ✓ |
| `compute_residual` `A2_out = (*funcA2)(...)` | `:556` | 556 | ✓ |
| `compute_residual` `BuildParSumOperator(...)` | `:557-558` | 557-558 | ✓ |
| `compute_residual` `A->Mult(vv, rr)` | `:559` | 559 | ✓ |
| Jacobian `opJ = BuildParSumOperator({0,1,2λ,1},...)` | `:655` | 655-656 | ✓ |
| Jacobian `opJ->Mult(v, w)` | `:657` | 657 | ✓ |
| refresh `BuildParSumOperator({1,λ,λ²,1},...)` | `:729` | 729-730 | ✓ |
| `SetExtraSystemMatrix` closure type | `:177-181` | 177-181 | ✓ |
| `SetOperators` without-C / with-C | `:191` / `:221` | 191 / 221 | ✓ |
| class comment (pencil eqn) | `nleps.hpp:146` | 146 | ✓ |
| `BuildParSumOperator` signature | `rap.cpp:832-841` | 832-841 (def 832-912) | ✓ |
| nonlinear `SetOperators` overload | `eps.hpp:69-74` | 69-74 | ✓ |

Every citation in the proposed theme is confirmed against on-disk source. The L1 entry's existing
citation ranges were found accurate; no carry-forward correction to `book/src/L1/apply_nonlinear_pencil.md`
is needed.

## Open questions / caveats

- **`A2`-closure assembly is below L1 resolution and surfaces only in this lowering.** The opaque
  `A2 : Real -> LinearOperator[N, N]` closure's internal realisation (frequency-dependent surface
  impedance, lumped-port admittance, `NewtonInterpolationOperator` Newton-polynomial interpolation,
  `palace/linalg/nleps.hpp:232-283`) is collapsed at L1 to a single opaque function. This theme
  treats it as an opaque leaf. If a future L2/L3 effort needs the *inside* of `A2` (e.g. to lift
  the frequency-dependence into a tensor-field op), the closure-assembly L0 surface
  (`NewtonInterpolationOperator`, the impedance/admittance integrators) would itself need a harvest
  — that is the natural follow-up boundary, recorded here so the lowering does not over-promise.
- **Jacobian-derivative-pencil decision is upstream-deferred (not this theme's).** The L1 entry's
  law 5 records the Jacobian `T'(λ)·v = apply_nonlinear_pencil(T', λ, v)` as a derivative-pencil
  apply; the `A2'` divided-difference build (`palace/linalg/nleps.cpp:650-654`, `opA2p =
  (*funcA2)(|Im λ|·(1+δ))` then `opAJ = BuildParSumOperator({1/denom, -1/denom}, {opA2p, A2n})`) is
  the only new content. Whether that warrants a small `divided_difference_operator` L1 primitive or
  is just `T'`-construction is **already in the plan / OQ ledger** (`scaffolding/open-questions.md`
  line 461 — "Defer the decision to the harvest that needs it"). This theme lowers only the bare
  `{1, λ, λ², 1}` residual/system-operator apply; the `{0, 1, 2λ, 1}` Jacobian build is cited
  (`:655`) as the purpose/coefficient-vector variant-axis witness, not lowered here.
- **Integrator note:** `book/src/L1-L0/index.md` and `book/src/SUMMARY.md` are shared with the
  parallel `nleps_deflated_solve` L1>L0 abstractor this cycle. The dep-map row and SUMMARY entry
  proposed here are for `apply-nonlinear-pencil-mutation-rotation` only (distinct slug,
  non-overlapping row — inserted directly after the existing `nleps-deflated-residual-mutation-
  rotation` row in index.md, and after `lu-solve-mutation-rotation` at SUMMARY.md line 99). No
  overlap with the `nleps_deflated_solve` rows.
- **Lowering-verifier follow-up:** the standard `verified_against:` audit (per the sibling-theme
  convention, cf. `lu-solve-mutation-rotation` §Verified-against and the cycle-023 deflated-residual
  audit) confirming the five-site surface-form recognition is exhaustive is the standard next step,
  not a status reduction.
