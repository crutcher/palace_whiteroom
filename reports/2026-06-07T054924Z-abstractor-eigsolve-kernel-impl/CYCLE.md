---
agent: abstractor
invoked_at: 2026-06-07T054924Z
scope: L3 eigsolve kernel-IMPLEMENTATION (DIRECTIVE-3 item-2c) — constructive Krylov-Schur/Lanczos/Arnoldi eigensolve in our krylov-step/lanczos_step vocabulary
status: pending
inputs:
  - book/src/L3/eigsolve.md (the kernel-API surface; partial-obstruction, role-labeled kernel-api this dispatch)
  - book/src/L3/krylov-step.md (firm; the per-step Krylov body the impl folds — Arnoldi/Lanczos basis-extension constituent)
  - book/src/L4/krylov-step.md (firm; the typed-wrapper companion)
  - book/src/L1/index.md:179 (the lanczos_step rough-in dep-map row — NOT a chapter on disk; from the MINRES obstruction theme)
  - palace/linalg/slepc.cpp:630-654,687-710,731-736 (EPSSetType KRYLOVSCHUR, the EPSSolve opaque loop, EPSGetBV basis-vectors)
  - palace/linalg/arpack.cpp:270,273,278,318,342,369 (Arnoldi-iteration param, shift-invert mode, naupd basis driver, neupd extraction)
  - reports/2026-06-07T054924Z-cycle-planner-cycle-121/CYCLE.md (D5)
integrated_at: 2026-06-07T054924Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (repaired). L3/eigsolve-impl + L3/lanczos_step roadmap_goal (DIRECTIVE-3); finalize de-linked 2 dead README.md links in eigsolve-impl.md."
---

# CYCLE: L3 eigsolve kernel-IMPLEMENTATION — constructive Krylov-Schur eigensolve

## Summary

The L3 [`eigsolve`](book/src/L3/eigsolve.md) entry is the canonical **opaque-library partial-obstruction**: its per-step shift-invert body lifts, but the eigen-iteration loop (Krylov-Schur restart / Arnoldi-Lanczos basis extension / Rayleigh-Ritz / convergence) does **not** lift because *Palace authors no loop* — the iteration is entirely inside SLEPc `EPSSolve` / ARPACK `naupd`. DIRECTIVE-3 (kernel-API vs kernel-IMPLEMENTATION) says: for a spine-dependency opaque-library kernel with a well-understood in-our-semantics implementation, author BOTH the kernel-API surface (the existing obstruction, role-labeled `kernel-api`) AND a constructive `kernel-impl` node realizing the kernel from our firm primitives, linked by a `realizes-kernel-api` `reference`-class edge.

