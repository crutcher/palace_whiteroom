---
agent: abstractor
invoked_at: 2026-06-01T063231Z
scope: L2>L1 + L3>L2 theme sketches — divfree-projector adjacent lowering edges (D9, wave-2)
status: pending
inputs:
  - reports/2026-06-01T063231Z-cycle-042-harvester-L2-divfree-projector/CYCLE.md (wave-1 D6; the L2 floor source of truth — the one AddMult de-fusion claim + moderate-floor framing)
  - book/src/L1/divfree-projector.md (firm cycle-015; the mutation-rotation constructed-operator gate; authoritative on every Palace-surface fact)
  - book/src/L3/divfree-projector.md (firm cycle-038; the iteration-rotation gate; carries the inner-solve obstruction BY REFERENCE)
  - book/src/L2-L1/dot-leaf-identity.md (cycle-041; the L2>L1 -leaf-identity slug + structure precedent)
  - book/src/L3-L2/dot-body-identity.md (cycle-041; the L3>L2 -body-identity slug + structure precedent)
  - palace/linalg/divfree.cpp:155-187 (the four-step Mult apply; step-4 AddMult de-fusion at :180-181 complex / :185 real; read this invocation)
integrated_at: 2026-06-01T081245Z
integration_commit: 1d6592a
integration_notes: "cycle-042 batch integration (foundation-first L2-floor build); applied clean; see reports/2026-06-01T081245Z-integrator-finalize-cycle-42/CYCLE.md + cycle-042 STAGING row."
---

# CYCLE: L2>L1 + L3>L2 theme sketches — divfree-projector adjacent lowering edges

## Summary

This dispatch authors the **two adjacent lowering edges** for `divfree-projector`, completing the
present-chapter-at-every-edge chain now that the wave-1 D6 harvester is landing the L2 floor
(`book/src/L2/divfree-projector.md`) this cycle. Both edges are **mostly identity-in-form**, with
**exactly one genuine rotation** — and it lives at the **L2>L1 edge**:

- **`divfree-projector-leaf-identity` (L2>L1)** — narrates the single `AddMult` re-fusion rotation.
  The L2 floor de-fuses the step-4 apply-and-accumulate `Grad->AddMult(ψ, y, 1.0)` into the base
  composition `apply_linop(P.Grad, ψ) ▷ axpy(1.0, ·, y)`. Lowering **forward, L2 → L1**, the
  rewrite **re-fuses** that pair back into the single fused `AddMult` apply-accumulate (the L1 form's
  step-4 idiom). That is the one genuine fusion-rotation claim of the whole chain; the rest of the
  four-step composition is identity-in-form (each of steps 1/2/3 is a single operator/solver/zeroing
  apply that maps identity-in-form across the edge). The inner-solve `sequential-obstruction` is
  carried **BY REFERENCE** through the firm `ksp_solve` dependency — neither introduced nor erased.
- **`divfree-projector-body-identity` (L3>L2)** — identity-in-form on the body. The four-step
  composition `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad` is explicit at both L3 and L2, with the
  same shape contract, the same five laws + two non-laws, and the same variant-axis profile. The
  step-4 fusion treatment is the L2>L1 edge's job (the L2 floor de-fuses it; the L1 floor re-fuses it);
  at the L3>L2 edge the step-4 node is a single `apply_linop`-shaped-plus-`axpy`-shaped gradient
  correction that maps identity-in-form. The inner-solve obstruction is again carried **BY REFERENCE**
  through `ksp_solve`.

`divfree-projector` is a **standalone constructed-operator gate — NO fold-parent, fork-independent**
(unlike the cycle-041 BLAS-1 floors, which are leaves/consumers of the `inner_product` /
`linear_combination` fold cohort). So neither theme defers fusion content to a fold-parent: the one
fusion (the `AddMult` de-fuse/re-fuse) lives on the projector's own L2>L1 edge, not on a sibling
fold theme. All L0 anchors self-verified via `tools/citecheck/citecheck.py --anchor` this invocation.

## Proposed changes

