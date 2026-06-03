---
agent: lowering-verifier
invoked_at: 2026-06-03T185421Z
scope: L1 operator 2nd-gate (test-coverage) audit — matrix-weighted-norm
status: pending
inputs:
  - book/src/L1/matrix-weighted-norm.md
  - reference/palace/test/unit/test-domainpostoperator.cpp:75-93 (GetElectricFieldEnergy energy-units test)
  - palace/models/domainpostoperator.cpp:219-231 (GetElectricFieldEnergy energy-form body)
  - palace/linalg/operator.cpp:599-619 (the Norml2(comm,x,B,Bx) √-overload — the named entry point)
  - book/src/L4/domain_energy_reduce.md (coupled critical-path consumer re-anchor)
integrated_at: 2026-06-03T192132Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (D1, staging row 2). matrix-weighted-norm 2nd-gate audit → warrant SHARPENED, +0 firm: the SPD radicand ⟨E,M E⟩+½ is now positively test-covered (test-domainpostoperator.cpp), but the outer √ at linalg::Norml2 is NOT (firm-on-positive-structure escape RULED OUT); token STAYS rough-in (test-coverage-bounded). §Status bullet sharpened, Evidence line rewritten, 3-entry verified_against: block appended. Coupled re-anchor of L4 domain_energy_reduce (energy-form radicand now test-covered; gate-(a) PARTIALLY advanced, not discharged). Build exit 0, linkcheck2 clean. retroactive-budget 0, gate hits 0. PARTIALLY-ADVANCES OQs matrix-weighted-norm-...-c028 + domain_energy_reduce-promotion-double-gated. D1 landed +0 firm so D2's conditional index fold-note no-ops (30/37 tally correct)."
---

# CYCLE: Audit matrix-weighted-norm 2nd (test-coverage) gate

## Summary

Audited `book/src/L1/matrix-weighted-norm.md` (`rough-in (test-coverage-bounded)`, 0 `verified_against:` blocks) against the cycle-079-surfaced positive test route: `test-domainpostoperator.cpp:75-93`, which calls `GetElectricFieldEnergy(*E_field)` and asserts the result against the closed-form `0.5·ε₀·E₀²·sx·sy·sz` via `CHECK_THAT(..., WithinRel(..., 0.01))`. The test positively exercises the SPD-weighted **radicand** `⟨E, M_elec E⟩` (via `M_elec->Mult(E.Real(), D); dot = linalg::LocalDot(E.Real(), D)`) plus the `½` scaling — i.e. the *energy-form constituent* that `domain_energy_reduce` folds — but it does **NOT** exercise the outer `√` of `matrix-weighted-norm = √(xᴴ B x)` at the operator's named entry point `linalg::Norml2(comm, x, B, Bx)` (the energy form returns `0.5 * dot`, with no `sqrt` and never calling `Norml2`). **Verdict: partially-supported — sharpen the `rough-in (test-coverage-bounded)` warrant; NO full firm promotion.** The firm-on-positive-structure escape does NOT apply: laws 4 / 6 / 7 (triangle, Cauchy–Schwarz, parallelogram) carry genuine norm-axiom content requiring the inner-product structure on `B`, NOT syntactic operator-algebra identities — this is the `eigsolve`-convergence-semantics situation, not the `apply_linop` syntactic-identity situation. The squared/energy-form radicand is now positively test-covered; the √-overload's named entry point is still not the tested entry point. The coupled consumer `domain_energy_reduce.md` is re-anchored to the sharpened (unchanged-token, precision-refined) maturity.

## Per-citation audit

