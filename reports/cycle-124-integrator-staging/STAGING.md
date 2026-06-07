# Integrator staging log — cycle-124 (batch-40 OPENER)

Per-report integration staging for cycle-124, the first cycle of batch-40 (cycles 124/125/126;
meta-phase fires after 126). Each `integrator-per-report` invocation appends one row below
(newest LAST; **row ORDER is the authoritative apply-order record**, NOT the `applied_at`
timestamps). `integrator-finalize` reads this log to reconcile the cycle (rebuild book, commit,
mark `integrated_at`, write cycle-record/log, resolve any `deferred` rows).

**Dependency-ordering plan (from the cycle-124 planner):**
- **D1 → D2** — D1 (this report) is the LEAD: lands the `nleps-deflated-eigensolve` L3
  composition-root, fires RE3 + grounds RE11 nodes. D2 (lowering-verifier) audits D1's wiring
  (the `eigsolve-impl → eigsolve` `realizes-kernel-api` edge stays `reference`-class; the impl↔api
  correspondence; D1's `depends-on` edges to `eigsolve-impl`/`deflate`/`gram` are faithful).
- **D3 → D4 → D5** — a dependent chain.
- **D6** — independent.
- **D7** — independent.

**Batch-40 forward-direction context (ASK-2, "A then B"):** finish the constructive-kernel layer
(element-local rank-tensor / matrix-free assembly) THEN a 5-driver L4-completeness audit capstone;
fold in D (P1 edge-typing / true-detritus sweep) opportunistically. This cycle's D1 advances the
constructive-kernel front by building the deflate/NLEPS consumer that grounds the eigsolve kernel-impl cohort.

---

## 2026-06-07T112037Z-harvester-deflate-nleps-consumer
applied_at: 2026-06-07T120500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3/nleps-deflated-eigensolve.md (created — new L3 composition-root chapter, status/rank roadmap_goal)
- book/src/L3/index.md (dep-map ROW inserted in "Solver capabilities & field transitions" grouping, alpha position between `lanczos_step` and `orthogonalize`; §Vocabulary-cohort bullet reworded to add the two kernel-impl roadmap_goals + this composition-root)
- book/src/SUMMARY.md (chapter entry inserted in L3 "Solver capabilities & field transitions" sub-group, alpha position between `lanczos_step` and `orthogonalize`)
- scaffolding/open-questions.md (append-only — 2 OQ sections promoted, see below)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (finalize sees the full staging log — only D1 row so far)
- concept_writes on existing slug: 0 (new slug)
- forward-edge claim without surface: 0 (all 14 link targets verified on disk)
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (4 variant axes declared in frontmatter + §Signature)
- bookkeeping incomplete: 0
- SUMMARY chapter registration auto-fix: 0 (report proposed the SUMMARY edit explicitly; applied as-given, alpha-correct)
- alphabetical-position insert: applied-as-specified (report specified the alpha position for both the index dep-map row and the SUMMARY entry — no integrator discretion needed)
- citecheck bounds + path-hygiene: 49 ok, 1 failing — the lone `[MISS] graded-stack-baseline-exceptions.md:199` is a documented tool-scope FALSE POSITIVE (citecheck searches reference/* + book/src, NOT scaffolding/). The file exists (213 lines); :199 (RE3 promotion condition) and :209 (RE11 cohort) were content-verified on disk this invocation. NOT a real MISS/AMBIG/OOB — no repair/defer needed.
- rank gate (§(h) well-foundedness): PASS — consumer lands roadmap_goal (rank 0); blocking depends-on deps include eigsolve-impl (rank 0); rank(consumer)=0 ≤ min(deps)=0 holds. No firm-flip over a sub-firm dep.

Open questions promoted:
- nleps-deflated-eigensolve-nev-config-vs-runtime-loop-bound-split
- nleps-deflate-gram-typed-frontmatter-edge-on-deflate-chapter

Build-relevant: yes

Notes:
- **RE3 FIRED + RE11 GROUNDED — track for finalize/meta.** This report wires the faithful blocking
  `depends-on (composes)` edges that (a) FIRE **RE3** (`graded-stack-baseline-exceptions.md:199` —
  the `deflate → L2/gram` faithful constituent edge becomes reachable through a built consumer) and
  (b) GROUND **`L3/eigsolve-impl` + `L3/lanczos_step`** off the RE11 reference-only-reachable cohort
  (`:209`) — this consumer is the first faithful `depends-on` consumer of `eigsolve-impl` (direct)
  and `lanczos_step` (transitive via eigsolve-impl's `folds` edge). The finalize/meta should
  re-check the RE3 / RE11 baseline-exception rows against the rebuilt graph (the reachability-GC /
  graded-stack-lint may now confirm the discharge; if so, the RE3 row + the eigsolve-impl/lanczos_step
  RE11 entries can be marked discharged in `scaffolding/graded-stack-baseline-exceptions.md` — that
  is meta-phase write-territory, flagged here for the batch-40 meta).
- The landed chapter rank is `roadmap_goal` BY DESIGN (the §(h) cap from the rank-0 eigsolve-impl
  seed), NOT a failed discharge — the grounding lands independent of the chapter's own rank because
  liveness flows over `depends-on` regardless of rank. Do not read the roadmap_goal rank as an
  incomplete discharge.
- D2 (lowering-verifier) is dispatched after this to audit the wiring (per the dep-ordering plan).
- The `realizes-kernel-api` / `folds` / `composes` / `pulled-by-root` edge `kind:` sub-labels in the
  new chapter's frontmatter are documentation the linters ignore (optional-kind mechanism) — no new
  linter edge-semantics introduced.
- Several of the report's Open-questions/caveats were dispatch-coordination notes (the rank-cap-is-
  not-a-failed-discharge note for the integrator; the D2-audits-the-wiring note; the lanczos_step-is-
  reference-not-depends-on chain note) — those are captured here in Notes / the gate rows rather than
  re-filed as ledger OQs (they are not standing cross-cycle questions). The 2 promoted OQs are the
  genuinely forward-looking caveats (nev config/run-time split; the deflate→gram typed-frontmatter-edge
  follow-up).
- deferred integrated_at to finalize per role-spec (per-report integrator does NOT touch the consumed
  report's frontmatter; integrated_at + integration_commit are finalize-only).

---

## 2026-06-07T112037Z-lowering-verifier-eigsolve-impl-correspondence
applied_at: 2026-06-07T115421Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3/nleps-deflated-eigensolve.md (block A — FRESH `verified_against:` fenced YAML block appended at end of file; 5 entries; D1's consumer chapter had none)
- book/src/L3/eigsolve-impl.md (block B — ONE list entry INSERTED into the existing `verified_against:` block, after the arpack.cpp:369 entry's note, before the closing fence; block now 8 entries)

Gate hits:
- retroactive-budget per-slice: 0 (audit-kind, retroactive-evidence backfill — two verified_against blocks, no content/rank change)
- retroactive-budget global: 0 (finalize sees the full staging log; D1 + this D2 row so far)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0 (consumer chapter on disk from D1; eigsolve-impl pre-existing)
- variant-axis missing on multi-variant operator: 0 (no operator/theme authored)
- bookkeeping incomplete: 0
- SUMMARY chapter registration auto-fix: 0 (no new chapter created; no SUMMARY change)
- alphabetical-position insert: n/a (no SUMMARY/index row added)
- YAML well-formedness (verified_against round-trip): PASS — both blocks `yaml.safe_load`-clean on disk (consumer chapter: 1 fenced block, 5 entries; eigsolve-impl: 1 fenced block, 8 entries). No leading-quote scalar fault.
- insertion-anchor match on-disk: PASS — block A appended cleanly at EOF (no prior verified_against block confirmed by grep); block B inserted after the arpack.cpp:369 note (was line 190) before the closing ``` fence (was line 191), matching the report's anchor instruction exactly.
- citecheck bounds + path-hygiene: 10 ok, 3 failing — all 3 BENIGN, none on a load-bearing source citation: two are report-to-report self-refs (`[MISS] CYCLE.md:121`, `CYCLE.md:31` — cycle-planner provenance pointers, not Palace citations) and one is `[AMBIG] eigsolve.md:104` (basename collision resolving unambiguously to book/src/L3/eigsolve.md by context). Every load-bearing nleps.cpp/slepc.cpp pinpoint anchor-`[ok]`. No real MISS/AMBIG/OOB — no repair/defer needed.

Open questions promoted:
- (none — all 3 §Open-questions caveats already covered in the ledger or are GC-time notes; see Notes)

Build-relevant: yes

Notes:
- **Both proposed-changes applied as-specified.** Block A = a FRESH `verified_against:` block on D1's
  consumer chapter (`nleps-deflated-eigensolve.md`) — D1 authored no such block, confirmed by grep
  this invocation; appended at EOF. Block B = a SINGLE list entry inserted into the PRE-EXISTING
  `verified_against:` block in `eigsolve-impl.md` (the c122 structural-correspondence audit), placed
  after the last existing entry (arpack.cpp:369) and before the closing fence per the report's anchor.
  No second fenced block created (the report explicitly warns against it). No content/rank/status edits.
- **No rank-gate action.** This report proposes NO promotions and NO new depends-on edges — only audit
  evidence blocks. D2 explicitly preserves `eigsolve-impl` at `roadmap_goal` (D1 did not promote) and
  the kernel-api `L3/eigsolve` at `partial-obstruction`. Verdict was edge-integrity PASS +
  consumer-faithfulness PASS (per CYCLE.md + META.md). Nothing to block.
- **OQ disposition.** The 3 §Open-questions caveats are NOT new standing cross-cycle questions:
  (1) empirical-match-deferred-to-firming is the EXISTING OQ `eigsolve-impl ↔ kernel-api correspondence`
  (open-questions.md:1715) — D2 discharges its STRUCTURAL portion, empirical-match stays deferred to
  firming per that OQ; (2) the deflate/gram typed-frontmatter-edge follow-up was already promoted by D1
  (`nleps-deflate-gram-typed-frontmatter-edge-on-deflate-chapter`, open-questions.md:1920); (3) the
  `lanczos_step` transitive-grounding "does the reachability-GC linter walk the chain" note is a
  GC-execution question the report itself routes to integrator/meta at GC time — captured here, not
  re-filed as a standing OQ.
- **RE3 / RE11 (flagged for finalize/meta, NOT re-modified here).** This D2 audit CONFIRMS (does not
  itself fire) D1's RE3-fired / RE11-grounded disposition: edge-class integrity holds (the
  `realizes-kernel-api` edges stay `reference`-class, re-confirmed on disk at eigsolve-impl.md:19-23 by
  the report + critic), and the new consumer's `depends-on` edges to eigsolve-impl/deflate/gram are
  faithful constituent-use. Whether the reachability-GC linter actually marks lanczos_step live over the
  transitive chain is the GC-time confirmation for finalize/meta (graded-stack-baseline-exceptions.md is
  meta-phase write-territory; flagged, not touched).
- deferred integrated_at to finalize per role-spec (per-report integrator does NOT touch the consumed
  report's frontmatter; integrated_at + integration_commit are finalize-only).

---

## 2026-06-07T112037Z-harvester-basis-apply-quad-contract
applied_at: 2026-06-07T123500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/basis_apply.md (full-file replace — roadmap_goal → firm; rank: firm; +concepts/element-local-tensor reference edge; stale design/l4_calculus.md §1.2.1 → live semantics/index.md §1.2.1; repaired EvalMode pinpoints :41/:49)
- book/src/L1/quad_point_contract.md (full-file replace — roadmap_goal → firm; rank: firm; +concepts/element-local-tensor reference edge; stale path fix; re-anchored apply-QFunction citations :457-458/:462/:492/:493, f_apply_22 :260, integrator.cpp:451-495 + :423-445)
- book/src/L1/index.md (in-place maturity flips ONLY: 2 §Vocabulary-cohort bullets roadmap_goal→FIRM + 2 dep-map rows roadmap_goal→firm; distinct rows, NO consolidated firm-count tally / cohort-header touch — DEFERRED to D5)

Gate hits:
- retroactive-budget per-slice: 0 (maturity-flip, not retroactive evidence backfill)
- retroactive-budget global: 0 (finalize sees full staging log — D1 + D2 + this D3)
- concept_writes on existing slug: 0 (no concept page authored here; concepts/element-local-tensor is D5's)
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0 (all frontmatter edges reference-class; prose matches B/Bᵀ-around-D, D-consuming-B's-shape)
- H1 reuses page heading: 0
- append on missing slug: 0 (both chapters pre-existing roadmap_goal since c122 D4)
- variant-axis missing on multi-variant operator: 0 (basis_apply covers all 4 BasisMode/EvalMode + de-Rham family; quad_point_contract covers mass vs grad-grad block-shape)
- bookkeeping incomplete: 0
- SUMMARY chapter registration auto-fix: 0 (no new chapter; both registered since c122 D4 — maturity flip in-place, no SUMMARY change, per planner overlap note)
- alphabetical-position insert: n/a (in-place flips, no new rows)
- citecheck bounds + path-hygiene: 20 ok, 3 failing — all 3 [AMBIG] basename collisions (integrator.{cpp,hpp} exist under both palace/fem/ AND palace/fem/libceed/); the report's prose disambiguates with the full palace/fem/libceed/ path everywhere, so these clear on full paths (critic confirmed via --anchor; I re-confirmed the repaired pinpoints :41/:49 on the full path via codemap read_range). NO MISS/OOB. Non-blocking false-positive of --scan basename-stripping.
- rank gate (§(h) well-foundedness): PASS — both ops flip to firm (rank 3); neither frontmatter carries a depends-on edge (only reference-class: pulled-by / weak_form_term / element-local-tensor / geom_factor_build / tensor-field-lift), so no blocking dep constrains the firm flip; firm-on-positive-structure escape governs (syntactic-identity laws on read-not-constructed positive libCEED source). No firm-flip over a sub-firm depends-on dep.

Open questions promoted:
- (none — all 5 §Open-questions caveats are dispatch-coordination / sequencing notes, NOT standing cross-cycle questions: the co-wave forward-ref-slug coordination; the maturity-call-is-firm rationale; the consolidated-tally-deferred-to-D5 partition; the element_restrict/geom_factor_build sibling-ops note; the no-SUMMARY-change note. Captured here in Notes, not re-filed as ledger OQs — consistent with D1/D2's coordination-caveat handling this cycle.)

Build-relevant: yes

Notes:
- **D5 OWNS THE L1/index CONSOLIDATED TALLY — D3's two firm flips MUST be reflected in D5's tally (D5 applies AFTER D3).** Per the planner's parallel-blind-shared-index partition, D3 emits ONLY its own 2 cohort bullets + 2 dep-map rows (flipped in-place to firm) and DEFERS the L1/index substrate-cohort consolidated firm-count tally + the cohort-bullet HEADER count ("Roadmap_goal (libCEED contraction substrate — 4 …)") to D5. As of THIS landing, 2 of the 4 substrate ops (basis_apply, quad_point_contract) are now firm; the header still reads the pre-flip count on disk (I did NOT touch it). **D5's tally update must account for D3's 2 firm flips** (and D4's element_restrict/geom_factor_build flips if those land before D5). Flagged for finalize: if D5 for any reason does not run / does not adjust the tally, the cohort header will be stale (2 of 4 now firm, header unupdated) — finalize should reconcile.
- **concepts/element-local-tensor.md does NOT yet exist on disk** (confirmed by ls this invocation) — it is the co-wave D5 deliverable (the 5th integration, applies AFTER this D3). Both firm chapters + both dep-map rows link `../concepts/element-local-tensor.md` as live markdown. The single finalize `cargo make book` rebuild runs AFTER all per-report integrations, so the file is present at the one build IFF D5 lands before finalize (the wave schedule does this). If D5 slips, linkcheck2 hard-errors on the live link AND the rank-invariant is violated (firm node whose closing vocabulary page is absent/non-firm) — the report's honest fallback is rough-in (test-coverage-bounded) for both. The reference-class edge to element-local-tensor is lint-invisible, so this is a human/integrator-judgment gate, NOT lint-caught — flagged for finalize to verify D5 landed the page firm before the rebuild.
- **Stale path fix applied (informational, intended correction not drift):** both chapters' on-disk `book/src/design/l4_calculus.md §1.2.1` is replaced by the live `book/src/semantics/index.md §1.2.1` (confirmed §1.2.1 = "Named shape groups", semantics/index.md:73) via the full-file replacement.
- **Repaired pinpoints confirmed on disk:** the repairer's :36→:41 (CEED_EVAL_INTERP AddInput) and :48→:49 (CEED_EVAL_GRAD AddInput) corrections verified via codemap read_range on the full palace/fem/libceed/integrator.cpp path this invocation; the re-anchored quad_point_contract apply-QFunction citations (:457-458 geom_data, :462 q_w) were critic-confirmed.
- **No SUMMARY.md / no consolidated-tally / no sibling-op edits** — D3's footprint is exactly: 2 full-file chapter firm-flips + 4 in-place L1/index line flips. element_restrict + geom_factor_build (D4) and the libceed-quadrature-kernel-impl consumer promotion are NOT mine.
- deferred integrated_at to finalize per role-spec (per-report integrator does NOT touch the consumed report's frontmatter; integrated_at + integration_commit are finalize-only).

---

## 2026-06-07T112037Z-harvester-element-restrict-geom-factor
applied_at: 2026-06-07T124500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/element_restrict.md (full-file replace — roadmap_goal → rough-in; rank: rough-in; +depends-on (shape-vocabulary) concepts/element-local-tensor; stale design/l4_calculus.md §1.2.1 → live semantics/index.md §1.2.1; re-anchored restriction.cpp InitRestriction END :425→:426)
- book/src/L1/geom_factor_build.md (full-file replace — roadmap_goal → rough-in; rank: rough-in; +depends-on (shape-vocabulary) concepts/element-local-tensor; stale path fix; re-anchored integrator.cpp build-QFunction citations: AssembleCeedGeometryData :335-421, switch :348-384, attr :387 / q_w :388 / grad_x :389-390, geom_data :397-398, MFEM_VERIFY :395, consumer AssembleCeedOperator :423-427 + field-set :483-484)
- book/src/L1/index.md (in-place maturity flips ONLY: 2 §Vocabulary-cohort bullets roadmap_goal→rough-in [lines 103/106] + 2 dep-map rows roadmap_goal→rough-in [lines 188/191], each gaining the depends-on (shape-vocabulary) edge to concepts/element-local-tensor; distinct rows, NO consolidated tally / cohort-header touch — DEFERRED to D5)
- scaffolding/open-questions.md (append-only — 1 OQ section promoted, see below)

Gate hits:
- retroactive-budget per-slice: 0 (maturity-flip + citation re-anchor, not retroactive evidence backfill)
- retroactive-budget global: 0 (finalize sees full staging log — D1 + D2 + D3 + this D4)
- concept_writes on existing slug: 0 (no concept page authored here; concepts/element-local-tensor is D5's)
- forward-edge claim without surface: 0 (the depends-on (shape-vocabulary) target concepts/element-local-tensor is a forward-ref handled per spec — bare slug in frontmatter, plain inline-code in prose, NOT a live markdown link; the only live markdown links in both chapters resolve on disk: libceed-quadrature-kernel-impl / basis_apply / quad_point_contract / weak_form_term / element_restrict / geom_factor_build)
- edge-label / prose mismatch: 0 (depends-on (shape-vocabulary) + pulled-by/tensor-field-lift/build-time-vs-run-time-stratification reference edges all match prose)
- H1 reuses page heading: 0
- append on missing slug: 0 (both chapters pre-existing roadmap_goal since c122 D4)
- variant-axis missing on multi-variant operator: 0 (element_restrict covers lexico/native + oriented/unoriented index-map variants; geom_factor_build covers the 𝒟-determined metric form + (dim,space_dim) QFunction dispatch + affine special case)
- bookkeeping incomplete: 0
- SUMMARY chapter registration auto-fix: 0 (no new chapter; both registered since c122 D4 — maturity flip in-place, no SUMMARY change, per planner overlap note)
- alphabetical-position insert: n/a (in-place flips, no new rows)
- citecheck bounds + path-hygiene: 8 ok, 2 failing — both [AMBIG] basename collisions (integrator.cpp / integrator.hpp exist under both palace/fem/ AND palace/fem/libceed/); the report prose disambiguates with the full palace/fem/libceed/ path everywhere, so these clear on full paths (critic confirmed via --anchor, 16/16 clean). NO MISS/OOB. Non-blocking --scan basename-stripping false-positive.
- rank gate (§(h) well-foundedness): PASS (contingent on D5, confirmed by META repair) — both ops flip to rough-in (rank 2) with a sole depends-on (shape-vocabulary) edge to concepts/element-local-tensor. That page is NOT on disk this invocation (confirmed by ls — it is D5's co-wave deliverable, the 5th integration applying AFTER this D4). The META repair section verified D5 lands the page at rank firm (3); rank(u)=2 ≤ min(deps)=3 holds. No firm-flip over a sub-firm dep (this is the conservative one-rank honest climb from roadmap_goal, NOT firm).

Open questions promoted:
- batch-37-era-stale-design-l4-calculus-path-drift-sweep

Build-relevant: yes

Notes:
- **D5 OWNS THE L1/index CONSOLIDATED TALLY — D4's two rough-in flips MUST be reflected in D5's tally (D5 applies AFTER D4).** Per the planner consolidated-tally partition, D4 emits ONLY its own 2 cohort bullets + 2 dep-map rows (flipped in-place to rough-in) and DEFERS the L1/index substrate-cohort consolidated count + the cohort-bullet HEADER ("Roadmap_goal (libCEED contraction substrate — 4 …)", line 101) to D5. On-disk state I OBSERVED this invocation: the line-101 header still reads "— 4" (I did NOT touch it); of the 4 substrate ops, basis_apply + quad_point_contract are FIRM (D3's prior landing, observed in the bullets at lines 104/105 + the dep-map rows at 189/190), and now element_restrict + geom_factor_build are ROUGH-IN (this D4 landing). So as of this D4 landing ALL FOUR substrate ops have left roadmap_goal (2 firm, 2 rough-in) but the "— 4" cohort header is stale. D5's tally update must reconcile the cohort header (now "— 0" roadmap_goal if all four have promoted) + the firm/rough-in counts. Flagged for finalize: if D5 does not run / does not adjust the tally, the cohort header is stale.
- **concepts/element-local-tensor.md does NOT yet exist on disk — OBSERVED via ls this invocation** (NOT assumed from the staging log). It is the co-wave D5 deliverable (the 5th integration, applies AFTER this D4). Both rough-in chapters carry the depends-on (shape-vocabulary) edge target as a BARE SLUG in frontmatter (linter reads the slug, lint-invisible reference) and reference it in prose ONLY as plain inline-code (NOT a live markdown link), so no linkcheck2 error is introduced by my edits. The single finalize cargo make book rebuild runs AFTER all per-report integrations, so the page is present at the one build IFF D5 lands before finalize (the wave schedule does this). If D5 slips, the rank-invariant is left resting on an absent dep — the report's honest fallback would be roadmap_goal; flagged for finalize to verify D5 landed the page (META repair confirms D5 authors it at rank firm).
- **Maturity is rough-in BY DESIGN (honest clean-gate), NOT a failed promotion.** Both ops qualify for the firm-on-positive-structure escape (syntactic gather/scatter-add + setup-stratum-purity identities on positive source), but well-foundedness caps them at rough-in while the to-be-firm shape home concepts/element-local-tensor is itself firming this wave (a rough-in op MAY rest on a to-be-firm dep; a firm op may NOT). Per META, D5 lands the shape home FIRM this wave, so a same-cycle or next-cycle rough-in→firm flip of these two is the clean follow-up. Do not read rough-in as an incomplete discharge — it is the one-rank honest climb from roadmap_goal.
- **Stale path fix applied (intended correction, not drift):** both chapters' on-disk book/src/design/l4_calculus.md §1.2.1 replaced by the live book/src/semantics/index.md §1.2.1 (§1.2.1 = named shape groups). Promoted the standing OQ batch-37-era-stale-design-l4-calculus-path-drift-sweep (distinct from the c116 index.md:NNN prose-ref cohort) so a meta-phase grep -rn 'design/l4_calculus' book/src can enumerate any remaining batch-37-era instances.
- **No SUMMARY.md / no consolidated-tally / no sibling-op edits** — D4's footprint is exactly: 2 full-file chapter rough-in flips + 4 in-place L1/index line flips (each gaining the shape-vocabulary edge). The libceed-quadrature-kernel-impl consumer promotion + the concepts/element-local-tensor page are NOT mine (D5).
- Most of the report's §Open-questions caveats were dispatch-coordination / sequencing notes (consolidated-tally-deferred-to-D5; the forward-ref handling; the rough-in-not-firm honest-cap rationale) — captured here in Notes / gate rows rather than re-filed as ledger OQs, consistent with D1/D2/D3's coordination-caveat handling this cycle. The 1 promoted OQ is the genuinely forward-looking standing sweep candidate.
- deferred integrated_at to finalize per role-spec (per-report integrator does NOT touch the consumed report's frontmatter; integrated_at + integration_commit are finalize-only).

---
## 2026-06-07T112037Z-layer-intro-author-element-local-tensor
applied_at: 2026-06-07T134500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/element-local-tensor.md (CREATED — new `kind: record` page, rank firm; the [E,L]/[E,P,C]/[E,P,G] element-local rank-tensor shape-family definition home; resolves the D3 firm live-link + D4 rough-in bare-slug forward-refs to concepts/element-local-tensor)
- book/src/L1/libceed-quadrature-kernel-impl.md (promoted roadmap_goal → rough-in: frontmatter comment + `rank: rough-in`; `## Status` block; `## Substrate L1 operators` section retitled "c124 cohort: 2 firm + 2 rough-in". `realizes-kernel-api`/`realizes-leaf` reference edges UNTOUCHED — DIRECTIVE-3 integrity preserved)
- book/src/semantics/index.md (NEW §1.2.3 "Named axes of fixed meaning (the element-local family)" inserted after §1.2's LinOp paragraph, before §1.3 — USE+LINK: states the convention, links the record page for the axis definitions, does NOT restate the axis table or substrate algebra)
- book/src/L1/index.md (SOLE-OWNED consolidated tally: (4c) grand-total header 43 → 45 + new libCEED-substrate sub-spine; (4a) kernel-impl bullet roadmap_goal → rough-in; (4b) substrate cohort header "— 4" → "DRAINED — 2 firm + 2 rough-in")
- book/src/SUMMARY.md (concepts Part — inserted `element-local-tensor — record definition` in alpha position between `eigsolve` and `elementwise-product`)
- scaffolding/open-questions.md (append-only — 1 OQ section promoted, see below)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (finalize sees the full staging log — D1+D2+D3+D4+this D5)
- concept_writes on existing slug: 0 (new slug concepts/element-local-tensor — Write, file confirmed absent pre-apply)
- forward-edge claim without surface: 0 (all 7 reference link targets + 3 L0 cites-evidence targets verified on disk this invocation)
- edge-label / prose mismatch: 0 (concepts page: depends-on=cites-evidence to L0, reference to consumers; kernel-impl: realizes-kernel-api/realizes-leaf reference edges untouched)
- H1 reuses page heading: 0 (`# element-local-tensor` is the slug, not a parent heading reuse)
- append on missing slug: 0 (new page created; no append-to-missing case)
- variant-axis missing on multi-variant operator: 0 (record page — no operator variants; the C-component EvalMode axis is documented as a consumer-op property, not a hidden branch)
- bookkeeping incomplete: 0
- SUMMARY chapter registration auto-fix: 0 (report proposed the SUMMARY edit explicitly; applied as-given — alpha-correct: eigsolve < element-local-tensor < elementwise-product, `-` 0x2d < `w` 0x77; consistent with the existing "DofSet — record definition" concepts-Part record-page label convention)
- alphabetical-position insert: applied-as-specified (report specified the alpha position; no integrator discretion needed)
- index-placeholder displacement: n/a (no placeholder row)
- implied-component stub materialization: n/a (the page is a full firm record authored by the report, not an integrator-materialized stub)
- citecheck bounds + path-hygiene: 8 ok, 3 failing — all 3 [AMBIG] on bare `integrator.cpp` basename (collides palace/fem/integrator.cpp vs palace/fem/libceed/integrator.cpp); the report's load-bearing citations all carry the full palace/fem/libceed/ path (frontmatter cites-evidence targets + L0-source-home section), so they clear on full path. Critic confirmed via --anchor. NO MISS/OOB. Non-blocking --scan basename-stripping false-positive.
- rank gate (§(h) well-foundedness): PASS — (a) concepts page `firm`: only blocking edges are cites-evidence depends-on to L0 (rank-terminal ground truth) → vacuous, consumer edges are reference (free); (b) kernel-impl `rough-in`: 4 depends-on (composes) deps = 2 firm + 2 rough-in (VERIFIED on disk: basis_apply/quad_point_contract firm, element_restrict/geom_factor_build rough-in), min(deps)=rough-in, rank(impl)=rough-in ≤ min(deps) holds (2≤2) — CANNOT be firm, correct. No firm-flip over a sub-firm dep.

Open questions promoted:
- libceed-substrate-rough-in-to-firm-flip-and-45-to-47-tally-followup

Build-relevant: yes

Notes:
- **D3 + D4 confirmed landed before this D5 apply (re-read on disk this invocation, NOT assumed).** I grepped the four substrate-op chapters' on-disk `rank:`: basis_apply=firm, quad_point_contract=firm (D3), element_restrict=rough-in, geom_factor_build=rough-in (D4). The repairer's integrator-ordering note (apply D3/D4 before D5) is satisfied — the rough-in cap on the kernel-impl and the 43→45 tally arithmetic both rest on these observed on-disk maturities, not on a presumed apply order.
- **The new firm concepts/element-local-tensor.md closes the D3/D4 forward-link risk.** D3's two firm chapters carried live markdown links `../concepts/element-local-tensor.md` (a missing target is a linkcheck2 hard-error); D4's two rough-in chapters carried the bare-slug depends-on edge. The page now exists firm before finalize's single `cargo make book`, so both the linkcheck2 link and the D4 rank-invariant (rough-in resting on a now-firm dep) resolve.
- **Tally arithmetic, sole-owned this wave:** 33 main + 4 FE-assembly + 5 FE-space + 1 Mesh-construction + 2 libCEED-substrate = 45. D5 added only the +2 firm from D3 (basis_apply + quad_point_contract); D4's two are rough-in (not counted firm) and the kernel-impl is rough-in (not counted firm). The cohort header "— 4 roadmap_goal" is now drained (2 firm + 2 rough-in). D3/D4 own their own member bullets + dep-map rows (left in place); I reconciled only the grand-total header, the cohort header, and the kernel-impl bullet, as the planner partitioned.
- **The 45→47 firm-flip is DEFERRED to c125, NOT done this wave** (promoted as the OQ above). D4's two ops + the kernel-impl qualify for rough-in→firm now that the shape home is firm on disk, but that cap-rises-to-firm is a *consequence* of D5 landing — applied next cycle by the integrator's cross-report rank-propagation, not retroactively inside D5's own apply (those two were rough-in on-disk at apply time). Honest current state: 45 firm, 2 rough-in substrate + 1 rough-in consumer.
- **Ledger entries resolved-by-this-landing (flagged for meta-phase unify, NOT closed by me):** `record-element-local-tensor-needs-definition-home-at-firming` (open-questions.md:1777 — its Action "at the firm flip … concepts/element-local-tensor.md definition home" is exactly satisfied) and `libceed-substrate-element-local-rank-tensor-l1-vocabulary-front` (the migrated front, line ~1894). Closing/migrating these is meta-phase write-territory.
- **Semantic §1.2.3 is USE+LINK per the semantic-consolidation discipline** — states the concrete-named-axis-vs-congruence-group convention and routes the per-axis definitions to the record page; does not restate the axis table or the substrate ops' algebra. Verified the substrate ops keep only their own signatures (D3/D4's thin §1.2.1 links, no general-rule restatement to relocate).
- deferred integrated_at to finalize per role-spec (per-report integrator does NOT touch the consumed report's frontmatter; integrated_at + integration_commit are finalize-only).

---
## 2026-06-07T112037Z-combinator-miner-re6-arity-refactor
applied_at: 2026-06-07T143000Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/linear_combination.md (group A — §Arity specializations heading normalized to clean `#arity-specializations` anchor; +per-arity unique-L0-anchor fold-in table from the 4 deleted L2 leaves; §Dependencies collapse-schedule reworded reduce-to-stub→eliminated cycle-124 RE6)
- book/src/L3/linear_combination.md (group A — heading normalized; +per-arity unique-L0-anchor + live-consumer-sites fold-in table from the 4 deleted L3 leaves incl. the load-bearing α==1.0 fast-path vector.cpp:702-712, the γ==0 arity-collapse vector.cpp:749-751, the scal consumer sites iterative.cpp:632,811 / operator.cpp:661,673 / nleps.cpp:486-491; :29 + :135 stub-framing reworded to eliminated, :135 leaf links dropped to inline-code + back-link to #arity-specializations)
- book/src/L2/scal.md (DELETED via git rm)
- book/src/L2/axpy.md (DELETED via git rm)
- book/src/L2/axpby.md (DELETED via git rm)
- book/src/L2/axpbypcz.md (DELETED via git rm)
- book/src/L3/scal.md (DELETED via git rm)
- book/src/L3/axpy.md (DELETED via git rm)
- book/src/L3/axpby.md (DELETED via git rm)
- book/src/L3/axpbypcz.md (DELETED via git rm)
- book/src/SUMMARY.md (group C — removed 8 leaf sub-chapter lines; L3 BLAS-1 group keeps dot/inner_product/linear_combination/nrm2; L2 fold-family-stubs group keeps dot/nrm2; neither group empty)
- book/src/L2/index.md (group D — dropped 4 dep-map rows axpby/axpbypcz/axpy/scal, kept dot+nrm2; re-pointed normalize-row scal link → #arity-specializations; working-notes cycle-043-cohort bullet: re-pointed 3 live links axpy/axpby/axpbypcz [critic Issue 1 CORRECTION — the falsely-"no-risk" bullet] + reworded reduced-to-stub→eliminated)
- book/src/L3/index.md (group D — dropped 4 dep-map rows axpby/axpbypcz/axpy/scal, kept dot/inner_product/linear_combination/nrm2; linear_combination-row §Deps leaf links dropped to inline-code + folded-into-§Arity framing; re-pointed live links in :29 obstruction-spectrum [scal], elementwise_product-row [scal, critic Issue 2], normalize-row [scal, critic Issue 3], divfree-projector-row [axpy], orthogonalize-row [axpy, critic Issue 4]; :26 linear-update-family narrative reworded combinator-primary [inline-code])
- book/src/L2/fold-family-stubs-intro.md (group D — reference: edges trimmed to L2/dot+L2/nrm2; body: 4 linear_combination arity bullets removed + replaced with eliminated-cycle-124 note linking #arity-specializations; six→two stubs)
- book/src/L3/blas1-intro.md (group D — reference: edges trimmed to L3/{dot,inner_product,linear_combination,nrm2}; linear_combination bullet leaf links dropped + eliminated note; "All eight"→"All")
- book/src/L2/normalize.md (group E — frontmatter consumes: edge book/src/L2/scal.md → book/src/L2/linear_combination.md; 9 [scal](./scal.md) body links → #arity-specializations)
- book/src/L2/divfree-projector.md (group E — 2 [scal] links → #arity-specializations)
- book/src/L2/elementwise_product.md (group E — :269 [scal] link → #arity-specializations; :445 bare code-span book/src/L2/scal.md retext → linear_combination §Arity specializations [non-link, build-safe, retext for accuracy])
- book/src/L2/reciprocal.md (group E — 7 [scal](./scal.md) links → #arity-specializations incl. the :409 special [`book/src/L2/scal.md`](./scal.md) re-target+retext → linear_combination)
- book/src/L3/chebyshev.md (group E — axpy/axpby/scal/axpbypcz links → #arity-specializations)
- book/src/L3/divfree-projector.md (group E — axpy link → #arity-specializations)
- book/src/L3/elementwise_product.md (group E — 2 [scal] links → #arity-specializations)
- book/src/L3/ksp_solve.md (group E — :136 transitive-primitives list axpy/axpby/axpbypcz/scal links → #arity-specializations)
- book/src/L3/normalize.md (group E — 8 [scal] links → #arity-specializations)
- book/src/L3/orthogonalize.md (group E — 2 axpy + 1 scal links → #arity-specializations)
- book/src/L3/reciprocal.md (group E — scal/axpy/axpby/axpbypcz links → #arity-specializations)
- book/src/L3-L2/orthogonalize-variant-split.md (group E cross-Part — :134 [axpy](../L3/axpy.md), :259 [L3/axpy](../L3/axpy.md), :260 [L2/axpy](../L2/axpy.md) all → ../{L3,L2}/linear_combination.md#arity-specializations)
- scaffolding/open-questions.md (append-only — 1 OQ promoted, see below)

Gate hits:
- retroactive-budget per-slice: 0 (in-layer fold-in + delete + re-point; no retroactive evidence backfill)
- retroactive-budget global: 0 (finalize sees the full staging log — D1..D6)
- concept_writes on existing slug: 0 (no concept page authored)
- forward-edge claim without surface: 0 (no new forward edges; all re-pointed targets resolve to the firm in-disk linear_combination chapters)
- edge-label / prose mismatch: 0 (re-points preserve link TEXT as readout label; framing reworded reduce-to-stub→eliminated consistently)
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (arity axis preserved as the per-arity fold-in table rows; over-unification guard left dot/nrm2 standalone, NOT in RE6 scope)
- bookkeeping incomplete: 0
- SUMMARY chapter registration auto-fix: 0 (this is DE-registration — 8 lines removed per report group C; both groups remain non-empty, verified)
- alphabetical-position insert: n/a (deletions + re-points, no new rows)
- citecheck bounds + path-hygiene: scan reports 0 ok / 20 failing, ALL [MISS]/[AMBIG] — the KNOWN nested-palace-layout artifact (real path reference/palace/palace/linalg/vector.{hpp,cpp}, confirmed present on-disk this invocation; citecheck --scan roots do not include the double-nested palace/palace/). NOT real drift: the critic verified EVERY load-bearing pinpoint (vector.cpp:749-751 γ==0, vector.cpp:702-712 α==1.0, the scal consumer sites) by direct on-disk read; this is a refactor MOVING already-verified anchors in-layer, no re-localization claim. NO real MISS/AMBIG/OOB. Non-blocking.
- rank gate (§(h) well-foundedness): PASS / n/a — no DAG node added, no rank/liveness change. The combinator was already firm + root-reachable; the eliminated leaves were rank-3 dependents depending UP on the combinator — removing dependents never affects a node's own rank/liveness. RE6 strictly SHRINKS the node count (8 standalone nodes → 0).
- DANGLING-LINK SAFETY-NET GREP (the load-bearing gate for this destructive refactor): ZERO hits on BOTH report greps + a broad sweep — `grep -rnE '\((\.\./)?(L2|L3)/(axpy|axpby|axpbypcz|scal)\.md' book/src/` = 0; `grep -rnE '\]\(\./(axpy|axpby|axpbypcz|scal)\.md' book/src/L2 book/src/L3` = 0; broad `\]\([^)]*(L2|L3)/(axpy|axpby|axpbypcz|scal)\.md` = 0. No surviving link targets any of the 8 deleted files. EXCLUDED L1/* + concepts/* links confirmed INTACT + untouched (L1/scal.md + concepts/scal.md still on disk). SUMMARY.md = 0 deleted-leaf references.

Open questions promoted:
- inner-product-family-re-style-elimination-candidate

Build-relevant: yes

Notes:
- **RE6 DISCHARGED** (flag for finalize + meta-phase). This is the RE6 elimination refactor per DIRECTIVE 2 / memory project_lift_through_deferred_in_scope ("the axpy-family arity leaves … the combinator-arity-notes refactor"). The 8 off-spine `linear_combination` arity-leaf standalone nodes are ELIMINATED (the higher-value disposition: delete, not ground) — their unique L0 anchors folded into the combinator §Arity specializations at each layer, the standalone chapters deleted, SUMMARY + index dep-maps de-registered, ~90 inbound links re-pointed. The RE set's RE6 row should be marked DISCHARGED.
- **Both combinator §Arity specializations headings normalized to clean `#arity-specializations` anchors** (group A heading-shortening, the integrator's-call recommended by the report) — so the ~90 re-pointed `#arity-specializations` fragment links resolve cleanly (not just to bare file). warning-policy=warn means a fragment miss would be a warning anyway, but the clean anchor avoids the warnings entirely.
- **All L0 anchors PRESERVED in the fold-in** — including the load-bearing γ==0 arity-collapse `vector.cpp:749-751`, the α==1.0 constant-fold fast-path `vector.cpp:702-712`, and the L3 scal live-consumer sites `iterative.cpp:632,811` / `operator.cpp:661,673` / `nleps.cpp:486-491`. The L3 fold-in table additionally carries the live-consumer sites the L2 table does not (the scal chapter's extra consumers), per the report's group A note.
- **citecheck --scan = 0 ok / 20 failing is a FALSE POSITIVE** (the double-nested palace/palace/ layout falls outside citecheck --scan roots; basename collisions like operator.cpp are disambiguated by the linalg/ prefix in prose). Confirmed reference/palace/palace/linalg/vector.cpp exists on disk this invocation. The critic independently verified every load-bearing pinpoint by direct on-disk read (citation-validity PASS). NOT a real citation defect — non-blocking per role-spec (DRIFT/artifact, not MISS/AMBIG/OOB on a real path).
- **The 4 critic-repaired re-points (Issues 1-4) are ALL applied:** L2/index.md cycle-043-cohort working-notes bullet (3 links axpy/axpby/axpbypcz — the falsely-"no-risk" bullet), L3/index.md elementwise_product-row [scal], normalize-row [scal], orthogonalize-row [axpy]. Each verified live on-disk before re-point + confirmed gone by the post-edit grep.
- **Non-blocking stale bare-code prose mentions LEFT AS-IS** (per the repairer's not-needed disposition + critic non-error classification): inline-code text spans naming the deleted files with NO `(./…)` link target — e.g. L2/jacobi-smoother.md:524, L3/linear_combination.md status-cell historical-provenance "reduced to specialization-stubs cycle-052", L3/{elementwise_product,normalize,reciprocal}.md frontmatter-region bare-path lifts_from/precedent notes (`book/src/L3/scal.md`), L3-L2/orthogonalize-variant-split.md:293. These are NOT linkcheck2 errors (no link target) and do NOT block the build; they read as pointing at now-absent files. Flagged for an OPTIONAL meta-phase readability sweep (grep -rn 'book/src/L[23]/\(scal\|axpy\|axpby\|axpbypcz\)\.md' book/src) — out of per-report hard-error scope.
- **D1..D5 sibling landings observed on disk this invocation** (NOT assumed): the staging log shows D3/D4/D5 rows; my edits to the shared index files (L2/index.md, L3/index.md, SUMMARY.md) re-read disk fresh and operated on the current on-disk state. D6's footprint is disjoint from the libCEED-substrate cohort (D3/D4/D5 touched L1/* + concepts/* + semantics/* + L1/index.md; D6 touches L2/* + L3/* + L3-L2/* + SUMMARY.md + the L2/L3 index BLAS-1 sections) — no contended anchors observed.
- deferred integrated_at to finalize per role-spec (per-report integrator does NOT touch the consumed report's frontmatter; integrated_at + integration_commit are finalize-only).

---

## 2026-06-07T112037Z-layer-intro-author-gmg-hygiene
applied_at: 2026-06-07T121500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/feature/geometric-multigrid-preconditioner.L4.md (a1: +1 `reference` edge `L2/correction_step`; a2: vcycle recursion prose reword naming correction_step per leg + a coarse-grid-correction = conjugated-B paragraph; a3: per-level smoother stage prose names correction_step)
- book/src/feature/geometric-multigrid-preconditioner.L1.md (a4: +1 `reference` edge `L2/correction_step` w/ DOWNWARD-annotation comment; a5: downward-annotation paragraph after the residual/update prose)
- book/src/L1/multigrid-relaxation-smoother.md (a6: +1 `reference` edge `L2/correction_step` w/ DOWNWARD-annotation comment; a7: downward-annotation paragraph after the two-leg list)
- book/src/L3/eigsolve.md (b1+b2: ido-99 cite `:330-333`→`:331-334` at lines 94 and 221)
- book/src/L3-L2/eigsolve-opaque-eigen-iteration.md (b3: ido-99 cite `:330-333`→`:331-334` at line 188)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0 (all 4 new edges `reference`-class; the L4→L2 is the permitted L4-may-reference-L2 down-link, the 2 L1 sites are EXPLICIT downward annotations with prose recording NO depends-on is created — edge direction matches prose)
- H1 reuse: 0
- append on missing slug: 0
- variant-axis missing: 0
- rank gate (well-foundedness): N/A — NO depends-on edge added, NO `## Status`/rank flip; zero rank/GC impact (all edges `reference`-class; per c123-meta RE11 adjudication the L4→L2 reference carries NO liveness, navigability completion not a reachability flip)
- bookkeeping incomplete: 0
- SUMMARY chapter registration auto-fix: 0 (no new files created)
- citecheck bounds + path-hygiene: 22 ok, 0 failing — clean scan, no MISS/AMBIG/OOB

Open questions promoted:
- interpolator-backward-reference-note-trim-target-unidentified (actionable — next planner must specify the exact file:line or confirm moot; the D7 agent correctly declined to invent a trim against an unspecified target)
- d7-ido99-citation-plan-path-correction-disposition (informational, resolved — plan named L1/eigsolve.md but the drift lived at L3/eigsolve.md:94,221 + L3-L2/eigsolve-opaque-eigen-iteration.md:188; corrected at the real homes, verified on-disk vs arpack.cpp:331-334)

Build-relevant: yes (touches book/src/*.md — 5 files)

Notes: D7, the 7th and FINAL report of cycle-124 — cheap-hygiene bundle, zero maturity/GC/rank impact. All on-disk anchors re-read this invocation and matched the report's `[old]` blocks exactly (the L4 vcycle prose, the L1 residual/update + two-leg prose, all three stale `:330-333` cites). Source-of-truth re-verified on disk: `reference/palace/palace/linalg/arpack.cpp:331-334` IS the `ido == 99` break clause (`:331` `else if`, `:332` `{`, `:333` `break;`, `:334` `}`); `:330` is the `ido == 2` close-brace — so `:330-333` was off-by-one on the start and `:331-334` is correct. All 4 new `correction_step` reference links point at `book/src/L2/correction_step.md` (confirmed present on disk — linkcheck2-safe). The 2 L1 sites are downward annotations explicitly recorded as NON-edges (L1-can't-depend-up-on-L2). Files disjoint from all 6 prior c124 landings (D1/D2 touched L3/eigsolve-impl.md, a DIFFERENT file from this dispatch's L3/eigsolve.md). The interpolator-trim item-5 was correctly declined-to-invent by the producer (no identifiable target) and is promoted as an OQ for the next planner — NO content edit attempted. Deferred `integrated_at` (and `integration_commit`) to finalize per role-spec.

---
