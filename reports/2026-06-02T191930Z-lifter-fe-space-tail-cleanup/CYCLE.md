---
agent: lifter
invoked_at: 2026-06-02T191930Z
scope: L1 FE-space sub-spine tail cleanup — fe-space-sub-spine-tail-cleanup (cycle-067 D1)
status: pending
integrated_at: 2026-06-02T193833Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-067 D1 — applied clean (first per-report integrator). FE-space sub-spine tail cleanup: eliminate_essential_bc.md prose shape-contract bullet now names [essential_dofs](./essential_dofs.md); fe_space.md:39,149 forward-refs upgraded to live links. All 3 entries stay firm, NO status flip, NO count change. Closed 2 OQs in-artifact. Build-relevant; cargo make book exit 0. Staging row: cycle-067-integrator-staging/STAGING.md."
inputs:
  - book/src/L1/eliminate_essential_bc.md
  - book/src/L1/eliminate_rhs.md
  - book/src/L1/fe_space.md
  - book/src/L1/essential_dofs.md (firm on disk — link target)
  - book/src/L1-L0/fe-space-construction-rotation.md (firm on disk — link target)
  - book/src/L1/fe_assemble.md (c065 opaque-parameter cross-ref precedent)
---

# CYCLE: Re-anchor fe-space-sub-spine-tail-cleanup

## Summary
Cycle-067 D1 (the batch-21 LEAD). Two surgical tail cleanups in `book/src/L1/`, closing the
FE-space sub-spine residue (the three batch-20-migrated follow-ons). Both are pure prose
cross-ref / live-link upgrades against targets verified firm on disk — NO status flips (all
entries stay `firm`), so NO index-cell touch and NO citation END-line changes.

(a) `eliminate_essential_bc.md` — upgrade the opaque `dofs: DofSet[N]` parameter to name its
constructor `[essential_dofs](./essential_dofs.md)` (firm on disk, cycle-066), the same
opaque-parameter replace-and-propagate class as the c065 `fe_space` pass. The upgrade lands in the
**prose shape-contract bullet (`:68`)**, NOT inside the ` ```text ` signature fence (`:56`) — the
c065 precedent (`fe_assemble.md:60` bare vs `:67-68` linked) keeps the signature fence free of
markdown links (a link inside a code fence renders literally).

(b) `fe_space.md:39` + `:149` — upgrade the two "forward-reference until on disk" notes for the
`fe-space-construction-rotation` L1>L0 theme to live links (the theme is firm on disk). Skill
`upgrade-plain-text-ref-to-live-link-when-target-on-disk`.

`eliminate_rhs.md` was JUDGED and gets **no link** — see §Discipline notes (the masking-projection
framing does not name a typed dof-set object).

## Proposed changes

### (a) eliminate_essential_bc.md — name the `essential_dofs` constructor (prose bullet only)

```edit:book/src/L1/eliminate_essential_bc.md
[old]: - `dofs` — `DofSet[N]` — the essential (Dirichlet) true-dof index set, a subset of `0..N` over the
  true-dof axis [`fe_space`](./fe_space.md) defines. At L0 the `mfem::Array<int> dbc_tdof_list`
  recorded by `SetEssentialTrueDofs` (`palace/linalg/rap.cpp:45-46`).
[new]: - `dofs` — `DofSet[N]` — the essential (Dirichlet) true-dof index set, a subset of `0..N` over the
  true-dof axis [`fe_space`](./fe_space.md) defines; the `DofSet[N]` constructed by
  [`essential_dofs`](./essential_dofs.md) (the firm `(space, bdr_attrs, bdr_attr_max) → DofSet[N]`
  boundary-attribute → essential-true-dof-set construction). At L0 the `mfem::Array<int> dbc_tdof_list`
  recorded by `SetEssentialTrueDofs` (`palace/linalg/rap.cpp:45-46`).
```

The ` ```text ` signature fence (`:56`, `dofs: DofSet[N]`) is intentionally left bare — links do
not render inside code fences; the c065 `fe_assemble`/`fe_space` precedent keeps the cross-ref in
prose.