- **Citation**: `reference/palace/test/unit/test-domainpostoperator.cpp:75-93`
  - **Theme claim** (proposed gate route): a positive Palace test exercising the SPD-weighted energy form.
  - **Found**: `TEST_CASE("DomainPostOperator - Electric Energy Units")`. `:83` `double energy_nondim = dom_post_op.GetElectricFieldEnergy(*E_field);`; `:90-91` `double expected_energy_SI = 0.5 * electromagnetics::epsilon0_ * E0_SI * E0_SI * sx_SI * sy_SI * sz_SI;`; `:93` `CHECK_THAT(energy_SI, WithinRel(expected_energy_SI, 0.01));`. A uniform field `E = E0·ẑ` is projected onto an ND space on a `[0,sx]×[0,sy]×[0,sz]` cube; the asserted closed form is the analytic `½·ε₀·E₀²·V`. citecheck `--anchor` `ok` for `GetElectricFieldEnergy@:83`, `expected_energy_SI@:90`, `WithinRel@:93`. The test header (`:31-32`) explicitly self-limits: "TODO: This test can be expanded/improved to be a more robust test for the actual function, not just the units."
  - **Verdict**: partially-supports.
  - **Notes**: positively covers the **radicand** `⟨E, M_elec E⟩` (the squared self-bilinear of law 8) + the `½` energy scaling; does NOT cover the outer `√` nor the named `Norml2` entry point. The 1% relative tolerance (`WithinRel(..., 0.01)`) is a discretization-error band (FE projection of a uniform field on a tet mesh at order 1), consistent with a units/integration check rather than a tight algebraic-law verification.

- **Citation**: `palace/models/domainpostoperator.cpp:219-231` (`DomainPostOperator::GetElectricFieldEnergy`)
  - **Theme claim** (proposed): the energy-form body exercised by the test — the SPD-weighted radicand + `½`.
  - **Found**: `:221` `if (M_elec)`; `:223` `M_elec->Mult(E.Real(), D);`; `:224` `double dot = linalg::LocalDot(E.Real(), D);`; `:225-229` adds the imaginary-part contribution when `E.HasImag()`; `:230` `Mpi::GlobalSum(1, &dot, E.GetComm());`; `:231` `return 0.5 * dot;`. No `std::sqrt` anywhere; the form is `½⟨E, M_elec E⟩`, i.e. `½ · matrix_weighted_norm(E, M_elec)²`. citecheck `--anchor` `ok` for `GetElectricFieldEnergy@:219`, `LocalDot@:224`, `0.5@:231`.
  - **Verdict**: supports (as evidence for the radicand constituent) / does-not-support (as evidence for the √-overload).
  - **Notes**: this is the WHOLE-domain `GetElectricFieldEnergy(const GridFunction &)` at `:219`, distinct from the per-domain `GetDomainElectricFieldEnergy(int idx, ...)` at `:255`. Confirms the test exercises the radicand `⟨E, M E⟩` (real + optional imaginary parts) but stops one operation short of `matrix-weighted-norm`'s defining `√`.

- **Citation**: `palace/linalg/operator.cpp:599-619` (the named √-overload entry point)
  - **Theme claim** (theme §Status gate (a)): `matrix-weighted-norm`'s named L0 entry point is `linalg::Norml2(comm, x, B, Bx)`, whose body is `B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)`.
  - **Found**: `:599-607` real specialization, `:606` `return std::sqrt(dot);`; `:609-619` complex specialization, `:618` `return std::sqrt(dot.real());`. citecheck `--anchor` `ok` for `std::sqrt@:606` within `:599-607`.
  - **Verdict**: supports (confirms the entry point and the `√`).
  - **Notes**: the `GetElectricFieldEnergy` energy form does NOT route through this function — it open-codes `M_elec->Mult` + `LocalDot` + `0.5 *` directly. So the test exercises the *same radicand shape* (`Operator::Mult` then dot) but through a different call path that omits the `√`. The named entry point `Norml2(comm,x,B,Bx)` remains test-uncovered (gate (a) still open); the test discharges only the radicand-constituent half.

## Applicability conditions

- **Condition**: `B` must be square (`LinearOperator[N,N]`).
  - **Verifiable**: yes — the test's `M_elec` is the ND-space electric mass matrix, square by construction. **Counter-example?** no.
- **Condition**: `B` Hermitian (self-adjoint) for `xᴴ B x` real.
  - **Verifiable**: indirectly — `M_elec` is a real symmetric mass integrator; the test uses a real field so the imaginary branch (`:225-229`) is not exercised. The complex-`x`/real-`B` Hermiticity-witness path (`operator.cpp:616-617` assert) is NOT exercised by this test. **Counter-example?** no.
