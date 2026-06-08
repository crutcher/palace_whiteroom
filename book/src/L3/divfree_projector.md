---
layer: L3
operator: divfree_projector
firmness: firm
edges:
  depends-on:
    - target: L2/divfree_projector
      kind: lowers-to
    - target: L1/set_subvector_zero
      kind: uses                        # step-2 essential-BC zeroing `Z_{bdr_eff}(rhs)` IS the set_subvector_zero primitive (divfree.cpp:171-174; §Semantics step 2). The firm L1 operator is the authoritative home; this depends-on gives the firm-but-absorbed set_subvector_zero cluster root-reachability via this projector.
    - target: concepts/set_subvector_zero
      kind: uses                        # the cross-cutting concept page for the same step-2 primitive (the §Dependencies prose pointer, now a typed liveness edge).
  reference:
    - L2-L1/divfree-projector-leaf-identity
variant_axes:
  orthogonal:
    - element-type (Vector real | ComplexVector complex; collapsed into the opaque DivFreeProjector closure; the complex apply is the same real-valued operators applied component-wise to Re/Im)
  absorbed:
    - operator-representation (the constructed M / WeakDiv / Grad operators, bdr_eff dof-subset, and the inner ksp solver are all built once at setup and collapsed into the opaque DivFreeProjector closure)
---

# divfree_projector

Divergence-free projector as a whole-tensor field operation at L3: the
constructed-operator gate `y' = divfree_project(P, y)` that maps an H(curl)
(Nedelec) field to its **divergence-free component** by removing the irrotational
(discrete-gradient) part. The iteration-rotation rendering of the same
Helmholtz-style subspace projection that L1 [`divfree_projector`](../L1/divfree_projector.md)
provides; identity-in-form lowering to L1 on the constructed-operator-gate apply.
Unlike the thinnest gate [`jacobi-smoother`](./jacobi-smoother.md), this gate's
per-call body **invokes an inner solve** — it carries a `sequential-obstruction`
**by reference** through its firm-L3 [`ksp_solve`](./ksp_solve.md) dependency
(never introducing a new obstruction, never erasing the inner one).

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as
whole-tensor primitives with no element loop exposed at the layer's vocabulary,
with sequential obstructions named explicitly per
[`sequential-obstruction`](../concepts/sequential-obstruction.md).
`divfree_projector` at L3 is the value-threaded form of the divergence-free
projection — the same constructed-operator gate that L1 names (replacing the L0
`DivFreeSolver<VecType>::Mult(VecType &y)` in-place mutation idiom,
`palace/linalg/divfree.cpp:155-187`), read at L3 as a whole-tensor field operation
over an opaque constructed projector value.

`divfree_projector` is a **constructed-operator gate** at L3, in the same family as
the firm [`ksp_solve`](./ksp_solve.md), [`eigsolve`](./eigsolve.md), and
[`jacobi-smoother`](./jacobi-smoother.md): its primary argument `P` is a structured
opaque value built once at solver setup (`palace/linalg/divfree.cpp:43-152`),
carrying the ε-weighted H1 mass operator `M`, the weak-divergence operator
`WeakDiv`, the discrete gradient `Grad`, the effective essential-boundary dof set
`bdr_eff`, and — load-bearing at L3 — the **construction-bound inner solver**
`P.ksp : Solver[P.M]`. Where `jacobi-smoother` is the *thinnest* gate (its apply is
one elementwise product, carrying no obstruction of any kind) and `apply_linop` is
a leaf operator-apply, `divfree_projector` sits with `ksp_solve` and `eigsolve` as
an **obstruction-carrying** gate — but with a sharp distinction in *how* it carries
the obstruction (see §"Iteration-rotation marker"): it carries one **by reference**,
through its inner `ksp_solve`, rather than authoring an outer loop of its own.

The four-step apply is a **fixed straight-line composition**
(`palace/linalg/divfree.cpp:155-187`): `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad`.
Only step 3 (the projected H1 solve `ksp->Mult(rhs, psi)`,
`palace/linalg/divfree.cpp:175`) contains an iteration, and that iteration is the
firm-L3 [`ksp_solve`](./ksp_solve.md) outer-driver fold — interior to that gate, not
to this one. The other three steps are whole-tensor field operations: two
`apply_linop`-shaped linear-operator applies (`WeakDiv·y`, `Grad·ψ`) and one
`set_subvector_zero` essential-BC zeroing. The gate is, at L3, a fixed composition
of three leaf field operations around one inner-gate invocation.

