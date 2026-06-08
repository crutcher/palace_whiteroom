# orthogonalize-mutation-rotation

The mutation rotation for Gram-Schmidt column orthogonalisation. Lowers the pure L1 form
`orthogonalize(w, V, variant) = (w', H)` (see [`L1/orthogonalize`](../L1/orthogonalize.md))
into Palace's header-only inline in-place L0 free functions, which overwrite the candidate
vector `w` in place and write the projection coefficients through a raw pointer. The
`variant` parameter (`MGS | CGS | CGS2`) selects between **three distinct L0 loop
structures**; this is the load-bearing axis of the theme.

## Slug

`orthogonalize-mutation-rotation`

## L1 form (LHS)

The pure-functional orthogonalisation consumes the prior candidate `w`, the read-only basis
`V`, and the variant tag; it produces a fresh pair `(w', H)` with no destination buffers in
the signature (firm; see [`L1/orthogonalize`](../L1/orthogonalize.md)):

      (w', H) = orthogonalize(w, V, variant)
      -- H[j] = ⟨w_eff(j), V[j]⟩ ;   w' = w − Σ_j H[j]·V[j]
      -- w_eff(j) = w (CGS/CGS2)  |  progressively-updated w^(j) (MGS)

`w'` is the `span(V)`-orthogonal residual (**not normalised** — the header contract); `H` is
the length-`m` coefficient vector (the leading entries of the Arnoldi/Hessenberg column).
The L1 form drops both L0 destination buffers (`w` overwrite, raw `H` pointer) and the
`MPI_Comm`. The runtime variant is inspected exactly once.

## L0 form (RHS)

Three sub-patterns of the same rewrite, distinguished by the `variant` tag. All three are
header-only inline mutating free functions that **overwrite `w` in place** via
`w.Add(-h, V[j])` (MFEM `Vector::Add` / `ComplexVector::AXPY`) and **write coefficients
through a raw `ScalarType *H` pointer** owned by the caller (the Hessenberg-column slice
`H.data() + j*(max_dim+1)`). The candidate destination is the named in/out `VecType &w`
argument, not a returned value; the coefficient destination is the raw pointer, not a
returned array. This is the central L1→L0 rebinding: the L1 pair `(w', H)` materialises as
mutation of the two caller-owned buffers.

The runtime dispatch over the three variants is the wrapper `OrthogonalizeIteration`
(`palace/linalg/iterative.cpp:307-325`), which `switch`es on the `Orthogonalization` enum
and forwards `j + 1` as the column count `m` (so the call orthogonalises `w` against the
leading `j + 1` columns); the ROM path uses a sibling wrapper `OrthogonalizeColumn`
(`palace/models/romoperator.cpp:51-66`) that forwards `j` and threads the `dot_op` hook.
The variant is bound at solver construction and dispatched once — never re-inspected
per column.

### Sub-pattern A — MGS (single interleaved loop)

    template <typename VecType, typename ScalarType, typename InnerProductW>
    inline void OrthogonalizeColumnMGS(MPI_Comm comm, const std::vector<VecType> &V,
                                       VecType &w, ScalarType *H, std::size_t m,
                                       const InnerProductW &dot_op = {})
    {
      for (std::size_t j = 0; j < m; j++)
      {
        H[j] = dot_op(w, V[j]);     // global inner product (order matters for complex)
        Mpi::GlobalSum(1, &H[j], comm);
        w.Add(-H[j], V[j]);         // in-place residual update
      }
    }

One `j`-loop. Each iteration does dot → reduce(size 1) → in-place `w.Add` **before** the
next iteration's dot. The `w.Add` in iteration `j` is read by the dot in iteration `j+1`
(`dot_op(w, V[j+1])` sees the updated `w`). This interleaving in a single loop body is the
L0 witness of the MGS sequential dependency: `w_eff(j) = w^(j)`, the progressively-updated
candidate. Collective shape: **`m` reductions of size 1.**

Justification kind: **structural** — the L1 sequential-dependency semantics (`w^(j+1) =
w^(j) − H[j]·V[j]`) is realised verbatim as the in-place overwrite threaded through the
loop; the in-place `w` IS the `w^(j)` intermediate.

Citations:
- `palace/linalg/orthog.hpp:41-53` — `OrthogonalizeColumnMGS`: the single `j`-loop with
  `H[j] = dot_op(w, V[j]); Mpi::GlobalSum(1, &H[j], comm); w.Add(-H[j], V[j])`.
- `palace/linalg/orthog.hpp:48` — `// Global inner product: Note order is important for
  complex vectors.` (the conjugation order, inherited by L1 `dot`).

### Sub-pattern B — CGS (split two-phase loop)

    template <typename VecType, typename ScalarType, typename InnerProductW>
    inline void OrthogonalizeColumnCGS(MPI_Comm comm, const std::vector<VecType> &V,
                                       VecType &w, ScalarType *H, std::size_t m,
                                       bool refine = false, const InnerProductW &dot_op = {})
    {
      if (m == 0) { return; }                       // empty-basis early return
      for (std::size_t j = 0; j < m; j++)
      {
        H[j] = dot_op(w, V[j]);                     // m local dots against the ORIGINAL w
      }
      Mpi::GlobalSum(m, H, comm);                   // single reduction of size m
      for (std::size_t j = 0; j < m; j++)
      {
        w.Add(-H[j], V[j]);                         // m in-place updates
      }
      // ... refine branch (sub-pattern C) ...
    }

Two separated `j`-loops with an early return for `m == 0`. **Phase 1** computes all `m`
local dots against the *unmodified original* `w` (`w_eff(j) = w` for every `j`), one
size-`m` reduction batching them. **Phase 2** applies all `m` in-place `w.Add`s. Because
the dots are all taken before any `w.Add`, the per-`j` dots are mutually independent — the
L0 witness that CGS has no inter-`j` dependency. Collective shape: **1 reduction of size
`m`** (the `refine=false` path). The `m == 0` early return is the L0 realisation of the
empty-basis identity law (`orthogonalize(w, [], variant) = (w, [])`).

Justification kind: **structural** — the L1 "every coefficient against the same original
`w`" semantics is realised by ordering all dots before all updates; the two-phase split is
exactly the absence of the MGS interleaving.

Citations:
- `palace/linalg/orthog.hpp:57-74` — `OrthogonalizeColumnCGS` (`refine=false` path): the
  `m == 0` early return, the `m`-local-dot loop, the single `Mpi::GlobalSum(m, H, comm)`,
  the `m`-`w.Add` loop.
- `test/unit/test-orthog.cpp:99-120` — empty-basis edge: all three variants leave `w`
  unchanged at `m = 0` (the `if (m == 0) return;` and the MGS/CGS2 zero-iteration loops
  both witness law 3).

### Sub-pattern C — CGS2 (doubled two-phase loop)

      // ... inside OrthogonalizeColumnCGS, after the first CGS pass ...
      if (refine)
      {
        std::vector<ScalarType> dH(m);
        for (int j = 0; j < m; j++)
        {
          dH[j] = dot_op(w, V[j]);                  // second-pass local dots
        }
        Mpi::GlobalSum(m, dH.data(), comm);         // second reduction of size m
        for (std::size_t j = 0; j < m; j++)
        {
          H[j] += dH[j];                            // accumulate correction into H
          w.Add(-dH[j], V[j]);                      // second in-place residual update
        }
      }

CGS2 is the CGS body (sub-pattern B) followed by a second, structurally-identical CGS pass
into a scratch `dH` array. The second pass reads the *once-orthogonalised* `w` left by phase
2, computes a correction `dH`, **accumulates** it into the caller's `H` (`H[j] += dH[j]` —
so the returned coefficients are the full projection `H + dH`), and applies a second round
of in-place `w.Add(-dH[j], V[j])`. The third loop fuses the accumulate and the update into
one body. The second pass is *not* algebraically fusible with the first (it reads the first
pass's output — "twice is enough", Kahan/Parlett). Collective shape: **2 reductions of size
`m`**. The `dH` scratch buffer is a transient (the L1 form returns only the summed `H`).

Justification kind: **algebraic** — the L1 CGS2 law `H_returned = H + dH`, `w' =
twice-projected w` grounds the accumulate-and-re-update; the re-application is the explicit
re-use of the idempotence law (law 4) that floating-point breaks.

Citations:
- `palace/linalg/orthog.hpp:75-88` — the `if (refine)` block: `dH` scratch, second
  local-dot loop, second `Mpi::GlobalSum(m, dH.data(), comm)`, the `H[j] += dH[j];
  w.Add(-dH[j], V[j])` accumulate-and-update loop.
- `palace/linalg/iterative.cpp:322` — `CGS2 = OrthogonalizeColumnCGS(comm, V, w, Hj,
  j + 1, true)`: the dispatch witness that CGS2 is the `refine = true` parametrisation.

## Applicability conditions

The rewrite (L1 `(w', H)` ⟸ L0 mutation of `w` + raw `H` write) preserves semantics when:

1. **No observer of the prior `w` value after the call.** The L0 call destroys the prior
   candidate `w` in place. At L1 the input `w` and output `w'` are distinct values; the
   lowering is valid only because every Palace call site discards the prior `w` after the
   orthogonalisation. Upheld lexically: GMRES (`iterative.cpp:630`) and FGMRES
   (`iterative.cpp:809`) read `w` only via the subsequent `Norml2(comm, w)` / `w *=
   1/Hj[j+1]`, i.e. they consume `w'`, never `w_old`.
2. **Caller owns and sizes the `H` buffer.** The raw `ScalarType *H` must point at ≥ `m`
   writable slots (the Hessenberg-column slice `H.data() + j*(max_dim+1)`); the L1 `H`
   result of length `m` materialises into those slots. The `MFEM_ASSERT(m <= V.size())`
   bounds-check guards the `V` read, not the `H` write — `H` sizing is the caller's
   contract.
3. **Basis columns are normalised; output is not.** The header contract
   (`orthog.hpp:18-23`): inputs assumed `‖V[j]‖ = 1` and mutually orthogonal; the output
   `w'` is **not** normalised. The caller's `Norml2` + `*= 1/‖w'‖` (`iterative.cpp:631-632`,
   `810-811`) is a *separate* step, outside this theme — the sub-diagonal `Hj[j+1] = ‖w'‖`
   is the caller's, not a coefficient this rewrite produces.
4. **No aliasing in the `w.Add(-h, V[j])` update.** `V[j]` is read while `w` is written;
   `w` must not alias any `V[j]`. Palace stores `V` and the candidate as distinct vectors
   (`V[j+1]` is the candidate slot in GMRES, `iterative.cpp:622`), so this holds.
5. **Single-rank collapse of the MPI reduction.** `Mpi::GlobalSum(n, ptr, comm)` collapses
   to a no-op local reduction under single-rank scope (per CLAUDE.md). The *number and
   size* of `GlobalSum` calls — `m`×size-1 (MGS), 1×size-`m` (CGS), 2×size-`m` (CGS2) — is
   the load-bearing variant cost-shape, recorded here as a per-sub-pattern property; it does
   not change the lowered value, only the collective shape. Flagged once: MPI is out of
   scope; the collective is read as a local sum over the single rank's DOFs.

## Justification kind

- **Sub-pattern A (MGS)** — `structural`. The in-place `w` threaded through the single loop
  IS the `w^(j)` intermediate; the sequential dependency is the loop carry.
- **Sub-pattern B (CGS)** — `structural`. The two-phase split (all dots, then all updates)
  is the absence of the MGS carry; the `m == 0` early return is the empty-basis law.
- **Sub-pattern C (CGS2)** — `algebraic`. `H_returned = H + dH`, twice-projected `w'`; the
  re-application is the idempotence law that floating-point breaks.

The theme as a whole is `structural` (the dominant rewrite is the buffer-rebinding of
`(w', H)` into in-place `w` + raw `H`), with the variant axis distinguishing three L0
loop-structures and one algebraic sub-rule (CGS2). Each variant's collective shape (m×1 /
1×m / 2×m) is read directly from the function bodies — no reconstruction.

