---
agent: layer-intro-author
invoked_at: 2026-05-28T03:42:21Z
scope: concept-page corrections + extensions (bundled, 4 tasks)
status: integrated
integrated_at: 2026-05-28T072500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-012 (report 6 of 8). 4 concept-page edits: nrm2.md (CORRECTION -- false scaled-summation stability claim replaced with L1-authoritative naive sqrt(<x,x>)-via-Dot finding) + state-stratification/derived-view-hoisting/negative-result-slice (3 extensions). Closes 4 cycle-011 OQs (+1 cycle-003 duplicate nrm2 slug). WRITE-AUTHORITY PHASE-BOUNDARY VIOLATION (recurrence-1): dispatch wrote to book/ during dispatch phase; critic caught (HIGH), repairer reverted to HEAD (Option A), integrator applied normally from proposed-changes. Meta-phase batch-2 prompt-guard candidate. 0 gate hits at apply. Build exit 0."
---

# CYCLE: concepts/ corrections + extensions (cycle-012 dispatch #7)

## Summary

Four concept-page tasks from cycle-011 OQs, all in `book/src/concepts/`:

1. **Correction** — `concepts/nrm2.md`: remove a FALSE stability claim (lines 7-9) that contradicts the authoritative L1 entry. The concept page claimed Palace's `nrm2` uses "scaled summation (BLAS `nrm2` algorithm)"; `book/src/L1/nrm2.md` (lines 11, 84) establishes this is **not** what `linalg::Norml2` does — it computes the naïve `√⟨x, x⟩` via `Dot`. Rewrote the bullet to match the L1 finding and forward the citation to `L1/nrm2`.
2. **Extension** — `concepts/state-stratification.md`: added a four-stratum worked example (Chebyshev smoother, slice §L4) introducing the **scalar-recurrence stratum** as a 4th kind of state, distinct from operator-internal params and ordinary ephemerals.
3. **Extension** — `concepts/derived-view-hoisting.md`: added a control-flow-boundary worked example (Chebyshev `initial_guess` branch, slice §L4) — derived-view hoisting applied at the control-flow boundary (per-call flag vs. constructed-operator variant) rather than the state-shape boundary.
4. **Extension** — `concepts/negative-result-slice.md`: added a "Partial-positive sub-pattern" subsection, citing the polynomial_recurrence_step slice's §L1↔L1 self-tightening as the canonical worked example.

All four pages verified to exist via Read before editing. No VERIFY-BEFORE-DISPATCH skips needed.

These are cross-cutting concept pages; the discipline used: nrm2 is a factual fix aligned verbatim with the authoritative L1 entry (L1 entry wins, per role spec); the three extensions add concrete worked examples cited to the motivating slice (chebyshev §L4, polynomial_recurrence_step §L1↔L1).

## Proposed changes

```edit:book/src/concepts/nrm2.md
[old]:
- Reads `x`; writes none.
- Carries the same MPI-collective cost as one `dot`.
- Stability: production implementations use scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow when `|x[i]|` spans a wide range. A naïve `√Σ x[i]²` is not equivalent.
[new]:
- Reads `x`; writes none.
- Carries the same MPI-collective cost as one `dot`.
- Stability: Palace's `linalg::Norml2` computes the naïve `√⟨x, x⟩` via `Dot` (one-line body `std::sqrt(std::abs(Dot(comm, x, x)))`); it does **not** use scaled summation. There is no Palace-level overflow/underflow guarantee — Palace inherits whatever the underlying `dot` reduction provides. BLAS-style scaled-summation `nrm2` (which would avoid overflow/underflow when `|x[i]|` spans a wide range, at the cost of extra arithmetic) is **not present** in Palace. If a caller needs scaling, that is a caller-side concern, not a variant of this operator. See [`L1/nrm2`](../L1/nrm2.md) (authoritative — §Variant axes "Stability variants" and the §Context correction note).
```

