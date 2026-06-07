---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T161500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-07T163000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of L4>L3 theme sketch — mk-matrix-free-operator-dissolution

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` reports 16 ok / 2 "failing", where the 2 are `[AMBIG]` basename-resolution artifacts on `operator.cpp` (matches both `linalg/operator.cpp` and `fem/libceed/operator.cpp`), NOT bounds failures — the report fully qualifies both as `palace/fem/libceed/operator.cpp:182-189` and `:483`, which is unambiguous and correct. All load-bearing L0 pinpoints verified on-disk via codemap `read_range` + per-line `grep -n`: `bilinearform.cpp:28` (`BilinearForm::PartialAssemble` signature), `:54` (`for (const auto &[geom, data] : mesh.GetCeedGeomFactorData(ceed))` — the per-geometry element loop), `:65/:67` (`GetCeedElemRestriction` trial/test), `:68/:69` (`GetCeedBasis`), `:75` (`integ->Assemble(...data.geom_data, data.geom_data_restr, &sub_op)`), `:77` (`op->AddSubOperator`), `:104` (`op->Finalize()`), `:118/:143` (`UseFullAssembly` predicate + the partial-vs-full branch), `:37-46` (the composite `ceed::Operator`/`SymmetricOperator` make_unique block) — all confirmed exact. `operator.cpp:182-189` confirmed: `void Operator::Mult(...) { y = 0.0; CeedAddMult(op,u,v,x,y); if (dof_multiplicity.Size()>0) y *= dof_multiplicity; }` — matches the report's transcription verbatim, including the `dof_multiplicity` post-scale. `operator.cpp:483` (`CeedOperatorAssembleCOO`, the `full`-variant boundary) confirmed. No `verified_against:` YAML block is emitted (the `## Verified-against` section is prose, not a fenced YAML payload), so the round-trip sub-check is N/A. Every claim carries a pointer and the pointers are in-range.

**surface-or-evidence — pass.** This is a new L4>L3 lowering theme (refinement-shaped: a new chapter, not a backfill). It modifies surface (a new theme chapter + index/SUMMARY rows) AND carries the rotation_claim evidence (the L0 `PartialAssemble`/`Mult` witnesses + the firm L2/L1 RHS constituents). Record-definition sub-check: the signature names `FESpace`, `WeakFormTerm`, `GeomFactors`, `LinearOperator` — but the theme explicitly transcribes these from the firm L4 cap `mk_matrix_free_operator` and the firm L2/L1 substrate chapters as their definition homes (USED+LINKED, not newly introduced here), and `GeomFactors`/`geom_factor_build` resolve to the firm `L1/geom_factor_build.md`. No signature-named record is described only by use without a definition home. Pass.

**rotation-quality — pass (load-bearing; verified GENUINE).** The asserted rotation is the flat global true-dof shape `Tensor[(N: ...)]` → element-local rank-tensor family `[(E,L)]`/`[(E,P,C)]`/`[(E,P,G)]`, plus the atomic-constructor-build → explicit-per-geometry-type-element-loop iteration shift. This is a genuine vocabulary translation, NOT a degenerate identity-in-named-terms rename: the L4 surface carries NO `E`/`L`/`P`/`C`/`G` axes at all (the L4 operator is a black box over the flat `(N: ...)` operator-domain group, the apply named only by its lowering to the L2 combinator); those axes materialize ONLY when the black-box apply is dissolved into the element-iterated contraction sweep, with `element_restrict`'s `G`/`Gᵀ` as the boundary between the two shape vocabularies. The L3 form is strictly more explicit/structured (state/structure exposure: the once-atomic build becomes an explicit element loop mutating a composite; the opaque `GeomFactors` becomes the rank-structured `[(E,P,G)]` carrier). This is the "state hiding / coarser substitution exposed" pass case, not the 1:1 smell. Pass.

**variant-axis-coverage — pass.** The orthogonal axes are addressed: (a) domain-vs-boundary integrator families — covered by the per-geometry-type loop (the volume / dimension−1 split, `bilinearform.cpp:71-77`/`:90-97`); (b) trial==test vs trial≠test — covered by the `SymmetricOperator` vs `Operator` construction note (`:37-46`); (c) the matrix-free (partial) vs materialized-CSR (full) representation axis — explicitly scoped out as a Palace-owned variant on the cap (`UseFullAssembly` false branch is THIS theme; `CeedOperatorFullAssemble`/`:483` is the `full` variant, named for the boundary, not covered). No hidden branch. Pass.

