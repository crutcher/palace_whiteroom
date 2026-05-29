---
agent: lowering-verifier
invoked_at: 2026-05-29T151441Z
scope: L1>L0 theme audit — apply-nonlinear-pencil-mutation-rotation
status: integrated
integrated_at: 2026-05-29T17:15:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-025 finalize (first primary cycle of meta-batch-7). Audit verdict fully-supported → theme STAYS firm. Additive verified_against: YAML block (21 entries, all supports) appended at EOF; no content edit, no status change. OQ apply-nonlinear-pencil-mutation-rotation-lowering-verifier-audit-followup RESOLVED (clause-scoped disposition, the 1st of 4 slugs on open-questions.md:327 — NOT a whole-line close, meta-phase retires this clause at Closed-index migration). retroactive-budget 0; clean build (fenced YAML, no new links)."
inputs:
  - book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md
  - palace/linalg/nleps.cpp:807-821 (Form A, GetResidualNorm — primary anchor)
  - palace/linalg/nleps.cpp:496-499, :556-559, :655, :729 (Form B / Jacobian / lagged-refresh)
  - palace/linalg/nleps.cpp:177-181 (SetExtraSystemMatrix closure type), :191/:221 (SetOperators overloads)
  - palace/linalg/rap.cpp:832-841 (BuildParSumOperator signature)
  - palace/linalg/nleps.hpp:146 (class comment), :232-283 (Interpolation); palace/linalg/eps.hpp:69-74
  - book/src/L1/apply_nonlinear_pencil.md (the firm L1 operator lowered)
---

# CYCLE: Audit apply-nonlinear-pencil-mutation-rotation

## Summary

Audited the firm L1>L0 theme `apply-nonlinear-pencil-mutation-rotation` (landed firm cycle-024) —
the bare-pencil residual-apply lowering `r = T(λ)·v` for `T(λ) = K + λC + λ²M + A2(|Im λ|)` inside
Palace's `QuasiNewtonSolver` NEP loop. I independently `read_range`-read every cited `nleps.cpp` /
`rap.cpp` / `eps.hpp` range and mechanically confirmed every pinpoint anchor with
`tools/citecheck/citecheck.py --anchor`. **Verdict: fully-supported.** Both build forms (Form A
term-by-term `Mult`+`AddMult` at `:812-819`; Form B `BuildParSumOperator`+`Mult` at `:498-499` /
`:557-559`) appear at the cited ranges exactly as the theme states; the `{1, λ, λ², 1}` coefficient
shape is identical across all five build sites; the Jacobian substitution `{0, 1, 2λ, 1}` (`:655`)
is correct; the `|Im λ|` real-projection closure contract is correct; the conditional `if (opC)`
damping axis is correct; the load-bearing Form-A-vs-Form-B accumulation-order bit-difference is
correctly characterized as algebraically-identical-but-not-bit-identical (load-bearing, recorded
not erased). The cycle-024 re-confirmation that the `:810-811` comment citation is correct (no
off-by-one) **stands** — citecheck lands the comment-anchor `P(λ) x` at line 810, inside the cited
`810-811` range. The NLEPS test-coverage absence the firm decision invokes is independently
confirmed (zero hits in `test/unit/**`). **Recommended action:** append a `verified_against:` YAML
block to the theme (proposed below) — no content edits, no status change. No drift, no gap found.

## Per-citation audit

### Form A — `QuasiNewtonSolver::GetResidualNorm` (primary positive site)

