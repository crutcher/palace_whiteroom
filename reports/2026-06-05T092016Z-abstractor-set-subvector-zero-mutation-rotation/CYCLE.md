---
agent: abstractor
invoked_at: 2026-06-05T092016Z
scope: L1>L0 theme sketch — set-subvector-zero-mutation-rotation (c105 D4 content tail)
status: integrated
integrated_at: 2026-06-05T100000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied clean (cycle-105 D4, batch-33 position 3/3, BATCH-CLOSING). CREATED `book/src/L1-L0/set-subvector-zero-mutation-rotation.md` — firm L1>L0 lowering theme (`Z_idx = I − P_idx` → in-place `SetSubVector(x,rows,0.0)`; A real vector.cpp:461-474 / B complex :476-492 + use-site cohort C; typed-from-start edges: depends-on {L1/set_subvector_zero kind:lowers-to, 3 L0 cites-evidence}, reference {scal/reciprocal-elementwise-product/divfree-projector}; rank: firm). SUMMARY + L1-L0/index.md dep-map row alpha-after `scal-mutation-rotation`. COUPLED de-stale: the c104 L1/set_subvector_zero.md entry's 4 (forthcoming) forward-refs repointed to live links (a `reference`, NOT `depends-on`, correctly avoiding the rank-direction error). Resolves OQ `set-subvector-zero-mutation-rotation-theme-forthcoming`. Build EXIT 0; rank well-foundedness 0 violations; citecheck theme 16 ok / set_subvector_zero 28 ok. The new L1>L0 theme = the L1>L0 tally +1.
inputs:
  - book/src/L1/set_subvector_zero.md  (firm L1 entry, c104)
  - palace/linalg/vector.cpp:461-474 (real SetSubVector body)
  - palace/linalg/vector.cpp:476-492 (complex SetSubVector body)
  - palace/linalg/vector.hpp:220-221 (decl)
  - palace/linalg/divfree.cpp:173 (use-site)
  - book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md (convention sibling)
  - book/src/methodology/graded-stack-scheme.md (edge typing)
---

# CYCLE: L1>L0 theme sketch — set-subvector-zero-mutation-rotation

## Summary

c104 landed the firm L1 entry `L1/set_subvector_zero` — the pure-functional
`x' = set_subvector_zero(x, idx)` index-set vector-zeroing primitive, modeled as the diagonal
0/1 orthogonal projector `Z_idx = I − P_idx`. Its L1>L0 lowering theme was deferred as a
plain-text "(forthcoming)" note (the c104 repairer correctly avoided a dangling `depends-on`).
This dispatch authors that theme. The lowering is a **clean syntactic-identity mutation
rotation**: the L1 pure-function (value-in / fresh-value-out) lowers to Palace's L0 in-place
`SetSubVector(x, rows, 0.0)` — the receiver argument `x` is both source and destination, the
per-index zeroing is realized by an `mfem::forall_switch` device-uniform element-loop writing
`X[id] = sr` (real) / `XR[id] = sr; XI[id] = 0.0` (complex) with `sr = 0`. Two element-type
sub-patterns (real `vector.cpp:461-474`, complex `:476-492`) + a use-site cohort. Status:
**firm** — every claim is a syntactic identity read straight off positive L0 source (the
firm-on-positive-structure escape; the L1 entry is already firm, and the rank well-foundedness
invariant holds: theme rank ≤ min(L1-endpoint firm=3, L0 rank-terminal) = firm/3). The theme
edges are typed from the start (HARD-gate-new): `depends-on` (lowers) the L1 entry + the L0
sites (cites-evidence). Coupled de-stale: the L1 entry's three "(forthcoming)" forward-refs are
repointed to this now-authored theme as a live link.

## Proposed changes

