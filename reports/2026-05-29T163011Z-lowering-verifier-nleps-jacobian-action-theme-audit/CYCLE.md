---
agent: lowering-verifier
invoked_at: 2026-05-29T16:47:29Z
scope: L1>L0 theme audit — nleps-jacobian-action-mutation-rotation
status: pending
inputs:
  - book/src/L1-L0/nleps-jacobian-action-mutation-rotation.md
  - palace/linalg/nleps.cpp:649-669 (the `w = J * v` block — the positive L0 site)
  - palace/linalg/nleps.cpp:329-347 (MatVecMult body), :412 (delta), :378 (w decl), :606-619 (deflation-basis growth), :673-676 (consumer)
  - book/src/L1/nleps_jacobian_action.md (the firm L1 operator the theme lowers)
integrated_at: 2026-05-29T203000Z
integration_commit: 1de17ed
integration_notes: "Applied clean (cycle-026 dispatch-6a). Additive verified_against: YAML block (24 entries, all verdict:supports) appended at EOF; theme stays firm, ZERO content/status change. Audit-followup OQ DISCHARGED; the re-confirmed L1-entry +1 drift was resolved same-cycle by D1's lifter re-anchor. Zero gate hits."

# CYCLE: Audit nleps-jacobian-action-mutation-rotation

## Summary

Audited the firm L1>L0 theme `nleps-jacobian-action-mutation-rotation` (authored firm cycle-025,
previously unaudited) against concrete L0 evidence in `palace/linalg/nleps.cpp`. The theme lowers
the per-step quasi-Newton `T'(λ)`-derivative-pencil Jacobian action (`w = J·v`) into the
`nleps.cpp:649-669` straight-line block, in three sub-patterns: A (divided-difference derivative
pencil `T'` build + big-space `opJ->Mult` apply), B (double `S⁻¹` back-projection materializing
`X·S⁻²·v₂`), C (two `AddMult` accumulations on the derivative pencil `opJ` and the value pencil
`A`). **Verdict: fully-supported.** Every one of the theme's 19 per-line L0 citations was
mechanically confirmed via `tools/citecheck/citecheck.py --anchor` against the on-disk
`reference/palace/` checkout — zero drift, zero out-of-range. The load-bearing semantic claims
(the divided-difference `A2'` non-law, the product-rule `∂_λ S⁻¹ = −S⁻²` double-solve, the
two-distinct-pencil `AddMult` product rule, the big-space-only output contract) are all confirmed
by reading the source. The theme was authored with the corrected on-disk numbers (`S`=664,
`Sv2`=665, `XSv2`=666, `XSSv2`=667), and those numbers are correct. **One carry-forward finding,
NOT in this theme:** the L1 ENTRY `book/src/L1/nleps_jacobian_action.md` still carries the
codemap `+1` drift on its deflation-block pinpoints (`:664`/`:666`/`:663`/`:659-660`/`:661-662`) —
this is dispatch-1's (lifter's) re-anchor scope this cycle, recorded here as confirmation and a
carry-forward cross-check, not a defect of the theme under audit.

Recommendation: append the additive `verified_against:` YAML block (below) to the theme. No content
edits to the theme are warranted — it is correct as authored.

## Per-citation audit

The theme cites `palace/linalg/nleps.cpp:649-669` as the enclosing L0 site, with per-line pinpoints.
Each was confirmed via `citecheck --anchor` (literal-substring anchor; lines are on-disk ground
truth). The block was also read in full (`nleps.cpp:645-684`) and matches the theme's L0-form
transcription verbatim.

- **Citation**: `nleps.cpp:649`
  - **Theme claim**: `// Compute w = J * v.` — the source's own naming of the operator.
  - **Found**: `// Compute w = J * v.` at line 649. citecheck `--anchor 'Compute w = J'` → line 649, in range.
  - **Verdict**: supports.

- **Citation**: `nleps.cpp:650`
  - **Theme claim**: `auto opA2p = (*funcA2)(std::abs(eig.imag()) * (1.0 + delta));` — bumped-frequency `A2((1+δ)|Im λ|)`.
  - **Found**: exact match at line 650. citecheck `--anchor 'funcA2'` → line 650.
  - **Verdict**: supports.

