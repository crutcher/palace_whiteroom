---
agent: abstractor
invoked_at: 2026-06-01T162018Z
scope: L2>L1 theme sketch — ksp-solve-outer-driver-unfold (the opacity-uncollapse rotation)
status: integrated
integrated_at: 2026-06-01T171229Z
integration_commit: bcd3bed
integration_notes: "Applied clean (D3; cycle-047). NEW firm L2>L1 theme book/src/L2-L1/ksp-solve-outer-driver-unfold.md (the rank-1 DRIVER-tier composition->opacity edge) + SOLE L2-L1/index count-owner (tally 19->21 firm + 1 partly-constructive) + own row + NEW §Vocabulary-cohort driver-tier sub-group + SUMMARY line. Closes ksp-solve-l2-l1-theme-gap; jointly with D4 closes residual-l2-l1-gap-audit + residual-l2-l1-gap-audit-planner-undercount (recommendations; meta-phase authority). Build clean, linkcheck2 green."
inputs:
  - book/src/L2/ksp_solve.md (firm; LHS — the outer-driver composition; §"Lowers from" :155-157 in-line narration the dedicated theme firms)
  - book/src/L1/ksp_solve.md (firm; RHS — the opaque solver-as-operator collapse)
  - book/src/L3-L2/ksp-solve-outer-driver.md (firm c021; UPWARD edge mirrored for asymmetry-closing structure)
  - book/src/L2-L1/index.md (themes-table + cohort + Working-Notes tally; SOLE count-owner this cycle)
  - reference/palace/palace/linalg/iterative.cpp (CG/GMRES Mult bodies; all L0 anchors self-verified via citecheck this dispatch)
  - reference/palace/palace/linalg/ksp.cpp (BaseKspSolver::Mult driver wrapper; factory)
  - reference/palace/palace/linalg/iterative.hpp (IterativeSolver base; result fields)
  - scaffolding/open-questions.md (closes ksp-solve-l2-l1-theme-gap; jointly w/ D4 closes residual-l2-l1-gap-audit)
---

# CYCLE: L2>L1 theme sketch — ksp-solve-outer-driver-unfold

## Summary

The firm L2 `ksp_solve` chapter (`book/src/L2/ksp_solve.md`) already narrates its L2>L1 rotation in-line in §"Lowers from" (`:155-157`) — the rotation is **non-identity**: the L1 opaque `Solver[A]` solver-as-operator collapse is **opened** at L2 into the explicit `krylov-step`-kernel / convergence-test-fold composition, and the L1-absorbed `krylov-method` axis re-surfaces as the L2 solver-method loop-shaping axis — but it **defers the dedicated firming-evidence theme to a file that did not exist**. This is the cycle-046 census RANK-1 L2>L1 gap (driver tier, widest downstream reuse: `eigsolve` / `divfree-projector` / `incremental-least-squares` all consume `ksp_solve`). The asymmetry is structural: the UPWARD L3>L2 edge IS themed (`book/src/L3-L2/ksp-solve-outer-driver.md`, firm c021), the DOWNWARD L2>L1 edge was not. This theme authors `book/src/L2-L1/ksp-solve-outer-driver-unfold.md` (slug deliberately parallels the upward `ksp-solve-outer-driver` to make the asymmetry-closing explicit), narrated forward L2→L1 per high→low discipline: the L2 kernel-fold composition **re-collapses** into the L1 opaque single operator application — the inverse of the L2 §"Lowers from" open. The rotation is `firm` (both endpoints firm; the un-collapse content is structurally grounded and L0-cited; the `SolveResult` boundary type is unchanged across the edge so the rotation is on the body, not the boundary). No speculative L1 operators are introduced (both endpoints are firm `ksp_solve` entries; the `krylov-step` kernel the L2 form folds is firm at both layers). As SOLE `L2-L1/index.md` count-owner this cycle I also write the consolidated firm-count tally bump accounting for both D3 (this theme) and D4 (`krylov-step-kernel-defusion`): **19 firm + 1 partly-constructive → 21 firm + 1 partly-constructive** (verified on-disk current tally = 19 firm + 1 partly-constructive).

## Proposed changes

```new:book/src/L2-L1/ksp-solve-outer-driver-unfold.md
# ksp-solve-outer-driver-unfold

The L2>L1 lowering theme for the `ksp_solve` **outer-driver composition**. The rewrite is **substantive (non-identity)**: the L2 explicit kernel-fold composition `iterate_while (krylov-step op) s_init predicate` — the [`krylov-step`](../L2/krylov-step.md) kernel made visible and folded under a convergence predicate — **re-collapses** into the L1 **opaque solver-as-operator** application `ksp_solve :: (K: Solver[A], b) -> SolveResult`, where the kernel, the fold, and the solver-method nesting all vanish back into the black-box `Solver[A]`. This is the **forward (high→low) narration of the inverse** of the L2 chapter's §"Lowers from" *open*: where the L2 entry *opens* the L1 opacity into the kernel-fold composition, this theme narrates how that composition *re-collapses* into the L1 opacity. It is the **downward complement** of the upward [`L3-L2/ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md) theme — that theme firms the L3↔L2 edge (explicit `iterate_while_L3` tail recursion ⟷ outer-driver-by-role wrap); this theme firms the L2↔L1 edge (kernel-fold composition ⟷ opaque operator), closing the per-edge asymmetry around the firm L2 `ksp_solve` driver.

## Slug

`ksp-solve-outer-driver-unfold`

The slug deliberately parallels the upward [`L3-L2/ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md) (firm cycle-021), with the `-unfold` suffix marking the downward direction: the L2 *unfolded* (opened) composition re-collapses into the L1 opaque operator. The asymmetry the slug-pair closes: the L3>L2 edge above `L2/ksp_solve` was themed (c021), the L2>L1 edge below it was not until this theme. Both edges of the firm L2 driver are now dedicated themes.

## Context

The `ksp_solve` lowering chain stretches across the layer-edges of the artifact:

- **L1 firm** ([`L1/ksp_solve`](../L1/ksp_solve.md)) — the **opaque solver-as-operator** collapse `(K: Solver[A], b) -> SolveResult`; the loop AND the kernel are both invisible (a solve is one indivisible operator application; `K` a black box that maps `b ↦ A⁻¹·b`). The RHS of this theme.
- **L2>L1 — this theme.** Narrates how the L2 kernel-fold composition lowers (re-collapses) into the L1 opaque operator. Substantive (non-identity): the kernel and the fold are erased back into the opaque `Solver[A]`; the L2 solver-method loop-shaping axis re-absorbs into the L1 `krylov-method` opacity-axis.
- **L2 firm** ([`L2/ksp_solve`](../L2/ksp_solve.md), firm cycle-021 wave-1) — the **outer-driver composition**: `(K, b) -> SolveResult` with body = the convergence-test fold of [`krylov-step`](../L2/krylov-step.md), the kernel and the fold visible (but the iteration view named-by-role, not rendered as explicit recursion). The LHS of this theme.
- **L3>L2 firm** ([`L3-L2/ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md), firm cycle-021 wave-2) — the iteration-rotation erasure (explicit `iterate_while_L3` tail recursion ⟷ outer-driver-by-role wrap). The upward complement this theme's slug parallels.

