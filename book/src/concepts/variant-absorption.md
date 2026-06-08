---
edges:
  reference:
    - concepts/rotation              # peer methodology concept
    - concepts/constructed-operators # canonical full-absorption route
    - L2/krylov_step                 # worked example slices (CG / GMRES variant axes)
---

# variant absorption

## Context

A peer concept to `rotation.md`. **Variant absorption** is the principle that when a slice has orthogonal axes of algorithmic variation — preconditioner side, orthogonalization variant, flexible vs. fixed preconditioner, restart vs. full Krylov, real vs. complex scalar type, etc. — the L1 form must absorb those variants **parametrically** rather than appending them as separate paragraphs.

This concept was extracted during the 2026-05-24 meta-review #2 (cycles 4–6 enactment) in response to two friction observations:

- **Cycle 5** (back-push on GMRES L1): variant combinations (`pc_side` × `gs_orthog` × flexible vs. fixed) were under-specified — the L1 form named the variants but did not show how they compose at the per-step level.
- **Cycle 6** (back-push on GMRES L1, with the Critic acknowledging cycle-5's improvements): the FGMRES paragraph was "bolted onto the end of L1 rather than absorbed: the rotation `x_m = x_0 + V_m y_m` has to be locally patched to `x_m = x_0 + Z_m y_m` for FGMRES, which suggests the L1 form should have been stated as `x_m = x_0 + W_m y_m` where W_m is the *update basis* (= V_m for GMRES, = Z_m for FGMRES) and `A W_m = V_{m+1} H̄_m`. That unified form would make FGMRES a parameter choice rather than a variant."

The Critic correctly applied check #8 (rotation quality) and found L0→L1 was a genuine rotation, but flagged the variant-handling as a separate quality failure deserving its own check (#9 in `prompts/critic.md`).

This concept is **methodology**, not a tensor primitive (same kind as `rotation.md`).

## The parametric-vs-appended test

For each orthogonal axis of variation a slice exposes, the L1 form must take ONE of two choices:

### (A) Parametric absorption

The variant is a **parameter** of the main L1 statement. The L1 form names a symbol whose binding ranges over the variant values.

**Worked example (GMRES / FGMRES).**
- Bad (appended): L1 states GMRES as `x_m = x_0 + V_m y_m`, then a FGMRES paragraph at the end patches it to `x_m = x_0 + Z_m y_m`. Two statements; the rotation has to "know about" the variant at every call site.
- Good (parametric): L1 states `x_m = x_0 + W_m y_m where W_m is the update basis and A W_m = V_{m+1} H̄_m`. The slice then notes `W_m = V_m` for GMRES (the trivial choice) and `W_m = Z_m = B V_m` for FGMRES (the flexible-preconditioner choice). One statement; the variant is a parameter.

**Worked example (orthogonalization variant).**
- Bad (appended): L1 says "apply MGS orthogonalization", then a paragraph at the end says "for CGS, replace the per-vector loop with batched dot products; for CGS2, follow CGS with one refinement pass."
- Good (parametric): L1 says `orthog := orthog_strategy(V[0..j], w)` and notes `orthog_strategy ∈ {mgs, cgs, cgs2}` as a slice parameter. The choice influences MPI-collective count and numerical stability, both noted parametrically.

### (B) Explicit scoping-out

The variant is **explicitly out of scope** for this slice and named either:
- In a "Scope" or "Open questions" subsection of the slice (with a brief note on why the variant is deferred).
- In a separate slice that explicitly covers the variant.

**Worked example (block GMRES).** A vanilla GMRES slice can scope out block-GMRES variants by saying "Block variants (multiple-RHS, BGMRES, BFGMRES) are deferred to a separate slice; they share the Arnoldi skeleton but the inner-product/orthogonalization grain changes from vector to block." That's explicit scoping; it's NOT "FGMRES paragraph bolted on."

### Failure mode

The variant is appended at the end of the L1 statement as a delta — "X is Y but with Z replaced by W" — without lifting Z into a parameter. This forces every L1→L2 rotation attempt to choose: handle the variant in L2 (which doubles the L2 work and breaks canonical form) or ignore it (which makes the spec wrong for the bolted-on variant). Neither is acceptable.

## The test

For each orthogonal axis of variation a slice exposes, ask: **can the variant be expressed as a binding of a parameter introduced in the main L1 statement?**

- **Yes** → parametric. The L1 form is honest about its degrees of freedom.
- **No, and the variant is essential** → split the slice; the variants are not actually orthogonal at L1 and deserve separate slices that share concepts at L2.
- **No, and the variant is deferable** → scope it out explicitly with a one-line note.

The "no, and bolt it on" path is **not** an option — that's the failure mode this concept exists to prevent.

## Levels of absorption

(Added 2026-05-24 meta-review #3, in response to cycles 7+9 friction where invariant-level absorption was achieved but procedural and primitive-sequence levels were not.)

Variant absorption operates at three levels. A genuine absorption holds at **all three**; partial absorption — typically (a) without (b) or (c) — must be explicitly declared.

### (a) Invariant-level absorption

The mathematical statement unifies. Example: `x = x_0 + W_m y_m` with `W_m = V_m` for GMRES and `W_m = Z_m` for FGMRES is invariant-level absorbed — one equation, parameter binding chooses the variant.

This is the level the original `variant-absorption.md` "parametric vs appended" test catches. Necessary but not sufficient.

### (b) Procedural absorption

The L1 procedure mentions the variant parameter **at most once**, in a binding or dispatch step, and never re-inspects it. Example: a procedure that says "let `op = construct_krylov_operator(A, M, side)`; then for each step, `w = op.apply(v)`" is procedurally absorbed — `side` appears once, at construction.

A procedure that re-inspects the variant at multiple steps (`if side == LEFT: ...; elif side == RIGHT: ...`) is **not** procedurally absorbed even if the invariant unifies. Cycle 9's GMRES (`W ∈ {V, Z}` selector referenced at Arnoldi step AND solution update) is the worked counter-example.

### (c) Primitive-sequence absorption

The L_{n+1} primitive chain is the **same shape** across parameter values, with the parameter binding only the operands (not the chain itself). Example: `[matvec, dot, axpy]` for all `side` values, with the matvec's operator argument changing.

A rotation whose L_{n+1} chain has different lengths or different primitives per parameter value is **not** primitive-sequence absorbed. Cycle 7's GMRES (right-fixed-M needs trailing `M.apply`; left and FGMRES don't) is the worked counter-example — three sequences masquerading as one.

**Note (added 2026-05-24 meta-review #5):** Achieving primitive-sequence absorption may require **state-schema changes**, not just a constructed operator. When the variant is *per-step* (e.g., FGMRES with `M_k` changing between Arnoldi iterations), constructing an operator can't absorb the variant — the threaded sim state itself must expand (add the per-step preconditioned basis `Z` to L1 state). See `constructed-operators.md` *Limits of constructed-operator absorption* for the worked GMRES↔FGMRES example and the decision rule.

## Partial absorption: how to disclose

A rotation that achieves (a) but not (b) or (c) is **partially absorbed**. The slice must say so explicitly — silent partial absorption is the failure mode this concept addresses.

Required disclosure when ≥1 of (b)/(c) fails:

- List the **parameter sites in L1 procedure** where the variant is re-inspected. The Critic uses this to verify completeness.
- List the **primitive-sequence divergences in L_{n+1}** as **residual axes**. The Critic verifies these are necessary (genuinely irreducible) rather than absorbable through a different framing (e.g., constructed operators — see `constructed-operators.md`).

A slice that achieves all three levels does not need a "residual axes" section. A slice that achieves only (a) and silently glosses over (b)/(c) fails Critic check #9.

## Routes to full absorption

When (b) or (c) fails, consider the canonical fixes:

- **Constructed operators** (see `constructed-operators.md`). Construct an operator that internalizes the variant at construct time; per-step procedure is uniform. Resolves both (b) and (c) when the variant influences operator behavior but not algorithm shape.
- **Restructure to eliminate the variant axis.** If the variant is forcing structural divergence at L_{n+1}, the variant may not actually be orthogonal — split the slice into per-variant slices that share L2 concepts.
- **Accept partial absorption and document residual axes** (the disclosure path above). Acceptable when the variant is genuinely structural and constructed-operator absorption is not appropriate (e.g., the variant changes asymptotic convergence behavior, not just per-step machinery).

## What this is NOT

- **Not a requirement that every axis be parametric.** Scoping-out is equally acceptable when the variant is genuinely deferable.
- **Not a ban on per-variant notes.** A parametric L1 form can (and should) note "MGS = J communication-collective calls; CGS = 1 communication-collective call" without bolting on a whole paragraph. The note is *about* the parameter, not a replacement for parametric absorption.
- **Not a license to over-parameterize.** If a slice has so many orthogonal variants that parametric absorption obscures the algorithm, that's signal that the slice is over-scoped (per `book/src/spec/index.md` slice-acceptance criterion #1). Split the slice.

## Critic's role

`prompts/critic.md` verification check #9 applies this concept. For each slice with orthogonal variation:

- If variants are parametric, check #9 passes.
- If variants are scoped out explicitly, check #9 passes.
- If variants are appended as bolt-on paragraphs, verdict: `revise`, `kind: labored_rotation_push_back_candidate`, `push_back_suggestion`: which parameter would unify the variants, or which slice should hold the scoped-out variant.

## Origin

Codified during the **2026-05-24 meta-review #2 enactment** (cycles 4–6). Cycle 6's Critic note (in `lessons.md` and `episodic.jsonl`) was the originating observation. The previous meta-review (`2026-05-24.md`, cycles 1–3) left the variant-handling lesson in `lessons.md` only — read by the Critic but not enforced by the Synthesizer. Meta-review #2 promoted it to this concept page + producer-side (Synthesizer) + consumer-side (Critic) enforcement.

## Working Notes

- The boundary between "orthogonal variant" and "fundamentally different algorithm" is fuzzy. FGMRES is parametrically absorbable into GMRES because they share the Arnoldi skeleton; LOBPCG vs. Arnoldi is not parametric — those are different slices. The test is whether the shared abstraction (Arnoldi-like inner loop, Krylov-basis-with-Galerkin-projection) is the same across variants; if yes, parametric is possible.
- The cycle 6 observation that suggested unifying `W_m = V_m | Z_m` is a clean example of variant absorption emerging from Critic friction. Future meta-reviews should look for similar friction-driven unifications — the loop is producing methodology, not just slices.
- This concept's relationship to `rotation.md`: variant absorption is *necessary* for criterion (1) state hiding to hold robustly. If the L1 form bolts on FGMRES paragraphs, an L1→L2 attempt either hides the variant logic (in which case the L1 form was over-detailed) or exposes it (in which case the L2 form has parallel branches that defeat state-hiding). Parametric L1 → clean L2.

## Structurally-distinct variants in otherwise-uniform families

(Added 2026-05-25 meta-review #11 after cycle 40 surfaced the pattern on the orthogonalization-family slice; predicted recurrence on the curl-curl projector slice and on FGMRES per-step preconditioner — the latter was the originating signal in cycle 7.)

A common variant family has the shape *N members share threaded-state structure but ONE member has fundamentally different state*. The shared-structure members absorb cleanly at all three levels under either parametric or constructed-operator strategies; the outlier breaks level-(c) primitive-sequence absorption no matter what strategy you reach for.

**Canonical examples**:

- Orthogonalization at `{MGS, CGS, CGS2, Householder}`. MGS/CGS/CGS2 thread the same state (the basis `V[0..j]` plus the projection coefficients column) and absorb at all three levels under residual-axis disclosure for the L2 collective shape. Householder threads a *reflector sequence* — fundamentally different state shape — and its L_{n+1} chain is `[reflect_apply, reflect_zero]` instead of `[dot, axpy]`.
- Preconditioner side at `{LEFT, RIGHT, none, flexible}`. The first three absorb into a constructed `apply_BA` (level-(c) primitive sequence is identical: 1–2 `apply_linop` calls). `flexible` (FGMRES) threads a *per-step basis* `Z[k]` distinct from `V[k]`, which is structurally different state.

**The fix paths**:

1. **Declare a residual axis at L1 with variant-conditional state schema.** The L1 state types include the outlier's extra state (`Z: Vec[]` for FGMRES; `reflectors: (Vec, real)[]` for Householder) marked conditional on the variant value. The L1 procedure inspects the variant exactly once (dispatch) and threads the variant-conditional state accordingly. Level-(c) is officially residual; the L_{n+1} prose enumerates the divergent primitive sequences.

2. **Split the outlier into a sibling slice with shared concept references.** The main slice's `## Scope` declares the outlier scoped out; the sibling slice shares concept references for the common primitives (`apply_linop`, `dot`, …) and provides its own L1/L2 forms. Level-(c) absorption is full *within each slice*; the inter-slice consolidation lives in cross-references and the shared concept entries.

**How to choose**: option (1) is preferred when the outlier is a small minority (1 of 4 members) and the conditional state is bounded in size (one extra array, not a tree of new types). Option (2) is preferred when the outlier's primitives are substantially distinct enough that the residual-axis prose would dominate the slice. The Synthesizer applies the [`classify-variant-axis`](../../../skills/classify-variant-axis/SKILL.md) skill to make the call.

**What's NOT this pattern**: differing *collective shape* / *cost annotation* across variants (e.g., CGS2 has 2× the dots-and-reductions of CGS) does NOT trigger structurally-distinct-variant treatment. That is cost annotation, captured per the `## L2` numerical-claim register. Per cycle 23 lesson: "cost annotation is not absorption failure."

Cross-reference: [`constructed-operators`](./constructed-operators.md) *Limits of constructed-operator absorption*.

## Concept: variant absorption

The discipline of handling orthogonal variation axes at L1 such that
the form is genuinely uniform across variant values, not just
cosmetically unified.

A slice often exposes multiple variant axes at L0 — enum-valued flags,
template parameters, runtime configuration, optional features. The
question at L1 is: at what level is each axis absorbed?

## Three levels of absorption

An L1 form absorbs a variant axis at three nested levels:

- **(a) Invariant-level**: the mathematical statement unifies. A single
  formula or recurrence covers all variant values, perhaps with the
  variant appearing as a parameter (e.g., `M⁻¹` with `M = I` as a
  legitimate special case).
- **(b) Procedural**: the L1 procedure mentions the variant parameter
  at most once (the binding or dispatch site) and never re-inspects
  it. Downstream sites use the bound result, not the variant.
- **(c) Primitive-sequence**: the L_{n+1} primitive chain is the same
  shape across variant values. The number, order, and identity of
  primitive calls do not depend on the variant.

All three together constitute full absorption. Partial absorption is
acceptable only when explicitly disclosed: list the residual axes in
the L1 form so downstream readers know where divergence happens.

## Resolution paths

Four ways to handle a variant axis at L1:

1. **Parametric**: the variant is a parameter of the main L1
   statement; downstream sites do not re-inspect it. Achieves all
   three levels when the variant is a clean scalar/option flowing
   through the recurrence.
2. **Constructed-operator**: construct an operator at solve start that
   internalizes the variant; the per-step procedure calls
   `op.apply(...)` uniformly. See
   [constructed-operators](./constructed-operators.md). Achieves (b)
   and (c) when (a) is awkward.
3. **Scope-out**: the variant is explicitly out of scope for this
   slice and named in "Open questions" or a separate slice.
4. **Residual-axis**: partial absorption with explicit disclosure of
   the residual divergence (the primitive sequence diverges at named
   sites). Honest about not fully unifying.

## Anti-pattern

Silent partial absorption — the L1 form looks uniform but the L2
unfolding reveals branching the L1 prose did not disclose. Critic
check #9 flags this.

## Slices that use this methodology

- [`krylov_step` (CG instance)](../L2/krylov_step.md) — three axes all absorbed parametrically.
- [`krylov_step` (GMRES instance)](../L2/krylov_step.md) — six axes; side absorbed via
  constructed-operator, others parametric or via primitive-contract
  (orthogonalization variant).
