---
name: propose-rotation
description: Produce a well-formed rotation_claim JSON for an Li→Li+1 rotation, including from_form, to_form, justification_kind selection, and substantive justification. Invoke whenever the Synthesizer produces a per-edge claim.
status: active
---

# propose-rotation

Every per-edge rotation the Synthesizer proposes emits a `rotation_claim` JSON validating against `schemas/rotation_claim.json`. This skill is the workflow for producing one.

## When to invoke

- **Synthesizer**, once per per-edge rotation per slice, per push. A push may produce multiple rotation_claims (e.g., L1→L2 on slice X *and* a SIDEWAYS unification on slice Y's L2).

## Procedure

1. **Name the edge.** Pick from `{L0→L1, L1→L2, L2→L3, L3→L4}`. L0→L1 claims consolidate the Explorer's output; L1→L2 unfolds optimization tricks; L2→L3 lifts iteration to global tensor field; L3→L4 maps into the formal calculus.

2. **Write the `from_form`.** Reproduce the Li form as briefly as possible — pseudocode or math, with cited primitives. This is what's being rotated *from*. Cite the prior-layer source.

3. **Write the `to_form`.** Express the Li+1 form using vocabulary appropriate to that layer:
   - L1: pure-functional with explicit input/output sets, mutation pattern noted.
   - L2: composition of base algebraic primitives, optimization tricks unfolded.
   - L3: global tensor-field operation (or `obstruction` if none exists).
   - L4: against the calculus at `book/src/design/l4_calculus.md`; TS-style record literals + Haskell-style monadic structure.

4. **Choose `justification_kind`.** In preference order when multiple apply:
   - **`empirical_match`** — cited test exercises the rotation directly. **Strongly preferred** when a test exists (executed test > algebraic argument).
   - **`reduction_chain`** — formal step-by-step equational rewriting (especially for L3→L4 against the calculus).
   - **`algebraic`** — informal algebraic argument that doesn't require formal chain.
   - **`structural`** — symmetry / structural argument (e.g., "the L2 form is a transpose of a known primitive").
   - **`obstruction`** — for negative results. The Li+1 form does NOT exist for principled reasons. Required for L2→L3 on genuinely sequential algorithms (Gauss-Seidel, triangular solves). Negative results are first-class output.

5. **Write the `justification` body.** Substantive — not just "this is obviously equivalent." For algebraic/reduction_chain, list the steps. For empirical_match, cite the test (file:line) and explain *what* the test exercises that pins the equivalence. For obstruction, name the structural barrier (sequentiality, reordering-dependence, etc.).

6. **Flag push-back if labored.** If producing the to_form required special cases or forced fits, populate `push_back_proposal` with `target_layer` (which lower layer to restructure) and `proposal` (what change would eliminate the friction). Push-back is first-class — surface it rather than absorbing.

7. **Alternative formulations.** Per CLAUDE.md *Process* #4: if multiple plausible `to_form`s exist and you can't yet pick one, emit multiple rotation_claims with the same `from_form` and a note explaining the alternatives. The Critic verifies each; coalescence happens by cross-slice pressure or in a later cycle. Don't force premature commitment. But check the duplication-explosion constraint: if the duals are forcing parallel work at the next layer up, they're competing designs, not duals.

## Output

A JSON object validating against `schemas/rotation_claim.json` (or multiple, for alternative formulations). Plus the unified diff covering the slice file additions. No editorializing in the spec content.

## Friction → `problems/`

If producing this skill's output consistently fights the schema (a justification doesn't fit any `justification_kind`; a rotation doesn't fit any edge; the diff is the wrong unit of output), file as a `problems/` entry for meta-review.