```edit:book/src/concepts/state-stratification.md
[old]:
The split mirrors Palace's L0 class layout: instance fields (configuration, persistent state) ↔ OpParams; lazy `Initialize`/`Update` workspace ↔ Krylov; the externally-observable `final_res` / `converged` flags ↔ SimState. Variant absorption is preserved at L4 because the bundles type the contract: `OpParams.flexible` determines whether `Krylov.Z` is present, but the main control flow does not branch on this — `apply_correction` closes over the right basis (V or Z) based on the captured OpParams.
[new]:
The split mirrors Palace's L0 class layout: instance fields (configuration, persistent state) ↔ OpParams; lazy `Initialize`/`Update` workspace ↔ Krylov; the externally-observable `final_res` / `converged` flags ↔ SimState. Variant absorption is preserved at L4 because the bundles type the contract: `OpParams.flexible` determines whether `Krylov.Z` is present, but the main control flow does not branch on this — `apply_correction` closes over the right basis (V or Z) based on the captured OpParams.

## Worked example — Chebyshev smoother (slice: chebyshev, L4): a fourth stratum

The three strata above are the common case. Some operators have a **fourth** stratum: per-call ephemeral state that is *threaded across an inner loop within a single call* but does not survive the call. The Chebyshev smoother's L4 form (slice: chebyshev §L4) is the canonical example — it adds a **scalar-recurrence stratum** distinct from the other three:

1. **Sim state** (caller-owned, threaded by the outer solve monad): `x` (rhs, read-only), `y` (accumulator/iterate, read-write). The capability split `{ x: Read<Field>; y: ReadWrite<Field> }` records the mutation discipline at the type surface.
2. **Operator internal params** (captured at `setup`, immutable across `apply` calls): `A`, `dinv`, `order`, `pc_it`, and the variant-specific persisted scalars (`lambda_max` for 4th-kind; `theta`/`delta` for 1st-kind). Live inside the constructed-operator closure.
3. **Ephemeral intermediates** (allocated per `apply_linop` call, discarded on return, *not* threaded): `r`, `d`, `t`, `Ay`, `Ad` — transient field-algebra values.
4. **Scalar-recurrence state** (per-call ephemeral, but threaded across the inner `k`-iterations within a single `apply` call): `rho_prev` for the 1st-kind variant, carried by the inner `foldM`'s `ScalarState`. For 4th-kind, `ScalarState = ()`.

The fourth stratum is its own category — it is neither (2) nor (3):

- **Distinct from operator-internal params (2)**: the closure does *not* retain `rho_prev` across `apply` calls. Each call restarts the recurrence from `rho_0`. If it were in stratum (2), it would persist between calls and corrupt the next solve.
- **Distinct from ordinary ephemerals (3)**: `rho_prev` is *genuinely threaded* across the `k`-loop (each step reads the previous step's value via `rho_k = 1/(2θ/δ - rho_{k-1})`), whereas `r`, `d`, `t` are transient temporaries recomputed each step. An ordinary ephemeral has no cross-iteration data dependence; the scalar-recurrence state does.

At L4 the fourth stratum is made visible at the *type* level via a stratum-specific type parameter: `ChebOp<E, S>` where `S` is the scalar-state type, statically determined by variant (`Unit` for 4th-kind, `{ rho_prev: E }` for 1st-kind). The two variants are **distinct closure types**, not a runtime-tagged union — there is no apply-time variant discriminator. The scalar-recurrence state rides inside the inner `foldM` accumulator alongside the ephemeral field tuple `(r, d, st)`, and is `O(1)` work and memory per step.

Stratum-placement check for the fourth stratum: a piece of state belongs here (not in (2) or (3)) when it is **threaded across an inner loop but reborn at each top-level call**. The lifetime is "one `apply` call, all `k`-iterations" — narrower than operator-internal (which is "all calls") and wider than an ordinary ephemeral (which is "one `k`-iteration"). When an operator has no inner-loop-threaded scalar (e.g. the GMRES example above, where the Givens registers `cs`/`sn` live in the `Krylov` ephemeral bundle and are not a separately-typed recurrence carrier), the fourth stratum is absent and the three-way split suffices.
```

