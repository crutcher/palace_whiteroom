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

> **⟢ kernel-impl (DIRECTIVE-3, role-label `kernel-impl`).** This is the **constructive realization** of the eigensolve kernel in our firm Krylov vocabulary — the from-our-primitives version a reviewer reads ALONGSIDE the opaque kernel-API contract ([`L3/eigsolve`](./eigsolve.md), `kernel-api`). It is **NOT** a claim about Palace source: Palace authors no eigen-iteration loop (the loop is inside SLEPc/ARPACK; see the kernel-api's `sequential-obstruction`). This chapter constructs the loop Palace defers to the library, from `krylov-step` / `lanczos_step` / `ksp_solve` / `orthogonalize`. It does **not** downgrade or replace the kernel-api; the two stand side-by-side, linked by the `realizes-kernel-api` `reference` edge, and the `lowering-verifier` audits that they compute the same eigenpairs.

> **⟢ roadmap_goal (rank 0) — claim-free intent.** This chapter carries **no positive Palace-source claim**. It is the *intent* node for the constructive eigsolve impl: a real, refactorable, link-resolving home for the speculative realization, pulled by the eigenmode driver root (see §Pulled-by) and the deflate/krylov-iteration consumers. Its constituent `lanczos_step` is itself a `roadmap_goal` (not yet on disk). Promotion `roadmap_goal → stub → rough-in` fires when (a) a blocking `depends-on` consumer wires in (RE3 deflate / RE8 krylov-iteration view), and (b) `lanczos_step` materializes against positive structure (the MINRES/symmetric-Lanczos L0). Everything asserted below about correspondence to the kernel-api is **speculative reconstruction**, flagged as such.

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

> **SPECULATIVE reconstruction** — the audit is the `lowering-verifier`'s job once both nodes are firm.

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

`structural` (primary) — the construction is a shape-driven decomposition of the eigensolve into the firm `(krylov-step, ksp_solve)` kernel/driver pair the kernel-api explicitly names as the analog. `reduction-chain` (secondary) — the small-step iteration semantics (basis-extension recurrence, Rayleigh-Ritz, thick-restart) are the load-bearing content. `empirical-match` is **deferred** — confirming the impl computes the same eigenpairs as the api (modulo tolerance + the four non-determinism sources the L1 entry catalogs) is the `lowering-verifier`'s audit, not asserted here.

## Pulled-by (reachability provenance)

This `roadmap_goal` is reachable from a feature root (the proliferation/liveness guard, [`resolution-ladder`](../methodology/resolution-ladder.md)):

- **Primary root chain:** [`feature/eigenmode.L4`](../feature/eigenmode.L4.md) (`feature_root: seed`, the GC-root) `composes` → [`L4/eigsolve`](../L4/eigsolve.md) `lowers-to` → [`L3/eigsolve`](./eigsolve.md) (the kernel-api) ← `realizes-kernel-api` ← **this impl**. NOTE: the `realizes-kernel-api` edge is `reference`-class (free), so it does NOT itself carry liveness — the impl's reachability is provided by the **blocking** consumer edges below.
- **Blocking consumers (the actual liveness edges — to wire as they land):**
  - **RE3 deflate / NLEPS-deflated eigensolve** consumer — deflation extends the thick-restart basis with locked converged vectors; the NLEPS-deflated eigensolve IS this fold with a deflation-projection stage. The natural primary blocking `depends-on` consumer.
  - **RE8 krylov-iteration view** consumer — a feature column composing the iteration-rotation eigensolve BY NAME would `depends-on` this impl.
  Until a blocking consumer wires in, this node's liveness rests on the **grounding disposition** ([[feedback_gc_ground_dont_remove_future_deps]]): it is a genuinely-wanted future dep of the eigenmode root, sketched into a roadmap_goal rather than left stranded.

## Speculative L3 operators proposed

- **`lanczos_step`** (rank-0 `roadmap_goal` co-cycle constituent; see the second proposed-changes block) — the symmetric/Hermitian three-term-recurrence basis-extension specialization of `krylov-step` (the kernel-api's `op.orthog` collapsed to the band-3 form). The MINRES/symmetric-Lanczos kernel the `L1/index.md:179` rough-in row names.
- **`eigsolve_impl`** (this chapter; rank-0 `roadmap_goal`) — the constructive eigensolve fold itself.
- **`rayleigh_ritz`** (sub-component, named inline; harvester may promote to its own entry if a second consumer appears) — the project-onto-basis + small-dense-eigensolve + lift-back extraction. Constituent of the impl; not its own dep-map row this cycle (single consumer).
- **`thick_restart`** (sub-component, named inline) — the Krylov-Schur basis-compression / lock-converged / re-seed cycle boundary. Constituent; not its own row this cycle.

## Status

`roadmap_goal` (rank 0) — `kernel-impl` role-label. Claim-free intent node for the constructive Krylov-Schur eigensolve realization. Rests on firm `L3/krylov-step` + `L3/ksp_solve` + `L3/apply_linop` + `L2/orthogonalize` and the roadmap_goal `L3/lanczos_step` (rank-0 may rest on rank-0). Linked `realizes-kernel-api` (`reference`-class) to the kernel-api [`L3/eigsolve`](./eigsolve.md) (partial-obstruction) + [`L4/eigsolve`](../L4/eigsolve.md). Promotion route: `roadmap_goal → stub` when a blocking `depends-on` consumer (RE3 deflate / RE8 krylov-iteration) wires in; `stub → rough-in → firm` as `lanczos_step` materializes against positive structure and the lowering-verifier audits the impl↔api eigenpair correspondence. Under DIRECTIVE-3, the SLEPc-EPS eigsolve kernel has BOTH surfaces (opaque api + constructive impl), reviewably linked.

## Evidence

The constituents are firm chapters; the Palace anchors are the kernel-api's loop sites (cited to show the impl realizes exactly the opaque loop the api leaves un-rendered — NOT cited as positive source FOR the impl construction, which is our reconstruction).

- `palace/linalg/slepc.cpp:630-654` — `SlepcEPSSolverBase::SetType`: `EPSSetType(eps, EPSKRYLOVSCHUR)` (`:635`), with `EPSPOWER` (`:638`), `EPSSUBSPACE` (`:641`), `EPSJD` (`:644`); the TOAR/STOAR/QARNOLDI/SLP/NLEIGS arm `MFEM_ABORT` (`:648-653`). The decisive evidence that the default opaque eigen-iteration IS Krylov-Schur — the algorithm this impl reconstructs (the `eigen-algorithm` variant axis source).
- `palace/linalg/slepc.cpp:687-709` — `SlepcEPSSolverBase::Solve`: `Customize()` (`:693`), the entire opaque iteration `EPSSolve(eps)` (`:694`), `EPSGetConverged(eps, &num_conv)` (`:695`), `RescaleEigenvectors(num_conv)` (`:707`). The kernel-api's "no Palace loop" anchor — what the impl's outer driver realizes.
- `palace/linalg/slepc.cpp:731-736` — `SlepcEPSSolverBase::GetBV`: `EPSGetBV(eps, &bv)` (`:734`). The SLEPc Krylov-basis-vectors object — the impl's `BV` carry.
- `palace/linalg/slepc.cpp:602-628` — `SlepcEPSSolverBase::SetProblemType`: `EPS_HEP` (`:607`), `EPS_NHEP` (`:610`), `EPS_GHEP` (`:613`), `EPS_GHIEP` (`:616`), `EPS_GNHEP` (`:619`). The `problem-symmetry` axis source — selects `lanczos_step` (Hermitian) vs `krylov-step` (non-Hermitian).
- `palace/linalg/arpack.cpp:318` — `naupd(fcomm, ido, ...)`: the ARPACK Arnoldi/Lanczos basis-iteration RCI driver — the impl's inner basis-extension loop, library-owned in Palace.
- `palace/linalg/arpack.cpp:315-339` — the ARPACK RCI loop: `while(true)` (`:315`), `naupd` (`:318`), `ApplyOp` dispatch on `ido==1||-1` (`:323-326`), `ApplyOpB` on `ido==2` (`:327-330`), break on `ido==99` (`:331-334`). The library-owned inner basis-extension loop the impl reconstructs.
- `palace/linalg/arpack.cpp:270` — `iparam[2] = (a_int)arpack_it; // Maximum number of Arnoldi iterations`: the basis-extension iteration bound; `arpack.cpp:273` — `iparam[6] = sinvert ? 3 : 1; // Problem mode` (mode-3 shift-invert); `arpack.cpp:278` — `which::largest_magnitude` (the dominant-θ selection the Rayleigh-Ritz extraction realizes).
- `palace/linalg/arpack.cpp:369` — `neupd(fcomm, rvec, ...)`: the ARPACK post-iteration eigenpair extraction — the impl's `rayleigh_ritz` + `extract_eigpairs`; `arpack.cpp:342` — `int num_it = (int)iparam[2]` (the iteration-count readout).
- `book/src/L3/eigsolve.md` — the **kernel-API surface** this impl realizes (partial-obstruction; role-labeled `kernel-api` by the D5-paired finalize this cycle). §Signature (the `apply_shift_invert` body the impl folds verbatim), §Semantics phase 2 (the opaque loop the impl constructs), §"Iteration-rotation marker" (the `(krylov-step, ksp_solve)`-analog shape this impl IS).
- `book/src/L3/krylov-step.md` (firm) — the per-step Arnoldi basis-extension body the impl's non-Hermitian inner loop folds. §Signature (the `(op, K, s) -> (K', s', outputs)` value-threaded form), §Semantics (the five primitive groups; the `op.orthog` MGS/CGS/CGS2 auxiliary stage).
- `book/src/L4/krylov-step.md` (firm) — the typed-wrapper companion; the Form-A/B distinction the impl inherits at the basis-extension step.
- `book/src/L3/ksp_solve.md` (firm) — the inner shifted-operator solve `(K − σM)⁻¹` the basis-extension step composes (the kernel-api's `apply_shift_invert` stage 2).
- `book/src/L3/apply_linop.md` (firm) — the whole-tensor operator-apply (kernel-api stage 1; Rayleigh-Ritz back-projection).
- `book/src/L2/orthogonalize.md` (firm) — the basis-orthogonalization stage keeping `BV` orthonormal (the `op.orthog` surface; collapses to the band-3 form for `lanczos_step`).
- `book/src/L1/index.md:179` — the `lanczos_step` rough-in dep-map row (from the MINRES `obstruction (enum-only-stub)` theme); the impl's symmetric-recurrence constituent, promoted here to a co-cycle `roadmap_goal` chapter.
- `book/src/feature/eigenmode.L4.md` (firm) — the GC-root the impl's pulled-by chain terminates at (`composes` → `L4/eigsolve`).
- `book/src/methodology/resolution-ladder.md` — the `roadmap_goal` rank-0 discipline + reachability/pulled-by requirement this node satisfies.
- `book/src/concepts/sequential-obstruction.md` — the classification preserved on the impl's basis-extension + thick-restart loops.
- `book/src/semantics/index.md` §1.2.1–§1.2.2 (named-shape-group convention, the `BV : Tensor[(B: ncv), (S: ...), complex]` form), §3.7 (`iterate_while`), §3.8 (demand-pruning) — USED + linked, not restated.