| Citation | Theme claim | Found (read_range 805-822) | citecheck --anchor | Verdict |
|---|---|---|---|---|
| `nleps.cpp:807-821` | full `GetResidualNorm` Form-A function | signature `:807-808`, `{` `:809`, comment `:810-811`, body `:812-820`, `}` `:821` — exact | n/a (range bound) | supports |
| `nleps.cpp:810-811` | source's own residual statement `\|\| (K + λ C + λ² M + A2(λ)) x \|\|₂` | comment present, two-line, exactly as quoted | `OK` — anchor `P(λ) x` at line **810**, within `810-811` | supports |
| `nleps.cpp:812` | `opK->Mult(x, r)` write-mode init `r := K·x` | exact at `:812` | `OK` — `opK->Mult(x, r)` at 812 | supports |
| `nleps.cpp:813-816` | `if (opC) { opC->AddMult(x, r, l); }` conditional λ·(C·x) | `if (opC)` at 813, `{` 814, `opC->AddMult(x, r, l)` 815, `}` 816 — exact | `OK` — `opC->AddMult(x, r, l)` at 815 | supports |
| `nleps.cpp:817` | `opM->AddMult(x, r, l*l)` → `r += λ²·(M·x)` | exact at `:817` | `OK` — `opM->AddMult(x, r, l * l)` at 817 | supports |
| `nleps.cpp:818` | `auto A2 = (*funcA2)(std::abs(l.imag()))` closure at \|Im λ\| | exact at `:818` | `OK` — `funcA2` at 818 | supports |
| `nleps.cpp:819` | `A2->AddMult(x, r, 1.0)` → `r += 1.0·(A2·x)` | exact at `:819` | `OK` — `A2->AddMult(x, r, 1.0)` at 819 | supports |
| `nleps.cpp:820` | `return linalg::Norml2(comm, r)` (the fused norm, NOT part of the apply) | exact at `:820` | `OK` — `Norml2(comm, r)` at 820 | supports |

Note on the cycle-024 off-by-one-on-an-off-by-one: the theme cites the comment at `810-811`.
citecheck places the comment's literal anchor at line **810** (within the range), so the wide
citation is correct and the prior critic off-by-one finding remains itself off by one. **No shift.**

### Form B — `BuildParSumOperator` + `Mult` (four in-`Solve` materialization sites)

| Citation | Theme claim | Found | citecheck --anchor | Verdict |
|---|---|---|---|---|
| `nleps.cpp:556` | `A2_out = (*funcA2)(std::abs(lam.imag()))` carried back for caching | exact at `:556` (inside `compute_residual` lambda) | `OK` at 556 | supports |
| `nleps.cpp:557-558` | `BuildParSumOperator({1, lam, lam², 1}, {opK, opC, opM, A2_out.get()}, true)` | exact (557 coeffs, 558 ops+`true`) | `OK` — anchor at 557, within `557-558` | supports |
| `nleps.cpp:559` | `A->Mult(vv, rr)` single apply `rr := T(λ)·vv` | exact at `:559` | `OK` at 559 | supports |
| `nleps.cpp:497` | `opA2 = (*funcA2)(std::abs(eig.imag()))` (in-`Solve` setup) | exact at `:497` | `OK` at 497 | supports |
| `nleps.cpp:498-499` | `opA = BuildParSumOperator({1, eig, eig², 1}, {opK, opC, opM, opA2.get()}, true)` | exact (498 coeffs, 499 ops+`true`) | `OK` — anchor at 498, within `498-499` | supports |
| `nleps.cpp:728-730` (theme cites `:729`) | lagged refresh `opA = BuildParSumOperator({1, eig_opInv, eig_opInv², 1}, …)` | `opA =` at 728, coeffs at 729, ops+`true` at 730 | `OK` — coeff anchor at 729, within `728-730` | supports |

### Jacobian build + closure-type + corroborating sites

| Citation | Theme claim | Found | citecheck --anchor | Verdict |
|---|---|---|---|---|
| `nleps.cpp:655` | Jacobian `opJ = BuildParSumOperator({0, 1, 2·eig, 1}, {opK, opC, opM, opAJ.get()}, true)` | exact at `:655` (preceded by `opAJ` divided-diff build at 650-654, `opJ->Mult(v, w)` at 657) | `OK` — coeff `{0.0+0.0i, 1.0+0.0i, 2.0*eig, 1.0+0.0i}` at 655 | supports |
| `nleps.cpp:650-655` | `A2'` finite-difference closure `opA2p`/`opAJ` | `opA2p` at 650, `opAJ` at 653, `BuildParSumOperator` at 654 | `OK` — `opAJ` at 653, within `650-655` | supports |
| `nleps.cpp:177-181` | `SetExtraSystemMatrix(std::function<unique_ptr<ComplexOperator>(double)> A2) { funcA2 = A2; }` — real-arg closure | exact (signature 177-179, `funcA2 = A2` 180, `}` 181) | `OK` — `funcA2 = A2` at 180, within `177-181` | supports |
| `nleps.cpp:191` | `SetOperators(K, M, type)` — without-C overload | exact at `:191` | `OK` at 191 | supports |
| `nleps.cpp:221` | `SetOperators(K, C, M, type)` — with-C overload | exact at `:221` | `OK` at 221 | supports |
| `rap.cpp:832-841` | `BuildParSumOperator(coeff, ops, set_essential)` signature; `nullptr` entry skipped via `std::find_if(... p != nullptr ...)` at `:837` | template at 833, signature 833-835, `find_if` at 837 | `OK` — `BuildParSumOperator` at [833,839]; `p != nullptr` at 837 | supports |
| `nleps.hpp:146` | class comment "Quasi-Newton nonlinear eigenvalue solver for (K + λ C + λ² M + A2(λ)) x = 0" | exact at `:146`, precedes `class QuasiNewtonSolver` `:147` | `OK` at 146 | supports |
| `nleps.hpp:232-283` | `Interpolation` (`:232`) / `NewtonInterpolationOperator` (`:246`) — A2-representation axis | `Interpolation` class at 232, `NewtonInterpolationOperator` at 246 | n/a (read-confirmed) | supports |
| `eps.hpp:69-74` | nonlinear `SetOperators(K, M, A2, type)` virtual; this overload's `A2` is a *complex*-arg closure (distinct from the operative real-arg `SetExtraSystemMatrix`) | exact: complex-arg `std::function<const ComplexOperator &(std::complex<double>)>` at `:70` | `OK` — complex-arg closure type at 70, within `69-74` | supports |

