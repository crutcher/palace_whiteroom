# Cycle-099 integrator staging log

Per-report integration staging for cycle-099 (batch-31 P2 slice-deletion campaign — krylov-trio completion). One row per `integrator-per-report` dispatch, appended serially (newest LAST, append-only). Row ORDER is the authoritative apply-order record; `applied_at` timestamps are advisory only. `integrator-finalize` reads this log to reconcile the cycle, rebuild the book, and do cycle-end housekeeping.

---

## 2026-06-05T010427Z-harvester-cg-unrolling-absorb-L4-krylov-step
applied_at: 2026-06-05T013525Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/krylov-step.md (Edit 1: inserted `### Worked example — CG Form B (v0.5 first-iteration-unrolling)` subsection under Form B §Semantics — CG-concrete `cg_first_step`/`cg_steady_step` typed bodies + `cg_solve` driver with `iterate_while_with_prev` + `forget_beta_prev` projection + v0.4↔v0.5 equivalence + pcg variant + L0-ground prose; AND re-anchored the §Semantics line-82 paragraph off its dangling `cg.md:*` slice-pointers. Edit 2: re-anchored §Status line-152 reference. Edit 4: re-anchored §Evidence line-171 bullet. Edit 3 was folded into Edit 1 per the report.)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- SUMMARY.md chapter registration auto-fix: 0 (no new file created; pure in-chapter edit)
- alphabetical-position insert: 0 (no SUMMARY/index row added)
- index-placeholder displacement: 0
- implied-component stub materialization: 0
- graded-stack rank-gate (rank(u) ≤ min over depends-on deps): PASS — see Notes
- citecheck bounds + path-hygiene lint: 33 ok, 4 failing — see Notes (none blocking)

Open questions promoted:
- cg-slice-27to141-fully-homed-clear-to-delete-and-evidence-pointer-residue-class-B

Build-relevant: yes