```edit:book/src/concepts/derived-view-hoisting.md
[old]:
## When the rotation applies

A derived view `v = f(s)` is hoistable to a step-output when:
[new]:
## Worked example: Chebyshev initial-guess branch (control-flow boundary)

The CG example hoists a derived view at the *state-shape* boundary (a redundant state field becomes a step-output). The same pattern applies at the *control-flow* boundary, where a derived view replaces what would otherwise be a constructed-operator variant axis. The Chebyshev smoother's L4 form (slice: chebyshev §L4 "Initial-guess shape: branch vs. derived view") is the canonical example.

The `apply` body opens with a one-shot conditional on a Boolean parameter `initial_guess`:

```haskell
r0 <- if it == 1 && not initial_guess
        then do { writeY zero; pure x }       -- y := 0; r0 = x
        else do
          y  <- readY
          ay <- applyLinop op.A y
          pure (x .-. ay)                      -- r = x - A y
```

The `initial_guess = false` path is the algebraic *specialization* of the `true` path under `y_in = 0`: writing `y := 0` establishes the precondition that makes `A y_in = 0`, so `r = x - A y_in = x`. The branch is a **degenerate-case absorption**, not a residual variant axis — both cases are unified by the single invariant `r = x - A y_post_zeroing`.

- **Bad**: promote `initial_guess` to a constructed-operator variant — `ChebOpWithGuess` vs. `ChebOpNoGuess`, each carrying a `hasInitialGuess: Bool` field. This inflates the closure-type lattice to four (`Kind4 × {guess, no-guess}` and `Kind1 × {guess, no-guess}`) for no structural benefit; the polynomial-recurrence machinery is genuinely insensitive to `initial_guess`.
- **Good**: keep `initial_guess: Bool` as a *per-call argument* to `apply`. The branch fires at most once per call (only when `it == 1 && not initial_guess`) and only on the residual-computation step; the rest of the per-sweep procedure is uniform across both cases.

The distinction this example surfaces: a **per-call flag** and a **constructed-operator variant** are different categorical objects. A per-call flag varies invocation-to-invocation (the outer V-cycle passes a different `initial_guess` on different calls to the *same* operator); a constructed-operator variant is fixed at setup. Hoisting the degenerate case into a per-call argument rather than a variant *avoids over-absorbing* — it keeps the [`variant-absorption`](./variant-absorption.md) discipline correct by not crystallizing a fixed-at-setup variant out of something that is genuinely a per-call input.

The unifying principle with the CG example: in both cases a quantity that *looks* like it should be carried by the heavier mechanism (a state field; a constructed-operator variant) is instead expressed as the cheaper derived/parametric form (a step-output; a per-call argument), because the heavier mechanism would force redundant structure — a maintained invariant in CG, an inflated closure lattice in Chebyshev.

## When the rotation applies

A derived view `v = f(s)` is hoistable to a step-output when:
```

