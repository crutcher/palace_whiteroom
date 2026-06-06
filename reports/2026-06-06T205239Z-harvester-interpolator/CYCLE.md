---
agent: harvester
invoked_at: 2026-06-06T205239Z
scope: L1 operator: interpolator
status: integrated
integrated_at: 2026-06-06T214845Z
integration_commit: ad3a65db89bec3cb0af734d5fab52bfee9db7455
integration_notes: "cycle-117 D5 (apply-order 4/5). New firm L1 op interpolator (de-Rham discrete grid-transfer; firm on the discrete piece + a GSLIB opaque-library-ownership obstruction sibling note kept separate). LOAD-BEARING linter-cleanliness fix VERIFIED by finalize: carries NO depends-on edge (the forthcoming L1-L0/interpolator-construction-rotation theme sits under reference, demoted from lowers-to per the repairer) -> unresolved_depends_on_targets HELD 0. Confirms D4's count: landed firm at the FE-space sub-spine. interpolator lands as detritus pending an inbound consumer (GC-ground-don't-remove; NEW node, not a block). All per-report gates PASS. 3 OQs promoted."
inputs:
  - cycle-117 D5 (WAVE-1) dispatch — open-all-feature-fronts directive B front (iii)-b (de-Rham discrete interpolator)
  - palace/fem/fespace.cpp:173-238 (BuildDiscreteInterpolator — the de-Rham-family DiscreteLinearOperator dispatch; the firm structural piece)
  - palace/fem/fespace.hpp:104-115 (GetDiscreteInterpolator on-the-fly accessor + cache)
  - palace/fem/bilinearform.hpp:95-115 (Palace-owned DiscreteLinearOperator wrapper + AddDomainInterpolator)
  - palace/fem/interpolator.hpp:50-56 + palace/fem/interpolator.cpp:133-310 (GSLIB InterpolateFunction point-interp path — library-owned obstruction)
  - palace/drivers/boundarymodesolver.cpp:322 + palace/linalg/divfree.cpp:117 + palace/models/spaceoperator.hpp:224-236 + curlcurloperator.hpp:112 + postoperator.cpp:1673 (consumer sites)
  - book/src/L1/divfree-projector.md, book/src/L1/apply_linop.md, book/src/L1/fe_space.md (sibling vocabulary + status precedent)
  - book/src/semantics/index.md §1.2.1–§1.2.3 (named shape groups / LinOp[(R: ...), (D: ...)] convention — USE+LINK)
canonical_slug: interpolator
---

# CYCLE: Formalize interpolator at L1

## Summary

Formalizes the **de-Rham discrete grid-transfer interpolator** at L1 as a new firm operator
`interpolator`. The operator is the `DiscreteLinearOperator`-based discrete differential
matrix that interpolates a field from an auxiliary FE space into a primal de-Rham-adjacent
space — discrete gradient (H1 → H(curl)), discrete curl (H(curl) → H(div) in 3D, H(curl) → L2
in 2D), and discrete divergence (H(div) → L2). It is produced on the fly by
`FiniteElementSpace::GetDiscreteInterpolator` / `BuildDiscreteInterpolator`
(`palace/fem/fespace.cpp:173-238`) and consumed as an opaque `LinOp` by the divfree projector
(`Grad`), the boundary-mode `Bz = curl(Et)` readout, AMS preconditioner setup, the curl-curl
operator, and post-processing.

There was no prior `interpolator` chapter; the substrate was named only as the rough-in
Vocabulary-cohort bullet `BuildDiscreteInterpolator (rough-in; no anchor yet)` and the dep-map
forward-reference inside `divfree-projector` (the `Grad` step). This dispatch lands the firm
operator entry.

**Maturity judgment: `firm`.** The discrete-interpolator structure is fully positive-anchored
— the entire `BuildDiscreteInterpolator` body is readable, the map-type dispatch enumerates
the four de-Rham edges exhaustively, and the de-Rham grid-transfer relation is **independent
of GSLIB**. The GSLIB point-interpolation path `fem::InterpolateFunction`
(`palace/fem/interpolator.cpp:133-310`) is a **separate, library-owned** function — not
load-bearing for the de-Rham relation — and is documented as a sibling
`obstruction (opaque-library-ownership)` sub-note, NOT folded into a firm claim. (Negative-
finding exhaustiveness for the GSLIB leaf established below.)

## Proposed changes

