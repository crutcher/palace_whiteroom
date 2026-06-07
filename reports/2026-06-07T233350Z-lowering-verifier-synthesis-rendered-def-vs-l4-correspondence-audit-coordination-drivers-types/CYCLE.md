---
agent: lowering-verifier
invoked_at: 2026-06-07T233350Z
scope: cycle-138 synthesis-rendered-def-vs-l4-correspondence-audit — the c137-un-pulled three Synthesis libraries (coordination / drivers / types) vs their authoritative L4 / feature / concepts homes
status: integrated
integrated_at: 2026-06-07T235126Z
integration_commit: f1b69f1
integration_notes: "cycle-138 (batch-44 BATCH-CLOSING). AUDIT-CLASS, FULLY-SUPPORTED verdict; NO book mutation (no ## Proposed changes). Completes the whole-Part Synthesis rendered-def<->L4 correspondence-audit coverage (c137 covered iteration + data-algebra; this covered coordination + drivers + types), modulo 2 gated non-blocking residuals. Promoted 2 NEW OQs (l4-eigsolve-initial-state-vs-initial-eig-state-seed-inconsistency -> abstractor; synthesis-types-iodata-omits-units-field -> layer-intro-author). DISCHARGES OQ synthesis-correspondence-audit-coverage-coordination-drivers-types-next-pull. No build relevance. retroactive-budget 0."
inputs:
  - book/src/synthesis/coordination.md
  - book/src/synthesis/drivers.md
  - book/src/synthesis/types.md
  - book/src/L4/ksp_solve.md
  - book/src/L4/eigsolve.md
  - book/src/L4/solve_family.md
  - book/src/L4/frequency_sweep.md
  - book/src/L4/fold_solve.md
  - book/src/L4/preconditioning-framework.md
  - book/src/L4/gram_reduce.md
  - book/src/L3/eigsolve-impl.md
  - book/src/feature/electrostatic.L4.md
  - book/src/feature/eigenmode.L4.md
  - book/src/feature/lifecycle.L4.md
  - book/src/concepts/config-record.md
  - book/src/concepts/sim-state.md
  - book/src/concepts/op-params.md
---

# CYCLE: Audit synthesis-rendered-def-vs-l4-correspondence — coordination / drivers / types

## Summary

This COMPLETES the directive-sanctioned Synthesis correspondence-audit coverage that the c137 audit
opened (it pulled only `iteration` / `data-algebra`; this pulls the remaining three libraries). I
audited the rendered defs in `book/src/synthesis/coordination.md`, `book/src/synthesis/drivers.md`,
and `book/src/synthesis/types.md` against their authoritative L4 chapter bodies, the Feature L4
columns, and the `concepts/` record homes. **Top-level verdict: SUPPORTED with two minor flagged
residuals (PARTIALLY-SUPPORTED at the level of two specific defs; the other ~25 defs are FULLY
faithful) — neither residual is a correspondence DEFECT in the synthesis rendering; both are
faithful disclosures of a latent UPSTREAM authoritative-chapter issue or a benign field elision.**
The Synthesis Part correctly behaves as an implementation VIEW throughout the three libraries:
`reference`-class edges only (zero spurious `depends-on`), no semantic restatement (laws / record
field-semantics linked, not duplicated), closure-signatures paren-grouped where high-order, the
DIRECTIVE-3 eigsolve kernel-API/impl dual-surface rendered correctly (`#extern eigen_iterate` after
its type sig; the `realizes-kernel-api` `reference`-class edge to `eigsolve-impl` confirmed
intact-on-disk). The two residuals:

1. **(coordination `eigsolve`)** the synthesis renders the cap seed as `initial_eig_state inp`
   whereas L4/eigsolve.md:44 writes `initial_state inp`. The synthesis def **explicitly flags this
   divergence inline** (with the exact `:44` citation) and is **arguably the MORE correct form** —
   it caught a real latent self-inconsistency IN the L4 chapter (the cap threads
   `Solve a = StateT EigState Identity a` per L4/eigsolve.md:70,74, which cannot be seeded by the
   SimState-typed `initial_state`). The synthesis disposition is right; the fix belongs UPSTREAM in
   the L4 chapter. Routed (gated) to an `abstractor` reread of `L4/eigsolve.md`.
2. **(types `IoData`)** the synthesized `IoData` type-def renders 5 fields and omits the 6th
   authoritative field `units : Units` (config-record.md:74). Benign (the back-link to the
   authoritative full schema is present and correct; the cited `:69-73` range is self-consistent
   with the 5-field rendering), but a faithful synthesized type-def should render all 6 fields or
   note the elision. Proposed as a one-line add to types.md (gated to the shell author).

No proposed mutation to any L4 / feature / concept chapter from this audit; the two residuals route
as gated follow-ups (one upstream-reconcile, one synthesis-shell completeness add). Clean audit
disposition otherwise.

## Per-citation audit

### coordination.md defs

