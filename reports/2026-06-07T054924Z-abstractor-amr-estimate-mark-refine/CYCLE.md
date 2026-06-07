---
agent: abstractor
invoked_at: 2026-06-07T054924Z
scope: L1>L0 theme sketch — amr-estimate-mark-refine (DIRECTIVE-2 grounded consumer-(2), AMR front opener)
status: pending
inputs:
  - palace/drivers/basesolver.cpp:153-276 (SolveEstimateMarkRefine — the estimate→mark→refine loop)
  - palace/drivers/basesolver.cpp:103-115 (MarkedElements — threshold→index-set)
  - palace/utils/dorfler.cpp:14-171 (ComputeDorflerThreshold — bulk-marking math, read SINGLE-RANK)
  - palace/linalg/errorestimator.cpp:184-268 (ComputeErrorEstimates — the ZZ flux-difference per-element reduction core)
  - palace/linalg/errorestimator.cpp:273-378 (GradFluxErrorEstimator ctor — electrostatic εE flux estimator)
  - palace/linalg/errorestimator.cpp:391-500 (CurlFluxErrorEstimator ctor — magnetostatic μ⁻¹B flux estimator)
  - palace/linalg/errorestimator.cpp:511-560 (TimeDependentFlux/BoundaryModeFlux composite estimators)
  - palace/main.cpp:304 (the SolveEstimateMarkRefine call site)
  - book/src/feature/lifecycle.L4.md, lifecycle.L0.md, spine-root.md (the loop is ALREADY homed via fold_solve state-generated)
  - book/src/L4/fold_solve.md (schedule-source=state-generated axis names the AMR loop as a witness)
integrated_at: 2026-06-07T054924Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (repaired). L1-L0/amr-estimate-mark-refine rough-in theme + 2 L1 rough-in verb rows (AMR front opener)."
---

# CYCLE: L1>L0 theme sketch — amr-estimate-mark-refine

## Summary

The AMR front opens cleanly with one **non-obvious finding that reshapes the dispatch**: the
estimate→mark→refine **outer loop is already homed** — `fold_solve`'s
`schedule-source = state-generated` axis explicitly names "the AMR Solve→Estimate→Mark→Refine loop
(basesolver.cpp:190, error-indicator-terminated)" as a witness (`book/src/L4/fold_solve.md:20`), and the
lifecycle feature column already presents the loop composition at L4/L1/L0 (`lifecycle.L4.md:52`,
`lifecycle.L0.md:39-42`, `spine-root.md:21`). So authoring a `roadmap_goal` for the *loop* would
duplicate a firm home — the redirect's degenerate-identity smell. The **genuine gap** is the
per-iteration **body vocabulary** the `fold_solve` `step` calls but which has NO L1 form yet: the
**estimate** verb (Zienkiewicz–Zhu flux recovery) and the **mark** verb (Dörfler bulk-marking). I land
the L1>L0 lowering theme `amr-estimate-mark-refine` for the **step body** — how the pure composition
`(mesh', indicators') = refine(mesh, mark(estimate(solve(mesh))))` lowers into Palace's imperative
loop body — and propose the **flux-recovery-estimator vocabulary cohort** + the **Dörfler-mark** verb
as speculative L1 operators (rough-in placeholders; harvester promotes). The **refine** stage is the
MFEM-opaque `ParMesh::GeneralRefinement` leaf — `obstruction (opaque-library-ownership)`, NOT forced.
This is a real vocabulary translation: a libCEED-backed flux-projection-solve + per-element quadrature
integration + sort/partial-sum/threshold-bisection marking + in-place mesh growth → a pure
`estimate ▷ mark ▷ refine` pipeline whose carry the already-firm `fold_solve` threads. Single-rank per
DIRECTIVE-1 (the Dörfler cross-rank threshold bisection is read as the trivial single-rank degeneracy).

## Proposed changes

