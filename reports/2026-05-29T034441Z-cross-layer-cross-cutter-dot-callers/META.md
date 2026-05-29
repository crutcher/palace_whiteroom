---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T040514Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T041530Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Cross-layer observation — Palace linalg::Dot caller-site conjugation-risk inventory"

## Critique

### Checks run

**citation-validity — pass.** I independently `read_range`-verified (via `palace-codemap`, not trusting self-verification) a strong sample across every classification bucket, and the crux 4 observable sites in full. **Invisible CG/PCG:** `iterative.cpp:395` (`beta = linalg::Dot(comm, z, r)` → `:396 CheckDot` → `:397 res = sqrt(abs(beta))`), `:404` (`beta_rhs = Dot(comm, p, b)` → `:410 CheckDot` → `:411 sqrt(abs)`), `:444` (`denom = Dot(comm, z, p)` → `:445 CheckDot` → `:446 alpha = beta/denom`), `:460` (in-loop `beta = Dot(comm, z, r)` → `:461 CheckDot` → `:462 sqrt(abs)`) — all four exact, all real-projected. **B-weighted Norml2:** `operator.cpp:603` (`double dot = Dot(comm, Bx, x)` → `:604 MFEM_ASSERT(dot > 0.0)` → `:605 sqrt(dot)`) and `:615` (`complex<double> dot = Dot(comm, Bx, x)` → `:616` asserts `dot.real() > 0.0 && abs(dot.imag()) < 1e-9*dot.real()` → `:617 sqrt(dot.real())`, comment `:612` "For SPD B, xᴴ B x is real.") — both exact, only `.real()` consumed. **nleps self-norms:** `:487,:492,:543,:696,:737` all `sqrt(abs(Dot(·,·)) + ·.squaredNorm())` magnitude consumptions, exact. **The 4 OBSERVABLE sites (verified in full):** `:522` `x2(j) = b2(j) - linalg::Dot(GetComm(), x1, X[j])` (= `X[j]ᴴ x1`) flowing into `:533 x2 = SS.fullPivLu().solve(x2)`, `:534 XSx2 = MatVecMult(X, S.solve(x2))`, `:535 AXPY(-1.0, XSx2, x1)` — full complex, no projection; `:529 SS(i,j) = linalg::Dot(GetComm(), X[i], X[j])` (= `X[j]ᴴ X[i]`) into `:532 SS = -S.solve(SS); :533 x2 = SS.solve(x2)` — full complex matrix, off-diagonals convention-sensitive; `:568 rr2(j) = linalg::Dot(GetComm(), vv, X[j])` (= `X[j]ᴴ vv`) — out-param, bound at `:587 compute_residual(eig, v, v2, u, u2, A2n)` to `u2`, consumed at `:674 u2_w0 = w2.adjoint()*u2` then `:675`; `:675 delta_eig = -(linalg::Dot(GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0)` (two distinct Dot calls on one line) into `:676 z.AXPBYPCZ(-delta_eig, w, ...)` and `:685 eig_trial = eig + alpha*delta_eig` (`eig.imag()` load-bearing throughout). Every citation lands in-range and supports its claim. Two sub-line anchor nuances exist (noted under Issues) but are 1-line off and non-substantive.

**surface-or-evidence — pass.** This is a retroactive-evidence census feeding an existing firm theme's applicability evidence — a legitimate evidence-backfill shape (no surface mutation proposed beyond an additive `verified_against`-style metadata block). The three headline claims all independently verify: (1) `palace/fem/` has ZERO Dot callers — confirmed, `search_text "Dot\(" -g palace/fem/**` → 0 hits; (2) the `linalg::Dot(` census is exactly the 20 hits the report tabulates (4 iterative, 10 nleps lines / 11 calls, 4 postoperator, 2 boundarymodeoperator) — confirmed via `search_text "linalg::Dot\(" -g palace/**`; (3) the convention is load-bearing in exactly one algorithm (SLEPc-NEP `nleps.cpp`) — confirmed, all 4 observable sites are there. The `:568` subtlety the prompt flagged is the most important sub-claim and it holds precisely: immediate `:575` consumption is `.squaredNorm()` (invisible alone), but the out-param escape through `:587`'s binding into `:674-675` makes the full complex value load-bearing. The report correctly self-flags this as "the subtlest site in the census."

**rotation-quality — pass (not applicable to a census/observation report).** No algebraic/structural rotation is asserted. The substitute substance — the invisible/observable classification logic — is sound: real-projection (`.real()`, `std::abs`, SPD/Hermitian diagonal, ratio-of-same-convention-dots) ⟹ invisible; full-complex / off-diagonal / out-param-escape ⟹ observable. Each table verdict is correctly derived from the verified consumption site.

**variant-axis-coverage — pass (not applicable).** No operator/theme with orthogonal variant axes is authored. The closest structure — weighted vs unweighted leaf, and invisible vs observable consumption — is exhaustively enumerated (the report explicitly partitions weighted/unweighted × invisible/observable in its proposed evidence block, and scopes `models/` and `orthog.hpp` out with named follow-ups). No hidden branch.

