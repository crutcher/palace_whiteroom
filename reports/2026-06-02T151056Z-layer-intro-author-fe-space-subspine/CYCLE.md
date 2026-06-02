---
agent: layer-intro-author
invoked_at: 2026-06-02T15:16:45Z
scope: L1 index — FE-space sub-spine framing + consolidated firm count-owner (cycle-064 D4, wave-2)
status: integrated
integrated_at: 2026-06-02T180000Z
integration_commit: PLACEHOLDER_SHA_CYCLE_064
integration_notes: |
  cycle-064 D4, applied clean by integrator-per-report (STAGING row 4, LAST), finalized by integrator-finalize.
  L1/index.md FE-space sub-spine front-shell + consolidated count: (Edit 1) §Vocabulary-cohort grand-total
  count line 31→32; (Edit 2) NEW "Firm (FE-space sub-spine — 1; opened cycle-064)" subsection, the
  authoritative cohort home for `fe_space` (it CONSTRUCTS the space; FE-assembly FOLDS over it — distinct
  vocabulary fronts). Verified: FE-assembly sub-spine STAYS 4, FE-space sub-spine is 1, grand total 32 =
  27 main + 4 FE-assembly + 1 FE-space, NO duplicate `fe_space` cohort prose bullet. The 2 co-landing
  live links (./fe_space.md + ../L1-L0/fe-space-construction-rotation.md) both resolve.
  retroactive-budget global = 0.
---

# CYCLE: L1 intro — FE-space sub-spine framing + consolidated count

## Summary

Cycle-064 opened the **FE-space / mesh-construction front** at L1: D2 lands the firm
`book/src/L1/fe_space.md` (the `(mesh, FECollection) → FiniteElementSpace[N]` construction; de-Rham
family variant axis) and D3 lands the firm `book/src/L1-L0/fe-space-construction-rotation.md`. As the
sole consolidated count-owner + front-shell author this cycle, I:

1. **Establish the FE-space sub-spine framing** — a new §Vocabulary-cohort subsection in
   `book/src/L1/index.md` analogous to the existing FE-assembly sub-spine subsection. It names what the
   sub-spine covers (the FE-space construction substrate under every assembled-operator pipeline), the
   **3-way boundary** (in-scope construction+typed-identity+de-Rham-family vs MFEM-owned
   dof-numbering/ordering/conformity/prolongation-read-as-given vs out-of-scope MPI/`Par*`/mesh-partitioning,
   flagged once), and the **deferred follow-on siblings** (`fe_collection`, `essential_dofs`,
   `fe_space_hierarchy`, `BuildDiscreteInterpolator`, `BuildProlongationAtLevel`). Cites the D1 survey
   for the partition.
2. **Consolidated count-owner** — refresh the §Vocabulary-cohort grand-total: `fe_space` is +1, L1 firm
   **31 → 32**. The new entry lands as its OWN sub-spine (FE-space, 1 member), distinct from the
   FE-assembly sub-spine (4) and the main cohort (27): `27 + 4 + 1 = 32`.

**Count discipline (the c057-meta count-owner guard):** firm count computed by reading each linked
chapter's `## Status` line / its proposed-changes status, NOT the drift-prone index cells. The two new
entries are not on disk during dispatch (parallel wave); I read their landing status from the dispatch
plan — D2's `fe_space` lands **firm** (de-Rham construction; clean-gate), D3's
`fe-space-construction-rotation` lands **firm** (L1>L0 theme). See §Count justification.

**Discipline observed:** I do NOT author D2's dep-map row / §Vocabulary-cohort bullet for `fe_space`,
nor D3's theme row / bullet for `fe-space-construction-rotation` — those are dual-registered by the
producers (D2 added its own row+bullet; D3 added its own theme row+bullet). I own only (3) the
consolidated tally + the new sub-spine framing prose.

## Proposed changes

### Edit 1 — refresh the §Vocabulary-cohort grand-total count line (L1 firm 31 → 32)

