---
agent: abstractor
invoked_at: 2026-05-28T14:40:01Z
scope: L1>L0 theme sketch — orthogonalize-mutation-rotation
status: integrated
integrated_at: 2026-05-28T200000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-013 finalize. New firm/structural L1>L0 theme landed (3 L0 variant loop-structures MGS/CGS/CGS2; repaired codemap-corrected orthog.hpp citations); SUMMARY-registered. Link target for the position-11 concepts/orthogonalization rewrite + the L0 linalg-orthog-file chapter (both resolved). Clean run."
inputs:
  - book/src/L1/orthogonalize.md (firm L1 operator, cycle-012)
  - book/src/L1-L0/axpby-mutation-rotation.md (sibling-theme shape precedent)
  - book/src/L1-L0/apply-linop-mutation-rotation.md (sibling-theme shape precedent)
  - palace/linalg/orthog.hpp:18-90 (L0 source, read in full via codemap)
  - palace/linalg/iterative.cpp:307-325, 630-632, 809-811 (dispatch + GMRES/FGMRES call sites)
  - palace/models/romoperator.cpp:51-66 (ROM consumer, dot_op hook)
  - test/unit/test-orthog.cpp:99-120 (empty-basis edge)
---

# CYCLE: L1>L0 theme sketch — orthogonalize-mutation-rotation

## Summary

The firm L1 operator `orthogonalize` (`book/src/L1/orthogonalize.md`) consumes `(w, V,
variant)` and produces a fresh pair `(w', H)`: the `span(V)`-orthogonal residual plus the
projection coefficients. Palace's L0 realises this as two header-only inline mutating
free functions — `OrthogonalizeColumnMGS` and `OrthogonalizeColumnCGS` (the latter with a
`refine` flag selecting CGS2) in `palace/linalg/orthog.hpp` — that overwrite the candidate
`w` **in place** (`w.Add(-H[j], V[j])`) and write the coefficients through a raw `ScalarType
*H` pointer into the caller's Hessenberg-column buffer. This theme lowers the L1 form forward
into those L0 patterns: the `w'`→`w` in-place overwrite, the `H`-array raw-pointer write, the
inner-product reduction loop, and the **three distinct L0 loop-structures** of the MGS / CGS /
CGS2 variant axis (single interleaved loop; split two-phase loop; doubled two-phase loop). The
`MPI_Comm comm` + `Mpi::GlobalSum` collapse to a local reduction under single-rank scope —
flagged once. Every L0 form is read from a positive source site, so the theme is
`firm` / `structural`; the variant-distinguishing collective-shape facts (m×1 / 1×m / 2×m
reductions) are read directly from the function bodies, not reconstructed.

## Proposed changes

