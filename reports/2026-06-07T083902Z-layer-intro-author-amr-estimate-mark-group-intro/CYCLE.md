---
agent: layer-intro-author
invoked_at: 2026-06-07T084500Z
scope: L1 AMR estimate/mark by-kind group-intro authoring + SUMMARY re-nest + L1/index.md dep-map header de-stale (cycle-123 D1)
status: pending
integrated_at: 2026-06-07T083902Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (D1; META was needs-revision SOLELY on the D4-before-D1 ordering coupling, fully discharged by the dispatch order — applied unchanged once D4 landed). amr-estimate-mark-intro.md navigational-container group-intro authored; 2 flat AMR verbs re-nested under the SUMMARY grouping; index.md dep-map group header de-staled. Closes OQ amr-estimate-mark-group-intro-needs-authoring. cargo make book EXIT 0; rank_violations 0; both step-5b block-conditions PASS. Batch-39 BATCH-CLOSING finalize."
---

# CYCLE: L1 — AMR estimate/mark group-intro (deferred c122 navigational hygiene)

## Summary

Closes OQ `amr-estimate-mark-group-intro-needs-authoring` — the deferred navigational hygiene
the c122 AMR wave left. Three coordinated edits:

1. **Create** `book/src/L1/amr-estimate-mark-intro.md` — the by-kind group-intro page for the
   AMR estimate/mark vocabulary sub-group (the two now-firm verbs
   [`flux_recovery_estimate`](../book/src/L1/flux_recovery_estimate.md) +
   [`dorfler_mark`](../book/src/L1/dorfler_mark.md), the estimate→mark stages of the
   `amr-estimate-mark-refine` L1>L0 theme). A `kind: navigational-container (group intro)` page
   with `reference`-only edges, following the `fe-space-intro.md` / `mesh-construction-intro.md`
   precedent (no `rank:`, alpha-listed members).
2. **Re-nest** the two FLAT `SUMMARY.md` entries (lines 245-246, the c122 build-clean fallback)
   into a nested `AMR estimate / mark` grouping under the new intro, placed after the
   `FE-space sub-spine` grouping.
3. **De-stale** the `book/src/L1/index.md` dep-map TABLE group-header (line 208)
   `**Rough-in (AMR estimate/mark vocabulary)**` → `**AMR estimate/mark vocabulary**` (both verbs
   are `firm` on disk; the "Rough-in" qualifier is stale — verb rows already read `firm`).

GATE: the group-intro page is created BEFORE SUMMARY nests it (the
`new-summary-kind-grouping-placeholder-link-duplicate-file-build-break` discipline — the new
SUMMARY link points at a freshly-created file, never an existing page as a placeholder, so
`cargo make book` stays EXIT 0 + linkcheck2 clean).

## Supporting evidence

**On-disk maturity confirmed by reading each chapter's `## Status` line (NOT the index cells):**
- `book/src/L1/flux_recovery_estimate.md` — frontmatter `rank: firm` / `status: firm` (line 2-3);
  `## Status` line: `` `firm` (AMR estimate verb; flux-channel variant axis Grad/Curl …) `` (line 250).
- `book/src/L1/dorfler_mark.md` — frontmatter `rank: firm` (line 4); `## Status` line:
  `` `firm` — the operator's structure is read directly from **positive** Palace source … `` (line 281).
Both FIRM → the dep-map TABLE header `Rough-in (…)` (L1/index.md:208) is stale; the narrative
cohort header at L1/index.md:134 already reads `Firm (AMR estimate/mark vocabulary)` (the dep-map
table header lags — the `index-table-status-cell-drifts-when-theme-file-promoted` drift class, here
on a group-HEADER rather than a status cell).

**Group-intro precedent read** (`fe-space-intro.md`, `mesh-construction-intro.md`): both are
`kind: navigational-container (group intro)` with the explanatory comment block + `edges: reference:`-only
(NO `rank:`), a one-paragraph orientation, a per-member line, and a trailing "Chapters are listed
alphabetically." The AMR intro mirrors this exactly.

**Member dataflow (for the intro orientation prose):** the two verbs are the **estimate → mark**
stages of Palace's AMR loop body (`SolveEstimateMarkRefine`, `palace/drivers/basesolver.cpp`);
`flux_recovery_estimate` (the ZZ a-posteriori estimate, `palace/linalg/errorestimator.cpp:184-268`)
produces the per-element indicator vector, and `dorfler_mark` (the bulk-marking verb,
`palace/utils/dorfler.cpp:14-171` ▷ `palace/drivers/basesolver.cpp:103-115`) selects which elements
to refine; the third stage, `refine`, is the MFEM-opaque leaf narrated in the
`amr-estimate-mark-refine` L1>L0 theme (`obstruction (opaque-library-ownership)`), NOT a fillable
L1 verb — so the grouping is correctly the **two-member estimate/mark vocabulary**, not estimate/mark/refine.

