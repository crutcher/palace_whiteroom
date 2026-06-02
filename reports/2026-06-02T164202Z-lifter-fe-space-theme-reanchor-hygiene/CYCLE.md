---
agent: lifter
invoked_at: 2026-06-02T16:48:30Z
scope: L1>L0 theme-layer re-anchor to firm fe_space (2 themes) + fe_space.md citation hygiene
status: integrated
integrated_at: 2026-06-02T194500Z
integration_commit: 062ae9e
integration_notes: "cycle-066 D3. fe_space-consumer THEME-LAYER re-anchor (fe-operator-assemble-mutation-rotation + weak-form-term-rotation -> live fe_space; completes replace-and-propagate begun at operator surface c065 D1) + multigrid.hpp:22-72->:22-73 close-brace hygiene at 3 fe_space.md loci (:84/:182/:203). All 3 targets stay firm (no status flip). CLOSED 2 OQs (theme-reanchor + multigrid-hpp-citation-hygiene); appended 1 follow-on OQ (forward-ref live-link upgrade). citecheck --scan 8 ok / 0 failing. No count change. Build clean; no build-repair."
inputs:
  - book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
  - book/src/L1-L0/weak-form-term-rotation.md
  - book/src/L1/fe_space.md
  - reference/palace/palace/fem/multigrid.hpp (L0 verification of ConstructFECollections template close)
---

# CYCLE: Re-anchor FE-space themes to firm `fe_space` + `multigrid.hpp:22-72→:22-73` hygiene

## Summary
Two bundled surgical clean-closes on already-firm content. **Close (a)** completes the
replace-and-propagate at the **theme layer** for the now-firm `book/src/L1/fe_space.md` (harvested
c064; operator-surface re-anchor done c065 D1). The OQ
`fe-space-opaque-param-l1-l0-theme-reanchor-to-firm-fe-space` asserted "4 consumer themes," but the
planner's on-disk verification (which I reconfirmed) shows only **2** L1>L0 theme files carry an
abstract FE-space reference: `fe-operator-assemble-mutation-rotation.md` and
`weak-form-term-rotation.md` (the BC-elimination legs are folded INTO the assemble theme — there are
no separate `eliminate-*` L1>L0 theme files). Re-anchor those 2 abstract references to live
`fe_space` cross-refs and close the OQ at the corrected denominator of 2. **Close (b)** fixes a
line-number citation drift in `fe_space.md`: `ConstructFECollections` is cited as
`multigrid.hpp:22-72` at three loci, but the on-disk template close is `:73` (body `return fecs;` at
`:72`, closing `}` at `:73`) — correct `:22-72` → `:22-73`. No structural, status, law, or signature
change to any file.

## On-disk verification performed (Read tool, NOT codemap)

- `reference/palace/palace/fem/multigrid.hpp` lines 70-76, read directly:
  - `:70` `std::reverse(fecs.begin(), fecs.end());`
  - `:71` (blank)
  - `:72` `return fecs;`
  - `:73` `}`  ← template close of `ConstructFECollections`
  - `:75` next construct (`ConstructFiniteElementSpaceHierarchy` comment)
  Confirms `:22-73` is the correct full-template range (`:22-72` truncates the closing brace).
- `python3 tools/citecheck/citecheck.py palace/fem/multigrid.hpp:22-73 --anchor ConstructFECollections`
  → `[ok]` (anchor `ConstructFECollections` at line 25 within range 22-73).
- `grep -n "multigrid.hpp:22-72" book/src/L1/fe_space.md` → **three** occurrences: lines 84, 182, 203
  (the dispatch flagged 84 + 182; 203 carries the same drifted range and is corrected in the same
  pass for consistency).
- `book/src/L1-L0/weak-form-term-rotation.md` `space` mentions: only `A(space, ·)` (`:98`) is the
  abstract opaque-space reference; `:105/:133/:144/:148` are descriptive/L0 uses ("the same space",
  "H1 space", "the space the BilinearForm is built over") and are NOT re-anchor targets.
- `book/src/L1/fe_space.md` exists on-disk (firm, c064); `book/src/L1-L0/fe-space-construction-rotation.md`
  also exists on-disk — so the `fe_space.md` forward-reference at `:39`/`:149` is now resolvable, but
  that is out of scope for this dispatch (operator-entry edit, not a theme re-anchor) and is left
  untouched.

## Proposed changes

### Close (a) — theme 1: `fe-operator-assemble-mutation-rotation.md` re-anchor