**cross-reference-integrity — warning.** All `[link]` targets resolve on disk (`L2/matrix-free-operator-apply`, the four `L1/*` substrate ops, `L1/libceed-quadrature-kernel-impl`, `L4/mk_matrix_free_operator`, `L4-L3/fe-assemble-fold-dissolution`, `concepts/element-local-tensor`, `concepts/build-time-vs-run-time-stratification`, `semantics/index`, `L3/apply_linop`, `L0/fem-bilinearform-file`, `L1-L0/fe-assemble-libceed-boundary-obstruction`, `L4-L3/index`, `SUMMARY.md` — all present). The `[4]` index-tally replacement string matches the on-disk line `L4-L3/index.md:72` exactly (the "10 → 11 / 11 firm … bc-elimination… this cohort" sentence), so that surgical replace is well-anchored. The table-row `[2]` and the Vocabulary-cohort bullet `[3]` insertion anchors are alpha-correct (after `ksp-solve-driver-dissolution`, before `solve-family-map-dissolution`; the bullet sublist's immediate alpha neighbors are `frequency-sweep` / `solve-family`, which the report correctly names). **However, two insertion anchors give the WRONG alphabetical slot** — see Issues found. The firm-body-inside-fence build-readiness guard PASSES: fence parity is even (6 fences = 3 balanced blocks), and the full firm apparatus (`## Status` + L4-form signature + the algebraic-laws-via-L2-combinator + the Verified-against/Evidence) sits INSIDE the first new-chapter fence (report lines 50–526).

**edge-label-fidelity — pass.** The edge label is L4→L3 throughout, and the prose discusses exactly that edge: LHS = the L4 `mk_matrix_free_operator` constructor; RHS = the L3 explicit element-iterated contraction sweep. The `depends-on (composes)` edges target the L2 combinator + four L1 substrate ops, and the prose composes exactly those by name. The `reference` edges (`lowers` to the L4 cap, `sibling` to `fe-assemble-fold-dissolution`) are discussed in matching prose. Rank-invariant sub-check (graded-stack #9): the `depends-on` constituents are ALL firm on disk (verified: `L2/matrix-free-operator-apply` rank firm; `L1/element_restrict`, `L1/basis_apply`, `L1/quad_point_contract`, `L1/geom_factor_build` all rank firm) — so a `firm` theme resting only on firm `depends-on` deps satisfies `rank(u) ≤ min(deps) = firm`. The L4 cap is `status: roadmap_goal` on disk (D1 has not yet flipped it), but the edge to the cap is `reference` (`kind: lowers`), which constrains nothing — correctly NOT a `depends-on` edge, and the report flags the firm-flip dependency in Open questions. No rank violation. Reachability (#10): the theme reaches a feature root via the cap's backend-lowering column (a `reference` edge to a root, the OWN-COMPOSITION path); since its `depends-on` constituents are independently root-reachable firm vocabulary, the theme is live. Pass.

**plan-kind-consistency — pass.** Declared `kind: lowering-theme`, `rank: firm`. Content shape matches: a complete L4-form / L3-form / applicability-conditions / justification-kind / DISSOLUTION-HOME-verdict structure with exhaustive positive-source citations and no rough-in placeholders. The `firm`-on-structural-rotation claim is justified (read directly off positive Palace source; firm-on-positive-structure — no test gates the contraction-composition syntactic identity). No mis-classification.

**skill-uptake-survey — warning (telemetry, non-blocking).** The report references `citecheck --anchor` for citation verification (good uptake). The shape of the `[3-block]` SUMMARY insert + the `[1]` frontmatter-list alpha insert is exactly the situation the `summary-md-surgical-insert` skill governs (alpha-positioned surgical insertion into SUMMARY.md / list-of-API sections), and that skill was NOT referenced — and the alpha mis-placement (see Issues) is precisely what invoking it would have caught. The `proposed-changes-fence-encloses-full-body-guard` was effectively satisfied (body inside fence) but not cited. Surfacing as telemetry, not blocking.

### Issues found

1. **Wrong alphabetical slot in the SUMMARY.md insert `[3-block]` (`CYCLE.md:546-549`) — `cross-reference-integrity` / alpha-ordering invariant.** The instruction places `mk-matrix-free-operator-dissolution` "after `iterate-while-with-prev-dissolution`, before `krylov-step-typed-wrapper-dissolution`" (i.e. between SUMMARY.md lines 99 and 100). The SUMMARY.md `# L4 > L3` Part is alphabetically ordered on disk (bc, fe, fgmres, fold, frequency, gmres, iterate-while, iterate-while-with-prev, krylov, ksp, solve-family). `mk` sorts AFTER both `krylov-step` (line 100) and `ksp-solve-driver-dissolution` (line 101). The correct alpha slot is **after `ksp-solve-driver-dissolution` (line 101), before `solve-family-map-dissolution` (line 102)**. Severity: low/mechanical (a mis-placed-but-valid link; build still succeeds, but it violates the alphabetical-list invariant `feedback_mdbook_subchapter_grouping_and_alpha_api`).

2. **Wrong alphabetical slot in the index frontmatter `reference:` list insert `[1]` (`CYCLE.md:528-531`) — same defect.** The instruction places the entry "between `iterate-while-with-prev-dissolution` and `krylov-step-typed-wrapper-dissolution`" (between `L4-L3/index.md` frontmatter lines 15 and 16). The frontmatter `reference:` list is strictly alphabetical on disk (lines 8–18). `mk` sorts after `krylov-step` (16) and `ksp-solve` (17); the correct slot is **after `ksp-solve-driver-dissolution` (line 17), before `solve-family-map-dissolution` (line 18)**. Severity: low/mechanical.

   Note the report is internally inconsistent: the table-row `[2]` and the Vocabulary-cohort bullet `[3]` use the CORRECT alpha anchor (after `ksp-solve`, before `solve-family`), while `[1]` and the SUMMARY `[3-block]` use the wrong one — so this is an isolated mis-statement of the alpha position in two of the four insertion instructions, not a systematic ordering misunderstanding.

3. **`operator.cpp` citations are basename-ambiguous to the citecheck scan (`CYCLE.md` §Verified-against / §Supporting evidence) — `citation-validity` (cleared, noted for the record).** `citecheck --scan` flags `operator.cpp:182-189` and `:483` as `[AMBIG]` because two files share the basename. The report DOES fully qualify them as `palace/fem/libceed/operator.cpp` in the inputs frontmatter and the §Verified-against body, and on-disk verification confirms the ranges are correct in `fem/libceed/operator.cpp`. No fix required for correctness; flagged only so a downstream re-scan is not mistaken for a real bounds failure. Severity: none (false-positive of the scan tool's basename heuristic).

---

## Repair

### Fixes attempted

- **Finding 1 (warning — alpha-ordering defect):** the SUMMARY.md insert `[3-block]` (CYCLE.md:547) and the index frontmatter `reference:`-list insert `[1]` (CYCLE.md:529) both placed `mk-matrix-free-operator-dissolution` in the WRONG alpha slot ("after `iterate-while-with-prev-dissolution`, before `krylov-step-typed-wrapper-dissolution`"). The correct slot — already used by the `[2]` table-row and `[3]` bullet — is after `ksp-solve-driver-dissolution`, before `solve-family-map-dissolution` (alpha: `ksp` < `mk` < `solve`).
  - **Decision:** repaired.
  - **Verification of on-disk alpha-neighbors before fixing:**
    - `book/src/SUMMARY.md` `# L4 > L3` Part (lines 92–102) is strictly alpha-ordered; `ksp-solve-driver-dissolution` is line 101, `solve-family-map-dissolution` is line 102 — `mk` sorts between them (and AFTER both `krylov-step` line 100 and `ksp-solve` line 101).
    - `book/src/L4-L3/index.md` frontmatter `reference:` list (lines 8–18) is strictly alpha-ordered; `ksp-solve-driver-dissolution` is line 17, `solve-family-map-dissolution` is line 18 — same correct slot.
  - **Action:** edited the 2 mis-stated insert anchors in `reports/2026-06-07T153721Z-abstractor-matrix-free-dissolution/CYCLE.md` §Proposed changes — the `[1]` index-frontmatter `reference:`-list insert instruction (CYCLE.md:529) and the SUMMARY.md `[3-block]` insert instruction (CYCLE.md:547) — to read "after `ksp-solve-driver-dissolution`, before `solve-family-map-dissolution`". All 4 insert instructions (`[1]` frontmatter, `[2]` table-row, `[3]` bullet, SUMMARY `[3-block]`) now name the consistent, alpha-correct slot. No book/ or other-report content touched; the chapter body, table-row text, and tally text were already correct and unchanged.

- **Finding 2 (warning — skill-uptake-survey telemetry):** `summary-md-surgical-insert` skill (which governs this exact alpha-positioned surgical insert into SUMMARY.md / list-of-API sections) was not referenced, and invoking it would have caught the misplacement.
  - **Decision:** not-needed (no content fix beyond finding-1's correction).
  - **Rationale:** non-blocking telemetry. The substantive consequence (the mis-placed anchors) is fully resolved by finding-1's repair; the skill-non-uptake itself is a producer-side telemetry signal for the meta-phase, not a defect in the report's content. No repair action available or required.

### Unrepairable findings

None. The only blocking-adjacent finding (alpha-ordering, finding 1) was a 2-of-4 insert-anchor mis-statement — purely mechanical/surgical, within repair authority, and now corrected. Finding 2 is non-blocking telemetry.

## Suggested resolution

`ready`. Both insert anchors are corrected and consistent with the already-correct table-row/bullet anchors; the integrator can apply all 4 inserts at the single alpha slot (after `ksp-solve-driver-dissolution`, before `solve-family-map-dissolution`) in both `book/src/SUMMARY.md` and `book/src/L4-L3/index.md` frontmatter. Note for the integrator: the report's own §Open-questions flags two finalize-time re-checks (the D1 cap firm-flip dependency for the LHS `reference` link, and the RE11 libceed-substrate sub-cohort grounding re-check on the landed tree) — both are forward-looking dispatch notes, not repair items.
