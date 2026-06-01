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
