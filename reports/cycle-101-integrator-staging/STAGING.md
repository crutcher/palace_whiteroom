# Cycle-101 integrator staging log

Per-report integrator rows, append-only, newest LAST. The row ORDER is the authoritative apply-order record (NOT the `applied_at` timestamps). integrator-finalize reconciles from this log.

---

## 2026-06-05T054154Z-harvester-bc-elimination-l4-disposition
applied_at: 2026-06-05T060521Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/eliminate_bc.md (new — firm L4 chapter, two co-equal verbs eliminate_essential_bc + eliminate_rhs; firm-on-positive-structure escape)
- book/src/L4-L3/bc-elimination-post-composition-dissolution.md (new — firm L4>L3 theme, DISSOLUTION-HOME verdict, no L3/eliminate_bc)
- book/src/L4/fe_assemble.md (edit — 3 sites: essential_dofs mis-attribution corrected to two construction inputs fe_space/fe_collection at :69 + status line; essential_dofs re-stated as post-assembly cohort feeder; c069 deferral re-anchored to the now-firm eliminate_bc cap in the "BC-elimination is NOT part of the fold" law)
- book/src/L4-L3/fe-assemble-fold-dissolution.md (edit — c069 deferral re-anchor: BC-elimination bullet now points to firm eliminate_bc + sibling bc-elimination-post-composition-dissolution theme)
- book/src/L4/index.md (edit — dep-map row for eliminate_bc, inserted in ALPHA position between eigenfreq_qfactor_reduce and fe_assemble; NOT the report's proposed after-fe_assemble append)
- book/src/L4-L3/index.md (edit — theme-list table row + Substantive-themes bullet, both inserted in ALPHA position FIRST/before fe-assemble-fold-dissolution; NOT the report's proposed after-fe_assemble append; consolidated tally replaced 9→10 (c070-era) with 10→11 firm themes)
- book/src/SUMMARY.md (edit — L4 chapter entry eliminate_bc between eigenfreq_qfactor_reduce and fe_assemble [alpha]; L4-L3 theme entry bc-elimination-post-composition-dissolution between Overview and fe-assemble-fold-dissolution [alpha])
- scaffolding/open-questions.md (append — 2 OQ sections)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- H1-reuse: 0
- append-on-missing-slug: 0
- variant-axis-missing: 0
- citecheck: 44 ok, 0 failing (no MISS/AMBIG/OOB)
- rank-invariant: PASS (eliminate_bc firm rests on linear_combination firm via the one blocking depends-on edge; fe_assemble edge is reference, non-blocking. L4>L3 theme firm rests on the firm cap + two firm L1 sources)
- alpha-position-insert: applied-discretionarily ×4 (see Notes)
- SUMMARY-registration: both new chapters registered (report proposed both; alpha-corrected)

Open questions promoted:
- record-DofSet-needs-definition-home
- eliminate-rhs-mutation-rotation L1>L0 half — forthcoming-vs-already-folded

Build-relevant: yes

Notes:
- ALPHA-POSITION-INSERT (applied-discretionarily, rationale alpha-position-insert): the report's proposed-changes placed the new dep-map/theme-list/bullet rows AFTER fe_assemble / fe-assemble-fold-dissolution (the prior append-after convention). The L4/index.md dep-map table (from line ~96) and the L4-L3/index.md theme-list table + Substantive-themes bullet list are BOTH alphabetically ordered on-disk. Per the directive-3 alphabetical-position-insert rule, I placed each row in alpha position instead: eliminate_bc between eigenfreq_qfactor_reduce and fe_assemble in L4/index.md (e-l-i < f); bc-elimination-... FIRST (before fe-assemble-...) in the L4-L3/index.md table AND the Substantive-themes bullet (b < f). SUMMARY entries were already alpha-correct as the report proposed them. Recorded discretionary; the four index/bullet repositions are alpha-local-correct.
- TALLY RECONCILIATION: the report's tally edit-block supplied a NEW paragraph reading "10 → 11 this cycle" with 11 firm themes. The on-disk tally read "9 → 10 this cycle" (c070-era, ending at frequency-sweep). I replaced the full on-disk tally paragraph with the report's 10→11 paragraph (which correctly enumerates all 11 incl. the new bc-elimination theme and re-attributes the row/bullet/tally as D1-authored). The report's old_string did not match on-disk verbatim; treated as a full-paragraph replace of the single tally line.
- INTENTIONAL PLAIN-TEXT (not a broken link): the `eliminate-rhs-mutation-rotation` L1>L0 reference in both new files is plain text per the missing-anchor convention — NOT a [link], confirmed no linkcheck hazard. The OQ ledger (existing fe-bc-elimination-l1-l0-theme-split-vs-fold + c065/c066 unification notes) records that bare name as a non-existent-file residue — the RHS-side leg already folds inline into the firm fe-operator-assemble-mutation-rotation.md. I promoted this as an OQ cross-referencing the existing split-vs-fold item (NOT a fresh independent item) so finalize/meta-phase reconcile the naming.
- record-DofSet OQ relates to existing kept-deferred dof-set-concept-page / fe-bc-dof-set-and-set-subvector-concept-pages (c055 cohort) — same record, re-triggered by the new L4 cap consumer; flagged for meta-phase unification.
- THIRD report caveat NOT promoted to OQ ledger (recorded here for layer-intro-author per the report's own framing): L4/index.md §Vocabulary-cohort firm-count narration ("Firm at L4 (19 + 4 outer-driver)") + the §"Cycle-068 (batch-21)" narrative block should increment / gain a cycle-101 BC-application-half entry. This is a non-blocking prose refresh in layer-intro-author's domain (the report added only the dep-map row + L4>L3 tally it owns); flagged, not edited.
- DofSet[N] / DiagPolicy / the b−K·x_bc unicode minus (−) and ParOperator/HypreParMatrix names round-trip; both new-file YAML frontmatters parse via yaml.safe_load (firmness: firm).
- All 15 referenced link targets verified present on disk (fe_assemble, linear_combination, the 4 concept pages, essential_dofs, apply_linop, the two firm L1 BC sources, fe-operator-assemble-mutation-rotation, ksp_solve, eigsolve, divfree-projector, fe_space).
- Deferred integrated_at to finalize per role-spec (also integration_commit). Did not rebuild book, did not commit.

---

## 2026-06-05T054115Z-layer-intro-author-concepts-depmap-refresh
applied_at: 2026-06-05T064500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/index.md (edit — Edit-A: header/why/lifecycle/concept-file-format/Index-note rewrite, strip pre-redirect orchestrator + slice-era framing → 14-agent Claude Code pipeline + layered L4→L0 + lowering Parts + feature spine + concept-pages-as-data-shape; the ../spec/slices/X.md format-example links + the concept_writes/orchestrator grep recipe removed. Edit-B: `algorithm` Kind one-liner de-slice-ified (dropped gmres example). Index Kind table left intact — 51 rows.)
- book/src/concepts/dependency-map.md (edit — Edit-A: intro re-derive, strip Synthesizer/Meta-Critic/Planner + prompts/* provenance + the 3-purpose forward-projection framing → 2-purpose + light depends-on/reference edge convention. Edit-B: replaced the entire `## Intermediate-tier algorithms (planned)` + L1/L2/L3/L4 slice-slug Mermaid block (~115 edges) with two re-derived sub-graphs — `## Primitives + algorithms` + `## Layer patterns + records` — anchored to on-disk concept pages; the duplicate-titled section renamed to `## L4 calculus + feature spine (tracked elsewhere)`. Edit-C: Maintenance-protocol + Origin rewrite to layer-intro-author/integrator/meta-phase + graded-stack reachability linter.)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0 (light depends-on/reference typing is in-prose-consistent; NOT the meta-phase graded-stack full typing campaign — report disclaims, OQ caveat flags reconcile-when-campaign-lands)
- H1-reuse: 0
- append-on-missing-slug: 0
- variant-axis-missing: 0
- SUMMARY-registration: 0 (no new concept page created; both targets are existing infra files)
- alpha-position-insert: 0 (Index Kind table left intact by the report; no row inserted)
- index-placeholder-displacement: 0
- citecheck: 1 ok, 0 failing (no MISS/AMBIG/OOB) — scan over CYCLE.md; the single L4/krylov-step.md:254 reference resolves
- rank-invariant: N/A (no maturity promotions; this is concepts-index + dep-map maintenance)
- reachability-GC: N/A (no node added/removed from the live graph that changes root-reachability; the re-derivation REMOVED dangling/deleted-slice nodes — improves graph hygiene)

Build-safety verification (CRITICAL gate, all PASS):
- No `../spec/slices/` reference survives in either file (grep NONE). The pre-existing slice links lived only inside the removed fenced ```markdown format-example block.
- The two `prompts/` grep hits are intentional HISTORICAL prose (the `:::planned`-retirement note + the Origin orchestrator/prompts-retirement note), not live refs.
- Exactly ONE `## Methodology concepts (cross-layer)` heading post-integration (the surviving authoritative original at on-disk lines 20-56; Edit-B's colliding section is renamed to `## L4 calculus + feature spine (tracked elsewhere)` per repairer Finding-2 fix). Confirmed grep -c == 1.
- All real prose markdown links resolve on disk: every `./<name>.md` concept link (incl. gmres.md, which exists — its Index-table row is retained), `../design/l4_calculus.md`. The `../feature/<name>.L<n>.md` + `../L<n>/<chapter>.md` are placeholders INSIDE the fenced ```markdown format-example (lines 45-64), not link targets.
- Re-derived Mermaid node set references only existing concept pages: the ONLY non-file node is `krylov-step-record` (the in-report-documented `krylov`-page readability alias, repairer-acknowledged lower-severity); the repairer-removed `reciprocal` dangling node is gone (verified `book/src/concepts/reciprocal.md` does not exist). `A`/`B` are from the prose edge-convention example, not graph nodes.
- Concept-page count verified on disk: 53 files, 51 concept pages (excl index.md + dependency-map.md) — matches the repairer-corrected "51" in the refreshed prose and the §Index table's 51 rows.

Open questions promoted: (none — the report's OQ section is explanatory caveats, not new questions; the two OQs its Summary names — concepts-index-and-depmap-orchestrator-era-framing-refresh, dependency-map-cg-precond-stale-mermaid-edges-RESCOPE-CORRECTION — are RESOLVED-by-this-report, and OQ closure is meta-phase unify authority, not per-report integrator. Flagged here for finalize/meta-phase.)

Build-relevant: yes

Notes:
- D1 (BC-elimination) landed earlier this cycle (its staging row precedes this one). I re-read both my targets off disk before editing; D1's targets (L4/index.md, L4-L3/index.md, SUMMARY.md, L4/fe_assemble.md, 2 new L4 chapters) do NOT overlap concepts/index.md or concepts/dependency-map.md — verified directly, no contention.
- CG Form-B pointer at L4/krylov-step.md:254 left untouched (report verified not stale; D2 made no edit to it and neither did I).
- Light edge-typing caveat carried forward: the depends-on/reference annotations are a light pass, NOT the meta-phase-owned graded-stack full edge-typing campaign (project_graded_stack_directive, priorities item 0). The dep-map edge set should be reconciled with that campaign when it lands; recorded so it is not mistaken for the authoritative typed graph.
- Deferred integrated_at to finalize per role-spec (also integration_commit). Did not rebuild book, did not commit.

---
