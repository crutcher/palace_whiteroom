---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/essential_dofs
    - L1/fe_collection
    - L1/fe_space
    - L1/fe_space_hierarchy
---

# L1 — FE-space sub-spine

The finite-element **space-construction** surface — the shared substrate every assembled-operator pipeline stands on, upstream of the FE-assembly sub-spine. Where FE-assembly folds weak-form terms into an operator over a space, this sub-spine constructs the space itself and the boundary-condition dof-set on it. The four members form a small producer→consumer DAG: `fe_collection` schedules the finest-to-coarsest `[FECollection]` p-multigrid order list (`(p, dim, mg_max_levels, coarsening, family) → [FECollection]`); `fe_space` constructs each typed `(mesh, FECollection) → FiniteElementSpace[N]` (de-Rham family variant axis H1/H(curl)/H(div)/L2); `essential_dofs` marks the essential-true-dof set `(space, bdr_attrs, bdr_attr_max) → DofSet[N]` on a constructed space; and `fe_space_hierarchy` folds `AddLevel` over per-level `fe_space` constructions to build the p-multigrid `FiniteElementSpaceHierarchy` (`[Mesh] → [FECollection] → Config → FiniteElementSpaceHierarchy`) — the combinator whose base case is one `fe_space` call.

These de-opaque the bare typed `space` / `N` / `DofSet[N]` parameters that `fe_assemble`, `weak_form_term`, `eliminate_essential_bc`, and `eliminate_rhs` previously took opaquely. The dof-numbering / ordering / conformity / prolongation-restriction internals are MFEM-owned-read-as-given (no `dof_map` mirror — that would be the identity-in-named-terms smell).

Chapters are listed alphabetically.
