---
agent: lowering-verifier
invoked_at: 2026-05-28T19:33:25Z
scope: chebyshev-lowering-themes-lowering-verifier-followup — audit two firm cycle-013 chebyshev lowering themes (L1>L0 smoother-mutation-rotation + L2>L1 iteration-fusion) against palace/linalg/chebyshev.{hpp,cpp}
status: integrated
integrated_at: 2026-05-29T003000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-014 position 3/8. Verdicts L1>L0 CONFIRMS-WITH-REFINEMENT + L2>L1 CONFIRMS; both themes UPHELD firm. Applied repairer-corrected anchor refinements (verifier's own :191→:190 signature + hpp:43→:44 member drift corrected) in BOTH prose + Verified-against of L1-L0/chebyshev-smoother-mutation-rotation.md (R1/R1b/R2/R3) + L2-L1/chebyshev-iteration-fusion.md (R4), plus verified_against YAML on both. Firm L1/L2 anchor entries NOT touched — element-kernel :69-78/:114-123 + :191→:190 six-site reconcile routed to cycle-015 OQ chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep. Build clean."
inputs:
  - book/src/L1-L0/chebyshev-smoother-mutation-rotation.md
  - book/src/L2-L1/chebyshev-iteration-fusion.md
  - palace/linalg/chebyshev.cpp (read_range :1-300 exhaustive)
  - palace/linalg/chebyshev.hpp (read_range :1-160 exhaustive)
  - palace/linalg/gmg.cpp:48-62, palace/linalg/distrelaxation.cpp:18-40 (consumers)
  - book/src/L1/chebyshev-smoother.md, book/src/L2/chebyshev-iteration.md (L1/L2 anchors)
---

# CYCLE: Audit chebyshev-lowering-themes (L1>L0 + L2>L1)

## Summary

Audited the two firm cycle-013 chebyshev lowering themes against
`palace/linalg/chebyshev.{hpp,cpp}` via independent `read_range` of the full source
(no transcription from the artifacts under audit). Both themes are **substantively
correct**: the L1>L0 smoother-mutation-rotation faithfully captures the output-arg
mutation idiom, the four sub-patterns (application / forwarding / transpose-alias /
construction), the `dinv` diagonal-scaling coupling, and the two-class variant
treatment; the L2>L1 iteration-fusion correctly identifies the resolution-collapse of
the per-degree three-term recurrence into the closed-form polynomial token, and the
fusion is algebraically sound (it is the L2 entry's already-firm law 1, not
hand-waved). The element-kernel coefficient/diagonal-scaling couplings are exact.

**Verdicts:**
- `chebyshev-smoother-mutation-rotation` (L1>L0): **CONFIRMS-WITH-REFINEMENT** — two
  citation-range drifts (4th-kind `Mult2` start foreign-brace at `:188`, canonical
  signature-to-close is `:190-220`; 4th-kind `SetOperator` end undershoot at `:186`)
  plus a minor 1st-kind `SetOperator` end overshoot, and an off-by-one `hpp:43`→`:44`
  miscitation for `mutable VecType d, r;`. No semantic defect.
- `chebyshev-iteration-fusion` (L2>L1): **CONFIRMS** — all four `verified_against`
  ranges land exactly (the element kernels carry the cycle-013-repaired `:68-78` /
  `:112-123`); the fusion semantics are sound. One inherited-anchor drift noted as a
  carry-forward against the L1/L2 anchor entries (not this theme's text).

No `REFUTES`. No partly-constructive caveat is warranted on either theme (both are
syntactic identities on fully-specified source; correctly distinguished from the
eigsolve `LinearSolveFailed` partly-constructive sub-part).

## Per-citation audit

### Theme 1 — chebyshev-smoother-mutation-rotation (L1>L0)

- **Citation**: `palace/linalg/chebyshev.cpp:188-220` (Sub-pattern A / Verified-against — 4th-kind `Mult2`)
  - **Theme claim**: the `pc_it` outer sweep, the `initial_guess` branch, in-place `y += d` / `y = 0.0`, scribbled `r`/`d`, `ApplyOrder0`/`ApplyOrderK` diagonal-scaled passes.
  - **Found**: 4th-kind `Mult2` is `template`@189, signature@**190** (`void ChebyshevSmoother<OperType>::Mult2(...)`), body `{`@191, function close `}`@220. Line **188 is the closing `}` of the preceding `SetOperator`**. (CORRECTION per cycle-014 repairer + critic: this report's original "signature@191" was wrong — line 191 is the opening brace; the signature is line **190**, verified via `read_range :185-200`.) All claimed body facts (the `for it < pc_it`, the `if (this->initial_guess || it > 0)` → `ApplyOp(*A,y,r); AXPBY(1,x,-1,r)` else `r=x; y=0.0`, `ApplyOrder0(4.0/(3.0*lambda_max),...)`, the `k`-loop with `y += d; ApplyOp(*A,d,r,-1.0)` + `sd=(2k-1)/(2k+3)`, `sr=(8k+4)/((2k+3)*lambda_max)` + `ApplyOrderK`, final `y += d`) are present and exact.
  - **Verdict**: supports (content) / **out-of-range start**. Range should be `:190-220` (signature-to-close) — `:189-220` includes the template line. `:188` pulls in the prior function's closing brace.
  - **Notes**: The L1 anchor and L2 anchor cite this construct as `:191-220`, which itself starts at the opening brace (excludes the signature@190); the canonical signature-to-close range is `:190-220`. The smoother theme carries the `:188` start (foreign brace). The L1/L2 anchor `:191-220` should also reconcile to `:190-220` — flagged as carry-forward below.

- **Citation**: `palace/linalg/chebyshev.cpp:261-293` (Sub-pattern A / Verified-against — 1st-kind `Mult2`)
  - **Theme claim**: identical scaffold, 1st-kind scalars.
  - **Found**: 1st-kind `Mult2` signature@261 (`void ChebyshevSmoother1stKind<OperType>::Mult2(...)` wrapping to 262), function close `}`@293. The `ApplyOrder0(1.0/theta,...)`, `rhop = delta/theta`, `rho = 1.0/(2.0*theta/delta - rhop)`, `sd = rho*rhop`, `sr = 2.0*rho/delta`, `rhop = rho` are all present.
  - **Verdict**: **supports** (range exact).

- **Citation**: `palace/linalg/chebyshev.hpp:43` (`mutable VecType d, r;`)
  - **Theme claim**: the two scribbled workspaces; `d` member, `r` passed.
  - **Found**: line **43** = `// Temporary vector for smoother application.` (comment); line **44** = `mutable VecType d, r;` (4th-kind member). (CORRECTION per cycle-014 repairer + critic: this report's original "line 43 = `mutable VecType d, r;` Exact" was an off-by-one miscitation that re-asserted the audited theme's own `hpp:43` defect; verified via `read_range :40-48`.) The member is at `:44`; cite `:44` (or `:43-44` to include the explanatory comment).
  - **Verdict**: supports (content at `:44`) / **off-by-one miscitation**. The audited theme (`chebyshev-smoother-mutation-rotation.md`) carries `hpp:43`; corrected range is `:44`.

- **Citation**: `palace/linalg/chebyshev.hpp:50-58` (`Mult` resize-forward), `:71` (`Mult2` decl), `:60-68` (`MultTranspose`), `:73-76` (`MultTranspose2` alias)
  - **Theme claim**: `Mult` resizes member `r`, forwards to `Mult2`; `MultTranspose2(x,y,r){ Mult2(x,y,r); }` ("Assumes operator symmetry").
  - **Found**: 4th-kind class: `Mult`@50-58, `MultTranspose`@60-68, `Mult2` pure-virtual decl@71, `MultTranspose2`@73-76 with `Mult2(x, y, r);  // Assumes operator symmetry`. All exact.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/chebyshev.cpp:169-186` (Sub-pattern D — 4th-kind `SetOperator`)
  - **Theme claim**: capture `A`, `AssembleDiagonal(dinv); dinv.Reciprocal()`, `lambda_max = sf_max * GetLambdaMax(...)`, `MFEM_VERIFY(lambda_max > 0.0, …)`.
  - **Found**: 4th-kind `SetOperator` is `template`@169, signature@170, body `{`@172, the `A=&op`/`d.SetSize`/`dinv.SetSize`/`AssembleDiagonal`/`Reciprocal`/`lambda_max = sf_max * GetLambdaMax`/`MFEM_VERIFY(lambda_max>0.0)`@183-184/`this->height`/`this->width`, close `}`@**188**. The cited end `:186` lands on `this->height = op.Height();` (line 186) — **undershoots the function by 2 lines** (misses `this->width`@187 and close@188). All claimed content IS within the cited range (the MFEM_VERIFY is @183-184, inside `:169-186`).
  - **Verdict**: supports (content) / **end undershoot**. Range should be `:169-188` (template-to-close) — the L1 anchor cites this as `:170-189` (sig + 1 trailing blank) and `:161-189` (ctor+SetOperator). Reconcile to `:169-188`.

- **Citation**: `palace/linalg/chebyshev.cpp:232-259` (Sub-pattern D — 1st-kind `SetOperator`)
  - **Theme claim**: same scaffold + `sf_min` default, `theta`, `delta`.
  - **Found**: 1st-kind `SetOperator` `template`@232, sig@233, the `sf_min <= 0.0` default `1.69/(std::pow(order,1.68)+2.11*order+1.98)`, `lambda_max = sf_max*GetLambdaMax`, `MFEM_VERIFY`@250-251, `lambda_min = sf_min*lambda_max`, `theta = 0.5*(lambda_max+lambda_min)`, `delta = 0.5*(lambda_max-lambda_min)`, `this->height`/`width`, close `}`@**258**. Cited end `:259` is one past close (259 is blank).
  - **Verdict**: supports (content) / **end overshoot by 1** (cosmetic). Range should be `:232-258`.

- **Citation**: `palace/linalg/chebyshev.cpp:13-27` (`GetLambdaMax` real + complex)
  - **Theme claim**: `DinvA = Dinv·A`; `linalg::SpectralNorm(comm, DinvA, hermitian)`; real overload passes literal `true` (`:13-18`); complex passes `A.IsReal()` (`:20-27`).
  - **Found**: real overload @14-19 (`DiagonalOperator Dinv(dinv); ProductOperator DinvA(Dinv, A); return linalg::SpectralNorm(comm, DinvA, true);`); complex @21-27 (`return linalg::SpectralNorm(comm, DinvA, A.IsReal());`). The `:13-27` envelope and the `true`/`A.IsReal()` distinction are correct (the literal `true` is on line 18, `A.IsReal()` on line 27 — both inside the cited sub-ranges).
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/chebyshev.cpp:161-167` / `:223-230` (ctors, `MFEM_VERIFY(order > 0)`)
  - **Found**: 4th-kind ctor sig@161, `MFEM_VERIFY(order > 0, ...)`@166, close@167. 1st-kind ctor sig@223, `MFEM_VERIFY(order > 0)`@229, close@230. Both exact.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/chebyshev.cpp:295-299` (element-type instantiations)
  - **Found**: `template class ChebyshevSmoother<Operator>;`@295, `<ComplexOperator>`@296, `ChebyshevSmoother1stKind<Operator>`@298, `<ComplexOperator>`@299. Exact.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/gmg.cpp:52-59` (consumer kind choice)
  - **Found**: `if (cheby_4th_kind)`@51, `ChebyshevSmoother<OperType>` construct@53-54, `else`/`ChebyshevSmoother1stKind` construct@57-58. The `:52-59` range covers the kind-branch (start@52 is one inside the `if`, acceptable framing).
  - **Verdict**: **supports** (range frames the construct; minor — `if` opens @51, but the construct body is fully inside `:52-59`).

- **Citation**: `palace/linalg/distrelaxation.cpp:21-36` / `:36` (`B_G->SetInitialGuess(false)`)
  - **Found**: `B_G->SetInitialGuess(false);` is at line **36**. Exact. The `:21-36` envelope covers the smoother construction + the `SetInitialGuess(false)` call.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/chebyshev.cpp:101-110, :150-159` (dead-code complex transpose kernels — Open questions)
  - **Found**: `ApplyOrder0` complex overload spans ~80-110 (the `Transpose` `else` branch `DR[i] = sr*(DIR*RR+DII*RI)` etc. is @101-110); `ApplyOrderK` complex `else` transpose branch is @150-159 (within the 125-156+ complex `ApplyOrderK`). The conjugate-`dinv` transpose forms exist and are unreachable under `MultTranspose2 → Mult2`. Claim is accurate.
  - **Verdict**: **supports** (correctly flagged as defined-not-used recognition rules).

### Theme 2 — chebyshev-iteration-fusion (L2>L1)

- **Citation**: `palace/linalg/chebyshev.cpp:188-220` (Verified-against — 4th-kind `Mult2`, the recurrence L2 makes explicit / L1 fuses)
  - **Theme claim**: the `order`-step recurrence (`ApplyOrder0`, `k`-loop with `sd`/`sr` closed forms, `ApplyOrderK`, `y += d` accumulates).
  - **Found**: same as Theme-1 finding — sig@**190**, brace@191, close@220; content exact. Cited start `:188` is the prior function's close.
  - **Verdict**: supports (content) / **out-of-range start**, same drift as Theme 1. Canonical signature-to-close `:190-220` (the L1/L2 anchor `:191-220` starts at the brace). (NOTE: this theme's own §Semantics-derivation citations in the body cite `:194-219` for the 4th-kind *sweep body* — exact — and `:261-293` for 1st-kind. Only the Verified-against block carries `:188`.)

- **Citation**: `palace/linalg/chebyshev.cpp:261-293` (Verified-against — 1st-kind `Mult2`)
  - **Found**: sig@261, close@293. Exact.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/chebyshev.cpp:68-78` (`ApplyOrder0` real — secondary fusion `d ← sr·dinv·r`)
  - **Theme claim**: element-fused initial-direction kernel `d ← sr·dinv·r`.
  - **Found**: `ApplyOrder0` real overload: `template`@67, signature `inline void ApplyOrder0(double sr, const Vector &dinv, const Vector &r, Vector &d)`@68, the `mfem::forall_switch(... { D[i] = sr * DI[i] * R[i]; })`@77, close `}`@78. The `:68-78` (sig-to-close) is **exact**, matching the dispatch prompt's "cycle-013 repaired ApplyOrder0 `:68-78`".
  - **Verdict**: **supports** (this is the repaired range).

- **Citation**: `palace/linalg/chebyshev.cpp:112-123` (`ApplyOrderK` real — secondary fusion `d ← sd·d + sr·dinv·r`)
  - **Theme claim**: element-fused direction-recurrence kernel `d ← sd·d + sr·dinv·r`.
  - **Found**: `ApplyOrderK` real overload: `template`@111, signature@112 (`inline void ApplyOrderK(const double sd, const double sr, const Vector &dinv, const Vector &r, Vector &d)`), the `mfem::forall_switch(... { D[i] = sd * D[i] + sr * DI[i] * R[i]; })`@122, close `}`@123. The `:112-123` is **exact**, matching the dispatch prompt's "ApplyOrderK `:112-123`".
  - **Verdict**: **supports** (repaired range).

## Applicability conditions

### Theme 1 (smoother-mutation-rotation) — 7 conditions

1. **No aliasing between `x`, `y`, `r`, `d`.** Verifiable: `Mult2` reads-and-writes `y` (`y += d`, `y = 0.0`), reads-and-writes `r` (`ApplyOp(*A,y,r)` writes, `AXPBY(1,x,-1,r)` reads+writes), reads-and-writes `d` (`ApplyOrderK` `D[i] = sd*D[i]+...`). The hpp `Mult` allocates member `r` distinct from caller `y` (`r.SetSize(y.Size())` is a separate buffer), and `d` is a distinct member. **Counter-example?** No — buffers are structurally distinct in the source.
2. **No observer of prior `y` after call.** Verifiable from `Mult2`: `y = 0.0` (no-guess first sweep) destroys prior `y`. Consumer-side property (lexical sequencing); cannot be falsified from chebyshev.cpp alone, but the claim is correctly scoped to consumer sites. **Counter-example?** N/A (consumer-dependent; correctly stated as upheld by sequencing).
3. **Closure immutability across calls.** Verifiable: `A`, `dinv`, `order`, `pc_it`, `lambda_max`/`theta`/`delta` are set once in `SetOperator` and only read in `Mult2`. `initial_guess` is `this->initial_guess` (member, set via `SetInitialGuess`, `distrelaxation.cpp:36`). **Counter-example?** No — `Mult2` is `const` and writes only `y`/`r`/`d`.
4. **Polynomial-kind is a setup-time class choice, not runtime tag.** Verifiable: `ChebyshevSmoother` and `ChebyshevSmoother1stKind` are distinct types; `gmg.cpp:51-58` chooses one at construction per `cheby_4th_kind`. **Counter-example?** No — no runtime kind branch exists in either `Mult2`.
5. **Element-type conformance.** Verifiable: `template class ...<Operator>;` and `<ComplexOperator>;`@295-299 for both kinds; `dinv` real-valued even for complex `A` (`hpp:37` `// real-valued for now` — confirmed). **Counter-example?** No.
6. **SPD operator (transpose-aliasing C).** Verifiable: `MultTranspose2 → Mult2` (hpp:73-76 `// Assumes operator symmetry`). **Counter-example?** No — alias is unconditional in source (the symmetry assumption is the documented precondition).
7. **Single-machine scope.** `comm`/`MPI_Comm` + `GetLambdaMax → SpectralNorm` read as single-rank. Correct per CLAUDE.md scope. **Counter-example?** N/A.

All 7 conditions are verifiable from the cited evidence and hold.

### Theme 2 (iteration-fusion) — 4 conditions

1. **No bit-exactness promise across fusion choices.** Verifiable: the element-fused kernels (`ApplyOrder0`/`ApplyOrderK`, single-pass FMA-shaped `D[i] = sd*D[i] + sr*DI[i]*R[i]`) are not bit-identical to an unfused `scal`+`elementwise_product`+`axpby` chain. Correctly classified as transparent-for-correctness / load-bearing-for-bit-reproduction. **Counter-example?** No — matches L2 non-law.
2. **Sequentiality preserved inside fused token.** Verifiable: the `k`-loop has `d_{k+1}` depending on `r_{k+1}` depending on `d_k` (`ApplyOp(*A, d, r, -1.0)` reads `d` writes `r`; `ApplyOrderK` reads `r` writes `d`). Genuinely sequential. **Counter-example?** No.
3. **`pc_it`-sweep sequentiality.** Verifiable: each `it`-sweep recomputes `r = x − A·y` from the post-previous-sweep `y` (the `it > 0` branch always takes `ApplyOp(*A,y,r); AXPBY(1,x,-1,r)`). **Counter-example?** No.
4. **Variant + element-type conformance.** Verifiable: primitive sequence identical across kinds (only `op.scalars` branches); element-type at primitive level. Holds for all four combinations. **Counter-example?** No.

All 4 conditions verifiable and hold.

## Algebraic laws (cited)

### Theme 1 — Sub-pattern C transpose alias (`algebraic`, = L1 law 3)

- **Law**: `chebyshev_smoother_transpose(op, …) = chebyshev_smoother(op, …)` for SPD `A`.
- **Holds on operators?** YES per source: `MultTranspose2(x,y,r) { Mult2(x,y,r); }` (hpp:73-76) forwards verbatim. The "Assumes operator symmetry" comment is the documented precondition. For the in-scope SPD-real wiring this is exact. The complex conjugate-transpose kernels (`cpp:101-110, :150-159`) exist but are dead under the symmetric alias — correctly flagged. **Holds.**

### Theme 2 — Fusion identity (`algebraic`, = L2 law 1)

- **Law**: `chebyshev_iteration(op, x, y, ig) = chebyshev_smoother(op, x, y, ig)` modulo floating-point reassociation — the explicit three-term recurrence *is* the matrix-free evaluation of `p_order(D⁻¹ A)`.
- **Holds on operators?** YES — and critically, **the fusion is NOT hand-waved**. The theme grounds the collapse in the L2 entry's already-firm law 1, and the L2 entry transcribes the exact recurrence: 4th-kind `α₀ = 4/(3·λ_max)`, `sd_k = (2k−1)/(2k+3)`, `sr_k = (8k+4)/((2k+3)·λ_max)` (source @215-216, confirmed); 1st-kind `ρ₀ = δ/θ`, `α₀ = 1/θ`, `ρ_k = 1/(2θ/δ − ρ_{k−1})`, `sd_k = ρ_k·ρ_{k−1}`, `sr_k = 2·ρ_k/δ` (source @283-287, confirmed). The closed-form polynomial token names *this* recurrence's value; the theme correctly forbids monomial re-expansion / reordering (numerically unstable; the sequential obstruction). The two-scalar-generator (4th stateless / 1st `ρ`-threaded) fusion into one `op.scalars` closure field is the correct variant-invariant-sequence framing (L2 law 2). **Holds; algebraically sound.**

## Proposed changes

Two follow-up edits routed to an **abstractor / lifter** (lowering-verifier audits, does not mutate `book/`). Both themes' `## Status` lines stay `firm` — these are citation-range refinements, not status changes. Append/update the `verified_against` block in each theme as a fenced YAML code block.

For `book/src/L1-L0/chebyshev-smoother-mutation-rotation.md` — correct the two drifting ranges in the prose citations AND the Verified-against block, then append the audit metadata:

```edit:book/src/L1-L0/chebyshev-smoother-mutation-rotation.md
[Refinement R1 — Sub-pattern A + Verified-against: 4th-kind Mult2 range `:188-220` -> `:190-220`
 (`:188` is the closing brace of the preceding SetOperator; the signature is line `:190`, brace `:191`, close `:220`.
 NOTE: the L1/L2 anchors' `:191-220` starts at the opening brace — canonical signature-to-close is `:190-220`; reconcile anchors via the carry-forward OQ below.)]
[Refinement R1b — Sub-pattern A `hpp:43` -> `hpp:44` for `mutable VecType d, r;` (`:43` is the explanatory comment; the member is `:44`. Use `:43-44` if the comment is wanted in-range.)]
[Refinement R2 — Sub-pattern D + Verified-against: 4th-kind SetOperator range `:169-186` -> `:169-188`
 (close brace is `:188`; `:186` undershoots, missing `this->width`@187 + close@188). Optionally `:170-188` to start at the signature.]
[Refinement R3 (cosmetic) — Sub-pattern D + Verified-against: 1st-kind SetOperator `:232-259` -> `:232-258` (`:259` is one past the close brace @258).]
[Then append the audit block below.]

~~~yaml
verified_against:
  - citation: palace/linalg/chebyshev.cpp:190-220
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: 4th-kind Mult2 signature-to-close; corrected from :188-220 (start was prior fn close brace; sig is :190, brace :191)
  - citation: palace/linalg/chebyshev.cpp:261-293
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
  - citation: palace/linalg/chebyshev.cpp:169-188
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: 4th-kind SetOperator; corrected from :169-186 (end undershot close @188)
  - citation: palace/linalg/chebyshev.cpp:232-258
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: 1st-kind SetOperator; corrected from :232-259 (end was 1 past close @258)
  - citation: palace/linalg/chebyshev.cpp:13-27
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: GetLambdaMax real(:18 true)/complex(:27 A.IsReal()); DinvA=Dinv*A
  - citation: palace/linalg/chebyshev.cpp:183-184
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: 4th-kind MFEM_VERIFY(lambda_max>0) setup precondition (1st-kind :250-251)
  - citation: palace/linalg/chebyshev.hpp:44
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: mutable VecType d, r (member d, passed r); corrected from :43 (:43 is the explanatory comment, member is :44)
  - citation: palace/linalg/chebyshev.hpp:50-76
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: Mult resize-forward + Mult2 decl + MultTranspose2 symmetry alias
  - citation: palace/linalg/chebyshev.cpp:295-299
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: both-kind x both-element-type instantiations
  - citation: palace/linalg/distrelaxation.cpp:36
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: B_G->SetInitialGuess(false) per-call initial_guess control (exact line 36)
  - citation: palace/linalg/chebyshev.cpp:101-110,150-159
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: dead-code complex conjugate-dinv transpose kernels (recognition rules)
~~~
```

For `book/src/L2-L1/chebyshev-iteration-fusion.md` — one Verified-against range correction + append audit metadata:

```edit:book/src/L2-L1/chebyshev-iteration-fusion.md
[Refinement R4 — Verified-against: 4th-kind Mult2 `:188-220` -> `:190-220` (same drift as Theme 1;
 signature is `:190`, brace `:191`, close `:220`; the theme's body §Semantics-derivation already uses the
 exact :194-219 for the sweep body, so only the Verified-against block needs the fix).]
[Then append the audit block below.]

~~~yaml
verified_against:
  - citation: palace/linalg/chebyshev.cpp:190-220
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: 4th-kind Mult2 recurrence (L2-explicit / L1-fused) signature-to-close; corrected from :188-220 (sig :190, brace :191)
  - citation: palace/linalg/chebyshev.cpp:261-293
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: 1st-kind Mult2 recurrence (rho-threaded)
  - citation: palace/linalg/chebyshev.cpp:68-78
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: ApplyOrder0 real (d <- sr*dinv*r); cycle-013-repaired range exact
  - citation: palace/linalg/chebyshev.cpp:112-123
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: ApplyOrderK real (d <- sd*d + sr*dinv*r); cycle-013-repaired range exact
~~~
```

## Supporting evidence

- `palace/linalg/chebyshev.cpp` — full `read_range` :1-300 (independent landing of every asserted anchor; no transcription from the audited artifacts):
  - `GetLambdaMax` real @14-19, complex @21-27 (`SpectralNorm(comm, DinvA, true)` @18 / `A.IsReal()` @27).
  - `ApplyOrder0` real @67(template)/68(sig)-78(close); complex @80-110.
  - `ApplyOrderK` real @111(template)/112(sig)-123(close); complex @125-156.
  - 4th-kind ctor @160-167 (`MFEM_VERIFY(order>0)`@166); `SetOperator` @169(template)/170(sig)-188(close), `MFEM_VERIFY(lambda_max>0)`@183-184; `Mult2` @189(template)/191(sig)-220(close).
  - 1st-kind ctor @221-230 (`MFEM_VERIFY(order>0)`@229); `SetOperator` @232(template)/233(sig)-258(close), `sf_min` default @246, `MFEM_VERIFY`@250-251, `theta`@256-equiv/`delta`; `Mult2` @260(template)/261(sig)-293(close).
  - template instantiations @295-299.
- `palace/linalg/chebyshev.hpp` — `read_range` :1-160: doc @14-20, 4th-kind members @28-44 (`dinv` `// real-valued for now`@37, comment@43, `mutable VecType d, r;`@**44**), `Mult`@50-58 / `MultTranspose`@60-68 / `Mult2` decl@71 / `MultTranspose2`@73-76; 1st-kind doc @78-85, members @86-105, `Mult`@112-120 / `MultTranspose`@126-134 / `Mult2` decl@136 / `MultTranspose2`@138-141.
- `palace/linalg/gmg.cpp:48-62` — `if (cheby_4th_kind)`@51, `ChebyshevSmoother`@53-54 / `1stKind`@57-58.
- `palace/linalg/distrelaxation.cpp:18-40` — kind branch @21-34, `B_G->SetInitialGuess(false)`@36.
- `book/src/L1/chebyshev-smoother.md`, `book/src/L2/chebyshev-iteration.md` — L1/L2 anchors; both consistent with the lowering themes' two-class variant treatment (4th-kind / 1st-kind absorbed into `op.scalars`; element-type real/complex dispatched at primitive level / `dinv` real-valued).

## Open questions / caveats

- **Inherited-anchor miscitation (carry-forward, NOT this theme's text) — ALL sites enumerated (cycle-014 critic + repairer).** The L1 anchor (`book/src/L1/chebyshev-smoother.md`) and L2 anchor (`book/src/L2/chebyshev-iteration.md`) cite the element kernels as `ApplyOrder0` `:69-78` and `ApplyOrderK` `:114-123` — the **pre-cycle-013-repair** ranges that start one line *inside* the signature (`:68`/`:112` are the signature lines; `:69`/`:114` start one line in). The fusion theme correctly carries the repaired `:68-78` / `:112-123`. The drift is NOT confined to the §Evidence block: the critic confirmed the **L2 anchor carries the drifting ranges at FOUR sites — lines 35, 143, 245, 247** — and the **L1 anchor at lines 245, 247**. A follow-up correction MUST sweep **all six occurrences**, not just the Evidence block. Additionally the L1/L2 anchor `Mult2` range `:191-220` starts at the opening brace; the canonical signature-to-close is `:190-220` (sig@190, brace@191) — reconcile the anchors' `:191`->`:190` in the same sweep. Per `lifter-scope-content-correction-boundary`, flag as a bounded carry-forward citation correction against the **anchor entries** (not the lowering themes). Route to a follow-up abstractor/lifter. Promoted to `scaffolding/open-questions.md` (cycle-014 repairer). (Skill-candidate `audit-report-inherited-miscitation-lint` precedent.)
- **`hpp:50-76` envelope over-coarsens four separately-verified constructs (cycle-014 critic note).** The Theme-1 proposed audit block compresses `:50-58` (`Mult` resize-forward), `:60-68` (`MultTranspose`), `:71` (`Mult2` pure-virtual decl — the load-bearing forwarding target), and `:73-76` (`MultTranspose2` symmetry alias) into a single `chebyshev.hpp:50-76` envelope that spans the gaps. The per-citation audit verified each separately and exactly; the envelope is coarser than what was verified. Not a falsified claim (cosmetic over-coarsening), but a follow-up may split the `verified_against` entry back into the four precise ranges to preserve audit granularity.
- **`Mult2` `:188` drift is multi-file.** The `:188-220` start appears in BOTH lowering themes' Verified-against blocks but NOT in the L1/L2 anchors (which use `:191-220`). The shared `:188` suggests a copy-forward between the two cycle-013 themes; the canonical range is `:191-220`. Corrected in both proposed-changes blocks above.
- **No `partly-constructive` caveat warranted.** Both themes are syntactic identities on fully-specified source — no negative-anchor reconstruction, no literature-inferred sub-part. The smoother theme's note that the `MFEM_VERIFY(lambda_max>0)` guard is a setup-time precondition (not a per-call error condition like eigsolve's `LinearSolveFailed`) is **correct** — confirmed @183-184 / @250-251 inside `SetOperator`, not in `Mult2`. No promotion is gated; both stay `firm` as-is.
- **`spectrum_estimate` opacity is correctly preserved.** Both themes treat `GetLambdaMax → SpectralNorm` as an opaque setup sub-action (the open `matrix-weighted-norm-and-bilinear-form` residual-cohort L1 candidate), not re-derived. This is consistent with the L1 anchor's Dependencies and imposes no caveat. Out of scope for this audit (no new L1 op proposed).
- **Directionality (high→low) check: PASS.** Both themes narrate the rewrite forward (L1>L0: "the L1 pure action dissolves into the L0 output-arg mutation idiom"; L2>L1: "the L2 recurrence collapses (fuses) upward into one named polynomial step at L1"). Reverse-direction lifting notes are correctly quarantined in §Open questions / caveats ("Lifting note (reverse direction, working notes only)"). No direction-of-definition violation.
- **No dedicated unit test** for chebyshev under `reference/palace/test/unit/` — both anchors and themes note this; coverage is via multigrid integration (`gmg.cpp`, `distrelaxation.cpp`). The cycle-012 firm-promotion was ratified keep-firm on the syntactic-identity basis. This audit does not disturb that — the themes' `firm` status is appropriate.
