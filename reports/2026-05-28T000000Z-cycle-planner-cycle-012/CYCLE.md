---
agent: cycle-planner
invoked_at: 2026-05-28T000000Z
scope: cycle-012 dispatch plan (third primary cycle of meta-batch-2)
status: pending
---

# Cycle-012 dispatch plan

## Goals selected this cycle

Cycle-012 is the **closing cycle of meta-batch-2** (cycles 010/011/012); meta-phase fires immediately after integrator-finalize completes. The planner's role is to push forward on actionable OQs and priorities while providing clean signals for meta-phase aggregation. Key constraints: **do NOT over-load the cycle**; a clean 8-9 dispatch cycle leaves room for meta-phase to surface patterns naturally rather than drowning them in new work. Dispatch targets are:

1. **High-priority OQ closure candidates** that benefit meta-phase aggregation (L3 directory-naming policy codification blocker; orthogonalize promotion gating further slice reduction; L1 Chebyshev firm-row promotion unblocking chebyshev.md reduction).
2. **Smallest-cost cleanup dispatches** (L4 index drift; L3 index prose refresh; concept-page corrections).
3. **Small audit/continuation dispatches** that close cycle-009/010 follow-ups (eigsolve lowering-verifier; SLEPc coordinate-convention audit).
4. **Phase-1 corpus reduction batch-3** (methodologically distinct: polynomial_recurrence_step was negative-result; plane_rotation_stream / divfree / cg_preconditioning_framework have heterogeneous disposition).

## Dispatches

