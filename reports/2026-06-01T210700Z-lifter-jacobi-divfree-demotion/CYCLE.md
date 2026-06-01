---
agent: lifter
invoked_at: 2026-06-01T210700Z
scope: L3>L2 + L2>L1 theme re-anchor — enact cycle-050 D8 DEMOTE-OK verdicts (jacobi-smoother both edges + divfree-projector-body-identity L3>L2); KEEP divfree-projector-leaf-identity (L2>L1)
status: integrated
integrated_at: 2026-06-01T22:14:50Z
integration_commit: 76721fec7a70c2ceed5e17de8c0f06ab3ad56205
integration_notes: "Applied clean by integrator-per-report (D4 of cycle-051); finalized cycle-051. jacobi-smoother-{body,leaf}-identity + divfree-projector-body-identity deleted (3 theme files); L3/jacobi-smoother + L2/jacobi-smoother + L3/divfree-projector re-anchored to in-line notes; KEPT divfree-projector-leaf-identity (genuine step-4 Grad->AddMult fusion rotation) reachable via 2 direct live links from L3/divfree-projector; cross-dispatch danglers at :22/:231 resolved by deletion; zero dangling live links to deleted slugs; build exit 0."
inputs:
  - reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md (the D8 verdict source)
  - book/src/L3-L2/jacobi-smoother-body-identity.md (DELETE)
  - book/src/L2-L1/jacobi-smoother-leaf-identity.md (DELETE)
  - book/src/L3-L2/divfree-projector-body-identity.md (DELETE)
  - book/src/L2-L1/divfree-projector-leaf-identity.md (KEEP — genuine step-4 fusion rotation)
  - book/src/L3/jacobi-smoother.md (re-anchor)
  - book/src/L2/jacobi-smoother.md (re-anchor)
  - book/src/L3/divfree-projector.md (re-anchor)
  - book/src/SUMMARY.md, book/src/L3-L2/index.md, book/src/L2-L1/index.md (de-link / row removal)
---

# CYCLE: Re-anchor jacobi-smoother (both edges) + divfree-projector-body-identity (L3>L2) — DEMOTE; KEEP divfree-projector-leaf-identity (L2>L1)

## Summary

Enacts the cycle-050 D8 verify-body audit (`reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`) under the 2026-06-01 VOCABULARY-SHIFT REDIRECT. Three degenerate identity-in-named-terms `-body-identity` / `-leaf-identity` themes are demoted to in-line notes and their theme files deleted: `jacobi-smoother-body-identity` (L3>L2), `jacobi-smoother-leaf-identity` (L2>L1), and `divfree-projector-body-identity` (L3>L2). The Jacobi apply is one elementwise product `op.dinv ⊙ x`, textually identical at L1/L2/L3 (no vocabulary shift); the divfree L3>L2 four-step composition `WeakDiv→Z→ksp_solve→Grad` is explicit + value-thread-isomorphic at both layers (the only genuine fusion in the projector chain lives on the L2>L1 edge, not this one). The **`divfree-projector-leaf-identity` (L2>L1) theme is KEPT** — it carries the one genuine step-4 `Grad->AddMult` apply-accumulate fusion rotation (de-fuses to `apply_linop(P.Grad,ψ)▷axpy` at L2, re-fuses to fused `Grad->AddMult(ψ,y,1.0)` at L1; `palace/linalg/divfree.cpp:185` real / `:180-181` complex). The new in-line §"Downward to L2" note on `L3/divfree-projector.md` points onward to BOTH the L2 floor AND the kept L2>L1 fusion theme so the genuine rotation stays reachable (OQ `divfree-l3-l2-demotion-must-keep-l2-floor-and-l2-l1-fusion-reachable`).

Total deleted by D4: **3 theme files** (jacobi ×2 + divfree-body-identity ×1). The `divfree-projector-leaf-identity` theme file + its SUMMARY line + its L2-L1 index row + Working-Notes bullet SURVIVE. The consolidated TALLY is DEFERRED to D5.

## Proposed changes

### 1. DELETE the 3 demoted theme files

```delete:book/src/L3-L2/jacobi-smoother-body-identity.md
```

```delete:book/src/L2-L1/jacobi-smoother-leaf-identity.md
```

```delete:book/src/L3-L2/divfree-projector-body-identity.md
```

### 2. Re-anchor `book/src/L3/jacobi-smoother.md` (frontmatter + §Context "Downward" + §"Lowers to")

The frontmatter `lowers_to` already routes through the L1 entry with no L3-L2 theme named, so no frontmatter edit is needed there — the body prose carries the `jacobi-smoother-body-identity` reference. Two body edits.

