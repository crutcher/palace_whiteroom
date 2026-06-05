# cycle-106 integrator staging log

Per-report integration landings for cycle-106 (batch-34). Newest LAST, append-only.
Row ORDER is the authoritative apply-order record (NOT the advisory `applied_at` timestamps).

---

## 2026-06-05T201831Z-cycle-106-D1-layer-intro-author-wave3-ksp-krylov
applied_at: 2026-06-05T203515Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/ksp_solve.md (frontmatter migrate: pre-scheme consumes:/lowers_to: → typed edges: block; rank: firm; 5 depends-on + 8 reference; variant_axes: retained verbatim)
- book/src/L4/krylov-step.md (frontmatter authored FROM SCRATCH: prepend edges: block before # krylov-step H1; rank: firm; 7 depends-on + 8 reference)
- scaffolding/open-questions.md (append-only: section krylov-step-pair-wave3-deferred-edges)

Gate hits:
- retroactive-budget (per-slice / global): 0
- concept_writes-on-existing-slug: 0 (frontmatter-only edge migration; no concept page created)
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- H1-reuses-page-heading: 0 (edit-2 prepends frontmatter before the existing H1; H1 unchanged)
- append-on-missing-slug: 0
- variant-axis-missing: 0 (variant_axes: block retained verbatim on ksp_solve)
- SUMMARY.md chapter-registration: not-applicable (both chapters pre-existing + already registered; no new file)
- citecheck bounds/path-hygiene: 0 ok, 0 failing (no path:line-line source citations in the report — frontmatter-only migration; no MISS/AMBIG/OOB)
- graded-stack rank_violations: 0 (HELD; firm/firm well-foundedness — both chapters rank: firm, every depends-on record target rank: firm; iterate-while + L2/krylov-step untyped → rank-check skips, warn-not-fail, scheme-conformant)

Open questions promoted:
- krylov-step-pair-wave3-deferred-edges (3 trigger-gated caveats: dofset-out-of-scope, iterate-while+L2/krylov-step-untyped, 8 non-node concept pages reference-only-encoding-pending)

Build-relevant: yes

Notes:
- THE LEAD of batch-34 WAVE-3 graded-stack typed-edge campaign. Both [old] anchors verified on-disk verbatim before applying (ksp_solve lines 1-15 frontmatter; krylov-step line 1 = bare `# krylov-step`, no leading `---`). Both edits applied cleanly.
- RESCUE IS MEASURABLE on live book/src: graded-stack-lint detritus 163 → 156 (7 nodes rescued). `L4/krylov-step` is now ROOT-REACHABLE (inbound `← L4/ksp_solve, L3/krylov-step`; ksp_solve is itself root-reachable via feature/{driven,electrostatic,magnetostatic}.L4). 5 records leave detritus via inbound `← L4/krylov-step`: sim-state, krylov, step-outputs, prev-carry, solve-result. `op-params` was already live (kept feature/transient.L4 inbound) + gained 2 more. `L4/iterate-while` rescued as a bonus (depends-on edge traversed for reachability though untyped). Confirmed via `--show-inbound` on live tree.
- `concepts/dofset` confirmed STILL garbage post-edit — correct; it is rescued by the sibling out-of-scope `L4/eliminate_bc` WAVE-3 tranche, not this pair.
- All 19 distinct edge targets resolve to on-disk files (5 depends-on + 8 reference on ksp_solve; 7 depends-on + 8 reference on krylov-step; deduped).
- YAML strict round-trip: krylov-step.md FULL frontmatter parses cleanly under yaml.safe_load. ksp_solve.md FULL frontmatter fails strict parse ONLY on the PRE-EXISTING `variant_axes:` `restarted:` mid-scalar colon (on-disk line ~29 col 76) — retained verbatim, NOT introduced by this migration; does not affect the graded-stack linter (custom minimal reader) or mdBook build (chapter renders for many cycles). The `edges:` block I authored sub-parses cleanly under strict YAML (5 depends-on + 8 reference). Matches the critic's documented non-blocking drive-by observation. NOT a defect in this migration; flagged for a future touch of that chapter's variant_axes: frontmatter.
- deferred integrated_at to finalize per role-spec.
- No deferrals.

---

## 2026-06-05T201831Z-cycle-106-D2-layer-intro-author-wave3-solvefamily-foldsolve
applied_at: 2026-06-05T211500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/solve_family.md (frontmatter migrate: pre-scheme consumes:/lowers_to: → typed edges: block; rank: firm; 5 depends-on [ksp_solve, iterate-while, op-params(uses-record), sim-state(uses-record), solve-family-map-dissolution(lowers-to)] + 4 reference; variant_axes: retained verbatim)
- book/src/L4/fold_solve.md (frontmatter migrate: same; rank: firm; 3 depends-on [iterate-while, op-params(uses-record), fold-solve-time-step-dissolution(lowers-to)] + 4 reference incl. solve_family as DELIBERATE contrast-sibling reference NOT depends-on; variant_axes: retained verbatim)
- scaffolding/open-questions.md (append-only: 2 sections — record-TimeState-needs-definition-home, fold_solve-sibling-reference-carries-no-liveness)

Gate hits:
- retroactive-budget (per-slice / global): 0
- concept_writes-on-existing-slug: 0 (frontmatter-only edge migration; no concept page created)
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0 (fold_solve→solve_family reference matches prose "not consumed, referenced for the map/fold distinction" verbatim, fold_solve.md:127)
- H1-reuses-page-heading: 0 (frontmatter-only edits; both H1s unchanged)
- append-on-missing-slug: 0
- variant-axis-missing: 0 (variant_axes: blocks retained verbatim on both chapters)
- SUMMARY.md chapter-registration: not-applicable (both chapters pre-existing + already registered; no new file)
- citecheck bounds/path-hygiene: 2 ok, 1 failing — [AMBIG] `fold_solve.md:161` (bare basename matches book/src/L3/fold_solve.md + book/src/L4/fold_solve.md). NON-BLOCKING: this is a path-hygiene slip in the report's §"Scheme conformance" supporting-evidence NARRATION (a `## Status` cite about the maturity word, independently true — the L4 chapter IS firm), NOT in any landed artifact content (the frontmatter blocks carry zero path:line citations). Intended target is unambiguously book/src/L4/fold_solve.md:161 (the L4 chapter being migrated; the `## Status` heading sits at L4 line 161 per the repairer's on-disk re-confirm of the 162→161 fix). Trivial fix is prepend `book/src/L4/`; report is append-only post-integration so cannot edit — recorded for finalize visibility. No MISS/OOB.
- graded-stack rank_violations: 0 (HELD; "RANK VIOLATIONS: none." on live tree — both source chapters rank: firm, every depends-on target firm: ksp_solve/iterate-while firm caps, op-params/sim-state rank: firm record pages, lowering themes firm-endpoint; rank(u)≤rank(v) firm/firm on every new + migrated depends-on edge)

