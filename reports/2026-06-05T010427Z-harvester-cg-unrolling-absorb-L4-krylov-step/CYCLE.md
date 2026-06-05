---
agent: harvester
invoked_at: 2026-06-05T010427Z
scope: L4 operator: krylov-step (absorb cg.md:27-141 CG-concrete v0.5 worked datum into Form B)
status: integrated
integrated_at: 2026-06-05T010427Z
integration_commit: cdbd8d851e1108ba48b1b54fff9d011968f462d2
integration_notes: "Applied clean by integrator-per-report (cycle-099 staging row 1/3), batch-31 P2 slice-deletion campaign COMPLETION. D1: absorbed the cg.md:27-141 v0.5 first-iteration-unrolling worked datum into book/src/L4/krylov-step.md as a NEW firm '### Worked example — CG Form B' subsection + re-anchored the dangling cg.md:* pointers (§Semantics:82/§Status:152/§Evidence:171). Rank stays 0 (firm-on-positive-structure; L0 ground is a rank-exempt cites-evidence edge). cargo make book EXIT 0; step-5b rank_violations 0 GATE PASSES; no newly-orphaned node. Recommended-CLOSE OQ: cg-slice-27to141-fully-homed-clear-to-delete-and-evidence-pointer-residue-class-B (for batch-31 meta unify)."
inputs:
  - book/src/spec/slices/cg.md:27-141 (the genuinely-unlifted CG-concrete v0.5 first-iteration-unrolling worked instance)
  - book/src/L4/krylov-step.md:28,:82,:152,:171 (the pre-named Form B home + the existing dangling cg.md slice-pointers)
  - book/src/concepts/first-iteration-unrolling.md:21-37 (the ABSTRACT generic rotation — NOT to be duplicated)
  - book/src/L1-L0/ksp-solve-mutation-rotation.md:159,:163,:217 (the (rough-in) L0 terminal home: Sub-pattern B, iterative.cpp:360-486 / :427-464)
  - reference/palace/palace/linalg/iterative.cpp:427-464 (per-step for-loop; :434-441 first-iteration branch)
  - cycle-099 D1 dispatch (batch-31 P2 slice-deletion campaign — krylov trio completion)
---

# CYCLE: Absorb the CG-concrete v0.5 first-iteration-unrolling worked datum into L4 `krylov-step` Form B

## Summary