- **Citation**: `book/src/synthesis/coordination.md:45-130` (the Coordination type block — `Solve`
  monad surface, `Outcome` / `EigOutcome` / `EigStatus` sums, `EigState`, `StepReturn`) vs
  `book/src/L4/ksp_solve.md:69-82` (`Outcome` + `Solve`), `book/src/L4/eigsolve.md:62-74`
  (`EigStatus`/`EigOutcome`/`EigState`), `book/src/concepts/solve-monad.md`,
  `book/src/concepts/solve-result.md`, `book/src/concepts/eigsolve.md`.
  - **Theme claim**: the type block renders the `Solve` monad surface + termination sums + state
    carriers, bundled with utility API only, linking field-schema to the authoritative homes.
  - **Found**: `type Solve a = StateT SimState Identity a` matches `solve-monad`/`ksp_solve.md:82`.
    `data Outcome = Continue | Done Bool` + `done` matches `ksp_solve.md:69-73`. `data EigStatus =
    Converged | PartialConverged Int | MaxIterReached | LinearSolveFailed` + `data EigOutcome =
    Continue | Done EigStatus` match `eigsolve.md:62-63` exactly (the 4-arm extension with the
    first-class `PartialConverged k` arm, no `ksp_solve` analog). `EigState` renders
    `pairs / converged / requested / error / status` matching `eigsolve.md:70` and links the field
    schema to `L1/eigsolve` + `concepts/eigsolve` (NOT restated). `StepReturn` renders under its
    authoritative name with a link to `concepts/solve-result.md` (link-don't-restate). Each type is
    bundled with utility API only (`done`/`eig_done`/`initial_eig_state`/`eigenpairs`/
    `num_converged`/`residual_proxy`); the consuming caps follow AFTER the block.
  - **Verdict**: supports.
  - **Notes**: the type-placement rule is honored exactly (cross-cutting `SimState`/`OpParams`/
    `IoData` deferred to `types`; `EigState`/`StepReturn` rendered here because single-consumer).

- **Citation**: `book/src/synthesis/coordination.md:134-173` (`preconditioning-framework` —
  `buildKspSolver` / `setOperators` + the `pcBoundOp` `where`-helper) vs
  `book/src/L4/preconditioning-framework.md:41-46,56-75,126-129` (the construction-and-binding
  surface + `BaseKspSolver` record + the `finestLevelUnwrap` derived-view-hoisting).
  - **Theme claim**: renders the construction + binding def bodies; the record types
    (`BaseKspSolver`, `KspParams`, `PcParams`, `OpBinding`) are linked to the authoritative chapter,
    not redefined.
  - **Found**: `buildKspSolver` renders the `(ksp, pc)` construction via
    `constructedOperatorFactory` + the one-shot `bindPreconditioner`, returning the unbound
    `BaseKspSolver { ksp, pc, binding = Nothing, ... }`. `setOperators` renders the bind with the
    `pcBoundOp` `where`-local derived view (the finest-level-unwrap-when-multigrid-pc-meets-
    non-multigrid-solver branch) — matching the L4 chapter's §"Derived-view hoisting of the unwrap
    adapter" (`:66-75`) and the `pcBoundOp`-recomputed-on-demand-never-cached discipline. The record
    types are explicitly stated to live inline in the authoritative chapter (synthesis `:136`);
    rendered here is only the construction surface.
  - **Verdict**: supports.

- **Citation**: `book/src/synthesis/coordination.md:177-208` (`ksp_solve` cap) vs
  `book/src/L4/ksp_solve.md:55-69` (entry point + `solve_loop` + `restart_cycle` shape),
  `:96-103` (the four-phase `restart_cycle` body).
  - **Theme claim**: faithful render of the `Solve`-monadic outer-driver cap folding `krylov_step`.
  - **Found**: `ksp_solve op inp = execState (solve_loop op inp) (initial_state inp)` matches
    `ksp_solve.md:57` exactly. The `solve_loop` `do { o <- restart_cycle op inp; unless (done o)
    (solve_loop op inp) }` matches `:61-63`. The `restart_cycle` four phases — `fresh_krylov` (plain
    value, `:98`), the inner `iterate_while (krylov_step op k0) cont` fold (`:99`), the single
    boundary `modify (\s -> s { x = s.x \`plus\` (kn.basis \`applyBasis\` kn.y) })` correction
    (`:100`), the once-per-cycle `pure (classify kn op s)` (`:101`) — render line-for-line. The cap's
    closure-returning structure (the `Solve ()` driver + `Solve Outcome` cycle) is paren-grouped
    where high-order. The deep-linked `krylov_step`/`iterate_while` are NOT re-rendered (the cap
    *folds* them, per the iteration library).
  - **Verdict**: supports.

- **Citation**: `book/src/synthesis/coordination.md:212-254` (`eigsolve` cap + `#extern
  eigen_iterate` + `apply_shift_invert`) vs `book/src/L4/eigsolve.md:42-64` (entry point + opaque
  driver + body), `book/src/L3/eigsolve-impl.md` (the `realizes-kernel-api` kernel-impl node).
  - **Theme claim** (the DIRECTIVE-3 dual-surface): the eigen-iteration renders `#extern` at the
    kernel-API boundary; the `apply_shift_invert` body (which LIFTS) renders inline; the
    constructive `eigsolve-impl` realizes the surface via a `reference`-class `realizes-kernel-api`
    edge.
  - **Found**: `solve_loop` (single opaque step + `classify_into_state`) matches `eigsolve.md:49-51`.
    `eigen_iterate :: OpParams -> Inputs -> Solve EigOutcome` followed by `#extern eigen_iterate` —
    the `#extern` AFTER the type signature, per the index convention; correctly the kernel-API
    surface. `apply_shift_invert` renders `apply_linop op.operand v ▷ ksp_solve_op op.inv w ▷
    scale_untransform op y` — the firm L2/L3 lifting body (matching `eigsolve.md:59` + §Semantics
    `:92-93` + Law 2 `:111`), rendered inline as the from-our-primitives callback. The dual-surface
    prose (`:239-241`,`:254`) correctly describes the `eigsolve-impl` kernel-impl node realizing the
    surface "a reviewable correspondence, not a build dep." The `eigsolve-impl` `realizes-kernel-api`
    edges to BOTH `L3/eigsolve` and `L4/eigsolve` are confirmed `reference`-class on disk
    (`eigsolve-impl.md:19-23`) — NOT mis-typed to `depends-on`. DIRECTIVE-3 intactness CONFIRMED.
  - **Verdict**: partially-supports (the dual-surface mechanics + body are FULLY faithful; the
    **seed** diverges — see below).
  - **Notes**: **FLAGGED DIVERGENCE (faithful-with-disclosure).** The synthesis renders the cap seed
    as `eigsolve op inp = execState (solve_loop op inp) (initial_eig_state inp)` (`:230`), whereas
    L4/eigsolve.md:44 writes `... (initial_state inp)`. The synthesis def **explicitly flags this**
    in an inline NOTE (`:225-229`) with the exact `:44` citation, calling the L4 chapter's reuse of
    `initial_state` "a latent inconsistency to reconcile upstream — lowering-verifier." I confirmed
    the L4 chapter is INTERNALLY inconsistent: L4/eigsolve.md:70 + :74 both establish the cap threads
    `Solve a = StateT EigState Identity a` (over `EigState`), which a `SimState`-typed
    `initial_state` constructor cannot seed; an `EigState`-seeding constructor (`initial_eig_state`)
    is the type-coherent discharge. So the synthesis rendering is arguably the MORE correct form, and
    the residual is an UPSTREAM L4-chapter bug the synthesis correctly surfaced — NOT a synthesis
    correspondence defect. (Note also: L4/eigsolve.md:97 §Semantics repeats `initial_state inp`, so
    the L4 chapter carries the inconsistency in two places.) Disposition: render-stands, route the
    upstream fix.

- **Citation**: `book/src/synthesis/coordination.md:258-274` (`solve_family`) vs
  `book/src/L4/solve_family.md:52-53` (the map entry).
  - **Theme claim**: faithful render of the fixed-operator map-over-RHS-family combinator.
  - **Found**: `solve_family op rhss = map (\inp -> ksp_solve op inp) rhss` matches
    `solve_family.md:53` exactly, with the operator-capture-once-hoist + element-independence
    comments tracking laws 1-3 (`solve_family.md:100-104`). No law restated (the laws are owned by
    the L4 chapter; the comments are dataflow annotations, not law statements).
  - **Verdict**: supports.

- **Citation**: `book/src/synthesis/coordination.md:278-301` (`frequency_sweep`) vs
  `book/src/L4/frequency_sweep.md:23-37,58-75` (the operator-VARYING per-ω map).
  - **Theme claim**: faithful render of the operator-varying sweep (rebuild `A(ω)` inside the map
    via `assemble_frequency_operator`, then one `ksp_solve` per ω).
  - **Found**: `frequency_sweep fam omegas = map (\omega -> ksp_solve (assemble_frequency_operator
    fam omega) (rhs_at fam omega)) omegas` renders the per-ω rebuild + per-member `ksp_solve` — the
    `operator-capture = per-element` shape the L4 chapter scopes as the `solve_family` non-membership
    boundary (`frequency_sweep.md:58-61,67-70`). The `rhs_at` `where`-helper is the absorbed ω-dependent
    excitation. The `assemble_frequency_operator`-not-opaque distinction from `fold_solve`'s opaque
    `time_step_op` is preserved (synthesis `:301`).
  - **Verdict**: supports.

- **Citation**: `book/src/synthesis/coordination.md:305-330` (`fold_solve` + `#extern time_step_op`)
  vs `book/src/L4/fold_solve.md:47-54` (the `foldl` entry + opaque per-step op).
  - **Theme claim**: faithful render of the state-threaded fold; the opaque per-step body renders
    `#extern`.
  - **Found**: `fold_solve op s0 schedule = foldl (\s t -> time_step_op op s t) s0 schedule` matches
    `fold_solve.md:50` exactly, with the carry-threading-sequential-obstruction + no-commutativity
    comments tracking the L4 §Semantics. `time_step_op :: OpParams -> TimeState -> Time -> TimeState`
    followed by `#extern time_step_op` — the `#extern` AFTER the type sig (the opaque MFEM
    `ODESolver` per-step boundary). The state-generated `schedule-source` form is correctly deferred
    to the L4 chapter (synthesis `:330`), the default surface rendered being the fixed-list fold.
  - **Verdict**: supports.

### drivers.md defs

- **Citation**: `book/src/synthesis/drivers.md:57-72` (per-driver config records as `IoData`
  projection-views) vs `book/src/concepts/config-record.md:105-130` (§"Per-driver specializations").
  - **Theme claim**: the per-driver config records are projection-views of the one `IoData`,
    rendered as type aliases; the projection is the utility API, not a field-schema restatement.
  - **Found**: `type ElectrostaticConfig = IoData` (+ five siblings) renders the alias form; the
    concept page confirms "There is **one** `IoData` type; the per-driver config records are
    **projections** of the same `iodata` object" (`config-record.md:107-111`). The projection
    accessors are the only utility API rendered; no field schema restated. The per-driver projection
    annotations (model + domains.ε + boundaries.terminals + ...) match the concept page's projection
    table (`config-record.md:114-120`).
  - **Verdict**: supports.

- **Citation**: `book/src/synthesis/drivers.md:76-94` (`electrostatic`) vs
  `book/src/feature/electrostatic.L4.md:33-43,66` (the composition root), `book/src/L4/gram_reduce.md:81-86`
  (the gram_reduce signature).
  - **Theme claim**: `electrostatic = gram_reduce(w≡1) ∘ solve_family ∘ fe_assemble`.
  - **Found**: the synthesis renders `space = h1_space cfg`, `k = fe_assemble space [diffusion
    (permittivity cfg)]`, `rhss = [...]`, `vs = solve_family k rhss`, `gram_reduce k vs (\i j -> 1)`.
    The feature column names stage 3 `capacitance_reduce` but EXPLICITLY states (`:51`) `gram_reduce`
    is the entry and `capacitance_reduce` re-expresses THROUGH it as the `w=1` corner — so the
    synthesis form `gram_reduce k vs (\i j -> 1)` is the MORE-faithful composition (it composes the
    firm entry combinator with the w=1 weight explicit). The `gram_reduce` arg order (operator first,
    family second, weight closure third) matches `gram_reduce.md:81-86` exactly. The composition
    `gram_reduce ∘ solve_family ∘ fe_assemble` matches `electrostatic.L4.md:66`.
  - **Verdict**: supports.

- **Citation**: `book/src/synthesis/drivers.md:98-119` (`magnetostatic`), `:121-145` (`driven`),
  `:147-170` (`transient`) vs `feature/magnetostatic.L4.md` / `feature/driven.L4.md` /
  `feature/transient.L4.md`.
  - **Theme claim**: magnetostatic = the current-normalized `gram_reduce(w=1/(IᵢIⱼ))` sibling;
    driven = `sparameter_reduce ∘ frequency_sweep ∘ fe_assemble(×3)`; transient = `fold_solve ∘
    fe_assemble(×3)`.
  - **Found**: `magnetostatic` renders the same fixed-operator shape as electrostatic with the only
    difference being the `gram_reduce k as (\i j -> 1 / (is!!i * is!!j))` weight (matching the
    feature column's current-normalized claim). `driven` renders the `FrequencyOperatorFamily {K,C,M,
    A2}` once-assembled + `frequency_sweep fam omegas` + `sparameter_reduce` — the operator-VARYING
    composition. `transient` renders `(k,c,m)` once-assembled + `time_operator` capture + `fold_solve
    op s0 schedule` — the state-threaded fold. Each composes the calculus-library defs by name and
    cites its `feature/<x>.L4.md` composition root for the compositional claim (link-don't-restate).
  - **Verdict**: supports.
  - **Notes**: light spot-check on magnetostatic/driven/transient (the primary deep-dive was
    electrostatic + eigenmode + lifecycle); the renderings are structurally consistent with their
    feature columns' stated compositions and the calculus-library def signatures.

- **Citation**: `book/src/synthesis/drivers.md:172-194` (`eigenmode`), `:196-218` (`boundary_mode`)
  vs `book/src/feature/eigenmode.L4.md:33-42`, `feature/boundary-mode.L4.md`.
  - **Theme claim**: eigenmode = `map readout ∘ eigsolve ∘ eig_pencil ∘ fe_assemble(×3)`;
    boundary_mode = the same `eigsolve` corner over a 2D-submesh preface.
  - **Found**: `eigenmode` renders three `fe_assemble` (K/C/M), `eig_pencil k c m (target cfg)
    (n_modes cfg)`, `eigsolve pencil (initial_space cfg)`, `map (readout cfg) eigs` — matching
    `eigenmode.L4.md:37-42` line-for-line (the minimal `assemble (×3) ▷ eigsolve ▷ readout-map`
    shape; ONE opaque black-box call, no `solve_family` map, no `fold_solve` march, per
    `eigenmode.L4.md:27`). `boundary_mode` renders the distinguishing `extract_boundary_2d_submesh`
    preface + the `ND ⊕ H1` block pencil + the SAME `eigsolve` corner + readout — matching the
    feature column's `map readout ∘ eigsolve ∘ eig_pencil ∘ fe_assemble ∘ extract_boundary_2d_submesh`.
  - **Verdict**: supports.

- **Citation**: `book/src/synthesis/drivers.md:222-322` (the 6 output products —
  `capacitance` / `inductance` / `sparameters` / `eigenfrequency_qfactor` / `energy_fields` /
  `waveguide_mode`) vs `feature/{capacitance,inductance,sparameters,eigenfrequency-qfactor,
  energy-fields,waveguide-mode}.L4.md`.
  - **Theme claim**: each output product is a one-reduction tail composing a c136-rendered
    `data-algebra` reduce verb by name over its producing driver's solution family.
  - **Found**: each product renders `(driver-family) ▷ (reduce-verb)`: `capacitance` =
    `gram_reduce k vs (\i j -> 1)` + `gram_inverse` tail; `inductance` = the current-normalized
    `gram_reduce` + inverse; `sparameters` = `sparameter_reduce (ports cfg) es`;
    `eigenfrequency_qfactor` = `eigenfreq_qfactor_reduce ptype kappa eigs`; `energy_fields` =
    `domain_energy_reduce doms field e_total` (driver-AGNOSTIC); `waveguide_mode` =
    `waveguide_mode_reduce eigs (omega cfg)`. Each composes the named `data-algebra` reduce verb
    (NOT re-rendered) and cites its feature column. The c074/c075 do-NOT-over-unify distinction
    (`sparameter_reduce` is port-projection, NOT a Gram self-fold) is preserved (synthesis `:261`).
  - **Verdict**: supports.

- **Citation**: `book/src/synthesis/drivers.md:326-359` (`lifecycle` spine ROOT) vs
  `book/src/feature/lifecycle.L4.md:36-44,63` (the spine-ROOT composition).
  - **Theme claim**: `lifecycle = fold_solve (dispatch (problem_type cfg)) ∘ build_mesh`; the AMR
    estimate-mark-refine is `fold_solve` in its state-generated `schedule-source` form; the AMR leaf
    is composed by reference (not a Synthesis deliverable).
  - **Found**: the synthesis renders `build_mesh cfg`, `dispatch (problemType cfg)` (the
    specialization seam over the 6 driver defs), the `step = \m -> estimate_mark_refine cfg (drv cfg
    m)` iterate, and `fold_solve_amr step mesh0 (refinement cfg)` whose `where`-clause expands it as
    `fold_solve (amr_op refcfg) m0 (amr_schedule refcfg)` — the state-generated `fold_solve` form.
    The `dispatch` table over `ELECTROSTATIC..BOUNDARYMODE` matches the L0 `switch
    (iodata.problem.type)` (`main.cpp:257-280`, cited at lifecycle.L4.md:50). The AMR-disabled
    degenerate-to-single-solve note + the estimate-mark-refine-composed-by-reference disclosure
    (synthesis `:351-355`) match the feature column's stage-3 claim (`lifecycle.L4.md:52,61`).
  - **Verdict**: supports.
  - **Notes**: the synthesis elaborates the feature column's `fold_solve step mesh0` into a
    `fold_solve_amr` `where`-wrapper + the explicit `dispatch` table — a faithful elaboration (it
    renders the synthesized code form of the same compositional claim), not a divergence. The AMR
    leaf is honestly composed-by-reference (AMR's synthesized impl is not a Synthesis deliverable),
    so the fold quantifies over `estimate_mark_refine` rather than fabricating a def — the correct
    disposition for an in-scope-but-un-rendered constituent.

### types.md defs

- **Citation**: `book/src/synthesis/types.md:26-49` (`IoData`) vs
  `book/src/concepts/config-record.md:67-75` (the authoritative `IoData` brace form).
  - **Theme claim**: renders the synthesized `IoData` type-def form + utility API, linking the
    authoritative field schema to `config-record.md`, not restating field semantics.
  - **Found**: the synthesis renders `IoData = { problem, model, domains, boundaries, solver }` (5
    fields) with the five `config::*Data` clean-room renamings annotated, citing
    `config-record.md:69-73`. The authoritative `IoData` brace form (`config-record.md:67-75`) has
    **SIX** fields — the five plus `units : Units // SI ↔ nondimensional scale converter`
    (`config-record.md:74`). The synthesis OMITS `units`. The cited range `:69-73` is self-consistent
    with the 5-field rendering (it excludes the `:74` `units` line), and the back-link to the
    authoritative full schema is present and correct.
  - **Verdict**: partially-supports (5 of 6 fields rendered; the elision is benign but a
    completeness gap in the synthesized type-def).
  - **Notes**: **FLAGGED RESIDUAL (benign field elision).** A faithful synthesized type-def should
    render all 6 authoritative fields (or note the elision). `units` is genuinely part of the
    construction-stratum `IoData` (the SI↔nondimensional scale converter). Because the authoritative
    schema lives ONCE in `config-record.md` (and the back-link IS present), this is not a
    semantic-consolidation violation, just an incomplete render. Proposed as a one-line add to
    types.md (gated to the shell author — see Proposed changes).

- **Citation**: `book/src/synthesis/types.md:51-78` (`OpParams`) vs `book/src/concepts/op-params.md`.
  - **Theme claim**: renders the readonly construction-time `OpParams` surface (constructed-operator
    surfaces + variant selectors + termination knobs), linking the field schema to `op-params.md`.
  - **Found**: `OpParams = { T, orthog?, scalars?, eps, pc_side, gs_orthog, flexible, poly_kind?,
    restart, max_dim, max_it, rel_tol, abs_tol }` renders the constructed-operator-surfaces +
    variant-selectors + termination-knobs grouping, citing `op-params.md` as the authoritative
    schema. The "kernel touches OpParams ONLY through the constructed-operator surfaces" discipline
    is preserved (a comment, not a restated law).
  - **Verdict**: supports.
  - **Notes**: light spot-check against the op-params concept home (present, authoritative-linked);
    the rendered grouping is consistent with the readonly construction-stratum claim.

- **Citation**: `book/src/synthesis/types.md:80-97` (`SimState`) vs `book/src/concepts/sim-state.md`,
  `book/src/L4/ksp_solve.md:79`.
  - **Theme claim**: renders the run-time-evolved five-field `SimState` (uniform across CG / GMRES /
    FGMRES / Chebyshev), linking the field schema to `sim-state.md`.
  - **Found**: `SimState = { x: Tensor[(S: ...)], it: Int, converged: Bool, final_res: Scalar,
    initial_res: Scalar }` matches the `ksp_solve.md:79` five-field shape exactly, with the iterate
    `x` named with shape group `S` (semantics §1.2.1, not a rank-1 axis), citing `sim-state.md` as
    authoritative. The `Solve a = StateT SimState Identity a`-deferred-to-coordination note is
    correct (the monad surface lives in `coordination`, not restated here).
  - **Verdict**: supports.

## Applicability conditions

The Synthesis-chapter-KIND obligations function as applicability conditions on every rendered def
across the three libraries:

- **Condition**: Implementation VIEW — renders synthesized code form; does NOT restate
  laws/semantics/record-field-schema (those live ONCE at the L4 / semantic-surface / concept home;
  the def LINKS to them).
  - **Verifiable**: yes — every audited def opens with a "Rendered from `../L4/<op>.md`" / "lives in
    `concepts/<record>.md`" link and renders only the code body + code-doc; no §Algebraic-laws
    section, no reduction rules, no record-field-semantics restatement. Caps link their coordination
    identities (`ksp_solve` `:181`, `eigsolve` `:216`, `solve_family` `:262`, etc.); drivers link
    their compositional claims to the feature columns; types link their schemas to `concepts/`.
  - **Found counter-example?**: no. No semantic-consolidation violation across the three libraries.

- **Condition**: `reference`-class edges only — no `depends-on` blocking edge, no `rank:` claim.
  - **Verifiable**: yes — all three chapters' frontmatter carry `edges: reference:` ONLY (no
    `depends-on:` key), `kind: navigational-container`, no `rank:`. The only `depends-on` text is
    comment prose stating what the chapters do NOT add (e.g. drivers.md `:8` "Adds no `depends-on`
    blocking edge").
  - **Found counter-example?**: no. Zero spurious `depends-on` — the specific defect this audit
    guards against (per the rescope kernel-API/impl correspondence bullet). The synthesis Part never
    blocks on / depends-on anything, including the opaque kernel-API surfaces it `#extern`s.

- **Condition**: `#extern NAME` after the type signature for opaque-library kernels; the
  from-our-primitives impl rendered inline where firm; the kernel-API/impl correspondence intact.
  - **Verifiable**: yes — `eigsolve`'s `eigen_iterate` is `#extern` after its sig (the SLEPc EPS
    kernel-API leaf); `fold_solve`'s `time_step_op` is `#extern` after its sig (the MFEM ODESolver
    boundary); both have the lifting callback / fold rendered around them. The `eigsolve-impl`
    `realizes-kernel-api` edges (to L3/eigsolve + L4/eigsolve) are confirmed `reference`-class
    on-disk — DIRECTIVE-3 intactness CONFIRMED.
  - **Found counter-example?**: no. The `#extern`-vs-inline split tracks the kernel-API/impl
    distinction exactly; no `realizes-kernel-api` edge mis-typed to `depends-on`.

