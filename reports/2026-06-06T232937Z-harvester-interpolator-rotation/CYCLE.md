---
agent: harvester
invoked_at: 2026-06-06T232937Z
scope: L1>L0 theme: interpolator-construction-rotation
status: integrated
integrated_at: 2026-06-07T003000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean as c118 D3 (batch-38 opener). New firm L1>L0 theme interpolator-construction-rotation.md (GSLIB opaque-library-ownership obstruction sub-note, route NONE) + interpolator reference→depends-on(lowers-to) edge upgrade (OUTBOUND; RE10 op stays batch-37-ratified baseline-excepted). cargo make book EXIT 0; rank_violations=0; STRONGER includes this theme (RE10-attributed). Non-blocking: interpolator.cpp:282-310 ~3-line over-range left in artifact (passing bounds, non-load-bearing). 0 gate hits."
inputs:
  - cycle-118 dispatch D3 (batch-38 mesh->fe_space substrate lowering campaign)
  - migrated OQ interpolator-construction-rotation-l1-l0-theme-needed (c117 D5)
  - book/src/L1/interpolator.md (firm c117; the L1 endpoint this theme lowers)
  - book/src/L1-L0/essential-dofs-construction-rotation.md (typed-frontmatter sibling shape)
  - book/src/L1-L0/fe-space-construction-rotation.md (construction-lowers/MFEM-owned-split precedent)
  - verified L0: palace/fem/fespace.cpp:173-238, fespace.hpp:107/:109-114, bilinearform.hpp:95-115,
    interpolator.hpp:50-56, interpolator.cpp GSLIB aborts :108/:278/:304/:363
---

# CYCLE: Formalize interpolator-construction-rotation at L1>L0

## Summary

Authors the L1>L0 construction-rotation theme `interpolator-construction-rotation`, grounding the
home of the firm L1 [`interpolator`](../L1/interpolator.md) de-Rham discrete grid-transfer operator
(c117). The theme narrates the genuine vocabulary translation from the pure L1 value
`G = interpolator(aux, primal)` (a referentially-transparent function of two FE spaces) into the
imperative L0 `BuildDiscreteInterpolator` body (`palace/fem/fespace.cpp:173-238`) reached through
the `GetDiscreteInterpolator` accessor (`palace/fem/fespace.hpp:107`). Three translation axes are
covered: (1) the **cache-drop + lazy-rebuild memoization rotation** (`G.reset()` on auxiliary-space
change, `fespace.hpp:109-114`) — the L1 purity is *implemented* by the L0 mutate-on-miss cache;
(2) the **map-type-pair dispatch → MFEM interpolator-kernel selection** (the four de-Rham edges); and
(3) a one-line **transparent 2D-native-vs-libCEED-PA representation note** (the 2D scalar-curl branch
bypasses libCEED partial assembly). The GSLIB point-interpolation sibling is carried as an in-theme
`obstruction (opaque-library-ownership)` sub-note (boundary + negative anchors; promotion route NONE),
NOT a lowering rule and NOT a fill-in target. Status `firm` (all anchors exhaustively cited and
verified on disk). Bundled coupled re-anchor: upgrade `L1/interpolator`'s `reference` →
`depends-on (kind: lowers-to)` edge to this now-authored firm theme.

## Proposed changes

```new:book/src/L1-L0/interpolator-construction-rotation.md
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
```

