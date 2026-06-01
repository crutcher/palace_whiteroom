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
([`dot-leaf-identity`](./dot-leaf-identity.md) / [`nrm2-leaf-identity`](./nrm2-leaf-identity.md)
/ [`scal-leaf-identity`](./scal-leaf-identity.md)) — but with two structural differences:
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
