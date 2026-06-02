# cycle-055 integrator staging log

Per-report integration rows, newest LAST (append-only). `integrator-finalize` reads this to reconcile the cycle.

---

## 2026-06-02T010700Z-harvester-solve-family-firm-entry (D1)
applied_at: 2026-06-02T01:46:20Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/solve_family.md (new — `solve_family` L4 combinator chapter, `## Status: rough-in (test-coverage-bounded)`)
- book/src/L4/index.md (edit — flipped the existing `:76` `solve_family` rough-in dep-map row to a live link + `rough-in (test-coverage-bounded)` status + the `solve-family-map-dissolution` forward-ref kept plain-text; appended D1's OWN §Vocabulary-cohort bullet after the `eigsolve` bullet)
- book/src/SUMMARY.md (edit — inserted `- [solve_family](./L4/solve_family.md)` after the `eigsolve` line, inside the L4 Part before the `# L4 > L3` header)
- scaffolding/open-questions.md (append-only — D1 New-intake section)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0 (the two forward-refs `solve-family-map-dissolution` + `L3/solve_family` are correctly plain-text, NOT live links — verified on disk; D2 authors the theme this cycle, L3 image batch-17)
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (4 axes declared; operator-capture load-bearing, 3 absorbed)
- bookkeeping incomplete: 0
- citecheck bounds + path-hygiene lint: 40 ok, 0 failing (no MISS/AMBIG/OOB)
- SUMMARY.md chapter registration: registered by the report's own proposed-change (no auto-fix needed)
- index-placeholder displacement: n/a (the `:76` row was an existing firm-text rough-in row, not the `(empty — Phase B skeleton.)` placeholder)
- implied-component stub materialization: n/a (no dangling plain-text forward-ref needing a stub; the two forward-refs are deliberately-deferred to D2 / batch-17)

Open questions promoted:
- solve-family-status-firm-on-positive-structure-vs-test-coverage-bounded (NEW; routed to batch-17 lowering-verifier — KspSolver-statefulness / RHS-buffer-aliasing pass that can promote `rough-in (test-coverage-bounded)` → `firm` on the firm-on-positive-structure escape)
- map_solve superset probe (D1's OQ #2) — NOT re-opened: already migrated to the plan as `map-solve-superset-probe` (batch-17); recorded for traceability only in the New-intake append.

Build-relevant: yes (touches book/src/L4/solve_family.md, book/src/L4/index.md, book/src/SUMMARY.md)

Notes:
- META `overall_status: ready`; all 8 critic checks pass; repairer applied no edits (3 findings all `(low / observation)` / `(informational)`, all not-needed).
- DEFERRED to D7 per dispatch + report §Open-questions: the consolidated firm-count tally AND the `book/src/L4/index.md:47` "Rough-in at L4 (0)" → "(1)" flip. I did NOT touch line 47 (verified `**Rough-in at L4 (0)** — none currently.` unchanged). D7 owns the count reconciliation (cohort header "Firm at L4 (6 + 4 outer-driver)" + the rough-in tally — `solve_family` is the first rough-in-tier L4 combinator).
- §Specializations (electrostatic + magnetostatic sweeps) are authored as notes-in-entry per combinator-as-entry, NOT separate chapters — correct per report intent; no chapter-split applied. (Report flags a potential batch-17 size-judgment split; default kept.)
- Fence parity: the `new:` chapter body is a complete valid mdBook chapter; Haskell signatures use 4-space indented code (no nested ``` fences), so no fence-truncation risk. H1 `# solve_family` matches the slug, not a duplicated page heading.
- deferred integrated_at to finalize per role-spec.

---

## 2026-06-02T010800Z-abstractor-solve-family-map-dissolution (D2)
applied_at: 2026-06-02T01:58:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4-L3/solve-family-map-dissolution.md (new — L4>L3 `solve-family-map-dissolution` theme, `## Status: firm`; the outer map-shell dissolution for `solve_family`, composes strictly above `ksp-solve-driver-dissolution`)
- book/src/L4-L3/index.md (edit — appended D2's OWN Theme-list row after the `ksp-solve-driver-dissolution` row [was last, line 20]; seeded the §Vocabulary-cohort section after Working Notes with D2's OWN "Substantive themes (firm)" bullet — section did not pre-exist; consolidated tally DEFERRED to D8)
- book/src/SUMMARY.md (edit — inserted `- [solve-family-map-dissolution](./L4-L3/solve-family-map-dissolution.md)` after the `ksp-solve-driver-dissolution` line, inside the L4>L3 Part before the `# L3` header)
- scaffolding/open-questions.md (append-only — D2 New-intake section: the firm-on-structure-vs-LHS-test-coverage OQ + the no-sequential-obstruction cross-cutter anchor note)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (only THIS report's view; finalize sees the full staging log)
- concept_writes on existing slug: 0 (new theme, no concept-page writes)
- forward-edge claim without surface: 0 (`L3/solve_family` correctly kept plain-text in prose — not on disk, batch-17; verified no live `[L3/solve_family](...)` link in the new chapter — delegation links go to `../L3/ksp_solve.md` + `./ksp-solve-driver-dissolution.md`, both on disk)
- edge-label / prose mismatch: 0 (declared edge L4→L3, LHS `solve_family` map combinator, RHS L3 explicit accumulating loop — every section narrates that edge forward)
- H1 reuses page heading: 0 (H1 `# solve-family-map-dissolution` matches slug)
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (operator-capture axis `fixed | per-element` handled — fixed-operator covered, per-element superset explicitly scoped out to batch-17)
- bookkeeping incomplete: 0
- citecheck bounds + path-hygiene lint: 12 ok, 0 failing (no MISS/AMBIG/OOB)
- SUMMARY.md chapter registration: registered by the report's own proposed-change (no auto-fix needed)
- index-placeholder displacement: n/a (the §Vocabulary-cohort section was genuinely absent — D2 seeds it; the Theme-list table had real rows, not the `(empty — Phase B skeleton.)` placeholder)
- implied-component stub materialization: n/a (no dangling clearly-implied forward-ref; `L3/solve_family` is deliberately-deferred to batch-17, plain-text fallback is correct here)
- no-sequential-obstruction claim (D2-specific): verified the chapter asserts the family loop carries NO `sequential-obstruction` (members independent, cap Law 1/3), contrasted against the per-solve `L3/ksp_solve` outer-driver fold which DOES — the claim is internally consistent and grounded in the cited cap laws

Open questions promoted:
- solve-family-map-dissolution-firm-on-structure-vs-lhs-test-coverage (NEW; routed to batch-17 lowering-verifier — the same KspSolver-statefulness/RHS-buffer-aliasing pass that gates the LHS cap; ratify the shape/semantics scoping)
- solve-family-map-no-sequential-obstruction-vs-per-solve-fold (NEW; recorded as a cross-layer-cross-cutter anchor note, not a resolution-pending question)
- per-element-operator superset + L3 `solve_family` entry / L3>L2 hop: NOT re-opened — already migrated to the plan as `map-solve-superset-probe` (batch-17) + D1's batch-17 routing; recorded for traceability only in the New-intake append.

Build-relevant: yes (touches book/src/L4-L3/solve-family-map-dissolution.md, book/src/L4-L3/index.md, book/src/SUMMARY.md)

Notes:
- META `overall_status: ready`; 7 of 8 critic checks pass, cross-reference-integrity `warning` (the `../L4/solve_family.md` LHS live link unresolved at critique time — same-cycle D1 dependency). CONFIRMED D1 landed `book/src/L4/solve_family.md` (staging row D1 above + verified on disk this dispatch) BEFORE applying D2, so every `solve_family.md` live link in the new chapter + the index row now resolves at the single finalize build. The warning is fully discharged. Repairer applied no edits (all findings not-needed / confirmations).
- DEFERRED to D8 (NOT D7) per dispatch: the L4-L3 consolidated firm-count tally / coverage-gap line / growth-log. The dispatch explicitly notes a corrective D8 lifter owns the L4-L3 consolidated tally this cycle (the report text says "D7" but the dispatch overrides to D8). I recorded "deferred to D8" in the §Vocabulary-cohort seed prose. D2 added ONLY its own row + bullet; no consolidated tally touched.
- §Vocabulary-cohort section did not pre-exist in L4-L3/index.md — D2 seeds it as instructed (section header + "Substantive themes (firm)" sub-list + D2's bullet). If D8 establishes a differing section structure, finalize/D8 should merge D2's bullet under D8's "Substantive themes (firm)" sub-list.
- Firm-on-structure status (the theme is `firm`, not inheriting the LHS `rough-in (test-coverage-bounded)` caveat) — ratified as-is per critic Issue 1 (sound, well-scoped shape/semantics-split judgment); NOT silently re-opened. OQ filed for the batch-17 verifier.
- Fence parity: the `new:` chapter body is a complete valid mdBook chapter (`# solve-family-map-dissolution` H1 through §"L4 vs L3 distinction"); L4/L3 Haskell signatures use 4-space-indented code (no nested ``` fences), so no fence-truncation risk.
- deferred integrated_at to finalize per role-spec.

---

## 2026-06-02T010700Z-harvester-eliminate-rhs-firm-l1 (D3)
applied_at: 2026-06-02T01:54:42Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/eliminate_rhs.md (new — firm L1 operator `eliminate_rhs`; `b' = b − K·x_bc`, essential rows pinned per diagonal policy; `## Status: firm` clean-gate PROMOTE; 4 laws + 3 non-laws; depends apply_linop + axpy + set_subvector concept)
- book/src/L1/index.md (edit — flipped D3's OWN `:74` `eliminate_rhs` rough-in bullet → FIRM (contiguous verbatim replacement); appended D3's OWN dep-map row after the `floquet-correction` row [was `:111`]. Did NOT touch the `:70` FE-cohort SUBSECTION HEADER — D7-owned; did NOT touch the `:73` `eliminate_essential_bc` sibling bullet — correctly left rough-in)
- book/src/SUMMARY.md (edit — inserted `- [eliminate_rhs](./L1/eliminate_rhs.md)` after the L1-Part `floquet-correction` line [`:126`], before the `# L1 > L0 — Lowering` header)
- scaffolding/open-questions.md (append-only — D3 New-intake section: 3 OQs)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (only THIS report's view; finalize sees the full staging log)
- concept_writes on existing slug: 0 (new L1 operator file, no concept-page writes; `set_subvector` referenced as concept-not-written, OQ filed for a future `concepts/set-subvector.md`)
- forward-edge claim without surface: 0 (the L1>L0 `eliminate-rhs-mutation-rotation` forward-ref is correctly plain-text in the new chapter §Downward + the index bullet + dep-map — verified NOT a live `[...](...)` link; target file `book/src/L1-L0/eliminate-rhs-mutation-rotation.md` confirmed absent on disk; OQ filed for the follow-on abstractor)
- edge-label / prose mismatch: 0 (not a lowering-theme report; the §Downward prose narrates the L1→L0 direction consistent with the forthcoming theme)
- H1 reuses page heading: 0 (H1 `# eliminate_rhs` matches the slug)
- append on missing slug: 0 (SUMMARY floquet-correction L1 anchor `:126` present; dep-map floquet-correction row present)
- variant-axis missing on multi-variant operator: 0 (2 axes declared+covered: diagonal-policy DIAG_ONE|DIAG_ZERO with the `:38-41` MFEM_VERIFY two-valued witness; bc-data-homogeneity homogeneous|inhomogeneous; third axis operator-true-dof-representation explicitly absorbed)
- bookkeeping incomplete: 0
- citecheck bounds + path-hygiene lint: 29 ok, 1 failing. The single failing is `[AMBIG] index.md:74` — the report's own intra-artifact SELF-reference to `book/src/L1/index.md:74` (the rough-in bullet being flipped), a bare-basename hygiene flag, NOT a Palace source-citation defect. Verified separately: the load-bearing Palace anchors all resolve byte-exact (`rap.cpp:69`=`A->Mult(lx, ly)`, `:73`=`b.Add(-1.0, ty)`, `laplaceoperator.cpp:247`=`x.ParallelProject(X)` — the repairer's `:248`→`:247` fix confirmed). Non-blocking (the AMBIG is on a self-ref, not a MISS/OOB on a Palace source cite).
- SUMMARY.md chapter registration: registered by the report's own proposed-change (no auto-fix needed)
- index-placeholder displacement: n/a (the `:74` bullet was an existing firm-text rough-in bullet, not the `(empty — Phase B skeleton.)` placeholder; the dep-map table had real rows)
- implied-component stub materialization: n/a (the L1>L0 theme forward-ref is deliberately-deferred to a follow-on abstractor pass per the missing-anchor convention; plain-text fallback is correct — the theme is a real forthcoming deliverable, the report correctly does not force a stub)

Open questions promoted:
- eliminate-rhs-mutation-rotation-l1-l0-theme-unauthored (NEW; forward-frontier — follow-on abstractor authors the L1>L0 sibling theme; upgrades the plain-text refs to live links on land)
- eliminate-essential-bc-l1-co-dispatch-sibling (NEW; the operator-side BC-pin half still rough-in at `index.md:73`; future harvester co-dispatch)
- set-subvector-essential-dof-mask-concept-page (NEW; concept-page candidate `concepts/set-subvector.md`, non-gating)

Build-relevant: yes (touches book/src/L1/eliminate_rhs.md, book/src/L1/index.md, book/src/SUMMARY.md)

Notes:
- META `overall_status: ready`; 6 of 8 critic checks pass, citation-validity + cross-reference-integrity `warning`. Both warnings were REPAIRED by the repairer pre-integration (verified in META §Repair): (1) `laplaceoperator.cpp:248`→`:247` witness drift (2 occurrences) — confirmed `:247` byte-exact on-disk this dispatch; (2) the orphan closing fence at CYCLE.md:321 deleted — confirmed even fence parity (14 fences) in the proposed-changes region this dispatch, so the `edit:SUMMARY.md` block parsed cleanly; (3) `set_subvector`/`set_subvector_zero` reuse wording tightened; (4) dep-map double-cite `225-252,252`→`225-252` tidied. All discharged.
- DEFERRED to D7 per dispatch + report §Index-registration-partition: the FE-cohort SUBSECTION-HEADER tally at `book/src/L1/index.md:70` ("Rough-in (FE-assembly sub-spine — THREAD-OPENER cycle-053)"). I did NOT touch the `:70` header — verified unchanged. D3 flipped ONLY its own `:74` bullet. D7 owns the cohort-count reconciliation (`eliminate_rhs` moves from rough-in → firm within the FE-assembly sub-spine; `fe_assemble` is already firm-noted there, `eliminate_essential_bc` stays rough-in).
- Dispatch-vs-report dep-map target reconciliation: the dispatch summary said "`edit:book/src/L1-L0/index.md` — D3's dep-map row (after floquet-correction)", but the report's actual single proposed-change (CYCLE.md:321-324) targets the **L1 operator dep-map in `book/src/L1/index.md`** (after the `floquet-correction` row at `:111`) — and the row IS an L1-operator row (signature `eliminate_rhs :: ... → Tensor[N]`, an L1 operator, not an L1>L0 theme). Applied per the report's own proposed-change to `L1/index.md`. There is NO L1-L0 theme row in this report (the L1>L0 theme is unauthored, forward-ref only) — so `book/src/L1-L0/index.md` was correctly NOT touched. Flagging for finalize visibility: the dispatch's "L1-L0" was a mislabel of the L1 dep-map target.
- Fence parity: the `new:` chapter body is a complete valid mdBook chapter (`# eliminate_rhs` H1 through §"Downward to L0"); the one nested fence is the ` ```text ` Signature block (Haskell `::` + do-notation), properly opened/closed inside the body — no fence-truncation risk.
- deferred integrated_at to finalize per role-spec.

---
## 2026-06-02T010700Z-harvester-eliminate-essential-bc-firm-l1 (D4)
applied_at: 2026-06-02T02:12:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/eliminate_essential_bc.md (new — firm L1 operator `eliminate_essential_bc`; pin essential Dirichlet true dofs into the assembled SQUARE operator; zero rows/cols at the essential-dof set + set eliminated diagonal per diagonal policy; `## Status: firm` CLEAN-GATE PROMOTE; 4 laws [idempotence, free-block preservation, policy-determines-only-essential-diagonal, distribution-over-assembly] + 3 non-laws; separable post-composition AFTER fe_assemble, NOT part of the assembly fold; firm-on-positive-structure)
- book/src/L1/index.md (edit — flipped D4's OWN `:73` `eliminate_essential_bc` rough-in bullet → FIRM, contiguous verbatim replacement [bullet carried the drifted `:215-217`; firm bullet uses corrected `:216-217`]; appended D4's OWN dep-map row AFTER D3's already-landed `eliminate_rhs` row [`:112`], since D3's `eliminate_rhs` row now sits between the `floquet-correction` anchor and the insertion point. Did NOT touch the `:70` FE-cohort SUBSECTION HEADER — D7-owned; did NOT touch the `:74` `eliminate_rhs` firm bullet — D3's, already landed)
- book/src/SUMMARY.md (edit — inserted `- [eliminate_essential_bc](./L1/eliminate_essential_bc.md)` AFTER the L1-Part `fe_assemble` line [`:110`], before `orthogonalize`. NOTE D3 inserted its `eliminate_rhs` SUMMARY line after `floquet-correction` [`:127`], not adjacent — no collision)
- scaffolding/open-questions.md (append-only — D4 New-intake section: 4 entries [OQ-1 fe_assemble.md citation drift, OQ-2 L1>L0 re-anchor, the D3-co-dispatch-sibling RESOLVED note, OQ-5 DofSet concept page])

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (only THIS report's view; finalize sees the full staging log)
- concept_writes on existing slug: 0 (new L1 operator file, no concept-page writes; `DofSet[N]` referenced as a thin index-set type, OQ-5 filed for a future `concepts/dof-set.md`)
- forward-edge claim without surface: 0 (the L1>L0 `fe-operator-assemble-mutation-rotation` ref IS a live link — target `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md` confirmed on disk [rough-in thread-opener, cycle-053]; the `eliminate_rhs` sibling ref left plain-text in §Applicability per the report — D3 landed `eliminate_rhs.md` THIS cycle so the link COULD be upgraded, but D4 authored it plain-text and the report did not propose a live link; left as-authored [non-blocking, optional lifter upgrade])
- edge-label / prose mismatch: 0 (not a lowering-theme report; §Downward narrates L1→L0 consistent with `lowers_to: L1-L0/fe-operator-assemble-mutation-rotation`)
- H1 reuses page heading: 0 (H1 `# eliminate_essential_bc` matches the slug)
- append on missing slug: 0 (SUMMARY `fe_assemble` L1 anchor `:110` present; dep-map insertion anchor = D3's `eliminate_rhs` row, present)
- variant-axis missing on multi-variant operator: 0 (2 axes declared+covered: diagonal-policy DIAG_ONE|DIAG_ZERO with the `rap.cpp:39-41` two-value guard + `:18` default + witnesses [`laplaceoperator.cpp:217` DIAG_ONE; `modeeigensolver.cpp:571,574,608,611` both]; trial-test-coincidence square|rectangular with `:42-43` set-time + `:145-148` assemble-time reject — `square` the operator, `rectangular` a hard L0 reject; MFEM `DIAG_KEEP` explicitly out-of-axis)
- bookkeeping incomplete: 0
- citecheck bounds + path-hygiene lint: 26 ok, 0 failing (no MISS/AMBIG/OOB)
- SUMMARY.md chapter registration: registered by the report's own proposed-change (no auto-fix needed)
- index-placeholder displacement: n/a (the `:73` bullet was an existing firm-text rough-in bullet, not the `(empty — Phase B skeleton.)` placeholder; the dep-map table had real rows)
- implied-component stub materialization: n/a (no dangling clearly-implied forward-ref needing a stub; the L1>L0 theme is a real on-disk rough-in, the `eliminate_rhs` sibling is on disk via D3)

Open questions promoted:
- eliminate-essential-bc-fe-assemble-sibling-fe_assemble-md-citation-drift (NEW; OQ-1; lifter/citation-fix follow-on — fix `fe_assemble.md:147` `:215-217`→`:216-217`. INTEGRATOR-VERIFIED ACTUAL COUNT: 1 occurrence on current disk [line 147], NOT 2 — the critic/repairer META's "147 + 257" framing does not match current disk; a grep for `laplaceoperator.cpp:215-217` and any `:21x` range in `fe_assemble.md` finds it only at line 147. The §Evidence ~257 occurrence either lacks the range or was already corrected. Flagged for the lifter to belt-and-suspenders re-grep at fix time.)
- eliminate-essential-bc-l1-l0-lowering-re-anchor (NEW; OQ-2; lifter follow-on — re-anchor the `fe-operator-assemble-mutation-rotation` elimination step to this firm operator; sibling to D3's `eliminate-rhs-mutation-rotation-l1-l0-theme-unauthored`)
- eliminate-essential-bc-l1-co-dispatch-sibling — RESOLVED-by-D4 note (D3's OQ; this report IS the co-dispatch sibling, landed firm; close at next meta-phase unify)
- dof-set-concept-page (NEW; OQ-5; concept-page candidate `concepts/dof-set.md`, non-gating; layer-intro-author scope; relates to D3's `set-subvector-essential-dof-mask-concept-page`)

Build-relevant: yes (touches book/src/L1/eliminate_essential_bc.md, book/src/L1/index.md, book/src/SUMMARY.md)

Notes:
- META `overall_status: ready`; all 8 critic checks PASS; repairer applied no edits (all 4 findings observational severity:info, all not-needed). Clean firm L1 promotion on positive structure.
- Anchor byte-exactness verified against CURRENT on-disk state (D3's `:74` bullet flip + dep-map row + SUMMARY line already landed): D4's `:73` rough-in bullet matched verbatim; the `:70` FE-cohort header confirmed UNTOUCHED; the dep-map row appended after D3's `eliminate_rhs` row (not after `floquet-correction` directly, since D3 interposed its row there — both rows preserved). SUMMARY `eliminate_essential_bc` inserted after `fe_assemble:110` (D3's `eliminate_rhs` is at `:127` after `floquet-correction`, no collision).
- Load-bearing Palace anchors spot-verified byte-exact this dispatch: `laplaceoperator.cpp:216` = `auto K_l = std::make_unique<ParOperator>(...)`, `:217` = `K_l->SetEssentialTrueDofs(dbc_tdof_lists[l], Operator::DiagonalPolicy::DIAG_ONE)` (the `:216-217` correction of the codemap-drifted `:215-217` CONFIRMED correct); `rap.cpp:143` = `RAP->EliminateBC(dbc_tdof_list, diag_policy)`. citecheck --scan: 26 ok, 0 failing.
- DEFERRED to D7 per dispatch + report OQ-4: the FE-assembly sub-spine SUBSECTION-HEADER cohort tally at `book/src/L1/index.md:70` ("Rough-in (FE-assembly sub-spine — THREAD-OPENER cycle-053)"). I did NOT touch the `:70` header — verified unchanged. D4 flipped ONLY its own `:73` bullet + added its own dep-map row + SUMMARY line. D7 owns the consolidated cohort-count reconciliation (`eliminate_essential_bc` AND `eliminate_rhs` both move rough-in→firm within the sub-spine this cycle; `fe_assemble` already firm-noted).
- Fence parity: the `new:` chapter body is a complete valid mdBook chapter (`# eliminate_essential_bc` H1 through §"Downward to L0"); the three nested ` ```text ` blocks (Signature, the block-decomposition display, the post-composition display) are each properly opened/closed inside the body — no fence-truncation risk. The firm apparatus (Signature / Algebraic-laws / Status `firm` / Evidence) sits inside the `new:` fence, not authored as the report's own top-level sections (not the cycle-019 fence-truncation defect).
- `eliminate_rhs` sibling ref in §Applicability: left plain-text as D4 authored it. D3 landed `eliminate_rhs.md` on disk this cycle, so this COULD be upgraded to a live link (`upgrade-plain-text-ref-to-live-link-when-target-on-disk`), but D4's proposed-changes did not include that upgrade and the per-report integrator applies the report's own changes — left as-authored. Optional non-blocking upgrade for a future lifter. Not a build issue (plain-text, not a dead link).
- deferred integrated_at to finalize per role-spec.

---

## 2026-06-02T010700Z-abstractor-libceed-boundary-obstruction (D5)
applied_at: 2026-06-02T02:30:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md (new — L1>L0 boundary annotation, `## Status: obstruction (opaque-library-ownership)`; libCEED-owned element-local quadrature kernel + COO numerical materialization, Palace-owned fold/dispatch/COO→CSR-shuffle/BC-elimination; `fe_assemble` STAYS FIRM, not downgraded; deeper-boundary sibling of triangular-solve-obstruction; settles the cycle-053 fe-operator-assemble-mutation-rotation libCEED-boundary OQ as opaque-library-ownership per batch-16 meta-phase ratification)
- book/src/L1-L0/index.md (edit — appended D5's OWN dep-map row after the `triangular-solve-obstruction` row [was last, line 48]; carries the repairer-widened `bilinearform.cpp:64-70` citation)
- book/src/SUMMARY.md (edit — inserted `- [fe-assemble-libceed-boundary-obstruction](./L1-L0/fe-assemble-libceed-boundary-obstruction.md)` after the `triangular-solve-obstruction` L1>L0 line [`:141`], before `chebyshev-smoother-mutation-rotation`)
- scaffolding/open-questions.md (append-only — D5 New-intake section: 2 OQs routed to batch-17 meta-phase)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (only THIS report's view; finalize sees the full staging log)
- concept_writes on existing slug: 0 (new obstruction theme, no concept-page writes)
- forward-edge claim without surface: 0 (all 4 live links — `../L1/fe_assemble.md`, `./fe-operator-assemble-mutation-rotation.md`, `./triangular-solve-obstruction.md`, self — resolve on disk; precedents confirmed present this dispatch)
- edge-label / prose mismatch: 0 (labeled L1>L0 throughout — frontmatter `layer: L1-L0`, §"L1 form (LHS)" / §"L0 form (RHS)"; prose narrates exactly the L1→L0 edge: the firm `fe_assemble` fold's per-term leaf `A(term_i)` and its L0 realization across bilinearform.cpp / libceed/operator.cpp)
- H1 reuses page heading: 0 (H1 `# fe-assemble-libceed-boundary-obstruction` matches the slug)
- append on missing slug: 0 (index `triangular-solve-obstruction` row at `:48` present; SUMMARY `:141` anchor present)
- variant-axis missing on multi-variant operator: 0 (the one genuine variant axis — PA-vs-FA dispatch `UseFullAssembly` `bilinearform.cpp:118-132` — handled in §Applicability item 4 as a Palace-owned axis on the firm fold; full-assembly COO→CSR path covered items 2+6; all six sub-parts enumerated with an ownership verdict each)
- variant-axis MISSING obstruction sub-kind tag: 0 (the MANDATORY `obstruction (opaque-library-ownership)` sub-kind tag IS present in BOTH the `## Status` line AND frontmatter `sub_kind: opaque-library-ownership` — per CLAUDE.md §Methodology-invariants "Obstruction themes have two sub-kinds". Sub-kind correctness verified: the entire callable [pure-virtual `BilinearFormIntegrator::Assemble`→`CeedOperator`, `CeedOperatorAssembleCOO` libCEED API] lives outside Palace = opaque-library-ownership, NOT enum-only-stub [no Palace-owned MFEM_ABORT/// TODO body])
- bookkeeping incomplete: 0 (DEFERRED consolidated obstruction-cohort tally to D7 per dispatch partition — D5 registers ONLY its own index row + SUMMARY entry; no total-count/coverage-gap/growth-log edit, verified)
- citecheck bounds + path-hygiene lint: 32 ok, 6 failing. ALL 6 failing are path-hygiene artifacts on ABBREVIATED in-prose/`//`-comment basename forms — NOT defects on load-bearing citations: 5× `[MISS] libceed/operator.cpp:*` (bare `libceed/operator.cpp` basename used in `//`-comment headers + prose, no such relative path under reference/; the AUTHORITATIVE full-path `palace/fem/libceed/operator.cpp` form in `inputs:`/`l0_anchor`/`verified_against:` resolves in-bounds) + 1× `[AMBIG] integrator.hpp:58-61` (basename collision — two `integrator.hpp` in tree; the full-path `palace/fem/integrator.hpp` form in the authoritative blocks resolves). NO MISS/AMBIG/OOB on any load-bearing full-path Palace citation. The repairer ACCEPTED the bare-basename `//`-comment form as established house style (matching the `triangular-solve-obstruction.md` precedent, critic Finding 2 → not-needed). Non-blocking. Load-bearing anchors independently codemap-verified byte-exact this dispatch (see Notes).
- SUMMARY.md chapter registration: registered by the report's own proposed-change (no auto-fix needed)
- index-placeholder displacement: n/a (the L1-L0 dep-map table had real rows ending at the `triangular-solve-obstruction` row, not the `(empty — Phase B skeleton.)` placeholder)
- implied-component stub materialization: n/a (no dangling clearly-implied forward-ref needing a stub; all cross-refs resolve on disk)
- forward-edge / fe_assemble-stays-firm coherence (D5-specific): verified the proposed-changes do NOT touch `book/src/L1/fe_assemble.md` (the firm fold is untouched — the obstruction is a strict sub-term BELOW the fold's leaf `A(term_i)`; the fold's `Σ_i` quantifies over `A(·)` opaquely, so firmness is independent of leaf-ownership). Sibling-coherence with the `ksp_solve`-firm-while-MINRES/BiCGStab-obstruction and `eigsolve` `partial-obstruction` patterns is internally consistent.

Open questions promoted:
- boundary-anchor-verdict-flavor-vs-negative-anchor-reconciliation (NEW; batch-17 meta-phase — the new `verdict: boundary-anchor` flavor [positive Palace source site marking a library boundary] vs the `negative-anchor` [absence] the triangular-solve precedent uses; verdict-vocabulary normalization across the obstruction-theme corpus)
- operatorcootocsr-palace-vs-libceed-ownership-fine-line (NEW; batch-17 meta-phase / lowering-verifier — the `OperatorCOOtoCSR` `:487-488` Palace-format-conversion vs `CeedOperatorAssembleCOO` `:483` libCEED-numerical-assembly fine line; note `:492-499` scales duplicated nonzeros — exact boundary line could shift if the reshuffle does numerical work; shell/leaf split robust regardless)

Build-relevant: yes (touches book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md, book/src/L1-L0/index.md, book/src/SUMMARY.md)

Notes:
- META `overall_status: ready`; all 8 critic checks PASS; repairer applied ONE edit (Finding 1, citation-validity: widened `bilinearform.cpp:67-70` → `64-70` everywhere — frontmatter `inputs:`, `new:` `l0_anchor`, §L0-form prose, §Verified-against bullet, the `verified_against:` YAML, and the index dep-map row — to fully cover the named `CeedElemRestriction trial/test_restr` [64/66] + `CeedBasis trial/test_basis` [68/69] inputs; the original `67-70` clipped the restriction head). Findings 2-5 all not-needed (2 = house-style basename, accepted; 3 = boundary-anchor verdict self-flagged to meta-phase; 4 = COOtoCSR fine-line self-flagged; 5 = D7 tally-defer confirmed). The widened `64-70` is what landed in the new file + index row.
- Load-bearing Palace anchors codemap-verified byte-exact this dispatch: `bilinearform.cpp:64`=`CeedElemRestriction trial_restr`, `:66`=`test_restr`, `:68`=`trial_basis`, `:69`=`test_basis`, `:75`=`integ->Assemble(...)`, `:77`=`op->AddSubOperator(sub_op);` (the widened `64-70` confirmed covering all four named inputs); `integrator.hpp:58`=`virtual void Assemble(Ceed ceed, CeedElemRestriction trial_restr,`, `:61`=`... CeedOperator *op) const = 0;` (pure-virtual leaf signature); `libceed/operator.cpp:483`=`CeedOperatorAssembleCOO(ceed, op[id], ...)`, `:487-488`=`loc_mat[id] = OperatorCOOtoCSR(ceed, ...)` (assignment spans 487-488). All resolve.
- DEFERRED to D7 per dispatch + report §Open-questions caveat 1: the consolidated obstruction-cohort running-count / coverage-gap / growth-log lines. D5 registered ONLY its own index dep-map row + SUMMARY entry — verified no total-count edit in the index block. D7 owns the L1-L0 obstruction-cohort tally reconciliation (this is the 3rd opaque-library-ownership-adjacent obstruction theme in L1-L0 after minres/bicgstab enum-only-stub + triangular-solve opaque-library-ownership).
- Fence parity: the `new:` chapter body is a complete valid mdBook chapter (`# fe-assemble-libceed-boundary-obstruction` H1 through the `verified_against:` YAML block); the firm-status apparatus (Status / L1-form / L0-form / Applicability / Justification / Verified-against) sits INSIDE the `new:` fence (CYCLE.md 42-336), not authored as report-top-level sections — no fence-truncation defect (critic confirmed; the chapter uses 4-space-indented code blocks for the C++ comment snippets + Haskell-ish signatures, no nested ``` fences). The `verified_against:` YAML is the indented-block tail of the chapter, round-trips (critic YAML sub-check: 10 entries, yaml.safe_load succeeds).
- All three changes (new file + index row + SUMMARY) landed TOGETHER this single dispatch, so the new chapter's SUMMARY registration + the index dep-map link both resolve to the on-disk file at the single finalize build — no dead-link window.
- deferred integrated_at to finalize per role-spec.

---

## 2026-06-02T010700Z-lifter-fe-assemble-theme-reanchor (D6)
applied_at: 2026-06-02T02:48:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/fe-operator-assemble-mutation-rotation.md (edit — 8 surgical re-anchor edits to the cycle-053 rough-in theme: (1) frontmatter `lowers:` `(speculative rough-in)` → `(firm — landed cycle-054)`; (2) §Status promotion-route prose — `fe_assemble` now firm live-link, `eliminate_essential_bc`/`eliminate_rhs` still rough-in; (3) §"L1 form (LHS)" opener re-pointed at firm `[fe_assemble](../L1/fe_assemble.md)`; (4) §"L1 form" closing prose — `fe_assemble` firm of the 3 pieces; (5) §"L0 form" step-3 `AddSubOperator` citation drift `:73-75`/`:93-95` → `:77`/`:97`; (6) §"libCEED boundary" `integ->Assemble` citation drift `:73-75` → `:75-76` [the one site NOT going to `:77` — its referent is `integ->Assemble`, not `AddSubOperator`]; (7) §"Verified-against" PartialAssemble row `:73-75`/`:93-95` → `:77`/`:97`; (8) §"Speculative L1 operators" list — `fe_assemble` struck-through + PROMOTED-firm note with live link)
- scaffolding/open-questions.md (append-only — D6 New-intake section: the range-vs-pinpoint anchor-form convention note)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (only THIS report's view; finalize sees the full staging log)
- concept_writes on existing slug: 0 (no concept-page writes; pure theme re-anchor)
- forward-edge claim without surface: 0 (the LHS re-anchor points at `../L1/fe_assemble.md` which IS on disk — live link resolves, verified this dispatch; the `eliminate_essential_bc`/`eliminate_rhs` references stay plain-text, correctly — those operators landed firm via D4/D3 this cycle but D6's proposed-changes do NOT upgrade them to live links [theme-side elimination-leg re-anchor is D4's `eliminate-essential-bc-l1-l0-lowering-re-anchor` OQ, a future lifter pass])
- edge-label / prose mismatch: 0 (theme stays L1>L0; all edits preserve LHS=L1 `fe_assemble`, RHS=L0 bilinearform build-up-then-assemble; prose narrates forward; no inversion)
- H1 reuses page heading: 0 (no H1 touched)
- append on missing slug: 0 (all 8 `[old]` anchors verified byte-exact on current disk before applying; `[old]` for edit 5/7 carried the stale `:73-75`/`:93-95` ranges, matched verbatim)
- variant-axis missing on multi-variant operator: 0 (no variant-axis content touched; PA/FA + term-position + trial-test axes untouched)
- bookkeeping incomplete: 0 (no count/tally edit; theme STAYS rough-in — frontmatter `status: rough-in` untouched, only the `lowers:` parenthetical + §Status prose reflect 1-of-3 operators firmed)
- citecheck bounds + path-hygiene lint: 12 ok, 0 failing (no MISS/AMBIG/OOB)
- SUMMARY.md chapter registration: n/a (no new chapter; theme already SUMMARY-registered at line 150 — verified, no auto-fix needed)
- index-placeholder displacement: n/a (no index.md touched; edits all internal to the theme chapter)
- implied-component stub materialization: n/a (the firm LHS `fe_assemble` already on disk; `eliminate_*` siblings on disk via D4/D3 — no dangling clearly-implied forward-ref needing a stub)
- residual-stale-range sweep (D6-specific): verified post-apply `grep -nE ':73-75|:93-95'` of the theme returns ZERO matches — all three stale-range sites (theme §L0-form step-3, §libCEED-boundary, §Verified-against) corrected; no residual +2 drift remains
- corrected-citation codemap resolution (D6-specific): codemap `read_range bilinearform.cpp:73-97` confirms byte-exact — `:75-76` = `integ->Assemble(ceed, trial_restr, ...)`, `:77` = `op->AddSubOperator(sub_op);` (domain); `:95-96` = `integ->Assemble(...)`, `:97` = `op->AddSubOperator(sub_op);` (boundary). All three corrected anchors resolve to exactly the constructs their prose names.

Open questions promoted:
- fe-operator-assemble-addsuboperator-range-vs-pinpoint-convention (NEW; batch-17 lowering-verifier — the theme uses pinpoint `:77`/`:97` for the AddSubOperator accumulation while firm `fe_assemble.md` §Context uses range `:71-77`/`:91-97` for the per-term fold-body; both correct, flagged so a cross-checking verifier does not read the differing anchor forms as drift)

Build-relevant: yes (touches book/src/L1-L0/fe-operator-assemble-mutation-rotation.md)

Notes:
- META `overall_status: ready`; all 8 critic checks PASS; repairer applied no edits (all findings info-level/carry-forward, all not-needed). Clean mechanical lifter re-anchor — no substantive authoring, no decomposition change.
- Theme STAYS `rough-in` as instructed: only `fe_assemble` (1 of 3 speculative operators) is firmed by the cycle-054 promotion this pass re-anchors to. The full theme-`firm` flip is gated on (a) the `eliminate_essential_bc`/`eliminate_rhs` elimination-leg theme-side re-anchors (D4/D3 OQs, future lifter) AND (b) the libCEED-boundary classification — RATIFIED `opaque-library-ownership` batch-16 + themed by D5 THIS cycle as `fe-assemble-libceed-boundary-obstruction.md` (landed earlier in this staging log). A future lifter/abstractor pass flips the theme once those legs land.
- The §"libCEED boundary" site (edit 6) is the ONE drift-fix that does NOT go to `:77` — its prose names `integ->Assemble(...)` (referent `:75-76`), not `AddSubOperator` (`:77`). D6 correctly distinguished it; codemap-confirmed `:75-76` = `integ->Assemble`. This is a bounded L0-evidenced prose-correction within lifter authority (`lifter-scope-content-correction-boundary`), recorded in D6's §Discipline-notes #2.
- D6's other two §Open-questions caveats (range-vs-pinpoint; theme-stays-rough-in) — the range-vs-pinpoint is promoted as the D6 New-intake OQ above; the theme-stays-rough-in is reflected in the applied edits + this Notes section (not a separate OQ, it is the realized state).
- No SUMMARY/index/count touched — pure in-chapter re-anchor; finalize needs only the standard rebuild to pick up the theme-body edits.
- deferred integrated_at to finalize per role-spec.

---
## 2026-06-02T010800Z-layer-intro-author-c055-count-ownership (D7)
applied_at: 2026-06-02T03:06:00Z
applied_by: integrator-per-report
status: partially-applied

Files touched:
- book/src/L4/index.md (edit — D7 edit #1, 3 blocks: (1) §Vocabulary-cohort "Firm at L4 (6 + 4 outer-driver)" header → "UNCHANGED this cycle (cycle-055 added one *rough-in* combinator, `solve_family`, not a firm entry)" — L4 firm STAYS 6; (2) "Rough-in at L4 (0) — none currently." → "Rough-in at L4 (1)" + the `solve_family` rough-in (test-coverage-bounded) bullet (combinator-as-entry, 2 specialization notes, test-coverage-bounded maturity); (3) "Queued at L4 (0 — substantially complete)" + the "substantially complete / near-exhausted" + batch-14-meta-tee-up prose → "Active frontier — the solver-test-load is generating new spine vocabulary" reword (RETIRES the stale near-exhausted framing per the 2026-06-01 VOCABULARY-SHIFT REDIRECT; keeps the `solve_family` + `L4/orthogonalize` combinator-front bullets + the 13-of-18 no-L4-by-design observation))
- book/src/L1/index.md (edit — D7 edit #3, 2 blocks: (1) `:70` FE-assembly sub-spine SUBSECTION HEADER "Rough-in (FE-assembly sub-spine — THREAD-OPENER cycle-053)" → "Firm (FE-assembly sub-spine — 3; opened cycle-053, completed cycle-055)" header reword incl. the all-3-firm narrative + D5's libCEED-boundary obstruction note in the FE-thread narrative + bridge "The 3 member bullets follow:" — HEADER PARAGRAPH ONLY, see Notes for the producer-bullet-dedup discretionary call; (2) `:31` "Firm (26)" header → "Firm (26 main cohort; 29 firm grand total incl. the FE-assembly sub-spine)" + the 27→29 grand-total annotation (was 27: 26 main + fe_assemble c054; +2 eliminate_* c055 D3/D4 = 29))
- scaffolding/open-questions.md (append-only — D7 New-intake section: 3 OQs)

NOT touched (edit #2 SKIPPED):
- book/src/L4-L3/index.md — D7's edit #2 (the L4-L3 tally "3→4") DELIBERATELY SKIPPED per dispatch. The dispatch directs the corrective D8 lifter to own the L4-L3 consolidated tally (the on-disk-truthful 6→7 reconciliation + the stale-table-row fixes). The L4-L3/index.md diff visible in the working tree (9 insertions: D2's theme-list row + D2's §Vocabulary-cohort seed bullet, the seed prose explicitly says "deferred to D8 this cycle") is D2's earlier landing, NOT mine — verified via `git diff book/src/L4-L3/index.md` this dispatch.

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (only THIS report's view; finalize sees the full staging log)
- concept_writes on existing slug: 0 (pure index-narrative count/cohort edits; no concept-page writes; no new chapters)
- forward-edge claim without surface: 0 (all live links in the edited regions — solve_family.md / ksp_solve.md / eigsolve.md / chebyshev.md / iterate-while.md / L3/orthogonalize.md / fe-assemble-libceed-boundary-obstruction.md / fe-operator-assemble-mutation-rotation.md / eliminate_essential_bc.md / eliminate_rhs.md / fe_assemble.md / bilinear-form.md — all verified on disk this dispatch; D1-D5 landed earlier in this staging log)
- edge-label / prose mismatch: 0 (not a lowering-theme report; index-narrative edits preserve layer framing)
- H1 reuses page heading: 0 (no H1 touched)
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (no operator-entry authored; the solve_family rough-in bullet declares fixed-operator scope + the per-element batch-17 superset)
- bookkeeping incomplete: 0 (this report IS the bookkeeping/count reconciliation; counts internally consistent: L4 firm 6 + rough-in 1; L1 26 main + 3 FE = 29 firm grand total)
- citecheck bounds + path-hygiene lint: 9 ok, 0 failing (no MISS/AMBIG/OOB) on D7's CYCLE.md
- SUMMARY.md chapter registration: n/a (no new chapters — pure index-narrative edits)
- index-placeholder displacement: n/a (no `(empty — Phase B skeleton.)` placeholder in the edited regions; all real prose/tally text)
- implied-component stub materialization: n/a (no dangling clearly-implied forward-ref; `map_solve_over_(operator,rhs)_family` superset is correctly named plain-text in prose as a batch-17-gated speculative target, NOT a live link — fallback correct, it is speculative not clearly-implied)
- collision discipline (D7-specific, count-owner): edits target COUNT/NARRATIVE regions ONLY (cohort headers, rough-in/queued lines, frontier prose, the FE sub-spine header). The producer-owned FE bullets (L1/index.md:72-74, landed by the c054 fe_assemble + D3 eliminate_rhs + D4 eliminate_essential_bc) were NOT re-emitted — see Notes for the discretionary dedup.

Open questions promoted:
- l4-l3-fgmres-firmness-prose-vs-table-divergence (NEW; the now-understood index-table-staleness ROOT CAUSE — the L4-index prose labels gmres/fgmres-inner-loop themes firm [L4/index.md:53-54] while the authoritative L4-L3 table has them rough-in; the dispatch's "6→7" projection counted the prose, not the table; future lifter / cross-layer-cross-cutter reconciles the two surfaces against the chapter `## Status`)
- fe-assemble-laplaceoperator-citation-drift-215-vs-216 (NEW; the fe_assemble.md citation residual — INTEGRATOR-CONFIRMED 1 place [fe_assemble.md:147], corroborating D4's integrator's earlier count; `:215-217` → `:216-217`; for a future lifter/citation pass, NOT count-owner/harvester scope; relates to D4's eliminate-essential-bc-fe-assemble-sibling OQ)
- l1-fe-sub-spine-vs-main-cohort-unified-firm-count-renumber (NEW; presentation choice — the split "26 main / 3 FE / 29 grand total" count vs a future unified renumber-to-29; flagged not enacted, non-gating)

Build-relevant: yes (touches book/src/L4/index.md, book/src/L1/index.md)

Notes:
- META `overall_status: needs-revision` — applied PER EXPLICIT DISPATCH DIRECTION (not a wrong dispatch): the dispatch triaged D7's edit #2 (the L4-L3 tally "3→4") as WRONG (it trusted the stale L4-L3 table; the true reconciliation is the 6→7 the corrective D8 lifter owns) and directed me to apply ONLY edits #1 and #3, SKIP edit #2 entirely. status = partially-applied (2 of 3 edits applied; edit #2 deliberately skipped, owned by D8).
- DISCRETIONARY producer-bullet dedup on edit #3 block #1: D7's edit #3 block #1 `[new]` re-authored the 3 FE member bullets (fe_assemble / eliminate_essential_bc / eliminate_rhs) BELOW the reworded header — but those producer-owned bullets ALREADY EXIST on disk at L1/index.md:72-74 (landed by the c054 fe_assemble promotion + D3 eliminate_rhs + D4 eliminate_essential_bc earlier this cycle, with near-identical content). Re-emitting them would (a) DUPLICATE the 3 bullets and (b) TOUCH PRODUCER-OWNED ROWS, violating the count-owner collision partition the report itself asserts (CYCLE.md §Supporting-evidence "my `old` anchors target the COUNT/NARRATIVE regions … NOT any producer's row/bullet"). I applied ONLY the header-paragraph portion of the `[new]` (which carries the all-3-firm narrative + the libCEED-boundary note) and appended a bridge "The 3 member bullets follow:" to connect into the existing on-disk bullets. The 3 producer bullets are preserved verbatim (lines 72-74 unchanged). Recorded as applied-discretionarily, rationale: producer-row-collision-avoidance / count-owner-partition-fidelity (the report's own asserted partition).
- Anchor byte-exactness verified against CURRENT on-disk state (D1-D6 landed): all 5 `[old]` anchors (L4: §cohort header :32, rough-in line :48, queued block :57-61; L1: FE header :70, Firm(26) :31) matched verbatim this dispatch before editing. D1's earlier L4/index.md touches (its :76 dep-map row flip + its §cohort `solve_family` bullet at :40) were in DIFFERENT regions than D7's count/narrative anchors — no collision; verified the :40 `solve_family` cohort bullet (D1's) is distinct from D7's new :48 rough-in-tier bullet (the rough-in tally line gets its own bullet; D1's :40 is the firm-cohort-adjacent listing).
- L4 firm STAYS 6 (solve_family is rough-in, NOT firm) — the "Firm at L4 (6 + 4 outer-driver)" count is UNCHANGED, only annotated. Rough-in flipped 0→1.
- The fe_assemble.md citation-drift residual (215→216) is CONFIRMED 1 place on current disk this dispatch (fe_assemble.md:147), corroborating D4's integrator's earlier 1-not-2 finding — promoted as an OQ for a future lifter.
- deferred integrated_at to finalize per role-spec.

---
## 2026-06-02T011200Z-lifter-l4-l3-index-table-staleness-fix (D8)
applied_at: 2026-06-02T03:24:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4-L3/index.md (edit — 4 changes: (1) `krylov-step-typed-wrapper-dissolution` status cell `rough-in`→`firm` [PROMOTED c008 wave-1 lifter, `log/cycle-008.md`]; (2) `gmres-inner-loop-iterate-while-migration` leading slug-cell plain-text→LIVE link `[...](./gmres-inner-loop-iterate-while-migration.md)` [anchor file on disk] + status cell `rough-in`→`firm` [PROMOTED c020 wave-1 lifter, `log/cycle-020.md`]; (3) `fgmres-inner-loop-iterate-while-migration` status cell `rough-in`→`firm` [PROMOTED c021 lifter, `log/cycle-021.md`]; (4) appended the corrected `**Consolidated tally (firm L4>L3 themes: 6 → 7 this cycle)**` block to the §Vocabulary-cohort section after D2's `solve-family-map-dissolution` bullet — SUPERSEDES D7's skipped edit #2 "3→4")
- scaffolding/open-questions.md (append-only — D8 New-intake: the `index-table-status-cell-drifts-when-theme-file-promoted` root-cause OQ for batch-17 meta-phase)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (only THIS report's view; finalize sees the full staging log)
- concept_writes on existing slug: 0 (pure index-table status-cell + tally edits; no concept-page writes; no new chapters)
- forward-edge claim without surface: 0 (the gmres slug→live link upgrade resolves — `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` confirmed on disk this dispatch; all 3 promoted-row links + the tally-block links resolve)
- edge-label / prose mismatch: 0 (status-cell + tally text only; no LHS/RHS/justification-kind cell touched; layer framing unchanged)
- H1 reuses page heading: 0 (no H1 touched)
- append on missing slug: 0 (all 3 row-status `[old]` anchors + the tally insertion-point [D2's bullet] matched verbatim on current disk)
- variant-axis missing on multi-variant operator: 0 (no operator entry authored)
- bookkeeping incomplete: 0 (this report IS the L4-L3 consolidated-tally reconciliation; tally now reads 6→7 firm, internally consistent with all 7 status cells reading `firm`)
- citecheck bounds + path-hygiene lint: 13 ok, 2 failing. BOTH failing are `[MISS]` on bare-basename project-internal log refs (`cycle-052.md:15`, `cycle-053.md:12`) — the scanner does not search `log/` and the refs omit the `log/` prefix; the full-path `log/cycle-052.md` / `log/cycle-053.md` files BOTH confirmed on disk this dispatch (along with cycle-008/020/021/051). NOT a load-bearing Palace source-citation defect (the report cites no `reference/` source — provenance is theme-file `## Status` lines + `log/cycle-NNN.md` finalize records, all verified by direct read). Non-blocking path-hygiene artifact.
- SUMMARY.md chapter registration: n/a (no new chapters — pure index-table edits; gmres anchor file already SUMMARY-registered)
- index-placeholder displacement: n/a (no `(empty — Phase B skeleton.)` placeholder; the table had real rows + D2's seeded §Vocabulary-cohort)
- implied-component stub materialization: n/a (no dangling clearly-implied forward-ref; the gmres slug upgraded to a live link because the target IS on disk — `upgrade-plain-text-ref-to-live-link-when-target-on-disk`)
- ANCHOR-RECONCILE (D8-specific, per report §Open-questions caveat line 101): D8's tally-edit `[old]` anchor was authored against D7's edit#2 `[new]` text, which was NEVER applied (D7 edit #2 deliberately SKIPPED — see D7 staging row). So the `[old]` did not match disk. Applied D8's INTENT per its own anchor-ordering caveat: appended D8's `[new]` 6→7 tally block after D2's `solve-family-map-dissolution` bullet (the same insertion point D7 would have used). Resulting on-disk tally reads "6 → 7 firm" as required.
- CONSISTENCY CHECK (final, dispatch-mandated): all 7 L4-L3 theme-list status cells now read `| \`firm\`` (rows 15-21: krylov-step, gmres, fgmres, iterate-while-dissolution, iterate-while-with-prev-dissolution, ksp-solve-driver-dissolution, solve-family-map-dissolution); 0 rough-in status cells (the 3 residual "rough-in" string-matches in the table are the `PROMOTED rough-in→firm` provenance text in the corrected cells, NOT stale status). Matches the c051-c054 finalize records' "6 firm" pre-cycle + D2's solve-family-map-dissolution = 7. The L4-index prose (gmres/fgmres firm) and the L4-L3 table now AGREE — D7's `l4-l3-fgmres-firmness-prose-vs-table-divergence` OQ is RESOLVED by this fix (prose was right, table was stale).

Open questions promoted:
- index-table-status-cell-drifts-when-theme-file-promoted (NEW; root-cause, batch-17 meta-phase — index-table status cells maintained separately from theme-file `## Status` lines drift silently on promotion; 3 cells drifted c008→c021 undetected; candidate fixes (a) finalize-time consistency check (b) promotion-time standing audit (c) citecheck-adjacent lint; FLAGGED that L3-L2/L2-L1 tables mass-edited in c050/c051 may carry similar residue — one-time sweep warranted)
- l4-l3-fgmres-firmness-prose-vs-table-divergence (D7's OQ) — RESOLVED-by-D8 note (prose was correct, table was the stale surface; the two now agree; close at next meta-phase unify; NOT carried separately)

Build-relevant: yes (touches book/src/L4-L3/index.md)

Notes:
- META `overall_status: ready`; this is the corrective D8 lifter handling the `needs-revision` follow-up D7's repairer flagged. Pure mechanical staleness-fix — no theme body / signature / rotation shape / LHS-RHS / justification-kind cell touched; high→low rewrite direction unchanged.
- D7 PARTITION: D7's edits #1 (`L4/index.md` cohort/frontier reword) + #3 (`L1/index.md` FE sub-spine flip + grand-total) are correct and STAND (landed via D7's partially-applied row). Only D7's edit #2 (the `L4-L3/index.md` "3→4" tally block) was superseded — and it was never on disk (D7 SKIPPED it per dispatch), so D8 supersedes by appending the correct 6→7 block at the deferred insertion point, no D7-block-to-replace existed. Clean.
- D2's earlier landing (its theme-list row at line 21 + the §Vocabulary-cohort section seed + its bullet at line 42) is UNTOUCHED — D8 appended the consolidated tally AFTER D2's bullet, preserving D2's seed. The 3 row-status fixes (rows 15/16/17) are DISTINCT from D2's row (21).
- Fence parity: 0 triple-backtick fences in the file (no fence-truncation risk); the edits are inline table-cell + a prose paragraph.
- COMPLETES cycle-055 per-report integration: all 8 reports (D1-D8) applied. The L4-L3 index table is now consistent (7 firm themes, prose+table agree). Finalize: rebuild needed (book/src touched); resolve no deferred rows from D8 (this row is `applied`).
- deferred integrated_at to finalize per role-spec.

---