This is a **nested-constructed-operator gate** per
[`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md):
the closure `P` carries another constructed-operator gate `P.ksp` as a sub-field, and
the L3 entry honours the **fidelity rule** — the inner gate's iteration stays interior
to `ksp_solve`'s own L3 entry and does **not** leak into this one. At this entry's
resolution `P.ksp->Mult(rhs, psi)` is the opaque `K⁻¹` action. The whole projector's
lowering is the *composition* of the adjacent-edge themes (the L1>L0
`divfree-projector-mutation-rotation` delegating its inner solve to
`ksp-solve-mutation-rotation`), not a single flattened rewrite that re-spells the CG
loop.

The relationship to the adjacent layers:

- **Upward** to L4: there is **no standalone L4 entry** for `divfree_projector`.
  Like the firm `apply_linop` / `ksp_solve` / `jacobi-smoother` constructed-operator
  gates, the projector apply carries no monadic effect of its own, no
  state-stratification typing, and no outer-driver structure authored at the
  projector level — its body is a fixed four-step composition whose only iteration is
  delegated to the inner `ksp_solve` gate. L4's first-class vocabulary carries one of
  (a) monadic effect, (b) state-stratification typing, or (c) outer-driver structure;
  the projector gate authors none of its own (the inner `ksp_solve`'s outer-driver
  structure lives in *that* gate's territory). Per CLAUDE.md §Methodology invariants
  "Layers are defined high→low", the absence of an L4 entry is a deliberate scoping
  verdict, not a gap.

- **Downward** to L2/L1: `divfree_projector` lowers to the adjacent L2 floor
  [`divfree_projector`](../L2/divfree_projector.md) and onward to L1
  [`divfree_projector`](../L1/divfree_projector.md). The L3>L2 rotation is a **degenerate
  identity-in-named-terms lowering**, annotated in-line here (no dedicated L3>L2 theme file):
  L1, L2, and L3 all see
  `divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]`
  with the same shape contract, the same five algebraic laws (plus the two load-bearing
  non-laws), and the same element-type variant axis. The four-step composition
  `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad` is **explicit and value-thread-isomorphic at
  BOTH L3 and L2** (the composition is not exposed at one layer and collapsed at the other —
  there is no vocabulary shift across the L3>L2 edge to rotate). The L3>L2 hop passes through the
  adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require
  both L levels**.
  **The ONE genuine fusion rotation in the whole projector chain lives on the L2>L1 edge,
  NOT this one**: the step-4 gradient correction de-fuses at L2 into
  `apply_linop(P.Grad, ψ) ▷ axpy` and re-fuses at L1 into the single fused
  `Grad->AddMult(ψ, y, 1.0)` apply-accumulate (`palace/linalg/divfree.cpp:185` real /
  `:180-181` complex) — a real translation across the L2↔L1 vocabulary boundary, captured by
  the KEPT firm theme [`divfree-projector-leaf-identity`](../L2-L1/divfree-projector-leaf-identity.md),
  reachable directly from this L3 entry via the live link above (the L2 floor entry itself
  carries no live link to the KEPT theme, only descriptive prose). The substantive leaf-mutation rotation in the chain is
  the L1>L0 rotation: the four-step apply lowers to Palace's in-place `Mult(VecType &y)`
  mutation idiom, captured by the firm L1>L0 theme
  [`divfree-projector-mutation-rotation`](../L1-L0/divfree-projector-mutation-rotation.md).
  The L3>L2 hop is a layer-coherence identity (each layer is coherent within itself), not an
  algebraic one; with no non-adjacent `L3-L1/` directory created — the transitive L3>L1
  identity is annotated in-line per the non-adjacent-identity convention (precedent:
  the firm L3 `jacobi-smoother` / `apply_linop` / `dot` / `scal` cohort, all of which note
  their identity rotations in-line).

This L3 entry is the **layer-coherence anchor**: a reader at L3 can find
`divfree_projector` here, in L3 vocabulary, without having to reach down to L1 to
recover the constructed-operator-gate apply, and without having to consult a
consuming eigensolver's projection slot to see the gate in use. It enacts the
methodology invariant **Identity-lowerings still require
both L levels** (CLAUDE.md §Methodology invariants; the firm L3 `krylov_step` backfill is the
precedent, the firm L3 `ksp_solve` + `jacobi-smoother` the
constructed-operator-gate siblings), and is one of the six (A) firm
identity-in-form L3 candidates ("constructed-operator gate, like firm-L3
`ksp_solve`").

## Signature

    divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]
    divfree_project P y = y + P.Grad · K⁻¹( Z_{P.bdr_eff}( P.WeakDiv · y ) )
                        where K⁻¹ is the opaque inner ksp_solve of  P.M · ψ = rhs

Shape contract (positional values; bunsen-style named axes; no element loop exposed
at L3; no monadic effect, no `readonly` typing — the typing distinctions are deferred
to the wrapper layers above):

- **`P`** — `DivFreeProjector[N_nd, N_h1]` — the constructed projector closure, an
  opaque value bound once at setup and immutable across calls. `N_nd` is the Nedelec
  (H(curl)) true-dof axis; `N_h1` is the H1 true-dof axis. The internal structure —
  the ε-weighted H1 mass operator `P.M : LinearOperator[N_h1, N_h1]`, the
  weak-divergence operator `P.WeakDiv : LinearOperator[N_nd, N_h1]`, the discrete
  gradient `P.Grad : LinearOperator[N_h1, N_nd]`, the essential-boundary dof subset
  `P.bdr_eff : DofSubset[N_h1]`, and the **inner solver** `P.ksp : Solver[P.M]` — is
  authoritative at the L1 entry (`book/src/L1/divfree_projector.md` §Signature) and is
  not re-derived here. At L3 the contract sees only the projector-action interface and
  the two domain axes; the construction is a separate setup action.
- **`y`** — `Field[N_nd]` — the input Nedelec field to project. Read-only at L3
  (value-threaded positionally; the L3 layer has no in-place mutation in vocabulary —
  mutation reappears only in the L1>L0 lowering). Element type `Vector` (real) or
  `ComplexVector` (complex).
- **result** — `Field[N_nd]` — the divergence-free component of `y`, satisfying the
  discrete divergence-free condition `Gᵀ M y' = 0` up to the inner `ksp` convergence
  tolerance on the non-essential dofs. A fresh value produced by the gate; no L0
  destination buffer is mentioned at L3 (the destination-binding rotation is an L1>L0
  concern). Same Nedelec axis `N_nd`.