```new:book/src/L1-L0/amr-estimate-mark-refine.md
---
# Lowering theme. Per graded-stack scheme §5: rank = min(endpoint ranks). The L1
# endpoints (flux_recovery_estimate / dorfler_mark) are rough-in speculative
# vocabulary (rank 2); the refine endpoint is an opaque-library obstruction leaf.
# So the theme is rough-in pending the harvester-promotion of its L1 cohort.
rank: rough-in
edges:
  depends-on:
    - target: L1/flux_recovery_estimate
      kind: lowers-to             # the ZZ flux-recovery estimate verb (rough-in; this cycle's cohort)
    - target: L1/dorfler_mark
      kind: lowers-to             # the Dörfler bulk-marking verb (rough-in; this cycle's cohort)
    - target: palace/drivers/basesolver.cpp:153-276
      kind: cites-evidence        # SolveEstimateMarkRefine: the estimate→mark→refine loop body
    - target: palace/utils/dorfler.cpp:14-171
      kind: cites-evidence        # ComputeDorflerThreshold: bulk-marking math (read single-rank)
    - target: palace/linalg/errorestimator.cpp:184-268
      kind: cites-evidence        # ComputeErrorEstimates: the ZZ flux-difference per-element reduction core
    - target: palace/linalg/errorestimator.cpp:273-378
      kind: cites-evidence        # GradFluxErrorEstimator ctor: electrostatic εE flux estimator
    - target: palace/linalg/errorestimator.cpp:391-500
      kind: cites-evidence        # CurlFluxErrorEstimator ctor: magnetostatic μ⁻¹B flux estimator
  reference:
    - L4/fold_solve                               # the loop is ALREADY homed: fold_solve state-generated witness
    - feature/lifecycle.L4                         # the loop composition home (estimate-mark-refine outer fold)
    - L1-L0/triangular-solve-obstruction          # sibling opaque-library-ownership obstruction (refine leaf is the analogue)
    - L1-L0/fe-assemble-libceed-boundary-obstruction  # the libCEED-quadrature kernel-api the estimate verb leans on
---

# amr-estimate-mark-refine

**Slug:** `amr-estimate-mark-refine`

How the pure L1 **estimate→mark→refine body** — the `step` the adaptive `fold_solve` threads — lowers
into Palace's imperative AMR loop body (`palace/drivers/basesolver.cpp:153-276`,
`SolveEstimateMarkRefine`). This is a **vocabulary translation, not a rename**: the L1 form is a pure
pipeline of three verbs over a referentially-transparent mesh-and-indicators carry —
`(mesh', indicators') = refine(mesh, mark(estimate(field, mat)))` — while the L0 form is an imperative
loop body that (a) calls a libCEED-backed **flux-recovery** computation writing into mutable grid-function
buffers, (b) **marks** by an in-place sort / partial-sum / threshold-bisection on a copied estimate
vector, and (c) **refines** by mutating the `ParMesh` in place via the MFEM-owned `GeneralRefinement`.
The translation has a **sharp three-way boundary**:

- the **estimate** verb lowers HERE (the ZZ flux-difference reduction is Palace-authored — the
  libCEED quadrature *integrator* it calls is a separate kernel-api, `fe-assemble-libceed-boundary-obstruction`);
- the **mark** verb lowers HERE (the Dörfler bulk-marking math is fully Palace-authored, `utils/dorfler.cpp`);
- the **refine** leaf does NOT lower — `mfem::ParMesh::GeneralRefinement` is MFEM-owned
  (`obstruction (opaque-library-ownership)`, narrated in the split below, NOT forced).

The **outer loop is intentionally NOT re-homed here** — it is already the firm L4
[`fold_solve`](../L4/fold_solve.md) in its `schedule-source = state-generated` form (the AMR loop is one
of its two named witnesses, `fold_solve.md` §variant-axes), presented at the lifecycle feature column
([`lifecycle.L4`](../feature/lifecycle.L4.md) §3, [`lifecycle.L0`](../feature/lifecycle.L0.md)). This
theme lowers the **body the fold threads**, not the fold; re-asserting the loop would be the
identity-lowering smell.

## Status

`rough-in` — the structural three-way decomposition (estimate / mark / refine) is positively anchored
at L0, but the two lowering endpoints are **speculative L1 vocabulary proposed THIS cycle**
(`flux_recovery_estimate` and `dorfler_mark` — plain-text forward-references, not-yet-on-disk speculative
ops per the rough-in forward-reference convention; the integrator may materialize them as rough-in
stub rows, both rough-in pending harvester promotion). The theme firms
to `firm` when both L1 endpoints are harvested firm (well-foundedness: a lowering theme is at most as
resolved as its least-resolved endpoint, scheme §5). The **refine** leg is a permanent
`obstruction (opaque-library-ownership)` sub-leaf (MFEM owns `GeneralRefinement`); it does not gate the
theme's promotion because it is a documented boundary, not an unfilled body (the
[`triangular-solve-obstruction`](./triangular-solve-obstruction.md) precedent for an opaque-library
sub-leaf inside an otherwise-constructive composition).

## L1 form (LHS)

The step body the `fold_solve` carry threads, in our vocabulary (named shape groups; the per-element
indicator vector is `Tensor[(E: n_elem)]`, the field DOF vector is `Tensor[(D: n_dof)]`):

    -- the carry fold_solve threads (lifecycle.L4 §3): { mesh, indicators, ntdof, err }
    amr_step :: Estimator -> RefineConfig -> AmrCarry -> AmrCarry
    amr_step est cfg carry = do
      let { field, ntdof } = solve carry.mesh            -- per-driver Solve override (the feature column body)
      let indicators       = flux_recovery_estimate est field   -- ESTIMATE (this cohort)
      let err              = nrm2 indicators                     -- existing L1 nrm2 (Norml2 reduction)
      let marked           = dorfler_mark cfg.fraction indicators -- MARK (this cohort)
      let mesh'            = refine carry.mesh marked            -- REFINE (opaque-library leaf)
      pure { mesh: mesh', indicators, ntdof, err }

where:

- `flux_recovery_estimate :: Estimator -> Tensor[(D: n_dof)] -> Tensor[(E: n_elem)]` *(speculative L1
  op, rough-in; plain-text forward-ref — not yet on disk)* — the ZZ
  flux-recovery estimate verb (rough-in, this cohort). Recovers a *smooth* flux by projecting the
  *discontinuous* material flux onto a smooth FE space, then returns the per-element L2 norm of the
  difference (the ZZ a-posteriori indicator).
- `dorfler_mark :: Real -> Tensor[(E: n_elem)] -> IndexSet[E]` — the Dörfler (bulk) marking verb
  (rough-in, this cohort). Returns the *smallest* element index set whose summed squared-error covers at
  least fraction θ of the total — `arg min |S| s.t. Σ_{i∈S} e_i² ≥ θ · Σ_i e_i²`.
- `refine :: Mesh -> IndexSet[E] -> Mesh` — the MFEM-opaque mesh refinement leaf (obstruction).
- `nrm2`, `solve` are existing vocabulary ([`nrm2`](../L1/nrm2.md); the per-driver `Solve` override is
  the feature-column body).

## Record definition

The three opaque types named in the signatures above, defined in themselves (single-consumer — this
chapter is the only current consumer; harvester promotes the fuller homes when the two L1 verbs firm):

- **`AmrCarry`** — the per-iteration carry the firm `fold_solve` threads:
  `{ mesh: Mesh, indicators: Tensor[(E: n_elem)], ntdof: Int, err: Real }` (the running mesh, the
  per-element error-indicator vector, the global true-DOF count, the scalar error estimate). The shape is
  presented at the lifecycle column `lifecycle.L4 §3` (the home of the loop composition); defined here for
  the step-body signature.
- **`RefineConfig`** — the (construction-time) refinement config record. The L0 home is the Palace
  `RefinementData` struct (`palace/utils/configfile.hpp:96-125`), the `refinement.*` IoData surface;
  the fields this step body reads are `fraction` (← `update_fraction`, the Dörfler bulk fraction θ,
  default 0.7, `:118-119`), with sibling construction-time fields `tol`/`max_it`/`max_size`/`max_nc_levels`
  also on the record. Construction-time stratum (read once before the loop), not run-time-threaded.
- **`Estimator`** — the per-driver flux-recovery estimator closure (construction-time): it bundles the
  flux coefficient (electrostatic `ε` / magnetostatic `μ⁻¹` / composite) + the `FluxProjector` member
  (the mass-matrix flux-projection sub-solver) + the libCEED per-element-integration kernel-api. Its
  precise constructed-operator-gate-vs-absorbed status is OPEN and routed to the harvester (OQ
  `flux-projector-constructed-operator-gate-vs-absorbed`); defined here as "the construction-time closure
  the estimate verb is parameterized over," fields to be firmed at harvest.
- **`IndexSet[E]`** — the marking result type: a set of element indices into the `E: n_elem` axis,
  `{ i : 0 ≤ i < n_elem }` (the marked-for-refinement subset). Produced by `dorfler_mark` as
  `{ i : e[i] ≥ threshold }` and consumed by `refine`; the L0 home is the `mfem::Array<int>` the
  `MarkedElements` `ind.Append(i)` loop fills (`palace/drivers/basesolver.cpp:103-115`).

## L0 form (RHS)

The imperative loop body, `palace/drivers/basesolver.cpp:153-276`:

- **Initial solve + estimate** (`:173-175`): `auto [indicators, ntdof] = Solve(mesh)` (`:174`);
  `double err = indicators.Norml2(comm)` (`:175`).
- **The `while` carry** (`:188-190`): `while (use_amr && !ExhaustedResources(it, ntdof) && err >= refinement.tol)`
  — the state-generated loop guard the firm `fold_solve` covers; NOT re-homed here.
- **Mark** (`:220-233`): the `marked_elements` lambda calls `utils::ComputeDorflerThreshold(comm, indicators.Local(), refinement.update_fraction)`
  (`:223-224`) then `MarkedElements(indicators.Local(), threshold)` (`:225`, the threshold→index-set at
  `palace/drivers/basesolver.cpp:103-115`).
- **Refine** (`:235-245`): `fine_mesh.GeneralRefinement(marked_elements, -1, refinement.max_nc_levels)`
  (`:239`) — the MFEM-opaque leaf.
- **Re-solve + estimate** (`:265-267`): `std::tie(indicators, ntdof) = Solve(mesh)` (`:266`);
  `err = indicators.Norml2(comm)` (`:267`).

### Sub-pattern A — estimate (ZZ flux recovery) → `flux_recovery_estimate`

The estimate verb's body is the Palace-authored `ComputeErrorEstimates` (`palace/linalg/errorestimator.cpp:184-268`):

1. **Recover the smooth flux**: `projector.Mult(F, G)` (`:193`) — a flux-projection *solve* that projects
   the discontinuous flux `F` (e.g. `εE = ε∇V` for `GradFluxErrorEstimator`,
   `μ⁻¹B ≃ μ⁻¹∇×E` for `CurlFluxErrorEstimator`) onto a smooth FE space, producing `G`.
2. **Prolong to grid functions**: `fespace.GetProlongationMatrix()->Mult(F, F_gf)` /
   `smooth_fespace.GetProlongationMatrix()->Mult(G, G_gf)` (`:203-204` real arm; the complex arm splits
   real/imag prolongation `:198-201`).
3. **Per-element integrate the squared difference**: a libCEED composite operator
   (`CeedOperatorApplyAdd(integ_op[...], CEED_VECTOR_NONE, estimates_vec, ...)`, `:252-253`) integrates
   `∫_K |G − F|²` over each element `K`, accumulating into `estimates` (`Vector estimates(mesh.GetNE())`,
   `:209`). The complex case adds the imaginary-part squared via a second `CeedOperatorApplyAdd` (`:259`).

The two material specializations differ only in the **flux coefficient** and the **libCEED qfunction
selector**: `GradFluxErrorEstimator` uses `ε`/`√ε`/`√ε⁻¹` (`palace/linalg/errorestimator.cpp:273-378`,
the `f_apply_hcurlhdiv_error_22/33` qfunctions at `:348-353`); `CurlFluxErrorEstimator` uses
`μ⁻¹`/`√μ⁻¹`/`√μ` (`:391-500`, `f_apply_l2h1_error` / `f_apply_hdivhcurl_error_33` at `:470-475`,
with the 2D-scalar-curl branch `:450`). The `√` and `½/Et` energy-correction factor is applied at
`AddErrorIndicator` (`linalg::Sqrt(estimates, (Et > 0.0) ? 0.5 / Et : 1.0)`, `:386` Grad / `:508` Curl).
The composite estimators `TimeDependentFluxErrorEstimator` (`:511-538` region) and
`BoundaryModeFluxErrorEstimator` (`:540-568` region) **sum** a Grad + Curl estimate
(`grad_estimates += curl_estimates`, `:536` / `:566`) — a `axpy(1, ...)`-shape composition over the
two material-flux indicators, NOT new verbs (the **flux-channel axis** of the same `flux_recovery_estimate`).

The libCEED quadrature integrator is a **kernel-api** boundary (the
[`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md) leaf the
estimate verb leans on); the flux-projection solve reuses the existing solve vocabulary
([`ksp_solve`](../L1/ksp_solve.md)-shape, via the `FluxProjector` member). What lowers HERE is the
ZZ structure (recover-smooth-flux ▷ per-element-norm-of-difference), not the quadrature kernel.

