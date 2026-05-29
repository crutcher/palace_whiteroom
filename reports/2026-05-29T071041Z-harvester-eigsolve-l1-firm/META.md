---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T08:14:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T08:42:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: layer-intro-author
---

# META: verification of "Formalize eigsolve at L1 (rough-in → firm)"

## Critique

### Checks run

**citation-validity — pass.** Ran `tools/citecheck/citecheck.py --scan` over the report (46 citations: 43 OK, 3 tool-resolution artifacts, 0 real out-of-range). The 3 non-OK are all cosmetic, not citation errors: `index.md:40` / `index.md:79` are `[AMBIG]` (bare basename matches 16 `index.md` files; both resolve to `book/src/L1/index.md` lines 40 and 79, which I read and confirmed in-range and carrying the exact cited "literature-inferred convergence semantics absent here" text); `drivers/eigensolver.cpp:367-374` is `[MISS]` solely because the report's self-verification shorthand (line 147) dropped the `palace/` path prefix — with the prefix (`palace/drivers/eigensolver.cpp:367-374`, the form used in the chapter at line 207) the range is in-bounds (file has 479 lines). I additionally bounds-checked all 10 new positive-source law anchors with full prefixes: every one is in-range. The anchor-drift token checks the report claims (`arpack.cpp:383`→`eig[i] = eig[i] * gamma;`, `slepc.cpp:554`→`EPSSetConvergenceTest(eps, EPS_CONV_REL)`, `slepc.cpp:694`→`EPSSolve(eps)`, `slepc.cpp:695`→`EPSGetConverged`) all verified line-exact via codemap `read_range`.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (status flip + law-rationale rewrite on an existing chapter). It modifies surface (Edits 1-5 rewrite the Algebraic-laws caveat, the `## Status` section, the Evidence list, and the `index.md` dep-map row + prose bullet) AND it is backed by retroactive evidence backfill (10 new positive-source law anchors). It is not a pure rotation_claim without surface. The core question — is the rough-in→firm flip JUSTIFIED — I verified by independently reading every cited Palace body (see Issues for the law-by-law verdict). The flip rests on positive source, not conjecture. Pass.

**rotation-quality — pass (not the primary axis; applies as the maturity-promotion soundness check).** No new L_{n+1}→L_n algebraic rotation is asserted here — the L1 mutation-rotation surface is unchanged; this is a maturity promotion within L1. I treated the load-bearing judgment as "is the promotion from rough-in to firm sound" and verified it independently (below). The report does NOT inflate any claim into a rotation it cannot support.

**variant-axis-coverage — pass.** The four live variant axes (problem-type, spectrum-target, spectral-transformation, scaling) and three collapsed axes (orchestration-pattern, SLEPc-Type, SLEPc-ProblemType) are unchanged by this status flip and were already inventoried (cycle-011). Critically, the firm claim is verified to hold *across all four backends* — the report's law anchors cover both SLEPc (`slepc.cpp`) and ARPACK (`arpack.cpp`) residual/normalization paths, and the un-scale-at-accessor (laws 4-5) is cited across EPS/PEP/NLEPS/NEP via the embedded cycle-012 4-backend audit. No hidden branch. The 2 ARPACK-unsupported spectrum-target stubs remain documented as constructor-time validity constraints (unchanged).

**cross-reference-integrity — pass (including the build-readiness guard).** All five edit blocks carry valid `OLD` anchors that match the live artifact exactly: Edit 1 OLD = `eigsolve.md:100`; Edit 2 OLD = `eigsolve.md:167-171`; Edit 3 OLD = `eigsolve.md:216`; Edit 4 OLD = `index.md:72`; Edit 5 OLD = `index.md:47` — all confirmed character-faithful against the current files. The firm-sibling precedent references (`apply_nonlinear_pencil`, `chebyshev-smoother`) resolve to real chapters carrying the cited framing. **Build-readiness guard (firm-body-inside-fence):** PASS. Fence enumeration via `grep -n '```'` yields 12 markers (even parity, all blocks balanced): five `edit:` blocks (29/36, 40/59, 63/83, 87/94, 98/105) + one `text` Signature block (114/116). The firm apparatus being promoted (`## Status` → firm) is INSIDE Edit 2's fence (lines 40-59). The cycle-019 fence-truncation defect signature — a firm body authored as the report's OWN top-level sections outside the fence — is ABSENT: the "Operator content" section (lines 107+) is an explicit re-statement summary (repeatedly marked "unchanged"), not the proposed-changes substrate. SUMMARY.md correctly unchanged (chapter already wired at `SUMMARY.md:63`).

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried; this is an intra-L1 maturity flip. The downstream-chain note (Edit 2, lines 56-57) correctly scopes the L3 `partial-obstruction` prediction as an L3-loop judgment, explicitly NOT an L1 claim — no edge-label mismatch.