`Z_S : Field[N_h1] -> Field[N_h1]` is the zero-on-subset operator
`(Z_S z)_i = 0 if i ∈ S else z_i` (the
[`set_subvector_zero`](../concepts/set_subvector_zero.md) primitive); `K⁻¹` denotes
the **opaque inner [`ksp_solve`](./ksp_solve.md)** of `P.M · ψ = rhs`, **not** exact
inversion and **not** spelled out at this entry's resolution.

`DivFreeProjector[N_nd, N_h1]` is an **opaque constructed type** at L3: its internal
representation (real vs. complex operators; the inner CG solver, already a
construction-bound gate; the empty-boundary synthetic single-dof pin) is not part of
the L3 signature. The setup that builds `DivFreeProjector[N_nd, N_h1]` from the FE
spaces and material coefficients (`palace/linalg/divfree.cpp:43-152`) is a separate
setup action (mirroring the L0 construction / `Mult` split); it is authoritative at
the L1 entry and is not re-derived here. The L3 entry reads the apply, not the setup.

No L4 wrapper machinery is present at L3, mirroring the firm `apply_linop` /
`ksp_solve` / `jacobi-smoother` L3 discipline:

1. **No `Solve` monad.** `divfree_project` is pure functional at L3; no `do`-block,
   no `modify`, no monadic effect *at the projector level*. (The inner `ksp_solve` has
   its own outer-driver structure, but that is interior to the `ksp_solve` gate, not
   surfaced here.) The apply consumes `y` and produces a fresh output; there is no
   `SimState` thread at the projector resolution.
2. **No `readonly` typing.** The L4 calculus would mark the `P` argument as `readonly`
   (the closure is never written through at apply time — the L0 `Mult` mutates only the
   field argument and the construction-bound scratch buffers `psi` / `rhs`, never the
   operators); at L3 this is a documented invariant (the L3 vocabulary has no `readonly`
   annotation; `P.M` / `P.WeakDiv` / `P.Grad` / `P.ksp` are read, never written).
3. **No element-loop exposure.** The L3 form's "no element loop visible at the layer"
   property is structural — each of the four steps is a whole-tensor field operation
   (two operator applies, one subvector-zeroing, one inner solve), never an iteration
   over the length axes `N_nd` / `N_h1` at the projector's resolution. This is what
   makes the gate L3-native by signature shape, the same property the firm L3
   `ksp_solve` / `jacobi-smoother` / `apply_linop` cohort inherits.

## Semantics

`divfree_project P y` realizes the **discrete Helmholtz decomposition** of a Nedelec
field: any `y ∈ Field[N_nd]` decomposes as `y = y_divfree + Grad·ψ`, where `Grad·ψ`
is the irrotational (gradient-range) part and `y_divfree` is the divergence-free
remainder satisfying `Gᵀ M y_divfree = 0` (`palace/linalg/divfree.hpp:28-31`). The
gate returns `y_divfree`. The result is determined entirely by `P` and `y` — no
hidden state, no per-call side effects, no in-place mutation at the L3 surface. The
L3 form is **pure functional** (the same `P` applied to the same `y` returns the same
`Field[N_nd]` value, modulo the inner-solve tolerance and the inherited reduction-tree
non-determinism).

The apply is a **fixed four-step straight-line composition**
(`palace/linalg/divfree.cpp:155-187`), in dataflow order:

1. **Weak divergence** `rhs ← P.WeakDiv · y` — an `apply_linop`-shaped whole-tensor
   linear-operator apply computing the H1-side residual measuring the divergence of
   `y` (`palace/linalg/divfree.cpp:159-168`; the complex Re/Im branches at `:162-163`,
   the real branch at `:167`).
2. **Essential-BC zeroing** `rhs ← Z_{P.bdr_eff}(rhs)` — the `set_subvector_zero`
   primitive zeroing the residual on the essential boundary dofs
   (`palace/linalg/divfree.cpp:171-174`).
3. **Projected H1 solve** `ψ ← K⁻¹ rhs`, i.e. the **opaque inner
   [`ksp_solve`](./ksp_solve.md)** of `P.M · ψ = rhs` via `P.ksp`
   (`palace/linalg/divfree.cpp:175`, `ksp->Mult(rhs, psi)`). **This is the only step
   carrying an iteration, and that iteration is interior to the `ksp_solve` gate** (see
   §"Iteration-rotation marker"). At this entry's resolution it is a single opaque
   field-to-field action.