The `cg` slice (`book/src/spec/slices/cg.md`) is reduced to a stub plus ONE genuinely-unlifted live datum: the `## L4 v0.5 — first-iteration unrolling (self-rotation)` section (`cg.md:27-141`) carrying the CG-CONCRETE worked instance — the `cg_first_step` / `cg_steady_step` typed bodies (with `beta_prev` dropped from the steady-state `CgState<S>` schema), the `forget_beta_prev` projection making the v0.4↔v0.5 equivalence formal, the `### Equivalence to v0.4` ratification, and the `### Variant: pcg under v0.5`. This material is the worked example that the L4 `krylov-step` chapter's **Form B** already names abstractly (`krylov-step.md:28-33,:82`) and already flags as "retained live in the reduced slice" (`:171`, citing `cg.md:52` `cg_first_step`, `cg.md:69` `cg_steady_step`, `cg.md:95-108` the `iterate_while_with_prev` driver). This dispatch pastes that CG-concrete worked instance INLINE into a new `### Worked example — CG Form B` subsection under Form B's §Semantics, re-anchors its dangling `cg.md:*` slice-pointers to the now-inline home + the L0 terminal home (`L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B, `iterative.cpp:360-486` / per-step for-loop `:427-464`), and thereby makes `cg.md:27-141` fully homed and clear-to-delete (consumed by D2 this same cycle). I do NOT restate the abstract generic `first_step`/`steady_step` rotation (that stays in `concepts/first-iteration-unrolling.md:21-37`); I land ONLY the CG-concrete bodies + the v0.4↔v0.5 equivalence/pcg-variant as the worked example Form B references. Status stays `firm` (firm-on-positive-structure escape: these are syntactic L4-self-rotation identities on a fully-specified read closure, the same law-confidence basis as the existing Form A / Form B).

## Paste-inline verification

### The CG-concrete worked datum on disk (`book/src/spec/slices/cg.md:27-141`)

Confirmed present and load-bearing — the unique material the cycle-009 reduction kept:

- `cg.md:39-50` — the v0.5 `CgState<S>` schema with `beta_prev` **gone** (the note at `:48-50`: `beta_prev` supplied as a closure-captured scalar from the prior step, not a state field).
- `cg.md:52-67` — `cg_first_step :: LinOp<S> -> Scalar -> CgState<S> -> { state, residual_norm }`; precondition `s.it == 0` so `p ← r` unconditionally; body `Ap = apply opA p'`, `alpha = s.beta / dot Ap p'`, `x' = axpy alpha p' s.x`, `r' = axpy (negate alpha) Ap s.r`, `beta' = dot r' r'`, `res' = sqrt (abs beta')`.
- `cg.md:69-84` — `cg_steady_step :: LinOp<S> -> Scalar -> Scalar -> CgState<S> -> { state, residual_norm }`; precondition `s.it >= 1, beta_prev > 0`; **branch-free**; `p' = axpby 1.0 s.r (s.beta / beta_prev) s.p`; rest identical to first-step.
- `cg.md:86-106` — `cg_solve` driver with the `iterate_while_with_prev s1 s0.beta` fold (`:99-105`) threading `beta_prev` as the loop carry.
- `cg.md:108` — `iterate_while_with_prev` is `iterate_while` over the pair `(state, beta_prev)`, a closure over the loop carry, not new machinery.
- `cg.md:110-114` — "What this rotation hides": `beta_prev` field gone; `if s.it == 0` branch gone from the body; `0/0`-avoidance moved from runtime branch to a static call-site obligation (`beta_prev > 0`).
- `cg.md:120-129` — `### Equivalence to v0.4`: observational identity across (1) initial convergence, (2) first iteration, (3) subsequent iterations, (4) `residual_history`; the `forget_beta_prev : CgState_v04<S> -> CgState_v05<S>` projection making the equivalence formal (`cg.md:129`).
- `cg.md:131-133` — `### Variant: pcg under v0.5`: `pcg_first_step` uses `p' = s.z` (since `s.z = B·s.r = B·b` on iteration 0); `pcg_steady_step` branch-free; `forget_z` composes with `forget_beta_prev` for the four-way equivalence.

### The Form-B home on disk (`book/src/L4/krylov-step.md`)

- `:28-33` — Form B signature already present: `first_step :: OpParams -> Krylov -> (SimState -> Solve {...carry: PrevCarry...})` / `steady_step :: ... -> (PrevCarry -> SimState -> ...)`.
- `:40` — `PrevCarry` shape contract: "the closure-threaded recurrence carry ... For CG: `β_prev`".
- `:82` — the §Semantics Form B paragraph; ENDS with the dangling slice citations (`cg.md:27-141`, `cg.md:52`, `cg.md:69`, "formerly cited as `cg.md:393-425`"). This is the insertion anchor — the new worked-example subsection lands immediately after it.
- `:152` — §Status references "the Form B v0.5 derivation remains live in the reduced slice at cg.md:27-141".
- `:171` — §Evidence bullet: "the unique material RETAINED live in the reduced slice at `book/src/spec/slices/cg.md:27-141` (`cg_first_step` at `cg.md:52`, `cg_steady_step` at `cg.md:69`, the `iterate_while_with_prev` driver at `cg.md:95-108`)".

These three pointers (`:82`, `:152`, `:171`) all become dangling when D2 deletes the slice this cycle; this dispatch re-anchors all three.

### The L0 terminal home (re-anchor target; on-disk status `rough-in`)

- `book/src/L1-L0/ksp-solve-mutation-rotation.md:159` — `### Sub-pattern B — inner CG body (CgSolver<OperType>::Mult)`.
- `:163` — `palace/linalg/iterative.cpp:360-486`.
- `:217` — "Per-step inner kernel + convergence test (`iterative.cpp:427-464`)".