### (b) fe_space.md — upgrade two `fe-space-construction-rotation` forward-references to live links

```edit:book/src/L1/fe_space.md
[old]: This chapter is defined in L1 vocabulary (the typed `(mesh, collection) → space` construction). The
forward rewrite into the L0 ctor + the `ConstructFiniteElementSpaceHierarchy` coarse-seed is the L1>L0
theme `fe-space-construction-rotation` (authored cycle-064 D3; forward-reference until on disk).
[new]: This chapter is defined in L1 vocabulary (the typed `(mesh, collection) → space` construction). The
forward rewrite into the L0 ctor + the `ConstructFiniteElementSpaceHierarchy` coarse-seed is the L1>L0
theme [`fe-space-construction-rotation`](../L1-L0/fe-space-construction-rotation.md) (authored cycle-064 D3).
```

```edit:book/src/L1/fe_space.md
[old]: The L1>L0 rotation `fe-space-construction-rotation` (cycle-064 D3) narrates how the typed
`(mesh, collection) → FiniteElementSpace[N]` construction rewrites into the L0 variadic ctor
(`fespace.hpp:67-75`) forwarding into `mfem::ParFiniteElementSpace`, and into the
`ConstructFiniteElementSpaceHierarchy` coarse-seed (`multigrid.hpp:89-90`) + `GetEssentialTrueDofs`
extraction (`multigrid.hpp:98-99`, via `mesh::AttrToMarker` `:97-98`). (Forward-reference until that
theme is on disk.)
[new]: The L1>L0 rotation [`fe-space-construction-rotation`](../L1-L0/fe-space-construction-rotation.md)
(cycle-064 D3) narrates how the typed
`(mesh, collection) → FiniteElementSpace[N]` construction rewrites into the L0 variadic ctor
(`fespace.hpp:67-75`) forwarding into `mfem::ParFiniteElementSpace`, and into the
`ConstructFiniteElementSpaceHierarchy` coarse-seed (`multigrid.hpp:89-90`) + `GetEssentialTrueDofs`
extraction (`multigrid.hpp:98-99`, via `mesh::AttrToMarker` `:97-98`).
```

## Discipline notes

**What changed and why.**
- (a) The `eliminate_essential_bc` `dofs: DofSet[N]` parameter was an opaque typed input with no
  constructor home. `essential_dofs` (firm on disk, cycle-066; signature
  `essential_dofs :: (space, bdr_attrs, bdr_attr_max) -> DofSet[N]`, `essential_dofs.md:19`) is the
  named constructor of exactly this `DofSet[N]` — `essential_dofs.md:21-24` states it "is the
  `DofSet[N]` that `eliminate_essential_bc` and `eliminate_rhs` consume opaquely — before this entry,
  those two took the essential-dof set as a bare typed parameter with no constructor home." This is
  the same opaque-parameter replace-and-propagate class as the c065 `fe_space` pass on `fe_assemble`.
  Pure prose cross-ref; no signature, decomposition, or law change. Operator stays `firm`.
- The cross-ref deliberately lands in the **prose shape-contract bullet (`:68`)**, NOT inside the
  ` ```text ` signature fence (`:56`). A markdown link inside a code fence renders as literal text;
  the c065 precedent (`fe_assemble.md`) keeps signature line `:60` bare (`FiniteElementSpace[N]`) and
  the live `[fe_space](./fe_space.md)` cross-ref in the `:67-68` prose bullet. I followed that pattern
  exactly. The dispatch scope named "`:56,68`"; the `:56` half is satisfied by the bare typed name in
  the fence (no link there by design) — recorded here so the integrator/critic does not read the
  unedited `:56` as a missed edit.
- (b) Both `fe_space.md` forward-reference notes (`:39`, `:149`) named the L1>L0 theme as plain text
  with a "(forward-reference until on disk)" / "(Forward-reference until that theme is on disk.)"
  caveat. The theme `book/src/L1-L0/fe-space-construction-rotation.md` is firm on disk (verified:
  `ls` 11759 bytes, Jun 2 08:46). Skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`
  applied: plain text → live link, and the now-stale "forward-reference until on disk" caveat dropped
  in both notes (it is false once the link is live). No other text in either note changed.

