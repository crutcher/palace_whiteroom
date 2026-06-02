---
agent: layer-intro-author
invoked_at: 2026-06-02T160332Z
scope: L1/index.md FE-space sub-spine consolidated count refresh (count-owner, cycle-065 D4 wave-2)
status: integrated
integrated_at: 2026-06-02T190000Z
integration_commit: f9084dcc9677092da2fcbba34432d13422771d41
integration_notes: "Applied cycle-065 (D4, wave-2 count-owner). book/src/L1/index.md x2: §Vocabulary-cohort grand-total 32->33 (27 main + 4 FE-assembly + 2 FE-space); FE-space sub-spine subsection header 1->2 (fe_collection folded into the sub-spine narrative as the upstream collection-order-schedule producer). Build-relevant; count-owner contingency on D2 landing fe_collection firm SATISFIED (verified on-disk). No gate hits; 0 new OQs."
---

# CYCLE: L1 index — FE-space sub-spine count + cohort-header refresh

## Summary

I am the SOLE `book/src/L1/index.md` consolidated count-owner for cycle-065. This report
refreshes ONLY the two count-bearing surfaces of `book/src/L1/index.md`:

1. The §Vocabulary-cohort **consolidated grand-total prose** (the `Firm (27 main cohort; … grand
   total …)` paragraph) — L1 firm grand total **32 → 33**.
2. The §Vocabulary-cohort **FE-space sub-spine subsection header + narrative** — sub-spine count
   **1 → 2**, folding `fe_collection` into the sub-spine narrative as the upstream order-schedule
   producer that feeds collection-lists into the multigrid `fe_space` constructions.

**Count arithmetic (every count carries chapter-`## Status` justification, NOT index-cell reading):**

| Cohort | Count | Source of each firm count |
|---|---|---|
| main cohort | 27 (unchanged) | the 27 listed firm bullets, each a firm `## Status` chapter |
| FE-assembly sub-spine | 4 (unchanged) | `fe_assemble` c054, `weak_form_term` c061, `eliminate_essential_bc` c055, `eliminate_rhs` c055 |
| FE-space sub-spine | **2** (was 1) | `fe_space` c064 (firm on disk) + `fe_collection` c065 (D2 CYCLE.md proposes `## Status: firm (firm-on-positive-structure)`) |
| **L1 firm grand total** | **33** (was 32) | 27 + 4 + 2 = 33 |

**Count discipline (c057-meta count-owner guard).** The firm count is computed by reading each
linked chapter's `## Status` line, NOT the index-table status cells. The +1 is
`fe_collection` (the only NEW L1 operator landing this cycle): D2's report
(`reports/2026-06-02T160332Z-harvester-fe-collection/CYCLE.md`) proposes
`book/src/L1/fe_collection.md` with frontmatter `status: firm` and a `## Status` line reading
`**firm (firm-on-positive-structure).**` — so `fe_collection` lands firm and is +1 to both the
FE-space sub-spine and the grand total. The other two cycle-065 L1-touching landings do NOT change
the operator count: D1 (lifter) re-anchored 4 existing firm entries to `fe_space` (no new entry);
D3 (abstractor) authored the L1>L0 THEME `fe-collection-construction-rotation` (a lowering theme,
not an L1 operator). The new chapter is not on disk during dispatch, so the firm `## Status` is read
from D2's proposed-changes block per the count-owner guard.

**fe_collection cohort-narrative placement.** It is folded into the FE-space sub-spine narrative as
the **upstream collection-schedule producer**: `fe_collection` schedules the `[FECollection]` list
(one per p-multigrid level) that `ConstructFiniteElementSpaceHierarchy` feeds one-per-level into
`fe_space` constructions — a producer→consumer relation across the `[FECollection]` boundary, NOT a
`fe_space` variant axis (D2's WARRANT=YES framing). It sits upstream of `fe_space`, which is in turn
upstream of the FE-assembly sub-spine.

## Discipline / scope boundary

I own ONLY the consolidated tally + the FE-space sub-spine narrative prose. I do NOT touch:
- D2's own dep-map table row for `fe_collection` (D2 owns + emits it).
- D2's own §Vocabulary-cohort `fe_collection` cohort bullet (the `[`fe_collection`](./fe_collection.md) **is now FIRM** *(cycle-065 D2)*…` bullet — D2 owns it; D2's edit replaces the old deferred-sibling plain-text bullet).
- D3's L1>L0 theme row.
- The deferred-follow-on-sibling list and its other entries (`essential_dofs`, `fe_space_hierarchy`, etc.) — only the now-promoted `fe_collection` deferred bullet is D2's to replace; I leave the rest.

