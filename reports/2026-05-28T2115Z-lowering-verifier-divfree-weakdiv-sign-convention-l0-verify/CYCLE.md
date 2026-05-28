---
agent: lowering-verifier
invoked_at: 2026-05-28T19:32:56Z
scope: L1 entry audit — divfree-projector WeakDiv sign-convention promotion gate (divfree-weakdiv-sign-convention-l0-verify)
status: integrated
integrated_at: 2026-05-29T003000Z
integration_commit: 73ecd3e
integration_notes: "cycle-014 position 1/8. Verdict UNBLOCK-PROMOTION: WeakDiv ≈ −GᵀM positively anchored in Palace-owned source (fem/integrator.hpp:217 + fem/integ/mixedvecgrad.cpp:202, repairer-corrected from :203), refuting cycle-013 out-of-scope-MFEM premise. Applied §Status UNBLOCKED note to L1/divfree-projector.md; caveat NOT dropped. partly-constructive→firm promotion (5 firming edits) GATED to cycle-015 abstractor via OQ divfree-projector-partly-constructive-to-firm-enactment. Build clean."
inputs:
  - book/src/L1/divfree-projector.md
  - palace/linalg/divfree.cpp:43-186 (construction + apply)
  - palace/linalg/divfree.hpp:28-72 (class doc + Mult decls)
  - palace/fem/integrator.hpp:217-226 (MixedVectorWeakDivergenceIntegrator class + a(u,v) doc)
  - palace/fem/integ/mixedvecgrad.cpp:148-205 (the Assemble body; the -1.0 coefficient)
  - palace/drivers/eigensolver.cpp:262 (divfree->Mult(v0) call site)
---

# CYCLE: Audit divfree-projector — WeakDiv ≈ -GᵀM sign-convention promotion gate

## Summary

I audited the `partly-constructive` caveat on `book/src/L1/divfree-projector.md`, whose
idempotence law (`P∘P=P`) and divergence-free output characterization were gated on the
unverified reading `WeakDiv ≈ GᵀM` (up to sign). The cycle-013 integrator marked the entry
`partly-constructive` on the premise that the sign rests on the **MFEM-vendored**
`MixedVectorWeakDivergenceIntegrator` internals, i.e. below the L0 scope boundary.

**That premise is refuted by Palace source.** `MixedVectorWeakDivergenceIntegrator` is a
**Palace-owned, libCEED-backed integrator** (`palace/fem/integrator.hpp:217-226`, body at
`palace/fem/integ/mixedvecgrad.cpp:148-205`), NOT the MFEM-vendored one. Its bilinear form
is documented **in Palace source** as `a(u, v) = -(Q u, grad v)` (`integrator.hpp:217`),
and the negating sign is materialized **in Palace source** as an explicit `-1.0`
coefficient passed to `PopulateCoefficientContext(space_dim, Q, transpose, -1.0)`
(`mixedvecgrad.cpp:202`) — side-by-side contrasted with the non-negated
`MixedVectorGradientIntegrator` (`mixedvecgrad.cpp:142`, no `-1.0`). The sign is therefore
**positively anchored in two Palace sites, fully in scope.**

**Verdict: UNBLOCK-PROMOTION.** The `WeakDiv ≈ -GᵀM` reading is confirmed from Palace source.
The promotion condition ("upstream MFEM behavior, out of scope") is mooted — it was based on a
mislocalization of the integrator. The constructive sub-part (idempotence + divergence-free
characterization) can be promoted to `firm`. I identify the exact firming edits below and route
them to a follow-up dispatch (abstractor); I do NOT drop the `## Status` caveat myself.
Two carry-forward citation corrections and one substantive semantic clarification are also
flagged (the `:177` "irrotational ... subtract" comment vs. the additive `+1.0`, and the
`Gᵀ M G` vs. `M` inner-operator distinction).

All cited `divfree.cpp` anchors (`:113`, `:117`, `:119`, `:159`, `:177`) and `divfree.hpp`
anchors (`:29`, `:51`, `:64-66`) re-confirmed exact via independent `read_range` — no drift
remaining from the cycle-013 off-by-1 (which was already repaired to `:113`/`:117`).

## Per-citation audit

