---
agent: lifter
invoked_at: 2026-06-02T160332Z
scope: L1 opaque-parameter re-anchor — 4 firm L1 entries → firm fe_space cross-ref (replace-and-propagate from c064 front-opening)
status: integrated
integrated_at: 2026-06-02T190000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-065 (D1). Opaque-parameter operator-surface re-anchor ENACTED: book/src/L1/{fe_assemble,weak_form_term,eliminate_essential_bc,eliminate_rhs}.md re-anchored to firm fe_space via live cross-refs over the true-dof axis N (fespace.hpp:96); all 4 stay firm (no status flip). Build-relevant; cargo make book exit 0. RESOLVES-BY-LANDING the c064 D1/D2 operator-surface re-anchor OQs; opened the NEW theme-layer follow-on OQ fe-space-opaque-param-l1-l0-theme-reanchor-to-firm-fe-space. No gate hits."
inputs:
  - book/src/L1/fe_space.md (firm, cycle-064 — the re-anchor target)
  - book/src/L1/fe_assemble.md (firm — takes space: FiniteElementSpace[N])
  - book/src/L1/weak_form_term.md (firm — A(space,·) folds over the space)
  - book/src/L1/eliminate_essential_bc.md (firm — takes DofSet[N], N from the space)
  - book/src/L1/eliminate_rhs.md (firm — N is the global true-dof count)
  - reference/palace/palace/fem/fespace.hpp:67-75,96 (ctor + GetTrueVSize, on-disk verified)
---

# CYCLE: Re-anchor 4 L1 entries to firm fe_space

## Summary

`fe_space` (`book/src/L1/fe_space.md`) firmed cycle-064 (D4 front-opening), and its own intro
explicitly names the four downstream consumers that "before this entry ... took the FE-space (and
its true-dof axis `N`, and the essential-dof set `DofSet[N]`) as bare opaque typed parameters":
`fe_assemble`, `weak_form_term`, `eliminate_essential_bc`, `eliminate_rhs`. This dispatch is the
replace-and-propagate the c064 D4 §"FE-space sub-spine" subsection deferred to "a later
replace-and-propagate dispatch, NOT this cycle." Each of the four currently carries **zero**
`fe_space.md` links (verified by grep). This is a pure cross-ref firming pass: at each entry's
`space` / `N` / `DofSet[N]` parameter locus I add a live `[fe_space](./fe_space.md)` cross-ref plus a
short "constructed by / defines `N`" clause, firming the bare typed name to a named construction. No
restructuring; no status / law / signature change; all four stay `firm`. The `N`-definition claim is
backed by the on-disk-verified `fespace.hpp:96` (`GetTrueVSize`) and the ctor `fespace.hpp:67-75`,
both already cited inside `fe_space.md` and re-verified this dispatch via `citecheck --anchor`.

## Proposed changes

### 1. `book/src/L1/fe_assemble.md` — `space` shape-contract bullet (the assembly domain/range)

Re-anchor the bare `space — FiniteElementSpace[N]` bullet to the firm `fe_space` construction.

```edit:book/src/L1/fe_assemble.md
[old]: - `space` — `FiniteElementSpace[N]` — the trial/test finite-element space; `N = space.GetTrueVSize()`
  is the global true-dof count (the operator's square dimension). Read-only.
[new]: - `space` — `FiniteElementSpace[N]` — the trial/test finite-element space, constructed by
  [`fe_space`](./fe_space.md) (the firm `(mesh, collection) → FiniteElementSpace[N]` construction);
  `N = space.GetTrueVSize()` (`palace/fem/fespace.hpp:96`) is the global true-dof count (the
  operator's square dimension) — the axis `fe_space` defines. Read-only.
```

### 2. `book/src/L1/weak_form_term.md` — the `A(space, ·)` realization reference

The term's realization is the per-term assembly map `A(space, ·)`, which folds over the space. Anchor
the first prose mention of the space (the slug-context paragraph naming `A(space, ·)`) to `fe_space`.

