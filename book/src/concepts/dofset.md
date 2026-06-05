---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/linalg/rap.hpp:35-36
      kind: cites-evidence
    - target: palace/linalg/rap.cpp:36-47
      kind: cites-evidence
    - target: palace/fem/multigrid.hpp:92-101
      kind: cites-evidence
  reference:
    - L1/essential_dofs
    - L1/eliminate_essential_bc
    - L1/eliminate_rhs
    - L4/eliminate_bc
    - L1/fe_space
    - concepts/set_subvector_zero
    - concepts/state-stratification
    - concepts/build-time-vs-run-time-stratification
---

# DofSet

> **Kind: `record`.** This page defines the *data shape* of `DofSet[N]` — its field, its
> type and meaning, the construction-vs-run-time stratum it occupies, and the L0 source home
> it mirrors. The *behaviour* over `DofSet[N]` — how `essential_dofs` constructs it and how
> `eliminate_essential_bc` / `eliminate_rhs` consume it — lives in those operator chapters;
> this page does not restate that algebra.

`DofSet[N]` is the **essential (Dirichlet) boundary true-dof index set**: an immutable set of
true-dof indices, a subset of `0 .. N`, over the true-dof axis `N` of a finite-element
[`fe_space`](../L1/fe_space.md). It is the typed value that names *which* degrees of freedom a
Dirichlet boundary condition pins. It is **produced** by [`essential_dofs`](../L1/essential_dofs.md)
(boundary-attribute list → essential-true-dof set) and **consumed opaquely** by the post-assembly
BC-application verb-pair [`eliminate_bc`](../L4/eliminate_bc.md)
([`eliminate_essential_bc`](../L1/eliminate_essential_bc.md) takes it as its `dofs: DofSet[N]`
parameter; [`eliminate_rhs`](../L1/eliminate_rhs.md) uses it to pin essential rows). Three
signature consumers across the L1/L4 entries put it above the ≥2-consumer bar, so it has a
cross-cutting definition home here rather than an in-chapter section.

## One-line semantics

`DofSet[N]` is an immutable index set — the essential true-dof indices on a finite-element space,
tagged by that space's true-dof axis `N`. It is a **value over** the space (an opaque index
structure), NOT an operation: it carries no algebra of its own; the constructor and the BC verbs
supply all behaviour.

## Record definition

`DofSet[N]` is a single-component record: a set of integer true-dof indices parameterised by the
axis size `N`. The TS brace form (the whole record readonly, construction-stratum):

```text
DofSet[N] = {
  indices : Set<TrueDofIndex>   -- the essential true-dof indices; each in 0 .. N
}
```

| field | type | meaning | stratum | L0 source |
|---|---|---|---|---|
| `indices` | `Set<TrueDofIndex>` (a subset of `0 .. N`) | the essential (Dirichlet) true dofs to pin — every true dof of `fe_space` lying on a boundary facet whose attribute was marked essential | readonly construction | backing member `mfem::Array<int> dbc_tdof_list` (`palace/linalg/rap.hpp:35-36`); materialized by `essential_dofs` at `palace/fem/multigrid.hpp:99-100` |

The type parameter `N` is the **true-dof axis** `N = fe_space.GetTrueVSize()` — the same `N`
carried by [`fe_space`](../L1/fe_space.md), [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md),
and [`eliminate_rhs`](../L1/eliminate_rhs.md). `N` is a phantom/index tag on the set, not a stored
field: it records *which* space's true-dof numbering the indices index into (the same attribute
list yields different sets on H1 vs H(curl) spaces, so the set is not meaningful detached from its
`N`). The set carries no ordering or multiplicity semantics beyond membership; at L0 it is stored
as a sorted `mfem::Array<int>` of distinct true-dof indices.

**Empty-set representation.** `DofSet[N] = ∅` (no essential dofs — e.g. a mesh with no boundary
attributes, or no Dirichlet boundary) is the natural minimal element. At L0 it is the zero-size
`dbc_tdof_list`: the `ParOperator::GetEssentialTrueDofs()` accessor returns `nullptr` exactly when
`dbc_tdof_list.Size() == 0` (`palace/linalg/rap.hpp:87-91`), and the rectangular-operator guard
requires `dbc_tdof_list.Size() == 0` for a non-square operator.

## Stratum — construction-time, readonly

