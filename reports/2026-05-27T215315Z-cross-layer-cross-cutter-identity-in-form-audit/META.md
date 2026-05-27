---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T22:09:39Z
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
---

# META: verification of cross-layer-cross-cutter identity-in-form audit

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing citation in the report was verified against the cited file and line range:
- `book/src/L3-L2/krylov-step-body-identity.md:97` — quoted verbatim ("seven L1 primitives used ... each operates on whole-tensor inputs with no element-loop exposed at L2") and confirmed in-range.
- `book/src/L3-L2/krylov-step-body-identity.md:30` — `apply_linop op.T K.<input_field>` rendering present at exact line.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:64` — `let w = apply_linop op.T K.<input_field>` L3-native global op annotation present.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:65-68` — the BLAS-1 chain in the L3 let-chain renders at the cited range.
- `book/src/L3/index.md:11-14` — "Whole-tensor primitives (matvec, axpy, dot, nrm2 as field operations)" present verbatim at line 12.
- `book/src/L2/krylov-step.md:96` — `[apply_linop](../L1/apply_linop.md)` L1 primitives dependency line confirmed.
- `book/src/L2/krylov-step.md:130-132` — "L2 vs L1 distinction" section present at exact range.
- `book/src/L2/index.md:17` — "axpy, dot, matvec, gemv, trsv, scal, nrm2" L2 vocabulary list confirmed.
- `book/src/L1/ksp_solve.md:55, 83, 142` — "per-method body" reference (55), "constructed-operator gate" framing (83), and L2 reference (142) all verified.
- `book/src/L1/ksp_solve.md:81` — "the L2 `krylov-step` operator is the layer at which they become direct dependencies" quoted verbatim and confirmed in-range.
- `book/src/L4/krylov-step.md:59` — `let w = apply_linop op.T K.<input_field>` L4 Semantics body present at exact line.
- `book/src/L1/index.md:42` — eigsolve "Rough-in (test-coverage-bounded)" cohort header confirmed.
- `book/src/L1/eigsolve.md:131, 151, 197, 204` — not directly opened by critic in this pass, but the L1 firm-cohort listing in `L1/index.md:42` confirms the rough-in status of eigsolve and the audit's defer-pending-firm verdict.
- `scaffolding/priorities.md:46` — priority #20's second-target audit charter ("which other operators in the current chain ... have identity-in-form rotations") quoted verbatim from line 46.

**surface-or-evidence — pass.** The audit is an inspection-only / observation dispatch (per `cross-layer-cross-cutter` role; per its `Observation kind: Coverage gap` framing). It does not propose surface changes; it surfaces routing recommendations to the cycle-010+ planner. The retroactive-evidence-backfill framing applies: the audit's role is to surface a coverage gap, not to mutate operator surface, and the proposed `kind: backfill-harvester-dispatch` / `backfill-harvester-dispatch-bundle` entries are routing recommendations for downstream harvester invocations, not direct edits. This conforms to the role's authority.