### Sub-pattern B — mark (Dörfler bulk-marking) → `dorfler_mark`

The mark verb's body is `utils::ComputeDorflerThreshold` (`palace/utils/dorfler.cpp:14-171`) +
`MarkedElements` (`palace/drivers/basesolver.cpp:103-115`). **Read single-rank** (DIRECTIVE-1): the
cross-rank threshold-bisection (`Mpi::GlobalMin`/`GlobalMax`/`GlobalSum` at `:67-68`, `:84-85`, the
`for (int i = 0; i < max_it; i++)` bisection `:101-166`) degenerates — single-rank, `min_threshold ==
max_threshold` (`:64-68`) and the bisection loop is entered only to confirm the already-exact local
threshold. The Palace-authored single-rank math:

1. **Sort the per-element estimates** ascending (`std::sort`, `:20`); square them and **partial-sum**
   (`std::partial_sum`, `:28`) to get cumulative squared-error; un-square the estimate copy (`:29-31`).
2. **Find the pivot**: the first estimate leaving fraction `(1−θ)` of the total squared-error *below*
   it — `std::lower_bound(sum.begin(), sum.end(), (1 - fraction) * local_total)` (`:36`), giving the
   `error_threshold` (`:38`).
3. **Threshold → index set**: `MarkedElements(e, threshold)` collects `{ i : e[i] ≥ threshold }`
   (`palace/drivers/basesolver.cpp:103-115`, the `ind.Append(i)` loop `:109-111`).

