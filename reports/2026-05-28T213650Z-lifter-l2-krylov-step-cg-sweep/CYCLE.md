---
agent: lifter
invoked_at: 2026-05-28T213650Z
scope: L2>L1 (citation sweep) theme re-anchor — book/src/L2/krylov-step.md cg.md dangling-pointer sweep
status: integrated
integrated_at: 2026-05-28T221238Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-016 (per-report position 3). Pure citation re-anchor of 12 dangling cg.md range pointers + 1 repair-added sibling iterative.cpp:244-250→:21-32 CheckDot drift correction in firm L2/krylov-step.md across 13 edit blocks; status stays firm. OQ l2-krylov-step-cg-md-citation-sweep answered (ledger:2793; 2 live-slice citations cg.md:27-141/:86-106 retained pending future slice removal). Retroactive-budget 0. Book build clean (exit 0)."
inputs:
  - book/src/L2/krylov-step.md
  - book/src/spec/slices/cg.md (reduced stub; 165 lines)
  - book/src/L3/krylov-step.md (cycle-010/015 terminal-home convention; cycle-015 L3 sweep terminus)
  - book/src/L1-L0/ksp-solve-mutation-rotation.md (CG L0 terminal home — Sub-pattern B)
  - book/src/L1/ksp_solve.md (preconditioner-variant terminal home)
  - book/src/concepts/first-iteration-unrolling.md
  - book/src/concepts/derived-view-hoisting.md
  - book/src/concepts/sequential-obstruction.md
  - reference/palace/palace/linalg/iterative.cpp:21-32, :243-250, :377-386, :427-464, :434-441 (L0 self-verify)
---

# CYCLE: Re-anchor book/src/L2/krylov-step.md cg.md dangling-pointer sweep

## Summary

`book/src/L2/krylov-step.md` carries **12 dangling `cg.md:NNN-MMM` pointers** that broke when the Phase-1 `cg.md` slice was reduced to a 165-line stub at cycle-010 (commit `30119eb`, "first phase-1 corpus reduction"). The L2 file's pointers reference ranges like `:172-188`, `:393-425`, `:430-446`, `:228-257`, `:325-339`, `:341-349`, `:381-391`, `:288` — **all of which now either fall past the reduced stub's 165-line boundary or land on content-drifted lines** (the only material retained in the stub is the L4-v0.5 first-iteration-unrolling derivation at `cg.md:27-141`). This is the same dangling-pointer cohort the cycle-015 L3 sweep already terminated against `L2/krylov-step.md:138`/`:146`; this dispatch sweeps L2's own outbound `cg.md` pointers down to their terminal homes below L2.

This is a **pure citation-refinement sweep** following the cycle-009/010 corpus-reduction convention already codified in the firm `book/src/L3/krylov-step.md` §Evidence (lines 196, 204): point each dangling range at its **terminal firm home** (the firm L0 source range or firm layered entry that now authoritatively holds the evidence), preserve the original pre-reduction range parenthetically, and cite the live retained slice material (`cg.md:27-141` for v0.5, `cg.md:86-106` for the `cg_solve` driver) where it still holds. No structural / decomposition / signature change. One bounded prose-correction is folded in (the drifted CheckDot citation `iterative.cpp:244-250` → `:21-32`; the cited `:244-250` is actually the `ApplyB` helper, not `CheckDot` — verified by direct L0 read).

**13 sites re-anchored (the 13th added in repair — the surviving line-171 `CheckDot` drift sibling). Terminal homes (all verified this dispatch):**

