# Cycle-009 integrator staging log

This file is the per-cycle staging log appended by `integrator-per-report` agents during cycle-009. Each per-report dispatch appends one section (newest LAST). `integrator-finalize` reads this log at cycle-end to run the book rebuild, repair breakage, mark consumed reports' `integrated_at`, append to cycle-record, write `log/cycle-009.md`, append to integrator-signals, and commit + push.

Append-only after a row is written. Per-report integrators MUST re-read disk before each Edit (a previous in-cycle integrator may have touched the same file).

---

## 2026-05-27T191730Z-lifter-krylov-step-body-identity-firm-promotion
applied_at: 2026-05-27T194356Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3-L2/krylov-step-body-identity.md (edit — 4 in-place edits: §Status full rewrite with inheritance-acknowledgment paragraph; Context bullet `firm-rough-in` → `firm`; §Speculative L3 operators 2-paragraph block updated for upstream firm + L4 iterate_while firm; §Verified-against L4/L3 evidence line updated for upstream firm cycle-008 with line 216 → 293 pointer + cycle-008 patch summary)
- book/src/L3-L2/index.md (edit — 1 in-place edit: dep-map row status cell `firm-rough-in (...)` → `firm (...; promoted cycle-009 via status-inheritance)`)

Gate hits:
- retroactive-budget per-slice: 0 (pure status flip; no retroactive-evidence backfill)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0 (critic pre-verified pass)
- H1 reuses page heading: 0 (no new pages)
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- SUMMARY.md auto-fix: 0 (no new pages)
- index-placeholder displacement auto-fix: 0 (existing dep-map row update, not first firm row)
- bookkeeping incomplete: 0

Open questions promoted:
- (none — report explicitly states "None" under §Open questions / caveats; the promotion is purely mechanical and asserts no new caveats)

Build-relevant: yes

Notes: First per-report integrator of cycle-009; bootstrapped this STAGING.md. Pure mechanical status-inheritance promotion (firm-rough-in → firm) — 5 edits consolidated into 4 anchor-and-insert blocks in `book/src/L3-L2/krylov-step-body-identity.md` + 1 dep-map row in `book/src/L3-L2/index.md`; no new content, no signature changes, no LHS/RHS shape changes, no applicability-condition changes. All edits applied cleanly on first attempt (anchors matched disk exactly; line numbers in CYCLE.md proposed-changes blocks matched current file state). Inheritance-acknowledgment paragraph added to §Status per role-spec for lifter status-inheritance promotions. The "first in-cycle status inheritance" pattern flagged in cycle-007 integrator-signals line 167 now has its first across-cycle precedent: cycle-008 upstream promotion satisfied plan-kind-consistency precondition, cycle-009 downstream promotion enacted mechanically. Deferred `integrated_at:` to finalize per role-spec.

---

