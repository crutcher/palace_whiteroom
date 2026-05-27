---
agent: cycle-planner
invoked_at: 2026-05-27T180000Z
scope: cycle-008 dispatch plan
status: pending
batch_cycle_ids: [cycle-008]
meta_batch: batch-1 (cycles 007/008/009; meta-phase fires after 009)
---

# Cycle 008 dispatch plan

## Goals selected this cycle

**Cycle-008 closes the iterate-while L3 trajectory-accumulation gap.** Cycle-007's wave-2 lowering-verifier audit (verdict (c)) identified the resolution path: cite `derived-view-hoisting` §3.8 collapse-rule, add a new Condition 5, sketch the two forms (pruned vs unpruned). The priority lifter dispatch lands this substantive patch at `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`, which both closes OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` AND auto-promotes the upstream L3>L2 `krylov-step-body-identity` theme from `firm-rough-in` to plain `firm` via status-inheritance.

Secondary goals: continue L0 bootstrap (bundle 4), harvest the first L1>L0 theme for a constructed-operator (ksp_solve), refresh L1 index with the new Constructed-operator absorption motif (motif 4), housekeep the 5 stale L0 forward-declaration notes, migrate GMRES inner-loop to iterate-while, and refresh L4 index with the Vocabulary-cohort subsection (3 firm L4 operators now eligible).

## Dispatches

| # | Agent | Scope | Deps | Rationale |
|---|---|---|---|---|
| 1 | `lifter` | `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` — apply cycle-007 wave-2 audit verdict (c) | none | **CYCLE-008 PRIORITY** per cycle-007 integrator-signals. Change 2: add `verified_against:` 10-citation block (trailing YAML per `axpby-mutation-rotation.md` precedent). Change 3: substantive §3.8 revision (cite Law 1 + `concepts/derived-view-hoisting.md`, replace 9-line sketch with two-form pruned/unpruned, add Condition 5 to applicability section). Upon landing, OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` becomes closeable + L3>L2 `krylov-step-body-identity` auto-promotes from `firm-rough-in` → `firm`. Closes OQ `iterate-while-l3-rendering-trajectory-accumulation-gap`. |
| 2 | `abstractor` | `book/src/L1-L0/ksp-solve-mutation-rotation.md` — L1>L0 theme for ksp_solve constructed-operator absorption | none | First L1>L0 theme for a structured opaque primary argument (KspSolver<OperType>* typed pointer). Routes the mutation-rotation of workspace-pattern absorption + constructed-operator factory selection logic. Closes OQ `ksp-solve-mutation-rotation-l1-l0-theme`. Parallel to dispatch #1. |
| 3 | `layer-intro-author` | `book/src/L1/index.md` — refresh after ksp_solve introduces Constructed-operator absorption motif (motif 4) + Vocabulary cohort 7→8 | 2 | Refresh Context / Semantics / Vocabulary-cohort subsection after dispatch #2 lands `ksp_solve`. Register motif 4 + update cohort count (7→8) to reflect the new firm L1 entry. Closes OQ `l1-intro-refresh-after-constructed-operator-gate`. Depends on ksp_solve landing (semantically, though artifact-wise no blocking). |
| 4 | `same-layer-cross-cutter` | 5 L0 chapters with stale forward-declaration italic notes | none | Cycle-007 L1 thinning sweep completed (priority #11); retroactively, 5 L0 chapters carry stale forward-declaration notes flagging the thinning as pending. Targets: `output-arg-vs-receiver.md:36`, `mfem-vector-types.md:42`, `linalg-free-functions.md:47`, `transparent-vs-load-bearing-tricks.md:34`, `apply-linop-overload-set.md:55`. Reword or remove mechanical notes. Bundlable into one short dispatch. Housekeeping. Parallel to #1. |
| 5 | `layer-intro-author` | `book/src/L0/` — bootstrap bundle 4 (eigensolver-wrapper candidate) | none | Continue priority #10 (bootstrap-L0-reference-layer). Cycle-007 OQ `eigensolver-wrapper-l0-coverage-candidate` identifies this as the bundle-4 candidate. Scope: similar pattern to prior L0 reference chapters (Conventions or File overviews grouping). Remaining candidates if not this cycle: `mpi-globalsum-and-collectives`, `par-types-single-rank-reading`, `linalg-operator-file`, `tests-as-semantic-supplement`. Parallel to #1. |
| 6 | `abstractor` | `book/src/L4-L3/` — GMRES-inner-loop iterate-while migration | none | Both iterate-while L4 anchors now firm (cycle-007). GMRES inner Arnoldi loop's predicate-in-body pattern is a natural migration target. Scope: write a rough-in L4>L3 lowering theme or brief speculative sketch of how the loop's body folds into iterate-while structure. Closes OQ `gmres-inner-loop-iterate-while-migration`. Parallel to #1. |
| 7 | `layer-intro-author` | `book/src/L4/index.md` — refresh post-3-firm-cohort (Vocabulary-cohort subsection) | 1 | L4 now has 3 firm operators (`krylov-step` cycle-006, `iterate_while` + `iterate_while_with_prev` cycle-007). Vocabulary-cohort subsection template eligible (≥3 firms per cycle-004 L1 precedent). Refresh intro structure + add Vocabulary-cohort subsection grouping the 3 firms. Closes OQ `l4-layer-intro-refresh-unblocked-by-first-firm-row` (expanded scope per cycle-007 signals). Depends on cycle-008 stabilization (wave-1 must be complete to count all firm cohort correctly). |

## Overlap analysis

**Dispatch 1 (lifter):**
- Writes to: `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (single file, two subsections: verified_against YAML block + §3.8 revision).
- No overlaps with dispatches 2–7 (each touches distinct files).

