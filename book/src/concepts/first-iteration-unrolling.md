# First-iteration unrolling

An L4-level structural rotation that hoists a step-internal `if it == 0 then base_case else recurrence` branch out of the steady-state iteration body by unrolling the first step explicitly.

## When it applies

Many iterative numerical methods carry a step-local control branch whose sole purpose is to handle the iteration-zero special case — a recurrence that needs `state_{k-1}` to fire, plus a base case for `k = 0` where `state_{-1}` doesn't exist (or exists trivially). Concretely:

- **CG / PCG**: `p_k = r_k + (β_k/β_{k-1})·p_{k-1}` for `k ≥ 1`, with `p_0 = r_0` (no `β_{-1}`). See the firm [`krylov-step` (CG instance)](../L2/krylov-step.md) + [`L4/krylov-step`](../L4/krylov-step.md) Form B.
- **GMRES**: the first Arnoldi step has no `v_{k-1}`. (Less acute because the orthogonalization loop handles `k = 0` naturally as a zero-length loop, but the same shape recurs in the Hessenberg column update.)
- **LOBPCG**: no prior eigenvalue estimate to subtract on the first Rayleigh-Ritz.
- **Chebyshev iteration**: no `x_{k-1}` for the two-step recurrence's first half-step.
- **BiCGStab, MINRES**: same shape, same fix.

In all cases the branch is **load-bearing** at L0–L2 (a real divide-by-zero or undefined-reference avoidance), but is **structurally avoidable** at L4 by separating the first step from the rest.

## The rotation

Given an iteration `iterate_while s_0 cond step` whose `step` body contains `if it == 0 then f_0 else f_k(prev_state_field)`, the rotation produces:

```
first_step  :: ... -> State -> StepResult         -- straight-line, no branch
steady_step :: ... -> PrevCarry -> State -> StepResult  -- branch-free; PrevCarry threaded externally
```

and a driver:

```
solve config ... =
  let s_0 = init ... in
  if terminates_already s_0 then trivial_result
  else
    let s_1 = first_step ... s_0 in
    iterate_while_with_carry s_1 (extract_carry s_0)
      cond
      (\(s, carry) -> (steady_step ... carry s, extract_carry s))
```

The carry (`beta_prev` in CG; `H_{k,k-1}` in GMRES; etc.) becomes a **closure parameter** of the loop driver rather than a **state field** of the iteration. The state schema is one slot lighter; the steady step is branch-free.

## What gets hidden

Per [`rotation`](./rotation.md) criterion (a) *state hiding*:

- The `_prev` field of the steady-state schema (the slot that carried the prior iteration's value of the recurrence variable).
- The `if it == 0` branch in the step body.
- The need for a sentinel initial value of the `_prev` field (typically `0` or `⊥`) that would otherwise trigger the runtime branch on iteration 0.

The load-bearing precondition (`_prev > 0` on entry to `steady_step`) is moved from a runtime check to a **static call-site obligation** — discharged by construction, since `steady_step` is only ever called after `first_step` has run and produced a well-defined carry.

## What is preserved

The algorithm's numerics are identical iteration-for-iteration. The total work is the same; the residual history is the same; the convergence test fires at the same iteration counts. The rotation rearranges *where the control choice lives*, not what is computed.

The L0/L1/L2 forms of the slice are unchanged. The source code still contains the per-step branch (the Palace authors did not unroll the first iteration). First-iteration unrolling is **purely an L4 presentation choice**, valid alongside the unrolled-into-step form. Both are acceptable L4 renderings of the same L3 form; the unrolled form is preferred when the slice's steady-state branch-freedom enables downstream reasoning (e.g., loop-fusion arguments, reduction-pattern recognition, or pattern-matching against other Krylov slices that have already adopted v0.5-style forms).

## Trade-offs

First-iteration unrolling pays for steady-state legibility with **code duplication at the driver level**: `first_step` and `steady_step` share most of their bodies (every named primitive after the branched one fires identically). When the branched primitive is *only* an `axpby` vs. a copy-of-`r`, as in CG, the duplication is small. When the branched logic is larger — e.g., a GMRES first-Arnoldi step that performs no orthogonalization vs. a steady step that does — the duplication can hurt; in those cases the in-step branch may be the better L4 rendering.

The rule of thumb: unroll when the branch's *only* consumer is the iteration-zero special case AND the branched expression is a single primitive call. Keep the in-step branch when the branched logic spans multiple primitives or when iteration zero has materially different shape (e.g., requires fewer arguments).

## Relation to other rotations

- Composes cleanly with [`derived-view hoisting`](./derived-view-hoisting.md): both are L4 self-rotations that tighten the state schema. CG's v0.5 form combines them — `res` is a derived view (v0.4) and `beta_prev` is closure-threaded (v0.5).
- Distinct from [`variant-absorption`](./variant-absorption.md), which deals with orthogonal *configuration* axes (preconditioner choice, restart strategy). First-iteration unrolling deals with a *temporal* axis (iteration-zero vs. steady-state).
- Compatible with [`sequential-obstruction`](./sequential-obstruction.md) at L3: the rotation does not change the L2→L3 outer-loop verdict. The iteration remains sequential; only the L4 presentation of that sequential iteration changes.

## Background

The pattern is folklore in numerical-software engineering — many production Krylov implementations *do* unroll the first iteration in the compiled code path (sometimes for branch-predictor reasons, sometimes for SIMD-friendly steady-state inner loops). Palace's source does not; the L4 form may. The L4 calculus's role as the presentation layer makes the choice a documentary one rather than a performance one.

The more general pattern — splitting a recurrence into a base case and a steady-state induction step — is loop-invariant code motion applied to control flow rather than data flow. Knuth (TAOCP vol. 1, §1.2.1) gives the canonical exposition under "loop unrolling" / "prologue and epilogue".

## Slices that use this pattern

- [`krylov-step` (CG instance)](../L2/krylov-step.md) — CG L4 v0.5 (firm-homed at [`L4/krylov-step`](../L4/krylov-step.md) Form B) was the first form to adopt the unrolling.
- (Forward markers) Future Krylov slices (GMRES, MINRES, BiCGStab, LOBPCG, Chebyshev) will pattern-match against this concept when they reach L4 presentation choices.