**plan-kind-consistency — pass.** Declared kind is a `firm` promotion. The content shape matches: the chapter carries full firm apparatus (Signature with shape contracts, Semantics, 6 laws + 8 non-laws, Dependencies, Variant axes, Evidence, embedded lowering-verifier audit), and the promotion is justified by per-law positive-source anchoring. No rough-in placeholders remain in the promoted content. The status string is internally consistent across all five edits (`firm` in Edit 2, dep-map row Edit 4, prose bullet Edit 5).

**skill-uptake-survey — pass (telemetry only).** The report references `tools/citecheck/` (self-verification, lines 147-148) and codemap `read_range` (line 149), which are the relevant procedures for a citation-backfill firm-promotion. `verify-citation-range` skill exists and would be the canonical invocation; the report uses the underlying `citecheck.py` tool directly, which is acceptable. No blocking gap.

### Issues found

The promotion is **sound**. I independently re-read every cited Palace body via codemap `read_range` and the law-by-law verdict confirms the producer's central claim — the laws are positive-source syntactic identities, not convergence-semantics conjectures:

- **Law 1 (defining-equation residual) — positive, confirmed.** `palace/linalg/slepc.cpp:828-835` (`SlepcEPSSolver::GetResidualNorm`) and `palace/linalg/arpack.cpp:603-610` (`ArpackEPSSolver::GetResidualNorm`) both literally build `opK->Mult(x, r); opM->AddMult(x, r, -l); return Norml2(r)` = `‖(K−λM)x‖₂`, with the verbatim comment "Compute the i-th eigenpair residual: || (K - λ M) x ||₂". `RescaleEigenvectors` (`slepc.cpp:497-510`, `arpack.cpp:463-473`) computes and STORES `res[i] = GetResidualNorm(...) / Norml2(x1)`; `GetError` (`slepc.cpp:483-495`) exposes it. This is a computed-and-stored post-condition, not a conjecture.
- **Law 2 (normalization) — positive, confirmed.** `GetEigenvectorNorm` (`slepc.cpp:470-481`) returns `Norml2(x)` (no B) or `Norml2(x, opB, Bx)` = `√(xᴴBx)`; `RescaleEigenvectors` sets `xscale[i] = 1.0 / GetEigenvectorNorm(...)`. Performed in source.
- **Laws 4-5 (shift/scaling un-transform) — positive, confirmed.** `arpack.cpp:383` is exactly `eig[i] = eig[i] * gamma;` (un-scale at accessor); `slepc.cpp:711-716` returns `l * gamma`. The 4-backend uniformity is the already-embedded cycle-012 lowering-verifier audit.
- **Law 3 (termination) — the ONLY delegated piece — is delegated to the LIBRARY THRESHOLD ONLY, identical to the `ksp_solve` basis.** `slepc.cpp:551-554` (`SetTol`) wires `EPSSetTolerances` + `EPSSetConvergenceTest(eps, EPS_CONV_REL)` positively; the count→status structural map reads `EPSSolve` + `EPSGetConverged` + `return (int)num_conv` (`slepc.cpp:694-708`). What is delegated is the tol→converged *threshold*, exactly as `ksp_solve` (firm) delegates convergence to its Krylov method. No eigsolve law asserts a convergence rate or guarantee — verified by reading the bodies. The cycle-009 "literature-inferred convergence semantics" premise IS over-stated, as the report argues.

No law is left resting on a convergence-semantics conjecture. The flip is justified.

Remaining issues are minor (candidates for repair, none blocking):

