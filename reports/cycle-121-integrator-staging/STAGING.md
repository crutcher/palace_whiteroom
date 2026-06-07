# cycle-121 integrator staging log

Per-report integration rows, newest LAST (append-only). The row ORDER is the
authoritative apply-order record; `applied_at` timestamps are advisory only.
integrator-finalize reads this log to reconcile the cycle (rebuild + commit).

---

## 2026-06-07T054924Z-harvester-multigrid-relaxation-smoother
applied_at: 2026-06-07T063046Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/multigrid-relaxation-smoother.md (created — new kernel-impl node, firm; full chapter: Signature, Record definition, 5 algebraic laws, non-laws/NL1-3, Dependencies, Evidence, Status)
- book/src/L1-L0/triangular-solve-obstruction.md (edited ## Status — added `kernel-api` role-label + clarified sub-kind bare `obstruction` → `obstruction (opaque-library-ownership)`; stays obstruction-kind, NOT downgraded/promoted)
- book/src/L1/index.md (edited — added dep-map row after `ksp_solve` in Constructed-operator gates group at alpha position; added "Kernel-impl (smoother)" bullet at TAIL of ## Vocabulary cohort)
- book/src/SUMMARY.md (edited — added 2-space nested entry after `ksp_solve` in the Constructed-operator gates by-kind group, alpha position m>k)

Gate hits:
- realizes-kernel-api edge-class check: PASS — edge is under `reference:` key (NOT `depends-on:`), `reference`-class, constrains neither rank nor liveness. Confirmed in frontmatter + prose + Status + index cells.
- graded-stack rank linter (Axis 1): PASS — 0 rank violations. New `firm` (rank 3) node rests only on firm `depends-on` deps (chebyshev-smoother, apply_linop, axpby, interpolator — all firm on disk); `realizes-kernel-api` reference-edge correctly excluded from rank computation. `rank(impl) ≤ min(rank(deps))` holds (firm ≤ firm).
- graded-stack reachability GC (Axis 2): node `L1/multigrid-relaxation-smoother` shows `[GARBAGE*]` (transiently unreachable) — EXPECTED + BENIGN. Its only consumer edge this report is `reference`-class via `L4/preconditioning-framework`; the GC marks over `depends-on` from feature roots. D1 (the GMG feature column, integrated NEXT this cycle) adds the hard `depends-on` consumer that makes it live. This report integrated FIRST precisely so D1's forward-ref resolves. NOT a defect — resolves intra-cycle when D1 lands. (Pre-existing baseline: 133 detritus / 61 untyped — the bounded type-the-edges adoption campaign, not a per-report gate; linter exit 0.)
- citecheck (--scan, bounds + path-hygiene): PASS — 26 ok, 0 failing. No MISS/AMBIG/OOB. (hpp field-pinpoint DRIFT was repaired by repairer + verified by critic via direct grep; --scan reports bounds only, not anchors — anchor-drift is upstream territory.)

Open questions promoted (5, appended to scaffolding/open-questions.md):
- multigrid-relaxation-smoother-mutation-rotation-theme-named-not-authored (→ abstractor dispatch, L1>L0 theme)
- multigrid-relaxation-smoother-l3-partial-obstruction-row-not-authored (→ L3-iteration-views planner, DIRECTIVE-2 item-4)
- multigrid-relaxation-smoother-lowering-verifier-realizes-kernel-api-audit (→ c122 candidate)
- multigrid-relaxation-smoother-d1-forward-reference-coupling (→ finalize reachability re-check after D1)
- multigrid-relaxation-smoother-index-tally-kernel-impl-count (→ integrator/layer-intro-author confirm separate kernel-impl count line)

Build-relevant: yes (touches book/src/*.md — new L1 chapter + 3 edits)

Notes:
- overall_status was `ready` (canonical) from the repairer; META checks all pass/repaired/not-needed. Applied cleanly.
- SUMMARY/dep-map/vocab-cohort placements followed the repairer-resolved anchors: NO new "Kernel-impl (smoother)" SUMMARY/dep-map group header introduced — kernel-impl-ness rides the `## Status` role-label + index status-cell `**kernel-impl**`, per the DIRECTIVE-3 sensible-default chapter-kind placement (no new linter/SUMMARY machinery). The chapter self-identifies as a constructed-operator gate, filed into that existing by-kind group.
- INDEX TALLY deliberately left unchanged (the "33 main / 43 firm" consolidated tally) — this is a distinct kind (kernel-impl), not a main-cohort firm operator. Flagged as OQ for finalize/layer-intro-author.
- deferred integrated_at to finalize per role-spec (did NOT touch the consumed report's frontmatter integrated_at / integration_commit).
- D1 coupling: this D3 report integrated FIRST so D1's forward-reference to book/src/L1/multigrid-relaxation-smoother.md resolves. No file collision with D1 (feature/*.md). Reachability becomes live once D1's depends-on edge lands — finalize should re-run the reachability GC after the full batch and confirm the node marks live (or note it stays GARBAGE* if D1 did not in fact add the hard edge).

---

## 2026-06-07T054924Z-layer-intro-author-geometric-multigrid-preconditioner
applied_at: 2026-06-07T065500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/feature/geometric-multigrid-preconditioner.L4.md (created — GMG L4 composition-root, kind: feature-surface, feature_root: seed, rank: rough-in; 8 depends-on (7 composes + 2 cites-evidence) + 2 reference edges; full body: composition / inputs-outputs / why-rough-in / single-machine / constituent down-links / Status)
- book/src/feature/geometric-multigrid-preconditioner.L1.md (created — GMG L1 pure-function surface, rank: rough-in; pure V-cycle recursion + 3 composed pieces + Status)
- book/src/feature/infrastructure.md (created — NEW by-kind group-intro for the 4th feature sub-kind "Infrastructure / shared-substrate columns"; navigational-container, no rank, reference edges to the GMG L4+L1 surfaces)
- book/src/feature/index.md (edited — added the Infrastructure/shared-substrate grouping header row + the GMG matrix row (L0 cell `—`) after the waveguide-mode row)
- book/src/SUMMARY.md (edited — added `- [Infrastructure / shared-substrate columns]` 0-indent grouping + 2 nested GMG L4/L1 entries after the waveguide-mode block, before `# Semantic surface`)

Gate hits:
- citecheck (--scan, bounds + path-hygiene): PASS — 40 ok, 0 failing. No MISS/AMBIG/OOB. (Repairer had already renumbered the +1 inline-pinpoint drift; --scan reports bounds only.)
- graded-stack rank linter (Axis 1): PASS — 0 rank violations. New `rough-in` (rank 2) GMG columns rest on firm (3) deps (preconditioning-framework, fe_space_hierarchy, jacobi-smoother, reciprocal, normalize) + partial-obstruction (~2.5) chebyshev + rough-in (2) multigrid-relaxation-smoother. `rank(rough-in) ≤ min(deps)` holds — the column is correctly capped at rough-in by the smoother leg, NOT firm.
- graded-stack reachability GC (Axis 2): PASS for the load-bearing assertion — `L1/multigrid-relaxation-smoother` is now LIVE (NOT in the garbage list). Inbound-ref report confirms `L1/multigrid-relaxation-smoother <- feature/geometric-multigrid-preconditioner.L1, feature/geometric-multigrid-preconditioner.L4` — D1's hard `depends-on (composes)` edges resolved the D3-transient `[GARBAGE*]` exactly as predicted. The two GMG columns show `[FRONTIER]` (reachable roots via `feature_root: seed`). unresolved_depends_on_targets: 0 (all edges resolve; smoother file on disk). Whole-artifact totals: 118 detritus (down from D3's 133 — the smoother + neighbors became reachable), 61 untyped (unchanged bounded baseline — the type-the-edges adoption campaign, not a per-report gate). Linter exit 0.
- RE9 grounding: CONFIRMED — GMG.L4/L1 → `L1/fe_space_hierarchy` (firm) `depends-on (composes)` edge present + resolving (the `GetProlongationOperators()` named consumer). RE1 (→ L3/chebyshev + L2/jacobi-smoother), RE5 (→ L1/normalize), RE7 (→ L1/reciprocal) edges all present + resolving.
- forward-edge / surface check: PASS — all live links + depends-on targets resolve on disk (the D3 forward-ref `book/src/L1/multigrid-relaxation-smoother.md` exists).
- new-SUMMARY-kind-grouping ⇒ group-intro stub in same landing: SATISFIED — the new "Infrastructure / shared-substrate columns" grouping's group-intro (`infrastructure.md`) was authored by the report and landed in the SAME apply; the SUMMARY grouping link points at it (NOT at a placeholder existing page). No mdBook Duplicate-file risk.

Open questions promoted (5, appended to scaffolding/open-questions.md):
- record-MultigridConfig-needs-definition-home
- geometric-multigrid-preconditioner-rough-in-promotion-smoother-leg-gated
- vcycle-level-recursive-combinator-mining-candidate
- geometric-multigrid-additional-driver-agnostic-consumers-hcurl-errorestimator
- geometric-multigrid-smoother-leg-edge-target-l3-vs-l4-chebyshev

Build-relevant: yes (touches book/src/*.md — 3 new chapters + index + SUMMARY)

Notes:
- overall_status was `needs-revision` (NOT ready) — but per the dispatch this is the SANCTIONED integration-sequencing exception, not a content defect: META checks are all pass/repaired/not-needed; the sole `cross-reference-integrity` warning was the D3 forward-ref to `book/src/L1/multigrid-relaxation-smoother.md`, which D3 ALREADY LANDED earlier this cycle (confirmed on disk this invocation + its STAGING row present). The repairer routed it with `follow_up_agent: integrator-per-report` precisely so I discharge the sequencing. All live links now resolve. Applied as-authored.
- D9 coordination: `book/src/feature/index.md` is also touched by D9 (waveguide cells), NOT yet integrated. My GMG-row edit used a distinct anchor (append after the waveguide-mode row + the new Infrastructure grouping). D9's later integration uses distinct anchors. No collision observed; if D9's anchor no longer matches after my edit, note: I appended the Infrastructure grouping + GMG row immediately AFTER the `waveguide-mode` matrix row (line ~57) — D9's waveguide/output-product cell edits should target the waveguide-mode row itself, which is unchanged.
- index.md frontmatter `reference:` edges list the 3 prior sibling group-intros but NOT `feature/infrastructure` — the report did not propose adding it. Left as-authored (non-blocking; the matrix-cell link to infrastructure.md provides navigation). Flag for finalize/layer-intro-author if the index frontmatter should enumerate the 4th grouping.
- record-FiniteElementSpaceHierarchy-promote-watch (c118 D6, UNFIRED) named "the geometric-multigrid preconditioner (the RE9 consumer)" as its 2nd-consumer trigger — but its trigger specifies a 2nd *FIRM* consumer, and GMG landed `rough-in` (not firm). Trigger NOT fired this cycle. Flag for layer-intro-author/c122: re-evaluate the watch when GMG promotes to firm.
- alpha-position-insert: the new "Infrastructure / shared-substrate columns" grouping was placed by the report AFTER the Output-product grouping (the by-kind order is semantic: spine-ROOT → driver-leaf → output-product → infrastructure, NOT cross-kind alpha). Position was report-specified; I did not exercise placement discretion. Within the grouping, GMG is the sole member (no within-kind alpha choice needed).
- deferred integrated_at to finalize per role-spec (did NOT touch the consumed report's frontmatter integrated_at / integration_commit).

---

## 2026-06-07T054924Z-layer-intro-author-fe-space-hierarchy-concepts-page
applied_at: 2026-06-07T063935Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/FiniteElementSpaceHierarchy.md (created — new record-definition concepts page; kind: record, rank: firm; field schema fespaces/P + per-field construction-vs-run-time strata + read surface + L0 backing class home; 1 cites-evidence depends-on to fespace.hpp:200-286, 6 reference edges incl. producer + both GMG-column levels)
- book/src/L1/fe_space_hierarchy.md (edited ×3 — (a) frontmatter: added `concepts/FiniteElementSpaceHierarchy` reference edge after `L1/build_mesh`; (b) §Record-definition: trimmed the in-chapter field table + accessor prose to a back-link to the concepts page + a producer-local fold-output note, fixing the stale "single-consumer / sole harvested producer/consumer" claim; (c) result-line in §Signature: pointed the "see *Record definition*" at the concepts page)
- book/src/SUMMARY.md (edited — inserted `[FiniteElementSpaceHierarchy — record definition]` in the Concepts Part between `finest-level-unwrap` and `first-iteration-unrolling`, case-insensitive alpha position `fine < fini < firs`)

Gate hits:
- citecheck (--scan, bounds + path-hygiene): PASS — 23 ok, 0 failing. No MISS/AMBIG/OOB. The new page's L0 citation `fespace.hpp:200-286` is in bounds. (The lone META `citation-validity: warning` was a no-edit Part-1 VERIFY-summary gmg.cpp pinpoint drift, already repaired by the repairer to `:191`/`:199` op-anchors; no proposed-changes block carried the drifted pin.)
- in-chapter trim ⇒ valid back-link: PASS — `grep -c concepts/FiniteElementSpaceHierarchy.md fe_space_hierarchy.md` = 2 (the §Record-definition pointer + the result-line back-link). The trimmed §Record-definition still names the producer-local fold-output note; no claim stranded.
- cross-reference integrity (new page + sibling files): PASS — all 6 `reference` targets exist on disk, incl. the D1-landed `feature/geometric-multigrid-preconditioner.{L4,L1}.md` (verified on disk this invocation), `L1/fe_space.md`, `concepts/mesh.md`, `concepts/build-time-vs-run-time-stratification.md`, `L1/divfree-projector.md`, `L1/build_mesh.md`. No dangling live link.
- SUMMARY alpha-position: PASS — case-insensitive sort verified (`sort -c` over the 3 lowercased keys). Display-text `— record definition` suffix matches the `DofSet — record definition` / `Mesh — record definition` capitalized-record convention. Concepts Part registration preserved (SUMMARY auto-fix not needed — report proposed the entry).
- rank-invariant (Axis 1): PASS by inspection — new page `rank: firm` (rank 3); sole blocking edge is `cites-evidence depends-on` to the rank-terminal L0 range (`rank(u) ≤ rank(v)` holds vacuously). Producer/consumer edges are `reference`-class (navigational, free) — the rough-in GMG consumer does NOT constrain the firm record page. Did NOT re-run the linter binary (no new depends-on into the live graph beyond the L0-terminal edge; D1's GMG row already ran the full reachability/rank linter this cycle).
- reachability (Axis 2): the new page is reachable as a `reference` target from the firm producer + the GMG column (a record page is named-by-use). Part 1 (D1's RE9 `depends-on` edge) makes `L1/fe_space_hierarchy` GC-reachable — authoritative confirmation deferred to the c122 linter `--show-inbound` re-run (OQ promoted).

Open questions promoted (3, appended to scaffolding/open-questions.md):
- record-FiniteElementSpaceHierarchy-promote-watch-wording-reconcile  (the firm-vs-rough-in nuance — D2's promotion is sanctioned under the live "≥2 consumers, not ≥2 firm" rule; the c118 watch's "2nd FIRM consumer" wording should be marked RESOLVED-by-promotion + reconciled by c122/meta-phase)
- fe-space-hierarchy-concepts-page-re9-c122-linter-confirm  (the authoritative RE9-discharge measurement is the c122 linter `--show-inbound` on L1/fe_space_hierarchy)
- (also: the report's Part-1 D1↔D2 shared-edge coordination + D1-MultigridConfig caveats are integrator-coordination notes already discharged by D1's landing — NOT re-promoted as standalone OQs; covered by the two above)

Build-relevant: yes (touches book/src/*.md — 1 new concepts page + 3 edits to an L1 chapter + 1 SUMMARY edit)

Notes:
- overall_status was `ready` (canonical) from the repairer; META checks pass/repaired/not-needed (the sole citation-validity warning was repaired). Applied cleanly as authored.
- PART 1 (the RE9 GROUND edge) was VERIFY-ONLY by design — D1 authored the `GMG → L1/fe_space_hierarchy depends-on (composes)` edge on both GMG levels; D2 added NO edge edit to avoid double-registration. I applied ONLY D2's Part-2 promotion edits. No edit collision with D1 on `fe_space_hierarchy.md`: D1 does not edit that file (its RE9 edge lives in the GMG frontmatter); D2's 3 edits are disjoint. Confirmed on disk this invocation: D1's GMG `.L4`/`.L1` files exist and the fe_space_hierarchy.md frontmatter D1-era `lowers-to` + `L1/fe_space`/`L1/fe_collection` composes edges are intact (I only appended a `reference` edge + trimmed the §Record-definition body + retargeted the result-line).
- FIRM-VS-ROUGH-IN NUANCE (per the dispatch judgment note): D2's critic ruled the ≥2-consumer bar MET (producer + GMG; bar = "≥2 consumers", not "≥2 firm", per the `concepts/mesh.md` precedent — a record page is a `reference` target). The c118 `record-FiniteElementSpaceHierarchy-promote-watch` named a 2nd *FIRM* consumer and GMG landed rough-in, so that watch's literal trigger did not strictly fire (D1's staging row noted this). NOT a conflict for application: D2's promotion is a sanctioned dispatch+critic judgment. Recorded both as an OQ (above) for c122/meta-phase wording reconciliation.
- deferred integrated_at to finalize per role-spec (did NOT touch the consumed report's frontmatter integrated_at / integration_commit).

---

## 2026-06-07T054924Z-layer-intro-author-waveguide-mode-drift-cleanup
applied_at: 2026-06-07T071500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/feature/waveguide-mode.L0.md (edited ×2 — (1) frontmatter `rank: rough-in` → `firm`, `feature_root: seed` KEPT; (2) `## Status` body reconciled `rough-in` → `firm`, OQ-resolved/gate-cleared narrative, `feature_root: seed` KEPT)
- book/src/feature/index.md (edited ×4 — output-product-cohort bullet verb `rough-in`→`firm`; the "only waveguide-mode remains seed" prose → "all 13 columns firm"; Chapter-kind-status split header `firm (12 columns)` → `firm (13 columns)`; seed-block: moved waveguide-mode into the firm output-product list + `seed (1 column)` → `seed (0 columns)`)
- book/src/feature/output-product.md (edited ×2 — waveguide-mode cohort bullet verb+column `rough-in`/`seed` → `firm`; closing cohort summary "five firm" → "all six firm")

Gate hits:
- citecheck (--scan, bounds + path-hygiene): PASS — 2 ok, 0 failing. No MISS/AMBIG/OOB. (DRIFT is anchor-level / upstream territory; --scan reports bounds only. Critic had already re-verified the lone load-bearing citation `boundarymodesolver.cpp:273-340` via `--anchor 'GetPropagationConstant'` → [ok].)
- flipped-cell-matches-referenced-chapter-Status (per-report safety net): PASS — verified on disk THIS invocation: `feature/waveguide-mode.L4.md` rank: firm + ## Status firm; `feature/waveguide-mode.L1.md` rank: firm + ## Status firm; `book/src/L4/waveguide_mode_reduce.md` firmness: firm + edges.rank: firm + ## Status firm. The flips are honest (faithful-or-finding satisfied).
- feature_root: seed KEPT: PASS — confirmed; only `rank:` + prose maturity tokens flip on waveguide-mode.L0; the GC-root marker preserved (the report KEEPS it on all three levels; L4/L1 unchanged this dispatch).
- forward-edge / cross-reference integrity: PASS — the `../L4/waveguide_mode_reduce.md` links newly introduced into index.md + output-product.md + L0 Status all resolve on disk (the `../L4/` pattern already in use in both files). No SUMMARY change needed (all 3 waveguide-mode chapters + the reduce verb already wired).
- rank-invariant (Axis 1): PASS by inspection — waveguide-mode.L0 `firm` (rank 3); its sole `depends-on` edge is `cites-evidence` to the rank-terminal L0 source range (rank(u) ≤ rank(v) holds vacuously). Consistent with the firm-L0 sibling convention (sparameters.L0 / eigenfrequency-qfactor.L0 / energy-fields.L0 / capacitance.L0 all firm + feature_root: seed on disk). Did NOT re-run the linter binary (no new depends-on into the live graph; D1's GMG landing already ran the full reachability/rank linter this cycle).

D1 firm-count reconciliation (the dispatch's load-bearing reconciliation ask):
- D1 landed earlier this cycle, adding a NEW "Infrastructure / shared-substrate columns" by-kind grouping + the GMG matrix row (rank: rough-in, L0 cell `—`) to `feature/index.md` (matrix-table rows, lines 58-59 on disk).
- D9's "firm 12→13, seed 1→0" arithmetic is the FEATURE-COLUMN kind firm/seed split (driver-leaf + output-product + spine-ROOT), and is CORRECT AS-AUTHORED post-D1: GMG landed `rough-in` in a SEPARATE Infrastructure kind, so it is NEITHER firm NOR seed in that split — it does NOT participate in the 12→13 tally. Verified on disk: D1 did NOT touch the Chapter-kind-status firm/seed block (lines 79-84 still read "firm (12 columns)" / "seed (1 column)" pre-D9). D9's 4 `feature/index.md` `[old]` anchors (cohort bullet, "remains seed" prose, "firm (12 columns)" header, the seed block) ALL matched on-disk verbatim — D1's matrix-table edits did not shift D9's prose-paragraph anchors. No anchor re-location needed. The post-D9 firm count is 13 feature-columns (1 spine-ROOT + 6 driver-leaf + 6 output-product); GMG remains separately tracked as `rough-in` in the Infrastructure grouping (NOT folded into the 13).

Open questions promoted: NONE (all 4 items in the report's §Open-questions are coordination/verification notes already discharged):
- shared-file coupling (D1↔D9 on feature/index.md) — DISCHARGED this invocation: anchors anchor-distinct, no collision (see D1 reconciliation above).
- OQ `waveguide-mode-reduce-needs-l4-verb-home` RESOLVED — ALREADY marked CLOSED-RESOLVED in scaffolding/open-questions.md (line 1578, c118 D5 closure); no re-append needed (the report's "if still listed open, mark closed" condition is already satisfied).
- "no SUMMARY change needed" + "13 columns total verified" — informational, no ledger action.

Build-relevant: yes (touches book/src/*.md — 3 feature-Part files edited)

Notes:
- overall_status was `ready` (canonical) from the critic directly (META checks all 8 pass; no repairer pass needed — clean all-pass report, the critic-sets-ready path). Applied cleanly as authored.
- Pure liveness/honesty-hygiene reconciliation: no new constructive claim, no new citation, no new chapter. Flips stale maturity tokens to the firm reality independently confirmed against the referenced chapters' on-disk ## Status.
- deferred integrated_at to finalize per role-spec (did NOT touch the consumed report's frontmatter integrated_at / integration_commit).

---

## 2026-06-07T054924Z-layer-intro-author-re10-interpolator-ground
applied_at: 2026-06-07T073000Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/divfree-projector.md (edited ×2 — (1) frontmatter: added `depends-on` edge `target: book/src/L1/interpolator.md` / `kind: uses` after the `L1/axpy` entry, before `reference:`; (2) §Dependencies L1-internal list: added `[interpolator](./interpolator.md)` bullet — the `P.Grad` discrete-gradient construction `uses` edge, build-time-vs-run-time distinction from apply_linop)
- book/src/L4/waveguide_mode_reduce.md (edited ×2 — (1) frontmatter: added `depends-on` edge `target: book/src/L1/interpolator.md` / `kind: uses` between the `L4/eigsolve` composes edge and the `cites-evidence` source edge; (2) §Dependencies prose: added the "one exception with a firm L1 home" sentence wiring `[interpolator](../L1/interpolator.md)` as the L4→L1 altitude-skip `uses` edge behind the `Bz` discrete-curl `CurlOp`)

Gate hits:
- citecheck (--scan, bounds + path-hygiene): PASS — 7 ok, 0 failing. No MISS/AMBIG/OOB. The two load-bearing source citations (`divfree.cpp:117`, `boundarymodesolver.cpp:319-323`) are in-bounds; the bare-basename `interpolator` AMBIG the planner flagged is disambiguated by the full `book/src/L1/interpolator.md` target paths in both edges. (DRIFT is anchor-level/upstream; --scan reports bounds only.)
- graded-stack reachability GC (Axis 2) — THE RE10 DISCHARGE, CONFIRMED on the post-apply tree: `L1/interpolator` is now ABSENT from BOTH garbage lists (STRONGER-GARBAGE-SIGNAL list now 18 nodes; edge-untyped detritus list). `--show-inbound` shows `L1/interpolator <- L1-L0/interpolator-construction-rotation, L1/divfree-projector, L1/multigrid-relaxation-smoother, L4/waveguide_mode_reduce` — both NEW `depends-on (uses)` edges (divfree-projector, waveguide_mode_reduce) resolved + propagated liveness (plus the D3-landed multigrid-relaxation-smoother, which also names it). The mutual-pair lowering theme `L1-L0/interpolator-construction-rotation` ALSO dropped off the garbage list (transitive liveness via its inbound `<- L1/interpolator`). RE10 = DISCHARGED. (Whole-artifact: 119 detritus / 61 untyped — bounded type-the-edges baseline, not a per-report gate; linter exit 0.)
- graded-stack rank linter (Axis 1): PASS — RANK VIOLATIONS: none. Both new edges are firm→firm: `L1/interpolator` rank firm (3), consumers `L1/divfree-projector` rank firm (3) + `L4/waveguide_mode_reduce` firmness firm / edges.rank firm (3). `rank(u) ≤ rank(v)` holds at 3≤3 for both — well-foundedness intact.
- edge-label / faithful-edge check (the focus, re-confirmed against on-disk source via the report's verified anchors + on-disk file reads this invocation): PASS — edge 1 (`divfree.cpp:117` = `Grad = &nd_fespace.GetDiscreteInterpolator(...)`) and edge 2 (`boundarymodesolver.cpp:319-323` = `GetDiscreteInterpolator(mode_op.GetNDSpace())` forming the `Bz` curl) are both genuine `GetDiscreteInterpolator` (= `interpolator`-operator) calls. The `uses` kind-label is faithful (build-time construction dependency, distinct from run-time apply). The L4→L1 altitude-skip on edge 2 is justified by waveguide_mode_reduce's own §Lowers-to (identity-in-form on the body, no intervening L3/L2 absorption) — read on disk this invocation. NOT a forced edge.
- forward-edge / cross-reference integrity: PASS — both new prose links resolve on disk: `[interpolator](./interpolator.md)` (divfree-projector, same-dir L1) and `[interpolator](../L1/interpolator.md)` (waveguide_mode_reduce, L4→L1 relative). `book/src/L1/interpolator.md` confirmed present on disk (linter inbound list resolves it). No SUMMARY change needed (all three chapters already registered; this is an edge-typing GROUND, no new chapter).

Open questions promoted (2, appended to scaffolding/open-questions.md):
- interpolator-backward-reference-note-redundant-after-ground
- interpolator-re10-discharge-c122-linter-re-measure

Build-relevant: yes (touches book/src/*.md — 2 chapters edited, frontmatter + prose)

Notes:
- overall_status was `ready` (canonical) from the critic directly (META all 8 checks pass; clean all-pass report, the critic-sets-ready path — no repairer pass). Applied cleanly as authored.
- RE10 DISCHARGE CONFIRMED ON THE LANDED-SO-FAR TREE: `L1/interpolator` is off the STRONGER-GARBAGE list (now 18) and reachable via the two new consumer edges; the report's pre-edit prose estimate ("STRONGER 27→25 / +2") was a producer estimate — the authoritative post-batch STRONGER-count delta vs the c122 pre-batch baseline is the c122 planner's standing RE-premise re-check (OQ `interpolator-re10-discharge-c122-linter-re-measure`). The load-bearing fact (interpolator flipped OFF garbage → RE10 discharged) is verified here at apply.
- The redundant backward `reference` note at `interpolator.md:23` was deliberately left as-is (no edit to interpolator.md in D8 scope; the authoritative forward edges live on the consumers per "edge belongs on the consumer" discipline) — flagged for a future dep-map refresh (OQ `interpolator-backward-reference-note-redundant-after-ground`).
- No edit collision with prior c121 landings: D8 touches `L1/divfree-projector.md` + `L4/waveguide_mode_reduce.md`, neither touched by the earlier D3/D1/D2/D9 rows. (D3's multigrid-relaxation-smoother independently names `L1/interpolator` as a `depends-on` dep — visible in the inbound list — but in its own file, no overlap; observed directly via the linter inbound output this invocation.)
- deferred integrated_at to finalize per role-spec (did NOT touch the consumed report's frontmatter integrated_at / integration_commit).

---
## 2026-06-07T054924Z-abstractor-libceed-quadrature-kernel-impl
applied_at: 2026-06-07T074500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/libceed-quadrature-kernel-impl.md (created — new kernel-impl node, rank: roadmap_goal (rank-0); full chapter: Status, L1 form (5-stage Gᵀ Bᵀ D B G contraction pipeline), Applicability, Justification, 4 speculative substrate ops, Verified-against, Related; edges: 4 reference (realizes-kernel-api → obstruction theme; realizes-leaf → fe_assemble; weak_form_term; tensor-field-lift) + 4 depends-on (composes) at the not-yet-existing substrate slugs)
- book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md (edited ## Status opening sentence — added `kernel-api` role-label + back-link to the kernel-impl node; KEPT `obstruction (opaque-library-ownership)`, NOT downgraded; "The entire callable that…" continuation intact)
- book/src/SUMMARY.md (edited — inserted `[libceed-quadrature-kernel-impl]` in the FE-assembly sub-spine block, alpha position after `fe_assemble`, before `weak_form_term` (f < l < w))
- book/src/L1/index.md (edited ×2 — (a) dep-map row inserted after the `fe_assemble` row, before the `weak_form_term` row, in FE-assembly sub-spine alpha position; (b) §Vocabulary-cohort bullet appended after the `eliminate_rhs` bullet, before the FE-space sub-spine header)

Gate hits:
- citecheck (--scan, bounds + path-hygiene): PASS — 14 ok, 0 failing. No MISS/AMBIG/OOB. (All libceed integrator.cpp ranges + the EvalMode hpp enum + bilinearform.cpp operands in bounds. Critic independently re-verified every load-bearing pinpoint via codemap read_range with zero drift; --scan reports bounds only.)
- graded-stack rank linter (Axis 1): PASS — 0 rank violations. The new node is rank-0 (`roadmap_goal`), so the well-foundedness invariant `rank(u) ≤ rank(v)` is VACUOUSLY satisfied for every `depends-on` edge. The 4 substrate `depends-on` targets (element_restrict / basis_apply / quad_point_contract / geom_factor_build) read `[UNRESOLVED]` (no file yet) — WARNING, NON-strict, linter exit 0 — exactly as authored (speculative roadmap-deps, harvester promotion targets). NO false firm/rough-in claim on any substrate dep. The node also appears in the Axis-1 PROMOTION FRONTIER (8) list — correct disposition.
- realizes-kernel-api edge-class check: PASS — confirmed `reference`-class (under `edges.reference:`, kind `realizes-kernel-api`), NOT `depends-on`. Confirmed EXCLUDED from rank + liveness by direct linter evidence (the node reads `[GARBAGE*]` on Axis-2 PRECISELY because the `realizes-*` reference inbound edges do NOT carry liveness — see next gate). The companion `realizes-leaf` edge (impl → fe_assemble) is likewise `reference`-class.
- graded-stack reachability GC (Axis 2): node `L1/libceed-quadrature-kernel-impl` shows `[GARBAGE*]` (STRONGER-GARBAGE list, 19 nodes) — EXPECTED + BENIGN + INTENDED per DIRECTIVE-3. Its only inbound edges are the FREE `realizes-kernel-api` / `realizes-leaf` reference edges (do NOT carry liveness), so the mark from feature roots over `depends-on` does not reach it; its own 4 `depends-on` substrate targets are unresolved. This is the correct disposition for a kernel-impl whose spine correspondence is a *reviewed reference*, not a build dependency. Grounded-future per `feedback_gc_ground_dont_remove_future_deps` (ground via the realizes-leaf correspondence + substrate-mining pull; do NOT remove). NOT a defect. (Whole-artifact baseline: 120 detritus / 61 untyped — the bounded type-the-edges adoption campaign, NOT a per-report gate; linter exit 0.)
- obstruction-theme disposition check: PASS — `fe-assemble-libceed-boundary-obstruction.md` STAYS `status: obstruction (opaque-library-ownership)` (verified the find/replace preserved the sub-kind tag); the ONLY change is the `## Status` opening gaining the `kernel-api` role-label + the back-link. NOT downgraded, NOT promoted.
- firm-count check: PASS — FE-assembly sub-spine firm count stays 4 (this node is rank-0 roadmap_goal, not firm). The index grand-total tally (43 firm) is untouched.

Open questions promoted (5, appended to scaffolding/open-questions.md):
- libceed-quadrature-kernel-impl-realizes-leaf-reference-label  (→ c122 lowering-verifier/meta-phase: the new `realizes-leaf` reference-edge label methodology question)
- libceed-quadrature-kernel-impl-roadmap-goal-vs-rough-in-disposition  (→ c122 planner: re-eval promotion if D6 substrate-probe surfaces firm-composable substrate)
- libceed-quadrature-kernel-impl-reachability-grounding-confirm  (→ c122 lowering-verifier/planner: confirm grounded-future, not swept; the GARBAGE* is intended)
- libceed-quadrature-kernel-impl-realizes-api-faithfulness-audit  (→ c122 lowering-verifier impl-realizes-API audit; pairs with the D3 smoother realizes-kernel-api audit)
- libceed-quadrature-kernel-impl-sum-factorization-classification  (→ harvester, when basis_apply is mined: confirm sum-factorization is transparent-not-load-bearing)

Build-relevant: yes (touches book/src/*.md — 1 new L1 chapter + 3 edits)

Notes:
- overall_status was `ready` (canonical) — set by the critic directly on an all-pass clean report (all 8 META checks pass; the critic-sets-ready path, no repairer pass needed). Applied cleanly as authored.
- DIRECTIVE-3 kernel-API/impl dual-surface landing: the kept obstruction theme (kernel-api, role-labeled this dispatch) + the new constructive kernel-impl node, linked by the free `realizes-kernel-api` reference edge. The obstruction stays the opaque CONTRACT; the impl is the from-our-tensor-algebra realization; the correspondence is reviewed (lowering-verifier c122 audit OQ promoted). This is the libCEED-quadrature founding kernel of the DIRECTIVE-3 dual-surface set (parallel to the D3 triangular-solve/GS-SSOR smoother + the forthcoming SLEPc eigsolve impl).
- The 4 substrate `depends-on` targets are deliberately at not-yet-existing slugs (the combinator-miner D6 shared-substrate probe of THIS cycle is designed to mine them once across the D3 relaxation / D4 contraction (this) / D5 Krylov kernel-impls). Their `[UNRESOLVED]` linter WARNING is the declared-future-dep state the graded stack tracks; non-blocking (exit 0, non-strict).
- No edit collision with prior c121 landings: D4 touches L1/libceed-quadrature-kernel-impl.md (new), L1-L0/fe-assemble-libceed-boundary-obstruction.md, SUMMARY.md (FE-assembly block), L1/index.md (FE-assembly dep-map + cohort). None of the earlier D3/D1/D2/D9/D8 rows touched the obstruction theme or the FE-assembly sub-spine SUMMARY block; the SUMMARY/index anchors all matched on-disk verbatim this invocation (read this invocation, not assumed).
- deferred integrated_at to finalize per role-spec (did NOT touch the consumed report's frontmatter integrated_at / integration_commit).

---

## 2026-06-07T054924Z-abstractor-eigsolve-kernel-impl
applied_at: 2026-06-07T064500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3/eigsolve-impl.md (created — new kernel-impl node, rank-0 roadmap_goal; full chapter: Intent, kernel-impl form, Correspondence-to-API table, Pulled-by, Status, Evidence. `realizes-kernel-api` declared impl→api under `reference:` key → L3/eigsolve + L4/eigsolve.)
- book/src/L3/lanczos_step.md (created — new kernel-impl-constituent node, rank-0 roadmap_goal; specializes krylov-step to the symmetric band-3 recurrence. depends-on includes L1/scal — the repairer-added edge — confirmed present in frontmatter + Status + Evidence.)
- book/src/L3/eigsolve.md (edited ## Status line 191 — prepended the `kernel-api` DIRECTIVE-3 role-label sentence; `partial-obstruction` status UNCHANGED (frontmatter `firmness: partial-obstruction` untouched). Frontmatter edge handling PROSE-ONLY per the report's integrator note + critic verification — the realizes-kernel-api edge is authoritatively impl→api; no outbound api-node edge needed by the linter.)
- book/src/L3/index.md (edited — inserted eigsolve-impl dep-map row after the `eigsolve` row (before fold_solve) in the "Solver capabilities & field transitions" group at alpha position; inserted lanczos_step row after the `ksp_solve` row (before orthogonalize) — `la` > `ks` > `kr`, < `or`. lanczos_step row's constituent list includes scal per the repairer fix.)
- book/src/SUMMARY.md (edited — added `eigsolve-impl` 2-space-nested entry after `eigsolve` (before fold_solve); added `lanczos_step` after `ksp_solve` (before orthogonalize). Alpha positions match the repairer-corrected instruction; on-disk SUMMARY group was at lines 124-128, NOT the report-stated 121-125 — the alpha-position content governed, applied to actual on-disk lines.)

Gate hits:
- citecheck bounds + path-hygiene (--scan): PASS — 21 ok, 0 failing (21 citations checked). No MISS/AMBIG/OOB. Confirmed incl. slepc.cpp:635 EPSSetType KRYLOVSCHUR, slepc.cpp:694/731/607/613, arpack.cpp:318/270/369. (DRIFT not in --scan scope; pinpoint-anchor territory, caught upstream.)
- realizes-kernel-api edge-class check: PASS — edge is under `reference:` key in eigsolve-impl.md frontmatter (NOT `depends-on:`), reference-class, constrains neither rank nor liveness. Confirmed in frontmatter + the Pulled-by note + Status + the Correspondence-to-API section. Direction impl→api correct.
- kernel-api status-preservation check: PASS — L3/eigsolve stays `partial-obstruction` (frontmatter `firmness: partial-obstruction` unchanged; Status line keeps `partial-obstruction` + adds the `kernel-api` role-label sentence that explicitly states "status is UNCHANGED"). NOT downgraded, NOT promoted.
- graded-stack rank linter (Axis-1 well-foundedness): PASS — 0 violations. eigsolve-impl is rank-0 roadmap_goal; per the well-foundedness invariant a rank-0 node may rest on ANYTHING (rank 0 ≤ all), so resting on firm krylov-step/ksp_solve/apply_linop/L2/orthogonalize AND the co-cycle rank-0 roadmap_goal lanczos_step is permitted (resolution-ladder.md:75-76). lanczos_step (rank-0) rests on firm krylov-step/apply_linop/dot/nrm2/axpy/scal — fine. The `lanczos_step → L1/scal` edge resolves (L1/scal.md exists on disk, firm).
- reachability (Axis-2): WARNING (non-blocking, intended) — both new roadmap_goals land with NO blocking inbound consumer this cycle; only inbound is the reference-class realizes-kernel-api / pulled-by edges (free, non-liveness-bearing). This is the SANCTIONED grounding disposition (feedback_gc_ground_dont_remove_future_deps) — genuinely-wanted future deps of the eigenmode root. NOT a defect; the c122 consumer-wiring grounding-trigger OQ is promoted so the meta-phase RE-recheck + c122 GC sweep pick it up. (Matches the parallel c121 D4 libceed reachability-grounding disposition.)
- SUMMARY chapter registration: both new chapters registered (no auto-fix needed — the report proposed both SUMMARY entries).
- link-target resolution (manual): PASS — all live-link targets exist on disk (L1/scal, L1-L0/minres-iteration, L2/orthogonalize, L3/{krylov-step,ksp_solve,apply_linop}, L4/eigsolve, feature/eigenmode.L4, L1/{dot,nrm2,axpy}).

Open questions promoted:
- eigsolve-impl-c122-consumer-wiring-grounding-trigger  (the RE3/RE8 c122 grounding-trigger — for the meta-phase RE-recheck, per dispatch instruction)
- eigsolve-impl-lanczos-step-materialization-route
- eigsolve-impl-lowering-verifier-correspondence-audit  (DIRECTIVE-3 kernel-api/impl-integrity audit cohort — pairs with the c121 multigrid/libceed audit OQs)
- eigsolve-impl-rayleigh-ritz-thick-restart-promotion  (+ the iterate_while_L3-over-basis-extension D6 shared-substrate candidate)

Build-relevant: yes

Notes: DIRECTIVE-3 item-2c constructive-kernel frontier opener — the SLEPc-EPS eigsolve kernel now has BOTH surfaces (opaque kernel-api L3/eigsolve + constructive kernel-impl L3/eigsolve-impl), reviewably linked by the reference-class realizes-kernel-api edge. Report was repaired (2 surgical fixes: lanczos_step→scal dep added; lanczos_step alpha-insert position corrected to after-ksp_solve/before-orthogonalize) — both repairs verified landed in the applied content. overall_status `ready` (canonical, repairer-set after fixes). NOTE on SUMMARY line drift: the report's stated SUMMARY lines (121-125) were stale vs on-disk (124-128, shifted by prior structure) — I applied via byte-anchored Edits on the actual on-disk sibling lines I read this invocation, so the inserts are correct regardless of the report's line numbers. The L3/eigsolve.md §Status line anchor (report said line 191) matched on-disk verbatim. Deferred integrated_at to finalize per role-spec.

---

## 2026-06-07T054924Z-combinator-miner-kernel-shared-substrate
applied_at: 2026-06-07T065939Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/index.md (insert one dep-map row — L2 combinator `correction_step` rough-in)
- scaffolding/open-questions.md (append 4 OQs)

Gate hits:
- citecheck bounds + path-hygiene lint: 0 (17 ok, 0 failing — no MISS/AMBIG/OOB)
- forward-edge-claim-without-surface: 0 (plain-text/inline-code slug, deliberately NO live link — chapter NOT authored this cycle, harvester formalizes later; no linkcheck2 risk)
- concept_writes / append-on-missing-slug / variant-axis / H1-reuse / index-placeholder / SUMMARY-registration: 0 (n/a — single dep-map row in an existing index table, no new chapter file, no SUMMARY entry needed)
- retroactive-budget: 0
- alpha-position-insert: applied-discretionarily (the critic flagged the row carried no kind-group/alpha hint; placed in the `### Step kernels` group, alpha between `chebyshev-iteration` and `krylov-step` — `correction_step` is a step-kernel combinator sibling of both, sorts c-h-e-b < c-o-r-r < k-r-y; rationale: alpha-position-insert)

Open questions promoted:
- correction-step-replace-and-propagate-scope
- correction-step-one-vs-two-operator-conjugated-form
- correction-step-construction-vs-apply-stratum-assemblediagonal-reciprocal
- correction-step-divfree-projector-borderline-7th-instance

Build-relevant: yes

Notes: D6 of the c121 wide all-fronts fan-out — combinator-miner shared-substrate mine (DIRECTIVE-2 lift-through; the L2 `correction_step` = `y + B·(x − A·y)` per-sweep body Palace names verbatim at gmg.cpp:174-176 + distrelaxation.cpp:104, the shared core across the smoother family + multigrid V-cycle level body). Landed as a SINGLE rough-in dep-map row only (no chapter authored — that is the harvester's formalization pass, OQ correction-step-replace-and-propagate-scope routes it). overall_status `ready` (canonical, all-pass clean — critic set directly, no repairer ran). Graded-stack rank gate: correction_step (rough-in, rank 2) rests on apply_linop + axpby (both firm, rank 3) — rank(u)=2 ≤ min(deps)=3 holds, no violation. The row's deps/signature/status text were pre-written by the producer; my only discretionary act was the kind-group + alpha placement (critic minor-flag 1). Replace-and-propagate is FLAGGED not enacted (correct-by-role for a rough-in row — the row cannot rewrite sibling chapters; routed to harvester + same-layer-cross-cutter via the propagation-scope OQ). On-disk verification: I read book/src/L2/index.md this invocation and confirmed the `### Step kernels` group + the chebyshev-iteration/krylov-step siblings as the anchor; no claim made about sibling-report landings (D6 touches a different file region than the D1-D5/abstractor rows above — L2/index.md was not touched by any prior c121 staging row). Deferred integrated_at to finalize per role-spec.

---

## 2026-06-07T054924Z-abstractor-amr-estimate-mark-refine
applied_at: 2026-06-07T064500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/amr-estimate-mark-refine.md (created — new L1>L0 lowering theme, rough-in; the estimate/mark/refine step-body lowering. Full chapter: 3-way A estimate (ZZ flux-recovery)/B mark (Dörfler bulk)/C refine (MFEM-opaque obstruction) split; `## Record definition` for AmrCarry/RefineConfig/Estimator/IndexSet[E]; outer loop NOT re-homed (already firm L4 fold_solve state-generated))
- book/src/SUMMARY.md (edited — added 2-space nested entry `amr-estimate-mark-refine` as alpha-FIRST child of the Construction-rotation themes sub-group, before build-mesh-construction-rotation)
- book/src/L1-L0/index.md (edited — inserted theme-list row alpha-FIRST in the **Construction-rotation** group, before build-mesh-construction-rotation row)
- book/src/L1/index.md (edited — added a new **Rough-in (AMR estimate/mark vocabulary)** dep-map sub-group after the Rough-in (obstruction) group, with 2 plain-text rough-in rows `dorfler_mark` + `flux_recovery_estimate`, alpha-ordered, no live-link anchor per the rough-in-rows-must-be-plain-text convention)

Gate hits:
- citecheck bounds + path-hygiene lint: PASS — `python3 tools/citecheck/citecheck.py --scan <CYCLE.md> --quiet` → 21 ok, 0 failing. No MISS/AMBIG/OOB. (Producer/critic used codemap `search_text` not `read_range` to avoid the +1 brace drift on basesolver/dorfler/errorestimator ranges; bounds scan confirms all ranges resolve.)
- graded-stack rank linter (Axis 1): PASS — 0 rank violations. New theme node is `rough-in` (rank 2); its `depends-on` deps L1/flux_recovery_estimate + L1/dorfler_mark are rough-in (rank 2, the speculative cohort); rank(theme)=2 ≤ min(deps)=2 holds (well-foundedness: a lowering theme is at most as resolved as its least-resolved endpoint, scheme §5). The 4 `reference` edges (fold_solve, lifecycle.L4, triangular-solve-obstruction, fe-assemble-libceed-boundary-obstruction) are reference-class, constrain no rank. The refine obstruction sub-leaf is a documented boundary, not a depends-on, does NOT gate.
- live-link-to-non-existent-file check: PASS — grep-confirmed NO live markdown links to L1/flux_recovery_estimate.md or L1/dorfler_mark.md remain in the new chapter (repairer de-linked the prose to plain-text forward-refs; the 2 dep-map rows are plain-text). The preserved live links (../L4/fold_solve.md, ../feature/lifecycle.{L4,L0}.md, ./triangular-solve-obstruction.md, ./fe-assemble-libceed-boundary-obstruction.md, ../L1/nrm2.md, ../L1/ksp_solve.md) all resolve on disk → clean rebuild expected.
- SUMMARY/index Construction-rotation placement: PASS — SUMMARY + L1-L0/index BOTH land amr-estimate-mark-refine in the Construction-rotation sub-group, alpha-first (mixed-kind theme: estimate/mark constructive endpoints dominate; refine obstruction sub-leaf is a documented boundary, not the theme's kind). Repairer reconciled the original ambiguous flat-list "amr before apply" instruction onto this single landing group consistently across both files.
- new-SUMMARY-kind-grouping group-intro: N/A — no NEW by-kind grouping opened (Construction-rotation themes group + intro page construction-rotation-intro.md already exist on disk).
- alpha-position-insert (directive-3): applied-discretionarily — the report specified alpha-first within Construction-rotation; for the L1/index.md rough-in rows the report said "append" without specifying the group, so I placed them in a new **Rough-in (AMR estimate/mark vocabulary)** sub-group (the existing **Rough-in (obstruction)** group is specifically the MINRES/BiCGStab enum-only-stub obstruction kernels — these AMR verbs are speculative-constructive vocabulary, a different kind; rationale: by-kind-grouping-preservation), rows alpha-ordered dorfler_mark < flux_recovery_estimate.
- implied-component stub materialization: NOT applied (deferred to harvest) — the 2 speculative L1 verbs are left as plain-text forward-refs + rough-in dep-map rows, NOT materialized as stub files. Rationale: the repairer already de-linked the prose so the rebuild is clean WITHOUT stubs; the report + critic + role-spec all flag stub materialization as the harvester's promotion route (OQ amr-estimate-mark-refine-theme-firmness-gate). The bar (≥2 converging references) is arguably met, but materializing now would pre-empt the harvester's record-firming + risk a claim-bearing stub; the clean-rebuild-via-de-link path is the safer fallback per the repairer's explicit integrator note.

Open questions promoted:
- flux-recovery-estimate-flux-channel-axis-vs-separate-verbs
- flux-projector-constructed-operator-gate-vs-absorbed
- dorfler-cross-rank-bisection-distributed-note-deferred
- amr-refine-obstruction-sub-kind-precedent
- amr-estimate-mark-refine-theme-firmness-gate

Build-relevant: yes

Notes: FINAL report of cycle-121 (D7, DIRECTIVE-2 grounded consumer-(2) AMR front opener). Clean apply, all per-report gates PASS, overall_status `ready` (canonical, repaired — repairer added in-chapter `## Record definition`, de-linked the speculative-op prose, reconciled SUMMARY/index onto the Construction-rotation group). No `roadmap_goal` authored for the AMR loop (correctly — already firm L4 fold_solve state-generated home; re-homing = degenerate-identity smell, confirmed by critic against fold_solve.md:20 / lifecycle.L4.md:52 / lifecycle.L0.md:39-42 / spine-root.md:21). Theme firms when both L1 verbs (flux_recovery_estimate, dorfler_mark) are harvested firm (c122+). I observed on disk: the Construction-rotation group + its intro already present (no group-intro stub needed); the prior 6 staging rows all `applied`; my edits to SUMMARY/L1-L0/index/L1 targeted byte-disjoint anchors from the prior multigrid/libceed/fe-space-hierarchy landings (re-read each file this invocation before editing). Deferred integrated_at to finalize per role-spec.

---