| # | Agent | Scope | Deps | Rationale |
|---|-------|-------|------|-----------|
| 1 | **same-layer-cross-cutter** | phase-1 corpus reduction batch-3 (2 slices: plane_rotation_stream + divfree) | none | Priority #19 continuation. Batch-3 has 4 remaining slices (plane_rotation_stream, divfree, cg_preconditioning_framework, sparse_triangular_solve). Audit 2 slices per dispatch per cycle-010/011 template. plane_rotation_stream is a subtask of the larger cycle-011 orthog audit (orthog slice reduced; plane-rotation sub-slice deferred to batch-3 joint audit per OQ). Divfree is independent. Yields disposition verdicts + reduction proposals + coverage-gap flags. Critical meta-phase input: if batch-3 closes, the Phase-1 corpus reduces to 4 remaining; if all Phase-1 slices eventually reduce, the methodology validates the "Phase 1 corpus reduces as material is lifted" directive. |
| 2 | **harvester** | L1/orthogonalize promotion (small, gated on orthog slice now reduced) | none | Cycle-010 OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog` — harvester-candidate. Landing unblocks further reduction of arnoldi_step.md + orthog.md (both flagged as 2-slice-blockers). Small operator per unimplemented-Palace-stub policy: gs_orthog + MPI-collective shape table. Cycle-010 cycle-planner added priority-weight upgrade for batch-2-or-3 harvester. Cycle-011 batch-2 reduced orthog.md (L0→L1 Gram-Schmidt body replaced with reduced stub); orthogonalize promotion is now unblocked. High-priority signal for slice reduction cascade. Cite: cycle-011 integrator-signals §Unblocked + cycle-010 wave-2 pass-8 OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog`. |
| 3 | **harvester** | L1/chebyshev-smoother + L2/chebyshev-iteration firm-row promotion (gated; bundled) | none | Cycle-011 OQ `l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion` — unblocks further chebyshev.md reduction. Cycle-011 wave-2 pass-9 surfaced: chebyshev.md currently retains L1/L2/L3/L4 sections pending the firm-row promotion. Landing would allow chebyshev.md reduction to just-the-slice-sections (removing the duplicative L1/L2 verb sections). Bundled as 2-operator dispatch (same conceptual gate: both needed to unblock the same slice reduction). Cite: cycle-011 integrator-signals §Suggested next dispatches. |
| 4 | **lowering-verifier** | L1>L0 eigsolve-mutation-rotation per-line audit (cycle-011 firm-structural-but-partly-constructive theme) | none | Cycle-011 wave-2 pass-6 landed `book/src/L1-L0/eigsolve-mutation-rotation.md` as first firm-structural-but-partly-constructive theme; Sub-pattern B (LinearSolveFailed materialisation) is partly-constructive pending upstream Palace refactor OR lowering-verifier audit. Defer per-line verification is standard for constructed-operator themes (cycle-008 ksp_solve precedent did the same). Walk each backend body (ARPACK / NLEPS / SLEPc shell) and confirm the 4 sub-pattern rewrites are exhaustive at the per-step level. Result: either unblock partly-constructive → firm promotion, or surface additional obstruction work. Cite: cycle-011 integrator-signals §Suggested next dispatches `eigsolve-mutation-rotation-lowering-verifier-followup`. |
| 5 | **lifter** / **lowering-verifier** / **harvester-NEP** | SLEPc-NEP coordinate-convention audit (small; concrete gap) | none | Cycle-011 wave-2 pass-7 repairer surfaced new OQ `eigsolve-slepc-nep-coordinate-convention-audit` — concrete follow-up on SLEPc-NEP coordinate-convention gap (gamma computed at SetOperators :1645-1651, :1711-1719 but not applied at GetEigenvalue :1554-1560; "NEP gamma = 1" reading is wrong). Routable to lifter / lowering-verifier / harvester-NEP. Small dispatch; can route to any of the three per expertise. Cite: cycle-011 integrator-signals §Unblocked (line 50). |
| 6 | **layer-intro-author** | L3 index semantics-overlay BLAS-1 cohort prose refresh (smallest-cost) | none | Cycle-011 wave-1 pass-4 OQ `l3-index-semantics-overlay-blas1-cohort-prose-refresh` — concrete refresh for L3 index `## Semantics (overlay)` prose at `book/src/L3/index.md:11-15`. Prose lists "matvec, axpy, dot, nrm2 as field operations" but does not literally name scal / axpby / axpbypcz / apply_linop (now fully reflected in the dep-map table). Smallest-cost cycle-012 cleanup. Cite: cycle-011 integrator-signals §Unblocked (line 48). |
| 7 | **same-layer-cross-cutter** / **layer-intro-author** | Concept-page corrections: nrm2-stability-claim + 3 concept-page extensions (bundled) | none | Cycle-011 OQ `concepts-nrm2-stability-claim-correction` — false stability claim at `book/src/concepts/nrm2.md:8-9` contradicts L1 entry's authoritative finding. Cite: cycle-011 integrator-signals §Unblocked (line 49). PLUS cycle-011 OQ cluster opening 3 concept-page extension OQs (state-stratification four-stratum / derived-view-hoisting control-flow-boundary / negative-result-slice partial-positive). Layer-intro-author can handle all 4 in one dispatch (concept-page extension pattern established; bundled concept work). Cite: cycle-011 integrator-signals §Unblocked (line 56). |
| 8 | **lifter** | L4/index.md:40 SUPERSEDED-text drift (smallest-cost) | none | Cycle-010 OQ carry-forward. Cycle-010 wave-1 pass-1 enacted substantive (added `book/src/L3/krylov-step.md`); the index drift is cross-reference cleanup that dispatch did not touch. Single-edit cleanup pointing at the cycle-010 wave-1 pass-1 L3 backfill enactment. Smallest-cost cycle-012 dispatch. Cite: cycle-011 integrator-signals §Suggested next dispatches (line 91). |

## Overlap analysis

| Pair | Touch Regions | Status |
|------|---------------|--------|
| 1–2 | `scaffolding/open-questions.md` (1 reads orthog reduction verdict; 2 appends new OQs on orthogonalize) | **SEQUENTIAL** (1 must complete first; 2 references orthog.md reduced status) |
| 1–3 | `scaffolding/open-questions.md`; no shared operator/file | **PARALLEL** (distinct file regions; append-before discipline holds) |
| 1–4 | No overlap (reduction audit vs lowering-verifier on distinct themes) | **PARALLEL** |
| 1–5 | No overlap | **PARALLEL** |
| 1–6 | `book/src/L3/index.md` (1 does not touch; 6 updates prose) | **PARALLEL** (1 calls plane_rotation_stream + divfree in spec/slices/; 6 touches L3/index.md directly) |
| 1–7 | `book/src/concepts/` + `scaffolding/open-questions.md` | **PARALLEL** (distinct file regions) |
| 1–8 | No overlap | **PARALLEL** |
| 2–3 | `book/src/L1/` (2 creates orthogonalize.md; 3 creates chebyshev-smoother.md) + `scaffolding/open-questions.md` | **PARALLEL** (distinct L1 files; append-before on OQs) |
| 2–4 | No overlap | **PARALLEL** |
| 2–5 | No overlap | **PARALLEL** |
| 2–6 | `book/src/L3/index.md` (2 does not touch; 6 updates prose) | **PARALLEL** |
| 2–7 | No overlap | **PARALLEL** |
| 2–8 | No overlap | **PARALLEL** |
| 3–4 | No overlap | **PARALLEL** |
| 3–5 | No overlap | **PARALLEL** |
| 3–6 | No overlap | **PARALLEL** |
| 3–7 | No overlap | **PARALLEL** |
| 3–8 | No overlap | **PARALLEL** |
| 4–5 | `book/src/L1-L0/eigsolve-mutation-rotation.md` (4 audits; 5 audits same file's SLEPc section) | **SEQUENTIAL** (4 lower-level audit may inform 5's concrete coordinate-convention fix) |
| 4–6 | No overlap | **PARALLEL** |
| 4–7 | No overlap | **PARALLEL** |
| 4–8 | No overlap | **PARALLEL** |
| 5–6 | No overlap | **PARALLEL** |
| 5–7 | No overlap | **PARALLEL** |
| 5–8 | No overlap | **PARALLEL** |
| 6–7 | `book/src/concepts/` (both touch concepts but different files: 6 → L3/index.md; 7 → nrm2.md + 3 extension pages) | **PARALLEL** |
| 6–8 | No overlap | **PARALLEL** |
| 7–8 | No overlap | **PARALLEL** |