```edit:book/src/L1/interpolator.md
---
layer: L1
operator: interpolator
firmness: firm
# Graded-stack scheme: this L1 entry is the de-Rham discrete grid-transfer operator. It is a
# leaf at L1 (its produced LinOp is consumed via apply_linop, but the interpolator's own
# construction folds no other L1 operator). The GSLIB point-interpolation sibling is an
# opaque-library-ownership obstruction, recorded in-chapter (a reference note, not a dep).
rank: firm
edges:
  # The L1>L0 `interpolator-construction-rotation` lowering theme is now authored + `status: firm`
  # (c118 D3), so its `lowers-to` edge is promoted from a navigational `reference` to a blocking
  # `depends-on (kind: lowers-to)` — rank 3 <= 3 holds (the theme is firm), matching the
  # `fe_space` -> `fe-space-construction-rotation` precedent. The firm rank still rests on positive
  # L0 source (the cites-evidence ground truth below + the now-firm lowering theme), not on any
  # sub-firm node.
  depends-on:
    - target: L1-L0/interpolator-construction-rotation
      kind: lowers-to             # the L1>L0 construction-rotation theme (firm, c118 D3)
  reference:
    - L1/apply_linop              # the produced LinOp is applied via apply_linop (consumed-by, not a build dep)
    - L1/fe_space                 # the trial/test FiniteElementSpace operands (operates-on)
    - L1/divfree-projector        # consumer: the Grad discrete-gradient interpolator
    - concepts/constructed-operators
---

# interpolator

De-Rham discrete grid-transfer operator: a pure-functional constructor
`G = interpolator(trial_space, primal_space)` that produces the **discrete
differential matrix** interpolating a field from an auxiliary (trial) finite
element space into a primal de-Rham-adjacent space — the discrete **gradient**,
**curl**, or **divergence** depending on the de-Rham map-type pair of the two
spaces. The constructed value is an opaque `LinOp` applied downstream via
[`apply_linop`](./apply_linop.md). The grid-transfer producer consumed by the
divergence-free projector (the `Grad` operator), the boundary-mode `Bz` readout
(the discrete `curl`), the AMS preconditioner setup, the curl-curl operator, and
field post-processing.

## Context

`interpolator` lifts `FiniteElementSpace::GetDiscreteInterpolator` /
`FiniteElementSpace::BuildDiscreteInterpolator`
(`palace/fem/fespace.cpp:173-238`; accessor `palace/fem/fespace.hpp:107`,
lazy-rebuild cache `:109-114`) — a `const` member that constructs (and caches)
the discrete differential operator `G` interpolating from the *auxiliary* space
`aux_fespace` into `*this` (the *primal* space). At L0 the member mutates a cached
`std::unique_ptr` `G` and a cached `aux_fespace` pointer, rebuilding lazily when
the auxiliary space changes (`palace/fem/fespace.hpp:109-114`); the L1 form drops
the cache and the mutate-on-miss idiom — the construction is a pure function of
the two spaces, and the caching is an L1>L0 lowering concern (now lowered by
[`interpolator-construction-rotation`](../L1-L0/interpolator-construction-rotation.md)).

The construction body dispatches on the **de-Rham map-type pair** of the trial
(auxiliary) and test (primal) spaces — the FE map type fixes which de-Rham edge
the spaces straddle, and that fixes which MFEM interpolator kernel assembles the
matrix:

- **VALUE → H_CURL**: discrete **gradient** `Grad` (H1 → H(curl)); MFEM
  `GradientInterpolator` (`palace/fem/fespace.cpp:190-198`).
- **H_CURL → H_DIV**: discrete **curl** `Curl` (3D: H(curl) → H(div)); MFEM
  `CurlInterpolator` (`palace/fem/fespace.cpp:199-207`).
- **H_CURL → INTEGRAL**: discrete **scalar curl** (2D: H(curl) → L2); MFEM
  `CurlInterpolator` via native (non-libCEED) assembly because libCEED has no
  partial-assembly path for this operator type (`palace/fem/fespace.cpp:208-221`).
- **H_DIV → INTEGRAL**: discrete **divergence** `Div` (H(div) → L2); MFEM
  `DivergenceInterpolator` (`palace/fem/fespace.cpp:222-230`).

Any other map-type pair is an unsupported configuration and aborts
(`palace/fem/fespace.cpp:231-235`). Each branch wraps the assembled matrix in a
[`ParOperator`](./apply_linop.md) (read single-rank per CLAUDE.md §Scope). The
`DiscreteLinearOperator` builder is **Palace-owned**
(`palace/fem/bilinearform.hpp:95-115`); only the per-edge interpolator *kernels*
(`GradientInterpolator` / `CurlInterpolator` / `DivergenceInterpolator`) are
MFEM-owned, and they are read-as-given the same way `fe_space`'s dof internals
and `apply_linop`'s representation are read-as-given — the **dispatch +
assembly structure** is fully positive on Palace source.

The order/direction pin is the `forward`/`swap` check at the head of the body
(`palace/fem/fespace.cpp:178-185`): the operator is well-defined only when the
trial space's map type matches the *derivative* map type of the test space (the
de-Rham relation `deriv(aux) → primal`); the reversed order aborts. This is the
constructive statement of "the two spaces are de-Rham-adjacent in the right
direction".

A cross-cutting note: `interpolator` is the construction-time sibling of
[`apply_linop`](./apply_linop.md), not a variant of it — `apply_linop` *applies*
an opaque `LinOp`; `interpolator` *constructs* the specific de-Rham `LinOp` that
is then applied. The `Grad` step inside [`divfree-projector`](./divfree-projector.md)
is exactly this constructed `LinOp` (`palace/linalg/divfree.cpp:117`).

## Signature

This is a higher-level operator (its result is itself a `LinOp`); shapes use the
named-shape-group / `LinOp[(R: ...), (D: ...)]` convention for a domain≠range
operator — see [`semantics §1.2.1–§1.2.3`](../semantics/index.md) for the rule.

```text
interpolator :: FiniteElementSpace[(D: ...)]      -- trial (auxiliary) space
             -> FiniteElementSpace[(R: ...)]      -- test (primal) space
             -> LinOp[(R: ...), (D: ...)]         -- the discrete differential matrix G
