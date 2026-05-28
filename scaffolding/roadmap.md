# Roadmap

A coarse map of what this project intends to cover, what's currently in flight, and what's done. The roadmap is **deliberately abstract**: a few dozen items, not a granular task list. It exists so the README's *Relative Progress* section can report proportional coverage with real denominators.

**Lifecycle.**

- The Meta-Critic reviews this file during every meta-cycle. Items move between `not-started` (`[ ]`), `in-progress` (`[~]`), and `done` (`[x]`) based on what landed in the window. New items are added as scope clarifies; items are not removed without a meta-review note.
- The README builder reads this file to compute the *Relative Progress* coverage report.
- Changes to this file are committed as part of the meta-cycle enactment (or as immediate follow-ups).

Status legend:

- `[x]` — landed; at least one slice at L4 (for solver/algorithm components) or the procedure/concept is in production (for methodology components).
- `[~]` — in flight; slice exists at L1/L2/L3 but not at L4, OR the methodology component exists but is being refined.
- `[ ]` — not started.

## Shared infrastructure (PRIORITY — user directive 2026-05-27)

Components that underlie all five solver pipelines. **Raised above per-solver pipelines** per user directive: shared infrastructure is the leverage point — every per-solver pipeline depends on it. Krylov + smoothers + projections + FE assembly all gate per-solver coverage. The remaining unstarted shared-infrastructure items (MINRES, BiCGStab, Householder QR, Jacobi, SGS, ILU, AMS, multigrid V-cycle, curl-curl projector, FE assembly, boundary conditions) should be prioritised in cycle-planner dispatch selection over individual per-solver work.

