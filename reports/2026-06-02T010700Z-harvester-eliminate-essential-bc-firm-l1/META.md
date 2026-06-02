---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T012851Z
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
repaired_at: 2026-06-02T013500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "Formalize eliminate_essential_bc at L1" (cycle-055 D4)

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` on the report: **26 ok, 0 failing** (all in-range, path-hygiene clean). Spot-verified the load-bearing pinpoints via codemap `read_range` (source of truth):
- `laplaceoperator.cpp:216` = `auto K_l = std::make_unique<ParOperator>(...)` (construction), `:217` = `K_l->SetEssentialTrueDofs(dbc_tdof_lists[l], Operator::DiagonalPolicy::DIAG_ONE)`. **The `:216-217` correction is CORRECT**; the dispatch-supplied `:215-217` was genuinely drifted (line 215 is the closing `}` of the print block, not the call). D4's drift-call is verified, not hand-asserted.
- `rap.cpp:36-47` = `SetEssentialTrueDofs` def with the `policy ∈ {DIAG_ONE,DIAG_ZERO}` guard (`:39-41`) and `height == width` guard (`:42-43`), `MakeRef` at `:45`, `diag_policy = policy` at `:46` — all as cited.
- `rap.cpp:141-143` = `RAP->EliminateBC(dbc_tdof_list, diag_policy)` under the `&trial_fespace == &test_fespace` guard; `:145-148` = the rectangular-reject `MFEM_VERIFY(... "Essential BC elimination is only available for square ParOperator!")`. Both exact.
- `rap.cpp:18` = `diag_policy(DiagonalPolicy::DIAG_ONE)` ctor default. Exact.
- `modeeigensolver.cpp:571` = `Ar->EliminateBC(... DIAG_ONE)`, `:574` = `Ai->EliminateBC(... DIAG_ZERO)`, `:608` = `Br->EliminateBC(... DIAG_ZERO)`, `:611` = `Bi->EliminateBC(... DIAG_ZERO)`. All four exact. No `verified_against:` YAML block in this report (harvester, not lowering-verifier) — sub-check N/A.

**surface-or-evidence — pass.** Not a refinement of an existing operator entry; this is a NEW firm L1 operator (`new:book/src/L1/eliminate_essential_bc.md`) promoting a `rough-in` plain-text bullet to a full firm chapter. Surface (the operator text) is authored AND grounded in positive Palace source. Not applicable in the refinement sense; the new-surface-with-evidence shape is satisfied.

**rotation-quality — pass.** Not a lowering-theme report (no L_{n+1}→L_n rotation claim is the primary product). The report does carry an implicit L1-vs-L0 compression in §"L1 vs L0 distinction": the L0 deferred-config-then-apply two-step on a mutable `ParOperator` wrapper + in-place `HypreParMatrix` mutation collapses to a single pure value-returning post-composition `K' = eliminate_essential_bc(K, dofs, policy)`. This is genuine state-hiding (wrapper state + apply-time staging erased), not a rename — pass for the part that applies. The actual L1>L0 rotation is correctly deferred to the `fe-operator-assemble-mutation-rotation` theme (a lifter follow-on, OQ-2).

**variant-axis-coverage — pass.** Two axes declared and both fully covered. **diagonal-policy** (`DIAG_ONE`/`DIAG_ZERO`): both values defined, semantically distinguished (solve-side vs. energy/mass-block), grounded in the `:39-41` guard, witnessed (`DIAG_ONE` at `laplaceoperator.cpp:217`; both exercised in the eigen pipeline). MFEM's third policy `DIAG_KEEP` is explicitly scoped OUT with the `ParOperator` boundary guard as the reason — not a hidden branch. **trial-test-coincidence** (`square`/`rectangular`): the `square` case is the operator; `rectangular` is a hard L0 reject (`:145-148`), explicitly scoped out, not silently dropped. No hidden combination.

