# cycle-122 integrator staging log

Per-report integration staging for cycle-122 (batch-39). Newest row LAST (append-only).
Row ORDER is the authoritative apply-order record; `applied_at` timestamps are advisory only.

---

## 2026-06-07T071941Z-harvester-libceed-substrate-ops
applied_at: 2026-06-07T091500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/element_restrict.md (new — rank-0 roadmap_goal, the G/Gᵀ stage)
- book/src/L1/basis_apply.md (new — rank-0 roadmap_goal, the B/Bᵀ stage)
- book/src/L1/quad_point_contract.md (new — rank-0 roadmap_goal, the D stage)
- book/src/L1/geom_factor_build.md (new — rank-0 roadmap_goal, the geometry-factor build-pass)
- book/src/L1/index.md (edit — new §Roadmap_goal (libCEED contraction substrate — 4) subsection bullet block after the kernel-impl bullet; + 4 dep-map rows after the kernel-impl dep-map row)
- book/src/SUMMARY.md (edit — 4 new L1 chapter entries under the FE-assembly sub-spine, after libceed-quadrature-kernel-impl)
- scaffolding/open-questions.md (append — 3 OQs; see below)

Gate hits:
- citecheck (--scan): 19 ok, 0 failing (bounds + path-hygiene clean) — non-blocking.
- graded-stack rank linter: RANK VIOLATIONS none. Well-foundedness holds (the 4 new nodes are rank-0; consumer libceed-quadrature-kernel-impl correctly STAYS roadmap_goal — rank-0 ≤ rank-0 vacuous).
- unresolved_depends_on_targets: 6 → 2 (CONFIRMED by linter). The 4 libceed substrate targets (element_restrict/basis_apply/quad_point_contract/geom_factor_build) now resolve to LIVE files; the 2 remaining UNRESOLVED are the D1/D2 AMR verbs L1/dorfler_mark + L1/flux_recovery_estimate (out of this report's scope, c121-routed).
- SUMMARY.md chapter registration: report proposed all 4 entries — no auto-fix needed.
- alphabetical-position insert: NOT applied — the report explicitly specified the position (the 4 substrate ops grouped contiguously AFTER their consumer libceed-quadrature-kernel-impl, a deliberate cohort grouping within the FE-assembly sub-spine, mirroring the index.md cohort subsection). Position was report-specified, not integrator-chosen, so the alpha-directive (which governs only integrator-chosen positions) does not override.
- index-placeholder displacement: n/a (no placeholder rows).
- implied-component stub materialization: n/a (report authored all 4 chapters in full).

Open questions promoted:
- libceed-quadrature-kernel-impl-consumer-note-reanchor-after-substrate-land (the consumer's stale NOTE/speculative-ops text → c122-D6 / next integrator; same-file-collision deferral)
- libceed-substrate-element-local-rank-tensor-l1-vocabulary-front (batch-39 meta: schedule a dedicated element-local rank-structured tensor L1 vocabulary front that would firm all 4 + the consumer)
- record-element-local-tensor-needs-definition-home-at-firming (gated on firm flip: concepts/element-local-tensor.md definition home)
- (NOT promoted — RESOLVED in-report, not open: libceed-quadrature-kernel-impl-sum-factorization-classification = transparent trick, recorded in basis_apply; libceed-quadrature-kernel-impl-roadmap-goal-vs-rough-in-disposition = STAYS roadmap_goal.)

Build-relevant: yes (4 new book/src/L1/*.md + index.md + SUMMARY.md).

Notes:
- All 8 critic checks pass; overall_status: ready set by the critic directly on a clean all-pass report (no repairer ran) — accepted per role-spec (both critic-direct-ready and repairer-set-ready are valid).
- deferred integrated_at to finalize per role-spec (did NOT touch the report's frontmatter integrated_at / integration_commit).
- REACHABILITY-GC NOTE (for finalize/meta, NON-blocking): the graded-stack reachability GC marks only over `depends-on` edges; the 4 new nodes are `pulled-by` (reference-class, free) their consumer, and the consumer reaches the feature root only via reference-class `realizes-leaf`/`realizes-kernel-api` edges (NOT depends-on). So the GC flags the whole libceed-quadrature-kernel-impl roadmap_goal subtree as [GARBAGE*]/[garbage?] — BUT this is a PRE-EXISTING characteristic: the consumer (landed c121, present at HEAD) was ALREADY [GARBAGE*] under the depends-on-only GC before this report; the 4 new nodes simply inherit it via the pulled-by reference edges. This report introduced NO new rank violation and NO new detritus beyond the pre-existing reference-edge-liveness accounting question (whether reference edges to firm/root nodes should count toward liveness — a batch-39-meta-relevant scheme question, NOT a defect in this report). RESULT line: 0 rank violations, 127 detritus nodes total (pre-existing baseline + this subtree), 61 untyped warnings. The narration here is from the linter output I ran this invocation, not an assumed state.
- No sibling reports landed before this (first report of cycle-122; I created the staging dir + this log).

---

## 2026-06-07T071941Z-lowering-verifier-libceed-eigsolve-kernel-api-audit
applied_at: 2026-06-07T101800Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/libceed-quadrature-kernel-impl.md (edit — appended 8-entry `verified_against:` YAML block at EOF; PLUS the D4-confirmed stale-prose re-anchor: frontmatter `depends-on` NOTE "rough-in; no anchor yet" → "roadmap_goal (authored c122 D4)" for all 4 substrate targets, and the body §"Speculative L1 operators" header+bullets re-anchored to "Substrate L1 operators (roadmap_goal, authored c122 D4)" with live `[slug](./slug.md)` links to the 4 now-on-disk substrate chapters)
- book/src/L3/eigsolve-impl.md (edit — appended 7-entry `verified_against:` YAML block at EOF)
- scaffolding/open-questions.md (append — 2 OQs; see below)

Gate hits:
- citecheck (--scan on report CYCLE.md): 41 ok, 7 failing — all 7 are `AMBIG` (bare `integrator.hpp`/`integrator.cpp`/`operator.cpp` basenames in the report's PROSE-DISCUSSION correspondence tables, each matching 2 files under reference/palace/). NON-BLOCKING and NOT in the landed artifacts: every citation in the two `verified_against:` blocks I applied uses FULL paths (`reference/palace/palace/fem/integrator.hpp:58-61`, `.../fem/libceed/integrator.cpp:423-445`, `.../linalg/operator.cpp` not landed, etc.). I spot-verified the load-bearing full-path anchors on disk: slepc.cpp:635 = `EPSSetType(eps, EPSKRYLOVSCHUR)` exact; fem/integrator.hpp:58-61 = the `Assemble(...) const = 0` pure-virtual (shared pivot) exact; libceed/integrator.cpp:423 = `AssembleCeedOperator` exact; arpack.cpp:331/:333 = `else if (ido == 99)`/`break;` exact; test/unit/test-libceed.cpp:284 = `TestCeedOperatorFullAssemble` exact (single-`palace/`). No MISS/OOB. The AMBIG is on prose, not on the landed YAML — does not block.
- realizes-kernel-api edge-class gate: PASS — both edges stay `reference`-class. libceed impl: `realizes-kernel-api` under `reference:` (line 21); depends-on lists only the 4 substrate ops. eigsolve impl: both `realizes-kernel-api` edges (→ L3/eigsolve, → L4/eigsolve) under `reference:` (lines 21,23); depends-on lists only krylov-step/lanczos_step/ksp_solve/apply_linop/orthogonalize. My edits were append-only YAML + impl-side prose; touched NO edge declarations.
- API-status-preservation gate: PASS — libceed kernel-api `status: obstruction` / `sub_kind: opaque-library-ownership` UNCHANGED; eigsolve kernel-api `firmness: partial-obstruction` UNCHANGED (I did not touch either API file).
- YAML round-trip gate: PASS — both appended blocks `yaml.safe_load` clean (libceed 8 entries, eigsolve 7 entries); zero `note:` values lead with a quote of either kind (the `verified-against-note-no-leading-quote-of-either-kind` hazard clear).
- forward-edge / variant-axis / H1 / append-on-missing-slug / index-placeholder: n/a (append-only verified_against + impl-side prose refresh; no new chapters, no SUMMARY/index rows, no operator-algebra mutation).
- stale-prose-reanchor (the D6-routed Note-1): APPLIED — D4's 4 roadmap_goal substrate ops confirmed on disk this invocation (`book/src/L1/{element_restrict,basis_apply,quad_point_contract,geom_factor_build}.md` all `rank: roadmap_goal`), so the same-file-SEQUENTIAL deferral D4↔D6 is now safe to resolve. This RESOLVES the D4-promoted OQ `libceed-quadrature-kernel-impl-consumer-note-reanchor-after-substrate-land` (finalize may mark it resolved).

Open questions promoted:
- eigsolve-arpack-ido99-break-range-carry-forward (the `:330-333`→`:331-334` non-load-bearing nit on book/src/L3/eigsolve.md §Evidence; routed to a future lifter)
- kernel-impl-realizes-leaf-vs-realizes-kernel-api-label-vocabulary (D6 recommends KEEP DISTINCT as free documentation; optional batch-39-meta uniform-vocabulary decision)
- (NOT promoted — already in ledger from D4: libceed-quadrature-kernel-impl-consumer-note-reanchor-after-substrate-land, now RESOLVED by the re-anchor applied above. NOT promoted — STRUCTURAL-audit caveats that are not actionable open items: both-audits-structural-not-empirical, libceed-UNRESOLVED-edges-resolve-when-D4-lands [D4 has landed], no-directionality-violation.)

Build-relevant: yes (2 book/src/*.md edited).

Notes:
- All 8 critic checks pass; overall_status: ready set by the critic DIRECTLY on a clean all-pass report (no repairer ran) — accepted per role-spec (both critic-direct-ready and repairer-set-ready are valid).
- deferred integrated_at to finalize per role-spec (did NOT touch the report's frontmatter integrated_at / integration_commit).
- The libceed impl ALREADY carried a prose `## Verified-against` section (the producer's own list, lines 179-201 pre-edit); the appended `verified_against:` YAML block is the lowering-verifier's INDEPENDENT structured audit record (the dual-block convention: producer self-list prose + independent-verifier structured YAML). They coexist; no conflict.
- DISK-OBSERVED, not assumed: I directly read the 4 D4 substrate files (all `rank: roadmap_goal`) and both kernel-api surfaces (statuses unchanged) this invocation before claiming their state. The re-anchor was applied because the substrate files are present on disk NOW, not because a staging row asserted it.
- REACHABILITY-GC NOTE (for finalize/meta, NON-blocking, UNCHANGED by this report): the two impls (libceed-quadrature-kernel-impl, eigsolve-impl) reach the feature root only via reference-class `realizes-kernel-api`/`realizes-leaf` edges, so the depends-on-only GC continues to flag them `[GARBAGE*]` — a PRE-EXISTING characteristic (both present at HEAD before this report; this report appended only `verified_against:` audit blocks + a prose re-anchor, introducing NO new node, NO new edge, NO rank change). 0 new rank violations, 0 new detritus. Same reference-edge-liveness scheme question the D4 row flagged for batch-39 meta.

---

## 2026-06-07T071941Z-lowering-verifier-smoother-kernel-api-audit
applied_at: 2026-06-07T112000Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/multigrid-relaxation-smoother.md (edit — appended 8-entry `verified_against:` YAML block at EOF; PLUS the 4 off-by-one carry-forward citation corrections: DRIFT-1 sweep-loop header `distrelaxation.cpp:103`→`:102` at the NL1 site + the §Evidence Mult2-bullet site; DRIFT-2 `MultTranspose2` range `:121-152`→`:121-151` at the "NOT symmetric in general" non-law site + the §Evidence site)
- scaffolding/open-questions.md (append — 1 OQ; see below)

Gate hits:
- citecheck (--anchor on the 2 corrected anchors): both ok-zero-drift — `for (int it` ⇒ ok at distrelaxation.cpp:102; `MultTranspose2` ⇒ ok at distrelaxation.cpp:121-151. The 4 landed corrections all resolve exactly on disk.
- citecheck (--scan on report CYCLE.md): 20 ok, 0 failing — bounds + path hygiene CLEAN. (The repairer's frontmatter fixes `distrelaxation.cpp:1-157`→`:1-156` + `.hpp:1-93`→`:1-92` resolved the prior over-range provenance bounds; no MISS/AMBIG/OOB remains.) Non-blocking.
- realizes-kernel-api edge-class gate: PASS — the impl edge `target: L1-L0/triangular-solve-obstruction, kind: realizes-kernel-api` stays under `reference:` (lines 24-26), NOT `depends-on:` (lines 15-23). DISK-OBSERVED this invocation. My edits were append-only YAML + 4 anchor-token corrections; touched NO edge declaration.
- API-status-preservation gate: PASS — the kernel-api surface `book/src/L1-L0/triangular-solve-obstruction.md` Status line (:545) stays `obstruction (opaque-library-ownership)` — **kernel-api** (role-label, NOT a status flip). I did not touch that file; DISK-OBSERVED via grep.
- impl rank gate: PASS — `multigrid-relaxation-smoother.md` `rank: firm` UNCHANGED; all four `depends-on` constituents firm (well-foundedness firm ≤ firm holds). No status flip proposed or applied.
- YAML round-trip gate: PASS — appended block `yaml.safe_load` clean, 8 entries, all verdict `supports`; zero `note:` value leads with a quote of either kind (the leading-quote hazard clear).
- forward-edge / variant-axis / H1 / append-on-missing-slug / index-placeholder / SUMMARY-registration / alpha-position / stub-materialization: n/a (append-only verified_against + 4 in-place anchor-token corrections to an existing chapter; no new chapter, no SUMMARY/index row, no operator-algebra mutation, no status flip).

Open questions promoted:
- relaxation-slot-kernel-api-sibling-realizes-edges-cohort (the only "partial" — correctly-disclosed scoped coverage; whether to add free realizes-kernel-api reference edges from sibling chebyshev-smoother/jacobi-smoother so the relaxation-slot GS-free cohort is jointly navigable from the kernel-api surface; batch-39-meta DIRECTIVE-3-pair-review OR combinator-miner/abstractor follow-up; NOT blocking)
- (NOT promoted — by-design/not-defect/now-resolved disclosures, not open items: the kernel-api `[garbage?]` lint flag is by-design DIRECTIVE-3 grounded-future [planner already accounts]; the two off-by-one drifts are RESOLVED in-cycle by Change 2/3 applied above [no parked item]; no-directionality/rank-invariant-violation = clean negative finding.)

Build-relevant: yes (book/src/L1/multigrid-relaxation-smoother.md edited — verified_against block + 4 citation corrections; an mdBook-rendered chapter).

Notes:
- All 8 critic checks pass/repaired; overall_status: ready set by the REPAIRER after a low-severity citation-validity warning (two whole-file provenance over-ranges in the report frontmatter `inputs:` + Supporting-evidence, `distrelaxation.cpp:1-157`→`:1-156` / `.hpp:1-93`→`:1-92`) was fixed surgically. Those repairer fixes are REPORT-INTERNAL (frontmatter/supporting-evidence provenance), NOT artifact edits — confirmed: the report's three proposed-changes touch only the impl chapter, and the repaired bounds do not appear in any landed citation. Accepted per role-spec (repairer-set ready over a fixed warning is valid).
- deferred integrated_at to finalize per role-spec (did NOT touch the report's frontmatter integrated_at / integration_commit).
- The impl chapter had NO pre-existing `verified_against:` block (grep-confirmed before the append) — conflict-free append; this is the lowering-verifier's independent structured audit record.
- DISK-OBSERVED, not assumed: read the impl frontmatter (reference-class edge + rank: firm) and the kernel-api Status line this invocation before claiming their state. No sibling-report dependency: this is the 3rd report of cycle-122; the two prior staging rows (D-libceed-substrate-ops, D-libceed-eigsolve-audit) touched disjoint files (L1/libceed-* + L3/eigsolve-impl), so no re-read collision with this report's single-file target.

---

## 2026-06-07T071941Z-harvester-correction-step
applied_at: 2026-06-07T080754Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/correction_step.md (new — firm L2 step-kernel combinator `y + B·(x − A·y)`; rank: firm; depends-on L1/apply_linop + L1/axpby; reference edges to jacobi-smoother/chebyshev-iteration/divfree-projector/3 concepts)
- book/src/L2/index.md (edit — dep-map Step-kernels row flip `correction_step` rough-in→firm with live `./correction_step.md` link; + §Vocabulary-cohort: chebyshev-iteration bullet annotated as a `correction_step` specialization + new `correction_step` cohort bullet inserted before linear_combination; + preamble firm-count line `21 firm`→`22 firm`)
- book/src/SUMMARY.md (edit — new `[correction_step](./L2/correction_step.md)` entry in the Step-kernels grouping, alpha between chebyshev-iteration and krylov-step)
- book/src/L2/chebyshev-iteration.md (edit — propagation: re-expressed as a `correction_step` specialization choosing `B = p_order(D⁻¹A)`, with the verbatim-contract anchors)
- book/src/L2/jacobi-smoother.md (edit — propagation: re-expressed as the `B`-slot of `correction_step` for the Jacobi choice `B = ω·D⁻¹`, degree-0 non-iterated)
- scaffolding/open-questions.md (append — 1 new OQ; see below)

Gate hits:
- citecheck (--scan on report CYCLE.md): 33 ok, 0 failing (bounds + path-hygiene CLEAN) — non-blocking. The four decisive verbatim contract anchors (gmg.cpp:176 `Y <- Y + B (X - A Y)`, distrelaxation.cpp:104 `y = y + B (x - A y)`, chebyshev.cpp:193/:264 `y = y + p(A) (x - A y)`) were independently re-verified by the critic via --anchor against on-disk source (META check citation-validity: pass; the producer's +1 codemap-drift-on-chebyshev claim vindicated, on-disk wins). No MISS/AMBIG/OOB.
- graded-stack rank linter: RANK VIOLATIONS none — well-foundedness holds. `correction_step` firm (rank 3) rests on `apply_linop` + `axpby` (both firm, rank 3 confirmed on disk). RESULT: 0 rank violations, 128 detritus nodes (was 127; +1 = the one new node), 61 untyped warnings.
- forward-edge / variant-axis / H1 / append-on-missing-slug / index-placeholder: n/a (firm new chapter authored in full + 4 surface edits; no placeholder rows; no missing-slug append; H1 `# correction_step` distinct from the page-heading convention).
- SUMMARY.md chapter registration: report PROPOSED the SUMMARY entry — no auto-fix needed. Insertion position (between chebyshev-iteration and krylov-step) was report-specified AND alpha-correct within the Step-kernels grouping; no integrator alpha-position discretion exercised.
- implied-component stub materialization: n/a (combinator authored firm; deps already firm on disk).
- divfree-projector home-consistency (critic minor/clarity nit): the critic flagged `correction_step.md` §Borderline citing divfree-projector as `../L1/divfree-projector.md` (line ~248) then `./divfree-projector.md` (line ~258) within one paragraph (both exist/resolve, non-blocking). RESOLVED at apply-time: normalized the §Borderline body reference + the Dependencies "Borderline reference" to the L2 firm home `./divfree-projector.md` consistently. Recorded as applied-discretionarily, rationale `critic-flagged-cosmetic-link-home-consistency` (a single-home reference; both targets resolve, so no integrity change).

Open questions promoted:
- correction-step-wider-replace-and-propagate-set-l1-and-feature-column (the c123 same-layer-cross-cutter follow-on: confirm the wider replace-and-propagate set — L1 multigrid-relaxation-smoother / GMG V-cycle feature column / distributive-relaxation L1 — re-expresses per-sweep bodies THROUGH correction_step; partial-settlement of the c121 `correction-step-replace-and-propagate-scope` OQ, whose L2 leg this report enacted)
- (NOT promoted — the 3 c121 OQs the report SETTLES already exist in the ledger as append-only entries: `correction-step-replace-and-propagate-scope` [PARTIALLY settled — L2 leg done; wider set = the new OQ above], `correction-step-one-vs-two-operator-conjugated-form` [SETTLED, lean (a): one combinator, conjugated B=T·B'·Tᵀ a B-choice], `correction-step-divfree-projector-borderline-7th-instance` [SETTLED, negative: borderline NOTE, kept out of core roster]. Per role-spec I do not edit existing OQ entries; finalize/meta marks resolution. Also already-in-ledger and addressed by the chapter: `correction-step-construction-vs-apply-stratum-assemblediagonal-reciprocal` [the chapter keeps B-construction out of the run-time apply].)

Build-relevant: yes (1 new book/src/L2/*.md + 4 book/src/*.md edits — index.md, SUMMARY.md, chebyshev-iteration.md, jacobi-smoother.md).

Notes:
- All 8 critic checks pass; overall_status: ready set by the critic DIRECTLY on a clean all-pass report (no repairer ran) — accepted per role-spec (both critic-direct-ready and repairer-set-ready are valid).
- deferred integrated_at to finalize per role-spec (did NOT touch the report's frontmatter integrated_at / integration_commit).
- L2 firm count 21→22 (+1 `correction_step`); partly-constructive unchanged at 1 (`deflate`). Preamble line `book/src/L2/index.md:89` updated as the report flagged (D3 the only L2-index-touching dispatch this cycle per overlap analysis → safe single-owner update).
- All 12 distinct cross-reference link targets in the new chapter verified to resolve on disk this invocation (../L1/apply_linop, ../L1/axpby, ./jacobi-smoother, ./chebyshev-iteration, ./divfree-projector, ../L1/divfree-projector, ./krylov-step, ./eigsolve, ./assemble-diagonal, ../semantics/index, ../concepts/{sequential-obstruction,constructed-operators,variant-absorption}). The 4 propagation-edit anchor old_strings all matched uniquely.
- REACHABILITY-GC NOTE (for finalize/meta, NON-blocking): the rank linter flags `L2/correction_step` `[GARBAGE*]` under the depends-on-only reachability GC — the SAME pre-existing reference-edge-liveness scheme characteristic the prior c122 staging rows documented. `correction_step` is reachable from the feature roots ONLY via reference-class edges (its smoother/V-cycle CONSUMERS cite it as `reference`/specialization, not depends-on; an entry's specializations don't depends-on it), so the depends-on-only mark-sweep does not reach it. This is NOT a defect in this report — it is the batch-39-meta-relevant scheme question (whether reference edges to firm nodes should count toward liveness). 0 new rank violations introduced; detritus +1 is solely the new node under this known accounting question. Narration is from the linter output I ran this invocation.
- DISK-OBSERVED, not assumed: I re-read book/src/L2/index.md (full, both pages) before editing it (the earlier grep/sed did not satisfy the Edit read-gate); verified apply_linop/axpby `rank: firm` directly; confirmed SUMMARY insertion context lines 144-145 on disk before the edit; located + read both propagation anchors before editing. This is the 4th report of cycle-122; the three prior staging rows touched disjoint files (L1/libceed-*, L3/eigsolve-impl, L1/multigrid-relaxation-smoother) — no re-read collision with this report's L2 targets, confirmed by the clean unique anchor matches.

---

## 2026-06-07T071941Z-layer-intro-author-gmg-promotion-eval
applied_at: 2026-06-07T120500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/feature/geometric-multigrid-preconditioner.L4.md (edit ×4 — (1) frontmatter: re-type `L3/chebyshev` + `L2/jacobi-smoother` from `depends-on (composes)` → `reference` (sibling iteration-views) + `rank: rough-in`→`firm`; (2) §"Why this is rough-in"→§"Why this is firm (c122 re-check)"; (3) §Status reconciled rough-in→firm; (4) constituent down-link table cells — smoother rough-in→firm, chebyshev/jacobi labelled L3/L2 iteration-VIEW (reference))
- book/src/feature/geometric-multigrid-preconditioner.L1.md (edit ×3 — (5) frontmatter `rank: rough-in`→`firm` (edges already correctly `reference`-typed); (6) §"The pure V-cycle" smoother-leg prose stale-forward-ref reconcile (kernel-impl firm c121; iteration-views not blocking deps); (7) §Status reconciled rough-in→firm)
- book/src/feature/index.md (edit — GMG matrix cell `(rough-in)`→`(firm)`)
- scaffolding/open-questions.md (append — 2 OQs; see below)

Gate hits:
- graded-stack rank linter: RANK VIOLATIONS none — WELL-FOUNDEDNESS CONFIRMED post-flip. `rank(geometric-multigrid-preconditioner.L4/.L1 = firm) ≤ min(deps) = firm` holds: all 5 blocking `depends-on` constituents firm on disk (preconditioning-framework / fe_space_hierarchy / multigrid-relaxation-smoother / reciprocal / normalize), confirmed via `--show-inbound` (the now-firm column appears in each constituent's inbound depends-on set). The 2 re-typed edges (L3/chebyshev, L2/jacobi-smoother) are now `reference`-class — correctly NOT in the depends-on set, ignored by the rank check. RESULT: 0 rank violation(s), 134 detritus node(s), 61 untyped (warning), EXIT 0.
- citecheck (--scan on report CYCLE.md): 11 ok, 0 failing (bounds + path-hygiene CLEAN) — non-blocking. `gmg.cpp:126-205` verified in-bounds on disk (line 126 = `GeometricMultigridSolver<OperType>::Mult`; file is 210 lines; 205 well in-range). No MISS/AMBIG/OOB.
- forward-edge / variant-axis / H1 / append-on-missing-slug / index-placeholder / SUMMARY-registration / alpha-position / stub-materialization: n/a (status-promotion edits to 3 existing chapters; no new chapter, no SUMMARY/index ROW insert (only an in-place cell flip), no operator-algebra mutation, no missing-slug).
- edge re-type faithfulness: the central move (depends-on→reference on the 2 iteration-view edges) was independently confirmed FAITHFUL by the critic (META edge-label-fidelity: pass, "the decisive check") — NOT edge-laundering; it brings the L4 file into agreement with the already-correct L1 file's reference-class typing, and the firm smoother's own depends-on points at `L1/chebyshev-smoother` (firm), never at `L3/chebyshev`. Integrator concurs from on-disk reads this invocation.

Open questions promoted:
- gmg-firm-flip-re1-reachability-l2l3-iteration-views-absorbed-below-spine (the RE1 re-statement: L1 chebyshev-smoother GROUNDED via the smoother chain; L2/L3 chebyshev/jacobi iteration-VIEWS stay absorbed-below-spine like RE5/RE7; routed to c123/batch-39 meta standing RE-recheck — a faithful-classification correction, NOT a regression)
- gmg-firm-flip-satisfies-fespacehierarchy-2nd-firm-consumer-trigger (the firm-flip now ALSO satisfies the c118 watch's literal "2nd FIRM consumer" wording; folds into the already-scheduled `record-FiniteElementSpaceHierarchy-promote-watch-wording-reconcile`; operationally inert — page already on disk `rank: firm`, promotion already sanctioned at the ≥2-consumers floor)

Build-relevant: yes (3 book/src/feature/*.md edited — 2 chapters + index.md).

Notes:
- All 10 critic checks pass (the 8 canonical + rank-invariant + reachability); overall_status: ready set by the critic DIRECTLY on a clean all-pass report (no repairer ran) — accepted per role-spec (both critic-direct-ready and repairer-set-ready are valid). The critic scrutinized the firm claim HARD (META: "It was scrutinized hard … verified independently against on-disk artifact state and the Palace source via palace-codemap") and confirmed the edge re-type is FAITHFUL.
- THE FIRM FLIP + WELL-FOUNDEDNESS: column promoted rough-in→firm at BOTH levels; `feature_root: seed` KEPT on both (GC-root marker, a separate axis from the resolution ladder, per the report). Post-flip the rank linter reports 0 rank violations and the column's depends-on set is all-firm — well-foundedness `rank(firm) ≤ min(firm)` holds. The 2 demoted edges are now `reference`-class sibling iteration-views.
- deferred integrated_at to finalize per role-spec (did NOT touch the report's frontmatter integrated_at / integration_commit).
- DISK-OBSERVED, not assumed: I re-read both feature chapters + grepped feature/index.md line 59 before editing; all 8 edit-block `[old]` anchors matched uniquely on disk. The well-foundedness claim is from the rank linter I ran THIS invocation (RESULT line above + the `--show-inbound` constituent confirmation), not from an assumed state. This is the 5th report of cycle-122; the four prior staging rows touched disjoint files (L1/libceed-*, L3/eigsolve-impl, L1/multigrid-relaxation-smoother, L2/correction_step + its surface edits) — no re-read collision with this report's feature/ targets (confirmed: the prior c122-D5 row edited `L1/multigrid-relaxation-smoother.md`, which this report only LINKS to / does not edit; its `rank: firm` was read directly this invocation and is the basis for the GMG firm flip).
- REACHABILITY-GC NOTE (for finalize/meta, NON-blocking): the detritus count is 134 (was 128 at the c122-D3 row). The increase is NOT introduced by this report's firm-flip per se — it is the same pre-existing reference-edge-liveness scheme question the prior c122 rows documented (nodes reachable only via reference-class edges are flagged by the depends-on-only GC). This report introduced 0 new nodes, 0 new rank violations; it converted 2 depends-on edges to reference (which is exactly the faithful disposition and is WHY the chebyshev/jacobi iteration-views are now reference-only-reachable — the RE1 absorbed-below-spine question, flagged in the first OQ above for the batch-39 meta). The batch-39 meta should reconcile the running detritus baseline against the reference-edge-liveness scheme decision; not a defect in this report.

---

## 2026-06-07T071941Z-harvester-flux-recovery-estimate
applied_at: 2026-06-07T123000Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/flux_recovery_estimate.md (new — firm L1 ZZ flux-recovery a-posteriori error-estimate verb; the AMR estimate stage; rank: firm; depends-on L1/ksp_solve + L1/apply_linop + L1/nrm2; reference edges to fe-assemble-libceed-boundary-obstruction kernel-api / amr-estimate-mark-refine theme / fe_space / interpolator)
- book/src/L1/index.md (edit ×2 — (1) dep-map row flip rough-in→firm with live `./flux_recovery_estimate.md` link; (2) NEW §Vocabulary-cohort "Firm (AMR estimate/mark vocabulary) — DIRECTIVE-2" sub-list heading + D1 cohort bullet, appended after the Kernel-impl(smoother) block)
- book/src/SUMMARY.md (edit — new FLAT `[flux_recovery_estimate](./L1/flux_recovery_estimate.md)` L1 chapter entry after the FE-space sub-spine group, BEFORE the `# L1 > L0` divider — the build-clean flat fallback, NOT a nested group under the not-yet-existing amr-estimate-mark-intro.md)
- scaffolding/open-questions.md (append — 2 OQs; see below)

Gate hits:
- citecheck (--scan on report CYCLE.md): 26 ok, 0 failing (bounds + path-hygiene CLEAN) — non-blocking. No MISS/AMBIG/OOB. Spot-verified the repaired pinpoints on disk this invocation: errorestimator.cpp:176 = `Flux->Mult(x, rhs);` exact; :177 = `ksp->Mult(rhs, y);` exact; :211 = `estimates = 0.0;` exact; :245 = `// Each thread writes to non-overlapping entries...` exact; :386/:508 = `linalg::Sqrt(estimates, (Et > 0.0) ? 0.5 / Et : 1.0);` (Grad/Curl) exact; :163 = `ksp = ConfigureLinearSolver<OperType>(...)` exact. The repairer's interior-pinpoint drift-cluster fix resolved correctly.
- graded-stack rank linter: RANK VIOLATIONS none — well-foundedness holds. `flux_recovery_estimate` firm (rank 3) rests only on ksp_solve (firm, §Status), apply_linop (firm, frontmatter), nrm2 (firm, frontmatter); `rank(u) ≤ min(deps)` satisfied. Firm-on-positive-structure escape correctly applied (no-dedicated-test caveat non-gating per jacobi-smoother/reciprocal precedent). RESULT line: 0 rank violation(s), 135 detritus node(s), 61 untyped (warning).
- unresolved_depends_on_targets: 2 → 1 (CONFIRMED by linter). The L1/flux_recovery_estimate edge target now resolves to a LIVE file; the SOLE remaining unresolved is `L1-L0/amr-estimate-mark-refine -> L1/dorfler_mark` (D2's verb, not yet on disk — fires on D2's integration, which lands last). Matches the dispatch's "resolves 1 of the 2 remaining" expectation.
- SUMMARY.md chapter registration: report PROPOSED a nested group-header entry pointing at the not-yet-existing `./L1/amr-estimate-mark-intro.md`; per the dispatch instruction + META repair finding 8, applied the build-clean FLAT fallback instead (register the chapter directly in the L1 list at the tail, no missing-file link). `grep -c amr-estimate-mark-intro book/src/SUMMARY.md` = 0 (no dangling group link). All 8 new-chapter cross-reference link targets verified on disk this invocation (apply_linop/ksp_solve/nrm2/fe-assemble-libceed-boundary-obstruction/amr-estimate-mark-refine/fe_space/interpolator/libceed-quadrature-kernel-impl all OK).
- new-SUMMARY-kind-grouping group-intro stub: NOT created — the AMR estimate/mark grouping is DEFERRED whole (the group-intro is the c123 layer-intro-author's artifact, OQ promoted); the flat fallback avoids the duplicate-file/missing-file build break without prematurely materializing a grouping. Recorded the deferral as an OQ rather than auto-creating a stub (both D1 and D2 use the flat fallback by design per the dispatch).
- alpha-position insert: n/a for the SUMMARY flat entry (placed as a flat top-level L1 chapter at the tail of the L1 Part before the lowering divider — a transitional flat home pending the c123 AMR grouping; not an alpha-within-grouping insert). The index.md dep-map row position was report-specified (in the existing AMR-vocabulary dep-map group, replacing the rough-in row in place) — no integrator alpha discretion exercised.
- index-placeholder displacement / forward-edge / variant-axis / H1 / append-on-missing-slug / implied-component-stub: n/a (firm chapter authored in full + in-place row flip + cohort bullet + flat SUMMARY entry; no placeholder rows; H1 `# flux_recovery_estimate` distinct from page-heading convention; variant-axis (Grad/Curl) explicitly enumerated in the chapter).
- theme firm-flip (amr-estimate-mark-refine): NOT applied (correct) — D2 (dorfler_mark) is not yet on disk; the theme firm-flip requires BOTH verbs firm and is left to D2's integration, which lands last. This report lands ONLY flux_recovery_estimate firm.
- §Vocabulary-cohort grand-total tally: NOT touched — per the report + overlap analysis, flux_recovery_estimate is a NEW AMR-vocabulary-group member, distinct from the 43-member L1 firm grand total (main + FE-assembly + FE-space + Mesh-construction sub-spines); the AMR group carries no consolidated running count. The new cohort heading I added states this explicitly.

Open questions promoted:
- amr-estimate-mark-group-intro-needs-authoring (c123 layer-intro-author: author the by-kind group-intro navigational-container + convert the two flat SUMMARY entries to a nested AMR estimate/mark grouping + rename the index.md dep-map group header to drop "Rough-in")
- composite-as-l2-linear-combination-deferred-abstractor-pick (demand-gated future abstractor/combinator-miner: the 3D Grad+Curl composite as an L2 linear_combination over indicators if a 2nd indicator-combining site surfaces; for now recorded as in-chapter law 4)
- (NOT promoted — RESOLVED in-report, already in ledger as append-only entries: `flux-recovery-estimate-flux-channel-axis-vs-separate-verbs` [RESOLVED: single parametric axis, composite is L2 linear_combination not a 3rd verb], `flux-projector-constructed-operator-gate-vs-absorbed` [RESOLVED: construction-absorbed closure member, not a run-time gate]. NOT promoted — already in ledger and only PARTIALLY fired by this verb: `amr-estimate-mark-refine-theme-firmness-gate` [fires fully on D2 landing the 2nd verb dorfler_mark]. NOT promoted — by-design disclosures, not open items: ksp_solve-convergence + libCEED-integral are referenced opaque boundaries not reconstructed [the firm-vs-partly-constructive disposition, settled in-chapter]; single-rank DIRECTIVE-1 reading [settled in-chapter]. Per role-spec I do not edit existing OQ entries; finalize/meta marks resolution.)

Build-relevant: yes (1 new book/src/L1/*.md + index.md + SUMMARY.md edits).

Notes:
- overall_status: ready set by the REPAIRER after a low-severity citation-validity WARNING (an interior-pinpoint drift cluster — all 27 citations cleared citecheck --scan bounds; the drift was fine-grained pinpoint slip INSIDE otherwise-correct block ranges) was fixed surgically. The repairer's 7 pinpoint corrections (FluxProjector::Mult :180/:181→:176/:177 + block :170-181→:170-178; ksp config :165→:163; zero-init :209-210→:211; non-overlapping comment :248→:245; CeedOperatorApplyAdd boundary; hpp class end-lines; Curl Sqrt :506→:508) were re-verified on disk this invocation — all resolve exactly. Accepted per role-spec (repairer-set ready over a fixed warning is valid; canonical token).
- deferred integrated_at to finalize per role-spec (did NOT touch the report's frontmatter integrated_at / integration_commit).
- REACHABILITY-GC NOTE (for finalize/meta, NON-blocking): the rank linter flags `L1/flux_recovery_estimate` `[GARBAGE*]` under the depends-on-only reachability GC — the SAME pre-existing reference-edge-liveness scheme characteristic the prior c122 staging rows document. The verb is reachable from the feature roots only via the `amr-estimate-mark-refine` L1>L0 theme over `reference`-class edges (the theme cites it; an estimate verb is not depends-on'd by a feature column over a blocking edge), which the depends-on-only GC does not traverse. 0 new rank violations introduced; the +1 detritus (134→135) is solely this new node under the known accounting question (whether reference edges to firm/theme nodes should count toward liveness — a batch-39-meta-relevant scheme question, NOT a defect in this report). Narration is from the linter output I ran this invocation, not an assumed state.
- DISK-OBSERVED, not assumed: I read the index.md dep-map row + the §Vocabulary-cohort Kernel-impl tail before editing; the rough-in flux_recovery_estimate row was found at index.md line 206 (the report's claimed :195 had drifted because the prior c122-D-libceed-substrate-ops landing added FE-assembly/substrate rows + a Roadmap_goal cohort subsection above it — confirmed by re-reading on disk, not assumed from the staging log). Both depends-on firm statuses (apply_linop/nrm2 frontmatter `rank: firm`; ksp_solve §Status `firm`) read directly this invocation. This is the 6th report of cycle-122; the five prior staging rows touched index.md (D-libceed-substrate-ops added the substrate rows/subsection I read around) — I re-read the live index.md state and matched my dep-map old_string uniquely against the on-disk rough-in row, so no stale-cache collision. The other four prior rows touched disjoint files (L3/eigsolve-impl, L1/multigrid-relaxation-smoother, L2/correction_step + surfaces, feature/*) — no collision with this report's flux_recovery_estimate / SUMMARY targets.

---
## 2026-06-07T071941Z-harvester-dorfler-mark
applied_at: 2026-06-07T082439Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/dorfler_mark.md (new — firm L1 Dörfler bulk-marking verb; rank: firm; depends-on cites-evidence dorfler.cpp:14-171 / basesolver.cpp:103-115 / :220-233 / configfile.hpp:97-119 + lowers-to L1-L0/amr-estimate-mark-refine; reference edges to L1/flux_recovery_estimate, L1/nrm2, feature/lifecycle.L4)
- book/src/L1/index.md (edit — dep-map row flip rough-in→firm with live ./dorfler_mark.md link; repairer-re-anchored over-mark mechanism: single-rank lower-bound pivot :36, multi-rank bracket-selection tie-break :163 degenerates :64-67, coverage post-condition MFEM_VERIFY :167-169)
- book/src/SUMMARY.md (edit — new FLAT [dorfler_mark](./L1/dorfler_mark.md) L1 chapter entry, placed before the D1 flat flux_recovery_estimate entry (alpha: dorfler<flux), BEFORE the # L1 > L0 divider; build-clean flat fallback per repairer, NOT under the non-existent amr-estimate-mark-intro.md)
- book/src/L1-L0/amr-estimate-mark-refine.md (edit — AMR THEME FIRM-FLIP rough-in→firm per its stated gate; frontmatter rank + comment, ## Status body, the two L1-form endpoint annotations (now firm live-links), the "Speculative L1 operators"→"L1 operators (harvested firm)" section, trailing ## Status: rough-in→firm)
- scaffolding/open-questions.md (append — 2 NEW OQs; see below)

Gate hits:
- citecheck (--scan over CYCLE.md): 36 ok, 0 failing (bounds + path-hygiene clean) — non-blocking. Re-anchored dorfler.cpp:36 (std::lower_bound pivot), :163 (error_threshold = min_threshold), :167-169 (MFEM_VERIFY) all confirmed verbatim on-disk against reference/palace/palace/utils/dorfler.cpp this invocation.
- graded-stack rank linter: 0 rank violation(s) (CONFIRMED via --json: rank_violations: []). Well-foundedness holds — dorfler_mark firm (rank 3) rests on rank-terminal positive L0 evidence; the amr-estimate-mark-refine theme firm-flip is well-founded (rank = min(flux_recovery_estimate=firm, dorfler_mark=firm) = firm; the refine obstruction leg is a documented boundary that does NOT gate per the theme's own stated gate). firm-on-positive-structure escape correctly applied (no-dedicated-test caveat non-gating per set_subvector_zero/reciprocal precedent).
- unresolved_depends_on_targets: 1 → 0 (CONFIRMED via --json: unresolved_depends_on_targets: []). This D2 landing resolves the SOLE remaining unresolved edge (amr-estimate-mark-refine -> L1/dorfler_mark) — the last of the 2 the c122 cohort opened. The cycle's unresolved-target count is now ZERO.
- SUMMARY.md chapter registration: report PROPOSED the flat entry (repairer already converted to flat) — applied as proposed. grep -c amr-estimate-mark-intro book/src/SUMMARY.md = 0 (no dangling group-intro link). Both flat SUMMARY targets (dorfler_mark.md, flux_recovery_estimate.md) verified on disk this invocation.
- broken-SUMMARY-link check: none (both L1 flat entries resolve on disk).
- AMR THEME FIRM-FLIP disposition: APPLIED — rough-in → firm. The theme's stated gate (## Status :63-69 pre-edit) is "firms to firm when both L1 endpoints are harvested firm; the refine leg is a permanent obstruction (opaque-library-ownership) that does NOT gate promotion." D1 flux_recovery_estimate landed firm in the prior integration (file present on disk, prior staging row); D2 dorfler_mark lands firm now → BOTH constructive endpoints firm → flip fired. The refine leg stays a permanent obstruction sub-leaf (unchanged; ## Sub-pattern C). DISK-OBSERVED: I read flux_recovery_estimate.md present on disk + the theme's depends-on edges (both lowers-to endpoints now resolve to live firm files) this invocation, not assumed from the staging log.
- index-placeholder displacement / forward-edge / variant-axis / H1 / append-on-missing-slug / implied-component-stub / new-summary-kind-grouping-group-intro: n/a (firm chapter authored in full + in-place row flip + flat SUMMARY entry; no placeholder rows; H1 `# dorfler_mark` distinct from page-heading; variant-axis (θ / rank-multiplicity / no-coarsening-axis) explicitly enumerated in the chapter; NO new kind-grouping opened — flat fallback used, group-intro deferred to c123 layer-intro-author per existing OQ amr-estimate-mark-group-intro-needs-authoring).

Open questions promoted:
- record-RefinementData-needs-concept-definition-home (NEW)
- dorfler-coarsening-threshold-sibling-verb (NEW)
- (NOT promoted — already in ledger: dorfler-cross-rank-bisection-distributed-note-deferred [EXISTING; confirmed by this single-rank harvest]; amr-estimate-mark-refine-theme-firmness-gate [EXISTING; DISCHARGED by this landing — both endpoints now firm, theme flipped — but per role-spec I do not edit existing OQ entries; finalize/meta marks resolution]; amr-estimate-mark-group-intro-needs-authoring [EXISTING, c123 layer-intro-author; covers the index.md "Rough-in (AMR estimate/mark vocabulary)" header rename for both verbs + the SUMMARY re-nest]).

Build-relevant: yes

Notes: FINAL report of cycle-122 (D2, dorfler_mark). The two headline outcomes: (1) unresolved_depends_on_targets 1 → 0 — the cycle now has ZERO unresolved depends-on targets (the libceed-substrate row took 6→2, D1 flux-recovery took 2→1, this D2 takes 1→0). (2) AMR theme firm-flip APPLIED rough-in→firm per the theme's own stated two-endpoint gate (refine obstruction leg does not gate; stays a documented boundary). 0 rank violations; firm-flip well-founded. The index.md dep-map group header still reads "Rough-in (AMR estimate/mark vocabulary)" — its rename (drop "Rough-in" now both verbs are firm) is the c123 layer-intro-author's task per the existing OQ amr-estimate-mark-group-intro-needs-authoring (NOT edited here; the group-header rename + SUMMARY re-nest + amr-estimate-mark-intro.md authoring are one coordinated c123 layer-intro-author follow-up, since renaming the header without the group-intro/re-nest would be a partial change). REACHABILITY-GC NOTE (for finalize/meta, NON-blocking): the rank linter flags L1/dorfler_mark + L1/flux_recovery_estimate + L1-L0/amr-estimate-mark-refine [GARBAGE*] under the depends-on-only reachability GC — the SAME pre-existing reference-edge-liveness scheme characteristic the prior c122 staging rows document (the AMR verbs are reachable from the feature roots only via reference-class edges (theme→verb, feature→theme), which the depends-on-only GC does not traverse). 0 new rank violations; this is a batch-39-meta-relevant scheme accounting question (whether reference edges to firm/theme nodes count toward liveness), NOT a defect in this report. Narration from the linter --json I ran this invocation. deferred integrated_at to finalize per role-spec.

---
