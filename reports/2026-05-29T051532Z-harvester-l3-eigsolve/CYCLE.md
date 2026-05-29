---
agent: harvester
invoked_at: 2026-05-29T051532Z
scope: L3 operator: eigsolve (kernel+driver backfill — CONDITIONAL, anchor-check-first)
status: integrated
integrated_at: 2026-05-29T06:14:03Z
integration_commit: 881f200
integration_notes: "cycle-021 finalize (staging row #8; BLOCKED-inventory, Build-relevant:no, NO book changes). The L3 eigsolve backfill is BLOCKED on missing L1-firm + L2-entry anchors; the linear-EVP (SLEPc-EPS/ARPACK-EPS) has no Palace-authored kernel/driver pair (predicted sequential/partial-obstruction, the trsv-style outcome). NO L3 eigsolve stub materialized (honored META §Suggested resolution; clearly-implied bar NOT met — blocked-pending-prerequisites ≠ clearly-implied-ready; a stub would have no lowers_to target + would lift unconfirmed laws). 2 OQs promoted: the strict prerequisite chain (L1 eigsolve rough-in→firm → L2 eigsolve entry → L3 backfill) + the linear-EVP-no-krylov-step-kernel-analog structural prediction. ROUTED to the batch-5 meta-phase: reframe plan item #9 from 'next L3 inventory backfill' → 'blocked-pending-L1-firm+L2-entry' (priorities.md is meta/cycle-planner co-owned; not edited here). Linear-EVP scope kept distinct from the nonlinear-EVP NLEPS sibling dispatch. retroactive-budget 0; no rebuild needed on account of this report."
decision: BLOCKED (anchors insufficient) — inventory observation, no L3 backfill
inputs:
  - book/src/L1/eigsolve.md (L1 anchor — status `rough-in`, NOT firm)
  - book/src/L1/index.md:71 (L1 dep-map row: eigsolve `rough-in (test-coverage-bounded)`)
  - book/src/L2/index.md (L2 dep-map — NO eigsolve entry, not even a stub)
  - book/src/L1-L0/eigsolve-mutation-rotation.md (cycle-012 firm; the only firm eigsolve artifact below L3)
  - book/src/L3/ksp_solve.md (cycle-020 precedent — the kernel+driver split this dispatch was asked to mirror)
  - book/src/L3/krylov-step.md (cycle-010 firm L3 kernel — the krylov-step half of the ksp_solve pair)
  - book/src/L3/index.md (L3 dep-map + Context — negative L3 results are part of the deliverable)
  - scaffolding/open-questions.md:352 (the cycle-020 ksp_solve harvester's own "check L1/L2 firmness first" caveat)
  - palace/linalg/arpack.cpp:263-360, :513-590 (ARPACK RCI driver + ApplyOp kernel — self-verified)
  - palace/linalg/slepc.cpp:687-716 (SLEPc opaque EPSSolve driver — self-verified)
---

# CYCLE: Formalize eigsolve at L3 — DECISION: BLOCKED (prerequisite-surface inventory)

## Summary

This dispatch was scoped to **conditionally** backfill the L3 `eigsolve` entry as a kernel+driver
pair (mirroring the cycle-020 `krylov-step`/`ksp_solve` split) — but **only after checking the
L1/L2 eigsolve anchor firmness first**, with the explicit instruction to produce an inventory
observation rather than force an unanchored entry if the anchors are missing. The anchor-check is
**decisive and negative**: the anchors are insufficient on three independent grounds, so I produce
the **blocked-inventory observation** (the trsv-style "blocked, surface the prerequisite" outcome).

The eigsolve L3 backfill is **not the next actionable L3 inventory item**. The prerequisite chain is:
**(1) promote L1 `eigsolve` rough-in → firm, (2) author an L2 `eigsolve` entry (driver/kernel framing),
THEN (3) backfill L3.** Forcing an L3 entry now would lift unconfirmed algebraic-law confidence from a
rough-in L1 form into a brand-new layer and invent an L2 `lowers_to` target that does not exist —
both violations of the methodology. I emit no proposed-changes blocks for `book/`; the deliverable is
this observation + the precise prerequisite chain + two OQ appends below.

## Anchor-check findings

### Finding 1 — L1 `eigsolve` is `rough-in`, NOT firm

`book/src/L1/eigsolve.md:166` carries `status: rough-in (test-coverage-bounded, cycle-009; …)`. The
L1 dep-map row confirms (`book/src/L1/index.md:71`):

> `eigsolve` … `rough-in (test-coverage-bounded, harvested-by: harvester:2026-05-27T191929Z-harvester-eigsolve-L1)`

The L1 entry itself states the law-confidence caveat (`book/src/L1/eigsolve.md:100`):

> **Rough-in status caveat**: the laws below are stated at the level of confidence supported by
> direct source reading + literature anchors … Critic / lifter / lowering-verifier dispatches on this
> entry should treat all laws as `unconfirmed`.

Promotion to firm is gated (`book/src/L1/eigsolve.md:168-169`) on either (a) a dedicated
`test-eigensolver.cpp`, or (b) a future harvester adding literature-anchored evidence at
`ksp_solve`-equivalent confidence. **Neither has landed.** The only dedicated witness remains the
narrow `test-boundarymodeoperator.cpp` (three linear-EPS `LARGEST_REAL`-only cases —
`book/src/L1/eigsolve.md:216`).

**Contrast with the ksp_solve precedent:** the cycle-020 L3 `ksp_solve` backfill lifted from a
**firm** L1 `ksp_solve` (`book/src/L3/ksp_solve.md:7` `lifts_from: book/src/L1/ksp_solve.md`; that
L1 entry is firm). The L3 entry's trajectory-terminal algebraic laws are explicitly "inherited from
the L1 fixed-point laws" (`book/src/L3/ksp_solve.md:108`). Inheriting laws from a rough-in L1 form
whose laws are flagged `unconfirmed` would propagate that unconfirmed status into a new L3 layer —
the layer-coherence backfill would be coherent-but-unconfirmed, defeating the purpose.

### Finding 2 — L2 `eigsolve` does NOT exist (no entry, not even a stub)

`book/src/L2/index.md` dep-map (rows at `:47-53`) and the L2 directory listing both confirm: the L2
firm cohort is `krylov-step`, `chebyshev-iteration`, `linear_combination`, `inner_product`,
`orthogonalize`; the L2 stubs are `incremental-least-squares` and `ksp_solve`. **There is no
`eigsolve` L2 row and no `book/src/L2/eigsolve.md` file.** The two grep hits for "eigen" in L2 are
incidental (`linear_combination.md:107` mentions "eigenvector synthesis"; `orthogonalize.md:14`
mentions "eigenmode-ROM basis-extension") — neither is an eigsolve operator entry.

**Contrast with the ksp_solve precedent:** the cycle-020 L3 `ksp_solve` had a concrete (if `stub`)
L2 `lowers_to` target — `book/src/L3/ksp_solve.md:6` declares
`lowers_to: book/src/L2/ksp_solve.md (… L2 anchor still stub; NOT identity-in-form)`, and the L2
`ksp_solve` stub was materialized 2026-05-28 (`book/src/L2/index.md:53`). An L3 `eigsolve` entry
would have **no L2 `lowers_to` target to point at** — the high→low discipline requires the L3 entry
to record its lowering direction, and there is nothing below it at L2 to lower into.

### Finding 3 — the kernel+driver split does NOT map onto eigsolve's L0 structure

This is the deepest finding and the reason the dispatch-scope's "determine identity-vs-genuine-rotation
like the cycle-020 ksp_solve harvester did" cannot be answered yet: **eigsolve has no Palace-authored
per-step kernel of the `krylov-step` shape.**

The ksp_solve pair works because Palace **authors** the CG/GMRES per-step iterate arithmetic
line-for-line: `krylov-step` (firm L3 kernel) renders Palace's own `α = β/dot(Ap,p)`, `x += α·p`,
`r -= α·Ap` recurrence (`book/src/L3/krylov-step.md`); `ksp_solve` (firm L3 driver) renders Palace's
own `for (; it < max_it && !converged; it++)` loop (`reference/palace/palace/linalg/iterative.cpp:427`).
Both halves are *Palace-authored value-threaded arithmetic*.

Eigsolve has **no analogous Palace-authored loop or kernel**. Self-verified against source this dispatch:

- **SLEPc linear-EVP driver = a single opaque library call.** `SlepcEPSSolverBase::Solve()` is
  `Customize(); EPSSolve(eps); EPSGetConverged(eps, &num_conv); RescaleEigenvectors(num_conv);
  return num_conv;` (`palace/linalg/slepc.cpp:687-709`, verified `:694-695,:707-708`). The **entire**
  Krylov-Schur/Arnoldi iteration — outer loop, restart, convergence test, per-step Arnoldi
  arithmetic — lives **inside SLEPc** (`EPSSolve`). Palace authors **no loop and no kernel**; there is
  nothing at L3 to render as a value-threaded fold or a per-step transition.
- **ARPACK linear-EVP driver = an RCI loop dispatching opaque-library callbacks.**
  `ArpackEigenvalueSolver::SolveInternal` (`palace/linalg/arpack.cpp:263-358`) is a
  `while (true) { naupd(…, ido, …); if (ido==±1) ApplyOp(…); else if (ido==2) ApplyOpB(…);
  else if (ido==99) break; }` reverse-communication loop (verified `:312-340`). The Arnoldi state,
  the per-step three-term recurrence, the restart logic, and the convergence test all live **inside
  `naupd`** (the opaque ARPACK driver). The Palace loop is a **callback dispatcher**, not an
  iterate-update kernel — it carries no `(K, s) -> (K', s')` value-threaded transition.
- **The only Palace-authored per-step body is `ApplyOp` — and it is already firm L3 vocabulary.**
  `ArpackEPSSolver::ApplyOp` (`palace/linalg/arpack.cpp:563-590`, verified) is
  `opK->Mult(x1,z1); opInv->Mult(z1,y1); y1 *= 1/gamma;` (non-sinvert) — i.e. an
  `apply_linop` ▷ `ksp_solve` ▷ scale composition. Every primitive in it is **already a firm L3
  operator** (`book/src/L3/apply_linop.md`, the inner `ksp_solve`/`krylov-step` via the firm L3
  `ksp_solve` cycle-020). `ApplyOp` is **not a new eigen-kernel**; it is a composition of existing
  firm L3 leaves. There is no eigsolve-specific kernel to factor out (unlike `krylov-step`, which is
  genuinely new per-step arithmetic).

**Consequence for the "kernel+driver" scoping:** the cycle-020 ksp_solve harvester's own caveat
(`scaffolding/open-questions.md:352`) anticipated exactly this — "only an eigsolve *kernel* (if one is
factored, analogous to `krylov-step`) would be a clean identity-backfill candidate." The answer is:
**no Palace-authored eigsolve kernel exists to factor.** The eigsolve "driver" is an opaque-library
call (SLEPc) or a callback-dispatcher RCI loop (ARPACK); the eigsolve "step body" (`ApplyOp`) is a
composition of *already-firm* L3 leaves. The kernel+driver decomposition that made ksp_solve a clean
two-entry backfill **has no eigsolve analog** at the current scope.

