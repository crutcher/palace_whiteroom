---
agent: harvester
invoked_at: 2026-06-05T082448Z
scope: L1 homeless-primitive disposition — set_subvector_zero / trsv / gemv_basis
status: pending
inputs:
  - OQ concept-primitive-without-L1-home-trsv-set_subvector_zero-gemv_basis (c103 concept-typing)
  - book/src/concepts/{trsv,set_subvector_zero,gemv_basis}.md (existing concept pages, reference:[] or sideways edges)
  - book/src/L1/back_solve.md (firm c027 — the small-dense triangular-solve sibling)
  - book/src/L1-L0/triangular-solve-obstruction.md (the trsv obstruction theme, c028)
  - book/src/L1/{orthogonalize,eliminate_essential_bc,eliminate_rhs}.md
  - book/src/L2/linear_combination.md (the variadic scalar-weighted-vector-sum fold)
  - palace/linalg/vector.{hpp,cpp} (SetSubVector family), orthog.hpp (CGS/MGS), divfree.cpp / gmg.cpp / distrelaxation.cpp (use-sites)
integrated_at: 2026-06-05T093000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-104 D3, applied clean post-repair (staging row 3/4). NEW firm L1 entry book/src/L1/set_subvector_zero.md (the s=0.0 SetSubVector index-set vector-zeroing primitive, diagonal 0/1 projector Z_idx=I-P_idx; 3 cites-evidence depends-on -> vector.cpp:461-474/:476-492/vector.hpp:220-221; firm-on-positive-structure). Repairer had repaired 2 build-critical warnings pre-integration (dangling depends-on to forthcoming L1>L0 theme retyped to L0 cites; dangling reference to speculative L3 seed removed). SUMMARY + L1-index dep-map alpha-after scal; trsv + gemv_basis repointed. Resolves all 3 legs of OQ concept-primitive-without-L1-home-trsv-set_subvector_zero-gemv_basis. finalize updated the L1 firm-count narration 32 main/39 grand -> 33 main/40 grand (count-owner, D3 deferred it). rank_violations held 0; build EXIT 0."
---

# CYCLE: Disposition of three homeless concept-primitives at L1 — set_subvector_zero / trsv / gemv_basis

## Summary

