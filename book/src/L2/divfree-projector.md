---
layer: L2
operator: divfree-projector
firmness: firm
rank: firm
edges:
  depends-on:
    - target: L1/divfree-projector
      kind: lowers-to             # the L1 mutation-rotation gate this L2 floor lowers to
    - target: L2-L1/divfree-projector-leaf-identity
      kind: lowers-to             # the L2>L1 lowering theme this floor lowers through (mirrors how L1 ops reach their L1>L0 theme)
    - L2/ksp_solve                # the inner projected-H1 solve (step 3); nested-gate inner gate
  reference:
    - L3/divfree-projector        # the L3 consumer this floor parents
    - L1/apply_linop              # step-1 / step-4 apply (L1 anchor; no L2 chapter)
    - L1/axpy                     # step-4 accumulate (L1 anchor; no L2 chapter)
    - concepts/set_subvector_zero
    - concepts/nested-constructed-operator-gate
    - concepts/sequential-obstruction
---

# divfree-projector

The divergence-free Helmholtz-projection **constructed-operator gate** at the fusion-rotation
layer: the mutation-free linear projection `y' = divfree_project(P, y)` that maps an H(curl)
(Nedelec) field to its **divergence-free component** by removing the irrotational
(discrete-gradient) part. This is the **L2 floor** under the firm L3
[`divfree-projector`](../L3/divfree-projector.md) constructed-operator gate — present so the
L3 gate rests on an adjacent L2 parent per the **Identity-lowerings still require both L
levels** invariant, rather than skipping a layer down to the firm L1
[`divfree-projector`](../L1/divfree-projector.md). It is a **standalone four-step gate with no
fold-parent** — fork-independent, in the constructed-operator-gate family with the firm L2
[`ksp_solve`](./ksp_solve.md) and [`eigsolve`](./eigsolve.md), not a member of the
`inner_product` / `linear_combination` fold cohort.

## Context

L2 is the fusion-rotation layer (`book/src/L2/index.md`): "Kernel fusion across multiple
algebraic operations is unfolded into composition… Batched specialized BLAS calls are written
as compositions of base primitives." `divfree-projector` at L2 is the divergence-free
projection rendered at that layer — a fixed four-step composition over an opaque constructed
projector value, with the **one** kernel fusion in its body (the step-4 apply-and-accumulate)
de-fused back into the base `apply_linop ▷ axpy` composition (see § "Fusion note").

This entry is a **floor entry**. Its purpose is floor *presence*: the firm L3
[`divfree-projector`](../L3/divfree-projector.md) (the iteration-rotation gate, consumed inside
the eigensolver projection slot) and the firm L1
[`divfree-projector`](../L1/divfree-projector.md) (the mutation-rotation gate) sandwich a layer
at which the projector had no chapter. The L2 entry fills it so the lowering chain L3 → L2 → L1
has a present chapter at every adjacent edge, and the L3 gate lowers to an adjacent L2 parent
rather than non-adjacently to L1.

`divfree-projector` is **defined in L2 vocabulary** here (high→low discipline): the signature,
semantics, and algebraic laws are stated at the L2 fusion-rotation resolution. The two adjacent
rotations — how the L2 form lowers to L1 (where the in-place `Mult(VecType &y)` mutation idiom
and the construction-bound `psi`/`rhs` scratch reappear) and how the L3 form lowers to L2 — are
narrated by the separate lowering themes. This chapter does not define `divfree-projector` in
terms of L1 primitives.

The L1 entry [`L1/divfree-projector`](../L1/divfree-projector.md) is authoritative on every
factual claim about the Palace surface (the construction chain, the empty-boundary
synthetic single-dof pin, the `WeakDiv = -Gᵀ` sign convention, the complete L0 evidence list).
This L2 entry adds **fusion-rotation framing** and does not duplicate those Palace-surface details.

### Standalone gate — no fold-parent