(Note on the sibling boundary: this finding is about the **linear EVP** — SLEPc-EPS / ARPACK-EPS, the
dispatch's named scope. The nonlinear EVP `QuasiNewtonSolver` (`nleps.cpp`) IS a Palace-authored Newton
outer loop and is the only eigsolve family with a genuinely Palace-authored iteration — but it is the
SIBLING dispatch's scope this cycle, kept distinct here. Even there, the L1 `eigsolve` form absorbs the
three orchestrations into one opaque type, so a Newton-specific L3 kernel/driver would be a *different*
operator question, not the linear-EVP `eigsolve` this dispatch was scoped to.)

### Anchor-firmness summary table

| Anchor | Required for L3 backfill | Actual state | Verdict |
|---|---|---|---|
| L1 `eigsolve` operator | firm (ksp_solve precedent lifts from firm L1) | **`rough-in`** (test-coverage-bounded; laws `unconfirmed`) | INSUFFICIENT |
| L2 `eigsolve` entry | exists (≥ stub, as a `lowers_to` target) | **does not exist** (no row, no file) | MISSING |
| L1>L0 `eigsolve-mutation-rotation` theme | (helpful context) | firm (cycle-012) | present (not sufficient alone) |
| Palace-authored eigsolve kernel (krylov-step analog) | exists, to factor the kernel half | **none** (SLEPc opaque; ARPACK RCI-callback; `ApplyOp` = firm-L3-leaf composition) | NO ANALOG |

