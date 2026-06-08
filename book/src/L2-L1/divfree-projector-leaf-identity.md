---
# Lowering theme (L2>L1). Per graded-stack scheme §5: rank = min(endpoint ranks). Both
# endpoints (L2 + L1 divfree_projector) are firm (rank 3); so the theme is firm and
# rank(theme) <= min(endpoints) holds for free.
rank: firm
edges:
  depends-on:
    - target: L2/divfree_projector
      kind: lifts-from            # the L2 fusion-rotation floor (LHS)
    - target: L1/divfree_projector
      kind: lowers-to             # the L1 mutation-rotation gate (RHS)
  reference:
    - L2/ksp_solve                # the inner-solve obstruction carried by reference
    - L1-L0/divfree-projector-mutation-rotation  # the L1>L0 sibling leg
---

# divfree-projector-leaf-identity

The L2>L1 lowering theme for the `divfree_projector` constructed-operator gate. The rewrite is
**mostly identity-in-form on the gate, with exactly one genuine fusion rotation**: the L2
[`divfree_projector`](../L2/divfree_projector.md) fusion-rotation floor lowers to the L1
[`divfree_projector`](../L1/divfree_projector.md) mutation-rotation gate with the same signature,
the same four-step composition `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad`, the same five algebraic
laws (plus two non-laws), and the same variant-axis profile — **except** for step 4, where the L2
form's de-fused `apply_linop(P.Grad, ψ) ▷ axpy(1.0, ·, y)` composition **re-fuses** into the L1
form's single `Grad->AddMult(ψ, y, 1.0)` apply-and-accumulate idiom. That single re-fusion is the
one genuine rotation of the edge; everything else maps identity-in-form. The inner-solve
`sequential-obstruction` is carried **by reference** through the firm [`ksp_solve`](../L2/ksp_solve.md)
dependency — neither introduced nor erased at this edge.

## Slug

`divfree-projector-leaf-identity`

The `-leaf-identity` slug (NOT `-fold-specialization`) records that this is an identity-leaf-lowering
of a constructed-operator gate — a single gate's L2>L1 edge that is identity-in-form modulo one
value-preserving step-4 fusion, NOT a fold→leaf dispatch across a family. This gate is **standalone
— NO fold-parent**; the one fusion treatment lives on this edge itself, not deferred to a sibling
fold theme.

## Context

`divfree_projector` at L2 is the **fusion-rotation floor** (`book/src/L2/divfree_projector.md`):
the divergence-free Helmholtz-projection constructed-operator gate
rendered at the fusion-rotation layer, present so the firm L3
[`divfree_projector`](../L3/divfree_projector.md) gate rests on an adjacent L2 parent (per CLAUDE.md
§Methodology invariants **Identity-lowerings still require both L levels**) rather than skipping a
layer to L1. This theme is the L2>L1 edge of that floor.

The edge is the **mostly-identity-in-form** case with **one genuine fusion rotation**. This is the
sibling of the L3>L2 identity-in-form rotation — the degenerate `divfree-projector-body-identity`
relationship recorded as an in-line §"Downward to L2" note on the L3 entry
[`divfree_projector`](../L3/divfree_projector.md) (above it). The two edges split the projector's
lowering story:

- the **L3>L2** edge is pure identity-in-form (the four-step composition is explicit at both layers;
  step 4's fusion treatment is not the L3>L2 edge's content);
- the **L2>L1** edge (this theme) carries the **one** fusion the whole chain contains — the step-4
  `AddMult` apply-accumulate — as a re-fusion rotation.

**Why the one rotation is here and not at the L3>L2 edge.** The L2 floor is a **moderate floor**, not
a pure-thin one (`L2/divfree_projector` §"Fusion note"): it carries exactly one genuine fusion-rotation
claim — the step-4 `Grad->AddMult(ψ, y, 1.0)` apply-and-accumulate de-fused into
`apply_linop(P.Grad, ψ) ▷ axpy(1.0, ·, y)`. That de-fusion is the **defining L2-layer work** (kernel
fusion is unfolded at L2); so lowering L2 → L1 is where the de-fused pair **re-fuses** back into the
single fused apply-accumulate call. The L3>L2 edge sits above the fusion layer and is untouched by it:
the L3 form already writes step 4 as "`apply_linop`-shaped apply fused with an `axpy`-shaped
accumulate" (`book/src/L3/divfree_projector.md` §Semantics step 4), so the L3>L2 rotation is identity
on the node and the fusion treatment falls entirely on this L2>L1 edge.

