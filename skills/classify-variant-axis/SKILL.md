---
name: classify-variant-axis
description: Given a variant axis exposed at L0 (an enum, template parameter, or runtime flag selecting between N implementations of the same algorithmic role), classify each axis-value into one of four absorption strategies for L1: constructed-operator absorption, parametric absorption, scope-out to sibling slice, or residual-axis disclosure. Applied per cycle by the Synthesizer on every multi-variant slice.
status: active
---

# classify-variant-axis

The Synthesizer encounters a variant axis whenever the L0 source dispatches between N implementations of the same algorithmic role — `pc_side ∈ {LEFT, RIGHT}`, `gs_orthog ∈ {MGS, CGS, CGS2, Householder}`, `variant ∈ {1st-kind, 4th-kind}` Chebyshev, `B == null` vs. preconditioner present, etc. Choosing the absorption strategy at L1 is the central methodology decision; this skill names the four resolution paths and the criterion to pick between them.

## The four absorption paths

1. **Constructed-operator absorption** (preferred when applicable). The variant is absorbed into a constructed operator carrying the axis as immutable closure state. L1 procedure references the operator's `apply_linop` interface; the inner loop is variant-uniform. Achieves all three levels of absorption (invariant, procedural, primitive-sequence). See [`constructed-operators`](../../book/src/concepts/constructed-operators.md). Example: `apply_BA` in GMRES absorbing `pc_side ∈ {LEFT, RIGHT, none}`.

2. **Parametric absorption**. The variant is a scalar / set of scalars that the L1 procedure carries through. The procedure inspects the parameter ONCE (binding / dispatch); the primitive sequence is variant-uniform. Achieves levels (a), (b), (c). Example: Chebyshev `variant ∈ {1st-kind, 4th-kind}` absorbed by selecting different `(α₀, sdₖ, srₖ)` scalar generators while the polynomial recurrence shape is invariant.

3. **Scope-out to sibling slice**. The variant's algorithmic structure is genuinely different — not just different scalars / different operator instance, but a different primitive sequence with different threaded state. Create a sibling slice with shared concept references. The original slice declares the scoped-out value in `## Scope`. Example: Householder QR vs. Gram-Schmidt orthogonalization — different threaded state (reflector sequence vs. maintained Q), different primitive sequence (reflect-and-zero vs. project-and-subtract).

4. **Residual-axis disclosure**. The variant is partially absorbed (levels (a)/(b) hold) but breaks level (c) primitive-sequence absorption — the L_{n+1} chain genuinely differs across variants. The L1 state schema explicitly declares the *residual axis* (variant-conditional state fields, parameter re-inspection sites) and the L_{n+1} prose documents the primitive-sequence divergence as a legitimate residual. Example: MGS/CGS/CGS2 orthogonalization at L2 — same L1 contract, different L2 primitive chains; CGS2 has refinement; documented as residual axis per [`variant-absorption`](../../book/src/concepts/variant-absorption.md).

## Decision criterion: which level of absorption breaks?

The right path is determined by *which absorption level the variant fails*:

- All three levels hold under one strategy → take that strategy (almost always: constructed-operator or parametric).
- Level (c) breaks but (a) and (b) hold → **residual-axis disclosure**.
- Level (a) breaks too — different invariant statement, different threaded state shape → **scope-out to sibling slice**.

Avoid silent partial absorption: if level (c) breaks and you don't disclose the residual axis, the L1 form is misrepresenting the algorithm.

## Output contract (refined meta-12 item 2; sharpened meta-14 item 2)

When the L0 source exposes **≥2 variant axes** (or ≥2 values on a single
axis), the slice MUST include a `## Variant axes` block in the L1
section (or L2 if the divergence first surfaces there). For each axis,
enumerate per-axis-value:

1. The absorption path: `constructed-operator` / `parametric` / `residual-axis` / `scope-out`.
2. **WHICH primitive carries the load-bearing variant-conditional behavior** (the primitive that differs across values; named explicitly).
3. **WHICH state fields the setup binds** (variant-conditional state, per axis-value, named).

Generic placeholders fail the contract:

- ❌ "scalars closure captures variant" — does not name primitive or state.
- ❌ "one polymorphic function over V" — does not name the primitive lift.
- ❌ "constructed-operator absorbs variant" alone — does not enumerate state binding.

Correct form (block-diagonal lift from cycle 59 divfree):

```markdown
## Variant axes

- `scalar_type` ∈ {`Vector`, `ComplexVector`}: parametric (load-bearing primitive: `kspSolve`)
  - `Vector`: `kspSolve_real(L, b, x)` operates on real vectors directly.
  - `ComplexVector`: `kspSolve_complex(L, b, x) = block_diag(kspSolve_real ∘ Re, kspSolve_real ∘ Im)` — the polymorphic instance is the block-diagonal lift of the real solve. Setup binds the real solver instance and the complex view-pair into the closure.
  - State binding: both share `(L, M, tol, maxiter)`; complex additionally captures `(view_real, view_imag)`.
```

Or for orthogonalization (cycle 23):

```markdown
## Variant axes

- `gs_orthog` ∈ {`MGS`, `CGS`, `CGS2`}: residual-axis (primitive-sequence diverges; see L2 §collective-shape)
  - `MGS`: sequential `[dot, axpy] × m` — load-bearing primitive: per-step `dot` + `axpy` with sync-per-step.
  - `CGS`: batched `[dot × m, allreduce_sum, gemv_basis]` — load-bearing primitive: `gemv_basis` (rank-1 fused).
  - `CGS2`: `[CGS chain] × 2 + [axpy_scalar]` — load-bearing primitive: refinement re-entry with stability threshold scalar.
  - State binding: shared `V[0..j]` basis; CGS2 additionally captures `refine_threshold` scalar in setup.
```

The slice's L1 state schema and procedure must be consistent — each
named state binding appears in the state types; each named primitive
appears in the procedure.

Critic check #9 verifies the block is present when L0 source has
visible axis variability; check #11 verifies the named state bindings
appear in the L1 state schema. Single-variant slices do NOT need
the block; check #9 doesn't fire.

## Cross-references

- [`variant-absorption`](../../book/src/concepts/variant-absorption.md) — three levels of absorption and the named failure modes.
- [`constructed-operators`](../../book/src/concepts/constructed-operators.md) — limits of constructed-operator absorption.
- The classification informs Critic check #9 (variant absorption); a slice that omits this classification on multi-variant L0 should fail the check.
