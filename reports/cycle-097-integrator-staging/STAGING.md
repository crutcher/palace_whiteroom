# cycle-097 integrator staging log

Per-report integration landings for cycle-097, appended serially (newest LAST, append-only).
Authoritative apply-order = row ORDER (NOT `applied_at` timestamps, which are advisory).
`integrator-finalize` reads this log to rebuild, reconcile, and emit the batch CYCLE.md.

---

## 2026-06-04T232852Z-same-layer-cross-cutter-cg-precond-slice-delete (D1)
applied_at: 2026-06-04T235200Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/constructed-operator-factory.md (Edit — repoint A: slice link → ../L4/preconditioning-framework.md)
- book/src/concepts/solver-as-operator.md (Edit — repoint B)
- book/src/concepts/finest-level-unwrap.md (Edit — repoint C)
- book/src/concepts/complex-from-real-lift.md (Edit ×2 — repoint D, lines 25 + 31)
- book/src/concepts/counter-update.md (Edit — repoint E)
- book/src/concepts/two_operator_split.md (Edit — repoint F)
- book/src/concepts/build-time-vs-run-time-stratification.md (Edit — repoint G)
- book/src/spec/slices/cg_preconditioning_framework.md (DELETE-FILE via `git rm` — absorbed into firm L4 chapter)
- scaffolding/open-questions.md (append-only — 2 OQ sections: l4-preconditioning-framework-promotion close-note + dependency-map-cg-precond-stale-mermaid-edges)

