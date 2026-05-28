---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T034901Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-05-28T035321Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of chebyshev-smoother (L1) + chebyshev-iteration (L2) harvest

## Critique

### Checks run

**citation-validity — warning.** Spot-checked the load-bearing ranges directly against source via `read_range`. All major transcriptions are accurate:
- The flagged `rho_0` discrepancy is **CONFIRMED**: `palace/linalg/chebyshev.cpp:282` reads `double rhop = delta / theta;` — `delta/theta`, no factor of 2. The slice at `book/src/spec/slices/chebyshev.md:160` does say `rho_0 = delta / (2*theta)`. The report's flag, isolation (only the `rho_0` initialiser differs; `alpha_0 = 1/theta` matches `:281`), and decision to use the source value are all correct. This is a clean catch of a load-bearing numerical-coefficient error in the slice.
- 4th-kind `Mult2` (`:191-220`): residual `ApplyOp(*A, y, r); AXPBY(1, x, -1, r)`, the `r=x; y=0` first-sweep branch, `ApplyOrder0(4/(3·lambda_max), …)`, the `k`-loop with `sd=(2k−1)/(2k+3)`, `sr=(8k+4)/((2k+3)·lambda_max)`, trailing `y+=d` — all verified.
- 1st-kind `Mult2` (`:261-293`): identical scaffold, `ApplyOrder0(1/theta, …)`, `rho=1/(2θ/δ−rhop)`, `sd=rho·rhop`, `sr=2·rho/delta`, `rhop=rho` — all verified.
- `ApplyOrder0` (`:69-78`) `D[i]=sr·DI[i]·R[i]` and `ApplyOrderK` (`:114-123`) `D[i]=sd·D[i]+sr·DI[i]·R[i]` — verified; the de-fusion claims (`= scal(sr, elementwise_product(dinv, r))` and `= axpby(sd, d, sr, elementwise_product(dinv, r))`) are exact.
- `GetLambdaMax` (`:13-27`), `MFEM_VERIFY(order > 0)` at `:166`/`:229`, SetOperator setups (`:161-189`, `:233-259`, including the `sf_min` default `1.69/(order^1.68+2.11·order+1.98)` and `theta/delta` derivations), element-type instantiations (`:295-299`), consumers (`gmg.cpp:52-59`, `distrelaxation.cpp:21-36` with `B_G->SetInitialGuess(false)` at `:36`), and the hpp claims (`dinv` "real-valued for now" at `:37`, `MultTranspose2 → Mult2` "Assumes operator symmetry") — all verified.

The *warning* (not pass) is for two citation-precision slips, neither algorithm-altering:
1. **`SpectralNorm` hermitian-flag overstated.** The report states `linalg::SpectralNorm(comm, DinvA, /*hermitian=*/true)` (L1 entry Dependencies, line 277; Evidence line 372; Supporting-evidence line 731). This is exact for the **real** `GetLambdaMax` overload (`:18`), but the **complex** overload (`:27`) passes `A.IsReal()`, not a literal `true`. The "always Hermitian" gloss is correct for the real path and for the in-scope SPD-real wiring, but the literal-`true` citation does not hold for the complex overload it is attached to in the `:13-27` range cite.
2. The `chebyshev.cpp:13-27` range is cited as "the opaque `spectrum_estimate` setup sub-action" — fine — but the range spans both overloads, so the literal-`true` claim should be scoped to `:18` (real) with a note that `:27` (complex) is `A.IsReal()`.

**surface-or-evidence — pass.** This is a from-scratch firm-promotion of two new operator entries (not a refinement of existing operator/theme text), so the refinement-surface gate does not bind in the modifies-surface-AND-rotation-claim sense. The report carries full surface (complete L1 + L2 chapter bodies) plus dense L0 citation evidence for every law. The L1↔L2 equivalence is asserted as the fusion-rotation identity (L2 law 1) grounded in the source recurrence rather than a bare rotation_claim. Not a pure-rotation-without-surface case.

**rotation-quality — pass.** The L1 form genuinely hides state relative to L0: it drops the in-place `Mult2(x, y, r)` output-arg mutation, the workspace scribbling of `r`/`d`, and the member-bound `lambda_max`/`theta`/`delta`, re-expressing the action as a pure `(op, x, y, initial_guess) → y'`. The two L0 template classes collapse to one closure-parameterised operator (variant hidden in `op.scalars`) — that is coarser substitution / state-hiding, not a 1:1 rename. The L2 form is strictly more equational: it unfolds the opaque `p_order(D⁻¹A)` polynomial action into the explicit named-primitive three-term recurrence and de-fuses the HPC element-fused kernels. Both edges are real rotations (mutation rotation L1, fusion rotation L2), each more abstract/equational than the form below.

