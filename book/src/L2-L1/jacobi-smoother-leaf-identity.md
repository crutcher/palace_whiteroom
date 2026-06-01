# jacobi-smoother-leaf-identity

The L2>L1 lowering theme for the constructed-operator gate `jacobi-smoother`. The rewrite is
**identity-in-form on the gate**: the L2 [`jacobi-smoother`](../L2/jacobi-smoother.md) floor lowers
to the L1 [`jacobi-smoother`](../L1/jacobi-smoother.md) gate with the same signature, the same
single-elementwise-product apply, the same six algebraic laws, and the same three non-laws —
value-thread-isomorphic on the gate's apply. The L2 layer's defining fusion-rotation work
(de-fusing Palace's fused multi-operation kernels) is **not present on this gate**: the genuine
fusion observation is **negative** — the Jacobi apply is one elementwise product with **no fused
multi-operation kernel to unfold** — so the L2>L1 edge is the identity with the fusion treatment a
documented no-op. This is the **constructed-operator-gate analogue** of the BLAS-1-leaf
[`dot-leaf-identity`](./dot-leaf-identity.md) (identity-in-form on a single leaf, all L2-layer
fusion absent / deferred), differing only in that `jacobi-smoother` has **no fold-parent** to defer
to (it is a standalone gate, not a member of any fold cohort). The slug is `-leaf-identity` (NOT
`-fold-specialization`): the edge is an identity-leaf-lowering, not a fold→leaf dispatch.

## Slug

`jacobi-smoother-leaf-identity`

## Context

`jacobi-smoother` at L2 is the **constructed-operator-gate floor** entry
(`book/src/L2/jacobi-smoother.md`, harvested cycle-042 D5): the thinnest such gate, rendered as its
own same-named L2 chapter so the firm L3 [`jacobi-smoother`](../L3/jacobi-smoother.md) (cycle-037)
rests on an adjacent same-named L2 parent (per CLAUDE.md §Methodology invariants **Identity-lowerings
still require both L levels**) rather than skipping a layer to L1. This theme is the L2>L1 edge of
that floor — the lower of the two thin-identity edges the D5 floor introduces, the upper being the
co-dispatched L3>L2 [`jacobi-smoother-body-identity`](../L3-L2/jacobi-smoother-body-identity.md).

The edge is the **identity-in-form** case: the L2 `jacobi-smoother` gate and the L1
`jacobi-smoother` gate are value-thread-isomorphic on the apply. This is the L2>L1 analogue of the
L3>L2 [`jacobi-smoother-body-identity`](../L3-L2/jacobi-smoother-body-identity.md) (the upper thin
edge of the same gate), and a sibling shape to the firm
[`dot-leaf-identity`](./dot-leaf-identity.md) (identity-in-form on a single BLAS-1 leaf) — except
here the identity is on a *constructed-operator gate* (whose argument `op` is an opaque closure
built once at setup), and there is no fold-parent at all.

**Why this edge is identity, and why there is no fusion to defer.** The L2 layer's defining work
is kernel-fusion de-fusion — unfolding fused multi-operation kernels into compositions of base
primitives. For the inner-product cohort the `dot` leaf defers that work to the fold-parent
[`inner-product-fold-specialization`](./inner-product-fold-specialization.md) (the
`dot-leaf-identity` "fusion deferral" note); for `jacobi-smoother` **there is no fusion to defer at
all**. The L0 apply kernel (`palace/linalg/jacobi.cpp:30-39` real; `:41-70` complex) is a single
`mfem::forall_switch` computing `Y[i] = DI[i] * X[i]` (real) or the four-multiply componentwise
complex product (`:52-60`); there is no fusion of *distinct algebraic operations* (no `α·x + β·y`
pass, no fused residual-and-direction update) — only one elementwise product. The complex
four-multiply form is a *single* elementwise complex product (the base-algebra realisation of
componentwise `ℂ` multiplication), **not** a fused composition of separable L2 primitives. The L2
floor's §"Negative fusion observation" records this as the entry's genuine — and *negative* —
fusion-rotation fact: the L2 form is identical to the L1 form because there is nothing to de-fuse.
So this theme's edge is the identity, with the fusion treatment a documented no-op rather than a
deferral to a fold-parent.

## L2 form (LHS)

The L2 form is the `jacobi-smoother` constructed-operator-gate floor
(`book/src/L2/jacobi-smoother.md` §Signature, harvested cycle-042 D5) — the mutation-free
single-elementwise-product apply over an opaque constructed closure:

    jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]
    jacobi_smoother op x = op.dinv ⊙ x
                         = (ω · diag(A)⁻¹) ⊙ x