Only the L1>L0 mutation-rotation theme is firm — and a lowering theme is **not** an operator anchor:
it lowers the L1 form into L0, it does not establish a firm L1 *operator* nor an L2 entry to lift from
or lower to.

## DECISION: BLOCKED — inventory observation, no L3 entry forced

Per the dispatch's conditional clause ("If anchors are MISSING/insufficient … DO NOT force an
unanchored L3 entry. Instead produce an inventory observation"), and per the cycle-020 ksp_solve
harvester's own gating caveat (`scaffolding/open-questions.md:352`: scope eigsolve as kernel+driver
"**after the L1/L2 eigsolve anchors are checked for firmness**"), the decision is **BLOCKED**.

No `book/` proposed-changes are emitted. Producing an L3 `eigsolve.md` now would:
- lift `unconfirmed` algebraic laws from the rough-in L1 form into a fresh L3 layer (Finding 1);
- declare a `lowers_to` target (`book/src/L2/eigsolve.md`) that does not exist, breaking the high→low
  lowering-direction discipline and producing a dead in-prose reference (Finding 2);
- invent a kernel/driver split with no L0 structural basis — the eigsolve "kernel" would either be a
  re-statement of already-firm L3 leaves (`ApplyOp` = `apply_linop`∘`ksp_solve`) or an empty wrapper
  around an opaque library call (Finding 3).