**cross-reference-integrity — pass.** The theme target `book/src/L2-L1/inner-product-fold-specialization.md` exists; its "§Condition 5" resolves (line 284, "The conjugate-pair re-order is observable for full-complex-value uses"). The L1 leaves `book/src/L1/dot.md` and `book/src/L1/bilinear-form.md` and `book/src/L2/inner_product.md` all exist on disk. The proposed `conjugation_caller_inventory:` block is a proposal for the integrator/lifter (not a direct write), correctly fenced as an `edit:` proposal per dispatch-phase write-guard. The follow-up surfaces (lifter cite the 4 nleps sites; combinator-miner `deflate`/`gram` candidate; `orthog.hpp:35` LocalDot+GlobalSum bypass surface) are framed as OQs/candidates, not enacted. Notably, the report's census directly answers a *pre-existing* OQ embedded in the theme itself (lines 469-478: "A full caller audit classifying every `linalg::Dot` site as 'real-projected (re-order invisible)' vs 'full-complex (re-order observable)' would tighten the re-order story to per-site precision; deferred as a `lowering-verifier`/`same-layer-cross-cutter` follow-up") — the cross-reference is not only valid but anticipated.

**edge-label-fidelity — pass.** The declared scope edge is "L2↔L1 / L1↔L0 cross-cut". The prose discusses exactly that: the L1/L2 `xᴴ y` convention vs the Palace L0 `yᴴ x` (`linalg::Dot`) convention, classified at the L0 call sites, feeding the L2>L1 `inner-product-fold-specialization` theme's applicability evidence and (forward-referenced) an L1>L0 `dot-mutation-rotation` lowering. No edge-direction mismatch.

**plan-kind-consistency — pass.** Declared `agent: cross-layer-cross-cutter`, "Observation kind: Coverage gap." The content shape matches: a read-only L0-evidence census surfacing a coverage gap in a theme's applicability evidence, with proposals (not direct writes) and OQs. No firm-operator/rough-in mis-classification; the "Direction-of-definition: clean" self-note is accurate (no `book/` mutation, no high→low violation).

**skill-uptake-survey — warning.** The report's shape (exhaustive per-site `read_range` verification of every cited L0 range) is precisely the `verify-citation-range` procedure, but the report never names a skill invocation. The methodology is embodied (44+20+0 `search_text` triage + per-site `read_range`, all "verified this invocation" in §Supporting evidence) — so this is pure telemetry, not a quality defect. Surfacing it because the census-of-citations shape is the strongest possible match for `verify-citation-range` and uptake-recording would help the meta-phase track skill use on observation reports.

### Issues found

1. **[low — internal-consistency, prose tally] Inconsistent invisible-site count: "12 of 16" vs "11 of 16".** Summary (§Summary, CYCLE.md:31-33) says "12 of the 16 caller sites are invisible ... and 4 are observable"; Risk-inventory item 2 (CYCLE.md:113) says "11 of 16 in-scope sites are invisible." Recounting the classified caller rows in the table (excluding the 2 definition-internal `:628,:637` the report itself says are "Not an independent caller"): invisible = 11 (iterative 4 + nleps self-norms 5 + operator Norml2 2), observable = 4 → 15 total. The `:575` `rr` self-norm (invisible) appears in the `search_text` results and is mentioned in the `:568` evidence but has no own table row; counting it gives invisible = 12 / total = 16. The two tallies disagree on whether `:575` (and/or `:628/:637`) is in the denominator. The per-site classifications are all individually correct and verified — this is a headline-arithmetic slip, not a classification error. Recommend reconciling to a single stated denominator (e.g. "15 caller sites: 11 invisible + 4 observable; plus `:575` self-norm and 2 definition-internal passthroughs"). Location: CYCLE.md:31-33 and CYCLE.md:113.

2. **[very-low — sub-line anchor nuance, `:522` flow] MatVecMult anchor off by one.** The `:522` table row (CYCLE.md:76) describes the downstream flow as "`:533` `x2 = SS.fullPivLu().solve(x2)`, then `:535` `MatVecMult(X, S·solve(x2))` AXPY'd into `x1`". Verified actual: `:533` `x2 = SS.fullPivLu().solve(x2)` (exact), `:534` `XSx2 = MatVecMult(X, S.fullPivLu().solve(x2))`, `:535` `AXPY(-1.0, XSx2, x1)`. The MatVecMult is at `:534`, not `:535` (`:535` is the AXPY). The data-flow claim (full complex value, no projection → observable) is unaffected and correct. Location: CYCLE.md:76.

3. **[informational — not a defect] The gap-finding against wave-1 is fair and accurate, not an overreach.** The report's central new claim — that the cycle-020 wave-1 lowering-verifier census MISSED the 4 observable nleps sites because it sampled nleps only at the invisible `:487,:492` — is verified true and fairly framed. The wave-1 report's own Condition 5 evidence set (its CYCLE.md:165-169, :232-233, and `verified_against` block) confirms it cited nleps only at `:487,:492` (both `std::abs` self-norms, invisible), and its sole observable witness is the *weighted* `boundarymodeoperator.cpp:90` (`models/`, exercising the `bilinear_form` leaf). So the bare `dot` leaf genuinely had no cited unweighted observable witness before this report. The cross-cutter does NOT overreach: it does not downgrade the theme's `firm` status, frames its output as additive applicability evidence, correctly distinguishes the weighted (`:90`) from unweighted (`:522,:529,:568,:675`) leaves, and the theme itself (lines 469-478) had already logged an OQ requesting exactly this audit. Net: the finding strictly improves the theme's evidence. Recorded as a positive verification, not an issue.