### L0 source confirmed (`reference/palace/palace/linalg/iterative.cpp`)

`citecheck --anchor` + on-disk read confirm the v0.5-relevant CG body — the SAME body the branch-unrolled form renders:

- `:427-464` — the per-step `for (; it < max_it && !converged; it++)` loop (citecheck `[ok]`, anchor `p = z` at `:436`).
- `:434-441` — the `if (!it) { p = z; } else { AXPBY(1.0, z, beta/beta_prev, p); }` first-iteration branch (citecheck `[ok]`, anchor `if (!it)` at `:434`) — the branch v0.5 unrolls out.
- `:443` — `A->Mult(p, z)` (the `apply opA`); `:444` `Dot(z, p)` → denom; `:446` `alpha = beta/denom`.
- `:448-449` — `x.Add(alpha, p)` / `r.Add(-alpha, z)` (the `axpy` pair).
- `:451` — `beta_prev = beta` (the carry v0.5 moves out of the state into a closure parameter).
- `:460` — `beta = Dot(z, r)`; `:462` `res = std::sqrt(std::abs(beta))`.
- `:360-486` — `CgSolver<OperType>::Mult` (ends at `:486`, on-disk read confirms `}`).

### Non-duplication confirmation

`concepts/first-iteration-unrolling.md:21-37` carries the ABSTRACT generic `first_step` / `steady_step` rotation signatures (referenced by `krylov-step.md:118,:166`). The new subsection lands ONLY the CG-CONCRETE typed bodies + the v0.4↔v0.5 equivalence + the pcg-variant as the worked instance; it does NOT restate the generic signatures — it cross-references the concept page for the abstract rotation, matching the existing `:82` / `:40` discipline.

## Proposed changes

Single file touched: `book/src/L4/krylov-step.md`. Two edits — (1) the new worked-example subsection inserted after the §Semantics Form B paragraph; (2)+(3)+(4) re-anchoring the three dangling `cg.md:*` slice-pointers (§Semantics `:82`, §Status `:152`, §Evidence `:171`).

### Edit 1 — insert the CG-concrete worked-example subsection under Form B's §Semantics (after line 82)

