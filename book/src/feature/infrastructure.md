---
kind: navigational-container (feature group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - feature/geometric-multigrid-preconditioner.L4
    - feature/geometric-multigrid-preconditioner.L1
    - feature/krylov-iteration.L4
    - feature/krylov-iteration.L1
    - feature/matrix-free-operator.L4
    - feature/matrix-free-operator.L1
---

# Infrastructure / shared-substrate columns

The fourth feature sub-kind, alongside the [Spine ROOT (lifecycle)](./spine-root.md),
[Driver-leaf columns](./driver-leaf.md), and [Output-product columns](./output-product.md).
An **infrastructure / shared-substrate** column is a composition-root for a feature surface
that is **driver-agnostic** — not an entry-point a user invokes directly, but a shared
substrate that *every* driver's solve composes. It is the *solve-side* analog of the
driver-agnostic [`energy-fields`](./energy-fields.L4.md) output product (a shared postprocess
all field-bearing drivers point at): here the shared surface sits under the Krylov solve
rather than over the solution field.

These columns follow the same composition-root discipline as the other sub-kinds —
inputs = config + the operator/space hierarchy; output = the infrastructure action (e.g. a
preconditioner); body = the composition of already-firm decomposed vocabulary at that level;
they link DOWN to constituent ops/combinators. They are **not** reciprocal-cross-linked to a
single producing/consuming driver (the driver-agnostic exception): a shared-substrate column
links generically to the set of drivers that compose it, and the drivers are not edited to
add an UP-link. The within-column level ordering stays **high→low (L4→L1→L0)**, the deliberate
FEATURE-SURFACE exception; columns sort **alpha-within-this-kind** in the matrix and in
`SUMMARY.md`.

Current members (alpha-within-this-kind):

- [**geometric-multigrid preconditioner**](./geometric-multigrid-preconditioner.L4.md) — the
  V-cycle preconditioner every multi-level Krylov solve (and the firm
  [`divfree_projector`](../L1/divfree_projector.md)) hangs under; the DIRECTIVE-2 grounded
  consumer-(1) that GROUNDS RE9/RE1/RE5/RE7 by composing the prolongation level-stack +
  smoother leg + diagonal-preconditioner chains by name. (firm.)
- [**krylov-iteration**](./krylov-iteration.L4.md) — the Krylov / Arnoldi **iteration spine**
  every iterative solve hangs under; the iteration-rotation parallel of the GMG column. The
  DIRECTIVE-2 item-4b grounded consumer that DISCHARGES RE2 (`L3/orthogonalize`) and RE8
  (`L3/krylov_step`, `L3/fold_solve`) by composing the L3 iteration-rotation form BY NAME via
  blocking `depends-on (composes)` edges (a genuine depends-on reachability flip). (rough-in —
  capped at partial-obstruction by its `fold_solve` / `orthogonalize` iteration-views, the
  body-lifts-loop-doesn't honesty; coupled to the roadmap_goal
  [`eigsolve-impl`](../L3/eigsolve-impl.md) constructive eigensolve consumer.)
- [**matrix-free-operator**](./matrix-free-operator.L4.md) — the matrix-free FE operator
  **backend-lowering surface** every high-order driver's assemble stage composes when the
  order-threshold `UseFullAssembly` dispatch selects partial assembly; the **assemble-side**
  infrastructure analog of the solve-side GMG column. The batch-41 "A" / DIRECTIVE-3 grounded
  consumer that firms the [`mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md) cap off
  `roadmap_goal` (composing the constructor cap + the firm L2 contraction-chain combinator by name)
  and GROUNDS the RE11 libceed-substrate sub-cohort (its L1 surface names the four firm element-local
  substrate ops `element_restrict`/`basis_apply`/`quad_point_contract`/`geom_factor_build` via
  blocking `depends-on (composes)` edges — a genuine depends-on reachability flip). (firm — the
  constructor surface is a fixed contraction chain with no loop obstruction, all blocking deps firm.)