4. **Gradient correction** `y' ← y + P.Grad · ψ` — an `apply_linop`-shaped apply
   fused with an `axpy`-shaped accumulate (`palace/linalg/divfree.cpp:177-186`, via
   `Grad->AddMult(ψ, y, 1.0)`; the complex Re/Im branches at `:180-181`, the real
   branch at `:185`).

The mathematical projector is `P = I − Grad (Gᵀ M G)⁻¹ Gᵀ M` (the M-orthogonal
projection onto the divergence-free subspace). The **sign convention** of `WeakDiv`
(it absorbs the negating `-1.0` of the weak-divergence form,
`palace/fem/integ/mixedvecgrad.cpp:202`) makes the correction *additive*
(`y + Grad·ψ`, not `y − Grad·ψ`) while the net effect *removes* the gradient part —
this is a load-bearing non-law carried unchanged from L1 (see Algebraic laws). The
triple product `Gᵀ M G` is never materialized; the system passed to the inner solve is
`P.M` itself, with `Gᵀ` realized by `P.WeakDiv` on the RHS side and `G` by `P.Grad`
on the correction side.

The complex specialization is the same projection applied component-wise to `Re(y)`
and `Im(y)` with the same real-valued operators (`palace/linalg/divfree.cpp:159-184`);
the inner `ksp` step is a single solve on the `ComplexOperator`-typed system whose CG
recursion is component-blind. There is no cross-coupling between the real and imaginary
parts through the projection.

### Iteration-rotation marker

L3 is the iteration-rotation layer. **`divfree_project`'s four-step apply lifts as a
fixed whole-tensor composition** — three leaf field operations (`WeakDiv·y`,
`Z_{bdr_eff}`, `Grad·ψ`) around one inner-gate invocation — and the L1 form's
`(DivFreeProjector[N_nd, N_h1], Field[N_nd]) -> Field[N_nd]` signature is
identity-in-form to the L3 form. **The gate authors NO iteration obstruction of its
own**: the projector body has no convergence loop, no recurrence, no sweep at the
projector's resolution; it is a straight-line dataflow of four steps.

But — and this is the sharp distinction from the thinnest gate `jacobi-smoother`
(which carries **no** obstruction of any kind because its apply is one elementwise
product) — `divfree_project` carries a `sequential-obstruction` **by reference**. Step
3 is the inner [`ksp_solve`](./ksp_solve.md) (`palace/linalg/divfree.cpp:175`), whose
**outer convergence-test fold is itself a `sequential-obstruction`** (the canonical
outer-loop obstruction documented at the firm `ksp_solve` L3 entry and the
[`sequential-obstruction`](../concepts/sequential-obstruction.md) concept). The gate:

- does **not introduce a new** obstruction — its own four-step body is a fixed
  composition with no projector-level loop; and
- does **not erase** the inner obstruction — the CG iteration interior to `P.ksp`
  remains an un-lifting fold.

This is exactly the [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md)
**fidelity rule** at L3: the inner gate's iteration stays interior to `ksp_solve`'s own
L3 entry; at this entry's resolution `P.ksp->Mult(rhs, psi)` is an opaque field-to-field
action. In obstruction-profile terms `divfree_projector` is an **obstruction-carrying**
gate (with `ksp_solve`, `eigsolve`) rather than an obstruction-free leaf (`jacobi-smoother`,
`apply_linop`, `dot`, `scal`) — but it carries its obstruction *by composition*, not by
authoring an outer loop. `ksp_solve` authors its own fold; `eigsolve` delegates to an
opaque library loop; `divfree_projector` delegates to its inner `ksp_solve` gate. The
three are the obstruction-carrying constructed-operator gates at L3, distinguished by
*whose* loop carries the obstruction.

## Algebraic laws

The five laws that hold at L1 transport unchanged to L3, because the
constructed-operator-gate apply is identity-in-form across the L3→L1 hop. The two
load-bearing non-laws also transport unchanged. The laws are reproduced here so the L3
reader does not have to reach to L1 for the listing; the L1 entry
(`book/src/L1/divfree_projector.md` §Algebraic laws) is authoritative on every factual
claim about the Palace surface.

1. **Linearity.** `divfree_project P (α·u + β·v) = α · divfree_project P u + β · divfree_project P v`.
   Each of the four steps is linear (`WeakDiv`, `Z`, `Grad` are linear operators; the
   inner `ksp_solve` is a linear solve), and vector addition is linear
   (`palace/linalg/divfree.cpp:159-184`). Holds exactly in exact arithmetic; modulo the
   inner `ksp` tolerance under the approximate solve.

2. **Idempotence (projector law).** `divfree_project P (divfree_project P y) = divfree_project P y`
   in exact arithmetic: applying the projector to an already-divergence-free field
   returns it unchanged. By the defining condition `Gᵀ M (P·y) = 0`
   (`palace/linalg/divfree.hpp:28-31`), `P·y` lies in the divergence-free subspace, so
   `WeakDiv·(P·y) = 0` (step 1 yields zero residual), hence the correction `Grad·ψ = 0`
   and `P·(P·y) = P·y`. Holds modulo the inner `ksp` tolerance.