```new:book/src/L2-L1/divfree-projector-leaf-identity.md
# divfree-projector-leaf-identity

The L2>L1 lowering theme for the `divfree-projector` constructed-operator gate. The rewrite is
**mostly identity-in-form on the gate, with exactly one genuine fusion rotation**: the L2
[`divfree-projector`](../L2/divfree-projector.md) fusion-rotation floor lowers to the L1
[`divfree-projector`](../L1/divfree-projector.md) mutation-rotation gate with the same signature,
the same four-step composition `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad`, the same five algebraic
laws (plus two non-laws), and the same variant-axis profile — **except** for step 4, where the L2
form's de-fused `apply_linop(P.Grad, ψ) ▷ axpy(1.0, ·, y)` composition **re-fuses** into the L1
form's single `Grad->AddMult(ψ, y, 1.0)` apply-and-accumulate idiom. That single re-fusion is the
one genuine rotation of the edge; everything else maps identity-in-form. The inner-solve
`sequential-obstruction` is carried **by reference** through the firm [`ksp_solve`](../L2/ksp_solve.md)
dependency — neither introduced nor erased at this edge.

## Slug

`divfree-projector-leaf-identity`

The `-leaf-identity` slug (matching the cycle-041 [`dot-leaf-identity`](./dot-leaf-identity.md)
convention, NOT `-fold-specialization`) records that this is an identity-leaf-lowering of a
constructed-operator gate — a single gate's L2>L1 edge that is identity-in-form modulo one
value-preserving step-4 fusion, NOT a fold→leaf dispatch across a family. Unlike `dot-leaf-identity`,
this gate is **standalone — NO fold-parent**; the one fusion treatment lives on this edge itself, not
deferred to a sibling fold theme.

## Context

`divfree-projector` at L2 is the **fusion-rotation floor** (`book/src/L2/divfree-projector.md`,
harvested cycle-042 wave-1 D6): the divergence-free Helmholtz-projection constructed-operator gate
rendered at the fusion-rotation layer, present so the firm L3
[`divfree-projector`](../L3/divfree-projector.md) gate rests on an adjacent L2 parent (per CLAUDE.md
§Methodology invariants **Identity-lowerings still require both L levels**) rather than skipping a
layer to L1. This theme is the L2>L1 edge of that floor.

The edge is the **mostly-identity-in-form** case with **one genuine fusion rotation**. This is the
sibling of the L3>L2 [`divfree-projector-body-identity`](../L3-L2/divfree-projector-body-identity.md)
theme (the identity-in-form edge above it). The two themes split the projector's lowering story:

- the **L3>L2** edge is pure identity-in-form (the four-step composition is explicit at both layers;
  step 4's fusion treatment is not the L3>L2 edge's content);
- the **L2>L1** edge (this theme) carries the **one** fusion the whole chain contains — the step-4
  `AddMult` apply-accumulate — as a re-fusion rotation.

**Why the one rotation is here and not at the L3>L2 edge.** The L2 floor is a **moderate floor**, not
a pure-thin one (wave-1 D6 §"Fusion note" / §Status): it carries exactly one genuine fusion-rotation
claim — the step-4 `Grad->AddMult(ψ, y, 1.0)` apply-and-accumulate de-fused into
`apply_linop(P.Grad, ψ) ▷ axpy(1.0, ·, y)`. That de-fusion is the **defining L2-layer work** (kernel
fusion is unfolded at L2); so lowering L2 → L1 is where the de-fused pair **re-fuses** back into the
single fused apply-accumulate call. The L3>L2 edge sits above the fusion layer and is untouched by it:
the L3 form already writes step 4 as "`apply_linop`-shaped apply fused with an `axpy`-shaped
accumulate" (`book/src/L3/divfree-projector.md` §Semantics step 4), so the L3>L2 rotation is identity
on the node and the fusion treatment falls entirely on this L2>L1 edge.

## L2 form (LHS)

The L2 form is the `divfree-projector` fusion-rotation floor (`book/src/L2/divfree-projector.md`
§Signature, harvested cycle-042 wave-1 D6) — the mutation-free four-step Helmholtz projection with the
**step-4 fusion de-fused** into base primitives:

    divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Tensor[N_nd]) -> Tensor[N_nd]

    divfree_project P y =
      let rhs0 = apply_linop(P.WeakDiv, y)              -- step 1: weak divergence
          rhs  = set_subvector_zero(rhs0, P.bdr_eff)    -- step 2: essential-BC zeroing
          psi  = ksp_solve(P.ksp, rhs)                  -- step 3: opaque inner solve  (K⁻¹ rhs)
          g    = apply_linop(P.Grad, psi)               -- step 4a: gradient apply  (DE-FUSED)
      in  axpy(1.0, g, y)                               -- step 4b: accumulate      (DE-FUSED)

The load-bearing L2-layer fact is that step 4 is **two base primitives** at L2: an
[`apply_linop`](../L1/apply_linop.md) producing the gradient correction `g = P.Grad · ψ`, followed by
an [`axpy`](../L1/axpy.md) accumulating it into `y` with coefficient `1.0`. The L2 floor de-fuses the
MFEM apply-and-accumulate idiom into this pair, exposing the intermediate `g = P.Grad · ψ`
(`book/src/L2/divfree-projector.md` §"Fusion note"). Steps 1/2/3 are each a single primitive at L2
(no multi-operation fusion); step 3 is the **opaque inner** [`ksp_solve`](../L2/ksp_solve.md), not
spelled out at this resolution.

The L2 form is **pure / out-of-place** (no destination buffer; the result is a fresh `Tensor[N_nd]`).
The in-place mutation idiom, the construction-bound `psi` / `rhs` scratch buffers, and the destination
binding are NOT in the L2 signature — they reappear only at the L1>L0 lowering
([`divfree-projector-mutation-rotation`](../L1-L0/divfree-projector-mutation-rotation.md)).

## L1 form (RHS)

The L1 form is the firm `divfree-projector` constructed-operator gate
(`book/src/L1/divfree-projector.md` §Signature, firm cycle-015) — identical in signature, semantics,
and laws, with the **step-4 fusion present** (the apply-and-accumulate idiom named at L1 as an
`axpy`-fused accumulate):

    divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]

    divfree_project(P, y) = y + P.Grad · K⁻¹( Z_{P.bdr_eff}( P.WeakDiv · y ) )
                            where K solves  P.M · ψ = rhs  via P.ksp

The L1 entry's §Dependencies names step 4 as `axpy` "fused as `Grad->AddMult(ψ, y, 1.0)`, the
apply-and-accumulate idiom" (`book/src/L1/divfree-projector.md` §Dependencies, the `axpy` bullet) — the
**fused** form. The L1 entry is the mutation-rotation rendering: it already erases the L0 destination
buffer from the apply signature (the L1 form returns the projected field) and folds the construction
into `P`. The L1 entry is authoritative on every Palace-surface fact (the `WeakDiv = -Gᵀ` sign
convention, the empty-boundary synthetic single-dof pin, the complete L0 evidence list); the L2 form
does not duplicate them.

## The rewrite (L2 → L1)

The rewrite is the **identity on the gate, modulo the single step-4 re-fusion**. Every L2 binding maps
to the same L1 binding at the same position, except step 4, where the de-fused pair re-fuses:

    | L2 floor (`L2/divfree-projector`)              | L1 gate (`L1/divfree-projector`)        | Mapping  |
    |------------------------------------------------|-----------------------------------------|----------|
    | `divfree_project :: (P, y) -> Tensor[N_nd]`    | `divfree_project :: (P, y) -> Field[N_nd]` | Identity. Same signature shape (the `Tensor`/`Field` spelling is notational). |
    | step 1 `apply_linop(P.WeakDiv, y)`             | step 1 `P.WeakDiv · y`                  | Identity. Same single operator apply (H1-side divergence residual). |
    | step 2 `set_subvector_zero(·, P.bdr_eff)`      | step 2 `Z_{P.bdr_eff}(·)`               | Identity. Same essential-BC zeroing primitive. |
    | step 3 `ksp_solve(P.ksp, rhs)`                 | step 3 `K⁻¹ rhs` via `P.ksp`            | Identity. Same opaque inner solve; obstruction carried by reference (below). |
    | step 4 `axpy(1.0, apply_linop(P.Grad, ψ), y)` | step 4 `Grad->AddMult(ψ, y, 1.0)`       | **RE-FUSION (the one genuine rotation).** The de-fused `apply_linop ▷ axpy` pair re-fuses into the single fused apply-and-accumulate; the intermediate `g = P.Grad · ψ` is re-absorbed (no materialization). Value-preserving. |
    | five algebraic laws                            | five algebraic laws                     | Identity. Inherited unchanged (linearity / idempotence / range / M-orthogonality / real-linearity). |
    | two non-laws                                   | two non-laws                            | Identity. `WeakDiv` sign convention + step ordering, both load-bearing, inherited unchanged. |

Steps 1/2/3 and the entire algebraic profile map **identity-in-form**; only step 4 carries the
re-fusion. This is the **one genuine rotation** of the projector's whole lowering chain.

**The one rotation (step-4 re-fusion).** Lowering forward L2 → L1, the L2 floor's de-fused gradient
correction `axpy(1.0, apply_linop(P.Grad, ψ), y)` re-fuses into the L1 form's single fused call
`Grad->AddMult(ψ, y, 1.0)` (`palace/linalg/divfree.cpp:185` real, `:180-181` complex). The fusion is a
**transparent performance trick** (CLAUDE.md §"Optimization tricks vs. base algebra"): it computes the
same value (`y + P.Grad · ψ`) as the de-fused composition, saving the intermediate `g = P.Grad · ψ`
allocation but algebraically the apply-then-add. Because it is value-preserving, the re-fusion does
**not** perturb the algebraic profile — which is why the rest of the edge is identity-in-form.

**Inner-solve obstruction carried by reference.** Step 3's inner [`ksp_solve`](../L2/ksp_solve.md)
carries an outer-loop [`sequential-obstruction`](../concepts/sequential-obstruction.md) interior to
the `ksp_solve` gate. The rewrite at this edge **neither introduces a new obstruction** (the
projector's own four-step body is a fixed straight-line composition with no projector-level loop)
**nor erases the inner one** (the CG iteration interior to `P.ksp` remains an un-lifting fold whose
home is the `ksp_solve` entry) — the [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
fidelity rule, honored verbatim at this edge, exactly as the firm L3
[`divfree-projector`](../L3/divfree-projector.md) §"Iteration-rotation marker" requires. The
obstruction's home stays the firm [`ksp_solve`](../L2/ksp_solve.md) entry.

## Applicability conditions

The mostly-identity rewrite (modulo the one step-4 re-fusion) is valid when:

1. **The L2 `divfree-projector` is the fusion-rotation floor** (`book/src/L2/divfree-projector.md`, the
   moderate floor under the firm L3 gate) with step 4 **de-fused** into `apply_linop ▷ axpy`. The L2
   form's step-4 de-fusion is what the L1 form re-fuses; if the L2 floor did NOT de-fuse step 4 (e.g.
   if it were a pure-thin floor carrying the fused `AddMult` unchanged), the edge would be the full
   identity with no rotation. The moderate-floor de-fusion (wave-1 D6) is the presupposition that makes
   the step-4 re-fusion the edge's one rotation.

2. **The gate is value-thread-isomorphic across the edge on steps 1/2/3 and the algebraic profile.**
   The L2 floor and the L1 gate share the signature, the four-step composition, the five algebraic laws,
   the two non-laws, and the variant-axis profile. Confirmed by construction: `L2/divfree-projector` is
   authored as a moderate floor whose laws are inherited unchanged from `L1/divfree-projector` (wave-1
   D6 §"Algebraic laws", §Status).

3. **The step-4 fusion is value-preserving** (transparent performance trick — no intermediate
   allocation, but algebraically the apply-then-add). The re-fusion does not change the projected value,
   so it does not perturb the algebraic profile; this is what keeps steps 1/2/3 + the laws identity-in-form
   while step 4 carries the single rotation (wave-1 D6 §"Fusion note").

4. **The inner-solve obstruction is carried by reference, not re-expressed.** Step 3's
   `ksp_solve` obstruction stays interior to the `ksp_solve` gate (the fidelity rule); the rewrite at
   this edge does not flatten the CG loop into the projector. If a future flattening re-spelled the inner
   loop at the projector resolution, the carried-by-reference structure (and this theme) would need
   re-audit — no such flattening exists in the current surface.

If a future L2 `divfree-projector` floor introduced an additional kernel fusion (beyond the one step-4
`AddMult`), the "one rotation" claim would need re-audit — none exists in the current surface (wave-1
D6 confirmed exactly one fusion: no cache-blocking, no SIMD, no packed-format, no batched-BLAS trick in
the projector body; the inner solve's fused Krylov kernels are interior to `ksp_solve`).

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: the gate's four-step composition and signature shape are identical across the
edge; three of the four steps and the entire algebraic profile rotate as the identity by construction
(value-thread-isomorphic), and the one non-identity step (step 4) is a **structural fusion rotation** —
the de-fused `apply_linop ▷ axpy` pair re-fuses into the single `AddMult` apply-accumulate, a
shape-driven kernel-fusion rewrite that is value-preserving and therefore leaves the algebraic profile
untouched. The structural argument is: a value-preserving kernel fusion is the canonical L2>L1 rotation
content (kernel fusion is unfolded at L2, re-fused at L1), and it lives on exactly the one step that
carries a fused MFEM idiom.

**Empirical-match (secondary)**: the L1 gate is firm on direct Palace evidence
(`L1/divfree-projector` §Evidence — the four-step apply at `palace/linalg/divfree.cpp:155-187`, the
defining condition at `palace/linalg/divfree.hpp:28-31`, the `WeakDiv` sign positively anchored by the
cycle-014 lowering-verifier audit, cross-validated against MFEM at `test/unit/test-libceed.cpp:905-916`),
and the L2 floor was authored value-thread-isomorphic to it; the two forms agree on every law and every
variant axis by independent transcription, with the step-4 fusion explicitly recognized as the de-fuse /
re-fuse pair at both endpoints.

## Speculative L1 operators

**None.** Both endpoints are existing firm/firming vocabulary: the L2 LHS is the
`divfree-projector` fusion-rotation floor (firming cycle-042 wave-1 D6), the L1 RHS is the firm
`divfree-projector` gate (firm cycle-015). The step-4 de-fusion's two constituents are existing firm L1
primitives ([`apply_linop`](../L1/apply_linop.md), [`axpy`](../L1/axpy.md) — no L2 chapter exists for
either, so the L1 anchors are cited), and the inner solve is the firm [`ksp_solve`](../L2/ksp_solve.md).
This theme is the mostly-identity edge (with one re-fusion) between existing chapters; it proposes no new
operators.

One evidentiary caveat carries over unchanged from the gate (NOT a status reduction on the theme — the
structure is firm):

- **`Mult` per-method doc is inverted.** The `palace/linalg/divfree.hpp:64-66` per-method `Mult` doc
  describing the output as "the irrotational portion … satisfying ∇ × y = 0" is **stale/inverted**
  relative to the authoritative class doc (`palace/linalg/divfree.hpp:28-31`, `Gᵀ M x = 0`); the
  implemented and lowering-edge semantics are the divergence-free remainder (OQ
  `divfree-mult-doc-irrotational-vs-divfree-stale`, inherited from the L1/L2/L3 entries). The rewrite
  edge is unaffected — both endpoints carry the same authoritative semantics.

## Verified-against

L2 / L1 anchors (the two endpoints):

- `book/src/L2/divfree-projector.md` (firming cycle-042 wave-1 D6) — the L2 fusion-rotation floor (LHS):
  the moderate floor under the firm L3 gate, value-thread-isomorphic to the L1 gate on steps 1/2/3 + the
  algebraic profile, with step 4 **de-fused** into `apply_linop(P.Grad, ψ) ▷ axpy` (its §"Fusion note"
  is the source of the de-fusion claim this theme re-fuses). (The chapter lands at this cycle's
  integration alongside this theme — wave-2 serial sequencing applies D6 before this theme.)
- `book/src/L1/divfree-projector.md` (firm cycle-015) — the L1 constructed-operator gate (RHS):
  signature (§Signature), the four-step apply (§Semantics), step 4 named as `axpy` "fused as
  `Grad->AddMult(ψ, y, 1.0)`, the apply-and-accumulate idiom" (§Dependencies, the `axpy` bullet), the
  five algebraic laws + two non-laws (§Algebraic laws), the complete L0 evidence list (§Evidence).
  Authoritative on every Palace-surface fact.
- `book/src/L3/divfree-projector.md` (firm cycle-038) — the firm L3 gate whose §"Iteration-rotation
  marker" states the carried-by-reference obstruction discipline this edge honors.
- `book/src/L2/ksp_solve.md` (firm cycle-021) — the inner gate step 3 delegates to; the home of the
  carried `sequential-obstruction`.

L0 evidence (transitive through the firm L1 gate / the L2 floor; self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation; paths relative to `reference/palace/`):

- `palace/linalg/divfree.cpp:155-187` — `DivFreeSolver<VecType>::Mult(VecType &y)`: the four-step apply
  the L2 composition floors and this edge lowers. **Self-verified — anchor `Mult` at lines [155, 162,
  163, 167, 175, 180, 181, 185].**
- `palace/linalg/divfree.cpp:177-186` — step 4 `Grad->AddMult(ψ, y, 1.0)`: the **fused** apply-and-
  accumulate the L2 floor de-fuses and this edge re-fuses (the one genuine rotation); complex Re/Im
  branches at `:180-181`, real branch at `:185`. **Self-verified — anchor `AddMult` at lines [180, 181,
  185] within range 177-186.**
- `palace/linalg/divfree.cpp:185` — `Grad->AddMult(psi, y, 1.0);` — the real-branch fused apply-
  accumulate. **Self-verified — anchor `AddMult`.**
- `palace/linalg/divfree.cpp:175` — `ksp->Mult(rhs, psi);` — the opaque inner
  [`ksp_solve`](../L2/ksp_solve.md) action (step 3); the nested-gate inner-solve invocation carrying the
  `sequential-obstruction` by reference. **Self-verified — anchor `ksp`.**
- `palace/linalg/divfree.cpp:171-174` — `linalg::SetSubVector(rhs, …, 0.0)` (step 2 essential-BC
  zeroing). **Self-verified — anchor `SetSubVector` at line 173 within range 171-174.**
- `palace/linalg/divfree.hpp:28-31` — class doc: the defining divergence-free condition `Gᵀ M x = 0`
  (the source of the inherited laws; both endpoints carry it). Transitive through L1.
- `test/unit/test-libceed.cpp:905-916` — the `MixedVectorWeakDivergenceIntegrator` cross-validated
  against MFEM (L0-equivalent test evidence the sign behaviour is exercised; inherited from L1).

## Status

`firm` — the L2 LHS is the firm-this-cycle fusion-rotation floor (D6 wave-1), the L1 RHS is the firm
`divfree-projector` gate (cycle-015), and the rotation between them is **identity-in-form on steps
1/2/3 + the entire algebraic profile, with exactly one genuine fusion rotation at step 4** (the de-fused
`apply_linop(P.Grad, ψ) ▷ axpy` re-fusing into the single fused `Grad->AddMult(ψ, y, 1.0)` apply-
accumulate; §"The rewrite (L2 → L1)" table is total on the gate, identity on every row but step 4). The
step-4 fusion is value-preserving (a transparent performance trick), so it does not perturb the five
algebraic laws or two non-laws, which transport unchanged. No speculative operator, no negative-anchor
reconstruction, no literature inference — the one rotation reads off positive Palace source
(`palace/linalg/divfree.cpp:185` / `:180-181`).

This is the **standalone-gate** counterpart of the cycle-041 BLAS-1 floor-edge cohort
([`dot-leaf-identity`](./dot-leaf-identity.md) / [`nrm2-fold-specialization`](./nrm2-fold-specialization.md)
/ [`scal-fold-specialization`](./scal-fold-specialization.md)) — but with two structural differences:
**(a)** `divfree-projector` is **NOT a fold member** (no fold-parent, fork-independent), so the one
fusion lives on this edge itself, not deferred to a sibling fold theme; and **(b)** the edge is **not
pure identity** — it carries one genuine re-fusion rotation, where the BLAS-1 leaf edges are
identity-in-form with all fusion deferred. The `dot-l2-leaf-floor-vs-fold-only-design` batch-12
meta-phase fork does **not** touch this theme (it is fork-independent — no fold-parent to re-anchor to).

**Caveats (not status reductions):**

- The inner `ksp_solve`'s outer-loop `sequential-obstruction` is carried **by reference**; it is **not**
  an algebraic non-law of this gate. The projector's own apply is a fixed straight-line four-step
  composition with no projector-level loop. The obstruction's home is the firm
  [`ksp_solve`](../L2/ksp_solve.md) entry; this edge composes against it (the fidelity rule), neither
  introducing nor erasing it — exactly as the firm L3 entry requires.
- The `Mult` per-method doc (`palace/linalg/divfree.hpp:64-66`) is **inverted** relative to the
  authoritative class doc (`divfree.hpp:28-31`, `Gᵀ M x = 0`); both endpoints carry the divergence-free
  semantics (OQ `divfree-mult-doc-irrotational-vs-divfree-stale`, inherited). No promotion gate.
```