**`eliminate_rhs.md` judgment — NO LINK (recorded per dispatch directive).** The dispatch asked me
to add an `essential_dofs` cross-ref to `eliminate_rhs.md` ONLY IF the essential-dof set is named
there as a typed `DofSet` object, and explicitly warned NOT to manufacture a link where the text uses
masking projections. **I judge NO link is warranted.** `eliminate_rhs.md` never carries the
essential-dof set as a typed `DofSet[N]` parameter: its signature (`:51-57`) takes
`(K, x_bc, b, policy)` — no dof-set argument. The essential dofs enter only through the
`restrict_essential` / `set_essential` gather/scatter, which `:79-82` explicitly frames as
"masking projections onto the essential-dof subspace, **not separate L1 spine operators**", and at L0
the dofs appear only as the `dbc_tdof_list` index inside cited `rap.cpp` ranges
(`:62-64,76,80`), never as a typed object the entry constructs or consumes by name. Adding an
`essential_dofs` link here would manufacture a typed-object framing the entry deliberately does not
use (it would also collide with the entry's own anti-mirror posture at `:79-82`). This is exactly the
"masking-projection framing may NOT warrant a link" case the dispatch flagged. Left unchanged.

**Layer-definition discipline.** All edits are L1-internal cross-refs/links narrated in L1
vocabulary; no high→low direction inverted, no lowering prose moved into L1 entries.

## Supporting evidence

- `book/src/L1/essential_dofs.md:19,21-24` — the firm `essential_dofs` constructor signature
  `(space, bdr_attrs, bdr_attr_max) -> DofSet[N]` and its self-statement that it constructs the
  `DofSet[N]` consumed opaquely by `eliminate_essential_bc` and `eliminate_rhs`. Link target (a).
- `book/src/L1/fe_assemble.md:60` (bare signature) vs `:67-68` (live `[fe_space](./fe_space.md)`
  prose cross-ref) — the c065 opaque-parameter replace-and-propagate precedent governing where the
  link lands (prose, not fence).
- `book/src/L1-L0/fe-space-construction-rotation.md` — firm on disk (11759 bytes, verified `ls`).
  Link target (b).
- `book/src/L1/eliminate_essential_bc.md:56,68` — the `DofSet[N]` parameter loci (signature fence +
  prose bullet).
- `book/src/L1/fe_space.md:37-39,143-150` — the two forward-reference notes upgraded.
- `book/src/L1/eliminate_rhs.md:51-57,79-82` — the masking-projection framing that warrants NO link
  (judgment recorded above).

## Open questions / caveats

- **No open structural questions.** Both deliverables are pure prose cross-ref/link upgrades against
  firm on-disk targets; nothing here required content decisions beyond the explicit `eliminate_rhs`
  link/no-link judgment, which the dispatch delegated to lifter judgment and which I recorded with its
  supporting citations. No abstractor reread is implied.
- **Citation END lines unchanged.** Per role-spec §Discipline (recurrence-6 close-brace
  `--anchor`-blind-spot), I changed no `path:lo-hi` END line — every edit is prose cross-ref text. The
  only `path:lo-hi` citations in the edited regions (`palace/linalg/rap.cpp:45-46` in the (a) bullet;
  the `fespace.hpp:67-75` / `multigrid.hpp:89-90,98-99,97-98` cites in the (b)#2 note) are carried
  through verbatim, untouched — no END-line re-anchor was needed or made, so no on-disk END-line
  re-Read was required.
- **No index-cell touch** — no `## Status` flip in any of the three entries (all stay `firm`), so per
  the index-table-status-cell guard there is no `L1/index.md` row status-cell to update.
- **`:56` signature-fence non-edit is intentional, not a miss** (restated for the critic): the
  dispatch named `:56,68` but the c065 precedent puts the link in prose only; the `:56` fence stays
  bare by design. Flagged here so the unedited `:56` is not read as a dropped deliverable.
