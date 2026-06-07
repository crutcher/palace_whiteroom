---
# Lowering theme. Per graded-stack scheme §5: rank(theme) = min(endpoint ranks). The L1
# endpoint (interpolator) is firm (rank 3); the L0 endpoint is rank-terminal ground truth.
# So the theme is firm and rank(theme) <= min(endpoints) holds for free.
rank: firm
edges:
  depends-on:
    - target: L1/interpolator
      kind: lowers-to             # the L1 source construction this theme lowers
    - target: palace/fem/fespace.cpp:173-238
      kind: cites-evidence        # BuildDiscreteInterpolator full body (dispatch + 4 kernels + abort)
    - target: palace/fem/fespace.hpp:107-114
      kind: cites-evidence        # GetDiscreteInterpolator accessor + lazy G.reset() rebuild cache
    - target: palace/fem/bilinearform.hpp:95-115
      kind: cites-evidence        # Palace-owned DiscreteLinearOperator builder + AddDomainInterpolator
  reference:
    - L1-L0/fe-space-construction-rotation         # sibling construction-lowers/bookkeeping-MFEM-owned split
    - L1-L0/fe-collection-construction-rotation    # upstream FE-space sub-spine producer
    - L1-L0/triangular-solve-obstruction           # opaque-library-ownership obstruction precedent (GSLIB sub-note)
---

# interpolator-construction-rotation

**Slug:** `interpolator-construction-rotation`

How the pure L1 [`interpolator`](../L1/interpolator.md) de-Rham discrete grid-transfer construction
lowers into the concrete Palace `FiniteElementSpace::BuildDiscreteInterpolator` body
(`palace/fem/fespace.cpp:173-238`) reached through the `GetDiscreteInterpolator` accessor
(`palace/fem/fespace.hpp:107`). This is a **vocabulary translation, not a rename**: the L1 form is a
*pure value* — `G = interpolator(aux, primal)`, a function of the two FE spaces naming the discrete
differential matrix `G` — while the L0 form is an *imperative, memoized, map-type-dispatched ctor*
that lazily rebuilds a cached `std::unique_ptr` `G` on auxiliary-space change and selects an MFEM
interpolator kernel by the spaces' de-Rham map-type pair. The translation has two sharp boundaries —
the **construction + kernel-selection lowers (Palace-owned) / the per-edge interpolator kernel is
MFEM-owned-read-as-given**, and the **memoization cache is an L1>L0 concern that the L1 purity
absorbs** — narrated in the splits below.

## Status

`firm` — structural. Every piece of the rewrite is positively anchored at L0 and verified on disk:
the accessor + lazy-rebuild cache (`fespace.hpp:107-114`), the full `BuildDiscreteInterpolator` body
(`fespace.cpp:173-238`) with its forward/swap direction pin (`:178-185`), the exhaustive four-way
map-type-pair dispatch (Grad `:190-198`, Curl-3D `:199-207`, Curl-2D-native `:208-221`, Div
`:222-230`) and the unsupported-pair abort (`:231-235`), and the Palace-owned
`DiscreteLinearOperator` builder (`bilinearform.hpp:95-115`). The per-edge interpolator *kernels*
(`GradientInterpolator` / `CurlInterpolator` / `DivergenceInterpolator`) are **MFEM-owned-read-as-given**
(same posture as `fe-space-construction-rotation` toward dof structure and `weak-form-term-rotation`
toward the libCEED quadrature kernel) — a witnessed library-ownership boundary, NOT a constructive
reconstruction, so it does not gate firmness. The **GSLIB point-interpolation sibling facility** is a
separate, library-owned operation disposed `obstruction (opaque-library-ownership)` (in-theme sub-note
below); it is orthogonal to this firm construction and does not reduce its maturity. MPI/`Par*` is read
single-rank per CLAUDE.md §Scope. Promoted on the **firm-on-positive-structure escape**: the rewrite is
a syntactic structural mapping on fully-specified positive source, so the absence of a dedicated
`test-fespace.cpp` interpolator test does not gate firm (the `fe-space-construction-rotation` /
`fe-collection-construction-rotation` / `essential-dofs-construction-rotation` precedent).