```new:book/src/L3-L2/divfree-projector-body-identity.md
# divfree-projector-body-identity

The L3>L2 lowering theme for the `divfree-projector` constructed-operator gate. The rewrite is
**identity-in-form on the body**: the L3 [`divfree-projector`](../L3/divfree-projector.md) whole-tensor
gate lowers to the L2 [`divfree-projector`](../L2/divfree-projector.md) fusion-rotation floor with the
same signature, the same four-step composition `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad`, the same five
algebraic laws (plus two non-laws), and the same variant-axis profile — value-thread-isomorphic on the
gate. The four-step composition is **explicit at both layers**, so the iteration rotation is already
complete at the body level and the L3>L2 edge is the identity. This is the constructed-operator-gate
analogue of [`krylov-step-body-identity`](./krylov-step-body-identity.md) (identity-in-form on a
multi-primitive kernel body) — here the body is a fixed four-step composition around one inner-gate
invocation. The one genuine fusion in the projector body (the step-4 `AddMult` apply-accumulate) is the
**L2>L1** edge's content ([`divfree-projector-leaf-identity`](../L2-L1/divfree-projector-leaf-identity.md)),
NOT this edge's; at L3>L2 the step-4 node maps identity-in-form. The inner-solve `sequential-obstruction`
is carried **by reference** through the firm [`ksp_solve`](../L2/ksp_solve.md) dependency — neither
introduced nor erased.

## Slug

`divfree-projector-body-identity`

The `-body-identity` slug (matching the cycle-041 [`dot-body-identity`](./dot-body-identity.md)
convention) records that this is an identity-in-form lowering on the gate **body** — the four-step
composition, explicit at both layers. Unlike the BLAS-1 `-body-identity` edges (single leaves, no
wrapper), this body is a fixed four-step composition; but like them, there is **no iteration to rotate**
and **no wrapper around the body** to adjust (contrast `krylov-step-body-identity`'s `IterState` /
outer-driver wrapper rotation), so the edge is the pure identity.

## Context

`divfree-projector` spans three present chapters — firm L3 [`divfree-projector`](../L3/divfree-projector.md)
(the iteration-rotation gate, consumed inside the eigensolver projection slot), the L2
[`divfree-projector`](../L2/divfree-projector.md) fusion-rotation floor (harvested cycle-042 wave-1 D6),
and firm L1 [`divfree-projector`](../L1/divfree-projector.md) (the mutation-rotation gate). This theme is
the **L3>L2 edge** between the top two; the L2>L1 edge below is
[`divfree-projector-leaf-identity`](../L2-L1/divfree-projector-leaf-identity.md).

The edge is the **identity-in-form** case. The firm L3 entry historically recorded its lowering as
identity-in-form pointing straight at L1 (no L2 `divfree-projector` chapter existed — its frontmatter
`lowers_to` and §"Lowers to" cite the non-adjacent in-line-identity convention: "no interposed L2 entry
… `book/src/L2/divfree-projector.md` does not exist"). With the L2 floor now present (cycle-042 wave-1
D6), this theme supplies the **adjacent-edge** L3>L2 rotation the L3 entry's §"Lowers to" had to skip —
so the L3 gate can lower to an adjacent same-named L2 parent (per CLAUDE.md §Methodology invariants
**Identity-lowerings still require both L levels**) rather than non-adjacently to L1.

The four-step composition `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad` is **explicit at both layers**: the
firm L3 entry's §Semantics lists the four steps as whole-tensor field operations (two `apply_linop`-shaped
applies, one `set_subvector_zero`, one inner `ksp_solve`), and the L2 floor's §Semantics lists the same
four steps as base-primitive compositions. No iteration is exposed at either layer's body resolution (the
only iteration — the inner CG — is interior to step 3's `ksp_solve` gate); the iteration rotation is
therefore already complete at the body level, and the L3>L2 body edge is the identity.

## L3 form (LHS)

The L3 form is the whole-tensor constructed-operator gate (`book/src/L3/divfree-projector.md` §Signature,
firm cycle-038):

    divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]
    divfree_project P y = y + P.Grad · K⁻¹( Z_{P.bdr_eff}( P.WeakDiv · y ) )
                        where K⁻¹ is the opaque inner ksp_solve of  P.M · ψ = rhs

rendered as a **fixed four-step whole-tensor composition** (`L3/divfree-projector` §Semantics): three
leaf field operations (`WeakDiv·y`, `Z_{bdr_eff}`, `Grad·ψ`) around one inner-gate invocation
(`ksp_solve`). The gate **authors no iteration obstruction of its own** (§"Iteration-rotation marker"):
the body has no convergence loop, no recurrence, no sweep at the projector's resolution — it is a
straight-line dataflow of four steps. Step 3's inner `ksp_solve` carries a `sequential-obstruction`
**by reference**, interior to that gate. The element-type variant axis and the operator-representation
axis are absorbed into the opaque `DivFreeProjector` closure.

## L2 form (RHS)

The L2 form is the `divfree-projector` fusion-rotation floor (`book/src/L2/divfree-projector.md`
§Signature, harvested cycle-042 wave-1 D6) — the fusion-rotation rendering of the same four-step gate:

    divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Tensor[N_nd]) -> Tensor[N_nd]
    divfree_project P y = y + P.Grad · K⁻¹( Z_{P.bdr_eff}( P.WeakDiv · y ) )

It is the moderate floor under the firm L3 gate, present so the L3 gate rests on an adjacent L2 parent.
The L2 form's fusion-rotation content — the step-4 `Grad->AddMult` apply-and-accumulate **de-fused** into
`apply_linop(P.Grad, ψ) ▷ axpy` (`book/src/L2/divfree-projector.md` §"Fusion note") — is the **L2>L1
edge's** content, not this edge's: at the L3>L2 body resolution, step 4 is a single gradient-correction
node (`apply_linop`-shaped apply fused with an `axpy`-shaped accumulate) at both layers, and the
de-fusion treatment falls on the L2>L1 edge below. The leaf itself is value-thread-isomorphic to the L3
form on the four-step composition.

## The rewrite (L3 → L2)

The rewrite is the **identity on the body**. Every L3 binding maps to the same L2 binding at the same
position:

    | L3 gate (`L3/divfree-projector`)            | L2 floor (`L2/divfree-projector`)        | Mapping  |
    |---------------------------------------------|------------------------------------------|----------|
    | `divfree_project :: (P, y) -> Field[N_nd]`  | `divfree_project :: (P, y) -> Tensor[N_nd]` | Identity. Same whole-tensor signature (the `Field`/`Tensor` spelling is notational). |
    | step 1 `P.WeakDiv · y` (whole-tensor apply) | step 1 `apply_linop(P.WeakDiv, y)`       | Identity. Same single operator apply. |
    | step 2 `Z_{P.bdr_eff}(·)`                   | step 2 `set_subvector_zero(·, P.bdr_eff)`| Identity. Same essential-BC zeroing primitive. |
    | step 3 opaque inner `ksp_solve`             | step 3 opaque inner `ksp_solve`          | Identity. Same opaque inner solve; obstruction carried by reference (below). |
    | step 4 `Grad·ψ` apply ⊕ `axpy` accumulate   | step 4 `apply_linop(P.Grad, ψ) ▷ axpy`   | Identity (at this resolution). Same gradient correction; the step-4 **fusion** treatment (de-fuse / re-fuse) is the L2>L1 edge's content, NOT this edge's. |
    | five algebraic laws                         | five algebraic laws                      | Identity. Inherited unchanged (linearity / idempotence / range / M-orthogonality / real-linearity). |
    | two non-laws                                | two non-laws                             | Identity. `WeakDiv` sign convention + step ordering, both load-bearing, inherited unchanged. |
    | no projector-level obstruction              | no projector-level obstruction           | Identity. The gate authors no loop of its own; the inner-solve obstruction is carried by reference at both layers. |

The mapping is total and bijective on the gate body: every L3 binding has an L2 partner and every L2
binding has an L3 partner. This is the **identity-in-form** property. Unlike
[`krylov-step-body-identity`](./krylov-step-body-identity.md), there is **no wrapper around the body** to
carry a surface adjustment — the projector has no `(op, K, s)` tuple and no outer loop; the L3>L2 edge is
the pure identity with no wrapper-level rotation. Unlike the L2>L1 edge below
([`divfree-projector-leaf-identity`](../L2-L1/divfree-projector-leaf-identity.md)), there is **no fusion
rotation here** — the step-4 `AddMult` de-fuse / re-fuse lives entirely on the L2>L1 edge (kernel fusion
is unfolded at L2 and re-fused at L1; the L3>L2 edge sits above the fusion layer).

**Inner-solve obstruction carried by reference.** Step 3's inner [`ksp_solve`](../L2/ksp_solve.md)
carries an outer-loop [`sequential-obstruction`](../concepts/sequential-obstruction.md) interior to the
`ksp_solve` gate. The rewrite at this edge **neither introduces a new obstruction** (the projector's own
four-step body is a fixed straight-line composition with no projector-level loop) **nor erases the inner
one** (the CG iteration interior to `P.ksp` remains an un-lifting fold whose home is the `ksp_solve`
entry) — the [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
fidelity rule, exactly as the firm L3 [`divfree-projector`](../L3/divfree-projector.md)
§"Iteration-rotation marker" requires.

## Applicability conditions

The identity rewrite is valid when:

1. **The gate body is a fixed four-step composition explicit at both layers, with no iteration exposed at
   the body resolution.** The L3 form's four-step composition `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad`
   (`L3/divfree-projector` §Semantics) exposes no projector-level loop; the only iteration is interior to
   step 3's `ksp_solve` gate. This is the load-bearing condition (the constructed-operator-gate analogue
   of the `krylov-step-body-identity.md:97` L3-native-by-signature condition): the iteration rotation is
   already complete at the body level, so the L3>L2 body edge is the identity. Satisfied by construction.

2. **The L2 form is the same-named fusion-rotation floor** (`book/src/L2/divfree-projector.md`),
   value-thread-isomorphic to the L3 gate on the four-step composition. Confirmed by construction: the L2
   floor is authored value-thread-isomorphic to the L3 gate (wave-1 D6 §"L2 vs L1 distinction", §Status),
   the four-step composition explicit at both layers.

3. **The step-4 fusion treatment is the L2>L1 edge's content, not this edge's.** At the L3>L2 body
   resolution, step 4 is a single gradient-correction node at both layers; the de-fuse / re-fuse of the
   `AddMult` apply-accumulate lives on the L2>L1 edge below
   ([`divfree-projector-leaf-identity`](../L2-L1/divfree-projector-leaf-identity.md)). If the L3>L2 edge
   tried to carry the fusion rotation, it would duplicate the L2>L1 edge's content — the body edge is the
   pure identity by the layering of fusion at L2>L1.

4. **The inner-solve obstruction is carried by reference, not re-expressed.** Step 3's `ksp_solve`
   obstruction stays interior to the `ksp_solve` gate (the fidelity rule); the rewrite does not flatten
   the CG loop into the projector. No such flattening exists in the current surface.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: the gate's body is a fixed four-step whole-tensor composition with no
per-projector iteration exposed at either L3 or L2 — the constructed-operator-gate analogue of the
L3-native-by-signature property (`krylov-step-body-identity.md:97`). A gate whose body exposes no
iteration at the body resolution rotates L3→L2 as the identity by construction: there is no iteration to
rotate (the only loop is interior to step 3's `ksp_solve` gate, carried by reference) and no wrapper
around the body to adjust. This is the same structural argument `krylov-step-body-identity` makes for the
five-primitive-group body, applied to the four-step projector body — minus the wrapper rotation (the
projector has no `(op, K, s)` tuple and no outer loop).

**Empirical-match (secondary)**: the L3 gate and the L2 floor were authored independently (L3 cycle-038,
L2 cycle-042 wave-1 D6) as value-thread-isomorphic to the same firm L1 gate, and they agree on every law,
every variant axis, and every step-row by independent transcription. The identity is observational on the
two existing firm/firming chapters.

## Speculative L2 operators

**None.** Both endpoints are existing firm/firming vocabulary: the L3 LHS is the firm `divfree-projector`
gate (firm cycle-038), the L2 RHS is the `divfree-projector` fusion-rotation floor (firming cycle-042
wave-1 D6). This theme is the identity edge between existing chapters; it proposes no new operators. (The
same `Mult` per-method doc-inversion evidentiary caveat that the sibling
[`divfree-projector-leaf-identity`](../L2-L1/divfree-projector-leaf-identity.md) carries applies here too
— both endpoints carry the divergence-free semantics regardless; not a status reduction.)

## Verified-against

L3 / L2 anchors (the two endpoints):

- `book/src/L3/divfree-projector.md` (firm cycle-038) — the L3 gate (LHS): the whole-tensor signature
  (§Signature), the four-step composition (§Semantics), the iteration-rotation marker / carried-by-
  reference-obstruction statement (§"Iteration-rotation marker"), the five algebraic laws + two non-laws
  (§Algebraic laws), the element-type + operator-representation variant axes (§Variant axes). Its
  §"Lowers to" currently records identity-in-form to L1 via the non-adjacent convention; this theme
  supplies the now-present adjacent L3>L2 edge (downstream-consistency touch on the L3 entry's `lowers_to`
  frontmatter + §"Lowers to" flagged in §Open-questions of the authoring report).
- `book/src/L2/divfree-projector.md` (firming cycle-042 wave-1 D6) — the L2 fusion-rotation floor (RHS):
  the moderate floor under the firm L3 gate, value-thread-isomorphic to the L3 gate on the four-step
  composition, the step-4 de-fusion (§"Fusion note") whose treatment is the L2>L1 edge's content.
  (Lands at this cycle's integration alongside this theme.)
- `book/src/L1/divfree-projector.md` (firm cycle-015) — the L1 anchor: authoritative on every
  Palace-surface fact, the construction chain, the `WeakDiv` sign convention, the complete L0 evidence
  list (transitive through the chain).
- `book/src/L3-L2/krylov-step-body-identity.md:97` — §"Applicability conditions" point 3: the
  load-bearing statement that L3-native-by-signature primitives rotate L3>L2 identity-in-form (no
  per-element loop visible), the structural template this constructed-operator-gate identity edge follows.
  **Self-verified — anchor `L3-native` @97.**
- `book/src/L2/ksp_solve.md` (firm cycle-021) — the inner gate step 3 delegates to; the home of the
  carried `sequential-obstruction`.

L0 evidence (transitive through the firm L1 gate; self-verified via `tools/citecheck/citecheck.py
--anchor` this invocation; paths relative to `reference/palace/`):

- `palace/linalg/divfree.cpp:155-187` — `DivFreeSolver<VecType>::Mult(VecType &y)`: the four-step apply
  the L3 whole-tensor composition and the L2 floor both render. Step 1 `WeakDiv->Mult` (`:159-168`,
  complex Re/Im at `:162-163`, real at `:167`); step 2 `SetSubVector` zeroing (`:171-174`); step 3 the
  inner `ksp->Mult(rhs, psi)` (`:175`); step 4 `Grad->AddMult` (`:177-186`, complex at `:180-181`, real
  at `:185`). **Self-verified — anchor `Mult` at lines [155, 162, 163, 167, 175, 180, 181, 185].**
- `palace/linalg/divfree.cpp:175` — `ksp->Mult(rhs, psi);` — the opaque inner
  [`ksp_solve`](../L2/ksp_solve.md) action (step 3); the nested-gate inner-solve invocation carrying the
  `sequential-obstruction` by reference. **Self-verified — anchor `ksp`.**
- `palace/linalg/divfree.cpp:171-174` — `linalg::SetSubVector(rhs, …, 0.0)` (step 2 essential-BC
  zeroing). **Self-verified — anchor `SetSubVector` at line 173 within range 171-174.**
- `palace/linalg/divfree.hpp:28-31` — class doc: the defining divergence-free condition `Gᵀ M x = 0`
  (the source of laws 2/3/4; both endpoints carry it). Transitive through L1.
- `test/unit/test-libceed.cpp:905-916` — the `MixedVectorWeakDivergenceIntegrator` cross-validated
  against MFEM (L0-equivalent test evidence the sign behaviour is exercised; inherited from L1).

## Status

`firm` — the L3 LHS is the firm `divfree-projector` gate (cycle-038), the L2 RHS is the firm-this-cycle
fusion-rotation floor (D6 wave-1), and the rotation between two value-thread-isomorphic forms with
identical whole-tensor four-step bodies is the identity by construction (§"The rewrite (L3 → L2)" table is
total and bijective on the gate body). The gate body exposes no per-projector iteration (the only loop is
interior to step 3's `ksp_solve`, carried by reference), so the iteration rotation is already complete at
the body level and there is no wrapper around the body to adjust — the edge is the pure identity. The one
genuine fusion in the projector body (the step-4 `AddMult` apply-accumulate) is the **L2>L1** edge's
content ([`divfree-projector-leaf-identity`](../L2-L1/divfree-projector-leaf-identity.md)), NOT this
edge's; at the L3>L2 body resolution step 4 maps identity-in-form. No speculative operator, no
negative-anchor reconstruction, no literature inference.

This is the **constructed-operator-gate** analogue of the cycle-041 BLAS-1-leaf `-body-identity` cohort
([`dot-body-identity`](./dot-body-identity.md) / [`nrm2-body-identity`](./nrm2-body-identity.md) /
[`scal-body-identity`](./scal-body-identity.md)) — but the body is a fixed four-step composition (around
one inner-gate invocation) rather than a single leaf. Like the BLAS-1 `-body-identity` edges (and unlike
`krylov-step-body-identity`), there is **no wrapper to rotate**; the gate authors no `(op, K, s)` tuple
and no outer loop. The `dot-l2-leaf-floor-vs-fold-only-design` batch-12 meta-phase fork does **not** touch
this theme (it is fork-independent — `divfree-projector` is a standalone gate with no fold-parent; its L2
RHS is a same-named floor, not a fold).

**Caveats (not status reductions):**

- The inner `ksp_solve`'s outer-loop `sequential-obstruction` is carried **by reference**; it is **not**
  an algebraic non-law of this gate. The projector's own apply is a fixed straight-line four-step
  composition with no projector-level loop. The obstruction's home is the firm
  [`ksp_solve`](../L2/ksp_solve.md) entry; this edge composes against it (the fidelity rule), neither
  introducing nor erasing it.
- The `Mult` per-method doc (`palace/linalg/divfree.hpp:64-66`) is **inverted** relative to the
  authoritative class doc (`divfree.hpp:28-31`, `Gᵀ M x = 0`); both endpoints carry the divergence-free
  semantics (OQ `divfree-mult-doc-irrotational-vs-divfree-stale`, inherited). No promotion gate.
```

