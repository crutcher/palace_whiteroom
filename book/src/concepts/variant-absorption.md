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
