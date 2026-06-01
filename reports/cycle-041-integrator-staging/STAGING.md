# cycle-041 integrator staging log

Per-report integration rows, newest LAST (append-only). integrator-finalize reads this to reconcile the cycle.

---

## 2026-06-01T051607Z-cycle-041-harvester-L2-dot (D1)
applied_at: 2026-06-01T055151Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/dot.md (created — firm thin-identity-floor L2 entry)
- book/src/L2/index.md (dep-map ROW prepended before the `orthogonalize` row; D1's own row only)
- book/src/SUMMARY.md (L2 chapter registration `[dot](./L2/dot.md)` after the `inner_product` line, as proposed by the report)
- scaffolding/open-questions.md (appended — D1 OQ section; 2 entries)

Gate hits:
- citecheck scan: 15 ok, 0 failing (no MISS/AMBIG/OOB)
- fence-parity: 0 (4-space-indented signature samples, no nested fences)
- SUMMARY-registration auto-fix: 0 (registration was explicitly proposed by the report, applied as-proposed; not a discretionary add)
- index-placeholder displacement: 0 (L2/index.md already populated; row prepended before `orthogonalize`)
- implied-component stub: 0
- variant-axis / forward-edge / H1 / retroactive-budget: 0

Open questions promoted:
- l3-dot-lowers-to-non-adjacent-l1-wants-reanchor-to-new-l2-floor
- l2-index-vocabulary-cohort-firm-at-l2-list-add-dot-floor

Build-relevant: yes

Notes:
- First per-report integrator this cycle — created the staging dir + this log.
- **`palace/linalg/vector.hpp:246` pinpoint integrated UNCHANGED** per the repairer note + dispatch directive: the comment `// Calculate the parallel inner product yᴴ x or yᵀ x.` is on :246 (verified twice in the META repair section: Read + codemap read_range). The critic's `citation-validity: warning` was a false positive (a critic-side −1 read drift); do NOT apply any `:246`→`:245` change. META `overall_status: ready`, all `repairs: not-needed`.
- **Count-ownership respected** (friction-ledger `parallel-blind-shared-index-count-divergence`): D1 touched ONLY its own `dot` dep-map row in L2/index.md — NOT the §"Vocabulary cohort" "Firm at L2" running list / firm-count tally. **D7 (layer-intro-author) owns the L2 tally + cohort-list addition this cycle.** OQ `l2-index-vocabulary-cohort-firm-at-l2-list-add-dot-floor` records this for D7.
- `L2/dot.md` is the anchor for the D4-authored L2>L1 / L3>L2 `dot` lowering themes co-landing later this cycle. No live forward-links to those unwritten themes (kept as plain prose per build-readiness).
- Carry-forward OQ `l3-dot-lowers-to-non-adjacent-l1-wants-reanchor-to-new-l2-floor`: the firm L3 `dot` §"Lowers to" non-adjacent in-line identity-to-L1 may want a light re-anchor to the new L2 floor + the D4 L3>L2 theme. Self-flagged by the report; out of this dispatch's scope (planner candidate, not a blocker — possibly subsumed by D4/D5 this cycle).
- deferred integrated_at to finalize per role-spec.

---

## 2026-06-01T051607Z-cycle-041-harvester-L2-nrm2 (D2)
applied_at: 2026-06-01T060000Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/nrm2.md (created — firm thin-identity-floor L2 entry; repairer-fixed directive `new:`)
- book/src/L2/index.md (dep-map ROW inserted after the D1 `dot` row, before `orthogonalize`; D2's own row only)
- book/src/SUMMARY.md (L2 chapter registration `[nrm2](./L2/nrm2.md)` after the D1 `dot` line, inside the L2 sub-list per the repairer note)
- scaffolding/open-questions.md (appended — D2 OQ section; 3 entries)

Gate hits:
- citecheck scan: 11 ok, 0 failing (no MISS/AMBIG/OOB)
- fence-parity: 0 (6 fences, even parity, 3 balanced blocks; first block `new:` per repairer fix; `## Status` + Signature + Algebraic-laws + Evidence all INSIDE the body block 23-173)
- SUMMARY-registration: 0 (registration was explicitly proposed by the report; applied as-proposed, not a discretionary add)
- index-placeholder displacement: 0 (L2/index.md already populated; row inserted before `orthogonalize`)
- implied-component stub: 0
- variant-axis / forward-edge / H1 / retroactive-budget: 0 (firm entry, one variant axis present + explicitly justified collapse, no forward-edge claims without surface)

Open questions promoted:
- l2-no-dot-leaf-floor-but-fold-is-the-l2-surface
- l2-index-vocabulary-cohort-firm-at-l2-list-add-nrm2-floor
- l2-index-intro-third-category-identity-in-form-floor-leaves

Build-relevant: yes

Notes:
- META `overall_status: ready`; all critic checks pass; one repair applied (directive `edit:`→`new:` on the first block, since `book/src/L2/nrm2.md` did not exist on disk). Applied via `Write` (file confirmed absent before apply).
- **Count-ownership respected** (friction-ledger `parallel-blind-shared-index-count-divergence`): D2 touched ONLY its own `nrm2` dep-map row in L2/index.md — NOT the §"Vocabulary cohort" "Firm at L2" running list / firm-count, and NOT the §"Working Notes" batch tally. **D7 (layer-intro-author) owns the consolidated L2 firm-count + cohort-list + §Working-Notes batch entry this cycle.** OQ `l2-index-vocabulary-cohort-firm-at-l2-list-add-nrm2-floor` records this for D7.
- **Consumer-not-member framing honored**: the entry lists `inner_product` under `consumes` (`nrm2 = √ ∘ abs ∘ inner_product` at `y=x`), never as a fold member — matches the do-NOT-merge boundary in L2/index.md §"Fold-cohort boundary" + the `inner_product` dep-map row. The `std::abs` load-bearing numerical guard is preserved as an explicit algebraic claim (L2 discipline).
- `L2/nrm2.md` is the anchor for the D5-authored L2>L1 / L3>L2 `nrm2` lowering themes co-landing later this cycle. No live forward-links to those unwritten themes (kept as plain prose per build-readiness `rough-in-forward-reference-must-be-plain-text-not-live-link`). The existing firm `L1-L0/nrm2-mutation-rotation` + `L3-L2/krylov-step-body-identity` are live links (on-disk).
- Re D1's `dot.md` floor landing: D2's `nrm2` correctly depends on the `inner_product` *fold* (the consumer-of-fold framing), not on D1's new `dot` leaf floor — consistent with L2 fold-cohort vocabulary. OQ `l2-no-dot-leaf-floor-but-fold-is-the-l2-surface` notes the report's "no L2 `dot.md` needed" framing is partly superseded by D1 (a `dot.md` floor now exists), but `nrm2`'s fold-dependency choice remains correct.
- deferred integrated_at to finalize per role-spec.

---

## 2026-06-01T051607Z-cycle-041-harvester-L2-scal (D3)
applied_at: 2026-06-01T060056Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/scal.md (created — firm thin-identity-floor L2 entry; arity-1 member of `linear_combination` fold, cited-not-merged)
- book/src/L2/index.md (dep-map ROW inserted immediately after the `linear_combination` anchor row; D3's own `scal` row only)
- book/src/SUMMARY.md (L2 chapter registration `[scal](./L2/scal.md)` between `linear_combination` and `inner_product`, inside the L2 sub-list, as proposed by the report)
- scaffolding/open-questions.md (appended — D3 OQ section; 5 entries)

Gate hits:
- citecheck scan: 8 ok, 0 failing (no MISS/AMBIG/OOB)
- fence-parity: 0 (8 fences, even parity; the `new:book/src/L2/scal.md` block ENCLOSES the full firm body — Signature/Semantics/Algebraic-laws/Status/Evidence all inside; the nested ```text signature fence opens+closes inside the `new:` block, NOT the cycle-019 truncation defect)
- SUMMARY-registration: 0 (registration explicitly proposed by the report; applied as-proposed, not a discretionary add)
- index-placeholder displacement: 0 (L2/index.md already populated; row inserted after `linear_combination`)
- implied-component stub: 0
- variant-axis / forward-edge / H1 / retroactive-budget: 0 (firm entry; two variant axes present + L0-anchored; no forward-edge claims without surface; forward-refs to D6 themes kept plain-text)

Open questions promoted:
- l2-blas1-floor-cohort-completeness-planner-confirm
- l2-scal-fusion-l3-l2-scal-themes-plain-text-forward-ref-upgrade
- l2-scal-fold-parent-frontmatter-field-convention
- l2-normalize-as-fused-l2-primitive-inherited
- l2-index-intro-third-category-and-firm-count-add-scal-floor

Build-relevant: yes

Notes:
- META `overall_status: ready`; all eight critic checks pass; all `repairs: not-needed` (zero defects; three downstream notes are non-defects). Applied via `Write` (`book/src/L2/scal.md` confirmed absent before apply).
- **`palace/linalg/vector.cpp:207-211` pinpoint integrated UNCHANGED** per the repairer anti-regression note + dispatch directive: the `if (si == 0.0)` branch body is at :207 (read-confirmed by the critic via codemap; `--anchor 'si == 0.0'` resolves in-range). The exploratory `--anchor 'imag'` `[DRIFT -1]`→:206 was a wrong-token false-positive, NOT producer drift. Do NOT regress :207→:206.
- **`fold_parent` frontmatter field kept AS AUTHORED** per dispatch directive — it is a convention signal for the meta-phase / layer-intro-author (NOT a defect). L1/L3 `scal` carry no such field; ratification (adopt across the fold cohort vs. keep prose-only) is meta-phase territory. OQ `l2-scal-fold-parent-frontmatter-field-convention` records it.
- **Count-ownership respected** (friction-ledger `parallel-blind-shared-index-count-divergence`): D3 touched ONLY its own `scal` dep-map row in L2/index.md — NOT the §"Vocabulary cohort" "Firm at L2" running list / firm-count, NOT the §"Working Notes" batch tally, NOT the third-category motif naming. **D7 (layer-intro-author) owns the consolidated L2 firm-count + cohort-list + §Working-Notes batch entry + the identity-in-form-floor-leaves third-category naming this cycle.** OQ `l2-index-intro-third-category-and-firm-count-add-scal-floor` records this for D7 (cohort sibling of D2's third-category slug).
- **Fold-cohort do-NOT-merge boundary honored**: `scal` is cited as the arity-1 member of `linear_combination` via the derived identity `scal(α,x) = linear_combination [(α,x)]` (law 4 / fold-specialization), NOT merged — the leaf stays firm + standalone, matching the load-bearing boundary at L2/index.md §"Fold-cohort boundary". The fold-parent is cited in the dep-map row + frontmatter + body §Dependencies.
- `L2/scal.md` is the anchor for the D6-authored `L2-L1/scal-fusion` + L3>L2 `scal` lowering themes co-landing later this cycle. No live forward-links to those unwritten themes (kept plain prose per `rough-in-forward-reference-must-be-plain-text-not-live-link`); OQ `l2-scal-fusion-l3-l2-scal-themes-plain-text-forward-ref-upgrade` flags the future live-link upgrade.
- SUMMARY placement: the report's proposed anchor (`linear_combination` → `scal` → `inner_product`) still applied cleanly — the `linear_combination`/`inner_product` anchor lines remained adjacent on disk (D1's `dot` + D2's `nrm2` registrations landed AFTER `inner_product`), so `scal` slots between its fold-parent and `inner_product`, inside the L2 sub-list. Discoverability preserved.
- deferred integrated_at to finalize per role-spec.

---

## 2026-06-01T051607Z-cycle-041-abstractor-dot-themes (D4)
applied_at: 2026-06-01T060800Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2-L1/dot-leaf-identity.md (created — firm L2>L1 thin-identity theme; slug = `dot-leaf-identity`, the producer's correct rename from the dispatch-proposed `dot-fold-specialization`)
- book/src/L3-L2/dot-body-identity.md (created — firm L3>L2 thin-identity theme)
- book/src/L2-L1/index.md (dep-map ROW inserted after the `inner-product-fold-specialization` row; D4's own `dot-leaf-identity` row only)
- book/src/L3-L2/index.md (dep-map ROW inserted after the `krylov-step-body-identity` row, before `ksp-solve-outer-driver`; D4's own `dot-body-identity` row only)
- book/src/SUMMARY.md (TWO registrations: `[dot-body-identity]` after `krylov-step-body-identity` under L3>L2 Part; `[dot-leaf-identity]` after `inner-product-fold-specialization` under L2>L1 Part — both as proposed by the report)
- scaffolding/open-questions.md (appended — D4 OQ section; 3 entries, the design-fork promoted prominently)

Gate hits:
- citecheck scan: 17 ok, 0 failing (no MISS/AMBIG/OOB)
- fence-parity: 0 (both new bodies use 4-space-indented signature/mapping-table blocks, no nested ```text fences; `## Status` + full apparatus INSIDE each body block — critic confirmed 6 balanced code-fence pairs, the lone odd backtick run at CYCLE.md:574 is an inline literal in prose)
- SUMMARY-registration: 0 (both registrations explicitly proposed by the report; applied as-proposed, not discretionary)
- index-placeholder displacement: 0 (both index.md theme-list tables already populated; rows inserted after existing anchors)
- implied-component stub: 0 (no plain-text forward-ref needing materialization — both new themes cross-link each other + `../L2/dot.md`, all live on disk at the single post-stage build: D1's `L2/dot.md` already landed, the two D4 themes co-land here)
- variant-axis / forward-edge / H1 / retroactive-budget: 0 (firm identity themes; tdot variant axis covered + explicitly mapped identity-in-form across each edge; no forward-edge claims without surface)

Open questions promoted:
- dot-l2-leaf-floor-vs-fold-only-design (LOAD-BEARING batch-12 META-PHASE SIGNAL — PROMOTED PROMINENTLY)
- l3-dot-lowers-to-non-adjacent-l1-wants-reanchor-to-new-l2-floor-d4-converging-flag (converges with D1's same-named flag)
- dot-tdot-type-api-surface-only-caveat-inherited

Build-relevant: yes

Notes:
- META `overall_status: ready`; all 8 critic checks pass; all `repairs: not-needed` (zero defects; the two critic observations are non-defects routed to the integrator — co-landing sequencing + OQ-promotion).
- **Slug rename applied**: the L2>L1 chapter is `dot-leaf-identity` (NOT the dispatch-proposed `dot-fold-specialization`). The producer applied the rename in-report (§"Naming decision") and the critic confirmed it correct under plan-kind-consistency: `inner-product-fold-specialization`'s RHS IS `L1/dot`, so the `-fold-specialization` suffix would both misname an identity-leaf-edge as a fold-dispatch AND collide conceptually with the existing fold-parent. File/slug/SUMMARY/dep-map all use `dot-leaf-identity`. The L3>L2 slug `dot-body-identity` kept as proposed.
- **LOAD-BEARING design-fork OQ `dot-l2-leaf-floor-vs-fold-only-design` promoted PROMINENTLY** per dispatch directive — a genuine wave-1 contradiction (D1 built the same-named leaf-floor; D2 argued fold-only). Cross-linked to the wave-1 D1 + D2 reports in the OQ body. This governs the WHOLE cycle-041 L2 BLAS-1 floor cohort (D1 `dot` / D2 `nrm2` / D3 `scal`) + the D7 third-category motif naming, not just D4's themes. **integrator-finalize + the batch-12 meta-phase should treat this as the headline cycle-041 design signal**; the meta-phase should adjudicate the leaf-floor-vs-fold-only design before the D4 themes (and the D1 chapter) are treated as design-final. The D4 themes are self-coherent under the D1 leaf-floor reading they are built on (recorded in each theme's §Applicability-conditions + §Status design-presupposition note).
- **Count-ownership respected** (friction-ledger `parallel-blind-shared-index-count-divergence`): D4 touched ONLY its own dep-map rows in L2-L1/index.md + L3-L2/index.md — NOT any consolidated theme-count tally, NOT the §"Vocabulary cohort"/"Working Notes" running lists. **D7 (layer-intro-author) owns the consolidated L2-L1 + L3-L2 tallies + cohort-list additions this cycle.** (D4's report §"Anchor note for the integrator" on both index edits explicitly states this.)
- **Co-landing sequencing**: D1's `L2/dot.md` already on disk (landed earlier this cycle); the two D4 themes cross-link each other + `../L2/dot.md`. All three resolve at the single post-stage `cargo make book` build (integrator-finalize runs it). No live forward-link to an absent file.
- Downstream-consistency touch on `book/src/L3/dot.md` §"Lowers to" (re-anchor to the new adjacent L2 floor + the `dot-body-identity` theme) is NOTED-not-actioned — converges with D1's `l3-dot-lowers-to-non-adjacent-l1-wants-reanchor-to-new-l2-floor` OQ; out of D4 abstractor scope (firm L3 entry edit is harvester/lifter scope).
- deferred integrated_at to finalize per role-spec.

---

## 2026-06-01T051607Z-cycle-041-abstractor-nrm2-themes (D5)
applied_at: 2026-06-01T061400Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2-L1/nrm2-fold-specialization.md (created — firm L2>L1 thin-identity theme; repairer-fixed directive `new:`; section-anchor `§"Fold-cohort boundary"`→`§"Consumer (NOT an instance)"` applied as-corrected)
- book/src/L3-L2/nrm2-body-identity.md (created — firm L3>L2 thin-identity theme; repairer-fixed directive `new:`; same section-anchor correction applied)
- book/src/L2-L1/index.md (dep-map ROW inserted after the D4 `dot-leaf-identity` row; D5's own `nrm2-fold-specialization` row only)
- book/src/L3-L2/index.md (dep-map ROW inserted after the D4 `dot-body-identity` row, before `ksp-solve-outer-driver`; D5's own `nrm2-body-identity` row only)
- book/src/SUMMARY.md (TWO registrations: `[nrm2-body-identity]` after `dot-body-identity` under L3>L2 Part; `[nrm2-fold-specialization]` after `dot-leaf-identity` under L2>L1 Part — both as proposed by the report)
- scaffolding/open-questions.md (appended — D5 OQ section; 2 entries)

Gate hits:
- citecheck scan: 4 ok, 0 failing (no MISS/AMBIG/OOB)
- fence-parity: 0 (both new bodies use 4-space-indented signature/mapping-table blocks, no nested ```text fences; `## Status` + full apparatus INSIDE each body block — critic confirmed 6 balanced fence pairs, even parity; conversion-to-indent done correctly)
- SUMMARY-registration: 0 (both registrations explicitly proposed by the report; applied as-proposed, not discretionary)
- index-placeholder displacement: 0 (both index.md theme-list tables already populated; rows inserted after existing D4 anchors)
- implied-component stub: 0 (no plain-text forward-ref needing materialization — both new themes cross-link each other + `../L2/nrm2.md` (D2 landed) + `../L3/nrm2.md`/`../L1/nrm2.md`/`krylov-step-body-identity`/`inner-product-fold-specialization` — all live on disk)
- variant-axis / forward-edge / H1 / retroactive-budget: 0 (firm identity themes; single element-type variant axis covered + explicitly collapsed identity-in-form across each edge; no forward-edge claims without surface)

Open questions promoted:
- nrm2-l2-floor-rides-l2-floor-under-l3-blas1-cohort-design-fork (rides the SAME load-bearing batch-12 meta-phase signal as D4's `dot-l2-leaf-floor-vs-fold-only-design`)
- nrm2-fold-specialization-slug-vs-consumer-framing-rename-candidate (slug-naming tension vs D4's `dot-leaf-identity` — meta-phase signal per dispatch)

Build-relevant: yes

Notes:
- META `overall_status: ready`; all 8 critic checks pass (two `warning`s both repaired); repairs applied = (1) section-anchor `§"Fold-cohort boundary"`→`§"Consumer (NOT an instance)"` in both bodies — applied as-corrected (the do-NOT-merge consumer discipline lives in `L2/inner_product.md` §"Consumer (NOT an instance)" `:390`, NOT a `Fold-cohort boundary` heading); (2) directive `edit:`→`new:` on the two NEW theme files (both confirmed absent on disk before apply). The four index/SUMMARY blocks are `edit:` against existing files.
- **Co-land dependency RESOLVED**: both themes reference `../L2/nrm2.md` (LHS of L2>L1 / RHS of L3>L2) — D2 (`harvester-L2-nrm2`) landed `book/src/L2/nrm2.md` earlier this cycle (confirmed on disk before apply), so the live links resolve at the single post-stage build. D1's `L2/dot.md` (referenced transitively via the sibling `dot-leaf-identity`/`dot-body-identity` D4 themes) also on disk.
- **Count-ownership respected** (friction-ledger `parallel-blind-shared-index-count-divergence`): D5 touched ONLY its own dep-map rows in L2-L1/index.md + L3-L2/index.md — NOT any consolidated theme-count tally, NOT the §"Vocabulary cohort"/"Working Notes" running lists, NOT the BLAS-1-leaf-floor third-category motif naming. **D7 (layer-intro-author) owns the consolidated L2-L1 + L3-L2 tallies + cohort-list additions + §Working-Notes batch entries this cycle.** (The report's §"Open questions / caveats" COUNT-OWNERSHIP bullet explicitly states this.)
- **Consumer-not-fold-member framing honored**: both `nrm2` themes carry the `√ ∘ inner_product` at `y=x` CONSUMER framing (NOT a fold member) verbatim through both edges, matching the do-NOT-merge boundary at `L2/inner_product` §"Consumer (NOT an instance)" + the D2 `L2/nrm2` floor. The `std::abs` load-bearing numerical guard is correctly handled as preserved-at-L2 / absorbed-at-L1 (non-negativity claim), not silently dropped.
- **DESIGN-FORK dependency (for integrator-finalize + batch-12 meta-phase)**: the existence of the L2 `nrm2` floor (LHS/RHS of the two D5 themes) rides the SAME `l2-floor-under-l3-blas1-cohort` leaf-floor-vs-fold-only fork that D4 promoted PROMINENTLY as `dot-l2-leaf-floor-vs-fold-only-design`. If the meta-phase adopts the fold-only reading, the D5 L2>L1 theme dissolves and the D5 L3>L2 theme re-homes as a non-adjacent in-line identity note at `L3/nrm2`. The D5 themes are self-coherent under the D1 leaf-floor reading they are built on. The whole cycle-041 L2 BLAS-1 floor cohort (D1 `dot` / D2 `nrm2` / D3 `scal` + the D4/D5 lowering themes) shares this single headline design signal — the meta-phase should adjudicate it before treating the cohort as design-final. OQ `nrm2-l2-floor-rides-l2-floor-under-l3-blas1-cohort-design-fork` cross-links D4's prominent OQ.
- **SLUG-NAMING tension (meta-phase signal)**: D5 kept `-fold-specialization` (per its dispatch instruction to mirror the precedents) while D4 *renamed* its sibling L2>L1 `dot` theme to `dot-leaf-identity` — producing a divergent slug convention across the two sibling BLAS-1-leaf thin-identity themes (D4 `dot-leaf-identity` vs D5 `nrm2-fold-specialization`, same shape). Recorded as OQ `nrm2-fold-specialization-slug-vs-consumer-framing-rename-candidate` for a batch-12 meta-phase / lowering-verifier rename-reconciliation audit. NOT a hard defect — both slugs resolve cleanly in SUMMARY/index; body content is slug-agnostic.
- `verified_against:` blocks deferred to a `lowering-verifier` cycle per the sibling-theme convention (both themes `firm` on positively-anchored fully-specified source; the audit block is corroboration, not a promotion gate).
- deferred integrated_at to finalize per role-spec.

---

## 2026-06-01T051607Z-cycle-041-abstractor-scal-themes (D6)
applied_at: 2026-06-01T062100Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2-L1/scal-fold-specialization.md (created — firm L2>L1 thin-identity theme; arity-1 degenerate single-term shadow of `linear-combination-fold-specialization`, fold member cited NOT merged)
- book/src/L3-L2/scal-body-identity.md (created — firm L3>L2 thin-identity theme; identity-in-form on the body, no wrapper to rotate — leaf-primitive counterpart of `krylov-step-body-identity`)
- book/src/L2-L1/index.md (dep-map ROW inserted immediately after the `linear-combination-fold-specialization` anchor row; D6's own `scal-fold-specialization` row only)
- book/src/L3-L2/index.md (dep-map ROW inserted immediately after the `ksp-solve-outer-driver` anchor row, before §Working Notes; D6's own `scal-body-identity` row only)
- book/src/SUMMARY.md (TWO registrations: `[scal-fold-specialization]` after `linear-combination-fold-specialization` under L2>L1 Part; `[scal-body-identity]` after `ksp-solve-outer-driver` under L3>L2 Part — both as proposed by the report)
- scaffolding/open-questions.md (appended — D6 OQ section; 2 entries)

Gate hits:
- citecheck scan: 10 ok, 0 failing (no MISS/AMBIG/OOB)
- fence-parity: 0 (both new bodies use 4-space-indented signature/mapping-table blocks, ZERO triple-backtick fences in either file — no nested-fence truncation risk; `## Status` + full apparatus all inside each body)
- SUMMARY-registration: 0 (both registrations explicitly proposed by the report; applied as-proposed, not discretionary)
- index-placeholder displacement: 0 (both index.md theme-list tables already populated; rows inserted after existing named anchors)
- implied-component stub: 0 (no plain-text forward-ref needing materialization — both new themes cross-link each other + `../L2/scal.md` (D3 landed earlier this cycle, confirmed on disk) + firm `../L1/scal.md` / `../L3/scal.md` / `linear-combination-fold-specialization` / `krylov-step-body-identity`, all live on disk)
- variant-axis / forward-edge / H1 / retroactive-budget: 0 (firm identity themes; element-type + scalar-promotion variant axes covered + explicitly collapsed identity-in-form across each edge; no forward-edge claims without surface)

Open questions promoted:
- scal-leaf-vs-linear-combination-fold-realization-fork (rides the SAME load-bearing batch-12 meta-phase signal as D4's `dot-l2-leaf-floor-vs-fold-only-design` + D5's `nrm2-l2-floor-rides-...-design-fork`)
- scal-fold-specialization-slug-vs-leaf-identity-rename-candidate (third divergent-slug data point in the cohort; sibling to D5's slug OQ)

Build-relevant: yes

Notes:
- META `overall_status: ready`; all 8 critic checks pass; all `repairs: not-needed` (zero defects; both new theme files confirmed `new:` directives by the repairer — no `edit:`→`new:` fix needed, unlike D2/D5). Both files confirmed absent on disk before apply; created via `Write`.
- **`palace/linalg/vector.cpp:207-211` pinpoint integrated UNCHANGED** per the dispatch anti-regression directive + the critic/repairer anti-repair flag: the `if (si == 0.0)` two-real-call promotion branch body spans :207-211 exactly (critic verified by direct Read of `vector.cpp:200-227`). The exploratory `--anchor 'imag'` `[DRIFT -1]`→:206 is a wrong-token false-positive (`s.imag()` is *read* at :206, one line above the cited branch body), NOT producer drift. Both new files cite `207-211` correctly (grep-confirmed at scal-fold-specialization.md:104,173 + scal-body-identity.md:201). Did NOT regress :207→:206.
- **Co-land RESOLVED**: D3's `book/src/L2/scal.md` (LHS of the L2>L1 theme / RHS of the L3>L2 theme) landed earlier this cycle — confirmed on disk before apply (ls + citecheck). The live `[scal](../L2/scal.md)` links in both new themes resolve at the single post-stage `cargo make book` (integrator-finalize runs it). No live forward-link to an absent file.
- **Count-ownership respected** (friction-ledger `parallel-blind-shared-index-count-divergence`): D6 touched ONLY its own dep-map rows in L2-L1/index.md + L3-L2/index.md — NOT any consolidated theme-count tally, NOT the L2-L1/index §"Vocabulary cohort" firm-list, NOT the §"Working Notes" cohort-growth log, NOT the L3-L2/index §Working-Notes. **D7 (layer-intro-author) owns the consolidated L2-L1 + L3-L2 tallies + cohort-list additions + §Working-Notes batch entries this cycle.** (The report's §"Count-ownership note" + two per-index insertion notes explicitly state this.)
- **Fold-cohort do-NOT-merge boundary honored**: `scal` is cited as the arity-1 member of `linear_combination` via the law-6 identity `scal(α,x) = linear_combination [(α,x)]`, NOT merged — the leaf keeps its own standalone L2 floor (D3) and its own L2>L1 edge (this theme), the fold's arity-1 row factored out under the load-bearing `L2/index.md` §"Fold-cohort boundary".
- **DESIGN-FORK dependency (for integrator-finalize + batch-12 meta-phase)**: both D6 themes ride the SAME `l2-floor-under-l3-blas1-cohort` leaf-floor-vs-fold-only fork that D4 promoted PROMINENTLY (`dot-l2-leaf-floor-vs-fold-only-design`) and D5 echoed. The whole cycle-041 L2 BLAS-1 floor cohort (D1 `dot` / D2 `nrm2` / D3 `scal` + the D4/D5/D6 lowering themes) shares this single headline design signal — the meta-phase should adjudicate it before treating the cohort as design-final. D6 themes are self-coherent under the (b) leaf-floor reading they are built on. OQ `scal-leaf-vs-linear-combination-fold-realization-fork` cross-links D4/D5's prominent OQs.
- **SLUG-NAMING tension (meta-phase signal)**: D6 kept `-fold-specialization` (per dispatch). With D4 (`dot-leaf-identity`) and D5 (`nrm2-fold-specialization`) this is the THIRD divergent-slug data point in the cohort — recorded as OQ `scal-fold-specialization-slug-vs-leaf-identity-rename-candidate` for the batch-12 rename-reconciliation audit (track jointly with D5's slug OQ). NOT a hard defect — resolves cleanly in SUMMARY/index, body slug-agnostic.
- **Non-adjacent L3>L1 identity stays in-line** per CLAUDE.md invariant — the transitive L3>L1 `scal` identity (the `scal-body-identity` L3>L2 ∘ the `scal-fold-specialization` L2>L1) is captured by these two adjacent themes composing; no `book/src/L3-L1/` directory. Noted in `scal-body-identity` §Open-questions.
- deferred integrated_at to finalize per role-spec.

---

## 2026-06-01T051607Z-cycle-041-layer-intro-author-index-refresh (D7)
applied_at: 2026-06-01T064500Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/index.md (§Semantics third motif "identity-in-form BLAS-1 floors" + §Vocabulary-cohort "Firm at L2" floor sub-group (3 bullets) + §Working-Notes cycle-041 cohort note w/ design-fork + slug-naming signals; firm 9 → 12, deflate unchanged at 1)
- book/src/L2-L1/index.md (§Vocabulary-cohort floor-edge sub-group (3 bullets) + §Working-Notes cohort-growth-log prepend + design-fork bullet; firm 7 → 10, deflate-composition-lowering unchanged at 1)
- book/src/L3-L2/index.md (§Vocabulary-cohort subsection PROMOTED first-time at this index (2 pre-existing + 3 new BLAS-1-leaf body edges) + §Working-Notes cohort-growth/coverage-gap-progress + design-fork; firm 2 → 5; l3-l2-rotation-theme-coverage-gap 2-of-18 → 5-of-18)
- scaffolding/open-questions.md (appended — D7 OQ section; 3 entries)

Gate hits:
- citecheck scan: 3 ok, 2 failing (both MISS are scaffolding/ plan-item pointers — roadmap.md:116, priorities.md:62 — which citecheck does NOT search; critic confirmed both resolve verbatim: priorities.md:62 = l3-l2-rotation-theme-coverage-gap line, roadmap.md:116 = foundation_solidity weight block. NOT source-range citation defects into reference/; non-blocking)
- retroactive-budget per-slice / global: 0
- concept_writes / forward-edge / edge-label / H1 / append-on-missing-slug / variant-axis: 0
- SUMMARY-registration auto-fix: 0 (D7 created NO files — all 9 chapters landed via D1-D6; D7 touches index prose + counts only)
- index-placeholder displacement: 0 (all three indices already populated)
- implied-component stub: 0 (no plain-text forward-ref to materialize — all referenced slugs landed via D1-D6, live on disk)
- bookkeeping incomplete: 0

Open questions promoted:
- dot-l2-leaf-floor-vs-fold-only-design-D7-consolidated-reaffirmation (CONSOLIDATION pointer; canonical OQ dot-l2-leaf-floor-vs-fold-only-design already filed under D4 — track jointly as the single batch-12 meta-phase adjudication)
- l3-l2-coverage-gap-denominator-live-tracking
- l3-l2-vocabulary-cohort-promotion-first-at-this-index

Build-relevant: yes

Notes:
- D7 applied LAST in the wave-3 serial sequence per dispatch + META suggested-resolution. All six producer landings (D1 dot / D2 nrm2 / D3 scal floors; D4/D5/D6 L2>L1 + L3>L2 themes) confirmed on disk before tallying.
- **Consistency verification PASSED** against on-disk row enumeration (D1-D6 rows had shifted line numbers but anchor TEXT matched verbatim — confirmed, not line-number-matched):
  - L2/index.md dep-map = 13 rows (9 original firm + dot/nrm2/scal at lines 53/55/56 + deflate) = **12 firm + 1 partly-constructive**; D7 cohort list = 9 + 3 = 12 firm + deflate. ✓ matches.
  - L2-L1/index.md theme-list = 11 rows (7 original firm + deflate-composition-lowering + dot-leaf-identity + nrm2-fold-specialization + scal-fold-specialization) = **10 firm + 1 partly-constructive**; D7 cohort list = 7 + 3 = 10 firm + deflate. ✓ matches.
  - L3-L2/index.md theme-list = 5 rows (krylov-step-body-identity + dot-body-identity + nrm2-body-identity + ksp-solve-outer-driver + scal-body-identity) = **5 firm**; D7 cohort subsection = 2 + 3 = 5 firm. ✓ matches.
- **deflate / deflate-composition-lowering held OUT of firm tallies** (unchanged at 1 each) — verified NOT folded into the firm counts at any index.
- **`5-of-18` denominator left as-authored** — the 18 denominator is the plan-item's (priorities.md:62 / roadmap.md:116), maintained by planner/meta-phase; D7 did not re-count the L3 index (out of count-owner scope). OQ l3-l2-coverage-gap-denominator-live-tracking flags this for finalize/planner to use the live denominator if it has drifted.
- **L3>L2 §Vocabulary-cohort subsection PROMOTED first-time at this index** (crossed ≥3-firm threshold 2→5) — D7 prose subsection (substantive krylov/ksp pair vs thin-identity BLAS-1-leaf cohort); does NOT collide with the producers' theme-list TABLE row appends (different section — prose cohort vs table). OQ l3-l2-vocabulary-cohort-promotion-first-at-this-index records its collapsibility.
- **Two meta-phase signals surfaced PROMINENTLY in all three index §Working-Notes** (per dispatch focus item): the leaf-vs-fold design fork (dot-l2-leaf-floor-vs-fold-only-design) and the L2>L1 slug-naming split (dot-leaf-identity vs nrm2/scal -fold-specialization). Framed capture-not-resolve; the canonical fork OQ + the slug OQs are already on the ledger under D4/D5/D6; D7's appended OQs reaffirm + cross-link them as the consolidated batch-12 adjudication.
- D7 created NO new files, touched NO dep-map/theme-list ROW (those are D1-D6's), NO chapter body, NO SUMMARY.md — confined to the three indices' orientation prose + the three consolidated counts (count-ownership partition, friction-ledger parallel-blind-shared-index-count-divergence; D7 is SOLE count-owner this cycle).
- deferred integrated_at to finalize per role-spec.

---