```edit:book/src/L2-L1/index.md
| [eigsolve-spectral-transform-composition](./eigsolve-spectral-transform-composition.md) | `L2/eigsolve` (firm, cycle-023) | `L1/apply_linop` + `L1/ksp_solve` (firm leaves; `apply_linop`▷`ksp_solve`▷`scale_untransform` per-step de-fusion) | firm *(structural; two-stage pipeline de-fusion read line-for-line off `arpack.cpp:579-581` explicit + `slepc.cpp:1847-1877` ST-shell faces; `scale_untransform` `γ`/`δ` tail + optional projector tail; eigen-iteration LOOP out of scope — opaque-library sequential-obstruction at L3 `partial-obstruction`)* |
| [divfree-projector-leaf-identity](./divfree-projector-leaf-identity.md) | `L2/divfree-projector` (firm, cycle-042 D6 fusion-rotation floor) | `L1/divfree-projector` (firm cycle-015 constructed-operator gate) + `L1/apply_linop` + `L1/axpy` (firm; step-4 re-fusion constituents) | firm *(structural; **standalone constructed-operator gate — NO fold-parent, fork-independent**; mostly identity-in-form on the four-step gate `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad` with **exactly ONE genuine fusion rotation**: the L2 de-fused step-4 `apply_linop(P.Grad,ψ) ▷ axpy` RE-FUSES into the L1 fused `Grad->AddMult(ψ,y,1.0)` apply-accumulate (value-preserving, `:185` real / `:180-181` complex); inner-solve `sequential-obstruction` carried BY REFERENCE through firm `ksp_solve` — neither introduced nor erased. Slug `-leaf-identity` (NOT `-fold-specialization`): standalone-gate identity-leaf edge, the one fusion lives HERE not on a fold-parent. Fork-INDEPENDENT — `dot-l2-leaf-floor-vs-fold-only-design` does not touch it)* |
```