```new:book/src/L1/interpolator.md
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
  # NB: the L1>L0 `interpolator-construction-rotation` lowering theme is NOT yet authored, so its
  # `lowers-to` edge is carried as a navigational `reference` (slug-as-text), NOT a blocking
  # `depends-on` edge — a `depends-on` edge to a non-existent target would be an unresolved
  # depends-on target (graded-stack rank-linter). The firm rank rests on positive L0 source
  # (cites-evidence, rank-terminal ground truth), not on the forthcoming lowering theme; the edge
  # is promoted to a `depends-on (kind: lowers-to)` once the theme is authored + `status: firm`
  # (rank 3 <= 3), matching the `fe_space` -> `fe-space-construction-rotation` precedent. Authoring
  # tracked by OQ `interpolator-construction-rotation-l1-l0-theme-needed`.
  reference:
    - L1-L0/interpolator-construction-rotation   # FORTHCOMING L1>L0 lowering theme (lowers-to-once-authored; navigational until then)
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
(`palace/fem/fespace.cpp:173-238`; accessor `palace/fem/fespace.hpp:104-115`) —
a `const` member that constructs (and caches) the discrete differential operator
`G` interpolating from the *auxiliary* space `aux_fespace` into `*this` (the
*primal* space). At L0 the member mutates a cached `std::unique_ptr` `G` and a
cached `aux_fespace` pointer, rebuilding lazily when the auxiliary space changes
(`palace/fem/fespace.hpp:108-114`); the L1 form drops the cache and the
mutate-on-miss idiom — the construction is a pure function of the two spaces, and
the caching is an L1>L0 lowering concern.

The construction body dispatches on the **de-Rham map-type pair** of the trial
(auxiliary) and test (primal) spaces — the FE map type fixes which de-Rham edge
the spaces straddle, and that fixes which MFEM interpolator kernel assembles the
matrix:

- **VALUE → H_CURL**: discrete **gradient** `Grad` (H1 → H(curl)); MFEM
  `GradientInterpolator` (`palace/fem/fespace.cpp:191-198`).
- **H_CURL → H_DIV**: discrete **curl** `Curl` (3D: H(curl) → H(div)); MFEM
  `CurlInterpolator` (`palace/fem/fespace.cpp:200-208`).
- **H_CURL → INTEGRAL**: discrete **scalar curl** (2D: H(curl) → L2); MFEM
  `CurlInterpolator` via native (non-libCEED) assembly because libCEED has no
  partial-assembly path for this operator type (`palace/fem/fespace.cpp:209-223`).
- **H_DIV → INTEGRAL**: discrete **divergence** `Div` (H(div) → L2); MFEM
  `DivergenceInterpolator` (`palace/fem/fespace.cpp:225-231`).

Any other map-type pair is an unsupported configuration and aborts
(`palace/fem/fespace.cpp:231-234`). Each branch wraps the assembled matrix in a
[`ParOperator`](./apply_linop.md) (read single-rank per CLAUDE.md §Scope). The
`DiscreteLinearOperator` builder is **Palace-owned**
(`palace/fem/bilinearform.hpp:95-115`); only the per-edge interpolator *kernels*
(`GradientInterpolator` / `CurlInterpolator` / `DivergenceInterpolator`) are
MFEM-owned, and they are read-as-given the same way `fe_space`'s dof internals
and `apply_linop`'s representation are read-as-given — the **dispatch +
assembly structure** is fully positive on Palace source.

The order/direction pin is the `forward`/`swap` check at the head of the body
(`palace/fem/fespace.cpp:179-185`): the operator is well-defined only when the
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
(`G.reset()` on auxiliary-space change, `palace/fem/fespace.hpp:108-114`) is an
L1>L0 memoization concern, not part of the L1 semantics.

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

The 2D scalar-curl branch (`palace/fem/fespace.cpp:209-223`) is the one case that
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
   the L0 cache is an implementation of this purity, `palace/fem/fespace.hpp:108-114`.)
3. **De-Rham-edge selection by map-type pair.** The de-Rham edge — and thus which
   differential operator `G` realizes — is determined entirely by the
   `(aux_map_type, primal_map_type)` pair (plus dimension for curl), per the
   `BuildDiscreteInterpolator` dispatch (`palace/fem/fespace.cpp:186-230`). (Holds:
   exhaustive over the four supported pairs; all others abort.)
4. **Direction asymmetry (NON-law / well-definedness pin).** `interpolator` is NOT
   symmetric in its arguments: it is defined only for the `deriv(aux) → primal`
   direction; the reversed order is rejected at construction
   (`palace/fem/fespace.cpp:179-185`, `MFEM_VERIFY(forward, ...)`). There is no
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
(`palace/fem/interpolator.cpp:190-198`, `:293-301`), guarded by
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
(`palace/fem/interpolator.cpp:27,83,108,135,190-198,278,285,293-301,304,311,363`).
The GSLIB facility is therefore opaque-library-owned, promotion route NONE (stays
obstruction unless Palace re-architects to a non-GSLIB point-interpolation), and is
**orthogonal to** the firm de-Rham discrete interpolator — they share a directory
(`palace/fem/interpolator.*` vs `palace/fem/fespace.*`) and the word "interpolate"
but are different operations. The firm `interpolator` operator above does not depend
on GSLIB.

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

The GSLIB point-interpolation facility is an `obstruction (opaque-library-ownership)`
sibling (see above), NOT a dependency.

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
rank-terminal ground truth), NOT on any sub-firm or unauthored node. The L1>L0
`interpolator-construction-rotation` lowering theme is **not yet authored**, so it is
carried as a navigational `reference` (slug-as-text), NOT a blocking `depends-on`
`lowers-to` edge — this avoids asserting a `depends-on` edge to a non-existent target
(which would regress the rank-linter's `unresolved_depends_on_targets`). The edge is
promoted to `depends-on (kind: lowers-to)` once that theme is authored + `status: firm`
(rank 3 ≤ 3), matching the `fe_space` → `fe-space-construction-rotation` precedent
(which carries the `lowers-to` `depends-on` edge only BECAUSE its theme exists and is firm).
The remaining `reference` edges (`apply_linop`, `fe_space`, `divfree-projector` — all firm)
carry no rank constraint. So no `depends-on` edge rests on a sub-firm or non-existent node,
and the firm rank is well-founded. Authoring the lowering theme is tracked by OQ
`interpolator-construction-rotation-l1-l0-theme-needed`.

## Evidence

- `palace/fem/fespace.cpp:173-238` — `BuildDiscreteInterpolator` full body: the
  `forward`/`swap` de-Rham direction check (`:179-185`), the four map-type-pair
  branches (Grad `:186-199`, Curl-3D `:200-208`, Curl-2D native `:209-223`, Div
  `:225-231`), and the unsupported-pair abort (`:231-234`).
- `palace/fem/fespace.hpp:104-115` — `GetDiscreteInterpolator` on-the-fly accessor +
  lazy `G.reset()` rebuild cache (the L0 mutate-on-miss idiom dropped at L1).
- `palace/fem/bilinearform.hpp:95-115` — Palace-owned `DiscreteLinearOperator` class
  (`:95`) + `AddDomainInterpolator` template (`:114-115`).
- `palace/fem/fespace.cpp:191-198` / `:200-208` / `:225-231` — the
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
  `:190-198` / `:293-301` (`FindPointsGSLIB`), `:278` / `:304` / `:108` / `:363`
  (`MFEM_ABORT` GSLIB-absent fallbacks).
```