with the constructed-operator closure `op : JacobiSmoother[N]` carrying `op.dinv` (the damped
inverse diagonal `ω · diag(A)⁻¹`, same element-type as the operator), `op.omega` (already absorbed
into `dinv` at apply time), and `op.sf_max` (consumed only by the estimated-damping setup). The L2
form is **pure / out-of-place** (no destination buffer; the result is a fresh `Tensor[N]`). The
constructed-operator type is opaque at L2: the element-type variant (real / complex `dinv`) and
the operator-representation axis are absorbed into the closure, with the per-element kernel
dispatching on element type. The **negative fusion observation** is the L2 layer's only
contribution here — there is no fused multi-operation kernel to unfold (the apply is one
elementwise product). The in-place L0 output-arg mutation idiom (`Mult(x, y)` writes through `y`)
and the `mfem::forall_switch` element-loop are NOT in the L2 signature — they reappear only at the
L1>L0 lowering (`book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` sub-pattern B
+ `book/src/L1-L0/jacobi-smoother-mutation-rotation.md`).

## L1 form (RHS)

The L1 form is the firm `jacobi-smoother` constructed-operator gate
(`book/src/L1/jacobi-smoother.md` §Signature, firm) — identical in signature, semantics, and laws:

    jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]
    jacobi_smoother op x = op.dinv ⊙ x
                         = (ω · diag(A)⁻¹) ⊙ x

The L1 gate is the **mutation-rotation** rendering: it already erases the L0 destination buffer `y`
(dropped from the signature; the smoother consumes `x` and produces a fresh output), drops the
`initial_guess` parameter as a precondition (the `Mult` body asserts `!this->initial_guess`,
`palace/linalg/jacobi.cpp:102`), and collapses the element-type and damping-mode axes into the
opaque closure. The setup that builds `JacobiSmoother[N]` from `(A, omega, sf_max)` — the
`assemble_diagonal → reciprocal → ω-fold` chain plus the opaque `spectrum_estimate` sub-action on
the `ω = 0` path — is authoritative at the L1 entry (`book/src/L1/jacobi-smoother.md` §Signature)
and is not duplicated here. The L1 entry is authoritative on every Palace-surface fact; the L2 form
does not duplicate them.

## The rewrite (L2 → L1)

The rewrite is the **identity on the gate**. Every L2 binding maps to the same L1 binding at the
same position:

| L2 gate (`L2/jacobi-smoother`) | L1 gate (`L1/jacobi-smoother`) | Mapping |
|---|---|---|
| `jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]` | same signature | Identity. Same signature shape; same opaque constructed-operator closure `op`. |
| `jacobi_smoother op x = op.dinv ⊙ x` (single elementwise product) | same apply | Identity. Same single elementwise-product field operation; same `(ω · D⁻¹) ⊙ x` body. |
| element-type / damping-mode / operator-representation axes absorbed into `op` | same absorption | Identity. The two orthogonal + one absorbed variant profile transports unchanged. |
| six algebraic laws + three non-laws | six laws + three non-laws | Identity. Inherited unchanged (linearity, zero-vector annihilation, `assemble_diagonal` round-trip, damping absorption, estimated-damping degenerate case, self-transpose; plus the dead-code Hermitian-transpose / no-iteration / bit-determinism non-laws). |

There is **no L2 binding without an L1 partner and no L1 binding without an L2 partner**; the
mapping is total and bijective on the gate. This is the identity-in-form property.

