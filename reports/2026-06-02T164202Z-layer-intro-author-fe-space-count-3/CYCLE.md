---
agent: layer-intro-author
invoked_at: 2026-06-02T16:42:02Z
scope: L1/index.md consolidated count refresh (FE-space sub-spine 2→3, L1 firm grand total 33→34) — cycle-066 D4, SOLE count-owner
status: integrated
integrated_at: 2026-06-02T194500Z
integration_commit: 062ae9e
integration_notes: "cycle-066 D4 (SOLE count-owner). L1/index.md x2: grand-total :31 L1 firm 33->34 / FE-space sub-spine 2->3 / '34 firm rows on-table'; §'Firm (FE-space sub-spine)' header :78 '— 2'->'— 3' folding essential_dofs into the sub-spine narrative (DAG fe_collection > fe_space > essential_dofs). Arithmetic exact (27 main + 4 FE-assembly + 3 FE-space = 34). index-cell anti-drift guard n/a-clean (tally from chapter ## Status lines; D1 firm dep-map row co-landed so table [34] matches tally [34]). citecheck --scan 3 ok / 0 failing. Build clean; no build-repair."
---

# CYCLE: L1 index consolidated count refresh (essential_dofs cohort)

## Summary

Cycle-066 D4 (wave 2). I am the **SOLE `book/src/L1/index.md` consolidated count-owner** this cycle.
D1 (`harvester`) lands NEW firm `book/src/L1/essential_dofs.md` (warrant=YES; `## Status: firm`); D1
owns its own dep-map row + §Vocabulary-cohort cohort bullet and DEFERS the consolidated tally to me.
D3 (lifter) and D2 (abstractor, a THEME not an L1 operator) make no L1-operator-count change.

This report refreshes ONLY the two consolidated-count surfaces I own:

1. **§Vocabulary-cohort consolidated-tally paragraph** (`book/src/L1/index.md` line 31) — L1 firm grand
   total **33 → 34**; FE-space sub-spine **2 → 3**.
2. **§"Firm (FE-space sub-spine)" subsection header + narrative** (`book/src/L1/index.md` line 78) —
   header count **2 → 3**, and fold `essential_dofs` into the sub-spine narrative as the dof-set
   producer that de-opaques the `DofSet[N]` consumed by `eliminate_essential_bc`/`eliminate_rhs`.

**Refreshed counts (every count carries chapter-`## Status` justification):**

| Cohort | Count | Source-of-truth (each chapter's on-disk `## Status` line; `essential_dofs` from D1's CYCLE.md) |
|---|---|---|
| Main cohort | 27 (unchanged) | unchanged this cycle |
| FE-assembly sub-spine | 4 (unchanged) | `fe_assemble` `firm` / `weak_form_term` `firm` / `eliminate_essential_bc` `firm` / `eliminate_rhs` `firm` |
| FE-space sub-spine | **3** (was 2) | `fe_space` `## Status: **firm (firm-on-positive-structure).**` + `fe_collection` `## Status: **firm (firm-on-positive-structure).**` + **`essential_dofs` `## Status: firm`** (D1 CYCLE.md `book/src/L1/essential_dofs.md` frontmatter `firmness: firm` + body `## Status: firm`) |
| **L1 firm grand total** | **34** (was 33) | 27 main + 4 FE-assembly + 3 FE-space = 34 |

