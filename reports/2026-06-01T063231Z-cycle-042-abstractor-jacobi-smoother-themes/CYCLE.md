---
agent: abstractor
invoked_at: 2026-06-01T063231Z
scope: TWO adjacent thin-identity lowering themes for jacobi-smoother — L2>L1 (jacobi-smoother-leaf-identity) + L3>L2 (jacobi-smoother-body-identity)
status: pending
inputs:
  - reports/2026-06-01T063231Z-cycle-042-harvester-L2-jacobi-smoother/CYCLE.md (wave-1 D5; the proposed L2/jacobi-smoother floor — SOURCE OF TRUTH for the L2 form; co-lands this cycle)
  - book/src/L1/jacobi-smoother.md (firm; the L1 constructed-operator gate — RHS of the L2>L1 theme)
  - book/src/L3/jacobi-smoother.md (firm cycle-037; the L3 iteration-rotation rendering — LHS of the L3>L2 theme)
  - book/src/L2-L1/dot-leaf-identity.md (firm cycle-041; the L2>L1 thin-identity precedent — `-leaf-identity` slug convention)
  - book/src/L3-L2/scal-body-identity.md (firm cycle-041; the L3>L2 thin-identity precedent — `-body-identity` slug convention)
  - L0 (transitive through L1): palace/linalg/jacobi.cpp:38 (real apply kernel), :61-69 (dead-code transpose branch), :79-80 (setup chain), :103 (Apply dispatch); jacobi.hpp:43 (transpose alias)
  - dispatch: cycle-042 D8 (wave-2; fork-INDEPENDENT, standalone constructed-operator gate, NO fold-parent; COUNT-OWNERSHIP deferred to D11)
integrated_at: 2026-06-01T081245Z
integration_commit: 1d6592a
integration_notes: "cycle-042 batch integration (foundation-first L2-floor build); applied clean; see reports/2026-06-01T081245Z-integrator-finalize-cycle-42/CYCLE.md + cycle-042 STAGING row."
---

# CYCLE: TWO adjacent thin-identity lowering themes for jacobi-smoother

## Summary

Authors the two adjacent thin-identity lowering themes that close `jacobi-smoother`'s
downward edges from the firm L3 entry (cycle-037) through the co-landing L2 floor
(wave-1 D5, this cycle) to the firm L1 gate: **`jacobi-smoother-body-identity`** (L3>L2)
and **`jacobi-smoother-leaf-identity`** (L2>L1). Both are **identity-in-form** because the
Jacobi smoother is the thinnest constructed-operator gate — its per-call body is **one
elementwise product** `op.dinv ⊙ x = (ω · D⁻¹) ⊙ x`, with no operator-apply, no reduction,
no sweep loop, no convergence test, and (the defining fact across both edges) **no fused
multi-operation kernel to unfold** and **no fold-parent to dispatch through**. `jacobi-smoother`
is **standalone, fork-INDEPENDENT, NO fold-parent** — it is NOT a member of the
`linear_combination` / `inner_product` fold cohort, so the cycle-041
`dot-l2-leaf-floor-vs-fold-only-design` leaf-vs-fold fork does **not** reach it (the two
themes carry no design-presupposition gate of the kind the `dot` / `scal` floor-edges carry).
The L3>L2 theme is the constructed-operator-gate analogue of the firm BLAS-1-leaf
`scal-body-identity` — identity-in-form on the body, **no wrapper to rotate** (no
`(op, K, s)`→`IterState` consolidation, no outer-loop dissolution); the L2>L1 theme is the
analogue of the firm `dot-leaf-identity` — identity-in-form on the gate, with the genuine
L2-layer fusion-rotation observation **negative** (there is no fusion to de-fuse) and the
substantive rotation in the whole chain deferred to the L1>L0 leaf-mutation themes
(`reciprocal-elementwise-product-mutation-rotation` sub-pattern B +
`jacobi-smoother-mutation-rotation`). Both themes `firm`.

## Proposed changes