| L2 site | dangling `cg.md` range | terminal firm home |
|---|---|---|
| §Context (line 7) | `:103-115, :172-188, :393-425` (CG step bodies) | this entry §Evidence (firm L2 home) + `L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B (`iterative.cpp:360-486`) + live v0.5 slice `cg.md:27-141` |
| §Context (line 9) | `:341-349` (sequential-obstruction) | `concepts/sequential-obstruction.md` + `arnoldi_step.md:194-213` |
| §Semantics breakdown (line 67) | `:288` + `iterative.cpp:244-250` (CheckDot) | `iterative.cpp:21-32` (CheckDot; drift-corrected) + `L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B |
| §Semantics first-iteration (line 69) | `:172-188, :393-425, :381-391` | `concepts/first-iteration-unrolling.md` + live slice `cg.md:27-141` (v0.5) / `cg.md:120-133` (forget_β_prev) |
| §Algebraic laws 1 (line 77) | `:325-339` (residual-norm hoisting) | `concepts/derived-view-hoisting.md` §"Worked example: CG residual norm" |
| §Algebraic laws 2 (line 79) | `:103-115` (primitive enumeration) | this entry §Evidence + `iterative.cpp:443` (apply_linop per step) via `ksp-solve-mutation-rotation.md` |
| §Algebraic laws 3 (line 81) | `:103-115` (state-stratum independence) | same terminal home as line 79 |
| §Variant axes 1 (line 116) | `:228-257` (PCG vs unpreconditioned) | `L1/ksp_solve.md` Variant axes + `iterative.cpp:377-386` via `ksp-solve-mutation-rotation.md` Sub-pattern B |
| §Variant axes 4 (line 119) | `:172-188, :393-425` (first-iteration variant) | `concepts/first-iteration-unrolling.md` + live slice `cg.md:39-106` |
| §Evidence (line 138) | `:103-115, :172-188, :393-425` (slice instances) | live slice `cg.md:27-141` (v0.5 retained) + L0 via `ksp-solve-mutation-rotation.md` |
| §Evidence (line 146) | `:208-220, :430-446` (outer-driver) | live slice `cg.md:86-106` (`cg_solve` driver) + `iterative.cpp:427-464` via `ksp-solve-mutation-rotation.md` |
| §Evidence (line 172) | `:288` (CheckDot tests) | `iterative.cpp:21-32` (CheckDot) |
| §Evidence (line 171, repair-added) | `iterative.cpp:244-250` (CheckDot mislabel) | `iterative.cpp:21-32` (CheckDot; same ApplyB-drift correction as line 67) |

## Proposed changes

```edit:book/src/L2/krylov-step.md
[old]: The Phase-1 slice corpus exhibits a recurring pattern: every iterative method written as a per-step kernel composed of (at most) five primitive groups, threaded by an outer fold. CG (`cg.md:103-115, :172-188, :393-425`), GMRES (`gmres.md:459-471`), Chebyshev (`book/src/L4/chebyshev.md` §Semantics `innerStep` — the polynomial-recurrence kernel), Arnoldi (`arnoldi_step.md:99-105, :285-298`), and the three polynomial-recurrence sites cataloged at `polynomial_recurrence_step.md:119-160` all factor into the same kernel-plus-driver shape. The combinator-miner cycle-002 enumerated the five pattern instances and proposed `krylov-step` as the L2 name for the kernel. This chapter is the firm operator definition.
[new]: The Phase-1 slice corpus exhibits a recurring pattern: every iterative method written as a per-step kernel composed of (at most) five primitive groups, threaded by an outer fold. CG (the firm CG step-body evidence lives in this entry's §Evidence and lowers to L0 at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B — `iterative.cpp:360-486`; the L4-v0.5 first-iteration-unrolled rendering remains live at `book/src/spec/slices/cg.md:27-141`; original pre-reduction slice ranges `cg.md:103-115, :172-188, :393-425`), GMRES (`gmres.md:459-471`), Chebyshev (`book/src/L4/chebyshev.md` §Semantics `innerStep` — the polynomial-recurrence kernel), Arnoldi (`arnoldi_step.md:99-105, :285-298`), and the three polynomial-recurrence sites cataloged at `polynomial_recurrence_step.md:119-160` all factor into the same kernel-plus-driver shape. The combinator-miner cycle-002 enumerated the five pattern instances and proposed `krylov-step` as the L2 name for the kernel. This chapter is the firm operator definition.
```

