---
agent: abstractor
invoked_at: 2026-06-02T17:05:00Z
scope: L1>L0 theme sketch — essential-dofs-construction-rotation
status: integrated
integrated_at: 2026-06-02T194500Z
integration_commit: 062ae9e
integration_notes: "cycle-066 D2. essential-dofs-construction-rotation LANDED FIRM L1>L0 (book/src/L1-L0/essential-dofs-construction-rotation.md — LHS L1 essential_dofs -> RHS L0 dbc block multigrid.hpp:92-101; construction-head-lowers / dof-resolution-tail-MFEM-owned split). Applied: L1-L0/index.md theme row + SUMMARY. Live link ../L1/essential_dofs.md RESOLVES (D1 landed first). citecheck --scan 23 ok / 0 failing. L1>L0 firm themes +1. Build clean; no build-repair."
inputs:
  - cycle-066 dispatch D2 (wave 2) prompt
  - D1 report reports/2026-06-02T164202Z-harvester-essential-dofs/CYCLE.md (WARRANT=YES, essential_dofs firm)
  - L1 op (this-cycle, forward-ref live-link): book/src/L1/essential_dofs.md (canonical slug)
  - L0 anchors (on-disk Read + citecheck --anchor, NOT codemap, per confirmed ±1 drift this batch):
    - palace/fem/multigrid.hpp:92-101 (dbc block inside ConstructFiniteElementSpaceHierarchy)
    - palace/utils/geodata.hpp:75-96 (mesh::AttrToMarker doc + decl + template wrappers)
    - palace/models/spaceoperator.cpp:169-206 (standalone CheckBoundaryProperties site)
  - sibling precedent: book/src/L1-L0/fe-space-construction-rotation.md (c064),
    fe-collection-construction-rotation.md (c065)
---

# CYCLE: L1>L0 theme sketch — essential-dofs-construction-rotation

## Summary

This theme lowers the pure L1 `essential_dofs` constructor (authored this cycle by D1, WARRANT=YES)
into the concrete Palace dbc block at `palace/fem/multigrid.hpp:92-101`. The translation is a genuine
**vocabulary shift, not a rename** (per the 2026-06-01 redirect): the L1 form is a *value* —
`essential_dofs(space, bdr_attrs, bdr_attr_max) → DofSet[N]`, a typed essential-true-dof set over a
space — whereas the L0 form is an *imperative attribute → marker → GetEssentialTrueDofs sequence* with
an out-parameter write. The rewrite has a sharp ownership boundary, carried forward from D1's harvest:

- **HEAD lowers cleanly (Palace-authored).** `bdr_attr_max` extraction
  (`mesh.bdr_attributes.Size() ? .Max() : 0`, `multigrid.hpp:95-97`) + `mesh::AttrToMarker`
  (`palace/utils/geodata.hpp:75-96` — attribute-list → dense `{0,1}` boolean marker over
  `[1..bdr_attr_max]`, with the `-1`-singleton wildcard ⇒ all-ones). Both are Palace-owned and read
  off positive source.
- **TAIL is the opaque-MFEM boundary (read-as-given).** `space.Get().GetEssentialTrueDofs(marker, out)`
  (`multigrid.hpp:99`) — the marker → true-dof-set resolution lives entirely in MFEM; the theme
  documents the boundary and does NOT lower it.

This construction-lowers-head / opaque-MFEM-tail split is the direct analogue of the c064
`fe-space-construction-rotation` construction-lowers / dof-bookkeeping-MFEM-owned split (and the
sibling `fe-collection-construction-rotation` produced-collection-internals-MFEM-owned posture).
**Status assigned: `firm`** (structural) — the whole Palace-authored head is positively anchored; the
MFEM tail is a witnessed library-ownership boundary (read-as-given, NOT a constructed sub-part from
negative anchors), so it does not gate firmness, exactly as in `fe-space-construction-rotation`.

## Proposed changes

