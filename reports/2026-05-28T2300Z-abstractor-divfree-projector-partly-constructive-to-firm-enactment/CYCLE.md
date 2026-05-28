---
agent: abstractor
invoked_at: 2026-05-28T2300Z
scope: L1 partly-constructive→firm enactment — divfree-projector (close the partly-constructive ENTRY→EXIT lifecycle)
status: integrated
integrated_at: 2026-05-29T0030Z
integration_commit: 1af0c3d
integration_notes: "Applied cycle-015 (per-report position 1). divfree-projector partly-constructive→firm ENACTED — first full partly-constructive ENTRY→EXIT lifecycle (entered cycle-013, UNBLOCKED cycle-014, exits firm cycle-015). WeakDiv approx -GᵀM sign positively anchored (fem/integrator.hpp:217 + fem/integ/mixedvecgrad.cpp:202). L1 firm 10->11. OQs divfree-projector-partly-constructive-to-firm-enactment + divfree-weakdiv-sign-convention-l0-verify closed. All 8 proposed-change blocks applied clean; book build clean."
inputs:
  - book/src/L1/divfree-projector.md (current partly-constructive entry + cycle-014 UNBLOCKED §Status note)
  - book/src/L1/index.md (dep-map cell for divfree-projector + Vocabulary cohort firm count)
  - reports/2026-05-28T2115Z-lowering-verifier-divfree-weakdiv-sign-convention-l0-verify/CYCLE.md (verdict UNBLOCK-PROMOTION; the 5 firming edits)
  - palace/fem/integrator.hpp:217 (re-confirmed via read_range: `// Integrator for a(u, v) = -(Q u, grad v)`)
  - palace/fem/integ/mixedvecgrad.cpp:202 (re-confirmed via read_range: `PopulateCoefficientContext(space_dim, Q, transpose, -1.0)`)
  - palace/fem/integ/mixedvecgrad.cpp:142 (re-confirmed: sibling MixedVectorGradientIntegrator, no -1.0)
---

# CYCLE: L1 partly-constructive→firm enactment — divfree-projector

## Summary

This dispatch **enacts the gated promotion** of `book/src/L1/divfree-projector.md` from
`partly-constructive` to `firm`. The entry entered `partly-constructive` (cycle-013) because
its idempotence law `P∘P = P` and divergence-free output characterization hinged on the
unverified reading `WeakDiv ≈ Gᵀ M` (up to sign), which the cycle-013 integrator believed
rested on MFEM-vendored integrator internals below the L0 boundary. The **cycle-014
lowering-verifier audit** (verdict UNBLOCK-PROMOTION) refuted that premise:
`MixedVectorWeakDivergenceIntegrator` is **Palace-owned, libCEED-backed**, its bilinear form
is documented **in Palace source** as `a(u, v) = -(Q u, grad v)` (`palace/fem/integrator.hpp:217`),
and the negating sign is materialized as an explicit `-1.0` coefficient
(`palace/fem/integ/mixedvecgrad.cpp:202`) — side-by-side contrasted with the non-negated
sibling `MixedVectorGradientIntegrator` (`palace/fem/integ/mixedvecgrad.cpp:142`, no `-1.0`).
I re-confirmed both anchors via `read_range` (the cycle-014 `:203`→`:202` drift is **not**
present here — the `-1.0` line is exactly `:202`, the `// a(u, v) = -(Q u, grad v)` doc is
exactly `:217`). The sign is therefore **positively anchored in scope**, the idempotence
sub-law's contingency is resolved, and the `partly-constructive` gate closes. I emit the 5
firming edits + the §Status flip + the L1 index dep-map cell change as proposed-changes
blocks; the per-report integrator applies them. **L1 firm count: 10 → 11.**

This **completes the partly-constructive ENTRY→EXIT lifecycle** for divfree (entered
cycle-013, exits firm cycle-015) — the first clean full-lifecycle traversal of the
cycle-012-codified `partly-constructive` status. The constructive sub-part (idempotence) was
grounded in a positive source site exactly as the codified **promotion condition**
("an upstream positive source site") prescribed.

## Anchor re-confirmation (read_range, this dispatch)