```edit:book/src/L1/index.md
| [`fe_space`](./fe_space.md) | `(mesh: Mesh, collection: FECollection) → FiniteElementSpace[N]` (i.e. the typed FE space; `N = GetTrueVSize()` the global true-dof count) | (leaf; the construction pairs a `Mesh` with an `FECollection` and produces an immutable typed value; consumed-by [`fe_assemble`](./fe_assemble.md)/[`weak_form_term`](./weak_form_term.md)/[`eliminate_essential_bc`](./eliminate_essential_bc.md)/[`eliminate_rhs`](./eliminate_rhs.md) — those are consumed-by relations, NOT dependencies; the dof-numbering/ordering/conformity/prolongation-restriction internals are MFEM-owned-read-as-given) | `firm` (FE-space-construction front prime entry; the shared substrate under all 5 solver pipelines; **de-Rham family variant axis** H1/H(curl)/H(div)/L2 ↔ `H1_/ND_/RT_/L2_FECollection`, all 4 witnessed at construction sites `palace/models/spaceoperator.cpp:47/49/51` (ND/H1/RT) + `:72-75` (2-D L2-curl); L0: variadic ctor `palace/fem/fespace.hpp:67-75` forwarding into `mfem::ParFiniteElementSpace`, `GetTrueVSize` `:96`, MFEM-forwarders `:93-103`; coarse-seed `palace/fem/multigrid.hpp:89-90` inside `ConstructFiniteElementSpaceHierarchy` `:78-126`; harvested cycle-064; clean-gate PROMOTE; firm-on-positive-structure, no-dedicated-test caveat non-gating per `fe_assemble`/`apply_linop` precedent; laws: true-dof-axis determinism, family-selection-by-collection-type, mesh/collection separability, coarse-seed identity; NO `dof_map` mirror (MFEM-owned-read-as-given dof structure = identity-in-named-terms smell); opaque-parameter fan-out re-anchors `fe_assemble`/`weak_form_term`/`eliminate_essential_bc`/`eliminate_rhs` in a later replace-and-propagate pass; deferred siblings `fe_collection`/`essential_dofs`/`fe_space_hierarchy` named-not-authored; L1>L0: `fe-space-construction-rotation` cycle-064 D3) |
| [`interpolator`](./interpolator.md) | `FiniteElementSpace[(D: ...)] → FiniteElementSpace[(R: ...)] → LinOp[(R: ...), (D: ...)]` (i.e. the de-Rham discrete differential matrix `G` interpolating from the trial/auxiliary space into the primal space; `G · u_aux` is the discrete Grad/Curl/Div) | (leaf at construction; the assembly is the MFEM-owned interpolator kernel marshalled by the Palace-owned `DiscreteLinearOperator` builder; the produced `LinOp` is consumed via [`apply_linop`](./apply_linop.md) and operates-on two [`fe_space`](./fe_space.md) values — consumed-by/operates-on relations, NOT dependencies; the GSLIB point-interp sibling facility is an `obstruction (opaque-library-ownership)`, NOT a dep) | `firm` (FE-space sub-spine de-Rham grid-transfer operator; **de-Rham-edge variant axis** Grad (H1→ND) / Curl-3D (ND→RT) / Curl-2D (ND→L2) / Div (RT→L2) selected by the map-type pair; L0: whole `BuildDiscreteInterpolator` body `palace/fem/fespace.cpp:173-238` (forward/swap direction pin `:179-185`, four map-type branches `:186-231`, unsupported abort `:231-234`), accessor `palace/fem/fespace.hpp:104-115`, Palace-owned `DiscreteLinearOperator` `palace/fem/bilinearform.hpp:95-115`; consumers `palace/models/spaceoperator.hpp:224-236` + `palace/linalg/divfree.cpp:117` + `palace/drivers/boundarymodesolver.cpp:322` + `palace/models/curlcurloperator.hpp:112` + `palace/models/postoperator.cpp:1673`; harvested cycle-117; firm-on-positive-structure, no-dedicated-test caveat non-gating per `fe_space`/`fe_assemble` precedent; laws: produced-op linearity, construction-determinism, edge-selection-by-map-type, direction-asymmetry NON-law; de-Rham exactness `Curl·Grad=0`/`Div·Curl=0` recorded as DEFINING-FAMILY property NOT Palace-read law; GSLIB point-interp `fem::InterpolateFunction` an `obstruction (opaque-library-ownership)` sibling, orthogonal, non-gating; L1>L0: `interpolator-construction-rotation` forthcoming) |
```