## L2 form (LHS)

The L2 form is the `divfree_projector` fusion-rotation floor (`book/src/L2/divfree_projector.md`
§Signature) — the mutation-free four-step Helmholtz projection with the
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
(`book/src/L2/divfree_projector.md` §"Fusion note"). Steps 1/2/3 are each a single primitive at L2
(no multi-operation fusion); step 3 is the **opaque inner** [`ksp_solve`](../L2/ksp_solve.md), not
spelled out at this resolution.

The L2 form is **pure / out-of-place** (no destination buffer; the result is a fresh `Tensor[N_nd]`).
The in-place mutation idiom, the construction-bound `psi` / `rhs` scratch buffers, and the destination
binding are NOT in the L2 signature — they reappear only at the L1>L0 lowering
([`divfree-projector-mutation-rotation`](../L1-L0/divfree-projector-mutation-rotation.md)).

## L1 form (RHS)

The L1 form is the firm `divfree_projector` constructed-operator gate
(`book/src/L1/divfree_projector.md` §Signature) — identical in signature, semantics,
and laws, with the **step-4 fusion present** (the apply-and-accumulate idiom named at L1 as an
`axpy`-fused accumulate):

    divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]

    divfree_project(P, y) = y + P.Grad · K⁻¹( Z_{P.bdr_eff}( P.WeakDiv · y ) )
                            where K solves  P.M · ψ = rhs  via P.ksp

The L1 entry's §Dependencies names step 4 as `axpy` "fused as `Grad->AddMult(ψ, y, 1.0)`, the
apply-and-accumulate idiom" (`book/src/L1/divfree_projector.md` §Dependencies, the `axpy` bullet) — the
**fused** form. The L1 entry is the mutation-rotation rendering: it already erases the L0 destination
buffer from the apply signature (the L1 form returns the projected field) and folds the construction
into `P`. The L1 entry is authoritative on every Palace-surface fact (the `WeakDiv = -Gᵀ` sign
convention, the empty-boundary synthetic single-dof pin, the complete L0 evidence list); the L2 form
does not duplicate them.

## The rewrite (L2 → L1)

The rewrite is the **identity on the gate, modulo the single step-4 re-fusion**. Every L2 binding maps
to the same L1 binding at the same position, except step 4, where the de-fused pair re-fuses:

    | L2 floor (`L2/divfree_projector`)              | L1 gate (`L1/divfree_projector`)        | Mapping  |
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
[`divfree_projector`](../L3/divfree_projector.md) §"Iteration-rotation marker" requires. The
obstruction's home stays the firm [`ksp_solve`](../L2/ksp_solve.md) entry.

## Applicability conditions

The mostly-identity rewrite (modulo the one step-4 re-fusion) is valid when:

1. **The L2 `divfree_projector` is the fusion-rotation floor** (`book/src/L2/divfree_projector.md`, the
   moderate floor under the firm L3 gate) with step 4 **de-fused** into `apply_linop ▷ axpy`. The L2
   form's step-4 de-fusion is what the L1 form re-fuses; if the L2 floor did NOT de-fuse step 4 (e.g.
   if it were a pure-thin floor carrying the fused `AddMult` unchanged), the edge would be the full
   identity with no rotation. The moderate-floor de-fusion is the presupposition that makes
   the step-4 re-fusion the edge's one rotation.

2. **The gate is value-thread-isomorphic across the edge on steps 1/2/3 and the algebraic profile.**
   The L2 floor and the L1 gate share the signature, the four-step composition, the five algebraic laws,
   the two non-laws, and the variant-axis profile: `L2/divfree_projector` is
   a moderate floor whose laws are inherited unchanged from `L1/divfree_projector`
   (`L2/divfree_projector` §"Algebraic laws").

3. **The step-4 fusion is value-preserving** (transparent performance trick — no intermediate
   allocation, but algebraically the apply-then-add). The re-fusion does not change the projected value,
   so it does not perturb the algebraic profile; this is what keeps steps 1/2/3 + the laws identity-in-form
   while step 4 carries the single rotation (`L2/divfree_projector` §"Fusion note").

