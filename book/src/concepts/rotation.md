# rotation

## Context

A **rotation** is the methodology's fundamental unit of progress: a re-expression of a piece of work from layer L_n into layer L_{n+1} that *changes the impedance* — mutation → purity (L0→L1), fusion-unfolding → algebraic decomposition (L1→L2), iteration → global tensor op (L2→L3), operator algebra → formal calculus (L3→L4). See `CLAUDE.md` *Output structure: an incremental impedance-matching stack* for layer semantics.

This entry distinguishes **genuine rotations** from **renamings**. It was extracted during the 2026-05-24 meta-review, in response to cycle 3's friction: an L1→L2 attempt on GMRES where the proposed L2 form was "essentially the L1 inner loop rewritten with primitive names" — the rotation collapsed to a renaming, with no algebraic compression and no abstraction shift.

This concept entry is **methodology**, not a tensor primitive. It lives under `concepts/` because the Meta-Critic placed it there, and because "what counts as a rotation" is a concept the agent loop needs in its working vocabulary. (Most `concepts/` entries — `axpy`, `dot`, `matvec`, etc. — are algebraic primitives the slices reuse. This one is different in kind: it's a primitive of the *methodology*, not of the spec content.)

## When a rotation has occurred

For a proposed L_n → L_{n+1} rotation to count, **at least ONE** of the following must hold:

### (1) State hiding

L_{n+1} hides at least one piece of state that L_n exposed.

**Worked example (GMRES, cycle 3 friction).** L1 threads `(V, H, s, cs, sn, j, w-scratch)` through the inner loop; the indexing arithmetic — `H.data() + j*(max_dim+1)`, `Hj[k] = …` for `k=0..j`, `V[0..j_final]` — is visible to the reader of L1. A genuine L2 rotation introduces an `arnoldi_step` primitive whose signature hides those threaded buffers: the caller writes `(state', residual_norm) = arnoldi_step(state, A, B)`. The Givens accumulator, the Hessenberg column slot, the orthogonalization scratch — all hidden inside the primitive's contract.

If the proposed L2 still says `arnoldi_with_givens(V, H, j, ...)` with the same indices threading, no state was hidden, and (1) does not hold.

### (2) Coarser substitution

L_{n+1} admits substitution / replacement at a coarser grain than L_n.

**Worked example.** At L1, swapping MGS (modified Gram-Schmidt) for CGS (classical Gram-Schmidt) requires re-threading per-vector collectives, dot accumulators, and inner-loop structure. At a genuine L2, the choice is a single primitive substitution: `orthog := mgs_step | cgs_step | cgs2_step`. Whole-algorithm correctness arguments factor through the primitive's contract rather than its implementation.

If swapping a sub-algorithm at L_{n+1} still requires touching the same number of call sites and the same threaded state as at L_n, no coarser-substitution interface emerged, and (2) does not hold.

### (3) Threaded-state compression

The state bundle threaded through L_{n+1} is strictly smaller, or at least strictly more abstract, than at L_n.

**Worked example.** L1 of GMRES threads `(V[0..max_dim+1], H column-major packed, s, cs[max_dim], sn[max_dim], j, max_dim, w-scratch, restart)`. A genuine L2 restart-cycle primitive threads `(iterate, residual, basis_handle, convergence_flag)` — same per-step computation, much smaller surface. The implementation buffers are encapsulated in `basis_handle`.

If the L_{n+1} step's signature mentions the same buffers with the same shapes as L_n, the threaded state didn't compress, and (3) does not hold.

## If none of (1)/(2)/(3) hold

The proposed rotation is a **renaming**, not a rotation. The L_{n+1} form is L_n with different identifiers, providing no impedance change. Two possible responses:

- **Merge.** Drop the proposed L_{n+1} for this slice and treat the L_n form as the highest layer the slice has reached. The next attempted rotation on this slice should reach further, with one of (1)/(2)/(3) clearly in view.
- **Redesign.** Reframe the L_{n+1} attempt so one of the criteria holds — typically by identifying a primitive that hides the threaded state (route (1)) or by recognizing a substitution interface that L_n was obscuring (route (2)).

Either response is recorded as a `labored_rotation_push_back_candidate` in the Critic's verdict, with the `push_back_suggestion` naming the route.

## Carry-through: not every concept must rotate

(Added 2026-05-24 meta-review #2, in response to user feedback that the original criteria risked false-positive `revise` verdicts on legitimate-but-modest rotations.)

A genuine rotation moves *some* of the slice forward (via (1) state hiding, (2) coarser substitution, or (3) threaded-state compression). It does **not** require every concept in the slice to be transformed.

A concept that **carries through unchanged** from L_n to L_{n+1} is **legitimate** when:

- **Idiomatic at L_{n+1}.** Its current shape is at the right grain for L_{n+1}'s abstraction; "rotating" it would be cosmetic — a renaming for renaming's sake.
- **Not in conflict with L_{n+1}'s framing.** The rotation of *other* parts of the slice doesn't expose tension with this carry-through (e.g., the carried-through concept doesn't force the rotated parts to re-expose state they hid).

The renaming anti-pattern is **"ALL concepts carry through unchanged with new names"** — nothing moved toward the next layer. A genuine rotation may pass some concepts through unchanged; what matters is that **something** rotated.

**Worked example.** In a hypothetical CG L1→L2 rotation:
- The `axpy(α, x, y)` primitive is already at the right grain for L2 (it's an algebraic operation, not an iterative mutation pattern). L1 already uses `axpy` because the Synthesizer extracted it from the source's `x.Add(α, y)`. At L2, `axpy` carries through unchanged — **legitimate carry-through**.
- The `dot(x, y)` primitive likewise carries through unchanged from L1 to L2 — already idiomatic at L2.
- The actual rotation work at L1→L2 is hiding the explicit per-step indexing of `r_k → r_{k+1}` behind a `cg_step(state) → state'` primitive. That's the **state-hiding** criterion (1) firing for the changed portion.
- A rotation_claim covering this step honestly identifies: criterion (1) state-hiding satisfied for the iteration-index threading; `axpy`/`dot` carry through as already-idiomatic L2 primitives.

The Critic's check #8 (per `prompts/critic.md`) verifies the rotated portion satisfies a criterion. Concepts carrying through are **not** failures unless ALL concepts carry through — that's the genuine-rename anti-pattern.

When emitting a rotation_claim, the Synthesizer's pre-emit self-check (per `prompts/synthesizer.md` *Rotation self-check*) requires identifying both the rotated portion (with named criterion) and any carry-through (with named idiomaticity), so the Critic can verify both halves.

## What this is NOT

- **Not a quality-of-prose test.** A rotation can be terse or verbose; what matters is whether it changes the abstraction shape.
- **Not a "fewer-symbols" test.** L_{n+1} may have *more* identifiers if those identifiers are now reusable across slices (the unification pattern).
- **Not a requirement that all three criteria hold.** One is enough — they characterize different ways a rotation can succeed.
- **Not a blocker for negative results.** An L2→L3 rotation that fails because the algorithm is genuinely sequential (Gauss-Seidel, triangular solve, …) is **not** a rename-not-rotation failure — it's an `obstruction` result, first-class output. The criteria here distinguish "did a rotation happen at all" from "could a rotation happen given the algorithm's structure."

## Critic's role

`prompts/critic.md` verification check #8 applies these criteria. When no criterion holds for a proposed rotation:

- Verdict: `revise`.
- Issue kind: `labored_rotation_push_back_candidate`.
- `push_back_suggestion`: which lower-layer reframing would make a real rotation possible — or recommend layer-merge if the rotation is genuinely premature for this slice.

## Origin

Codified during the **2026-05-24 meta-review enactment**, in response to cycle 3 of the loop's first GMRES push (`be11242  cycle: forward gmres [L1→L2] → revise`). The Critic in that cycle wrote the friction observation that motivated this entry — without the cycle's friction, the criteria above would not have been written. See `book/src/meta-reviews/2026-05-24.md`.

## Working Notes

- The criteria may be too sharp; the meta-review's risk-notes flagged the possibility of false-positive `revise` verdicts on legitimate-but-modest rotations. Watch the next 3 cycles. If genuine rotations are being rejected, soften the framing (e.g., require "approximately one of (1)/(2)/(3) plus a justification" rather than strict one-of).
- Subsequent meta-reviews should check whether the L3→L4 calculus rotation has its own quality criteria. The (1)/(2)/(3) shape here is most natural for L1→L2 and L2→L3 rotations of imperative-style content; L3→L4 (algebraic-spec → formal calculus) may benefit from a different set of tests (e.g., "does the formal version expose a substitution / equation theorem the algebraic version cannot state?").