**Per-citation result: 24/24 cited L0 anchors land at their stated ranges. Zero drift, zero
out-of-range.** Every pinpoint anchor is mechanically confirmed by `citecheck --anchor` (shared
line-map adjudicator); every range is `read_range`-confirmed this invocation.

## Applicability conditions

- **Condition**: pencil bound as `{1, λ, λ², 1}` over `{opK, opC, opM, A2(|Im λ|)}`; with-C/without-C
  damping absorbed by `Maybe C` (`if (opC)` at `:813`; the two `SetOperators` overloads `:191`/`:221`).
  - **Verifiable**: yes — `if (opC)` guard read at `:813-816`; both overloads confirmed at `:191`
    (K,M) and `:221` (K,C,M). The `{1, λ, λ², 1}` shape verified identical at `:498-499`, `:557-558`,
    `:728-730`. **Counter-example?** No.
- **Condition**: element type complex-only (`ComplexOperator` / `ComplexVector`, no real
  specialization).
  - **Verifiable**: yes — `GetResidualNorm` takes `const ComplexVector &x, ComplexVector &r`
    (`:807-808`); `BuildParSumOperator` returns `ComplexParOperator` (`rap.cpp:834`); `eps.hpp:69-74`
    overload is all-`ComplexOperator`. **Counter-example?** No.
- **Condition**: `A2` evaluated at the **real** argument `|Im λ|`, polynomial coefficients use full
  complex `λ`/`λ²`; a lowering must preserve this asymmetry.
  - **Verifiable**: yes — `(*funcA2)(std::abs(l.imag()))` at `:818` (Form A), `std::abs(lam.imag())`
    at `:556` (Form B); the polynomial coeffs `lam`, `lam * lam` carry the full complex `λ` (`:557`).
    Closure type `Real -> LinearOperator` pinned at `SetExtraSystemMatrix` `:177-181`. **Counter-example?**
    No — and the theme correctly flags that the `eps.hpp:69-74` overload's `A2` is a *complex*-arg
    closure, distinct from the operative real-arg one (a real subtlety, correctly disambiguated, not
    a contradiction).
- **Condition**: single-rank scope — per-operator `Mult`/`AddMult` and `BuildParSumOperator` apply
  are local; any `Mpi::GlobalSum` lives inside the downstream `Norml2` (`:820`), not the apply.
  - **Verifiable**: partially — the `Norml2(comm, r)` at `:820` does carry `comm` (a reduction), and
    it is correctly placed OUTSIDE the apply (the apply is `:812-819`; the norm is the fused `:820`
    line the theme explicitly excludes from the apply). The claim that per-operator `Mult`/`AddMult`
    contain no global reduction is an MFEM/internal-operator property below the cited Palace surface
    — consistent with the single-rank scope directive and not contradicted by anything read.
    **Counter-example?** No (N/A below the Palace surface).