- **`palace/fem/integrator.hpp:217`** — `// Integrator for a(u, v) = -(Q u, grad v) for u in H(curl) and v in H1.` — exact at `:217`; the class `MixedVectorWeakDivergenceIntegrator` opens at `:218`, body decls through `:226`. Confirmed.
- **`palace/fem/integ/mixedvecgrad.cpp:202`** — `auto ctx = PopulateCoefficientContext(space_dim, Q, transpose, -1.0);` — exact at `:202` (read window `:138-205`; the `Assemble` body opens `:148`, sets `info.trial_ops = EvalMode::Interp` / `info.test_ops = EvalMode::Grad` at `:199-200`, then the `-1.0` populate at `:202`). Confirmed — **`:202`, not `:203`**.
- **`palace/fem/integ/mixedvecgrad.cpp:142`** — `auto ctx = PopulateCoefficientContext(space_dim, Q, transpose);` (the sibling `MixedVectorGradientIntegrator`, NO `-1.0`) — exact at `:142`. The deliberate sign contrast holds.

## Proposed changes

### Edit 1 — add the positive sign anchor to the `P.WeakDiv` signature bullet

```edit:book/src/L1/divfree-projector.md
  - `P.WeakDiv : LinearOperator[N_nd, N_h1]` — the ε-weighted weak-divergence
    operator (Nedelec → H1), from a `MixedVectorWeakDivergenceIntegrator`,
    partially assembled (`palace/linalg/divfree.cpp:111-116`). The negating sign
    of the weak-divergence form is set in Palace source: the integrator's
    bilinear form is `a(u, v) = -(ε u, ∇v)` for `u ∈ H(curl)`, `v ∈ H1`
    (`palace/fem/integrator.hpp:217`), materialized as an explicit `-1.0`
    coefficient in the assemble body
    (`palace/fem/integ/mixedvecgrad.cpp:202`) — contrast the non-negated
    `MixedVectorGradientIntegrator` (`palace/fem/integ/mixedvecgrad.cpp:142`,
    no `-1.0`). Thus `WeakDiv = -Gᵀ` (ε-weighted), a positive Palace source
    site. Read-only.
```

(Replaces the current bullet:
```
  - `P.WeakDiv : LinearOperator[N_nd, N_h1]` — the ε-weighted weak-divergence
    operator (Nedelec → H1), from a `MixedVectorWeakDivergenceIntegrator`,
    partially assembled (`palace/linalg/divfree.cpp:111-116`). Read-only.
```
)

### Edit 2 — rewrite the Idempotence law to "confirmed", drop the `partly-constructive` sub-law tag and the Caveat paragraph

```edit:book/src/L1/divfree-projector.md
- **Idempotence (projector law).**
  `P∘P = P` in exact arithmetic: applying the
  projector to an already-divergence-free field returns it unchanged. By the
  defining condition `Gᵀ M (P·y) = 0`
  (`palace/linalg/divfree.hpp:28-31`), `P·y` lies in the divergence-free
  subspace, so `WeakDiv·(P·y) = 0` (step 1 yields zero residual), hence the
  correction `Grad·ψ = 0` and `P·(P·y) = P·y`. The identification of `WeakDiv`
  with the (negated) `Gᵀ M` of the defining condition is anchored in Palace
  source — the weak-div bilinear form is `a(u,v) = -(ε u, ∇v)`
  (`palace/fem/integrator.hpp:217`) with the `-1.0` set at
  `palace/fem/integ/mixedvecgrad.cpp:202` (contrast the non-negated
  `MixedVectorGradientIntegrator`, `palace/fem/integ/mixedvecgrad.cpp:142`) —
  so the derivation is unconditional in exact arithmetic. Holds modulo `ksp`
  tolerance: `Gᵀ M (P·y) = 0` only up to the convergence tolerance on the
  non-essential dofs (`palace/linalg/divfree.cpp:140,142`, rel-tol set at :140,
  abs-tol = machine epsilon at :142).
```

(Replaces the current Idempotence bullet — note the header changes from
`**Idempotence (projector law) — \`partly-constructive\` sub-law; see Status.**`
to `**Idempotence (projector law).**`, and the entire "**Caveat (added on repair):**"
trailing paragraph that hedged the contingency on the WeakDiv-sign OQ is removed;
the `:140-142` "abs-tol = machine epsilon at :141" anchor is corrected to `:140,142`
with abs-tol at `:142`.)

### Edit 3 — rewrite the "Non-law (load-bearing): sign convention" bullet to positively-anchored

