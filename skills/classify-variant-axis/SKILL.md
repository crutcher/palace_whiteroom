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

## Output contract (refined meta-12 item 2)

When the L0 source exposes **≥2 variant axes** (or ≥2 values on a single
axis), the slice MUST include a `## Variant axes` block in the L1
section (or L2 if the divergence first surfaces there) enumerating each
axis with its absorption path:

```markdown
## Variant axes

- `<axis_name>` ∈ { <v_a>, <v_b>, ... }: <constructed-operator (via <op_name>) | parametric (scalar `<param>`) | residual-axis (primitive-sequence diverges; see L2 §<sect>) | scoped out (sibling slice `<slice>`)>
```

The slice's L1 state schema and procedure must be consistent with this
classification — variant-conditional state fields named, dispatch points
enumerated, scoped-out values noted.

Critic check #9 (variant absorption) verifies the block is present
when the L0 source has visible axis variability. Single-variant slices
do NOT need the block; check #9 doesn't fire.

The block format makes skill uptake measurable: a cycle that touches a
multi-variant L0 source should produce a `## Variant axes` block. Absence
is the signal that classification was skipped (silent partial
absorption).

## Cross-references

- [`variant-absorption`](../../book/src/concepts/variant-absorption.md) — three levels of absorption and the named failure modes.
- [`constructed-operators`](../../book/src/concepts/constructed-operators.md) — limits of constructed-operator absorption.
- The classification informs Critic check #9 (variant absorption); a slice that omits this classification on multi-variant L0 should fail the check.