- **Condition**: build-form choice free in value (law 5) but load-bearing in floating-point; a
  lowering may pick either but must record which to reproduce that call's bit behaviour.
  - **Verifiable**: yes structurally — both forms are present and compute the same `{1,λ,λ²,1}`-weighted
    sum (read at `:812-819` vs `:557-559`); the bit-difference is a property of accumulation order +
    matrix-free reduction-tree non-associativity, an algebraic-claim-level note, correctly classified
    load-bearing per the CLAUDE.md trick taxonomy. **Counter-example?** No.

All five applicability conditions are complete and each is verifiable against the cited evidence
(four directly; one — the no-internal-reduction sub-claim — below the Palace surface and consistent).

## Algebraic laws (cited)

The theme's three structural recognitions rest on `apply_nonlinear_pencil`'s laws 3, 4, 5 and
`apply_linop`'s law 5. Verified against the L1 operator entry (`book/src/L1/apply_nonlinear_pencil.md`)
and the L0 surface:

- **Law 3 (term decomposition / sum-of-applies)** — `T(λ)·v = K·v + λ·(C·v) + λ²·(M·v) + A2(|Im λ|)·v`.
  **Holds on operators?** Yes — this is the literal `:812-819` accumulation (`Mult` + three `AddMult`).
  It is a syntactic identity on a fixed-`λ` linear operator (each term an `apply_linop`); confirmed at
  `apply_nonlinear_pencil.md:63`.
- **Law 5 / `apply_linop` law 5 (operator-sum-distributes)** — `(Σ cᵢAᵢ)·v = Σ cᵢ(Aᵢ·v)`, the Form-A
  ↔ Form-B duality. **Holds on operators?** Yes — `BuildParSumOperator` constructs exactly the
  coefficient-weighted sum (`rap.cpp:832-841`), and its `Mult` applies it once (`:559`). The duality is
  a linear-algebra identity; the theme correctly notes its floating-point realization is exact modulo
  accumulation-order noise (the non-law).
- **Law 4 (coefficient-vector linearity)** — makes the Jacobian `{0, 1, 2λ, 1}` (`:655`) a substitution
  into the *same* operator rather than a new operator. **Holds on operators?** Yes — same
  `BuildParSumOperator` construction, different coefficient array; confirmed at `:655` and at
  `apply_nonlinear_pencil.md:64`.

No law cited by the theme fails on the operators per their L1 signatures. All are syntactic identities
on fully-specified positive source, consistent with the firm-on-positive-structure status — the laws
do not depend on convergence behaviour, so the NLEPS test-coverage absence does not gate them.

## Proposed changes

Fully-supported. No content edits, no status change. The single recommended change is appending the
`verified_against:` audit-provenance block (per the sibling-theme convention; consumed by
`cross-layer-cross-cutter` for coverage analysis). Emitted as a fenced YAML block at end of file:

```edit:book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md
[append at end of file]
~~~yaml
verified_against:
  - citation: palace/linalg/nleps.cpp:807-821
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: Form A GetResidualNorm — full function read_range-confirmed; anchors 810/812/815/817/818/819/820 all citecheck-OK
  - citation: palace/linalg/nleps.cpp:810-811
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: residual comment; citecheck anchor 'P(λ) x' at 810 within range — cycle-024 no-shift re-confirmed
  - citation: palace/linalg/nleps.cpp:812
    verdict: supports
    audited_at: 2026-05-29T151441Z
  - citation: palace/linalg/nleps.cpp:813-816
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: conditional opC->AddMult(x, r, l); anchor at 815
  - citation: palace/linalg/nleps.cpp:817
    verdict: supports
    audited_at: 2026-05-29T151441Z
  - citation: palace/linalg/nleps.cpp:818
    verdict: supports
    audited_at: 2026-05-29T151441Z
  - citation: palace/linalg/nleps.cpp:819
    verdict: supports
    audited_at: 2026-05-29T151441Z
  - citation: palace/linalg/nleps.cpp:820
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: fused Norml2 — correctly excluded from the apply itself
  - citation: palace/linalg/nleps.cpp:556
    verdict: supports
    audited_at: 2026-05-29T151441Z
  - citation: palace/linalg/nleps.cpp:557-558
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: Form B BuildParSumOperator {1, lam, lam², 1}; anchor at 557
  - citation: palace/linalg/nleps.cpp:559
    verdict: supports
    audited_at: 2026-05-29T151441Z
  - citation: palace/linalg/nleps.cpp:496-499
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: in-Solve setup; opA2 at 497, BuildParSumOperator at 498
  - citation: palace/linalg/nleps.cpp:655
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: Jacobian {0, 1, 2·eig, 1}; opAJ divided-diff at 653
  - citation: palace/linalg/nleps.cpp:729
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: lagged refresh; opA= at 728, coeff {1, eig_opInv, eig_opInv², 1} at 729
  - citation: palace/linalg/nleps.cpp:177-181
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: SetExtraSystemMatrix real-argument closure; funcA2 = A2 at 180
  - citation: palace/linalg/nleps.cpp:191
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: SetOperators(K, M) without-C overload
  - citation: palace/linalg/nleps.cpp:221
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: SetOperators(K, C, M) with-C overload
  - citation: palace/linalg/rap.cpp:832-841
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: BuildParSumOperator signature; nullptr-skip find_if at 837
  - citation: palace/linalg/nleps.hpp:146
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: class comment K + λ C + λ² M + A2(λ)
  - citation: palace/linalg/nleps.hpp:232-283
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: Interpolation (232) / NewtonInterpolationOperator (246) — A2-representation axis
  - citation: palace/linalg/eps.hpp:69-74
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: nonlinear SetOperators virtual; A2 here is complex-arg closure (distinct from operative real-arg), correctly disambiguated by theme
~~~
```