```edit:book/src/L1/divfree-projector.md
- **Non-law (load-bearing): sign convention.** The correction is *additive*
  (`y + Grad·ψ`) because `WeakDiv` (built from
  `MixedVectorWeakDivergenceIntegrator`, `palace/linalg/divfree.cpp:113`)
  internally absorbs the minus sign of the weak divergence form: its bilinear
  form is `a(u,v) = -(ε u, ∇v)` (`palace/fem/integrator.hpp:217`), the `-1.0`
  materialized at `palace/fem/integ/mixedvecgrad.cpp:202` (versus the
  non-negated `MixedVectorGradientIntegrator`,
  `palace/fem/integ/mixedvecgrad.cpp:142`). A flipped L0 sign would invert the
  correction direction. This is a property of the constructed `WeakDiv`
  operator, honored verbatim at L1 and **positively re-derived from Palace
  source** (cycle-014 lowering-verifier audit; the `WeakDiv = -Gᵀ` reading is
  anchored, not inferred).
```

(Replaces the current bullet, which ended "...honored verbatim at L1, **not
independently re-derived** — see Open questions for the unverified-integrator-sign
caveat." The "not independently re-derived" hedge and the forward-pointer to the
unverified-sign caveat are removed.)

### Edit 4 — add the irrotational/divfree doc-tension Semantics note

```edit:book/src/L1/divfree-projector.md
The mathematical projector is `P = I − Grad (Gᵀ M G)⁻¹ Gᵀ M` (the M-orthogonal
projection onto the divergence-free subspace). The materialized form computes
the *complementary* gradient component and the **sign convention** of `WeakDiv`
makes the correction *additive* (`y + Grad·ψ`, not `y − Grad·ψ`): the apply
overwrites `y` with `y + Grad·ψ` where `Grad·ψ` is the gradient correction added
with `+1.0` (`palace/linalg/divfree.cpp:185`), but because `WeakDiv` carries the
negating `-1.0` sign (`palace/fem/integ/mixedvecgrad.cpp:202`), the net effect
*removes* the gradient part — yielding the divergence-free remainder matching the
class doc `Gᵀ M y' = 0` (`palace/linalg/divfree.hpp:28-31`). The `Mult` doc
comment `palace/linalg/divfree.hpp:64-66` describing the output as "the
irrotational portion ... satisfying ∇ × y = 0" is **stale/misleading relative to
the implemented behavior** (a Palace-internal documentation inconsistency, OQ
`divfree-mult-doc-irrotational-vs-divfree-stale`); the implemented and L1
semantics are the divergence-free target of the class doc. See Algebraic laws.
```

(Replaces the current paragraph ending "...makes the correction *additive*
(`y + Grad·ψ`, not `y − Grad·ψ`): see Algebraic laws and Open questions." —
inserting the doc-tension clarification while preserving the forward references.)

### Edit 5 — rewrite `## Status` to `firm` (drop the partly-constructive block + the UNBLOCKED blockquote)

```edit:book/src/L1/divfree-projector.md
## Status

`firm`.

The **structural decomposition is firm**: every step of the apply is read from a
positive source site (`palace/linalg/divfree.cpp:155-186`), the construction is
fully read (`palace/linalg/divfree.cpp:43-152`), and the linearity, range,
M-orthogonality, real-linearity, idempotence, and step-ordering laws follow from
the defining condition stated in the source (`palace/linalg/divfree.hpp:28-31`)
and the SPD/real properties asserted in the source
(`palace/linalg/divfree.cpp:119`).

The entry was `partly-constructive` (cycle-013) on one named sub-part — the
**idempotence law `P∘P = P`** and the **divergence-free output characterization**,
both contingent on the `WeakDiv ≈ -Gᵀ M` sign reading. The **cycle-014
lowering-verifier audit**
(`reports/2026-05-28T2115Z-lowering-verifier-divfree-weakdiv-sign-convention-l0-verify/`,
verdict **UNBLOCK-PROMOTION**) **resolved that contingency at the evidence level**:
the sign is positively anchored in Palace-owned source. The cycle-013 framing
("rests on the MFEM-vendored `MixedVectorWeakDivergenceIntegrator`, below the L0
scope boundary") was a mislocalization — `MixedVectorWeakDivergenceIntegrator` is
**Palace-owned, libCEED-backed** (`palace/fem/integrator.hpp:218-226`), its
bilinear form is documented **in Palace source** as `a(u, v) = -(Q u, grad v)`
(`palace/fem/integrator.hpp:217`), and the negating sign is materialized as an
explicit `-1.0` coefficient
`PopulateCoefficientContext(space_dim, Q, transpose, -1.0)`
(`palace/fem/integ/mixedvecgrad.cpp:202`) — side-by-side contrasted with the
non-negated `MixedVectorGradientIntegrator`
(`palace/fem/integ/mixedvecgrad.cpp:142`, no `-1.0`), and cross-validated against
MFEM (`test/unit/test-libceed.cpp:905-916`). The `WeakDiv = -Gᵀ M` reading is
therefore unconditional, the idempotence sub-law and divergence-free
characterization are now firm, and the entry **promotes to `firm`** (cycle-015
enactment; OQ `divfree-projector-partly-constructive-to-firm-enactment` closed,
OQ `divfree-weakdiv-sign-convention-l0-verify` resolved).

No dedicated unit test exists (`test/unit/test-divfree.cpp` is absent; confirmed
by codemap call-site survey — only `divfree.cpp`-internal `Mult` calls and the
`eigensolver.cpp` / `arpack.cpp` / `slepc.cpp` driver call sites appear). The
test absence does not block `firm` (cf. the
[`chebyshev-smoother`](./chebyshev-smoother.md) precedent, where every law is a
verified-exact syntactic identity): the projector's semantics are a fully-read
linear projection with a source-stated defining condition, and the previously
sign-contingent sub-law is now positively anchored. Supporting test evidence: the
`MixedVectorWeakDivergenceIntegrator` is cross-validated against
`mfem::MixedVectorWeakDivergenceIntegrator` at `test/unit/test-libceed.cpp:905-916`
(L0-equivalent integrator-level coverage that exercises the sign behavior).
```