## 2026-05-27T192051Z-layer-intro-author-L0-bootstrap-bundle-5
applied_at: 2026-05-27T194918Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L0/mpi-globalsum-and-collectives.md (create — copied from report dir, 164 lines, repaired version)
- book/src/L0/preconditioner-classes-overview.md (create — copied from report dir, 185 lines, repaired version)
- book/src/L0/index.md (edit — 2 anchor-and-insert dep-map rows: `preconditioner-classes-overview` appended after `eigensolver-wrapper` in "Overload sets and class interfaces" group; `mpi-globalsum-and-collectives` appended after `linalg-iterative-file` in "File overviews" group)
- book/src/SUMMARY.md (edit — 2 separate insertions per repairer's finding-7 split: "File — palace/utils/communication.hpp (MPI collectives)" appended after `linalg-iterative-file` in File cluster; "Class — preconditioner classes overview" appended after `eigensolver-wrapper` in Class cluster)
- scaffolding/open-questions.md (edit — 3 changes: (1) status of `l0-bundle-5-candidates` flipped `open` → `answered` with `answered_at: cycle-009` and `answered_in: reports/<id>/` + 1-paragraph closure note; (2) new OQ `tests-as-semantic-supplement-l0-vs-concepts-decision` appended; (3) new OQ `l0-bundle-6-candidates` appended for bundle-6 forward-routing)

Gate hits:
- retroactive-budget per-slice: 0 (new L0 chapter creations; no retroactive backfill)
- retroactive-budget global: 0 (this report)
- concept_writes on existing slug: 0 (both new chapters are new slugs in `book/src/L0/`; verified no pre-existing files)
- forward-edge claim without surface: 0 (chapters use `(forward-target)` annotation convention per cycle-008 bundle-4 precedent; critic confirmed pass)
- edge-label / prose mismatch: 0 (L0 reference notes are layer-internal; no edge labels)
- H1 reuses page heading: 0 (mpi chapter H1 "File — `palace/utils/communication.hpp` (`palace::Mpi` collectives and `mpi::DataType`)" differs from SUMMARY entry "File — palace/utils/communication.hpp (MPI collectives)"; preconditioner chapter H1 "Class — preconditioner-classes overview (`palace/linalg/{amg,ams,jacobi,chebyshev,distrelaxation,gmg,blockprecond}.{hpp,cpp}`)" differs from SUMMARY entry "Class — preconditioner classes overview")
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (critic verified `OperType ∈ {Operator, ComplexOperator}` axis correctly handled in preconditioner-classes-overview)
- SUMMARY.md auto-fix: 0 (report already proposed SUMMARY.md edits explicitly with finding-7 split into File-cluster + Class-cluster insertions; no auto-fix required)
- index-placeholder displacement auto-fix: 0 (book/src/L0/index.md is long-established dep-map; no placeholder)
- bookkeeping incomplete: 0

Open questions promoted:
- tests-as-semantic-supplement-l0-vs-concepts-decision (new — placement decision for the deferred third bundle-5 candidate)
- l0-bundle-6-candidates (new — bundle-6 forward-routing per source-report §Bundle 6 candidate ordering)
- l0-bundle-5-candidates (status update only — `open` → `answered` since bundle 5 dispatched and 2 of 3 candidates landed; remaining 2 candidates re-routed via the two new OQs above)

Build-relevant: yes

Notes: Second per-report integrator of cycle-009 (pass 2 of 4). All 4 proposed-changes blocks from CYCLE.md applied cleanly on first attempt — 2 file creations via `cp` from report dir (both files carry the repairer's 8 in-place fixes from META.md §Repair: 32→42 GlobalSum count propagation, 28→20 Mpi::Print count, "32-line wrapper" → "thin 12-line class definition (inside a 31-line header file)", "four"→"five" workspace vectors, `jacobi.cpp:99-104`→`100-104` off-by-one, `ksp.cpp:125-204`↔`125-240` reconciliation with annotated switch sub-range `136-204`, SUMMARY.md categorization split, `ksp.cpp:213-232` interpretive imprecision rephrasing), plus 4 anchor-and-insert edits across `book/src/L0/index.md` (2 dep-map rows) and `book/src/SUMMARY.md` (2 insertions in the correct File/Class clusters per repairer's finding-7). Verified anchors matched disk exactly (no pre-existing files at the target chapter paths; index.md and SUMMARY.md anchors at expected lines). Bundle-5 size discipline honored (2 chapters delivered as dispatched; tests-as-semantic-supplement deferred via new OQ). No conflicts with pass-1 (`book/src/L3-L2/*` files untouched here). Deferred `integrated_at:` to finalize per role-spec. L0 chapter count: 14 → 16 after this landing.

---

## 2026-05-27T191929Z-harvester-eigsolve-L1
applied_at: 2026-05-27T195530Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/eigsolve.md (create — new L1 rough-in chapter, 79 lines; content copied verbatim from CYCLE.md §"Operator content" markdown-fenced block lines 55-260, including repairer's 6 in-place fixes: ARPACK sort site relocated from wrong `drivers/eigensolver.cpp:480` to correct dual-site `arpack.cpp:374-398` + `modeeigensolver.cpp:479-492`, both ellipsis ranges concretized to `nleps.cpp:351-805` + `nleps.cpp:254-323` SetInitialGuess clarification, ARPACK 2-of-9 stub spectrum-target values documented with exact MFEM_ABORT quote + stub-policy cross-ref to `ksp.cpp:53-57` + L1>L0 obstruction note, exact print-template quote `" Found {:d} converged eigenvalue{}{}\n"` with singular-base/conditional-`s` annotation, modeeigensolver dispatch site corrected `1029-1047`→`1030-1053` with ARPACK/SLEPc sub-branch breakdown)
- book/src/L1/index.md (edit — 3 anchor-and-insert blocks: (1) new "Rough-in (test-coverage-bounded)" subsection inserted between Firm bullet list and "Rough-in (obstruction)" subsection per repairer's finding-4 restructure (cohort-purity preserving — Firm (8) header and bullets unchanged); (2) eigsolve dep-map row inserted after ksp_solve, before lanczos_step; (3) Cycle-009 working-note bullet appended after Cycle-008 bullet)
- book/src/SUMMARY.md (edit — 1 insertion: `- [eigsolve](./L1/eigsolve.md)` after `- [ksp_solve]` line under L1 Part)
- scaffolding/open-questions.md (edit — 5 changes: (1) `eigsolve-l1-operator-rough-in-candidate` status flipped `open` → `partially-answered` with `partial_answer_at: cycle-009` + `partial_answer_in: reports/<id>/` + 1-paragraph partial-closure note explaining rough-in landing + firm-promotion gating + cross-reference to 4 new follow-up OQs; (2-5) 4 new OQs appended before `## Dropped`: `eigsolve-linear-solve-failed-status-anchor`, `eigsolve-scaling-coordinate-convention`, `eigsolve-initial-space-axis-placement`, `eigsolve-iteration-count-result-field` — all `opened_at: cycle-009`, `opened_by: harvester`, `status: open`, sourced from CYCLE.md §Open questions / caveats items 1-4)

Gate hits:
- retroactive-budget per-slice: 0 (new L1 chapter creation; no retroactive backfill — `eigsolve` slug did not exist pre-cycle-009)
- retroactive-budget global: 0 (this report)
- concept_writes on existing slug: 0 (new file at `book/src/L1/eigsolve.md`; verified no pre-existing file via `ls`)
- forward-edge claim without surface: 0 (`L1>L0` references point to forward-targets and use `eigsolve-mutation-rotation` as a forward-target slug, with explicit "future cycle" framing — not a forward-edge claim requiring immediate surface)
- edge-label / prose mismatch: 0 (L1 operator entry; no L_{n+1}→L_n lowering-edge labels to verify per critic edge-label-fidelity pass)
- H1 reuses page heading: 0 (chapter H1 `# eigsolve` differs from SUMMARY entry `eigsolve` — chapter H1 is the canonical operator name, no page-heading reuse violation)
- append on missing slug: 0 (all referenced slugs verified to exist: `L0/eigensolver-wrapper`, `L1/ksp_solve`, `L1/apply_linop`, `L1/dot`, `L1/nrm2`, `L1/axpy`, `L1/axpby`, `L1-L0/ksp-solve-mutation-rotation`, `L1-L0/minres-iteration`, all `concepts/*`, `design/l4_calculus`)
- variant-axis missing on multi-variant operator: 0 (critic verified — 4 preserved axes (problem-type / spectrum-target / spectral-transformation / scaling) + 3 collapsed axes (orchestration-pattern / slepc-internal-method / slepc-problem-type) + 3 explicit out-of-scope items all enumerated with rationale; the 2 ARPACK-unsupported spectrum-target values flagged as unimplemented stubs per repairer's finding-3 alignment with CLAUDE.md stub policy)
- SUMMARY.md auto-fix: 0 (report explicitly proposed SUMMARY.md edit; no auto-fix needed)
- index-placeholder displacement auto-fix: 0 (L1/index.md long-established; no placeholder text)
- bookkeeping incomplete: 0
- LinearSolveFailed constructive introduction without L0 anchor: NOT a safety-net violation — the rough-in chapter explicitly flags this in Algebraic-laws §3, marks it in "Laws that explicitly do not hold" §"Sum-type completeness of `EigStatus`", and routes it to new OQ `eigsolve-linear-solve-failed-status-anchor`. The constructive introduction is well-handled (not silently asserted) and the rough-in status is the appropriate epistemic disclaimer.

Open questions promoted:
- eigsolve-linear-solve-failed-status-anchor (new — rough-in's constructive `EigStatus::LinearSolveFailed` case has no direct L0 anchor; routes to critic/lifter review or future L1>L0 lowering)
- eigsolve-scaling-coordinate-convention (new — `EigResult.eigenvalues` coordinate-system convention under `ScaleType::NORM_2`; two coherent options flagged)
- eigsolve-initial-space-axis-placement (new — `initial_space` placement decision: per-call EigControl field vs construction-bound EigSolver field)
- eigsolve-iteration-count-result-field (new — whether `EigResult` should carry `iterations` field analogous to `SolveResult.iterations`)
- eigsolve-l1-operator-rough-in-candidate (status update only — `open` → `partially-answered`; the cycle-008 OQ from layer-intro-author bundle-4 is partially closed by this rough-in landing, with firm-promotion follow-up tracked via remaining status)

Build-relevant: yes

Notes: Third per-report integrator of cycle-009 (pass 3 of 4). All 4 proposed-changes blocks from CYCLE.md applied cleanly on first attempt — chapter content sourced verbatim from CYCLE.md's markdown-fenced block (lines 55-260; repairer's META.md confirms all 6 META findings repaired in-place with `overall_status: ready`). Verified anchors matched disk exactly: `book/src/L1/eigsolve.md` did not pre-exist (new file); `book/src/L1/index.md` Firm bullet list ended at line 38 with `ksp_solve` (firmly the last firm bullet) followed by existing "Rough-in (obstruction)" heading at line 40, so new "Rough-in (test-coverage-bounded)" subsection slots cleanly between (cohort purity preserved per repairer's finding-4); `book/src/SUMMARY.md` `ksp_solve` line at 40 with `# L1 > L0 — Lowering` header at line 42 unchanged from pass 2 (pass 2 touched L0 section only, lines ~52-94 region). The four newly-introduced rough-in caveats (LinearSolveFailed without L0 anchor; scaling coordinate convention; initial_space placement; iterations field) all explicitly captured in the chapter prose and individually OQ-tracked — no silent assumption surfaces in the artifact. The `partially-answered` status on `eigsolve-l1-operator-rough-in-candidate` is a deliberate departure from binary `open|answered` to preserve firm-promotion tracking; precedent for fine-grained closure states is `iterate-while-l3-rendering-trajectory-accumulation-gap` (multiple verdict statuses) and parallels the cycle-008 pattern of cycle-005's `l0-bootstrap-bundle-1` series being incrementally closed across bundles. L1 firm count unchanged (8); L1 rough-in (test-coverage-bounded) count: 0 → 1; L1 rough-in (obstruction) count unchanged (6). No conflicts with pass-1 (`book/src/L3-L2/*`) or pass-2 (`book/src/L0/*` + L0 sections of SUMMARY.md + open-questions L0-bundle-5/6 entries). The "second constructed-operator gate at L1" composition pattern (`eigsolve` over `ksp_solve` over `apply_linop`) is the first multi-level constructed-operator composition in the firm+rough-in L1 vocabulary; integrator-finalize may want to flag this as a methodology-signal milestone in `scaffolding/integrator-signals.md` (per cycle-007's "Constructed-operator absorption" precedent). Deferred `integrated_at:` to finalize per role-spec.

---

## 2026-05-27T192047Z-combinator-miner-check-stop-into-carry-reuse
applied_at: 2026-05-27T195851Z
applied_by: integrator-per-report
status: applied

Files touched:
- scaffolding/open-questions.md (edit — 1 anchor-and-insert: 6 new OQ entries appended before the `## Dropped` heading, all with `opened_at: cycle-009`, `opened_by: combinator-miner`, `status: open`)

Gate hits:
- retroactive-budget per-slice: 0 (inspection-only dispatch; no book/ artefact creation, no surface mutation, no retroactive backfill)
- retroactive-budget global: 0 (this report)
- concept_writes on existing slug: 0 (no concept page touched)
- forward-edge claim without surface: 0 (no claims authored — verdict is defer)
- edge-label / prose mismatch: 0 (no edges authored — no new L4>L3 row, no dep-map change)
- H1 reuses page heading: 0 (no new pages)
- append on missing slug: 0 (all OQ source references resolve: `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md`, the cycle-008 abstractor report path, the Palace source ranges, and the cited L1-L0 spec slices all verified by upstream critic citation-validity pass)
- variant-axis missing on multi-variant operator: 0 (no new operator authored; the OQ on `variant-absorption-vs-instance-counting-policy` is a meta-question about the corpus's variant-absorption convention, correctly routed to meta-phase rather than enforced as an axis-coverage gate at the integrator level)
- SUMMARY.md auto-fix: 0 (no new pages)
- index-placeholder displacement auto-fix: 0 (no index.md touched)
- bookkeeping incomplete: 0
- combinator-miner-authority §Status-edit-on-defer scope question: NOT a safety-net violation — the combinator-miner already self-flagged this at CYCLE.md §Open questions / caveats item 6 and the repairer dropped the non-standard §Status-edit block per Finding 4 (Decision: repaired). The authority-scope question is captured in OQ `combinator-miner-authority-defer-verdict-status-edit-scope` and routed to meta-phase per the strict-vs-relaxed-reading framing in that OQ. No integrator action needed beyond OQ promotion.

Open questions promoted:
- nleps-spec-gap-as-check-stop-into-carry-reuse-blocker (new — NLEPS slice-spec gap as the actual reuse-blocker; routes to harvester on NLEPS at cycle-010+)
- check-stop-into-carry-parameterization-over-stop-condition (new — monomorphic-vs-parameterized helper-signature design choice; routes to combinator-miner / lifter at helper-promotion time)
- variant-absorption-vs-instance-counting-policy (new — cross-cutter policy question about "second slice" promotion-criterion language under variant-absorbed slices; routes to meta-phase)
- iterate-while-witness-alternative-combinator-design (new — alternative L4 combinator that would dissolve the helper entirely; routes to lifter / combinator-miner concurrent with NLEPS promotion)
- standalone-iterate-while-l4-l3-theme-pending (new — standalone L4>L3 dissolution theme for iterate-while not yet authored; not blocking but flagged; routes to abstractor / lifter when second iterate-while-using theme lands; cross-referenced via `relates_to:` to the cycle-006 OQ closed in cycle-008)
- combinator-miner-authority-defer-verdict-status-edit-scope (new — role-spec scope question for combinator-miner: should `defer` verdicts permit upstream §Status-block updates? routes to meta-phase for codification)

Build-relevant: no

Notes: Fourth and final per-report integrator of cycle-009 (pass 4 of 4). This is an audit / inspection dispatch — CYCLE.md verdict is `defer`, §Proposed changes section contains **zero** proposed-changes blocks against `book/` (repairer dropped the only candidate block per Finding 4, replacing it with a prose paragraph naming the two natural future-incorporation channels). Verified via `grep -nE "^\`\`\`(edit|create):" CYCLE.md` returning no matches. The entire integration consists of promoting the 6 §Open questions / caveats items to the open-questions ledger as canonical YAML+paragraph entries. Each OQ has a unique slug (verified no collision against existing slugs in the ledger), `opened_by: combinator-miner`, `opened_at: cycle-009`, and a paragraph body preserving the source-report substance plus routing destination. One OQ (`standalone-iterate-while-l4-l3-theme-pending`) carries a `relates_to:` cross-reference to the cycle-006 closed OQ per the existing precedent at `iterate-while-log-effect-vs-trajectory-channel`. No conflicts with pass-1 (`book/src/L3-L2/*`), pass-2 (`book/src/L0/*` + SUMMARY.md L0 region + open-questions L0-bundle-5/6 entries), or pass-3 (`book/src/L1/*` + SUMMARY.md L1 region + open-questions eigsolve entries) — pass-4 only touches `scaffolding/open-questions.md` (append-only insertion before `## Dropped`), and the 4 new eigsolve OQs from pass-3 plus the 2 new L0-bundle OQs from pass-2 are upstream of pass-4's insertion point. Two methodology-signal items for integrator-finalize: (1) cycle-008's "defer until a second slice needs it" promotion criterion received its first programmatic survey in cycle-009 — the cross-cycle round-trip from abstractor-criterion → combinator-miner-verdict is a methodology pattern worth flagging in integrator-signals; (2) the combinator-miner-authority OQ surfaces a recurring role-scope question (when can a `defer` agent edit upstream content?) that meta-phase batch-1 aggregation should examine alongside the cycle-008 abstractor-write-authority-violation pattern. Deferred `integrated_at:` to finalize per role-spec. All four cycle-009 per-report integrations now complete; pass 5 (integrator-finalize) is unblocked.

---