interpolator(aux, primal) = G   where   G · u_aux = (deRham_edge primal aux) u_aux
```

Shape contract (named axes):

- `aux` — `FiniteElementSpace[(D: ...)]` — the trial / auxiliary space; its true-dof
  run is the **domain** group `D` of the produced operator. Read-only.
- `primal` — `FiniteElementSpace[(R: ...)]` — the test / primal space; its true-dof
  run is the **range** group `R` of the produced operator. Read-only.
- result — `LinOp[(R: ...), (D: ...)]` — the discrete differential matrix `G`,
  applied via [`apply_linop`](./apply_linop.md) as `G · u_aux : Tensor[$D] -> Tensor[$R]`.

At **L1/L0** the Palace FE-space dof-vectors are genuinely flat (rank-1), so the
concrete realization is `LinOp[N_primal, N_aux]` with `N_aux = aux.GetTrueVSize()`,
`N_primal = primal.GetTrueVSize()` and `apply_linop` operands `Tensor[N_aux]` →
`Tensor[N_primal]`; the `LinOp[(R: ...), (D: ...)]` group form is the rank-agnostic
spelling carried for the calculus rendering (per semantics §1.2.3). The four de-Rham
edges are not separate L1 operators — they are the single `interpolator` selecting a
kernel from the map-type pair of its two arguments (the **de-Rham-edge variant axis**;
see Variant axes).

The result is genuinely **rectangular** (`R ≠ D` in general): `Grad` maps the
H1 dof-space to the larger Nedelec dof-space, `Div` maps H(div) down to the L2
dof-space, etc. — this is one of the genuine `M ≠ N` cases named in
[`apply_linop`](./apply_linop.md)'s signature note.

## Semantics

`interpolator(aux, primal)` returns the discrete differential operator realizing
the de-Rham edge between `aux` and `primal`, determined entirely by the two
spaces' FE map types (and dimension, for the 2D-vs-3D curl). The result is a
function of the two spaces only — the L1 form is pure; the L0 lazy-rebuild cache
(`G.reset()` on auxiliary-space change, `palace/fem/fespace.hpp:109-114`) is an
L1>L0 memoization concern, not part of the L1 semantics (lowered by
[`interpolator-construction-rotation`](../L1-L0/interpolator-construction-rotation.md)).

The operator is the **discrete** (interpolatory) realization of the continuous
de-Rham differential operator: `Grad` is the matrix taking nodal (H1) dof values
to edge (Nedelec) dof values such that the resulting field is the discrete
gradient; `Curl` the H(curl)→H(div) edge; `Div` the H(div)→L2 edge. These compose
into the de-Rham complex `H1 --Grad--> H(curl) --Curl--> H(div) --Div--> L2`; the
defining exactness property `Curl · Grad = 0` and `Div · Curl = 0` holds at the
discrete level for the interpolatory operators (it is what makes them *the* de-Rham
maps), but Palace assembles each edge independently — the complex-level composition
is not materialized as a single Palace call, so the exactness identities are stated
here as the **defining property of the de-Rham family** rather than as a Palace-read
algebraic law (see Algebraic laws, which separates the two).

The 2D scalar-curl branch (`palace/fem/fespace.cpp:208-221`) is the one case that
bypasses libCEED partial assembly and uses MFEM native `Assemble`/`Finalize`/
`LoseMat` — a representation choice (libCEED has no PA path for that operator type),
not a semantic difference; the produced `LinOp` is the same discrete-curl matrix.
This is a transparent representation note, recorded in the L1>L0 lowering, not a
distinct L1 operator.

## Algebraic laws

Stated only where they hold; the de-Rham complex identities are flagged as
**defining-family properties** vs. Palace-read laws.

1. **Linearity (of the produced operator).** The result `G` is a `LinOp`, hence
   `G · (α·u + β·v) = α·(G·u) + β·(G·v)` — this is the `apply_linop` linearity law
   inherited by the constructed value. (Holds: `G` is an assembled sparse / matrix-
   free linear operator.)
2. **Construction determinism / space-functionality.** `interpolator(aux, primal)`
   depends only on `aux` and `primal` (same spaces ⇒ same operator). (Holds at L1;
   the L0 cache is an implementation of this purity, `palace/fem/fespace.hpp:109-114`.)
3. **De-Rham-edge selection by map-type pair.** The de-Rham edge — and thus which
   differential operator `G` realizes — is determined entirely by the
   `(aux_map_type, primal_map_type)` pair (plus dimension for curl), per the
   `BuildDiscreteInterpolator` dispatch (`palace/fem/fespace.cpp:188-230`). (Holds:
   exhaustive over the four supported pairs; all others abort.)
4. **Direction asymmetry (NON-law / well-definedness pin).** `interpolator` is NOT
   symmetric in its arguments: it is defined only for the `deriv(aux) → primal`
   direction; the reversed order is rejected at construction
   (`palace/fem/fespace.cpp:178-185`, `MFEM_VERIFY(forward, ...)`). There is no
   "reverse interpolator" obtained by swapping arguments — the adjoint/transfer in the
   other direction is a distinct construction (prolongation/restriction, a different
   operator; see [`fe_space`](./fe_space.md)'s prolongation note and
   `apply_linop`'s transpose discussion).
5. **De-Rham exactness (DEFINING-FAMILY property, NOT a Palace-read law).**
   `Curl · Grad = 0` and `Div · Curl = 0` hold for the discrete de-Rham
   interpolators — this is the property that *characterizes* the family and the reason
   these specific kernels are chosen. It is **not** read off a single Palace site
   (Palace assembles each edge separately and never composes them in one call), so it
   is recorded as the defining family property, not promoted to a verified-on-Palace
   algebraic law. (A literature/MFEM-de-Rham anchor would be required to promote it to
   a law; flagged in Open questions.)

Non-laws explicitly: **not commutative/symmetric in arguments** (law 4); **not
defined for non-de-Rham-adjacent space pairs** (aborts, law 3); **not a quadrature/
reduction** (it is an assembled differential matrix, no summation-order load-bearing
concern at the L1 surface — the assembly summation order is an `apply_linop`/`fe_assemble`
representation concern, not an `interpolator`-construction one).

## GSLIB point-interpolation sibling — obstruction (opaque-library-ownership)

Palace's `palace/fem/interpolator.{hpp,cpp}` also exposes a **distinct**
interpolation facility — **GSLIB point/field interpolation** — which is **NOT**
the de-Rham discrete grid-transfer operator above and is **library-owned**:

- `fem::InterpolateFunction(const mfem::GridFunction &U, mfem::GridFunction &V)`
  — mesh-to-mesh field interpolation (`palace/fem/interpolator.hpp:52`, body
  `palace/fem/interpolator.cpp:133-280`).
- `fem::InterpolateFunction(const mfem::Vector &xyz, ...)` — point-list
  interpolation (`palace/fem/interpolator.hpp:56`, body
  `palace/fem/interpolator.cpp:282-310`).
- the `InterpolationOperator` probe-field class
  (`palace/fem/interpolator.hpp:24-44`).

**Disposition: `obstruction (opaque-library-ownership)`.** Every code path in
this facility is the MFEM `mfem::FindPointsGSLIB` find-points/interpolate engine
(`palace/fem/interpolator.cpp:190`, `:293`), guarded by
`#if defined(MFEM_USE_GSLIB)` with an `MFEM_ABORT("... requires MFEM_USE_GSLIB!")`
fallback when GSLIB is absent (`palace/fem/interpolator.cpp:278`, `:304`, `:108`,
`:363`). There is no Palace-owned numerical body to lift — the interpolation is a
black-box point-location + barycentric/Newton evaluation inside GSLIB; Palace only
marshals points and orderings around it.