**variant-axis-coverage — pass.** Two orthogonal axes are identified and each is explicitly handled: **polynomial-kind** (4th/1st) absorbed into `op.scalars` (with the (c) primitive-sequence-absorption claim and the witness that the `sweep` body does not branch on kind), and **element-type** (real/complex) dispatched at the primitive level with `dinv` real-valued. The report also explicitly scopes out the spectral-bound-estimation method (power-iteration vs SLEPc, absorbed into the opaque setup sub-action) and correctly classifies `order`/`pc_it` as construction parameters, not variant axes. No hidden branch: the one genuine control-flow branch (`initial_guess` first-sweep `r=x; y=0`) is surfaced as law 5 with the source line cite (`:201-205, :271-275`). The (c) primitive-sequence-absorption assertion is the only place to double-check at repair time — the 4th-kind scalar generator is stateless closed-form while the 1st-kind threads `rho`, so the two `op.scalars` differ in *state arity* (`S = Unit` vs `S = {rho_prev}`); the report does call this out (L2 signature, lines 465-469, and matches krylov-step.md:118), and the *primitive sequence* (the `sweep` body) is genuinely identical, so the (c) claim holds — but it is the kind of claim a future lowering-verifier should re-witness.

**cross-reference-integrity — pass.** All `[link]` targets resolve: `ksp_solve.md`, `eigsolve.md`, `apply_linop.md`, `axpy.md`, `axpby.md`, `axpbypcz.md`, `scal.md`, `krylov-step.md`, and the six concept pages (`chebyshev-iteration`, `variant-absorption`, `elementwise-product`, `sequential-obstruction`, `first-iteration-unrolling`, `derived-view-hoisting`) all exist. The two entry files under proposal (`L1/chebyshev-smoother.md`, `L2/chebyshev-iteration.md`) do not yet exist — expected for a create. Verified the two non-trivial cross-artifact claims: `krylov-step.md:7` does catalog `chebyshev.md:354-362` as a polynomial-recurrence pattern instance; `variant-absorption.md:72` does define a "(c) Primitive-sequence absorption" level; `krylov-step` variant-axis (3) (krylov-step.md:118) is indeed polynomial-kind with the `op.scalars` closure. The index-anchor claims also check out: `L1/index.md:29` says "Firm (8)" (bump to 9 is correct), the `bilinear-form` row exists at `:44`/`:69` (insertion anchor valid), and `L2/index.md` shows only `krylov-step` as firm (so "second firm L2 operator", OQ caveat 6, is accurate).

**edge-label-fidelity — pass.** No explicit `L_{n+1}→L_n` edge labels are carried (this is an operator-row harvest, not a lowering theme). The L1↔L2 relationship discussed in prose matches the layers being authored (L1 closed-form action above, L2 base-algebra unfolding below). The report is careful to scope the L1>L0 and L2>L1 lowering *themes* out (OQ caveat 5) and references the forthcoming L1>L0 theme in prose without linking a nonexistent file — correct edge discipline.

**plan-kind-consistency — warning.** The declared kind is firm for both rows. Content shape (complete signatures, full algebraic-law sets with deliberate non-laws, exhaustive evidence, no rough-in placeholders) is consistent with firm authoring. The warning is about the firm *decision* itself, not the content shape: the report lands firm despite **no dedicated unit test** (multigrid-integration coverage only), and explicitly distinguishes this from the `eigsolve` precedent (which was rough-in pending coverage) on the grounds that every law here is "a syntactic identity on fully-specified source code rather than a literature-inferred property." That reasoning is internally coherent and the source-transcription confidence is genuinely high (I verified the transcriptions are exact). However, this is a *judgment-call deviation* from the nearest constructed-operator-gate precedents — per the report's own framing, `ksp_solve` and `eigsolve` were the prior two gates and at least `eigsolve` was rough-in without a dedicated test. The firm-without-test promotion is defensible but is a policy call that an integrator should ratify against the constructed-operator-gate precedent rather than have settled silently inside a harvest. Flagging as warning so the decision surfaces to repair/integration triage, not because the content is mis-shaped.

**skill-uptake-survey — warning.** The report's shape implies several relevant skills exist but does not reference invoking them. `classify-variant-axis` is directly applicable (the report does substantial variant-axis classification work — polynomial-kind, element-type, and the (c) primitive-sequence-absorption determination) yet no invocation is recorded. `verify-citation-range` is applicable given the dense L0 citation set and the load-bearing `rho_0` coefficient check, and is not referenced. `verify-refinement-surface` is plausibly relevant to the firm-promotion gate. The Supporting-evidence section documents MCP-based localization (`list_files`/`search_text`/`find`) but no SKILL.md invocations. Pure-presence telemetry, non-blocking: the work appears to have been done correctly by hand, but the skills that exist to standardize exactly these steps were not visibly taken up.