1. **(low / cosmetic) Self-verification path-prefix drift — `reports/.../CYCLE.md:147`.** The citation self-verification line lists `drivers/eigensolver.cpp:367-374` without the `palace/` prefix, which trips `citecheck` as a `[MISS]`. The canonical form (used in the chapter at `eigsolve.md:207`) is `palace/drivers/eigensolver.cpp:367-374`, which is in-range. This drift is confined to the report's prose self-report; it does NOT appear in any of the five `edit:` blocks, so it does not propagate into the artifact. Repair would be to add the `palace/` prefix in the self-verification listing.

2. **(low / informational) `index.md:40` / `index.md:79` cited as bare basenames — `reports/.../CYCLE.md` (Summary line 10, Supporting-evidence line 144).** The firm-sibling precedent citations use bare `index.md:40` / `index.md:79`, which are ambiguous to `citecheck` (16 candidate `index.md` files). Both resolve to `book/src/L1/index.md` and I verified the lines carry the cited text; this is an in-house artifact cross-reference, not a `reference/` source citation, so the bare form is conventional. No artifact impact (does not appear in edit blocks). Optional: qualify as `L1/index.md:40` for tooling cleanliness.

3. **(low / accuracy) `slepc.cpp:273-274` is characterized as "the `Customize`-side tol+max_it binding" (Edit 3, Evidence anchor, line 79).** Independently reading `slepc.cpp:270-276`, lines 273-274 are `EPSSetDimensions(eps, 1, ...)` + `EPSSetTolerances(eps, tol, max_it)` sitting inside what appears to be an internal norm/backward-scaling EPS sub-solve helper (it sets dimensions to 1 and immediately `EPSSolve`s), NOT the main-solve `Customize()` path (whose `SetTol` is at `slepc.cpp:551-554`, the separately-cited anchor). The lines DO contain the cited `max_it`-binding tokens and the anchor is in-range, so the law-3 `MaxIterReached` substrate claim is supported; only the "Customize-side" descriptor is imprecise. Repair: relabel as "an EPS `max_it`-binding site" or drop the `Customize`-side parenthetical.

4. **(low / scoping note, already self-flagged) Stale cycle-009 narrative bullet — `book/src/L1/index.md:96`.** The report (Open questions §3) correctly identifies that `index.md:96`'s cycle-history bullet ("status is rough-in pending …") will be stale post-flip and correctly routes it to the layer-intro-author rather than editing historical narrative in-place. No action needed from this report; noting for the integrator's awareness that the layer-intro narrative will lag the dep-map until a layer-intro-author pass lands.

---
repaired_at: 2026-05-29T08:42:00Z
repairer_version: 1

## Repair

### Fixes attempted

- **Finding 1**: Self-verification path-prefix drift — `CYCLE.md:147` lists `drivers/eigensolver.cpp:367-374` without the `palace/` prefix, tripping `citecheck` as `[MISS]`.
  - **Decision**: repaired
  - **Action**: Edited `CYCLE.md` Supporting-evidence self-verification listing (the `Bounds-checked via tools/citecheck/citecheck.py` line) to `palace/drivers/eigensolver.cpp:367-374`. Verified the corrected form via `citecheck.py --show`: `[ok] range in bounds (file has 479 lines)`, resolving to `eigen->Solve()` + converged-count print at lines 367-374. Mechanical prefix add; confined to report prose self-report — did NOT appear in any `edit:` block, so it never propagated to the artifact regardless.

- **Finding 2**: Bare-basename cross-references — `index.md:40` / `index.md:79` cited as bare basenames (Summary line 19, Supporting-evidence line 144), ambiguous to `citecheck` (16 candidate `index.md` files).
  - **Decision**: repaired
  - **Action**: Qualified both occurrences to `L1/index.md:40` / `L1/index.md:79` in `CYCLE.md` (Summary precedent-alignment sentence + Supporting-evidence "Precedent alignment" bullet). The frontmatter `inputs:` lines 9-10 were already `L1/index.md`-qualified — no change needed there. Both resolve to `book/src/L1/index.md`; this is an in-house artifact cross-reference (not a `reference/` source citation), and the bare form does not appear in any `edit:` block.