The §"L1 form (LHS)" prose says the operator "consumes a finite-element space" abstractly; re-anchor
to the live `fe_space` cross-ref.

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: The LHS is the now-firm L1 operator [`fe_assemble`](../L1/fe_assemble.md) (landed cycle-054). It
consumes a finite-element space and an **immutable list of weak-form terms** (each term a
`(coefficient, differential-operator)` pair naming a bilinear weak-form contribution `a_i(u, v)`),
and produces a fresh global linear operator. Nothing is mutated; there is no container built up in
place, no sub-operator accumulator, no finalize step.
[new]: The LHS is the now-firm L1 operator [`fe_assemble`](../L1/fe_assemble.md) (landed cycle-054). It
consumes a finite-element space — the firm [`fe_space`](../L1/fe_space.md) value
`fe_space(mesh, collection) :: FiniteElementSpace[N]` (the substrate that *defines* the true-dof axis
`N`) — and an **immutable list of weak-form terms** (each term a
`(coefficient, differential-operator)` pair naming a bilinear weak-form contribution `a_i(u, v)`),
and produces a fresh global linear operator. Nothing is mutated; there is no container built up in
place, no sub-operator accumulator, no finalize step.
```

§"What lifts cleanly vs. what needs new vocabulary" carries a now-stale "no L1 form yet" claim for
the FE space — `fe_space` IS that L1 form (firm c064). Bounded prose-correction (see §Discipline
notes): the FE space is no longer un-lifted spine vocabulary; it now has its firm L1 home, and the
remaining new-vocabulary item is the weak-form term, not the space.

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: - The **FE space** itself (`FiniteElementSpace`) — the dof-numbering / mesh-topology object — is a
  whole sub-thread (`book/src/L0/fespace-file.md` exists at L0; no L1 form yet).
[new]: - The **FE space** itself (`FiniteElementSpace`) — the dof-numbering / mesh-topology object — now
  has its firm L1 home [`fe_space`](../L1/fe_space.md) (firm c064; the `(mesh, collection) →
  FiniteElementSpace[N]` construction that defines the true-dof axis `N` every `[N]`-indexed operand
  shares), lowering to L0 via the `fe-space-construction-rotation` L1>L0 theme. The dof-numbering /
  ordering / conformity internals stay MFEM-owned-read-as-given (see `fe_space` §"MFEM-owned");
  `book/src/L0/fespace-file.md` is the L0 localization.
```

### Close (a) — theme 2: `weak-form-term-rotation.md` re-anchor

The one abstract opaque-space reference is `A(space, ·)` in §"The identity-lowers / kernel-opaque
split". Re-anchor the `space` argument to the live `fe_space` cross-ref (matching the fan-out note in
`fe_space.md:160`: "`weak_form_term` — `A(space, ·)` over an opaque `space` cross-refs `fe_space`").
The KERNEL `A` stays libCEED-opaque — only its `space` argument is de-opaqued; no change to the
obstruction classification.

```edit:book/src/L1-L0/weak-form-term-rotation.md
[old]: - **The term's KERNEL stays OPAQUE (lowers elsewhere, as an obstruction).** *How* a term's integrand
  `(Q · 𝒟u, 𝒟v)` is evaluated — the element-local quadrature contraction + dof restriction performed by the
  integrator's `Assemble` method — is the libCEED-owned opaque map. It is already classified as the
  `opaque-library-ownership` obstruction [`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md)
  (c055), identical across all 5 solver pipelines. It does NOT lower through this theme; this theme stops at the
  registration call.