```new:book/src/L3-L2/jacobi-smoother-body-identity.md
# jacobi-smoother-body-identity

The L3>L2 lowering theme for the constructed-operator gate `jacobi-smoother`. The rewrite is
**identity-in-form on the body** with **no wrapper rotation** — `jacobi-smoother` is a
single whole-tensor field operation (one elementwise product `op.dinv ⊙ x`), not a step body
and not an outer driver, so the L3 whole-tensor form lowers into the L2 floor form by the
identity on the gate's apply itself. There is no `(op, K, s)`→`IterState` consolidation and no
outer-loop dissolution to perform (the two surface adjustments the sibling
[`krylov-step-body-identity`](./krylov-step-body-identity.md) carries at its wrapper, and the
substantive driver rotation [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) carries);
`jacobi-smoother` has no wrapper and no loop. The body IS the identity. This is the
**constructed-operator-gate analogue** of the BLAS-1-leaf [`scal-body-identity`](./scal-body-identity.md)
— a single field operation, no wrapper to rotate — and the thinnest constructed-operator-gate
member of the L3>L2 lowering family.

## Slug

`jacobi-smoother-body-identity`

## Context

The `jacobi-smoother` lowering relationships span three adjacent layers, all identity-in-form
because `jacobi-smoother` is the **thinnest constructed-operator gate** — a single elementwise
product with no iteration view, no reduction, no kernel fusion, and no fold-parent:

- **L3 form** ([`L3/jacobi-smoother`](../L3/jacobi-smoother.md), firm cycle-037) — the
  whole-tensor field operation `jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]`,
  the iteration-rotation rendering. Carries **no iteration view** (a leaf-shaped gate, not a
  step body or a driver) and **no sequential obstruction of any kind** (the apply is one
  elementwise product over independent length-axis indices). The LHS of this theme.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/jacobi-smoother`](../L2/jacobi-smoother.md), firm cycle-042 D5) — the
  fusion-rotation floor gate, the same single elementwise-product apply, with the genuine
  fusion-rotation observation **negative** (no fused multi-operation kernel to unfold). The RHS
  of this theme.
- **L2>L1 form** ([`L2-L1/jacobi-smoother-leaf-identity`](../L2-L1/jacobi-smoother-leaf-identity.md),
  firm cycle-042 D8 — co-dispatched) — the onward edge into the L1 gate; also identity-in-form.

This theme is the **constructed-operator-gate counterpart** of the firm
[`scal-body-identity`](./scal-body-identity.md) (cycle-041 D6). The `scal` theme establishes
the pattern "identity-in-form on the body, **no wrapper to rotate** — `scal` is a leaf, not a
step body, so the two wrapper adjustments the `krylov-step` theme carries have no analog";
`jacobi-smoother` follows the same shape one tier richer in framing (it is a *constructed-operator
gate*, not a BLAS-1 leaf — its argument `op` is an opaque closure built once at setup — but its
*apply* is just as leaf-shaped: one elementwise product). The `krylov-step-body-identity`
point-3 applicability condition names the L3-native-by-signature-shape property — "each operates
on whole-tensor inputs with no element-loop exposed at L2" (`krylov-step-body-identity.md:97`);
the Jacobi gate's apply satisfies this *at L2 already*, so the L3>L2 rotation is the identity, not
a decomposition.

**The contrast that defines this theme.** The L3 `jacobi-smoother` entry classifies the gate's
obstruction-profile against its siblings: `ksp_solve` and `eigsolve` carry outer-loop sequential
obstructions (the convergence-tested fold; the opaque-library eigen-iteration), `chebyshev` is
`partial-obstruction` (inner `k`-recurrence + outer `pc_it` sweep), and `jacobi-smoother` carries
**none** — "the gate is, in obstruction-profile terms, a leaf — like `apply_linop`, `dot`, `scal`
— not a step body or a driver" (`L3/jacobi-smoother.md` §Iteration-rotation marker). That is
exactly why this L3>L2 edge is the identity: there is no loop in the apply for the iteration
rotation to have rotated, and so nothing for the L3>L2 lowering to dissolve.

## L3 form (LHS)

The L3 whole-tensor form ([`L3/jacobi-smoother`](../L3/jacobi-smoother.md) §Signature):

    jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]
    jacobi_smoother op x = op.dinv ⊙ x
                         = (ω · diag(A)⁻¹) ⊙ x

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `op` a
`JacobiSmoother[N]` — the opaque constructed closure bound once at setup (carrying `op.dinv`,
the damped inverse diagonal `ω · diag(A)⁻¹`; `op.omega`, already absorbed into `dinv`; and
`op.sf_max`, consumed only at setup); `x : Tensor[N]` a single length axis, read-only at L3;
result `Tensor[N]` of the same axis. The gate carries **no iteration view** (it is a leaf-shaped
field operation, not a step body or a driver) and **no sequential obstruction** (the apply is
one elementwise product over independent length-axis indices — embarrassingly parallel, fully
GPU-friendly). No L4 wrapper machinery applies: the gate carries no monadic effect, no
state-stratification typing, and no outer-driver structure — its body is one elementwise product
(the constructed-operator-gate "L4 CONFIRMED-NOT-NEEDED" verdict shared with the firm
`apply_linop` / `ksp_solve` gates; `L3/jacobi-smoother.md` §Lifts from).