```edit:book/src/L1/weak_form_term.md
[old]: `weak_form_term` is the **per-term value** the [`fe_assemble`](./fe_assemble.md) fold quantifies over. It is NOT
the assembled operator (that is `fe_assemble`'s result `K = Σ_i A(term_i)`), and it is NOT the per-term assembly
**map** `A(space, ·)` (the element-local quadrature kernel + restriction, libCEED-owned — see *Dependencies*).
[new]: `weak_form_term` is the **per-term value** the [`fe_assemble`](./fe_assemble.md) fold quantifies over. It is NOT
the assembled operator (that is `fe_assemble`'s result `K = Σ_i A(term_i)`), and it is NOT the per-term assembly
**map** `A(space, ·)` (the element-local quadrature kernel + restriction over the finite-element space
[`fe_space`](./fe_space.md) constructs, libCEED-owned — see *Dependencies*).
```

### 3. `book/src/L1/eliminate_essential_bc.md` — the `K` and `dofs` shape-contract bullets

The operator takes `K: LinearOperator[N, N]` and `dofs: DofSet[N]` over the true-dof axis `N` that
`fe_space` defines. Re-anchor the `N`-source on the `K` bullet, and the `DofSet[N]` index-set bullet.

```edit:book/src/L1/eliminate_essential_bc.md
[old]: - `K` — `LinearOperator[N, N]` — an assembled **square** operator over the true-dof axis `N`
  (`N = space.GetTrueVSize()`); the output of [`fe_assemble`](./fe_assemble.md). Read-only;
  squareness is required (essential-BC elimination is defined only for `height == width` — the L0
  guard `palace/linalg/rap.cpp:42-43`, and the rectangular-reject branch
  `palace/linalg/rap.cpp:145-148`).
- `dofs` — `DofSet[N]` — the essential (Dirichlet) true-dof index set, a subset of `0..N`. At L0 the
  `mfem::Array<int> dbc_tdof_list` recorded by `SetEssentialTrueDofs`
  (`palace/linalg/rap.cpp:45-46`).
[new]: - `K` — `LinearOperator[N, N]` — an assembled **square** operator over the true-dof axis `N`
  (`N = space.GetTrueVSize()`, `palace/fem/fespace.hpp:96`); the output of
  [`fe_assemble`](./fe_assemble.md). The axis `N` is defined by the finite-element space
  [`fe_space`](./fe_space.md) constructs. Read-only; squareness is required (essential-BC elimination
  is defined only for `height == width` — the L0 guard `palace/linalg/rap.cpp:42-43`, and the
  rectangular-reject branch `palace/linalg/rap.cpp:145-148`).
- `dofs` — `DofSet[N]` — the essential (Dirichlet) true-dof index set, a subset of `0..N` over the
  true-dof axis [`fe_space`](./fe_space.md) defines. At L0 the `mfem::Array<int> dbc_tdof_list`
  recorded by `SetEssentialTrueDofs` (`palace/linalg/rap.cpp:45-46`).
```

### 4. `book/src/L1/eliminate_rhs.md` — the `K` shape-contract bullet (the true-dof axis `N`)

`eliminate_rhs` takes `K: LinearOperator[N, N]` and `x_bc`/`b: Tensor[N]` over the true-dof count `N`;
the `dbc_tdof_list` essential-dof list indexes that same axis. Re-anchor the `N`-source on the `K`
bullet (the first parameter naming `N`).

```edit:book/src/L1/eliminate_rhs.md
[old]: - `K` — `LinearOperator[N, N]` — the assembled (square) global operator; `N` is the global true-dof
  count. The **unconstrained** operator action is applied (`A->Mult`, the local matrix before
  essential-row elimination — `reference/palace/palace/linalg/rap.cpp:69`). Read-only.
[new]: - `K` — `LinearOperator[N, N]` — the assembled (square) global operator; `N` is the global true-dof
  count `space.GetTrueVSize()` (`reference/palace/palace/fem/fespace.hpp:96`), the axis the
  finite-element space [`fe_space`](./fe_space.md) constructs and defines (the same `N` the essential
  `dbc_tdof_list` indexes). The **unconstrained** operator action is applied (`A->Mult`, the local
  matrix before essential-row elimination — `reference/palace/palace/linalg/rap.cpp:69`). Read-only.
```