- **Condition**: closure-returning signatures paren-grouped where high-order (semantics §1.3.1).
  - **Verifiable**: yes — the high-order cap/driver/combinator signatures render paren-grouped where
    they return closures (`ksp_solve`'s `solve_loop :: ... -> Solve ()`, `eigsolve`'s `eigen_iterate
    :: ... -> Solve EigOutcome`, etc.); the rendering convention is declared at coordination.md:41 +
    drivers.md:49 and honored.
  - **Found counter-example?**: no.

- **Condition**: topological def order (a def appears after everything it uses).
  - **Verifiable**: yes — coordination.md orders type-block → `preconditioning-framework` →
    `ksp_solve` → `eigsolve` → `solve_family`/`frequency_sweep`/`fold_solve` (the combinators that
    fold/map the caps last). drivers.md orders per-driver config records → 6 drivers → 6 output
    products → lifecycle ROOT (topologically last, composing all). types.md orders
    `IoData` → `OpParams` → `SimState` (construction-time inputs before the run-time-threaded state).
  - **Found counter-example?**: no.

## Algebraic laws (if cited)

N/A as a primary check — the Synthesis chapter KIND deliberately does NOT state algebraic laws (they
live ONCE at the L4 chapters). The audit's law-relevant check is the converse: that each rendered
code BODY is semantics-preserving w.r.t. its L4 body whose laws are stated elsewhere. That
body-equivalence is the per-citation audit above. Spot-confirmation of the law-bearing structure each
rendered coordination/driver body must preserve:

