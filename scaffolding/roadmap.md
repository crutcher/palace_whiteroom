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

## Per-solver pipelines (5 solvers)

A solver pipeline is *covered* when its driver algorithm has at least one slice at L4 AND all its support primitives are at least at L2. None of the five pipelines is fully covered yet — the Krylov-only footprint is shared across all five and is largely done, but per-pipeline FE assembly + boundary conditions + post-processing are not yet touched.

- [ ] **Electrostatic** — Poisson-like (∇·(ε∇φ) = ρ); SPD; uses CG + (eventually) geometric multigrid.
- [ ] **Magnetostatic** — curl-curl (∇×(μ⁻¹∇×A) = J); uses GMRES + (eventually) AMS.
- [ ] **Eigenmode** — generalized eigenvalue (∇×(μ⁻¹∇×E) = ω²εE); uses ARPACK/FEAST + shift-invert.
- [ ] **Driven** (frequency-domain) — Helmholtz with complex shifts; uses GMRES with complex arithmetic.
- [ ] **Transient** (time-domain) — ODE integrator over time stepping.

## Shared infrastructure

Components that underlie all five solver pipelines.

### Krylov solvers

- [x] **CG** — preconditioned conjugate gradient (cg slice at L4; v0.2 + preconditioned variant).
- [x] **GMRES / FGMRES** — restarted with `pc_side × gs_orthog × flexible` variants at L4 (gmres slice).
- [ ] **MINRES** — symmetric-indefinite three-term recurrence.
- [ ] **BiCGStab** — non-symmetric short-recurrence.

### Orthogonalisation

- [x] **MGS / CGS / CGS2** — at L4 (orthog slice; residual-axis disclosure for L2 primitive-sequence divergence).
- [ ] **Householder QR** — sibling slice; structurally-distinct variant per `book/src/concepts/variant-absorption.md`.

### Smoothers and preconditioners

- [x] **Chebyshev (1st-kind and 4th-kind)** — at L4 (chebyshev slice; constructed-operator variant absorption).
- [ ] **Jacobi / damped Jacobi** — point-wise.
- [ ] **Symmetric Gauss-Seidel** — element-wise; genuinely sequential at L3 (predicted obstruction).
- [ ] **ILU(0) / ILU(k)** — incomplete LU factorisations.
- [ ] **AMS** (auxiliary-space Maxwell, Hiptmair-Xu) — Palace's multigrid-equivalent for curl-curl.
- [ ] **Geometric multigrid V-cycle** — driver + level-recurrence + restriction/prolongation.

### Projections and auxiliary operators

- [~] **Divergence-free projection** (divfree slice) — at L3, L4 in flight.
- [ ] **Curl-curl projector** — predicted similar-pattern to divfree.

### FE assembly

- [ ] **Mesh + FE-space construction** — quadrature points, basis tables, geometric-factor computation.
- [ ] **Sparse-assembly patterns** — partial-assembly vs full-assembly vs matrix-free.
- [ ] **Operator composition** — sum/product/transpose of FE operators.
- [ ] **Boundary conditions** — essential (Dirichlet), natural (Neumann), periodic.

### Coordination and post-processing

- [ ] **Time-stepping** (transient): explicit/implicit integrators, step-size control.
- [ ] **Frequency sweep** (driven): adaptive parameter sweep, output collection.
- [ ] **Eigenpair extraction** (eigenmode): Arnoldi/Lanczos restart, residual selection.
- [ ] **Output / I/O** — VTK/ParaView field outputs, S-parameters, port modes.

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

- [x] 24 concepts on disk, categorised in `book/src/concepts/index.md` (3 methodology, 4 algorithm, 10 primitive, 6 layer-pattern, 1 auxiliary), auto-maintained on every concept create.
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

## Working Notes

- Cycles 1–79 covered Krylov + orthogonalisation + smoothers (Chebyshev only so far) + one projection (divfree). FE assembly and time-stepping are the next major surfaces. Mesh construction and boundary conditions are also untouched.
- The methodology has stabilised through 17 meta-reviews; the per-solver pipeline buildup is now the dominant remaining work.
- If a roadmap item is genuinely out of scope (e.g., a methodology change rules it out), strike it through (`~~text~~`) with a meta-review note rather than deleting.