3. **Range.** `Range(divfree_project P ·) = {x ∈ Field[N_nd] : Gᵀ M x = 0}` — the
   discrete divergence-free subspace (`palace/linalg/divfree.hpp:28-31`).

4. **M-orthogonality (kernel = gradient range).** `Ker(divfree_project P ·) = Range(P.Grad)`:
   the removed component is the irrotational (gradient) part, and the projection is
   orthogonal in the M-inner-product (the projected H1 problem `P.M·ψ = rhs` encodes the
   M-weighted normal equations `Gᵀ M G ψ = Gᵀ M y`). `P.M` is SPD by construction
   (`palace/linalg/divfree.cpp:119`), making the M-inner-product well-defined.

5. **Real-linearity / block-diagonal complex action.** For `ComplexVector`,
   `divfree_project P (u + i·v) = (divfree_project P u) + i·(divfree_project P v)` where
   the operators are real-valued, so the action is block-diagonal over `{Re, Im}`
   (`palace/linalg/divfree.cpp:159-184`).

Laws that explicitly **do not** hold (inherited unchanged from L1, both load-bearing):

- **Sign convention (additive correction).** The correction is *additive*
  (`y + Grad·ψ`) because `WeakDiv` (built from `MixedVectorWeakDivergenceIntegrator`)
  internally absorbs the minus sign of the weak-divergence form: its bilinear form is
  `a(u,v) = -(ε u, ∇v)` (`palace/fem/integrator.hpp:217`), the `-1.0` materialized at
  `palace/fem/integ/mixedvecgrad.cpp:202` (versus the non-negated
  `MixedVectorGradientIntegrator`, `palace/fem/integ/mixedvecgrad.cpp:142`). A flipped
  L0 sign would invert the correction direction. Property of the constructed `WeakDiv`
  operator, honoured verbatim at L3 and positively re-derived from Palace source.

- **Step ordering.** The essential-BC zeroing `Z_{bdr_eff}` must compose *after*
  `WeakDiv·y` and *before* the inner `ksp_solve` (`palace/linalg/divfree.cpp:159-175`).
  Reordering changes the result; the sequence `WeakDiv → Z → ksp_solve → Grad` is
  load-bearing. This is the projector body's only ordering constraint; it is a
  straight-line dataflow dependency, **not** a sequential iteration obstruction (the
  obstruction lives inside step 3's `ksp_solve`, by reference).

The non-law set is **inherited unchanged** from L1; the L3 rendering introduces no new
non-laws. This is what makes the L3>L1 hop identity-in-form on the gate's apply: the
entire algebraic profile (laws + non-laws) transports unchanged. The inner-solve
`sequential-obstruction` is **not** an algebraic non-law of this gate — it is a property
of the inner `ksp_solve` carried by reference (§"Iteration-rotation marker").

## Dependencies

**Same-layer (L3)**:

- [`ksp_solve`](./ksp_solve.md) — the inner projected H1 solve `P.M · ψ = rhs` (step 3,
  `palace/linalg/divfree.cpp:175`). **Direct, load-bearing dependency**: this is the
  nested-constructed-operator gate's inner gate. `divfree_projector`'s closure carries
  `P.ksp : Solver[P.M]` as a sub-field; the per-call body invokes it opaquely. The CG
  iteration internal to `ksp_solve` is the standard outer-loop `sequential-obstruction`;
  it is interior to `ksp_solve` and **does not leak** into `divfree_projector` (the
  fidelity rule). This is the structural fact that makes `divfree_projector`
  obstruction-carrying-by-reference rather than obstruction-free.
- [`apply_linop`](./apply_linop.md) — the `P.WeakDiv·y` (step 1) and `P.Grad·ψ` (step 4)
  whole-tensor linear-operator applications.
- [`axpy`](./linear_combination.md#arity-specializations) — the `y + Grad·ψ` gradient-correction accumulate (step 4, fused as
  `Grad->AddMult(ψ, y, 1.0)`, the apply-and-accumulate idiom).

**Cross-cutting concepts**:

- [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md) —
  the structural shape this entry instantiates at L3: the closure `P` carries the inner
  gate `P.ksp`. The firm-instances list names `divfree_projector` (one nested gate) and
  the transitive chain `eigsolve ⊃ divfree_projector ⊃ ksp_solve`. The fidelity rule
  (inner iteration stays interior to the inner gate) is the discipline this L3 entry
  follows.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the canonical
  write-up of the outer-loop obstruction this gate carries **by reference** through its
  inner `ksp_solve`.
- [`set_subvector_zero`](../concepts/set_subvector_zero.md) — the `Z_{bdr_eff}`
  essential-BC zeroing (step 2).
- [`constructed-operators`](../concepts/constructed-operators.md) /
  [`variant-absorption`](../concepts/variant-absorption.md) — the construction-time
  absorption of `M`, `WeakDiv`, `Grad`, `bdr_eff`, `ksp` into the opaque
  `DivFreeProjector` closure, and the element-type axis absorption.

The setup-side dependencies (the construction-time assembly of `M`, `WeakDiv`, `Grad`,
`bdr_eff`, and the inner `ksp` solver, `palace/linalg/divfree.cpp:43-152`) are
L1-entry concerns, not part of the L3 apply — they are consumed once at construction,
before the gate is folded into any L3 expression.

**L1 anchor**: [`L1/divfree_projector`](../L1/divfree_projector.md) (firm; the
constructed-operator gate at L1) — authoritative on the Palace-surface details, the
construction chain, the empty-boundary single-dof pin, the `WeakDiv` sign convention,
and the complete L0 evidence list. This L3 entry does not duplicate those details; the
L3>L1 rotation is identity-in-form on the gate's apply.

**Strawman reference**: `book/src/semantics/index.md` is the L4/L3 conventions
source; this L3 entry follows the strawman's Haskell `::` signature notation (rendered
as 4-space-indented code blocks here). The L4 layer does not surface
`divfree_projector` as a standalone entry (per the constructed-operator-gate L4 verdict
shared with the firm `apply_linop` / `ksp_solve` / `jacobi-smoother` gates).