```new:book/src/L1-L0/essential-dofs-construction-rotation.md
# essential-dofs-construction-rotation

**Slug:** `essential-dofs-construction-rotation`

How the pure L1 [`essential_dofs`](../L1/essential_dofs.md) construction lowers into the concrete
Palace Dirichlet-boundary (dbc) block inside `ConstructFiniteElementSpaceHierarchy`
(`palace/fem/multigrid.hpp:92-101`). This is a **vocabulary translation, not a rename**: the L1 form
is a *value* — a `(space, bdr_attrs, bdr_attr_max)` triple naming the essential-true-dof set `DofSet[N]`
on a function space — while the L0 form is an *imperative attribute → marker → GetEssentialTrueDofs
sequence* that writes its result into a caller-provided out-parameter. The translation has a sharp
boundary — the **construction head lowers (Palace-authored) / the dof-resolution tail is
MFEM-owned-read-as-given** — narrated in the split below.

## Status

`firm` — structural. The construction head is positively anchored at L0: the `bdr_attr_max` extraction
(`multigrid.hpp:95-97`, witnessed standalone at `spaceoperator.cpp:174`) and the fully Palace-authored
marker constructor `mesh::AttrToMarker` (`geodata.hpp:75-96`, with its documented `{0,1}`-membership +
`-1`-wildcard contract `geodata.hpp:76-78`). The marker → true-dof-set step (`GetEssentialTrueDofs`,
`multigrid.hpp:99`) is **documented as MFEM-owned-read-as-given** — it is a witnessed library-ownership
boundary, NOT a constructive reconstruction, so it does not gate firmness (cf. the firm
[`fe-space-construction-rotation`](./fe-space-construction-rotation.md) construction-lowers /
dof-bookkeeping-MFEM-owned split, and the `opaque-library-ownership`
[`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md)). Because
the tail is read-as-given (not a sub-part materialized from negative anchors), this is `firm`, not
`partly-constructive`. The no-dedicated-`test-multigrid.cpp` caveat is non-gating per the
`fe_space`/`fe_collection`/`fe_assemble` firm-on-positive-structure precedent. MPI/`Par*` and mesh
partitioning are flagged once and read single-rank (out of scope per CLAUDE.md §Scope).

## L1 form (LHS)