- **Finding 3**: Imprecise descriptor — `slepc.cpp:273-274` characterized as "the `Customize`-side tol+max_it binding" (Edit 3 Evidence anchor, line 79), but the lines sit inside an internal singular-value EPS sub-solve helper, not the main-solve `Customize()` path.
  - **Decision**: repaired
  - **Action**: Independently re-read `palace/linalg/slepc.cpp:260-280` via codemap `read_range` — confirmed lines 273-274 (`EPSSetDimensions(eps, 1, …)` + `EPSSetTolerances(eps, tol, max_it)`) are inside a `MatCreateShell` + `EPSSetProblemType(EPS_HEP)` + immediate `EPSSolve` block computing a maximum singular value (the `herm` branch), NOT the main `Customize()` path (whose `SetTol` is the separately-cited `slepc.cpp:551-554`). Relabeled the Edit-3 Evidence-anchor descriptor (inside the `<<<NEW` block, so it lands in the chapter's Evidence list) to "an EPS `max_it`-binding site — this is an internal singular-value EPS sub-solve helper, not the main-solve `Customize()` path whose `SetTol` is the separately-cited `slepc.cpp:551-554`". The `max_it`-binding tokens are present and the range is in-bounds, so the law-3 `MaxIterReached` substrate claim is unchanged — only the descriptor's precision improved. Surgical prose fix; no claim altered.

- **Finding 4**: Stale cycle-009 narrative bullet — `book/src/L1/index.md:96`'s cycle-history bullet will be stale post-flip; the report self-flagged it (Open questions §3) and routed it to layer-intro-author.
  - **Decision**: not-needed (record-only)
  - **Rationale**: This is artifact-prose (the layer-intro cycle-history narrative), not report-prose, and it requires a substantive authoring decision (append a cycle-022 promotion bullet vs. how to phrase it) that exceeds repair authority and the harvester's scope. The report correctly did NOT edit historical narrative in-place. Routed to `layer-intro-author` for a future dispatch. The dep-map row + operator prose bullet (Edits 4-5) DO carry the firm status, so the artifact is internally consistent for integration; only the cycle-history narrative lags.

Post-repair verification: `citecheck.py --scan` over the repaired `CYCLE.md` → **43 ok, 0 failing** (finding 1's `[MISS]` cleared, finding 2's two `[AMBIG]` bare basenames now qualify cleanly). No new issues introduced.

### Unrepairable findings

None. All four findings were either repaired (1, 2, 3) or are record-only scoping notes for a downstream agent (4). No finding required substantive authoring within the artifact or contradicted existing content.

## Suggested resolution

`overall_status: ready` — the critic returned all 8 checks PASS (the rough-in→firm flip was independently confirmed sound — laws are positive-source syntactic identities, not convergence-semantics conjectures), and the four minor sub-findings were all cosmetic and confined to the report's prose. Findings 1-3 are repaired; the five `edit:` blocks that mutate the artifact were unaffected by findings 1-2 (those occurrences live only in report-prose self-verification / precedent-alignment) and improved-in-precision by finding 3 (the Evidence-anchor descriptor inside Edit 3's `<<<NEW`).

**For the integrator**: apply the five edit blocks as-is (Edit 1 Algebraic-laws caveat→firm rationale; Edit 2 `## Status` flip; Edit 3 Evidence law-anchor additions with the corrected `slepc.cpp:273-274` descriptor; Edit 4 dep-map row; Edit 5 prose bullet). SUMMARY.md needs no change (`eigsolve` already wired at `SUMMARY.md:63`).

**Follow-up routing (`follow_up_agent: layer-intro-author`)**: finding 4 — a future `layer-intro-author` pass on `book/src/L1/index.md` should append a cycle-022 bullet noting the `eigsolve` rough-in→firm promotion, leaving the historical cycle-009 bullet at line 96 intact as an accurate record of the cycle-009 state. This is non-blocking for the current integration; the layer-intro cycle-history narrative will simply lag the (correct) dep-map until that pass lands. Note also the report's two carried-forward OQs (§1 the `source-read-confirmed, empirically-unwitnessed` residual caveat — keep open, `test-eigensolver.cpp` likely out of write-scope; §2 the L3 `partial-obstruction` prediction for the cycle-022 prerequisite-chain step 3) for promotion to the OQ ledger.