[new]: - **The term's KERNEL stays OPAQUE (lowers elsewhere, as an obstruction).** *How* a term's integrand
  `(Q · 𝒟u, 𝒟v)` is evaluated — the element-local quadrature contraction + dof restriction performed by the
  integrator's `Assemble` method — is the libCEED-owned opaque map `A(space, ·)` over the firm
  [`fe_space`](../L1/fe_space.md) (the `space` argument is the de-opaqued FE-space value; only the
  realization `A` stays library-owned). It is already classified as the
  `opaque-library-ownership` obstruction [`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md)
  (c055), identical across all 5 solver pipelines. It does NOT lower through this theme; this theme stops at the
  registration call.
```

### Close (b) — `fe_space.md` citation hygiene `:22-72` → `:22-73` (three loci)

```edit:book/src/L1/fe_space.md
[old]: The **collection order schedule** itself (`ConstructFECollections`, `palace/fem/multigrid.hpp:22-72`)
[new]: The **collection order schedule** itself (`ConstructFECollections`, `palace/fem/multigrid.hpp:22-73`)
```

```edit:book/src/L1/fe_space.md
[old]: `ConstructFECollections` order schedule — `multigrid.hpp:22-72`), `essential_dofs` (the
[new]: `ConstructFECollections` order schedule — `multigrid.hpp:22-73`), `essential_dofs` (the
```

```edit:book/src/L1/fe_space.md
[old]: - `palace/fem/multigrid.hpp:22-72` — `ConstructFECollections` (the deferred order-schedule context):
[new]: - `palace/fem/multigrid.hpp:22-73` — `ConstructFECollections` (the deferred order-schedule context):
```

### OQ close

```edit:scaffolding/open-questions.md
[old]: fe-space-opaque-param-l1-l0-theme-reanchor-to-firm-fe-space
[new]: fe-space-opaque-param-l1-l0-theme-reanchor-to-firm-fe-space [CLOSED c066 D3]
```

(Integrator: apply the close marker per the ledger's actual close convention; the OQ is resolved —
denominator corrected from 4 to 2, both consumer themes re-anchored. If the ledger entry text
differs from the slug stub above, match the on-disk OQ wording when marking it closed.)

## Discipline notes

- **Pure lifter re-anchor + hygiene; no restructuring.** No `## Status` line, frontmatter status,
  algebraic law, or signature was touched in any of the three files. Both themes remain `firm`;
  `fe_space.md` remains `firm`. No index-table status cell flips (no status change), so the
  index-cell anti-drift guard does not apply this dispatch.
- **Bounded L0-evidenced prose-correction** (recorded per the `lifter-scope-content-correction-boundary`
  in-scope rule): the `fe-operator-assemble-mutation-rotation.md:228` claim "`book/src/L0/fespace-file.md`
  exists at L0; **no L1 form yet**" is a now-false statement — `book/src/L1/fe_space.md` exists firm
  on-disk (c064; verified by `ls`). The correction is (i) directly supported by the on-disk existence
  of the firm L1 entry I read, (ii) bounded (fixing a stale "no L1 form" claim, not re-architecting
  the theme's decomposition), and (iii) recorded here. It is the natural completion of the same
  re-anchor: the theme's "needs new vocabulary" list should no longer name the FE space as un-lifted.
- **Re-anchor scope is the THEME layer.** The c065 D1 operator-surface re-anchor handled the L1
  *operator* entries' bare typed parameters; this dispatch handles the two L1>L0 *theme* files'
  abstract space references. The `weak-form-term-rotation.md` `A(space, ·)` re-anchor matches the
  `fe_space.md:160` fan-out note's prescription verbatim (cross-ref the opaque `space`, leave the
  realization map `A` library-owned).
- **Denominator correction recorded.** The OQ's "4 consumer themes" overcounted by treating the two
  BC-elimination legs as separate L1>L0 theme files; on-disk they are folded into
  `fe-operator-assemble-mutation-rotation.md` (no `eliminate-*` theme files exist). The real
  denominator is 2; both are re-anchored, so the OQ closes complete.

## Supporting evidence

- `book/src/L1/fe_space.md` — firm L1 entry harvested c064 (`harvested_by:
  harvester:2026-06-02T151056Z-harvester-fe-space`); its §"Downward (to L0)" fan-out note (`:152-164`)
  is the replace-and-propagate forward-look this dispatch enacts at the theme layer.
- `reference/palace/palace/fem/multigrid.hpp:70-73` — on-disk `ConstructFECollections` template close
  (`return fecs;` `:72`, `}` `:73`); the L0 ground for the `:22-72`→`:22-73` hygiene fix.
- `tools/citecheck/citecheck.py palace/fem/multigrid.hpp:22-73 --anchor ConstructFECollections` → `[ok]`.
- c065 D1 (operator-surface re-anchor) — the prior half of the replace-and-propagate this completes.

## Open questions / caveats

- **None blocking.** Both re-anchors are pure vocabulary substitutions matching the firm `fe_space`
  entry's own prescribed fan-out; the hygiene fix is a confirmed off-by-one line correction. No
  signature/law contradiction surfaced that would require an abstractor reread.
- **Out-of-scope adjacent (flagged, not enacted):** `fe_space.md:39` and `:149` carry a
  "forward-reference until [`fe-space-construction-rotation`] on disk" note, but that theme file now
  exists on-disk (`book/src/L1-L0/fe-space-construction-rotation.md`). Upgrading those two
  plain-text/forward-reference mentions to live links is an *operator-entry* edit (and an on-disk→
  live-link upgrade, skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`), outside this
  theme-re-anchor dispatch's scope — recommend a follow-on touch (or fold into the next `fe_space`
  hygiene pass). Not actioned here to keep this dispatch surgical to the OQ's two closes.