- **Law (ksp_solve `execState`/`StateT` discharge fusion + classify-once)**: preserved — the
  rendered `execState (solve_loop op inp) (initial_state inp)` is the exact discharge the L4 law-1
  rests on; the single `pure (classify kn op s)` is the classify-once site (L4 law 5).
- **Law (eigsolve `apply_shift_invert` body-composition identity, L4 law 2)**: preserved — the
  rendered `apply_linop ▷ ksp_solve_op ▷ scale_untransform` is the exact lifting composition; the
  `EigOutcome` classify-once (L4 law 3) is the single `classify_into_state o`.
- **Law (solve_family concatenation-homomorphism / operator-capture-once-hoist)**: preserved — the
  rendered `map (ksp_solve op)` is the exact list-homomorphism the L4 laws hold of; op captured once
  outside the map.
- **Law (frequency_sweep concatenation-homomorphism-despite-varying-operator / NO-SetOperators-hoist)**:
  preserved — the rendered per-ω rebuild inside the map is exactly the `operator-capture =
  per-element` shape the non-hoist non-law requires.
- **Law (fold_solve fold-threading / NON-commutativity)**: preserved — the rendered `foldl (\s t ->
  time_step_op op s t) s0 schedule` is the exact carry-threading the sequential-obstruction non-law
  requires; `time_step_op` folded opaquely.