## L2 form (RHS)

The L2 floor form ([`L2/jacobi-smoother`](../L2/jacobi-smoother.md) §Signature, firm cycle-042 D5):

    jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]
    jacobi_smoother op x = op.dinv ⊙ x
                         = (ω · diag(A)⁻¹) ⊙ x

The same constructed-operator gate in the fusion-rotation vocabulary — **the thinnest such gate**,
a single elementwise product. The signature is **textually identical to the L3 form** modulo
notation; the body is the same single whole-tensor field operation. The six algebraic laws hold
unchanged across the edge (L3 §Algebraic laws ≡ L2 §Algebraic laws — both inherit the L1 gate's
six laws: linearity, zero-vector annihilation, the `assemble_diagonal` round-trip, damping
absorption, the estimated-damping degenerate case, self-transpose under symmetric wiring), and the
non-law set transports unchanged (the dead-code Hermitian-transpose non-realisation, the
no-iteration non-equivalence, the representation-dependent bit-determinism non-law). The **only**
fusion note the L2 floor carries is a *negative* one (`L2/jacobi-smoother.md` §"Negative fusion
observation"): the Jacobi apply has no fused multi-operation kernel to unfold, so the L2
fusion-rotation work is a no-op — the L2 form is identical to the L1 form because there is nothing
to de-fuse. At L3 even that negative note is documentary (L3 exposes no element loop at all).

## Rewrite shape

The rewrite is the **identity on the gate's body**, with **no wrapper adjustment**:

    jacobi_smoother op x   (L3 whole-tensor field op)   ⇒   jacobi_smoother op x   (L2 floor gate)

The body maps trivially — one binding, one elementwise-product field operation, same position,
same dataflow:

| L3 form | L2 form | Mapping |
|---|---|---|
| `jacobi_smoother op x = op.dinv ⊙ x` (whole-tensor field operation; no iteration view; no obstruction) | `jacobi_smoother op x = op.dinv ⊙ x` (constructed-operator-gate floor; single elementwise product; negative fusion observation) | Identity. Same signature, same single elementwise-product field operation. The only framing difference is documentary: L3 frames the gate as a whole-tensor field operation in the iteration-rotation vocabulary (the thinnest of the constructed-operator-gate family, carrying no obstruction); L2 frames the same gate as a base fusion-rotation primitive whose fusion observation is *negative* (no fused multi-operation kernel to unfold). No operational adjustment occurs. |

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface
adjustments at the wrapper around its kernel body (the L3 `(op, K, s)` tuple → L2 `IterState`
record; the L3 tail-recursive outer loop → L2 outer-driver-by-role reference), and
`ksp-solve-outer-driver` carries the substantive driver rotation. **Neither has an analog for
`jacobi-smoother`**: the Jacobi gate is a single elementwise-product field operation, not a step
body with an `(op, K, s)` carrier and not a driver with an outer loop. There is no `IterState`
(the `op` closure is the gate's only structured argument and it is *opaque-and-immutable*, not a
threaded iteration state), and there is no outer driver (no loop folds `jacobi_smoother` calls at
the gate itself; the gate is *called by* consumers — the Krylov preconditioner slot
`ksp.cpp:198-200`, the error-estimator, etc. — but those loops belong to the consuming solver, not
to the gate, exactly as `scal` is called by step bodies whose loops are not `scal`'s). The mapping
is total and bijective on a single binding — the degenerate maximal case of the identity-in-form
property, identical in shape to the `scal-body-identity` leaf case but on a constructed-operator
gate rather than a BLAS-1 leaf.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `jacobi-smoother` endpoints)
when:

1. **`jacobi-smoother` is treated as a single field operation, not decomposed.** The gate's apply
   does not decompose into other L3 or L2 primitives — the single elementwise product `op.dinv ⊙ x`
   is below both layers' resolution (no L2 / L3 `elementwise_product` floor exists yet; see
   §Open-questions). Its sub-operations (the per-element multiply, the complex four-multiply
   componentwise product) are below both layers' resolution. The body is one elementwise-product
   field operation at both layers.