This dispatch sketches the **kernel-impl**: a constructive Krylov-Schur eigensolve as an explicit value-threaded **L3 iteration-rotation fold** over the firm [`L3/krylov-step`](book/src/L3/krylov-step.md) (its Arnoldi/Lanczos basis-extension instantiation) — `lanczos_step` for the symmetric/Hermitian shift-invert pencil (`EPS_HEP`/`EPS_GHEP`), `arnoldi`-flavored `krylov-step` for the non-symmetric pencil — building a `BV`-shaped Krylov basis to dimension `ncv`, then doing **Rayleigh-Ritz** extraction (project the shift-inverted operator onto the basis, solve the small dense eigenproblem, lift the Ritz vectors back), with **thick-restart** (Krylov-Schur) compressing the basis between cycles. The whole construction is exactly the `(krylov-step, ksp_solve)`-style kernel/driver pair the L3 `eigsolve` obstruction says *would* exist if Palace authored the loop — we author it. The eigen-iteration loop carries a `sequential-obstruction` (the basis trajectory reads the prior step's vector + the restart re-seed is carry-threaded) — preserved, not erased.

**Status decision (clean-gate).** The impl node lands as a **rank-0 `roadmap_goal`** (`book/src/L3/eigsolve-impl.md`): Palace does not author this loop (we are constructing an intended/speculative realization, not transcribing positive source), and the rank invariant forbids a `rough-in` (rank 2) from depending-on the `lanczos_step` constituent — which is itself **not on disk** (only a rough-in dep-map row at `L1/index.md:179`, from the MINRES enum-only-stub obstruction theme). Per the planner caveat, `lanczos_step` lands as a co-cycle **rank-0 `roadmap_goal` constituent** (`book/src/L3/lanczos_step.md`) and the impl `depends-on` it; a `roadmap_goal` may rest on anything (including other roadmap_goals + the firm `krylov-step`), so the well-foundedness invariant holds. When the c122 consumers (RE3 deflate/NLEPS, RE8 krylov-iteration view) wire their blocking `depends-on` edges and `lanczos_step` firms against positive structure, the impl promotes `roadmap_goal → stub → rough-in`.

**RE3 coupling (noted, not forced).** The deflate/NLEPS consumer (RE3) is the natural blocking consumer that grounds this impl next cycle: deflation extends the Krylov-Schur basis with locked converged vectors, and the NLEPS-deflated eigensolve is exactly this fold with a deflation-projection stage. I record the coupling in §Open-questions and as the impl's primary pulled-by provenance; I do NOT author a deflate edge this cycle (it is a c122 consumer dispatch).

## Proposed changes

```new:book/src/L3/eigsolve-impl.md
---
layer: L3
operator: eigsolve-impl
kind: kernel-impl
status: roadmap_goal
rank: roadmap_goal
edges:
  depends-on:
    - target: L3/krylov-step
      kind: folds                       # the per-step Arnoldi/Lanczos basis-extension body the eigen-iteration fold folds (firm); the eigsolve-impl's inner loop is iterate_while_L3 over this kernel's arnoldi/lanczos instantiation
    - target: L3/lanczos_step
      kind: folds                       # the symmetric/Hermitian three-term-recurrence basis-extension specialization for EPS_HEP/EPS_GHEP pencils (roadmap_goal co-cycle constituent; rank-0, may be rested on by this rank-0 node)
    - target: L3/ksp_solve
      kind: composes                    # the inner shifted-operator solve (K − σM)⁻¹ inside each basis-extension step — the shift-invert spectral-transform action (firm)
    - target: L3/apply_linop
      kind: composes                    # the whole-tensor operator-apply M·v (linear shift-invert) / K·v (no-transform) feeding the inner solve; and the Rayleigh-Ritz back-projection apply (firm)
    - target: L2/orthogonalize
      kind: composes                    # the basis-orthogonalization stage (MGS/CGS/CGS2) keeping the Krylov basis BV-orthonormal; the same op.orthog surface krylov-step folds (firm)
  reference:
    - target: L3/eigsolve
      kind: realizes-kernel-api         # DIRECTIVE-3: this constructive impl realizes the kernel-API surface (the partial-obstruction L3/eigsolve); reference-class (navigational, free — does NOT constrain rank, does NOT carry liveness; the impl does not block on the opaque API). lowering-verifier audits the impl↔API correspondence.
    - target: L4/eigsolve
      kind: realizes-kernel-api         # the L4 cap of the same kernel (the Solve-monadic outer-driver obstruction-marker wrapper); navigational sibling of the L3 kernel-api
    - target: semantics/index           # §1.2.1–§1.2.2 named-shape-group convention; §3.7 iterate_while; §3.8 demand-pruning — USED + linked, not restated
    - target: concepts/sequential-obstruction
    - target: concepts/constructed-operators
    - target: concepts/solver-as-operator
variant_axes:
  - eigen-algorithm (krylov-schur = thick-restart Arnoldi/Lanczos / arnoldi = non-restarted Arnoldi / lanczos = symmetric three-term / subspace = block / power = single-vector — selects the basis-extension recurrence; the impl's PRIMARY new axis vs the kernel-api's backend-orchestration axis)
  - problem-symmetry (hermitian = lanczos_step three-term recurrence, EPS_HEP/EPS_GHEP / non-hermitian = full arnoldi krylov-step, EPS_NHEP/EPS_GNHEP — selects krylov-step vs lanczos_step)
  - spectral-transformation (none / shift-invert / shift-invert-precond — inherited from the kernel-api; selects what op.inv inverts)
  - problem-type (linear / quadratic-linearized / nonlinear — inherited)
  - restart-shape (non-restarted / thick-restart-Krylov-Schur — the basis-compression cycle)
---

# eigsolve-impl

> **⟢ kernel-impl (DIRECTIVE-3, role-label `kernel-impl`).** This is the **constructive realization** of the eigensolve kernel in our firm Krylov vocabulary — the from-our-primitives version a reviewer reads ALONGSIDE the opaque kernel-API contract ([`L3/eigsolve`](./eigsolve.md), `kernel-api`). It is **NOT** a claim about Palace source: Palace authors no eigen-iteration loop (the loop is inside SLEPc/ARPACK; see the kernel-api's `sequential-obstruction`). This chapter constructs the loop Palace defers to the library, from `krylov-step` / `lanczos_step` / `ksp_solve` / `orthogonalize`. It does **not** downgrade or replace the kernel-api; the two stand side-by-side, linked by the `realizes-kernel-api` `reference` edge, and the [`lowering-verifier`](../../README.md) audits that they compute the same eigenpairs.

> **⟢ roadmap_goal (rank 0) — claim-free intent.** This chapter carries **no positive Palace-source claim**. It is the *intent* node for the constructive eigsolve impl: a real, refactorable, link-resolving home for the speculative realization, pulled by the eigenmode driver root (see §Pulled-by) and the c122 deflate/krylov-iteration consumers. Its constituent `lanczos_step` is itself a co-cycle `roadmap_goal` (not yet on disk). Promotion `roadmap_goal → stub → rough-in` fires when (a) a blocking `depends-on` consumer wires in (RE3 deflate / RE8 krylov-iteration view), and (b) `lanczos_step` materializes against positive structure (the MINRES/symmetric-Lanczos L0). Everything asserted below about correspondence to the kernel-api is **speculative reconstruction**, flagged as such.

The L3 [`eigsolve`](./eigsolve.md) kernel-api records that the eigen-iteration loop is a witnessed [`sequential-obstruction`](../concepts/sequential-obstruction.md) rooted in **opaque-library-ownership**: *"there is no Palace-authored eigen-step kernel / eigen-iteration driver pair analogous to `(krylov-step, ksp_solve)` — the iteration is entirely library-internal."* This chapter is that missing pair, constructed. The kernel-api opens the per-step **body** (`apply_shift_invert`); this impl wraps it in the **loop** the api leaves opaque, using exactly the firm `(krylov-step, ksp_solve)` machinery the api names as the shape the loop *would* have.

## Intent

What this `roadmap_goal` will become: a `rough-in`→`firm` **L3 kernel-impl operator** `eigsolve_impl` — the constructive iteration-rotation rendering of the eigensolve fold, in our vocabulary, decomposed as:

1. an **outer thick-restart driver** (`iterate_while_L3` over restart cycles, Krylov-Schur basis compression between cycles), realizing the SLEPc `EPSKRYLOVSCHUR` algorithm (`palace/linalg/slepc.cpp:635` `EPSSetType(eps, EPSKRYLOVSCHUR)` — the decisive evidence that the opaque loop IS Krylov-Schur);
2. an **inner basis-extension loop** (`iterate_while_L3` over basis columns to dimension `ncv`), each step one `krylov-step` (non-Hermitian Arnoldi) or one [`lanczos_step`](./lanczos_step.md) (Hermitian three-term recurrence), whose body is exactly the kernel-api's `apply_shift_invert` followed by `orthogonalize` against the basis;
3. a **Rayleigh-Ritz extraction** (project the shift-inverted operator onto the orthonormal basis `BV`, solve the small dense eigenproblem `H y = θ y`, lift Ritz vectors `x = BV·y`, undo the spectral transform `λ = σ + 1/θ` and Higham scaling), realizing ARPACK `neupd` (`palace/linalg/arpack.cpp:369`) / SLEPc post-`EPSSolve` extraction.

## kernel-impl form (the constructive realization)

> **SPECULATIVE.** The value-threaded form below is a *reconstruction* in our L3 vocabulary, not a transcription of Palace source. It composes only firm/roadmap_goal constituents.

Shape contract (positional values; the operator-domain shape group `S` and the square operator form `LinOp[(S: ...), $S]` follow the named-shape-group convention of [`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2; `complex` is the element type; the basis `BV` is `Tensor[(B: ncv), (S: ...), complex]` — a named-shape-group run `B` of basis columns each congruent to the operator domain `S`):

    eigsolve_impl :: (op, control) -> EigResult
    -- op : the kernel-api operator-parameters surface (op.operand, op.inv, op.projector, σ, mode)
    --      — identical to the L3/eigsolve `op` (this impl REALIZES that api).
    -- control : EigControl (requested mode count N, ncv basis dim, tol, max restarts).

    eigsolve_impl op control =
      let st0 = seed_basis op control                          -- BV ← [v0 / ‖v0‖]; v0 from control.initial_space
      let (BV_f, H_f) = iterate_while_L3                        -- OUTER thick-restart driver (Krylov-Schur)
                          (st0)
                          (\st -> not (converged st control) && st.cycle < control.max_restarts)
                          (\st ->
                             let ext = extend_basis op st control   -- INNER basis-extension to dim ncv (below)
                             let (Θ, Y) = rayleigh_ritz op ext      -- project + small dense eigensolve
                             in thick_restart ext Θ Y control)      -- compress: lock converged Ritz pairs, re-seed
      let (Θ, Y) = rayleigh_ritz op (BV_f, H_f)                 -- final Ritz extraction
      in extract_eigpairs op Θ Y                                -- λ = σ + 1/θ + Higham un-scale; normalize; residual; count→status

      where
        -- INNER basis-extension loop: ncv steps, each one krylov-step / lanczos_step
        extend_basis op st control =
          iterate_while_L3 st (\s -> s.j < control.ncv) (\s ->
            -- ONE basis-extension step. The per-step body IS the kernel-api apply_shift_invert,
            -- wrapped with orthogonalization against the current basis BV[0..j].
            let step = if op.hermitian
                       then lanczos_step (op, s.BV, s.j)        -- symmetric three-term recurrence (EPS_HEP/GHEP)
                       else krylov-step  (op, s.BV, s.j)        -- full Arnoldi (EPS_NHEP/GNHEP); op.orthog = MGS/CGS/CGS2
            in append_column s step)                            -- BV[j+1] ← step.v_next; H[*, j] ← step.coeffs

