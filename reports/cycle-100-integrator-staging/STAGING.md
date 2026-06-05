# Cycle-100 integrator staging log

Per-report integration rows, append-only, newest LAST. Row ORDER is the authoritative apply-order record (NOT the advisory `applied_at` timestamps). integrator-finalize reconciles from this log.

---

## 2026-06-05T044916Z-lowering-verifier-apply-linop-mutation-rotation
applied_at: 2026-06-05T05:02:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/apply-linop-mutation-rotation.md (edit — `## Status` body flipped `rough-in` → `firm` with the firm-on-positive-structure / syntactic-identity escape reasoning; `verified_against:` block replaced with the 23-row corrected payload, incl. the repairer's fresh off-by-one fix in the operator.cpp:428-441 note 438→439 / 439→440, and the three pre-existing drift corrections operator.cpp:509-519→520, rap.cpp:320-360→361, rap.cpp note line 220→219)
- book/src/L1-L0/index.md (edit — dep-map row ~line 21 status column ONLY flipped `rough-in` → `firm *(structural; 5 sub-patterns ...)*`; no other rows touched)
- book/src/L3/apply_linop.md (edit — line 169 coupled re-anchor of stale `apply_linop` "Downward to L_n" cross-ref maturity token `(rough-in; cycle-007)` → `(firm; cycle-007, promoted cycle-100)`)

Gate hits:
- rank-gate (well-foundedness): 0 (firm promotion; both deps firm — `L1/apply_linop` firm cycle-004, L0 rank-3 ground truth; `rank(theme) ≤ min(firm,firm) = firm` holds)
- retroactive-budget: 0
- concept_writes / forward-edge / edge-label / H1 / append-on-missing-slug / variant-axis / SUMMARY-registration / placeholder-displacement / implied-stub: 0 (none triggered; all three target files pre-existing + SUMMARY-registered, status-only flips + coupled re-anchor)
- citecheck bounds + path-hygiene lint: 45 ok, 0 MISS, 0 OOB, 21 AMBIG (NON-blocking) — the 21 AMBIG are basename collisions (`operator.{hpp,cpp}` resolves to both `palace/linalg/` and `palace/fem/libceed/`); the theme's `palace/linalg/` intent is unambiguous from context (confirmed by critic + repairer). No real citation defects.

Open questions promoted:
- apply-linop-mutation-rotation-corpus-census-optional-not-a-gate (optional `search_text 'void .*::Mult'` corpus census to harden the illustrative-corpus ~30-40 estimate; explicitly NOT a promotion gate — surfaced for the planner only)

Build-relevant: yes

Notes: First per-report integrator in cycle-100 (created the staging dir + this log). `overall_status: ready` confirmed in META (set by repairer after fixing the single internal-line off-by-one; checks otherwise pass/repaired/not-needed). This is a `lowering-verifier` firm-promotion of an existing L1>L0 theme — surgical status/cell/token flips on three pre-existing book files, no new files/concepts/SUMMARY entries. The escape application (firm-on-positive-structure / syntactic-identity) was verified sound by the critic. Deferred `integrated_at` (and `integration_commit`) to finalize per role-spec. All edits matched on-disk pre-edit text exactly. I observed only the file states I directly read this invocation (no sibling-landing claims — this is report 1/4, no prior staging rows existed).

---

## 2026-06-05T044840Z-lowering-verifier-ksp-solve-mutation-rotation
applied_at: 2026-06-05T05:05:32Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/ksp-solve-mutation-rotation.md (edit — (1) `## Status` body flipped `rough-in` → `firm` with the firm-on-positive-structure / syntactic-identity escape reasoning + 4-sub-pattern confirmation + cg-residual-quirk-rides-in note; (2) appended the 10 cycle-100 per-step `verified_against:` rows after the last existing row `iterative.cpp:21-32` (CG axpby/dot/converged 440/443/444/460/463, GMRES ApplyBA/Orthogonalize/Givens/write-out 627/630/636-640/703-704, ksp.cpp:310 END close-brace); (3) **safety-net YAML fix**: single-quoted TWO pre-existing unquoted-mid-string-colon note values that broke `yaml.safe_load` — the cycle-007 `case MINRES: case BICGSTAB: ...` note (`ksp.cpp:53-57` row, flagged by report+critic) AND a SECOND pre-existing defect the full-block parse surfaced, the `iterative.cpp:377-386` row `if (this->initial_guess) branch: A->Mult(x, r); ...` note (NOT flagged in the report — found by my post-edit block-parse safety-net))
- book/src/L1-L0/index.md (edit — dep-map row line 36 (`ksp-solve-mutation-rotation`) status column ONLY flipped `rough-in *(firmed cycle-008)*` → `firm *(structural; 4 sub-patterns ...)*`; no other cells/rows touched. D1's edit at line 21 (apply-linop) was already on disk — re-read confirmed line 36 is my target row)

Gate hits:
- rank-gate (well-foundedness): 0 (firm promotion; L1 endpoint `L1/ksp_solve` firm (critic-confirmed `L1/ksp_solve.md:104`), L0 rank-3 ground truth; per-step `apply-linop` is a `reference`/recognition edge per the lowering-verifier, and its OWN staging row this cycle (report 1/4) records it firmed `rough-in→firm` — so `rank(ksp-solve)=firm ≤ min(firm deps)` holds under either edge-typing reading)
- citecheck bounds + path-hygiene lint: 44 ok, 0 failing (0 MISS / 0 AMBIG / 0 OOB) — no citation defects in the report. The repairer-removed false `:42→:41` drift flag was NOT applied (ksp.cpp:42 `SetRestartDim` is line-exact, left untouched per critic+repair instruction)
- verified_against YAML parse (safety-net): block parses clean after BOTH quote fixes — 32 rows total (22 original + 10 appended), `yaml.safe_load` OK; all 10 appended rows present
- concept_writes / forward-edge / edge-label / H1 / append-on-missing-slug / variant-axis / SUMMARY-registration / placeholder-displacement / implied-stub / retroactive-budget: 0 (none triggered; status-only flips + verified_against append on 2 pre-existing SUMMARY-registered book files)

Open questions promoted:
- ksp-solve-firm-rests-on-apply-linop-per-step-reference-edge (WATCH-ITEM for the planner: confirm the per-step apply-linop edge-typing (reference vs depends-on) when the graded-stack type-the-edges campaign reaches the L1>L0 mutation-rotation cohort; de-risked — apply-linop itself firmed this cycle per the prior staging row, so the rank invariant now holds at firm/firm either way)
- (cg-initial-residual-quirk upstream-confirmation portion already open in the ledger as `cg-initial-residual-quirk-palace-bug-flag-lift` sub-OQ, out-of-scope — NOT re-opened; report's bullet 1 (GMRES `:42` re-verified, no action), bullet 4 (token-drift sweep, no residue), bullet 5 (pre-existing YAML defect, resolved by me) needed no OQ)

Build-relevant: yes

Notes: Report 2/4 in cycle-100. `overall_status: ready` confirmed in META (repairer removed the report's sole blocking finding — a false-positive `:42→:41` drift flag that would have corrupted a correct citation; checks otherwise pass/repaired/not-needed). Surgical firm-promotion of an existing L1>L0 theme: status flip + 10-row verified_against append + index status-cell flip. **TWO safety-net YAML fixes** (not one): the report+critic flagged ONE pre-existing unquoted-colon note (`ksp.cpp:53-57` MINRES row); my post-edit full-block `yaml.safe_load` surfaced a SECOND, pre-existing, NOT-report-flagged defect on the `iterative.cpp:377-386` row (`branch: A->Mult...`) — both single-quoted as bounded make-machine-readable fixes since I was editing the YAML block. The block now parses clean. Did NOT touch ksp.cpp:42 (correct per critic+repair). For the apply-linop dep cross-reference: I read D1's prior staging row (report 1/4) which records apply-linop firmed this cycle, and I did NOT need to re-read apply-linop's file for this report's edits — my claim about its firm status is backed by its staging row, not an assumption. Deferred `integrated_at` (and `integration_commit`) to finalize per role-spec. All edits matched on-disk pre-edit text exactly.

---

## 2026-06-05T044919Z-cross-layer-cross-cutter-l4-backend-lowering-completeness
applied_at: 2026-06-05T05:42:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/index.md (edit — TWO mechanical `essential_dofs` mis-attribution repoints: (1) the `fe_assemble` bullet ~line 48, `the three construction inputs (fe_space/fe_collection/essential_dofs) absorb into the readonly construction stratum` → `the two construction inputs (fe_space/fe_collection) absorb ...; essential_dofs is NOT a fe_assemble input — it produces the DofSet[N] consumed by the post-assembly BC cohort (eliminate_essential_bc/eliminate_rhs, L1/essential_dofs.md:22-23,72), L4 disposition open (see OQ bc-elimination-cohort-l4-disposition)`; (2) the `fe_assemble` table row ~line 100 `state-stratification` cell, same `essential_dofs` repoint in the row's slightly-different `three construction inputs fe_space/fe_collection/essential_dofs absorbed` phrasing. Both matched on-disk pre-edit text exactly. NO body-prose sites touched.)

Gate hits:
- retroactive-budget (per-slice / global): 0 (observational survey; the only book change is a 2-site mechanical parenthetical repoint, no retroactive firm/structure rewrite)
- rank-gate (well-foundedness): 0 (no rank promotion in this report — observational; the BC cohort stays where it is, L4-disposition routed to the new OQ)
- concept_writes / forward-edge / edge-label / H1 / append-on-missing-slug / variant-axis / SUMMARY-registration / placeholder-displacement / implied-stub / alpha-position-insert: 0 (none triggered — no new files, no concept pages, no new SUMMARY/dep-map/index rows, no new slugs created; pure in-place text repoint on a pre-existing SUMMARY-registered file. The repoint ADDS a forward-ref to the new OQ slug — an OQ-ledger reference, not a book forward-edge claim, so the forward-edge-without-surface gate does not apply)
- citecheck bounds + path-hygiene lint: 14 ok, 0 failing (0 MISS / 0 AMBIG / 0 OOB) over the report CYCLE.md — no citation defects

Open questions promoted:
- bc-elimination-cohort-l4-disposition (filed as a PROMOTION of the existing c069 sibling-deferral, NOT a brand-new question — provenance L4/fe_assemble.md:119 + L4-L3/fe-assemble-fold-dissolution.md:127; the BC-half analog of the assemble-half closed c068, plan-tag fe-cohort-l4-lift. Carries the recurring-mis-attribution-site note for L4/fe_assemble.md:69,147,175 — the three chapter-body sites deliberately NOT corrected this cycle, to be widened TOGETHER with the OQ's BC-disposition decision)

Build-relevant: yes

Notes: Report 3/4 in cycle-100. `overall_status: ready` confirmed in META (canonical; set by repairer after the surface-or-evidence "undispositioned" overstatement was softened to "deferred-but-undecided" with the c069 citations; all other checks pass/repaired/not-needed). Observational cross-layer survey — high-value EVIDENCE artifact (no large book mutation; the single book change is the producer's mechanical index repoint). 

**FLAG for finalize + meta-phase:** this survey REFUTED the stale memory claim in `project_l4_is_backend_lowering_target` that "the FE-assembly/FE-space cohort stranded at L1 is a hole to close" — on disk the **assemble-half closed at cycle-068** (`L4/fe_assemble.md` firm; FE-space construction constituents `fe_space`/`fe_collection`/`weak_form_term` carry an explicit on-disk no-L4-by-design verdict; `assemble_frequency_operator` firm L4 c069). The memory is stale by ~30 cycles. The real remaining FE-cohort hole is narrowed to the BC-elimination cohort (the new OQ). RECOMMEND meta-phase refresh `project_l4_is_backend_lowering_target` to re-scope its named hole from "FE-assembly/FE-space stranded at L1" to "BC-elimination cohort L4-disposition open" (cross-cutter Recommendation item 3, deferred to meta-phase). The survey also confirmed all 5 solver pipelines + all 5 output-products reach firm L4 feature surfaces.

Did NOT widen the mechanical correction to the three `L4/fe_assemble.md` chapter-body sites (`:69,:147,:175`) per the repairer's explicit scoping decision (they sit in combinator-as-entry body prose, best fixed with the BC-disposition decision); recorded that recurring-site note in the new OQ instead, so it travels with the eventual resolution.

Deferred `integrated_at` (and `integration_commit`) to finalize per role-spec. All edits matched on-disk pre-edit text exactly. On sibling state: I read the 2 prior staging rows (reports 1/4 + 2/4 — apply-linop + ksp-solve L1>L0 firm promotions, disjoint files); they do not touch L4/index.md or the OQ ledger sections I edited, so no re-read conflict. I narrate only file state I directly observed this invocation.

---

## 2026-06-05T045201Z-same-layer-cross-cutter-class-b-slice-residue-cleanup
applied_at: 2026-06-05T05:30:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/krylov-step.md (edit — REPOINTED the 2 bare dead-slice pointers, lines 255-256 pre-edit: (1) GMRES L4 `inner_loop` `gmres.md:459-471` → absorbed-into-Form-A + L0 ground [`ksp-solve-mutation-rotation`] §"Sub-pattern C" (`iterative.cpp:543-705`) + loop-migration home [`gmres-inner-loop-iterate-while-migration`]; (2) `arnoldiStep` `arnoldi_step.md:285-298` → absorbed-into-Form-A + orthogonalization constituent L0 [`orthogonalize-mutation-rotation`] (`orthog.hpp:41-88`, MGS 41-53 + CGS 57-74 + refine 75-88 named inline, the repairer-widened span). Both deleted-slice paths replaced with git-history provenance.)
- book/src/L4/chebyshev.md (edit — STRUCK dead `spec/slices/chebyshev.md` §L4 path :287-439, kept narrative + git-history record)
- book/src/L3/chebyshev.md (edit — STRUCK dead §L3 path :229-285)
- book/src/L2/chebyshev-iteration.md (edit — STRUCK dead §L2 path :122-228)
- book/src/L1/chebyshev-smoother.md (edit — STRUCK dead §L1 path :34-116; `rho_0` correction note preserved)
- book/src/L2/index.md (edit — line 133 STRUCK `spec/slices/chebyshev.md:354-362` innerStep path → "former Phase-1 chebyshev §L4 innerStep, deleted cycle-099")
- book/src/L3/index.md (edit — TWO occurrences: line 53 chebyshev dep-map-row provenance + line 99 narrative-bullet, both STRUCK `spec/slices/chebyshev.md` → "reduced cycle-015, deleted cycle-099; git history is the record")
- book/src/L1/orthogonalize.md (edit — line 299-301 LIGHT NORMALIZATION of the already-"(now-deleted)" `spec/slices/orthog.md` provenance to standard git-history phrasing; already cited L0 directly, no re-citation needed)

Disposition tally (matches report): repointed 2 pointers (both in L4/krylov-step.md) | struck 6 pointers (chebyshev cohort L1/L2/L3/L4 + L2/index:133 + L3/index lines 53+99) | normalized 1 (L1/orthogonalize) | left-untouched 2 (L1-L0/triangular-solve-obstruction.md:339 Related-narrative + :533 frozen audit-YAML — both already document their own cycle-097 deletion; striking would damage provenance; correctly out of scope).

Gate hits:
- broken-markdown-link / forward-edge-without-surface: 0 — all 3 repoint targets exist on disk (ksp-solve-mutation-rotation.md, gmres-inner-loop-iterate-while-migration.md, orthogonalize-mutation-rotation.md verified present); §"Sub-pattern C" anchor confirmed in ksp-solve-mutation-rotation.md:371; no LIVE markdown link to any `spec/slices/` path remains in the 8 edited files (grep clean). The new arnoldi L0 range `orthog.hpp:41-88` in-bounds (file=93 lines).
- citecheck bounds + path-hygiene lint (over CYCLE.md, --scan): 15 ok, 5 failing — ALL 5 failing (2 OOB-resolving-to-concepts/gmres.md + 3 MISS on spec/slices paths) are the dead-slice OLD-string text the report is STRIKING, NOT landed-text defects. The NEW (landed) text uses plain-text source-range citations to live Palace files (iterative.cpp:543-705, orthog.hpp:41-88) which resolve fine. NON-blocking: the failing hits ARE the deletion targets.
- retroactive-budget (per-slice/global) / concept_writes / edge-label / H1 / append-on-missing-slug / variant-axis / SUMMARY-registration / alpha-position-insert / placeholder-displacement / implied-stub / rank-gate: 0 (none triggered — pure plaintext repoint/strike on 8 pre-existing SUMMARY-registered firm chapters; no new files, no concepts, no SUMMARY/dep-map/index ROW additions, no status flips, no new slugs, no Mermaid edge edits)

Open questions promoted:
- dependency-map-cg-precond-stale-mermaid-edges-RESCOPE-CORRECTION (premise correction + re-scope of the existing ledger OQ at line ~1457: NO literal `cg_preconditioning_framework` Mermaid node exists; the ~40 stale edges are keyed on deleted krylov-trio slugs gmres/orthog/arnoldi_step/cg/etc. Appended as a NEW superseding section — left the existing entry intact per append-only authority for the meta-phase to unify. FLAG for cycle-planner/meta-phase to fold the corrected premise into the plan item.)
- concepts-index-and-depmap-orchestrator-era-framing-refresh (concepts/index.md + concepts/dependency-map.md carry whole-file pre-redirect orchestrator/slice-era framing; recommend a dedicated layer-intro-author dep-map/concepts refresh next cycle = batch-32 plan candidate, natural pairing with graded-stack typed-edge campaign priorities #0; carries the adjacent L4/krylov-step.md:254 CG-Form-B residue note for the same refresh)

Build-relevant: yes

Notes: Report 4/4 in cycle-100 (last per-report before finalize). `overall_status: ready` confirmed in META — canonical token, set by repairer after the single warning-severity citation-precision nit was repaired (arnoldi L0 range widened `orthog.hpp:41-74` → `41-88` to be a single in-file span covering all three sub-patterns incl. the refine block, matching the absorb-home's own line-map). All other checks pass/repaired/not-needed. All 8 OLD-strings matched on-disk pre-edit text exactly (re-read each before editing). Per the planner overlap analysis + my own check, none of D4's 8 files overlap the prior 3 staging rows' targets (D1=apply-linop L1-L0/* + L3/apply_linop.md; D2=ksp-solve L1-L0/* + index.md; D3=L4/index.md) — I re-read each target region fresh anyway and observed only the file states I directly read this invocation (no sibling-landing assumptions). The CG Form B pointer at L4/krylov-step.md:254 (`spec/slices/cg.md:27-141`) is pre-existing residue the report deliberately left OUT of scope (it carries its own live link + L0 ground + narrative framing); recorded it in the concepts-refresh OQ for the eventual coherent refresh rather than half-editing here, per the cross-cutter "don't half-edit a legacy artifact" posture. Did NOT touch the 2 triangular-solve-obstruction.md pointers (correctly historical). Deferred `integrated_at` (and `integration_commit`) to finalize per role-spec. No book rebuild, no commit (finalize's job).

---