## Variant axes

`divfree_project` has **one orthogonal variant axis at L3, plus the absorbed
operator-representation axis** — the same framing as L1
(`book/src/L1/divfree_projector.md`), transported unchanged. Both are absorbed into the
constructed-operator closure; neither appears in the per-call apply's positional
signature.

One orthogonal axis:

1. **element-type** (`Vector` real | `ComplexVector` complex) — collapsed into the
   opaque `DivFreeProjector[N_nd, N_h1]` closure. The L0 source instantiates both
   (`template class DivFreeSolver<Vector>;` / `<ComplexVector>;`,
   `palace/linalg/divfree.cpp:189-190`); the complex apply is the same real-valued
   operators applied component-wise to `Re(y)` and `Im(y)`
   (`palace/linalg/divfree.cpp:159-184`), with no cross-coupling. The apply is identical
   in form (the same four steps) across element types. At L3 the absorption is a
   documented invariant (no `readonly` typing).

Absorbed axis:

- **operator-representation** — the constructed `M` / `WeakDiv` / `Grad` operators (each
  with its own sparse / partially-assembled / interpolator representation), the
  `bdr_eff` dof-subset, and the **inner `ksp` solver** (itself a construction-bound gate
  with its own preconditioner / tolerance / iteration-cap absorption) are all built once
  at setup and collapsed into the opaque `DivFreeProjector` closure. By the time the gate
  is applied, the representation distinctions have been erased; the L3 apply sees only the
  projector-action interface. The L1 contract collapses this axis identically.

The variant-axis profile (one orthogonal + one absorbed) matches the L1 entry exactly.
**No new axes introduced by the L3 rendering; no axes merged or split.** (Note: the inner
`ksp_solve`'s own five loop-shaping variant axes — krylov-method, initial-guess-policy,
etc. — are interior to that gate, absorbed into `P.ksp` at construction; they are not
`divfree_projector` axes.)

## Caveats

The firm-on-positive-structure basis governs the absence of a
dedicated `test-divfree.cpp` under `reference/palace/test/unit/`: every L3 law is a
syntactic identity transported from the firm L1 entry, whose laws read off positive
source (the four-step apply at `palace/linalg/divfree.cpp:155-187`; the defining
condition at `palace/linalg/divfree.hpp:28-31`; the `WeakDiv` sign at
`palace/fem/integ/mixedvecgrad.cpp:202`) — not literature-inferred convergence claims —
so the missing dedicated test does not gate firm. The `WeakDiv` sign is cross-validated
against MFEM at `test/unit/test-libceed.cpp:905-916` (L0-equivalent coverage). Behaviour
is exercised through integration paths only — the eigensolver projection call sites
(`palace/drivers/eigensolver.cpp:260-262`; the per-iteration `opProj->Mult(...)` sites in
`arpack.cpp` / `slepc.cpp`).

Caveats (not status reductions):

- The inner `ksp_solve`'s outer-loop `sequential-obstruction` is carried by reference;
  it is **not** an algebraic non-law of this gate. The projector's own apply is a fixed
  straight-line four-step composition with no projector-level loop. The obstruction's home
  is the firm `ksp_solve` L3 entry; this gate composes against it (the fidelity rule),
  neither introducing nor erasing it.
- The `Mult` class doc comment `palace/linalg/divfree.hpp:64-66` describing the output as
  "the irrotational portion ... satisfying ∇ × y = 0" is stale/misleading relative to the
  implemented divergence-free behaviour (a Palace-internal documentation inconsistency, OQ
  `divfree-mult-doc-irrotational-vs-divfree-stale`, inherited from the L1 entry); the
  implemented and L3 semantics are the divergence-free target of the class doc
  `palace/linalg/divfree.hpp:28-31`.

## Lowers to