```new:book/src/L1-L0/set-subvector-zero-mutation-rotation.md
---
# Lowering theme. Per graded-stack scheme §5: a theme's rank = min(endpoint ranks);
# the lowering edge is a depends-on on BOTH endpoints. L1 endpoint is firm (rank 3,
# c104); the L0 endpoint is rank-terminal ground truth. So this theme is firm (rank 3)
# and rank(theme) ≤ min(endpoints) holds for free.
rank: firm
edges:
  depends-on:
    - target: L1/set_subvector_zero
      kind: lowers-to            # the L1 source entry this theme lowers (documentation; linter reads the depends-on bucket)
    - target: palace/linalg/vector.cpp:461-474
      kind: cites-evidence       # real SetSubVector body — X[id]=sr at :472
    - target: palace/linalg/vector.cpp:476-492
      kind: cites-evidence       # complex body — XR[id]=sr :489, XI[id]=0.0 :490
    - target: palace/linalg/vector.hpp:220-221
      kind: cites-evidence       # the `double s` SetSubVector declaration
  reference:
    - L1-L0/scal-mutation-rotation                       # sibling receiver-mutation BLAS-1 thin-theme
    - L1-L0/reciprocal-elementwise-product-mutation-rotation  # sibling forall_switch in-place→pure thin-theme
    - L1-L0/divfree-projector-mutation-rotation          # consumer theme (uses this zeroing at its RHS-clean)
---

# set-subvector-zero-mutation-rotation

The mutation rotation for the vector-side essential/port boundary-condition cleanup atom.
Lowers the pure L1 form [`set_subvector_zero`](../L1/set_subvector_zero.md) —
`x' = set_subvector_zero(x, idx)`, the diagonal 0/1 orthogonal projector
`Z_idx = I − P_idx` that annihilates the `idx` coordinates and is the identity on their
complement — into Palace's L0 in-place index-set overwrite
`linalg::SetSubVector(x, rows, 0.0)` (the `s = 0.0` specialization of the `double`-valued
`SetSubVector` overload). Narrated forward: the L1 pure-functional projector application
(value `x` in, fresh zeroed value out) dissolves into an L0 `mfem::forall_switch` element-loop
that writes zero through the **receiver argument `x` itself** (the destination *is* the input
argument, via `x.ReadWrite(use_dev)`), with the index set gathered as `rows.Read(use_dev)`.
Sibling thin-theme to [`scal-mutation-rotation`](./scal-mutation-rotation.md) and
[`reciprocal-elementwise-product-mutation-rotation`](./reciprocal-elementwise-product-mutation-rotation.md)
(same BLAS-1-leaf in-place→pure rewrite class, same single-`forall_switch`-pass shape); the
canonical *consumer* of the zeroing is [`divfree-projector-mutation-rotation`](./divfree-projector-mutation-rotation.md)
(zero the H1 RHS on the boundary true-dofs before the inner solve).

## Slug

`set-subvector-zero-mutation-rotation`

## L1 form (LHS)

A pure-functional, reduction-free, rank-local diagonal projector application
([`L1/set_subvector_zero`](../L1/set_subvector_zero.md) §Signature/§Semantics):

    set_subvector_zero :: (x: Tensor[N], idx: DofSet[N]) -> Tensor[N]
    set_subvector_zero(x, idx) = the y with  y[i] = 0  (i in idx),  y[i] = x[i]  (i not in idx)

Equivalently the linear map `Z_idx = I − P_idx`, `P_idx` the diagonal 0/1 projector onto the
`idx` coordinates. The L1 form takes `x` as a value and returns a **fresh** vector; it carries
no destination buffer, no device dispatch, no index-gather mechanism. The element type is the
**element-type variant axis** (real `Vector` | complex `ComplexVector`); in the complex case the
*whole* complex dof is zeroed (both real and imaginary parts). The empty index set is the
identity (`set_subvector_zero(x, ∅) = x`); the full index set yields the zero vector. The
per-index writes are independent — no reduction, no cross-entry summation order
([`L1/set_subvector_zero`](../L1/set_subvector_zero.md) §Algebraic laws, no-reduction non-law).

## L0 form (RHS)