Count discipline (the c057-meta count-owner guard): the grand total is computed by reading each linked
chapter's `## Status` line, NOT the index-table status cells. The two existing FE-space members were
read on disk (`fe_space.md` / `fe_collection.md` both `## Status: **firm (firm-on-positive-structure).**`);
`essential_dofs` is not on disk during dispatch, so its `firm` status is read from D1's CYCLE.md
(`reports/2026-06-02T164202Z-harvester-essential-dofs/CYCLE.md`: frontmatter `firmness: firm`, the
`new:book/src/L1/essential_dofs.md` body `## Status` = "`firm` — FE-space sub-spine essential-dof-set
constructor."). All four FE-assembly members read `firm` on disk (frontmatter `firmness: firm`).

## Proposed changes

### Edit 1 — §Vocabulary-cohort consolidated-tally paragraph (line 31)

```edit:book/src/L1/index.md
[old]: **Firm (27 main cohort; 33 firm grand total incl. the FE-assembly + FE-space sub-spines).** The 27 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm (`fe_assemble` c054 + `weak_form_term` c061 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), and the FE-space sub-spine adds **2** more firm (`fe_space` c064 + `fe_collection` c065 — see the §"Firm (FE-space sub-spine)" subsection), bringing the L1 firm grand total to **33** (was 32 after cycle-064: 27 main + 4 FE-assembly sub-spine + 1 FE-space sub-spine; cycle-065 D2 added the FE-space sub-spine's second firm member `fe_collection`, the upstream collection-order-schedule producer). Count discipline: the grand total is computed by reading each linked chapter's `## Status` line, not the index cells — 27 main + 4 FE-assembly + 2 FE-space = 33; equivalently the dep-map table now holds **33** `firm` rows (incl. `assemble_frequency_operator` c062, `fe_assemble` c054, `fe_space` c064, and `fe_collection` c065). All firm rows are now on-table; there is no off-table firm operator.
[new]: **Firm (27 main cohort; 34 firm grand total incl. the FE-assembly + FE-space sub-spines).** The 27 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm (`fe_assemble` c054 + `weak_form_term` c061 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), and the FE-space sub-spine adds **3** more firm (`fe_space` c064 + `fe_collection` c065 + `essential_dofs` c066 — see the §"Firm (FE-space sub-spine)" subsection), bringing the L1 firm grand total to **34** (was 33 after cycle-065: 27 main + 4 FE-assembly sub-spine + 2 FE-space sub-spine; cycle-066 D1 added the FE-space sub-spine's third firm member `essential_dofs`, the boundary-attribute→essential-true-dof-set constructor that de-opaques the `DofSet[N]` parameter of the FE-assembly BC-treatment post-compositions). Count discipline: the grand total is computed by reading each linked chapter's `## Status` line, not the index cells — 27 main + 4 FE-assembly + 3 FE-space = 34; equivalently the dep-map table now holds **34** `firm` rows (incl. `assemble_frequency_operator` c062, `fe_assemble` c054, `fe_space` c064, `fe_collection` c065, and `essential_dofs` c066). All firm rows are now on-table; there is no off-table firm operator.
```

### Edit 2 — §"Firm (FE-space sub-spine)" subsection header + narrative (line 78)

```edit:book/src/L1/index.md
[old]: **Firm (FE-space sub-spine — 2; opened cycle-064)** — the finite-element **space-construction** surface (the MFEM-equivalent FE-space substrate under every assembled-operator pipeline, in scope per CLAUDE.md mesh/FE), opened cycle-064 by the firm [`fe_space`](./fe_space.md) (cycle-064 D2) + its L1>L0 rotation [`fe-space-construction-rotation`](../L1-L0/fe-space-construction-rotation.md) (cycle-064 D3), and extended cycle-065 by its **upstream collection-order-schedule producer** [`fe_collection`](./fe_collection.md) (cycle-065 D2) + its L1>L0 rotation [`fe-collection-construction-rotation`](../L1-L0/fe-collection-construction-rotation.md) (cycle-065 D3). This sub-spine is **upstream** of the FE-assembly sub-spine: where FE-assembly folds weak-form terms into an operator over a space, this sub-spine **constructs the space itself** — the typed `(mesh, FECollection) → FiniteElementSpace[N]` domain/range object that `fe_assemble`, `weak_form_term`, `eliminate_essential_bc`, and `eliminate_rhs` (and the four solver-model operators) currently take **opaquely** as a bare typed `space` / true-dof axis `N` / `DofSet[N]` (the cycle-064 D1 opaque-parameter inventory, `reports/2026-06-02T151056Z-cross-layer-cross-cutter-fe-space-front-survey/CYCLE.md` §4). A firm `fe_space` de-opaques those parameters: it is the shared substrate the whole assembled-operator front stands on. The two members sit in producer→consumer order across the `[FECollection]` boundary: `fe_collection` is the **list-producing order schedule** `(p, dim, mg_max_levels, coarsening, family) → [FECollection]` (one `FECollection` per p-multigrid level) — NOT a `fe_space` variant axis but a self-standing schedule (D2 WARRANT=YES, on the strength of list-producing laws `fe_space` lacks: finest-to-coarsest order sequence, family-dependent `pmin` floor, `mg_max_levels` length bound, LINEAR/LOGARITHMIC policy-determines-order-step, singleton-collapse-to-one-`fe_space`-input). Its `[FECollection]` output is exactly the per-level `collection` input that `ConstructFiniteElementSpaceHierarchy` (`palace/fem/multigrid.hpp:78-126`) feeds one-per-level into [`fe_space`](./fe_space.md) constructions. So the sub-spine reads upstream→downstream as `fe_collection` (schedule the order list) ▷ per-level `fe_space` (construct each space), and downstream into the FE-assembly sub-spine.
[new]: **Firm (FE-space sub-spine — 3; opened cycle-064)** — the finite-element **space-construction** surface (the MFEM-equivalent FE-space substrate under every assembled-operator pipeline, in scope per CLAUDE.md mesh/FE), opened cycle-064 by the firm [`fe_space`](./fe_space.md) (cycle-064 D2) + its L1>L0 rotation [`fe-space-construction-rotation`](../L1-L0/fe-space-construction-rotation.md) (cycle-064 D3), extended cycle-065 by its **upstream collection-order-schedule producer** [`fe_collection`](./fe_collection.md) (cycle-065 D2) + its L1>L0 rotation [`fe-collection-construction-rotation`](../L1-L0/fe-collection-construction-rotation.md) (cycle-065 D3), and extended cycle-066 by its **boundary-condition dof-set member** [`essential_dofs`](./essential_dofs.md) (cycle-066 D1) + its L1>L0 rotation [`essential-dofs-construction-rotation`](../L1-L0/essential-dofs-construction-rotation.md) (cycle-066 D2). This sub-spine is **upstream** of the FE-assembly sub-spine: where FE-assembly folds weak-form terms into an operator over a space, this sub-spine **constructs the space itself** — and the boundary-condition dof-set on it — the typed `(mesh, FECollection) → FiniteElementSpace[N]` domain/range object plus the `DofSet[N]` that `fe_assemble`, `weak_form_term`, `eliminate_essential_bc`, and `eliminate_rhs` (and the four solver-model operators) previously took **opaquely** as a bare typed `space` / true-dof axis `N` / `DofSet[N]` (the cycle-064 D1 opaque-parameter inventory, `reports/2026-06-02T151056Z-cross-layer-cross-cutter-fe-space-front-survey/CYCLE.md` §4). The firm members de-opaque those parameters: this sub-spine is the shared substrate the whole assembled-operator front stands on. The three members sit in a small producer→consumer DAG across the `[FECollection]` and `DofSet[N]` boundaries: `fe_collection` is the **list-producing order schedule** `(p, dim, mg_max_levels, coarsening, family) → [FECollection]` (one `FECollection` per p-multigrid level) — NOT a `fe_space` variant axis but a self-standing schedule (D2 WARRANT=YES, on the strength of list-producing laws `fe_space` lacks: finest-to-coarsest order sequence, family-dependent `pmin` floor, `mg_max_levels` length bound, LINEAR/LOGARITHMIC policy-determines-order-step, singleton-collapse-to-one-`fe_space`-input); its `[FECollection]` output is exactly the per-level `collection` input that `ConstructFiniteElementSpaceHierarchy` (`palace/fem/multigrid.hpp:78-126`) feeds one-per-level into [`fe_space`](./fe_space.md) constructions. `essential_dofs` is the **boundary-condition dof-set member** `(space, bdr_attrs, bdr_attr_max) → DofSet[N]` — it constructs the essential-true-dof set *on* an already-constructed `fe_space` (the `N` true-dof axis and read-only dof structure come from `fe_space`), via a Palace-authored marker head (`mesh::AttrToMarker`) over an MFEM-opaque-tail (`GetEssentialTrueDofs`, read-as-given like `fe_space`'s dof internals). Its `DofSet[N]` output is exactly the essential-dof set that the FE-assembly BC-treatment post-compositions `eliminate_essential_bc`/`eliminate_rhs` previously consumed as a bare typed parameter with no constructor home (D1 WARRANT=YES, on the strength of marker-head laws `fe_space` lacks: wildcard saturation, empty-boundary identity, marker subset-monotonicity, and marker union-additivity as a join-semilattice homomorphism witnessed at `spaceoperator.cpp:187-205`). So the sub-spine reads as the DAG `fe_collection` (schedule the order list) ▷ per-level `fe_space` (construct each space) ▷ `essential_dofs` (mark the boundary dof-set on each space), and downstream into the FE-assembly sub-spine — `fe_space` feeding the operator domain/range and `essential_dofs` feeding the BC-elimination dof-set.
```

## Supporting evidence

- **Operators currently firm at L1 (FE-space sub-spine), by on-disk `## Status`:**
  - `book/src/L1/fe_space.md` — `## Status: **firm (firm-on-positive-structure).**` (read on disk).
  - `book/src/L1/fe_collection.md` — `## Status: **firm (firm-on-positive-structure).**` (read on disk).
  - `essential_dofs` — `## Status: firm` (from D1's CYCLE.md `new:book/src/L1/essential_dofs.md`
    body; frontmatter `firmness: firm`). Not on disk during dispatch — read from the proposed change,
    per the count-owner guard's "read the proposed `## Status` from D1's CYCLE.md" instruction.
- **FE-assembly sub-spine (unchanged at 4), by on-disk frontmatter `firmness: firm`:** `fe_assemble.md`,
  `weak_form_term.md`, `eliminate_essential_bc.md`, `eliminate_rhs.md` (all `firm`; all `## Status:
  `firm`. **Clean-gate call: PROMOTE`).
- **Cross-reference (D1 framing forwarded into the narrative):** D1's CYCLE.md §"Open questions /
  caveats" (the "Layer-intro refresh (D4 / layer-intro-author)" bullet) explicitly asks the intro
  author to add `essential_dofs` to the sub-spine narrative "as the **dof-set producer that de-opaques
  the `DofSet[N]`** parameter of `eliminate_essential_bc`/`eliminate_rhs`" and frames the sub-spine as a
  DAG `fe_collection ▷ fe_space`, `fe_space ▷ essential_dofs`. Edit 2 implements exactly that framing.

## Scope discipline (per the index-dual-registration partition)

- I own ONLY **(3) the consolidated tally + the sub-spine narrative prose** (Edit 1 + Edit 2). I did NOT
  touch D1's **(1) own dep-map row** (D1's `essential_dofs` firm dep-map table row + its rough-in→firm
  bullet conversion at `book/src/L1/index.md:89`) NOR **(2) D1's own §Vocabulary-cohort cohort bullet**.
  D2's L1-L0 theme row is likewise untouched (a theme, not an L1 operator — no L1-count change).
- Index-cell anti-drift guard (c057-meta): the dep-map status cells are derived; the consolidated tally
  in Edit 1 is recomputed from the chapter `## Status` lines (not from the cells). `essential_dofs`'
  firm dep-map row is D1's to land in the SAME cycle (D1's CYCLE.md carries it), so the table will not
  lag the chapter; my tally and D1's row land together this cycle.

## Open questions / caveats

- **Tally arithmetic is exact and self-consistent:** 27 main + 4 FE-assembly + 3 FE-space = 34, and the
  dep-map table will hold 34 firm rows once D1's `essential_dofs` firm row lands (D1 owns that row). If
  D1's row does NOT land this cycle (integration ordering), the table-vs-tally parity check at finalize
  would surface a 33-row-vs-34-tally mismatch — but D1's CYCLE.md does carry the firm row, so this is a
  co-landing, not a divergence. Flagging for the per-report integrator's ordering awareness only.
- No on-disk/record status mismatch found: all FE-space + FE-assembly chapters carry explicit `## Status`
  lines matching the cycle record; no firm-apparatus-missing chapter is being labeled firm.
- The §Vocabulary-cohort §"Deferred follow-on siblings" list (line 86+) still carries `essential_dofs`
  as a "named, NOT authored" deferred sibling under the c065 framing. That bullet is **D1's to convert**
  (it is D1's own cohort registration, NOT my consolidated tally) — I left it untouched per the
  partition. If D1's proposed changes do not also flip that deferred-sibling bullet to firm, it is a
  residual stale-bullet for the per-report integrator / a follow-up; out of my count-owner scope.