**cross-reference-integrity — pass (with one in-report cross-chapter drift correctly out-of-scope).** All `[link]` targets resolve on-disk: `fe_assemble.md`, `floquet-correction.md`, `concepts/nested-constructed-operator-gate.md` (via index row context), `../L1-L0/fe-operator-assemble-mutation-rotation.md` exist. The `eliminate_rhs` reference is left plain-text per the forward-reference convention (target not on-disk at dispatch time) — correct. **Build-readiness fence guard:** fence enumeration of CYCLE.md shows 16 ``` markers (even parity). The `new:book/src/L1/eliminate_essential_bc.md` block opens at L41, closes at L342, and ENCLOSES the full firm apparatus inside the fence: `## Signature` (L94), `## Algebraic laws` (L163), `## Status` (L253, "`firm`"), `## Evidence` (L296) all sit between L41 and L342. The three nested `text` fences (96/99, 119/124, 142/144) are balanced inside. This is NOT the cycle-019 fence-truncation defect — the firm body is inside the fence, not authored as the report's own top-level sections. The four `edit:`/`new:` insert-anchor blocks (index.md ×3, SUMMARY.md ×1) all match on-disk anchor text (the `:73` rough-in bullet, the `floquet-correction` dep-map row, the `fe_assemble` SUMMARY line). The sibling `fe_assemble.md` residual `:215-217` drift at lines 147 and 257 is **confirmed present** and **correctly left un-edited** (see plan-kind / issues).

**edge-label-fidelity — pass.** The proposal's lowering edge is L1>L0 (`lowers_to: L1-L0/fe-operator-assemble-mutation-rotation`), and the §"Downward to L0" / §"L1 vs L0 distinction" prose discusses exactly that edge (L1 pure form → L0 deferred-config-then-apply). No mismatched edge label.

**plan-kind-consistency — pass.** Declared kind is firm L1 operator; content shape matches — full signature, shape contract, semantics, four algebraic laws with explicit non-laws, applicability, variant axes, firm `## Status` with a stated clean-gate justification, evidence, L1/L0 distinction. No rough-in placeholders inside the firm body. The firm-on-positive-structure escape (no dedicated test, non-gating for syntactic-identity laws) is correctly invoked with the `apply_linop`/`fe_assemble` precedent — and I verified the laws ARE syntactic identities on the read `EliminateBC` zero-rows-cols-then-set-diagonal map + recorded `(dofs, policy)`, not constructed claims, so `firm` (not `rough-in (test-coverage-bounded)`) is the right tier.

**skill-uptake-survey — pass.** Report references `citecheck.py --anchor` (the citation source-of-truth, §"Supporting evidence"), codemap localization, and names `upgrade-plain-text-ref-to-live-link-when-target-on-disk` for the `eliminate_rhs` follow-on. Telemetry present; no missing-skill signal.

### Issues found

