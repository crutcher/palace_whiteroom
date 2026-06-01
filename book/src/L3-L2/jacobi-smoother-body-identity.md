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
