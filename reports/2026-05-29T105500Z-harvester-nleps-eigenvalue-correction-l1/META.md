---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T120000Z
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
repaired_at: 2026-05-29T123000Z
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

# META: verification of "Formalize nleps_eigenvalue_correction at L1"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing citation was verified verbatim against on-disk Palace source via `palace-codemap` `read_range`. The core positive site `palace/linalg/nleps.cpp:672-677` is exact line-for-line: `:672` comment "Undamped Newton step for the eigenvalue; the line search damps it", `:673` `const std::complex<double> u2_w0 = std::complex<double>(w2.adjoint() * u2)`, `:674-675` `delta_eig = -(linalg::Dot(GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0)`, `:676` `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)`, `:677` `z2 = -u2`. The consumer/producer wiring all verified at the exact cited lines: `:587` `compute_residual(eig, v, v2, u, u2, A2n)` (residual write), `:657` `opJ->Mult(v, w)` (Jacobian action), `:542-545` `deflated_solve(c, c2, w0, w2)` + the `norm_w0` normalization (projection direction), `:540` "only used as a projection direction for the eigenvalue correction" comment, `:682` `deflated_solve(z, z2, du, du2)` (downstream solve), `:691` `eig_trial = eig + alpha * delta_eig`, `:704-708` Armijo test + `eig = eig_trial` commit, `:684-686` "`<w0, w>` is near-singular" comment, `:606-619` deflation-basis growth (all sub-line refs `:610-611`/`:614`/`:615`/`:616-618`/`:619` exact), `:354-362` Jarlebring–Koskela–Mele 2018 / Effenberger 2013 / SLEPc-NEP-minimality-index-1 literature anchors. The dot conjugation convention is correctly grounded: `vector.hpp:246` "Calculate the parallel inner product yᴴ x or yᵀ x" (second C++ arg conjugated) and `vector.cpp:674-685` `LocalDot` real/imag split `{Re·Re+Im·Im, Im·Re−Re·Im} = yᴴx` — the report's algebra at line 162 is correct and the projection-direction-is-conjugated derivation (semantics point 2) is sound. One minor inherited-citation drift noted under Issues (the `nleps_deflated_solve.md:145` pointer is off-by-one). No claim lacks a citation.

**surface-or-evidence — pass.** Not a refinement-shaped proposal; this is a wholly-new firm L1 operator entry (`new:book/src/L1/nleps_eigenvalue_correction.md`) plus two surgical dep-map/SUMMARY inserts. The new operator's surface is fully authored and every claim carries a positive source pointer. The check is satisfied by direct positive-evidence authoring rather than rotation_claim backfill.

**rotation-quality — pass.** The L1 form is a genuine mutation rotation of the L0 source: the destination-buffer overwrites (`z`, `z2`), the consume-then-reuse aliasing of `u`/`u2` into `z`/`z2` (source comment `:699-700`), the Armijo `α` damping, and the `AXPBYPCZ`-γ=0 build form are all hidden behind a pure-functional `{ δλ, z, z2 } = nleps_eigenvalue_correction(resid, jac_action, proj_dir)` signature. The L1 representation is strictly more compact and more equational (the projected Newton ratio named as `−⟨[w0;w2],[u;u2]⟩ / ⟨[w0;w2],w⟩`; the RHS factored through firm `axpby`/`scal`). This is state-hiding + threaded-state compression, not a 1:1 rename.

**variant-axis-coverage — pass.** Two variant axes are identified and handled: the **deflation-present** axis (`k = 0` un-deflated vs `k > 0` deflated) is covered with the `k = 0` degeneration stated explicitly (coordinate parts `u2`/`w2`/`z2` empty, `num = dot(w0, u)`), and the **purpose (committed-step)** axis is scoped out with a cited reason (no trial/committed structural variant within the atom; the trial loop re-evaluates the *residual* sibling, not this correction). Three further axes (AXPBYPCZ-γ=0 build-form, projection-direction lag/normalization, Armijo damping `α`) are explicitly listed as collapsed/absorbed with citations. No hidden branches: the `k > 0` deflation block (`:658-671`) is correctly noted to accumulate only into the big-space `w` (justifying the no-coordinate-Jacobian-part claim, semantics point 4), which I confirmed against source.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: `dot.md`, `axpby.md`, `scal.md`, `axpbypcz.md`, `axpy.md`, `ksp_solve.md`, `lu_solve.md`, `eigsolve.md`, `nleps_deflated_solve.md`, `nleps_deflated_residual.md`, `apply_nonlinear_pencil.md`, `L0/eigensolver-wrapper.md`, `L2/linear_combination.md` all exist. The target file `nleps_eigenvalue_correction.md` correctly does not yet exist (this report creates it). The `nleps_jacobian_action` forward-reference is correctly rendered as plain text / inline-code (NOT a live link) per the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention — verified `nleps_jacobian_action.md` is not on disk, so a live link would have been an `mdbook-linkcheck2` hard error; the report avoids it correctly. The `dot.md:43` arg-1-conjugated convention pointer is exact (`⟨x, y⟩ = xᴴ y`, "the L1 signature names the conjugated argument first"). **Build-readiness guard (firm-body-inside-fence):** fence enumeration shows 10 markers (even parity); the `new:book/src/L1/nleps_eigenvalue_correction.md` block opens at line 25 and closes at line 174, with the full firm apparatus ENCLOSED inside it — `## Status` (line 137), Signature (38), Algebraic laws (97), Semantics (71), Evidence (150) all sit between 25 and 174. The two nested ` ```text ` blocks (40-58, 75-81) are inner content. This is the identical nesting pattern the cycle-023 sibling `nleps_deflated_solve` report used and the integrator demonstrably applied (verified: that report opens its `new:` fence at line 28, nests ` ```text ` at 39/45/51/71/90/94/98/107, closes at 214). No cycle-019 fence-truncation defect: the body is NOT authored as the report's own top-level sections outside the fence.