The "always choose the lower threshold, over-mark rather than under-mark" tie-break (`:163`, with the
explanatory comment `:161-162`) is a
**load-bearing** marking-set choice (the Dörfler predicate is the *smallest* set covering ≥θ; the
implementation returns the over-marking lower-threshold result) — preserved as an explicit algebraic
claim on `dorfler_mark`, not erased. The sort + partial-sum + lower-bound is a transparent
performance shape over the abstract "select smallest index set covering θ of total squared error."

### Sub-pattern C — refine (MFEM-opaque) → obstruction

`mfem::ParMesh::GeneralRefinement(marked_elements, -1, refinement.max_nc_levels)`
(`palace/drivers/basesolver.cpp:239`) mutates the mesh in place. This is
`obstruction (opaque-library-ownership)`: the refinement kernel (element subdivision, hanging-node /
nonconforming constraint generation, the `max_nc_levels` nonconforming-level cap) is **MFEM-owned** —
Palace never exposes it as a standalone callable, it calls the MFEM method. The optional
`mesh::RebalanceMesh` (`:247-261`) + `mesh.back()->Update()` (`:262`) are likewise MFEM/distributed
(read single-rank: rebalancing is a no-op on one rank). **Negative anchor (opaque-library-ownership
witness):** there is no Palace-authored mesh-refinement body — the only refinement site in the AMR loop
is the MFEM `GeneralRefinement` call (`:239`); cf. the a-priori (non-adaptive) `mesh::RefineMesh`
(`palace/utils/geodata.cpp`) which is likewise an MFEM-uniform-refinement wrapper. NOT forced; documented
as the boundary the AMR step crosses.