- **Law (driver compositional claims)**: each driver's rendered composition (e.g. electrostatic
  `gram_reduce ∘ solve_family ∘ fe_assemble`) is the exact composition the feature L4 column's
  compositional claim asserts.

## Proposed changes

**No mutation to any L4 / feature / concept chapter is proposed from this audit** (audit-class; the
two residuals route as gated follow-ups, not in-this-audit edits). The two flagged residuals:

### Residual 1 (UPSTREAM — gated to an `abstractor` reread of `L4/eigsolve.md`)

The synthesis `eigsolve` def correctly renders `initial_eig_state` and flags the L4 chapter's
`initial_state` (`:44` + `:97`) as a latent inconsistency. The fix belongs in `L4/eigsolve.md` (the
authoritative chapter), NOT in the synthesis rendering (which is already correct). The exact upstream
edit (for the gated `abstractor` follow-up to apply, NOT applied here):

- `book/src/L4/eigsolve.md:44`: `eigsolve op inp = execState (solve_loop op inp) (initial_state inp)`
  → `... (initial_eig_state inp)` (the EigState-seeding constructor coherent with the cap's
  `Solve a = StateT EigState Identity a` threading established at `:70` + `:74`).
- `book/src/L4/eigsolve.md:97` (§Semantics net-effect prose): the `initial_state inp` reference
  reconciled to the same `initial_eig_state` (or explicitly noted as the EigState seed).