The pure construction value (D2's prime entry [`L1/essential_dofs`](../L1/essential_dofs.md)):

    essential_dofs :: (space: FiniteElementSpace[N], bdr_attrs: [Attr], bdr_attr_max: Nat) -> DofSet[N]

`DofSet[N]` is the essential (Dirichlet) true-dof set — a subset of `[0 .. N)` over the true-dof axis
`N = space.GetTrueVSize()`. At L1 this is a referentially-transparent function: given the same
`(space, bdr_attrs, bdr_attr_max)` it names the same set; the result is a fresh immutable value, and
the dof structure is an opaque property of `space` (the index axis `N`), not a separate operation. The
single-element list `[-1]` is the all-boundaries wildcard. `essential_dofs` is the producer of the
`DofSet[N]` that [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md) and
[`eliminate_rhs`](../L1/eliminate_rhs.md) consume opaquely.

## L0 form (RHS)

The concrete Palace dbc block — the cleanest single-construction anchor is the coarse-seed inside
`ConstructFiniteElementSpaceHierarchy`:

    // palace/fem/multigrid.hpp:92-101 (the dbc block, guarded on dbc_attr && dbc_tdof_lists)
    mfem::Array<int> dbc_marker;
    if (dbc_attr && dbc_tdof_lists)
    {
      int bdr_attr_max = mesh[coarse_mesh_l]->Get().bdr_attributes.Size()
                             ? mesh[coarse_mesh_l]->Get().bdr_attributes.Max()
                             : 0;
      dbc_marker = mesh::AttrToMarker(bdr_attr_max, *dbc_attr);
      fespaces.GetFinestFESpace().Get().GetEssentialTrueDofs(dbc_marker,
                                                             dbc_tdof_lists->emplace_back());
    }

The L1 triple maps onto this block as: `bdr_attrs = *dbc_attr`, `bdr_attr_max` = the extracted max,
`space = fespaces.GetFinestFESpace()`, and the returned `DofSet[N]` = the `mfem::Array<int>` written
into `dbc_tdof_lists->emplace_back()`. The mutation-rotation reads the out-parameter write
(`emplace_back()` receiver, `multigrid.hpp:99-100`) as a returned value. The same idiom recurs
standalone (non-hierarchy) at `spaceoperator.cpp:204-205` (writing into
`aux_bdr_tdof_lists.emplace_back()`).

### The construction-head-lowers / dof-resolution-tail-MFEM-owned split (the translation boundary)

The translation is sharp on the last line of the block: `...GetEssentialTrueDofs(dbc_marker, out)`.

- **LOWERS HERE (Palace-authored head).** The two construction stages are Palace-owned and rewrite
  directly:
  1. **`bdr_attr_max` extraction** — `mesh.bdr_attributes.Size() ? mesh.bdr_attributes.Max() : 0`
     (`multigrid.hpp:95-97`; witnessed standalone at `spaceoperator.cpp:174`). The empty-guard is the
     L1 empty-boundary identity (`bdr_attr_max = 0` ⇒ empty marker ⇒ `∅`).
  2. **marker construction** — `mesh::AttrToMarker(bdr_attr_max, *dbc_attr)` (`multigrid.hpp:98`),
     which is **fully Palace-authored** in `palace/utils/geodata.hpp:75-96` (it is in `palace/utils/`,
     not an MFEM call). It returns an `mfem::Array<int>` of size `bdr_attr_max` containing only zeros
     and ones, ones at the listed attributes (`geodata.hpp:76-78`); the single `-1` entry marks all
     boundaries (the wildcard, `geodata.hpp:77-78`). This stage is the membership-indicator /
     join-semilattice-homomorphism head carrying the L1 marker-level laws (wildcard saturation, marker
     subset-monotonicity, marker union-additivity witnessed at `spaceoperator.cpp:187-198`).
- **MFEM-OWNED-READ-AS-GIVEN (does NOT lower here).** The marker → true-dof-set resolution is
  `space.Get().GetEssentialTrueDofs(dbc_marker, out)` (`multigrid.hpp:99-100`), called on `.Get()` —
  the wrapped `mfem::ParFiniteElementSpace`. The true-dof numbering, the marker → dof resolution, and
  the essential-dof semantics are **MFEM-owned, read-as-given** (the same posture
  [`fe_space`](../L1/fe_space.md) takes toward dof structure). This theme treats the dof-set as an
  opaque index structure tagged by the space's true-dof axis `N`; it does NOT crack open the dof
  numbering (doing so would be the identity-in-named-terms smell the 2026-06-01 vocabulary-shift
  redirect warns against — the dof set is a *value over* the space, not a separate L1 operation that
  re-mirrors MFEM dof internals).

This split is the exact analogue, at the essential-dof-construction altitude, of the
construction-lowers / dof-bookkeeping-MFEM-owned split in
[`fe-space-construction-rotation`](./fe-space-construction-rotation.md): the *shell* (attribute → marker
case logic) is Palace-owned and lowers; the *dof-index internals* are MFEM-owned and read-as-given. As
in the `fe_space` sibling — and unlike the libCEED owner of
[`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md) — the
opaque owner here is **MFEM dof-management**. The boundary does not downgrade the theme: the head is
positively anchored and firm (firm-on-positive-structure precedent).

### Variant axis — attribute-wildcard (2 rewrite cases on the head)

The construction is identical modulo how `bdr_attrs` resolves into the marker:

| L1 `bdr_attrs` case | L0 marker form | anchor |
|---|---|---|
| explicit list `[a₁, …]` | dense `{0,1}` marker, ones at listed attrs | `geodata.hpp:76` |
| all-boundaries wildcard `[-1]` | all-ones marker | `geodata.hpp:77-78` |

Both feed the same `GetEssentialTrueDofs` tail unchanged; the variant is entirely on the Palace-authored
head. (A second reuse axis — per-level-hierarchy-application, where the *same* built marker is reapplied
per FE-space level, `multigrid.hpp:106-111`/`:117-122`, accumulating into `dbc_tdof_lists` — is a
property of the *hierarchy* consumer `fe_space_hierarchy`, not of this single-space rewrite; noted under
Applicability.)

## Applicability conditions

- The rewrite applies to the single-space construction `essential_dofs(space, bdr_attrs, bdr_attr_max)`.
  The cleanest anchor is the coarse-seed dbc block (`multigrid.hpp:92-101`); the standalone
  `CheckBoundaryProperties` site (`spaceoperator.cpp:169-206`) is the same idiom with a pointwise-OR
  marker union over eight conditions (`:187-198`) before a single `GetEssentialTrueDofs` (`:204-205`) —
  i.e. the marker union-additivity law applied at the head.
- `bdr_attrs` is a list of 1-based boundary-attribute numbers, OR the single-element wildcard `[-1]`.
  `bdr_attr_max` is `mesh.bdr_attributes.Max()` (0 when the mesh has no boundary attributes), supplied
  by the `bdr_attr_max` extraction at the head.
- **Per-level hierarchy fan-out is upstream/sibling, not this theme.** In the multigrid path the same
  marker is reapplied per level (`multigrid.hpp:106-111`, `:117-122`), each call writing one more
  `dbc_tdof_lists` entry. That fan-out belongs to the deferred `fe_space_hierarchy` sibling; this theme
  is the per-space rewrite the hierarchy iterates.
- Single-rank reading: `mfem::ParFiniteElementSpace` / `bdr_attributes` / `GetEssentialTrueDofs` are
  read as their serial equivalents (out of scope per CLAUDE.md §Scope; flagged once). The
  `dbc_tdof_lists` per-level accumulation is the hierarchy/partition concern, also out of scope here.

## Justification kind

**Structural** — the rewrite is shape-driven: the L1 value `essential_dofs(space, bdr_attrs,
bdr_attr_max)` maps onto the concrete attribute → marker → `GetEssentialTrueDofs` block, with the
attribute-wildcard as the positively-anchored case axis. No reduction chain or algebraic re-derivation
is needed; the boundary (what lowers vs. what is MFEM-owned-read-as-given) is established by the call
site on `.Get()` (`multigrid.hpp:99`), exactly as the `fe_space` thin-forwarding accessors establish
the dof-bookkeeping boundary there.

## Verified-against

- `palace/fem/multigrid.hpp:92-101` — the dbc block: `bdr_attr_max` extraction (`:95-97`),
  `dbc_marker = mesh::AttrToMarker(bdr_attr_max, *dbc_attr)` (`:98`),
  `GetEssentialTrueDofs(dbc_marker, dbc_tdof_lists->emplace_back())` (`:99-100`). Per-level
  reapplication of the same marker: `:106-111` (h-refinement), `:117-122` (p-refinement). (Verified
  on-disk via Read + `citecheck --anchor bdr_attr_max`/`GetEssentialTrueDofs`; codemap NOT used.)
- `palace/utils/geodata.hpp:75-96` — `mesh::AttrToMarker`: the size-`max_attr` zero/one
  membership-indicator + `-1`-wildcard contract documentation (`:75-78`), the `(int, const int*, int,
  Array&, bool)` decl (`:79-80`), the iterable-overload template wrapper (`:82-88`), and the
  return-by-value template wrapper that builds the `mfem::Array<int>` marker (`:90-96`). (Verified
  on-disk; `citecheck --anchor AttrToMarker` ✓ at `:79`.)
- `palace/models/spaceoperator.cpp:169-206` — `CheckBoundaryProperties` standalone site: `bdr_attr_max`
  (`:174`), `mesh::AttrToMarker(bdr_attr_max, dbc_attr)` (`:175`), the pointwise-OR marker union over
  eight per-condition markers (`:187-198`), and the per-level
  `GetEssentialTrueDofs(aux_bdr_marker, aux_bdr_tdof_lists.emplace_back())` (`:202-205`). (Verified
  on-disk; `citecheck --anchor GetEssentialTrueDofs` ✓ at `:204`.)
- [`L1/essential_dofs`](../L1/essential_dofs.md) — the prime L1 entry this theme lowers (D1 this-cycle).
- Sibling precedent: [`fe-space-construction-rotation`](./fe-space-construction-rotation.md) (c064;
  construction-lowers / dof-bookkeeping-MFEM-owned split),
  [`fe-collection-construction-rotation`](./fe-collection-construction-rotation.md) (c065),
  [`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md) (c055;
  opaque-library-ownership posture).

## Open questions / caveats

- **Lifting note (reverse direction, working-note only).** The L0 dbc block lifts to L1
  `essential_dofs` cleanly precisely because the dof-resolution tail is read-as-given — the lift retains
  only the `(space, bdr_attrs, bdr_attr_max) → DofSet[N]` shape and the Palace-authored marker
  semantics, discarding the MFEM true-dof numbering. The structure the lift would need to be *complete*
  (rather than opaque) is the marker → dof-index algebra, which is MFEM's and out of scope.
  (High→low formal content stays in the chapter above; this is a working note.)
- **`fe_space_hierarchy` per-level fan-out.** The `dbc_tdof_lists` per-level accumulation
  (`multigrid.hpp:99-100`, `:106-111`, `:117-122`) is the hierarchy consumer's property, not this
  single-space rewrite's. It belongs in the eventual `fe_space_hierarchy` entry; flagged so that entry
  picks up the per-level dof-set fan-out.
- **Replace-and-propagate (later cycle).** `eliminate_essential_bc`'s `dofs: DofSet[N]` and
  `eliminate_rhs`'s essential-row pin can now cross-ref `essential_dofs` for `DofSet[N]` provenance
  (currently bare typed names). Same follow-up class as the `fe_space` opaque-parameter fan-out.
- **Forward-reference resolution.** The live-link to [`L1/essential_dofs`](../L1/essential_dofs.md)
  (D1, this cycle) resolves once D1's entry lands; per CLAUDE.md §Integration-may-materialize, both
  D1's and D2's chapters land in the same cycle.
```

```edit:book/src/L1-L0/index.md
| [fe-space-construction-rotation](./fe-space-construction-rotation.md) | [`L1/fe_space`](../L1/fe_space.md) (firm c064) | `palace/fem/fespace.hpp:67-75` (variadic ctor) + `:93-103` (MFEM-forwarding dof accessors), `palace/fem/multigrid.hpp:90` (single-space coarse-seed), `palace/models/spaceoperator.cpp:47/49/51/75` (de-Rham instantiation sites) | firm *(structural; vocabulary-translation — pure `(mesh, collection) → FiniteElementSpace[N]` value → imperative `mfem::ParFiniteElementSpace`-wrapping ctor; **construction-lowers / dof-bookkeeping-MFEM-owned split** — the `(mesh, collection)` pairing + de-Rham case selection + `ResetCeedObjects` cache-init lower HERE at the ctor `fespace.hpp:67-75`, the dof/vdof numbering + ordering + conformity + prolongation/restriction matrices are MFEM-owned-read-as-given via thin forwarding accessors `fespace.hpp:93-103` (analogue of the libCEED-leaf boundary but MFEM-dof-management-owned, not libCEED-quadrature); 4 de-Rham rewrite cases H1/`H1_FECollection` `:49` + H(curl)/`ND_FECollection` `:47` + H(div)/`RT_FECollection` `:51` + L2/`L2_FECollection` `:75` (2-D-curl INTEGRAL-map load-bearing variant); single-space coarse-seed `multigrid.hpp:90`; hierarchy/`fe_collection` deferred siblings; MPI/`Par*` + mesh-partitioning out-of-scope single-rank; firm-on-positive-structure)* |
| [essential-dofs-construction-rotation](./essential-dofs-construction-rotation.md) | [`L1/essential_dofs`](../L1/essential_dofs.md) (firm c066) | `palace/fem/multigrid.hpp:92-101` (dbc block: `bdr_attr_max` `:95-97`, `AttrToMarker` `:98`, `GetEssentialTrueDofs` `:99-100`; per-level `:106-111`/`:117-122`), `palace/utils/geodata.hpp:75-96` (`mesh::AttrToMarker` doc+decl+wrappers), `palace/models/spaceoperator.cpp:169-206` (standalone `CheckBoundaryProperties`: `bdr_attr_max` `:174`, marker-OR union `:187-198`, `GetEssentialTrueDofs` `:204-205`) | firm *(structural; vocabulary-translation — pure `(space, bdr_attrs, bdr_attr_max) → DofSet[N]` essential-true-dof-set value → imperative attribute→marker→`GetEssentialTrueDofs` block with out-parameter write (`emplace_back()` receiver read as return); **construction-head-lowers / dof-resolution-tail-MFEM-owned split** — `bdr_attr_max` extraction (`multigrid.hpp:95-97`, empty-guard ⇒ `∅`) + fully-Palace-authored `mesh::AttrToMarker` (`geodata.hpp:75-96`; dense `{0,1}` membership-indicator over `[1..bdr_attr_max]`, `-1`-singleton wildcard ⇒ all-ones `:77-78`) lower HERE; the marker→true-dof-set `space.Get().GetEssentialTrueDofs` (`multigrid.hpp:99`) is MFEM-owned-read-as-given (same posture as `fe-space-construction-rotation` toward dof structure), NOT a constructed sub-part — so firm, not partly-constructive; attribute-wildcard variant axis (explicit-list vs `[-1]` all-ones, 2 head cases); marker union-additivity (join-semilattice homomorphism) witnessed at `spaceoperator.cpp:187-198`; per-level-hierarchy fan-out is the `fe_space_hierarchy` consumer's property (out of scope); analogue of the c064 `fe-space-construction-rotation` construction-lowers/dof-bookkeeping-MFEM-owned split; MPI/`Par*` + partitioning out-of-scope single-rank; firm-on-positive-structure, no-dedicated-`test-multigrid.cpp` caveat non-gating per `fe_space`/`fe_collection`/`fe_assemble`)* |
```

(The `fe-space-construction-rotation` row above is reproduced verbatim as the insert anchor; the new
`essential-dofs-construction-rotation` row is appended immediately after it in the Theme list table.
This is registration artifact **(1)** — my OWN table row, per the dual-registration partition.)

```edit:book/src/SUMMARY.md
- [fe-space-construction-rotation](./L1-L0/fe-space-construction-rotation.md)
- [essential-dofs-construction-rotation](./L1-L0/essential-dofs-construction-rotation.md)
- [fe-collection-construction-rotation](./L1-L0/fe-collection-construction-rotation.md)
```

## Speculative operators proposed

None. This theme lowers the already-firm L1 `essential_dofs` (D1 this-cycle); both the Palace-authored
head primitives (`AttrToMarker`, `bdr_attr_max` extraction) and the MFEM-opaque tail
(`GetEssentialTrueDofs`) are existing source constructs, not new L1 vocabulary. No rough-in operators
to hand off to the harvester.

## Dual-registration note (per partition)

The `book/src/L1-L0/index.md` carries **only** a Theme-list table + a Working-Notes section — there is
**no §Vocabulary-cohort bullet section and no consolidated running-count tally** in this index (unlike
the `book/src/L1/index.md` firm-count machinery). Therefore my registration obligations reduce to:

1. **My Theme-list table row** — authored above (artifact (1), always mine). ✓
2. **My §Vocabulary-cohort bullet** — N/A: this index has no cohort-bullet section. (The cohort/count
   narrative for the FE-space sub-spine lives in `book/src/L1/index.md`, which is D1's + D4's surface,
   not this L1>L0 index.)
3. **Consolidated tally** — N/A here. The L1 firm grand-total / FE-space-sub-spine count update
   (2→3 members; 33→34 firm) is the `book/src/L1/index.md` tally, **DEFERRED to D4** (the named
   count-owner this cycle) per D1's report — this L1>L0 theme does not touch that count.

SUMMARY.md registration of the new theme chapter is mine (artifact above).

## Supporting evidence

All L0 citations verified on-disk via the `Read` tool against `reference/palace/palace/...` and
re-confirmed with `tools/citecheck/citecheck.py --anchor` (codemap NOT used — ±1 drift confirmed
2-of-2 on FE headers this batch):

- `palace/fem/multigrid.hpp:92-101` — read on-disk (lines 88-127). `bdr_attr_max` empty-guard at
  `:95-97`; `dbc_marker = mesh::AttrToMarker(bdr_attr_max, *dbc_attr)` at `:98`;
  `GetEssentialTrueDofs(dbc_marker, dbc_tdof_lists->emplace_back())` at `:99-100`. Per-level reapply
  `:106-111`/`:117-122`. `citecheck` ✓ (`bdr_attr_max` in 95-100; `GetEssentialTrueDofs` at `:99`).
- `palace/utils/geodata.hpp:75-96` — read on-disk (lines 73-97). Doc comment `{0,1}`-marker +
  `-1`-wildcard at `:75-78`; decl `:79-80`; iterable template wrapper `:82-88`; return-by-value
  template wrapper `:90-96`. `citecheck --anchor AttrToMarker` ✓ at `:79`.
- `palace/models/spaceoperator.cpp:169-206` — read on-disk (lines 169-208). `bdr_attr_max` at `:174`;
  `mesh::AttrToMarker(bdr_attr_max, dbc_attr)` at `:175`; pointwise-OR marker union `:187-198`;
  per-level `GetEssentialTrueDofs(aux_bdr_marker, aux_bdr_tdof_lists.emplace_back())` at `:204-205`.
  `citecheck --anchor GetEssentialTrueDofs` ✓ at `:204`.

Citation root is `palace/...` (strips the on-disk `reference/palace/` prefix), per the existing
`fe-space-construction-rotation.md` / `fe-collection-construction-rotation.md` index rows.

## Open questions / caveats

- **Forward-reference live-link.** The theme links `[L1/essential_dofs](../L1/essential_dofs.md)` as a
  live link per dispatch (D1 lands `book/src/L1/essential_dofs.md` this same cycle). If integration
  applies this report BEFORE D1's, the link is momentarily dead — resolved within the cycle (both land
  in the same finalize); flagged for integrator ordering awareness, not a defect in this report.
- **Lifting note (reverse direction).** Recorded inside the chapter's §Open-questions as a working
  note (high→low formal content stays in the chapter body; the lift discards MFEM dof-numbering).
- **`fe_space_hierarchy` per-level fan-out + `eliminate_*` cross-ref replace-and-propagate** — both
  deferred to later cycles (the same follow-ups D1 flagged); noted in the chapter for downstream pickup.
