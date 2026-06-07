---
# Lowering theme. Per graded-stack scheme §5: rank = min(endpoint ranks). The two
# constructive L1 endpoints (flux_recovery_estimate / dorfler_mark) are BOTH harvested
# firm (rank 3) as of cycle-122 (flux_recovery_estimate D1, dorfler_mark D2); the refine
# endpoint is a permanent opaque-library obstruction leaf that does NOT gate promotion
# (a documented boundary, not an unfilled body — see ## Status). So the theme firm-flips
# rough-in → firm: rank = min(firm, firm) = firm.
rank: firm
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

`firm` — the structural three-way decomposition (estimate / mark / refine) is positively anchored
at L0, and the two constructive lowering endpoints are now **both harvested firm L1 vocabulary**
([`flux_recovery_estimate`](../L1/flux_recovery_estimate.md), cycle-122 D1, and
[`dorfler_mark`](../L1/dorfler_mark.md), cycle-122 D2 — both live on-disk firm chapters, no longer the
plain-text forward-references of the original rough-in authoring). The theme firm-flipped
rough-in → `firm` per its stated gate (well-foundedness: a lowering theme is at most as
resolved as its least-resolved endpoint, scheme §5 — `rank = min(firm, firm) = firm`). The **refine** leg is a permanent
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

- [`flux_recovery_estimate`](../L1/flux_recovery_estimate.md) `:: Estimator -> Tensor[(D: n_dof)] -> Tensor[(E: n_elem)]` *(firm L1
  op, cycle-122 D1)* — the ZZ
  flux-recovery estimate verb. Recovers a *smooth* flux by projecting the
  *discontinuous* material flux onto a smooth FE space, then returns the per-element L2 norm of the
  difference (the ZZ a-posteriori indicator).
- [`dorfler_mark`](../L1/dorfler_mark.md) `:: Real -> Tensor[(E: n_elem)] -> IndexSet[E]` *(firm L1 op, cycle-122 D2)* — the Dörfler (bulk) marking verb.
  Returns the *smallest* element index set whose summed squared-error covers at
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

## L1 operators (harvested firm, cycle-122)

- [`flux_recovery_estimate`](../L1/flux_recovery_estimate.md) — the ZZ flux-recovery a-posteriori error estimate verb (firm, cycle-122 D1).
- [`dorfler_mark`](../L1/dorfler_mark.md) — the Dörfler bulk-marking verb (smallest index set covering θ of total squared error; firm, cycle-122 D2).

Both endpoints are now harvested firm; the theme firm-flipped this cycle (see ## Status). (The `refine`
leaf is NOT proposed as a fillable operator — it is the MFEM-opaque obstruction sub-leaf, the AMR
analogue of `triangular-solve-obstruction`.)

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

## Status: firm
