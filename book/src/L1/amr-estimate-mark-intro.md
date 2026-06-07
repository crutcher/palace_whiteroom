---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5).
edges:
  reference:
    - L1/dorfler_mark
    - L1/flux_recovery_estimate
---

# L1 — AMR estimate / mark vocabulary

The single-machine **adaptive-mesh-refinement** estimate→mark vocabulary — the two pure-functional
verbs that drive Palace's `estimate ▷ mark ▷ refine` adaptation loop body
(`SolveEstimateMarkRefine`, `palace/drivers/basesolver.cpp`). Both are **driver-agnostic** (they
operate only on the per-element scalar indicator vector, with no knowledge of the physics that
produced it), so they live here as their own kind grouping rather than under any single solver
pipeline. AMR is now in active scope as the DIRECTIVE-2 grounded consumer-(2); the distributed
Dörfler bracket-bisection / cross-rank reconciliation is read single-rank (DIRECTIVE-1 deferred
future-direction note, not lifted).

The two members are the loop's **first two stages**:

- [`flux_recovery_estimate`](./flux_recovery_estimate.md) (`FluxEstimator → Tensor[N] → Tensor[E]`)
  — the **estimate** stage: the Zienkiewicz–Zhu a-posteriori error estimate. It recovers the smooth
  flux `G = M⁻¹·Flux·F` by L2 projection of the discontinuous material flux (`εE` for the Grad
  channel, `μ⁻¹B` for the Curl channel) onto a conforming FE space, and returns the per-element
  squared L2 difference `η²_K = ‖flux(F)−G‖²_K` — one entry per mesh element.
- [`dorfler_mark`](./dorfler_mark.md) (`Real → Tensor[N] → IndexSet[N]`) — the **mark** stage: the
  Dörfler bulk-marking verb. Given the per-element indicator vector and the bulk fraction `θ`, it
  returns the smallest element index set whose summed squared error covers at least fraction `θ` of
  the total — `arg min |S| such that Σ_{i∈S} e_i² ≥ θ · Σ_i e_i²`.

The dataflow is estimate ▷ mark: `flux_recovery_estimate` produces the indicator vector that
`dorfler_mark` consumes (a `reference`/dataflow edge between siblings, NOT a `depends-on` — the
marker is agnostic to how the indicators were produced). The third loop stage, `refine`, is the
**MFEM-opaque** mesh-subdivision leaf (`obstruction (opaque-library-ownership)`) narrated in the
[`amr-estimate-mark-refine`](../L1-L0/amr-estimate-mark-refine.md) L1>L0 theme — it is not a
fillable L1 verb, so the grouping is the two-member estimate/mark vocabulary, not estimate/mark/refine.
The shared AMR config record `RefinementData` (the `refinement.*` IoData surface; `θ ←
update_fraction`, `palace/utils/configfile.hpp:97-119`) has its cross-cutting record-definition home
in [`concepts/RefinementData`](../concepts/RefinementData.md).

Chapters are listed alphabetically.