```edit:book/src/L1/index.md
[old]: **Firm (27 main cohort; 31 firm grand total incl. the FE-assembly sub-spine).** The 27 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm (`fe_assemble` c054 + `weak_form_term` c061 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), bringing the L1 firm grand total to **31** (was 30 after cycle-061: 26 main + 4 FE-assembly sub-spine; cycle-062 D3 added the 27th main-cohort operator `assemble_frequency_operator`). Count discipline: the grand total is computed by reading each linked chapter's `## Status` line, not the index cells — 27 main + 4 FE-assembly = 31; equivalently the dep-map table now holds **31** `firm` rows (incl. `assemble_frequency_operator` c062 and `fe_assemble` c054 — the latter's dep-map row was added cycle-063 D3, moving it from off-table to on-table so the in-table firm-row count self-sums to the grand total). All firm rows are now on-table; there is no off-table firm operator.
[new]: **Firm (27 main cohort; 32 firm grand total incl. the FE-assembly + FE-space sub-spines).** The 27 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm (`fe_assemble` c054 + `weak_form_term` c061 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), and the FE-space sub-spine adds **1** more firm (`fe_space` c064 — see the §"Firm (FE-space sub-spine)" subsection), bringing the L1 firm grand total to **32** (was 31 after cycle-062: 27 main + 4 FE-assembly sub-spine; cycle-064 D2 opened the FE-space sub-spine with its first firm member `fe_space`). Count discipline: the grand total is computed by reading each linked chapter's `## Status` line, not the index cells — 27 main + 4 FE-assembly + 1 FE-space = 32; equivalently the dep-map table now holds **32** `firm` rows (incl. `assemble_frequency_operator` c062, `fe_assemble` c054, and `fe_space` c064). All firm rows are now on-table; there is no off-table firm operator.
```

### Edit 2 — add the FE-space sub-spine framing subsection (the front-opening shell)

Inserted immediately AFTER the FE-assembly sub-spine subsection's four member bullets (which end with the
`eliminate_rhs` bullet) and BEFORE the `**Queued (open questions)**` subsection.

```edit:book/src/L1/index.md
[old]: **Queued (open questions)** — small primitives that bottom-out remaining L0 patterns referenced by the firm cohort:
[new]: **Firm (FE-space sub-spine — 1; opened cycle-064)** — the finite-element **space-construction** surface (the MFEM-equivalent FE-space substrate under every assembled-operator pipeline, in scope per CLAUDE.md mesh/FE), opened this cycle by the firm [`fe_space`](./fe_space.md) (cycle-064 D2) + its L1>L0 rotation [`fe-space-construction-rotation`](../L1-L0/fe-space-construction-rotation.md) (cycle-064 D3). This sub-spine is **upstream** of the FE-assembly sub-spine: where FE-assembly folds weak-form terms into an operator over a space, this sub-spine **constructs the space itself** — the typed `(mesh, FECollection) → FiniteElementSpace[N]` domain/range object that `fe_assemble`, `weak_form_term`, `eliminate_essential_bc`, and `eliminate_rhs` (and the four solver-model operators) currently take **opaquely** as a bare typed `space` / true-dof axis `N` / `DofSet[N]` (the cycle-064 D1 opaque-parameter inventory, `reports/2026-06-02T151056Z-cross-layer-cross-cutter-fe-space-front-survey/CYCLE.md` §4). A firm `fe_space` de-opaques those parameters: it is the shared substrate the whole assembled-operator front stands on.

The sub-spine's scope is fixed by the cycle-064 D1 survey's **3-way boundary** (`reports/2026-06-02T151056Z-cross-layer-cross-cutter-fe-space-front-survey/CYCLE.md` §1):

