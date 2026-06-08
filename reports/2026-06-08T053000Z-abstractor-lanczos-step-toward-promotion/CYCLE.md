---
agent: abstractor
invoked_at: 2026-06-08T053000Z
scope: L3 lanczos_step advance toward promotion — lanczos-step-toward-promotion
status: integrated
integrated_at: 2026-06-08T165758Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-139 (batch-45 OPENER, 1/3). 5 in-place edits to book/src/L3/lanczos_step.md; STAYS rank-0 roadmap_goal (arm-A positive-structure UNSATISFIABLE from palace/ — MINRES enum-only-stub; live path arm-B blocking-consumer); eigsolve-impl roadmap_goal->stub did NOT fire. 2 OQs. NOTE: the finalize step-5c build-repair converted this chapter's §Signature indented $-sigil block to a fenced ```text block (KaTeX collision)."
inputs:
  - book/src/L3/lanczos_step.md (the roadmap_goal chapter advanced)
  - book/src/L3/eigsolve-impl.md (the pulling kernel-impl consumer; front-3 of batch-45)
  - book/src/L3/krylov-step.md (firm; the operator lanczos_step specializes)
  - book/src/L1-L0/minres-iteration.md (the L0 home; enum-only-stub obstruction, empty L0 RHS)
  - book/src/L1/index.md:202 (the lanczos_step rough-in dep-map row)
  - book/src/semantics/index.md §1.2.1–§1.2.2, §1.2.2-R (operator-shape spelling)
---

# CYCLE: L3 lanczos_step advance toward promotion — lanczos-step-toward-promotion

## Summary

`L3/lanczos_step` is front-3's named blocker: building/advancing it is the named consumer
that fires `eigsolve-impl`'s `roadmap_goal → stub` promotion condition (`eigsolve-impl.md:40,49,129`).
I advanced the chapter against its on-disk positive structure and reached the **redirect-correct
finding**: `lanczos_step` **STAYS `roadmap_goal`**. The symmetric three-term recurrence
`w = A·v_j − α_j·v_j − β_{j-1}·v_{j-1}` is well-formed and composes only firm constituents
(`apply_linop`, `dot`, `nrm2`, `axpy`, `scal`), but its L0 home — MINRES — is an
`obstruction (enum-only-stub)` with an **empty L0 RHS** (`minres-iteration.md:41-59`: the
recurrence is *literature-anchored* against Paige–Saunders, NOT read from a positive Palace site;
`KrylovSolver::MINRES` routes to `MFEM_ABORT` at `ksp.cpp:53-57`). Per DIRECTIVE-3 +
no-forced-pull-up, there is no positive site to ground it to `stub`/`rough-in`, so it stays a
claim-free `kernel-impl-constituent` intent node — and that is a finding, not a failure.

The advance is therefore a **sharpening within `roadmap_goal`**, not a promotion: (1) tighten
§Signature to the `LinOp[(S: ...), $S]` operator-value spelling (§1.2.2 / §1.2.2-R), making the
high-order operator-apply argument explicit instead of bare `A`; (2) sharpen §Semantics to state
the band-3 collapse and the `reorthogonalization` variant axis as the *named numerical caveat the
promotion gate must resolve*; (3) **state the promotion gate explicitly** as a two-arm condition
(positive-L0-OR-MFEM-substrate-decision AND blocking-consumer) with the explicit note that arm-1
is currently **unsatisfiable in `palace/`** (the redirect-correct floor); (4) fix the citation
drift `L1/index.md:179 → :202` (the lanczos_step rough-in row is at line 202; 179 is
`nleps_deflated_residual`). The `specializes` edge to firm `krylov-step` and the
`reorthogonalization` / `matrix-pencil` variant axes are confirmed correct on disk and unchanged.

## Proposed changes

```edit:book/src/L3/lanczos_step.md
[Replace the §"kernel-impl form (the constructive realization)" Shape-contract block + signature,
 the §Status block, and the two L1/index.md:179 citation-drift occurrences (§"Relationship to
 krylov-step" line and §Evidence row). Author the full sharpened sections inside this fence.]
```

The four edits below are the integrator's apply targets. Each is an exact-string replacement on
`book/src/L3/lanczos_step.md`.

### Edit 1 — §Signature shape-contract + operator-value spelling (tighten)