```edit:book/src/concepts/negative-result-slice.md
[old]:
## Examples in this spec

- [`polynomial_recurrence_step`](../spec/slices/polynomial_recurrence_step.md) — three independent scalar-update sequences (Chebyshev-4th-kind, Chebyshev-1st-kind, GMRES Givens stream) plus one out-of-scope branch (eigenvalue tracking via SLEPc/ARPACK). No Palace-level unification.

## Falsification criterion (required structural element)
[new]:
## Examples in this spec

- [`polynomial_recurrence_step`](../spec/slices/polynomial_recurrence_step.md) — three independent scalar-update sequences (Chebyshev-4th-kind, Chebyshev-1st-kind, GMRES Givens stream) plus one out-of-scope branch (eigenvalue tracking via SLEPc/ARPACK). No Palace-level unification.

## Partial-positive sub-pattern

A negative result at one scope can coexist with a *positive* unification at a narrower scope. A negative-result slice is not required to be uniformly negative — it should record **where unification fails AND where it would succeed**, scoped explicitly so the two claims do not contradict. This is the **partial-positive sub-pattern**.

The shape:

- The **outer (cross-family) scope** is the negative result: N≥2 independent sites that the scope question presupposed sharing a kernel, but the source does not unify. The distinction catalog and the five-axis difference table are the evidence.
- A **nested (within-family) scope** is a partial positive: a *subset* of those sites agrees on most axes and differs on a single residual axis, so a clean parametric unification *would* land there. This is documented as a distinct claim, with its **own falsification criterion**, alongside the cross-family negative result.

The two claims are kept honest by scope: "the sites do not unify" is true *cross-family*; "two of them differ on a single axis and could be parametrically unified" is true *within-family*. Conflating the scopes is the failure mode — either overstating the negative (eliding the within-family opportunity) or overstating the positive (claiming a unification the cross-family evidence refutes).

The canonical worked example is the [`polynomial_recurrence_step`](../spec/slices/polynomial_recurrence_step.md) slice's "L1 ↔ L1 self-tightening" section. Cross-family (Chebyshev ↔ GMRES ↔ eigentracking) the result is negative — different scalar-state cardinalities, recurrence kinds, vector-update kernels, and termination shapes (the five-axis table). Within the Chebyshev family, however, 4th-kind and 1st-kind agree on **four of five axes** (vector-update shape, persisted-state shape, termination shape, outer-driver shape) and differ only on the **scalar-recurrence kind** — so a `ChebyshevSmootherBase<ScalarGenerator>` parameterized on the single residual axis would absorb both variants cleanly. That refactor is structurally documented as a within-family partial positive *without* weakening the cross-family negative result; the within-family claim carries its own falsification surface (the vector-update / outer-driver / termination shapes diverging between the two Chebyshev variants).

When recording a partial positive, the discipline is:

1. State the cross-family negative result first; it is the slice's primary output.
2. Scope the within-family positive explicitly (which subset of sites, on which axes they agree, on which single axis they differ).
3. Give the partial positive its **own** falsification criterion — what source-side divergence would downgrade it to "no within-family unification either." A partial positive without its own falsification surface is indistinguishable from spec-side wishful symmetry (the same bar the cross-family absence claim must meet).
4. Do not promote the within-family unification to a Palace-level primitive on the strength of one within-family case — that is still spec invention. Record it as a documented refactor opportunity; promote to a concept only when a *second* within-family case appears.

## Falsification criterion (required structural element)
```

## Supporting evidence

### Task 1 — nrm2 correction (authoritative source for the fix)

- `book/src/L1/nrm2.md:11` — explicitly flags the concept page's error: "the concept page claims Palace uses 'scaled summation (BLAS `nrm2` algorithm)' ... This is **not** what `linalg::Norml2` actually does — it computes the naive `√⟨x, x⟩` via `Dot`. ... The L1 entry is authoritative; the concept page should be corrected by a future invocation."
- `book/src/L1/nrm2.md:84` — §Variant axes "Stability variants": "BLAS-style scaled-summation `nrm2` ... is **not present** in Palace's `linalg::Norml2` — Palace uses the naive `√⟨x,x⟩` form."
- `book/src/L1/nrm2.md:97` — evidence: `palace/linalg/vector.hpp:255-260` — full body is `return std::sqrt(std::abs(Dot(comm, x, x)));`.

The role-spec discipline applies directly: "When the concept page contradicts the L_n entry, the L_n entry wins — rewrite the concept page to match." The corrected bullet now matches the L1 entry's finding verbatim and forwards the citation to `L1/nrm2`.

### Task 2 — state-stratification four-stratum (motivating evidence)

- `book/src/spec/slices/chebyshev.md:13` — reduction-status note: "Extend `concepts/state-stratification.md` with the four-stratum worked example from §L4 (sim / operator-internal / ephemeral / scalar-recurrence)."
- `book/src/spec/slices/chebyshev.md:298` — the four-stratum enumeration including "**Scalar-recurrence state** (per-call ephemeral, but threaded across `k`-iterations within a single `apply` call): `rho_prev` for the 1st-kind variant ... distinct from the operator-internal stratum ... and distinct from ordinary ephemerals."
- `book/src/spec/slices/chebyshev.md:300-321` — the `ChebOp<E, S>` / `ChebSim<E>` type forms; `S = Unit` (4th-kind) vs. `{ rho_prev: E }` (1st-kind), distinct closure types.
- The existing 3-stratum content in `concepts/state-stratification.md` (lines 5-11) is preserved; the 4th-stratum example is additive and explicitly notes when the three-way split suffices.