**Summary**: 1 sequential edge (1→2; 2 gates on orthog reduction); 1 sequential edge (4→5; 4 audit may inform 5); all others PARALLEL.

## Sequencing schedule

**Wave 1 (parallel)**: dispatches 3, 6, 7, 8 (no inter-dependencies; smallest-cost cleanups + Chebyshev harvester + concept work).

**Wave 2 (parallel; after wave-1 completes)**: dispatches 2, 5 (dispatch 2 gates on dispatch 1's orthog reduction verdict; dispatch 5 may benefit from dispatch 4's audit).

**Wave 3 (serial)**: dispatch 1 (phase-1 corpus reduction audit; depends only on cycle-011 slice-reductions being landed; placed last to use wave-1/wave-2 dispatch results as context for plane_rotation_stream audit if needed).

**Wave 4 (serial after wave 3)**: dispatch 4 (lower-level audit; no hard dependency but placed after corpus audit to see full context).

**Rationale for reordering**: Phase-1 corpus reduction batch-3 is methodologically distinct (mixed disposition; plane_rotation_stream is a sub-task of cycle-011 orthog audit) and large in scope. Moving it to wave-3/4 gives the smaller, highest-priority cleanups (wave-1) and the orthogonalize/Chebyshev harvesters (wave-2, gated by orthog reduction) time to complete. When the integrator applies the later dispatches, they'll have fresh context on the corpus status.

## Accuracy check notes

**File path verification for dispatches' source citations:**

- **Dispatch 2** (orthogonalize): L0 source at `reference/palace/` (MCP localization on first call will verify gs_orthog enum location).
- **Dispatch 3** (Chebyshev harvester): L0 source at `palace/linalg/chebyshev.cpp` / `palace/linalg/chebyshev.hpp` — **VERIFY-BEFORE-DISPATCH** that these exist (not chebyshev_smoother.cpp, etc.).
- **Dispatch 4** (eigsolve lowering-verifier): references `book/src/L1-L0/eigsolve-mutation-rotation.md` (confirmed existed cycle-011 wave-2 pass-6); SLEPc source at `reference/palace/eigensolver/slepc.cpp` (exists per cycle-011 references).
- **Dispatch 5** (SLEPc-NEP audit): references `palace/eigensolver/slepc.cpp:1645-1651`, `:1711-1719`, `:1554-1560` — **VERIFY-BEFORE-DISPATCH** that line ranges are accurate (high probability of drift in large file; dispatch should re-grep on first call).
- **Dispatch 6** (L3 index refresh): `book/src/L3/index.md` (confirmed exists; cycle-011 wave-1 passes 1-4 touched it 4 times; current line ranges likely stable).
- **Dispatch 7** (concept corrections): `book/src/concepts/nrm2.md` + 3 extension candidates — **VERIFY-BEFORE-DISPATCH** on the 3 extension candidates (state-stratification, derived-view-hoisting, negative-result-slice) that the 3 concept-page slugs do not yet exist.
- **Dispatch 8** (L4 index drift): `book/src/L4/index.md:40` — **VERIFY-BEFORE-DISPATCH** that the SUPERSEDED text still exists (carry-forward from cycle-010; may have been edited in cycle-011 wave-2 passes).