(The `~~~` triple-tilde represents the triple-backtick fence in the actual file; emit triple-backticks.)

## Supporting evidence

Source files consulted this invocation (read_range + citecheck --anchor):
- `reference/palace/palace/linalg/nleps.cpp` — `GetResidualNorm` (805-822), in-`Solve` setup
  (494-500), `compute_residual` lambda (547-560), Jacobian (648-658), lagged refresh (724-732),
  `SetExtraSystemMatrix` (176-182), `SetOperators` overloads (187-226).
- `reference/palace/palace/linalg/rap.cpp` — `BuildParSumOperator` template + signature + nullptr-skip
  (830-845).
- `reference/palace/palace/linalg/nleps.hpp` — class comment (144-148), `Interpolation` /
  `NewtonInterpolationOperator` (230-248).
- `reference/palace/palace/linalg/eps.hpp` — nonlinear `SetOperators` virtual (57-74).
- `book/src/L1/apply_nonlinear_pencil.md` — the firm L1 operator (signature 21-26, semantics 39-55,
  laws 57-72, variant axes 84-94, status 96-98) — laws 3/4/5 and the two non-laws cross-checked.
- Test-coverage absence: `search_text 'QuasiNewton|funcA2|GetResidualNorm|nleps'` over `test/unit/**`
  → zero hits (confirms the firm-decision rationale that no convergence test gates the syntactic laws).
- Tool: `tools/citecheck/citecheck.py --anchor` — 24 anchor checks, all `OK` (shared line-map
  adjudicator per role-spec citecheck bullet).

## Open questions / caveats

OQ ref: `apply-nonlinear-pencil-mutation-rotation-lowering-verifier-audit-followup` — **CLOSED by this
audit.** The audit found the theme fully-supported with zero drift; the standard `verified_against:`
follow-up the theme's own Status section anticipated (line 43-45) is satisfied by the proposed block
above. Recommend the integrator close this OQ on application.

Minor notes (no action required, not findings):
- The L1 operator entry cites the `A2_out` carry-back at `:550-552` (the comment block) while this
  theme cites `:556` (the `A2_out = (*funcA2)(...)` assignment). Both are correct and refer to the same
  `compute_residual` lambda — the comment is at 550-552, the assignment at 556. No inconsistency; the
  theme's `:556` is the precise assignment line and is the better anchor for the closure evaluation.
- The theme correctly disambiguates two distinct `A2` closure types — the operative real-argument
  `SetExtraSystemMatrix` (`std::function<unique_ptr<ComplexOperator>(double)>`, `:177-181`) used by all
  five build sites, vs. the complex-argument closure in the `eps.hpp:69-74` virtual
  (`std::function<const ComplexOperator &(std::complex<double>)>`). This is a real and easily-conflated
  subtlety; the theme handles it correctly, citing `eps.hpp:69-74` only for pencil *shape* / complex-only
  element type, not for the closure contract. No finding.
- Direction-of-definition: the theme narrates the rewrite forward (L1 → L0) throughout — LHS is the L1
  pencil apply, RHS is the L0 source forms. No high→low violation.