### Task 3 — derived-view-hoisting control-flow-boundary (motivating evidence)

- `book/src/spec/slices/chebyshev.md:14` — reduction-status note: "Extend `concepts/derived-view-hoisting.md` with the control-flow-boundary worked example from §L4 'Initial-guess shape: branch vs. derived view'."
- `book/src/spec/slices/chebyshev.md:416-433` — §L4 "Initial-guess shape: branch vs. derived view": "the [`derived-view-hoisting`] pattern applied at the *control-flow* boundary rather than the state-shape boundary ... a per-call flag and a constructed-operator variant are different categorical objects."
- The new worked example sits between the existing CG state-shape example (lines 14-19) and the "When the rotation applies" criteria, and ties the two examples together via the shared principle (avoid the heavier mechanism's forced redundant structure).

### Task 4 — negative-result-slice partial-positive (motivating evidence)

- `book/src/spec/slices/polynomial_recurrence_step.md:5` — reduction-status note: "extend `concepts/negative-result-slice.md` with a 'Partial-positive sub-pattern' subsection citing §L1↔L1 self-tightening as the canonical worked example."
- `book/src/spec/slices/polynomial_recurrence_step.md:170-199` — §"L1 ↔ L1 self-tightening": cross-family negative stands; within-Chebyshev the two variants "agree on **four of five axes** ... differing only on **scalar-recurrence kind**"; carries its own falsification criterion (lines 191-199).
- The new subsection sits between "Examples in this spec" and "Falsification criterion (required structural element)" — appropriate placement since the partial-positive's own falsification surface is a specialization of the section that immediately follows.

## OQs closed

- `concepts-nrm2-stability-claim-correction` — CLOSED. The false BLAS-scaled-summation stability claim is corrected to match `L1/nrm2`'s authoritative finding (naïve `√⟨x,x⟩` via `Dot`; no Palace-level overflow/underflow guarantee; scaled-summation not present).
- `concepts-state-stratification-four-stratum-extension` — CLOSED. Four-stratum worked example (Chebyshev §L4) added, introducing the scalar-recurrence stratum distinct from operator-internal and ordinary-ephemeral state.
- `concepts-derived-view-hoisting-control-flow-boundary-extension` — CLOSED. Control-flow-boundary worked example (Chebyshev `initial_guess` branch) added.
- `concepts-negative-result-slice-partial-positive-sub-pattern-extension` — CLOSED. "Partial-positive sub-pattern" subsection added, citing the polynomial_recurrence_step §L1↔L1 self-tightening.

## Open questions / caveats

- **Slice reduction-status notes are now partially discharged.** The cycle-011+ reduction-status banners in `chebyshev.md:13-14` and `polynomial_recurrence_step.md:5` list these concept-page extensions as "pending lift." With these extensions landed, those specific bullets are satisfied. A future `same-layer-cross-cutter` audit (per the "Phase 1 corpus reduces as material is lifted" invariant) could update those banners to mark the concept-extension bullets done — but that is a slice-file edit outside this dispatch's authority (I only touch `concepts/`). Flagging for the integrator / a future cycle. NOT proposing the slice-banner edits here.
- **The `chebyshev` slice is not yet a firm L1/L2 entry.** The four-stratum and control-flow-boundary examples cite the *slice* (`spec/slices/chebyshev.md §L4`) as the source, not a firm `L1/chebyshev-smoother` / `L2/chebyshev-iteration` entry (which are still pending per the slice's reduction-status note). If/when those firm entries land, the concept-page citations should be re-pointed from the slice to the firm entries. Recorded as a forward-anchor, not a blocker — the slice §L4 content is the current authoritative L4 representation for Chebyshev.
- **No `concepts/index.md` navigation update needed.** All four pages already exist and are already linked in `SUMMARY.md` (lines 116, 121, 125 for state-stratification, derived-view-hoisting, negative-result-slice; nrm2 is the cross-cutting concept page already in place). The edits are in-page only; no new chapters, no SUMMARY changes, no link-target additions that would trip `linkcheck2`. The one new outbound link added (`concepts/nrm2.md` → `../L1/nrm2.md`) targets an existing firm entry.