```edit:book/src/L4/krylov-step.md
Form B (first-iteration-unrolled) splits the body into two named functions per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) §"The rotation". `first_step` produces the initial `PrevCarry` from a base-case computation; `steady_step` consumes `PrevCarry` (the prior iteration's recurrence variable, e.g., `β_prev`) as a closure argument rather than reading it from `Krylov`. The `Krylov` schema in Form B is one slot lighter (no `β_prev` field); the branch-free `steady_step` is the body folded by `iterate_while_with_prev`. Both forms are valid L4 renderings of the same L2 `krylov-step`; the choice is the `first-iteration-unrolled` variant axis (inherited unchanged from L2). The CG instantiation of Form B is worked below; the abstract `(first_step, steady_step)` rotation it specialises lives in [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) §"The rotation" and is not restated here.

### Worked example — CG Form B (v0.5 first-iteration-unrolling)

This is the canonical CG instantiation of Form B: the `Krylov` bundle is `CgState<S>`, the `PrevCarry` is `β_prev`, and the rotation drops `β_prev` from the steady-state schema by threading it as a closure argument of the loop driver. It is the worked datum that grounds Form B and the `first-iteration-unrolling` concept; the abstract `(first_step, steady_step)` signatures it specialises are in [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) §"The rotation" (not restated here).

The v0.5 `CgState<S>` schema is one scalar lighter than the Form-A (v0.4) schema — `beta_prev` is gone:

    type CgState<S> = {
      x:         Tensor[S],
      r:         Tensor[S],
      p:         Tensor[S],
      beta:      Scalar,        // (r, r); always nonzero on entry to a steady step
      it:        Int,
      converged: Bool,
    }
    -- `beta_prev` is gone. The steady step uses (s.beta / beta_prev) where
    -- beta_prev is supplied as a closure-captured scalar from the prior step,
    -- not a state field.

The first iteration is unrolled (precondition `s.it == 0`, so `p ← r` unconditionally — the Form-A `if it == 0` branch is hoisted out); the steady step is branch-free (precondition `s.it >= 1, beta_prev > 0`):

    cg_first_step
      :: LinOp<S> -> Scalar -> CgState<S>
      -> { state: CgState<S>, residual_norm: Scalar }
    cg_first_step opA eps s =
      let p'    = s.r in                         -- s.it == 0 ⇒ p ← r
      let Ap    = apply opA p' in
      let alpha = s.beta / (dot Ap p') in
      let x'    = axpy alpha p' s.x in
      let r'    = axpy (negate alpha) Ap s.r in
      let beta' = dot r' r' in
      let res'  = sqrt (abs beta') in
      { state: { x: x', r: r', p: p',
                 beta: beta',
                 it: 1, converged: res' < eps },
        residual_norm: res' }

    cg_steady_step
      :: LinOp<S> -> Scalar -> Scalar -> CgState<S>
      -> { state: CgState<S>, residual_norm: Scalar }
    cg_steady_step opA eps beta_prev s =
      let p'    = axpby 1.0 s.r (s.beta / beta_prev) s.p in
      let Ap    = apply opA p' in
      let alpha = s.beta / (dot Ap p') in
      let x'    = axpy alpha p' s.x in
      let r'    = axpy (negate alpha) Ap s.r in
      let beta' = dot r' r' in
      let res'  = sqrt (abs beta') in
      { state: { x: x', r: r', p: p',
                 beta: beta',
                 it: s.it + 1, converged: res' < eps },
        residual_norm: res' }

The driver runs the first step, then folds `cg_steady_step` with `iterate_while_with_prev` — `iterate_while` over the pair `(state, beta_prev)`, threading the prior step's `beta` as the next step's `beta_prev` without storing it in `CgState`. This is a closure over the loop carry, not new calculus machinery:

    cg_solve
      :: !CgConfig -> LinOp<S> -> Tensor[S] -> Tensor[S] -> Bool
      -> { final_state: CgState<S>, residual_history: [Scalar] }
    cg_solve config opA b x_initial initial_guess =
      let { state: s0, initial_res } = cg_init opA b x_initial initial_guess in
      let eps = max (config.rel_tol * initial_res) config.abs_tol in
      if sqrt (abs s0.beta) < eps then
        { final_state: { ...s0, converged: True }, residual_history: [] }
      else
        let { state: s1, residual_norm: res1 } = cg_first_step opA eps s0 in
        if s1.converged || s1.it >= config.max_it then
          { final_state: s1, residual_history: [res1] }
        else
          let { final_state, trajectory } =
            iterate_while_with_prev s1 s0.beta
              (\(s, _) -> s.it < config.max_it && not s.converged)
              (\(s, beta_prev) ->
                let r = cg_steady_step opA eps beta_prev s in
                (r, s.beta)) in
          { final_state, residual_history: [res1] ++ trajectory.map(\t -> t.residual_norm) }

**What this CG rotation hides.** (a) The `beta_prev` state field is gone — the steady-state schema is one scalar lighter, and a reader of `CgState<S>` sees only fields with a non-trivial role at *every* step. (b) The `if s.it == 0` branch is gone from the step body — both `cg_first_step` and `cg_steady_step` are straight-line, each named primitive firing exactly once per call. (c) The `0/0`-avoidance precondition moves from a runtime branch to a static call-site obligation: `cg_steady_step` requires `beta_prev > 0`, automatically satisfied by construction (only ever called with `s.beta` from a strictly-preceding step, and `beta > 0` is the `CheckDot` precondition on SPD systems).

**Equivalence to Form A (v0.4↔v0.5).** The two CG forms are observationally identical for any input `(opA, b, x_initial, initial_guess, config)`: (1) both test `sqrt|beta_0| < eps` before any work — v0.5 as an outer `if`, v0.4 folded into the first `cg_step` via the `converged` field; (2) the first iteration runs `p' = s.r` in both (v0.4 via the `if` branch, v0.5 directly), with identical remaining body; (3) subsequent iterations run the same `axpby` (v0.4 reading `s.beta_prev` from state, v0.5 receiving `beta_prev` as a closure parameter), with identical `Ap`, `alpha`, `x'`, `r'`, `beta'`, `res'`; (4) `residual_history` is element-for-element identical. The projection `forget_beta_prev : CgState_v04<S> → CgState_v05<S>` that drops `beta_prev` makes the equivalence formal — `cg_step` and the v0.5 split commute through it (modulo the closure-vs-field choice of where `beta_prev` lives). This is the CG witness of the L4 non-law catalogued in §"Algebraic laws" (form-equivalence-under-monad-laws): Form A and Form B are trajectory-identical but NOT related by a monad-law β-reduction — the rotation drops a `Krylov` field and threads a closure argument.