- **Condition**: `B` SPD (positive-definite) for true-norm / radicand `> 0`.
  - **Verifiable**: indirectly — a mass matrix is SPD; the test's positive non-zero asserted energy is consistent with `dot > 0`. The energy form does NOT carry the `MFEM_ASSERT(dot > 0.0)` guard that `Norml2` does (the energy form never sqrt's, so it tolerates `dot = 0`); the SPD-strict run-time guard at the named entry point stays untested. **Counter-example?** no.

## Algebraic laws (firm-on-positive-structure escape assessment)

The escape (a `rough-in (test-coverage-bounded)` entry is `firm` when its laws are syntactic identities on fully-specified positive source, so the missing test does not gate them) was assessed and **does NOT apply** here:

- **Law 8 (self-bilinear identity `‖x‖²_B = xᴴ B x`)**: syntactic — holds by definition; the test's radicand coverage now *also* gives it positive empirical backing.
- **Law 3 / 9 / 11 / 12 (homogeneity, identity-collapse, phase-invariance, zero)**: follow trivially from `apply_linop` + `dot` laws (near-syntactic).
- **Law 4 (triangle), Law 6 (Cauchy–Schwarz), Law 7 (parallelogram)**: **NOT syntactic** — these carry genuine norm-axiom / inner-product-structure content that the L0 source does NOT verify (the source neither checks `B` Hermitian nor proves sub-additivity). Their confidence is exactly what a dedicated √-overload-entry-point test would raise. This is the law cohort that keeps the entry `rough-in`, mirroring `eigsolve`'s convergence-semantics gate (NOT `apply_linop`'s all-syntactic situation).

Therefore: the structural decomposition is firm, the radicand constituent is now positively test-covered, but the norm-axiom laws remain test-gated → **no firm promotion; sharpen the warrant.**

## Proposed changes

Two edits. Edit 1 sharpens the `matrix-weighted-norm` §Status warrant and adds the fenced `verified_against:` block (token UNCHANGED — stays `rough-in (test-coverage-bounded)`). Edit 2 re-anchors the coupled consumer `domain_energy_reduce.md` (radicand-constituent now positively test-covered; maturity token unchanged so the inheritance note stays accurate).

### Edit 1 — sharpen §Status warrant + add `verified_against:` (matrix-weighted-norm.md)

Replace the §Status promotion-gate (a) bullet text and the closing "No direct test evidence" Evidence line, and append the `verified_against:` block at end of file.

```edit:book/src/L1/matrix-weighted-norm.md
[replace the gate-(a) bullet at line 113]
- **(a) Direct test coverage of the √-overload entry point** (STILL OPEN): a Palace unit test that exercises `linalg::Norml2(comm, x, B, Bx)` on a known-SPD `B` and verifies the closed-form `√(xᴴ B x)` against a hand-computed value. **Partially advanced (cycle-080):** `test/unit/test-domainpostoperator.cpp:75-93` ("DomainPostOperator - Electric Energy Units") now positively covers the SPD-weighted **radicand** `⟨E, M_elec E⟩` (the squared self-bilinear of law 8) plus the `½` energy scaling — it calls `GetElectricFieldEnergy(*E_field)` (`palace/models/domainpostoperator.cpp:219-231`: `M_elec->Mult(E.Real(), D); dot = linalg::LocalDot(E.Real(), D); ... return 0.5 * dot;`) and asserts against the closed-form `0.5·ε₀·E₀²·sx·sy·sz` via `WithinRel(..., 0.01)`. This discharges the **radicand-constituent** half of gate (a). It does **NOT** discharge the gate: the energy form returns `0.5 * dot` with no `√` and never routes through `Norml2`, so the outer `√` of `matrix-weighted-norm = √(xᴴ B x)` at its named entry point `linalg::Norml2(comm, x, B, Bx)` (`palace/linalg/operator.cpp:606` `return std::sqrt(dot)`) remains the untested entry point. Full discharge still needs a test at the `Norml2(comm,x,B,Bx)` entry point itself (or a literature-anchor pass raising law-4/6/7 confidence to `ksp_solve`-equivalent).
```