## Applicability conditions

- AMR is enabled: `refinement.max_it > 0` (`:158-163`); NOT transient
  (`ProblemType::TRANSIENT` aborts AMR, `:158-160`).
- The estimate verb requires a per-driver flux coefficient (electrostatic `ε`, magnetostatic `μ⁻¹`,
  driven/eigenmode the composite Grad+Curl); the marker is driver-agnostic (operates on the scalar
  per-element indicator vector).
- Single-rank reading (DIRECTIVE-1): the Dörfler cross-rank threshold bisection and the mesh rebalance
  are read as their single-rank degeneracies; no MPI collective lowers here.

## Justification kind

**structural** — the three-way estimate/mark/refine decomposition is read directly off the loop body
(`SolveEstimateMarkRefine`), each stage positively anchored. The estimate ZZ structure and the Dörfler
marking math are syntactic identities on positive Palace source; the refine leg is a documented opaque
boundary, not a reconstructed claim.

## Speculative L1 operators (need harvester promotion)

- `flux_recovery_estimate` — the ZZ flux-recovery a-posteriori error estimate verb.
- `dorfler_mark` — the Dörfler bulk-marking verb (smallest index set covering θ of total squared error).

(The `refine` leaf is NOT proposed as a fillable operator — it is the MFEM-opaque obstruction sub-leaf,
the AMR analogue of `triangular-solve-obstruction`.)

## Verified-against

- `palace/drivers/basesolver.cpp:153-276` (`SolveEstimateMarkRefine`; loop head `:188-190`, mark
  `:220-233`, refine `:235-245`, re-solve `:265-267`) — citecheck `[ok]`, on-disk END confirmed `:276` `}`.
- `palace/drivers/basesolver.cpp:103-115` (`MarkedElements`) — citecheck `[ok]`.
- `palace/utils/dorfler.cpp:14-171` (`ComputeDorflerThreshold`; sort `:20`, partial-sum `:28`, pivot
  `:36`, lower-threshold tie-break `:163`) — citecheck `[ok]`.