`DofSet[N]` is **construction-stratum and readonly**: it is built **once at assembly-config time**
(when the operator graph is assembled and the boundary conditions are recorded) and **never
mutated at solve/run time**. This is the same construction-vs-run-time split named in
[`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md): the set is
build-time scaffolding the BC verb-pair reads, not a per-iteration run-time value. In the L4 BC
surface it is part of the `readonly` **BC stratum** `(DofSet[N], DiagPolicy)` captured once at
construction (per [`state-stratification`](./state-stratification.md); see
[`eliminate_bc`](../L4/eliminate_bc.md) §Semantics) — the assembled operator `K`, the boundary
data `x_bc`, and the RHS `b` are the per-call operands; the dof set is fixed.

Concretely in Palace: `ParOperator::SetEssentialTrueDofs(tdof_list, policy)` records the set once
by reference (`dbc_tdof_list.MakeRef(tdof_list)`, `palace/linalg/rap.cpp:45`) alongside the
diagonal policy; the subsequent `EliminateBC` / `EliminateRHS` applies read it but never write it.

## L0 source home — the `dbc_tdof_list` backing member

The backing struct member is `mfem::Array<int> dbc_tdof_list` on `ParOperator`
(`palace/linalg/rap.hpp:35-36`; comment "Lists of constrained essential boundary true dofs for
elimination"). Its lifecycle across the L0 surface:

- **Materialized** by `essential_dofs`: `GetEssentialTrueDofs(dbc_marker, dbc_tdof_lists->emplace_back())`
  (`palace/fem/multigrid.hpp:99-100`) writes the true-dof indices into a freshly-emplaced
  `mfem::Array<int>` — the dof set construction (boundary-attribute marker → essential true dofs;
  see [`essential_dofs`](../L1/essential_dofs.md) for the two-stage construction).
- **Recorded by reference** on the operator wrapper:
  `ParOperator::SetEssentialTrueDofs(const mfem::Array<int> &tdof_list, DiagonalPolicy policy)`
  does `dbc_tdof_list.MakeRef(tdof_list)` (`palace/linalg/rap.cpp:45`), guarding `policy ∈
  {DIAG_ONE, DIAG_ZERO}` (`:39-41`) and `height == width` (`:42-43`).
- **Read** by the elimination applies (`EliminateBC` / `EliminateRHS`) and exposed by the
  `GetEssentialTrueDofs()` accessor (`palace/linalg/rap.hpp:87-91`), which returns `nullptr` for
  the empty set.

Backing type note: `mfem::Array<int>` is an MFEM container of true-dof indices read as its
single-rank equivalent (MPI/`Par*`/partitioning out of scope). `DofSet[N]` un-mixes the *index-set
value* from the mutable `ParOperator` wrapper that records it: the wrapper is a deferred-config
state carrier (an L4>L3 lowering concern of `eliminate_bc`); the `DofSet[N]` value itself is the
immutable readonly index set this page defines.

## Signatures that name this record

The ≥2-consumer evidence for the standalone page (three signature consumers):

- [`essential_dofs`](../L1/essential_dofs.md) — the **producer**:
  `essential_dofs :: (space: FiniteElementSpace[N], bdr_attrs: [Attr], bdr_attr_max: Nat) -> DofSet[N]`
  (`book/src/L1/essential_dofs.md:19,62`).
- [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md) — the operator-side consumer; its
  `dofs: DofSet[N]` parameter (the L4 signature `LinearOperator[N,N] -> DofSet[N] -> DiagPolicy ->
  LinearOperator[N,N]`, `book/src/L4/eliminate_bc.md:76-77,100-102`).
- [`eliminate_rhs`](../L1/eliminate_rhs.md) — the RHS-side consumer; uses the set to pin essential
  rows of the adjusted RHS.

The L4 surface [`eliminate_bc`](../L4/eliminate_bc.md) presents the consuming verb-pair as one
chapter; its §Record-definition (`:119-134`) flagged this page as the home
(`record-DofSet-needs-definition-home`).

## See also

- [`essential_dofs`](../L1/essential_dofs.md) — the producer; defines HOW the set is constructed
  (boundary-attribute marker → MFEM `GetEssentialTrueDofs`). This page defines only the *shape* of
  its output.
- [`eliminate_bc`](../L4/eliminate_bc.md) / [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md)
  / [`eliminate_rhs`](../L1/eliminate_rhs.md) — the consumers; define the *behaviour over* the set
  (the BC application algebra). This page does NOT restate that algebra.
- [`set_subvector_zero`](./set_subvector_zero.md) — its `idx: IndexSet` parameter is an **instance
  of this shape**: the essential-dof index set used for in-place BC-enforcement zeroing on a
  residual/RHS. `set_subvector_zero` is the *behaviour* (the zeroing verb); `DofSet[N]` is the
  *index-set value* it operates on.
- [`state-stratification`](./state-stratification.md) — `DofSet[N]` is part of the `readonly` BC
  stratum `(DofSet[N], DiagPolicy)` of the L4 BC surface.
- [`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md) — the
  construction-vs-run-time split this record sits on the build-time side of.
- [`fe_space`](../L1/fe_space.md) — supplies the true-dof axis `N` the set indexes into.

**If this page and a consumer chapter / the L0 source disagree on any factual claim about the
record, the L0 source (`palace/linalg/rap.hpp` / `rap.cpp` / `palace/fem/multigrid.hpp`) wins and
this page is corrected.**

## Status

`firm` — the data shape is a single readonly index-set field backed by the cited
`ParOperator::dbc_tdof_list` member (`palace/linalg/rap.hpp:35-36`), its materialization site
(`palace/fem/multigrid.hpp:99-100`), and its record-by-reference site
(`palace/linalg/rap.cpp:36-47`); the construction-vs-run-time stratum (build-once-at-assembly-config,
readonly-at-solve) is the defining property and is read directly from the positive
`SetEssentialTrueDofs` / `EliminateBC` lifecycle. The record-definition obligation is met: this is
the cross-cutting home for `DofSet[N]`, referenced by ≥2 consumers (`L1/essential_dofs`,
`L1/eliminate_essential_bc`, `L1/eliminate_rhs`, surfaced at `L4/eliminate_bc`). All L0 citations
self-verified against on-disk source this dispatch via codemap `read_range`.

Well-foundedness (rank): the page is a `record` DAG node at `rank: firm`; all its blocking edges
are `cites-evidence depends-on` to L0 source ranges (rank-terminal ground truth), so the
`rank(u) ≤ rank(v)` invariant holds vacuously. The edges to the producer/consumer operator
chapters and the L4 surface are `reference` (navigational — a record page is named-by-use, it does
not block on its consumers).