2. **The signature is whole-tensor at both layers** — `(op: JacobiSmoother[N], x: Tensor[N]) ->
   Tensor[N]` with no per-element loop exposed at L2 and no iteration view at L3. This is the
   `krylov-step-body-identity` point-3 condition (`krylov-step-body-identity.md:97`) specialized to
   the standalone constructed-operator gate: the apply's signature has no per-element loop visible,
   so it is L3-native by construction and the rotation is identity-in-form rather than a
   decomposition. The opaque `op` closure absorbs the element-type and operator-representation
   axes identically at both layers.

3. **No iteration view, no sequential obstruction, no fold-parent.** The Jacobi apply is
   element-local, reduction-free, rank-local; every element is independent. There is no outer
   loop, no carry trajectory, no recurrence — so there is nothing for the L3 iteration rotation
   to have rotated and nothing for the L3>L2 lowering to dissolve. And `jacobi-smoother` is a
   **standalone constructed-operator gate with NO fold-parent** — it is not a member of the
   `linear_combination` (reduce-to-`Tensor[N]`) or `inner_product` (reduce-to-`Scalar`) fold
   cohort — so the cycle-041 `dot-l2-leaf-floor-vs-fold-only-design` leaf-vs-fold design fork
   (which gates the `dot` / `scal` floor-edge themes) **does not reach this theme**. The L2 floor
   under it is unconditional regardless of how that fork resolves.