Gate hits:
- repoint-anchor-verify: 8/8 OLD anchors matched on-disk byte-for-byte BEFORE editing (verified via Read of each target line). All repoint targets resolve to existing book/src/L4/preconditioning-framework.md (337-line firm chapter).
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- graded-stack rank-gate (step-5b): 0 NEW violations. No new firm node created; deleted a reference-only reachability-GC leaf. Verified no inbound `depends-on` (blocking) edge targets the slice (report §3 + critic independently confirmed; the firm chapter's own depends-on targets are L4/ksp_solve + the ksp.cpp L0 range, NOT the slice). All 7 inbound concept-page links were navigational (`reference`-class "Used by"/"Worked example"). Deletion reachability-safe.
- SUMMARY.md / spec/index.md auto-fix: NOT triggered — those rows are D5's single-owner removal per the cycle-097 hard constraint; correctly left untouched here.
- citecheck (--scan, bounds + path-hygiene): 25 ok, 0 failing. No MISS/AMBIG/OOB. Non-blocking.

Residual slice string-refs after deletion (verified, all correctly out-of-D1-scope):
- book/src/SUMMARY.md, book/src/spec/index.md — D5 single-owner rows (untouched).
- book/src/concepts/dependency-map.md — aggregate Mermaid node edges (~22), OQ-logged; D5 handles dependency-map cleanup this cycle (cross-ref OQ dependency-map-cg-precond-stale-mermaid-edges). Mermaid node label, NOT a markdown link → not a linkcheck2 hard error.
- book/src/meta-reviews/2026-05-26-cycles-*.md, book/src/concepts/rotation.md:136 — historical narrative, left as-is by design (rewriting would falsify the cycle-history record).
- book/src/L4/preconditioning-framework.md, book/src/L4/index.md — the firm chapter's OWN §Status absorption-provenance mention + index row referencing the slice as the absorbed precursor (correct, expected).

Open questions promoted:
- l4-preconditioning-framework-promotion (CLOSE-NOTE — RESOLVED-by-c096-D1; recommend meta-phase CLOSE at batch-31 unify; per-report integrator has no OQ-close authority)
- dependency-map-cg-precond-stale-mermaid-edges (new — cross-references cycle-097 D5's dependency-map cleanup ownership; verify-after-D5 trigger)

Build-relevant: yes (edits touch book/src/concepts/*.md and delete book/src/spec/slices/*.md — finalize must rebuild; the slice deletion + 7 repoints must pass linkcheck2 with the firm L4 chapter as the live target).

Notes: First per-report integration of cycle-097 — created this STAGING.md (header + first row). Clean all-pass report (overall_status: ready set by critic directly; no repairer ran). Did NOT run `cargo make book` (finalize's job). Deferred `integrated_at:` to finalize per role-spec (per-report integrator must not touch consumed-report frontmatter). All file-state claims above are from disk I read/edited THIS invocation, not from any assumed sibling landing — D5 had NOT yet run at this point (staging log had no prior rows; I am position 1). The SUMMARY.md / spec/index.md / dependency-map rows are LEFT for D5; finalize/D5 should confirm the dependency-map regeneration after D5 lands.

---

## 2026-06-04T232852Z-same-layer-cross-cutter-divfree-slice-delete (D2)
applied_at: 2026-06-04T235900Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/ksp_solve.md (Edit — proposed-change 1: repoint :131 parenthetical slice link → ./divfree-projector.md, positive L0 `divfree.cpp:175` kept inline)
- book/src/L1/ksp_solve.md (Edit — proposed-change 2: Evidence bullet `spec/slices/divfree.md` slice-precedent → firm home `book/src/L1/divfree-projector.md`)
- book/src/L1/divfree-projector.md (Edit — proposed-change 3: footer slice-corpus-precedent link → claim-free Provenance prose, no slice link)
- book/src/spec/slices/divfree.md (DELETE-FILE via `git rm` — proposed-change 4; absorb was a no-op, firm homes already carry positive L0)

Gate hits:
- repoint-anchor-verify: 3/3 OLD `Replace:` anchors matched on-disk byte-for-byte BEFORE editing (Read of ksp_solve.md:131/:143 + divfree-projector.md:325-327). Repaired CYCLE.md applied as written (proposed-change blocks untouched by repairer per META; analysis-section basenames disambiguated but not load-bearing for apply).
- surviving-md-link-to-slice: 0 (post-edit grep over book/src/ for `]( ... spec/slices/divfree` → empty; the two repointed L1 files carry zero slice refs).
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- graded-stack rank-gate (step-5): 0 NEW violations. Deleted a reachability-GC-detritus slice (no frontmatter, bare `# Slice:` heading, no inbound `depends-on` blocking edge — report §5 + critic independently grep-confirmed). All inbound refs were `reference`-class navigational. No new firm node created. Reachability-safe.
- SUMMARY.md / spec/index.md auto-fix: NOT triggered — `SUMMARY.md:295` + `spec/index.md:18` are D5's single-owner rows per the cycle-097 hard constraint; correctly left untouched.
- citecheck (--scan, bounds + path-hygiene): 37 ok, 4 failing. The 4 are all benign/expected: 3 `[MISS]` on `slices/divfree.md` (the deletion target's OWN path — the report's refs to the file it deletes + self-cite; self-resolving) + 1 `[AMBIG] ksp_solve.md:131` (the repairer-intentionally-left verbatim grep-transcript residual, a recorded shell output not a cross-ref). No `OOB`. None unrepairable; non-blocking.

Open questions promoted:
- (none) — the report's §Open-questions are integrator-sequencing caveats (D5 co-landing boundary, krylov-trio-constraint compliance confirmation, the drive-by stale-slice-header note resolved BY the deletion), not net-new cross-cycle questions. No divfree-specific dependency-map/concept-page residue to log (report §3/§4 grep-verified ZERO concept-page and eigsolve/eigensolver-wrapper slice links).

Build-relevant: yes (edits touch book/src/L1/*.md and delete book/src/spec/slices/divfree.md — finalize must rebuild; the slice deletion + 3 repoints must pass linkcheck2).

Notes: Second per-report integration of cycle-097 (appended after D1's cg-precond slice-delete row). HARD CO-LANDING CONSTRAINT for finalize: the divfree slice deletion (change 4) leaves `book/src/SUMMARY.md:295` + `book/src/spec/index.md:18` as dangling linkcheck2 errors UNLESS D5 removes those two rows in the same cycle — D5 is dispatched this cycle and owns them; the report + critic + this row all flag it for the finalize `cargo make book` build gate. All file-state claims here are from disk I read/edited THIS invocation. I did NOT verify D5 had landed (I see only this report + the staging log; D5 has no staging row as of this append — the SUMMARY/index rows remain present, correctly out of my scope). Did NOT run `cargo make book` (finalize's job). Deferred `integrated_at:` to finalize per role-spec.

---
## 2026-06-04T232852Z-same-layer-cross-cutter-sparse-trisolve-slice-delete (D3)
applied_at: 2026-06-05T001200Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/triangular-solve-obstruction.md (Edit — Change 1a: new §(d) absorbed subsection (d1/d2/d3) inserted before `## Applicability conditions`)
- book/src/L1-L0/triangular-solve-obstruction.md (Edit — Change 1b: 7 absorbed L0 anchors appended to Verified-against prose list after the blockprecond red-herring bullet)
- book/src/L1-L0/triangular-solve-obstruction.md (Edit — Change 2a: §Related slice cross-link block replaced; `annotated-and-retained` framing retired, theme declared sole home; self-link to slice collapsed)
- book/src/L1-L0/triangular-solve-obstruction.md (Edit — Change 2b: verified_against YAML slice entry → `verdict: absorbed-and-deleted` deletion-record, no dangling slice path)
- book/src/concepts/scope-out-obstruction.md (Edit — Change 3a: §Canonical-instance opening link repointed slice → ../L1-L0/triangular-solve-obstruction.md)
- book/src/concepts/sequential-obstruction.md (Edit — Change 3b: §Sub-kind out-of-scope link repointed, CONTEXT-ANCHORED via line-52 sentence opener; confined to :53 region, did NOT touch D4's :83-85)
- book/src/concepts/negative-result-slice.md (Edit — Change 3c: §Examples bullet repointed slice → firm theme)
- book/src/spec/slices/sparse_triangular_solve.md (DELETE-FILE via `git rm` — Change 4; absorbed into firm theme §(d))
- scaffolding/open-questions.md (append-only — 2 OQ close-note sections: sparse-trisolve-rename-to-sparse-direct-solver-wrapper + sparse-trisolve-mfem-superlu-factor-allgatherv-family, both RECOMMEND CLOSE)

Gate hits:
- repoint-anchor-verify: all OLD anchors matched on-disk byte-for-byte BEFORE editing (Read of triangular-solve-obstruction.md :199/:273-308/:355-359/:464-467; scope-out-obstruction.md :68; sequential-obstruction.md :52-53; negative-result-slice.md :47). The repaired D3 Change-3b context-anchored block matched lines 52-53 exactly. All absorbed L0 cites applied as written (critic-verified against reference/palace via codemap).
- surviving-md-link-to-slice: 0 from THIS dispatch's files (post-edit `grep -nE '\]\([^)]*sparse_triangular_solve[^)]*\)' book/src/` → only SUMMARY.md:300 + spec/index.md:21 remain, BOTH D5-owned per hard constraint; the two triangular-solve-obstruction.md hits at :339/:533 are backtick code-span tokens inside prose/YAML-note, NOT markdown links — do not break linkcheck2). The firm-theme self-link at :277 was collapsed by Change 2a.
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- graded-stack rank-gate (step-5): 0 NEW violations. The absorption ADDS firm L0 negative-anchor content to an existing firm `obstruction` theme (no rank change — obstruction is a separate kind). The deletion removes reachability-GC detritus: the slice carried no typed frontmatter and every inbound referrer was a `reference`-kind navigational link (now repointed); NO inbound `depends-on` blocking edge targeted it (report §4 + critic grep-confirmed). Reachability-safe.
- SUMMARY.md / spec/index.md auto-fix: NOT triggered — SUMMARY.md:300 + spec/index.md:21 are D5's single-owner rows per the cycle-097 hard constraint; correctly left untouched.
- post-apply YAML re-anchor (suggested-resolution #3): checked. The repointed concept links landed at scope-out-obstruction.md:68 and sequential-obstruction.md:53 — SAME line numbers as before (section-header positions absorbed the +1 inserts), so the firm theme's verified_against YAML referent line-ints :68/:53 (now at theme lines :534/:538) stay VALID. No re-anchor needed. (The two YAML note: prose strings still say "cites the slice as canonical instance" — mildly stale in phrasing but backtick prose tokens, not links, and still meaningfully accurate; left per proposed-change scope.)
- citecheck (--scan, bounds + path-hygiene): 39 ok, 0 failing. No MISS/AMBIG/OOB. Non-blocking.

Open questions promoted:
- sparse-trisolve-rename-to-sparse-direct-solver-wrapper (RECOMMEND CLOSE — resolved-by-obstruction; meta-phase batch-31 unify)
- sparse-trisolve-mfem-superlu-factor-allgatherv-family (RECOMMEND CLOSE — out-of-scope upstream-library-internal; meta-phase batch-31 unify)

Build-relevant: yes (edits touch book/src/L1-L0/*.md + book/src/concepts/*.md and delete book/src/spec/slices/sparse_triangular_solve.md — finalize must rebuild; the slice deletion + 3 concept repoints + theme self-link collapse must pass linkcheck2).

Notes: Third per-report integration of cycle-097 (appended after D1 cg-precond + D2 divfree rows). HARD CO-LANDING CONSTRAINT for finalize (mirrors D1/D2): the sparse-trisolve slice deletion (Change 4) leaves `book/src/SUMMARY.md:300` + `book/src/spec/index.md:21` as dangling linkcheck2 markdown-links UNLESS D5 removes those two rows this cycle — D5 owns them per the cycle-097 plan; this row + report + critic all flag it for the finalize `cargo make book` build gate. If D5 does NOT land this cycle, finalize should defer Change 4's deletion (absorption Changes 1-3 are independently link-safe). D3↔D4 same-file coupling on sequential-obstruction.md is dissolved on D3's side: Change 3b is context-anchored (line-52 opener) and edits only the :53 region; D4's :83-85 Givens-stream edit is 30 lines away and untouched by me. I did NOT verify D4 or D5 had landed — I see only this report + the staging log (D4/D5 have no staging rows as of this append; SUMMARY.md:300 + spec/index.md:21 remain present on disk, correctly out of my scope). ONE discretionary smoothing: Change 3a's `with:` block ended mid-phrase ("— sparse triangular solves with") which, against the preserved line-69 continuation ("the scope question targeted sparse triangular solves with"), produced a doubled "...with / the scope question targeted sparse triangular solves with..." garble; I closed the new clause with "the absorbed §(d) holds the wrapper-surface L0 evidence):" so it flows cleanly into the preserved continuation prose. Link target + meaning are exactly as proposed; only the trailing connective phrasing differs (applied-discretionarily, rationale: avoid-landing-garbled-sentence). All file-state claims above are from disk I read/edited THIS invocation. Did NOT run `cargo make book` (finalize's job). Deferred `integrated_at:` + `integration_commit:` to finalize per role-spec.

---
## 2026-06-04T232852Z-same-layer-cross-cutter-plane-rotation-slice-delete (D4)
applied_at: 2026-06-05T002400Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/sequential-obstruction.md (Edit — Change 1: §"Worked example: Givens-stream replay-prefix" body replaced; retitled to (GMRES least-squares update), re-anchored DIRECTLY to L0 `iterative.cpp:634-640`, +3 absorbed sub-analyses [local-triviality-at-extend, cross-target-no-batch-dim, Householder-WY sibling boundary]. Confined to the Givens region :84-113; did NOT touch D3's sparse-trisolve :53 edit 30 lines above)
- book/src/concepts/givens.md (Edit — Change 2: :40 repoint slice → ../L2/incremental-least-squares.md)
- book/src/concepts/givens_apply.md (Edit — Change 3: :27 repoint slice → ../L1/ls-update-column.md)
- book/src/concepts/givens_generate.md (Edit — Change 4: :27 repoint slice → ../L1/ls-update-column.md)
- book/src/concepts/plane-rotation-stream.md (Edit — Change 5: :37 repoint slice → ../L2/incremental-least-squares.md)
- book/src/spec/slices/plane_rotation_stream.md (DELETE-FILE via `git rm` — Change 6; absorbed §L3 + 5 inbound repointed)
- scaffolding/open-questions.md (append-only — 1 OQ section: plane-rotation-givens-l0-citation-range-reconcile RECOMMEND CLOSE [resolved-by-deletion] + an appended end-bound-divergence note from the D4 critic's Issue 3)

Gate hits:
- repoint-anchor-verify: 6/6 OLD anchors matched on-disk byte-for-byte BEFORE editing (Read of sequential-obstruction.md:84-113 full worked-example body; givens.md:38-41; givens_apply.md:27; givens_generate.md:27; plane-rotation-stream.md:37). D3 had already landed its sequential-obstruction.md:53 edit; I verified the Givens region :84+ was intact (D3's row + the on-disk Read both confirm D3 confined itself to :53). Both repoint targets resolve on disk (book/src/L1/ls-update-column.md, book/src/L2/incremental-least-squares.md).
- repaired-CYCLE.md-applied: Change 1 NEW body applied with the resolved `../L1/ls-update-column.md` path inline (the repairer's fix; no `(ls-update-column-firm-home-placeholder)` token shipped). The OQ-reconcile paste-inline correction was a CYCLE.md presentation fix, not a proposed-change — no apply impact.
- surviving-md-link-to-slice (from D4's 6 files): 0 (post-edit `grep -l plane_rotation_stream` over all 5 touched concept files → empty; slice file deleted).
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- L0-absorption-verify: the absorbed direct-L0 ranges were re-verified against source THIS invocation — `iterative.cpp:70-73` (:72 template, :73 GeneratePlaneRotation signature) and `:634-640` (replay-prefix loop :634-637, extend triple :638-640) read off disk at `reference/palace/palace/linalg/iterative.cpp`; match the report + critic. The OQ's `:73-108` canonical range is the start-bound resolution; the deletion excises the divergent in-slice `:72-108`.
- graded-stack rank-gate (step-5): 0 NEW violations. Change 1 ADDS firm L0 content to an existing firm worked-example inside `sequential-obstruction.md` (no rank change — re-anchoring a concept worked-example to L0). The deletion removes reachability-GC detritus: the slice lives in Phase-1 `spec/slices/` (raw material, NOT the typed L-graph); every inbound referrer was `reference`-kind navigational (the 5 repointed concept links + SUMMARY/index nav rows + dependency-map Mermaid nodes); NO inbound `depends-on` blocking edge targeted it (report §4 + critic grep-confirmed). Reachability-safe.
- SUMMARY.md / spec/index.md auto-fix: NOT triggered — `SUMMARY.md:298` + `spec/index.md:19` are D5's single-owner rows per the cycle-097 hard constraint; correctly left untouched (verified present on disk).
- citecheck (--scan, bounds + path-hygiene): 38 ok, 3 failing. The 3 `[MISS]` are all on `reference/palace/linalg/iterative.cpp` (:70-73, :72, :634-637) — a PATH-RESOLUTION artifact, NOT a real citation defect: the actual clone layout is `reference/palace/palace/linalg/iterative.cpp` (the report's `--scan` text used the `reference/palace/linalg/...` full-path form; the canonical book citations use `palace/linalg/...` relative to `reference/`). I confirmed the file IS present and the cited ranges resolve byte-for-byte via `sed` on the true path THIS invocation (and the critic verified independently via codemap). No MISS on a book-internal path; no AMBIG/OOB. Non-blocking.

Residual slice string-refs after deletion (verified, all correctly out-of-D4-scope):
- book/src/SUMMARY.md:298, book/src/spec/index.md:19 — D5 single-owner nav rows (untouched; hard co-landing constraint mirrors D1/D2/D3 — see Notes).
- book/src/concepts/dependency-map.md:165/:247/:314-317 — 4-6 Mermaid graph-node edges (`plane_rotation_stream --> givens/sequential-obstruction/tensor-field-lift/trsv`). Mermaid node labels, NOT markdown links → NOT linkcheck2 hard errors. Report-flagged as layer-intro-author OQ (out of D4 named scope).
- book/src/spec/slices/orthog.md:225/:227/:230/:234 — the sibling-slice "Plane-rotation stream (reduced)" stub-pointer (separate slice file). Report-flagged as a future same-layer-cross-cutter/layer-intro-author OQ (out of D4 named scope). The `:230` markdown bullet `book/src/spec/slices/plane_rotation_stream.md` is a bare path-as-text (no `]( )` link wrapper), so not a linkcheck2 anchor; the `:234` ref is inside the stub prose. Neither breaks the build, but a downstream pass should repoint/drop the stub.
- book/src/meta-reviews/2026-05-26-cycles-*.md — frozen historical narrative, left as-is by convention.

Open questions promoted:
- plane-rotation-givens-l0-citation-range-reconcile (RECOMMEND CLOSE — resolved-by-deletion; meta-phase batch-31 unify. Appended an end-bound-divergence sub-note from the D4 critic Issue 3 — :73-109/:73-120/:73-118 in arnoldi_step/polynomial_recurrence_step/composition-lowering — a DISTINCT still-open end-bound inconsistency, logged for a downstream verify-citation-range pass, NOT closed here.)

Build-relevant: yes (edits touch book/src/concepts/*.md + delete book/src/spec/slices/plane_rotation_stream.md — finalize must rebuild; the slice deletion + 5 repoints + 1 worked-example re-anchor must pass linkcheck2 with the firm homes as live targets).

Notes: Fourth per-report integration of cycle-097 (appended after D1 cg-precond + D2 divfree + D3 sparse-trisolve rows). overall_status: ready set by the REPAIRER after fixing a citation-validity warning (the OQ-reconcile paste-inline line-numbers were corrected to :72=template/:73=signature, and Change 1's NEW body had its `(ls-update-column-firm-home-placeholder)` token inlined to `../L1/ls-update-column.md`); I applied the repaired CYCLE.md — Change 1 shipped with the resolved path, no placeholder. HARD CO-LANDING CONSTRAINT for finalize (mirrors D1/D2/D3): the plane_rotation_stream slice deletion (Change 6) leaves `book/src/SUMMARY.md:298` + `book/src/spec/index.md:19` as dangling linkcheck2 markdown-links UNLESS D5 removes those two rows this cycle — D5 owns them per the cycle-097 plan; this row + report + critic all flag it for the finalize `cargo make book` build gate. If D5 does NOT land this cycle, finalize should defer Change 6's deletion (absorption Change 1 + repoints Changes 2-5 are independently link-safe). D3↔D4 same-file coupling on sequential-obstruction.md is fully dissolved: D3's :53 edit and D4's :84-113 worked-example edit are ~30 lines apart and non-overlapping — I verified the Givens region was intact on disk (D3's staging row + my own Read both confirm it), NOT assumed from D3's stated landing. All file-state claims above are from disk I read/edited THIS invocation. I did NOT verify D5 had landed — D5 has no staging row as of this append, and the SUMMARY.md:298 + spec/index.md:19 rows remain present on disk, correctly out of my scope. Did NOT run `cargo make book` (finalize's job). Deferred `integrated_at:` + `integration_commit:` to finalize per role-spec (per-report integrator must not touch consumed-report frontmatter).

---
## 2026-06-04T232852Z-lifter-domain-energy-reduce-377-landclean (D6)
applied_at: 2026-06-05T003600Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/domain_energy_reduce.md (Edit — Site 1: Evidence §"Folded L1 primitives" :377 `matrix-weighted-norm (rough-in (test-coverage-bounded))` → `(firm c091 ... firm-on-positive-structure escape)`)
- book/src/L4/domain_energy_reduce.md (Edit — Site 2: `## Lowers to` :268 `(firm / rough-in) L1 folded primitives` → `(both firm) L1 folded primitives`)
- book/src/L4/domain_energy_reduce.md (Edit — Site 3: Evidence §"Supporting test" :374 `(the rough-in test-gate, §Status point 2)` → per-domain test-gate held REDUNDANT under the firm-on-positive-structure escape)
- scaffolding/open-questions.md (append-only — 2 OQ sections: domain_energy_reduce-377-mwn-stale-rough-in-residue [RECOMMEND CLOSE — resolved-by-re-anchor] + domain_energy_reduce-313-gram_reduce-bilinear-form-c095-stale-rough-in-narration [new follow-up])

Gate hits:
- anchor-verify: 3/3 OLD anchors matched on-disk byte-for-byte BEFORE editing (Read of domain_energy_reduce.md :264-275 covering the :268 `(firm / rough-in)` site, and :370-381 covering the :374 `rough-in test-gate` + :375-378 `(rough-in (test-coverage-bounded))` sites). This file was NOT touched by D1–D5 (D1=concepts/cg-precond, D2=L1/ksp_solve+divfree, D3=L1-L0/triangular-solve-obstruction+concepts, D4=concepts/sequential-obstruction+givens, D5=SUMMARY/spec-index/dependency-map per cycle-097 plan); on-disk anchors confirm no prior in-cycle landing disturbed them.
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- graded-stack rank-gate (step-5): 0 NEW violations. NO node status flip — this is a within-file maturity-NARRATION re-anchor only; frontmatter `rank: firm` already on disk and unchanged. The rank invariant `rank(domain_energy_reduce)=firm ≤ min(participation_ratio firm c077, matrix-weighted-norm firm c091)` already held (both depends-on deps firm on disk; matrix-weighted-norm.md:4 `rank: firm` verified by the critic). No frontmatter `rank:`/`edges:` flip needed or made. No new firm node, no new edge.
- SUMMARY.md / concepts auto-fix: NOT triggered — no new file created, no chapter/index registration involved (pure in-file prose re-anchor of an already-registered chapter).
- citecheck (--scan, bounds + path-hygiene): 6 ok, 0 failing (ran `python3 tools/citecheck/citecheck.py --scan <this CYCLE.md> --quiet` THIS invocation). No MISS/AMBIG/OOB. Non-blocking.

Open questions promoted:
- domain_energy_reduce-377-mwn-stale-rough-in-residue (RECOMMEND CLOSE — resolved-by-re-anchor; the three D6 edits discharge it; meta-phase batch-31 unify)
- domain_energy_reduce-313-gram_reduce-bilinear-form-c095-stale-rough-in-narration (new — gram_reduce-cohort follow-up: `:313-316` gram_reduce "STAYS rough-in" may itself be stale since `bilinear-form` flipped firm c095; deliberately out of D6's one-residue-cohort scope; surfaced for a future land-clean)

Build-relevant: yes (edits touch book/src/L4/domain_energy_reduce.md — finalize must rebuild; all three are single-sentence prose-token swaps with no new/changed markdown links, so no new linkcheck2 surface, but the rebuild should confirm the file still parses).

Notes: Sixth per-report integration of cycle-097 (appended after D1 cg-precond + D2 divfree + D3 sparse-trisolve + D4 plane-rotation rows; D5 has NO staging row as of this append — I see only this report + the staging log, and I do not claim D5 landed). overall_status: ready set by the CRITIC directly (all 8 checks pass, no repairer ran). The deliberate scoping-OUT of the `:313-316` gram_reduce "STAYS rough-in" narration was PRESERVED as instructed — I did NOT touch :313-316 (a different verb's residue, logged as the new follow-up OQ above). All file-state claims here are from disk I read/edited THIS invocation, not from any assumed sibling landing: I verified the 3 anchors directly via Read before each Edit. Did NOT run `cargo make book` (finalize's job). Deferred `integrated_at:` + `integration_commit:` to finalize per role-spec (per-report integrator must not touch consumed-report frontmatter).

---
## 2026-06-04T232852Z-layer-intro-author-summary-spec-index-row-removal (D5)
applied_at: 2026-06-05T000723Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/SUMMARY.md (Edit ×2 — remove the 4 deleted-slice rows: `cg_preconditioning_framework`, `divfree`, `plane_rotation_stream`, `sparse_triangular_solve`; 5 survivor rows preserved by bracketing)
- book/src/spec/index.md (Edit ×1 — remove the 4 status-table rows; the interleaved survivor `arnoldi step` row preserved inside the single replacement block; no header count-prose to decrement — header is qualitative + frozen-date only)
- book/src/concepts/dependency-map.md (Edit ×10 — mermaid reachability-GC: remove all snake_case `divfree`/`cg_preconditioning_framework`/`plane_rotation_stream` `-->` edges across the L1/L2/L3/L4 blocks; hyphenated `plane-rotation-stream` + `sparse-triangular-solve:::planned` nodes preserved)

Gate hits:
- anchor-verify: ALL anchors matched on-disk byte-for-byte BEFORE editing. SUMMARY.md `:294`/`:295`/`:298`/`:300` deleted rows + `:292`/`:293`/`:296`/`:297`/`:299` survivors (Read of :288-305); spec/index.md deleted rows `:18`/`:19`/`:21`/`:22` + survivors `:15`/`:16`/`:17`/`:20`/`:23` (Read of full file); all 10 dependency-map `[old]` blocks (Reads of :148-194 L1, :214-264 L2, :278-318 L3, :347-392 L4). These three files were NOT touched by D1–D4 or D6 (D6 row + on-disk anchors confirm — D6 touched only L4/domain_energy_reduce.md), so anchors intact as the report verified. The repairer touched only CYCLE.md analysis-prose (44→61 tally + green-build claim softening), NOT the proposed-change blocks — applied as written.
- surviving-row-points-at-deleted-file: 0 (post-apply grep over SUMMARY.md + spec/index.md for links to the 4 deleted slugs → EMPTY; 5 survivor rows confirmed present in BOTH surfaces).
- mermaid-snake_case-deleted-slug-edges-remaining: 0 (post-apply `grep -nE '(divfree|cg_preconditioning_framework|plane_rotation_stream) -->'` → NONE). Hyphenated survivor nodes intact: `plane-rotation-stream:::planned` (:74-75/:93/:95/:172-179) + `sparse-triangular-solve:::planned` (:81/:99-101) preserved — distinct planned-marker/L1-stream nodes, NOT the deleted slices.
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- variant-axis-missing: n/a (removal-only, no operator surface)
- H1-reuses-page-heading / append-on-missing-slug / concept_writes-on-existing-slug: n/a (no file creation, no slug create, no append)
- SUMMARY.md / spec/index.md / concept auto-fix: NOT triggered — this report IS the single-owner shared-index removal; nothing to auto-register (the inverse — removing entries for deleted files).
- graded-stack reachability-GC (step-5b): the campaign's per-slice COMPLETION. Removing these three shared-index reference surfaces (SUMMARY nav rows, spec-index status rows, mermaid `reference`-class edges) makes the 4 deleted slices FULLY unreachable from any root over any edge — all 4 are now graph-GC-collected (the D1–D4 deletions removed the files + repointed the 18 inbound markdown links; D5 removes the last index/SUMMARY/mermaid references). 0 NEW rank violations (removal-only; no node status flip, no new firm node, no new edge). All removed edges were `reference`-class navigational (no `depends-on` blocking edge targeted any deleted slug — D1–D4 rows + this report §3 grep-confirmed). Reachability-safe.
- citecheck (--scan, bounds + path-hygiene): 6 ok, 0 failing (ran `python3 tools/citecheck/citecheck.py --scan <this CYCLE.md> --quiet` THIS invocation). No MISS/AMBIG/OOB. Non-blocking.

Open questions promoted:
- (none net-new) — `roadmap-goal-unbuilt-frontier-SUMMARY-grouping-deferred` ALREADY exists in the ledger (open-questions.md:1319) and STAYS deferred: no `roadmap_goal` chapter minted this cycle (all 4 deleted slices absorbed into existing firm homes by D1–D4; the report explicitly did NOT re-open it or add a `## Roadmap goals — unbuilt frontier` SUMMARY grouping). Per append-only discipline I did NOT duplicate the existing section. The report's other §Open-questions items are integrator-sequencing caveats (D5 co-landing boundary, no header count-prose, ambiguous-edge-check-none-found) + a closeability signal for `l4-preconditioning-framework-promotion` (already logged by D1's row), none net-new OQ sections.

Build-relevant: yes (edits touch book/src/SUMMARY.md + book/src/spec/index.md + book/src/concepts/dependency-map.md — finalize must rebuild; these removals are the GENUINE hard-breakers' resolution: a SUMMARY entry pointing at a deleted file is an mdBook hard-fail, so D5 MUST co-land with the D1–D4 slice deletions in the same `cargo make book` — which it does, as the cycle's FINAL per-report integration).

Notes: SEVENTH and FINAL per-report integration of cycle-097 (the cycle's last dispatch; appended after D1 cg-precond + D2 divfree + D3 sparse-trisolve + D4 plane-rotation + D6 domain_energy_reduce rows). This is the SUMMARY/index/mermaid row-removal that makes the 4 slice deletions linkcheck2-safe + mdBook-safe for finalize's authoritative rebuild. overall_status: ready set by the REPAIRER after softening the §Summary green-build claim to cycle-scope and correcting the 44→61 edge tally; the proposed-change blocks were critic-verified verbatim and untouched by the repairer — I applied them as written. CAMPAIGN STATE (graded-stack P2 slice-deletion, first tranche): 4 of 9 slices now FULLY DELETED + unreachable (`cg_preconditioning_framework`, `divfree`, `plane_rotation_stream`, `sparse_triangular_solve`); 5 slices REMAIN by design (`arnoldi_step`, `cg`, `gmres`, `orthog`, `polynomial_recurrence_step`) — deferred to c098/c099, their SUMMARY rows + spec-index rows + mermaid edges intentionally left intact (I verified all 5 survivor rows present in both index surfaces + survivor mermaid edges untouched). All file-state claims here are from disk I read/edited THIS invocation, not from any assumed sibling landing: I directly Read each anchor region before every Edit and the post-apply greps confirm the end state. The 4 deleted slice FILES were already removed by D1–D4 (confirmed via on-disk `[ -e ]` check this invocation: all 4 gone, 5 survivors present) — D5 removes only the dangling index/SUMMARY/mermaid references. Did NOT run `cargo make book` (finalize's job — authoritative rebuild + linkcheck2 + step-5b graded-stack linter run). Deferred `integrated_at:` + `integration_commit:` to finalize per role-spec (per-report integrator must not touch consumed-report frontmatter).

---