The inner `krylov-step`/`lanczos_step` body, expanded, is **exactly the kernel-api's `apply_shift_invert`** plus the orthogonalize stage:

    -- per basis-extension step (the krylov-step `op.T` instantiated as the shift-invert action):
    --   w  = apply_linop op.operand BV[j]      -- M·v (shift-invert) / K·v (none)   [kernel-api stage 1]
    --   y  = ksp_solve  op.inv     w           -- (K − σM)⁻¹ w                       [kernel-api stage 2]
    --   y' = scale_untransform op  y           -- Higham γ/δ un-scale                [kernel-api stage 3]
    --   (v_next, H[*,j]) = orthogonalize (BV[0..j], y')   -- MGS/CGS/CGS2; the new basis col + recurrence coeffs
    --   [lanczos_step: orthogonalize collapses to the symmetric band-3 form α_j, β_j, β_{j-1}]

So the kernel-api's opaque `eigen_iterate op st0 apply_shift_invert` is realized as
`iterate_while_L3 (extend_basis ▷ rayleigh_ritz ▷ thick_restart)` — the obstruction's "no Palace loop" replaced by our authored loop, with `apply_shift_invert` as the kernel-api names it sitting verbatim inside the basis-extension step.

## Correspondence to the kernel-API (the `realizes-kernel-api` claim)

> **SPECULATIVE reconstruction** — the audit is the [`lowering-verifier`](../../README.md)'s job once both nodes are firm.

| kernel-API ([`L3/eigsolve`](./eigsolve.md)) | kernel-impl (this chapter) |
|---|---|
| `apply_shift_invert op v` (per-step body; **lifts**) | the inner `krylov-step`/`lanczos_step` body — verbatim `apply_linop ▷ ksp_solve ▷ scale_untransform`, then `orthogonalize` |
| `eigen_iterate op st0 apply_shift_invert` (the **opaque** fold; obstruction) | `iterate_while_L3` thick-restart driver ▷ inner basis-extension loop (CONSTRUCTED here) |
| SLEPc `EPSSolve` / `EPSKRYLOVSCHUR` (`slepc.cpp:694`,`:635`) | the outer thick-restart driver realizing Krylov-Schur |
| ARPACK `naupd` RCI basis driver (`arpack.cpp:318`); `iparam[2]` Arnoldi-iters (`:270`) | the inner basis-extension loop to dim `ncv` |
| SLEPc `BV` basis-vectors (`slepc.cpp:731` `EPSGetBV`) | the `BV : Tensor[(B: ncv), (S: ...), complex]` basis carry |
| `extract_eigpairs` (un-transform `l*gamma`; `slepc.cpp:715`) / ARPACK `neupd` (`:369`) | `rayleigh_ritz` + `extract_eigpairs` (`λ = σ + 1/θ`; Higham un-scale; normalize) |

The impl **preserves the obstruction the api records** — it does not dissolve it. The inner basis-extension loop and the outer thick-restart cycle are each a `sequential-obstruction`: the basis trajectory `BV[j] → BV[j+1]` reads the prior column (Arnoldi/Lanczos recurrence), and the thick-restart re-seed is carry-threaded across cycles. What changes is *ownership*: the kernel-api says "the library owns this loop, we cannot render it"; the impl says "here is the loop rendered in our vocabulary, IF we were to author it instead of calling the library." Both are honest: Palace calls the library; we can construct the equivalent.

## Justification kind

`structural` (primary) — the construction is a shape-driven decomposition of the eigensolve into the firm `(krylov-step, ksp_solve)` kernel/driver pair the kernel-api explicitly names as the analog. `reduction-chain` (secondary) — the small-step iteration semantics (basis-extension recurrence, Rayleigh-Ritz, thick-restart) are the load-bearing content. `empirical-match` is **deferred** — confirming the impl computes the same eigenpairs as the api (modulo tolerance + the four non-determinism sources the L1 entry catalogs) is the `lowering-verifier`'s c122 audit, not asserted here.

## Pulled-by (reachability provenance)

This `roadmap_goal` is reachable from a feature root (the proliferation/liveness guard, [`resolution-ladder`](../methodology/resolution-ladder.md)):

- **Primary root chain:** [`feature/eigenmode.L4`](../feature/eigenmode.L4.md) (`feature_root: seed`, the GC-root) `composes` → [`L4/eigsolve`](../L4/eigsolve.md) `lowers-to` → [`L3/eigsolve`](./eigsolve.md) (the kernel-api) ← `realizes-kernel-api` ← **this impl**. NOTE: the `realizes-kernel-api` edge is `reference`-class (free), so it does NOT itself carry liveness — the impl's reachability is provided by the **blocking** consumer edges below.
- **Blocking consumers (the actual liveness edges — to wire as they land):**
  - **RE3 deflate / NLEPS-deflated eigensolve** (c122 consumer) — deflation extends the thick-restart basis with locked converged vectors; the NLEPS-deflated eigensolve IS this fold with a deflation-projection stage. The natural primary blocking `depends-on` consumer. (Coupling NOTED, edge NOT forced this cycle.)
  - **RE8 krylov-iteration view** (c122 consumer) — a feature column composing the iteration-rotation eigensolve BY NAME would `depends-on` this impl.
  Until a blocking consumer wires in, this node's liveness rests on the **grounding disposition** ([[feedback_gc_ground_dont_remove_future_deps]]): it is a genuinely-wanted future dep of the eigenmode root, sketched into a roadmap_goal rather than left stranded. If c122 fails to wire a consumer, the GC sweep flags it — that is the correct accountability, not a defect to pre-empt.

## Speculative L3 operators proposed

- **`lanczos_step`** (rank-0 `roadmap_goal` co-cycle constituent; see the second proposed-changes block) — the symmetric/Hermitian three-term-recurrence basis-extension specialization of `krylov-step` (the kernel-api's `op.orthog` collapsed to the band-3 form). The MINRES/symmetric-Lanczos kernel the `L1/index.md:179` rough-in row names.
- **`eigsolve_impl`** (this chapter; rank-0 `roadmap_goal`) — the constructive eigensolve fold itself.
- **`rayleigh_ritz`** (sub-component, named inline; harvester may promote to its own entry if a second consumer appears) — the project-onto-basis + small-dense-eigensolve + lift-back extraction. Constituent of the impl; not its own dep-map row this cycle (single consumer).
- **`thick_restart`** (sub-component, named inline) — the Krylov-Schur basis-compression / lock-converged / re-seed cycle boundary. Constituent; not its own row this cycle.

## Status

`roadmap_goal` (rank 0) — `kernel-impl` role-label. Claim-free intent node for the constructive Krylov-Schur eigensolve realization. Rests on firm `L3/krylov-step` + `L3/ksp_solve` + `L3/apply_linop` + `L2/orthogonalize` and the co-cycle roadmap_goal `L3/lanczos_step` (rank-0 may rest on rank-0). Linked `realizes-kernel-api` (`reference`-class) to the KEPT kernel-api [`L3/eigsolve`](./eigsolve.md) (partial-obstruction, undowngraded) + [`L4/eigsolve`](../L4/eigsolve.md). Promotion route: `roadmap_goal → stub` when a blocking `depends-on` consumer (RE3 deflate / RE8 krylov-iteration) wires in; `stub → rough-in → firm` as `lanczos_step` materializes against positive structure and the lowering-verifier audits the impl↔api eigenpair correspondence. This is the DIRECTIVE-3 item-2c constructive-kernel frontier opener — the SLEPc-EPS eigsolve kernel now has BOTH surfaces (opaque api + constructive impl), reviewably linked.

## Evidence

The constituents are firm chapters; the Palace anchors are the kernel-api's loop sites (cited to show the impl realizes exactly the opaque loop the api leaves un-rendered — NOT cited as positive source FOR the impl construction, which is our reconstruction). All Palace citations self-verified this dispatch via codemap `read_range` + `citecheck --anchor` against the on-disk file.

- `palace/linalg/slepc.cpp:630-654` — `SlepcEPSSolverBase::SetType`: `EPSSetType(eps, EPSKRYLOVSCHUR)` (`:635`), with `EPSPOWER` (`:638`), `EPSSUBSPACE` (`:641`), `EPSJD` (`:644`); the TOAR/STOAR/QARNOLDI/SLP/NLEIGS arm `MFEM_ABORT` (`:648-653`). The decisive evidence that the default opaque eigen-iteration IS Krylov-Schur — the algorithm this impl reconstructs (the `eigen-algorithm` variant axis source).
- `palace/linalg/slepc.cpp:687-709` — `SlepcEPSSolverBase::Solve`: `Customize()` (`:693`), the entire opaque iteration `EPSSolve(eps)` (`:694`), `EPSGetConverged(eps, &num_conv)` (`:695`), `RescaleEigenvectors(num_conv)` (`:707`). The kernel-api's "no Palace loop" anchor — what the impl's outer driver realizes.
- `palace/linalg/slepc.cpp:731-736` — `SlepcEPSSolverBase::GetBV`: `EPSGetBV(eps, &bv)` (`:734`). The SLEPc Krylov-basis-vectors object — the impl's `BV` carry.
- `palace/linalg/slepc.cpp:602-628` — `SlepcEPSSolverBase::SetProblemType`: `EPS_HEP` (`:607`), `EPS_NHEP` (`:610`), `EPS_GHEP` (`:613`), `EPS_GHIEP` (`:616`), `EPS_GNHEP` (`:619`). The `problem-symmetry` axis source — selects `lanczos_step` (Hermitian) vs `krylov-step` (non-Hermitian).
- `palace/linalg/arpack.cpp:318` — `naupd(fcomm, ido, ...)`: the ARPACK Arnoldi/Lanczos basis-iteration RCI driver — the impl's inner basis-extension loop, library-owned in Palace.
- `palace/linalg/arpack.cpp:270` — `iparam[2] = (a_int)arpack_it; // Maximum number of Arnoldi iterations`: the basis-extension iteration bound; `arpack.cpp:273` — `iparam[6] = sinvert ? 3 : 1; // Problem mode` (mode-3 shift-invert); `arpack.cpp:278` — `which::largest_magnitude` (the dominant-θ selection the Rayleigh-Ritz extraction realizes).
- `palace/linalg/arpack.cpp:369` — `neupd(fcomm, rvec, ...)`: the ARPACK post-iteration eigenpair extraction — the impl's `rayleigh_ritz` + `extract_eigpairs`; `arpack.cpp:342` — `int num_it = (int)iparam[2]` (the iteration-count readout).
- `book/src/L3/eigsolve.md` — the **kernel-API surface** this impl realizes (partial-obstruction; role-labeled `kernel-api` by the D5-paired finalize this cycle). §Signature (the `apply_shift_invert` body the impl folds verbatim), §Semantics phase 2 (the opaque loop the impl constructs), §"Iteration-rotation marker" (the `(krylov-step, ksp_solve)`-analog shape this impl IS).
- `book/src/L3/krylov-step.md` (firm, cycle-010) — the per-step Arnoldi basis-extension body the impl's non-Hermitian inner loop folds. §Signature (the `(op, K, s) -> (K', s', outputs)` value-threaded form), §Semantics (the five primitive groups; the `op.orthog` MGS/CGS/CGS2 auxiliary stage).
- `book/src/L4/krylov-step.md` (firm, cycle-006) — the typed-wrapper companion; the Form-A/B distinction the impl inherits at the basis-extension step.
- `book/src/L3/ksp_solve.md` (firm) — the inner shifted-operator solve `(K − σM)⁻¹` the basis-extension step composes (the kernel-api's `apply_shift_invert` stage 2).
- `book/src/L3/apply_linop.md` (firm) — the whole-tensor operator-apply (kernel-api stage 1; Rayleigh-Ritz back-projection).
- `book/src/L2/orthogonalize.md` (firm) — the basis-orthogonalization stage keeping `BV` orthonormal (the `op.orthog` surface; collapses to the band-3 form for `lanczos_step`).
- `book/src/L1/index.md:179` — the `lanczos_step` rough-in dep-map row (from the MINRES `obstruction (enum-only-stub)` theme); the impl's symmetric-recurrence constituent, promoted here to a co-cycle `roadmap_goal` chapter.
- `book/src/feature/eigenmode.L4.md` (firm) — the GC-root the impl's pulled-by chain terminates at (`composes` → `L4/eigsolve`).
- `book/src/methodology/resolution-ladder.md` — the `roadmap_goal` rank-0 discipline + reachability/pulled-by requirement this node satisfies.
- `book/src/concepts/sequential-obstruction.md` — the classification preserved on the impl's basis-extension + thick-restart loops.
- `book/src/semantics/index.md` §1.2.1–§1.2.2 (named-shape-group convention, the `BV : Tensor[(B: ncv), (S: ...), complex]` form), §3.7 (`iterate_while`), §3.8 (demand-pruning) — USED + linked, not restated.
```

```new:book/src/L3/lanczos_step.md
---
layer: L3
operator: lanczos_step
kind: kernel-impl-constituent
status: roadmap_goal
rank: roadmap_goal
edges:
  depends-on:
    - target: L3/krylov-step
      kind: specializes                 # lanczos_step IS krylov-step with the orthogonalization-variant axis collapsed to the symmetric band-3 (three-term) recurrence; same per-step shape, narrowed auxiliary stage (firm)
    - target: L3/apply_linop
      kind: composes                    # the symmetric operator-apply A·v_curr (firm)
    - target: L1/dot
      kind: composes                    # the diagonal recurrence coefficient α_j = ⟨A v_j, v_j⟩ (firm)
    - target: L1/nrm2
      kind: composes                    # the off-diagonal coefficient β_j = ‖w‖ (firm)
    - target: L1/axpy
      kind: composes                    # the three-term update w = A v_j − α_j v_j − β_{j-1} v_{j-1} (firm)
    - target: L1/scal
      kind: composes                    # the normalize step v_{j+1} = w / β_j = scal (1/β_j) w (firm)
  reference:
    - target: L3/eigsolve-impl
      kind: pulled-by                   # the sole consumer this cycle: the Hermitian basis-extension step of the constructive eigensolve fold
    - target: L1-L0/minres-iteration
      kind: cites-evidence              # the L1 rough-in row's home (MINRES obstruction theme, enum-only-stub); the symmetric-Lanczos kernel referenced there
    - target: semantics/index
variant_axes:
  - reorthogonalization (none = pure three-term recurrence / full = re-orthogonalize against all prior basis cols to combat loss-of-orthogonality / selective = Paige's criterion — informational; the band-3 recurrence is the unstable-but-cheap default)
  - matrix-pencil (standard = A only / generalized = (A, B)-inner-product Lanczos for EPS_GHEP — selects the inner product the orthogonality is measured in)
---

# lanczos_step

> **⟢ kernel-impl-constituent (DIRECTIVE-3).** The symmetric/Hermitian specialization of the per-step Krylov basis-extension body, constructed for the Hermitian arm of [`eigsolve-impl`](./eigsolve-impl.md) (`EPS_HEP` / `EPS_GHEP` pencils). Not a Palace-authored callable — the symmetric Lanczos recurrence is inside SLEPc/ARPACK; this is the from-our-primitives realization.

> **⟢ roadmap_goal (rank 0) — claim-free intent.** This chapter carries no positive Palace-source claim. It is the intent node for the symmetric three-term-recurrence basis-extension step the `L1/index.md:179` rough-in row names (from the MINRES `obstruction (enum-only-stub)` theme). Pulled by [`eigsolve-impl`](./eigsolve-impl.md) (the Hermitian basis-extension consumer). Promotes `roadmap_goal → stub → rough-in → firm` as it materializes against the symmetric-Lanczos L0 (MINRES) and a blocking consumer firms. Speculative reconstruction; not asserted as Palace source.

## Intent

What this becomes: a `firm` L3 operator `lanczos_step` — `krylov-step` with the `op.orthog` orthogonalization-variant axis **collapsed to the symmetric band-3 (three-term) recurrence**. Where Arnoldi (`krylov-step`'s non-Hermitian form) orthogonalizes the new basis column against ALL prior columns (full upper-Hessenberg `H`), the Hermitian case needs only the previous TWO columns — the projection onto the rest is zero by symmetry. This produces a **tridiagonal** `H` (the symmetric Lanczos `T` matrix), the structural saving the Hermitian eigensolve exploits.

## kernel-impl form (the constructive realization)

> **SPECULATIVE** — a reconstruction in our L3 vocabulary, composing only firm constituents.

Shape contract (the operator-domain shape group `S` per [`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2; `v_prev`, `v_curr`, `v_next` each `Tensor[(S: ...), complex]`; the recurrence coefficients `α_j, β_j` scalar):

    lanczos_step :: (A, v_prev, v_curr, β_prev) -> (v_next, α_j, β_j)
    -- A : the (shift-inverted) symmetric/Hermitian operator op.operand ▷ op.inv action (from eigsolve-impl's op)
    -- v_prev, v_curr : the previous two orthonormal basis columns BV[j-1], BV[j]
    -- β_prev : the prior off-diagonal coefficient (β_{j-1}); β_{-1} = 0 at the first step (first-iteration-unrolled)

    lanczos_step A v_prev v_curr β_prev =
      let w0  = apply_linop A v_curr                  -- symmetric operator-apply A·v_j
      let α_j = real (dot w0 v_curr)                  -- diagonal coeff α_j = ⟨A v_j, v_j⟩ (real for Hermitian A)
      let w1  = axpy (negate α_j) v_curr w0           -- w ← A v_j − α_j v_j
      let w   = axpy (negate β_prev) v_prev w1        -- w ← w − β_{j-1} v_{j-1}   (the THIRD term — band-3)
      let β_j = nrm2 w                                -- off-diagonal coeff β_j = ‖w‖
      let v_next = scal (1 / β_j) w                   -- normalize: v_{j+1} = w / β_j   (β_j = 0 ⇒ invariant subspace / breakdown)
      in (v_next, α_j, β_j)

This is **exactly [`krylov-step`](./krylov-step.md) with `op.orthog` = the band-3 form**: the kernel-api / `eigsolve-impl` per-step body `apply_shift_invert` produces `w0` (here `A` is the already-shift-inverted action `op.operand ▷ op.inv ▷ scale_untransform`), and the orthogonalize stage — which for full Arnoldi is MGS/CGS/CGS2 against all of `BV[0..j]` — collapses to the two `axpy` subtractions against `v_curr` and `v_prev` only. The `(α_j, β_j)` are the tridiagonal `T`-matrix entries `eigsolve-impl`'s Rayleigh-Ritz solves.

## Relationship to `krylov-step`

`lanczos_step` `specializes` [`krylov-step`](./krylov-step.md): same `(op, K, s) -> (K', ...)` per-step iteration-rotation shape, with two narrowings — (1) the orthogonalization-variant axis (`{MGS, CGS, CGS2}`) collapses to the symmetric band-3 recurrence (orthogonality against only the prior two columns, exact in infinite precision by Hermitian symmetry); (2) the recurrence coefficients `(α_j, β_j)` are the tridiagonal entries vs Arnoldi's full Hessenberg column. The L2 [`krylov-step`](../L2/krylov-step.md) note (`book/src/L2/krylov-step.md:187`) already records this: *"MINRES is the symmetric specialisation of `arnoldiStep`; its `lanczos_step` would specialise `krylov-step`'s orthogonalization-variant axis to a band-3 form."* This chapter is that specialization, constructed.

## Justification kind

`structural` — a shape-driven narrowing of the firm `krylov-step` per-step body. `reduction-chain` (secondary) — the three-term recurrence small-step is the content.

## Status

`roadmap_goal` (rank 0) — `kernel-impl-constituent` role. Claim-free intent node for the symmetric Lanczos basis-extension step. Rests on firm `L3/krylov-step` (specializes) + `L3/apply_linop` + `L1/dot` + `L1/nrm2` + `L1/axpy`. Pulled by [`eigsolve-impl`](./eigsolve-impl.md). Promotion: materialize against the symmetric-Lanczos L0 (the MINRES obstruction theme's literature-anchored form, `L1-L0/minres-iteration.md`) + a blocking consumer firms. The known-loss-of-orthogonality of the pure band-3 recurrence (the `reorthogonalization` variant axis) is the numerical caveat to resolve at firming.

## Evidence

> All Palace citations are to the symmetric-eigensolve sites the recurrence realizes (the library-owned Lanczos is inside SLEPc/ARPACK); NOT positive source for the reconstruction.

- `book/src/L3/krylov-step.md` (firm, cycle-010) — the operator this specializes; §Variant-axes axis 2 (orthogonalization-variant, the axis that collapses to band-3), §Semantics (the `op.orthog` auxiliary stage).
- `book/src/L2/krylov-step.md:187` — the standing note that `lanczos_step` specializes `krylov-step`'s orthogonalization axis to band-3 (the MINRES symmetric-specialization).
- `book/src/L1/index.md:179` — the `lanczos_step` rough-in dep-map row `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` (the signature this chapter realizes) + its constituent list `apply_linop, dot, axpy, nrm2`.
- `book/src/L1-L0/minres-iteration.md` — the MINRES `obstruction (enum-only-stub)` theme; the symmetric-Lanczos kernel home (the literature-anchored form the firming would draw on).
- `palace/linalg/slepc.cpp:607,613` — `EPS_HEP` / `EPS_GHEP`: the Hermitian / generalized-Hermitian problem types that select the symmetric Lanczos recurrence (the `matrix-pencil` variant axis).
- `book/src/L1/dot.md`, `book/src/L1/nrm2.md`, `book/src/L1/axpy.md`, `book/src/L1/scal.md` — the firm BLAS-1 constituents of the three-term update (`scal` is the normalize step `v_{j+1} = scal (1/β_j) w`).
- `book/src/semantics/index.md` §1.2.1–§1.2.2 — the named-shape-group convention; USED + linked.
```

```edit:book/src/L3/index.md
[append to the L3 dep-map / operator list, in alpha position among the L3 operator rows:

| `eigsolve-impl` *(roadmap_goal; kernel-impl)* | `(op, control) → EigResult` | `krylov-step`, `lanczos_step`, `ksp_solve`, `apply_linop`, `L2/orthogonalize` | `roadmap_goal (kernel-impl, proposed-by: abstractor:2026-06-07T054924Z-abstractor-eigsolve-kernel-impl)` |
| `lanczos_step` *(roadmap_goal; kernel-impl-constituent)* | `(A, v_prev, v_curr, β_prev) → (v_next, α_j, β_j)` | `krylov-step` (specializes), `apply_linop`, `dot`, `nrm2`, `axpy`, `scal` | `roadmap_goal (kernel-impl-constituent, proposed-by: abstractor:2026-06-07T054924Z-abstractor-eigsolve-kernel-impl)` |

Note for the integrator: insert each row in its alpha position within the L3 operator-list table. Alpha order in the "Solver capabilities & field transitions" group is `eigsolve < fold_solve < krylov-step < ksp_solve < orthogonalize` (verified against on-disk SUMMARY.md lines 121-125). So `eigsolve-impl` inserts after `eigsolve` (before `fold_solve`), and `lanczos_step` inserts after `ksp_solve` (before `orthogonalize`) — `la` sorts after `ks`/`kr` and before `or`. Both rows are plain-text-named where the anchor is new this cycle, but the anchor FILES are created this cycle (the two `new:` blocks above), so the integrator MAY link them once landed.]
```

```edit:book/src/L3/eigsolve.md
[role-label the kernel-API surface — append the kernel-api role marker to the §Status line WITHOUT changing the partial-obstruction status. Locate the §Status line opening "`partial-obstruction` — the per-step body" and prepend the role-label sentence:]

## Status

`partial-obstruction` — **`kernel-api`** (DIRECTIVE-3 role-label: this node is the kernel-API contract — the opaque-library boundary the spine calls; its constructive realization is the `kernel-impl` [`eigsolve-impl`](./eigsolve-impl.md), linked by a `realizes-kernel-api` `reference`-class edge. The `partial-obstruction` status is UNCHANGED — the loop is genuinely opaque-library-owned; the impl constructs what the loop *would* be, it does not make this node's loop non-opaque). The per-step body (`apply_shift_invert = apply_linop ▷ ksp_solve ▷ scale_untransform [▷ project]`) lifts cleanly to a global tensor-field expression (every line is whole-tensor by signature shape; the body-composition laws 1, 2, 4, 5 are syntactic identities read from the positive Palace `ApplyOp` / `__pc_apply_EPS` bodies, identity-in-form to the firm L2 [`eigsolve`](../L2/eigsolve.md)); the **eigen-iteration loop is a witnessed [`sequential-obstruction`](../concepts/sequential-obstruction.md) rooted in opaque-library-ownership** — SLEPc folds inside `EPSSolve(eps)` (`palace/linalg/slepc.cpp:694`), ARPACK folds inside the `naupd` RCI driver (`palace/linalg/arpack.cpp:318`, callback-dispatched by `:315-339`), with **no Palace-authored eigen-step kernel / eigen-iteration driver pair** analogous to `(krylov-step, ksp_solve)`.

[Integrator note: also append a `reference` edge to the eigsolve.md frontmatter (it currently has none of the typed-edge block — the chapter predates the edge-typing campaign; add a minimal `edges: reference:` block) OR, if adding frontmatter edges is out of the per-report safety scope, record the inbound `realizes-kernel-api` correspondence in the §"L3 vs L4 distinction"/§Status prose only. The authoritative direction of the realizes-kernel-api edge is impl→api (declared in eigsolve-impl.md frontmatter); the api node needs no outbound edge for the linter. Minimal-blast-radius: prose role-label only is sufficient.]
```

```edit:book/src/SUMMARY.md
[add two chapter entries under the `# L3` Part "Solver capabilities & field transitions" group, in alpha position among the L3 operator chapters (on-disk SUMMARY.md lines 121-125: eigsolve / fold_solve / krylov-step / ksp_solve / orthogonalize). Insert:
  - `eigsolve-impl` immediately after the existing `- [eigsolve](./L3/eigsolve.md)` line (line 121), before `- [fold_solve]`
  - `lanczos_step` immediately after the existing `- [ksp_solve](./L3/ksp_solve.md)` line (line 124), before `- [orthogonalize]` — `la` sorts after `ks`, before `or`]

  - [eigsolve-impl](./L3/eigsolve-impl.md)
  - [lanczos_step](./L3/lanczos_step.md)
```

## Speculative operators proposed

- **`eigsolve-impl`** :: `(op, control) -> EigResult` — the constructive Krylov-Schur eigensolve fold (outer thick-restart driver ▷ inner basis-extension loop ▷ Rayleigh-Ritz extraction), realizing the opaque SLEPc-EPS / ARPACK-naupd loop in our `(krylov-step, ksp_solve)` vocabulary. Rank-0 `roadmap_goal`, role `kernel-impl`. Motivation: DIRECTIVE-3 item-2c — the eigsolve kernel is a spine-dependency opaque-library obstruction with a well-understood Krylov-Schur implementation; the impl is the from-our-primitives surface a reviewer reads alongside the opaque contract.
- **`lanczos_step`** :: `(A, v_prev, v_curr, β_prev) -> (v_next, α_j, β_j)` — the symmetric/Hermitian three-term-recurrence basis-extension step (`krylov-step` with `op.orthog` collapsed to band-3). Rank-0 `roadmap_goal`, role `kernel-impl-constituent`. Motivation: the Hermitian arm of `eigsolve-impl` (`EPS_HEP`/`EPS_GHEP`); the kernel the `book/src/L1/index.md:179` rough-in row and the L2 note (`book/src/L2/krylov-step.md:187`) already name.
- **`rayleigh_ritz`** / **`thick_restart`** — sub-components named inline in `eigsolve-impl`; not their own dep-map rows this cycle (single consumer each). Harvester may promote if a second consumer appears.

## Supporting evidence

Palace anchors (kernel-api loop sites the impl realizes; self-verified via `citecheck --anchor` against on-disk this dispatch):
- `palace/linalg/slepc.cpp:635` `EPSSetType(eps, EPSKRYLOVSCHUR)` — decisive: the opaque loop IS Krylov-Schur (the algorithm reconstructed). `:694` `EPSSolve` (the opaque iteration); `:731` `EPSGetBV` (the `BV` basis); `:607/:613` `EPS_HEP/EPS_GHEP` (Hermitian → Lanczos).
- `palace/linalg/arpack.cpp:318` `naupd` (the Arnoldi/Lanczos basis RCI driver); `:270` `iparam[2]` Arnoldi-iteration bound; `:369` `neupd` (post-iteration extraction = Rayleigh-Ritz).
- Firm constituents: `book/src/L3/krylov-step.md`, `book/src/L3/ksp_solve.md`, `book/src/L3/apply_linop.md`, `book/src/L2/orthogonalize.md`, `book/src/L1/{dot,nrm2,axpy}.md`.
- Root chain: `book/src/feature/eigenmode.L4.md` (`feature_root: seed`) `composes` → `L4/eigsolve` → `L3/eigsolve` (kernel-api) ← `realizes` ← impl.

## Open questions / caveats

- **RE3 deflate/NLEPS is the natural blocking consumer (c122).** Deflation = thick-restart basis + locked-converged-vector extension; the NLEPS-deflated eigensolve IS `eigsolve-impl` + a deflation-projection stage. I did NOT wire the deflate `depends-on` edge this cycle (per the planner caveat: coupling noted, not forced — it is a c122 consumer dispatch). The impl's liveness this cycle rests on the grounding disposition ([[feedback_gc_ground_dont_remove_future_deps]]); if c122 does not wire a blocking consumer, the GC sweep correctly flags it. **Flag for the c122 planner:** the deflate/RE3 and krylov-iteration-view/RE8 consumers should `depends-on` `L3/eigsolve-impl` (and `L3/lanczos_step` via it), firing both roadmap_goals' `roadmap_goal → stub` promotion.
- **`lanczos_step` materialization route.** Landed as a rank-0 `roadmap_goal` co-constituent (clean-gate choice B per the planner caveat — author it as a same-cycle constituent at rank-0, NOT firm). Its firming draws on the MINRES obstruction theme's literature-anchored symmetric-Lanczos form (`L1-L0/minres-iteration.md`) — but MINRES itself is an `obstruction (enum-only-stub)` (Palace routes it to `MFEM_ABORT`), so `lanczos_step` has no positive Palace-source body to firm against directly. Its firming is therefore a **literature-anchor + impl-correspondence** route, not a positive-source route. This is the honest caveat: the Lanczos recurrence is inside SLEPc/ARPACK; our `lanczos_step` is a reconstruction whose authority is the operator-algebra (specializes firm `krylov-step`) + literature, not a Palace read.
- **kernel-api frontmatter edge.** `book/src/L3/eigsolve.md` predates the typed-edge campaign and has NO `edges:` frontmatter block. I proposed the role-label as PROSE-ONLY (minimal blast radius — the `realizes-kernel-api` edge is authoritatively declared impl→api in `eigsolve-impl.md`, and the linter needs no outbound edge on the api node). If the integrator/lowering-verifier wants a symmetric `reference` back-edge on the api node, that is a follow-on; flagged, not done here.
- **lowering-verifier audit (c122 candidate).** The impl↔api eigenpair-correspondence (does `eigsolve-impl` compute the same converged `(λᵢ, xᵢ)` as the opaque `EPSSolve`, modulo tolerance + the four L1 non-determinism sources?) is the `lowering-verifier`'s job once both nodes firm — the `empirical-match` justification is deferred to it, not asserted here. Flag for the c122 planner per the plan's §Open-questions kernel-api/impl-integrity note.
- **Rayleigh-Ritz / thick-restart sub-components.** Named inline rather than as their own dep-map rows (single-consumer bar). If a second eigensolve-flavor consumer appears (e.g. a JD/Davidson impl, or the subspace-iteration `EPSSUBSPACE` variant at `slepc.cpp:641`), `rayleigh_ritz` should promote to its own L3 entry (it is the shared extraction substrate across all projection-based eigensolvers). Flag for combinator-miner.
- **Shared-substrate coupling with D4 (libceed-impl) / D3 (relaxation-impl) / D6 (combinator-miner probe).** D6 mines the shared tensor-contraction / iteration substrate across D3/D4/D5. My impl's shared core with the wide wave is the **`iterate_while_L3` value-threaded basis/sweep loop** (shared with the relaxation smoother's GS sweep and the multigrid V-cycle) + the **orthogonalize/contraction inner kernels**. I did not author a shared combinator (combinator-miner's job); flagged the `iterate_while_L3`-over-basis-extension shape as a D6 substrate candidate.