4. **The inner-solve obstruction is carried by reference, not re-expressed.** Step 3's
   `ksp_solve` obstruction stays interior to the `ksp_solve` gate (the fidelity rule); the rewrite at
   this edge does not flatten the CG loop into the projector. If a future flattening re-spelled the inner
   loop at the projector resolution, the carried-by-reference structure (and this theme) would need
   re-audit — no such flattening exists in the current surface.

If a future L2 `divfree_projector` floor introduced an additional kernel fusion (beyond the one step-4
`AddMult`), the "one rotation" claim would need re-audit — none exists in the current surface (exactly
one fusion: no cache-blocking, no SIMD, no packed-format, no batched-BLAS trick in
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
(`L1/divfree_projector` §Evidence — the four-step apply at `palace/linalg/divfree.cpp:155-187`, the
defining condition at `palace/linalg/divfree.hpp:28-31`, the `WeakDiv` sign positively anchored,
cross-validated against MFEM at `test/unit/test-libceed.cpp:905-916`),
and the L2 floor is value-thread-isomorphic to it; the two forms agree on every law and every
variant axis by independent transcription, with the step-4 fusion explicitly recognized as the de-fuse /
re-fuse pair at both endpoints.

## Speculative L1 operators

**None.** Both endpoints are existing firm vocabulary: the L2 LHS is the
`divfree_projector` fusion-rotation floor, the L1 RHS is the firm
`divfree_projector` gate. The step-4 de-fusion's two constituents are existing firm L1
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

## Evidence

L2 / L1 anchors (the two endpoints):

- `book/src/L2/divfree_projector.md` (firm) — the L2 fusion-rotation floor (LHS):
  the moderate floor under the firm L3 gate, value-thread-isomorphic to the L1 gate on steps 1/2/3 + the
  algebraic profile, with step 4 **de-fused** into `apply_linop(P.Grad, ψ) ▷ axpy` (its §"Fusion note"
  is the source of the de-fusion claim this theme re-fuses).
- `book/src/L1/divfree_projector.md` (firm) — the L1 constructed-operator gate (RHS):
  signature (§Signature), the four-step apply (§Semantics), step 4 named as `axpy` "fused as
  `Grad->AddMult(ψ, y, 1.0)`, the apply-and-accumulate idiom" (§Dependencies, the `axpy` bullet), the
  five algebraic laws + two non-laws (§Algebraic laws), the complete L0 evidence list (§Evidence).
  Authoritative on every Palace-surface fact.
- `book/src/L3/divfree_projector.md` (firm) — the firm L3 gate whose §"Iteration-rotation
  marker" states the carried-by-reference obstruction discipline this edge honors.
- `book/src/L2/ksp_solve.md` (firm) — the inner gate step 3 delegates to; the home of the
  carried `sequential-obstruction`.

L0 evidence (transitive through the firm L1 gate / the L2 floor; paths relative to `reference/palace/`):

- `palace/linalg/divfree.cpp:155-187` — `DivFreeSolver<VecType>::Mult(VecType &y)`: the four-step apply
  the L2 composition floors and this edge lowers.
- `palace/linalg/divfree.cpp:177-186` — step 4 `Grad->AddMult(ψ, y, 1.0)`: the **fused** apply-and-
  accumulate the L2 floor de-fuses and this edge re-fuses (the one genuine rotation); complex Re/Im
  branches at `:180-181`, real branch at `:185`.
- `palace/linalg/divfree.cpp:185` — `Grad->AddMult(psi, y, 1.0);` — the real-branch fused apply-
  accumulate.
- `palace/linalg/divfree.cpp:175` — `ksp->Mult(rhs, psi);` — the opaque inner
  [`ksp_solve`](../L2/ksp_solve.md) action (step 3); the nested-gate inner-solve invocation carrying the
  `sequential-obstruction` by reference.
- `palace/linalg/divfree.cpp:171-174` — `linalg::SetSubVector(rhs, …, 0.0)` (step 2 essential-BC
  zeroing).
- `palace/linalg/divfree.hpp:28-31` — class doc: the defining divergence-free condition `Gᵀ M x = 0`
  (the source of the inherited laws; both endpoints carry it). Transitive through L1.
- `test/unit/test-libceed.cpp:905-916` — the `MixedVectorWeakDivergenceIntegrator` cross-validated
  against MFEM (L0-equivalent test evidence the sign behaviour is exercised; inherited from L1).