**Negative-finding exhaustiveness** (per skill `establish-negative-finding-exhaustiveness`):
a full scan of `palace/fem/interpolator.cpp` for `MFEM_USE_GSLIB` / `FindPointsGSLIB`
/ `MFEM_ABORT` confirms **every** interpolation entry point (`InterpolateFunction`
×2, `InterpolationOperator::ProbeField`, `ComputeLineIntegral`) routes through the
GSLIB guard with an abort fallback and **no** alternative Palace-internal body
(`palace/fem/interpolator.cpp:83,108,135,190,278,285,293,304,311,363`).
The GSLIB facility is therefore opaque-library-owned, promotion route NONE (stays
obstruction unless Palace re-architects to a non-GSLIB point-interpolation), and is
**orthogonal to** the firm de-Rham discrete interpolator — they share a directory
(`palace/fem/interpolator.*` vs `palace/fem/fespace.*`) and the word "interpolate"
but are different operations. The firm `interpolator` operator above does not depend
on GSLIB. The boundary + negative anchors are carried in the L1>L0
[`interpolator-construction-rotation`](../L1-L0/interpolator-construction-rotation.md)
theme's GSLIB sub-note as well.

(The GSLIB obstruction is recorded here in-chapter as a sibling note rather than as a
separate L1>L0 obstruction theme because it is a *facility-level* boundary adjacent to
this operator, not a lowering of `interpolator` itself; if the field-interp facility
gains its own feature-surface consumer that needs a dedicated theme, that theme is a
later dispatch — flagged in Open questions.)