- **Citation**: `nleps.cpp:651-652`
  - **Theme claim**: `const std::complex<double> denom = std::complex<double>(0.0, delta * std::abs(eig.imag()));` — denominator `i·δ·|Im λ|`.
  - **Found**: exact match (651 declares, 652 initializes). citecheck `--anchor 'denom'` → line 651, in range.
  - **Verdict**: supports.

- **Citation**: `nleps.cpp:653-654`
  - **Theme claim**: `BuildParSumOperator({1.0 / denom, -1.0 / denom}, {opA2p.get(), A2n.get()}, true)` — the divided-difference `A2'(λ)` (quasi-Newton non-law).
  - **Found**: exact match (653 `std::unique_ptr<ComplexOperator> opAJ =`, 654 the `BuildParSumOperator`). citecheck `--anchor '1.0 / denom, -1.0 / denom'` → line 654, in range.
  - **Verdict**: supports.

- **Citation**: `nleps.cpp:655-656`
  - **Theme claim**: `BuildParSumOperator({0.0+0.0i, 1.0+0.0i, 2.0*eig, 1.0+0.0i}, {opK, opC, opM, opAJ.get()}, true)` — derivative pencil `T'(λ)`, coeffs `{0, 1, 2λ, 1}`.
  - **Found**: exact match. citecheck `--anchor '2.0 * eig'` → line 655, in range.
  - **Verdict**: supports. The coefficient vector `{0, 1, 2λ, 1}` is the literal C++ `{0.0+0.0i, 1.0+0.0i, 2.0*eig, 1.0+0.0i}` over `{opK, opC, opM, opAJ}` — `K` weight 0, `C` weight 1, `M` weight `2λ`, `A2'` weight 1.

- **Citation**: `nleps.cpp:657`
  - **Theme claim**: `opJ->Mult(v, w);` — big-space apply `w := T'(λ)·v`.
  - **Found**: exact match. citecheck `--anchor 'opJ->Mult(v, w)'` → line 657.
  - **Verdict**: supports.

- **Citation**: `nleps.cpp:658`
  - **Theme claim**: `if (k > 0)` — deflation-present guard; when `k = 0`, only `:650-657` run (bare derivative-pencil apply, law 1 reduction).
  - **Found**: `if (k > 0)  // Deflation` at line 658. citecheck `--anchor 'k > 0'` → line 658.
  - **Verdict**: supports.