This theme is the **downward edge** of the firm L2 `ksp_solve` driver. The firm L2 entry's §"Lowers from" (`book/src/L2/ksp_solve.md:155-157`) already records the rotation in-line, asserting it is **non-identity** ("the L2↔L1 rotation is **non-identity**: it is the *un-collapse* of the L1 opacity into a composition") and explicitly deferring the firming evidence to a working-note / dedicated-theme concern: "The reverse direction (how the L1 collapse re-absorbs the L2 composition) and the firming evidence for the open are working-notes / OQ-ledger concerns, not chapter content, per the high→low discipline." This theme IS that dedicated firming evidence, narrated forward L2→L1 (the L2 composition re-collapses into the L1 opacity).

The L2 entry's §"Lowers from" narrates the **open** (L1-opacity → L2-composition) from the L2 side; per the high→low discipline the formal lowering direction is L2 → L1 (the higher layer's composition dissolves into the lower layer's opaque operator). The two are the same rotation seen from the two sides; this theme is the canonical forward-narrated home.

## L2 form (LHS)

The L2 form is reproduced from [`L2/ksp_solve`](../L2/ksp_solve.md) §Signature — the outer-driver composition (the convergence-test fold of the visible kernel):

    ksp_solve :: (K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) -> SolveResult[N]
    ksp_solve K b =
      let (op, s_0)     = setup K b                          -- bind kernel op-surface; seed state (iterate, eps, counters)
      let s_init        = init_convergence op s_0            -- residual proxy + eps + pre-loop converged flag
      let s_n           = iterate_while                       -- the outer-driver fold over the kernel (NAMED BY ROLE)
                            (\s -> (krylov-step op s).state)  --   body: the L2 kernel (state projection) — VISIBLE
                            s_init                            --   seed
                            (\s -> not s.converged && s.it < op.max_it)  -- convergence predicate
      let s_final       = materialise_iterate op s_n          -- fold restart-cycle correction into s.x (identity for CG)
      in extract_result s_final                               -- the four-field SolveResult readout

At L2 the L1 opacity is **opened**: `K` is destructured by `setup` into the kernel op-surface `op` (which [`krylov-step`](../L2/krylov-step.md) consumes per-step) plus the loop-shaping fields the driver fold reads; the [`krylov-step`](../L2/krylov-step.md) kernel and the convergence-test fold that wraps it are **visible** as the body of an explicit composition. The L2 form carries the **solver-method** loop-shaping axis (CG single-fold / GMRES restart-nested-fold / FGMRES restart-nested-fold — selects the fold nesting + the result-residual proxy), which is the re-exposure of the L1-absorbed `krylov-method` axis (per `book/src/L2/ksp_solve.md:142`, the `KrylovSolver` factory cases `reference/palace/palace/linalg/ksp.cpp:34-58`).

## L1 form (RHS)