### Citation: palace/linalg/divfree.cpp:113 (WeakDiv integrator)
- **Theme claim**: `WeakDiv` built from `MixedVectorWeakDivergenceIntegrator`, partial assembly.
- **Found** (`read_range` :111-116): `BilinearForm weakdiv(nd_fespace, h1_fespaces.GetFinestFESpace()); weakdiv.AddDomainIntegrator<MixedVectorWeakDivergenceIntegrator>(epsilon_func); WeakDiv = std::make_unique<ParOperator>(weakdiv.PartialAssemble(), ...)`. Line `:113` is exactly the `AddDomainIntegrator` line.
- **Verdict**: supports. Exact.
- **Notes**: `epsilon_func` is the `MaterialPropertyCoefficient` over the real permittivity (`:84-85`), so `WeakDiv` is ε-weighted — theme correct. Trial space = `nd_fespace` (Nedelec/H(curl)), test = finest H1 — confirms the `[N_nd] -> [N_h1]` direction in the signature.

### Citation: palace/linalg/divfree.cpp:117 (Grad)
- **Theme claim**: `Grad` = discrete interpolator (H1 → Nedelec).
- **Found**: `Grad = &nd_fespace.GetDiscreteInterpolator(h1_fespaces.GetFinestFESpace());` — exact at `:117`. It is a borrowed pointer (`const Operator *Grad`, `divfree.hpp:42`), not owned. Theme's "Read-only" is correct; minor: theme does not note it's a non-owning pointer, but that's L1-irrelevant.
- **Verdict**: supports. Exact.

### Citation: palace/linalg/divfree.cpp:119 (real and SPD)
- **Theme claim**: `// The system matrix for the projection is real and SPD.`
- **Found**: exact at `:119`. Justifies M-inner-product / M-orthogonality.
- **Verdict**: supports.

### Citation: palace/linalg/divfree.cpp:155-186 (four-step apply)
- **Theme claim**: 4 steps — WeakDiv·y → Z_bdr → ksp solve M·ψ=rhs → y += Grad·ψ.
- **Found** (`read_range` :154-187): Confirmed. Step 1 `WeakDiv->Mult(y, rhs)` at `:166` (real branch), complex branches `:161-162`. Step 2 `linalg::SetSubVector(rhs, *bdr_tdof_list_M, 0.0)` at `:173`. Step 3 `ksp->Mult(rhs, psi)` at `:175`. Step 4 `Grad->AddMult(psi, y, 1.0)` at `:185` (real), complex at `:180-181`.
- **Verdict**: supports.
- **Notes**: theme cites step 4 complex branches at `:180-181` and real at `:185` — both exact. Step 1 the theme cites `:159-168`; the actual `WeakDiv->Mult` real call is `:166` and the comment "Compute the divergence of y." is `:159` — range is correct/inclusive. Step 3 theme cites `:175` — exact.

### Citation: palace/linalg/divfree.cpp:177 ("irrotational portion ... and subtract")
- **Theme claim**: in-apply comment "Compute the irrotational portion of y and subtract." cited as the intent-comment in tension with the additive `+1.0`.
- **Found**: exact at `:177`: `// Compute the irrotational portion of y and subtract.` Immediately followed by `Grad->AddMult(psi, y, 1.0)` (coefficient **+1.0**, an addition).
- **Verdict**: supports (the comment text is exact), BUT see "Substantive semantic finding" — the theme reconciles "subtract" with "+1.0" via the WeakDiv minus sign, and that reconciliation is now POSITIVELY CONFIRMED (not merely a plausible reading).

