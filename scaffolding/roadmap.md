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

## Layered-spec progress (added cycle-002; updated cycle-009)

The 6-phase agent loop now builds the L4→L0 layered stack. Per-layer dep-map populations as of cycle-009 (closes meta-batch-1):

- **L0** — **reference-note overlay bundle 1 landed cycle-005** (priority #10): 6 reference chapters (Conventions: `output-arg-vs-receiver`, `transparent-vs-load-bearing-tricks`, `mfem-vector-types`, `linalg-free-functions`; File overviews: `linalg-vector-file`, `ksp-factory-file`). **Bundle 2 landed cycle-006**: 2 new chapters (`apply-linop-overload-set`, `kspsolver-base-class`) plus new "Overload sets and class interfaces" L0 grouping. **Bundle 3 landed cycle-007**: 3 new chapters (`mfem-wrapper-solver`, `linalg-iterative-file`, `mutable-workspace-pattern`). **Bundle 4 landed cycle-008**: 3 new chapters (`eigensolver-wrapper` — Overload-sets-and-class-interfaces; `par-types-single-rank-reading` — Conventions; `linalg-operator-file` — File overviews). **Bundle 5 landed cycle-009** (2 chapters; third bundle-5 candidate `tests-as-semantic-supplement` deferred via cycle-009 OQ `tests-as-semantic-supplement-l0-vs-concepts-decision`): `mpi-globalsum-and-collectives` (File overviews — `palace/utils/communication.hpp`, the home of the `palace::mpi::DataType<T>` family + the `palace::Mpi` collective wrappers); `preconditioner-classes-overview` (Overload-sets-and-class-interfaces — 7-class survey across `palace/linalg/{amg,ams,jacobi,chebyshev,distrelaxation,gmg,blockprecond}.{hpp,cpp}`; three-group split: Hypre-wrapped algebraic / native `Solver<OperType>` smoothers / composition preconditioners; L0 anchor for future `L1/apply_preconditioner` and L2 V-cycle algebra work). **16 chapters total** (well past initial ~13-chapter target; bundle 6 candidates surfaced — see cycle-009 OQ `l0-bundle-6-candidates`).
- **L1** — **8 firm operators** (`axpy` pilot-1, `dot` cycle-002, `nrm2` cycle-003, `axpby` cycle-003, `scal` cycle-004, `apply_linop` cycle-004, `axpbypcz` cycle-004, `ksp_solve` cycle-007 — **first L1 op with structured opaque primary argument**, introduces Constructed-operator absorption motif) + **1 rough-in (test-coverage-bounded) operator landed cycle-009** (`eigsolve` — **second constructed-operator gate at L1**, composing against `ksp_solve` for spectral-transformation inverse application; first multi-level constructed-operator composition in the L1 vocabulary; introduces partial-convergence `PartialConverged` status as a distinguishing feature relative to `ksp_solve`'s soft-fail; promotion to firm gated on expanded test coverage or additional literature anchoring per cycle-009 OQ `eigsolve-l1-operator-rough-in-candidate` partial-closure) + **6 rough-in obstruction operators** (`lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min` from `minres-iteration` theme; `bicgstab_step`, `omega_update`, `stabilisation_update` from `bicgstab-iteration` theme — **decision NOT to promote any landed cycle-005** per `scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md`). **Cycle-006 retroactive-thinned 4 L1 entries** (scalar-promotion sweep). **Cycle-007 retroactive-thinned all 7 pre-`ksp_solve` firm L1 entries** (~55% net Context shrink). **Cycle-008 L1/index refresh** added the closing-the-loop pointer at motif 4 + ksp_solve Status-cell L1>L0 link. **Cycle-009 L1/index refresh** added the new "Rough-in (test-coverage-bounded)" subsection (cohort-purity preserving — Firm bullet list unchanged) + eigsolve dep-map row + cycle-009 Working Notes bullet.
- **L1>L0** lowering — **6 themes**: `axpby-mutation-rotation` (cycle-002); `minres-iteration` (cycle-004, **obstruction**); `bicgstab-iteration` (cycle-004, **obstruction**); `apply-linop-mutation-rotation` (cycle-005, 5 sub-patterns A-E); `axpbypcz-mutation-rotation` (cycle-005, 4 sub-patterns + first mixed-justification sub-rule); **`ksp-solve-mutation-rotation` (cycle-008 wave-1 abstractor)** — first L1>L0 theme for a constructed-operator-absorption operator; 4 sub-patterns (A workspace allocation, B initial-guess threading, C statistics-counter mutation, D convergence-warning logging) × {CG, GMRES, FGMRES} outer-loop variants. Mutation-rotation cohort 4 themes; obstruction cohort 2 themes.
- **`concepts/dot.md`** — rewritten cycle-004.
- **`concepts/scalar-promotion.md`** — landed cycle-005.
- **L2** — **1 firm operator** (`krylov-step`, cycle-005).
- **L3>L2** — **1 firm theme** (`krylov-step-body-identity`, cycle-007 abstractor at `firm-rough-in`; **promoted cycle-009 via status-inheritance** to plain `firm` after upstream L4>L3 theme firmed cycle-008 — first across-cycle status-inheritance promotion in the artifact; closes the cycle-007 firm-rough-in pattern's first instantiation).
- **L4** — **3 firm operators**: `krylov-step` (cycle-006), `iterate_while` (cycle-007), `iterate_while_with_prev` (cycle-007). **Cycle-008 L4/index refresh**: Semantics-overlay placeholder replaced with grounded 4-motif overlay; new `## Vocabulary cohort` subsection added (template adapted: middle slot uses L4>L3 cross-layer themes rather than rough-in same-layer operators, since L4 currently has no rough-in operators; cycle-009+ meta-phase consideration via OQ `vocabulary-cohort-middle-slot-cross-layer-adaptation`); dep-map widened 4→5 columns with new `Lowers to` column splitting cross-layer references out of `Dependencies`.
- **L4>L3** — **1 firm theme + 1 rough-in theme**: `krylov-step-typed-wrapper-dissolution` (cycle-006 wave-2 abstractor; **promoted cycle-008 wave-1 lifter** from rough-in → firm with two-form pruned/unpruned sketch + Condition 5 + L3-side Law-1 image reduction rule + 10-citation `verified_against:` YAML block); `gmres-inner-loop-iterate-while-migration` (cycle-008 wave-2 abstractor, **rough-in** — pending upstream gmres.md §L4 v0.6→v0.7 self-rotation; documents migrated L4 form + L3 form + 4-axis variant pass-through; speculative `check_stop_into_carry` L4 helper surveyed cycle-009 combinator-miner with **verdict defer** per "second slice needs it" promotion criterion — NLEPS is the natural second consumer but is not yet spec'd at L1+, blocking promotion per cycle-009 OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`).
- **L2>L1**, **L3** — Part skeletons only.
- **Krylov-step lowering chain fully firm post-cycle-009**: L4 `krylov-step` (firm cycle-006) > L4>L3 `krylov-step-typed-wrapper-dissolution` (firm cycle-008) > L3 (rendered in the L4>L3 theme) > L3>L2 `krylov-step-body-identity` (firm cycle-009) > L2 `krylov-step` (firm cycle-005). First fully-firm cross-layer chain in the artifact. Significant structural milestone closing meta-batch-1.

Forward indicator (post-cycle-009, meta-batch-1 close): L1 vocabulary at **8 firm + 1 rough-in (test-coverage-bounded) + 6 rough-in (obstruction)**. L2 has 1 firm. **L3>L2 has 1 firm theme** (promoted cycle-009 via status-inheritance, completing the krylov-step lowering chain). L4 has 3 firm. **L4>L3 has 1 firm + 1 rough-in**. L0 bootstrap at **16 chapters** (bundle 5 landed cycle-009 with 2 chapters). L1>L0 has **6 themes** unchanged. **Meta-batch-1 (cycles 007/008/009) summary**: L0 chapters **8 → 16** (doubled the reference layer); L4 firm operators **1 → 3**; L4>L3 themes **0 → 1 firm + 1 rough-in**; L3>L2 themes **0 → 1 firm** (full krylov-step chain); L1 firm operators **7 → 8 + 1 rough-in**; L1>L0 themes **5 → 6**; net OQ ledger **6 closures + 16 new opens across batch** (net +10 — mostly from cycle-009's combinator-miner survey + eigsolve rough-in's 4 partial-closure follow-ups). **Cycle-010+ candidates**: `eigsolve` firm-promotion follow-ups (4 cycle-009 OQs: `eigsolve-linear-solve-failed-status-anchor`, `eigsolve-scaling-coordinate-convention`, `eigsolve-initial-space-axis-placement`, `eigsolve-iteration-count-result-field`); L0 bundle 6 (cycle-009 OQ `l0-bundle-6-candidates`); NLEPS L1 spec gap (cycle-009 OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`); matrix-weighted-norm + bilinear-form L1 rough-ins (deferred from cycle-009 planner per capacity, cycle-008 OQ); `gmres.md §L4 v0.6 → v0.7` self-rotation (firms cycle-008's rough-in L4>L3 theme); MCP codemap rollout decision per cycle-009 meta-phase. **Meta-phase batch-1 aggregation** fires after this cycle-009 finalize commit lands.

## Working Notes

- Cycles 1–79 covered Krylov + orthogonalisation + smoothers (Chebyshev only so far) + one projection (divfree). FE assembly and time-stepping are the next major surfaces. Mesh construction and boundary conditions are also untouched.
- The methodology has stabilised through 17 meta-reviews; the per-solver pipeline buildup is now the dominant remaining work.
- If a roadmap item is genuinely out of scope (e.g., a methodology change rules it out), strike it through (`~~text~~`) with a meta-review note rather than deleting.