L3 `divfree_projector` lowers to the adjacent L2 floor
[`divfree_projector`](../L2/divfree_projector.md) and onward to L1
[`divfree_projector`](../L1/divfree_projector.md) — **no non-adjacent L3-L1 directory**.
The L3>L2 rotation is a **degenerate identity-in-named-terms lowering**, annotated in-line
here rather than as a dedicated L3>L2 theme file: L1, L2, and L3 all see
`divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]`
with the same shape contract, the same five algebraic laws, the same two-non-law set, and
the same one-orthogonal-plus-one-absorbed variant profile. The four-step composition
`WeakDiv → Z_{bdr_eff} → ksp_solve → Grad` is explicit and value-thread-isomorphic at BOTH
L3 and L2 — no vocabulary shift across the edge to rotate. The L3>L2 hop passes through the adjacent floor
rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.
**The ONE genuine fusion rotation in the projector chain lives on the L2>L1 edge, not this
one**: the step-4 `Grad->AddMult` apply-accumulate (`palace/linalg/divfree.cpp:185` real /
`:180-181` complex) de-fuses at L2 into `apply_linop(P.Grad, ψ) ▷ axpy` and re-fuses at L1,
captured by the firm theme
[`divfree-projector-leaf-identity`](../L2-L1/divfree-projector-leaf-identity.md) — reachable
directly from this L3 entry via the live link above (not via the L2 floor, which carries no
live link to the kept theme). The L3>L2 hop is a layer-coherence
identity (each layer is coherent within itself), not an algebraic one; the transitive L3>L1
identity is annotated in-line here (precedent: the firm L3 `jacobi-smoother` / `apply_linop`
/ `dot` / `scal` cohort, all of which note their identity rotations in-line; the
non-adjacent-identity convention).

