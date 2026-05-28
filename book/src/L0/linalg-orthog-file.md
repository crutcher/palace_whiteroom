# File — `palace/linalg/orthog.hpp`

A reference note for the firm L1 [`orthogonalize`](../L1/orthogonalize.md) operator and the
`concepts/` pages [`orthogonalization`](../concepts/orthogonalization.md) /
[`gemv_basis`](../concepts/gemv_basis.md). `palace/linalg/orthog.hpp` is **header-only**
(93 lines; there is no `orthog.cpp`) and houses Palace's entire vector-against-basis
Gram-Schmidt family: the two inline column-orthogonalisation routines `OrthogonalizeColumnMGS`
and `OrthogonalizeColumnCGS` (with a `refine` flag that selects classical-Gram-Schmidt-twice,
"CGS2"), plus the `IdentityInnerProduct` policy struct they default to. Sibling to
[`linalg-iterative-file`](./linalg-iterative-file.md), which holds the runtime dispatch
wrapper (`OrthogonalizeIteration`) that switches the `Orthogonalization` enum
(`MGS | CGS | CGS2`) over these two routines.

## At a glance

The header (`palace/linalg/orthog.hpp:1-93`) declares, inside `namespace palace::linalg`
(opened at line 15):

- **`IdentityInnerProduct`** (line 30) — a small policy struct supplying the default
  inner-product functor; the two orthogonalisation templates are parameterised on an
  inner-product type and default to this when the caller wants the plain Euclidean dot.
- **`OrthogonalizeColumnMGS`** (lines 41-53) — *modified* Gram-Schmidt. Sequentially
  subtracts each basis projection from the candidate before computing the next coefficient
  (`m` sequential dots, each followed by an `AXPY`-style update). The numerically-stabler,
  more-communication-bound variant.
- **`OrthogonalizeColumnCGS`** (lines 57-89) — *classical* Gram-Schmidt. Computes all `m`
  projection coefficients against the *original* candidate in one batch (one fused
  multi-dot), then applies the combined update. The `refine` parameter re-runs the whole
  pass once more (`CGS2`), trading a second communication round for restored orthogonality.

Both routines take `(MPI_Comm comm, const std::vector<VecType> &V, VecType &w, ...)`:
read-only stored basis `V[0..m-1]`, in-place candidate `w` (overwritten with its
orthogonal residual), and an output coefficient array (the leading Hessenberg/Arnoldi
column). The `MPI_Comm` parameter is the collective handle for the inner-product reductions;
per the single-rank reading rule ([`par-types-single-rank-reading`](./par-types-single-rank-reading.md))
the `comm`-scoped `GlobalSum` collapses to a local reduction at L1.

## The two variants and what each buys

The MGS / CGS split is **load-bearing numerical structure**, not a transparent trick
(per [`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md)):
the two routines compute the same mathematical projection but with different rounding-error
accumulation and different communication patterns:

- **MGS** — `m` sequential reductions; each projection is taken against the *partially
  orthogonalised* candidate. Better orthogonality in finite precision; `m` separate
  `GlobalSum` round-trips (latency-bound at scale).
- **CGS** — one batched reduction of all `m` coefficients against the *original* candidate;
  a single `GlobalSum` of an `m`-vector (bandwidth-bound, one round-trip). Cheaper
  communication, worse orthogonality.
- **CGS2** (`OrthogonalizeColumnCGS(..., refine=true)`) — CGS applied twice. "Twice is
  enough" (Giraud et al.): two CGS passes recover MGS-level orthogonality at two
  round-trips instead of `m`. This is the variant Palace's GMRES default uses.

The runtime selection over these three lives one file away in `iterative.cpp` (the
`OrthogonalizeIteration` wrapper, `palace/linalg/iterative.cpp:308-325`), not here; this
header is purely the per-variant algebra.

## Notes for higher layers

- **The three variants become L1's single runtime variant axis.** The firm L1
  [`orthogonalize`](../L1/orthogonalize.md) operator carries one variant axis
  (`MGS | CGS | CGS2`) that maps exactly onto these two routines plus the `refine` flag.
  The `IdentityInnerProduct` default is absorbed (L1 takes the inner product as the plain
  field dot unless a weighted form is requested).
- **The in-place `w` overwrite is L0-internal** ([`output-arg-vs-receiver`](./output-arg-vs-receiver.md)):
  the L1 form returns a fresh orthogonal residual `w'` plus the coefficient column `H`
  rather than mutating `w`.
- **The `comm` argument is the only `Par`-adjacent surface** and collapses under
  single-rank reading; the routines themselves are otherwise rank-agnostic
  (`std::vector<VecType>` of local vectors).

## Referenced from

- [`L1/orthogonalize`](../L1/orthogonalize.md) — the firm operator that lifts this family.
- [`L0/linalg-iterative-file`](./linalg-iterative-file.md) — sibling file holding the
  `OrthogonalizeIteration` runtime dispatch wrapper over these two routines.
- [`concepts/orthogonalization`](../concepts/orthogonalization.md) — the cross-cutting
  narrative.
- [`concepts/gemv_basis`](../concepts/gemv_basis.md) — the batched-projection (CGS) form
  as a GEMV-against-the-basis.

## Evidence (representative)

- `palace/linalg/orthog.hpp:1-93` — the header file (header-only; no `orthog.cpp`).
- `palace/linalg/orthog.hpp:15` — `namespace palace::linalg` open.
- `palace/linalg/orthog.hpp:30` — `struct IdentityInnerProduct` (default inner-product policy).
- `palace/linalg/orthog.hpp:41-53` — `OrthogonalizeColumnMGS` template (modified Gram-Schmidt; `m` sequential dots).
- `palace/linalg/orthog.hpp:57-89` — `OrthogonalizeColumnCGS` template (classical Gram-Schmidt; batched multi-dot; `refine` flag → CGS2).
- `palace/linalg/iterative.cpp:308-325` — `OrthogonalizeIteration` runtime dispatch (`switch` over `MGS | CGS | CGS2`; CGS2 = `OrthogonalizeColumnCGS(..., refine=true)`); the construction side, in the sibling file.