```edit:book/src/L3/jacobi-smoother.md
[old]: - **Downward** to L2/L1: `jacobi-smoother` lowers to the **present adjacent L2 floor** [`jacobi-smoother`](../L2/jacobi-smoother.md) (cycle-042) via the `jacobi-smoother-body-identity` L3>L2 theme, and onward to L1 [`jacobi-smoother`](../L1/jacobi-smoother.md). The rotation is **identity-in-form on the constructed-operator-gate apply** — L1, L2, and L3 all see `jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]` with the same shape contract, the same algebraic laws, the same variant-axis profile, and the same absorbed operator-representation type. The substantive rotation in the chain is the L1>L0 leaf-mutation rotation: the apply's single elementwise product lowers to Palace's in-place `forall_switch` element-loop (`Y[i] = DI[i] * X[i]`), captured by the firm L1>L0 theme [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) (sub-pattern B) and the constructed-operator-closure theme [`jacobi-smoother-mutation-rotation`](../L1-L0/jacobi-smoother-mutation-rotation.md). The L3>L2 hop is by contrast a layer-coherence rotation (each layer is coherent within itself), not an algebraic one; the L3>L2 identity-in-form annotation is captured by the adjacent-edge theme, with no non-adjacent `L3-L1/` directory created — the transitive L3>L1 identity is annotated in-line per the cycle-012 non-adjacent-identity convention (precedent: the firm L3 `dot` / `scal` / `apply_linop` cohort, all of which note their identity rotations in-line).
[new]: - **Downward** to L2/L1: `jacobi-smoother` lowers to the **present adjacent L2 floor** [`jacobi-smoother`](../L2/jacobi-smoother.md) (cycle-042) and onward to L1 [`jacobi-smoother`](../L1/jacobi-smoother.md). The L3>L2 rotation is a **degenerate identity-in-named-terms lowering** annotated in-line here (no dedicated L3>L2 theme file): the apply is one whole-tensor elementwise product `op.dinv ⊙ x`, spelled identically at L1, L2, and L3 (`jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]`, same shape contract, same six algebraic laws, same three non-laws, same two-orthogonal-plus-one-absorbed variant profile) — there is no vocabulary shift across the L3>L2 edge to rotate. (The former `jacobi-smoother-body-identity` L3>L2 theme file was demoted to this in-line note cycle-051 per the 2026-06-01 VOCABULARY-SHIFT REDIRECT, `METHODOLOGY-REDIRECT.md` — a degenerate identity-in-named-terms lowering, the §1d smell the redirect names; cycle-050 D8 verify-body audit `reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md` DEMOTE-OK.) The substantive rotation in the chain is the L1>L0 leaf-mutation rotation: the apply's single elementwise product lowers to Palace's in-place `forall_switch` element-loop (`Y[i] = DI[i] * X[i]`, `palace/linalg/jacobi.cpp:38`), captured by the firm L1>L0 theme [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) (sub-pattern B) and the constructed-operator-closure theme [`jacobi-smoother-mutation-rotation`](../L1-L0/jacobi-smoother-mutation-rotation.md). The L3>L2 hop is by contrast a layer-coherence identity (each layer is coherent within itself), not an algebraic one; with no non-adjacent `L3-L1/` directory created — the transitive L3>L1 identity is annotated in-line per the cycle-012 non-adjacent-identity convention (precedent: the firm L3 `dot` / `scal` / `apply_linop` cohort, all of which note their identity rotations in-line).
```