This is NOT a synthesis correspondence defect (the synthesis render is the more-correct form with a
faithful inline disclosure); it is an authoritative-chapter self-inconsistency the audit surfaced.
Routed as OQ `l4-eigsolve-initial-state-vs-initial-eig-state-seed-inconsistency` → `abstractor`.

### Residual 2 (synthesis-shell completeness — gated to the `layer-intro-author` shell pass)

The synthesis `types.md` `IoData` renders 5 of the 6 authoritative fields, omitting `units : Units`.
Proposed one-line completeness add (for the gated shell-author follow-up to apply, NOT applied here),
inside the existing ` ```text ` `IoData` block at `book/src/synthesis/types.md:43`:

    solver     : SolverConfig       -- linear/eigen/driven/transient solver settings + tolerances
    units      : Units              -- SI ↔ nondimensional scale converter (config-record.md:74)

and widen the cited range comment at `types.md:34` from `config-record.md:69-73` to
`config-record.md:69-74` (to cover the `units` field). Benign; the authoritative back-link already
carries the full schema. Routed as OQ
`synthesis-types-iodata-omits-units-field` → `layer-intro-author` shell pass.

## Supporting evidence

- `book/src/synthesis/index.md` §"Rendering conventions" — the per-library-chapter rendering
  obligations (topological order, `#extern` after sig, inline unchanged artifacts, link-don't-restate,
  reference-class-only edges); all confirmed satisfied by the three audited libraries.