(Replaces the entire current `## Status` section — the `partly-constructive`
declaration, the Constructive-sub-part / Negative-anchor / Promotion-condition
bullet block, the `> UNBLOCKED by the cycle-014 lowering-verifier audit`
blockquote, and the closing test-absence paragraph — with the firm version above.)

### Edit 6 — append the two sign anchors + supporting evidence to `## Evidence`

```edit:book/src/L1/divfree-projector.md
- `palace/fem/integrator.hpp:217` — `// Integrator for a(u, v) = -(Q u, grad v)
  for u in H(curl) and v in H1.` (the weak-div bilinear form; the negating sign
  in Palace source).
- `palace/fem/integrator.hpp:218-226` — `class MixedVectorWeakDivergenceIntegrator`
  (Palace-owned, libCEED-backed — NOT MFEM-vendored).
- `palace/fem/integ/mixedvecgrad.cpp:202` — `PopulateCoefficientContext(space_dim,
  Q, transpose, -1.0)` (the `-1.0` materializing the weak-divergence sign).
- `palace/fem/integ/mixedvecgrad.cpp:142` — sibling `MixedVectorGradientIntegrator`
  with NO `-1.0` (the side-by-side sign contrast).
- `palace/linalg/divfree.hpp:51` — `// Linear solver for the projected linear
  system (Gᵀ M G) y = x.` (the conceptual normal-equations form; the apply solves
  against `M`).
- `test/unit/test-libceed.cpp:905-916` — Palace's `MixedVectorWeakDivergenceIntegrator`
  cross-validated against `mfem::MixedVectorWeakDivergenceIntegrator` (L0-equivalent
  test evidence that the sign behavior is exercised).
```

(Appended to the existing `## Evidence` bullet list, after the
`palace/linalg/arpack.cpp ... slepc.cpp` driver-call-site bullet and before the
slice-corpus-precedent paragraph.)

### Edit 7 — L1 index dep-map cell: `partly-constructive` → `firm`

```edit:book/src/L1/index.md
| [`divfree-projector`](./divfree-projector.md) | `(P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) → Field[N_nd]` | `ksp_solve` (direct, inner H1 solve), `apply_linop` (WeakDiv·y, Grad·ψ), `axpy` (gradient correction); `set_subvector_zero` (concept) | `firm` (constructed-operator gate; L0: `palace/linalg/divfree.cpp:155-186`; harvested cycle-013, promoted partly-constructive→firm cycle-015; WeakDiv-sign positively anchored `palace/fem/integrator.hpp:217` + `palace/fem/integ/mixedvecgrad.cpp:202`) |
```

(Replaces the current row, which read `... | partly-constructive (constructed-operator
gate; L0: palace/linalg/divfree.cpp:155-186; harvested cycle-013; structure firm,
idempotence sub-law contingent on WeakDiv-sign OQ divfree-weakdiv-sign-convention-l0-verify
— promotion: verify-citation-range on MixedVectorWeakDivergenceIntegrator) |`.)

### Edit 8 — L1 index Vocabulary cohort: firm count 10 → 11, add the divfree-projector firm bullet

