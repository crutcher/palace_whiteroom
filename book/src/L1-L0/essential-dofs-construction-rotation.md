---
# Lowering theme. Per graded-stack scheme §5: rank = min(endpoint ranks). The L1
# endpoint (essential_dofs) is firm (rank 3); the L0 endpoint is rank-terminal ground
# truth. So the theme is firm and rank(theme) <= min(endpoints) holds for free.
rank: firm
edges:
  depends-on:
    - target: L1/essential_dofs
      kind: lowers-to             # the L1 source construction this theme lowers
    - target: palace/fem/multigrid.hpp:92-101
      kind: cites-evidence        # the dbc block in ConstructFiniteElementSpaceHierarchy
    - target: palace/utils/geodata.hpp:75-96
      kind: cites-evidence        # mesh::AttrToMarker (Palace-authored marker constructor)
    - target: palace/fem/multigrid.hpp:99-100
      kind: cites-evidence        # GetEssentialTrueDofs (MFEM-owned-read-as-given tail)
  reference:
    - L1-L0/fe-space-construction-rotation        # sibling construction-lowers/bookkeeping-MFEM-owned split
    - L1-L0/fe-operator-assemble-mutation-rotation # the BC-elimination consumer theme
---

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

The marker → true-dof-set step (`GetEssentialTrueDofs`, `multigrid.hpp:99`) is **MFEM-owned-read-as-given**
— a witnessed library-ownership boundary, not a constructive reconstruction (cf. the firm
[`fe-space-construction-rotation`](./fe-space-construction-rotation.md) construction-lowers /
dof-bookkeeping-MFEM-owned split, and the `opaque-library-ownership`
[`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md)). MPI/`Par*`
and mesh partitioning are read single-rank (out of scope per CLAUDE.md §Scope).

## L1 form (LHS)

The pure construction value ([`L1/essential_dofs`](../L1/essential_dofs.md)):

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

### The construction-head-lowers / dof-resolution-tail-MFEM-owned split

*The translation boundary.*

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
  numbering (doing so would be the identity-in-named-terms smell the vocabulary-shift discipline
  warns against — the dof set is a *value over* the space, not a separate L1 operation that
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

## Evidence

- `palace/fem/multigrid.hpp:92-101` — the dbc block: `bdr_attr_max` extraction (`:95-97`),
  `dbc_marker = mesh::AttrToMarker(bdr_attr_max, *dbc_attr)` (`:98`),
  `GetEssentialTrueDofs(dbc_marker, dbc_tdof_lists->emplace_back())` (`:99-100`). Per-level
  reapplication of the same marker: `:106-111` (h-refinement), `:117-122` (p-refinement).
- `palace/utils/geodata.hpp:75-96` — `mesh::AttrToMarker`: the size-`max_attr` zero/one
  membership-indicator + `-1`-wildcard contract documentation (`:75-78`), the `(int, const int*, int,
  Array&, bool)` decl (`:79-80`), the iterable-overload template wrapper (`:82-88`), and the
  return-by-value template wrapper that builds the `mfem::Array<int>` marker (`:90-96`).
- `palace/models/spaceoperator.cpp:169-206` — `CheckBoundaryProperties` standalone site: `bdr_attr_max`
  (`:174`), `mesh::AttrToMarker(bdr_attr_max, dbc_attr)` (`:175`), the pointwise-OR marker union over
  eight per-condition markers (`:187-198`), and the per-level
  `GetEssentialTrueDofs(aux_bdr_marker, aux_bdr_tdof_lists.emplace_back())` (`:202-205`).
- [`L1/essential_dofs`](../L1/essential_dofs.md) — the prime L1 entry this theme lowers.
- Sibling precedent: [`fe-space-construction-rotation`](./fe-space-construction-rotation.md)
  (construction-lowers / dof-bookkeeping-MFEM-owned split),
  [`fe-collection-construction-rotation`](./fe-collection-construction-rotation.md),
  [`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md)
  (opaque-library-ownership posture).

## Open questions / caveats

- **`fe_space_hierarchy` per-level fan-out.** The `dbc_tdof_lists` per-level accumulation
  (`multigrid.hpp:99-100`, `:106-111`, `:117-122`) is the hierarchy consumer's property, not this
  single-space rewrite's. It belongs in the eventual `fe_space_hierarchy` entry, which picks up the
  per-level dof-set fan-out.
- **Downstream `DofSet[N]` provenance.** `eliminate_essential_bc`'s `dofs: DofSet[N]` and
  `eliminate_rhs`'s essential-row pin cross-ref `essential_dofs` for `DofSet[N]` provenance.