The c103 concept-typing surfaced three concept pages (`concepts/{trsv, set_subvector_zero,
gemv_basis}.md`) with **no `L1/<name>.md` home**, leaving their typed `edges:` blocks as
`reference: []` or pointing sideways. This dispatch audits each against Palace source
(audit-first: do NOT manufacture operators that don't exist) and lands the honest disposition.

The three split cleanly into three different dispositions:

1. **`set_subvector_zero` → AUTHOR `L1/set_subvector_zero.md` (firm).** It is a genuine,
   heavily-reused Palace primitive with a positive L0 site: `linalg::SetSubVector(x, rows, 0.0)`
   — the `s = 0.0` specialization of the scalar-set overload declared `vector.hpp:221`, defined
   real `vector.cpp:461-474` + complex `:476-492`. ~40 call sites zero a vector's essential/port
   true-dofs (divfree, gmg restriction-residual, distrelaxation, spaceoperator RHS-clean, waveport,
   curlcurl, romoperator). It is the **vector-side** BC-cleanup primitive — distinct from the
   already-firm matrix-side `eliminate_essential_bc` (`EliminateBC` on an assembled operator) and
   from `eliminate_rhs` (the affine RHS-lift `b − K·x_bc`); both of those *consume* this vector
   primitive. New firm L1 entry, typed `edges:` from the start, alpha-wired into SUMMARY + L1 index.

2. **`trsv` → KEEP CONCEPT-ONLY, REPOINT (no new file).** The disposition is already fully
   settled in the artifact: a general triangular-solve has **no positive Palace L0 site** — it is
   the `triangular-solve-obstruction` L1>L0 theme (c028, `obstruction`), and the one positively-
   anchored triangular component Palace *does* implement is the firm small-dense `back_solve`
   (c027). The `trsv` concept page's `reference: []` is repointed to those two existing nodes
   (the obstruction theme = the resolution; `back_solve` = the sibling). No L1 operator is
   manufactured — that would violate CLAUDE.md §Scope (unimplemented Palace components are not
   direct implementation targets). The planner's suggested `L1/back_solve` exists and is the
   correct sibling target; there is no `L1/back_solve` ambiguity.

3. **`gemv_basis` → KEEP CONCEPT-ONLY, REPOINT.** It has **no standalone callable** in Palace:
   its only L0 referent is the inline CGS basis-correction loop `for j: w.Add(-H[j], V[j])`
   (`orthog.hpp:71-74`) inside `OrthogonalizeColumnCGS` — already covered by the firm
   `L1/orthogonalize`. The *batched fold* `w + α·Σ H[j]·V[j]` is conceptually a specialization of
   the L2 `linear_combination` fold (the variadic scalar-weighted vector sum), realised as an
   unfolded loop of `axpy`, never as a fused BLAS-2 `gemv`. So it stays a concept (a derived
   fold-shape note), with its `reference` edge extended to point at `L2/linear_combination` (the
   fold home) and `L1/orthogonalize` (the L0-anchored consumer) alongside the existing
   `concepts/orthogonalization`.

Net new book node: **one** firm L1 operator (`set_subvector_zero`). Two concept-page edge
repoints. OQ `concept-primitive-without-L1-home-trsv-set_subvector_zero-gemv_basis` resolved.

## Proposed changes

```new:book/src/L1/set_subvector_zero.md
---
layer: L1
operator: set_subvector_zero
rank: firm
edges:
  depends-on:
    # A firm L1 operator's blocking dependency is its POSITIVE L0 SOURCE (rank-terminal
    # ground truth), not the not-yet-authored L1>L0 lowering theme. Repaired cycle-104
    # (repairer): the `firm` rank rests on the read-in-full L0 bodies + decl below, so the
    # well-foundedness invariant rank(u) ≤ rank(v) holds against rank-terminal evidence.
    - kind: cites-evidence
      target: palace/linalg/vector.cpp:461-474   # real SetSubVector body (X[id]=sr at :472)
    - kind: cites-evidence
      target: palace/linalg/vector.cpp:476-492   # complex body (XR[id]=sr :489, XI[id]=0.0 :490)
    - kind: cites-evidence
      target: palace/linalg/vector.hpp:220-221   # the `double s` SetSubVector declaration
  reference:
    - L1/eliminate_essential_bc
    - L1/eliminate_rhs
    - L1/divfree-projector
    - concepts/set_subvector_zero
# The L1>L0 lowering theme `set-subvector-zero-mutation-rotation` is forthcoming (not yet
# authored); it is a plain-text "(forthcoming)" note in §Downward, NOT a blocking depends-on
# edge to a missing file (would be a linkcheck2 hard error + rank-invariant violation).
# The speculative L3 form `set-subvector-zero-mask-multiply` is a plain-text future-form note
# in §Downward, NOT a live reference edge (the seed does not exist).
---

# set_subvector_zero

Mutation-lifted index-set vector zeroing: `x' = set_subvector_zero(x, idx)` returns a fresh
vector equal to `x` with every entry at an index in `idx` set to zero, and every other entry
unchanged. The pure-functional lift of Palace's `linalg::SetSubVector(x, rows, 0.0)` — the
`s = 0.0` specialization of the index-set scalar-set primitive. The **vector-side** essential /
port boundary-condition cleanup atom: it zeros the Dirichlet/essential/port true-dofs of a
residual, RHS, or correction vector so that the value lives in the free-dof subspace before (or
after) a linear solve.

## Context

`set_subvector_zero` lifts the single most reused vector-cleanup call in Palace's linear-algebra
layer. The backing primitive is the `double`-valued `SetSubVector` overload — declared once over
both `Vector` and `ComplexVector` (`palace/linalg/vector.hpp:220-221`, "Sets all entries of the
vector corresponding to the given indices to the given (real) value") and defined twice:

- **real** `SetSubVector(Vector &x, const mfem::Array<int> &rows, double s)`
  (`palace/linalg/vector.cpp:461-474`) — a `forall` over `rows` writing `X[id] = sr`
  (`:472`);
- **complex** `SetSubVector(ComplexVector &x, const mfem::Array<int> &rows, double s)`
  (`palace/linalg/vector.cpp:476-492`) — a `forall` writing `XR[id] = sr` (`:489`) and
  `XI[id] = 0.0` (`:490`).

This entry covers the **`s = 0.0`** call shape specifically — the dominant call form (the entry
appears ~40 times in the tree, the overwhelming majority with literal `0.0`). The non-zero scalar
form (`SetSubVector(diag, dofs, 1.0)`, `rap.cpp:186`; `SetSubVector(tE0t, …, 1.0)`,
`waveportoperator.cpp:73`) is the general index-set scalar-set, of which this is the zeroing
specialization; the zeroing-specific name is what signals BC-enforcement intent at the call site
(the concept page [`concepts/set_subvector_zero`](../concepts/set_subvector_zero.md) makes this
naming distinction). Note that in the **complex** case the zeroing sets BOTH the real and
imaginary parts of each indexed dof to zero (`:489-490` with `sr = 0`), so
`set_subvector_zero` zeros the whole complex dof, not just its real part.

The canonical use-sites span the whole solver surface:

- **divfree projector**: `linalg::SetSubVector(rhs, *bdr_tdof_list_M, 0.0)`
  (`palace/linalg/divfree.cpp:173`) — zero the H1 RHS on the boundary true-dofs before the inner
  `ksp->Mult(rhs, psi)` so the projected system `M·ψ = rhs` respects the essential BC. This is the
  use-site the [`divfree-projector`](./divfree-projector.md) chapter's dep-map already names as
  `set_subvector_zero (concept)` — now a live L1 node.
- **geometric-multigrid restriction residual**: `linalg::SetSubVector(X[l-1],
  *dbc_tdof_lists[l-1], 0.0)` (`palace/linalg/gmg.cpp:194`) — zero the restricted residual on the
  coarse-level essential dofs between V-cycle levels.
- **distributive relaxation**: `linalg::SetSubVector(x_G, *dbc_tdof_list_G, 0.0)`
  (`palace/linalg/distrelaxation.cpp:114` and `:143`) — zero the auxiliary-space correction on
  its essential dofs.
- **per-ω driven RHS clean**: `linalg::SetSubVector(RHS, nd_dbc_tdof_lists.back(), 0.0)`
  (`palace/models/spaceoperator.cpp:945,959,1031`) — zero the assembled driven RHS on the
  Nedelec essential true-dofs.

`set_subvector_zero` is the vector-side companion of two firm matrix/RHS-side BC operators that
**consume** it:

- [`eliminate_rhs`](./eliminate_rhs.md) (firm c055) — the affine RHS-lift `b' = b − K·x_bc` with
  the essential rows pinned; its essential-dof pin is exactly a `set_subvector_zero` on the
  essential dofs (the `eliminate_rhs` chapter already names `set_subvector (concept)` at
  `palace/linalg/rap.cpp:64,76,80`).
- [`eliminate_essential_bc`](./eliminate_essential_bc.md) (firm c055) — the **matrix-side**
  `EliminateBC` row/column zeroing on an assembled square operator; the operator analog of this
  vector primitive (zeros operator entries, not vector entries — a distinct, higher-arity
  operation that does not reduce to `set_subvector_zero`).

## Signature

```text
set_subvector_zero :: (x: Tensor[N], idx: DofSet[N]) -> Tensor[N]

set_subvector_zero(x, idx) = the y with  y[i] = 0  (i in idx),  y[i] = x[i]  (i not in idx)
```

Shape contract (bunsen-style, named axes):

- `x` — `Tensor[N]` — the input vector over the dof axis `N` (a true-dof vector: residual, RHS,
  or correction). Read on entry. The element type is the **element-type variant axis** (real
  `Vector` | complex `ComplexVector`); in the complex case the whole complex dof is zeroed
  (real and imaginary parts both, `vector.cpp:489-490`).
- `idx` — `DofSet[N]` — the index set whose entries are zeroed: a subset of `0..N` over the same
  dof axis (the `mfem::Array<int> rows` argument, `vector.cpp:461`). Read-only; not mutated. In
  the BC-enforcement use-sites this is an essential / port Dirichlet true-dof set (the `DofSet[N]`
  constructed by [`essential_dofs`](./essential_dofs.md)), but the operator is agnostic to the
  set's provenance.
- result — `Tensor[N]` — a fresh vector equal to `x` outside `idx` and zero on `idx`. Same shape
  and element type as `x`.

The empty index set (`idx = ∅`) is the identity (`set_subvector_zero(x, ∅) = x`; the `forall`
over zero rows does nothing). The full index set (`idx = 0..N`) yields the zero vector.

## Semantics

`set_subvector_zero(x, idx)` returns the vector obtained from `x` by setting to zero every entry
whose index is in `idx`, leaving all other entries unchanged. It is the **linear projector**
`Z_idx : Tensor[N] → Tensor[N]` that annihilates the `idx` coordinates and is the identity on
their complement:

```text
(Z_idx · x)[i] = 0       if i ∈ idx
(Z_idx · x)[i] = x[i]     if i ∉ idx
```

Equivalently `Z_idx = I − P_idx`, where `P_idx` is the diagonal 0/1 projector onto the `idx`
coordinates. (This is the same diagonal free-dof projection `P_F` that the matrix-side
[`eliminate_essential_bc`](./eliminate_essential_bc.md) applies as `K ↦ P_F K P_F`; here it is
applied to a vector on one side.)

The L1 form is pure-functional: the same `(x, idx)` yields the same result, with no destination
buffer. The L0 source overwrites `x` in place (the destination *is* the input argument:
`x.ReadWrite(use_dev)`, `vector.cpp:467`; the `forall` writes `X[id] = sr` with `sr = 0`), and
in the complex case threads the real and imaginary device buffers separately
(`XR`/`XI`, `:483-484`). The in-place overwrite, the device-vs-host `use_dev` dispatch, the
`rows.Read(use_dev)` index gather, and the `mfem::forall_switch` kernel are **L1>L0 lowering
concerns** (the `set-subvector-zero-mutation-rotation` theme, forthcoming — plain-text forward
reference, not yet authored), not part of the L1 signature.

The per-index writes are **independent** — each `X[id]` write reads no other entry — so there is
no sequential dependency across the `i ∈ idx` updates and **no reduction**. This is what makes
the operation a clean diagonal projector with the laws below; it is also why the L3 lift is a
direct mask-multiply with no obstruction (see *Downward*).

## Algebraic laws

The laws below hold; absences are deliberate. `Z_idx` denotes `set_subvector_zero(·, idx)`.

1. **Idempotence.** `set_subvector_zero(set_subvector_zero(x, idx), idx) =
   set_subvector_zero(x, idx)`. After zeroing the `idx` entries they are already zero; re-zeroing
   the same set is the identity. `Z_idx ∘ Z_idx = Z_idx` — `Z_idx` is a projector.

2. **Linearity.** `set_subvector_zero(α·x + β·y, idx) = α·set_subvector_zero(x, idx) +
   β·set_subvector_zero(y, idx)` for scalars `α, β`. `Z_idx = I − P_idx` is a linear map (a fixed
   diagonal 0/1 matrix). In particular `set_subvector_zero(0, idx) = 0`.

3. **Empty / full boundary.** `set_subvector_zero(x, ∅) = x` (identity; the `forall` over zero
   rows is a no-op, `vector.cpp:461-474`). `set_subvector_zero(x, 0..N) = 0` (the whole vector is
   zeroed). Degenerate cases of the projector.

4. **Index-set monotonicity / nesting.** For `idx₁ ⊆ idx₂`,
   `set_subvector_zero(set_subvector_zero(x, idx₂), idx₁) = set_subvector_zero(x, idx₂)`
   (zeroing a subset of an already-zeroed set is the identity), and
   `set_subvector_zero(set_subvector_zero(x, idx₁), idx₂) = set_subvector_zero(x, idx₂)`. More
   generally the projectors compose by union: `Z_{idx₁} ∘ Z_{idx₂} = Z_{idx₁ ∪ idx₂}`. Hence
   the two orderings commute (`Z_a ∘ Z_b = Z_b ∘ Z_a = Z_{a∪b}`) — the operation is order-free in
   its index set.

5. **Self-adjointness.** `Z_idx` is self-adjoint with respect to the standard inner product
   (`⟨Z_idx x, y⟩ = ⟨x, Z_idx y⟩`), since `Z_idx = I − P_idx` and `P_idx` is a real diagonal 0/1
   matrix. Combined with idempotence (law 1) this makes `Z_idx` an **orthogonal** projector.

6. **Support-disjoint commutation.** `Z_idx` commutes with any linear operator `A` whose action
   does not couple the `idx` coordinates to their complement (support disjoint from `idx`):
   `Z_idx · A = A · Z_idx`. (For a general `A` this fails — recorded below.)

Laws that explicitly **do not** hold:

- **Not the identity (for non-empty `idx`).** `set_subvector_zero(x, idx) ≠ x` whenever any
  `x[i], i ∈ idx` is nonzero. The empty-set case (law 3) is the only identity.
- **No general commutation with operators.** `Z_idx · A ≠ A · Z_idx` for an arbitrary `A` that
  couples `idx` to its complement (e.g. a stiffness matrix with nonzero essential-row coupling).
  The matrix-side cleanup `eliminate_essential_bc` exists precisely *because* zeroing the vector
  is not the same as zeroing the operator's coupling rows/columns. Recorded so the vector cleanup
  is not mistaken for the operator cleanup.
- **No reduction / reduction-order non-law.** Unlike `dot` / `nrm2`, there is no cross-entry
  reduction here — the writes are independent (`vector.cpp:469-472`), so there is **no**
  load-bearing summation-order claim. The operation is order-free (law 4). Recorded as an absence
  so the device-`forall` ordering is not read as load-bearing.

## Dependencies

(leaf) — `set_subvector_zero` depends on no other L1 operator. It consumes a dense vector `x` and
an index set `idx` and produces a dense vector; the per-index zeroing write is atomic at L1 (the
in-place overwrite, the `use_dev` device dispatch, the `rows.Read` index gather, and the
`forall_switch` kernel surface only in the L1>L0 lowering).

It is the **vector-side** sibling of the matrix-side
[`eliminate_essential_bc`](./eliminate_essential_bc.md) on the "essential-BC cleanup" axis, split
by the vector-entry vs operator-row/column representation. It is **not** built on those operators
and they are **not** built on it as a dep-map edge (the references are navigational); rather
[`eliminate_rhs`](./eliminate_rhs.md) and [`divfree-projector`](./divfree-projector.md) *use* this
primitive at their essential-dof pin / RHS-clean steps (those chapters currently name it as a
`(concept)` reference; with this firm entry landed those become live-node references — flagged for
an edge-retype follow-up in Open questions, out of this one-operator scope).

Concept reference (cross-cutting; do not duplicate):

- [`concepts/set_subvector_zero`](../concepts/set_subvector_zero.md) — the cross-cutting concept
  page naming the BC-enforcement intent and the general-`set_subvector` distinction; this L1 entry
  is its positively-anchored book home.

## Variant axes

- **element type** (absorbed): `real` (`Vector`) | `complex` (`ComplexVector`). The two L0 bodies
  (`vector.cpp:461-474` real, `:476-492` complex) differ only in that the complex body threads
  `XR`/`XI` and zeros both parts (`:489-490`); the index-set semantics are identical. Absorbed as a
  uniform element-type parameter; in the complex case the whole complex dof is zeroed.
- **index-set size** (parameterised, absorbed-as-form): `|idx|` from `0` (identity) to `N` (whole
  vector). A size parameter, not a behavioural variant; the per-index write is size-uniform.

There is **no** scalar-value axis on *this* operator — it is the `s = 0.0` specialization of the
general index-set scalar-set `SetSubVector(x, rows, s)`. The general scalar-set (with `s = 1.0`
at `rap.cpp:186`, `waveportoperator.cpp:73-74`) is the broader primitive of which this is the
zeroing case; it is recorded here as the parent shape, not folded into this entry (the
zeroing-specific name and BC-enforcement role are what warrant the dedicated entry, per the
concept page's naming rationale).

## Status

`firm` — the operator's structure is read directly from **positive** Palace source: the two
`double`-valued `SetSubVector` bodies (real `vector.cpp:461-474`, complex `:476-492`) read in
full, the declaration `vector.hpp:220-221`, and ~40 `s = 0.0` call sites across the solver
surface (divfree `divfree.cpp:173`, gmg `gmg.cpp:194`, distrelaxation `distrelaxation.cpp:114,143`,
spaceoperator `spaceoperator.cpp:945,959,1031`, et al.). The signature's shape (vector over the
dof axis, index set, fresh zeroed vector) matches the body exactly; the algebraic laws
(idempotence, linearity, empty/full boundary, index-set union/commutation, self-adjointness,
support-disjoint commutation) are standard properties of a diagonal 0/1 orthogonal projector
`Z_idx = I − P_idx`, modulo the explicitly-recorded non-identity, general-non-commutation, and
no-reduction non-laws.

This is the **firm-on-positive-structure** decision, exactly as for the BLAS-1 elementwise leaves
([`reciprocal`](./reciprocal.md), [`elementwise_product`](./elementwise_product.md)) and the
sibling BC operators ([`eliminate_essential_bc`](./eliminate_essential_bc.md),
[`eliminate_rhs`](./eliminate_rhs.md)): every law is a **syntactic identity on fully-specified
positive source** (operator-algebra facts about a fixed diagonal 0/1 projector), not a convergence
or numerical-tolerance fact. No dedicated `SetSubVector` unit test exists in
`reference/palace/test/unit/` (the primitive is exercised only indirectly through the
divfree / gmg / driven paths) — but **a missing test does not gate syntactic-identity laws** (the
`apply_linop` / `reciprocal` / `eliminate_essential_bc` firm-on-positive-structure situation, not
the `eigsolve`-convergence situation): the projector laws do not depend on iteration or
convergence, so the absent test does not reduce law-confidence. Hence `firm`, not `rough-in
(test-coverage-bounded)`.

Well-foundedness: the `depends-on` edges are `cites-evidence` edges to the **positive L0 source**
(real `vector.cpp:461-474`, complex `:476-492`, decl `vector.hpp:220-221`), which is rank-terminal
ground truth — so the `firm` (rank 3) operator rests only on rank-terminal evidence and the
graded-stack invariant `rank(u) ≤ rank(v)` holds. (Repaired cycle-104: the earlier draft routed
the sole `depends-on` through the not-yet-authored L1>L0 theme `set-subvector-zero-mutation-rotation`,
which is both a dangling live link and a firm-resting-on-missing-dep rank violation; the firmness
in fact grounds on the positive L0 read, exactly as for the BLAS-1 leaves `reciprocal` /
`elementwise_product`, whose firmness does not block on their L1>L0 themes.) The L1>L0 lowering
theme is a downward narration (forthcoming, plain-text), not an upward rank-blocking dependency.

Resolves the `set_subvector_zero` leg of OQ
`concept-primitive-without-L1-home-trsv-set_subvector_zero-gemv_basis` (the vector-zeroing
primitive now has a firm, positively-anchored L1 home).

## Record definition

No new record is named in the signature. `DofSet[N]` is the cross-cutting essential-true-dof index
set already defined by [`essential_dofs`](./essential_dofs.md) (the `mfem::Array<int>` of true-dof
indices); this entry references it, it does not redefine it.

## Downward to L0

The lowering is the forthcoming `set-subvector-zero-mutation-rotation` L1>L0 theme (not yet
authored — plain-text forward reference; this entry's firmness rests on the positive L0 read,
cited as `cites-evidence` deps, not on a blocking edge to a missing file): it narrates how this
pure projector lowers into Palace's in-place index-set overwrite —
the `x.ReadWrite(use_dev)` destination-is-input idiom (`vector.cpp:467` / `:483-484`), the
`rows.Read(use_dev)` index gather (`:466` / `:482`), the `mfem::forall_switch` device-vs-host
kernel dispatch (`:468` / `:485`), and the complex `XR`/`XI` two-buffer threading
(`:483-484, 489-490`). All of these are L0 mechanism; the L1 signature carries none of them.

**Downward to L3 (non-adjacent identity rotation, annotated in-line):** the L3 tensor-field form
is a single **mask-multiply** `Z_S : V → V`, `(Z_S x)_i = 0 if i ∈ S else x_i` (a
`set-subvector-zero-mask-multiply` form, a speculative future L3 seed — plain-text future-form
note, not a live edge, as the seed does not yet exist). Because the per-index writes are
independent (no sequential dependency across the `i ∈ idx`
updates — they are independent writes, *Semantics* above), the per-element L1 form rotates
**directly** to the global tensor-field form with **no obstruction** — the per-dof iteration
disappears and `Z_S` is one tensor-field map. The intervening L2 absorption is identity-like (a
diagonal projector is already in its most-decomposed shape), so the L1→L3 relationship is the
transitive consequence of the adjacent-edge themes and is annotated here in-line per the CLAUDE.md
non-adjacent-identity-rotation convention, not via an `L1-L3/` directory.

## Evidence

- `palace/linalg/vector.hpp:220-221` — the declaration `template <typename VecType> void
  SetSubVector(VecType &x, const mfem::Array<int> &rows, double s);` with the comment "Sets all
  entries of the vector corresponding to the given indices to the given (real) value". The
  signature anchor. Self-verified via citecheck `--anchor` (line 221, zero-drift).
- `palace/linalg/vector.cpp:461-474` — the **real** body `SetSubVector(Vector &x, const
  mfem::Array<int> &rows, double s)`: `forall` over `rows` writing `X[id] = sr` (`:472`); the
  in-place `x.ReadWrite` destination (`:467`) and `rows.Read` gather (`:466`). The `s = 0.0` case
  is the zeroing this entry covers. Self-verified (`--anchor 'SetSubVector(Vector &x, const
  mfem::Array<int> &rows, double s)'` line 461; `--anchor 'X[id] = sr'` line 472).
- `palace/linalg/vector.cpp:476-492` — the **complex** body
  `SetSubVector(ComplexVector &x, const mfem::Array<int> &rows, double s)`: `forall` writing
  `XR[id] = sr` (`:489`) AND `XI[id] = 0.0` (`:490`) — grounds the complex-case whole-dof zeroing.
  Self-verified (`--anchor 'SetSubVector(ComplexVector &x, const mfem::Array<int> &rows, double s)'`
  line 477; `--anchor 'XI[id] = 0.0'` line 490).
- `palace/linalg/divfree.cpp:173` — `linalg::SetSubVector(rhs, *bdr_tdof_list_M, 0.0);` — the
  divfree-projector use-site (zero the H1 RHS on the boundary true-dofs before the inner solve);
  the use-site `divfree-projector`'s dep-map names as `set_subvector_zero (concept)`.
  Self-verified (`--anchor 'SetSubVector(rhs'` line 173).
- `palace/linalg/gmg.cpp:194` — `linalg::SetSubVector(X[l - 1], *dbc_tdof_lists[l - 1], 0.0);` —
  the geometric-multigrid restriction-residual zeroing. Self-verified (`--anchor 'SetSubVector(X[l
  - 1]'` line 194).
- `palace/linalg/distrelaxation.cpp:114` — `linalg::SetSubVector(x_G, *dbc_tdof_list_G, 0.0);` —
  the distributive-relaxation auxiliary-space correction zeroing (also `:143`). Self-verified
  (`--anchor 'SetSubVector(x_G'` line 114).
- `palace/models/spaceoperator.cpp:945,959,1031` — `linalg::SetSubVector(RHS, nd_dbc_tdof_lists
  .back(), 0.0);` — the driven per-ω assembled-RHS clean on the Nedelec essential true-dofs (one
  of several spaceoperator clean sites).
- `palace/linalg/rap.cpp:186` — `linalg::SetSubVector(diag, dbc_tdof_list, 1.0);` — a **non-zero**
  scalar-set call (the parent shape this entry specializes; recorded to ground the
  zeroing-vs-general distinction in *Variant axes*).
- `book/src/L1/eliminate_essential_bc.md` — the firm c055 matrix-side BC operator (`EliminateBC`
  on an assembled square operator); the operator-side sibling on the essential-BC-cleanup axis.
- `book/src/L1/eliminate_rhs.md` — the firm c055 affine RHS-lift `b − K·x_bc`; consumes this
  primitive at its essential-dof pin (`rap.cpp:64,76,80`).
- `book/src/concepts/set_subvector_zero.md` — the cross-cutting concept page; this L1 entry is its
  positively-anchored book home, and supersedes the page's `reference: []` (now repointed to this
  entry — see the concept-page edit below).

```yaml
verified_against:
  - citation: palace/linalg/vector.hpp:221
    verdict: supports
    audited_at: 2026-06-05T082448Z
    note: SetSubVector(VecType, rows, double s) declaration; citecheck --anchor zero-drift on-disk.
  - citation: palace/linalg/vector.cpp:461
    verdict: supports
    audited_at: 2026-06-05T082448Z
    note: real SetSubVector(Vector, rows, double s) body open; X[id]=sr at :472; zero-drift.
  - citation: palace/linalg/vector.cpp:472
    verdict: supports
    audited_at: 2026-06-05T082448Z
    note: real body write `X[id] = sr` (sr=0 is the zeroing case); zero-drift.
  - citation: palace/linalg/vector.cpp:477
    verdict: supports
    audited_at: 2026-06-05T082448Z
    note: complex SetSubVector(ComplexVector, rows, double s) body open; zero-drift.
  - citation: palace/linalg/vector.cpp:490
    verdict: supports
    audited_at: 2026-06-05T082448Z
    note: complex body `XI[id] = 0.0` — whole complex dof zeroed in the s=0 case (XR[id]=sr at :489); zero-drift.
  - citation: palace/linalg/divfree.cpp:173
    verdict: supports
    audited_at: 2026-06-05T082448Z
    note: divfree RHS boundary-zeroing use-site SetSubVector(rhs, *bdr_tdof_list_M, 0.0); zero-drift.
  - citation: palace/linalg/gmg.cpp:194
    verdict: supports
    audited_at: 2026-06-05T082448Z
    note: gmg restriction-residual zeroing SetSubVector(X[l-1], *dbc_tdof_lists[l-1], 0.0); zero-drift.
  - citation: palace/linalg/distrelaxation.cpp:114
    verdict: supports
    audited_at: 2026-06-05T082448Z
    note: distributive-relaxation aux-correction zeroing SetSubVector(x_G, *dbc_tdof_list_G, 0.0); zero-drift.
  - citation: book/src/L1/eliminate_essential_bc.md
    verdict: positive-cross-reference
    audited_at: 2026-06-05T082448Z
    note: firm matrix-side BC operator (EliminateBC); the operator-side sibling on the essential-BC-cleanup axis.
  - citation: book/src/L1/eliminate_rhs.md
    verdict: positive-cross-reference
    audited_at: 2026-06-05T082448Z
    note: firm affine RHS-lift b - K x_bc; consumes set_subvector_zero at its essential-dof pin (rap.cpp:64,76,80).
```
```

```edit:book/src/concepts/trsv.md
---
edges:
  reference:
    - L1-L0/triangular-solve-obstruction   # the disposition: a general trsv has NO positive
                                            # Palace L0 site — it is an obstruction theme.
    - L1/back_solve                         # the one positively-anchored triangular component
                                            # Palace DOES implement (small-dense GMRES/FGMRES
                                            # restart back-substitution); the sibling of a general trsv.
---

# trsv

Base primitive: triangular solve `T · y = b` for a triangular matrix `T` and conforming vectors `b`, `y`. The BLAS-2 routine `?trsv`.

## Disposition: no L1 home — obstruction + a positively-anchored sibling

A **general** triangular solve (`trsv` / `trsm` / `SpTrSV`, sparse or dense, acting on the
length-`N` field) has **no positive Palace source site** and gets **no L1 operator** — this is
the settled disposition, documented by the L1>L0 obstruction theme
[`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md) (c028,
`obstruction`): every triangular substitution that occurs in a Palace run lives inside opaque
library calls (HYPRE GS/SSOR relaxation selected by an integer enum, forward/back substitution
inside external MUMPS/SuperLU/STRUMPACK factorizations), and Palace-authored smoothers are
deliberately GS-free (Jacobi + Chebyshev only, citing Adams et al. 2003). Per CLAUDE.md §Scope an
unimplemented Palace component is not a direct implementation target, so no constructive `trsv`
L1 form is proposed.

The **one** triangular-solve component Palace *does* implement positively is the small-dense
GMRES/FGMRES restart-correction back-substitution — the firm L1 leaf
[`back_solve`](../L1/back_solve.md) (c027). It solves the dense upper-triangular `R · y = s` over
the small running-QR R-factor (coordinate space, dimension `j+1` ≤ `max_dim`, no collective), and
is the *small-dense-triangular* sibling of [`lu_solve`](../L1/lu_solve.md). It is **not** a
general `trsv` (which would act on the length-`N` field). This concept page is therefore a
non-node pointer to those two homes: the obstruction theme (the resolution for the general case)
and `back_solve` (the positively-anchored special case).

## Contract

- Reads `T` and `b`; writes `y` (or, by in-place convention, overwrites `b` with `y`).
- The triangle (upper/lower) and the diagonal (unit/non-unit) are parameters.
- Sequentially dependent: solving for `y[k]` requires `y[0..k-1]` (for lower triangular). At L3 this is an obstruction — `trsv` does not lift to a tensor-field operation without algorithmic change (e.g., level-set or block-Jacobi triangular preconditioning).
- Numerical: ill-conditioned or near-singular `T` produces large `y`; the caller is responsible for guarding against it.

## Role in higher-layer rotations

In GMRES, [`back_solve`](../L1/back_solve.md) is one `trsv` against the upper-triangular block of `H̄_j` (produced by replayed Givens rotations) with RHS `s[0..j]`. The size is `O(max_dim)`, which is small (default 30), so the primitive's serial cost is irrelevant.

## Palace mapping

- The GMRES/FGMRES restart back-substitution loop in `palace/linalg/iterative.cpp:652-660` (GMRES) / `:831-840` (FGMRES) — the positively-anchored small-dense case, firm at L1 as [`back_solve`](../L1/back_solve.md).
- The **general** `trsv` (sparse / large-field) has no Palace site: see the obstruction theme [`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md) for the exhaustive negative anchors (HYPRE-internal GS/SSOR, external direct-solver factorizations, the GS-free Palace smoother cohort).
```

```edit:book/src/concepts/gemv_basis.md
---
edges:
  reference:
    - concepts/orthogonalization   # primary use-site (CGS/CGS2 basis correction)
    - L2/linear_combination        # the variadic scalar-weighted-vector-sum fold this is the
                                    # batched-coefficient specialization of (the fold home)
    - L1/orthogonalize             # the L0-anchored consumer: the CGS basis-correction loop
                                    # `for j: w.Add(-H[j], V[j])` (orthog.hpp:71-74) lives inside it.
---

# gemv_basis

**Primitive (concept-only).** `gemv_basis(w, alpha, V[0..m-1], H[0..m-1]) → w'`

Batched coefficient–basis combination: given a stored basis `V[0..m-1]` (m vectors of length n) and a length-m coefficient vector `H`, update

```
w' = w + alpha · Σⱼ H[j] · V[j]
```

in one fused step. Equivalent to `w' = w + alpha · (V H)` viewing `V` as an n×m matrix and `H` as an m-vector — hence the name `gemv` (general matrix–vector) over a basis.

## Disposition: concept-only — no standalone L0 callable

`gemv_basis` has **no standalone callable in Palace** and gets **no L1 operator**. Its only L0
referent is the **inline** CGS basis-correction loop `for j: w.Add(-H[j], V[j])`
(`palace/linalg/orthog.hpp:71-74`) inside `OrthogonalizeColumnCGS` — Palace writes the unfolded
loop of `axpy`, never a fused BLAS-2 `gemv`. That inline loop is already covered by the firm L1
operator [`orthogonalize`](../L1/orthogonalize.md) (which lifts the whole CGS/MGS/CGS2 family).
The *batched-coefficient fold shape* `w + α·Σⱼ H[j]·V[j]` is a specialization of the L2 variadic
scalar-weighted-vector-sum fold [`linear_combination`](../L2/linear_combination.md) (the
expand-1→n adjoint of `dot`'s reduce-n→1). So this page stays a **concept** documenting the
fold-shape; it is a non-node pointer to its fold home (`linear_combination`) and its L0-anchored
consumer (`orthogonalize`), not a book operator.

## Relation to axpy

`gemv_basis(w, α, V, H)` is the fused form of `m` sequential `axpy(w, α·H[j], V[j])` calls. The semantics are identical when the m axpys are independent of one another (no read–write dependency between iterations j and j+1 on `w`'s entries they share — and there is none, since each axpy is `w += scalar · V[j]` with all `V[j]` read-only). The fusion is transparent at L2: a slice may write the unfolded loop or the fused primitive interchangeably; the choice is an implementation detail (BLAS-2 packed call vs. loop of BLAS-1 axpys vs. hand-fused kernel).

Where the m updates are *not* independent — as in MGS, where each axpy mutates `w` and the next dot reads the mutated `w` — `gemv_basis` does NOT apply, and the unfolded axpy loop is the correct L2 form.

## Use sites

- **CGS / CGS2 orthogonalization** ([`orthogonalization`](./orthogonalization.md), lifted by firm L1 [`orthogonalize`](../L1/orthogonalize.md)): after the batched reduction yields the full coefficient vector `H[0..m-1]`, the basis correction `w − V H` is the unfolded loop `for j: w.Add(-H[j], V[j])` (`palace/linalg/orthog.hpp:71-74`). The MGS variant cannot use the batched form for the reasons above.
- **GMRES basis combination**: forming `x_m = x_0 + V_m y_m` after the back-solve is the same fold shape (with `alpha = +1`) — the downstream `linear_combination` lift in [`back_solve`](../L1/back_solve.md) (`x.Add(s[k], V[k])`, `iterative.cpp:666`).
- **Projection / restriction operators on stored bases** (anticipated for eigensolver and FE slices).

## L2 status

`gemv_basis` is a derived fold shape: it is `dot`'s adjoint (dot reduces n→1 along a basis direction; gemv_basis expands 1→n along a basis direction with a coefficient vector). Both are batched forms of pointwise vector–scalar operations. As such it is a coefficient-batched specialization of the L2 [`linear_combination`](../L2/linear_combination.md) fold — NOT a separate book operator. Whether it is realized as packed BLAS-2, a manual loop of axpys, or a fused custom kernel is an L3/L2-implementation choice and is transparent.

## Citations

- `palace/linalg/orthog.hpp:71-74` — the CGS post-reduction loop `for j: w.Add(-H[j], V[j])` is the unfolded form (the only L0 referent — an inline loop, not a standalone callable); this concept covers its fold shape, and the firm L1 [`orthogonalize`](../L1/orthogonalize.md) lifts the loop.
```

```edit:book/src/L1/index.md
| [`scal`](./scal.md) | `(α, x) → α·x` | (leaf; subsumed by `axpby` via β=0) | `firm` |
| [`set_subvector_zero`](./set_subvector_zero.md) | `(x: Tensor[N], idx: DofSet[N]) → Tensor[N]` (i.e. `x` with entries on `idx` zeroed) | (leaf; vector-side essential-BC cleanup atom; sibling of matrix-side `eliminate_essential_bc`, consumed by `eliminate_rhs` / `divfree-projector`) | `firm` (index-set vector zeroing; the `s=0.0` specialization of `linalg::SetSubVector(x, rows, s)`; the diagonal 0/1 orthogonal projector `Z_idx = I − P_idx`; L0: `palace/linalg/vector.cpp:461-474` real + `:476-492` complex, decl `palace/linalg/vector.hpp:220-221`, ~40 `0.0` call sites incl. `palace/linalg/divfree.cpp:173`, `palace/linalg/gmg.cpp:194`, `palace/linalg/distrelaxation.cpp:114,143`; harvested cycle-104; firm-on-positive-structure, no-dedicated-test caveat non-gating per `reciprocal` / `eliminate_essential_bc` precedent; element-type variant axis absorbed; idempotence / linearity / index-set-union-commutation / self-adjoint laws, not-identity / no-general-operator-commutation / no-reduction non-laws; L1>L0: `set-subvector-zero-mutation-rotation` forthcoming; L3 mask-multiply identity-rotation annotated in-line) |
```

```edit:book/src/L1/index.md
- [`elementwise_product`](./elementwise_product.md) — pure-functional **Hadamard pointwise product** `result = a ⊙ b`, `result[i] = a[i] · b[i]`; the diagonal-operator-action primitive at L1 (law 9: `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`) and the per-call kernel of the diagonally-scaled-preconditioner cohort (`jacobi-smoother`, `chebyshev-smoother`). Strictly generalises `scal` via broadcast specialisation (`scal(α, x) = elementwise_product(broadcast(α, N), x)`); composes with `reciprocal` (D2 sibling this cycle) to close the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner chain that `assemble-diagonal` §Dependencies named "forthcoming, plain text". Canonical L0 site is the operator-class `BaseDiagonalOperator<OperType>::Mult` (real `palace/linalg/operator.cpp:486`; complex `:504-505` six-fused-multiply-add) plus the **conjugate variant** `MultHermitianTranspose` (`:564-565` complex-only, three sign flips realising `ā ⊙ b`); the `jacobi.cpp` `Apply` helper (`:30-69`) is a line-for-line consumer duplicate. Two variant axes: element-type (real | complex) × conjugation (straight | conjugate-first-operand, complex-only). Firm-on-positive-structure (the `apply_linop` / `lu_solve` / `back_solve` / `ls_update_column` / `jacobi-smoother` no-dedicated-test precedent): every law is a syntactic identity on positive source. Closes the §Dependencies forward-references in `assemble-diagonal:73` and `jacobi-smoother:289-297`.
- [`set_subvector_zero`](./set_subvector_zero.md) — pure-functional **index-set vector zeroing** `x' = set_subvector_zero(x, idx)`; the vector-side essential / port boundary-condition cleanup atom (zeros a residual / RHS / correction on its Dirichlet true-dofs). The `s = 0.0` specialization of Palace's `linalg::SetSubVector(x, rows, s)` (real `palace/linalg/vector.cpp:461-474` + complex `:476-492`, decl `palace/linalg/vector.hpp:220-221`); the diagonal 0/1 orthogonal projector `Z_idx = I − P_idx`. The **vector-side** sibling of the matrix-side [`eliminate_essential_bc`](./eliminate_essential_bc.md) (which zeros operator rows/columns, not vector entries) and the primitive that [`eliminate_rhs`](./eliminate_rhs.md) / [`divfree-projector`](./divfree-projector.md) use at their essential-dof pin / RHS-clean steps (those chapters' `(concept)` references now resolve to this live node — edge-retype follow-up flagged). ~40 `0.0` call sites span the solver surface (divfree `divfree.cpp:173`, gmg restriction-residual `gmg.cpp:194`, distrelaxation `distrelaxation.cpp:114,143`, driven RHS-clean `spaceoperator.cpp:945,959,1031`). Firm-on-positive-structure (the `reciprocal` / `eliminate_essential_bc` no-dedicated-test precedent): idempotence / linearity / index-set-union-commutation / self-adjointness laws, not-identity / no-general-operator-commutation / **no-reduction** (independent writes, no load-bearing summation-order) non-laws. Element-type variant axis absorbed (complex case zeros the whole dof, both parts). L3 form is a single mask-multiply `Z_S` with no obstruction (independent per-dof writes), annotated in-line per the non-adjacent-identity-rotation convention. Resolves the `set_subvector_zero` leg of the homeless-primitive OQ. Harvested cycle-104.
```

```edit:book/src/SUMMARY.md
  - [scal](./L1/scal.md)
  - [set_subvector_zero](./L1/set_subvector_zero.md)
```

## Operator content

The full firm `set_subvector_zero` chapter body is in the `new:book/src/L1/set_subvector_zero.md`
block above (Status, Signature with named-axis shape contract, six algebraic laws + three non-laws,
Dependencies, Variant axes, Record-definition note, Downward-to-L0 + in-line L3 identity-rotation
annotation, Evidence with verified_against YAML). The two concept-page edits repoint `trsv` and
`gemv_basis` to their existing homes and add a §Disposition section to each. The L1-index edits
add the dep-map table row (alpha-placed after `scal`, before the `**Operator application &
assembly**` group header) and the §Vocabulary-cohort firm-sub-list bullet (placed with the BLAS-1
elementwise leaves, after `elementwise_product`). The SUMMARY edit adds the chapter under the
BLAS-1 sub-chapter grouping, alpha after `scal`.

Index-registration partition: I author (1) my own dep-map table row and (2) my own §Vocabulary-
cohort bullet. I do **not** touch (3) the consolidated firm running-count tally — the dispatch
does not name me as count-owner and other content-tail dispatches may land L1 entries this cycle;
the firm grand-total reconciliation (currently 39: 32 main + 4 FE-assembly + 3 FE-space → would
become 33 main / 40 grand) is **deferred to the cycle's designated count-owner**. Flagged in Open
questions so the owner reconciles the absolute total once the cohort lands.

## Supporting evidence

Per-primitive disposition reasoning:

- **`set_subvector_zero`** — positive L0 site confirmed: `SetSubVector(x, rows, double s)` declared
  `vector.hpp:220-221`, defined real `vector.cpp:461-474` (`X[id]=sr` at `:472`) + complex
  `:476-492` (`XR[id]=sr` `:489`, `XI[id]=0.0` `:490`); the `s=0.0` zeroing case has ~40 call sites
  (codemap `search_text SetSubVector`). It is a genuinely distinct primitive from the firm
  matrix-side `eliminate_essential_bc` (read `eliminate_essential_bc.md` in full: it operates on an
  assembled operator via `EliminateBC`, zeroing rows/columns — a different arity and object) and
  from `eliminate_rhs` (the affine `b − K·x_bc`). Both *consume* this vector primitive at their
  essential-dof pin. Genuine reused primitive with positive L0 → author L1 entry. All citations
  citecheck-verified zero-drift.
- **`trsv`** — checked the obstruction theme FIRST per the dispatch note. The
  `triangular-solve-obstruction` theme (c028) is exhaustive: a whole-tree codemap search for
  `trsv|trsm|TriSolve|TriangularSolve|SpTrSV` returns zero hits, and Palace's smoother cohort is
  deliberately GS-free. So `trsv` is **deliberately home-less because it is an obstruction**, with
  the one positive case (`back_solve`, c027) already firm. Repoint the concept edge to the
  obstruction theme + `back_solve`; do NOT manufacture an operator (CLAUDE.md §Scope). The
  planner's `L1/back_solve` hypothesis is correct (the file exists, read in full).
- **`gemv_basis`** — checked `orthog.hpp` in full: the CGS basis correction is an **inline** loop
  `for j: w.Add(-H[j], V[j])` (`:71-74`), not a standalone callable; no fused BLAS-2 gemv exists in
  the tree. The inline loop is already lifted by firm `L1/orthogonalize`. The batched fold shape is
  a specialization of the L2 `linear_combination` variadic fold. Concept-only, repoint to
  `L2/linear_combination` + `L1/orthogonalize` (both confirmed to exist). The concept page itself
  already framed it as "a derived L2 primitive" — the disposition formalizes that.

## Open questions / caveats

- **`set-subvector-zero-mutation-rotation` L1>L0 theme is forthcoming** (RESOLVED by repairer,
  cycle-104). The earlier draft routed the firm entry's sole `depends-on` through this not-yet-
  authored theme — both a dangling live link (linkcheck2 hard error) and a firm-resting-on-missing-
  dep rank violation. **Repaired:** the `depends-on` edges now point at the positive L0 source as
  `cites-evidence` (rank-terminal ground truth), grounding the `firm` rank well-foundedly; the
  L1>L0 theme is a plain-text "(forthcoming)" note in §Downward / §Status, not a blocking edge.
  This matches how `reciprocal` / `elementwise_product` are firm without their L1>L0 themes blocking
  rank. No integrator decision remains. (The theme itself is still a real future authoring item —
  tracked separately when an L1>L0 lowering pass lands it.)
- **`set-subvector-zero-mask-multiply` L3 entry is forthcoming** (RESOLVED by repairer, cycle-104).
  The earlier draft carried a live `reference` edge to this non-existent L3 seed (linkcheck2 hard
  error). **Repaired:** the edge is removed; the §Downward in-line L3 annotation is now a plain-text
  future-form note (the prose already carried the full identity-rotation annotation, so nothing is
  lost). No integrator decision remains.
- **Edge-retype follow-up on consumers** (out of this one-operator scope): `divfree-projector` (L1
  index dep-map `:147`) and `eliminate_rhs` (`:165`) name `set_subvector_zero` / `set_subvector` as
  `(concept)` references because no L1 home existed. With this firm entry landed, those should be
  retyped to live `reference` (or `depends-on`, if the integrator judges the BC-pin a blocking
  constituent) edges to `L1/set_subvector_zero`. Flagged for a follow-up edge-typing pass; I do not
  edit those chapters here (one operator per invocation).
- **Firm-count tally reconciliation deferred to the cycle count-owner** (see §Operator content): the
  L1 firm grand total moves 39 → 40 (main cohort 32 → 33) with `set_subvector_zero`. I registered my
  row + bullet but did NOT update the consolidated running-count prose at `L1/index.md:47`; the
  count-owner reconciles the absolute total post-cohort.
- **`trsv` / `gemv_basis` are concept-only by honest disposition, not by omission.** Recorded
  here so a future audit does not re-open them as "missing L1 homes": `trsv` is an obstruction
  (the resolution is the obstruction theme + the `back_solve` sibling); `gemv_basis` is an inline
  fold-shape with no standalone callable (lifted by `orthogonalize`, a specialization of
  `linear_combination`). Neither warrants an L1 operator.
```