- **In scope (L1-lifted here):** the `(mesh, FECollection) → FiniteElementSpace[N]` **construction** itself (the Palace-side pairing of a mesh with an FE collection, `palace/fem/fespace.hpp:67-75`); the FE-space as a **typed identity** carrying a known true-dof count `N = GetTrueVSize()`; and the **de-Rham family variant axis** H1 (VALUE) / H(curl) (ND) / H(div) (RT) / L2 (INTEGRAL) — the FE-collection type axis, the construction being identical across the family modulo the collection type (cf. `book/src/L0/fespace-file.md:165-169`).
- **MFEM-owned, read-as-given (NOT re-anchored at L1):** dof / vdof numbering, byNODES/byVDIM ordering, element-to-dof tables, conformity, and the prolongation/restriction matrices (`GetProlongationMatrix`/`GetRestrictionMatrix`) — forwarded verbatim to `mfem::ParFiniteElementSpace` (`palace/fem/fespace.hpp:93-103`; framed as MFEM's at `book/src/L0/fespace-file.md:18-25,154-158`). The L1 `fe_space` treats the space as an **opaque index structure** with the true-dof count `N` and an L-vector↔true-dof transfer — it does NOT crack open the dof structure (splitting it into a thin `dof_map` mirror is the identity-in-named-terms smell the 2026-06-01 vocabulary-shift redirect warns against; the dof structure is a *property* of the `FiniteElementSpace` value, not a distinct L1 operation — the D1 granularity verdict §3).
- **Out of scope (flag once + skip, per CLAUDE.md §Scope):** MPI / `Par*` — the wrapped `mfem::ParFiniteElementSpace` / `mfem::ParMesh` are read single-rank (the existing `par-types-single-rank-reading` rule, `book/src/L0/fespace-file.md:13-16`); mesh **partitioning** (the `Mesh` wrapper's `loc_attr`/`loc_bdr_attr` per-process attribute-remapping, `palace/fem/mesh.hpp:53-60`); and the libCEED basis/restriction caches (transparent performance machinery, re-derivable on demand — a one-line note at most, `book/src/L0/fespace-file.md:97-104,159-164`).

**Deferred follow-on siblings** (named, NOT authored this cycle — the D1 fan-out-ranked pick list §2 + sibling-pull gating §3):

- `fe_collection` *(rough-in; no anchor yet)* — the FE-collection order schedule `(p, dim, mg_max_levels, coarsening, family) → [FECollection]` (`ConstructFECollections`, `palace/fem/multigrid.hpp:22-75`). The order-*schedule* (pmin floor, GaussLobatto/Legendre + LOR basis selection, LINEAR/LOGARITHMIC coarsening) is borderline-second-entry: fold-first as `fe_space`'s collection-input variant axis, split only if its self-standing laws justify a chapter (D1 §3).
- `essential_dofs` *(rough-in; no anchor yet)* — boundary-attribute-marker → essential-true-dof-set (`GetEssentialTrueDofs` ∘ `AttrToMarker`, `palace/fem/multigrid.hpp:97-99`); the `DofSet[N]` that `eliminate_essential_bc`/`eliminate_rhs` take opaquely. Straddles the MFEM-owned boundary (the attribute→marker *shape* lifts; the dof-numbering is read-as-given) — lean noted-property-of-`fe_space` unless `eliminate_*`'s `DofSet[N]` demands a self-standing home (OQ).
- `fe_space_hierarchy` *(rough-in; no anchor yet)* — the h/p-refinement multigrid stack (`ConstructFiniteElementSpaceHierarchy`, `palace/fem/multigrid.hpp:78-126`); lower fan-out for the assembly front (the geometric-multigrid preconditioner consumes it, not the assembled-operator pipeline).
- `BuildDiscreteInterpolator` *(rough-in; no anchor yet)* — the de-Rham interpolator; **sibling-pull-gated** (name, don't dispatch).
- `BuildProlongationAtLevel` *(rough-in; no anchor yet)* — the multigrid transfer (`AddLevel`/`GetProlongationAtLevel`); **sibling-pull-gated** (name, don't dispatch).

Once `fe_space` is firm on disk, the four opaque-parameter entries above gain live cross-refs for their `space` / `N` / `DofSet` parameters (currently bare typed names) — a later replace-and-propagate dispatch, NOT this cycle (D1 §4 forward-look).

**Queued (open questions)** — small primitives that bottom-out remaining L0 patterns referenced by the firm cohort:
```

## Count justification (count-owner audit trail)

Per the c057-meta count-owner guard: **firm count is computed from each linked chapter's `## Status`
line / its landing status, NOT from index cells.**

**Pre-cycle firm grand total = 31** (the current header arithmetic, verified against the dep-map table):

- **27 main cohort** — the 27 firm rows listed in §Vocabulary-cohort "Firm" main bullets (axpy … through
  `assemble_frequency_operator` c062, the 27th).
- **+4 FE-assembly sub-spine** — `fe_assemble` (firm c054), `weak_form_term` (firm c061),
  `eliminate_essential_bc` (firm c055), `eliminate_rhs` (firm c055). All four carry `firm` dep-map rows
  and §subsection bullets on disk.
- **= 31.** Matches the current header and the on-table firm-row count.

**This cycle's landings (read from the dispatch plan, not yet on disk — parallel wave):**

- **D2 `book/src/L1/fe_space.md` lands `firm`** — the `(mesh, FECollection) → FiniteElementSpace[N]`
  construction; de-Rham family variant axis; clean-gate per the D1 granularity verdict (ONE entry, not a
  `fe_space`+`fe_collection`+`dof_map` split). **+1 firm.** D2 owns its own dep-map row + cohort bullet
  (dual-registration; I do not author them).
- **D3 `book/src/L1-L0/fe-space-construction-rotation.md` lands `firm`** — the L1>L0 rotation theme. This
  is a **theme**, not an L1 operator, so it does NOT increment the L1 operator firm count; it lands in the
  L1-L0 theme table (D3 owns that row). The L1-L0 index carries **no consolidated firm tally** to own
  (its "Working Notes" is a one-line evidence note, not a running count) — confirmed by read; nothing for
  the count-owner to update there.

**Post-cycle firm grand total = 32:** `27 main + 4 FE-assembly + 1 FE-space (fe_space) = 32`. The new
`fe_space` lands as its OWN sub-spine (FE-space, distinct from FE-assembly: it constructs the space, it
does not assemble over it), so the header now reads "27 main cohort; 32 firm grand total incl. the
FE-assembly + FE-space sub-spines."

## Supporting evidence

- **D1 survey** `reports/2026-06-02T151056Z-cross-layer-cross-cutter-fe-space-front-survey/CYCLE.md` —
  the in-scope / MFEM-owned / out-of-scope 3-way partition (§1), the fan-out-ranked pick list (§2), the
  ONE-`fe_space`-entry granularity verdict (§3), the opaque-parameter inventory (§4). All framing prose
  citations forwarded from this survey.
- **L0 anchor** `book/src/L0/fespace-file.md` (on disk, verified) — FE-space wrapper + hierarchy;
  MFEM-as-given framing `:18-25,154-158`; de-Rham family `:165-169`; transparent-cache classification
  `:97-104,159-164`; single-rank `Par*` reading `:13-16`.
- **Palace source (via D1 survey, codemap-verified there):** `palace/fem/fespace.hpp:67-75` (variadic
  ctor forwarding), `:93-103` (MFEM-forwarding dof accessors); `palace/fem/multigrid.hpp:22-75`
  (`ConstructFECollections`), `:78-126` (`ConstructFiniteElementSpaceHierarchy`), `:97-99`
  (`GetEssentialTrueDofs` ∘ `AttrToMarker`); `palace/fem/mesh.hpp:53-60` (partitioning attr-remap,
  out-of-scope).
- **Opaque-parameter inventory (de-opaqued by firm `fe_space`):** `book/src/L1/fe_assemble.md:60,67`,
  `book/src/L1/weak_form_term.md:79,166`, `book/src/L1/eliminate_essential_bc.md:56,63,67`,
  `book/src/L1/eliminate_rhs.md` (the bare `space` / `N` / `DofSet[N]` parameters).

## Open questions / caveats

- **D2/D3 CYCLE.md not yet on disk at dispatch time (parallel wave-2).** Landing status (`fe_space` firm,
  `fe-space-construction-rotation` firm) read from the cycle-064 dispatch plan, not from the producers'
  proposed-changes blocks. If either producer lands at a maturity OTHER than firm (e.g. `fe_space`
  promotes to rough-in on a discovered law-confidence gap), the integrator must adjust the grand total:
  the framing prose's count line (`32`) and the new sub-spine header (`1`) would need to drop to `31` /
  `0`-firm-with-rough-in. Flagged for the per-report integrator to reconcile against D2's actual
  proposed `## Status` line.
- **Live links to co-landed files.** The framing prose links `[`fe_space`](./fe_space.md)` and
  `[`fe-space-construction-rotation`](../L1-L0/fe-space-construction-rotation.md)` as **live links** (not
  plain-text), on the basis that both land firm this same cycle and the integrator applies all reports
  before the book rebuild (the `weak_form_term` c061 co-landed-row precedent). The five **deferred
  siblings** (`fe_collection`, `essential_dofs`, `fe_space_hierarchy`, `BuildDiscreteInterpolator`,
  `BuildProlongationAtLevel`) are referenced as **plain-text** `*(rough-in; no anchor yet)*` per the
  `rough-in-rows-must-be-plain-text-when-anchor-missing` convention (no anchor files exist).
- **L1-L0 index has no consolidated tally to own.** As count-owner I confirm `book/src/L1-L0/index.md`
  carries only a theme table + a one-line Working Note (no running firm count); D3 adds its own theme
  row. No edit to that index is mine this cycle.