### Issues found

1. **[citation-precision, low severity] `SpectralNorm` hermitian flag overstated as literal `true`.** L1 entry Dependencies (CYCLE.md "Operator content — L1" §Dependencies, line ~277), Evidence bullet (line ~372), and Supporting-evidence (line ~731) all render the call as `linalg::SpectralNorm(comm, DinvA, /*hermitian=*/true)`. Verified against source: the **real** `GetLambdaMax` overload (`palace/linalg/chebyshev.cpp:18`) passes literal `true`, but the **complex** overload (`:27`) passes `A.IsReal()`. Since the cited range `:13-27` spans both overloads, the literal-`true` annotation is inaccurate for the complex path. Fix: scope the `true` to the real overload (`:18`) and note `:27` is `A.IsReal()`, or soften the annotation to "Hermitian for the real/SPD-real wiring in scope."

2. **[firm-decision policy, medium severity] firm-without-dedicated-test deviates from the eigsolve constructed-operator-gate precedent.** L1 §Status (lines 324-336) and L2 §Status (lines 619-628) both land firm with the test-coverage gap recorded as a caveat rather than a status reduction, and explicitly argue this differs from `eigsolve` (rough-in pending coverage). The source-transcription-confidence argument is sound and the transcriptions verify exact, but the promotion is a judgment-call against the nearest two gate precedents (`ksp_solve`, `eigsolve`). This should be surfaced to integrator triage to ratify against the constructed-operator-gate firm-bar rather than settled inside the harvest. Candidate for repair to reframe as an explicit "firm-promotion-with-precedent-deviation, integrator to ratify" note, or for the integrator to confirm/downgrade.

3. **[witness-robustness, low severity] (c) primitive-sequence-absorption claim leans on a state-arity-difference that the variant-absorption concept explicitly calls a risk.** L2 law 2 (lines 539-545) and §Variant axes claim full (c) primitive-sequence absorption across 4th/1st kind. `variant-absorption.md:76-78` warns that differing per-step state schema can defeat (c) and may require state-schema changes. Here the two kinds differ in scalar-state arity (`S = Unit` vs `S = {rho_prev}`) but share an identical `sweep` primitive sequence — so the (c) claim does hold (the divergence is in the absorbed `op.scalars` closure's internal state, not in the `sweep` body's primitive chain). Not a defect, but the claim is exactly the pattern the concept flags for explicit witnessing; a lowering-verifier should re-confirm when the L2>L1 theme is authored. Recorded for downstream attention, not necessarily a repair item.

4. **[skill-uptake, informational] no skill invocations recorded for variant-axis classification or citation-range verification.** The report performs `classify-variant-axis`- and `verify-citation-range`-shaped work without referencing the corresponding skills. Telemetry only; surfaces a possible skill-uptake gap for meta-phase, not a content defect.

5. **[non-defect, noted] the slice `rho_0` correction is correctly deferred, not applied.** The report flags the `book/src/spec/slices/chebyshev.md:160` error and (correctly, per one-operator + slice-authority discipline) leaves the slice unedited, filing the correction for the slice-reduction OQ residual (OQ caveat 1). No action required of the harvester; flagged here so the integrator does not lose the slice-correction follow-up — the erroneous `delta/(2*theta)` line will persist in the slice until that reduction lands.

---

## Repair

### Fixes attempted

- **Finding 1 (warning, citation precision): `SpectralNorm` hermitian flag overstated as literal `true`.**
  - **Decision**: repaired.
  - **Action**: Re-verified `palace/linalg/chebyshev.cpp:13-27` directly via `read_range` — the real `GetLambdaMax` overload (`:18`) passes literal `true`; the complex overload (`:27`) passes `A.IsReal()`. Corrected all three occurrences of `linalg::SpectralNorm(comm, DinvA, /*hermitian=*/true)` in CYCLE.md to scope the literal-`true` claim to the real overload (`:18`) and note the complex overload (`:27`) passes `A.IsReal()`:
    - CYCLE.md "Operator content — L1" §Dependencies (`spectrum_estimate` bullet, ~line 277).
    - CYCLE.md "Operator content — L1" §Evidence (`chebyshev.cpp:13-27` bullet, ~line 372).
    - CYCLE.md §Supporting evidence ("Eigenvalue bound located" bullet, ~line 731).
  - **Rationale**: Mechanical citation-precision fix — the source range trivially supports the corrected annotation; no content authored. Squarely in repair scope (citation off-fact, source verified).