This is a **valid and valuable result**: it precisely identifies the prerequisite work and prevents a
premature, low-confidence L3 entry that a later cycle would have to rework once the L1 form firms.

## The prerequisite dispatch chain (what must land before L3 eigsolve)

In strict dependency order:

1. **Promote L1 `eigsolve` rough-in → firm.** Gate (per `book/src/L1/eigsolve.md:168-169`): either
   (a) dedicated `test-eigensolver.cpp` coverage exercising linear/quadratic/nonlinear surfaces, **or**
   (b) a harvester invocation adding per-law literature anchors (Higham 2008 scaling;
   Lehoucq–Sorensen ARPACK convergence; Hernandez–Roman–Vidal SLEPc convergence) at
   `ksp_solve`-equivalent confidence. Path (b) is harvester-actionable now; path (a) depends on test
   authorship that is out of this project's write scope. **Route:** `harvester` (literature-anchor pass)
   or `lowering-verifier` (re-evaluate law confidence against `eigsolve-mutation-rotation` evidence).
2. **Author an L2 `eigsolve` entry.** Decide the L2 framing first: is the linear-EVP eigsolve an L2
   *named composition* (the `ApplyOp` shift-invert action `apply_linop ▷ ksp_solve`, which IS factorable
   at L2 as a composition of firm L2 leaves), or an L2 *outer-driver stub* (mirroring the L2 `ksp_solve`
   stub at `book/src/L2/index.md:53`)? The opaque-library reality (Finding 3) suggests the **only**
   genuinely-Palace-authored L2 content for the *linear* EVP is the `ApplyOp` composition — the
   "driver" is opaque (SLEPc `EPSSolve` / ARPACK `naupd`). **Route:** `abstractor` (L2 eigsolve framing
   + L2>L1 theme) or `combinator-miner` (if the `apply_linop ▷ ksp_solve` shift-invert action is a
   recurrent named composition). This step likely produces a **stub** first (per the implied-component
   stub policy) and refines later.