Open questions promoted:
- record-TimeState-needs-definition-home (single-consumer; in-chapter `## Record definition` is the home; trigger: ≥2-consumer bar trips → concepts/time-state.md page)
- fold_solve-sibling-reference-carries-no-liveness (deliberate reference-not-depends-on; both chapters independently root-reachable)

Build-relevant: yes

Notes:
- THE LEAD of batch-34 WAVE-3 (position 2/5). Both [old] anchors verified verbatim on-disk before applying (solve_family lines 1-16, fold_solve lines 1-16 frontmatter). Both edits applied cleanly.
- D5 RESIDUAL RESOLVED: clearing solve_family's typed edges (all targets exist on disk) leaves NO `[UNRESOLVED] L4/solve_family ->` or `[UNRESOLVED] L4/fold_solve ->` rows in the live linter run — the single residual unresolved_depends_on_targets entry deferred to this owning dispatch is gone. Verified by grep over the linter output.
- RESCUE MEASURABLE on live book/src (--show-inbound): `concepts/sim-state` rescued from `[garbage?]` → inbound `← L4/krylov-step, L4/ksp_solve, L4/solve_family` (gains L4/solve_family from THIS report). `concepts/op-params` inbound climbed → `← L4/fold_solve, L4/krylov-step, L4/ksp_solve, L4/solve_family, feature/transient.L4` (gains BOTH solve_family + fold_solve from this report). Neither flagged garbage post-edit. Both lowering themes carry inbound from their L4 source (solve-family-map-dissolution ← L4/solve_family; fold-solve-time-step-dissolution ← L4/fold_solve).
- All 12 distinct edge targets across both blocks resolve to on-disk .md files (checked individually).
- YAML round-trip: both files' FULL frontmatter fails strict yaml.safe_load ONLY on the PRE-EXISTING `variant_axes:` mid-scalar colons (the unquoted `per-element:`/`state-generated:` prose colons; solve_family ~line 24, fold_solve ~line 20) — retained verbatim, NOT introduced by this migration; identical situation to D1's ksp_solve `restarted:` colon. Does not affect the graded-stack linter (custom minimal reader: RANK VIOLATIONS none) or mdBook build. The `edges:` blocks I authored both sub-parse cleanly under strict YAML (solve_family 5 dep + 4 ref; fold_solve 3 dep + 4 ref). Flagged for a future touch of those chapters' variant_axes: frontmatter.
- TimeState correctly NOT forced into an edge (no concepts/time-state.md home; single-consumer → in-chapter Record definition is the right home) — routed to Open questions per §(f) / record-definition obligation.
- deferred integrated_at to finalize per role-spec.
- No deferrals (the AMBIG citecheck finding is non-blocking report-narration path-hygiene, recorded above for finalize, not an artifact defect).