## L1 form (LHS)

The pure construction value (D3's prime entry [`L1/interpolator`](../L1/interpolator.md)):

    interpolator :: FiniteElementSpace[(D: ...)]      -- trial (auxiliary) space
                 -> FiniteElementSpace[(R: ...)]      -- test (primal) space
                 -> LinOp[(R: ...), (D: ...)]         -- the discrete differential matrix G
    interpolator(aux, primal) = G   where   G · u_aux = (deRham_edge primal aux) u_aux

At L1 this is referentially transparent: given the same `(aux, primal)` pair, `interpolator` names the
same discrete-differential `LinOp`; *which* differential operator (gradient / 3D-curl / 2D-scalar-curl
/ divergence) is a pure function of the two spaces' FE map types (plus dimension for the curl). There
is no cache, no rebuild, no mutation — those are L0 implementation idioms this theme lowers into.

## L0 form (RHS)

The concrete C++ construction is reached lazily through the `const`-member accessor and built once per
distinct auxiliary space. Two cooperating member functions:

    // palace/fem/fespace.hpp:107-114  (GetDiscreteInterpolator accessor)
    const auto &GetDiscreteInterpolator(const FiniteElementSpace &aux_fespace_) const
    {
      if (&aux_fespace_ != aux_fespace)   // auxiliary space changed since last build?
      {
        G.reset();                        // drop the cached operator
        aux_fespace = &aux_fespace_;      // remember the new auxiliary space
      }
      return G ? *G : BuildDiscreteInterpolator();   // cached hit, else build (+memoize)
    }

`G` and `aux_fespace` are `mutable` members of `FiniteElementSpace` (`fespace.hpp:38-39`), so the
accessor is `const` while still memoizing. `BuildDiscreteInterpolator` (`fespace.cpp:173-238`)
constructs the operator into `G` and returns `*G`.

### Translation axis 1 — the cache-drop + lazy-rebuild memoization rotation

The L1 `interpolator` is a pure function of `(aux, primal)`. The L0 form *implements that purity* with
a mutate-on-miss cache keyed on the auxiliary-space identity:

- **Cache hit** (`&aux_fespace_ == aux_fespace` and `G != nullptr`): the accessor returns the cached
  `*G` without rebuilding (`fespace.hpp:114`).
- **Cache miss / auxiliary-space change**: `G.reset()` drops the stale operator and `aux_fespace` is
  re-pointed (`fespace.hpp:111-112`), then `BuildDiscreteInterpolator()` rebuilds.

This is the construction-rotation analogue of the in-place-mutation rotations in the mutation-rotation
cohort: the L1 value is pure; the L0 cache (`G.reset()` + lazy rebuild) is a **transparent memoization
trick** (per CLAUDE.md §Optimization-tricks — algebraically equivalent to recomputing the pure value).
The L1 form drops the cache *and* the `mutable`-member mutate-on-miss idiom entirely; the purity law
`interpolator(aux, primal)` depends only on its arguments (L1 law 2) *is* what the cache realizes (the
cache is correct precisely because the value is a function of `aux` — the only key it tracks). The
cache keys only on the **auxiliary** space because `*this` (the primal space) is fixed for a given
`FiniteElementSpace` instance — re-pairing the *same* primal with a *different* auxiliary is the only
way to change the produced operator from one instance, hence the single-key cache.

### Translation axis 2 — map-type-pair dispatch → MFEM interpolator-kernel selection

`BuildDiscreteInterpolator` first pins the de-Rham **direction**, then dispatches on the
**(domain, range) map-type pair** to choose which MFEM discrete-derivative kernel assembles `G`.

**Direction pin (`fespace.cpp:178-187`).** `forward` holds when the primal (test) space's map type
equals the auxiliary (trial) space's *derivative* map type — i.e. the spaces are de-Rham-adjacent in
the `deriv(aux) → primal` direction; `swap` detects the reversed order. `MFEM_VERIFY(!swap, ...)`
(`:182-183`) rejects reversed order and `MFEM_VERIFY(forward, ...)` (`:184-185`) rejects non-adjacent
pairs. `trial_fespace`/`test_fespace` are then bound (`:186-187`) and their map types read
(`:188-189`). This is the constructive L0 statement of the L1 **direction-asymmetry non-law** (L1 law
4): `interpolator` is not symmetric in its arguments.

**Kernel selection (the four de-Rham edges).** The `(aux_map_type, primal_map_type)` pair selects the
MFEM interpolator kernel marshalled into the Palace-owned `DiscreteLinearOperator` builder
(`bilinearform.hpp:95-115`); the assembled matrix is wrapped in a `ParOperator` (read single-rank):

| L1 de-Rham edge | `(aux, primal)` map-type pair | MFEM kernel | L0 branch | dim |
|---|---|---|---|---|
| **Grad** (H1 → H(curl)) | `VALUE → H_CURL` | `GradientInterpolator` | `fespace.cpp:190-198` | any |
| **Curl-3D** (H(curl) → H(div)) | `H_CURL → H_DIV` | `CurlInterpolator` | `fespace.cpp:199-207` | 3D |
| **Curl-2D** (H(curl) → L2, scalar curl) | `H_CURL → INTEGRAL` | `CurlInterpolator` (native, see axis 3) | `fespace.cpp:208-221` | 2D |
| **Div** (H(div) → L2) | `H_DIV → INTEGRAL` | `DivergenceInterpolator` | `fespace.cpp:222-230` | any |
| (any other pair) | — | — | `MFEM_ABORT` `fespace.cpp:231-235` | — |

Three branches (Grad, Curl-3D, Div) build identically: construct `DiscreteLinearOperator interp(trial,
test)`, `interp.AddDomainInterpolator<T>()` with the kernel type `T`, then
`G = make_unique<ParOperator>(interp.PartialAssemble(), trial, test, true)`. The **only difference** is
the template kernel `T` — this is the L1 **de-Rham-edge variant axis** realized as a one-token
compile-time dispatch on the map-type pair. The exhaustive-over-four-pairs + abort-otherwise shape is
the L0 evidence for L1 law 3 (edge-selection by map-type pair) and the abort half of L1 law 4.

The `DiscreteLinearOperator` builder is **Palace-owned** (`bilinearform.hpp:95-115`): its ctor stores
the trial/test spaces (`:105-109`) and `AddDomainInterpolator<T>(args...)` (`:114-115`) pushes a
`make_unique<T>` into the owned `domain_interps` container (`:117`). Only the per-edge interpolator
*kernels* (`GradientInterpolator` / `CurlInterpolator` / `DivergenceInterpolator`) are MFEM-owned and
read-as-given — the **dispatch + builder + PartialAssemble + ParOperator-wrap structure** is fully
positive on Palace source.

### Translation axis 3 — transparent 2D-native-vs-libCEED-PA representation note

The 2D scalar-curl branch (`H_CURL → INTEGRAL`, `fespace.cpp:208-221`) is the one edge that does
**not** go through Palace's libCEED partial-assembly path. Instead of `interp.PartialAssemble()` it
const-casts the two spaces to raw `mfem::ParFiniteElementSpace*` (`:213-214`), builds an
`mfem::DiscreteLinearOperator` (`:215`), adds a raw `new mfem::CurlInterpolator` (`:216`), and uses
MFEM **native** `Assemble()` / `Finalize()` / `LoseMat()` (`:217-219`) to extract the assembled
`SparseMatrix`, wrapping it in the same `ParOperator`. The reason is stated in the source comment
(`:211-212`): *"Uses MFEM's native assembly because libCEED does not support partial assembly for this
operator type."*

**This is a transparent representation choice (per CLAUDE.md §Optimization-tricks), NOT a semantic
variant** — the produced `LinOp` is the *same* discrete-curl matrix `G`; only the assembly *path*
(MFEM-native vs. libCEED-PA) differs, forced by a libCEED capability gap. It gets this one-line note in
the L1>L0 lowering and is **not** a distinct L1 operator (the L1 `interpolator` entry already records
it as the assembly-representation variant axis, not a semantic one). No load-bearing numerical property
rides on the choice — both paths assemble the identical interpolatory matrix.

## GSLIB point-interpolation sibling — obstruction (opaque-library-ownership), in-theme sub-note

Palace's `palace/fem/interpolator.{hpp,cpp}` exposes a **distinct** interpolation facility — **GSLIB
point/field interpolation** — that is **NOT** the de-Rham discrete grid-transfer operator this theme
lowers, and is **library-owned**. It is recorded here as a sibling sub-note (boundary + negative
anchors), **not** as a lowering rule and **not** as a fill-in target (per CLAUDE.md §Scope: document
the boundary; do not target Palace stubs/opaque-library facilities for fill-in).

**Decls** (`palace/fem/interpolator.hpp:50-56`):

- `void InterpolateFunction(const mfem::GridFunction &U, mfem::GridFunction &V)` — mesh-to-mesh field
  interpolation (`interpolator.hpp:52`; body `interpolator.cpp:133-280`).
- `void InterpolateFunction(const mfem::Vector &xyz, const mfem::GridFunction &U, mfem::Vector &V, ...)`
  — point-list interpolation (`interpolator.hpp:56`; body `interpolator.cpp:282-310`).

**Disposition: `obstruction (opaque-library-ownership)`.** Every code path in this facility is the MFEM
`mfem::FindPointsGSLIB` find-points/interpolate engine (`interpolator.cpp:190`, `:293`), guarded by
`#if defined(MFEM_USE_GSLIB)` (`:135`, `:285`, `:83`, `:311`) with an `MFEM_ABORT("... requires
MFEM_USE_GSLIB!")` fallback when GSLIB is absent (`interpolator.cpp:108` `ProbeField`, `:278` /`:304`
`InterpolateFunction`, `:363` `ComputeLineIntegral`). There is no Palace-owned numerical body to lift —
the interpolation is black-box point-location + barycentric/Newton evaluation inside GSLIB; Palace only
marshals points and orderings around it. **Promotion route: NONE** (stays obstruction unless Palace
re-architects to a non-GSLIB point-interpolation). This facility is orthogonal to the firm de-Rham
discrete interpolator — they share the directory and the word "interpolate" but are different
operations; the firm `interpolator` does not depend on GSLIB.

(The GSLIB obstruction is recorded as a sub-note here, NOT as a separate first-class L1>L0 obstruction
theme, because it is a *facility-level* boundary adjacent to this operator, not a lowering of
`interpolator` itself. Whether the field-interp facility earns its own dedicated obstruction theme is
deferred to the trigger of a field-probe/point-sample output-product feature consumer landing — OQ
`gslib-field-interp-facility-dedicated-obstruction-theme`.)

## Applicability conditions

- The rewrite applies to the de-Rham discrete grid-transfer construction `interpolator(aux, primal)`
  reached through `GetDiscreteInterpolator` (`fespace.hpp:107`). The `(aux, primal)` pair must be
  de-Rham-adjacent in the `deriv(aux) → primal` direction (the `forward` pin, `fespace.cpp:178-185`);
  reversed order and non-adjacent pairs abort.
- `(aux_map_type, primal_map_type)` must be one of the four supported pairs (the variant axis); any
  other pair aborts (`fespace.cpp:231-235`).
- Single-rank reading: `mfem::ParFiniteElementSpace` / `ParOperator` are read as their serial
  equivalents (out of scope per CLAUDE.md §Scope).
- The GSLIB point-interpolation facility is **out of this theme's lowering scope** — it is the
  `obstruction (opaque-library-ownership)` sub-note above, not a rewrite case.

## Justification kind

**Structural** — the rewrite is shape-driven: the L1 pure value `interpolator(aux, primal)` maps onto
the concrete `GetDiscreteInterpolator` → `BuildDiscreteInterpolator` ctor sequence, with the de-Rham
map-type pair as the positively-anchored compile-time case axis and the lazy cache as a transparent
memoization of the L1 purity. No algebraic law or reduction chain is needed for the rewrite itself; the
two boundaries (the MFEM-owned per-edge kernel; the transparent 2D-native assembly path) are
established by direct read of the dispatch body, and the GSLIB obstruction by exhaustive
negative-anchor scan.

## Verified-against

- `palace/fem/fespace.cpp:173-238` — `BuildDiscreteInterpolator` full body (verified via read_range):
  forward/swap direction pin `:178-185` (`MFEM_VERIFY` `:182-185`), trial/test binding + map-type read
  `:186-189`, Grad branch `:190-198`, Curl-3D branch `:199-207`, Curl-2D native branch `:208-221`
  (libCEED-bypass comment `:211-212`, native `Assemble`/`Finalize`/`LoseMat` `:217-219`), Div branch
  `:222-230`, unsupported-pair abort `:231-235`.
- `palace/fem/fespace.hpp:107-114` — `GetDiscreteInterpolator` accessor + lazy `G.reset()` rebuild
  cache (`if` `:109`, `G.reset()` `:111`, `aux_fespace` re-point `:112`, cached-or-build return `:114`).
- `palace/fem/fespace.hpp:38-39` — `mutable const FiniteElementSpace *aux_fespace;` (`:38`) +
  `mutable std::unique_ptr<Operator> G;` (`:39`) — the cache members the `const` accessor mutates.
- `palace/fem/bilinearform.hpp:95-115` — Palace-owned `DiscreteLinearOperator` class (`:95`), ctor
  storing trial/test spaces (`:105-109`), `AddDomainInterpolator<T>` template (`:114-115`) pushing into
  the owned `domain_interps` container (`:117`).
- GSLIB obstruction anchors: `palace/fem/interpolator.hpp:50-56` (decls — `InterpolateFunction`
  GridFunction `:52`, point-list `:56`), `palace/fem/interpolator.cpp:133-280` + `:282-310`
  (`InterpolateFunction` bodies), `:190` / `:293` (`mfem::FindPointsGSLIB`), `:135` / `:285` / `:83` /
  `:311` (`#if defined(MFEM_USE_GSLIB)` guards), `:108` / `:278` / `:304` / `:363` (`MFEM_ABORT`
  GSLIB-absent fallbacks).
- [`L1/interpolator`](../L1/interpolator.md) — the firm L1 entry (c117) this theme lowers (the coupled
  `reference` → `depends-on (kind: lowers-to)` edge upgrade lands with this theme).

## Open questions / caveats

- **Lifting note (reverse direction, working-note only).** The L0 ctor lifts to L1 `interpolator`
  cleanly precisely because the per-edge interpolator kernels are read-as-given — the lift discards the
  MFEM kernel internals and the cache, retaining only the `(aux, primal) → LinOp` shape selected by the
  map-type pair. (High→low formal content stays in the chapter above; this is a working note.)
- **De-Rham exactness law anchor.** The exactness identities `Curl · Grad = 0` / `Div · Curl = 0` are
  recorded in the L1 entry as a *defining-family property*, not a Palace-read law (Palace assembles
  each edge separately, never composing them in one call) — promoting them to a verified law would need
  a literature/MFEM-de-Rham anchor (carried OQ `interpolator-derham-exactness-law-anchor`, c117 D5).
  This theme lowers the per-edge *construction*, not the complex-level composition, so the OQ is
  unaffected by this theme.
- **GSLIB facility dedicated obstruction theme** (carried OQ
  `gslib-field-interp-facility-dedicated-obstruction-theme`, c117 D5) — the field-interp facility is an
  in-theme sub-note here; whether it earns a first-class obstruction theme triggers on a
  field-probe/point-sample output-product feature consumer landing.