**edge-label-fidelity — pass.** Not applicable to a same-layer L1 operator entry — the report carries no L_{n+1}→L_n edge label. It correctly defers the L1>L0 mutation-rotation theme to a separate abstractor dispatch (Open questions, CYCLE.md line 209) rather than authoring a lowering edge here. The "Downward to L0 is L1>L0 concern" framing in the L1-vs-L0 section is direction-consistent (high→low).

**plan-kind-consistency — pass.** Declared kind is `firm` L1 operator; content shape matches. The firm decision rests on the firm-on-positive-structure escape (syntactic-identity laws on firm BLAS-1 leaves `dot`/`axpby`/`scal`, every constituent read from the single positive site `:672-677`), which is the correct tier — NOT `partly-constructive` (no constructive sub-part from negative anchors) and NOT `rough-in (test-coverage-bounded)` (the laws are syntactic identities, not test-gated convergence semantics). This is the `apply_nonlinear_pencil`/`nleps_deflated_residual`/`nleps_deflated_solve` precedent, correctly invoked. No rough-in placeholders in a firm entry. The four non-laws (λ-nonlinearity upstream; `⟨[w0;w2],w⟩=0` near-singularity; `δλ` undamped; reduction-tree non-determinism) are recorded as non-laws, not asserted as identities — consistent with the firm-on-syntactic-identity rationale.

**skill-uptake-survey — warning (non-blocking).** A firm-operator harvest of this shape (positive-site citation verification, firm-status decision, variant-axis classification) has directly relevant skills: `verify-citation-range`, `classify-variant-axis`, and the firm-on-positive-structure status discipline. The report's Supporting-evidence section documents verbatim verification and the `search_text` no-test confirmation in prose, but does not explicitly name a skill invocation. This is a pure-presence telemetry surface, not a correctness defect — the verification work was clearly done (and I independently confirmed every citation). Surfaced for telemetry only.

### Issues found

1. **[minor / warning] Inherited-citation off-by-one** — `reports/.../CYCLE.md:143` (Status §, Test-coverage caveat). The report cites the sibling's inherited no-test caveat as `book/src/L1/nleps_deflated_solve.md:145`, but the `**Test-coverage caveat**` paragraph in that file is at line **146** (line 145 is blank, between the Single-algorithm-concentration and Test-coverage paragraphs). The cited content is present one line below the pointer. This is exactly the live inline-anchor-drift friction this batch was flagged for; the pointer should read `:146`. Non-substantive (the referenced caveat exists and the inheritance claim is correct).

2. **[informational] Forward-reference range `:650-672` slightly over-spans into the eigenvalue-correction comment** — `CYCLE.md:63` and `:154` cite the `nleps_jacobian_action` producer block as `palace/linalg/nleps.cpp:650-672`. The Jacobian-action block runs `:649` ("Compute w = J * v" comment) through `:671` (the `k>0` deflation block close); `:672` is the "Undamped Newton step" comment that belongs to THIS atom, not the Jacobian action. The over-span is one line and is a forward-reference to a *parallel* dispatch's scope (not a claim this report formalizes), so it is informational only — the integrator/critic of the parallel `nleps_jacobian_action` report owns the precise boundary.