## Variant axes

- **De-Rham edge** (THE load-bearing variant axis): `{ Grad (H1→ND), Curl-3D (ND→RT),
  Curl-2D (ND→L2), Div (RT→L2) }`, selected by the `(aux_map_type, primal_map_type)`
  pair + dimension. All four are witnessed at construction sites: `GetGradMatrix`
  (`palace/models/spaceoperator.hpp:224-227`), `GetCurlMatrix` 2D/3D split
  (`palace/models/spaceoperator.hpp:228-236`), the curl-curl operator's discrete
  curl `GetCurlMatrix` (`palace/models/curlcurloperator.hpp:112`), the divfree projector's `Grad`
  (`palace/linalg/divfree.cpp:117`), the boundary-mode `Bz = curl(Et)` discrete-curl
  (`palace/drivers/boundarymodesolver.cpp:322`), and the post-processing curl
  (`palace/models/postoperator.cpp:1673`).
- **Assembly representation** (2D scalar-curl native vs. libCEED PA) — a transparent
  representation choice, NOT a semantic variant; the produced `LinOp` is the same
  discrete-curl matrix. Recorded in the L1>L0 lowering, not as an L1 variant.
- **Element type / `Par*` parallel wrapper** — read single-rank per CLAUDE.md §Scope;
  absorbed (the produced operator is a `ParOperator` read as its single-rank operator).

## Dependencies

L1-internal: **(leaf at construction).** `interpolator` folds no other L1 operator
to *build* `G` — the assembly is the MFEM-owned interpolator kernel marshalled by the
Palace-owned `DiscreteLinearOperator` builder. The produced value is *consumed* via
[`apply_linop`](./apply_linop.md) (a consumed-by/reference relation, not a build
dependency), operates-on two [`fe_space`](./fe_space.md) values, and is consumed by
[`divfree-projector`](./divfree-projector.md) (the `Grad` step). The discrete-curl
edge is the operator behind the boundary-mode `Bz` readout.

The construction lowers to L0 via the firm
[`interpolator-construction-rotation`](../L1-L0/interpolator-construction-rotation.md)
theme (the `depends-on (kind: lowers-to)` edge). The GSLIB point-interpolation facility
is an `obstruction (opaque-library-ownership)` sibling (see above), NOT a dependency.

## Status

**`firm`.** The de-Rham discrete grid-transfer interpolator is firm on positive
structure: the entire `BuildDiscreteInterpolator` body is read
(`palace/fem/fespace.cpp:173-238`), the map-type dispatch is exhaustive over the four
supported de-Rham edges (all others abort), the Palace-owned `DiscreteLinearOperator`
builder is read (`palace/fem/bilinearform.hpp:95-115`), and the produced operator's
linearity/determinism/edge-selection/direction-asymmetry laws are syntactic
read-offs over that body plus the inherited `apply_linop` linearity. Promoted on the
**firm-on-positive-structure escape**: the laws are syntactic identities on fully
specified positive source, so the absence of a dedicated `test-fespace.cpp`
interpolator test does not gate firm (the `fe_space` / `fe_assemble` / `apply_linop`
no-dedicated-test precedent). The MFEM interpolator *kernels*
(`GradientInterpolator` etc.) are read-as-given the same way `fe_space`'s dof
internals are — NOT `partly-constructive`, since no sub-part is materialized from
negative anchors.

The **GSLIB point-interpolation sibling facility** is a separate, library-owned
operation disposed as `obstruction (opaque-library-ownership)` (see the dedicated
section above) — it is orthogonal to this firm operator and does not reduce its
maturity.

Well-foundedness: the firm rank rests on **positive L0 source** (the read
`BuildDiscreteInterpolator` body + the Palace-owned `DiscreteLinearOperator` builder —
rank-terminal ground truth). The L1>L0
`interpolator-construction-rotation` lowering theme is now **authored + `status: firm`**
(c118 D3), so its `lowers-to` edge is promoted from a navigational `reference` to a
blocking `depends-on (kind: lowers-to)` — rank 3 ≤ 3 holds (the theme is firm),
matching the `fe_space` → `fe-space-construction-rotation` precedent (which carries the
`lowers-to` `depends-on` edge BECAUSE its theme exists and is firm). The remaining
`reference` edges (`apply_linop`, `fe_space`, `divfree-projector` — all firm) carry no
rank constraint. So no `depends-on` edge rests on a sub-firm or non-existent node, and
the firm rank is well-founded.