## Speculative L1 operators

None. Both L1 dependencies the lowered forms compose — [`dot`](../L1/dot.md) (the
`dot_op(w, V[j])` inner product) and [`axpy`](../L1/axpy.md) (the `w.Add(-h, V[j])` rank-1
update) — are already firm, and `orthogonalize` itself is firm. This theme proposes no new
operators; it is a pure lowering of an existing firm operator onto existing firm leaves.
(The inner-product hook variant — identity vs B-weighted `dot_op` — is a substitution of
the firm `dot` dependency, not a new operator; see the L1 entry's "inner-product hook"
variant axis.)

## Evidence

L0 evidence ranges (positive source sites):

- `palace/linalg/orthog.hpp:18-23` — header scope contract (assumes normalised input, does
  NOT normalise output).
- `palace/linalg/orthog.hpp:25-37` — `IdentityInnerProduct` / `InnerProductHelper`: the
  `dot_op` template hook (`LocalDot` + the MPI reduction added by the routine).
- `palace/linalg/orthog.hpp:41-53` — `OrthogonalizeColumnMGS`: single interleaved loop
  (sub-pattern A); `m` reductions of size 1.
- `palace/linalg/orthog.hpp:57-74` — `OrthogonalizeColumnCGS` (`refine=false`): empty-basis
  early return + split two-phase loop (sub-pattern B); 1 reduction of size `m`.