Unlike the BLAS-1 floors ([`dot`](./inner_product.md#specializations) / [`nrm2`](./inner_product.md#consumer-nrm2-and-matrix-weighted-norm) /
[`scal`](./linear_combination.md#arity-specializations)), which are leaves / consumers of the `inner_product` /
`linear_combination` fold cohort and carry a load-bearing do-NOT-merge boundary,
`divfree-projector` is **not a member of any fold cohort**. It is a **constructed-operator
gate**: its primary argument `P` is a structured opaque value assembled once at solver setup
(`palace/linalg/divfree.cpp:43-152`), and its apply is a fixed four-step composition over that
value. There is no fold-parent to cite and no fold-cohort boundary to defend. Its L2 family is
the **constructed-operator gates** — the firm L2 [`ksp_solve`](./ksp_solve.md) (outer-driver
composition) and [`eigsolve`](./eigsolve.md) (shift-invert composition) — distinguished from
them by being a **fixed straight-line composition** rather than an outer-driver / spectral
fold (see § "Iteration rotation: obstruction carried by reference").

## Signature

    divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Tensor[N_nd]) -> Tensor[N_nd]
    divfree_project P y = y + P.Grad · K⁻¹( Z_{P.bdr_eff}( P.WeakDiv · y ) )
                        where K⁻¹ is the opaque inner ksp_solve of  P.M · ψ = rhs

Shape contract (bunsen-style; named axes; no element loop exposed at L2; pure value semantics —
no monadic state thread, no in-place mutation at the L2 surface):

- **`P`** — `DivFreeProjector[N_nd, N_h1]` — the constructed projector value, an opaque
  closure bound once at setup and immutable across calls. `N_nd` is the Nedelec (H(curl))
  true-dof axis; `N_h1` is the H1 true-dof axis. Its internal structure — the ε-weighted H1
  mass operator `P.M : LinearOperator[N_h1, N_h1]`, the weak-divergence operator
  `P.WeakDiv : LinearOperator[N_nd, N_h1]`, the discrete gradient
  `P.Grad : LinearOperator[N_h1, N_nd]`, the essential-boundary dof subset
  `P.bdr_eff : DofSubset[N_h1]`, and the **inner solver** `P.ksp : Solver[P.M]` — is
  authoritative at the L1 entry ([`L1/divfree-projector`](../L1/divfree-projector.md)
  §Signature) and is not re-derived here. At L2 the contract sees only the projector-action
  interface and the two domain axes; the construction is a separate setup action.
- **`y`** — `Tensor[N_nd]` — read-only; the input Nedelec field to project. (The L0 form
  mutates it in place; the L2 form is value-producing — the destination buffer is an L1>L0
  lowering concern.) Element type `real` (`Vector`) or `complex` (`ComplexVector`).
- **result** — `Tensor[N_nd]` — the divergence-free component of `y`, satisfying the discrete
  divergence-free condition `Gᵀ M y' = 0` up to the inner `ksp` convergence tolerance on the
  non-essential dofs. Same Nedelec axis `N_nd`.

`Z_S : Tensor[N_h1] -> Tensor[N_h1]` is the zero-on-subset operator
`(Z_S z)_i = 0 if i ∈ S else z_i` (the [`set_subvector_zero`](../concepts/set_subvector_zero.md)
primitive); `K⁻¹` denotes the **opaque inner [`ksp_solve`](./ksp_solve.md)** of `P.M · ψ = rhs`,
**not** exact inversion and **not** spelled out at this entry's resolution.

The L2 signature is identical in shape to the L1 [`divfree-projector`](../L1/divfree-projector.md)
signature and the L3 [`divfree-projector`](../L3/divfree-projector.md) signature; the rotation
L2 → L1 is identity-in-form on the gate's apply (the fusion the L2 layer un-does lives in the
step-4 apply-accumulate, recorded by the L2>L1 lowering theme, not in the signature).

`DivFreeProjector[N_nd, N_h1]` is an **opaque constructed type** at L2: its internal
representation (real vs. complex operators; the inner CG solver, itself a construction-bound
gate; the empty-boundary synthetic single-dof pin) is not part of the L2 signature. The setup
that builds it from the FE spaces and material coefficients
(`palace/linalg/divfree.cpp:43-152`) is a separate setup action (mirroring the L0 construction
/ `Mult` split); it is authoritative at the L1 entry and is not re-derived here. The L2 entry
reads the apply, not the setup.

## Semantics

`divfree_project P y` realizes the **discrete Helmholtz decomposition** of a Nedelec field:
any `y ∈ Tensor[N_nd]` decomposes as `y = y_divfree + Grad·ψ`, where `Grad·ψ` is the
irrotational (gradient-range) part and `y_divfree` is the divergence-free remainder satisfying
`Gᵀ M y_divfree = 0` (`palace/linalg/divfree.hpp:28-31`). The gate returns `y_divfree`. The
result is determined entirely by `P` and `y` — pure value semantics, no hidden state, no
in-place mutation at the L2 surface.

The apply is a **fixed four-step straight-line composition**
(`palace/linalg/divfree.cpp:155-187`), in dataflow order:

1. **Weak divergence** `rhs ← P.WeakDiv · y` — an [`apply_linop`](../L1/apply_linop.md)-shaped
   linear-operator apply computing the H1-side residual measuring the divergence of `y`
   (`palace/linalg/divfree.cpp:159-168`; the complex Re/Im branches at `:162-163`, the real
   branch at `:167`).
2. **Essential-BC zeroing** `rhs ← Z_{P.bdr_eff}(rhs)` — the
   [`set_subvector_zero`](../concepts/set_subvector_zero.md) primitive zeroing the residual on
   the essential boundary dofs (`palace/linalg/divfree.cpp:171-174`, `SetSubVector(rhs, …, 0.0)`).
3. **Projected H1 solve** `ψ ← K⁻¹ rhs`, i.e. the **opaque inner
   [`ksp_solve`](./ksp_solve.md)** of `P.M · ψ = rhs` via `P.ksp`
   (`palace/linalg/divfree.cpp:175`, `ksp->Mult(rhs, psi)`). This is the only step carrying an
   iteration, and that iteration is interior to the `ksp_solve` gate (see § "Iteration
   rotation"). At this entry's resolution it is a single opaque field-to-field action.
4. **Gradient correction** `y' ← y + P.Grad · ψ`
   (`palace/linalg/divfree.cpp:177-186`, via `Grad->AddMult(ψ, y, 1.0)`; the complex Re/Im
   branches at `:180-181`, the real branch at `:185`). **This step is the one fused kernel the
   L2 layer un-folds** — `AddMult` is the apply-and-accumulate idiom fusing an
   [`apply_linop`](../L1/apply_linop.md) and an [`axpy`](../L1/axpy.md) into one call (see §
   "Fusion note").

The mathematical projector is `P = I − Grad (Gᵀ M G)⁻¹ Gᵀ M` (the M-orthogonal projection onto
the divergence-free subspace). The triple product `Gᵀ M G` is never materialized: the system
passed to the inner solve is `P.M` itself, with `Gᵀ` realized by `P.WeakDiv` on the RHS side
and `G` by `P.Grad` on the correction side. The **sign convention** of `WeakDiv` (it absorbs
the negating `-1.0` of the weak-divergence form, `palace/fem/integ/mixedvecgrad.cpp:202`) makes
the correction *additive* (`y + Grad·ψ`, not `y − Grad·ψ`) while the net effect *removes* the
gradient part — this is a load-bearing non-law carried unchanged from L1 (see Algebraic laws).

The complex specialization is the same projection applied component-wise to `Re(y)` and `Im(y)`
with the same real-valued operators (`palace/linalg/divfree.cpp:159-184`); the inner `ksp` step
is a single solve on the `ComplexOperator`-typed system whose CG recursion is component-blind.
There is no cross-coupling between the real and imaginary parts through the projection.

### Iteration rotation: obstruction carried by reference

L2 is the fusion-rotation layer (the iteration view is erased here, re-appearing at L3). The
projector's **four-step apply authors NO iteration obstruction of its own**: the body is a
fixed straight-line dataflow of four steps with no convergence loop, no recurrence, no sweep
at the projector's resolution. But step 3 is the inner [`ksp_solve`](./ksp_solve.md)
(`palace/linalg/divfree.cpp:175`), whose outer convergence-test fold is itself a
[`sequential-obstruction`](../concepts/sequential-obstruction.md) — the canonical outer-loop
obstruction documented at the firm L2 [`ksp_solve`](./ksp_solve.md) entry. The gate carries
that obstruction **by reference**:

- it does **not introduce a new** obstruction — its own four-step body is a fixed composition
  with no projector-level loop; and
- it does **not erase** the inner obstruction — the CG iteration interior to `P.ksp` remains an
  un-lifting fold whose home is the `ksp_solve` entry.

This is the [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
**fidelity rule** at L2: the inner gate's iteration stays interior to `ksp_solve`'s own entry;
at this entry's resolution `P.ksp->Mult(rhs, psi)` is an opaque field-to-field action. The
firm L3 [`divfree-projector`](../L3/divfree-projector.md) §"Iteration-rotation marker" states
the same carried-by-reference discipline at the iteration-rotation layer; the L2 floor honors
it verbatim — the obstruction is **neither introduced nor erased here**, exactly as the firm L3
entry requires.

## Fusion note

`divfree-projector`'s apply contains **exactly one kernel fusion** at L2, and the L2 layer
un-folds it:

- **Step 4 `Grad->AddMult(ψ, y, 1.0)`** is the MFEM **apply-and-accumulate** idiom: a single
  call that applies the operator `P.Grad` to `ψ` and accumulates the result into `y` with
  coefficient `1.0`, without materializing the intermediate `Grad·ψ`. L2 de-fuses this into
  the base composition `y' = axpy(1.0, apply_linop(P.Grad, ψ), y)` — an
  [`apply_linop`](../L1/apply_linop.md) producing the gradient correction, followed by an
  [`axpy`](../L1/axpy.md) accumulating it into `y`. The fused form computes the same value as
  the de-fused composition (the fusion is a transparent performance trick — no intermediate
  allocation, but algebraically the apply-then-add). This is the **one genuine fusion-rotation
  claim** of this entry.

Everything else in the apply is **already in unfused base-algebra form** at the projector's
resolution: step 1 (`WeakDiv->Mult`) and step 3 (`ksp->Mult`) are single operator/solver
applies with no multi-operation fusion; step 2 (`SetSubVector`) is a single subvector-zeroing
primitive. There is **no cache-blocking, no SIMD intrinsic, no packed-format trick, no
batched-BLAS fusion** in the projector body — the inner solve's fused Krylov reduction kernels
are interior to [`ksp_solve`](./ksp_solve.md) and de-fused there, not here. The triple-product
`Gᵀ M G` non-materialization is an **algebraic structuring choice** (already exposed at L1/L3,
where `Gᵀ` = `WeakDiv` on the RHS and `G` = `Grad` on the correction), **not a kernel fusion** —
so it is not L2 de-fusion content; it is part of the gate's definition at every layer.

This is why the entry is a **moderate floor**, not a non-trivial decomposition: the only fusion
the L2 layer un-does (the `AddMult` apply-accumulate) is already named as an `axpy`-fused
accumulate in the L1 entry's Dependencies §; the four-step composition is already explicit at
L1 and L3. The L2 entry's contribution is the fusion-rotation **framing** plus this one
explicit de-fusion claim.

## Algebraic laws

The five laws that hold at L1/L3 transport unchanged to L2, because the constructed-operator-gate
apply is identity-in-form across the L2 rotation (the only fusion the L2 layer un-does — the
step-4 apply-accumulate — is value-preserving). The two load-bearing non-laws also transport
unchanged. Reproduced so the L2 reader does not have to reach to L1; the L1 entry
([`L1/divfree-projector`](../L1/divfree-projector.md) §Algebraic laws) is authoritative on every
factual claim about the Palace surface.

1. **Linearity.** `divfree_project P (α·u + β·v) = α · divfree_project P u + β · divfree_project P v`.
   Each of the four steps is linear (`WeakDiv`, `Z`, `Grad` are linear operators; the inner
   `ksp_solve` is a linear solve), and the step-4 `axpy` accumulate is linear
   (`palace/linalg/divfree.cpp:159-184`). Holds exactly in exact arithmetic; modulo the inner
   `ksp` tolerance under the approximate solve.

2. **Idempotence (projector law).**
   `divfree_project P (divfree_project P y) = divfree_project P y` in exact arithmetic. By the
   defining condition `Gᵀ M (P·y) = 0` (`palace/linalg/divfree.hpp:28-31`), `P·y` lies in the
   divergence-free subspace, so `WeakDiv·(P·y) = 0` (step 1 yields zero residual), hence the
   correction `Grad·ψ = 0` and `P·(P·y) = P·y`. Holds modulo the inner `ksp` tolerance.

3. **Range.** `Range(divfree_project P ·) = {x ∈ Tensor[N_nd] : Gᵀ M x = 0}` — the discrete
   divergence-free subspace (`palace/linalg/divfree.hpp:28-31`).

4. **M-orthogonality (kernel = gradient range).** `Ker(divfree_project P ·) = Range(P.Grad)`:
   the removed component is the irrotational (gradient) part, and the projection is orthogonal
   in the M-inner-product (the projected H1 problem `P.M·ψ = rhs` encodes the M-weighted normal
   equations `Gᵀ M G ψ = Gᵀ M y`). `P.M` is SPD by construction
   (`palace/linalg/divfree.cpp:119`, `// … real and SPD.`), making the M-inner-product
   well-defined.

5. **Real-linearity / block-diagonal complex action.** For `ComplexVector`,
   `divfree_project P (u + i·v) = (divfree_project P u) + i·(divfree_project P v)` — the
   operators are real-valued, so the action is block-diagonal over `{Re, Im}`
   (`palace/linalg/divfree.cpp:159-184`).

Laws that explicitly **do not** hold (inherited unchanged from L1, both load-bearing):

- **Sign convention (additive correction).** The correction is *additive* (`y + Grad·ψ`)
  because `WeakDiv` (built from `MixedVectorWeakDivergenceIntegrator`) internally absorbs the
  minus sign of the weak-divergence form: its bilinear form is `a(u,v) = -(ε u, ∇v)`
  (`palace/fem/integrator.hpp:217`), the `-1.0` materialized at
  `palace/fem/integ/mixedvecgrad.cpp:202` (versus the non-negated `MixedVectorGradientIntegrator`,
  `palace/fem/integ/mixedvecgrad.cpp:142`). A flipped L0 sign would invert the correction
  direction. Property of the constructed `WeakDiv` operator, honored verbatim at L2 and
  positively re-derived from Palace source (the `WeakDiv = -Gᵀ` reading is anchored, not inferred).

- **Step ordering.** The essential-BC zeroing `Z_{bdr_eff}` must compose *after* `WeakDiv·y`
  and *before* the inner `ksp_solve` (`palace/linalg/divfree.cpp:159-175`). Reordering changes
  the result; the sequence `WeakDiv → Z → ksp_solve → Grad` is load-bearing. This is the
  projector body's only ordering constraint; it is a straight-line dataflow dependency, **not**
  a sequential iteration obstruction (the obstruction lives inside step 3's `ksp_solve`, by
  reference).

The inner-solve `sequential-obstruction` is **not** an algebraic non-law of this gate — it is a
property of the inner `ksp_solve` carried by reference (§ "Iteration rotation"). The algebraic
profile (five laws + two non-laws) is **inherited unchanged**; the L2 rendering introduces no
new laws or non-laws, which is what makes the L2↔L1 hop identity-in-form on the gate's apply.

## Dependencies

**Same-layer (L2):**

- [`ksp_solve`](./ksp_solve.md) (firm) — the inner projected H1 solve `P.M · ψ = rhs`
  (step 3, `palace/linalg/divfree.cpp:175`). **Direct, load-bearing dependency**: this is the
  nested-constructed-operator gate's inner gate. The CG iteration internal to `ksp_solve` is the
  standard outer-loop `sequential-obstruction`; it is interior to `ksp_solve` and **does not
  leak** into `divfree-projector` (the fidelity rule). This is the structural fact that makes
  `divfree-projector` obstruction-carrying-by-reference rather than obstruction-free.

**Cross-layer constituents (no L2 chapter exists; L1 anchors):**

- [`apply_linop`](../L1/apply_linop.md) (firm) — the `P.WeakDiv·y` (step 1) and the `P.Grad·ψ`
  apply inside the step-4 de-fusion. No L2 `apply_linop` chapter exists; the L1 anchor is cited.
- [`axpy`](../L1/axpy.md) (firm) — the `+ y` accumulate the step-4 `Grad->AddMult(ψ, y, 1.0)`
  fuses; the de-fused half. No L2 `axpy` chapter exists; the L1 anchor is cited.

**Cross-cutting concepts:**

- [`set_subvector_zero`](../concepts/set_subvector_zero.md) — the `Z_{bdr_eff}` essential-BC
  zeroing (step 2).
- [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md) — the
  structural shape this entry instantiates: the closure `P` carries the inner gate `P.ksp`; the
  fidelity rule (inner iteration stays interior to the inner gate) is the discipline this entry
  follows.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the canonical write-up of
  the outer-loop obstruction this gate carries **by reference** through its inner `ksp_solve`.
- [`constructed-operators`](../concepts/constructed-operators.md) — the construction-time
  absorption of `M`, `WeakDiv`, `Grad`, `bdr_eff`, `ksp` into the opaque `DivFreeProjector`
  closure.

The setup-side dependencies (the construction-time assembly of `M`, `WeakDiv`, `Grad`,
`bdr_eff`, and the inner `ksp` solver, `palace/linalg/divfree.cpp:43-152`) are L1-entry
concerns, not part of the L2 apply — they are consumed once at construction, before the gate is
folded into any L2 expression.

**No fold-parent.** `divfree-projector` is a standalone constructed-operator gate, not a member
of the `inner_product` / `linear_combination` fold cohort; there is no fold-parent dependency
and no do-NOT-merge boundary (contrast the BLAS-1 floors [`dot`](./inner_product.md#specializations) /
[`nrm2`](./inner_product.md#consumer-nrm2-and-matrix-weighted-norm) / [`scal`](./linear_combination.md#arity-specializations)).

**L1 anchor:** [`L1/divfree-projector`](../L1/divfree-projector.md) (firm) —
authoritative on the Palace surface, the construction chain, the empty-boundary single-dof pin,
the `WeakDiv` sign convention, and the complete L0 evidence list. The L2 entry does not
duplicate those details.

## Variant axes

`divfree_project` has **one orthogonal variant axis at L2, plus the absorbed
operator-representation axis** — the same framing as L1 and L3, transported unchanged. Both are
absorbed into the constructed-operator closure; neither appears in the per-call apply's
positional signature.

One orthogonal axis:

1. **element-type** (`real` `Vector` | `complex` `ComplexVector`) — collapsed into the opaque
   `DivFreeProjector[N_nd, N_h1]` closure. The L0 source instantiates both
   (`template class DivFreeSolver<Vector>;` / `<ComplexVector>;`,
   `palace/linalg/divfree.cpp:189-190`); the complex apply is the same real-valued operators
   applied component-wise to `Re(y)` and `Im(y)` (`palace/linalg/divfree.cpp:159-184`), with no
   cross-coupling. The apply is identical in form (the same four steps, the same single
   `AddMult` fusion) across element types.

Absorbed axis:

- **operator-representation** — the constructed `M` / `WeakDiv` / `Grad` operators (each with
  its own sparse / partially-assembled / interpolator representation), the `bdr_eff` dof-subset,
  and the **inner `ksp` solver** (itself a construction-bound gate with its own preconditioner /
  tolerance / iteration-cap absorption) are all built once at setup and collapsed into the
  opaque `DivFreeProjector` closure. By the time the gate is applied, the representation
  distinctions have been erased; the L2 apply sees only the projector-action interface.

The variant-axis profile (one orthogonal + one absorbed) matches the L1 and L3 entries exactly.
**No new axes introduced by the L2 rendering; none merged or split.** (The inner `ksp_solve`'s
own loop-shaping variant axes are interior to that gate, absorbed into `P.ksp` at construction;
they are not `divfree-projector` axes.)

## Stale-doc caveat

The `Mult` class doc comment `palace/linalg/divfree.hpp:64-66` describing the output as "the
irrotational portion … satisfying ∇ × y = 0" is **stale/misleading** relative to the implemented
divergence-free behaviour (a Palace-internal documentation inconsistency; the per-method doc is
**inverted** relative to the authoritative class doc); the implemented and L2 semantics are the
divergence-free target of the class doc `palace/linalg/divfree.hpp:28-31`.

## L2 vs L1 distinction

- **L1**: constructed-operator gate as a pure-functional projection — the mutation-rotated form
  of the L0 `DivFreeSolver<VecType>::Mult(VecType &y)` in-place mutation idiom (the destination
  field dropped from the signature; the construction-bound `psi` / `rhs` scratch absorbed; the
  element-type collapsed into the closure). The L1 vocabulary frames the gate against the L0
  source.
- **L2**: the same gate rendered as the **fusion-rotation** floor. The one fused kernel in the
  body (the step-4 `Grad->AddMult` apply-accumulate) is recognized as a kernel-fusion choice and
  de-fused into `apply_linop ▷ axpy`; the rest of the body is already in unfused base-algebra
  form. The signature is identical to L1; the rotation L2 → L1 is identity-in-form on the gate's
  apply (the fusion the L2 layer un-does is in the step-4 implementation, captured by the L2>L1
  lowering theme — not in the signature).

The two layers' entries share signature, algebraic laws (five), non-laws (two), variant-axis
profile (one orthogonal + one absorbed), and the cited L0 evidence (transitive). They differ in
**layer interpretation**: L1 frames the gate as the mutation-rotated form of the L0 `Mult`
virtual; L2 frames it as the fusion-rotation floor with the single `AddMult` de-fusion. The
layer-coherence invariant (CLAUDE.md §Methodology invariants "Identity-lowerings still require
both L levels") requires the L2 entry to exist so the firm L3 gate has an adjacent L2 parent.

## Evidence

The L2 form is value-thread-isomorphic to the firm L1 form (per the identity-in-form rotation on
the constructed-operator-gate apply, modulo the one value-preserving step-4 de-fusion); all L0
evidence is transitive through L1. Direct citations relevant to this L2 entry (paths relative to
`reference/palace/`):

- [`book/src/L1/divfree-projector.md`](../L1/divfree-projector.md) (firm) —
  authoritative on the Palace surface, the signature, the algebraic laws (inherited unchanged at
  L2), the variant axes (inherited unchanged at L2), the `WeakDiv` sign convention, and the
  complete L0 evidence list.
- [`book/src/L3/divfree-projector.md`](../L3/divfree-projector.md) (firm) — the L3
  consumer this floor goes under; the iteration-rotation gate whose adjacent L2 parent this entry
  supplies; the carried-by-reference obstruction discipline this entry honors.
- [`book/src/L2/index.md`](./index.md) — the dep-map + the constructed-operator-gate / floor
  motif framing; the BLAS-1-floor cohort note (the standalone-vs-fold-member contrast).
- [`book/src/L2/ksp_solve.md`](./ksp_solve.md) (firm) — the inner gate this projector
  delegates to; the home of the carried `sequential-obstruction`.
- `palace/linalg/divfree.cpp:155-187` — `DivFreeSolver<VecType>::Mult(VecType &y)`: the four-step
  apply the L2 composition floors. Step 1 `WeakDiv->Mult` (`:159-168`, complex Re/Im at
  `:162-163`, real at `:167`); step 2 `SetSubVector` zeroing (`:171-174`); step 3 inner
  `ksp->Mult(rhs, psi)` (`:175`); step 4 `Grad->AddMult(ψ, y, 1.0)` (`:177-186`, complex at
  `:180-181`, real at `:185`).
- `palace/linalg/divfree.cpp:175` — `ksp->Mult(rhs, psi);` — the opaque inner
  [`ksp_solve`](./ksp_solve.md) action (step 3); the nested-gate inner-solve invocation carrying
  the `sequential-obstruction` by reference.
- `palace/linalg/divfree.cpp:43-152` — the construction body building `M`, `WeakDiv`, `Grad`,
  `bdr_eff`, and the inner `ksp` solver into the opaque `DivFreeProjector` closure (setup, not L2
  apply content; the `ksp` setup at `:121-149`, `WeakDiv` at `:111-116`, `M` at `:84-110`, `Grad`
  at `:117`).
- `palace/linalg/divfree.cpp:189-190` — `template class DivFreeSolver<Vector>;` /
  `<ComplexVector>;` — the element-type variant axis instantiation.
- `palace/linalg/divfree.hpp:28-31` — class doc: the defining divergence-free condition
  `Gᵀ M x = 0`, the range, and the kernel (gradient nullspace). The source of laws 2/3/4.
- `palace/linalg/divfree.cpp:119` — `// … real and SPD.` — `P.M` SPD, justifying the
  M-inner-product / M-orthogonality (law 4).
- `palace/fem/integrator.hpp:217` — `// Integrator for a(u, v) = -(Q u, grad v) for u in
  H(curl) and v in H1.` (the weak-div bilinear form; the negating sign in Palace source).
- `palace/fem/integ/mixedvecgrad.cpp:202` — `PopulateCoefficientContext(space_dim, Q, transpose,
  -1.0)` (the `-1.0` materializing the weak-divergence sign).
- `palace/fem/integ/mixedvecgrad.cpp:142` — sibling `MixedVectorGradientIntegrator` with NO
  `-1.0` (the side-by-side sign contrast).
- `palace/drivers/eigensolver.cpp:260-262` — the `divfree->Mult(v0)` initial-vector projection
  call site (the integration-path behaviour exercise).
- `test/unit/test-libceed.cpp:905-916` — Palace's `MixedVectorWeakDivergenceIntegrator`
  cross-validated against `mfem::MixedVectorWeakDivergenceIntegrator` (L0-equivalent test
  evidence that the sign behaviour is exercised).
- [`book/src/concepts/nested-constructed-operator-gate.md`](../concepts/nested-constructed-operator-gate.md)
  (firm) — the concept this entry instantiates at L2; the fidelity rule this entry follows.