```edit:book/src/L1/index.md
REPLACE the Vocabulary-cohort bullet (book/src/L1/index.md:112):

  OLD:
- `BuildDiscreteInterpolator` *(rough-in; no anchor yet)* — the de-Rham interpolator; **sibling-pull-gated** (name, don't dispatch).

  NEW:
- [`interpolator`](./interpolator.md) **is now FIRM** *(cycle-117 D5)* — the de-Rham discrete grid-transfer operator `FiniteElementSpace[(D: ...)] → FiniteElementSpace[(R: ...)] → LinOp[(R: ...), (D: ...)]`: the `DiscreteLinearOperator`-based discrete differential matrix (Grad H1→ND / Curl ND→RT-3D, ND→L2-2D / Div RT→L2) produced on the fly by `GetDiscreteInterpolator`/`BuildDiscreteInterpolator` (`palace/fem/fespace.cpp:173-238`). **De-Rham-edge variant axis** selected by the trial/test map-type pair; firm-on-positive-structure (whole body read; the `forward` direction pin de-Rham-adjacency well-definedness `:179-185`). The **GSLIB point-interpolation sibling** `fem::InterpolateFunction` (`palace/fem/interpolator.cpp:133-310`, all `MFEM_USE_GSLIB`-guarded `FindPointsGSLIB` with `MFEM_ABORT` fallback) is a **separate, library-owned facility** disposed `obstruction (opaque-library-ownership)` — orthogonal to and non-gating for the firm de-Rham operator. Consumed by the divfree `Grad`, boundary-mode `Bz=curl(Et)`, AMS setup, curl-curl, post-processing. L1>L0: `interpolator-construction-rotation` (forthcoming).
```

