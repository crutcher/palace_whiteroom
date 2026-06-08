---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5).
edges:
  reference:
    - L1/build_mesh
---

# L1 — Mesh & FE-space construction

The geometric-substrate surface upstream of the FE-space sub-spine: the single-machine **mesh construction** that produces the [`Mesh`](../concepts/mesh.md) typed value every solver pipeline stands on. Where the FE-space sub-spine constructs the function space (and its hierarchy + boundary-dof sets) on a given mesh, this surface constructs the mesh itself — load → preprocess → partition (read single-rank) → a-priori refine — from the `Config`/`IoData` surface. This is a **standalone kind grouping** (NOT folded into the FE-space sub-spine): mesh construction (the geometric substrate) is a genuinely distinct kind from FE-space construction (the function space on a given mesh), and the boundary is drawn explicitly above.

Currently one member: [`build_mesh`](./build_mesh.md) (`(config: Config) → Mesh`), the a-priori half of the lifecycle-root stage-(1) mesh build; its L1>L0 forward rewrite is the [`build-mesh-construction-rotation`](../L1-L0/build-mesh-construction-rotation.md) theme, and its produced [`Mesh`](../concepts/mesh.md) value has a cross-cutting record-definition home. The MFEM-opaque adaptive-AMR refinement leaf stays obstruction-documented at the lifecycle root (not forced); the `Par*` / distributed mesh-partitioning stage is read single-rank (flag-once-skip, out of scope). The grouping stays single-member because the would-be siblings are out-of-scope / MFEM-opaque — it is not a transitional under-population (a future single-machine mesh-accessor / derived-submesh op would land here).

Chapters are listed alphabetically.