- `book/src/L3/eigsolve-impl.md:19-23` — the `realizes-kernel-api` edges to `L3/eigsolve` +
  `L4/eigsolve` confirmed `reference`-class on disk (the DIRECTIVE-3 dual-surface integrity check);
  the kernel-impl node `eigsolve-impl` correctly reaches the eigenmode root via its blocking
  `depends-on` constituent edges, with the `realizes-kernel-api` edge free/navigational (the RE11
  intended disposition).
- `book/src/concepts/config-record.md:67-75,105-130` — the authoritative 6-field `IoData` brace form
  (the `units` field at :74 the synthesis omits) + the §"Per-driver specializations" projection table
  the drivers.md per-driver aliases render against.
- `book/src/L4/eigsolve.md:44,70,74,97` — the latent `initial_state`-vs-`StateT EigState` self-
  inconsistency the synthesis `eigsolve` def caught (:44 + :97 seed via `initial_state`; :70 + :74
  thread `EigState`).
- `book/src/feature/{electrostatic,eigenmode,lifecycle}.L4.md` — the composition roots the drivers.md
  defs render against (deep-audited; magnetostatic/driven/transient/boundary-mode + the 6 output
  products spot-checked structurally).
- L0 anchor spot-check via the citecheck adjudicator is N/A here — the synthesis defs carry NO L0
  citations (link-don't-re-cite convention); the L0 substrate is owned by the L4 / feature / concept
  chapters the synthesis links to. The audit's anchors are book-internal (rendered-def ↔
  authoritative-chapter line correspondences), each `Read`-confirmed on disk above.