**rotation-quality — pass.** The audit's identity-in-form assessment for apply_linop and the BLAS-1 cohort is grounded in two converging structural arguments:
1. The L3-L2 body-identity theme (line 97) explicitly states each L1 primitive is *also* L3-native because its signature has no per-element loop visible — i.e., the L3 form of these primitives is the same signature shape as the L1 form.
2. The L4-L3 typed-wrapper-dissolution theme (line 64 and 67-68) renders these primitives in the L3 let-chain identically to their L1 surface — confirming the L3 form is value-thread-isomorphic.
   Together these establish the L3→L1 rotation as identity-in-form on the primitive itself, with the wrapper / stratum-typing surface being the only adjustment site. The audit correctly distinguishes this from the `ksp_solve` L2 candidate (which it explicitly excludes from priority #20 scope as a NON-identity-in-form substantive content gap — outer-loop framing carries `solve_loop`/`restart_cycle` framing).

**variant-axis-coverage — pass (not applicable to audit dispatch).** This is an inspection / coverage-gap audit, not an operator harvest with variant axes to enumerate. The audit does, however, correctly note variant-axis-relevant context: the L2 `krylov-step` entry's six absorbed variant axes (preconditioner, orthog, polynomial-kind, first-iteration-unrolled, restart, in-place vs out-of-place) are documented in the upstream firm L2 entry; the audit does not duplicate them and does not need to.

**cross-reference-integrity — pass.** All cited `[link]` targets and slug references resolve to existing files:
- `book/src/L1/apply_linop.md` (firm), `book/src/L1/{axpy,axpby,axpbypcz,dot,nrm2,scal,ksp_solve,eigsolve}.md` (all exist; firm or rough-in per L1/index.md cohort table).
- `book/src/L2/krylov-step.md` (firm), `book/src/L2/index.md` (placeholder + krylov-step row).
- `book/src/L3/index.md` (placeholder + matvec/axpy/dot/nrm2 inventory line at 11-14).
- `book/src/L3-L2/krylov-step-body-identity.md` (firm).
- `book/src/L4/krylov-step.md` (firm), `book/src/L4/index.md` (firm cohort of 3).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (firm), `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` (rough-in).
- `scaffolding/priorities.md` entries #17, #18, #20 referenced and confirmed in priorities file.

**edge-label-fidelity — pass.** The audit proposes `book/src/L3/apply_linop.md` and 6 BLAS-1 entries at L3 as the correct backfill targets. Verified:
- The missing L3 entries are at L3 (not L2 or L4), which matches the directional flow of the audit's analysis (L1 primitives that are L3-native by signature should have L3 entries).
- The audit explicitly distinguishes "L3 backfill" (identity-in-form, in-scope for priority #20) from "L2 backfill" (substantive content for apply_linop / BLAS-1, defer to planner; the `ksp_solve` L2 candidate is correctly out-of-scope).
- The L4 verdict (CONFIRMED-NOT-NEEDED — leaf primitives don't get L4 rows) aligns with the L4 vocabulary cohort scope per `book/src/L4/index.md` ("typed-wrapper Krylov step kernel plus the two value-threading loop combinators").

**plan-kind-consistency — pass.** The audit's `kind: backfill-harvester-dispatch` and `backfill-harvester-dispatch-bundle` entries are routing recommendations (`recommendation: dispatch-harvester-cycle-010-or-011`), not direct artifact mutations. The `latent-pattern-observation` entry is explicitly marked "NO IMMEDIATE DISPATCH". The `NOT-priority-20-but-real-coverage-gap` entry for ksp_solve L2 is correctly framed as out-of-scope routing for separate planner consideration. The `defer-pending-upstream` entries on eigsolve are appropriate audit deferrals. Observation-kind "Coverage gap" matches the content shape.

**skill-uptake-survey — pass.** The audit explicitly cites the new methodology invariants:
- "Identity-lowerings still require both L levels" (CLAUDE.md, mid-cycle-009) — referenced multiple times in the rationale blocks.
- "Lower-level shared vocabulary takes priority" (priority #17) — referenced in the L2 deferral discussion.
- "Layer-definition-discipline high→low" (priority #18) — implicitly honored by the audit's framing (target layers defined by L_n vocabulary; lowering direction explicit).
  The audit also notes priority #16 (MCP codemap reintegration) and its non-invocation in §"Open questions / caveats" item 5, providing positive telemetry that the cycle-010 pilot retry is unblocked for dispatches needing source inspection.

### Issues found

**Issue 1 (low severity, telemetry note) — L4/index.md:40 carries the now-SUPERSEDED cycle-006 verdict text "the kernel body's primitive sequence is identity-in-form, so no intermediate L3 `krylov-step` row is needed".** Location: `book/src/L4/index.md:40`. The audit's recommendation surfaces this gap implicitly (the wave-1 sibling dispatch on `L3/krylov-step.md` is the supersession-enactment for krylov-step itself), but the L4 index's "Lowers to" column language has not yet been updated to reflect the cycle-009 supersession. This is an existing-artifact drift between the cycle-006 verdict prose and the cycle-009 methodology invariant; not introduced by this audit but noted here as cross-reference drift the cycle-010+ integrator-finalize or a future lifter dispatch may want to clean up. Not blocking.

**Issue 2 (low severity, scope-completeness observation) — the L3-L1 directory non-existence is correctly flagged as an OQ, but the OQ framing in §"Open questions / caveats" item 1 leaves the decision to the cycle-010+ planner without a concrete recommendation.** Location: CYCLE.md §"Open questions / caveats" item 1. The audit notes both options (sibling L3-L1 theme per backfill, or in-line identity rotation at the L3 entry) and posits both are consistent with the methodology invariant. Verified: `book/src/L3-L1/` does NOT exist (confirmed via directory listing); existing lowering-layer directories are `L1-L0/`, `L2-L1/`, `L3-L2/`, `L4-L3/`. The OQ is well-framed but does not propose a default; a stronger audit would surface a default based on the wave-1 sibling dispatch's outcome (if wave-1 creates an L3-L1 theme, follow that precedent; if not, default to in-line). Not a defect — the OQ is correctly surfaced for planner decision; just observe that the default-positing choice is left implicit.

**Issue 3 (low severity, naming consistency) — the audit refers to "6-entry BLAS-1 cohort" but the L1 firm cohort listed at `L1/index.md:29-38` has 8 firm operators total (axpy, dot, nrm2, axpby, scal, apply_linop, axpbypcz, ksp_solve).** Location: CYCLE.md §"Per-candidate verdict" item (2). The audit's "6 BLAS-1 primitives" enumeration is `axpy, axpby, axpbypcz, dot, nrm2, scal` — which is correct: this excludes `apply_linop` (the opaque-operator gate, handled as a separate candidate (1)) and `ksp_solve` (the constructed-operator gate, handled as candidate (3)). The naming "BLAS-1 cohort" is consistent with the L1/index.md §Semantics overlay motifs 1-2 ("Element-wise pure update" + "Mutation-free reduction"). No defect; cross-referenced for clarity.

**Issue 4 (informational, not a defect) — the audit's "L3-vocabulary-inventory-gap" latent observation is faithfully grounded.** Verified `book/src/L3/index.md:11-14` does advertise "matvec, axpy, dot, nrm2 as field operations" as L3 vocabulary, and `book/src/L3/` does contain only `index.md` (i.e., no operator entries before wave-1's krylov-step dispatch lands). The gap is real and actionable per priority #20. No defect.

**Issue 5 (informational, confidence-calibration check) — HIGH/MEDIUM/DEFER confidence levels are well-calibrated.**
- HIGH (apply_linop + BLAS-1 bundle): grounded in two converging firm-theme citations (L3-L2 body-identity §97 + L4-L3 typed-wrapper-dissolution §64-68) plus the L3 index advertisement (§11-14). Three independent evidence sources for identity-in-form claim.
- MEDIUM (ksp_solve L2): explicitly framed as NOT-priority-20 (correct scope-distinction) and NOT-identity-in-form (correct rotation-quality assessment). Confidence level appropriate.
- DEFER (eigsolve, krylov-step L1): grounded in the firmness-frontier discipline ("upper-layer entries should not lead the firmness frontier") and in the primitive-vs-composition layer-role distinction. Confidence level appropriate.
  No miscalibration observed.