### Citation: palace/linalg/divfree.hpp:28-31 (defining condition Gᵀ M x = 0)
- **Theme claim**: class doc states the projection target is `Gᵀ M x = 0`, G = discrete gradient spanning curl-curl nullspace.
- **Found** (`read_range` :20-31, `search_text`): comment is on `:27-30`; the literal `Gᵀ M x = 0` text is on `:29`. Theme's `:28-31` range encloses it.
- **Verdict**: supports. (Minor anchor-tightening available: the exact `Gᵀ M x = 0` line is `:29`; the theme's `:28-31` enclosing range is acceptable but `:27-30` is the true comment block.)

### Citation: palace/linalg/divfree.hpp:63-72 (Mult decls)
- **Theme claim**: `Mult(y)` in-place + `Mult(x,y)` = `y=x; Mult(y)`.
- **Found**: `Mult(VecType &y)` decl at `:65`; out-of-place `Mult(const VecType &x, VecType &y) { y = x; Mult(y); }` at `:67-71`. Theme cites `:68-72` for the out-of-place body — actual body is `:67-71` (off by ~1; the inner `y=x; Mult(y);` is `:69-70`). Minor drift, non-load-bearing.
- **Verdict**: supports (with a minor anchor note, below).
- **Notes**: **NEW finding not in theme** — the `Mult` doc at `:63-65` says the result is "the **irrotational** portion of this vector field. The resulting vector will satisfy `∇ x y = 0`" (curl-free!). This is the *complementary* characterization to the class-doc divergence-free `:29` target. See Substantive semantic finding.

### Citation: palace/linalg/divfree.cpp:121-149 (ksp setup), :140-142 (tolerances)
- **Theme claim**: CG + BoomerAMG (depth 1) / GMG (depth>1), rel-tol, abs-tol = epsilon, max-it.
- **Found** (`read_range` :119-149, :139-143): CG `:138-139`, `SetRelTol(tol)` `:140`, `SetAbsTol(std::numeric_limits<double>::epsilon())` `:142`, `SetMaxIter(max_it)` `:143`. `ksp->SetOperators(*M, *M)` `:147`. Theme's "abs-tol = machine epsilon at :141" is off by 1 — it's `:142`.
- **Verdict**: supports (with a `:141`→`:142` anchor correction).

### Citation: palace/drivers/eigensolver.cpp:260-262 (divfree->Mult(v0))
- **Theme claim**: initial-vector projection call site.
- **Found** (`read_range` :256-264): `if (divfree) { divfree->Mult(v0); }` — the `Mult` call is `:262`. Exact.
- **Verdict**: supports.

### Citation (NOT in theme, surfaced by audit): palace/fem/integrator.hpp:217 + palace/fem/integ/mixedvecgrad.cpp:202 — THE SIGN ANCHOR
- **Theme claim**: theme asserts (Status, Non-law sign convention) that `WeakDiv` "internally absorbs the minus sign" but that this is "a reading of the integrator's internals, not a read of a positive Palace site" and rests on MFEM internals below L0.
- **Found**: `MixedVectorWeakDivergenceIntegrator` is **Palace-owned**, defined at `palace/fem/integrator.hpp:218-226`, with class doc `// Integrator for a(u, v) = -(Q u, grad v) for u in H(curl) and v in H1.` (`:217`). Its `Assemble` body (`palace/fem/integ/mixedvecgrad.cpp:148-205`) materializes the sign via `PopulateCoefficientContext(space_dim, Q, transpose, -1.0)` (`:202`). The sibling `MixedVectorGradientIntegrator::Assemble` (`a(u,v) = (Q grad u, v)`) calls `PopulateCoefficientContext(space_dim, Q, transpose)` with NO `-1.0` (`:142`) — direct side-by-side contrast confirms the `-1.0` is the deliberate weak-divergence sign.
- **Verdict**: **supports — and REFUTES the theme's "out of scope / not a positive site" framing.** The sign IS a positive Palace source site.
- **Notes**: `test/unit/test-libceed.cpp:905-916` cross-validates Palace's `MixedVectorWeakDivergenceIntegrator` against `mfem::MixedVectorWeakDivergenceIntegrator` — i.e. Palace ships its own implementation and tests it against MFEM's. This is the L0-equivalent test evidence (semantic supplement) that the sign behavior is exercised. The bilinear form `a(u,v) = -(εu, ∇v)` with trial `u∈H(curl)`, test `v∈H1`, and `(u,∇v) = (u, Gv)_{H(curl)} = (Gᵀu, v)_{H1}` (G = discrete gradient `divfree.cpp:117`), gives `WeakDiv = -Gᵀ(ε-weighted)` — exactly the `WeakDiv ≈ -GᵀM` (signed) reading. The `M` in `GᵀM` is the ε-mass; here ε enters through `Q=epsilon_func`. The sign is unambiguous and in-scope.

## Applicability conditions

- **Condition: `WeakDiv ≈ GᵀM` (up to sign) — the gated reading.**
  - **Verifiable**: YES, from `palace/fem/integrator.hpp:217` (`a(u,v) = -(Q u, grad v)`) + `mixedvecgrad.cpp:202` (`-1.0`). Both are positive Palace sites in scope.
  - **Found counter-example?**: No. The `-1.0` is confirmed deliberate (contrast `:142`).

- **Condition: idempotence `P∘P=P` (the partly-constructive sub-part).**
  - **Verifiable**: YES, now that the sign is anchored. With `WeakDiv = -GᵀεG_mass`-style and the additive `+1.0` correction, `P·y = y + Grad·M⁻¹·Z(WeakDiv·y)`. For a field already satisfying `Gᵀεy=0`, `WeakDiv·y = 0` (the weak-div of a divergence-free field is zero, sign immaterial to the zero), so the correction vanishes and `P(P·y)=P·y`. The exact-arithmetic derivation holds; modulo ksp tolerance as the theme states.
  - **Found counter-example?**: No.

- **Condition: divergence-free output `Gᵀ M y' = 0`.**
  - **Verifiable**: YES (class doc `divfree.hpp:29` + the now-anchored sign). NOTE the `Mult` doc `divfree.hpp:64-66` describes the output as the **irrotational** (`∇×y=0`) portion — a complementary characterization. See Substantive semantic finding; this is a NEW tension the theme should address but does NOT refute the divergence-free claim (the two doc comments describe the Helmholtz split from the two complementary projector viewpoints; the class is named for the divergence-free target it computes).

- **Condition: step ordering `WeakDiv → Z → ksp → Grad` load-bearing.**
  - **Verifiable**: YES, source order `:159-185` matches; reordering changes result.
  - **Found counter-example?**: No.

## Algebraic laws

- **Linearity** — Holds. Each step linear (`WeakDiv`, `SetSubVector`-zero, `Grad->AddMult`, ksp). Confirmed against `:159-185`.
- **Idempotence `P∘P=P`** — Holds in exact arithmetic; **now firm** given the anchored sign (was the gated sub-law). The sign no longer blocks it.
- **Range `{x : Gᵀ M x = 0}`** — Holds per `divfree.hpp:29`.
- **M-orthogonality / Ker(P)=Range(Grad)** — Holds; `M` SPD (`:119`).
- **Real-linearity (block-diagonal complex)** — Holds; complex branches `:161-162`, `:180-181` apply real operators component-wise.
- **Non-law sign convention** — The "load-bearing sign" claim is CORRECT and now **positively re-derivable** from `integrator.hpp:217` + `mixedvecgrad.cpp:202`. The theme's hedge ("not independently re-derived ... unverified-integrator-sign caveat") is now obsolete.
- **Non-law step ordering** — Holds.

## Inner-operator distinction (substantive note, not a defect)

The class field comment `divfree.hpp:51` reads `// Linear solver for the projected linear system (Gᵀ M G) y = x.` — i.e. the *abstract* projected system is `(GᵀMG)ψ = GᵀMy`. But the apply solves `ksp` against **`M`** (the H1 `DiffusionIntegrator` mass-like operator), not `GᵀMG`: `ksp->SetOperators(*M, *M)` (`:147`), `ksp->Mult(rhs, psi)` (`:175`). The theme's Semantics step 3 already records this correctly ("The triple product `Gᵀ M G` is never materialized: the system passed to `ksp` is `M` itself, with `Gᵀ` realized by `WeakDiv` on the RHS side and `G` realized by `Grad` on the correction side"). I confirm this is accurate against source — the `GᵀMG` at `:51` is the *conceptual* normal-equations form; the implementation uses the H1 Poisson operator `M` because on H1 dofs `Grad` is the identity-like discrete interpolator and the H1 stiffness `M` (DiffusionIntegrator) already equals `GᵀM_ndG` in the relevant sense. This is a faithful Palace optimization, correctly captured. No edit needed; flagged for completeness.

## Proposed changes

**Verdict is UNBLOCK-PROMOTION. The follow-up dispatch (abstractor) applies these edits, THEN
drops the `## Status` caveat. I do NOT enact the promotion or edit `book/` myself.**

### Edit 1 (REQUIRED for promotion) — add the positive sign anchor to Evidence + Signature
Add to the `P.WeakDiv` bullet in `## Signature` and to `## Evidence`:

```edit:book/src/L1/divfree-projector.md
[in the P.WeakDiv signature bullet, after the divfree.cpp:111-116 citation, append:]
  The negating sign of the weak-divergence form is set in Palace source: the
  integrator's bilinear form is `a(u, v) = -(ε u, ∇v)` for `u ∈ H(curl)`, `v ∈ H1`
  (`palace/fem/integrator.hpp:217`), materialized as an explicit `-1.0` coefficient
  in the assemble body (`palace/fem/integ/mixedvecgrad.cpp:202`) — contrast the
  non-negated `MixedVectorGradientIntegrator` (`palace/fem/integ/mixedvecgrad.cpp:142`,
  no `-1.0`). Thus `WeakDiv = -Gᵀ` (ε-weighted), a positive Palace source site.

[in ## Evidence, append:]
- `palace/fem/integrator.hpp:217` — `// Integrator for a(u, v) = -(Q u, grad v) for u
  in H(curl) and v in H1.` (the weak-div bilinear form; the negating sign in Palace source).
- `palace/fem/integ/mixedvecgrad.cpp:202` — `PopulateCoefficientContext(space_dim, Q,
  transpose, -1.0)` (the `-1.0` materializing the sign).
- `palace/fem/integ/mixedvecgrad.cpp:142` — sibling `MixedVectorGradientIntegrator` with
  NO `-1.0` (the side-by-side sign contrast).
- `palace/fem/integrator.hpp:218-226` — `class MixedVectorWeakDivergenceIntegrator`
  (Palace-owned, libCEED-backed — NOT MFEM-vendored).
- `palace/linalg/divfree.hpp:51` — `// Linear solver for the projected linear system
  (Gᵀ M G) y = x.` (the conceptual normal-equations form; the apply solves against M).
- `test/unit/test-libceed.cpp:905-916` — Palace's `MixedVectorWeakDivergenceIntegrator`
  cross-validated against `mfem::MixedVectorWeakDivergenceIntegrator` (L0-equivalent test).
```

### Edit 2 (REQUIRED for promotion) — rewrite the idempotence Caveat to "confirmed"
Replace the "Caveat (added on repair)" paragraph in the Idempotence bullet so it cites the
positive sign anchor and removes the contingency, and remove the `partly-constructive` tag
from the law header:

```edit:book/src/L1/divfree-projector.md
- **Idempotence (projector law).**
  `P∘P = P` in exact arithmetic: applying the projector to an already-divergence-free
  field returns it unchanged. By the defining condition `Gᵀ M (P·y) = 0`
  (`palace/linalg/divfree.hpp:28-31`), `P·y` lies in the divergence-free subspace, so
  `WeakDiv·(P·y) = 0` (step 1 yields zero residual), hence the correction `Grad·ψ = 0`
  and `P·(P·y) = P·y`. The identification of `WeakDiv` with the (negated) `Gᵀ M` of the
  defining condition is anchored in Palace source — the weak-div bilinear form is
  `a(u,v) = -(ε u, ∇v)` (`palace/fem/integrator.hpp:217`) with the `-1.0` set at
  `palace/fem/integ/mixedvecgrad.cpp:202` — so the derivation is unconditional in exact
  arithmetic. Holds modulo `ksp` tolerance: `Gᵀ M (P·y) = 0` only up to the convergence
  tolerance on the non-essential dofs (`palace/linalg/divfree.cpp:140,142`, rel-tol set
  at :140, abs-tol = machine epsilon at :142).
```

### Edit 3 (REQUIRED for promotion) — rewrite ## Status to firm
Replace `## Status` body: change `partly-constructive` → `firm`; remove the constructive
sub-part / negative-anchor / promotion-condition block; state that the sign reading was
audited (this report) and positively anchored at `integrator.hpp:217` + `mixedvecgrad.cpp:202`.
Keep the "no dedicated unit test" note but soften it (the `test-libceed.cpp:905-916`
integrator cross-validation is now cited as supporting test evidence).

### Edit 4 (REQUIRED — substantive semantic clarification) — address the irrotational/divfree doc tension
The `Mult` doc (`divfree.hpp:64-66`) calls the output the "irrotational portion ... satisfying
`∇ × y = 0`", while the class doc (`:29`) and the `:177` comment ("irrotational portion ...
and subtract") frame the projector as computing the *divergence-free* component. Add a one-
sentence Semantics note: the apply OVERWRITES `y` with `y + Grad·ψ` where `Grad·ψ` is the
*irrotational correction added back*, so the net mutated `y` is the divergence-free remainder
(class doc `:29`), while the `Mult` doc comment `:64-66` describing "the irrotational portion"
is **stale/misleading relative to the implemented behavior** (the code computes and ADDS the
gradient correction with `+1.0`, but because `WeakDiv` carries the `-1.0` sign, the net effect
removes the gradient part — yielding the divergence-free field, matching `:29` not `:64-66`).
This is a documentation inconsistency IN Palace, worth a one-line note + an `open-questions`
breadcrumb; it does NOT change the L1 semantics (which match the class-doc divergence-free
target and the eigensolver use as a divergence-free projector).

### Edit 5 (anchor hygiene, carry-forward) — tighten three off-by-one anchors
- `:141` → `:142` for "abs-tol = machine epsilon" (two occurrences: Idempotence bullet and the
  parenthetical at the end of the abs-tol note). Confirmed: `SetAbsTol` is `:142`.
- `divfree.hpp:68-72` → `:67-71` for the out-of-place `Mult(x,y)` body (the `{ y=x; Mult(y); }`
  block). The `Mult(x,y)` declaration opens at `:67`.
- `divfree.hpp:28-31` → `:27-30` for the class-doc block IF tightening is desired (the literal
  `Gᵀ M x = 0` line is `:29`); the enclosing `:28-31` is acceptable, low priority.

## Supporting evidence

- `palace/linalg/divfree.cpp:43-152` — full construction read; pin (`:51-81`), M (`:84-110`),
  WeakDiv (`:111-116`, integrator `:113`), Grad (`:117`), SPD note (`:119`), ksp (`:121-149`,
  `SetOperators(*M,*M)` `:147`).
- `palace/linalg/divfree.cpp:154-187` — full apply read; the additive `Grad->AddMult(...,1.0)`
  at `:180-181` (complex) / `:185` (real); the `:177` "subtract" comment.
- `palace/linalg/divfree.hpp:20-72` — class doc `:27-30` (`Gᵀ M x = 0`), field comment `:51`
  (`(Gᵀ M G) y = x`), Mult doc `:63-65` (irrotational / `∇×y=0`), out-of-place body `:67-71`.
- `palace/fem/integrator.hpp:217-226` — the Palace-owned WeakDiv integrator + its
  `a(u,v) = -(Q u, grad v)` doc.
- `palace/fem/integ/mixedvecgrad.cpp:142,148-205` — the `-1.0` sign (`:202`) vs. the
  non-negated gradient integrator (`:142`).
- `palace/drivers/eigensolver.cpp:262` — `divfree->Mult(v0)` consumer.
- `test/unit/test-libceed.cpp:905-916` — integrator cross-validation against MFEM.

## Open questions / caveats

- **OQ `divfree-weakdiv-sign-convention-l0-verify` is RESOLVED by this audit.** The sign is
  positively anchored in Palace source (`integrator.hpp:217` + `mixedvecgrad.cpp:202`); it is
  NOT below the L0 boundary. The cycle-013 framing ("rests on MFEM-vendored internals, out of
  scope") was a mislocalization — Palace owns the integrator. The follow-up dispatch should mark
  this OQ closed when enacting Edits 1-3.
- **NEW open question (file a breadcrumb): `divfree-mult-doc-irrotational-vs-divfree-stale`.**
  The `Mult` doc comment `divfree.hpp:64-66` ("the irrotational portion ... `∇×y=0`") describes
  the output as curl-free, contradicting the class doc `:29` (divergence-free, `Gᵀ M x = 0`)
  and the actual computed result. This is a Palace-internal doc inconsistency, not an L1
  semantic ambiguity. Edit 4 records it; recommend an `open-questions.md` append, not a
  blocker. The implemented semantics (divergence-free output, per `:29` + eigensolver use)
  are unambiguous.
- **Promotion is GATED, not enacted by me** (per role discipline + the cycle-012
  `partly-constructive` invariant): I have confirmed the structure AND identified the exact
  firming edits (Edits 1-5), but I leave the `## Status` line `partly-constructive`. A
  follow-up abstractor dispatch (cycle-014 repair/integrate or cycle-015) applies Edits 1-5,
  THEN flips Status to `firm` and closes the OQ.
- **Direction-of-definition**: the theme narrates the L1 form forward (mutation-lifted pure
  function, with L0 reintroduction flagged as an L1>L0 concern) — no high→low violation.
- **Carry-forward citation corrections** (Edit 5) are bounded, evidenced anchor fixes within
  audit scope per `lifter-scope-content-correction-boundary`; routed to the follow-up dispatch.