The **substantive** rotation in the chain is the L1>L0 leaf-mutation rotation, not the
L3>L1 hop: the four-step apply lowers to Palace's in-place `Mult(VecType &y)` mutation
idiom (the destination field `y` mutated through `WeakDiv->Mult` / `SetSubVector` /
`ksp->Mult` / `Grad->AddMult`, with the construction-bound `psi` / `rhs` scratch buffers),
captured by the firm L1>L0 theme
[`divfree-projector-mutation-rotation`](../L1-L0/divfree-projector-mutation-rotation.md).
That theme's inner `ksp->Mult` step delegates to the firm
[`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md) theme per the
nested-constructed-operator-gate fidelity rule (the inner CG loop is the inner theme's
concern). None of that destination-binding / inner-loop content is L3 content; the L3 form
sees a fixed four-step whole-tensor composition with the inner solve opaque.

## Lifts from

**`divfree_projector` has no standalone L4 entry.** Like the firm `apply_linop` /
`ksp_solve` / `jacobi-smoother` constructed-operator gates, the projector apply authors
no monadic effect of its own, no state-stratification typing, and no outer-driver
structure — its body is a fixed four-step composition delegating its only iteration to the
inner `ksp_solve` gate. First-class L4 vocabulary carries one of (a) monadic effect, (b)
state-stratification typing, or (c) outer-driver structure; the projector gate authors
none of its own (the inner `ksp_solve`'s outer-driver structure is *that* gate's
territory, not the projector's). Promoting it to a standalone L4 entry would over-promote
a fixed-composition constructed-operator action and add no calculus content.

The L3 form is value-thread-isomorphic to the firm L1 form on the gate's apply; the entry
exists for layer-coherence reasons — a reader navigating L3 (whose index advertises
whole-tensor field operations and constructed-operator gates as L3 vocabulary) must find
`divfree_projector` defined in L3 vocabulary, not have to reach down to L1 to recover the
constructed-operator-gate apply. The firm L3 `krylov_step` backfill is the
structural precedent for the constructed-operator-shaped layer-coherence backfill; the
firm L3 `ksp_solve` and `jacobi-smoother` are the
constructed-operator-gate siblings — `ksp_solve` the obstruction-authoring inner gate this
projector delegates to, `jacobi-smoother` the obstruction-free contrast.

## Evidence

The L3 form is value-thread-isomorphic to the firm L1 form (per the identity-in-form
rotation on the constructed-operator-gate apply); all L0 evidence is transitive through
L1. Direct citations relevant to this L3 entry:

- `book/src/L1/divfree_projector.md` (firm) — the L1 entry whose signature, semantics,
  five algebraic laws, two non-laws, one-orthogonal-plus-one-absorbed variant profile, and
  complete L0 evidence list are transported unchanged to L3. Authoritative on every
  Palace-surface factual claim.
- `book/src/L3/index.md:46` — the L3-cohort-growth audit verdict
  naming `divfree_projector` as one of the six (A) firm identity-in-form L3 backfill
  candidates ("constructed-operator gate, like firm-L3 `ksp_solve`").
- `palace/linalg/divfree.cpp:155-187` — `DivFreeSolver<VecType>::Mult(VecType &y)`: the
  four-step apply the L3 whole-tensor composition lowers to. Step 1 `WeakDiv->Mult`
  (`:159-168`, complex Re/Im at `:162-163`, real at `:167`); step 2 `SetSubVector` zeroing
  (`:171-174`); step 3 the inner `ksp->Mult(rhs, psi)` (`:175`); step 4 `Grad->AddMult`
  (`:177-186`, complex at `:180-181`, real at `:185`).
- `palace/linalg/divfree.cpp:175` — `ksp->Mult(rhs, psi);` — the opaque inner
  [`ksp_solve`](./ksp_solve.md) action (step 3); the nested-gate inner-solve invocation
  carrying the `sequential-obstruction` by reference.
- `palace/linalg/divfree.cpp:43-152` — the construction body building `M`, `WeakDiv`,
  `Grad`, `bdr_eff`, and the inner `ksp` solver into the opaque `DivFreeProjector` closure
  (setup, not L3 apply content; the `ksp` setup at `:121-149`).
- `palace/linalg/divfree.cpp:189-190` — `template class DivFreeSolver<Vector>;` /
  `<ComplexVector>;` — the element-type variant axis instantiation.
- `palace/linalg/divfree.hpp:28-31` — class doc: the defining divergence-free condition
  `Gᵀ M x = 0`, the range, and the kernel (gradient nullspace). The source of laws 2/3/4.
- `palace/linalg/divfree.cpp:119` — `// ... real and SPD.` — `P.M` SPD, justifying the
  M-inner-product / M-orthogonality (law 4).
- `palace/fem/integrator.hpp:217` + `palace/fem/integ/mixedvecgrad.cpp:202` (the `-1.0`)
  vs `:142` (non-negated sibling) — the `WeakDiv` sign-convention non-law, positively
  anchored, inherited unchanged from L1.
- `palace/drivers/eigensolver.cpp:260-262` — the `divfree->Mult(v0)` initial-vector
  projection call site (the integration-path behaviour exercise).
- `book/src/L1-L0/divfree-projector-mutation-rotation.md` (firm) — the L1>L0 leaf-mutation
  rotation the four-step apply lowers through (the substantive rotation in the chain; not
  L3 content; its inner-solve step delegates to `ksp-solve-mutation-rotation` per the
  fidelity rule).
- `book/src/concepts/nested-constructed-operator-gate.md` (firm) — the concept this entry
  instantiates at L3; the firm-instances list names `divfree_projector` (one nested gate)
  and the transitive chain `eigsolve ⊃ divfree_projector ⊃ ksp_solve`; the fidelity rule
  this entry follows.
- `book/src/L3/ksp_solve.md` (firm) — the inner gate this projector delegates to;
  the home of the carried `sequential-obstruction`.
- `book/src/L3/jacobi-smoother.md` (firm), `book/src/L3/krylov_step.md` (firm),
  `book/src/L3/apply_linop.md` (firm) — the L3 identity-in-form /
  constructed-operator-gate backfill precedents this entry follows; `jacobi-smoother` the
  obstruction-free contrast.

## L3 vs L4 distinction

- **L4**: no standalone `divfree_projector` entry. A projector action that delegates its
  only iteration to an inner solve carries no monadic effect, no typed records, no
  outer-driver structure of its own; if it appeared at L4 it would be a let-binding
  consuming a constructed projector (which itself consumes a constructed solver), not
  first-class L4 vocabulary. The constructed-operator-gate L4 verdict is shared with the
  firm `apply_linop` / `ksp_solve` / `jacobi-smoother` gates.
- **L3**: standalone entry (this file). Positional value-threading: `divfree_project P y =
  y + P.Grad · K⁻¹( Z_{P.bdr_eff}( P.WeakDiv · y ) )`. No monadic effect, no typed records,
  no `readonly` typing, no `do`-block at the projector level. The gate's apply is a fixed
  four-step whole-tensor composition with the operator-representation, inner-solver, and
  element-type axes absorbed into the opaque closure.

## L3 vs L1 distinction

- **L1**: constructed-operator gate as a pure-functional projection — the mutation-rotated
  form of the L0 `DivFreeSolver<VecType>::Mult(VecType &y)` in-place mutation idiom (the
  destination field dropped from the signature; the construction-bound `psi` / `rhs`
  scratch absorbed; the element-type collapsed into the closure). The L1 vocabulary frames
  the gate against the L0 source.
- **L3**: constructed-operator gate as a whole-tensor field operation — one of the
  iteration-rotation layer's gates (alongside `ksp_solve`, `eigsolve`, `jacobi-smoother`),
  specifically an **obstruction-carrying-by-reference** gate: its four-step apply authors
  no obstruction of its own, but its inner `ksp_solve` carries a `sequential-obstruction`
  the gate neither introduces nor erases. **The gate's apply is identity-in-form to L1** —
  no change in shape, no change in algebraic laws, no change in variant axes. The L3 entry
  exists for layer-coherence: a reader at L3 finds the gate defined in L3 vocabulary,
  without having to drop down to L1.

The two layers' entries share signature, algebraic laws (five), non-laws (two),
variant-axis profile (one orthogonal + one absorbed), and the cited L0 evidence
(transitive). They differ in **layer interpretation**: L1 frames the gate as the
mutation-rotated form of the L0 `Mult` virtual; L3 frames it as an obstruction-carrying
constructed-operator gate at the iteration-rotation layer, distinguished from the
obstruction-free `jacobi-smoother` by its inner-solve delegation. The two framings are
complementary, and the layer-coherence invariant (CLAUDE.md §Methodology invariants
"Identity-lowerings still require both L levels") requires both entries to exist.