```edit:book/src/L3/jacobi-smoother.md
[old]: L3 `jacobi-smoother` lowers to the **present adjacent L2 floor** [`jacobi-smoother`](../L2/jacobi-smoother.md) (cycle-042) via the `jacobi-smoother-body-identity` L3>L2 theme, and onward to L1 [`jacobi-smoother`](../L1/jacobi-smoother.md) — **no non-adjacent L3-L1 directory**. The rotation is identity-in-form on the constructed-operator-gate apply: L1, L2, and L3 all see `jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same three-non-law set, and the same two-orthogonal-plus-one-absorbed variant profile. The L2 floor is the standalone constructed-operator-gate floor (cycle-042) — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**. The L3>L2 hop is a layer-coherence rotation (each layer is coherent within itself), not an algebraic one; the L3>L2 identity-in-form annotation is captured by the adjacent-edge theme, and the transitive L3>L1 identity is annotated in-line here (precedent: the firm L3 `dot` / `scal` / `apply_linop` cohort, cycle-011, all of which note their identity rotations in-line; cycle-012 non-adjacent-identity convention).
[new]: L3 `jacobi-smoother` lowers to the **present adjacent L2 floor** [`jacobi-smoother`](../L2/jacobi-smoother.md) (cycle-042) and onward to L1 [`jacobi-smoother`](../L1/jacobi-smoother.md) — **no non-adjacent L3-L1 directory**. The L3>L2 rotation is a **degenerate identity-in-named-terms lowering**, annotated in-line here rather than as a dedicated L3>L2 theme file: L1, L2, and L3 all see `jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]` with the same shape contract, the same six algebraic laws, the same three-non-law set, and the same two-orthogonal-plus-one-absorbed variant profile — no vocabulary shift across the edge to rotate. The L2 floor is the standalone constructed-operator-gate floor (cycle-042) — so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**. (The former `jacobi-smoother-body-identity` L3>L2 theme file was demoted to this in-line identity note cycle-051 under the 2026-06-01 VOCABULARY-SHIFT REDIRECT `METHODOLOGY-REDIRECT.md`; cycle-050 D8 verify-body audit DEMOTE-OK, `reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`.) The transitive L3>L1 identity is likewise annotated in-line (precedent: the firm L3 `dot` / `scal` / `apply_linop` cohort, cycle-011, all of which note their identity rotations in-line; cycle-012 non-adjacent-identity convention).
```

### 3. Re-anchor `book/src/L2/jacobi-smoother.md` (frontmatter + §"Lowers to") — in-line §"Downward to L1" note

The frontmatter `lowers_to` names the thin L2>L1 theme by slug (`jacobi-smoother-apply-identity`, a D8 plain-text forward-ref that never landed; the on-disk theme is `jacobi-smoother-leaf-identity`). Re-anchor the frontmatter to drop the theme reference and the §"Lowers to" body to an in-line identity note.

```edit:book/src/L2/jacobi-smoother.md
[old]:   - book/src/L1/jacobi-smoother.md (identity-in-form on the constructed-operator-gate apply; the apply is a single whole-tensor elementwise product with no kernel fusion to unfold — the L2>L1 theme is the thin `jacobi-smoother-apply-identity` D8 this cycle; the substantive leaf-mutation rotation lives at L1>L0 reciprocal-elementwise-product-mutation-rotation sub-pattern B + jacobi-smoother-mutation-rotation)
[new]:   - book/src/L1/jacobi-smoother.md (identity-in-form on the constructed-operator-gate apply; the apply is a single whole-tensor elementwise product with no kernel fusion to unfold — the L2>L1 rotation is a degenerate identity-in-named-terms lowering annotated in-line in §"Lowers to", no dedicated theme file as of cycle-051 demotion; the substantive leaf-mutation rotation lives at L1>L0 reciprocal-elementwise-product-mutation-rotation sub-pattern B + jacobi-smoother-mutation-rotation)
```

```edit:book/src/L2/jacobi-smoother.md
[old]: L2 `jacobi-smoother` lowers to L1 [`jacobi-smoother`](../L1/jacobi-smoother.md)
via an **identity-in-form** rotation: both layers see `jacobi_smoother :: (op:
JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]` with the same shape contract, the
same six algebraic laws, the same non-law set, and the same two-orthogonal-plus-one-absorbed
variant profile. There is **no kernel fusion to unfold** — the apply is a single
elementwise product (the negative fusion observation above). The thin L2>L1 theme
`jacobi-smoother-apply-identity` (D8 this cycle — plain-text forward-reference,
file not yet on disk) narrates the identity rotation; this entry captures it
in-line following the `scal` / `dot` / `nrm2` L2-floor precedent for in-line
identity-rotation annotation.
[new]: L2 `jacobi-smoother` lowers to L1 [`jacobi-smoother`](../L1/jacobi-smoother.md)
via a **degenerate identity-in-named-terms** rotation, annotated in-line here
rather than as a dedicated L2>L1 theme file: both layers see `jacobi_smoother ::
(op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]` with the same shape contract,
the same six algebraic laws, the same non-law set, and the same
two-orthogonal-plus-one-absorbed variant profile. There is **no kernel fusion to
unfold** — the apply is a single elementwise product (the negative fusion
observation above), so there is no vocabulary shift across the edge to rotate.
(The former `jacobi-smoother-leaf-identity` L2>L1 theme file was demoted to this
in-line note cycle-051 under the 2026-06-01 VOCABULARY-SHIFT REDIRECT
`METHODOLOGY-REDIRECT.md` — a degenerate identity-in-named-terms lowering, the §1d
smell the redirect names; cycle-050 D8 verify-body audit DEMOTE-OK,
`reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`.)
This follows the `scal` / `dot` / `nrm2` L2-floor precedent for in-line
identity-rotation annotation.
```

### 4. Re-anchor `book/src/L3/divfree-projector.md` (frontmatter + §Context "Downward" + §"Lowers to") — in-line §"Downward to L2" note pointing onward to BOTH the L2 floor AND the KEPT L2>L1 fusion theme

The reachability constraint (OQ `divfree-l3-l2-demotion-must-keep-l2-floor-and-l2-l1-fusion-reachable`): the new in-line note MUST point onward to BOTH `L2/divfree-projector.md` (the floor) AND `L2-L1/divfree-projector-leaf-identity.md` (the KEPT step-4 fusion rotation) so the one genuine rotation in the projector chain stays reachable from the L3 entry.

```edit:book/src/L3/divfree-projector.md
[old]:   - book/src/L2/divfree-projector.md (identity-in-form on the constructed-operator-gate apply; lowers through the present adjacent L2 floor via the `divfree-projector-body-identity` L3>L2 theme — the four-step apply is a fixed straight-line composition whose L2 floor form is value-thread-isomorphic by signature shape; the substantive leaf-mutation rotation lives at L1>L0 divfree-projector-mutation-rotation, and the inner-solve obstruction is carried BY REFERENCE through the firm-L3 ksp_solve dependency, never introduced or erased here)
[new]:   - book/src/L2/divfree-projector.md (identity-in-form on the constructed-operator-gate apply; lowers through the present adjacent L2 floor — the L3>L2 rotation is a degenerate identity-in-named-terms lowering annotated in-line in §"Lowers to" as of cycle-051 demotion, no dedicated L3>L2 theme file; the four-step apply WeakDiv→Z→ksp_solve→Grad is a fixed straight-line composition whose L2 floor form is value-thread-isomorphic by signature shape. The ONE genuine fusion rotation in the chain lives on the L2>L1 edge: the step-4 Grad->AddMult re-fusion, captured by the KEPT firm theme book/src/L2-L1/divfree-projector-leaf-identity.md — reachable onward from the L2 floor, not orphaned. The substantive leaf-mutation rotation lives at L1>L0 divfree-projector-mutation-rotation; the inner-solve obstruction is carried BY REFERENCE through the firm-L3 ksp_solve dependency, never introduced or erased here)
```

```edit:book/src/L3/divfree-projector.md
[old]: - **Downward** to L2/L1: `divfree-projector` lowers to the **present adjacent L2 floor**
  [`divfree-projector`](../L2/divfree-projector.md) (cycle-042) via the
  `divfree-projector-body-identity` L3>L2 theme, and onward to L1
  [`divfree-projector`](../L1/divfree-projector.md). The rotation is **identity-in-form on the
  constructed-operator-gate apply** — L1, L2, and L3 all see
  `divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]`
  with the same shape contract, the same five algebraic laws (plus the two
  load-bearing non-laws), and the same element-type variant axis. The L2 floor is the
  same-named fusion-rotation floor under the firm L3 gate (cycle-042); the L3>L2 hop passes
  through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings
  still require both L levels**. The substantive rotation in the chain is the L1>L0
  leaf-mutation rotation: the four-step apply lowers to Palace's in-place `Mult(VecType &y)`
  mutation idiom, captured by the firm L1>L0 theme
  [`divfree-projector-mutation-rotation`](../L1-L0/divfree-projector-mutation-rotation.md).
  The L3>L2 hop is a layer-coherence rotation (each layer is coherent within itself),
  not an algebraic one; the L3>L2 identity-in-form annotation is captured by the adjacent-edge
  `divfree-projector-body-identity` theme, with no non-adjacent `L3-L1/` directory created —
  the transitive L3>L1 identity is annotated in-line per the cycle-012 non-adjacent-identity
  convention (precedent: the firm L3 `jacobi-smoother` / `apply_linop` / `dot` / `scal`
  cohort, all of which note their identity rotations in-line).