## Open questions expected to close this cycle

**High confidence (>85%) — meta-phase will observe these as CLOSED or PARTIALLY-ANSWERED:**

1. `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog` (dispatch 2 harvester) — **ANSWERED** (operator lands as firm L1 entry).
2. `l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion` (dispatch 3 harvester) — **ANSWERED** (both operators land; unblocks chebyshev.md reduction).
3. `l3-index-semantics-overlay-blas1-cohort-prose-refresh` (dispatch 6 layer-intro-author) — **ANSWERED** (prose refreshed to include scal / axpby / axpbypcz / apply_linop).
4. `concepts-nrm2-stability-claim-correction` (dispatch 7 same-layer-cross-cutter) — **ANSWERED** (concept page corrected).
5. `eigsolve-slepc-nep-coordinate-convention-audit` (dispatch 5 lifter/lowering-verifier) — **PARTIALLY-ANSWERED** (audit completed; may surface deeper Palace refactor need).
6. `eigsolve-mutation-rotation-lowering-verifier-followup` (dispatch 4 lowering-verifier) — **PARTIALLY-ANSWERED** (per-line audit completed; partly-constructive gate assessment may remain pending upstream Palace work).
7. `book/src/L4/index.md:40` SUPERSEDED-text drift (dispatch 8 lifter) — **ANSWERED** (single-edit cleanup).

**Medium confidence (60–85%) — meta-phase will observe as PARTIALLY-ANSWERED or candidate for future dispatch:**

8. `phase-1-corpus-reduction-remaining-7-slices` (dispatch 1 same-layer-cross-cutter) — **PARTIALLY-ANSWERED** (batch-3 closes 2 of 4 remaining slices; net ledger reduces 6 of 10 → 8 of 10; remaining 2 deferred to batch-4+ or left as stable verdicts).
9. 3 concept-page extension OQs (dispatch 7 layer-intro-author) — **ANSWERED** (3 concept pages created/extended).

**Low-medium confidence (40–60%) — may remain OPEN for cycle-013+:**

10. `l3-l1-directory-naming-structure-policy` — **NOT closed by dispatch.** This is a **meta-phase decision item** (count = 7 exceeds threshold). Cycle-012 dispatch does not address; meta-phase decides codification vs directory-structure change.

## Note on cycle-012 meta-phase inputs

This dispatch is intentionally **light** (8 dispatches; cap 12 allows 4 more if bottlenecks surface; planner is being conservative). Rationale:

1. **Clean signal landscape for meta-phase:** Meta-phase aggregates evidence across cycles 010/011/012. Over-loading cycle-012 with speculative work (e.g., gmres.md §L4 v0.6→v0.7 self-rotation, NLEPS at L1+, L2 cohort growth candidates) would generate new OQ noise that obscures recurring patterns the meta-phase needs to detect (negative-anchor citation, partly-constructive theme status, lifter-scope content-correction boundary, dispatch-prompt framing drift, skill-uptake-survey gap).

2. **Critical meta-phase targets preserved:** The integrator-signals §CRITICAL cycle-012 meta-phase batch-2 aggregation targets are:
   - `l3-l1-directory-naming-structure-policy` closure decision (count = 7 exceeds threshold) — **NOT dispatched; meta-phase decides**.
   - Negative-anchor-citation pattern at recurrence-2 — **NOT changed by dispatch; 2-cycle pattern stands for meta-phase codification**.
   - Partly-constructive lowering-theme-status at recurrence-2 — **dispatch 4 may add slight evidence; not the focus**.
   - Lifter-scope content-correction boundary at recurrence-2 — **dispatch 7 may touch edge of this via concept-correction; not the focus**.
   - Dispatch-prompt framing drift at recurrence-2 — **dispatch 5 brief checked; path `/palace/eigensolver/slepc.cpp` verified; low risk**.
   - MCP codemap usage stable post-pilot SUCCESS — **cycle-012 MCP usage expected to be light; no escalation**.
   - Phase-1 corpus reduction batch-3 / skill-promotion — **dispatch 1 advances batch-3; skill promotion is meta-phase scope**.

3. **Integrator-finalize context:** Split integrator (integrator-per-report serial + integrator-finalize) runs every cycle. After 8 wave-parallel dispatches, integration will be clean per 7-cycle precedent (cycles 005–011 all clean; zero deferrals/rejections). Integrator's final report will feed directly into meta-phase aggregation.

---

**Cycle-012 opens now. Plan complete.**