3. **[informational] Shared-edit merge coordination** — `CYCLE.md:176-184` (the `edit:book/src/L1/index.md` + `edit:book/src/SUMMARY.md` blocks). Both this report and the parallel `nleps_jacobian_action` harvester anchor their surgical dep-map / SUMMARY inserts on the SAME existing `nleps_deflated_solve` row (index.md line 87 / SUMMARY.md line 78), and both will need the `Firm (17)` cohort header (index.md line 31) bumped. The report explicitly flags this for integrator coordination (CYCLE.md:208, :210) and correctly does NOT touch the `Firm (17)` count itself (deferred to layer-intro-author). The dep-map row + SUMMARY entry proposed here are distinct, non-overlapping with the jacobian-action ones, and the anchor row (`nleps_deflated_solve`) matches on-disk verbatim. No defect — surfaced so the serial integrator-per-report applies the two reports' shared-file edits without clobbering (apply one, re-anchor the second).

4. **[informational, no action] firm-status escape verified** — the `firm` claim on the firm-on-positive-structure footing is correct: I confirmed `apply_nonlinear_pencil.md:98` does carry the firm-on-positive-structure rationale the report cites as precedent (line 98 is the `## Status` firm paragraph), and the single positive site `:672-677` does supply every constituent (the three `dot`/`.adjoint()*` calls, the ratio, the `AXPBYPCZ`, the negation) — no constructive sub-part, so `firm` (not `partly-constructive`) is the right tier.

## Repair

### Fixes attempted

- **Finding**: [minor / warning] Inherited-citation off-by-one — CYCLE.md Status § Test-coverage caveat cites the sibling's inherited no-test caveat as `book/src/L1/nleps_deflated_solve.md:145`; the `**Test-coverage caveat**` paragraph in that file is at line 146 (line 145 is blank).
  - **Decision**: repaired
  - **Action**: Corrected the inline anchor `:145` → `:146` in the Test-coverage-caveat paragraph of `reports/2026-05-29T105500Z-harvester-nleps-eigenvalue-correction-l1/CYCLE.md` (Status §). Verified on-disk: read `book/src/L1/nleps_deflated_solve.md` lines 139-151 — `## Status` at 139, Single-algorithm-concentration at 143, blank at 145, `**Test-coverage caveat**` paragraph at 146. The pointer now resolves to the cited content. This maps to the critic's `citation-validity` check (which passed overall but flagged this one minor inline-anchor drift under Issues); the repair clears the residual drift. (Pure mechanical off-by-one correction within repair authority: "Citation line range off by a small offset.")

- **Finding**: [informational] Forward-reference range `:650-672` slightly over-spans into the eigenvalue-correction comment (CYCLE.md:63, :154) — the `nleps_jacobian_action` producer block.
  - **Decision**: not-needed
  - **Rationale**: Informational only per critic. This is a forward-reference to a *parallel* dispatch's scope (`nleps_jacobian_action`), not a claim this report formalizes; the over-span is one line and the precise boundary is owned by the parallel report's own critic/integrator. No edit to this report.

- **Finding**: [informational] Shared-edit merge coordination (CYCLE.md:176-184) — both this report and the parallel `nleps_jacobian_action` harvester anchor surgical dep-map / SUMMARY inserts on the same `nleps_deflated_solve` row.
  - **Decision**: not-needed
  - **Rationale**: No defect. The report already flags this for integrator coordination (CYCLE.md:208, :210) and correctly does not touch the `Firm (17)` count. The proposed dep-map row + SUMMARY entry are distinct and non-overlapping with the jacobian-action ones; this is a serial-integrator-per-report apply-order note, not a repair target.

- **Finding**: [informational, no action] firm-status escape verified (critic confirmed the `firm` tier is correct).
  - **Decision**: not-needed
  - **Rationale**: Critic-confirmed correct; nothing to repair.

- **Finding**: skill-uptake-survey — warning (non-blocking telemetry). The report does verbatim citation verification + firm-status decision + variant-axis classification but does not explicitly name a skill invocation.
  - **Decision**: not-needed
  - **Rationale**: Pure-presence telemetry surface, not a correctness defect. The critic independently confirmed the verification work was done. A skill-naming omission is not a mechanical/surgical repair target and authoring a skill-uptake claim post-hoc would be substantive. No fix.

### Unrepairable findings

None. The single substantive-ish finding (inline-anchor off-by-one) was mechanically repairable and is repaired; all other findings are informational/telemetry requiring no action.

## Suggested resolution

`ready`. The one inline-anchor drift is corrected (`:145` → `:146`); the inheritance claim it carries is verified-correct. Note for the integrator: this report and the parallel `nleps_jacobian_action` harvester both edit `book/src/L1/index.md` (dep-map, anchored on the `nleps_deflated_solve` row) and `book/src/SUMMARY.md` (entry after `nleps_deflated_solve`) — apply them serially and re-anchor the second so the shared-file inserts don't clobber. Neither report touches the `Firm (NN)` cohort header/count (deferred to layer-intro-author per CYCLE.md:210). The `nleps_jacobian_action` forward-reference in this report is intentionally plain-text (not a live link) per the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention — the integrator may upgrade it to a live link only if the sibling lands this cycle.