[new]: - **Downward** to L2/L1: `divfree-projector` lowers to the **present adjacent L2 floor**
  [`divfree-projector`](../L2/divfree-projector.md) (cycle-042) and onward to L1
  [`divfree-projector`](../L1/divfree-projector.md). The L3>L2 rotation is a **degenerate
  identity-in-named-terms lowering**, annotated in-line here (no dedicated L3>L2 theme file):
  L1, L2, and L3 all see
  `divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]`
  with the same shape contract, the same five algebraic laws (plus the two load-bearing
  non-laws), and the same element-type variant axis. The four-step composition
  `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad` is **explicit and value-thread-isomorphic at
  BOTH L3 and L2** (the composition is not exposed at one layer and collapsed at the other —
  there is no vocabulary shift across the L3>L2 edge to rotate). The L2 floor is the
  same-named floor under the firm L3 gate (cycle-042); the L3>L2 hop passes through the
  adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require
  both L levels**. (The former `divfree-projector-body-identity` L3>L2 theme file was demoted
  to this in-line identity note cycle-051 under the 2026-06-01 VOCABULARY-SHIFT REDIRECT
  `METHODOLOGY-REDIRECT.md`; cycle-050 D8 verify-body audit DEMOTE-OK,
  `reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`.)
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
  identity is annotated in-line per the cycle-012 non-adjacent-identity convention (precedent:
  the firm L3 `jacobi-smoother` / `apply_linop` / `dot` / `scal` cohort, all of which note
  their identity rotations in-line).
