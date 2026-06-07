---
agent: layer-intro-author
invoked_at: 2026-06-07T022759Z
scope: feature/lifecycle.L4 — §2f GROUND the faithful build_mesh stage-1 composes edge (L4 sibling of c118 D4)
status: pending
integrated_at: 2026-06-07T034500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "D1 cycle-119. Applied clean (staging row D1, status applied). §2f GROUND edge feature/lifecycle.L4 →depends-on(composes)→ L1/build_mesh added (3 surgical edits on book/src/feature/lifecycle.L4.md). Honest-typing of the L4 lifecycle sibling — build_mesh ALREADY reachable via lifecycle.L1→build_mesh (c118 D4); reachable HELD at 139 (no flip). well-foundedness firm(3)→firm(3) HOLDS. cargo make book EXIT 0, no build-repair. Step-5b rank_violations=0 HELD, no newly-orphaned node. OQ lifecycle-l4-sibling-analogous-unground-build_mesh-edge RESOLVED-by-landing (producer self-appended the RESOLVED note; closure is meta-phase authority)."
---

# CYCLE: feature/lifecycle.L4 — GROUND the build_mesh stage-1 `depends-on` edge

## Summary

The §2f GROUND disposition (CLAUDE.md / `METHODOLOGY-GRADED-STACK.md` §2f; `.claude/agents/layer-intro-author.md` §(g)), L4 sibling of cycle-118's D4 (which grounded the analogous edge on `feature/lifecycle.L1`). The `feature/lifecycle.L4` spine-ROOT column genuinely **composes** `build_mesh` as its stage-1 (`config → mesh`) — it is named in the do-block (`mesh0 = build_mesh cfg`), the stage-1 narration, the `lifecycle = … ∘ build_mesh` lowering line, and the down-link table — but the constituent edge was **absent from the frontmatter `edges` block** because `build_mesh` did not exist as a graded-stack node when this column was authored (it landed as a firm L1 node only at/around c118 D6). This is a textbook **GROUND** (faithful, citation-grounded, honestly-classified `depends-on`/`composes` edge), NOT a forced reachability-manufacture: `build_mesh` is **already reachable** via `feature/lifecycle.L1 → L1/build_mesh` (c118 D4), so this is honest-typing of the L4 sibling and **reachable HOLDS at 139** (no flip).

Faithfulness confirmed (the central discipline): the L4 lifecycle does NOT abstract mesh construction away — it composes `build_mesh` as a literal driver-agnostic stage, citing the same backing `palace/main.cpp:287-302`. The edge is faithful, so the edge is added (not declined-as-finding).

Well-foundedness: `lifecycle.L4` is `rank: firm` (3); `build_mesh` is `rank: firm` (3). The new edge `lifecycle.L4 →depends-on→ build_mesh` satisfies `rank(u)=3 ≤ rank(v)=3`. HOLDS at firm/firm.

Surgical: ONE file (`book/src/feature/lifecycle.L4.md`). `book/src/L1/build_mesh.md` NOT touched.

## Proposed changes

```edit:book/src/feature/lifecycle.L4.md
[old]:
  depends-on:
    - target: L4/fold_solve
      kind: composes
    - target: palace/main.cpp:158-328
[new]:
  depends-on:
    - target: L1/build_mesh
      kind: composes               # stage-1: config -> mesh scaffold (mesh::Load/Preprocess/Partition/RefineMesh)
    - target: L4/fold_solve
      kind: composes
    - target: palace/main.cpp:158-328
```

```edit:book/src/feature/lifecycle.L4.md
[old]:
1. **Build the mesh (driver-agnostic scaffold).** `build_mesh cfg` loads, preprocesses, partitions, and a-priori-refines the mesh sequence — the `readonly` construction stratum every driver consumes. L0: `mesh::Load` / `Preprocess` / `Partition` / `RefineMesh` (`palace/main.cpp:287-302`).
[new]:
1. **Build the mesh (driver-agnostic scaffold).** [`build_mesh`](../L1/build_mesh.md) `cfg` loads, preprocesses, partitions, and a-priori-refines the mesh sequence — the `readonly` construction stratum every driver consumes (the `Mesh` record it produces is [`concepts/mesh`](../concepts/mesh.md)). L0: `mesh::Load` / `Preprocess` / `Partition` / `RefineMesh` (`palace/main.cpp:287-302`).
```