The L0 target is the `double`-valued `SetSubVector` overload, declared once over both vector
types (`palace/linalg/vector.hpp:220-221`, "Sets all entries of the vector corresponding to the
given indices to the given (real) value") and defined twice. This theme covers the `s = 0.0`
call shape (`sr = 0`). The rewrite splits into two element-type sub-patterns realizing the same
in-place receiver-argument zeroing kernel, plus a consumer-call-site cohort C.

### Sub-pattern A — real `SetSubVector(Vector &x, …, 0.0)` in-place receiver-arg zeroing

The L1 value `x' = set_subvector_zero(x, idx)` lowers to the in-place mutation of `x`'s indexed
entries to zero. The destination *is* the input argument `x` (`x.ReadWrite(use_dev)`):

        void SetSubVector(Vector &x, const mfem::Array<int> &rows, double s)
        {                                              // palace/linalg/vector.cpp:461-474
          const bool use_dev = x.UseDevice();
          const int N = rows.Size();
          const double sr = s;                         //   sr = 0 for the zeroing case
          const auto *idx = rows.Read(use_dev);        //   index-set gather (idx <- rows)
          auto *X = x.ReadWrite(use_dev);              //   x is BOTH source and destination
          mfem::forall_switch(use_dev, N,
                              [=] MFEM_HOST_DEVICE(int i)
                              {
                                const auto id = idx[i];
                                X[id] = sr;            //   :472  per-index write (sr = 0)
                              });
        }

One write per indexed dof, `X[id] = sr` at `:472`, `sr = 0` in the zeroing case. The loop runs
over `N = rows.Size()` (the size of `idx`, NOT the vector length) — the empty-index identity is
the `forall` over zero rows, a structural no-op. Reduction-free, rank-local.

### Sub-pattern B — complex `SetSubVector(ComplexVector &x, …, 0.0)` two-buffer in-place zeroing

The complex element-type lowers to the two-buffer kernel that threads the real and imaginary
device pointers separately and zeros **both** parts of each indexed dof:

        template <>
        void SetSubVector(ComplexVector &x, const mfem::Array<int> &rows, double s)
        {                                              // palace/linalg/vector.cpp:476-492
          const bool use_dev = x.UseDevice();
          const int N = rows.Size();
          const double sr = s;                         //   sr = 0 for the zeroing case
          const auto *idx = rows.Read(use_dev);
          auto *XR = x.Real().ReadWrite(use_dev);      //   real component receiver
          auto *XI = x.Imag().ReadWrite(use_dev);      //   imag component receiver
          mfem::forall_switch(use_dev, N,
                              [=] MFEM_HOST_DEVICE(int i)
                              {
                                const int id = idx[i];
                                XR[id] = sr;           //   :489  real part <- sr (= 0)
                                XI[id] = 0.0;          //   :490  imag part <- 0.0 (literal)
                              });
        }

In the zeroing case `sr = 0`, so `XR[id] = 0` AND `XI[id] = 0.0` — the whole complex dof is
zeroed. Note the imaginary write `XI[id] = 0.0` is a hard literal-`0.0`, independent of `sr`
(the `double`-valued `SetSubVector` sets only the real part to `s` and always zeros the
imaginary part; for `s = 0` the two coincide and the kernel is the clean complex zeroing this
theme lowers). This grounds the L1 §Semantics "the whole complex dof is zeroed" claim.

### Sub-pattern C — use-site cohort (`SetSubVector(v, dofs, 0.0)` BC-cleanup calls)

The `s = 0.0` call form appears ~40× across the solver surface; each is an L0 surface witness of
the same projector-application lowering. Representative cohort (all positively cited under
*Verified-against*):

- `palace/linalg/divfree.cpp:173` — `linalg::SetSubVector(rhs, *bdr_tdof_list_M, 0.0);` — zero
  the H1 RHS on the boundary true-dofs before the inner `ksp->Mult(rhs, psi)`. Consumed by
  [`divfree-projector-mutation-rotation`](./divfree-projector-mutation-rotation.md).
- `palace/linalg/gmg.cpp:194` — `linalg::SetSubVector(X[l - 1], *dbc_tdof_lists[l - 1], 0.0);`
  — zero the restricted residual on coarse-level essential dofs between V-cycle levels.
- `palace/linalg/distrelaxation.cpp:114` (also `:143`) —
  `linalg::SetSubVector(x_G, *dbc_tdof_list_G, 0.0);` — zero the auxiliary-space correction on
  its essential dofs.
- `palace/models/spaceoperator.cpp:945` (also `:959,:1031`) —
  `linalg::SetSubVector(RHS, nd_dbc_tdof_lists.back(), 0.0);` — zero the assembled driven RHS on
  the Nedelec essential true-dofs.

These are not distinct rewrites — they are the same A/B kernel invoked at the BC-enforcement
call sites. The cohort is the exhaustiveness evidence that the `s = 0.0` form is the dominant
call shape and that the lowering is uniform across the solver pipelines.

### The crucial L0 facts the L1 form erases

- **Receiver-argument destination mutation (destination *is* input).** The L1 form takes `x` as
  a value and returns a fresh result. The L0 form has no separate destination — `x` is read AND
  written through `x.ReadWrite(use_dev)` (`:467` real / `:483-484` complex). The mutation
  rotation is the receiver-as-destination idiom — here the destination is the **first function
  argument** `x` (not a `*this` receiver as in `scal`'s `x *= α`, not a separate `y` output-arg
  as in `apply_linop`'s `A.Mult(x, y)`; a third destination-binding variant). The L1>L0 job is
  to materialize the destination as the argument `x` itself, then route the projector through it.
- **`rows.Read(use_dev)` index-set gather.** The L1 `idx: DofSet[N]` is an abstract index set;
  the L0 form gathers it as a device pointer `idx = rows.Read(use_dev)` (`:466` / `:482`) and
  loops `N = rows.Size()` times. The gather and the device-residency of the index array are L0
  mechanism the L1 form does not carry.
- **`mfem::forall_switch` device-uniform dispatch.** The host/device split (`:468` / `:485`) is
  a transparent execution-model concern; the L1 form is the projector map, agnostic to where it
  runs.
- **Complex two-buffer threading + hard imaginary zero.** The complex kernel threads `XR`/`XI`
  separately (`:483-484`) and writes `XI[id] = 0.0` as a literal (`:490`), independent of `sr`.
  The L1 form sees one complex zeroing; the two-buffer split and the literal-`0.0` imaginary
  write are L0 mechanism.
- **No reduction, independent writes.** Each `X[id]` write reads no other entry — no sequential
  dependency, no summation order. The device-`forall` write ordering is **not** load-bearing
  (recorded as the L1 no-reduction non-law). This is why the projector lowers cleanly with no
  reduction-order obstruction (contrast `dot`/`nrm2`).
- **No `s = 0.0` constant-folding fast path.** There is no separate zero-optimized kernel — the
  `s = 0.0` case runs the same general `X[id] = sr` write with `sr = 0`. The zeroing
  specialization is a *call-shape* fact (which scalar is passed), not a kernel branch. The
  general non-zero scalar form (`SetSubVector(diag, dofs, 1.0)` `rap.cpp:186`,
  `SetSubVector(tE0t, …, 1.0)` `waveportoperator.cpp:73`) is the parent shape; this theme
  lowers only the `s = 0.0` projector specialization (the parent general-scalar-set is recorded
  in [`L1/set_subvector_zero`](../L1/set_subvector_zero.md) §Variant axes as the parent, not
  folded into this theme).

## Applicability conditions

The rewrite preserves semantics when:

1. **Receiver-as-destination is safe (no aliasing concern).** Each per-index write `X[id] = sr`
   reads no other entry and writes a constant — the receiver-as-source-and-destination is
   correct element-locally (the receiver IS the destination, intentionally; unlike a binary op,
   there is no second operand to alias). No aliasing precondition.
2. **Index validity.** Each `id ∈ idx` must be a valid index into `x` (`0 ≤ id < N`). The L0
   kernel performs no bounds check (`X[id] = sr` is a raw write); the caller guarantees
   `idx ⊆ 0..N` (in the BC use-sites, `idx` is an essential/port true-dof set, structurally a
   subset of the dof axis). The empty index set (`rows.Size() == 0`) is the safe identity (the
   `forall` over zero rows is a no-op).
3. **Element-type conformance.** Real `Vector` lowers to sub-pattern A (`vector.cpp:461-474`);
   complex `ComplexVector` lowers to sub-pattern B (`:476-492`). Dispatch is by the static C++
   `VecType` at the call site (the `template <typename VecType>` declaration `vector.hpp:220-221`
   with the explicit `Vector` / `ComplexVector` specializations). In the complex case the WHOLE
   complex dof is zeroed (both parts), matching the L1 §Semantics.
4. **Scalar is `0.0` (the zeroing specialization).** This theme lowers the `s = 0.0` call shape.
   The general `SetSubVector(x, rows, s)` with `s ≠ 0` is the parent index-set scalar-set (e.g.
   `s = 1.0` at `rap.cpp:186`), which this entry's L1 form does NOT cover — it is the
   `set_subvector_zero` specialization (the zeroing-specific name signals BC-enforcement intent
   at the call site).
5. **Single-machine scope.** Both sub-patterns are rank-local element-loops over disjoint slices
   of the dof axis; no MPI collective at any layer (the index writes are rank-local, no boundary
   exchange). MPI distribution is out of scope per CLAUDE.md §Scope; flagged once here.

## Justification kind

**Structural** — the rewrite is the syntactic destination-binding of the L1 fresh-return into
the receiver argument `x`, realized by the `forall_switch` per-index constant-write kernel. No
algebraic recognition rule is needed: the L0 body writes the literal projector definition
(`X[id] = 0` for `id ∈ idx`, every other entry untouched) verbatim — the L1 `Z_idx` projector
IS the kernel's action. Both sub-patterns read straight off positively-cited source with no
literature inference and no negative-anchor reconstruction. The element-type variant axis is
absorbed by L0 template specialization. This is a clean syntactic-identity mutation rotation.

## Speculative L1 operators

**None.** This theme lowers an already-firm L1 leaf
([`L1/set_subvector_zero`](../L1/set_subvector_zero.md), landed c104); it proposes no new L1
vocabulary. A speculative `set_subvector(x, idx, s)` general index-set scalar-set (the `s ≠ 0`
parent shape) is named in [`L1/set_subvector_zero`](../L1/set_subvector_zero.md) §Variant axes /
§Context as the parent primitive (with the `s = 1.0` anchors `rap.cpp:186`,
`waveportoperator.cpp:73`), but it is recorded as the parent shape, not authored here — it is a
distinct (non-zeroing) operator and out of this theme's scope.

## Verified-against

L0 evidence ranges (self-verified via `tools/citecheck/citecheck.py --anchor` this invocation,
plus a direct on-disk Read of the body close-brace boundaries `:474` / `:492` per the FE-source
close-brace END-line guard):

- `palace/linalg/vector.hpp:220-221` — the declaration
  `template <typename VecType> void SetSubVector(VecType &x, const mfem::Array<int> &rows,
  double s);` + doc-comment "Sets all entries of the vector corresponding to the given indices
  to the given (real) value". Citecheck `--anchor 'SetSubVector'` → line 221, in-range
  (zero-drift). The signature anchor.
- `palace/linalg/vector.cpp:461-474` — the **real** body `SetSubVector(Vector &x, const
  mfem::Array<int> &rows, double s)`: `x.ReadWrite(use_dev)` destination `:467`, `rows.Read`
  gather `:466`, `forall_switch` `:468`, per-index write `X[id] = sr` `:472`. The `s = 0.0` case
  is the zeroing. Citecheck `--anchor 'SetSubVector(Vector &x'` → line 461; `--anchor 'X[id] =
  sr'` → line 472. Close brace `}` confirmed at `:474` by direct on-disk Read.
- `palace/linalg/vector.cpp:476-492` — the **complex** body
  `SetSubVector(ComplexVector &x, const mfem::Array<int> &rows, double s)`: two-buffer threading
  `XR`/`XI` `:483-484`, per-index writes `XR[id] = sr` `:489` AND `XI[id] = 0.0` `:490`. Grounds
  the whole-complex-dof zeroing. Citecheck `--anchor 'SetSubVector(ComplexVector &x'` → line 477
  (in-range); `--anchor 'XR[id] = sr'` → line 489; `--anchor 'XI[id] = 0.0'` → line 490. Close
  brace `}` confirmed at `:492` by direct on-disk Read.
- `palace/linalg/divfree.cpp:173` — `linalg::SetSubVector(rhs, *bdr_tdof_list_M, 0.0);` — the
  divfree-projector use-site (Sub-pattern C). Confirmed via codemap read_range.
- `palace/linalg/gmg.cpp:194` — `linalg::SetSubVector(X[l - 1], *dbc_tdof_lists[l - 1], 0.0);` —
  the geometric-multigrid restriction-residual zeroing (Sub-pattern C). (Carried from the L1
  entry's self-verified Evidence block, c104.)
- `palace/linalg/distrelaxation.cpp:114` — `linalg::SetSubVector(x_G, *dbc_tdof_list_G, 0.0);` —
  distributive-relaxation aux-correction zeroing (Sub-pattern C; also `:143`). (Carried from L1
  entry, c104.)
- `palace/models/spaceoperator.cpp:945` — `linalg::SetSubVector(RHS, nd_dbc_tdof_lists.back(),
  0.0);` — driven per-ω assembled-RHS clean (Sub-pattern C; also `:959,:1031`). (Carried from L1
  entry, c104.)
- `palace/linalg/rap.cpp:186` — `linalg::SetSubVector(diag, dbc_tdof_list, 1.0);` — a **non-zero**
  scalar-set call (the parent general-scalar-set shape this theme's `s = 0.0` specialization sits
  under; recorded to ground the zeroing-vs-general distinction in §Applicability cond. 4 and
  §Speculative). (Carried from L1 entry, c104.)
- `book/src/L1/set_subvector_zero.md` — the firm c104 L1 operator this theme lowers (the LHS
  endpoint; `depends-on kind: lowers-to`).

```yaml
verified_against:
  - citation: palace/linalg/vector.hpp:220-221
    verdict: supports
    audited_at: 2026-06-05T092016Z
    note: template SetSubVector(VecType, rows, double s) declaration + doc-comment; citecheck --anchor 'SetSubVector' -> line 221 in-range, zero-drift.
  - citation: palace/linalg/vector.cpp:461-474
    verdict: supports
    audited_at: 2026-06-05T092016Z
    note: real SetSubVector(Vector, rows, double s) body; anchor 'SetSubVector(Vector &x' -> :461; X[id]=sr (sr=0 zeroing) -> :472; ReadWrite destination :467; rows.Read gather :466; close brace } confirmed on-disk at :474.
  - citation: palace/linalg/vector.cpp:476-492
    verdict: supports
    audited_at: 2026-06-05T092016Z
    note: complex SetSubVector(ComplexVector, rows, double s) body; anchor 'SetSubVector(ComplexVector &x' -> :477; XR[id]=sr -> :489; XI[id]=0.0 (literal, whole-dof zero) -> :490; two-buffer XR/XI :483-484; close brace } confirmed on-disk at :492.
  - citation: palace/linalg/divfree.cpp:173
    verdict: supports
    audited_at: 2026-06-05T092016Z
    note: SetSubVector(rhs, *bdr_tdof_list_M, 0.0) divfree RHS boundary-zeroing use-site (Sub-pattern C); confirmed via codemap read_range.
  - citation: palace/linalg/gmg.cpp:194
    verdict: supports
    audited_at: 2026-06-05T092016Z
    note: SetSubVector(X[l-1], *dbc_tdof_lists[l-1], 0.0) gmg restriction-residual zeroing (Sub-pattern C); carried self-verified from L1/set_subvector_zero Evidence (c104).
  - citation: palace/linalg/distrelaxation.cpp:114
    verdict: supports
    audited_at: 2026-06-05T092016Z
    note: SetSubVector(x_G, *dbc_tdof_list_G, 0.0) distrelaxation aux-correction zeroing (Sub-pattern C); carried self-verified from L1 entry (c104).
  - citation: palace/models/spaceoperator.cpp:945
    verdict: supports
    audited_at: 2026-06-05T092016Z
    note: SetSubVector(RHS, nd_dbc_tdof_lists.back(), 0.0) driven per-omega RHS clean (Sub-pattern C, also :959/:1031); carried from L1 entry (c104).
  - citation: palace/linalg/rap.cpp:186
    verdict: supports
    audited_at: 2026-06-05T092016Z
    note: SetSubVector(diag, dbc_tdof_list, 1.0) NON-zero scalar-set — the parent general index-set scalar-set shape this s=0.0 theme specializes; grounds zeroing-vs-general distinction; carried from L1 entry (c104).
  - citation: book/src/L1/set_subvector_zero.md
    verdict: positive-cross-reference
    audited_at: 2026-06-05T092016Z
    note: the firm c104 L1 operator this theme lowers (LHS endpoint; depends-on kind lowers-to).
```

## Status

`firm` — the rewrite is the structural expansion of the L1 pure-functional diagonal projector
`Z_idx = I − P_idx` into its L0 in-place receiver-argument zeroing surface, exhaustively pinned
by direct, self-verified positive evidence: the two `double`-valued `SetSubVector` bodies read in
full (real `vector.cpp:461-474` with the per-index write `X[id] = sr` at `:472`; complex
`:476-492` with `XR[id] = sr` `:489` and `XI[id] = 0.0` `:490`), the declaration
`vector.hpp:220-221`, and the ~40-site `s = 0.0` consumer cohort (divfree `divfree.cpp:173`, gmg
`gmg.cpp:194`, distrelaxation `distrelaxation.cpp:114,143`, spaceoperator
`spaceoperator.cpp:945,959,1031`). Every claim is a **syntactic identity on fully-specified
positive source** — the L0 kernel writes the literal projector definition verbatim, with no
literature inference and no negative-anchor reconstruction, so `firm` rather than
`partly-constructive`.

Per the firm-on-positive-structure precedent (the BLAS-1 leaf thin-themes
[`scal-mutation-rotation`](./scal-mutation-rotation.md),
[`reciprocal-elementwise-product-mutation-rotation`](./reciprocal-elementwise-product-mutation-rotation.md),
and the sibling BC operators), the absence of a dedicated `SetSubVector` unit test under
`reference/palace/test/unit/` does **not** gate `firm`: the projector laws are syntactic
identities, not iteration/convergence facts, so the missing test does not reduce
law-confidence. Behaviour is exercised indirectly through the divfree / gmg / distrelaxation /
driven consumer paths (Sub-pattern C). Hence `firm`, not `rough-in (test-coverage-bounded)`.

**Well-foundedness (graded-stack rank invariant).** The theme's `depends-on` edges are: the L1
source entry `L1/set_subvector_zero` (firm, rank 3, c104) via `kind: lowers-to`, and the L0
sites via `kind: cites-evidence` (rank-terminal ground truth). Per the graded-stack §5
lowering-theme rule, `rank(theme) = min(rank(L1-endpoint), rank(L0-endpoint)) = min(firm,
terminal) = firm` (rank 3), and `rank(theme) ≤ min(endpoints)` holds for free. The L1 entry
remains firm-grounded on its own positive L0 read (NOT on this theme — the lowering edge is a
downward narration, not an upward rank-blocking dependency).

**Caveats (not status reductions):**

- **Receiver-argument destination is a third destination-binding variant.** Unlike `scal`'s
  `*this` receiver (`x *= α`) or `apply_linop`'s separate `y` output-arg (`A.Mult(x, y)`), the
  destination here is the **first function argument** `x` (`SetSubVector(x, …)`), read AND
  written via `x.ReadWrite`. Recorded so the destination idiom is recognized at consuming sites.
- **Complex imaginary write is a hard literal `0.0`.** `XI[id] = 0.0` (`:490`) is independent of
  `sr`; the `double`-valued `SetSubVector` sets the real part to `s` and ALWAYS zeros the
  imaginary part. For the `s = 0.0` zeroing case the two coincide; the general (`s ≠ 0`) parent
  shape would zero the imaginary part while setting the real part to `s` — recorded so the
  imaginary-always-zero behaviour is not read as a zeroing-specific kernel.
- **No `s = 0.0` constant-folding fast path.** The zeroing runs the general `X[id] = sr` write
  with `sr = 0`; the specialization is a call-shape fact, not a kernel branch. (Contrast `axpy`'s
  `α == 1.0` skip.)
- **No MPI collective at any layer.** Rank-local element-loops over disjoint dof-axis slices;
  MPI distribution out of scope per CLAUDE.md §Scope.
- A `lowering-verifier` exhaustiveness audit (both element-type sub-patterns × the full `s = 0.0`
  consumer cohort, confirming no consumer passes a non-zero scalar through this path) is the
  standard follow-up, not a status reduction.

## Open questions / caveats

- **General `set_subvector(x, idx, s)` parent shape (`s ≠ 0`).** This theme lowers only the
  `s = 0.0` zeroing specialization. The parent general index-set scalar-set (`s = 1.0` at
  `rap.cpp:186`, `waveportoperator.cpp:73`) has no firm L1 home yet — it is recorded in
  [`L1/set_subvector_zero`](../L1/set_subvector_zero.md) §Variant axes as the parent. Whether the
  general scalar-set warrants its own L1 entry + lowering theme (vs staying a noted parent) is a
  future planner decision, not pursued here. No new OQ — covered by the L1 entry's existing
  parent-shape note.
- **Non-adjacent L1→L3 identity rotation.** The L1 entry §Downward annotates a speculative L3
  `set-subvector-zero-mask-multiply` form (a single mask-multiply `Z_S : V → V`) reachable with
  no obstruction (the per-index writes are independent → the per-element form rotates directly to
  the global tensor-field form). That is a future L3 seed, annotated in-line in the L1 entry per
  the non-adjacent-identity-rotation convention; this L1>L0 theme does not author it.
- **Consumer-theme edge retype.** [`divfree-projector-mutation-rotation`](./divfree-projector-mutation-rotation.md),
  gmg, distrelaxation, and the driven RHS-clean themes (where authored) *use* this zeroing at
  their BC-clean steps. With this theme landed, those consumer themes' references to the zeroing
  become live-node references; an edge-retype follow-up (out of this one-theme scope) is flagged
  for a future lifter/cross-cutter pass. (Same posture as the L1 entry's Dependencies note.)
```

```edit:book/src/L1-L0/index.md
| [scal-mutation-rotation](./scal-mutation-rotation.md) | `L1/scal` (firm) | `palace/linalg/vector.{hpp,cpp}`, `palace/linalg/{iterative,operator,nleps}.cpp` | firm *(structural; 2 element-type overloads; transparent complex imag==0 shape branch)* |
| [set-subvector-zero-mutation-rotation](./set-subvector-zero-mutation-rotation.md) | [`L1/set_subvector_zero`](../L1/set_subvector_zero.md) (firm c104) | `palace/linalg/vector.cpp:461-474` (real) / `:476-492` (complex), `vector.hpp:220-221` (decl); consumer cohort `divfree.cpp:173`, `gmg.cpp:194`, `distrelaxation.cpp:114,143`, `spaceoperator.cpp:945,959,1031` | firm *(structural; clean syntactic-identity mutation rotation — diagonal 0/1 orthogonal projector `Z_idx = I − P_idx` value → in-place `SetSubVector(x, rows, 0.0)` receiver-ARGUMENT zeroing via `x.ReadWrite` + `forall_switch` `X[id]=sr` (sr=0); 2 element-type sub-patterns A real / B complex two-buffer (whole-dof zero, `XI[id]=0.0` hard literal :490) + use-site cohort C; THIRD destination-binding variant (first-argument-as-destination, vs `scal` `*this`-receiver / `apply_linop` `y`-output-arg); independent writes → no-reduction non-law → clean projector lowering; `s=0.0` is a call-shape specialization not a kernel branch — general `s≠0` parent shape (`rap.cpp:186`) noted not folded; firm-on-positive-structure syntactic-identity escape, no-dedicated-test caveat non-gating)* |
| **Construction-rotation** | | | |
```

```edit:book/src/SUMMARY.md
  - [scal-mutation-rotation](./L1-L0/scal-mutation-rotation.md)
  - [set-subvector-zero-mutation-rotation](./L1-L0/set-subvector-zero-mutation-rotation.md)
- [Construction-rotation themes](./L1-L0/construction-rotation-intro.md)
```

## COUPLED de-stale — repoint `L1/set_subvector_zero` "(forthcoming)" forward-refs to the live theme

The c104 repairer left three plain-text "(forthcoming)" forward-references in
`book/src/L1/set_subvector_zero.md` (§Semantics, §Downward to L0) plus the frontmatter comment,
correctly avoiding a dangling `depends-on` to the then-missing theme file. With the theme now
authored, those forward-refs become live links. The L1 entry's firmness still grounds on its own
positive L0 read (NOT on the theme) — so the lowering relationship stays a `reference` edge
(downward navigational pointer), NOT a `depends-on` (the theme depends on the entry, not vice
versa; a `depends-on` from the firm entry to the theme would also be a rank-direction error). I
add the theme as a `reference` edge in the frontmatter and convert the three prose notes to live
links.

```edit:book/src/L1/set_subvector_zero.md
  reference:
    - L1/eliminate_essential_bc
    - L1/eliminate_rhs
    - L1/divfree-projector
    - concepts/set_subvector_zero
    - L1-L0/set-subvector-zero-mutation-rotation   # the L1>L0 lowering theme (authored c105); downward navigational pointer, NOT a rank-blocking dependency (the theme depends-on THIS entry, not vice versa)
# The L1>L0 lowering theme `set-subvector-zero-mutation-rotation` is AUTHORED (c105); it is a
# `reference` edge above (downward navigational pointer) + live-link forward-refs in §Semantics /
# §Downward, NOT a blocking depends-on edge (the firmness grounds on the positive L0 read below;
# the theme depends-on this entry, so a depends-on from here to the theme would be a rank-direction
# error as well as redundant).
# The speculative L3 form `set-subvector-zero-mask-multiply` is a plain-text future-form note
# in §Downward, NOT a live reference edge (the seed does not exist).
```

```edit:book/src/L1/set_subvector_zero.md
The in-place overwrite, the device-vs-host `use_dev` dispatch, the
`rows.Read(use_dev)` index gather, and the `mfem::forall_switch` kernel are **L1>L0 lowering
concerns** (the [`set-subvector-zero-mutation-rotation`](../L1-L0/set-subvector-zero-mutation-rotation.md)
theme, authored c105), not part of the L1 signature.
```

```edit:book/src/L1/set_subvector_zero.md
The lowering is the [`set-subvector-zero-mutation-rotation`](../L1-L0/set-subvector-zero-mutation-rotation.md)
L1>L0 theme (authored c105; this entry's firmness rests on the positive L0 read,
cited as `cites-evidence` deps, with the theme as a downward `reference` pointer, not a blocking
edge): it narrates how this
pure projector lowers into Palace's in-place index-set overwrite —
the `x.ReadWrite(use_dev)` destination-is-input idiom (`vector.cpp:467` / `:483-484`), the
`rows.Read(use_dev)` index gather (`:466` / `:482`), the `mfem::forall_switch` device-vs-host
kernel dispatch (`:468` / `:485`), and the complex `XR`/`XI` two-buffer threading
(`:483-484, 489-490`). All of these are L0 mechanism; the L1 signature carries none of them.
```

## Speculative operators proposed

**None.** This theme lowers the already-firm L1 leaf `L1/set_subvector_zero` (c104). It proposes
no new L1 vocabulary. The general index-set scalar-set parent shape (`s ≠ 0`) is noted as the
parent in the L1 entry §Variant axes, not authored here (a distinct future operator decision).

## Supporting evidence

- `palace/linalg/vector.cpp:461-474` — real `SetSubVector(Vector &x, …, double s)` body;
  `X[id] = sr` write at `:472`, `x.ReadWrite` destination `:467`, `rows.Read` gather `:466`.
  Codemap read_range + on-disk Read (close brace `}` at `:474`); citecheck `--anchor` zero-drift.
- `palace/linalg/vector.cpp:476-492` — complex `SetSubVector(ComplexVector &x, …, double s)`
  body; `XR[id] = sr` `:489`, `XI[id] = 0.0` `:490`, two-buffer `XR`/`XI` `:483-484`. Codemap +
  on-disk Read (close brace `}` at `:492`); citecheck `--anchor` zero-drift.
- `palace/linalg/vector.hpp:220-221` — the `template <typename VecType> void SetSubVector(VecType
  &x, const mfem::Array<int> &rows, double s);` declaration + doc-comment. Codemap + citecheck
  `--anchor 'SetSubVector'` → line 221 in-range.
- `palace/linalg/divfree.cpp:173` — `SetSubVector(rhs, *bdr_tdof_list_M, 0.0)` use-site; codemap
  read_range confirmed.
- `book/src/L1/set_subvector_zero.md` — the firm c104 L1 endpoint; its §Evidence block carries
  the gmg / distrelaxation / spaceoperator / rap.cpp consumer-cohort citations (self-verified
  c104) reused here for Sub-pattern C.
- `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` +
  `book/src/L1-L0/scal-mutation-rotation.md` — the convention/structural-template siblings (same
  BLAS-1-leaf in-place→pure rewrite class, indented-code-block authoring convention).

## Open questions / caveats

- **Consumer-theme edge retype (flagged, out of scope).** The divfree / gmg / distrelaxation /
  driven RHS-clean themes *use* this zeroing; with the theme landed their references to it become
  live-node references — an edge-retype follow-up for a future lifter/cross-cutter pass.
- **General `set_subvector(x, idx, s)` (`s ≠ 0`) L1 candidacy.** The parent index-set scalar-set
  has no firm L1 home; recorded as the parent in the L1 entry. Whether it warrants its own entry +
  theme is a future planner decision.
- **L1 entry de-stale verified build-safe.** All three repointed forward-refs + the new
  frontmatter `reference` edge resolve to the now-authored
  `book/src/L1-L0/set-subvector-zero-mutation-rotation.md` (live links, no dangling); the
  SUMMARY.md entry is alpha-placed; the index dep-map row uses live-link syntax (the anchor file
  is created in the same proposed-changes set). No `linkcheck2` hard error expected.