**The one note (negative fusion — NOT a fold deferral).** The L2 layer's defining work is
kernel-fusion de-fusion. For the inner-product cohort, `dot-leaf-identity` *defers* that work to the
fold-parent `inner-product-fold-specialization`. For `jacobi-smoother` there is **nothing to defer**:
the apply has no fused multi-operation kernel (the §"Negative fusion observation" in
`L2/jacobi-smoother.md`). The single real-elementwise kernel `Y[i] = DI[i] * X[i]`
(`palace/linalg/jacobi.cpp:38`) and the single complex four-multiply componentwise product
(`palace/linalg/jacobi.cpp:52-60`) are each *one* elementwise product, not a fused composition of
separable L2 primitives. So this theme's edge is the identity, and there is no fusion content to
read off a fold-parent (there is no fold-parent). The **substantive** rotation in the whole chain is
the L1>L0 leaf-mutation rotation — the apply's single elementwise product lowering to Palace's
in-place `mfem::forall_switch` element-loop writing through `y` — captured by the firm
[`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
(sub-pattern B) and [`jacobi-smoother-mutation-rotation`](../L1-L0/jacobi-smoother-mutation-rotation.md);
none of that destination-binding content is L2 content.

## Applicability conditions

The identity rewrite is valid when:

1. **The L2 `jacobi-smoother` is the constructed-operator-gate floor realization**
   (`book/src/L2/jacobi-smoother.md`, the same-named gate floor) — the unconditional floor under
   the firm L3 entry. Unlike the cycle-041 `dot-leaf-identity` (whose LHS presupposes the wave-1 D1
   same-named-leaf-floor realization and would dissolve into `inner-product-fold-specialization`
   under the (a) fold-only reading), this theme's LHS carries **no design-presupposition gate**:
   `jacobi-smoother` is a standalone constructed-operator gate with **no fold-parent**, so the
   cycle-041 `dot-l2-leaf-floor-vs-fold-only-design` leaf-vs-fold fork does **not** reach it. The L2
   floor is unconditional regardless of how that fork resolves.

2. **The gate is value-thread-isomorphic across the edge.** The L2 `jacobi-smoother` gate and the
   L1 `jacobi-smoother` gate share the signature, the single-elementwise-product apply, the opaque
   constructed-operator closure, the six algebraic laws, the three non-laws, and the
   two-orthogonal-plus-one-absorbed variant profile. Confirmed by construction: `L2/jacobi-smoother`
   is authored as a thin floor entry whose laws are inherited unchanged from `L1/jacobi-smoother`
   (D5 §Algebraic laws, §Signature).

3. **There is no fusion to de-fuse (negative fusion observation).** No fused multi-operation kernel
   exists in the Jacobi apply; the apply is one elementwise product. The L2 fusion-rotation work is
   therefore a documented no-op, not a deferral to a fold-parent (there is none). Confirmed by the
   D5 §"Negative fusion observation".

If a future L2 `jacobi-smoother` variant introduced a fused multi-operation kernel (e.g. a fused
residual-and-apply pass), the identity claim would need re-audit — none exists in the current
surface.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: the L2 `jacobi-smoother` gate's signature shape `(op: JacobiSmoother[N],
x: Tensor[N]) -> Tensor[N]` is identical to the L1 gate's signature shape — a whole-tensor field
operation (one elementwise product over an opaque constructed-operator closure) with no element
loop exposed at either layer and no fused kernel to de-fuse. The rotation between two
value-thread-isomorphic gates with identical signatures is the identity by construction; the only
L2-layer work (fusion de-fusion) is *absent* (negative fusion observation), leaving the gate's edge
a no-op.

**Empirical-match (secondary)**: the L1 gate is firm on direct Palace evidence
(`L1/jacobi-smoother` §Evidence, including the five consumer call sites — the principal Krylov
preconditioner slot `ksp.cpp:198-200`, the error-estimator estimated-damping site
`errorestimator.cpp:75-77`, and three default-damping consumers), and the L2 floor was authored
value-thread-isomorphic to it; the two forms agree on every law and every variant axis by
independent transcription. The identity is observational on the two existing firm/firming chapters,
not derivational.

## Speculative L1 operators

**None.** Both endpoints are existing vocabulary: the L2 LHS is the `jacobi-smoother` gate floor
(firm cycle-042 D5), the L1 RHS is the firm `jacobi-smoother` gate. This theme is the identity edge
between existing chapters; it proposes no new operators.

One forward-reference caveat carries over unchanged from the gate entries (NOT a status reduction —
the identity structure is firm):

- **No L2 `elementwise_product` / `reciprocal` floor exists yet.** The gate's apply body is one
  elementwise product `op.dinv ⊙ x`; at L2 (as at L1) it is a single base field operation below the
  layer's current resolution. Once the L2 `elementwise_product` floor lands (the D5 proposed plan
  item `l2-floor-elementwise-product-reciprocal`), the L2 LHS body would name
  `elementwise_product(op.dinv, x)` as a same-layer dependency; the identity edge maps it
  identity-in-form regardless (the L1 RHS would name the same dependency). The forward-reference is
  plain-text (no live link — target file does not exist).

## Verified-against

L2 / L1 anchors (the two endpoints):

- `book/src/L2/jacobi-smoother.md` (firm cycle-042 D5) — the L2 gate floor (LHS): the same-named
  constructed-operator-gate floor, value-thread-isomorphic to the L1 gate, laws inherited
  unchanged; the §"Negative fusion observation". (The chapter lands at this cycle's integration
  alongside this theme — wave-2 serial sequencing applies D5 before this theme.)
- `book/src/L1/jacobi-smoother.md` (firm) — the L1 gate (RHS): signature (`:56-59`), the
  single-elementwise-product apply, the setup chain, the six algebraic laws, the three non-laws,
  the complete L0 evidence list. Authoritative on every Palace-surface fact.
- `book/src/L2-L1/dot-leaf-identity.md` (firm cycle-041) — the BLAS-1-leaf precedent this theme
  follows in shape (identity-in-form on a single operation; `-leaf-identity` slug convention),
  differing only in that `dot-leaf-identity` *defers* its fusion to a fold-parent whereas
  `jacobi-smoother` has no fold-parent and no fusion to defer.

L0 evidence (transitive through the firm L1 gate; self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation; paths relative to `reference/palace/`):

- `palace/linalg/jacobi.cpp:38` — `Y[i] = DI[i] * X[i]` — the real elementwise-multiply kernel
  realising the apply (law 1 witness; the single elementwise product the L2 form is). **Self-verified
  (anchor `Y[i] = DI[i] * X[i]` @38).** Inherited transitively; the edge is identity so no new L0
  claim is made here.
- `palace/linalg/jacobi.cpp:52-60` — the complex forward-branch four-multiply componentwise complex
  product (a *single* elementwise complex product, not a fused composition — the negative fusion
  observation witness). Confirmed by direct read.
- `palace/linalg/jacobi.cpp:79-80` — `op.AssembleDiagonal(dinv); dinv.Reciprocal();` — the
  setup-side `assemble_diagonal → reciprocal` chain (L1-entry concern, not L2 apply content).
  **Self-verified (anchor `Reciprocal` @80).**
- `palace/linalg/jacobi.cpp:103` — `Apply(dinv, x, y);` — the single dispatch that is the entire
  per-call action. **Self-verified (anchor `Apply(dinv, x, y)` @103).**
- `palace/linalg/jacobi.hpp:43` — `void MultTranspose(...) const override { Mult(x, y); }` — the
  transpose self-alias (law 6) + the source of the dead-code Hermitian caveat. **Self-verified
  (anchor `Mult(x, y)` @43).**
- `palace/linalg/jacobi.cpp:61-69` — the complex `Apply<Transpose=true>` dead-code branch
  (conjugate-`dinv` apply); dead code under symmetric wiring (the non-law witness). Confirmed by
  direct read; inherited unchanged from L1.

## Status

`firm` — the L2 LHS is the firm-this-cycle gate floor (D5), the L1 RHS is the firm
`jacobi-smoother` gate, and the rotation between two value-thread-isomorphic gates with identical
signatures is the identity by construction (§"The rewrite (L2 → L1)" table is total and bijective on
the gate). The only L2-layer work — kernel-fusion de-fusion — is *absent* (the §"Negative fusion
observation": the apply is one elementwise product, no fused multi-operation kernel to unfold); this
theme has **no fold-parent** to defer fusion to (`jacobi-smoother` is a standalone gate), so the
edge is the identity with the fusion treatment a documented no-op. No speculative operator, no
negative-anchor reconstruction, no literature inference.

> **Fork-independence note (not a status reduction).** Unlike `dot-leaf-identity` (which
> presupposes the wave-1 D1 same-named leaf-floor realization of `L2/dot` and would re-anchor under
> the (a) fold-only reading — OQ `dot-l2-leaf-floor-vs-fold-only-design`), this theme carries **no
> design-presupposition gate**: `jacobi-smoother` is a standalone constructed-operator gate with no
> fold-parent on either codomain, so the cycle-041 leaf-vs-fold fork does not reach it. The L2 floor
> under it is unconditional regardless of how the batch-12 meta-phase resolves the BLAS-1 fork.

> **Forward-reference caveat (not a status reduction; inherited from the gate entries).** No L2
> `elementwise_product` / `reciprocal` floor exists yet; the apply is recorded as a single base
> field operation below the layer's current resolution (D5 proposed plan item
> `l2-floor-elementwise-product-reciprocal`). The identity edge maps it identity-in-form regardless.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L1 gate *up* to the L2 floor form is the value-thread-isomorphic identity rotation:
  the L1 signature has no fused kernel and no element loop exposed, which is exactly what makes it
  L2-native by construction (nothing to de-fuse). No additional structure is required for the lift.
  This reverse-direction note lives here in working notes per the high→low layer-definition
  discipline; the formal chapter narrates only L2 → L1.

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (the
  co-dispatched L3>L2 `jacobi-smoother-body-identity` identity ∘ this L2>L1 identity) is annotated
  in-line at the `jacobi-smoother` entries per the CLAUDE.md invariant "Identity rotations across
  non-adjacent layers are annotated in-line, not via a dedicated lowering directory" — no
  `book/src/L3-L1/` directory. This theme + the co-dispatched `jacobi-smoother-body-identity`
  compose to capture it.