Notes:
- `overall_status: ready` confirmed canonical (set by repairer after clean repairs: citation-validity + cross-reference-integrity both `repaired`, all others pass/not-needed). Applied as-is, no normalization needed.
- All four edit anchors verified against on-disk state this invocation (file was untouched earlier this cycle — I am the first per-report integrator of cycle-099). §Semantics line-82 paragraph, §Status line-152, §Evidence line-171 bullet all matched verbatim before editing.
- GRADED-STACK RANK-GATE PASS confirmed (per dispatch directive): the new firm worked-example subsection introduces NO `depends-on` edge to a rough-in node. Its L0 ground is a rank-exempt `cites-evidence` edge to `reference/palace/palace/linalg/iterative.cpp:360-486` (ground-truth C++). The link to `book/src/L1-L0/ksp-solve-mutation-rotation.md` (on-disk status `rough-in`) is a navigational `reference`-class edge, which does NOT constrain rank. No `depends-on`/`edges:` frontmatter block is present or proposed (verified by grep in repairer's META rank-safety section). The chapter's rank stays 0 (firm); firm-on-positive-structure escape correctly applied (syntactic L4-self-rotation identities on the `CgSolver::Mult` read closure, no convergence-semantics claim gated).
- citecheck `--scan` on the report's CYCLE.md: 33 ok / 4 failing. NONE blocking and none on a live inserted artifact claim: (1+2+3) three `[AMBIG]` lines (`krylov-step.md:28-33`, `krylov-step.md:118`, `gmres.md:459-471`) are bare-basename mentions in the report's PROSE — the inserted artifact text uses full-path `[link]`s; (4) `[OOB] cg.md:393-425` is the deliberate historical "pre-reduction range" provenance breadcrumb the report repeatedly labels as formerly-cited (CYCLE.md:40/169/174), not a live claim. No MISS, no AMBIG/OOB on a live inserted citation → non-blocking per the gate spec.
- Non-duplication-vs-concept-page verified by the critic: `concepts/first-iteration-unrolling.md:21-37` carries the ABSTRACT generic rotation only; the inserted subsection lands ONLY the CG-concrete bodies + equivalence + pcg-variant and cross-references the concept page rather than restating it.
- Class-B plain-text-mention residue: after D2 deletes `cg.md` this cycle, the §Evidence plain-text pointers `gmres.md:459-471` (line 172) and `arnoldi_step.md:285-298` (line 173) plus the historical `cg.md:393-425` parenthetical become stale-but-harmless plain-text provenance (NOT live `[link]`s — `linkcheck2` does not error on them). Tracked for the batch-31 meta-phase §Intake→plan migration. Recorded in the promoted OQ.
- `book/src/spec/slices/cg.md:27-141` is now FULLY HOMED and clear-to-delete; the slice delete + SUMMARY/spec-index repoint is D2's job THIS cycle (out of this single-file CG-only dispatch's scope). The four working-note OQs at `cg.md:18-23` should be migrated to scaffolding by D2 before the file is removed.
- deferred integrated_at to finalize per role-spec (did not touch the consumed report's frontmatter).

---

## 2026-06-05T010427Z-harvester-krylov-trio-hub-repoint-delete
applied_at: 2026-06-05T014455Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2-L1/incremental-least-squares-composition-lowering.md (Edit — Step 3: arnoldi plane-rotation end-bound reconcile `iterative.cpp:73-118 → :73-109`)
- book/src/L2/krylov-step.md (8 Edits — Step 1a: §Context :7 surgical clause-drop + §Semantics :69, variant-axis :119, §Evidence/outer-driver :138/:139/:141/:146/:147 slice-range parentheticals repointed to firm L0 homes)
- book/src/L2/index.md (2 Edits — Step 1a repaired-path blocks: :129 Consumed-by note + :131-134 pattern-instances sub-list)
- book/src/L3/krylov-step.md (10 Edits — Step 1b: :93/:158 obstruction→concept, :123 restart→L0 Sub-pattern C, :188/:189/:196/:197/:199/:204/:205 evidence/driver repoints)
- book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (3 Edits — Step 1c: :231/:232/:233)
- book/src/L4-L3/iterate-while-dissolution.md (2 Edits — Step 1d: :120/:155)
- book/src/L4-L3/iterate-while-with-prev-dissolution.md (6 Edits — Step 1e: :124/:130/:138/:142/:174/:182)
- book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md (3 Edits — Step 1f: :11 prose body + :176/:179)
- book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md (1 Edit — Step 1f: :166)
- book/src/L3-L2/krylov-step-body-identity.md (3 Edits — Step 1g: :125/:126/:128)
- book/src/L1/orthogonalize.md (1 Edit — Step 1h :306)
- book/src/L1-L0/minres-iteration.md (1 Edit — Step 1i :144)
- book/src/L3/apply_linop.md (3 Edits — Step 1j: :186/:187/:189)
- book/src/L4/iterate-while.md (2 Edits — Step 1k: :229/:230)
- book/src/L4/iterate-while-with-prev.md (1 Edit — Step 1l :233)
- book/src/concepts/nrm2.md, dot.md, axpy.md, apply_BA.md, scal.md, apply_linop.md, orthogonalization.md, variant-absorption.md, plane-rotation-stream.md, state-stratification.md, solve-monad.md, gmres.md, constructed-operators.md (×2), derived-view-hoisting.md, first-iteration-unrolling.md (×2) (Step 2: 25 Class-A markdown-link repoints → firm `L2/krylov-step.md` / L2/L1/L0 homes)
- book/src/L0/ksp-factory-file.md (Edit — Step 2: the two-link line → firm L2/L1 homes)
- book/src/SUMMARY.md (Edit — Step 5a: removed the entire `# Phase 1 corpus` Part — header + Index parent link + 3 slice children)
- book/src/introduction.md (Edit — Step 5b: removed the now-dangling `[Specification → Slice Status](./spec/index.md)` nav bullet)
- book/src/spec/slices/cg.md (DELETE — Step 4)
- book/src/spec/slices/gmres.md (DELETE — Step 4)
- book/src/spec/slices/arnoldi_step.md (DELETE — Step 4)
- book/src/spec/index.md (DELETE — Step 5c; producer option-(a) full removal, corpus empty)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- SUMMARY.md chapter registration auto-fix: 0 (this report REMOVES SUMMARY rows, does not add; alpha-position-insert N/A)
- index-placeholder displacement: 0
- implied-component stub materialization: 0
- graded-stack rank-gate (rank(u) ≤ min over depends-on deps): PASS — see Notes
- graded-stack reachability-GC (slice corpus 3→0): PASS — see Notes
- citecheck bounds + path-hygiene lint: 56 ok, 45 failing — see Notes (NONE blocking; all on removed/historical slice strings)

Open questions promoted:
- krylov-trio-slice-corpus-3to0-campaign-complete-retire-carveout-and-skill
- krylov-trio-class-B-plaintext-mention-residue-batch31-cleanup

Build-relevant: yes

Notes:
- `overall_status: ready` confirmed canonical (set by repairer after clean repairs: cross-reference-integrity `repaired`, all others pass/not-needed). The repair corrected two `edit:` block file-path labels (`L2/krylov-step.md` → `L2/index.md`) and softened an overstated Class-B completeness claim. Applied as-is, no normalization needed.
- ALL 67 edit-block anchors verified against on-disk state THIS invocation before editing (re-read each target file; D1 had only touched `L4/krylov-step.md`, which this report does NOT touch — confirmed). The two repaired `L2/index.md` blocks matched at lines 129 + 131 as the repairer determined. The arnoldi reconcile anchor matched at `incremental-least-squares-composition-lowering.md:112`.
- LOAD-BEARING inbound-link sweep PASSED on the REAL applied tree (post-delete): `grep -rnE '\]\([^)]*slices/(cg|gmres|arnoldi_step)\.md' book/src --include='*.md'` → ZERO; `grep -rnoE '\]\([^)]*spec/index\.md\)' book/src --include='*.md'` → ZERO. No `linkcheck2` hard error will occur on the deletions. (Before the deletes, the only surviving `slices/` link matches were the 3 rows INSIDE `spec/index.md` itself, which was then deleted in 5c.)
- GRADED-STACK: ran `tools/graded-stack-lint/graded_stack_lint.py` post-apply → **0 rank violation(s)**, exit 0. This report introduces NO `depends-on` edges and NO rank promotions (pure detritus-GC + citation-rehoming + deletion), so the rank invariant is structurally unaffected. The 3 slices were reachability-GC-unreachable (no inbound `depends-on` edge), so their deletion is clean GC. The 172-detritus / 142-untyped warnings are the pre-existing type-the-edges-campaign baseline, unrelated to this report. **Slice corpus 3→0; the campaign's mechanical-completion criterion (GC-unreachable + rank invariant holds + zero slice nodes) is MET.**
- `spec/` now contains only empty directories (`spec/`, `spec/slices/`) — harmless to git (untracked) and mdBook (only SUMMARY-referenced files are processed). Producer chose option (a) full removal; corpus empty.
- CITECHECK `--scan` on the report's CYCLE.md: 56 ok / 45 failing. NONE blocking and NONE on a live INSERTED citation. All 45 failures are on `cg.md`/`gmres.md`/`arnoldi_step.md`/`spec/slices/*` strings that appear ONLY in the `[old_string]` halves (the text being REMOVED) + the historical "Original pre-reduction slice ranges" provenance breadcrumbs in the report's prose; the `[OOB] gmres.md:*` entries are bare-basename AMBIG-collisions resolved to `book/src/concepts/gmres.md` (23 lines), not live inserted citations. The 4 key INSERTED L0 ranges (`iterative.cpp:543-705`, `:563-683`, `:73-109`, `:360-486`) all resolve `[ok]` in-bounds (882-line file) — separately checked. Non-blocking per the gate spec (no MISS/AMBIG/OOB on a live inserted artifact claim).
- All Class-A repoint targets verified present on disk: `L2/krylov-step.md`, `L4/krylov-step.md`, `L2/ksp_solve.md`, `L1/ksp_solve.md`, `concepts/sequential-obstruction.md`, `L1-L0/ksp-solve-mutation-rotation.md`. Per critic issue 3, the prose `§"MGS as sequential-obstruction"` references were left as prose (on-disk heading is `## Example: MGS as sequential-obstruction`); I did NOT convert them to a broken `#mgs-as-sequential-obstruction` fragment link.
- Campaign-COMPLETE flag (corpus 3→0) promoted to the OQ ledger for integrator-finalize / batch-31 meta-phase: retire the `annotated-and-retained` carve-out + skill `phase-1-slice-reduction-audit`. Residual ~50 Class-B plain-text mentions (stale-but-harmless, meta-reviews-convention KIND) promoted as a separate tracked follow-up OQ for the batch-31 §Intake→plan migration (dedicated batch-32 cleanup vs accept-as-historical).
- deferred integrated_at to finalize per role-spec (did not touch the consumed report's frontmatter).

---

## 2026-06-05T010427Z-lifter-bilinear-form-c095-residue-sweep
applied_at: 2026-06-05T015830Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied (no-op)

Files touched:
- (none — verified clean no-op; report's `## Proposed changes` = NONE)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- SUMMARY.md chapter registration auto-fix: 0 (no file created)
- alphabetical-position insert: 0 (no SUMMARY/index row added)
- index-placeholder displacement: 0
- implied-component stub materialization: 0
- graded-stack rank-gate (rank(u) ≤ min over depends-on deps): N/A — no edges added, no promotions; rank unchanged (stays 0/firm for both flipped operators)
- graded-stack reachability-GC: N/A — no nodes added or removed
- citecheck bounds + path-hygiene lint: 29 ok, 0 failing — clean

Open questions promoted:
- bilinear-form-c095-residue-sweep-clean-noop-and-L2-index-89-confirmed-non-stale

Build-relevant: no

Notes:
- `overall_status: ready` confirmed canonical — set DIRECTLY by the critic per the all-pass clean-report rule (META.md:14 `overall_status: ready`; META.md:106 "verified no-op land; `overall_status: ready` set per the all-pass clean-report rule"). No repairer ran (all 8 checks pass on a clean report); accepted as-is, no normalization needed.
- VERIFIED CLEAN NO-OP. The report's `## Proposed changes` section (CYCLE.md:132-139) is literally "NONE". The whole-book residue sweep for the cycle-095 `bilinear-form` firm-flip cascade found ZERO genuinely-stale instances outside the krylov hub — all 32 surviving `gram_reduce`/`bilinear-form` ⨯ `rough-in` co-mentions are correct post-cascade narration (promotion provenance / deliberate-historical worked-example-arc / immutable OQ-slug / FE-assembly slug-collision / different-operator rough-in). No artifact edit applied; bookkeeping only.
- `L2/index.md:89` OQ RESOLVED as NON-stale, re-confirmed on disk THIS invocation: I read book/src/L2/index.md:88-90 directly and observed line 89 reads "`bilinear-form` (M-weighted member, **firm** — promoted cycle-095)" — correct post-cascade narration of the now-firm L1/bilinear-form as the M-weighted `inner_product` leaf. D2's staging row (this cycle) lists L2/index.md edits at rows :129 and :131-134 only; :89 was NOT among D2's edits and was already correct on disk. No stale maturity assertion; no edit needed. (Narration backed by on-disk read + D2's staging row, not by assumption.)
- GRADED-STACK: no artifact change → rank stays 0 for both flipped operators (`gram_reduce` firm, `bilinear-form` firm; both `rank: firm` confirmed in the report's on-disk frontmatter paste, CYCLE.md:36-64). No `depends-on` edge added, no promotion proposed; rank-gate is a confirm-not-edit. Baseline rank-violation count unaffected.
- citecheck `--scan` on the report's CYCLE.md: 29 ok / 0 failing, exit 0 (clean — the report cites only on-disk firm-frontmatter ranges + valid book paths). Non-blocking.
- deferred integrated_at to finalize per role-spec (did not touch the consumed report's frontmatter).

---