3. **THEN backfill L3 `eigsolve`** — and only after steps 1–2 establish what the L3 entry lifts from
   (firm L1) and lowers to (L2 entry). At that point the kernel/driver question can be answered against
   real anchors: the likely outcome is that the *linear-EVP* eigsolve L3 entry is **NOT** a krylov-step
   analog but a **sequential-obstruction record** ("the eigen-iteration is opaque-library-owned / RCI;
   no Palace-authored value-threaded fold lifts") — a partial-obstruction or obstruction L3 entry, not a
   clean kernel+driver pair. The `QuasiNewtonSolver` (nonlinear) path is the only eigsolve family with a
   Palace-authored loop and is the candidate for a genuine L3 driver — but that is the sibling NLEPS
   scope.

This chain is the eigsolve analog of the trsv outcome (blocked at L1-localization; prerequisite
surfaced rather than a forced L3 entry — `scaffolding/open-questions.md:341-354`,
`book/src/L3/index.md:41` "subsequent L3 cohort growth … `ksp_solve` / `eigsolve` if their rotations
turn out to be near-identity").

## Supporting evidence

Citations self-verified against source this dispatch via `mcp__palace-codemap__read_range`
(per the `verify-citation-range` producer-self-verification discipline):

- `palace/linalg/arpack.cpp:263-358` — `ArpackEigenvalueSolver::SolveInternal`: the RCI
  `while (true) { naupd(…); if (ido==±1) ApplyOp; else if (ido==2) ApplyOpB; else if (ido==99) break; }`
  loop. Verified: `naupd` driver call at `:317-318`; `ApplyOp` dispatch at `:325`; `ApplyOpB` at `:329`;
  `ido==99` break at `:330`; the per-`WhichType` ARPACK-token switch + `MFEM_ABORT` (TARGET_REAL/
  TARGET_IMAGINARY) at `:279-305`. **Evidence that the Arnoldi state lives inside `naupd`, not in a
  Palace-authored kernel.**
- `palace/linalg/arpack.cpp:563-590` — `ArpackEPSSolver::ApplyOp`: the only Palace-authored per-step
  body. `opK->Mult(x1,z1); opInv->Mult(z1,y1); y1 *= 1/gamma;` (non-sinvert, `:572-575`);
  `opM->Mult; opInv->Mult; y1 *= gamma;` (sinvert, `:577-581`); optional `opProj->Mult` (`:584-587`).
  **Evidence that the eigsolve "kernel" is a composition of already-firm L3 leaves
  (`apply_linop` ▷ `ksp_solve`), not a new operator.**
- `palace/linalg/arpack.cpp:513-560` — `ArpackEPSSolver::Solve()`: `CheckParameters` + `ncv`-clamp
  against `N = linalg::GlobalSize(comm, z1)` (`:516-519`); `arpack_it` default `:521-523`; `SolveInternal`
  invocation at `:552`; `RescaleEigenvectors(nev)` at `:555`; `info = 0` reset at `:558`; `return
  num_conv` at `:559`. The Palace outer surface is parameter-setup + one `SolveInternal` call — no
  Palace iteration arithmetic.
- `palace/linalg/slepc.cpp:687-709` — `SlepcEPSSolverBase::Solve()`: `Customize(); EPSSolve(eps);
  EPSGetConverged(eps,&num_conv); … RescaleEigenvectors(num_conv); return (int)num_conv;`. Verified:
  `EPSSolve` at `:694`, `EPSGetConverged` at `:695`, `RescaleEigenvectors` at `:707`, `return` at `:708`.
  **Evidence that the entire SLEPc linear-EVP iteration is one opaque library call — zero
  Palace-authored loop or kernel.**
- `palace/linalg/slepc.cpp:711-716` — `SlepcEPSSolverBase::GetEigenvalue(i)` returns `l * gamma`
  (Higham un-scaling at the accessor). Confirms the result-extraction surface is per-pair accessors,
  not a value-threaded result record.
- `book/src/L1/eigsolve.md:166-169` — L1 `status: rough-in`; promotion gate (test coverage OR
  literature anchors). `:100` — the `unconfirmed`-laws caveat.
- `book/src/L1/index.md:71` — L1 dep-map row confirming `rough-in (test-coverage-bounded)`.
- `book/src/L2/index.md:30-53` — L2 dep-map: firm cohort + two stubs; **no eigsolve row**.
- `book/src/L1-L0/eigsolve-mutation-rotation.md:933-948` — the firm (cycle-012) L1>L0 theme; the only
  firm eigsolve artifact below L3 (a lowering theme, not an operator anchor).
- `book/src/L3/ksp_solve.md:5-19, :108, :167-179` — the cycle-020 precedent: lifts from FIRM L1
  `ksp_solve`; lowers to the L2 `ksp_solve` stub; laws inherited from L1 fixed-point laws. The
  template this dispatch was asked to mirror, and the source of the firm-anchor requirement.
- `book/src/L3/krylov-step.md` (cycle-010 firm) — the L3 kernel half: Palace-authored per-step iterate
  arithmetic. The structural feature eigsolve's linear-EVP path lacks.
- `book/src/L3/index.md:7, :30, :41` — L3 Context ("negative L3 results are part of the deliverable");
  the firm `ksp_solve` row; the Working Note flagging eigsolve L3 growth as gated on whether "their
  rotations turn out to be near-identity."
- `scaffolding/open-questions.md:352` — the cycle-020 ksp_solve harvester's own caveat: scope eigsolve
  as kernel+driver "after the L1/L2 eigsolve anchors are checked for firmness," and "only an eigsolve
  *kernel* (if one is factored, analogous to `krylov-step`) would be a clean identity-backfill candidate."
- `scaffolding/priorities.md:31` — plan item #9 `L3/eigsolve kernel+driver pair L3 backfill`
  (the dispatched item this observation answers as BLOCKED-with-prerequisite-chain).

## Open questions

(Append-only additions to `scaffolding/open-questions.md` — proposed for the integrator to migrate;
NOT applied here.)

- **`l3-eigsolve-blocked-on-l1-firm-and-l2-entry`** (NEW, HIGH-fan-out-blocker) — The L3 `eigsolve`
  kernel+driver backfill (plan #9, `priorities.md:31`) is **BLOCKED** on two missing anchors: L1
  `eigsolve` is `rough-in` (laws `unconfirmed`; `book/src/L1/eigsolve.md:166`) and there is **no** L2
  `eigsolve` entry. Prerequisite chain (strict order): (1) L1 eigsolve rough-in → firm
  (route `harvester` literature-anchor pass or `lowering-verifier` law-confidence re-eval); (2) author
  an L2 `eigsolve` entry — likely the `apply_linop ▷ ksp_solve` shift-invert *named composition*, since
  the linear-EVP "driver" is opaque-library-owned (route `abstractor`/`combinator-miner`); (3) THEN L3
  backfill. *Trigger:* steps 1+2 land. **Recommend the meta-phase reframe plan #9 from "next L3 inventory
  backfill" to "blocked-pending-L1-firm+L2-entry," and keep the `l3-vocabulary-inventory-gap` parent open
  against `eigsolve` (+ still-blocked `trsv`).**

- **`l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog`** (NEW, structural) — Self-verified this
  dispatch: the linear-EVP eigsolve has **no Palace-authored per-step kernel** of the `krylov-step` shape.
  SLEPc-EPS is one opaque `EPSSolve(eps)` call (`palace/linalg/slepc.cpp:694`); ARPACK-EPS is an RCI loop
  dispatching opaque `naupd` callbacks (`palace/linalg/arpack.cpp:317-318`, RCI loop `:312-340`); the only Palace-authored body
  is `ApplyOp` (`arpack.cpp:563-590`), which is an `apply_linop ▷ ksp_solve` composition of **already-firm**
  L3 leaves. **Consequence:** when the L3 eigsolve entry is eventually authored (after the prerequisite
  chain), the *linear-EVP* path is most likely a **sequential-obstruction / partial-obstruction record**
  ("the eigen-iteration is opaque-library-owned; no Palace value-threaded fold lifts"), NOT a clean
  kernel+driver pair like `ksp_solve`. The only eigsolve family with a Palace-authored iteration loop is
  the nonlinear `QuasiNewtonSolver` (`nleps.cpp`) — the sibling NLEPS dispatch's scope. *Trigger:* the L3
  eigsolve dispatch (post-prerequisite); resolves the cycle-020 caveat at `open-questions.md:352` about
  whether an eigsolve kernel is factorable.

## Caveats

- This observation covers the **linear EVP** (SLEPc-EPS / ARPACK-EPS) per the dispatch scope. The
  **nonlinear EVP** (`QuasiNewtonSolver`, `nleps.cpp`) is the sibling cycle-021 dispatch's scope and is
  deliberately kept distinct; it is the only eigsolve family with a Palace-authored Newton outer loop,
  and any L3 driver question there is a separate operator from the linear-EVP `eigsolve` examined here.
- No layer-intro refresh is needed from this dispatch (no `book/` edits). When the L3 eigsolve entry
  eventually lands, `book/src/L3/index.md` §Working Notes and the dep-map will need a row — flagged for
  the eventual post-prerequisite dispatch, not for this one.
- I did not read the full `nleps.cpp` Newton body (sibling scope); the one fact I assert about it (it
  IS a Palace-authored loop, unlike SLEPc/ARPACK) is cross-referenced from the firm L1>L0 theme
  (`book/src/L1-L0/eigsolve-mutation-rotation.md:235-237` cites the `QuasiNewtonSolver::Solve` Newton
  outer loop with `opInv->Mult` at `nleps.cpp:514`) and the L1 entry's §Context (`book/src/L1/eigsolve.md:11`),
  not from a fresh read this dispatch.