```edit:book/src/L1-L0/orthogonalize-mutation-rotation.md
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
- `palace/linalg/iterative.cpp:321-323` — `CGS2 = OrthogonalizeColumnCGS(comm, V, w, Hj,
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

## Verified-against

L0 evidence ranges (all read in full via codemap, positive source sites):

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

L1 anchor:

- `book/src/L1/orthogonalize.md` — the firm L1 operator (cycle-012) that all three
  sub-patterns lower from.

## Status

`firm` — every L0 form is read in full from a positive source site
(`orthog.hpp:18-90`, header-only inline), the dispatch wrapper and both call-site families
(GMRES/FGMRES Arnoldi + ROM) are read directly, and the three variant loop-structures plus
their collective shapes (m×1 / 1×m / 2×m) are read off the function bodies — no sub-part is
reconstructed from negative anchors or literature. The `structural` justification is the
buffer-rebinding of the L1 pair `(w', H)` into in-place `w` + raw-pointer `H`; the CGS2
algebraic sub-rule (`H_returned = H + dH`) is grounded in the explicit `H[j] += dH[j]`
accumulate at `orthog.hpp:85`. A future `lowering-verifier` audit should confirm the
sub-pattern recognition is exhaustive against the L0 corpus (the dispatch wrappers are the
only two call-site families; the free functions are not called directly elsewhere — see
codemap `get_call_sites` results in this report's Supporting evidence).
```

```edit:book/src/L1-L0/index.md
| [orthogonalize-mutation-rotation](./orthogonalize-mutation-rotation.md) | `L1/orthogonalize` (firm) | `palace/linalg/orthog.hpp`, `palace/linalg/iterative.cpp` | firm *(structural; 3 variant loop-structures)* |
```

```edit:book/src/SUMMARY.md
- [orthogonalize-mutation-rotation](./L1-L0/orthogonalize-mutation-rotation.md)
```

## Speculative operators proposed

None. This theme lowers an existing firm operator (`orthogonalize`) onto two existing firm
leaves (`dot`, `axpy`). No new vocabulary is required at any layer; the rewrite is a pure
buffer-rebinding plus variant-loop-structure enumeration. (Contrast the sibling
`axpby-mutation-rotation`, which proposed the rough-in `axpby`; this theme has no such
pending leaf.)

## Supporting evidence

- `codemap get_call_sites OrthogonalizeColumnMGS` → 3 sites: `iterative.cpp:316`
  (dispatch), `romoperator.cpp:59` (ROM dispatch), `test-orthog.cpp:87` (test harness).
- `codemap get_call_sites OrthogonalizeColumnCGS` → 6 sites: `iterative.cpp:319,322`
  (CGS + CGS2 dispatch), `romoperator.cpp:62,65` (ROM CGS + CGS2), `test-orthog.cpp:90,93`
  (test). Confirms the two free functions are reached ONLY through the two dispatch wrappers
  (`OrthogonalizeIteration` in iterative.cpp, `OrthogonalizeColumn` in romoperator.cpp) plus
  the test harness — no direct production call site bypasses the variant switch. This makes
  the sub-pattern recognition closed: the variant axis is the only L0 entry path.
- `palace/linalg/iterative.cpp:622` — `VecType &w = V[j + 1]`: the candidate occupies the
  next basis slot; `w` is distinct from `V[0..j]` (applicability condition 4, no aliasing).
- The `refine` branch's loop-index quirk (`for (int j = 0; j < m; j++)` with `int` vs the
  surrounding `std::size_t` — `orthog.hpp:78`) is a transparent signedness detail, not
  load-bearing; noted so a future verifier does not flag it as a semantic difference.

## Open questions / caveats

- **Naming parallel to the L1 entry.** The L1 operator is `orthogonalize` (vector-against-
  basis); the L0 functions are `OrthogonalizeColumn{MGS,CGS}` (column-faithful). The theme
  slug follows the L1 verb (`orthogonalize-mutation-rotation`), matching the sibling
  `*-mutation-rotation` naming. If a future cross-cutter renames the L1 operator to
  `orthogonalize-column`, this theme slug should track it.
- **`m` argument off-by-one between consumers (reverse-direction note).** GMRES/FGMRES
  forward `j + 1` (orthogonalise against leading `j+1` columns); ROM forwards `j`. This is a
  caller convention, not a property of the lowered operator (the L1 `V` is already the
  appropriately-sliced basis). When a downstream L2 `krylov-step` lift consumes this theme,
  it should slice `V` at the L1 boundary and not re-thread the `j`/`j+1` choice through the
  lowering. (Reverse-direction lift note — kept out of the formal theme content per the
  high→low discipline.)
- **CGS2 `dH` scratch buffer is a workspace mention-and-erase (reverse-direction note).**
  The lift from L0→L1 must recognise `dH` as a transient (it is summed into `H` and
  discarded); a naive lift might surface it as a second output. The forward (L1→L0)
  direction in the theme content correctly treats it as an L0-internal scratch. Recorded
  here, not in the chapter.
- **B-weighted inner-product hook coverage.** The ROM path threads a `dot_op` other than
  `IdentityInnerProduct` (`romoperator.cpp:59-65`). The theme treats this as a substitution
  of the firm `dot` dependency (per the L1 entry's inner-product-hook variant axis); a
  `lowering-verifier` should confirm the B-weighted `dot_op` does not change the loop
  structure (it should not — it only swaps the kernel inside `dot_op(w, V[j])`).
- **Exhaustiveness of the L0 corpus scan.** The `get_call_sites` results show the free
  functions are reached only via the two dispatch wrappers + test harness, so the recognition
  set is closed. Recommended a `lowering-verifier` audit confirm this and check whether any
  `linalg::AXPY`/`Add` site elsewhere should be cross-referenced as an orthogonalisation
  fragment (none expected — the orthogonalisation is encapsulated in `orthog.hpp`).