The two edits below are anchor-distinct from every co-dispatched producer's edits (they touch the
consolidated grand-total prose at line 31 and the sub-spine header/narrative at line 78; D2 touches
the table rows + the cohort-bullet list + the deferred-sibling bullet + SUMMARY.md).

## Proposed changes

```edit:book/src/L1/index.md
[old]: **Firm (27 main cohort; 32 firm grand total incl. the FE-assembly + FE-space sub-spines).** The 27 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm (`fe_assemble` c054 + `weak_form_term` c061 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), and the FE-space sub-spine adds **1** more firm (`fe_space` c064 — see the §"Firm (FE-space sub-spine)" subsection), bringing the L1 firm grand total to **32** (was 31 after cycle-062: 27 main + 4 FE-assembly sub-spine; cycle-064 D2 opened the FE-space sub-spine with its first firm member `fe_space`). Count discipline: the grand total is computed by reading each linked chapter's `## Status` line, not the index cells — 27 main + 4 FE-assembly + 1 FE-space = 32; equivalently the dep-map table now holds **32** `firm` rows (incl. `assemble_frequency_operator` c062, `fe_assemble` c054, and `fe_space` c064). All firm rows are now on-table; there is no off-table firm operator.
[new]: **Firm (27 main cohort; 33 firm grand total incl. the FE-assembly + FE-space sub-spines).** The 27 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm (`fe_assemble` c054 + `weak_form_term` c061 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), and the FE-space sub-spine adds **2** more firm (`fe_space` c064 + `fe_collection` c065 — see the §"Firm (FE-space sub-spine)" subsection), bringing the L1 firm grand total to **33** (was 32 after cycle-064: 27 main + 4 FE-assembly sub-spine + 1 FE-space sub-spine; cycle-065 D2 added the FE-space sub-spine's second firm member `fe_collection`, the upstream collection-order-schedule producer). Count discipline: the grand total is computed by reading each linked chapter's `## Status` line, not the index cells — 27 main + 4 FE-assembly + 2 FE-space = 33; equivalently the dep-map table now holds **33** `firm` rows (incl. `assemble_frequency_operator` c062, `fe_assemble` c054, `fe_space` c064, and `fe_collection` c065). All firm rows are now on-table; there is no off-table firm operator.
```

```edit:book/src/L1/index.md
[old]: **Firm (FE-space sub-spine — 1; opened cycle-064)** — the finite-element **space-construction** surface (the MFEM-equivalent FE-space substrate under every assembled-operator pipeline, in scope per CLAUDE.md mesh/FE), opened this cycle by the firm [`fe_space`](./fe_space.md) (cycle-064 D2) + its L1>L0 rotation [`fe-space-construction-rotation`](../L1-L0/fe-space-construction-rotation.md) (cycle-064 D3). This sub-spine is **upstream** of the FE-assembly sub-spine: where FE-assembly folds weak-form terms into an operator over a space, this sub-spine **constructs the space itself** — the typed `(mesh, FECollection) → FiniteElementSpace[N]` domain/range object that `fe_assemble`, `weak_form_term`, `eliminate_essential_bc`, and `eliminate_rhs` (and the four solver-model operators) currently take **opaquely** as a bare typed `space` / true-dof axis `N` / `DofSet[N]` (the cycle-064 D1 opaque-parameter inventory, `reports/2026-06-02T151056Z-cross-layer-cross-cutter-fe-space-front-survey/CYCLE.md` §4). A firm `fe_space` de-opaques those parameters: it is the shared substrate the whole assembled-operator front stands on.
[new]: **Firm (FE-space sub-spine — 2; opened cycle-064)** — the finite-element **space-construction** surface (the MFEM-equivalent FE-space substrate under every assembled-operator pipeline, in scope per CLAUDE.md mesh/FE), opened cycle-064 by the firm [`fe_space`](./fe_space.md) (cycle-064 D2) + its L1>L0 rotation [`fe-space-construction-rotation`](../L1-L0/fe-space-construction-rotation.md) (cycle-064 D3), and extended cycle-065 by its **upstream collection-order-schedule producer** [`fe_collection`](./fe_collection.md) (cycle-065 D2) + its L1>L0 rotation [`fe-collection-construction-rotation`](../L1-L0/fe-collection-construction-rotation.md) (cycle-065 D3). This sub-spine is **upstream** of the FE-assembly sub-spine: where FE-assembly folds weak-form terms into an operator over a space, this sub-spine **constructs the space itself** — the typed `(mesh, FECollection) → FiniteElementSpace[N]` domain/range object that `fe_assemble`, `weak_form_term`, `eliminate_essential_bc`, and `eliminate_rhs` (and the four solver-model operators) currently take **opaquely** as a bare typed `space` / true-dof axis `N` / `DofSet[N]` (the cycle-064 D1 opaque-parameter inventory, `reports/2026-06-02T151056Z-cross-layer-cross-cutter-fe-space-front-survey/CYCLE.md` §4). A firm `fe_space` de-opaques those parameters: it is the shared substrate the whole assembled-operator front stands on. The two members sit in producer→consumer order across the `[FECollection]` boundary: `fe_collection` is the **list-producing order schedule** `(p, dim, mg_max_levels, coarsening, family) → [FECollection]` (one `FECollection` per p-multigrid level) — NOT a `fe_space` variant axis but a self-standing schedule (D2 WARRANT=YES, on the strength of list-producing laws `fe_space` lacks: finest-to-coarsest order sequence, family-dependent `pmin` floor, `mg_max_levels` length bound, LINEAR/LOGARITHMIC policy-determines-order-step, singleton-collapse-to-one-`fe_space`-input). Its `[FECollection]` output is exactly the per-level `collection` input that `ConstructFiniteElementSpaceHierarchy` (`palace/fem/multigrid.hpp:78-126`) feeds one-per-level into [`fe_space`](./fe_space.md) constructions. So the sub-spine reads upstream→downstream as `fe_collection` (schedule the order list) ▷ per-level `fe_space` (construct each space), and downstream into the FE-assembly sub-spine.
```

## Supporting evidence

- **Operators currently firm at the FE-space sub-spine (count = 2):**
  - `fe_space` (slug `fe_space`) — firm on disk, cycle-064; `book/src/L1/fe_space.md`. Confirmed firm via its dep-map row (`book/src/L1/index.md:137`, status cell `firm`) and the existing sub-spine subsection prose.
  - `fe_collection` (slug `fe_collection`) — D2's proposed `book/src/L1/fe_collection.md` carries frontmatter `status: firm` and `## Status` line `**firm (firm-on-positive-structure).**` (`reports/2026-06-02T160332Z-harvester-fe-collection/CYCLE.md`, the `new:book/src/L1/fe_collection.md` block, lines `status: firm` + the `## Status` section). Read from the proposed-changes block per the count-owner guard (chapter not yet on disk during dispatch).
- **FE-assembly sub-spine stays 4** — `fe_assemble` (c054), `weak_form_term` (c061), `eliminate_essential_bc` (c055), `eliminate_rhs` (c055), each a firm `## Status` chapter; no cycle-065 landing touches it.
- **Main cohort stays 27** — no cycle-065 landing adds a main-cohort operator.
- **Grand total 27 + 4 + 2 = 33.**
- **Co-dispatched landings (cross-check the +1 is the only count change):**
  - D2 (harvester) — NEW firm `fe_collection` → +1 (the only operator-count change).
  - D1 (lifter) — re-anchored 4 existing firm entries to `fe_space`; NO new entry → 0.
  - D3 (abstractor) — NEW firm L1>L0 theme `fe-collection-construction-rotation`; a THEME, not an L1 operator → 0 to the L1 operator count.

## Open questions / caveats

- **fe_collection `## Status` read from D2's proposed-changes block, not from disk** — per the
  count-owner guard the chapter is not on disk during dispatch. If D2's `fe_collection.md` lands at a
  status OTHER than firm (e.g. the critic/repairer downgrades it), integrator-finalize must reconcile
  the FE-space sub-spine header back to `— 1` and the grand total back to `32`. As proposed, D2 lands
  firm, so the counts above stand.
- **Index-table status cells not consulted for the count** (c057-meta guard) — the grand total and
  sub-spine count are derived from each chapter's `## Status` line, not the dep-map table cells. The
  `fe_collection` table row + its `firm` cell are D2's to emit; this report does not read or own them.
  Because D2 flips no existing `## Status` (it ADDS a new firm chapter), there is no status-flip /
  index-cell anti-drift coupling owed here beyond the consolidated tally I own.
- **Stale `:22-75` corrected to `:22-73` is D2's edit, not mine** — D2's cohort-bullet edit replaces
  the old deferred-sibling plain-text `fe_collection` bullet (which cited `multigrid.hpp:22-75`) with
  the firm bullet citing the verified `:22-73`. I do not touch that bullet; flagged here only so the
  integrator sees the two edits (D2's bullet replacement + my header/grand-total refresh) are
  complementary, not conflicting.
- **No deferred-sibling-list edit by me** — `fe_collection` graduates out of the §"Deferred follow-on
  siblings" list; D2's edit removes/replaces its bullet there. The remaining deferred siblings
  (`essential_dofs`, `fe_space_hierarchy`, `BuildDiscreteInterpolator`, `BuildProlongationAtLevel`)
  are untouched.