## Evidence

- `palace/fem/fespace.cpp:173-238` — `BuildDiscreteInterpolator` full body: the
  `forward`/`swap` de-Rham direction check (`:178-185`), the four map-type-pair
  branches (Grad `:190-198`, Curl-3D `:199-207`, Curl-2D native `:208-221`, Div
  `:222-230`), and the unsupported-pair abort (`:231-235`).
- `palace/fem/fespace.hpp:107-114` — `GetDiscreteInterpolator` on-the-fly accessor +
  lazy `G.reset()` rebuild cache (`:109-114`; the L0 mutate-on-miss idiom dropped at
  L1); `mutable` cache members `aux_fespace` `:38` + `G` `:39`.
- `palace/fem/bilinearform.hpp:95-115` — Palace-owned `DiscreteLinearOperator` class
  (`:95`) + `AddDomainInterpolator` template (`:114-115`).
- `palace/fem/fespace.cpp:190-198` / `:199-207` / `:222-230` — the
  `GradientInterpolator` / `CurlInterpolator` / `DivergenceInterpolator` MFEM kernel
  selections.
- Consumer sites (de-Rham-edge variant-axis witnesses):
  `palace/models/spaceoperator.hpp:224-227` (`GetGradMatrix`), `:228-236`
  (`GetCurlMatrix`, 2D/3D split), `palace/models/curlcurloperator.hpp:112`,
  `palace/linalg/divfree.cpp:117` (divfree `Grad`),
  `palace/drivers/boundarymodesolver.cpp:322` (boundary-mode discrete-curl `Bz`),
  `palace/models/postoperator.cpp:1673` (post-processing curl).
- GSLIB obstruction anchors: `palace/fem/interpolator.hpp:50-56` (decls),
  `palace/fem/interpolator.cpp:133-280` + `:282-310` (`InterpolateFunction` bodies),
  `:190` / `:293` (`FindPointsGSLIB`), `:278` / `:304` / `:108` / `:363`
  (`MFEM_ABORT` GSLIB-absent fallbacks).
- L1>L0 lowering: [`interpolator-construction-rotation`](../L1-L0/interpolator-construction-rotation.md)
  (firm, c118 D3) — the construction-rotation theme this operator lowers through.