If a future L2 `jacobi-smoother` variant introduced an apply-time loop or a fused multi-operation
kernel not present in the current surface, the identity claim would need re-audit — none exists in
the current surface (the apply is one elementwise product; `L2/jacobi-smoother.md` §"Negative
fusion observation").

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the gate's apply signature shape `(op: JacobiSmoother[N], x: Tensor[N])
-> Tensor[N]` is whole-tensor by construction at both layers — no element loop is exposed at L2, no
iteration view at L3 — and the body is a single elementwise-product field operation with no
fold-parent and no obstruction. The L3 vocabulary at this scope demands whole-tensor field
operations with no element loop exposed; `jacobi-smoother`'s apply satisfies this *at L2 already*,
so the rotation is the identity. This is the same structural argument the `scal-body-identity`
theme makes for the standalone BLAS-1 leaf (the `krylov-step-body-identity` point-3 condition
promoted to dominant because there is no kernel body wrapping the operation), here applied to a
constructed-operator gate whose apply is just as leaf-shaped.

**Empirical-match (secondary)**: the firm L3 `jacobi-smoother` entry (cycle-037) was authored
value-thread-isomorphic to the firm L1 gate, and the wave-1 D5 L2 floor was authored
value-thread-isomorphic to both (its §Status records "value-thread-isomorphic to the firm L1 form
… and equally to the firm L3 form above it"). The three chapters agree on every law and every
variant axis by independent transcription; the identity is observational on the three existing
firm chapters, not derivational. The cycle-036 D2 cross-layer-cross-cutter audit
(`book/src/L3/index.md:46`) had already classified the gate as the "thinnest constructed-operator
gate, one `elementwise_product`" firm identity-in-form L3 candidate — this theme is the
downward-edge realization of that audited classification once the L2 floor exists (D5, this cycle)
for the rotation to target.

## Speculative L3 operators

**None.** This theme is the identity rotation between firm endpoints: the L3 LHS
([`L3/jacobi-smoother`](../L3/jacobi-smoother.md)) is firm (cycle-037), and the L2 RHS
([`L2/jacobi-smoother`](../L2/jacobi-smoother.md)) is firm (cycle-042 D5). No new L3 vocabulary is
introduced. `jacobi-smoother` does not get its own L4 typed-wrapper anchor (constructed-operator
gates with no monadic effect / no outer-driver structure appear inside L4 operator bodies as
let-bindings — the "L4 CONFIRMED-NOT-NEEDED" verdict shared with `apply_linop` / `ksp_solve`), so
there is no upstream L4>L3 theme for `jacobi-smoother` either; the L3 form is L3-native by
signature and this theme closes its downward edge to the L2 floor.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/jacobi-smoother.md` (cycle-037 firm) — the L3 whole-tensor form (LHS). Signature,
  semantics (inner-product-free, iteration-free, reduction-free; one elementwise product), the
  §"Iteration-rotation marker" (leaf-shaped, no obstruction), six algebraic laws, three non-laws,
  two-orthogonal-plus-one-absorbed variant profile.
- `book/src/L2/jacobi-smoother.md` (cycle-042 D5 floor — co-lands this cycle) — the L2 floor form
  (RHS). Identical signature and six laws; the constructed-operator-gate floor framing + the
  §"Negative fusion observation" (no fused multi-operation kernel to unfold).
- `book/src/L3-L2/scal-body-identity.md` (cycle-041 D6 firm) — the BLAS-1-leaf precedent: identity
  on the body, no wrapper to rotate. The structural shape this theme follows on a
  constructed-operator gate.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (cycle-007/009 firm) — the point-3 applicability
  condition classifying L3-native-by-signature-shape (no element loop ⇒ identity rotation, not
  decomposition). The structural justification this theme promotes to dominant.

Cross-layer audit (the empirical-match anchor):

- `book/src/L3/index.md:46` — the cycle-036 D2 cross-layer-cross-cutter audit verdict naming
  `jacobi-smoother` the "thinnest constructed-operator gate, one `elementwise_product`" firm
  identity-in-form L3 candidate; this theme is the downward-edge enactment of that classification.

Onward edges (cross-reference, not this theme's content):

- `book/src/L2-L1/jacobi-smoother-leaf-identity.md` (cycle-042 D8 — co-dispatched) — the onward
  L2>L1 edge into the L1 gate; also identity-in-form.
- `book/src/L1/jacobi-smoother.md` (firm) + `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md`
  (firm; sub-pattern B) + `book/src/L1-L0/jacobi-smoother-mutation-rotation.md` (firm) — the L1 gate
  and its in-place L0 mutation rotations, reached via the onward edge. The **substantive** rotation
  in the whole chain lives there, not in this thin L3>L2 hop.

Transitive L0 evidence (inherited from the firm L1 gate; not re-localized — identity-in-form edge,
L0 evidence transitive through L1; self-verified via `tools/citecheck/citecheck.py --anchor` this
invocation against on-disk `reference/palace/palace/linalg/jacobi.{hpp,cpp}`):

- `palace/linalg/jacobi.cpp:38` — `Y[i] = DI[i] * X[i]` — the real elementwise-multiply kernel that
  realises the apply (law 1 witness; the body the L3 whole-tensor elementwise product lowers to).
  Self-verified (anchor `Y[i] = DI[i] * X[i]` @38).
- `palace/linalg/jacobi.cpp:103` — `Apply(dinv, x, y);` — the single dispatch that is the entire
  per-call action. Self-verified (anchor `Apply(dinv, x, y)` @103).
- `palace/linalg/jacobi.cpp:79-80` — the `assemble_diagonal → reciprocal` setup chain
  (`op.AssembleDiagonal(dinv); dinv.Reciprocal();`). Self-verified (anchor `Reciprocal` @80).
- `palace/linalg/jacobi.hpp:43` — `void MultTranspose(...) const override { Mult(x, y); }` — the
  transpose self-alias (law 6). Self-verified (anchor `Mult(x, y)` @43).
- `palace/linalg/jacobi.cpp:61-69` — the complex `Apply<Transpose=true>` dead-code branch
  (conjugate-`dinv` apply, negated off-diagonal terms `YR[i] = DIR[i]·XR[i] + DII[i]·XI[i]`,
  `YI[i] = -DII[i]·XR[i] + DIR[i]·XI[i]`); dead code under symmetric wiring (the non-law witness).
  Confirmed by direct read; inherited unchanged from L1/L3.

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS
([`L3/jacobi-smoother`](../L3/jacobi-smoother.md)) is firm (cycle-037); the L2 RHS
([`L2/jacobi-smoother`](../L2/jacobi-smoother.md)) is firm (cycle-042 D5, co-landing). The body is
the identity rotation on a single elementwise-product field operation; **there is no wrapper to
rotate** (no `(op, K, s)`→`IterState` consolidation, no outer-loop dissolution — `jacobi-smoother`
is a leaf-shaped constructed-operator gate, not a step body and not a driver). The structural
justification (whole-tensor signature, no element loop, no iteration view, no obstruction, no
fold-parent) is the `krylov-step-body-identity` point-3 condition specialized to the standalone
gate and promoted to dominant; the empirical-match anchor is the firm L3 entry + the cycle-036 D2
audit's "thinnest constructed-operator gate" classification (`L3/index.md:46`). No speculative
operator, no negative-anchor reconstruction, no sequential obstruction. The thinnest
constructed-operator-gate member of the L3>L2 lowering family — the constructed-operator-gate
counterpart of the BLAS-1-leaf `scal-body-identity`.

**`jacobi-smoother` is fork-INDEPENDENT (NOT subject to the leaf-vs-fold design fork).** Unlike
the cycle-041 `dot` / `scal` floor-edge themes — which presuppose the (b) same-named leaf-floor
realization and would re-anchor under the batch-12 meta-phase's (a) fold-only reading
(`dot-l2-leaf-floor-vs-fold-only-design`) — `jacobi-smoother` is a standalone constructed-operator
gate with **no fold-parent on either codomain**. There is no `linear_combination` / `inner_product`
fold for it to be a member of, so this theme carries **no design-presupposition gate**: its L2 RHS
is the unconditional `jacobi-smoother` floor regardless of how the BLAS-1 fork resolves. This is the
explicit fork-independence fact recorded in the L2 floor's §Status and §Dependencies.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L2 floor gate *up* to the L3 whole-tensor form is the value-thread-isomorphic
  identity rotation: the L2 signature has no element loop exposed (the apply is one whole-tensor
  elementwise product), which is exactly what makes it L3-native by construction. No additional
  structure is required for the lift. This reverse-direction note lives here in working notes per
  the high→low layer-definition discipline; the formal chapter narrates only L3 → L2.

- **No L2 / L3 `elementwise_product` floor exists yet** (genuine gap, not a defect of this theme).
  The Jacobi apply's body — one elementwise product `op.dinv ⊙ x` — is recorded as a single base
  field operation below both layers' current resolution. Once an L2 `elementwise_product` floor
  lands (the wave-1 D5 proposed plan item `l2-floor-elementwise-product-reciprocal`), this theme's
  L2 RHS body would name `elementwise_product(op.dinv, x)` as a same-layer dependency; the
  identity-in-form edge is unaffected (the L3 form would name the same dependency). Inherited
  unchanged from the L2/L3 entries.

- **`Apply<Transpose=true>` dead-code consumer branch** (`palace/linalg/jacobi.cpp:61-69`) — the
  conjugate-`dinv` Hermitian-transpose kernel exists but no consumer instantiates `Apply<true>`
  (`MultTranspose` aliases `Mult`). Recorded by reference (non-law inherited unchanged from
  L1/L3/L2); ties to OQ `reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch`. No
  new action at this edge — the identity rotation maps the (dead) transpose path identity-in-form
  whether or not it is exercised.

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (this
  theme's L3>L2 identity ∘ the L2>L1 `jacobi-smoother-leaf-identity` identity) is annotated in-line
  at the `jacobi-smoother` entries per the CLAUDE.md invariant "Identity rotations across
  non-adjacent layers are annotated in-line, not via a dedicated lowering directory" — no
  `book/src/L3-L1/` directory. This theme + the co-dispatched `jacobi-smoother-leaf-identity`
  compose to capture it. (NOTE: before this cycle the L3 entry lowered to L1 *directly*, skipping
  the L2 floor; the D5 L2 floor + these two adjacent themes replace that non-adjacent annotation
  with the proper adjacent-edge chain.)
```

```new:book/src/L2-L1/jacobi-smoother-leaf-identity.md
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
```

```edit:book/src/L2-L1/index.md
| [jacobi-smoother-leaf-identity](./jacobi-smoother-leaf-identity.md) | `L2/jacobi-smoother` (firm, cycle-042 D5 gate floor) | `L1/jacobi-smoother` (firm constructed-operator gate) | firm *(structural; identity-in-form on the constructed-operator gate — value-thread-isomorphic signature, single elementwise-product apply; **fork-INDEPENDENT, NO fold-parent** — the cycle-041 `dot-l2-leaf-floor-vs-fold-only-design` leaf-vs-fold fork does NOT reach it; the L2 fusion-rotation observation is **negative** (no fused multi-operation kernel to unfold), so the edge is identity with the fusion treatment a documented no-op — NOT a fold deferral; substantive rotation deferred to L1>L0 `reciprocal-elementwise-product-mutation-rotation` sub-pattern B + `jacobi-smoother-mutation-rotation`)* |
```

```edit:book/src/L2-L1/index.md
- `jacobi-smoother-leaf-identity` — the L2 `jacobi-smoother` constructed-operator-gate floor lowers to the L1 `jacobi-smoother` gate identity-in-form on the apply (single elementwise product). **Fork-INDEPENDENT, NO fold-parent** (the cycle-041 leaf-vs-fold fork does NOT reach it). The L2 fusion observation is **negative** — no fused multi-operation kernel to unfold — so there is no fusion to defer (no fold-parent) and the edge is the identity with the fusion treatment a documented no-op. Slug `-leaf-identity` (NOT `-fold-specialization`): an identity-leaf-lowering, not a fold→leaf dispatch.
```

```edit:book/src/L3-L2/index.md
| [`jacobi-smoother-body-identity`](./jacobi-smoother-body-identity.md) | L3 [`jacobi-smoother`](../L3/jacobi-smoother.md) §Signature — the whole-tensor field operation `jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]`; constructed-operator gate, **no iteration view, no sequential obstruction** (one elementwise product `op.dinv ⊙ x`). | L2 [`jacobi-smoother`](../L2/jacobi-smoother.md) §Signature — the constructed-operator-gate floor (cycle-042 D5); identical signature, single elementwise-product apply; **negative fusion observation** (no fused multi-operation kernel to unfold). | `structural` (whole-tensor signature, no element loop, no iteration view, no obstruction, **NO fold-parent** — `krylov-step-body-identity` point-3 condition specialized to the standalone constructed-operator gate) + secondary `empirical-match` (firm L3 entry cycle-037 + cycle-036 D2 audit `L3/index.md:46` "thinnest constructed-operator gate" classification) | `firm` (cycle-042 D8 abstractor; identity-in-form on the body, **no wrapper to rotate** — the constructed-operator-gate counterpart of the BLAS-1-leaf `scal-body-identity`; **fork-INDEPENDENT**) |
```

```edit:book/src/L3-L2/index.md
- `jacobi-smoother-body-identity` — the L3 whole-tensor `jacobi-smoother` constructed-operator-gate field operation lowers to the L2 same-named gate floor (cycle-042 D5); the body IS the identity (one elementwise product `op.dinv ⊙ x`), there is no wrapper to rotate. **Fork-INDEPENDENT, NO fold-parent** — the constructed-operator-gate counterpart of `scal-body-identity`, the thinnest constructed-operator-gate member of the family.
```

```edit:book/src/SUMMARY.md
- [jacobi-smoother-body-identity](./L3-L2/jacobi-smoother-body-identity.md)
```

```edit:book/src/SUMMARY.md
- [jacobi-smoother-leaf-identity](./L2-L1/jacobi-smoother-leaf-identity.md)
```

## Speculative operators proposed

**None.** Both themes are identity rotations between firm (or firm-this-cycle) endpoints:
- L3>L2: LHS firm `L3/jacobi-smoother` (cycle-037), RHS firm `L2/jacobi-smoother` (cycle-042 D5).
- L2>L1: LHS firm `L2/jacobi-smoother` (cycle-042 D5), RHS firm `L1/jacobi-smoother`.

No new L1/L2/L3 vocabulary introduced; `jacobi-smoother` gets no L4 anchor (constructed-operator-gate
"L4 CONFIRMED-NOT-NEEDED" verdict). The harvester has nothing to promote from these themes.

## Supporting evidence

L2/L1/L3 endpoint chapters (the four firm/firming anchors):
- `book/src/L3/jacobi-smoother.md` (firm cycle-037) — L3>L2 LHS.
- `book/src/L2/jacobi-smoother.md` (firm cycle-042 D5, co-landing) — L3>L2 RHS + L2>L1 LHS.
- `book/src/L1/jacobi-smoother.md` (firm) — L2>L1 RHS.
- `book/src/L3-L2/scal-body-identity.md` + `book/src/L2-L1/dot-leaf-identity.md` (firm cycle-041) —
  the two thin-identity precedents whose structure these themes follow.

L0 (transitive through firm L1; self-verified via `tools/citecheck/citecheck.py --anchor`
2026-06-01 against on-disk `reference/palace/palace/linalg/jacobi.{hpp,cpp}`):
- `jacobi.cpp:38` (`Y[i] = DI[i] * X[i]`) — `[ok]`.
- `jacobi.cpp:103` (`Apply(dinv, x, y)`) — `[ok]`.
- `jacobi.cpp:79-80` (`Reciprocal` @80) — `[ok]`.
- `jacobi.hpp:43` (`Mult(x, y)`) — `[ok]`.
- `jacobi.cpp:61-69` — the dead-code complex transpose branch (conjugate-`dinv` apply,
  `YR[i] = DIR[i]·XR[i] + DII[i]·XI[i]`, `YI[i] = -DII[i]·XR[i] + DIR[i]·XI[i]`); confirmed by direct
  read (the `else` branch of the `if constexpr (!Transpose)` at :52). Cited by-reference as the L1/L3
  entries do.
- `jacobi.cpp:52-60` — complex forward-branch four-multiply componentwise product (single
  elementwise complex product, negative-fusion witness); confirmed by direct read.

## Open questions / caveats

1. **COUNT-OWNERSHIP deferred to D11.** Per the dispatch directive I appended ONLY my two theme rows
   (one to each lowering index theme-table), my two cohort-growth bullets (one to each index's
   rotation-bullet list), my two SUMMARY registrations, and the two theme bodies. I did **NOT** touch
   the consolidated firm-count tallies / Working-Notes narrative bullets in either `L2-L1/index.md`
   or `L3-L2/index.md` (the `l3-l2-rotation-theme-coverage-gap` "5-of-18 → N-of-18" tally; the
   L2-L1 "firm 10 → N" cohort count). D11 owns the tallies. After both themes land the L3>L2 firm
   count is +1 (the `l3-l2-rotation-theme-coverage-gap` advances by one toward closure) and the L2>L1
   firm count is +1 — D11 should record both.

2. **Fork-independence vs. the cycle-041 BLAS-1 floor-edge cohort (recorded for D11 + batch-12
   meta-phase awareness).** The two cycle-041 sibling cohorts (`dot`/`scal`/`nrm2` L2>L1 floor-edges
   and L3>L2 body-edges) presuppose the (b) same-named leaf-floor realization and carry a
   design-presupposition gate under `dot-l2-leaf-floor-vs-fold-only-design`. `jacobi-smoother` is
   **fork-INDEPENDENT** — a standalone constructed-operator gate with no fold-parent — so neither of
   these themes carries that gate. Flagged so the batch-12 meta-phase, when it adjudicates the BLAS-1
   leaf-vs-fold fork, does NOT mistakenly sweep `jacobi-smoother` into it: the Jacobi floor + both
   thin edges stand unconditionally regardless of how the fork resolves.

3. **`l2-floor-elementwise-product-reciprocal` plan item (carried forward from D5, not re-proposed
   here).** Both themes' RHS/LHS bodies record the Jacobi apply as a single elementwise product
   below the L2/L3 layers' current resolution because no L2 `elementwise_product` / `reciprocal`
   floor exists yet. The D5 report proposes `l2-floor-elementwise-product-reciprocal` (floor the
   elementwise-primitives cohort under the firm L3 cohort, the same `l2-floor-under-l3-*`
   foundation-first pattern). When that floor lands, both themes' bodies would name
   `elementwise_product(op.dinv, x)` as an L2/L3 same-layer dependency; the identity-in-form edges
   are unaffected. No new plan item proposed by this dispatch — deferring to D5's.

4. **`Apply<Transpose=true>` dead-code consumer branch by reference** (`jacobi.cpp:61-69`). Noted by
   reference per the dispatch directive (NOT re-derived) — the conjugate-`dinv` Hermitian-transpose
   kernel exists but no consumer instantiates `Apply<true>` (`MultTranspose` aliases `Mult`). Ties to
   the standing OQ `reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch`. The
   identity rotations map the (dead) transpose path identity-in-form whether or not exercised; no new
   action at either edge.

5. **`l3-index-39-stale-self-citation-sweep-to-46` (NEW OQ, opened by repairer cycle-042).** The
   cycle-036 D2 audit verdict's "thinnest constructed-operator gate, one `elementwise_product`"
   classification of `jacobi-smoother` lives at `book/src/L3/index.md:46` (the "(A) Identity-in-form
   L3 backfill candidates — 6 firm" Working-Notes bullet); line 39 is a blank table-terminus. This
   report's four `L3/index.md:39` pinpoints were tightened to `:46` in-place by the repairer (verified
   on-disk: line 46 carries the exact quoted phrase). HOWEVER the `:39` pinpoint is INHERITED from the
   artifact's OWN stale self-citation — multiple firm artifact sites still repeat `L3/index.md:39` for
   this same verdict: `book/src/L3/jacobi-smoother.md` §Status, the `L3/index.md:33` firm row, and the
   `L3/index.md:58` cycle-037 landing-note bullet (line 39 was presumably the verdict's location
   before later Working-Notes rows were inserted above it, displacing the bullet to :46). Correcting
   only this report leaves a local `:46`-vs-upstream-`:39` inconsistency. *Follow-up:* a future lifter
   (or layer-intro-author L3-index-refresh) pass should sweep the inherited `:39`→`:46` stale
   self-citation across the artifact sites so the pinpoint is uniform. Out of repairer scope (the
   repairer does not modify `book/`); recorded so the sweep is tracked, not lost. *Trigger:* the next
   L3-index-touch dispatch (lifter / layer-intro-author), co-schedulable with any `L3/jacobi-smoother`
   re-anchor.