## Open questions / caveats

- **OQ `l4-eigsolve-initial-state-vs-initial-eig-state-seed-inconsistency` (NEW, intake → abstractor).**
  L4/eigsolve.md:44 + :97 seed the EigState-threaded cap via `initial_state` (a SimState constructor),
  contradicting the cap's own `Solve a = StateT EigState Identity a` threading (:70, :74). The
  synthesis `eigsolve` def renders the type-coherent `initial_eig_state` and already flags this. The
  fix is upstream (L4 chapter), gated to an `abstractor` reread — NOT a synthesis defect. See Proposed
  changes Residual 1.

- **OQ `synthesis-types-iodata-omits-units-field` (NEW, intake → layer-intro-author).** The synthesis
  `types.md` `IoData` renders 5 of 6 authoritative fields (omits `units : Units`,
  config-record.md:74). Benign (full schema is in the authoritative back-link); a one-line
  completeness add gated to the shell author. See Proposed changes Residual 2.

- **Per-library `kind: navigational-container` token vs the prior `stub`/`seed` index cells
  (navigational, non-blocking — INHERITED from c137, now confirmed across all three).** coordination.md
  carries `> Status: seed` (`:19`) in its body prose while drivers.md/types.md carry the
  `navigational-container` (rendered) convention the c136/c137 finalize normalized. This per-chapter
  status-token reconciliation across the 6 synthesis chapters is the shell-author/meta normalization
  the c137 finalize + the cycle-138 plan §Open-questions already flag (the D2 maintenance-floor sweep
  will FLAG residual token inconsistency). NOT a correspondence defect — the rendered bodies are
  faithful regardless of the cell/status label. Routed here, not auto-fixed (out of audit scope: the
  Synthesis status convention is the shell author's to set).

- **No directionality / rank-violation / mis-typed-edge issues found.** The Synthesis Part is an
  implementation VIEW (not a lowering theme), so the high→low theme-directionality check is N/A; the
  reference-class-only edge discipline means no rank-violation surface exists (the Part adds no
  blocking edges). The one `realizes-kernel-api` correspondence in scope (eigsolve dual-surface) has
  its edge confirmed `reference`-class on disk — no mis-typing.

- **Coverage now COMPLETE.** With this audit, all 6 Synthesis library chapters' rendered defs are
  verified faithful (c137: `iteration` + `data-algebra`; c138: `coordination` + `drivers` + `types`).
  The whole `# Synthesis` Part is correspondence-audited. The batch-44 meta inherits a fully-verified
  Synthesis surface modulo the two gated residuals above (one upstream L4-chapter fix, one
  synthesis-shell completeness add) — neither blocking.