**Dispatch 2 (abstractor on ksp_solve @ L1>L0):**
- Writes to: `book/src/L1-L0/ksp-solve-mutation-rotation.md` (new chapter) + `book/src/SUMMARY.md` (append).
- No overlaps with 1, 4, 5, 6, 7.
- Mild semantic dependency with dispatch 3 (context refresh) — 3 reads the results; both touch SUMMARY (same append-anchor discipline as prior cycles).

**Dispatch 3 (layer-intro-author on L1/index refresh):**
- Writes to: `book/src/L1/index.md` (refresh intro + update dep-map row for ksp_solve).
- Semantic dependency on dispatch 2 landing (`ksp_solve` must be firm).
- No artifact overlaps with 1, 4, 5, 6, 7.

**Dispatch 4 (same-layer-cross-cutter on 5 L0 stale notes):**
- Writes to: 5 L0 chapter files (output-arg-vs-receiver.md, mfem-vector-types.md, linalg-free-functions.md, transparent-vs-load-bearing-tricks.md, apply-linop-overload-set.md).
- No overlaps with 1, 2, 3, 5, 6, 7 (each L0 chapter is unique target).

**Dispatch 5 (layer-intro-author on L0 bootstrap bundle 4):**
- Writes to: `book/src/L0/<slug>.md` (new chapter) + possibly a new L0 grouping section in `book/src/L0/index.md`.
- Potential mild overlap with dispatch 4 if both edit L0/index.md (both append new rows) — handled via per-report serial dispatch; both use append-by-anchor discipline.
- No overlaps with 1, 2, 3, 6, 7.

**Dispatch 6 (abstractor on GMRES-inner-loop iterate-while):**
- Writes to: `book/src/L4-L3/` (new or extended theme) + `book/src/SUMMARY.md` (append).
- No overlaps with 1, 2, 3, 4, 5, 7 (distinct L4>L3 theme from dispatch 1).

**Dispatch 7 (layer-intro-author on L4/index refresh):**
- Writes to: `book/src/L4/index.md` (refresh intro + dep-map structure).
- No overlaps with 1, 2, 3, 4, 5, 6 (distinct from all).

**SUMMARY-wide write pattern**: Dispatches 2, 6 both append to SUMMARY.md. Per prior cycles (004, 005, 006), multiple per-report dispatches append to SUMMARY via distinct anchors; serial dispatch order + append-point discipline yields zero collisions. No sequencing constraint needed.

## Sequencing schedule

**Wave 1 (parallel):**
- Dispatches 1, 2, 4, 5, 6 (the priority lifter + four independent parallel siblings).

**Wave 2 (parallel, after wave-1 reports land):**
- Dispatch 3 (L1 intro refresh, depends on ksp_solve from dispatch 2 landing).
- Dispatch 7 (L4 intro refresh, depends on cycle-008 stabilization — can run after wave-1 integrators finalize to confirm cohort firmness).

**Rationale for two waves**: Dispatch 3 is a soft semantic dependency on dispatch 2 (context refresh after new operator); dispatch 7 is a soft observational dependency on the full wave-1 completion (to accurately report L4 cohort state). Both can logically run in parallel with wave-1, but sequentializing them avoids a brief window of potential stale-context reading. Per cycle-007 precedent, the split integrator (`integrator-per-report` runs serially, each reading fresh artifact state) naturally handles dependencies across per-report boundaries.

## Open questions / caveats

- **MCP codemap pilot still deferred to cycle-009 meta-phase.** Per cycle-007 resume-notes, tools still permission-denied. Cycle-008 dispatches do NOT reference mcp_* tools (vanilla Grep/Read/Bash only).

- **L0 bundle 4 candidate uncertainty.** Cycle-007 OQ `eigensolver-wrapper-l0-coverage-candidate` flagged eigensolver as a likely target, but pre-grep confirmation is recommended (e.g., `palace/linalg/eigenvalues.cpp` or similar) to verify the L0 surface exists and is not a stub-only placeholder. If eigensolver is enum-only / MFEM_ABORT, dispatcher should pivot to a different bundle candidate or flag as an obstruction-theme route.

- **Lifter Change 3 citation scope.** The cycle-007 audit verdict (c) specifically mentions Law 1 from `concepts/derived-view-hoisting.md` + the §3.8 collapse rule. Lifter should re-read that concept page and the specific L4>L3 theme subsection to confirm the citation range is fresh and accurate (cross-cycle anchor staleness per friction-ledger).

- **Wave-2 observer pattern note.** Dispatch 7 (L4 intro refresh) relies on observing that cycle-008's 3 L4 firm operators are stable. If a later cycle-008 dispatch somehow de-firms an L4 operator (unlikely but theoretically possible via a critic/repairer workflow), the refresh would need re-reading. This is a non-issue under the current split integrator (per-report integrator reports finalize serially), but flagging for meta-phase documentation if the pattern becomes common.

- **Dispatch 3 semantic flow.** L1 intro refresh (dispatch 3) reads the landing of `ksp_solve` from dispatch 2. The per-report integrator for dispatch 2 will write the artifact + append to open-questions; dispatch 3 per-report integrator will run sequentially after dispatch 2's finalize and will see the fresh artifact. No blocking artifact dependency; the dependency is purely "want correct context state before writing the refresh."

**No escalation items.** All 7 dispatches are well-scoped, unblocked, and within the 12-dispatch cycle cap.