```edit:book/src/L1/matrix-weighted-norm.md
[replace the closing Evidence line at line 143]
**Radicand-constituent test evidence (cycle-080), √-overload entry point still uncovered** — `test/unit/test-domainpostoperator.cpp:75-93` positively exercises the SPD-weighted radicand `⟨E, M_elec E⟩` + `½` scaling (the energy-form constituent that `domain_energy_reduce` folds) and asserts it against a closed form to 1% relative tolerance. This advances gate (a) from "no direct test evidence" to "radicand positively covered, √-overload named entry point (`linalg::Norml2(comm, x, B, Bx)`) still untested". The norm-axiom laws (4 triangle, 6 Cauchy–Schwarz, 7 parallelogram) carry genuine inner-product-structure content that the L0 source does not verify, so the firm-on-positive-structure escape does not apply and the entry stays `rough-in (test-coverage-bounded)`. Indirect coverage via the three eigensolver backends (ARPACK, SLEPc, NLEPS) is consistent but does not constitute algebraic-law verification.
```

```edit:book/src/L1/matrix-weighted-norm.md
[append at end of file]
~~~yaml
verified_against:
  - citation: test/unit/test-domainpostoperator.cpp:75-93
    verdict: partially-supports
    audited_at: 2026-06-03T185421Z
    note: GetElectricFieldEnergy energy-units test positively covers the SPD-weighted radicand ⟨E, M_elec E⟩ + ½ scaling (law-8 self-bilinear constituent) via WithinRel against the closed-form ½·ε₀·E₀²·V; does NOT cover the outer √ nor the named entry point linalg::Norml2(comm,x,B,Bx)
  - citation: palace/models/domainpostoperator.cpp:219-231
    verdict: partially-supports
    audited_at: 2026-06-03T185421Z
    note: GetElectricFieldEnergy body — M_elec->Mult(E.Real(),D); dot = LocalDot(E.Real(),D); return 0.5*dot — is the radicand ⟨x,B x⟩ + ½, NOT the √-overload; open-codes the form without routing through Norml2
  - citation: palace/linalg/operator.cpp:599-619
    verdict: supports
    audited_at: 2026-06-03T185421Z
    note: the named √-overload entry point linalg::Norml2(comm,x,B,Bx); :606 return std::sqrt(dot) (real), :618 return std::sqrt(dot.real()) (complex) — confirms the entry point and the outer √ that the energy-form test path omits; gate (a) stays open at this entry point
~~~
```

### Edit 2 — coupled consumer re-anchor (domain_energy_reduce.md)

