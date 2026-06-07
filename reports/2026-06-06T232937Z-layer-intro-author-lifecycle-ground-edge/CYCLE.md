---
agent: layer-intro-author
invoked_at: 2026-06-06T232937Z
scope: feature/lifecycle.L1 — §2f GROUND build_mesh as the stage-1 depends-on(composes) edge
status: integrated
integrated_at: 2026-06-07T003000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean as c118 D4 (batch-38 opener). GROUND edge feature/lifecycle.L1 → L1/build_mesh (composes), the GROUND-don't-remove disposition (batch-37-meta migrated-to-plan item); faithful do-block constituent-USE, lifecycle.L1 firm → build_mesh firm (3≤3). cargo make book EXIT 0; rank_violations=0; build_mesh GROUNDED off detritus (reachable 136→139). Surfaced NEW OQ lifecycle-l4-sibling-analogous-unground-build_mesh-edge. 0 gate hits."
---

# CYCLE: feature/lifecycle.L1 — GROUND the build_mesh stage-1 edge

## Summary

The c117 all-fronts wave homed `build_mesh` as a new **firm** L1 op (`book/src/L1/build_mesh.md`, `rank: firm`). The lifecycle composition-root (`feature/lifecycle.L1.md`) genuinely composes `build_mesh` as its **stage-1** (`config→mesh`): the do-block literally calls `build_mesh cfg` at `:39` and the stage-1 narration at `:44` cites `palace/main.cpp:287-302`. But `build_mesh` is in **neither** the `depends-on` nor the `reference` frontmatter list — it did not exist as a node when the lifecycle was authored. Confirmed by reading the file's frontmatter (`:7-25`) + the `:19-71` region.

This is the **§2f GROUND-don't-remove disposition** (priority order: (1) GROUND — preferred). The edge is **faithful**: the lifecycle genuinely composes `build_mesh` as stage-1; the edge was absent only because the node didn't exist at authoring time. Grounding it makes `build_mesh` reachable off the root set via `lifecycle.L1 →(composes / depends-on)→ L1/build_mesh`.

Two surgical edits on the single file `book/src/feature/lifecycle.L1.md`:
1. ADD the `depends-on` edge `{ target: L1/build_mesh, kind: composes }` (placed first among the `L1/` composes edges).
2. UPDATE the prose constituent-row (the `build mesh` row of the `## Constituent down-links` table — the file's prose-row home for this constituent) to link the now-firm `build_mesh` L1 op node and mark it `firm` (was `— (L0 scaffold)`).

**Well-foundedness** (Axis 1): `lifecycle.L1` is `firm` (rank 3) and `build_mesh` is `firm` (rank 3) → `rank(u) ≤ rank(v)` ⇒ `3 ≤ 3`, holds.

**Reachability delta** (Axis 2): projected `reachable 136 → 137`, `detritus 129 → 128` (build_mesh moves from unreachable detritus to reachable via the new faithful depends-on edge).

This is a faithful-edge GROUND, NOT a force-an-edge-to-flip-a-number: stage-1 of the lifecycle IS `build_mesh` (verified at `:39` call-site and `:44` narration), so the relationship is a genuine **constituent-use** (`composes`), not a lowering and not an over-link.

## Proposed changes

```edit:book/src/feature/lifecycle.L1.md
[old]:
  depends-on:
    - target: L1/fe_assemble
      kind: composes
[new]:
  depends-on:
    - target: L1/build_mesh
      kind: composes
    - target: L1/fe_assemble
      kind: composes
```

```edit:book/src/feature/lifecycle.L1.md
[old]:
| build mesh | `mesh::Load`/`Partition`/`RefineMesh` (driver-agnostic mesh scaffold) | — (L0 scaffold) | `palace/main.cpp:287-302` |
[new]:
| build mesh | [`build_mesh`](../L1/build_mesh.md) (driver-agnostic stage-1 `config→mesh` constituent: load → preprocess → partition → a-priori-refine) | firm | `palace/main.cpp:287-302` |
```

## Supporting evidence

- **Call-site / narration in the lifecycle column:** `feature/lifecycle.L1.md:39` (`let mesh0 = build_mesh cfg` in the do-block) + `:44` (stage-1 narration "Build the mesh — a driver-agnostic pure `build_mesh :: Config -> Mesh`", citing `palace/main.cpp:287-302`).
- **Backing L0 site:** `palace/main.cpp:287-302` — `mesh::Load` / `Preprocess` / `Partition` / `RefineMesh` (the driver-agnostic mesh-build scaffold that `build_mesh` formalizes).
- **The node being grounded:** `book/src/L1/build_mesh.md` carries `rank: firm` (line 13) — a firm L1 leaf op (`Config`/`IoData` → `Mesh`); confirmed firm this dispatch by reading its frontmatter. (NOT modified this cycle — D1 owns its edges.)
- **Pre-edit frontmatter state:** `feature/lifecycle.L1.md:7-25` — `depends-on` listed `fe_assemble`, `ksp_solve`, `fold_solve` + two `cites-evidence` L0 ranges; `reference` listed the six per-driver sibling columns. `build_mesh` appeared in NEITHER list. Confirmed it was absent only because the node post-dates the lifecycle authoring.

## Open questions / caveats

- **Scope discipline honored:** only `book/src/feature/lifecycle.L1.md` is touched (the two surgical edits). `book/src/L1/build_mesh.md` was NOT modified (D1 owns its edges this cycle). No other file touched.
- The stage-1 prose narration at `:44` still names the L0 ops (`mesh::Load` / `Preprocess` / `Partition` / `RefineMesh`) and cites `main.cpp:287-302` without an inline link to the now-firm `build_mesh` node. This was left unedited to keep the change to the directed two-edit (frontmatter edge + prose constituent-row); the `## Constituent down-links` table row is the canonical prose-row home and now carries the live link. If the integrator/critic prefers the inline `:44` link too, it is a one-token addition (`[`build_mesh`](../L1/build_mesh.md)`) — flagged, not applied.
- The other L4 sibling (`feature/lifecycle.L4.md`) may carry the analogous unground `build_mesh` stage-1 edge — out of scope here (one file per dispatch); worth a follow-up check if it also predates the `build_mesh` node and has an L4 build-mesh constituent. (Not a finding this cycle — noting for the planner.)