- `palace/linalg/errorestimator.cpp:184-268` (`ComputeErrorEstimates`; projector `:193`, prolong
  `:203-204`, libCEED integrate `:252-253`) — citecheck `[ok]`.
- `palace/linalg/errorestimator.cpp:273-378` (`GradFluxErrorEstimator` ctor; qfunction selector
  `:348-353`) + `:391-500` (`CurlFluxErrorEstimator` ctor; 2D-scalar-curl `:450`) — citecheck `[ok]`.
- `palace/main.cpp:304` (the `SolveEstimateMarkRefine` call site) — citecheck `[ok]`.

## Status: rough-in
```

```edit:book/src/L1/index.md
[append two rough-in rows to the L1 dep-map table (the speculative AMR estimate/mark vocabulary cohort);
 these are NOT firm — plain-text names, no live-link anchor yet, per the rough-in-rows-must-be-plain-text
 convention:

| `flux_recovery_estimate` *(rough-in; no anchor yet; proposed-by: abstractor:2026-06-07T054924Z-amr-estimate-mark-refine)* | ZZ flux-recovery a-posteriori error estimate `est ▷ field → per-element-indicator`; recover smooth flux by projecting the discontinuous material flux (εE / μ⁻¹B) onto a smooth FE space, return per-element L2 norm of the difference. The AMR estimate verb; flux-channel variant axis (Grad / Curl / Grad+Curl composite). libCEED quadrature integrator is a kernel-api leaf below. | `palace/linalg/errorestimator.cpp:184-268`, `:273-378`, `:391-500` | rough-in |
| `dorfler_mark` *(rough-in; no anchor yet; proposed-by: abstractor:2026-06-07T054924Z-amr-estimate-mark-refine)* | Dörfler (bulk) marking `θ ▷ indicators → IndexSet`; smallest element index set whose summed squared-error covers ≥ θ of total. Sort + partial-sum + lower-bound threshold + threshold→index-set; load-bearing over-mark tie-break. Read single-rank (cross-rank bisection degenerate). The AMR mark verb. | `palace/utils/dorfler.cpp:14-171`, `palace/drivers/basesolver.cpp:103-115` | rough-in |
]
```

```edit:book/src/SUMMARY.md
[add the chapter entry under the L1 > L0 Part's **Construction-rotation themes** sub-group (the head
 `- [Construction-rotation themes](./L1-L0/construction-rotation-intro.md)` at SUMMARY line 266), as a
 nested entry in alpha-position WITHIN that group. `amr-estimate-mark-refine` sorts alpha-FIRST in the
 Construction-rotation group (before `build-mesh-construction-rotation`), so insert it as the first
 child immediately after the Construction-rotation group-intro line and before
 `  - [build-mesh-construction-rotation](./L1-L0/build-mesh-construction-rotation.md)` (line 267):
   `  - [amr-estimate-mark-refine](./L1-L0/amr-estimate-mark-refine.md)`
 RATIONALE — landing-group choice (mixed-kind theme): estimate/mark are construction-rotation, refine is
 the opaque-library-ownership obstruction sub-leaf; the theme is filed in the **Construction-rotation**
 group (its two constructive endpoints dominate; the refine obstruction is a documented sub-leaf, not the
 theme's kind), CONSISTENT with the L1-L0/index.md change below. (The earlier "after `amr` sorts before
 `apply`" instruction was wrong — the L1>L0 Part has three KIND sub-groups, not a flat list, and
 `apply-linop-...` is in the Mutation-rotation group.)]