```edit:book/src/feature/lifecycle.L4.md
[old]:
| build mesh | driver-agnostic mesh scaffold (`mesh::Load`/`Partition`/`RefineMesh`) | — (L0 scaffold) | `palace/main.cpp:287-302` |
[new]:
| build mesh | [`build_mesh`](../L1/build_mesh.md) (driver-agnostic stage-1 `config→mesh` constituent: load → preprocess → partition → a-priori-refine) | firm | `palace/main.cpp:287-302` |
```

## Supporting evidence

- **Edge absent confirmation.** `grep -n "build_mesh" book/src/feature/lifecycle.L4.md` (pre-edit) returned only prose mentions (do-block `:39`, stage-1 narration `:46`, inputs `:54`, lowering line `:61`) — NONE in the frontmatter `edges` block (lines 7–24). Confirmed absent from both `depends-on` and `reference`.
- **Faithful composition.** lifecycle.L4 `:39` (`let mesh0 = build_mesh cfg`), `:46` (stage-1 "Build the mesh (driver-agnostic scaffold). `build_mesh cfg` loads, preprocesses, partitions, and a-priori-refines…"), `:61` (`lifecycle = fold_solve (dispatch (problem_type cfg)) ∘ build_mesh`), and the down-link table `:67` all compose mesh construction as stage-1. The L4 column does NOT abstract it differently — it is the same driver-agnostic scaffold the L1 sibling composes.
- **L0 backing verified on disk (palace-codemap `read_range palace/main.cpp:285-303`).** The mesh-build block: `mesh::Load(iodata, world_comm)` (`:287`), `solver->Preprocess(iodata, smesh, world_comm)` (`:288`), `mesh::Partition(...)` (`:290`), `mesh::RefineMesh(iodata, mfem_mesh)` (`:291`). The cited `palace/main.cpp:287-302` range is exact for the driver-agnostic mesh scaffold.
- **`build_mesh` is firm (rank 3).** `book/src/L1/build_mesh.md` frontmatter `rank: firm` (`:13`); `## Status` (`:177-187`): "**firm (firm-on-positive-structure).**" — read from the on-disk `## Status` line, NOT the index cell.
- **`lifecycle.L4` is firm (rank 3).** frontmatter `rank: firm` (`:6`); `## Status` (`:73-79`) `firm`.
- **Canonical homes.** `book/src/L1/build_mesh.md` and `book/src/concepts/mesh.md` both confirmed present on disk (the `Mesh` record was promoted to `concepts/mesh.md` at c118 D6). No stale in-chapter location re-pointed.
- **Precedent.** c118 D4 (`feature/lifecycle.L1 → L1/build_mesh`, identical `composes` shape + identical `## Constituent down-links` `build_mesh` row); `energy-fields.L4 → L1/participation_ratio` (the §2f GROUND of an already-reachable node = honest-typing, not a reachability flip).

## Linter delta (projected)

- **Reachability GC: reachable HELD at 139.** `build_mesh` was already reachable via `feature/lifecycle.L1 →composes→ L1/build_mesh` (c118 D4). This dispatch adds a SECOND inbound `depends-on` from the L4 sibling — honest-typing of an edge that was always semantically present, NOT a new reachability rescue. No node flips live; no garbage cleared. Reachable count unchanged.
- **Rank/well-foundedness linter: clean.** New edge `lifecycle.L4 (firm,3) →depends-on→ build_mesh (firm,3)`: `rank(u) ≤ rank(v)` holds (3 ≤ 3). No new violation; no baseline-exception needed.
- After integration, `--show-inbound` on `L1/build_mesh` should list `feature/lifecycle.L4` alongside the existing `feature/lifecycle.L1` inbound edge.

## Open questions / caveats

- None blocking. The OQ that motivated this dispatch — `lifecycle-l4-sibling-analogous-unground-build_mesh-edge` (raised by c118 D4) — is **RESOLVED** by this dispatch (the L4 sibling edge is now grounded). The integrator may mark it closed.
- Drive-by (not in scope, NOT edited): the down-link table's adjacent rows label the per-driver sibling-column entries `firm / firm / firm / rough-in` and `firm`/`firm` etc. — these are `reference`-typed sibling cross-links (per the spine-ROOT OWN-COMPOSITION rule), correctly NOT `depends-on` edges; no action. The `fold_solve` stage-3 row remains correctly `depends-on`/`composes` (already in frontmatter).