- **Citation**: `nleps.cpp:660-661`
  - **Theme claim**: source comment `w1 = T'(l) v1 + U'(l) v2 = T'(l) v1 + T'(l)XS v2 - T(l)XS^2 v2` (the source's own product-rule decomposition) + scoping note.
  - **Found**: line 660 `// w1 = T'(l) v1 + U'(l) v2 = T'(l) v1 + T'(l)XS v2 - T(l)XS^2 v2. Scoping T(l)`, line 661 `// here lets the line search overwrite A2n freely; with no deflation we skip it.` citecheck `--anchor "w1 = T'(l) v1"` → line 660, in range. **Both the product-rule comment AND the scoping note the theme paraphrases are present at exactly `:660-661`.**
  - **Verdict**: supports.

- **Citation**: `nleps.cpp:662-663`
  - **Theme claim**: `auto A = BuildParSumOperator({1.0+0.0i, eig, eig*eig, 1.0+0.0i}, {opK, opC, opM, A2n.get()}, true);` — re-scoped value pencil `T(λ)`, coeffs `{1, λ, λ², 1}`, reusing cached `A2n`.
  - **Found**: exact match (662 the `BuildParSumOperator({1.0+0.0i, eig, eig*eig, 1.0+0.0i}`, 663 the operand list). citecheck `--anchor 'eig * eig'` → line 662, in range.
  - **Verdict**: supports. The value pencil is built ONLY inside the `k > 0` branch (it is the second product-rule term's operator) — the re-scoping claim is correct.

- **Citation**: `nleps.cpp:664`
  - **Theme claim**: `const Eigen::MatrixXcd S = eig * Eigen::MatrixXcd::Identity(k, k) - H;` — block `S = λI − H` (λ = current `eig`).
  - **Found**: exact match. citecheck `--anchor 'Identity(k, k) - H'` → line 664.
  - **Verdict**: supports. (This is the load-bearing `+1`-drift line cycle-025 flagged from codemap; the theme's on-disk `664` is correct — codemap was `663`.)

- **Citation**: `nleps.cpp:665`
  - **Theme claim**: `const Eigen::VectorXcd Sv2 = S.fullPivLu().solve(v2);` — first dense solve `S⁻¹·v₂` (`lu_solve`, fresh destination).
  - **Found**: exact match. citecheck `--anchor 'S.fullPivLu().solve(v2)'` → line 665.
  - **Verdict**: supports.

- **Citation**: `nleps.cpp:666`
  - **Theme claim**: `const ComplexVector XSv2 = MatVecMult(X, Sv2);` — back-projection `X·(S⁻¹·v₂)`.
  - **Found**: exact match. citecheck `--anchor 'MatVecMult(X, Sv2)'` → line 666.
  - **Verdict**: supports.

- **Citation**: `nleps.cpp:667`
  - **Theme claim**: `const ComplexVector XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2));` — second sequential solve + back-projection `X·S⁻²·v₂` (the `S⁻¹`-applied-twice signature).
  - **Found**: exact match. citecheck `--anchor 'S.fullPivLu().solve(Sv2)'` → line 667. The argument `Sv2` (the result of the `:665` solve) is fed back through `S.fullPivLu().solve` — confirming the double-sequential-solve structure the theme's Sub-pattern B turns on.
  - **Verdict**: supports.

- **Citation**: `nleps.cpp:668`
  - **Theme claim**: `opJ->AddMult(XSv2, w, 1.0);` — accumulates `+T'(λ)·X·S⁻¹·v₂` (product-rule first term; derivative pencil `opJ`, scale `+1`).
  - **Found**: exact match. citecheck `--anchor 'opJ->AddMult(XSv2, w, 1.0)'` → line 668.
  - **Verdict**: supports. The operator is `opJ` (the derivative pencil built at `:655-656`), confirming the `+` term uses `T'`.

- **Citation**: `nleps.cpp:669`
  - **Theme claim**: `A->AddMult(XSSv2, w, -1.0);` — accumulates `−T(λ)·X·S⁻²·v₂` (product-rule second term; value pencil `A`, scale `−1`).
  - **Found**: exact match. citecheck `--anchor 'A->AddMult(XSSv2, w, -1.0)'` → line 669.
  - **Verdict**: supports. The operator is `A` (the value pencil built at `:662-663`), scale `−1.0` — confirming the `−` term uses `T` and carries the `∂_λ S⁻¹ = −S⁻²` sign. **The two `AddMult`s use two distinct operators — the algebraic content of the product rule, read straight off the source.**

- **Citation**: `nleps.cpp:412` (with `:411` comment)
  - **Theme claim**: `const auto delta = std::sqrt(std::numeric_limits<double>::epsilon())` — the `δ = √ε` divided-difference step (the non-law's accuracy trade-off).
  - **Found**: line 412 exact match; line 411 `// Delta used in to compute divided difference Jacobian.` citecheck `--anchor 'std::sqrt'` → 412; `--anchor 'divided difference'` on `:411-412` → 411.
  - **Verdict**: supports. The `:411` comment independently confirms the divided-difference-Jacobian purpose the theme attributes to `δ`.

- **Citation**: `nleps.cpp:378`
  - **Theme claim**: `ComplexVector v, u, w, c, w0, z, du, v_trial;` — the `w` destination-buffer declaration.
  - **Found**: exact match (the line declares `w` among the reused scratch `ComplexVector`s). citecheck `--anchor 'w, c, w0'` → line 378.
  - **Verdict**: supports.

- **Citation**: `nleps.cpp:329-347`
  - **Theme claim**: `MatVecMult(X, y)` body — `z = 0`; per-`j` complex AXPY via two `linalg::AXPBYPCZ` on the real/imag carriers.
  - **Found**: read in full — `:340` `z = 0.0`, `:341-345` the `for (int j…)` loop with two `AXPBYPCZ` calls (`:343` real/imag mix into `z.Real()`, `:344` into `z.Imag()`). citecheck `--anchor 'MatVecMult'` → 329.
  - **Verdict**: supports. The four-real-multiply complex-product expansion across `.Real()`/`.Imag()` carriers is exactly as the theme describes.

- **Citation**: `nleps.cpp:606-619`
  - **Theme claim**: deflation-basis growth — normalize at `:610-611`, store `X[k] = v` at `:615`, no orthogonalization (the `X`-not-orthonormal fact).
  - **Found**: `:610` `const auto scale = linalg::Norml2(GetComm(), v);`, `:611` `v *= 1.0 / scale;`, `:615` `X[k] = v;` — no Gram-Schmidt / re-orthogonalization between columns. citecheck `--anchor 'X[k] = v'` → 615, in range.
  - **Verdict**: supports. (My first NOANC on `'1.0 / linalg::Norml2'` was a wrong-anchor guess on my part — the code splits it as `scale = Norml2(...)` then `v *= 1.0/scale`; the theme's claim is correct, confirmed by reading.)

- **Citation**: `nleps.cpp:673` / `:675` / `:676` (consumer — big-space-only confirmation)
  - **Theme claim**: `w` enters the Newton correction only through the big-space dot `⟨w, w0⟩` (`:675`) and the step `z = −delta_eig·w − u` (`:676`); the `w2.adjoint()*u2` at `:673` is the deflated-solve output, not a coordinate part of `J·v`.
  - **Found**: `:673` `const std::complex<double> u2_w0 = std::complex<double>(w2.adjoint() * u2);`, `:675` `-(linalg::Dot(GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0)`, `:676` `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0);`. citecheck `--anchor`s → 673, 675, 676. `w` is consumed only as a big-space vector (in `Dot(comm, w, w0)` and `AXPBYPCZ(…, w, …)`); no `w2` is computed at the Jacobian site.
  - **Verdict**: supports. The big-space-only contract (theme §"The big-space-only output") is confirmed at the consumer.

- **Citation**: `nleps.cpp:177-181`
  - **Theme claim**: `QuasiNewtonSolver::SetExtraSystemMatrix(...)` — the nonlinear closure type `Real -> ComplexOperator` (the `A2` evaluated at `|Im λ|` and `(1+δ)|Im λ|`).
  - **Found**: citecheck `--anchor 'SetExtraSystemMatrix'` → line 177, in range. (Confirms the `funcA2` closure provenance; consistent with the `(*funcA2)(…)` call at `:650`.)
  - **Verdict**: supports.

## Applicability conditions

The theme states six applicability conditions (§"Applicability conditions"). Each walked through:

- **Condition 1**: T(λ) and T'(λ) bound exactly as for solver setup (`T'` over `{0,1,2λ,1}` w/ `A2'`, `T` over `{1,λ,λ²,1}` w/ cached `A2n`); with-C/without-C absorbed by pencils.
  - **Verifiable**: Yes — `:655-656` (`T'`) and `:662-663` (`T`) read exactly as stated; the coefficient vectors are the literal C++ braces. The with-C/without-C absorption is inherited from `apply_nonlinear_pencil`'s damping axis (cross-referenced, firm).
  - **Found counter-example?**: No.

- **Condition 2**: Element type is complex-only (`ComplexVector` / `Eigen::VectorXcd` / `Eigen::MatrixXcd`).
  - **Verifiable**: Yes — every carrier at the site is a complex type (`:664` `Eigen::MatrixXcd`, `:665` `Eigen::VectorXcd`, `:666-667` `ComplexVector`, `w` `ComplexVector` at `:378`). No real specialization witnessed.
  - **Found counter-example?**: No.

- **Condition 3**: Deflation cardinality `k` is variadic (grows by one per converged eigenpair `:606-619`); `k = 0` branch (the `:658` guard) is the un-deflated degeneration.
  - **Verifiable**: Yes — `:619` `k++` after `X.resize(k+1)`/`X[k]=v` confirms variadic growth; `:658` `if (k > 0)` is the guard.
  - **Found counter-example?**: No.

- **Condition 4**: In-place destination overwrite permitted because `w` is dead-on-entry scratch (`:378` decl, overwritten `:657`, accumulated `:668-669`).
  - **Verifiable**: Yes — `w` declared at `:378`, fully overwritten by `opJ->Mult(v, w)` (`:657`, a Mult not an AddMult — no prior contents read), then accumulated. The comment at `:375-377` documents the scratch reuse of the buffer set. Dead-on-entry holds (Mult overwrites).
  - **Found counter-example?**: No.

- **Condition 5**: `δ = √ε` is a fixed solver-level constant (`:412`), not a structural variant (the load-bearing non-law); `A2n` caching and value-pencil re-scoping are transparent L1>L0 concerns.
  - **Verifiable**: Yes — `:412` is a single `const auto delta` computed once at solver setup (above the iteration loop), not recomputed per-step; the `:411` comment confirms its role.
  - **Found counter-example?**: No.

- **Condition 6**: Single-rank scope; big-space `Mult`/`AddMult` inherit the bit-deterministic-reduction trade-off; the `k×k` dense Eigen solves (`:665`,`:667`) are rank-local (coordinate space replicated on all ranks).
  - **Verifiable**: Partially — the single-rank scope is the project-wide CLAUDE.md scope rule (flagged, not re-derived). The `Eigen::MatrixXcd`/`VectorXcd` dense solves are inherently rank-local (small dense, no comm); the big-space `Mult`/`AddMult` route through `linalg::AXPBYPCZ`-style ops that carry the reduction-order trade-off (inherited from `apply_linop`, firm). No comm appears in the `:649-669` block except inside the (opaque, single-rank-collapsed) operator applies.
  - **Found counter-example?**: No.

The conditions are **complete** for the witnessed cases. The theme does not claim a real-valued
or distributed specialization; both are correctly excluded (complex-only, single-rank).

## Algebraic laws (cited)

The theme is `justification: structural` (with two load-bearing non-laws). It cites the L1 entry's
laws and `apply_nonlinear_pencil`'s laws as the algebraic backbone. Checked against operator
signatures:

- **Law (entry law 1) — deflation reduction `k = 0`**: `nleps_jacobian_action` with empty deflation
  = `apply_nonlinear_pencil(T', λ, v)` (bare derivative-pencil apply).
  - **Holds on operators?**: Yes. The `:658` `if (k > 0)` guard is false at `k = 0`, so only
    `:650-657` execute, leaving `w = opJ->Mult(v) = T'(λ)·v`. This is exactly
    `apply_nonlinear_pencil(T', λ, v)`. The signature of `apply_nonlinear_pencil` (firm cycle-021)
    accepts the derivative pencil `T'` as a `NonlinearPencil`. Holds.

- **Law (entry law 3 / `apply_nonlinear_pencil` law 3) — term decomposition of `T'·v`**:
  `apply_nonlinear_pencil(T', λ, v) = apply_linop(C,v)·1 + apply_linop(M,v)·2λ + apply_linop(A2'(λ),v)`
  (the `{0,1,2λ,1}` vector drops `K`).
  - **Holds on operators?**: Yes. The coefficient vector `{0, 1, 2λ, 1}` over `{K, C, M, A2'}`
    zeroes the `K` slot, so `K` drops; the remaining three terms are `apply_linop` of `C`, `M`, `A2'`
    weighted `1`, `2λ`, `1`. This is `apply_nonlinear_pencil`'s firm term-decomposition law applied
    to the derivative coefficient vector. Holds.

- **Law (entry law 4 / Semantics point 2) — deflation-coupling product rule**:
  `U'(λ)·v₂ = T'(λ)·X·S⁻¹·v₂ − T(λ)·X·S⁻²·v₂`, with `∂_λ S⁻¹ = −S⁻¹·(∂_λ S)·S⁻¹ = −S⁻²` since
  `∂_λ S = ∂_λ(λI − H) = I`.
  - **Holds on operators?**: Yes. The derivation is exact (product rule on `U(λ) = T(λ)·X·S⁻¹`;
    `S = λI − H` ⟹ `∂_λ S = I` ⟹ `∂_λ S⁻¹ = −S⁻²`). The L0 realizes it as `opJ->AddMult(XSv2, w, +1)`
    (`:668`, `T'` pencil) and `A->AddMult(XSSv2, w, −1)` (`:669`, `T` pencil), with `XSSv2 = X·S⁻²·v₂`
    materialized by the double sequential solve (`:665`→`:667`). The two-distinct-pencil structure
    (`opJ` for the differentiated `T'` term, `A` for the un-differentiated `T` term) is the algebraic
    content of the product rule, read straight off the source. **Holds — this is the central law and
    it is correctly characterized.**

- **Law (entry law 2) — linearity in the extended direction `(v, v₂)` at fixed `(T, λ, P)`**.
  - **Holds on operators?**: Yes. Each step is a fixed linear map at fixed `λ`:
    `apply_nonlinear_pencil(T'/T, λ, ·)` is the fixed linear operator (firm law 1, linearity-in-`v`),
    `lu_solve(S, ·)` is the fixed linear `S⁻¹` (firm `lu_solve` law 2), `linear_combination(X, ·)` is
    linear. The composite is the action of the fixed Jacobian operator. Holds. (The theme does not
    over-claim linearity/polynomiality *in `λ`* — the entry's "Laws that do not hold" correctly
    excludes that; the theme inherits the exclusion.)

**Non-law 1 — divided-difference `A2'` ≠ exact `∂_λ A2`** (Sub-pattern A; the quasi-Newton
approximate Jacobian).
  - **Correctly characterized?**: Yes. `A2'(λ) = (A2((1+δ)|Im λ|) − A2(|Im λ|)) / (i·δ·|Im λ|)`,
    `δ = √ε` is a one-sided divided difference, NOT the analytic derivative. The theme records it as
    an explicit non-law (not asserted as a tight identity) and ties the `O(δ)` truncation /
    `O(ε/δ)` roundoff balance at `δ = √ε` to the CLAUDE.md load-bearing-numerical-trick taxonomy.
    The `i` in the denominator (frequency `|Im λ|` is the imaginary part of `λ`, so a frequency bump
    is an `i·δ·|Im λ|` bump in `λ`) is correctly explained. The `:411` source comment ("Delta used in
    to compute divided difference Jacobian") independently confirms the intent. **The non-law is
    correctly characterized — this was the load-bearing point flagged in the audit scope, and it is
    sound.** Recording it as a non-law (rather than a tight identity) is exactly why the theme does
    not need a test to be firm.

**Non-law 2 — big-space accumulation is not bit-identical to a single combined apply** (Sub-pattern
C accumulation-order note).
  - **Correctly characterized?**: Yes. The three-step `Mult`(`:657`) + `AddMult`(`:668`) +
    `AddMult`(`:669`) orders FP additions differently from an algebraically-equal single apply; the
    matrix-free `A2'`/`A2` terms inherit reduction-tree non-associativity from `apply_linop`. The
    law identities are mathematical, the FP realization exact-modulo-accumulation-order. Recorded
    (not erased) per the trick taxonomy, consistent with the entry's `:103` non-law.

## Proposed changes

The theme is fully-supported as authored — **no content edits are warranted**. The only proposed
change is the additive `verified_against:` metadata block (consumed by `cross-layer-cross-cutter`
for coverage analysis), appended at end of file. Emitted as a fenced YAML code block per the
channel-format requirement.

```edit:book/src/L1-L0/nleps-jacobian-action-mutation-rotation.md
[append at end of file]
    ```yaml
    verified_against:
      - citation: palace/linalg/nleps.cpp:649-669
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: complete `w = J * v` block; full read + per-line citecheck --anchor, zero drift
      - citation: palace/linalg/nleps.cpp:649
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: "// Compute w = J * v. — source's own operator naming"
      - citation: palace/linalg/nleps.cpp:650
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: opA2p bumped-frequency A2((1+δ)|Im λ|)
      - citation: palace/linalg/nleps.cpp:651-652
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: denom = i·δ·|Im λ|
      - citation: palace/linalg/nleps.cpp:653-654
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: divided-difference A2'(λ) (quasi-Newton non-law); anchor at 654
      - citation: palace/linalg/nleps.cpp:655-656
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: derivative pencil T'(λ) coeffs {0, 1, 2λ, 1}; anchor at 655
      - citation: palace/linalg/nleps.cpp:657
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: opJ->Mult(v, w) big-space apply w := T'(λ)·v
      - citation: palace/linalg/nleps.cpp:658
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: if (k > 0) deflation guard; k=0 is the bare derivative-pencil apply
      - citation: palace/linalg/nleps.cpp:660-661
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: source product-rule comment + scoping note (both present at this range)
      - citation: palace/linalg/nleps.cpp:662-663
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: re-scoped value pencil T(λ) coeffs {1, λ, λ², 1} reusing cached A2n; anchor at 662
      - citation: palace/linalg/nleps.cpp:664
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: block S = λI − H (on-disk truth; codemap was 663, +1 drift)
      - citation: palace/linalg/nleps.cpp:665
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: first dense solve S⁻¹·v₂ (lu_solve, fresh destination)
      - citation: palace/linalg/nleps.cpp:666
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: back-projection X·(S⁻¹·v₂) (MatVecMult / linear_combination)
      - citation: palace/linalg/nleps.cpp:667
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: second sequential solve + back-projection X·S⁻²·v₂ (the S⁻¹-applied-twice signature)
      - citation: palace/linalg/nleps.cpp:668
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: opJ->AddMult(XSv2, w, 1.0) +T'(λ)·X·S⁻¹·v₂ (derivative pencil, +1)
      - citation: palace/linalg/nleps.cpp:669
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: A->AddMult(XSSv2, w, -1.0) −T(λ)·X·S⁻²·v₂ (value pencil, −1; the ∂_λ S⁻¹ = −S⁻² sign)
      - citation: palace/linalg/nleps.cpp:412
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: δ = √ε divided-difference step (:411 comment confirms intent)
      - citation: palace/linalg/nleps.cpp:378
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: w destination-buffer declaration (dead-on-entry scratch)
      - citation: palace/linalg/nleps.cpp:329-347
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: MatVecMult(X, y) fold body (z=0; per-j complex AXPY via two AXPBYPCZ)
      - citation: palace/linalg/nleps.cpp:606-619
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: deflation-basis growth (normalize :610-611, store X[k]=v :615, no orthogonalization)
      - citation: palace/linalg/nleps.cpp:673
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: w2.adjoint()*u2 is the deflated-solve output, not a coordinate part of J·v
      - citation: palace/linalg/nleps.cpp:675
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: w consumed only via big-space dot ⟨w, w0⟩ (big-space-only confirmation)
      - citation: palace/linalg/nleps.cpp:676
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: z = −delta_eig·w − u Newton step direction (second consumer of w, big-space)
      - citation: palace/linalg/nleps.cpp:177-181
        verdict: supports
        audited_at: 2026-05-29T16:47:29Z
        note: SetExtraSystemMatrix — nonlinear closure type Real -> ComplexOperator (funcA2 provenance)
    ```
```

(The inner `verified_against:` block is rendered 4-space-indented inside the `edit:`
proposed-changes block — per the `convert-nested-fences-to-indented-code-in-proposed-changes-block`
skill, option (b) — so the inner ```` ```yaml ```` fence is captured as literal content rather than
mis-toggling the outer `edit:` block. The integrator strips the 4-space indent on apply and appends
the resulting ```` ```yaml ```` fenced block at end-of-file, after the existing
`## Verified-against` prose section.)

## Supporting evidence

- `reference/palace/palace/linalg/nleps.cpp:645-684` — read in full; the `w = J * v` block
  (`:649-669`) matches the theme's L0-form transcription verbatim, including the source comments at
  `:649`, `:660-661`.
- `reference/palace/palace/linalg/nleps.cpp:329-347` — `MatVecMult` body, read in full; confirms the
  complex-AXPY fold.
- `reference/palace/palace/linalg/nleps.cpp:606-619` — deflation-basis growth, read in full;
  confirms normalize-at-`:610-611`, store-at-`:615`, no orthogonalization (`X`-not-orthonormal).
- `reference/palace/palace/linalg/nleps.cpp:408-415` — confirms `δ = √ε` at `:412` and the `:411`
  divided-difference-Jacobian comment.
- `reference/palace/palace/linalg/nleps.cpp:375-380` — confirms `w` declaration at `:378` and the
  scratch-reuse comment.
- `book/src/L1/nleps_jacobian_action.md:12-120` — read; the L1 form (LHS) is fully consistent with
  the theme's L1-form section, including the big-space-only contract (`:75`), the product-rule
  derivation (`:77`), the divided-difference non-law (`:79`, law `:101`), and the accumulation-order
  non-law (`:103`).
- `tools/citecheck/citecheck.py --anchor` runs (all on-disk `reference/palace/`): every one of the
  theme's 19 numbered L0 pinpoints confirmed in-range with the expected token (full run log in this
  report's audit-trail; zero `DRIFT`, zero `OOB`, zero `NOANC` on correctly-quoted anchors).
- Cross-theme live links: all 11 referenced theme/operator chapters exist on disk
  (`nleps-deflated-residual-…`, `nleps-deflated-solve-…`, `apply-nonlinear-pencil-…`,
  `lu-solve-…`, `dot-…` themes; `apply_nonlinear_pencil`, `lu_solve`, `apply_linop`, `ksp_solve`,
  `linear_combination`, `linear-combination-fold-specialization` chapters).

## Open questions / caveats

1. **L1 ENTRY `+1` drift — carry-forward, NOT this theme's defect (dispatch-1 scope).** The L1
   ENTRY `book/src/L1/nleps_jacobian_action.md` still cites the codemap `+1`-drift numbers for the
   deflation block:
   - entry's `:664` (first solve `S⁻¹·v₂`) → on-disk `:665` (citecheck DRIFT +1, suggested `:665`)
   - entry's `:666` (second solve / back-projection) → on-disk `:667` (citecheck DRIFT +1)
   - entry's `:663` (block `S = λI − H`) → on-disk `:664` (citecheck DRIFT +1)
   - entry's `:659-660` (source comment) and `:661-662` (value pencil) read OK only because the
     ranges are wide enough to enclose the (off-by-one) anchor.

   This is the exact codemap brace-boundary `+1` drift cycle-025 flagged, and it is **dispatch-1's
   (lifter's) re-anchor scope for this same cycle (cycle-026)** — recorded here as an independent
   citecheck confirmation and a cross-check that the lifter's correction target is right, NOT as a
   finding against the THEME under audit. The THEME uses the corrected on-disk numbers throughout
   and is drift-free. Per the audit-report-inherited-miscitation discipline
   (`lifter-scope-content-correction-boundary`), I flag this as a carry-forward; the lifter's
   dispatch-1 should apply `:663→:664`, `:664→:665`, `:666→:667` (and the comment/pencil ranges
   `:659-660→:660-661`, `:661-662→:662-663` for pinpoint precision). No action needed on this theme.

2. **No dedicated NLEPS unit test exists.** `test/unit/**` has zero hits for
   `QuasiNewton|nleps|funcA2|GetResidualNorm` (consistent with the entire NEP-interior cohort).
   The firm decision rests on exhaustive positive structural citation, which I confirmed. The two
   non-laws (divided-difference `A2'`, accumulation-order) are recorded as non-laws precisely so
   they do not require a test to firm — this is correctly reasoned in the theme. Not a blocker; a
   future empirical-match test (if a `test-nleps.cpp` were ever added — out of project write-scope
   today) would upgrade the law-confidence but is not required for the firm status.

3. **Directionality check (high→low).** The theme narrates forward (L1 → L0): the LHS is the pure
   L1 `nleps_jacobian_action`, the RHS is the `w = J * v` L0 block, and the §"Rewrite — forward
   (L1 → L0)" prose narrates the rewrite in that direction. No reverse-direction (L0-lifts-to-L1)
   narration found in the formal sections. No directionality violation.

OQ ledger disposition appended: `nleps-jacobian-action-mutation-rotation-lowering-verifier-audit-followup`.