**Variant: pcg under v0.5.** The preconditioned variant rotates symmetrically. `pcg_first_step` uses `p' = s.z` (since `s.z = B·s.r = B·b` on iteration 0); `pcg_steady_step` is branch-free. The `forget_z : PCgState → CgState` equivalence composes with `forget_beta_prev` to give the four-way equivalence between `pcg_*` Identity-instantiated and `cg_*` un-`z`'d.

**L0 ground.** Both CG forms render the *same* Palace CG body — the v0.5 unrolling is a purely L4-level rearrangement and does not change the L0/L1/L2/L3 forms (Palace's source keeps the `if (!it)` branch inside the loop). The terminal L0 home is [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md) §"Sub-pattern B — inner CG body" (`CgSolver<OperType>::Mult`, `palace/linalg/iterative.cpp:360-486`): the per-step for-loop at `iterative.cpp:427-464` carries the Form-A first-iteration branch `if (!it) { p = z; } else { AXPBY(1.0, z, beta/beta_prev, p); }` (`iterative.cpp:434-441`) that v0.5 hoists out, the operator apply `A->Mult(p, z)` (`iterative.cpp:443`), the `alpha`/`x.Add`/`r.Add` updates (`iterative.cpp:446-449`), the `beta_prev = beta` carry that v0.5 moves into the closure (`iterative.cpp:451`), and the `beta`/`res` readout (`iterative.cpp:460-462`).
```

### Edit 2 — re-anchor the §Status reference (line 152) off the to-be-deleted slice

```edit:book/src/L4/krylov-step.md
`firm` — typed-wrapper signature is the canonical fold-body shape for the `solve-monad`'s inner driver; algebraic laws are inherited from the L2 entry (with state-stratum independence sharpened by the typing) and reduced to one non-trivial property (the demand-pruning law) plus two structural invariants; non-laws are catalogued explicitly, including the form-equivalence non-law for Form A vs Form B; variant-axis profile is closed at six, inherited unchanged from L2. The pattern is well-attested at the L4 level across four slices' explicit L4 sections (CG L4 Form A `cg_step` and L4-v0.5 Form B `cg_first_step`/`cg_steady_step` — lifted into the firm `book/src/L2/krylov-step.md` §Evidence registry, line 138, per the cycle-009 corpus reduction, with the CG-concrete Form B v0.5 bodies now worked inline in §Semantics §"Worked example — CG Form B"; gmres.md:459-471; arnoldi_step.md:285-298), and the slot is the consumed-by surface for the L4 concepts `solve-monad`, `state-stratification`, and `first-iteration-unrolling`, which previously referenced "step" without a vocabulary anchor.
```

### Edit 3 — re-anchor the §Semantics Form B citation tail (the residual `cg.md:*` pointer at line 82 is removed by Edit 1; this confirms the new sentence carries no slice-pointer)

(Folded into Edit 1: the replaced line 82 paragraph drops the `cg.md:27-141 / cg.md:52 / cg.md:69 / cg.md:393-425` slice citations entirely and replaces them with the inline worked example + the concept-page cross-reference. No separate edit needed.)

### Edit 4 — re-anchor the §Evidence bullet (line 170-171) off the to-be-deleted slice

```edit:book/src/L4/krylov-step.md
  - CG L4 v0.5 `cg_first_step` / `cg_steady_step` split (Form B) — worked inline in this chapter's §Semantics §"Worked example — CG Form B (v0.5 first-iteration-unrolling)"; the canonical CG instantiation of the abstract rotation in `concepts/first-iteration-unrolling.md`, also registered in firm `book/src/L2/krylov-step.md` §Evidence (line 138). The L0 ground is the same CG body as Form A: [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md) §"Sub-pattern B" (`palace/linalg/iterative.cpp:360-486`; per-step for-loop `:427-464`; first-iteration branch `:434-441`). (This material was previously retained live in the reduced slice at `book/src/spec/slices/cg.md:27-141`, absorbed here in cycle-099 so the slice is clear-to-delete; original pre-reduction range was `cg.md:393-425`.)
```

## Open questions / caveats

- **`book/src/spec/slices/cg.md:27-141` is now FULLY HOMED and clear-to-delete.** The one genuinely-unlifted live datum (the CG-concrete v0.5 first-iteration-unrolling worked instance — `cg_first_step` / `cg_steady_step` / `iterate_while_with_prev` driver / `forget_beta_prev` projection / v0.4↔v0.5 equivalence / pcg-variant) is absorbed inline into `book/src/L4/krylov-step.md` §Semantics §"Worked example — CG Form B" by this dispatch. The three former slice-pointers (§Semantics `:82`, §Status `:152`, §Evidence `:171`) are re-anchored to the inline home + the L0 terminal home (`L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B, on-disk status `rough-in`). The remaining slice content above `:27` is the cycle-009 stub header (already superseded per its own list at `cg.md:5-14`) plus four still-pending working-note OQs at `cg.md:18-23` (initial-residual quirk, CheckDot per-call-site, unpreconditioned-as-primary modeling, unit-test coverage gap) — these are scaffolding-OQ targets, NOT book-chapter content, so they do not block deletion (they should be migrated to `scaffolding/open-questions.md` if not already, by D2/the integrator, before the slice file is removed). **D2 (this same cycle) owns the slice delete + the SUMMARY/spec-index repoint.** This dispatch touched ONLY `book/src/L4/krylov-step.md` per the hard constraint.