```

```edit:book/src/L1-L0/index.md
[insert into the Theme list table under the **Construction-rotation** group-header row
 (`| **Construction-rotation** | | | |`), in alpha-position WITHIN that group. As a mixed-kind theme
 (estimate/mark = construction-rotation, refine = opaque-library-ownership obstruction sub-leaf) it is
 filed in the **Construction-rotation** group — CONSISTENT with the SUMMARY.md change above (same
 landing group). `amr-estimate-mark-refine` sorts alpha-FIRST in the group, so insert this row
 immediately after the `| **Construction-rotation** | | | |` header row and before the
 `build-mesh-construction-rotation` row:

| [amr-estimate-mark-refine](./amr-estimate-mark-refine.md) | `L1/flux_recovery_estimate` (rough-in) + `L1/dorfler_mark` (rough-in) | `palace/drivers/basesolver.cpp:153-276`, `palace/utils/dorfler.cpp:14-171`, `palace/linalg/errorestimator.cpp:184-268`,`:273-378`,`:391-500` | rough-in *(structural; 3-way estimate/mark/refine split: A ZZ flux-recovery estimate (recover-smooth-flux ▷ per-element-norm-of-difference; flux-channel axis Grad/Curl/composite; libCEED quadrature kernel-api leaf) / B Dörfler bulk-mark (sort+partial-sum+lower-bound threshold, read single-rank, load-bearing over-mark tie-break) / C refine = MFEM-opaque `GeneralRefinement` obstruction (opaque-library-ownership) leaf; outer loop NOT re-homed — already firm L4 `fold_solve` state-generated; firms when both L1 endpoints harvested firm)* |
]
```

## Speculative operators proposed

- **`flux_recovery_estimate`** — intended signature
  `flux_recovery_estimate :: Estimator -> Tensor[(D: n_dof)] -> Tensor[(E: n_elem)]`. The
  Zienkiewicz–Zhu (flux-recovery / "smooth flux") a-posteriori error estimate. Recovers a smooth flux
  `G` by projecting the discontinuous material flux `F` (electrostatic `εE = ε∇V`; magnetostatic
  `μ⁻¹B ≃ μ⁻¹∇×E`) onto a smooth FE space (a flux-projection solve via the `FluxProjector` member), then
  returns the per-element L2 norm of `G − F` as the indicator vector. The **flux-channel** variant axis
  (Grad-only / Curl-only / Grad+Curl composite — the time-dependent + boundary-mode estimators *sum*
  the two channels, a `axpy(1,·)`-shape over indicators, NOT new verbs). The libCEED element-quadrature
  *integration* it calls is a kernel-api leaf (`fe-assemble-libceed-boundary-obstruction`), tied below;
  the flux-projection solve reuses `ksp_solve`-shape vocabulary. The estimate half of the AMR step body;
  the per-driver indicator producer the lifecycle `fold_solve` carry threads. Harvester should verify
  the four concrete estimators (`Grad`/`Curl`/`TimeDependent`/`BoundaryMode`) collapse to this one verb
  on the flux-channel axis.

- **`dorfler_mark`** — intended signature
  `dorfler_mark :: Real -> Tensor[(E: n_elem)] -> IndexSet[E]`. The Dörfler (bulk / "equilibrium")
  marking verb: given a fraction `θ` and per-element error indicators, returns the **smallest** element
  index set `S` with `Σ_{i∈S} e_i² ≥ θ · Σ_i e_i²`. The Palace single-rank body is sort-ascending +
  squared partial-sum + lower-bound pivot (the `(1−θ)·total` cut) + `{ i : e_i ≥ threshold }`. One
  **load-bearing** algebraic claim: the implementation returns the *over-marking* lower-threshold set
  ("rather over-mark than under-mark," `dorfler.cpp:163`, comment `:161-162`) — the Dörfler predicate is the smallest
  covering set; the realized result is the lower-threshold over-cover. Read single-rank (DIRECTIVE-1):
  the cross-rank threshold-bisection collapses (min==max threshold on one rank). The mark half of the
  AMR step body; driver-agnostic. Harvester should record the bisection as the single-rank-degenerate
  cross-rank reconciliation (an MPI collective folded into a future L1>L0 distributed note, not the
  single-rank L1 signature).

## Supporting evidence

- **The AMR loop is already homed** (the dispatch-reshaping finding): `book/src/L4/fold_solve.md:20`
  (`schedule-source = state-generated` axis explicitly names "the AMR Solve→Estimate→Mark→Refine loop
  (basesolver.cpp:190, error-indicator-terminated)" as a witness); `book/src/feature/lifecycle.L4.md:52`
  (stage 3 = the firm `fold_solve` state-generated adaptive estimate-mark-refine fold);
  `book/src/feature/lifecycle.L0.md:39-42` (the L0 loop composition); `book/src/feature/spine-root.md:21`
  (the lifecycle ROOT's directly-owned firm estimate-mark-refine fold). So the loop is NOT a gap — only
  the per-iteration *body vocabulary* (estimate + mark) is.
- **The estimate ZZ structure**: `palace/linalg/errorestimator.cpp:184-268` (`ComputeErrorEstimates`:
  flux-projection `projector.Mult(F, G)` `:193`, prolongation `:203-204`, libCEED per-element integration
  `:252-253`); the two material specializations `:273-378` (`GradFluxErrorEstimator`, `ε`-flux) +
  `:391-500` (`CurlFluxErrorEstimator`, `μ⁻¹`-flux); the composite Grad+Curl sum `:536` / `:566`.
- **The Dörfler marking math** (read single-rank): `palace/utils/dorfler.cpp:14-171` (sort `:20`,
  squared partial-sum `:28`, pivot `:36`, over-mark tie-break `:163`); the threshold→index-set
  `palace/drivers/basesolver.cpp:103-115` (`MarkedElements`).
- **The refine obstruction**: `palace/drivers/basesolver.cpp:239`
  (`fine_mesh.GeneralRefinement(...)`, MFEM-owned).
- All pinpoint citations citecheck `[ok]` against on-disk source (run this dispatch); function-body END
  lines confirmed by direct on-disk Read (`SolveEstimateMarkRefine` ends `:276`).

## Open questions / caveats

- **`flux_recovery_estimate` flux-channel axis vs separate verbs.** The four concrete estimators
  (`Grad`/`Curl`/`TimeDependent`/`BoundaryMode`) share `ComputeErrorEstimates`; the composites *sum* a
  Grad + Curl call. I propose ONE verb with a flux-channel variant axis (the `+=` composite being an
  `axpy(1,·)`-shape over indicators). Harvester should confirm this collapse holds — alternatively the
  composite is a thin `linear_combination`-over-indicators wrapper (still not a new estimate verb). Filed
  as OQ `flux-recovery-estimate-flux-channel-axis-vs-separate-verbs`.
- **The flux-projection solve inside `flux_recovery_estimate`.** `projector.Mult(F, G)`
  (`errorestimator.cpp:193`) is a `FluxProjector`-member solve (a mass-matrix projection, `use_mg`-gated
  multigrid). It reuses `ksp_solve`-shape vocabulary but the `FluxProjector` is its own constructed-operator
  closure (sibling to `divfree-projector`'s `P.ksp`). Harvester decision: is `FluxProjector` a distinct
  constructed-operator gate, or absorbed into `flux_recovery_estimate`'s `Estimator` closure? Lean:
  absorbed (it is a construction-time member, like `divfree-projector`'s sub-solver). OQ
  `flux-projector-constructed-operator-gate-vs-absorbed`.
- **Dörfler cross-rank reconciliation as a future distributed note.** The full `ComputeDorflerThreshold`
  cross-rank threshold bisection (`dorfler.cpp:101-166`, with `Mpi::Global*` collectives) is read
  single-rank-degenerate per DIRECTIVE-1. When/if a sharding-math note is lifted (the deferred
  DIRECTIVE-1 future direction), the bisection is the canonical "select a global threshold from per-rank
  local thresholds" reconciliation — flag for that future note, NOT lifted now. OQ
  `dorfler-cross-rank-bisection-distributed-note-deferred`.
- **`refine` obstruction sub-kind precedent.** I marked `refine` `obstruction (opaque-library-ownership)`
  (MFEM owns `GeneralRefinement`; nothing for Palace to fill upstream). This is the AMR analogue of
  `triangular-solve-obstruction`. NOT a `kernel-api/impl` candidate (DIRECTIVE-3): mesh refinement is not
  a "well-understood-in-our-tensor-semantics" kernel (hanging-node constraint generation is genuinely
  MFEM-structural, not a tensor contraction) — it stays single-node obstruction, no constructive impl
  owed. Lowering-verifier may confirm the boundary at a later pass.
- **Theme firmness gate.** The theme is `rough-in` until BOTH `flux_recovery_estimate` and `dorfler_mark`
  are harvested firm (scheme §5 min-endpoint-rank). A natural c122+ follow-up: harvest the two verbs
  (the estimate verb leans on the libCEED kernel-api, already on disk; the mark verb is self-contained),
  then firm-flip this theme.
- **No `roadmap_goal` authored.** Per the finding that the loop is already homed, I did NOT author a
  `roadmap_goal` chapter for the AMR loop (it would duplicate the firm `fold_solve` home — the
  degenerate-identity smell). The two speculative L1 verbs are rough-in dep-map rows + a rough-in theme,
  the in-discipline form for "real-but-undissected referent with a live consuming home" (the consumer
  being the firm lifecycle `fold_solve` step). If the integrator/critic judges the estimate/mark verbs
  should instead be rank-0 `roadmap_goal` chapters (intended-but-not-yet-real), the pulled-by provenance
  is the lifecycle root → `fold_solve` step → these verbs; flagged for integrator judgment.