**Per the unimplemented-Palace-components policy (user directive 2026-05-27, see CLAUDE.md §Scope):** Shared Infra items that are enum-only stubs in Palace (MINRES + BiCGStab confirmed cycle-004; possibly others — see priority #13 discovery item) are NOT direct implementation targets. They land as L1>L0 obstruction themes; their literature-anchored L1 forms may inform higher-form abstraction (L2 combinators like `krylov-step`); speculative operators are promoted only when small AND simplifying higher-form semantics. Status notation: items marked `[stub]` are enum-only-with-MFEM_ABORT (documented obstruction); items marked `[?stub]` haven't been grepped yet; items with normal `[ ]` are believed implemented in Palace.

## Per-solver pipelines (5 solvers)

A solver pipeline is *covered* when its driver algorithm has at least one slice at L4 AND all its support primitives are at least at L2. None of the five pipelines is fully covered yet — the Krylov-only footprint is shared across all five and is largely done, but per-pipeline FE assembly + boundary conditions + post-processing are not yet touched.

- [ ] **Electrostatic** — Poisson-like (∇·(ε∇φ) = ρ); SPD; uses CG + (eventually) geometric multigrid.
- [ ] **Magnetostatic** — curl-curl (∇×(μ⁻¹∇×A) = J); uses GMRES + (eventually) AMS.
- [ ] **Eigenmode** — generalized eigenvalue (∇×(μ⁻¹∇×E) = ω²εE); uses ARPACK/FEAST + shift-invert.
- [ ] **Driven** (frequency-domain) — Helmholtz with complex shifts; uses GMRES with complex arithmetic.
- [ ] **Transient** (time-domain) — ODE integrator over time stepping.

## Shared infrastructure — detail

Detail rows for the prioritised section above.

### Krylov solvers

- [x] **CG** — preconditioned conjugate gradient (cg slice at L4; v0.2 + preconditioned variant).
- [x] **GMRES / FGMRES** — restarted with `pc_side × gs_orthog × flexible` variants at L4 (gmres slice).
- [stub] **MINRES** — symmetric-indefinite three-term recurrence. Palace ships enum (`KspType::MINRES`) + JSON parser entry but routes to `MFEM_ABORT` at `palace/linalg/ksp.cpp:53-56`. L1>L0 obstruction theme landed cycle-004 (`book/src/L1-L0/minres-iteration.md`). NOT a direct implementation target per the unimplemented-stub policy; L1 form available as guidance for `krylov-step` at L2.
- [stub] **BiCGStab** — non-symmetric short-recurrence. Same enum-only-with-MFEM_ABORT pattern as MINRES. L1>L0 obstruction theme landed cycle-004 (`book/src/L1-L0/bicgstab-iteration.md`). NOT a direct implementation target.

### Orthogonalisation

- [x] **MGS / CGS / CGS2** — at L4 (orthog slice; residual-axis disclosure for L2 primitive-sequence divergence).
- [?stub] **Householder QR** — sibling slice; structurally-distinct variant per `book/src/concepts/variant-absorption.md`. Stub-status unverified — pre-grep `palace/utils/labels.hpp` + orthog selection points before harvester dispatch (per priority #13 enum-discovery sweep).

### Smoothers and preconditioners

- [x] **Chebyshev (1st-kind and 4th-kind)** — at L4 (chebyshev slice; constructed-operator variant absorption).
- [?stub] **Jacobi / damped Jacobi** — point-wise. Stub-status unverified — pre-grep before dispatch.
- [?stub] **Symmetric Gauss-Seidel** — element-wise; genuinely sequential at L3 (predicted obstruction). Stub-status unverified.
- [?stub] **ILU(0) / ILU(k)** — incomplete LU factorisations. Stub-status unverified.
- [ ] **AMS** (auxiliary-space Maxwell, Hiptmair-Xu) — Palace's multigrid-equivalent for curl-curl.
- [ ] **Geometric multigrid V-cycle** — driver + level-recurrence + restriction/prolongation.

### Projections and auxiliary operators

- [~] **Divergence-free projection** (divfree slice) — at L3, L4 in flight. (Status unchanged through meta-18; no L4 landing in cycles 80-85.)
- [ ] **Curl-curl projector** — predicted similar-pattern to divfree.

### FE assembly

- [ ] **Mesh + FE-space construction** — quadrature points, basis tables, geometric-factor computation.
- [ ] **Sparse-assembly patterns** — partial-assembly vs full-assembly vs matrix-free.
- [ ] **Operator composition** — sum/product/transpose of FE operators.
- [ ] **Boundary conditions** — essential (Dirichlet), natural (Neumann), periodic.

### Framework slices

(Added 2026-05-26 meta-22 after cg_preconditioning_framework appeared as an organically-extracted framework slice — different from algorithm or primitive slices.)

- [~] **CG Preconditioning Framework** — abstract preconditioner-as-LinOp interface used by CG and its variants. L0→L1 cycle 123; **L2→L3 cycle 141** (meta-24 — L1→L2 was attempted cycle 133 but tripped role-parametrized-factory renaming and was back-corrected). Likely first of a family of "framework slices" capturing the operator/preconditioner contracts that algorithm slices consume.

### Coordination and post-processing

- [ ] **Time-stepping** (transient): explicit/implicit integrators, step-size control.
- [ ] **Frequency sweep** (driven): adaptive parameter sweep, output collection.
- [ ] **Eigenpair extraction** (eigenmode): Arnoldi/Lanczos restart, residual selection.
- [ ] **Output / I/O** — VTK/ParaView field outputs, S-parameters, port modes.

## Intermediate-tier algorithms (added 2026-05-25 from user directive)

A tier of algorithmic primitives that sit BETWEEN leaf primitives (axpy, dot, apply_linop, …) and top-level driver algorithms (CG, GMRES, Chebyshev). Each intermediate is reused by multiple top-level algorithms and packages a meaningful chunk of shared concept vocabulary. Solving these gives **large bang-for-buck**: one intermediate slice unblocks several downstream slices and exercises cross-slice consistency on the concepts it uses.

**Targeting principle.** Per the user 2026-05-25 directive: the Planner should prioritize intermediate-tier slices over top-level roots when forward-frontier work is available. The loop's first pass picked roots (GMRES, CG, Chebyshev) and traced down to leaves; intermediates were filled retroactively. Going forward, intermediates that aren't yet extracted as standalone slices should be picked positively, ranked by **concept-overlap × downstream-slice-count**.

Candidates, roughly ordered by impact:

- [x] **Arnoldi step** (one inner-loop iteration of Krylov-subspace construction). Reused by: GMRES, FGMRES, MINRES (variant), eigenmode-via-Arnoldi. Concept overlap: `apply_linop`, `orthogonalize`, `dot`, `axpy`, `nrm2`, `scal`. **Landed at L4 via cycles 98–102 (meta-20 window) — first intermediate-tier algorithm extracted.** See `book/src/spec/slices/arnoldi_step.md`.
- [~] **Plane-rotation stream** (Givens-rotation accumulator + replay for least-squares update). Reused by: GMRES (Hessenberg LS update), eigenmode (QR algorithm), driven (complex Givens). Concept overlap: `givens` (generate + apply). L0→L1 cycle 108; L1→L2 cycle 124; **L2→L3 cycle 144** (meta-24). L4 pending.
- [~] **Polynomial-recurrence step** (degree-k Chebyshev / Richardson / Jacobi recurrence body). Reused by: Chebyshev 1st/4th-kind, Jacobi smoother, Richardson iteration. Concept overlap: `axpy`, `elementwise_product`, `scal`. **L0→L1 landed cycle 130** (meta-23 window via retroactive-gate retry); refined cycle 132.
- [~] **Sparse triangular solve** (TRSV variant). Reused by: ILU(0), ILU(k), AMS (smoother), Gauss-Seidel preconditioner, back-solve in direct solvers. Concept overlap: `trsv` (already a leaf concept; this is the *sweep* over a sparse triangular factor). **L0→L1 landed cycle 112** (meta-21 window) — emitted as a *negative result* per Palace not exposing sparse triangular sweep as a top-level primitive; lifting still unblocks future ILU/Gauss-Seidel/AMS work.
- [ ] **Diagonal-preconditioner apply** (extract diagonal + reciprocal + elementwise multiply). Reused by: Jacobi, Chebyshev (already uses it), block-Jacobi, polynomial preconditioners. Concept overlap: `extract_diagonal`, `reciprocal`, `elementwise_product`. Lifting consolidates the pattern across smoothers.
- [ ] **Residual update** (`r ← b - A·x` or accumulator form). Reused by: every iterative solver (CG, GMRES, MINRES, BiCGStab, Chebyshev, multigrid). Already implicit; making it a named intermediate clarifies the residual-management invariant across solvers.
- [ ] **Restart machinery** (state save / reset / re-initialize for restarted Krylov). Reused by: restarted GMRES, restarted Arnoldi, multigrid level-recurrence. Concept overlap: state-stratification, solve-monad. Currently embedded.

**Impact ranking heuristic** (used by Planner per `prompts/planner.md` forward-frontier criterion). For each candidate, score:

```
impact_score(slice) = |concepts(slice)|
                    × |slices_that_reuse(concepts(slice))|
                    × (1 / cycles_to_extract_estimate)
```

The intermediate-tier candidates above have impact scores estimated as: Arnoldi step ≫ Plane-rotation stream ≈ Polynomial-recurrence step > Sparse triangular solve > Diagonal-preconditioner apply > Residual update > Restart machinery.

The Planner uses this list (and the impact score) as input to the forward-frontier criterion (`prompts/planner.md`). Lifting any of these from "embedded in a root slice" to a standalone intermediate slice simultaneously:

1. Sharpens the root slice (clearer separation of concerns).
2. Unblocks downstream slices that reuse the intermediate.
3. Stresses concept vocabulary on cross-slice reuse (driving canonicalization).

## Methodology infrastructure

The agent loop itself. This is meta-development scope, not the spec deliverable.

### Roles

- [x] Planner, Explorer, Synthesizer, Critic (per-cycle).
- [x] Meta-Critic (meta-cycle driver).
- [x] README Builder (meta-cycle finaliser).

### Skills extracted

- [x] `classify-variant-axis` — variant-axis classification (4 absorption paths).
- [x] `verify-citation-range` — L0 citation cross-symbol-boundary check.
- [ ] *(more skills as recurring procedural patterns surface — meta-cycle proposes; user approves)*

### Concept library

- [x] 25 concepts on disk (cycle-005 added `scalar-promotion`), categorised in `book/src/concepts/index.md` (4 methodology incl. scalar-promotion, 4 algorithm, 10 primitive, 6 layer-pattern, 1 auxiliary), auto-maintained on every concept create. **Housekeeping cycle-006**: duplicate rows fixed by cycle-006 wave-1 same-layer-cross-cutter (`complex-from-real-lift` pure copy-paste deleted; `solver-as-operator` divergent-kind misclassification resolved by keeping `layer-pattern` row).
- [ ] Coverage gaps: complex-arithmetic primitives, FFT-based solves, time-stepping primitives, FE-assembly primitives.

### Integrator and orchestrator features

- [x] Channel set: file_creates, section_appends, file_edits, slice_index_updates, concept_writes (create/append-section), dependency_map_edges.
- [x] Verdict-downgrade with bookkeeping vs content classification.
- [x] Same-cycle create+edit merge.
- [x] Concept-existence loud-failure enforcement (meta-17).
- [x] Synthesizer streaming + max_tokens=24576.
- [ ] *(future)* Parallel-cycle integrator (BOOTSTRAP Phase 8).
- [ ] *(future)* Automated meta-cycle enactment (currently human-approved).

### Critic checks

- [x] 15 numbered checks. Stable through cycles 60+ with incremental additions per meta-review.

## Phase progression (per `BOOTSTRAP.md`)

- [x] **Phase 0** — workspace setup, `.env` plumbing, MCP registration.
- [x] **Phase 1** — Rust MCP codemap server (tree-sitter wrapper).
- [x] **Phase 2** — memory and schemas seed.
- [x] **Phase 3** — refinement plan + critic verdict schemas.
- [x] **Phase 4** — five agent prompts.
- [x] **Phase 5** — Python orchestrator (raw Anthropic SDK).
- [x] **Phase 6** — GMRES smoke test (DONE at meta-10).
- [~] **Phase 6+** — continuation: drive other slices toward L4, fill solver-pipeline coverage (currently here).
- [ ] **Phase 7** — execution grounding (build and run target; verify spec matches behaviour).
- [ ] **Phase 8** — parallel cycles (multiple Explorers, integration-plan queue).
- [ ] **Phase 9+** — UI, embedding store, alternative front-ends.

## How proportional coverage is computed

For the README's *Relative Progress* section:

- **Solver pipelines:** count of pipelines fully at L4 / total. Currently 0 / 5 (no full pipeline; Krylov-only footprint is shared).
- **Krylov solvers:** 2 / 4 at L4 (CG, GMRES; pending MINRES, BiCGStab).
- **Smoothers:** 1 / 6 at L4 (Chebyshev; pending Jacobi, SGS, ILU, AMS, multigrid).
- **Projections:** 0 / 2 at L4 (divfree at L3 in flight; curl-curl not started).
- **FE assembly:** 0 / 4 components.
- **Methodology infrastructure:** roles 3/3 done; skills extracted 2 / N (N grows on demand); 24 concepts on disk.
- **Phase progression:** 7 / 10+ phases done; Phase 6+ in flight.

The denominators are rough by design. The roadmap is reviewed and adjusted during each meta-cycle; if a category's denominator grows (new components surface as in-scope), the README's coverage report reflects it.

## Layered-spec progress (added cycle-002; updated cycle-011)

The 6-phase agent loop now builds the L4→L0 layered stack. Per-layer dep-map populations as of cycle-011 (second primary cycle of meta-batch-2; cycle-012 closes meta-batch-2):

- **L0** — **reference-note overlay bundle 1 landed cycle-005** (priority #10): 6 reference chapters (Conventions: `output-arg-vs-receiver`, `transparent-vs-load-bearing-tricks`, `mfem-vector-types`, `linalg-free-functions`; File overviews: `linalg-vector-file`, `ksp-factory-file`). **Bundle 2 landed cycle-006**: 2 new chapters (`apply-linop-overload-set`, `kspsolver-base-class`) plus new "Overload sets and class interfaces" L0 grouping. **Bundle 3 landed cycle-007**: 3 new chapters (`mfem-wrapper-solver`, `linalg-iterative-file`, `mutable-workspace-pattern`). **Bundle 4 landed cycle-008**: 3 new chapters (`eigensolver-wrapper` — Overload-sets-and-class-interfaces; `par-types-single-rank-reading` — Conventions; `linalg-operator-file` — File overviews). **Bundle 5 landed cycle-009** (2 chapters; third bundle-5 candidate `tests-as-semantic-supplement` deferred): `mpi-globalsum-and-collectives` + `preconditioner-classes-overview`. **Bundle 6 candidate #1 landed cycle-011**: `linalg-solver-file` (File overviews — `palace/linalg/solver.{hpp,cpp}`; `Solver<OperType>` type-axis-root chapter — corrects dispatch-prompt framing of "direct-solver-only base" with all eight concrete subclass families enumerated; closes cycle-009 OQ `l0-bundle-6-candidates` #1 to partially-answered). **17 chapters total** (well past initial ~13-chapter target; bundle-6 items #2 + #3 still open).
- **L1** — **8 firm operators** (`axpy` pilot-1, `dot` cycle-002, `nrm2` cycle-003, `axpby` cycle-003, `scal` cycle-004, `apply_linop` cycle-004, `axpbypcz` cycle-004, `ksp_solve` cycle-007 — **first L1 op with structured opaque primary argument**, introduces Constructed-operator absorption motif) + **3 rough-in (test-coverage-bounded / lower-layer-shared-vocabulary) operators** (`eigsolve` cycle-009 — **second constructed-operator gate at L1**, composing against `ksp_solve`; `matrix-weighted-norm` cycle-010 — L1 energy-norm primitive `α = ‖x‖_B = √(xᴴ B x)` for SPD `B`, priority #17 first target; `bilinear-form` cycle-010 — `bilinear_form(x, M, y) = xᴴ M y` for arbitrary linear `M`, priority #17 second target, first cycle-010 citation-validity FAIL repaired cleanly) + **6 rough-in obstruction operators** (`lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min` from `minres-iteration` theme; `bicgstab_step`, `omega_update`, `stabilisation_update` from `bicgstab-iteration` theme — **decision NOT to promote any landed cycle-005** per `scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md`). **Cycle-006 retroactive-thinned 4 L1 entries** (scalar-promotion sweep). **Cycle-007 retroactive-thinned all 7 pre-`ksp_solve` firm L1 entries** (~55% net Context shrink). **Cycle-008 L1/index refresh** added the closing-the-loop pointer at motif 4 + ksp_solve Status-cell L1>L0 link. **Cycle-009 L1/index refresh** added the new "Rough-in (test-coverage-bounded)" subsection (cohort-purity preserving — Firm bullet list unchanged) + eigsolve dep-map row + cycle-009 Working Notes bullet. **Cycle-010 L1 cohort growth** added matrix-weighted-norm + bilinear-form rough-in rows; cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` both halves landed (status `partially-answered`; SpectralNorm + L1>L0 themes residuals tracked). **L1 cohort frontmatter divergence noted cycle-010** — matrix-weighted-norm no frontmatter; bilinear-form 8-field frontmatter; future-normalization candidate for cycle-012 meta-phase batch.
- **L1>L0** lowering — **7 themes (5 firm/rough-in + 2 obstruction)**: `axpby-mutation-rotation` (cycle-002); `minres-iteration` (cycle-004, **obstruction**); `bicgstab-iteration` (cycle-004, **obstruction**); `apply-linop-mutation-rotation` (cycle-005, 5 sub-patterns A-E); `axpbypcz-mutation-rotation` (cycle-005, 4 sub-patterns + first mixed-justification sub-rule); **`ksp-solve-mutation-rotation` (cycle-008 wave-1 abstractor)** — first L1>L0 theme for a constructed-operator-absorption operator; 4 sub-patterns × {CG, GMRES, FGMRES} outer-loop variants. **`eigsolve-mutation-rotation` (cycle-011 wave-2 abstractor)** — second L1>L0 mutation-rotation theme for a structured opaque primary argument; 4-sub-pattern decomposition (A setup / B inner-solve mutation-rotation / C result-status flow / D teardown); exhaustively cites 10 `opInv->Mult` callsites across ARPACK (4) + NLEPS (1) + SLEPc shell (5); **first firm-structural-but-partly-constructive theme** in artifact (Sub-pattern B `LinearSolveFailed` materialisation partly-constructive pending upstream Palace refactor OR lowering-verifier audit). Mutation-rotation cohort 5 themes; obstruction cohort 2 themes.
- **`concepts/dot.md`** — rewritten cycle-004.
- **`concepts/scalar-promotion.md`** — landed cycle-005.
- **L2** — **1 firm operator** (`krylov-step`, cycle-005).
- **L3>L2** — **1 firm theme** (`krylov-step-body-identity`, cycle-007 abstractor at `firm-rough-in`; **promoted cycle-009 via status-inheritance** to plain `firm` after upstream L4>L3 theme firmed cycle-008 — first across-cycle status-inheritance promotion in the artifact; closes the cycle-007 firm-rough-in pattern's first instantiation).
- **L4** — **3 firm operators**: `krylov-step` (cycle-006), `iterate_while` (cycle-007), `iterate_while_with_prev` (cycle-007). **Cycle-008 L4/index refresh**: Semantics-overlay placeholder replaced with grounded 4-motif overlay; new `## Vocabulary cohort` subsection added (template adapted: middle slot uses L4>L3 cross-layer themes rather than rough-in same-layer operators, since L4 currently has no rough-in operators; cycle-009+ meta-phase consideration via OQ `vocabulary-cohort-middle-slot-cross-layer-adaptation`); dep-map widened 4→5 columns with new `Lowers to` column splitting cross-layer references out of `Dependencies`.
- **L4>L3** — **1 firm theme + 2 rough-in themes**: `krylov-step-typed-wrapper-dissolution` (cycle-006 wave-2 abstractor; **promoted cycle-008 wave-1 lifter** from rough-in → firm); `gmres-inner-loop-iterate-while-migration` (cycle-008 wave-2 abstractor, **rough-in** — pending upstream gmres.md §L4 v0.6→v0.7 self-rotation); **`fgmres-inner-loop-iterate-while-migration` (cycle-011 wave-2 lifter, **rough-in**) — first L4>L3 rough-in sister-theme in artifact; sibling to cycle-008 GMRES theme with FGMRES variant-axis collapses (`pc_side = RIGHT`, `flexible = true`) and textually-identical `:823-828` break-site finding; 6 applicability conditions (5 inherited from sibling + 1 FGMRES-specific); closes cycle-010 OQ `fgmres-inner-loop-iterate-while-migration-lifter-candidate`. **Cycle-011 firm-promotion of `check_stop_into_carry` remains deferred** per `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`; the cycle-010 lower-edge "second reuse" reading is preserved and reinforced by this dispatch.
- **L3** — **8 firm operators**: `krylov-step` (cycle-010 wave-1 harvester — first firm L3 operator in the artifact; identity-lowering backfill); **+7 BLAS-1 cohort entries cycle-011 wave-1**: `apply_linop` (pass 1; first primitive-flavored L3 backfill), `axpy` + `axpby` + `axpbypcz` (pass 2; linear-update cohort), `dot` + `nrm2` (pass 3; reduction cohort), `scal` (pass 4; closes cohort). **L3 firm-operator count: 1 → 8 cycle-011** — fully closes the BLAS-1 cohort portion of OQ `l3-backfill-apply-linop-and-blas1-cohort` (HIGH CONFIDENCE recommendations from cycle-010 cross-layer-cross-cutter audit); priority #20 second target fully met. L3 cohort frontmatter uniformly with-frontmatter at 8/8. Cumulative in-line identity-rotation count reaches 7 — exceeds cycle-010 OQ `l3-l1-directory-naming-structure-policy` revisit threshold of 6; strong candidate for cycle-012 meta-phase closure decision (codify in-line convention vs introduce `book/src/L3-L1/` directory). Cohort growth candidates beyond BLAS-1 remain routed via the `l3-vocabulary-inventory-gap` OQ (gemv, trsv, etc.).
- **L2>L1** — Part skeleton only.
- **Krylov-step lowering chain extended cycle-010**: L4 `krylov-step` (firm cycle-006) > L4>L3 `krylov-step-typed-wrapper-dissolution` (firm cycle-008) > L3 `krylov-step` (firm cycle-010) > L3>L2 `krylov-step-body-identity` (firm cycle-009) > L2 `krylov-step` (firm cycle-005) > L1 `ksp_solve` (firm cycle-007) > L1>L0 `ksp-solve-mutation-rotation` (firm cycle-008). **All 7 layer/lowering positions occupied explicitly**; first fully-firm cross-layer chain in the artifact extended with the cycle-010 L3 backfill closing the only gap.
- **Phase 1 slice corpus reduction batches landed cycles-010+011** — cycle-010 batch-1 (3 slices: gmres.md -42%; cg.md -67%; arnoldi_step.md -8%; net 842 lines removed). **Cycle-011 batch-2 (3 slices)**: orthog.md (L0→L1 Gram-Schmidt body replaced with reduced stub; plane-rotation-stream sub-slice deferred to batch-3 joint-audit), chebyshev.md (Consumers / Open-questions / Concept-references condensed; L1/L2/L3/L4 sections retained pending L1/chebyshev-smoother + L2/chebyshev-iteration firm-row promotion), polynomial_recurrence_step.md (**first negative-result slice audited** — verdict `blocked / minimal reduction; the slice IS the artifact`; methodologically distinct from batch-1 precursor-slice verdicts; 2 narrow forward-pointers added; load-bearing distinction catalog retained verbatim). **Cumulative slice-corpus coverage 6 of 10**; remaining 4 for batch-3+: divfree + cg_preconditioning_framework + plane_rotation_stream + sparse_triangular_solve. Audit template machine-replayable across both batches.

Forward indicator (post-cycle-011, second primary cycle of meta-batch-2): L1 vocabulary at **8 firm + 3 rough-in (test-coverage-bounded / lower-layer-shared-vocabulary) + 6 rough-in (obstruction)**. L2 has 1 firm. **L3 has 8 firm** (krylov-step from cycle-010 + 7 BLAS-1 entries from cycle-011 wave-1 — BLAS-1 cohort closed). **L3>L2 has 1 firm theme** (krylov-step-body-identity, promoted cycle-009 via status-inheritance). L4 has 3 firm. **L4>L3 has 1 firm + 2 rough-in** (+fgmres-inner-loop-iterate-while-migration cycle-011). L0 bootstrap at **17 chapters** (+linalg-solver-file cycle-011 wave-2; bundle-6 candidate #1). L1>L0 has **7 themes** (5 firm/rough-in + 2 obstruction) — +eigsolve-mutation-rotation cycle-011. **Phase 1 slice corpus reducing**: 6 of 10 slices reduced cumulative (cycle-010 batch-1 + cycle-011 batch-2); remaining 4 routed for batch-3+. **Cycle-011 incremental delta over cycle-010**: L3 firm operators **1 → 8** (+7 BLAS-1 cohort entries — first cohort-bundle harvester landings); L4>L3 themes **2 → 3** (+fgmres rough-in); L1>L0 themes **6 → 7** (+eigsolve-mutation-rotation firm structural / partly-constructive); L0 chapters **16 → 17** (+linalg-solver-file); slice corpus -3 slices reduced (orthog / chebyshev / polynomial_recurrence_step); net OQ ledger **4 resolutions + 1 partial-answer flip + 12 new opens + 7 status updates + 1 amendment** (net +8; cycle-011 emphasized OQ closure over OQ generation vs cycle-010). **Cycle-012+ candidates per cycle-011 integrator-signals**: close cycle-010 OQ `l3-l1-directory-naming-structure-policy` (count = 7 exceeds threshold; meta-phase decision); phase-1 corpus reduction batch-3 (4 remaining slices); `gmres.md §L4 v0.6→v0.7` self-rotation (large dispatch carry-forward); `L4/index.md:40` SUPERSEDED text drift (smallest-cost lifter); `l1-orthogonalize` harvester (gated on orthog slice now reduced); L2 cohort growth (priority #17 — no L2 entries cycle-011); L0 bundle-6 candidates #2 + #3; eigsolve-mutation-rotation lowering-verifier audit; `slepc-convergence-reason-lift-sub-theme` abstractor/lifter; `eigsolve-slepc-nep-coordinate-convention-audit` lifter / lowering-verifier / harvester-NEP. **MCP codemap usage stable** post-cycle-010 pilot SUCCESS — cycle-011 dispatches used MCP routinely with 0 permission-denied; friction-ledger entry `mcp-codemap-permission-denied-across-batch-1` remains resolution-candidate for cycle-012 meta-phase enactment. **Meta-phase batch-2 aggregation** fires after cycle-012 finalize.

## Working Notes

- Cycles 1–79 covered Krylov + orthogonalisation + smoothers (Chebyshev only so far) + one projection (divfree). FE assembly and time-stepping are the next major surfaces. Mesh construction and boundary conditions are also untouched.
- The methodology has stabilised through 17 meta-reviews; the per-solver pipeline buildup is now the dominant remaining work.
- If a roadmap item is genuinely out of scope (e.g., a methodology change rules it out), strike it through (`~~text~~`) with a meta-review note rather than deleting.