The L1 form is reproduced from [`L1/ksp_solve`](../L1/ksp_solve.md) §Signature — the opaque solver-as-operator:

    ksp_solve :: (K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) -> SolveResult[N]

    SolveResult[N] = {
      x          : Tensor[N],   -- approximate solution to A · x = b
      converged  : Bool,        -- whether the convergence test was satisfied
      iterations : Int,         -- number of inner Krylov iterations consumed
      initial_res: Real,        -- initial residual norm (per the solver's residual proxy)
      final_res  : Real         -- final residual norm (per the solver's residual proxy)
    }

At L1 the entire method body — outer loop, restart logic, per-step kernel — is collapsed into an **opaque** application: `K` is a black box, `Solver[A]` an opaque type with a system-operator axis `N` and an element type, guaranteed only to satisfy the convergence-test semantics; the per-method Krylov body (CG / GMRES / FGMRES) is NOT part of the L1 signature (`book/src/L1/ksp_solve.md:37`). The `krylov-method` axis is **absorbed into the opaque type** (per `book/src/L1/ksp_solve.md:93-95`, the canonical *variant absorption* application for the constructed-operator vocabulary). The `SolveResult` boundary record is **byte-identical** to the L2 boundary record (same four statistics fields + `x`) — so the rotation is on the *body*, not the boundary type.

## Rewrite shape

The rewrite is the **substantive re-collapse of the kernel-fold composition into the opaque operator**, the inverse of the L2 §"Lowers from" open. The whole content of the hop is the opacity re-closing: the visible kernel and the visible fold vanish back into `Solver[A]`. The `SolveResult` boundary type is unchanged. There are three forward-narrated re-collapse steps.

1. **The L2 explicit `iterate_while (krylov-step op) …` kernel-fold re-collapses into the L1 opaque `(K, b) -> SolveResult` operator application.** At L2 the fold body is `krylov-step op` — the kernel *visible* as a same-layer L2 composition (per `book/src/L2/ksp_solve.md:53-65`, the body is the convergence-test fold of the kernel). At L1 the fold and the kernel both **disappear** into the opaque `Solver[A]`: a solve becomes one indivisible operator application (per `book/src/L1/ksp_solve.md:37`, "the L1 entry collapses across all L0 representations"). This is the inverse of the L2 §"Lowers from" *open* — where the L2 entry opens the L1 black box into the kernel-fold composition, this lowering re-closes it. **This is the substantive content of the hop**: the kernel-fold composition is not a wrapper change around an identity body — the visibility of the kernel and the fold IS the L2 content, and erasing them back into opacity IS the rotation.

2. **The L2 solver-method loop-shaping axis re-absorbs into the L1 `krylov-method` opacity-axis.** At L2 the **solver-method** axis (`CG | GMRES | FGMRES`) is *exposed at composition granularity*: it selects the fold nesting (single vs. restart-nested) and the result-extraction residual proxy (`final_res = res` √|β| proxy for CG `reference/palace/palace/linalg/iterative.cpp:484`; `final_res = beta` LS-residual proxy for GMRES `:703`), per `book/src/L2/ksp_solve.md:142`. At L1 the same axis **collapses into the opaque `Solver[A]` type** as the absorbed `krylov-method` axis (per `book/src/L1/ksp_solve.md:93-95`): the L1 contract sees only the construction-bound solver and its convergence semantics; the per-method body is an L0 (and L2-`krylov-step`) concern. The L2 re-exposure of the axis at composition granularity re-absorbs into the L1 opacity. (The L1 preconditioner-side, absorbed into the kernel op-surface `op.T` at L2 per `book/src/L2/ksp_solve.md:144`, likewise re-absorbs; it is kernel-side, not a separate driver axis at L1.)

3. **The L2 fold-terminal laws re-collapse into the L1 fixed-point laws on the opaque operator (supporting; information-preserving).** At L2 the algebraic content is **fold-terminal properties** — laws about the fixed point the fold converges to (per `book/src/L2/ksp_solve.md:95-103`): terminal operator-inverse, zero-RHS / converged-warm-start short-circuit, terminal-solution linearity, per-call referential transparency. At L1 these restate as **fixed-point laws stated directly on the opaque operator** (per `book/src/L1/ksp_solve.md:57-74`): linearity in `b`, zero-RHS-zero-solution, operator-inverse, idempotent re-solve, construction-commutes-with-`SetOperators`. The laws are the *same* (the L2 entry states they are "inherited from `L1/ksp_solve`"); the rotation re-collapses the fold-terminal framing (laws about where the fold lands) into the operator framing (laws about what the black box computes). **Information-preserving**: no law is added or dropped; the fold-terminal framing is the L2 surface of the same fixed point the L1 operator names. Supporting, not the substantive content — the substantive content is (1)+(2), the kernel-fold→opacity re-collapse.

The mapping at the body's structural level:

| L2 line | L1 form | Mapping |
|---|---|---|
| `let (op, s_0) = setup K b` + `let s_init = init_convergence op s_0` | (inside the opaque `Solver[A]` apply) | **Substantive re-collapse.** The L2 explicit setup / convergence-init (destructuring `K` into the kernel op-surface, seeding `eps = max(rel_tol·initial_res, abs_tol)` and the pre-loop `converged = (res < eps)`) re-collapses into the opaque solver's internal state. L0 anchor `reference/palace/palace/linalg/iterative.cpp:417-418`. At L1 the setup is invisible (the black box owns it). |
| `let s_n = iterate_while (\s -> (krylov-step op s).state) s_init predicate` | (inside the opaque `Solver[A]` apply) | **Substantive (non-identity) — the heart of the hop.** The L2 VISIBLE kernel-fold over the unified `IterState` re-collapses into the L1 OPAQUE single operator application. The kernel ([`krylov-step`](../L2/krylov-step.md)) and the fold both vanish into `Solver[A]`. The L0 loop guard `for (; it < max_it && !converged; it++)` (`reference/palace/palace/linalg/iterative.cpp:427`) and the per-step `converged = (res < eps)` (`:463`) are the iteration the L1 form treats as one indivisible application. **This is the line where the L1 opacity re-closes — the substantive content.** |
| `let s_final = materialise_iterate op s_n` | (inside the opaque apply) | Re-collapse (identity-modulo-opacity). The final-iterate materialisation (identity for CG/Chebyshev; folds the last partial restart-cycle correction `K.V · K.y` for GMRES/FGMRES) re-collapses into the opaque solve. Same materialisation, now invisible. |
| `in extract_result s_final` | the `SolveResult[N]` record | **Boundary-identity.** Same four-field readout (`converged`/`iterations`/`initial_res`/`final_res`) + `x`. The `SolveResult` boundary record is byte-identical across the edge (the L2 entry's §"Lowers from" states "The `SolveResult` boundary type is unchanged (so the rotation is on the body, not the boundary)"). L0 result-write tails CG `:484-485`, GMRES `:703-704`; `GetConverged()` gate `reference/palace/palace/linalg/iterative.hpp:98`. |

The mapping is total on the body's structure, but it is **not** an identity-in-form mapping (contrast the BLAS-1 `-leaf-identity` cohort): the central line (the kernel-fold) carries a genuine rotation (visible composition → opaque application), and the solver-method axis carries a genuine re-absorption (composition-granularity → opacity). These are the non-identity content; the boundary line (`extract_result` → `SolveResult`) is identity; the law line is identity-modulo the fold-terminal↔fixed-point reframing.

## Applicability conditions

The rewrite is valid when all of the following hold (satisfied for the firm L2 and L1 forms by construction):

1. **The L2 form is the firm `L2/ksp_solve` outer-driver composition** — the convergence-test fold of [`krylov-step`](../L2/krylov-step.md) with the kernel and the fold visible, the iteration view named-by-role (per `book/src/L2/ksp_solve.md`). If a future Krylov-shaped slice (MINRES, BiCGStab — currently obstruction-only per [`L1-L0/minres-iteration`](../L1-L0/minres-iteration.md), [`L1-L0/bicgstab-iteration`](../L1-L0/bicgstab-iteration.md)) is firmed at L2 with a different kernel-fold structure, the re-collapse narration would need re-audit. Per the unimplemented-Palace-stub policy these are not implementation targets, so re-audit is not currently planned.
2. **The L1 form is the firm `L1/ksp_solve` opaque solver-as-operator** — the `(K, b) -> SolveResult` collapse with the `krylov-method` axis absorbed into the opaque `Solver[A]` type (per `book/src/L1/ksp_solve.md`). The firm L1 entry's §Semantics + §"Variant axes" record the opacity and the absorbed axis this theme re-collapses into.
3. **The `SolveResult` boundary type is identical across the edge.** The L2 §Signature `SolveResult[N]` record (four statistics + `x`) and the L1 §Signature `SolveResult[N]` record are byte-identical (the L2 entry's §"Lowers from" asserts this explicitly: "The `SolveResult` boundary type is unchanged (so the rotation is on the body, not the boundary)"). This is what makes the rotation a body-only rotation (the boundary line is identity).
4. **The kernel's own lowering is the L1>L0 concern, not this theme.** This theme covers only the L2→L1 driver re-collapse (kernel-fold composition → opaque operator). The per-step kernel body's lowering to L0 mutation source is the L1>L0 `ksp-solve-mutation-rotation` concern (cycle-008); the L2 kernel `krylov-step`'s own L2>L1 de-fusion is the *sibling* D4 theme `krylov-step-kernel-defusion` (this cycle). The clean division: this theme re-collapses the *driver* (the fold + the kernel-as-black-box), the sibling de-fuses the *kernel body* (the seven L1 primitives + the in-place→out-of-place buffer rotation). The two are disjoint and complementary, mirroring the L3>L2 kernel/driver division (`book/src/L3-L2/ksp-solve-outer-driver.md` §"Kernel-identity / driver-non-identity contrast").

## Justification kind

**`structural`** (dominant) with secondary **`reduction-chain`**.

**Structural (dominant)**: the non-identity content is a structural fact about the two layer surfaces — L2 renders the solve as an explicit kernel-fold composition (a visible composition is a structural form), L1 collapses it to an opaque operator application (an opaque black box is a structural absence of the kernel and the fold). The solver-method axis's re-absorption is structural: the axis is exposed at composition granularity at L2 (it shapes the visible fold nesting) and absorbed into the opaque type at L1 (it is a construction-bound choice inside `Solver[A]`). This is a claim about the shapes of the two forms (visible composition vs. opaque application; composition-granularity axis vs. opacity-absorbed axis), not about algebraic laws or step-semantics — hence structural. The contrast with the BLAS-1 `-leaf-identity` cohort is itself a structural observation: those edges are identity-in-form (the L2 leaf signature is value-thread-isomorphic to the L1 leaf), this edge is non-identity (the L2 composition is NOT value-thread-isomorphic to the L1 opaque application — the kernel and the fold are present at L2, absent at L1).

**Reduction-chain (secondary)**: the kernel-fold composition's re-collapse is grounded in the small-step `iterate_while` semantics from the strawman `book/src/design/l4_calculus.md` §3.7 — the L2 fold is the named-by-role combinator wrap, and the L1 opaque operator is the *fully-folded* (un-introspectable) terminal of that combinator's reduction. The forward L2→L1 narration re-collapses the visible combinator-wrap into the opaque single application. This is the reduction-chain backing for the central kernel-fold line; it is secondary because the load-bearing content (the kernel-fold → opacity re-collapse + the solver-method axis re-absorption) is structural.

**Abstraction-direction note**: L2 is the higher-abstraction layer for this edge (it has the L1 opacity opened into the kernel-fold composition); L1 is the lower-abstraction layer (it leaves the solve as one opaque operator application). The rotation direction is L2 → L1: the L2 form lowers to the L1 form by **re-collapsing** the visible kernel-fold composition into the opaque operator and **re-absorbing** the solver-method axis into the opacity. This matches the methodology's high→low lowering direction; the reverse (how the L1 opaque operator opens into the L2 composition — the *open*) is recorded only in the L2 entry's §"Lowers from" in-line, not narrated here.

## Speculative L1 operators

**None.** This theme is the substantive re-collapse rotation between two firm endpoints; no new L1 vocabulary is introduced. The L2 form referenced in the LHS is the firm [`L2/ksp_solve`](../L2/ksp_solve.md) entry; the L1 form referenced in the RHS is the firm [`L1/ksp_solve`](../L1/ksp_solve.md) entry. The [`krylov-step`](../L2/krylov-step.md) kernel both forms reference is firm at L2 ([`L2/krylov-step`](../L2/krylov-step.md), cycle-005). The `iterate_while` combinator is firm (`book/src/L4/iterate-while.md`, firmed cycle-007); it is referenced, not introduced.

## L2>L1 vs L3>L2 distinction (the asymmetry-closing pair)

The firm L2 `ksp_solve` driver now carries dedicated themes on **both** its edges, closing the per-edge asymmetry the cycle-046 census surfaced:

- **`ksp-solve-outer-driver-unfold` (this theme; the DOWNWARD L2>L1 edge)**: the L2 kernel-fold composition re-collapses into the L1 opaque solver-as-operator. Substantive (non-identity): the kernel and the fold vanish into `Solver[A]`; the solver-method axis re-absorbs into the `krylov-method` opacity-axis. The `SolveResult` boundary is identity.
- **[`ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md) (firm c021; the UPWARD L3>L2 edge)**: the L3 explicit `iterate_while_L3` tail recursion (carrying the named outer-loop `sequential-obstruction`) dissolves into the L2 outer-driver-by-role wrap. Substantive (non-identity): the iteration view is erased; the obstruction shadows to the L2 non-laws.

Both edges are non-identity, and they rotate *different* aspects: the L2>L1 edge rotates **opacity** (the kernel-fold composition's visibility — opened at L2, closed at L1); the L3>L2 edge rotates the **iteration view** (the fold's explicit-recursion rendering — rendered at L3, erased to a role reference at L2). The two are orthogonal: the L2 form sits at the junction — it has the opacity OPEN (vs. L1) and the iteration view ERASED (vs. L3). This theme firms the downward (opacity) edge; the c021 theme firms the upward (iteration-view) edge. Together they make the L2 driver's both-edge rotation profile explicit in the artifact.

## Verified-against

L2 evidence (the LHS):

- `book/src/L2/ksp_solve.md` (firm, cycle-021 wave-1) — the L2 outer-driver composition this theme references as LHS. §Signature (the `iterate_while (krylov-step op) …` kernel-fold, `:53-65`), §"Relationship to the L1 collapse" (`:33-37`, the open this theme inverts — "This L2 entry opens that black box into the kernel-fold composition"; "The L2↔L1 rotation is **non-identity**: it is the *un-collapse* of the L1 opacity into a composition"), §"Lowers from" (`:155-157`, the in-line L2>L1 narration this theme firms — explicitly defers the firming evidence to a dedicated theme / working-note), §"Variant axes" axis 1 (`:142`, the solver-method axis re-exposed at composition granularity), §"Algebraic laws" (`:95-103`, the fold-terminal laws that re-collapse to the L1 fixed-point laws), §"L2 vs L1 distinction" (`:163-166`, the layer-distinction this theme narrates as a rotation).
- `book/src/L2/krylov-step.md` (firm, cycle-005) — the L2 kernel half the L2 driver folds, made visible at L2 and re-collapsed into opacity at L1.

L1 evidence (the RHS):

- `book/src/L1/ksp_solve.md` (firm) — the L1 opaque solver-as-operator this theme lowers to. §Semantics (`:39-55`, the opaque solver, soft-fail, statistics-as-driver-side; "at L1 the operator-bound solver `K` is opaque about whether it is CG, GMRES, or FGMRES under the hood"), §Signature (`:37`, "`Solver[A]` is an *opaque type* at L1"; "the L1 entry collapses across all L0 representations"), §"Variant axes" collapsed-axis (`:93-95`, the `krylov-method` axis absorbed into the opaque type — the axis this theme re-absorbs into), §"Algebraic laws" (`:57-74`, the five fixed-point laws the L2 fold-terminal laws re-collapse into), §"L1 vs L0 distinction" (`:106-109`).

Sibling-theme evidence (the upward complement + the kernel sibling):

- `book/src/L3-L2/ksp-solve-outer-driver.md` (firm, cycle-021 wave-2) — the upward L3>L2 edge this theme's slug parallels (asymmetry-closing pair). §"Kernel-identity / driver-non-identity contrast" is the labour-division template; the two edges rotate orthogonal aspects (iteration-view vs. opacity).
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` (the L1>L0 edge below, cycle-008) — the next edge down the chain; the kernel body's lowering to L0 mutation source, out of this theme's scope (this theme stops at the L1 opaque operator).

L0 evidence (self-verified against `reference/palace/` source via `tools/citecheck/citecheck.py --anchor` this dispatch):

- `reference/palace/palace/linalg/iterative.cpp:361-486` — `CgSolver<OperType>::Mult` — the canonical single-fold outer driver the L2 form renders as a visible kernel-fold and the L1 form collapses to an opaque application. Setup + pre-loop test `eps = max(rel_tol·initial_res, abs_tol)` (`:417`), `converged = (res < eps)` pre-loop short-circuit (`:418`); the outer-driver loop guard `for (; it < max_it && !converged; it++)` (`:427`); the per-step in-loop convergence test `converged = (res < eps)` (`:463`); result write `final_res = res; final_it = it;` (`:484-485`).
- `reference/palace/palace/linalg/iterative.cpp:544-705` — `GmresSolver<OperType>::Mult` — the restart-nested double-fold outer driver. The outer restart loop `for (; it < max_it; restart++)` (`:563`); result write `final_res = beta; final_it = it;` (`:703-704`) — the LS-residual proxy the solver-method axis selects.
- `reference/palace/palace/linalg/iterative.cpp:377-386` — the CG initial-guess threading (the initial-guess-policy axis; loop-shaping at both layers, re-absorbed into the opaque `K` at L1).
- `reference/palace/palace/linalg/iterative.hpp:52-55` — `IterativeSolver<OperType>` result fields `converged` / `initial_res` / `final_res` / `final_it` — the four `SolveResult` fields' L0 origins (the boundary record identical across the edge); `GetConverged()` with its `rel_tol > 0 || abs_tol > 0` gate at `:98`.
- `reference/palace/palace/linalg/ksp.cpp:296-309` — `BaseKspSolver<OperType>::Mult` — the cumulative-statistics driver wrapper *above* this operator: `ksp->Mult(x, y)` (`:300`, the per-method fold both layers compose), the `GetConverged()` check + `Mpi::Warning` (`:301-306`), counter increments `ksp_mult++` / `ksp_mult_it += ksp->GetNumIterations()` (`:308-309`). The cumulative counters are driver-side above the per-solve operator — unchanged across the L2>L1 hop (driver-side at both layers).
- `reference/palace/palace/linalg/ksp.cpp:34-58` — `ConfigureKrylovSolver` factory switch on the `KrylovSolver` enum: implemented arms CG / GMRES / FGMRES; MINRES / BICGSTAB / DEFAULT abort at `:53-56` (`MFEM_ABORT` at `:56`) — the solver-method / krylov-method axis closed at three implemented arms.
- `reference/palace/palace/linalg/ksp.cpp:312-313` — explicit `BaseKspSolver` template instantiations for `Operator` and `ComplexOperator` (the element-type axis).
- `reference/palace/palace/linalg/ksp.hpp:71` — `Mult(const VecType &x, VecType &y) const` — the L0 central entry point (argument-name swap: `x` is the RHS, `y` is the solution) the L1 form lifts to `ksp_solve(K, b)`.
- `reference/palace/palace/linalg/divfree.cpp:175` — `ksp->Mult(rhs, psi)` call site inside `DivFreeSolver<VecType>::Mult` — one of the three driver-tier consumers (`eigsolve` / `divfree-projector` / `incremental-least-squares`) that motivate this theme's RANK-1 fan-out.

Strawman / combinator evidence (the reduction-chain backing):

- `book/src/design/l4_calculus.md` §3.7 — the `iterate_while` conventions source; the L2 fold is the named-by-role combinator wrap, the L1 opaque operator is the fully-folded terminal of the combinator's reduction.
- `book/src/L4/iterate-while.md` (firm cycle-007) — the firm `iterate_while` combinator the L2 fold references (and the L1 opacity collapses).

Cross-cutting concept references (consumed unchanged across the rotation):

- `book/src/concepts/solver-as-operator.md` — the type-level rotation; the L1 collapse this theme re-collapses into (the opaque `Solver[A]` substitutable for an `apply_linop`-style primitive).
- `book/src/concepts/variant-absorption.md` — the `krylov-method`-axis absorption into the opaque type (re-absorbed at L1; re-exposed as the solver-method composition-axis at L2).
- `book/src/concepts/convergence-test.md` — the stopping-predicate surface (the `\s -> not s.converged && s.it < op.max_it` predicate; visible at L2, internal to the opaque operator at L1).
- `book/src/concepts/constructed-operators.md` / `book/src/concepts/apply_BA.md` — the preconditioner-side absorption into the kernel op-surface (re-absorbed into the opaque `K` at L1).
- `book/src/concepts/ksp_solve.md` — the methodology-era concept page (the constructed-operator-companion framing; the divfree slice use). Cross-referenced, not duplicated.

Open-questions ledger:

- `scaffolding/open-questions.md` slug `ksp-solve-l2-l1-theme-gap` — the open question this theme closes. Status updates to `closed` on integration with answer-link `book/src/L2-L1/ksp-solve-outer-driver-unfold.md` (this file).
- `scaffolding/open-questions.md` slug `residual-l2-l1-gap-audit` — closed jointly with the sibling D4 theme `krylov-step-kernel-defusion` (the two L2>L1 gaps the cycle-046 census found).

## Status

`firm` — the theme's content is firm: both endpoints are firm ([`L2/ksp_solve`](../L2/ksp_solve.md) cycle-021 wave-1; [`L1/ksp_solve`](../L1/ksp_solve.md) firm); the substantive non-identity content (the kernel-fold → opacity re-collapse + the solver-method-axis re-absorption) is structurally grounded and citation-backed at both layers and the L0 source; the `SolveResult` boundary type is byte-identical across the edge (the rotation is body-only, not boundary); the fold-terminal-laws → fixed-point-laws re-collapse is information-preserving; the rewrite-shape table is total on the body structure with the substantive lines (the kernel-fold line + the solver-method-axis line) explicitly delimited; no speculative L1 vocabulary is introduced; the four applicability conditions are stated and confirmed. The firm L2 entry's §"Lowers from" (`book/src/L2/ksp_solve.md:155-157`) already narrated this rotation in-line and deferred the firming evidence to a dedicated theme — this theme IS that dedicated firming evidence, narrated forward L2→L1 per the high→low discipline.

Authored cycle-047 (D3, abstractor), enacting **Identity-lowerings still require both L levels** (both layers carry a firm `ksp_solve` entry; this theme is the connecting downward rotation), **Layers are defined high→low** (LHS L2, RHS L1, forward narration: the L2 composition re-collapses into the L1 opacity), and **Lower-level shared vocabulary takes priority** (the driver-tier `ksp_solve` is consumed by `eigsolve` / `divfree-projector` / `incremental-least-squares` — RANK-1 fan-out). The slug `ksp-solve-outer-driver-unfold` deliberately parallels the upward [`L3-L2/ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md) (firm cycle-021), closing the per-edge asymmetry around the firm L2 driver: both its edges are now dedicated themes. Unlike the BLAS-1 `-leaf-identity` cohort (identity-in-form floor edges), this rotation is **substantive** — the kernel-fold composition's visibility is the L2 content, and re-collapsing it into the L1 opacity is the whole rotation. It is the downward complement of the upward iteration-view erasure: the L2 driver sits at the junction (opacity OPEN vs. L1, iteration-view ERASED vs. L3), and the two non-identity edges rotate orthogonal aspects.
```

```edit:book/src/L2-L1/index.md
| [incremental-least-squares-composition-lowering](./incremental-least-squares-composition-lowering.md) | `L2/incremental-least-squares` (firm, cycle-026) | `L1/back_solve` (firm leaf, cycle-027; terminal back-solve) + `concepts/givens_generate`/`givens_apply` (firm; de-fused 4-sub-step Face 2) + `L2/linear_combination` (firm; back-solve reconstruction) + `ls_update_column` *(forthcoming column-streaming leaf; plain-text forward-ref)* | firm *(algebraic; running-QR fan-down `replay▷generate▷apply▷apply_rhs`▷back-solve; FIXED sub-step sequence — replay-before-generate non-commutative load-bearing; two parametric axes `basis_kind∈{V,Z}` + `variant∈{real,complex}`; reduction-path = rotation-ordering + LAPACK scaling, NO MPI collective; terminal back-solve = firm `back_solve` leaf, NOT general `trsv` (separately blocked))* |
| [ksp-solve-outer-driver-unfold](./ksp-solve-outer-driver-unfold.md) | `L2/ksp_solve` (firm, cycle-021 wave-1) | `L1/ksp_solve` (firm) | firm *(structural; the DOWNWARD opacity edge of the firm L2 `ksp_solve` driver — the L2 VISIBLE kernel-fold composition `iterate_while (krylov-step op) …` RE-COLLAPSES into the L1 OPAQUE solver-as-operator `(K, b) -> SolveResult`; the inverse of the L2 §"Lowers from" open; solver-method composition-axis re-absorbs into the L1 `krylov-method` opacity-axis; `SolveResult` boundary byte-identical (rotation body-only); slug parallels the UPWARD `L3-L2/ksp-solve-outer-driver` (firm c021), closing the per-edge asymmetry — both edges of the L2 driver now dedicated themes; the two edges rotate ORTHOGONAL aspects (this = opacity; c021 = iteration-view))* |
```

(My OWN index-table row — appended after the `incremental-least-squares-composition-lowering` row. Dual-registration partition: this row is always mine.)

```edit:book/src/L2-L1/index.md
- `incremental-least-squares-composition-lowering` — running-QR / Givens-stream fan-down `replay ▷ generate ▷ apply ▷ apply_rhs` ▷ back-solve; FIXED sub-step sequence (replay-before-generate non-commutative load-bearing); two parametric axes `basis_kind ∈ {V, Z}` + `variant ∈ {real, complex}`.

*Substantive driver-tier composition→opacity edge (cycle-047; the DOWNWARD edge of the firm L2 `ksp_solve` driver — NOT a leaf-identity, NOT a fold-specialization; the visible kernel-fold composition re-collapses into the L1 opaque operator):*

- `ksp-solve-outer-driver-unfold` (cycle-047 D3) — the L2 `ksp_solve` **outer-driver composition** (the convergence-test fold of the VISIBLE [`krylov-step`](../L2/krylov-step.md) kernel) lowers to the L1 **opaque solver-as-operator** `(K, b) -> SolveResult` by RE-COLLAPSING the kernel-fold composition back into the black-box `Solver[A]` (the inverse of the L2 §"Lowers from" *open*). **Substantive (non-identity)**: the kernel and the fold are visible at L2, opaque at L1; the L2 solver-method composition-granularity axis re-absorbs into the L1 `krylov-method` opacity-axis; the `SolveResult` boundary record is byte-identical (rotation body-only). Slug parallels the UPWARD [`L3-L2/ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md) (firm c021), closing the per-edge asymmetry around the firm L2 driver — both its edges now dedicated themes, rotating ORTHOGONAL aspects (this edge = **opacity**, opened at L2 / closed at L1; the c021 edge = **iteration-view**, rendered at L3 / erased at L2). Driver-tier RANK-1 fan-out (consumed by `eigsolve` / `divfree-projector` / `incremental-least-squares`).
```

(My OWN §Vocabulary-cohort bullet — a new sub-group heading for the substantive driver-tier composition→opacity edge (it is neither a leaf-identity nor a fold-specialization, so it gets its own sub-group), appended after the `incremental-least-squares-composition-lowering` firm bullet. Dual-registration partition: this bullet is always mine. The D4 sibling `krylov-step-kernel-defusion` appends its own cohort bullet.)

```edit:book/src/L2-L1/index.md
- Cohort growth log (most-recent first): `ksp-solve-outer-driver-unfold` (D3) + `krylov-step-kernel-defusion` (D4) firm cycle-047 (the **driver+kernel L2>L1 edge-pair** closing the cycle-046-census two-gap residual — the `ksp_solve` **driver** opacity-edge + the `krylov-step` **kernel** de-fusion-edge, the two firm-L2-entries that lacked a dedicated L2>L1 theme; firm **19 → 21** = 21 firm + 1 partly-constructive; `ksp-solve-outer-driver-unfold` is the DOWNWARD opacity edge of the firm L2 `ksp_solve` driver (substantive: the visible kernel-fold composition re-collapses into the L1 opaque solver-as-operator — the inverse of the L2 §"Lowers from" open; closes `ksp-solve-l2-l1-theme-gap`), its slug paralleling the UPWARD `L3-L2/ksp-solve-outer-driver` (firm c021) to close the per-edge asymmetry around the L2 driver — both edges now dedicated themes, rotating ORTHOGONAL aspects (opacity vs. iteration-view); `krylov-step-kernel-defusion` is the kernel-body de-fusion edge resolving the dangling `L2/krylov-step.md:121` in-place-buffer forward-reference; the two together close `residual-l2-l1-gap-audit`); `axpy-leaf-identity` + `axpby-leaf-identity` + `axpbypcz-leaf-identity` + `normalize-leaf-identity` firm cycle-043 (the **leaf-cohort floor-edge batch** — the L2>L1 thin-identity edges of the four new same-named L2 floors; firm **15 → 19** = 19 firm + 1 partly-constructive; the `axpy`-family three are fold-PARENTED arity-2/2/3 members of `linear_combination` (UNBLOCKED by the batch-12 leaf-floor (b) ratification — RESOLVED, no longer under the §"Design fork"), `normalize-leaf-identity` is the fused-composite edge with NO fold-parent (design-final like the cycle-042 standalone edges); the cycle-043 D1 lifter sweep also normalized `nrm2-fold-specialization`→`nrm2-leaf-identity` + `scal-fold-specialization`→`scal-leaf-identity` (net-zero on counts) so the whole L2>L1 identity-edge cohort is now uniform `-leaf-identity`); `assemble-diagonal-leaf-identity` + `jacobi-smoother-leaf-identity` + `divfree-projector-leaf-identity` + `reciprocal-leaf-identity` + `elementwise-product-leaf-identity` firm cycle-042 (the **fork-INDEPENDENT standalone-floor-edge cohort** — the L2>L1 thin-identity edges of the five new same-named L2 floors, each with **NO fold-parent**; firm **10 → 15** = 15 firm + 1 partly-constructive; four pure identity-in-form, `divfree-projector-leaf-identity` carries the one genuine step-4 `AddMult` re-fusion; **design-final, NOT subject to the §"Design fork"** — having no fold-parent, none can be re-anchored into a fold); `dot-leaf-identity` + `nrm2-leaf-identity` + `scal-leaf-identity` firm cycle-041 (the FOLD-PARENTED BLAS-1-floor-edge cohort — the L2>L1 thin-identity edges of the same-named L2 floors `dot`/`nrm2`/`scal`, firm 7 → 10; all fusion deferred to the fold-parents, all identity-in-form on the primitive; `nrm2`/`scal` renamed cycle-043 from `-fold-specialization` to the uniform `-leaf-identity` convention; **presuppose the (b) leaf-floor design realization — under batch-12 meta-phase adjudication, see §"Design fork" below**); `incremental-least-squares-composition-lowering` firm cycle-028 (closes the L2 `l2-named-composition-lifts` lowering side); `eigsolve-spectral-transform-composition` + `gram-fold-specialization` firm cycle-022/023 (eigsolve chain-step-2 + Gram fold-lift); `deflate-composition-lowering` partly-constructive cycle-022 (first L2>L1 partly-constructive entry); `orthogonalize-composition-lowering` firm cycle-019; `inner-product-fold-specialization` + `linear-combination-fold-specialization` firm cycle-018/019 (the variadic-fold unification); `chebyshev-iteration-fusion` firm cycle-013 (first L2-L1 chapter).
```

(The CONSOLIDATED running-count tally — I am SOLE count-owner this cycle. This `edit:` replaces the on-disk Cohort growth log line (verified current on-disk: firm **19** + 1 partly-constructive, the cycle-043 head) with the cycle-047 head accounting for BOTH D3 (this theme) AND D4 (`krylov-step-kernel-defusion`, which defers its tally to me): **19 firm + 1 partly-constructive → 21 firm + 1 partly-constructive**. D4 authors its own row + cohort bullet but NOT this tally.)

```edit:book/src/SUMMARY.md
- [divfree-projector-leaf-identity](./L2-L1/divfree-projector-leaf-identity.md)
- [ksp-solve-outer-driver-unfold](./L2-L1/ksp-solve-outer-driver-unfold.md)
```

(My OWN SUMMARY.md chapter entry under the `# L2 > L1 — Lowering` Part — appended after the last existing L2-L1 chapter line `divfree-projector-leaf-identity`. Always mine.)

## Speculative operators proposed

**None.** This theme is the substantive re-collapse rotation between two firm endpoints — firm [`L2/ksp_solve`](book/src/L2/ksp_solve.md) (LHS) and firm [`L1/ksp_solve`](book/src/L1/ksp_solve.md) (RHS). No new L1 vocabulary is introduced; the [`krylov-step`](book/src/L2/krylov-step.md) kernel the L2 form folds is firm at L2, and the `iterate_while` combinator the fold references is firm (`book/src/L4/iterate-while.md`, cycle-007). Nothing for the harvester to promote.

## Supporting evidence

L2 / L1 endpoints (both firm):

- `book/src/L2/ksp_solve.md` (firm, cycle-021 wave-1) — LHS. §Signature `:53-65` (the visible `iterate_while (krylov-step op) …` kernel-fold), §"Relationship to the L1 collapse" `:33-37` (the *open* this theme inverts; the explicit non-identity assertion), §"Lowers from" `:155-157` (the in-line narration this theme firms; defers the firming evidence to a dedicated theme), §"Variant axes" axis 1 `:142` (the solver-method axis re-exposed at composition granularity), §"Algebraic laws" `:95-103` (fold-terminal laws).
- `book/src/L1/ksp_solve.md` (firm) — RHS. §Signature `:37` (the opaque `Solver[A]` type), §Semantics `:39-55` (opaque solver; soft-fail; statistics-as-driver-side), §"Variant axes" collapsed-axis `:93-95` (the `krylov-method` axis absorbed into the opaque type — re-absorbed here), §"Algebraic laws" `:57-74` (the five fixed-point laws).

Mirrored structure (the upward asymmetry-closing complement):

- `book/src/L3-L2/ksp-solve-outer-driver.md` (firm, cycle-021 wave-2) — the upward L3>L2 edge whose slug this theme parallels; the per-edge-asymmetry-closing pair. §"Kernel-identity / driver-non-identity contrast" is the labour-division template.

L0 source (all self-verified via `tools/citecheck/citecheck.py --anchor` this dispatch; every cited pinpoint returned `[ok]`):

- `reference/palace/palace/linalg/iterative.cpp:417` (`eps = max(...)`), `:418` (pre-loop `converged = (res < eps)`), `:427` (loop guard `for (; it < max_it && !converged; it++)`), `:463` (in-loop `converged = (res < eps)`), `:484-485` (CG result write `final_res = res; final_it = it;`), `:703-704` (GMRES result write `final_res = beta; final_it = it;`), `:377-386` (CG initial-guess threading).
- `reference/palace/palace/linalg/iterative.hpp:52-55` (the four result fields), `:98` (`GetConverged()` gate `rel_tol > 0 || abs_tol > 0`).
- `reference/palace/palace/linalg/ksp.cpp:300` (`ksp->Mult(x, y)` per-method fold), `:301-306` (`GetConverged()` + `Mpi::Warning`), `:308-309` (cumulative counters `ksp_mult++` / `ksp_mult_it`), `:53-56` (`MFEM_ABORT` for MINRES/BICGSTAB/DEFAULT), `:312-313` (template instantiations).
- `reference/palace/palace/linalg/ksp.hpp:71` (the L0 `Mult(x, y)` entry point), `reference/palace/palace/linalg/divfree.cpp:175` (one driver-tier consumer call site — `ksp->Mult(rhs, psi)`).

Strawman / combinator + concept references: `book/src/design/l4_calculus.md` §3.7 (`iterate_while`), `book/src/L4/iterate-while.md` (firm c007), `book/src/concepts/solver-as-operator.md`, `book/src/concepts/variant-absorption.md`, `book/src/concepts/convergence-test.md`, `book/src/concepts/ksp_solve.md`.

## Open questions / caveats

- **Closes `ksp-solve-l2-l1-theme-gap`** (`scaffolding/open-questions.md:182`) — the dedicated `L2-L1/ksp_solve` theme file the firm L2 §"Lowers from" deferred to. The integrator should set this OQ `closed` with answer-link `book/src/L2-L1/ksp-solve-outer-driver-unfold.md`.
- **Closes `residual-l2-l1-gap-audit` jointly with D4** (`krylov-step-kernel-defusion`). This theme covers the `ksp_solve` driver gap; D4 covers the `krylov-step` kernel gap. Once both land, the cycle-046 census's two-gap residual is closed. (The benign `residual-l2-l1-gap-audit-planner-undercount` data point `:184` also resolves — the planner used the census's gap-set of 2.)
- **Count-ownership note (this cycle).** I am SOLE `L2-L1/index.md` consolidated-tally owner. I verified the on-disk tally before bumping: the cycle-043 Cohort-growth-log head reads firm **19** + 1 partly-constructive (matching the 20 themes-table rows: 19 firm + 1 partly-constructive `deflate-composition-lowering`). My tally edit bumps to **21 firm + 1 partly-constructive**, accounting for BOTH D3 (this theme) and D4 (`krylov-step-kernel-defusion`, which defers its tally to me per the dual-registration partition). D4 authors its own table row + cohort bullet + SUMMARY line but NOT the tally; if D4 does not land this cycle, the integrator should reconcile the tally to **20 firm + 1 partly-constructive** (D3 only).
- **Forward-reference hygiene.** This theme references the sibling D4 theme `krylov-step-kernel-defusion` (in §"Applicability conditions" condition 4 and the cohort growth-log line) by **plain-text slug** (no live link), since its anchor file is authored in a parallel dispatch and may not be on-disk at this theme's integration moment. If D4 lands in the same cycle, the integrator may upgrade the plain-text reference to a live link (per skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`); otherwise it stays plain-text per the `rough-in-rows-must-be-plain-text-when-anchor-missing` convention.
- **Caveat (not a defect): the L2 §"Lowers from" narrates the OPEN, this theme narrates the LOWERING.** The L2 chapter's in-line §"Lowers from" describes the rotation from the L1→L2 *open* direction (the L1 opacity is opened into the L2 composition). Per the high→low discipline, the formal lowering direction is L2→L1 (the L2 composition re-collapses into the L1 opacity). These are the same rotation seen from the two sides; this theme is the canonical forward-narrated (high→low) home. No contradiction — the L2 in-line narration and this theme agree on the rotation content (non-identity; opacity open/closed); they differ only in narration direction, and this theme is the formally-correct one.

## Provenance

- Dispatched cycle-047 (D3) — abstractor, NEW L2>L1 theme `ksp-solve-outer-driver-unfold` + SOLE `L2-L1/index.md` consolidated-tally owner.
- Inputs read in full: `book/src/L2/ksp_solve.md`, `book/src/L1/ksp_solve.md`, `book/src/L3-L2/ksp-solve-outer-driver.md` (structure mirror + asymmetry-framing confirm), `book/src/L2-L1/index.md` (themes-table + cohort + Working-Notes tally), `book/src/SUMMARY.md` (L2-L1 Part).
- All L0 citations self-verified via `tools/citecheck/citecheck.py --anchor` this dispatch (every pinpoint `[ok]`).
- Deliverable `book/src/L2-L1/ksp-solve-outer-driver-unfold.md` verified ABSENT pre-authoring (genuine create).
- Write-guard honored: NO direct `book/` write; full chapter body inside the `new:` fence; index/SUMMARY edits inside `edit:` fences; all inner code samples rendered as 4-space-indented blocks (no nested ` ``` ` fences inside the proposed-changes blocks).