```edit:book/src/L1/index.md
**Firm (11)** — element-wise updates, BLAS-1 reductions, the opaque-operator gate, the constructed-operator solve gate, the polynomial-smoother gate, and the divergence-free projector gate:
```

(Replaces `**Firm (10)** — ... and the polynomial-smoother gate:`.)

Append to the firm cohort bullet list (after the `chebyshev-smoother` bullet):

```edit:book/src/L1/index.md
- [`divfree-projector`](./divfree-projector.md) — pure-functional divergence-free projector `y' = divfree_project(P, y)` over an H(curl) Nedelec field; the fourth constructed-operator gate at L1 (after `ksp_solve`, `eigsolve`, `chebyshev-smoother`), and the first whose constructed-operator argument *carries another constructed-operator* (`P.ksp : Solver[P.M]`) as a sub-field. Realizes the discrete Helmholtz decomposition `P = I − Grad(GᵀMG)⁻¹GᵀM`. Promoted partly-constructive→firm cycle-015: the idempotence sub-law's WeakDiv-sign contingency was resolved by the cycle-014 lowering-verifier audit (sign positively anchored `palace/fem/integrator.hpp:217` + `palace/fem/integ/mixedvecgrad.cpp:202`) — the first full partly-constructive ENTRY→EXIT lifecycle traversal (entered cycle-013, exits firm cycle-015).
```

## Status of this enactment

The constructive sub-part (idempotence law `P∘P = P` + divergence-free output
characterization) is now grounded in a **positive Palace source site**
(`palace/fem/integrator.hpp:217` + `palace/fem/integ/mixedvecgrad.cpp:202`), so the
cycle-012-codified **promotion condition** ("an upstream positive source site") is met.
The `partly-constructive` gate closes; the entry's status flips to **`firm`**.

This is the first complete partly-constructive **ENTRY→EXIT** lifecycle (entered cycle-013,
unblocked cycle-014, exits firm cycle-015) — clean evidence for the batch-3 meta-phase that
`partly-constructive` is a *transient gate*, not a permanent escape hatch.

## Open questions / caveats

- **OQ `divfree-projector-partly-constructive-to-firm-enactment` — CLOSED by this dispatch.**
  The 5 firming edits (now 8 proposed-changes blocks, splitting the index dep-map / cohort
  edits out) are emitted; the per-report integrator applies them and the status flips to
  `firm`. Mark this OQ closed when integrated.
- **OQ `divfree-weakdiv-sign-convention-l0-verify` — RESOLVED** (by the cycle-014 audit; this
  dispatch consumes the resolution). The sign is positively anchored
  (`palace/fem/integrator.hpp:217` + `palace/fem/integ/mixedvecgrad.cpp:202`), not below the
  L0 boundary. Confirm closed if not already closed by cycle-014 integration.
- **OQ `divfree-mult-doc-irrotational-vs-divfree-stale` — surfaced (carry-forward, NOT a
  blocker).** The `Mult` doc comment `palace/linalg/divfree.hpp:64-66` ("the irrotational
  portion ... ∇×y=0") describes the output as curl-free, contradicting the class doc `:29`
  (divergence-free, `Gᵀ M x = 0`) and the actual computed result. This is a Palace-internal
  documentation inconsistency, not an L1 semantic ambiguity; Edit 4 records it in-line. The
  integrator should ensure this OQ exists in `scaffolding/open-questions.md` (the cycle-014
  audit recommended filing it). It does NOT block the firm promotion.
- **Anchor hygiene applied:** the `:141`→`:142` off-by-one for "abs-tol = machine epsilon"
  is corrected in Edit 2 (now `:140,142` with abs-tol at `:142`). The `divfree.hpp:68-72` →
  `:67-71` out-of-place-`Mult` body correction and the `:28-31` → `:27-30` class-doc tighten
  flagged by the cycle-014 audit's Edit 5 are **low-priority, non-load-bearing**, and lie in
  the §Context / §Evidence prose I did not otherwise touch; I leave them for a lifter/repairer
  anchor-hygiene pass to avoid out-of-scope prose churn in a status-flip enactment. They do
  not affect the firm verdict.
- **Direction-of-definition:** all edits preserve the high→low discipline — the L1 entry
  narrates the pure-functional form forward; the WeakDiv-sign anchors are L0 evidence cited in
  support of an L1 algebraic law (idempotence), not an L0-vocabulary definition of the L1
  operator. No high→low violation.