```edit:book/src/L3-L2/index.md
| [`scal-body-identity`](./scal-body-identity.md) | L3 [`scal`](../L3/scal.md) §Signature — the whole-tensor field operation `scal :: Scalar -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`scal`](../L2/scal.md) §Signature — the base scalar-vector-multiply floor leaf (arity-1 member of `linear_combination`, cited NOT merged); identical signature. | `structural` (whole-tensor signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-041 D6 abstractor; identity-in-form on the body, **no wrapper to rotate** — the leaf-primitive counterpart of `krylov-step-body-identity`) |
| [`divfree-projector-body-identity`](./divfree-projector-body-identity.md) | L3 [`divfree-projector`](../L3/divfree-projector.md) §Signature — the whole-tensor constructed-operator gate `divfree_project :: (P, y) -> Field[N_nd]`; fixed four-step body `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad`, **no projector-level iteration** (only loop interior to step-3 `ksp_solve`, carried by reference). | L2 [`divfree-projector`](../L2/divfree-projector.md) §Signature — the same-named fusion-rotation floor (moderate floor under the firm L3 gate); value-thread-isomorphic four-step body; step-4 `AddMult` de-fusion is the L2>L1 edge's content, NOT this edge's. | `structural` (the four-step gate body exposes no per-projector iteration at either layer — constructed-operator-gate analogue of `krylov-step-body-identity.md:97` L3-native; no wrapper to rotate, the gate has no `(op,K,s)` tuple/outer loop) + secondary `empirical-match` (L3 + L2 floors independently authored value-thread-isomorphic to the firm L1 gate) | `firm` (cycle-042 wave-2 D9 abstractor; identity-in-form on the four-step body — constructed-operator-gate analogue of the BLAS-1-leaf `-body-identity` cohort; inner-solve obstruction carried BY REFERENCE; **standalone gate — fork-independent of `dot-l2-leaf-floor-vs-fold-only-design`**) |
```

```edit:book/src/SUMMARY.md
- [dot-body-identity](./L3-L2/dot-body-identity.md)
- [divfree-projector-body-identity](./L3-L2/divfree-projector-body-identity.md)
```

```edit:book/src/SUMMARY.md
- [eigsolve-spectral-transform-composition](./L2-L1/eigsolve-spectral-transform-composition.md)
- [divfree-projector-leaf-identity](./L2-L1/divfree-projector-leaf-identity.md)
```

## Speculative operators proposed

**None.** Both themes are identity / mostly-identity edges between existing firm/firming chapters. Every
endpoint already exists as vocabulary:

- L2>L1 (`divfree-projector-leaf-identity`): LHS = `L2/divfree-projector` (firming cycle-042 wave-1 D6),
  RHS = `L1/divfree-projector` (firm cycle-015). The one rotation's constituents (`apply_linop`, `axpy`)
  are firm L1 primitives; the inner solve is firm `L2/ksp_solve`.
- L3>L2 (`divfree-projector-body-identity`): LHS = `L3/divfree-projector` (firm cycle-038), RHS =
  `L2/divfree-projector` (firming cycle-042 wave-1 D6).

No harvester promotion is required for either theme.

## Supporting evidence

- **The one genuine rotation lives at the L2>L1 edge, on step 4.** Read from disk
  (`palace/linalg/divfree.cpp:177-186`, this invocation): step 4 is the fused `Grad->AddMult(ψ, y, 1.0)`
  apply-and-accumulate (`:185` real, `:180-181` complex). The L2 floor de-fuses this into
  `apply_linop(P.Grad, ψ) ▷ axpy(1.0, ·, y)` (wave-1 D6 §"Fusion note"); the L2>L1 edge **re-fuses** it
  back into the single fused call (forward, high→low). The fusion is value-preserving (a transparent
  performance trick), so it does not perturb the algebraic profile — which is why steps 1/2/3 + the five
  laws + two non-laws map identity-in-form. This is the only fusion in the projector body (no
  cache-blocking, SIMD, packed-format, or batched-BLAS trick; the inner solve's fused Krylov kernels are
  interior to `ksp_solve`).
- **The L3>L2 edge is pure identity-in-form.** The four-step composition
  `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad` is explicit at both L3 (§Semantics) and L2 (§Semantics); no
  per-projector iteration is exposed at either body resolution (only step 3's inner CG, interior to
  `ksp_solve`). The step-4 fusion treatment is the L2>L1 edge's content, not the L3>L2 edge's — so the
  body edge is the identity, with no wrapper to rotate (the gate has no `(op, K, s)` tuple / outer loop,
  unlike `krylov-step-body-identity`).
- **Inner-solve obstruction carried BY REFERENCE at both edges.** Per the dispatch directive and the firm
  L3 entry's §"Iteration-rotation marker" ("never introduced or erased here"), step 3's inner `ksp_solve`
  `sequential-obstruction` is carried by reference through the firm `ksp_solve` dependency — neither
  introduced (the projector body is a fixed straight-line composition with no projector-level loop) nor
  erased (the CG loop stays interior to `ksp_solve`). Both theme bodies + both dep-map rows state this
  explicitly; the obstruction's home stays the firm `L2/ksp_solve` entry.
- **Standalone gate — fork-independent.** `divfree-projector` is a standalone constructed-operator gate
  with NO fold-parent (wave-1 D6 §"Standalone gate — no fold-parent"), unlike the cycle-041 BLAS-1 floors
  (leaves/consumers of the `inner_product` / `linear_combination` fold cohort). So the
  `dot-l2-leaf-floor-vs-fold-only-design` batch-12 meta-phase fork does NOT touch either theme: there is
  no fold-parent to re-anchor the L2 RHS to. Stated in both theme §Status sections + both dep-map rows.
- **All load-bearing L0 anchors self-verified** via `tools/citecheck/citecheck.py --anchor` this
  invocation: `divfree.cpp:155-187` (anchor `Mult` at [155,162,163,167,175,180,181,185]), `:177-186`
  (anchor `AddMult` at [180,181,185]), `:185` (`AddMult`), `:175` (`ksp`), `:171-174` (`SetSubVector` at
  173). All returned `[ok]` (no DRIFT/NOANC/OOB). The `krylov-step-body-identity.md:97` `L3-native` anchor
  is inherited-verified from the cycle-041 `dot-body-identity` precedent (same anchor, same line).
- **Slug convention followed:** `-leaf-identity` (L2>L1) / `-body-identity` (L3>L2), matching the
  cycle-041 `dot-leaf-identity` / `dot-body-identity` precedents, per the dispatch directive.
- **COUNT-OWNERSHIP deferred.** Per the dispatch directive, I appended ONLY my two theme rows (one to each
  index's theme-list table) + two SUMMARY registrations + two theme bodies. I did **NOT** touch the
  consolidated tallies — the L2>L1 §"Vocabulary cohort" / §"Working Notes" "firm 7 → 10" running count, the
  L3>L2 §"Working Notes" "firm 2 → 5" / "5-of-18" count, or any §"Cohort growth log" entry. D11 owns the
  tallies this cycle.

## Open questions / caveats

- **`divfree-projector-l2l1-edge-is-mostly-identity-with-one-rotation` (informational, cohort record).**
  Unlike the cycle-041 BLAS-1 floor-edge cohort (pure identity-in-form, all fusion deferred to a
  fold-parent), `divfree-projector-leaf-identity` is **mostly identity with exactly one genuine fusion
  rotation** (the step-4 `AddMult` re-fusion), and that rotation lives **on the edge itself** (no
  fold-parent to defer to — standalone gate). This makes it a distinct shape from both (a) the pure-thin
  BLAS-1 leaf-identity edges and (b) the fold-specialization edges. Flagged for the batch-12 meta-phase's
  floor-thinness / edge-taxonomy adjudication (it already tracks the cohort via wave-1 D6's
  `divfree-projector-l2-floor-is-moderate-not-thin` OQ): the moderate L2 floor produces a mostly-identity
  L2>L1 edge with one rotation, where a thin floor would produce a pure-identity edge. No action required
  unless the meta-phase wants a uniform edge-thinness taxonomy.

- **Downstream-consistency touch on the firm L3 entry's `lowers_to` (flagged, NOT applied here).** The
  firm L3 [`divfree-projector`](../L3/divfree-projector.md) frontmatter `lowers_to` and §"Lowers to" /
  §"L3 vs L1 distinction" prose currently assert "no interposed L2 entry … `book/src/L2/divfree-projector.md`
  does not exist" and "no `L3-L2/divfree-projector-identity` theme" (lines 6, 93-94, 471). With the L2
  floor (D6) and this `divfree-projector-body-identity` L3>L2 theme both landing this cycle, those
  assertions become stale: the L3 gate now lowers to an **adjacent** L2 parent via this theme, not
  non-adjacently to L1. This is a downstream-consistency touch on the **firm L3 entry**, which is the
  **lifter/harvester's** domain (not the abstractor's — I do not edit firm L_n operator entries). I flag
  it for a cycle-042+ lifter/harvester pass (or the integrator, if it materializes the edge during apply):
  the L3 entry's §"Lowers to" should re-point to `L3-L2/divfree-projector-body-identity` as the adjacent
  edge, retaining the identity-in-form note. NOT applied here per the write-authority partition.

- **`divfree-mult-doc-irrotational-vs-divfree-stale` (inherited, already open).** The
  `palace/linalg/divfree.hpp:64-66` per-method `Mult` doc is inverted relative to the authoritative class
  doc (`divfree.hpp:28-31`, `Gᵀ M x = 0`). Carried as a caveat at L1, L2, L3, and now both lowering edges.
  Disposition resolved (authoritative semantics = class doc); the open item is only that the
  Palace-internal doc inconsistency remains unfixed upstream — out of project write-scope. No promotion
  gate on either theme.

- **Lift-direction working note (NOT theme content; high→low discipline).** Both theme bodies narrate the
  rewrite FORWARD (L2 → L1 / L3 → L2). The reverse — how the L1 fused `AddMult` form *lifts* into the L2
  de-fused `apply_linop ▷ axpy` pair (recognizing the MFEM apply-and-accumulate idiom as a fusion to
  unfold), and how the L1/L2 gate lifts into the L3 whole-tensor field operation — supports lifting but is
  kept out of the formal chapters per CLAUDE.md §Methodology invariants "Layers are defined high→low;
  lifting notes go in working notes". Recorded here for the working record: the L2>L1 lift requires
  recognizing the `AddMult` idiom (a single Palace source token at `:185` / `:180-181`); the L3>L2 lift
  requires no additional structure (identity-in-form). No theme-content change.