The maturity token `rough-in (test-coverage-bounded)` is UNCHANGED, so the frontmatter `consumes:` note at `:7` and the "least-firm folded primitive" note at `:278` stay structurally accurate. Refine them to record the radicand-constituent test coverage so the inheritance note is precise (the consumer's gate #1 at `:274-278` already correctly states the energy form is the folded primitive; gate #2 at `:281-283` already correctly states `test-domainpostoperator.cpp:83` supports the energy-form constituent but NOT the per-domain reduction — that text needs NO change, it is already correct). The only refinement is the frontmatter `:7` note, to mirror the sharpened L1 warrant.

```edit:book/src/L4/domain_energy_reduce.md
[replace the matrix-weighted-norm consumes line at line 7]
  - book/src/L1/matrix-weighted-norm.md (rough-in (test-coverage-bounded) — the ½⟨field, M_i field⟩ domain-restricted SPD energy form, the first folded primitive; the verb's rough-in maturity is inherited from it. Cycle-080 lowering-verifier audit: its radicand constituent ⟨field, M_i field⟩ + ½ is now positively test-covered by test-domainpostoperator.cpp:75-93, but its √-overload named entry point linalg::Norml2(comm,x,B,Bx) stays test-uncovered, so the token is unchanged)
```

(No change to `:274-283`: that prose is already correct — it folds the energy-form numerator as the `matrix-weighted-norm` primitive and correctly states `test-domainpostoperator.cpp:83` supports the energy-form constituent but NOT the per-domain reduction. The `:278` "as firm as its least-firm folded primitive" note stays accurate because the primitive's token is unchanged.)

## Supporting evidence

- `reference/palace/test/unit/test-domainpostoperator.cpp:26-94` — the full `TEST_CASE`; `:75-93` the energy/assert block; `:31-32` the self-limiting "units, not the actual function" TODO.
- `reference/palace/palace/models/domainpostoperator.cpp:219-231` — `GetElectricFieldEnergy` body (radicand + `½`, no `√`); `:255` the per-domain `GetDomainElectricFieldEnergy(int idx, ...)` distinguished.
- `reference/palace/palace/linalg/operator.cpp:599-619` — the named `Norml2(comm,x,B,Bx)` √-overload (real `:599-607` / complex `:609-619`), `:606`/`:618` the `std::sqrt`.
- `book/src/L4/domain_energy_reduce.md:7, 274-283` — the double-gated consumer; gate #1 (primitive maturity) + gate #2 (no dedicated per-domain test) both already correctly stated.
- citecheck `--anchor` runs: all 7 anchors `ok` on disk (`GetElectricFieldEnergy@:83`, `expected_energy_SI@:90`, `WithinRel@:93`, `GetElectricFieldEnergy@:219`, `LocalDot@:224`, `0.5@:231`, `std::sqrt@:606`). The codemap path `palace/models/domainpostoperator.cpp` resolves on disk to `reference/palace/palace/models/domainpostoperator.cpp` (double-`palace` layout); citecheck resolves the citation-convention path correctly.

## Notes for D2 / per-report integrator (shared-index discipline)

- **No firm-count delta this cycle.** Verdict is "sharpen the rough-in warrant", NOT a firm promotion. `matrix-weighted-norm` stays `rough-in (test-coverage-bounded)`; the L1 firm tally is UNCHANGED by this dispatch. D2 (harvester) remains the sole count-owner of `L1/index.md` consolidated tally + `SUMMARY.md`; this report contributes **+0** to the firm count. No status-cell maturity-token change is needed in `L1/index.md` either (token unchanged) — only the per-operator §Status warrant prose (Edit 1) changes.

## Open questions / caveats

- Append to `scaffolding/open-questions.md`:
  - Update `matrix-weighted-norm-and-bilinear-form-stay-rough-in-with-sharpened-per-operator-gates-c028`: the `matrix-weighted-norm` gate is **partially advanced** (cycle-080) — radicand constituent `⟨x, B x⟩` + `½` now positively test-covered via `test-domainpostoperator.cpp:75-93`; the √-overload named entry point `linalg::Norml2(comm,x,B,Bx)` is STILL the untested entry point. Full discharge needs either (a) a test at the `Norml2(comm,x,B,Bx)` entry point itself exercising the outer `√` on a known-SPD `B`, or (b) a literature-anchor pass raising the norm-axiom laws (4/6/7) confidence. The `bilinear-form` sibling half stays open (no positive test surfaced).
  - Update `domain_energy_reduce-promotion-double-gated`: gate (a) (folded `matrix-weighted-norm` maturity) is partially advanced (its radicand is now test-covered) but NOT discharged (the √-overload entry point stays uncovered AND the consumer's own gate #2 — a dedicated per-domain energy-participation test — is independently still open). The verb stays `rough-in`; no promotion this cycle.
- **Caveat (firm-on-positive-structure escape assessed, ruled inapplicable):** laws 4/6/7 are NOT syntactic identities (they carry inner-product-structure / norm-axiom content the L0 source does not verify), so the escape that firms `apply_linop`-class entries does not fire here. Recorded explicitly so a future producer does not re-litigate.
- **No directionality violation:** this is an L1 operator entry (not a lowering theme); the audit is of test coverage, not a high→low rewrite narration. N/A.
- **Broad re-anchor NOT triggered:** the ~30-file `matrix-weighted-norm` reference graph re-anchor would only fire on a FULL firm promotion. Verdict is not a promotion, so no broad sweep is needed (and would have been deferred as an OQ per the one-operator-per-dispatch discipline regardless). Only the single direct critical-path consumer `domain_energy_reduce.md` is re-anchored (Edit 2), per the floor-landing-implies-same-cycle-adjacent-entry-reanchor guard.