```edit:book/src/SUMMARY.md
  - [fe_space](./L1/fe_space.md)
  - [interpolator](./L1/interpolator.md)
```

## Operator content

(The full firm chapter body is authored inside the `` ```new:book/src/L1/interpolator.md `` block above.) Slug: **`interpolator`** (canonical, as dispatched). Signature
`interpolator :: FiniteElementSpace[(D: ...)] -> FiniteElementSpace[(R: ...)] -> LinOp[(R: ...), (D: ...)]`.
Status: **`firm`** (firm-on-positive-structure escape; GSLIB sibling `obstruction (opaque-library-ownership)`).

## Supporting evidence

All citations self-verified with `tools/citecheck/citecheck.py --anchor` against on-disk
`reference/` source (the `:173-238` body END close-brace at `:238` confirmed by direct on-disk
`Read`, per the codemap range-END drift guard):

- `palace/fem/fespace.cpp:173-238` (`BuildDiscreteInterpolator`), `:179-185` (`forward`/`swap`
  direction pin), `:191-198`/`:200-208`/`:225-231` (Grad/Curl/Div kernel selections), `:231-234`
  (unsupported-pair abort).
- `palace/fem/fespace.hpp:104-115` (`GetDiscreteInterpolator` accessor).
- `palace/fem/bilinearform.hpp:95-115` (Palace-owned `DiscreteLinearOperator` + `AddDomainInterpolator`).
- `palace/fem/interpolator.hpp:50-56`, `palace/fem/interpolator.cpp:133-310` + GSLIB guards
  `:190-198`/`:293-301` + `MFEM_ABORT` `:278`/`:304`/`:108`/`:363` (GSLIB obstruction, exhaustively scanned).
- Consumers: `palace/models/spaceoperator.hpp:224-227`/`:228-236`, `palace/models/curlcurloperator.hpp:112`,
  `palace/linalg/divfree.cpp:117`, `palace/drivers/boundarymodesolver.cpp:322`, `palace/models/postoperator.cpp:1673`.

Sibling vocabulary / status precedent: `book/src/L1/fe_space.md`, `book/src/L1/apply_linop.md`,
`book/src/L1/divfree-projector.md`. Named-shape-group / `LinOp[(R: ...), (D: ...)]` convention:
`book/src/semantics/index.md` §1.2.1–§1.2.3 (USE+LINK, not restated).

## Open questions / caveats

- **`interpolator-construction-rotation` L1>L0 theme not yet authored.** The dep-map `lowers-to`
  edge + the in-chapter "L1>L0" references point at a forthcoming theme (the cache-drop +
  lazy-rebuild memoization rotation + the 2D-native-vs-libCEED-PA representation note). Written as
  plain-text slug (no live link) per the forward-reference convention. Flag for a later abstractor
  dispatch: `interpolator-construction-rotation-l1-l0-theme-needed`.
- **De-Rham exactness as a verified law.** Laws `Curl·Grad = 0` / `Div·Curl = 0` are recorded as
  the DEFINING-FAMILY property, NOT promoted to a Palace-read algebraic law, because Palace never
  composes two edges in one call. Promoting them to verified laws would need a literature / MFEM
  de-Rham-complex anchor or a constructed composition test. OQ: `interpolator-derham-exactness-law-anchor`.
- **GSLIB field-interp facility — dedicated obstruction theme?** The GSLIB point-interpolation
  facility (`InterpolateFunction` / `InterpolationOperator` probe-field / `ComputeLineIntegral`) is
  recorded in-chapter as a sibling `obstruction (opaque-library-ownership)` note. If a feature-surface
  consumer (e.g. a field-probe output product) needs it as a first-class L1>L0 obstruction theme, that
  is a later dispatch. OQ: `gslib-field-interp-facility-dedicated-obstruction-theme`.
- **Index consolidated firm-count / tally NOT touched** (per parallel-blind-shared-index guard): only
  the OWN alpha-position dep-map row + OWN FE-space-sub-spine cohort bullet + OWN SUMMARY entry are
  proposed here. The L1-index running firm-count / narrative defers to D4 (the cycle-117 layer-intro-author).
- **`fe-space-intro.md` group-intro refresh** may want a one-line mention of the new `interpolator`
  chapter under the FE-space sub-spine — that is the layer-intro-author's (D4) domain, NOT touched here.
- **Canonical slug confirmed `interpolator`** (as dispatched). Considered `discrete-interpolator` /
  `derham-interpolator` for precision, but `interpolator` matches the dispatch scope and the FE-space
  sub-spine naming pattern (`fe_space`, `fe_collection`); kept.