```

```edit:book/src/L3/divfree-projector.md
[old]: L3 `divfree-projector` lowers to the **present adjacent L2 floor**
[`divfree-projector`](../L2/divfree-projector.md) (cycle-042) via the
`divfree-projector-body-identity` L3>L2 theme, and onward to L1
[`divfree-projector`](../L1/divfree-projector.md) — **no non-adjacent L3-L1 directory**.
The rotation is identity-in-form on the constructed-operator-gate apply: L1, L2, and L3
all see `divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]`
with the same shape contract, the same five algebraic laws, the same two-non-law set, and
the same one-orthogonal-plus-one-absorbed variant profile. The L2 floor is the same-named
fusion-rotation floor under the firm L3 gate (cycle-042); the L3>L2 hop passes through the
adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require
both L levels**. The L3>L2 hop is a layer-coherence rotation (each layer is coherent within
itself), not an algebraic one; the L3>L2 identity-in-form annotation is captured by the
adjacent-edge theme, and the transitive L3>L1 identity is annotated in-line here (precedent:
the firm L3 `jacobi-smoother` / `apply_linop` / `dot` / `scal` cohort, all of which note their
identity rotations in-line; cycle-012 non-adjacent-identity convention).
[new]: L3 `divfree-projector` lowers to the **present adjacent L2 floor**
[`divfree-projector`](../L2/divfree-projector.md) (cycle-042) and onward to L1
[`divfree-projector`](../L1/divfree-projector.md) — **no non-adjacent L3-L1 directory**.
The L3>L2 rotation is a **degenerate identity-in-named-terms lowering**, annotated in-line
here rather than as a dedicated L3>L2 theme file: L1, L2, and L3 all see
`divfree_project :: (P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]`
with the same shape contract, the same five algebraic laws, the same two-non-law set, and
the same one-orthogonal-plus-one-absorbed variant profile. The four-step composition
`WeakDiv → Z_{bdr_eff} → ksp_solve → Grad` is explicit and value-thread-isomorphic at BOTH
L3 and L2 — no vocabulary shift across the edge to rotate. The L2 floor is the same-named
floor under the firm L3 gate (cycle-042); the L3>L2 hop passes through the adjacent floor
rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.
(The former `divfree-projector-body-identity` L3>L2 theme file was demoted to this in-line
identity note cycle-051 under the 2026-06-01 VOCABULARY-SHIFT REDIRECT
`METHODOLOGY-REDIRECT.md`; cycle-050 D8 verify-body audit DEMOTE-OK,
`reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`.)
**The ONE genuine fusion rotation in the projector chain lives on the L2>L1 edge, not this
one**: the step-4 `Grad->AddMult` apply-accumulate (`palace/linalg/divfree.cpp:185` real /
`:180-181` complex) de-fuses at L2 into `apply_linop(P.Grad, ψ) ▷ axpy` and re-fuses at L1,
captured by the KEPT firm theme
[`divfree-projector-leaf-identity`](../L2-L1/divfree-projector-leaf-identity.md) — reachable
directly from this L3 entry via the live link above (not via the L2 floor, which carries no
live link to the KEPT theme), so not orphaned by this demotion. The L3>L2 hop is a layer-coherence
identity (each layer is coherent within itself), not an algebraic one; the transitive L3>L1
identity is annotated in-line here (precedent: the firm L3 `jacobi-smoother` / `apply_linop`
/ `dot` / `scal` cohort, all of which note their identity rotations in-line; cycle-012
non-adjacent-identity convention).
```

### 5. SUMMARY.md — remove the 3 deleted-slug lines (KEEP the divfree-leaf-identity line 105)

```edit:book/src/SUMMARY.md
[old]: - [jacobi-smoother-body-identity](./L3-L2/jacobi-smoother-body-identity.md)
- [divfree-projector-body-identity](./L3-L2/divfree-projector-body-identity.md)
[new]:
```

```edit:book/src/SUMMARY.md
[old]: - [jacobi-smoother-leaf-identity](./L2-L1/jacobi-smoother-leaf-identity.md)
[new]:
```

(The blank-line removals collapse cleanly; mdBook's SUMMARY parser tolerates the resulting adjacency. The `divfree-projector-leaf-identity` SUMMARY line 105 is NOT touched.)

### 6. `book/src/L3-L2/index.md` — remove D4's two `-body-identity` rows + the working-notes bullets for the 2 deleted L3>L2 slugs (KEEP the divfree-leaf-identity content; it is an L2>L1 slug not present in this index's rows)

Remove the dep-map table rows (lines 21, 22):

```edit:book/src/L3-L2/index.md
[old]: | [`jacobi-smoother-body-identity`](./jacobi-smoother-body-identity.md) | L3 [`jacobi-smoother`](../L3/jacobi-smoother.md) §Signature — the whole-tensor field operation `jacobi_smoother :: (op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]`; constructed-operator gate, **no iteration view, no sequential obstruction** (one elementwise product `op.dinv ⊙ x`). | L2 [`jacobi-smoother`](../L2/jacobi-smoother.md) §Signature — the constructed-operator-gate floor (cycle-042 D5); identical signature, single elementwise-product apply; **negative fusion observation** (no fused multi-operation kernel to unfold). | `structural` (whole-tensor signature, no element loop, no iteration view, no obstruction, **NO fold-parent** — `krylov-step-body-identity` point-3 condition specialized to the standalone constructed-operator gate) + secondary `empirical-match` (firm L3 entry cycle-037 + cycle-036 D2 audit `L3/index.md:46` "thinnest constructed-operator gate" classification) | `firm` (cycle-042 D8 abstractor; identity-in-form on the body, **no wrapper to rotate** — the constructed-operator-gate counterpart of the BLAS-1-leaf `scal-body-identity`; **fork-INDEPENDENT**) |
| [`divfree-projector-body-identity`](./divfree-projector-body-identity.md) | L3 [`divfree-projector`](../L3/divfree-projector.md) §Signature — the whole-tensor constructed-operator gate `divfree_project :: (P, y) -> Field[N_nd]`; fixed four-step body `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad`, **no projector-level iteration** (only loop interior to step-3 `ksp_solve`, carried by reference). | L2 [`divfree-projector`](../L2/divfree-projector.md) §Signature — the same-named fusion-rotation floor (moderate floor under the firm L3 gate); value-thread-isomorphic four-step body; step-4 `AddMult` de-fusion is the L2>L1 edge's content, NOT this edge's. | `structural` (the four-step gate body exposes no per-projector iteration at either layer — constructed-operator-gate analogue of `krylov-step-body-identity.md:97` L3-native; no wrapper to rotate, the gate has no `(op,K,s)` tuple/outer loop) + secondary `empirical-match` (L3 + L2 floors independently authored value-thread-isomorphic to the firm L1 gate) | `firm` (cycle-042 wave-2 D9 abstractor; identity-in-form on the four-step body — constructed-operator-gate analogue of the BLAS-1-leaf `-body-identity` cohort; inner-solve obstruction carried BY REFERENCE; **standalone gate — fork-independent of `dot-l2-leaf-floor-vs-fold-only-design`**) |
[new]:
```

Update the §Working-Notes cohort note (line 43) — the two gate edges are now demoted, not "remain theme files this cycle":

```edit:book/src/L3-L2/index.md
[old]: *Fork-INDEPENDENT standalone-floor / gate body edges (cycle-042; originally five fork-INDEPENDENT L2-floor edges, each with **NO fold-parent**; the leaf/gate-primitive analogue of `krylov-step-body-identity` with NO wrapper rotation). **Three were demoted to in-line notes cycle-050** (`assemble-diagonal-body-identity`, `reciprocal-body-identity`, `elementwise-product-body-identity` — degenerate identity-in-named-terms lowerings, per the 2026-06-01 vocabulary-shift redirect); the **two constructed-operator-gate edges below remain theme files this cycle** (`jacobi-smoother-body-identity`, `divfree-projector-body-identity`) and are both DEMOTE-OK for cycle-051 per the D8 verify-body audit — see the §Working-Notes cycle-050-vs-051 split:*
[new]: *Fork-INDEPENDENT standalone-floor / gate body edges (cycle-042; originally five fork-INDEPENDENT L2-floor edges, each with **NO fold-parent**; the leaf/gate-primitive analogue of `krylov-step-body-identity` with NO wrapper rotation). **All five were demoted to in-line §"Downward to L2" notes** — three cycle-050 (`assemble-diagonal-body-identity`, `reciprocal-body-identity`, `elementwise-product-body-identity`), the **two constructed-operator-gate edges cycle-051** (`jacobi-smoother-body-identity`, `divfree-projector-body-identity`, both DEMOTE-OK per the D8 verify-body audit) — as degenerate identity-in-named-terms lowerings per the 2026-06-01 VOCABULARY-SHIFT REDIRECT. Each operator's L3>L2 identity rotation remains captured in-line on the standalone L3 entry (none has a fold-parent, so no operator chapter collapses); see the §Working-Notes cycle-050-vs-051 split:*
```

Remove the two demoted-slug bullets (lines 46, 47):

```edit:book/src/L3-L2/index.md
[old]: - `jacobi-smoother-body-identity` — the L3 whole-tensor `jacobi-smoother` constructed-operator-gate field operation lowers to the L2 same-named gate floor; the body IS the identity (one elementwise product `op.dinv ⊙ x`), no wrapper to rotate; fork-INDEPENDENT, the thinnest constructed-operator-gate member.
- `divfree-projector-body-identity` — the L3 whole-tensor `divfree-projector` four-step gate lowers to the L2 same-named floor value-thread-isomorphic on the four-step body (`WeakDiv → Z_{bdr_eff} → ksp_solve → Grad`); inner-solve obstruction carried BY REFERENCE; the step-4 `AddMult` de-fusion is the L2>L1 edge's content, NOT this edge's; standalone gate — fork-independent.
[new]: - `jacobi-smoother-body-identity` / `divfree-projector-body-identity` — **DEMOTED cycle-051** (D4) to in-line §"Downward to L2" identity notes on `book/src/L3/jacobi-smoother.md` / `book/src/L3/divfree-projector.md` respectively, per the 2026-06-01 VOCABULARY-SHIFT REDIRECT (both DEMOTE-OK per the D8 verify-body audit `reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`). The Jacobi body is the degenerate identity (one elementwise product `op.dinv ⊙ x`, no wrapper to rotate); the divfree four-step body `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad` is value-thread-isomorphic at both layers with the inner-solve obstruction carried BY REFERENCE — the step-4 `AddMult` re-fusion is the L2>L1 edge's content (the KEPT `L2-L1/divfree-projector-leaf-identity` theme), NOT this edge's. Both rotations remain captured as in-line notes; the theme files are deleted.
```

Update the cohort-growth bullet (line 61) — the cycle-050 count `17 → 13` now drops by 2 more to `11` with these two demotions, and the "NEXT (cycle-051)" framing is now enacted:

```edit:book/src/L3-L2/index.md
[old]: - **Cohort growth (firm 17 → 13; cycle-050 degenerate-theme demotion).** Cycle-050 (the refactor-pass enactment under the 2026-06-01 VOCABULARY-SHIFT REDIRECT; `METHODOLOGY-REDIRECT.md`) **demoted four thin `-body-identity` L3>L2 themes to in-line §"Downward to L2" notes** on their L3 operator entries: `assemble-diagonal-body-identity` (D3), `elementwise-product-body-identity` (D4), `reciprocal-body-identity` (D5), `normalize-body-identity` (D6). Each was a degenerate identity-in-named-terms lowering (same signature / same laws / same variant profile across the edge — the §1d smell the redirect names), so its dedicated theme chapter was deleted and its one load-bearing fact folded into an in-line note on the standalone L3/L2 operator entry (none has a fold-parent, so no operator chapter collapses). **The L3>L2 rotation for each operator remains captured** (now as an in-line identity note, not a theme file) — the coverage-gap is unaffected in *kind*; only the firm-theme COUNT drops, **17 → 13** (4 thin-identity themes deleted; the 4 substantive themes + the remaining 9 thin-identity themes stay). The remaining cohort: thin `-body-identity` (9) — `krylov-step`, `dot`, `nrm2`, `scal`, `axpy`, `axpby`, `axpbypcz`, `jacobi-smoother`, `divfree-projector`; substantive / non-identity (4) — `ksp-solve-outer-driver`, `orthogonalize-variant-split`, `eigsolve-opaque-eigen-iteration`, `chebyshev-nested-recurrence`. **`jacobi-smoother-body-identity` + `divfree-projector-body-identity` are NEXT (cycle-051)** — both DEMOTE-OK per the D8 verify-body audit (`reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`); they were not demoted this cycle because they are the gated constructed-operator-gate pairs the c049 D3 audit flagged "verify-body-before-demoting" (the audit completed only this cycle). See the cycle-050-vs-051 split note below. *(Prior — coverage-gap history, retained:* cohort grew firm 2→5→10→14→15→17 across cycles 041–045; the `l3-l2-rotation-theme-coverage-gap` reached 17-of-18 effectively complete at cycle-045, the residual 1 being `apply_linop` (lowers L3→L1 directly, no L2 entry / no L3-L2 theme by design — the cycle-010 "CONFIRMED-NOT-NEEDED-WITH-CAVEAT"). The cycle-050 demotion does NOT re-open the coverage-gap: the demoted operators' rotations are captured in-line, not lost.)*
[new]: - **Cohort growth (firm 17 → 13 cycle-050 → 11 cycle-051; degenerate-theme demotion).** The refactor-pass enactment under the 2026-06-01 VOCABULARY-SHIFT REDIRECT (`METHODOLOGY-REDIRECT.md`) **demoted six thin `-body-identity` L3>L2 themes to in-line §"Downward to L2" notes** on their L3 operator entries across two cycles. Cycle-050 (D3–D6): `assemble-diagonal-body-identity`, `elementwise-product-body-identity`, `reciprocal-body-identity`, `normalize-body-identity`. **Cycle-051 (D4): `jacobi-smoother-body-identity` + `divfree-projector-body-identity`** — the two gated constructed-operator-gate pairs the c049 D3 audit flagged "verify-body-before-demoting", both confirmed DEMOTE-OK by the D8 verify-body audit (`reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`). Each was a degenerate identity-in-named-terms lowering (same signature / same laws / same variant profile across the edge — the §1d smell the redirect names), so its dedicated theme chapter was deleted and its load-bearing facts folded into an in-line note on the standalone L3 operator entry (none has a fold-parent, so no operator chapter collapses). **The L3>L2 rotation for each operator remains captured** (now as an in-line identity note, not a theme file) — the coverage-gap is unaffected in *kind*; only the firm-theme COUNT drops, **17 → 13 → 11** (6 thin-identity themes deleted; the 4 substantive themes + the remaining 7 thin-identity themes stay). The remaining cohort: thin `-body-identity` (7) — `krylov-step`, `dot`, `nrm2`, `scal`, `axpy`, `axpby`, `axpbypcz`; substantive / non-identity (4) — `ksp-solve-outer-driver`, `orthogonalize-variant-split`, `eigsolve-opaque-eigen-iteration`, `chebyshev-nested-recurrence`. *(Prior — coverage-gap history, retained:* cohort grew firm 2→5→10→14→15→17 across cycles 041–045; the `l3-l2-rotation-theme-coverage-gap` reached 17-of-18 effectively complete at cycle-045, the residual 1 being `apply_linop` (lowers L3→L1 directly, no L2 entry / no L3-L2 theme by design — the cycle-010 "CONFIRMED-NOT-NEEDED-WITH-CAVEAT"). The cycle-050/051 demotion does NOT re-open the coverage-gap: the demoted operators' rotations are captured in-line, not lost.)*
```

### 7. `book/src/L2-L1/index.md` — remove D4's `jacobi-smoother-leaf-identity` row + working-notes bullet (KEEP the `divfree-projector-leaf-identity` row 27 + bullet 62)

Remove the dep-map row (line 22):

```edit:book/src/L2-L1/index.md
[old]: | [jacobi-smoother-leaf-identity](./jacobi-smoother-leaf-identity.md) | `L2/jacobi-smoother` (firm, cycle-042 D5 gate floor) | `L1/jacobi-smoother` (firm constructed-operator gate) | firm *(structural; identity-in-form on the constructed-operator gate — value-thread-isomorphic signature, single elementwise-product apply; **fork-INDEPENDENT, NO fold-parent** — the cycle-041 `dot-l2-leaf-floor-vs-fold-only-design` leaf-vs-fold fork does NOT reach it; the L2 fusion-rotation observation is **negative** (no fused multi-operation kernel to unfold), so the edge is identity with the fusion treatment a documented no-op — NOT a fold deferral; substantive rotation deferred to L1>L0 `reciprocal-elementwise-product-mutation-rotation` sub-pattern B + `jacobi-smoother-mutation-rotation`)* |
[new]:
```

Update the working-notes bullet (line 61) to mark it demoted (the `divfree-projector-leaf-identity` bullet 62 is NOT touched):

```edit:book/src/L2-L1/index.md
[old]: - `jacobi-smoother-leaf-identity` — the L2 `jacobi-smoother` constructed-operator-gate floor lowers to the L1 gate identity-in-form on the apply (single elementwise product); **fork-INDEPENDENT, NO fold-parent**; the L2 fusion observation is **negative** (no fused multi-operation kernel), so the edge is identity with the fusion treatment a documented no-op (NOT a fold deferral). *(DEMOTE-OK per the D8 verify-body audit; scheduled cycle-051 — still a theme file this cycle.)*
[new]: - `jacobi-smoother-leaf-identity` — **DEMOTED cycle-051** (D4) to an in-line §"Downward to L1" identity note on `book/src/L2/jacobi-smoother.md`, per the 2026-06-01 VOCABULARY-SHIFT REDIRECT (DEMOTE-OK per the D8 verify-body audit `reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`). The L2 `jacobi-smoother` constructed-operator-gate floor lowers to the L1 gate identity-in-form on the apply (single elementwise product); **fork-INDEPENDENT, NO fold-parent**; the L2 fusion observation is **negative** (no fused multi-operation kernel), so the edge is a degenerate identity-in-named-terms lowering with the fusion treatment a documented no-op. The rotation remains captured in-line; the theme file is deleted.
```

### 7b. `book/src/L2-L1/divfree-projector-leaf-identity.md` (KEPT file) — defensive de-link of its ONE live inbound-style link to the deleted `divfree-projector-body-identity` slug

This is the only surviving **live markdown link** to a D4-deleted slug (line 36). Deleting the body-identity file without re-anchoring this link is a hard `linkcheck2` build error. Per scope (d) (re-anchor inbound live links to the 3 deleted slugs), re-anchor it to the in-line note on the L3 entry. The KEPT file otherwise stays a standalone theme; this is a minimal de-link, not a content edit.

```edit:book/src/L2-L1/divfree-projector-leaf-identity.md
[old]: The edge is the **mostly-identity-in-form** case with **one genuine fusion rotation**. This is the
sibling of the L3>L2 [`divfree-projector-body-identity`](../L3-L2/divfree-projector-body-identity.md)
theme (the identity-in-form edge above it). The two themes split the projector's lowering story:
[new]: The edge is the **mostly-identity-in-form** case with **one genuine fusion rotation**. This is the
sibling of the L3>L2 identity-in-form rotation — the degenerate `divfree-projector-body-identity`
lowering demoted cycle-051 (D4) to an in-line §"Downward to L2" note on the L3 entry
[`divfree-projector`](../L3/divfree-projector.md) (above it). The two edges split the projector's
lowering story:
```

Update the cohort-growth-log lead (line 73) — note the cycle-051 D4 demotion of `jacobi-smoother-leaf-identity` (the `divfree-projector-leaf-identity` KEEP is already correctly recorded there and is NOT changed):

```edit:book/src/L2-L1/index.md
[old]: **NOTE the cycle-050-vs-051 split (see also `L3-L2/index.md` §Working-Notes):** the fold-family pairs (`scal`/`axpy`/`axpby`/`axpbypcz`-`leaf-identity` → collapse into the new firm `linear_combination`; `dot-leaf-identity` → collapse into the new firm `inner_product`; `nrm2-leaf-identity` STAYS — `nrm2` is a do-NOT-merge consumer) + the `jacobi-smoother-leaf-identity` (DEMOTE-OK per D8) are **cycle-051**. **`divfree-projector-leaf-identity` is NOT demoted — KEEP-substantive**
[new]: **NOTE the cycle-050-vs-051 split (see also `L3-L2/index.md` §Working-Notes):** the fold-family pairs (`scal`/`axpy`/`axpby`/`axpbypcz`-`leaf-identity` → collapse into the new firm `linear_combination`; `dot-leaf-identity` → collapse into the new firm `inner_product`; `nrm2-leaf-identity` STAYS — `nrm2` is a do-NOT-merge consumer) are **cycle-051**; the `jacobi-smoother-leaf-identity` was **DEMOTED cycle-051 (D4)** to an in-line note on `book/src/L2/jacobi-smoother.md` (DEMOTE-OK per D8). **`divfree-projector-leaf-identity` is NOT demoted — KEEP-substantive**
```

## Discipline notes

- **DISPATCH-phase discipline observed.** All artifact changes are proposed-changes blocks; no direct write to `book/`. The 3 deletions are `delete:` blocks; the 6 re-anchored entries/indexes + SUMMARY are `edit:` blocks.
- **Pure structural rewrite.** No content authored. Every demoted edge's load-bearing facts (the single-elementwise-product apply for Jacobi; the four-step composition + the by-reference inner-solve obstruction for divfree) are preserved verbatim in the in-line notes. The KEPT `divfree-projector-leaf-identity` theme is untouched (file, SUMMARY line, L2-L1 index row 27, working-notes bullet 62 all survive).
- **Reachability constraint satisfied (the one non-mechanical subtlety).** The new in-line §"Downward to L2" note on `book/src/L3/divfree-projector.md` (both the §Context "Downward" bullet and the §"Lowers to" section) points onward to BOTH the L2 floor [`L2/divfree-projector.md`](book/src/L2/divfree-projector.md) AND the KEPT [`L2-L1/divfree-projector-leaf-identity.md`](book/src/L2-L1/divfree-projector-leaf-identity.md) fusion theme, with the step-4 `Grad->AddMult` re-fusion fact named explicitly and L0-anchored. The one genuine fusion rotation in the projector chain is reachable **directly from the L3 entry** via the in-line note's live link to the KEPT theme — the L2 floor entry (`L2/divfree-projector.md`) itself carries no live link to the KEPT theme (only descriptive prose), so the load-bearing reachability is provided by the direct L3→KEPT-theme link, not via the L2 floor. The genuine rotation is reachable and not orphaned (OQ `divfree-l3-l2-demotion-must-keep-l2-floor-and-l2-l1-fusion-reachable`).
- **Layer-definition discipline (high→low) preserved.** All in-line notes narrate the rewrite forward (L3 into L2, L2 into L1); no L_n→L_{n+1} lift prose introduced into the chapter content.
- **De-link scope (d) — defensive de-link of inbound live links to the 3 deleted slugs.** Grep found inbound references in: (i) the L3/L2 operator entries being re-anchored above (handled, §§2–4), (ii) SUMMARY + the two indexes (handled, §§5–7), (iii) the deleted theme files themselves (`jacobi-smoother-body-identity` ↔ `jacobi-smoother-leaf-identity` cross-references — these vanish with the files), and (iv) **the KEPT `book/src/L2-L1/divfree-projector-leaf-identity.md`, which carries one LIVE markdown link** to `divfree-projector-body-identity` at its line 36 (`[\`divfree-projector-body-identity\`](../L3-L2/divfree-projector-body-identity.md)`). That is the only surviving live inbound link to a D4-deleted slug and WOULD dangle (hard `linkcheck2` error) — re-anchored to the L3 entry's in-line note in §7b. The dispatch brief's note that the deleted body-identity slugs "link to scal/dot/nrm2-body-identity (D1/D2/D3)" concerns links FROM the deleted files (which vanish with them), not TO them.
- **TALLY deferred to D5** per the dispatch brief. This report removes only D4's OWN SUMMARY lines (3) + dep-map rows (3 — two in L3-L2/index.md, one in L2-L1/index.md) + working-notes bullets for the 3 deleted slugs, and updates the cohort-count narratives. The consolidated cross-dispatch TALLY (final firm counts across D1–D4) is D5's.
- **Prose-correction (bounded, recorded):** in `book/src/L3/jacobi-smoother.md` §Context "Downward" I added the missing L0 anchor `palace/linalg/jacobi.cpp:38` to the `Y[i] = DI[i] * X[i]` kernel mention (it cited the kernel form but not the line); verified this invocation via `citecheck --anchor 'DI[i] * X[i]'` → `[ok] :38`. Supported directly by the L0 source the entry's own §Evidence already cites at `:38`. Bounded (adding a drifted-absent line anchor to an existing claim), not re-architecting.

## Supporting evidence

- **D8 verdict source:** `reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md` (integrated, commit `6985e03`) — the three DEMOTE-OK verdicts (jacobi both edges + divfree-body-identity) + the one KEEP-substantive (`divfree-projector-leaf-identity`) + the 17-denominator correction + the reachability OQ.
- **On-disk filename verification (`ls`):** all 4 theme files confirmed present before proposing deletes; `book/src/L2/divfree-projector.md` (L2 floor) + `book/src/L2-L1/divfree-projector-leaf-identity.md` (KEPT) confirmed present as reachability targets.
- **L0 anchors self-verified this invocation (`tools/citecheck/citecheck.py --anchor` against on-disk `reference/palace/`):**
  - `palace/linalg/jacobi.cpp:38` — `DI[i] * X[i]` → `[ok] :38` (the single Jacobi elementwise-multiply kernel; the preserved Jacobi load-bearing fact).
  - `palace/linalg/divfree.cpp:155-187` — `Mult` → `[ok]` anchor at `[155,162,163,167,175,180,181,185]` (the four-step apply, preserved divfree composition fact).
  - `palace/linalg/divfree.cpp:185` — `AddMult` → `[ok] :185` (real step-4 re-fusion; the KEPT-theme reachability anchor).
  - `palace/linalg/divfree.cpp:180-181` — `AddMult` → `[ok] :180,:181` (complex step-4 re-fusion).
- **Inbound-link grep:** `grep -rln` over `book/src/` for the 3 deleted slugs — all handled (entries + SUMMARY + indexes + self-referential deleted files).

## Open questions / caveats

- **RESOLVED (was a KEPT-file residual concern):** the KEPT `book/src/L2-L1/divfree-projector-leaf-identity.md` carried one LIVE markdown link to the deleted `divfree-projector-body-identity` slug (line 36, confirmed via `grep -nE "\]\([^)]*divfree-projector-body-identity"`). This is a defensive-de-link in scope (d), so I handled it in §7b (re-anchored to the L3 entry's in-line note) rather than deferring — leaving it would be a hard `linkcheck2` build break. The de-link is minimal (sibling-pointer prose only); the KEPT theme's substantive content, SUMMARY line, and L2-L1 index row 27 are untouched.
- **Caveat (count arithmetic, for D5 TALLY):** this report updates the L3-L2 cohort narrative to `17 → 13 → 11` (cycle-050 demoted 4, cycle-051 D4 demotes 2 more L3>L2 themes) and the L2-L1 narrative for the single `jacobi-smoother-leaf-identity` D4 demotion. D5's consolidated TALLY should reconcile these against the D1/D2/D3 fold-family collapses (`scal`/`axpy`/`axpby`/`axpbypcz`/`dot`-`leaf-identity` + their `-body-identity` partners) — D4's deletions are 3 theme files; D5 owns the final cross-dispatch firm counts.
- **Caveat (inherited, not a status reduction):** both divfree entries carry the `divfree-mult-doc-irrotational-vs-divfree-stale` per-method doc-inversion OQ (`palace/linalg/divfree.hpp:64-66` vs class doc `:28-31`). Orthogonal to this demotion; untouched.