---

## 2026-06-05T201831Z-cycle-106-D3-layer-intro-author-wave3-eliminatebc
applied_at: 2026-06-05T214500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/eliminate_bc.md (Edit 1 frontmatter migrate: pre-scheme consumes:/lowers_to:/depends_on: → ONE typed edges: block; rank: firm; 4 depends-on [linear_combination(folds), apply_linop(folds), dofset(uses-record), bc-elimination-post-composition-dissolution(lowers-to)] + 5 reference; variant_axes: retained verbatim. Edit 2 §Record-definition prose: retarget DofSet record-home off nonexistent concepts/DofSet.md onto existing concepts/dofset.md (rank: firm), drop stale not-yet-exist / record-DofSet-needs-definition-home flag)
- scaffolding/open-questions.md (append-only: section bc-driver-column-eliminate-bc-edge-gap-blocks-dofset-rescue)

Gate hits:
- retroactive-budget (per-slice / global): 0
- concept_writes-on-existing-slug: 0 (frontmatter-only edge migration + prose retarget; no concept page created — concepts/dofset.md only READ to confirm rank: firm)
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0 (the two reference classifications fe_assemble/essential_dofs match §Dependencies prose verbatim; the four folds/uses-record/lowers-to depends-on match signature body + §Dependencies)
- H1-reuses-page-heading: 0 (frontmatter + body-prose edits; H1 `# eliminate_bc` unchanged)
- append-on-missing-slug: 0
- variant-axis-missing: 0 (variant_axes: diagonal-policy/trial-test-coincidence/bc-data-homogeneity retained verbatim)
- SUMMARY.md chapter-registration: not-applicable (eliminate_bc pre-existing + registered SUMMARY line 62; concepts/dofset registered line 311; no new file)
- citecheck bounds/path-hygiene: 4 ok, 0 failing (no MISS/AMBIG/OOB on the report's 4 reference-resolved cites)
- graded-stack rank_violations: 0 (HELD; "RANK VIOLATIONS: none." on live tree — eliminate_bc rank: firm rests on all-firm depends-on targets: linear_combination/apply_linop firm, concepts/dofset rank: firm, dissolution-theme firm-endpoint; rank(u)≤rank(v) firm/firm on all 4)

Open questions promoted:
- bc-driver-column-eliminate-bc-edge-gap-blocks-dofset-rescue (routed FINDING: faithful column→eliminate_bc first-half edge deliberately NOT forced; recommends WAVE-3-followup adding feature/{electrostatic,magnetostatic,eigenmode}.L4 →composes eliminate_bc to make the dofset/eliminate_bc/firm-L1-BC-cohort rescue measurable)

Build-relevant: yes

Notes:
- WAVE-3 graded-stack typed-edge campaign, position 3/5 (THE LEAD). Both [old] anchors verified on-disk verbatim before applying (frontmatter lines 1-19; §Record-definition prose lines 121-131). Both edits applied cleanly.
- FAITHFUL-PATH-OR-FINDING outcome confirmed on live tree. The `concepts/dofset ← L4/eliminate_bc` uses-record edge IS present and GC-traversed in --show-inbound (confirmed at apply time), AND all four depends-on targets render as inbound edges (L4/linear_combination, L1/apply_linop, concepts/dofset, L4-L3/bc-elimination-post-composition-dissolution all ← L4/eliminate_bc). But dofset stays [garbage?] and eliminate_bc stays [GARBAGE*] — CORRECT: no feature column links to eliminate_bc, so the rescue's first half (column→eliminate_bc) is absent; D3 did NOT force an unfaithful edge, routed the gap as the OQ above. dofset garbage state confirmed directly off the linter output this invocation, not assumed.
- YAML strict round-trip: the FULL eliminate_bc.md frontmatter parses cleanly under yaml.safe_load (unlike D1 ksp_solve / D2 solve_family+fold_solve which fail strict only on PRE-EXISTING variant_axes mid-scalar colons — eliminate_bc's variant_axes are bare slugs with no embedded colons, so no such artifact here). edges: block sub-parses cleanly (4 depends-on, 5 reference).
- DofSet record-definition obligation now genuinely MET: concepts/dofset.md present at rank: firm / kind: record with the cited indices : Set<TrueDofIndex> field; concepts/DofSet.md confirmed ABSENT (case-exact). Edit 2 corrects the dangling reference AND drops the now-satisfied record-DofSet-needs-definition-home flag — no residual dangling flag in the chapter.
- reachable-from-roots reads 89 on live tree (up from D1/D2 prior landings this cycle); this report does NOT change it — the dofset/eliminate_bc rescue is deferred to the routed followup OQ. Not a regression.
- All 9 distinct edge targets (4 depends-on + 5 reference) resolve to on-disk files (checked individually).
- §Caveats in the report (dropped stale flag, fe_assemble left pre-scheme out-of-scope, single-file scope honored) are local apply-notes, not standalone cross-cycle questions — captured here, not promoted as separate OQ sections.
- deferred integrated_at to finalize per role-spec.
- No deferrals.

---

## 2026-06-05T201831Z-cycle-106-D4-lifter-setsubvector-backlink
applied_at: 2026-06-05T221500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/set_subvector_zero.md (frontmatter de-stale: replace doubly-stale `reference: []` + false "L1/set_subvector_zero does not exist" comment → bare-slug `reference` block [L1/set_subvector_zero, concepts/dofset]; page body untouched)
- scaffolding/open-questions.md (append-only: section set-subvector-zero-cluster-reachability-not-rescued-by-reference-backlink)

Gate hits:
- retroactive-budget (per-slice / global): 0
- concept_writes-on-existing-slug: 0 (frontmatter-only de-stale; no concept page created — `concepts/set_subvector_zero` already existed)
- forward-edge-without-surface: 0 (both `reference` targets resolve to on-disk files)
- edge-label/prose-mismatch: 0 (navigational `reference` edges; bare-slug form matches sibling concept pages per critic — `concepts/axpy.md`/`concepts/apply_linop.md`)
- H1-reuses-page-heading: 0 (frontmatter-only edit; `# set_subvector_zero` H1 unchanged)
- append-on-missing-slug: 0
- variant-axis-missing: 0 (not-applicable; frontmatter back-link, no operator variants)
- SUMMARY.md chapter-registration: not-applicable (page pre-existing + already registered; no new file)
- citecheck bounds/path-hygiene: 7 ok, 0 failing (no MISS/AMBIG/OOB)
- graded-stack rank_violations: 0 (HELD; "RANK VIOLATIONS: none." on live tree — this page is a non-node concept page carrying no `rank:` token; `reference` edges constrain neither rank nor liveness)

Open questions promoted:
- set-subvector-zero-cluster-reachability-not-rescued-by-reference-backlink (cross-refs D3's bc-driver-column-eliminate-bc-edge-gap-blocks-dofset-rescue; routes the L1/set_subvector_zero reachability sub-question into the same WAVE-3-followup sweep)

Build-relevant: yes

Notes:
- WAVE-3 graded-stack typed-edge campaign, position 4/5. The `[old]` anchor verified byte-for-byte on-disk before applying (lines 1-6, the `reference: []` block + 3-line false comment). Edit applied cleanly.
- YAML round-trip: the edited frontmatter parses cleanly under yaml.safe_load → `{'edges': {'reference': ['L1/set_subvector_zero', 'concepts/dofset']}}`. No mid-scalar-colon artifact here (unlike D1/D2's pre-existing variant_axes colons — this page has no variant_axes block).
- Both `reference` targets resolve on-disk: `L1/set_subvector_zero` → book/src/L1/set_subvector_zero.md (24662 bytes, firm), `concepts/dofset` → book/src/concepts/dofset.md (present). Reciprocal `concepts/dofset.md` already lists `concepts/set_subvector_zero`, so the edge is now bidirectional.
- Linter on the LIVE tree (with D1/D2/D3 + this D4 edit applied, observed directly this invocation): `RESULT: 0 rank violation(s), 156 detritus, 76 untyped`. `concepts/set_subvector_zero` confirmed REMOVED from the untyped-warning set (now typed). No UNRESOLVED edge involving `set_subvector_zero`/`dofset`.
- EXPECTED-NOT-DEFECT (per report + critic): a `reference` back-link does NOT create reachability — the `set_subvector_zero`/`L1/set_subvector_zero`/`dofset` cluster stays detritus; the page becoming typed (untyped −1) while joining the counted-detritus DAG (the report's c105-baseline +1) is benign. The substantive liveness rescue is routed to the new OQ + D3's eliminate_bc OQ.
- NOTE on counts: the live-tree absolute detritus/untyped counts differ from the report's c105-baseline (163/77 → 164/76) because D1/D2/D3 landed typed-edge migrations earlier this cycle (live detritus is 156, untyped 76). The DIRECTION (this page: untyped −1, joins counted detritus) matches the report exactly — I report only the live on-disk figures I observed this invocation, not the report's baseline-relative deltas.
- deferred integrated_at to finalize per role-spec.
- No deferrals.

---

## 2026-06-05T201831Z-cycle-106-D5-layer-intro-author-unresolved-target-reclassify
applied_at: 2026-06-05T204946Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/assemble_frequency_operator.md (frontmatter migrate: legacy depends_on:/lowers_to: → typed edges: block; 3 depends-on [L2/linear_combination(folds), L1/apply_linop, L1-L0/assemble-frequency-operator-rotation(lowers-to)]; variant_axes: retained)
- book/src/L1/eliminate_rhs.md (frontmatter migrate: legacy lowers_to:/lifts_from:[]/depends_on: → typed edges:; MISSING-PREFIX FIX bare apply_linop→L1/apply_linop, axpy→L1/axpy; 3 depends-on [L1/apply_linop, L1/axpy, L1-L0/fe-operator-assemble-mutation-rotation(lowers-to)])
- book/src/L2/ksp_solve.md (frontmatter migrate: legacy lifts_to:/lowers_from: → typed edges:; 2 depends-on [L3/ksp_solve(lifts-to), L1/ksp_solve(lowers-from)] — DISTINCT from WAVE-3 L4/ksp_solve)
- book/src/L3/apply_linop.md (frontmatter migrate: STRIKE prose lifts_from:(no L4 entry…) + clean lowers_to:; 1 depends-on [L1/apply_linop(lowers-to)]; nested variant_axes: orthogonal/absorbed retained)
- book/src/L3/assemble-diagonal.md (frontmatter migrate: STRIKE prose lifts_from:(none)… + clean lowers_to:; 1 depends-on [L2/assemble-diagonal(lowers-to)])
- book/src/L3/divfree-projector.md (frontmatter migrate: mis-parse(:-in-qualifier) lowers_to: re-encoded + STRIKE prose lifts_from:; 1 depends-on [L2/divfree-projector(lowers-to)] + 1 reference [L2-L1/divfree-projector-leaf-identity, the kept-but-one-edge-further theme]; nested variant_axes: retained)
- book/src/L3/elementwise_product.md (frontmatter migrate: mis-parse lowers_to: + STRIKE prose lifts_from:; 1 depends-on [L2/elementwise_product(lowers-to)])
- book/src/L3/jacobi-smoother.md (frontmatter migrate: mis-parse lowers_to: + STRIKE prose lifts_from:; 1 depends-on [L1/jacobi-smoother(lowers-to)]; nested variant_axes: retained)
- book/src/L3/reciprocal.md (frontmatter migrate: mis-parse lowers_to: + clean lifts_from:; 2 depends-on [L2/reciprocal(lowers-to), L1/reciprocal(lifts-from)])
- book/src/L4/assemble_frequency_operator.md (frontmatter migrate: consumes:→depends-on/reference + mis-parse lowers_to:; 2 depends-on [L4/linear_combination(specializes), L1/assemble_frequency_operator] + 1 reference [concepts/black-box-vs-accelerated-kernels])
- book/src/L4/dot.md (consumes:→depends-on/reference + mis-parse lowers_to:; 2 depends-on [L4/inner_product(specializes), L3/dot] + 2 reference [concepts/black-box-vs-accelerated-kernels, concepts/dot])
- book/src/L4/eigenfreq_qfactor_reduce.md (consumes:→depends-on + STRIKE prose lowers_to:; named L1 scalar-map homes→reference; 1 depends-on [L4/eigsolve] + 2 reference [L1/eigenvalue-untransform, L1/participation_ratio])
- book/src/L4/fe_assemble.md (consumes:→depends-on/reference; container+concepts→reference; 1 depends-on [L4-L3/fe-assemble-fold-dissolution(lowers-to)] + 3 reference [L4/index(navigational-container), concepts/black-box-vs-accelerated-kernels, concepts/state-stratification])
- book/src/L4/frequency_sweep.md (consumes:→depends-on + mis-parse lowers_to:; concept→reference; 4 depends-on [L4/assemble_frequency_operator, L4/ksp_solve, L4/iterate-while, L4-L3/frequency-sweep-dissolution(lowers-to)] + 1 reference [concepts/state-stratification])
- book/src/L4/inner_product.md (consumes:→depends-on/reference + mis-parse lowers_to:; 1 depends-on [L3/inner_product] + 2 reference [concepts/black-box-vs-accelerated-kernels, concepts/dot])
- book/src/L4/linear_combination.md (consumes:→depends-on/reference + mis-parse lowers_to:; 1 depends-on [L3/linear_combination] + 2 reference [concepts/black-box-vs-accelerated-kernels, concepts/scalar-promotion])
- book/src/L4/nrm2.md (consumes:→depends-on/reference + mis-parse lowers_to:; 2 depends-on [L4/inner_product, L3/nrm2] + 2 reference [concepts/black-box-vs-accelerated-kernels, concepts/nrm2])
- book/src/L4/sparameter_reduce.md (consumes:→depends-on + STRIKE prose lowers_to:(the per-port port-mode linear functional …); 1 depends-on [L4/frequency_sweep])
- scaffolding/open-questions.md (append-only: 2 sections — graded-stack-lint-block-mapping-misparse-on-legacy-edge-prose-colon [the linter-reader-bug finding], solve_family-last-unresolved-target-handed-to-d3 [recorded RESOLVED-this-cycle by D2])

Gate hits:
- retroactive-budget (per-slice / global): 0
- concept_writes-on-existing-slug: 0 (frontmatter-only edge migration on 18 PRE-EXISTING chapters; no concept page created)
- forward-edge-without-surface: 0 (every depends-on/reference target resolves to an on-disk file — 36 distinct targets, all present)
- edge-label/prose-mismatch: 0 (depends-on vs reference splits match each chapter's §Dependencies/body prose; lowering-endpoint keys→depends-on, narrative-concept + navigational-container + one-edge-further kept-theme→reference per critic spot-check)
- H1-reuses-page-heading: 0 (frontmatter-only edits; every H1 unchanged)
- append-on-missing-slug: 0
- variant-axis-missing: 0 (the [old] anchors end at the `variant_axes:` line; every host's variant_axes: block retained verbatim, including the nested orthogonal/absorbed mappings on apply_linop/divfree-projector/jacobi-smoother)
- SUMMARY.md chapter-registration: not-applicable (all 18 chapters pre-existing + registered; no new file; SUMMARY.md confirmed unmodified)
- alphabetical-position-insert: not-applicable (no SUMMARY/index row inserted)
- citecheck bounds/path-hygiene: 1 ok, 3 failing — 3 [MISS] all on `graded_stack_lint.py:{211,431,519-543}` (tools/ linter line-refs, NOT under citecheck's reference/* + book/src roots). NON-BLOCKING: these are linter-mechanics citations into the tool itself, already verified EXACT by the critic via direct Read (the bm regex at :211, derive_rank at :431, legacy-key migration at :519-543); they are NOT Palace-source claims and NOT in any landed artifact (frontmatter blocks carry zero path:line citations). No MISS/AMBIG/OOB on any book/reference content.
- graded-stack rank_violations: 0 (HELD; "RANK VIOLATIONS: none." on live tree after applying — `firmness: firm` supplies each host's rank: firm via derive_rank, no rank token added, every depends-on target verified resolving; firm/firm well-foundedness preserved)
- graded-stack unresolved_depends_on_targets (--strict): 0 (THE CAMPAIGN GOAL — 21→0). Live-tree before this report: 20 (D2 already cleared L4/solve_family's residual earlier this cycle, so the 21st was gone). D5's 18 edits cleared the remaining 20: no [UNRESOLVED] rows remain, the UNRESOLVED header line is gone, and `--strict` EXIT CODE is now 0 (was non-zero, gated only by the unresolved count). item-2 sub-target graded-stack-lazy-tail-typing COMPLETE.

Open questions promoted:
- graded-stack-lint-block-mapping-misparse-on-legacy-edge-prose-colon (the linter-reader-bug finding — legacy `:`-in-qualifier items mis-read as block-mapping dicts; D5 migration removed the trigger for these 18 files; latent until next un-migrated `:`-bearing legacy item; routed to P1 campaign for fix-reader-vs-rely-on-migration decision)
- solve_family-last-unresolved-target-handed-to-d3 (RESOLVED-this-cycle: D2's WAVE-3 migration of L4/solve_family cleared the cross-dispatch hand-off; recorded for the record)

Build-relevant: yes

Notes:
- WAVE-3 graded-stack typed-edge campaign, position 5/5 (THE FINAL report this cycle). MEDIUM lazy-tail reclassification: 18 frontmatter-only edits, each migrating legacy edge keys (depends_on:/lowers_to:/lifts_from:/lifts_to:/lowers_from:/consumes:) into a typed `edges:` block. All 18 [old] anchors verified verbatim on-disk before applying (read every host's frontmatter region this invocation); every edit applied cleanly.
- CAMPAIGN GOAL REACHED on the live tree (observed directly this invocation): unresolved_depends_on_targets 20→0, rank_violations HELD 0, --strict exit code 0. Combined with D2's solve_family migration, the full 21 false-positive unresolved targets are cleared. All 21 were confirmed false-positives (un-migrated legacy frontmatter), NOT genuine missing targets — every one of the 36 distinct re-encoded edge targets resolves to an on-disk book/src/<slug>.md (verified by individual existence sweep this invocation).
- YAML round-trip: all 18 `edges:` sub-blocks parse cleanly under strict yaml.safe_load (depends-on + reference lists). NOTABLY all 18 FULL frontmatters also parse cleanly under strict YAML this time — none of these 18 carries the mid-scalar `variant_axes:` colon artifact that D1/D2's WAVE-3 chapters (ksp_solve/solve_family/fold_solve) hit; the bare-slug variant_axes on these hosts have no embedded unquoted colons.
- THREE classes of fix applied, matching the report: (a) STRIKE prose-as-slug — the `(no L4 entry; …)` / `(none) — …` / "the per-mode scalar maps …" / "the per-port port-mode linear functional …" items were genuine prose with no recoverable slug, correctly struck (NOT invented as stubs); case-12's two named L1 scalar-map homes (L1/eigenvalue-untransform, L1/participation_ratio) routed to `reference` (named body-references, not lowering endpoints); (b) re-encode `:`-in-qualifier mis-parses to clean edges:; (c) MISSING-PREFIX fix on L1/eliminate_rhs (bare apply_linop→L1/apply_linop, axpy→L1/axpy — same-layer L1 homes, the correct disambiguation among L1/L2/L3/concepts homonyms per critic).
- WAVE-3 EXCLUSION HONORED: none of the 5 WAVE-3 chapters (L4/{ksp_solve,krylov-step,solve_family,fold_solve,eliminate_bc}) is among the 18 — D5 edits L2/ksp_solve (distinct layer) and the L4 ops (dot/inner_product/nrm2/linear_combination/assemble_frequency_operator/eigenfreq_qfactor_reduce/fe_assemble/frequency_sweep/sparameter_reduce), all distinct from the WAVE-3 set. L4/solve_family deliberately untouched (D2-owned).
- `kind:` annotations (folds/lowers-to/lifts-from/lifts-to/lowers-from/specializes) preserved on the dict-form edges to retain the human-readable edge-type the legacy key encoded; linters ignore them (scheme §2); the bare-string and {target:,kind:} forms are interchangeable.
- No rank token added (the 18 hosts stay rank-typed via firmness: firm); the report deliberately left firmness:→rank: normalization to the P1 campaign — outside this edges-correction-only scope.
- deferred integrated_at to finalize per role-spec.
- No deferrals.

---