- **No abstract-rotation duplication.** The generic `first_step` / `steady_step` signatures stay solely in `concepts/first-iteration-unrolling.md:21-37`; the new subsection cross-references that page and lands ONLY the CG-concrete specialisation. Verified `krylov-step.md:118,:166` already link the concept page; the worked example adds the concrete witness those links describe abstractly.

- **Status stays `firm`** under the firm-on-positive-structure escape: the worked example's claims are syntactic L4-self-rotation identities (the `forget_beta_prev` commutation, the branch-hoisting equivalence) on a fully-specified read closure (`CgSolver::Mult`, `iterative.cpp:360-486`), the same law-confidence basis as the chapter's existing Form A / Form B treatment. No new test is gated because no convergence-semantics claim is made — only the v0.4↔v0.5 observational-identity rotation, which is a structural rewrite on positive source.

## Supporting evidence

- Absorb target / Form-B home: `book/src/L4/krylov-step.md:28-33` (Form B signature), `:40` (`PrevCarry`=`β_prev` for CG), `:82` (§Semantics Form B paragraph + dangling slice-pointers), `:110` (the form-equivalence non-law the worked example witnesses), `:152` (§Status slice-pointer), `:171` (§Evidence slice-pointer).
- Absorbed datum: `book/src/spec/slices/cg.md:39-50,:52-67,:69-84,:86-106,:108,:110-114,:120-129,:131-133`.
- Non-duplication anchor: `book/src/concepts/first-iteration-unrolling.md:21-37`.
- L0 terminal home (on-disk status `rough-in`): `book/src/L1-L0/ksp-solve-mutation-rotation.md:159,:163,:217`; `reference/palace/palace/linalg/iterative.cpp:360-486,:427-464,:434-441,:443,:446-449,:451,:460-462` (all citecheck/on-disk verified this dispatch).