**SUMMARY placement** (`book/src/SUMMARY.md`): the L1 chapters block ends with the `FE-space sub-spine`
grouping (lines 239-244); the two AMR verbs sit FLAT at 245-246 immediately after. The new grouping
nests them under the intro in the same position (after FE-space sub-spine, last in the L1 Part before
the `# L1 > L0 — Lowering` Part at line 248).

## Proposed changes

```edit:book/src/L1/amr-estimate-mark-intro.md
[new file]:
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
```

```edit:book/src/SUMMARY.md
[old]:
- [FE-space sub-spine](./L1/fe-space-intro.md)
  - [essential_dofs](./L1/essential_dofs.md)
  - [fe_collection](./L1/fe_collection.md)
  - [fe_space](./L1/fe_space.md)
  - [fe_space_hierarchy](./L1/fe_space_hierarchy.md)
  - [interpolator](./L1/interpolator.md)
- [dorfler_mark](./L1/dorfler_mark.md)
- [flux_recovery_estimate](./L1/flux_recovery_estimate.md)
[new]:
- [FE-space sub-spine](./L1/fe-space-intro.md)
  - [essential_dofs](./L1/essential_dofs.md)
  - [fe_collection](./L1/fe_collection.md)
  - [fe_space](./L1/fe_space.md)
  - [fe_space_hierarchy](./L1/fe_space_hierarchy.md)
  - [interpolator](./L1/interpolator.md)
- [AMR estimate / mark vocabulary](./L1/amr-estimate-mark-intro.md)
  - [dorfler_mark](./L1/dorfler_mark.md)
  - [flux_recovery_estimate](./L1/flux_recovery_estimate.md)
```

```edit:book/src/L1/index.md
[old]:
| **Rough-in (AMR estimate/mark vocabulary)** | | | |
[new]:
| **AMR estimate/mark vocabulary** | | | |
```

## Open questions / caveats

- **`concepts/RefinementData.md` is created by the co-dispatched D4, not this dispatch.** The AMR
  group-intro I author references `../concepts/RefinementData.md` (in the closing paragraph). The
  cycle-123 plan dispatches D4 (`layer-intro-author`, `RefinementData` record-definition concept page)
  in the SAME wave; per the plan's deliverable-presence verification (D4 row), that page is being
  created this cycle and wired into `SUMMARY.md` under the `concepts/` Part by D4. The reference link
  in the intro therefore resolves on the landed tree. **Integrator coupling note:** if D4 does NOT
  land this cycle (e.g. dropped at repair), the single `../concepts/RefinementData.md` link in the
  intro's last paragraph must be defanged to plain text or the sentence dropped, to keep `linkcheck2`
  clean — flagging so the integrator can sequence (apply D4 before, or defang if absent). This is the
  only cross-dispatch link dependency in my proposed changes.
- **Shared-file coupling on `book/src/SUMMARY.md` (flagged for the integrator).** D1 (this dispatch)
  edits the L1-chapters block (the FE-space sub-spine → AMR fallback region, lines ~239-246); D2 edits
  the `# Feature surfaces` Part region (~line 54, the Infrastructure grouping); D4 edits the
  `# Concept library` Part region (the `concepts/` block). The three SUMMARY touches are in **disjoint
  regions** with distinct anchor text — my `[old]` anchor block is the FE-space-sub-spine-through-flat-AMR
  span, which neither D2's feature-Part anchor nor D4's concepts-Part anchor overlaps. Parallel-safe by
  the per-report on-disk re-read; no consolidated-tally / shared-count situation (each dispatch owns its
  own distinct SUMMARY region).
- **The narrative cohort header (L1/index.md:134) already reads "Firm"; only the dep-map TABLE header
  (L1/index.md:208) was stale.** These are two separate headers (§Vocabulary-cohort narrative vs the
  dep-map table grouping). I de-stale only the table header — the narrative header was already correct
  on disk (landed firm by the c122 AMR wave). The verb ROWS (209-210) already read `firm` in their
  status cells; only the GROUP header carried the stale "Rough-in" qualifier. No tally to update (the
  AMR cohort carries no consolidated running count per the L1/index.md:134 note — its members are an
  AMR-vocabulary group, distinct from the 43-member L1 firm grand total).
- **No new operator algebra / no claims authored.** The group-intro is purely navigational
  (`kind: navigational-container`, `reference`-only edges, no `rank:`) — it composes/indexes the two
  already-firm verbs, restating one-line semantics only (matching the precedent group intros). The
  citation-validity / surface-or-evidence / rotation-quality / variant-axis critic checks no-op on a
  navigational container.