No blocking issues. The clean-gate + firm call is **correct**, the citation-drift correction is **verified correct against source**, the variant axes are **sound and exhaustive**, and the separable-post-composition framing is **well-grounded** (matches `fe_assemble.md` law 5's upstream framing; the elimination acts on `(K, dofs, policy)` independent of how `K` was assembled). The following are minor/observational, surfaced for the repairer/integrator to weigh — none changes the verdict.

1. **(observational, severity: info — by-design, correctly handled) Sibling `fe_assemble.md` residual drift.** `book/src/L1/fe_assemble.md` carries the un-corrected `palace/models/laplaceoperator.cpp:215-217` at line 147 (§Algebraic laws law 5) and line 257 (§Evidence). I confirmed both on-disk; the correct range is `216-217`. D4 **correctly did NOT edit it** — this is a different chapter, outside the dispatch's write-scope (harvester writes only `reports/<id>/CYCLE.md` + the new operator file via proposed-changes; cross-chapter edits to a sibling firm entry are not in the dispatch-phase partition). D4 flagged it as OQ-1 for a follow-on citation-fix dispatch / the integrator. This is the right call. Recording it here so the integrator has the exact locations (fe_assemble.md:147, fe_assemble.md:257) if it chooses to fix-on-touch.

2. **(observational, severity: info) Law-4 affine-distribution sign of the `DIAG_ONE` clause.** Law 4 states `eliminate_essential_bc(K₁ + K₂, E, DIAG_ONE) = eliminate_essential_bc(K₁, E, DIAG_ONE) + eliminate_essential_bc(K₂, E, DIAG_ZERO)` (the `I_E` added once via the `DIAG_ONE` term, the second term using `DIAG_ZERO` so `I_E` is not double-counted). This is algebraically correct (`P_F K₁ P_F + I_E) + (P_F K₂ P_F) = P_F(K₁+K₂)P_F + I_E`) and the prose ("the `I_E` is added once, not per-term") makes the asymmetry explicit. No defect — noting only because the mixed-policy RHS is initially surprising and a future reader/lifter should not "normalize" it to symmetric `DIAG_ONE` on both terms (which would double-count `I_E`).

3. **(observational, severity: info) Eigen-pipeline "both policies" claim.** §Variant-axes states the eigen pipeline "exercises both [policies] across its A/B blocks." Verified against source: `Ar` uses `DIAG_ONE` (`:571`), `Ai`/`Br`/`Bi` use `DIAG_ZERO` (`:574,608,611`). So both policies ARE exercised (DIAG_ONE on the real A block; DIAG_ZERO on the imag-A and both B blocks). The claim is accurate; the slightly-loose "across its A/B blocks" phrasing is fine.

4. **(observational, severity: info) `DofSet[N]` un-typed concept.** D4 introduces `DofSet[N]` in the signature and flags (OQ-5) that it is not yet a `concepts/` page, correctly deferring authorship to layer-intro-author scope. No action needed; the type is a thin index-subset and the deferral is appropriate. Surfaced as telemetry for the plan (it will recur under `eliminate_rhs`).

## Repair

### Fixes attempted

All 8 critic checks PASS with no blocking issues; all 4 surfaced items are explicitly observational (severity: info) and carry no fix. There is nothing in repair scope to apply — no missing citation, no off-by-N range slip in the report's own surface, no dep-map/append-by-slug gap, no fence/heading normalization, no SIDEWAYS/append-fallback rewrite. The report is a clean firm L1 promotion on positive structure.

Per-finding accountability:

- **Finding 1 — sibling `fe_assemble.md` residual `:215-217` drift (lines 147, 257).**
  - **Decision**: not-needed (repair).
  - **Rationale**: This is a different chapter from the report's product. Editing `book/src/L1/fe_assemble.md` is an artifact (book/) mutation, which is explicitly out of repairer authority — the repairer does not modify `book/`. D4 correctly left it un-edited (out of dispatch-phase write-partition) and routed it as OQ-1. Recording the exact integrator-facing locations below. NOTE: the critic confirmed the drift is present at fe_assemble.md:147 (§Algebraic laws law 5) AND fe_assemble.md:257 (§Evidence) — i.e. in 2 line locations within 1 sibling chapter (the task framing's "1 place not 2" refers to it being a single chapter; the critic's META lists two line anchors). Correct range is `216-217`.

- **Finding 2 — law-4 mixed-policy (`DIAG_ONE`/`DIAG_ZERO`) RHS note.**
  - **Decision**: not-needed (repair).
  - **Rationale**: Critic verified the law is algebraically correct and the prose already makes the `I_E`-added-once asymmetry explicit. No defect; observational only (a guard against a future reader "normalizing" it to symmetric DIAG_ONE).

- **Finding 3 — eigen-pipeline "both policies" confirmation.**
  - **Decision**: not-needed (repair).
  - **Rationale**: Critic verified the claim accurate against source (`Ar` DIAG_ONE `:571`; `Ai`/`Br`/`Bi` DIAG_ZERO `:574,608,611`). Accurate as written.

- **Finding 4 — deferred `DofSet[N]` concept page.**
  - **Decision**: not-needed (repair).
  - **Rationale**: Authoring a `concepts/` page is substantive content authoring (layer-intro-author scope), out of repair authority. Correctly deferred via OQ-5; plan telemetry only.

### Unrepairable findings

None. No finding required substantive authoring or contradicted artifact content in a way the integrator must defer; the only artifact-touching item (Finding 1) is a by-design out-of-scope sibling drift routed as an OQ, not a defect in this report's surface.

## Suggested resolution

`overall_status: ready` — clean firm L1 promotion; `follow_up_agent: null`.

Notes for the integrator:
- **D4 proposed-changes**: `new:book/src/L1/eliminate_essential_bc.md` (firm, full apparatus inside a parity-balanced fence) + the `index.md` `:73` rough-in→firm bullet flip + the `floquet-correction` dep-map row + the `SUMMARY.md` line. Fence parity even (16 markers); the `new:` block at CYCLE.md L41–342 encloses the full firm body (Signature L94 / Algebraic-laws L163 / Status L253 / Evidence L296). Citation gate clean: citecheck 26 ok / 0 failing.
- **DEFERRED**: the cohort-header count adjustment is owned by D7 (not D4) — do not double-count here.
- **OQ-1 to promote (for a future lifter / citation-fix dispatch)**: sibling `book/src/L1/fe_assemble.md` carries the stale `palace/models/laplaceoperator.cpp:215-217` at lines **147** and **257**; correct range is **216-217**. Out of D4's write-partition; fix-on-touch optional for the integrator. (Single sibling chapter, two line anchors.)
- Findings 2–4 are info-level telemetry; no integrator action required.