- `palace/linalg/orthog.hpp:75-88` — the `if (refine)` block (sub-pattern C): doubled
  two-phase loop with `H[j] += dH[j]` accumulate + second `w.Add`; 2 reductions of size `m`.
- `palace/linalg/iterative.cpp:307-325` — `OrthogonalizeIteration`: runtime variant
  dispatch (`switch` over `MGS / CGS / CGS2`; `CGS2 = ...(true)`; forwards `j + 1` as `m`).
- `palace/linalg/iterative.cpp:629-632` — GMRES Arnoldi call site: `OrthogonalizeIteration(
  gs_orthog, comm, V, w, Hj, j)` immediately followed by `Hj[j+1] = Norml2(comm, w);
  w *= 1.0/Hj[j+1]` — confirms normalisation is the caller's (applicability condition 3).
- `palace/linalg/iterative.cpp:808-811` — FGMRES Arnoldi call site: same pattern (second
  consumer of the dispatch wrapper).
- `palace/models/romoperator.cpp:51-66` — ROM `OrthogonalizeColumn` sibling dispatch:
  forwards `j` (not `j + 1`) and threads the `dot_op` hook (the B-weighted inner-product
  consumer; third call-site family).
- `test/unit/test-orthog.cpp:99-120` — empty-basis edge: all three variants leave `w`
  unchanged at `m = 0` (sub-pattern B's `if (m == 0) return;` + the zero-iteration loops).

- `palace/utils/labels.hpp:165-170` — `enum Orthogonalization {MGS, CGS, CGS2}` — the
  recognition set is provably exhaustive (exactly 3 variants).

L1 anchor:

- `book/src/L1/orthogonalize.md` — the firm L1 operator that all three sub-patterns lower
  from.

## Status

`firm` — every L0 form is read in full from a positive source site
(`orthog.hpp:18-90`, header-only inline), the dispatch wrapper and both call-site families
(GMRES/FGMRES Arnoldi + ROM) are read directly, and the three variant loop-structures plus
their collective shapes (m×1 / 1×m / 2×m) are read off the function bodies — no sub-part is
reconstructed from negative anchors or literature. The `structural` justification is the
buffer-rebinding of the L1 pair `(w', H)` into in-place `w` + raw-pointer `H`; the CGS2
algebraic sub-rule (`H_returned = H + dH`) is grounded in the explicit `H[j] += dH[j]`
accumulate at `orthog.hpp:85`. The MGS/CGS/CGS2 recognition set is exhaustive (the enum has
exactly 3 variants; the dispatch wrappers are the only two call-site families).