```edit:book/src/L2/krylov-step.md
[old]: `krylov-step` lives at **L2**, not L3 or L4. L3 is the iteration-rotation layer; the *outer* iteration of every Krylov method carries a `sequential-obstruction` at L3 (cg.md:341-349, arnoldi_step.md:194-213), and the step body composes L3-native primitives without a global lift opportunity.
[new]: `krylov-step` lives at **L2**, not L3 or L4. L3 is the iteration-rotation layer; the *outer* iteration of every Krylov method carries a `sequential-obstruction` at L3 (the firm [`sequential-obstruction`](../concepts/sequential-obstruction.md) concept page; live anchor `arnoldi_step.md:194-213` — the original CG evidence `cg.md:341-349` was lifted into the concept page + `book/src/L3/krylov-step.md` §"Iteration-rotation marker" per the cycle-009 corpus reduction), and the step body composes L3-native primitives without a global lift opportunity.
```

```edit:book/src/L2/krylov-step.md
[old]: The kernel can carry **breakdown signals** through the `outputs.breakdown_token` slot. Palace's `CheckDot` (cg.md:288, iterative.cpp:244-250) is the L0 anchor: the dot-product is partial-functioned on finiteness and (for SPD systems) positivity.
[new]: The kernel can carry **breakdown signals** through the `outputs.breakdown_token` slot. Palace's `CheckDot` (`reference/palace/palace/linalg/iterative.cpp:21-32` — real overload at :22, complex overload at :28; called at :396, :410, :445, :461; recognised at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B) is the L0 anchor: the dot-product is partial-functioned on finiteness and (for SPD systems) positivity.
```

```edit:book/src/L2/krylov-step.md
[old]: The kernel can carry a **first-iteration branch** internally (CG v0.4 form, cg.md:172-188) or be unrolled out to a separate `cg_first_step` kernel before `iterate_while_with_prev` (CG v0.5 form, cg.md:393-425). Both are valid `krylov-step` shapes; the variant axis `first-iteration-unrolled` is a *step-shape* variant, not a *step-body* variant. Each form has a fixed (different) record schema; the unrolled form's steady-state record drops `β_prev` (cg.md:381-391). The choice is documented at [`concepts/first-iteration-unrolling`](../concepts/first-iteration-unrolling.md).
[new]: The kernel can carry a **first-iteration branch** internally (CG v0.4 form; the L0 `if (!it) { p = z; } else { AXPBY(...beta/beta_prev...); }` branch at `iterative.cpp:434-441`) or be unrolled out to a separate `cg_first_step` kernel before `iterate_while_with_prev` (CG v0.5 form, live at `book/src/spec/slices/cg.md:27-141`). Both are valid `krylov-step` shapes; the variant axis `first-iteration-unrolled` is a *step-shape* variant, not a *step-body* variant. Each form has a fixed (different) record schema; the unrolled form's steady-state record drops `β_prev` (the `forget_beta_prev` projection making the v0.4↔v0.5 equivalence formal is at `book/src/spec/slices/cg.md:120-133`). The choice is documented at [`concepts/first-iteration-unrolling`](../concepts/first-iteration-unrolling.md). (Original pre-reduction slice ranges: `cg.md:172-188`, `:393-425`, `:381-391`.)
```

```edit:book/src/L2/krylov-step.md
[old]: Witnessed at cg.md:325-339 (the residual-norm hoisting), `book/src/L4/chebyshev.md` §"Initial-guess shape: branch vs derived view" (the derived-view treatment of `initial_guess`-as-control), and gmres.md:471-489 (the LS-residual proxy). This is the *only* non-trivial algebraic law `krylov-step` carries.
[new]: Witnessed at [`concepts/derived-view-hoisting`](../concepts/derived-view-hoisting.md) §"Worked example: CG residual norm" (the residual-norm hoisting; the canonical CG evidence lifted from the now-reduced slice per the cycle-009 corpus reduction — original pre-reduction range `cg.md:325-339`), `book/src/L4/chebyshev.md` §"Initial-guess shape: branch vs derived view" (the derived-view treatment of `initial_guess`-as-control), and gmres.md:471-489 (the LS-residual proxy). This is the *only* non-trivial algebraic law `krylov-step` carries.
```