## Discipline notes

- **Pure cross-ref firming, no structural change.** Every edit is confined to the shape-contract
  bullet (or the slug-context sentence for `weak_form_term`) that names the bare typed parameter. I
  added a live `[fe_space](./fe_space.md)` link + a short "constructed by / defines `N`" clause at
  each parameter locus. No `## Status` line, signature, algebraic law, or variant axis was touched in
  any of the four. All four remain `firm` (their firmness frontmatter is unchanged).
- **This is the replace-and-propagate (combinator-miner re-mandate: replace-and-propagate, not
  mine-and-strand) set up by c064 D4.** `fe_space` was firmed as the shared FE-space substrate; the
  c064 D4 §"FE-space sub-spine" subsection explicitly deferred re-anchoring the four consumers to "a
  later replace-and-propagate dispatch, NOT this cycle." c065 D1 is that dispatch. `fe_space.md`'s own
  intro (lines 14-17) names exactly these four entries as the consumers that took the FE-space as bare
  opaque parameters — this re-anchor closes that loop.
- **No prose-correction made.** Each entry's `N = space.GetTrueVSize()` claim was already correct and
  already (in `fe_assemble` / `eliminate_essential_bc`) cited; I added the `fespace.hpp:96` pinpoint
  where it strengthened the new cross-ref clause, but corrected no existing claim (this stayed inside
  the bounded cross-ref-firming scope, not the L0-evidence-driven correction carve-out).
- **`weak_form_term` has no `space`/`N`/`DofSet` parameter of its own** (it is an inert
  `(coefficient, diff_op)` pair). Its only space-reference is the realization map `A(space, ·)`. I
  anchored the first prose mention of that map to `fe_space` (the space `A` realizes the term over),
  which is the minimal faithful re-anchor for an entry that references the space only indirectly. This
  is the scope's "`A(space,·)` ... re-anchor the `space` reference" instruction.

## Supporting evidence

- `book/src/L1/fe_space.md` — the firm re-anchor target (cycle-064). Intro lines 14-17 name the four
  consumers; Signature §lines 53-61 define `N = result.GetTrueVSize()` (`palace/fem/fespace.hpp:96`)
  as "the operator that *defines* `N`."
- `reference/palace/palace/fem/fespace.hpp:67-75` — `FiniteElementSpace(Mesh &mesh, T &&...args)`
  ctor (the `(mesh, collection)` pairing). `citecheck --anchor 'FiniteElementSpace'` → ok, anchor at
  `:68` within range.
- `reference/palace/palace/fem/fespace.hpp:96` — `GetTrueVSize()` (the source of `N`).
  `citecheck --anchor 'GetTrueVSize'` → ok, anchor at `:96`.
- grep confirmation: all four target files carried `0` occurrences of `fe_space` before this pass.

## Open questions / caveats

- None blocking. The firmed `fe_space` signature (`(mesh, collection) → FiniteElementSpace[N]`) is
  fully consistent with what all four entries assumed about the bare typed parameter (a
  `FiniteElementSpace[N]` whose `N = GetTrueVSize()`) — no signature contradiction, so this is a pure
  lift, not an abstractor reread.
- Out of this dispatch's scope (flag only, NOT edited here): `fe_assemble.md` §"Downward to L0",
  `eliminate_essential_bc.md` §"Downward to L0", and `eliminate_rhs.md` §"Downward to L0" each note a
  pending lifter re-anchor of their **L1>L0 theme** (`fe-operator-assemble-mutation-rotation` /
  `eliminate-rhs-mutation-rotation`) to the now-firm L1 operators — those are *theme* re-anchors at
  the L1>L0 edge, a separate dispatch from this *operator-cross-ref* pass. Not bundled here (one
  concern per invocation; this dispatch is the FE-space opaque-param cross-ref only).