```

```edit:book/src/L1-L0/index.md
| [fe-space-construction-rotation](./fe-space-construction-rotation.md) | [`L1/fe_space`](../L1/fe_space.md) (firm c064) | `palace/fem/fespace.hpp:67-75` (variadic ctor) + `:93-103` (MFEM-forwarding dof accessors), `palace/fem/multigrid.hpp:90` (single-space coarse-seed), `palace/models/spaceoperator.cpp:47/49/51/75` (de-Rham instantiation sites) | firm *(structural; vocabulary-translation — pure `(mesh, collection) → FiniteElementSpace[N]` value → imperative `mfem::ParFiniteElementSpace`-wrapping ctor; **construction-lowers / dof-bookkeeping-MFEM-owned split** — the `(mesh, collection)` pairing + de-Rham case selection + `ResetCeedObjects` cache-init lower HERE at the ctor `fespace.hpp:67-75`, the dof/vdof numbering + ordering + conformity + prolongation/restriction matrices are MFEM-owned-read-as-given via thin forwarding accessors `fespace.hpp:93-103` (analogue of the libCEED-leaf boundary but MFEM-dof-management-owned, not libCEED-quadrature); 4 de-Rham rewrite cases H1/`H1_FECollection` `:49` + H(curl)/`ND_FECollection` `:47` + H(div)/`RT_FECollection` `:51` + L2/`L2_FECollection` `:75` (2-D-curl INTEGRAL-map load-bearing variant); single-space coarse-seed `multigrid.hpp:90`; hierarchy/`fe_collection` deferred siblings; MPI/`Par*` + mesh-partitioning out-of-scope single-rank; firm-on-positive-structure)* |
| [interpolator-construction-rotation](./interpolator-construction-rotation.md) | [`L1/interpolator`](../L1/interpolator.md) (firm c117) | `palace/fem/fespace.cpp:173-238` (`BuildDiscreteInterpolator` body), `palace/fem/fespace.hpp:107-114` (accessor + lazy `G.reset()` cache), `palace/fem/bilinearform.hpp:95-115` (Palace-owned `DiscreteLinearOperator` builder); GSLIB sub-note `palace/fem/interpolator.{hpp,cpp}` | firm *(structural; vocabulary-translation — pure `interpolator(aux, primal) → LinOp` value → imperative memoized map-type-dispatched ctor; **3 translation axes**: (1) cache-drop + lazy-rebuild memoization rotation (`G.reset()` on auxiliary-space change `fespace.hpp:109-114`; the L1 purity (law 2) IS what the single-key cache realizes — transparent memoization trick), (2) map-type-pair dispatch → MFEM interpolator-kernel selection (4 de-Rham edges Grad `VALUE→H_CURL` `:190-198` / Curl-3D `H_CURL→H_DIV` `:199-207` / Curl-2D `H_CURL→INTEGRAL` `:208-221` / Div `H_DIV→INTEGRAL` `:222-230`, + forward/swap direction pin `:178-185` = L0 evidence for L1 laws 3/4, + unsupported-pair abort `:231-235`; one-token compile-time kernel-type dispatch, only `T` differs across 3 of 4 branches), (3) transparent 2D-native-vs-libCEED-PA representation note (the 2D scalar-curl branch `:208-221` bypasses libCEED PA for MFEM-native `Assemble`/`Finalize`/`LoseMat` `:217-219` — same matrix, forced by libCEED capability gap, §Optimization-tricks one-line note); per-edge interpolator KERNELS (`GradientInterpolator`/`CurlInterpolator`/`DivergenceInterpolator`) MFEM-owned-read-as-given (cf. `fe-space-construction-rotation` dof-bookkeeping split + `weak-form-term-rotation` kernel-opaque split), dispatch+builder Palace-owned; **GSLIB point-interpolation sibling = `obstruction (opaque-library-ownership)` in-theme sub-note** (NOT a lowering rule, NOT a fill-in target — every entry point routes through `mfem::FindPointsGSLIB` `interpolator.cpp:190`/`:293` with `MFEM_ABORT` GSLIB-absent fallbacks `:108`/`:278`/`:304`/`:363`, promotion route NONE; orthogonal to the firm de-Rham interpolator); MPI/`Par*` out-of-scope single-rank; firm-on-positive-structure, no-dedicated-`test-fespace.cpp` caveat non-gating per `fe_space`/`fe_collection`/`fe_assemble`; coupled re-anchor upgraded `L1/interpolator`'s `reference`→`depends-on (kind: lowers-to)` edge)* |
| [weak-form-term-rotation](./weak-form-term-rotation.md) | [`L1/weak_form_term`](../L1/weak_form_term.md) (firm c061) | `palace/fem/bilinearform.hpp:53-57` (`AddDomainIntegrator<T>(Q)` instantiation), `palace/fem/integrator.hpp:39-130` (wrapper layer), `palace/models/laplaceoperator.cpp:188-194` (Gradient/diffusion witness), `palace/models/curlcurloperator.cpp:170-181` (Curl/curl-curl witness) | firm *(structural; vocabulary-translation — pure `(coefficient, differential-operator)` pair → C++ template-type `T` (diff-op, compile-time) + runtime-arg `Q` (coefficient) dispatch into mutable owned `domain_integs` container; **identity-lowers / kernel-opaque split** — term IDENTITY (which `Q`, which `𝒟`) Palace-readable at the `AddDomainIntegrator<T>(Q)` site and lowers HERE, term KERNEL (`Assemble` quadrature) is the libCEED `opaque-library-ownership` boundary `fe-assemble-libceed-boundary-obstruction` c055, lowers ELSEWHERE; 2 grounded rewrite cases Gradient/`DiffusionIntegrator(epsilon_func)` `laplaceoperator.cpp:191-194` + Curl/`CurlCurlIntegrator(muinv_func)` `curlcurloperator.cpp:179-181` (same `BilinearForm`-fold, integrator-slot-only difference); mass/`Identity` + div-div/`Divergence` named pending-pull axis points NOT authored; container build-up is the sibling `fe-operator-assemble-mutation-rotation` c057; firm-on-positive-structure)* |
```

```edit:book/src/SUMMARY.md
  - [fe-space-construction-rotation](./L1-L0/fe-space-construction-rotation.md)
  - [interpolator-construction-rotation](./L1-L0/interpolator-construction-rotation.md)
  - [weak-form-term-rotation](./L1-L0/weak-form-term-rotation.md)
```

## Operator content

The theme content is fully authored inside the `new:book/src/L1-L0/interpolator-construction-rotation.md`
block above. Summary of the firm theme:

- **Slug + one-line:** `interpolator-construction-rotation` — how the pure L1 `interpolator(aux, primal)`
  de-Rham discrete grid-transfer construction lowers into the L0 memoized, map-type-dispatched
  `BuildDiscreteInterpolator` ctor.
- **L1 form (LHS):** `interpolator :: FiniteElementSpace[(D)] -> FiniteElementSpace[(R)] -> LinOp[(R),(D)]`,
  a pure function of the two spaces.
- **L0 form (RHS):** `GetDiscreteInterpolator` accessor (`fespace.hpp:107-114`) → `BuildDiscreteInterpolator`
  body (`fespace.cpp:173-238`).
- **Translation axes (3):** (1) cache-drop + lazy-rebuild memoization rotation; (2) map-type-pair dispatch
  → MFEM kernel selection over four de-Rham edges + direction pin + abort; (3) transparent
  2D-native-vs-libCEED-PA representation note.
- **GSLIB sub-note:** `obstruction (opaque-library-ownership)`, promotion route NONE, in-theme sub-note
  (boundary + negative anchors), NOT a lowering rule / fill-in target.
- **Status:** `firm` (structural; firm-on-positive-structure escape).
- **Justification kind:** structural.

## Supporting evidence

All L0 citations verified on disk this dispatch (read_range / Read):

- `palace/fem/fespace.cpp:173-238` — full `BuildDiscreteInterpolator` body, line-by-line confirmed:
  direction pin `:178-189`, Grad `:190-198`, Curl-3D `:199-207`, Curl-2D native (libCEED-bypass comment
  `:211-212`, `Assemble`/`Finalize`/`LoseMat` `:217-219`) `:208-221`, Div `:222-230`, abort `:231-235`.
- `palace/fem/fespace.hpp:107-114` — accessor + lazy cache verified (`if` `:109`, `G.reset()` `:111`,
  re-point `:112`, return `:114`); `mutable` members `aux_fespace` `:38`, `G` `:39` confirmed.
- `palace/fem/bilinearform.hpp:95-115` — `DiscreteLinearOperator` class `:95`, ctor `:105-109`,
  `AddDomainInterpolator` template `:114-115` confirmed (`:113` is blank).
- `palace/fem/interpolator.hpp:50-56` — GSLIB decls (`InterpolateFunction` `:52` + `:56`) confirmed.
- `palace/fem/interpolator.cpp` GSLIB anchors confirmed via search: `FindPointsGSLIB` `:190`/`:293`,
  `MFEM_USE_GSLIB` guards `:27`/`:83`/`:135`/`:285`/`:311`, `MFEM_ABORT` `:108`/`:278`/`:304`/`:363`,
  function bodies `InterpolateFunction` `:133-280` + `:282-307` (`ComputeLineIntegral` starts `:309`).
- Sibling-shape references: `book/src/L1-L0/essential-dofs-construction-rotation.md` (typed
  `edges:`/`rank:` frontmatter shape), `book/src/L1-L0/fe-space-construction-rotation.md`
  (construction-lowers/MFEM-owned-split + firm-on-positive-structure precedent).

## Open questions / caveats

(Appended to `scaffolding/open-questions.md`.)

- **`interpolator-construction-rotation-l1-l0-theme-needed` (c117 D5) — CLOSED-RESOLVED by this
  dispatch (c118 D3):** the L1>L0 theme is now authored + `status: firm`, and the coupled re-anchor
  upgraded `L1/interpolator`'s `reference` → `depends-on (kind: lowers-to)` edge to it. The
  `interpolator` L1>L0 home is grounded.
- **`interpolator-derham-exactness-law-anchor` (carried, c117 D5):** the de-Rham exactness identities
  (`Curl·Grad=0` / `Div·Curl=0`) stay a *defining-family property* (the L1 entry's law 5), NOT a
  Palace-read law — Palace assembles each edge separately and never composes them in one call. This
  theme lowers the per-edge *construction*, not the complex composition, so the OQ is unaffected.
  *Trigger:* a literature-anchor harvester/lowering-verifier pass.
- **`gslib-field-interp-facility-dedicated-obstruction-theme` (carried, c117 D5):** the GSLIB
  point-interpolation facility is an in-theme sub-note in both `L1/interpolator` and this theme; whether
  it earns a first-class L1>L0 obstruction theme triggers on a field-probe/point-sample output-product
  feature consumer landing. Negative-anchor exhaustiveness is already established (every entry point
  routes through `FindPointsGSLIB` with an abort fallback).
- **RE10 baseline-exception note (no change):** `interpolator` the OP stays RE10 baseline-excepted (no
  faithful inbound consumer edge yet). This theme grounds the *home* (the L1>L0 lowering), NOT the op's
  inbound reachability — no inbound edge was forced. The faithful inbound consumers (`divfree-projector`
  `Grad`, boundary-mode `Bz` curl) remain `reference`-classified consumed-by relations per the existing
  `interpolator` entry; promoting one to a blocking `depends-on` is a separate reachability-grounding
  judgment, not in this dispatch's scope.