- **Finding 2 (warning, plan-kind-consistency): firm-without-dedicated-test deviates from the `eigsolve` constructed-operator-gate precedent.**
  - **Decision**: repaired (surfacing-for-triage, option (b) keep-firm-with-justification).
  - **Action**: Appended a blockquoted "**Firm-promotion-with-precedent-deviation — integrator to ratify**" note to CYCLE.md §Status of both the L1 (`chebyshev-smoother`) and L2 (`chebyshev-iteration`) entries. The note explicitly (i) names the deviation from `ksp_solve`/`eigsolve`, (ii) records the distinguishing rationale already argued in the report (every chebyshev law is a *verified-exact syntactic identity on fully-specified C++ source*, vs. `eigsolve`'s *literature-inferred convergence semantics* that warranted its rough-in; plus chebyshev is a bounded fixed-degree polynomial action with closed-form coefficients and live integration coverage, not a composite solve-to-convergence with constructed sum-type status), and (iii) routes the firm/rough-in decision to integrator ratification rather than leaving it settled silently inside the harvest.
  - **Rationale**: The critic flagged this as a judgment-call deviation needing integrator triage, *not* a clear error, and recommended leaning toward keep-firm-with-justification. Choosing option (b): the firm rationale already exists in the report (verified-exact transcriptions, constructed-operator-gate framing); the repair only makes the decision visible to integrator triage and does not author new substantive content or change the declared kind. The firm/rough-in *content decision* is deliberately left to the integrator — that is out of repair scope, so I surface it rather than resolve it. Option (a) (downgrade to rough-in) was considered and not taken: chebyshev materially differs from `eigsolve` (no literature-inferred semantics; closed-form bounded action; integration coverage), so the precedent does not unambiguously bind, and forcing a downgrade would itself be a content decision exceeding repair authority.

- **Finding 3 (rho_0 discrepancy): verify the OQ is well-formed.**
  - **Decision**: not-needed (verified well-formed).
  - **Action**: None — confirmed CYCLE.md §"Open questions / caveats" item 1 is well-formed: it cites the slice error site (`book/src/spec/slices/chebyshev.md:160`, `rho_0 = delta/(2*theta)`), the correct source value (`rhop = delta/theta`, `palace/linalg/chebyshev.cpp:282`), confirms isolation (slice `alpha_0 = 1/theta` matches `:281`), records that the firm L1/L2 entries use the source value (δ/θ), recommends slice correction at the slice-reduction step, and correctly leaves the slice unedited per one-operator + slice-authority discipline. The critic independently confirmed the source value via `read_range`. No repair needed.

- **Finding 4 (skill-uptake, informational): no skill invocations recorded.**
  - **Decision**: not-needed.
  - **Rationale**: Pure telemetry; non-blocking; the critic verified the work was done correctly by hand. Skill-uptake gaps are meta-phase concerns, not repair items.

- **Finding 5 (non-defect, noted): slice `rho_0` correction correctly deferred.**
  - **Decision**: not-needed.
  - **Rationale**: Already correctly handled (see finding 3); the slice-correction follow-up is recorded for the integrator/slice-reduction OQ. No repair authority over the slice.

### Unrepairable findings

None. Both warning findings were addressed within repair authority (finding 1 by mechanical citation correction; finding 2 by surfacing-for-triage without changing the declared kind). The remaining findings are informational/non-defect or already correctly handled by the dispatch.

## Suggested resolution

`overall_status: pass-after-repair`. Notes for the integrator:

1. **Ratify the firm decision (finding 2).** Both entries now carry an explicit "integrator to ratify" note in §Status. The recommendation (and the critic's lean) is **keep firm**: chebyshev's laws are verified-exact syntactic identities on fully-specified source (not literature-inferred like `eigsolve`), it is a bounded fixed-degree polynomial action with closed-form coefficients, and it has live integration coverage (`gmg.cpp`, `distrelaxation.cpp`). If the integrator instead judges the constructed-operator-gate test-bar to bind, downgrade **both** L1 and L2 to rough-in in lockstep and adjust the two `index.md` rows + the L1 "Firm (8)→(9)" bump accordingly. Either outcome is internally consistent with the report as repaired.

2. **Carry the slice `rho_0` correction forward (findings 3/5).** The erroneous `book/src/spec/slices/chebyshev.md:160` line (`rho_0 = delta/(2*theta)`) persists in the slice; the firm entries already use the correct source value (δ/θ). Ensure the slice-reduction OQ residual retains this correction item so the wrong coefficient does not survive into the (eventually authoritative) reduced slice.

3. No other action required. Citation precision (finding 1) is fully corrected in CYCLE.md.