Replace:

    Shape contract (the operator-domain shape group `S` per [`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2; `v_prev`, `v_curr`, `v_next` each `Tensor[(S: ...), complex]`; the recurrence coefficients `α_j, β_j` scalar):

        lanczos_step :: (A, v_prev, v_curr, β_prev) -> (v_next, α_j, β_j)
        -- A : the (shift-inverted) symmetric/Hermitian operator op.operand ▷ op.inv action (from eigsolve-impl's op)
        -- v_prev, v_curr : the previous two orthonormal basis columns BV[j-1], BV[j]
        -- β_prev : the prior off-diagonal coefficient (β_{j-1}); β_{-1} = 0 at the first step (first-iteration-unrolled)

With:

    Shape contract (the operator-domain shape group `S` per [`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2; the operator `A` carries the square operator-VALUE spelling `LinOp[(S: ...), $S]` of §1.2.2 / §1.2.2-R — a Hermitian operator on the basis-column domain `S`, the closed-over shift-invert action, NOT a bare type-application; `v_prev`, `v_curr`, `v_next` each `Tensor[(S: ...), complex]` congruent to that domain; the recurrence coefficients `α_j` real, `β_j` real-nonnegative; USED + linked, the convention is not restated here):

        lanczos_step :: LinOp[(S: ...), $S] -> Tensor[$S, complex] -> Tensor[$S, complex] -> RealScalar
                     -> (Tensor[$S, complex], RealScalar, RealScalar)
        -- positional: A v_prev v_curr β_prev -> (v_next, α_j, β_j)
        -- A      : the (shift-inverted) symmetric/Hermitian operator — op.operand ▷ op.inv action from eigsolve-impl's op;
        --          read-only across the step (closed-over !-tagged operator value per semantics §2 / §1.3.1).
        -- v_prev, v_curr : the previous two orthonormal basis columns BV[j-1], BV[j].
        -- β_prev : the prior off-diagonal coefficient β_{j-1} (real-nonnegative); β_{-1} = 0 at the first step (first-iteration-unrolled).

### Edit 2 — §Status (sharpen; state the promotion gate explicitly; STAYS roadmap_goal)

Replace:

    `roadmap_goal` (rank 0) — `kernel-impl-constituent` role. Claim-free intent node for the symmetric Lanczos basis-extension step. Rests on firm `L3/krylov-step` (specializes) + `L3/apply_linop` + `L1/dot` + `L1/nrm2` + `L1/axpy` + `L1/scal`. Pulled by [`eigsolve-impl`](./eigsolve-impl.md). Promotion: materialize against the symmetric-Lanczos L0 (the MINRES obstruction theme's literature-anchored form, `L1-L0/minres-iteration.md`) + a blocking consumer firms. The known-loss-of-orthogonality of the pure band-3 recurrence (the `reorthogonalization` variant axis) is the numerical caveat to resolve at firming.

With:

    `roadmap_goal` (rank 0) — `kernel-impl-constituent` role. Claim-free intent node for the symmetric Lanczos basis-extension step. Rests on firm `L3/krylov-step` (specializes) + `L3/apply_linop` + `L1/dot` + `L1/nrm2` + `L1/axpy` + `L1/scal`. Pulled by [`eigsolve-impl`](./eigsolve-impl.md) (advancing this node fires that consumer's `roadmap_goal → stub` promotion condition).

    **Why this STAYS `roadmap_goal` (the redirect-correct floor — a finding, not a failure).** This dispatch advanced the chapter against its on-disk positive structure and confirmed there is **no positive Palace site** to ground it to `stub`/`rough-in`. The symmetric three-term recurrence is **literature-anchored** (Paige–Saunders 1975), NOT read from a Palace L0 implementation: its L0 home [`minres-iteration`](../L1-L0/minres-iteration.md) is an `obstruction (enum-only-stub)` with an **empty L0 RHS** — `KrylovSolver::MINRES` routes to `MFEM_ABORT` (`palace/linalg/ksp.cpp:53-57`), there is no `MinresSolver<OperType>` class under `palace/linalg/`, and no test linkage (`minres-iteration.md:41-59,128-140`). Per DIRECTIVE-3 (no constructive impl is manufactured into a positive claim absent a positive site) + the no-forced-rectangular-pull-up redirect, the node holds at `roadmap_goal`. The constructive band-3 form below is a **speculative reconstruction in our firm vocabulary**, not a Palace-source claim.

    **Promotion gate (sharpened — a conjunction; arm-1 currently UNSATISFIABLE in `palace/`).**
    - **Arm A — positive structure** (`roadmap_goal → stub/rough-in`): EITHER (i) Palace gains an in-tree `MinresSolver`-shaped Lanczos kernel under `palace/linalg/iterative.cpp` (`minres-iteration.md:61-67`, route 1) — currently absent, so this arm cannot fire from the present `palace/` corpus; OR (ii) an integrator decision widens L0 to admit vendored MFEM `mfem::MINRESSolver` as L0 substrate (`minres-iteration.md:68-72`, route 2; MFEM not currently checked into `reference/`). Until one fires, arm A is **open by design** — this is the enum-only-stub obstruction floor, not a gap to force.
    - **Arm B — blocking consumer** (`→ firm`): a blocking `depends-on` consumer firms `lanczos_step` by use — the Hermitian arm of [`eigsolve-impl`](./eigsolve-impl.md), itself reachable from the `feature/eigenmode.L4` root. Currently `eigsolve-impl` is co-`roadmap_goal`; arm B fires when that fold materializes (RE3 deflate / RE8 krylov-iteration consumers, `eigsolve-impl.md:122-125`).
    - **Numerical caveat the firming must resolve.** The pure band-3 recurrence is the **unstable-but-cheap** default: it suffers known loss-of-orthogonality in finite precision (the `reorthogonalization` variant axis — `none` = pure three-term / `full` = re-orthogonalize against all prior BV columns / `selective` = Paige's criterion). The `matrix-pencil` axis (`standard` A-only vs `generalized` (A,B)-inner-product for `EPS_GHEP`) selects the inner product the orthogonality is measured in. Both axes are informational at `roadmap_goal`; a firm Lanczos kernel MUST pin a `reorthogonalization` policy (the band-3 alone is not numerically self-sufficient for a converged eigensolve).

### Edit 3 — §"Relationship to `krylov-step`" citation drift fix (L1/index.md:179 → :202)

Replace (in the §"Relationship to `krylov-step`" paragraph):

    The L2 [`krylov-step`](../L2/krylov-step.md) note (`book/src/L2/krylov-step.md:187`) already records this: *"MINRES is the symmetric specialisation of `arnoldiStep`; its `lanczos_step` would specialise `krylov-step`'s orthogonalization-variant axis to a band-3 form."* This chapter is that specialization, constructed.

With:

    The L2 [`krylov-step`](../L2/krylov-step.md) note (`book/src/L2/krylov-step.md:187`) already records this: *"MINRES is the symmetric specialisation of `arnoldiStep`; its `lanczos_step` would specialise `krylov-step`'s orthogonalization-variant axis to a band-3 form."* The `L1/index.md:202` rough-in dep-map row carries the matching signature `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` (constituents `apply_linop, dot, axpy, nrm2`). This chapter is that specialization, constructed (band-3, with the normalize `scal` made explicit).

### Edit 4 — §Evidence citation drift fix (L1/index.md:179 → :202)

Replace:

    - `book/src/L1/index.md:179` — the `lanczos_step` rough-in dep-map row `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` (the signature this chapter realizes) + its constituent list `apply_linop, dot, axpy, nrm2`.

With:

    - `book/src/L1/index.md:202` — the `lanczos_step` rough-in dep-map row `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` (`rough-in (obstruction, …)`; the signature this chapter realizes) + its constituent list `apply_linop, dot, axpy, nrm2`. (Prior chapter text cited `:179`; the row is at `:202` — `:179` is `nleps_deflated_residual`. Carry-forward drift fix.)

### Edit 5 — §roadmap_goal banner citation drift fix (L1/index.md:179 → :202)

Replace (in the `> **⟢ roadmap_goal (rank 0) — claim-free intent.**` banner line):

    It is the intent node for the symmetric three-term-recurrence basis-extension step the `L1/index.md:179` rough-in row names (from the MINRES `obstruction (enum-only-stub)` theme).

With:

    It is the intent node for the symmetric three-term-recurrence basis-extension step the `L1/index.md:202` rough-in row names (from the MINRES `obstruction (enum-only-stub)` theme).

## Speculative operators proposed

None new. `lanczos_step` itself remains the speculative `kernel-impl-constituent` (rank-0
`roadmap_goal`); this dispatch advanced its definition, did not promote it, and proposes no
sibling operator. The constituent set (`apply_linop`, `dot`, `nrm2`, `axpy`, `scal`) is all firm
and unchanged. The two inline sub-axes (`reorthogonalization`, `matrix-pencil`) stay informational
variant axes on the chapter, not separate operators.

## Supporting evidence

All citations self-verified this dispatch via `citecheck --anchor` against the on-disk file.

- `book/src/L1-L0/minres-iteration.md:1-9,41-59,61-72,97-110,128-140` — the L0 home: MINRES is an
  obstruction theme with an **empty L0 RHS**; the symmetric-Lanczos recurrence is literature-anchored
  (Paige–Saunders), `KrylovSolver::MINRES` routes to `MFEM_ABORT`, no `MinresSolver` class, no test
  linkage. The decisive evidence that `lanczos_step` has NO positive Palace site and STAYS `roadmap_goal`.
- `reference/palace/palace/linalg/ksp.cpp:53-57` — `KrylovSolver::MINRES` case routed to `MFEM_ABORT`
  (citecheck `[ok]`, anchor `MINRES` at :53). The absence-anchor.
- `book/src/L1/index.md:202` — the `lanczos_step` rough-in dep-map row, signature
  `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)`, `rough-in (obstruction, …)` (citecheck `[ok]`,
  anchor `lanczos_step` at :202). The row this chapter realizes; corrects the chapter's `:179` drift.
- `book/src/L3/krylov-step.md:1-16,33-68,153-164,210-211` — firm; the operator `lanczos_step`
  `specializes`. §Variant axes (orthogonalization-variant axis 2, the axis that collapses to band-3);
  the §Evidence note (`:210`) that "its `lanczos_step` at L3 would be a specialisation of this
  `krylov-step` with the orthogonalization-variant axis collapsed to a band-3 form." The
  `specializes` edge confirmed correct on disk.
- `book/src/L3/eigsolve-impl.md:40,49,82-84,122-129` — the pulling consumer (front-3); advancing
  `lanczos_step` fires its `roadmap_goal → stub` condition. The Hermitian arm `lanczos_step (op, s.BV, s.j)`
  is the blocking-consumer (arm B) shape.
- `reference/palace/palace/linalg/slepc.cpp:602-628` — `EPS_HEP` (:607) / `EPS_GHEP` (:613): the
  Hermitian / generalized-Hermitian problem types selecting the symmetric Lanczos recurrence (the
  `matrix-pencil` variant axis source; citecheck `[ok]`, anchor `EPS_HEP` at :607).
- `book/src/semantics/index.md` §1.2.1–§1.2.2, §1.2.2-R (`:73,:87,:97-110`), §1.3.1 (`:169-181`),
  §2 — the named-shape-group + operator-value-spelling + closure-ownership conventions the tightened
  §Signature USES + links (not restated). The `LinOp[(S: ...), $S]` operator-value spelling for `A`
  is the §1.2.2-R compliant form (avoids the opaque `LinearOperator[N,N]` type-application smell).

## Open questions / caveats

- **Arm-A unsatisfiability is structural, not transient.** `lanczos_step` cannot promote off
  `roadmap_goal` from positive structure until EITHER Palace adds an in-tree Lanczos kernel OR an
  integrator widens L0 to vendored MFEM. Neither is in the present corpus / scope. This is the
  enum-only-stub obstruction floor (`project_unimplemented_palace_components` — MINRES is explicitly
  named there as NOT a direct implementation target). Recorded so a future producer does not
  re-attempt a forced lift. **Lifting note (working-context, NOT chapter content):** were arm A to
  fire via the MFEM-substrate route, the lift would re-target the recurrence against
  `mfem::MINRESSolver` source (not in `reference/`); that is a reverse-direction L0-lift note, kept
  here per the high→low chapter discipline.
- **Arm B is the live promotion path this batch.** `eigsolve-impl` (front-3) is the blocking
  consumer; if it materializes its Hermitian-arm fold, `lanczos_step` firms *by use* even with arm A
  open (a `roadmap_goal` may be rested-on by a `roadmap_goal`; the firm-flip is gated on the consumer
  firming AND the numerical `reorthogonalization` caveat being pinned). The batch-45 front-3 advance
  on `eigsolve-impl` should re-check this gate.
- **No SUMMARY.md / dep-map registration change.** The chapter already exists and is registered;
  this is an in-place advance of an existing `roadmap_goal` chapter (status unchanged), so no new
  table row, no §Vocabulary-cohort bullet, no SUMMARY entry. The four edits are body refinements +
  a carry-forward citation-drift fix.