4. **[informational — scope handling sound] `orthog.hpp:35` correctly excluded.** Verified `orthog.hpp:35` is `return LocalDot(x, y)` inside `IdentityInnerProduct::operator()` — a `LocalDot` caller, NOT a `linalg::Dot` caller. The report correctly excludes it from the Dot-caller census and flags it (Open questions, CYCLE.md:197-202) as a sibling unweighted inner-product surface routing through `LocalDot`+`GlobalSum` with the same arg-2-conj convention but a different call shape — a likely coverage gap of its own. Accurate scoping; the follow-up is well-formed. Not an issue.

## Repair

### Fixes attempted

- **Finding**: [low — internal-consistency tally slip] Summary says "12 of 16 invisible"; Risk-inventory item 2 says "11 of 16" — the two tallies disagree on the denominator (whether `:575` / the definition-internal `:628`/`:637` are counted).
  - **Decision**: repaired
  - **Action**: Reconciled both figures to the table's actual census (CYCLE.md §Summary and §Risk-inventory item 2). Recounted the classified caller rows in the §Caller-site classification table: 11 invisible rows (iterative `:395,:404,:444,:460` + nleps self-norms `:487,:492,:543,:696,:737` + operator Norml2 `:603,:615`) + 4 observable sites (nleps `:522,:529,:568,:675`×2, counting the two `:675` calls as one site per the report's own "4 observable" framing) = **15 caller sites**. The 2 `operator.cpp:628,:637` rows are explicitly "definition-internal" passthroughs (not independent callers); `:575` is a `squaredNorm` consumer of `:568`'s out-param with no caller row of its own. Changed §Summary "12 of the 16" → "11 of the 15"; changed §Risk-inventory item 2 "11 of 16 in-scope sites" → "11 of the 15 in-scope caller sites" and appended a one-clause note naming the 4 observable + the 2 definition-internal passthroughs + the `:575` non-row, so the denominator is now explicit and self-consistent. The invisible count (11) was already correct in item 2; the Summary's "12" and both denominators were the slip. No per-site classification changed.

- **Finding**: [very-low — sub-line anchor] `:522` table row cites the MatVecMult AXPY downstream flow as `:535`; MatVecMult is actually at `:534` (`:535` is the AXPY).
  - **Decision**: repaired
  - **Action**: Verified via `palace-codemap read_range` on `palace/linalg/nleps.cpp:520-537`: `:533` `x2 = SS.fullPivLu().solve(x2)`, `:534` `const ComplexVector XSx2 = MatVecMult(X, S.fullPivLu().solve(x2))`, `:535` `linalg::AXPY(-1.0, XSx2, x1)`. Edited the `:522` row (CYCLE.md §Caller-site classification table) from "then `:535` `MatVecMult(X, S·solve(x2))` AXPY'd into `x1`" to "then `:534` `XSx2 = MatVecMult(X, S·solve(x2))` and `:535` `AXPY(-1.0, XSx2, x1)` into `x1`". Data-flow claim (full complex value, no real-projection → observable) unaffected.

- **Finding**: [skill-uptake-survey — warning] Report embodies `verify-citation-range` but never names the skill invocation; pure telemetry.
  - **Decision**: not-needed
  - **Rationale**: Telemetry-only, not a quality defect (critic's own framing). Skill-uptake recording is meta-phase tracking, not a mechanical repair surface; no edit is in repair scope.

- **Finding**: [confirmed-valid proposal] The `conjugation_caller_inventory:` evidence block for the theme's §Condition 5 (anticipated by the theme's OQ at lines 469-478).
  - **Decision**: not-needed
  - **Rationale**: Critic confirmed the proposal is valid; per instruction, left intact. It is a proposal for the integrator/lifter, not a repair target.

### Unrepairable findings

None. Both substantive findings (the tally slip and the `:534` anchor) were mechanical/surgical and within repair authority; the remaining items are telemetry / a confirmed-valid proposal that need no edit.

## Suggested resolution

`ready`. Notes for the integrator:
- The two tally figures now agree at "11 invisible + 4 observable = 15 caller sites" (the 2 definition-internal passthroughs and the `:575` non-row are called out explicitly in §Risk-inventory item 2). No classification changed.
- The `:522` MatVecMult anchor is corrected to `:534`; the data-flow / observability verdict is unchanged.
- The `conjugation_caller_inventory:` proposed-changes block for `book/src/L2-L1/inner-product-fold-specialization.md` §Condition 5 is critic-confirmed valid and answers the theme's own anticipating OQ (theme lines 469-478) — applying it (or routing to the proposed follow-up `lifter`) gives the bare `dot` leaf its first cited unweighted observable witness.