```edit:book/src/L2/krylov-step.md
[old]: This is the cost-metric invariant Krylov-methods literature uses; `krylov-step` makes it a first-class structural property. Witnessed by the per-slice primitive-call enumeration at cg.md:103-115, arnoldi_step.md:99-105, `book/src/L4/chebyshev.md` §Semantics `innerStep` (one `applyLinop op.A d` per `k`).
[new]: This is the cost-metric invariant Krylov-methods literature uses; `krylov-step` makes it a first-class structural property. Witnessed by the per-slice primitive-call enumeration: for CG, the one `A->Mult(p, z)` per step at `iterative.cpp:443` inside the inner for-loop `iterative.cpp:427-464` (recognised at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B; original pre-reduction slice range `cg.md:103-115`); arnoldi_step.md:99-105; `book/src/L4/chebyshev.md` §Semantics `innerStep` (one `applyLinop op.A d` per `k`).
```

```edit:book/src/L2/krylov-step.md
[old]: This is what makes per-step parallelism *between strata* (the field-side `axpy` and the scalar-side recurrence-update at the same step time) a transparent performance optimisation at L1>L0, not an algebraic change. Witnessed at cg.md:103-115 (CG's `dot z'_A p'` reads `z'_A` from the apply, but no `axpy` reads the same scalar before the dot completes).
[new]: This is what makes per-step parallelism *between strata* (the field-side `axpy` and the scalar-side recurrence-update at the same step time) a transparent performance optimisation at L1>L0, not an algebraic change. Witnessed at `iterative.cpp:427-464` (CG's inner loop: `denom = Dot(comm, z, p)` at :444 reads `z` from the `A->Mult(p, z)` apply at :443, but the `x.Add(alpha, p)` / `r.Add(-alpha, z)` axpy updates at :448-449 do not read `denom`/`beta` before the dot completes — recognised at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B; original pre-reduction slice range `cg.md:103-115`).
```

```edit:book/src/L2/krylov-step.md
[old]: 1. **preconditioner present/absent** — CG vs. PCG; GMRES via the `apply_BA = A·M⁻¹` / `M⁻¹·A` / `B^{1/2}·A·B^{1/2}` constructed-operator surface. Absorbed at level (c) into `op.T`. Witnessed at cg.md:228-257 (PCG vs. unpreconditioned CG), gmres.md:135-150 (`apply_BA` pc-side absorption).
[new]: 1. **preconditioner present/absent** — CG vs. PCG; GMRES via the `apply_BA = A·M⁻¹` / `M⁻¹·A` / `B^{1/2}·A·B^{1/2}` constructed-operator surface. Absorbed at level (c) into `op.T`. Witnessed for CG/PCG at the L0 `if (B) { ApplyB(B, r, z, ...); } else { z = r; }` preconditioner branch inside the inner loop `iterative.cpp:427-464` plus the initial-guess/preconditioner threading at `iterative.cpp:377-386` (the variant collapse is documented at [`L1/ksp_solve`](../L1/ksp_solve.md) Variant axes; the L1>L0 reintroduction at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B; original pre-reduction slice range `cg.md:228-257`), gmres.md:135-150 (`apply_BA` pc-side absorption).
```

```edit:book/src/L2/krylov-step.md
[old]: 4. **first-iteration-unrolled vs. branch-in-body** — CG v0.4 (cg.md:172-188) keeps the `if it == 0 then s.r else axpby ...` branch inside the kernel; CG v0.5 (cg.md:393-425) splits `cg_first_step` and `cg_steady_step` and threads `β_prev` via `iterate_while_with_prev`. Both forms are valid `krylov-step` shapes; the variant axis selects which.
[new]: 4. **first-iteration-unrolled vs. branch-in-body** — CG v0.4 keeps the `if it == 0 then s.r else axpby ...` branch inside the kernel (L0 anchor `iterative.cpp:434-441`); CG v0.5 (live at `book/src/spec/slices/cg.md:39-106`) splits `cg_first_step` and `cg_steady_step` and threads `β_prev` via `iterate_while_with_prev`. Both forms are valid `krylov-step` shapes; the variant axis selects which. (Original pre-reduction slice ranges: `cg.md:172-188`, `:393-425`.)
```

```edit:book/src/L2/krylov-step.md
[old]: - `book/src/spec/slices/cg.md:103-115` (CG L2 step body), `:172-188` (CG L4 `cg_step`), `:393-425` (CG L4 v0.5 split into `cg_first_step` and `cg_steady_step`).
[new]: - CG L2 / L4 / L4-v0.5 step bodies — the firm L0 terminal home is `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B (the inner CG body `iterative.cpp:360-486`; the per-step kernel for-loop `iterative.cpp:427-464`). The L4-v0.5 first-iteration-unrolling rendering (`cg_first_step` / `cg_steady_step`) remains the unique live material retained in the reduced slice at `book/src/spec/slices/cg.md:27-141`. (Original pre-reduction slice ranges: `cg.md:103-115` L2 step body, `:172-188` L4 `cg_step`, `:393-425` L4 v0.5 split.)
```

```edit:book/src/L2/krylov-step.md
[old]: - `book/src/spec/slices/cg.md:208-220`, `:430-446` (CG `cg_solve` calling `iterate_while` / `iterate_while_with_prev`).
[new]: - CG `cg_solve` calling `iterate_while` / `iterate_while_with_prev` — the v0.5 driver remains live in the reduced slice at `book/src/spec/slices/cg.md:86-106`; the L0 outer composition is `BaseKspSolver::Mult` at `ksp.cpp:296-310` wrapping the inner CG for-loop `iterative.cpp:427-464` (recognised at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-patterns A/B). (Original pre-reduction slice ranges: `cg.md:208-220`, `:430-446`.)
```

```edit:book/src/L2/krylov-step.md
[old]: - Per cg.md:288, gmres.md:128, and `book/src/L1/chebyshev-smoother.md:260` (no dedicated unit test under `reference/palace/test/unit/`; behaviour exercised only through multigrid integration): no direct unit tests on CG / GMRES / Chebyshev step kernels (integration tests only) — coverage gap inherited from the rough-in; not introduced by this firm-up.
[new]: - Per the `CheckDot` site `reference/palace/palace/linalg/iterative.cpp:21-32` (the CG SPD-guard; no dedicated unit test references `CgSolver`/`PCG` — CG is exercised only via integration tests at `test/examples/`, per `book/src/L1-L0/ksp-solve-mutation-rotation.md`'s coverage note), gmres.md:128, and `book/src/L1/chebyshev-smoother.md:260` (no dedicated unit test under `reference/palace/test/unit/`; behaviour exercised only through multigrid integration): no direct unit tests on CG / GMRES / Chebyshev step kernels (integration tests only) — coverage gap inherited from the rough-in; not introduced by this firm-up. (Original pre-reduction slice range: `cg.md:288`.)
```

```edit:book/src/L2/krylov-step.md
[old]: - `reference/palace/palace/linalg/iterative.cpp:244-250` — `CheckDot` partial-function guard.
[new]: - `reference/palace/palace/linalg/iterative.cpp:21-32` — `CheckDot` partial-function guard (real overload at :22, complex overload at :28; the `MFEM_ASSERT(std::isfinite(dot) && dot >= 0.0, ...)` guard; called for CG at :396, :410, :445, :461). The previously-cited `:244-250` is the `ApplyB` preconditioner-apply helper, not `CheckDot` — same drifted-citation correction applied at §Semantics breakdown (the kernel's `breakdown_token` slot), verified by direct L0 read this dispatch.
```

## Discipline notes

**Sweep convention.** This dispatch applies the cycle-009/010 corpus-reduction re-anchoring convention already codified in the firm `book/src/L3/krylov-step.md` §Evidence (lines 196, 204): when a slice is reduced and a pointer dangles, point it at the **terminal firm home** (firm L0 source range or firm layered entry), preserve the original pre-reduction range parenthetically (auditability — a reader can confirm the lift against git history), and cite the **live retained slice material** (`cg.md:27-141` v0.5 unrolling; `cg.md:86-106` / `:39-106` for the `cg_solve` driver / v0.4-v0.5 forms; `cg.md:120-133` for the `forget_beta_prev` projection) where it still holds. No structural / decomposition / signature edits — the five-primitive-group decomposition, the six variant axes, the three algebraic laws, the `firm` status are all unchanged. The L2 entry's narrative direction stays high→low (LHS = L2 `krylov-step`; the cited evidence is the L0 / firm-layered substrate it composes from).

**Bounded prose-correction (1, recorded per `lifter-scope-content-correction-boundary`).** §Semantics line 67 cited `CheckDot` at `iterative.cpp:244-250`. Direct L0 read (codemap `read_range`) shows `iterative.cpp:243-250` is the **`ApplyB` preconditioner-apply helper** (`BlockTimer bt(Timer::KSP_PRECONDITIONER, ...); B->Mult(x, y);`), **not** `CheckDot`. `CheckDot` is the `MFEM_ASSERT(std::isfinite(dot) && dot >= 0.0, ...)` partial-function guard at `iterative.cpp:21-32` (real overload :22, complex :28; called at :396, :410, :445, :461) — exactly the "partial-functioned on finiteness and positivity" the L2 prose describes. The firm `ksp-solve-mutation-rotation.md` (Sub-pattern B recognition note line 251; Verified-against row line 785) and the firm `L3/krylov-step.md` (line 190) both independently anchor `CheckDot` at `iterative.cpp:21-32`/`:22-32`. The L2 file's `:244-250` is a drifted citation (it names the wrong helper); corrected to `:21-32`. This is bounded (fixing a drifted citation, not re-architecting) and L0-evidenced (read this dispatch). The companion `cg.md:288` (also CheckDot at §Evidence line 172) is re-anchored to the same terminal `iterative.cpp:21-32`.

**Self-verification (per `producer-citation-drift-verify-not-self-invoked`; verify-citation-range "Producer self-verification before emitting citations").** Every emitted re-anchor target verified against source this dispatch:
- `iterative.cpp:21-32` — `CheckDot` real/complex overloads (codemap `read_range` + `search_text` confirm the two `inline void CheckDot` definitions at :22 and :28, the `isfinite && >= 0.0` guard, and the four CG call sites :396/:410/:445/:461). TERMINAL L0.
- `iterative.cpp:243-250` — `ApplyB` (confirmed NOT CheckDot; basis for the prose-correction). 
- `iterative.cpp:427-464` — CG inner for-loop: one `A->Mult(p, z)` at :443, `Dot` at :444/:461, `x.Add`/`r.Add` axpy at :448-449, `ApplyB`/`z=r` preconditioner branch, `CheckDot` at :445/:461. TERMINAL L0.
- `iterative.cpp:434-441` — the `if (!it) { p = z; } else { AXPBY(...beta/beta_prev...); }` first-iteration branch. TERMINAL L0.
- `iterative.cpp:377-386` — CG initial-guess / preconditioner threading (read via `ksp-solve-mutation-rotation.md` Sub-pattern B + `L1/ksp_solve.md`). TERMINAL L0.
- `ksp-solve-mutation-rotation.md` Sub-pattern B — read in full; it is the firm CG L0 terminal home (`iterative.cpp:360-486` + per-step ranges). TERMINAL firm entry.
- `concepts/sequential-obstruction.md`, `concepts/derived-view-hoisting.md` §"Worked example: CG residual norm", `concepts/first-iteration-unrolling.md` — all read; each authoritatively holds the lifted CG material. TERMINAL firm entries.
- Live slice ranges `cg.md:27-141`, `:86-106`, `:39-106`, `:120-133` — confirmed against the 165-line reduced stub: lines 27-141 are the "L4 v0.5 — first-iteration unrolling" section, :86-106 are the `cg_solve` definition, :120-133 are §"Equivalence to v0.4" (the `forget_beta_prev` projection at :129) + §"Variant: pcg under v0.5". TERMINAL (these are the actual retained-material lines, not relocated-dangles). **No re-anchor points at another dangling pointer** — every destination is either firm-layered, firm-L0, or live retained-slice material.

**Cross-check against cycle-015 L3 sweep failure mode.** The dispatch scope warned that cycle-015's L3 sweep pointed 2 re-anchors at relocated-dangle targets. The firm L3 entry (lines 196, 204) terminates the CG step-body / driver evidence at `L2/krylov-step.md:138`/`:146` — i.e., L2 is the terminus from L3's perspective. For L2's *own* outbound pointers (this sweep) the terminus is therefore one layer further down: the L0 source (`iterative.cpp` via `ksp-solve-mutation-rotation.md`) and the firm concept pages, plus the live retained-slice material for the v0.5 unrolling (which has no firmer home — it is the canonical methodology evidence for `concepts/first-iteration-unrolling.md`, per the stub header line 16). The L2 §Evidence rows (138/146) now resolve downward rather than re-citing the reduced slice's dead ranges, closing the loop the cycle-015 L3 sweep left pointing at L2.

## Supporting evidence

- `book/src/L3/krylov-step.md` §Evidence lines 188-206 — the cycle-009/010 terminal-home convention this sweep mirrors (the same CG dangling cohort, resolved one layer up; this sweep resolves L2's copies one layer down).
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B (lines 159-295) + Verified-against (lines 745-789) — firm CG L0 terminal home; CheckDot at `iterative.cpp:21-32`, inner loop at `:427-464`, initial-guess threading at `:377-386`.
- `book/src/concepts/{sequential-obstruction,derived-view-hoisting,first-iteration-unrolling}.md` — firm terminal homes for the lifted CG sequential-obstruction / residual-norm-hoisting / first-iteration-unrolling material.
- `book/src/spec/slices/cg.md` (reduced 165-line stub; header lines 5-16 map each former section to its firm superseding home; live v0.5 material at lines 27-141).
- L0 self-verify reads this dispatch: `reference/palace/palace/linalg/iterative.cpp:21-32` (CheckDot), `:243-250` (ApplyB — drift basis), `:427-464` (CG inner loop), `:434-441` (first-iteration branch).
- Prior-art commit `30119eb` (cycle-010 integrator-finalize) — the corpus reduction that reduced `cg.md` and stranded these pointers.

## Open questions / caveats

- **Scope-statement assumption corrected (no action needed).** The dispatch framing said the `cg.md` Phase-1 slice "was removed". It was **not removed** — it was **reduced to a 165-line stub** at cycle-010 (the `chebyshev.md` slice was the one removed, at cycles 010/014/015). The dangling-pointer symptom is identical either way (the cited ranges no longer resolve to their claimed content), and the re-anchor targets are unchanged. Noting for the record so the integrator does not expect a removed file.
- **The L2 §Evidence rows (138/146) intentionally retain the live-slice citation `cg.md:27-141` / `:86-106`.** This is NOT a dangling pointer — it is the live retained v0.5 / `cg_solve`-driver material, which per the stub header (line 16) is the canonical methodology evidence for `concepts/first-iteration-unrolling.md` and has no firmer home. If a future cycle fully removes the `cg.md` stub (lifting the v0.5 derivation into `concepts/first-iteration-unrolling.md` proper), these two citations will need a follow-on re-point to the concept page. Flagged for the eventual slice-removal audit; not actionable now (the slice is still live).
- **No abstractor reread needed.** All re-anchors are pure citation refinement to terminal firm homes already established by the firm L3 entry, the firm L1>L0 theme, and the firm concept pages; the firmed-up vocabulary does not change the L2 entry's LHS shape, decomposition, laws, variant axes, or status. The one prose-correction (CheckDot citation drift) is bounded and L0-evidenced.
