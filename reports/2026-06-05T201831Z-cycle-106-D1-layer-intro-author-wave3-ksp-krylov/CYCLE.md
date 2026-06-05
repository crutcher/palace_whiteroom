---
agent: layer-intro-author
invoked_at: 2026-06-05T201831Z
scope: WAVE-3 op-chapter typed-edge migration — the coupled solve-kernel pair L4/ksp_solve + L4/krylov-step
status: integrated
integrated_at: 2026-06-05T223000Z
integration_commit: 7592988
integration_notes: "cycle-106 D1 (THE LEAD), applied clean. L4/ksp_solve migrated to typed edges + L4/krylov-step edges authored from scratch → krylov-step root-reachable, 5 records rescued (sim-state/krylov/step-outputs/prev-carry/solve-result), detritus 163→156. Build EXIT 0; rank_violations 0; reachable 36→88 (with D2-D5). OQ krylov-step-pair-wave3-deferred-edges promoted. Pre-existing ksp_solve variant_axes mid-scalar-colon strict-YAML artifact retained verbatim (not introduced this cycle, non-blocking)."
---

# CYCLE: WAVE-3 op-chapter typed-edge migration (ksp_solve + krylov-step)

## Summary

Cycle-106 D1, the LEAD: §(f) WAVE-3 op-chapter `uses-record` typed-edge migration for the
**coupled solve-kernel pair** `book/src/L4/ksp_solve.md` + `book/src/L4/krylov-step.md`.

Two frontmatter-only edits (no prose / operator-semantics change):

1. **`L4/ksp_solve.md`** — migrated off the pre-scheme `consumes:` / `lowers_to:`
   (`variant_axes:` kept) into a typed scheme `edges:` block. Preserves its real `depends-on`
   edges — **including the load-bearing `depends-on` → `L4/krylov-step`** (the 18 body refs;
   this edge is what rescues `krylov-step` from GC-garbage, since `ksp_solve` is already
   root-reachable). Adds `uses-record` `depends-on` → `concepts/op-params`, `concepts/sim-state`.
   The former `consumes:` index entry (`L4/index`) + the non-node concept narrative-pointers
   become `reference` edges.
2. **`L4/krylov-step.md`** — had **NO frontmatter at all** (line 1 = `# krylov-step`). Authored
   its `edges:` block FROM SCRATCH: `uses-record` `depends-on` → `concepts/op-params`,
   `concepts/krylov`, `concepts/sim-state`, `concepts/step-outputs`, `concepts/prev-carry`,
   `concepts/solve-result` (the six §(f) records), plus its real `depends-on` lowers-to edge to
   `L2/krylov-step` and the non-node concept `reference` see-alsos.

Both chapters typed `rank: firm` (their on-disk `## Status` lines read `firm`). All six records
are already `rank: firm` resting on firm L0 cites, so **well-foundedness holds firm/firm** — the
rank linter holds at **0 violations**.

**The rescue is MEASURABLE** (linter re-run against a scratch copy of `book/src`, results below):
`L4/krylov-step` is now root-reachable via `ksp_solve`, and 5 of the 6 records gain inbound
edges and leave the detritus set (`dofset` correctly stays garbage — it is rescued by the
out-of-scope `L4/eliminate_bc` migration, a sibling WAVE-3 tranche). Detritus **163 → 156**
(7 nodes rescued: `L4/krylov-step`, `L4/iterate-while`, and 5 records); rank violations held 0.

## Proposed changes

### Edit 1 — `book/src/L4/ksp_solve.md` frontmatter (migrate `consumes:`/`lowers_to:` → typed `edges:`)

```edit:book/src/L4/ksp_solve.md
[old]:
---
layer: L4
operator: ksp_solve
firmness: firm
consumes:
  - book/src/L4/index.md (solve_loop / restart_cycle / Outcome — the firm c047 outer-driver vocabulary rows)
  - book/src/concepts/solve-monad.md (Solve = StateT SimState Identity; §Shape, §"Termination as a sum type")
lowers_to:
  - book/src/L3/ksp_solve.md (the value-threaded outer-driver fold; theme L4-L3/ksp-solve-driver-dissolution pending — D3's job, NOT this entry's)
variant_axes:
  - outcome-classification (Done True converged / Done False exhausted-max_it / Continue restart-warranted — the 3-arm Outcome sum)
  - restart-shape (non-restarted: solve_loop recurses one_cycle / restarted: solve_loop recurses restart_cycle — selects the per-cycle driver, not the loop algebra)
  - element-type (real / complex — absorbed into OpParams; the Solve threading is element-uniform)
  - convergence-failure-policy (soft-fail; the Bool inside Done — Palace's only variant)
---
[new]:
---
layer: L4
operator: ksp_solve
firmness: firm
rank: firm
edges:
  depends-on:
    - target: L4/krylov-step
      kind: folds                     # the inner per-step fold body restart_cycle runs (18 body refs); the canonical L4 kernel/driver pair. Load-bearing: this depends-on edge makes krylov-step root-reachable via the root-reachable ksp_solve.
    - target: L4/iterate-while
      kind: folds                     # the inner kernel-fold combinator restart_cycle invokes (and solve_loop's outer tail-recursion degenerates to per Law 2)
    - target: L3/ksp_solve
      kind: lowers-to                 # the firm L3 value-threaded outer-driver fold this cap lowers to (lowering edge = depends-on on both endpoints, scheme §5)
    - target: concepts/op-params
      kind: uses-record               # OpParams readonly operator-internal config record named in the signature (ksp_solve :: OpParams -> Inputs -> SimState); see §Signature shape contract
    - target: concepts/sim-state
      kind: uses-record               # SimState the Solve = StateT SimState Identity persistent-state record discharged by execState; the cap's net effect is the SimState transition; see §Signature
  reference:
    - L4/index                        # navigational container: the L4 Part overview anchoring the firm c047 solve_loop / restart_cycle / Outcome outer-driver vocabulary rows (was a consumes: entry; an index is a navigational container → reference, scheme §2)
    - concepts/solve-monad            # the Solve = StateT SimState Identity outer-driver pattern this cap realises (non-node narrative-pointer concept page → reference)
    - concepts/state-stratification   # the three-stratum SimState / OpParams / Krylov typing
    - concepts/convergence-test       # the stopping-predicate surface the Outcome classification reads
    - concepts/derived-view-hoisting  # §3.8 demand-pruning governing the trajectory-vs-classifier demand split
    - concepts/variant-absorption     # the body-variant absorption + readonly OpParams typing
    - concepts/sequential-obstruction # the outer-loop obstruction the cap carries at the coordination layer
    - concepts/constructed-operators  # the preconditioner-side absorption into op.T
variant_axes:
  - outcome-classification (Done True converged / Done False exhausted-max_it / Continue restart-warranted — the 3-arm Outcome sum)
  - restart-shape (non-restarted: solve_loop recurses one_cycle / restarted: solve_loop recurses restart_cycle — selects the per-cycle driver, not the loop algebra)
  - element-type (real / complex — absorbed into OpParams; the Solve threading is element-uniform)
  - convergence-failure-policy (soft-fail; the Bool inside Done — Palace's only variant)
---
```

### Edit 2 — `book/src/L4/krylov-step.md` — author the `edges:` block FROM SCRATCH (prepend before the `# krylov-step` H1)

```edit:book/src/L4/krylov-step.md
[old]:
# krylov-step

Typed-wrapper step kernel for iterative Krylov-shaped solvers
[new]:
---
layer: L4
operator: krylov-step
firmness: firm
rank: firm
edges:
  depends-on:
    - target: L2/krylov-step
      kind: lowers-to                 # the firm L2 primitive-composition row this L4 typed-wrapper lowers to (via the L4>L3>L2 chain); lowering edge = depends-on on both endpoints (scheme §5)
    - target: concepts/op-params
      kind: uses-record               # OpParams readonly operator-internal config record in the kernel signature (krylov-step :: OpParams -> Krylov -> (SimState -> Solve {...})); see §Signature shape contract
    - target: concepts/krylov
      kind: uses-record               # Krylov the solve-local ephemeral bundle threaded as a plain value through the kernel; born at restart entry, discarded at restart exit; §Signature
    - target: concepts/sim-state
      kind: uses-record               # SimState the Solve = StateT SimState Identity persistent-state record; the kernel's sole monadic effect is the SimState.it counter increment; §Signature
    - target: concepts/step-outputs
      kind: uses-record               # StepOutputs the demand-prunable per-step readout record (residual norm / LS residual / breakdown token) returned as the monadic action's value; §Signature result record
    - target: concepts/prev-carry
      kind: uses-record               # PrevCarry the Form-B closure-threaded recurrence carry the first-iteration-unrolling rotation moves out of the steady-state schema; §Signature (Form B only)
    - target: concepts/solve-result
      kind: uses-record               # SolveResult the terminal solve-readout record shape the kernel's per-step SimState transition accumulates toward (the four-field readout the outer driver discharges); §Signature
  reference:
    - L2/krylov-step                  # the L2 companion entry naming the underlying primitive composition (sibling cross-link; the depends-on lowers-to edge above is the blocking dependency)
    - concepts/state-stratification   # the three-stratum SimState / OpParams / Krylov typing
    - concepts/solve-monad            # the Solve = StateT SimState Identity outer driver that consumes this kernel as its fold body
    - concepts/first-iteration-unrolling # the rotation supplying Form B's (first_step, steady_step) split
    - concepts/derived-view-hoisting  # the demand-pruning algebra underwriting Law 1
    - concepts/convergence-test       # the stopping-predicate surface consumed by the outer iterate_while driver (referenced for the placement discipline)
    - concepts/variant-absorption     # the absorption discipline making the six variant axes structural via the OpParams readonly typing
    - concepts/sequential-obstruction # the L3-edge classification recording why the L3>L2 step lowering is plausibly identity-in-form
---

# krylov-step

Typed-wrapper step kernel for iterative Krylov-shaped solvers
```

## Supporting evidence

### Edge classification rationale (scheme §2 / §(e) / §(f))

**`L4/ksp_solve` `depends-on` (blocking; constrains rank + carries liveness):**
- `L4/krylov-step` (`folds`) — the §(f) load-bearing rescue edge. `ksp_solve`'s body references
  `krylov-step` 18× (the inner per-step fold body `restart_cycle` runs inside the
  `iterate-while`-family fold; §Semantics phase 2, §Dependencies "L4 row dependencies",
  §Signature shape-3, the kernel/driver pairing throughout). Was already an authoritative
  in-prose dependency; now a typed `depends-on`.
- `L4/iterate-while` (`folds`) — the inner kernel-fold combinator `restart_cycle` invokes and
  that, by Law 2, `solve_loop`'s outer tail-recursion degenerates to (§Dependencies, §Algebraic
  laws Law 2).
- `L3/ksp_solve` (`lowers-to`) — preserved from the old `lowers_to:`; the lowering edge is a
  `depends-on` on both endpoints (scheme §5).
- `concepts/op-params`, `concepts/sim-state` (`uses-record`) — the §(f) record additions, both
  named in the cap's signature `ksp_solve :: OpParams -> Inputs -> SimState` /
  `Solve = StateT SimState Identity` (§Signature shape contract).

**`L4/ksp_solve` `reference` (navigational; no liveness):**
- `L4/index` — a **navigational container** (scheme §2/§5); the former `consumes:` entry that
  anchored the firm c047 outer-driver vocabulary rows. An edge to an index is `reference`, never
  `depends-on`.
- `concepts/solve-monad` + the six other concept see-alsos (`state-stratification`,
  `convergence-test`, `derived-view-hoisting`, `variant-absorption`, `sequential-obstruction`,
  `constructed-operators`) — **non-node narrative-pointer concept pages** (no rank / no edges
  frontmatter today); edges to them are `reference` (a non-node carries no liveness, scheme §5).

**`L4/krylov-step` `depends-on`:**
- `L2/krylov-step` (`lowers-to`) — the firm L2 primitive-composition row this L4 typed-wrapper
  lowers to via the L4>L3>L2 chain (§Lowers to, §Dependencies "L2 dependencies"); the lowering
  edge is `depends-on` on both endpoints (scheme §5).
- `concepts/{op-params, krylov, sim-state, step-outputs, prev-carry, solve-result}`
  (`uses-record`) — the six §(f) records, every one named in the kernel signature / shape
  contract (§Signature: `OpParams`, `Krylov`, `SimState`, the result record
  `{ sim, krylov, outputs }` carrying `StepOutputs`, Form-B `PrevCarry`; `SolveResult` is the
  terminal solve-readout shape the per-step `SimState` transition accumulates toward).

**`L4/krylov-step` `reference`:** the L2 companion sibling cross-link (the blocking dependency is
the `depends-on lowers-to` edge above; the bare `L2/krylov-step` in `reference` is the
navigational see-also the prose carries) + the eight non-node concept narrative-pointers.

### Linter verification (scratch copy of `book/src` — edits applied, linter re-run, copy deleted)

Both edits were applied to a throwaway copy of `book/src` (NOT to `book/`), the linter re-run,
then the copy deleted — to keep this a pure DISPATCH-phase report (no `book/` mutation).

Invocation: `python3 tools/graded-stack-lint/graded_stack_lint.py [--book-src <copy>] [--show-inbound]`

**Aggregate (before → after):**
```
BEFORE: RESULT: 0 rank violation(s), 163 detritus node(s), 77 untyped (warning).
AFTER:  RESULT: 0 rank violation(s), 156 detritus node(s), 77 untyped (warning).
```
- **Rank violations held at 0** (firm/firm: both chapters `rank: firm`, every `depends-on` record
  target `rank: firm`; the `L4/iterate-while` + `L2/krylov-step` targets are `firm`-per-`## Status`
  but untyped, so the rank-check skips them — no violation, scheme-conformant incremental).
- **Detritus 163 → 156** = **7 nodes rescued**: `L4/krylov-step`, `L4/iterate-while`, and the 5
  records `concepts/{sim-state, krylov, step-outputs, prev-carry, solve-result}`.
- The untyped-set delta was **purely removals, zero additions** (verified by diffing the
  `--show-untyped` lists) — the edits introduced no new untyped/garbage files and cleanly
  resolved the targeted nodes. (The summary's `77` line is a separate aggregate that did not move
  in scope; `L4/krylov-step` did leave the untyped set, `L4/ksp_solve` was already typed via the
  old `consumes:`.)

**`--show-inbound` (the rescue, MEASURABLE) — AFTER:**
```
  L4/krylov-step  <-  L3/krylov-step, L4/ksp_solve
  L4/ksp_solve  <-  L4-L3/solve-family-map-dissolution, L4/frequency_sweep, L4/preconditioning-framework, L4/solve_family, feature/driven.L4, feature/electrostatic.L4, feature/magnetostatic.L4
  concepts/krylov  <-  L4/krylov-step
  concepts/op-params  <-  L4/krylov-step, L4/ksp_solve, feature/transient.L4
  concepts/prev-carry  <-  L4/krylov-step
  concepts/sim-state  <-  L4/krylov-step, L4/ksp_solve
  concepts/solve-result  <-  L4/krylov-step
  concepts/step-outputs  <-  L4/krylov-step
```
- `L4/krylov-step` now carries inbound `← L4/ksp_solve` — and since `L4/ksp_solve` is itself
  root-reachable (`← feature/driven.L4`, `feature/electrostatic.L4`, `feature/magnetostatic.L4`,
  …), `krylov-step` is now **root-reachable** (no longer in the detritus set).
- All six records named in the two `edges:` blocks gain inbound edges; the 5 in krylov-step's
  set (`sim-state`, `krylov`, `step-outputs`, `prev-carry`, `solve-result`) leave detritus;
  `op-params` was already live (it kept its `feature/transient.L4` inbound) and gains two more.

**BEFORE `--show-inbound` (baseline, for contrast):**
```
    [garbage?] L4/krylov-step          (only inbound was L3/krylov-step, itself garbage)
    [garbage?] concepts/sim-state / krylov / step-outputs / prev-carry / solve-result / dofset
```

## Open questions / caveats

- **`concepts/dofset` remains GC-garbage — correctly, and OUT OF MY SCOPE.** `dofset` is reached
  only via `L4/eliminate_bc`'s `uses-record` edge (`L4/eliminate_bc → dofset`, per §(f)), which is
  a **different WAVE-3 op chapter** not in this dispatch's pair. It is rescued by the
  `eliminate_bc` migration tranche (`solve_family` / `fold_solve` / `eliminate_bc` are the other
  §(f) op chapters); confirmed still garbage after my edits, as expected. No action from D1.
- **`L4/iterate-while` and `L2/krylov-step` are `firm`-per-`## Status` but carry no `rank:`
  frontmatter** (untyped). My `depends-on` edges to them are scheme-conformant (the rank-check
  treats an untyped dep as warn-not-fail; reachability still traverses the edge — which is why
  `L4/iterate-while` was also rescued from detritus as a bonus). Typing those two chapters is a
  separate WAVE / lazy-convergence item, not this dispatch's scope.
- **The eight non-node concept pages I `reference` (`solve-monad`, `state-stratification`,
  `convergence-test`, `derived-view-hoisting`, `variant-absorption`, `sequential-obstruction`,
  `constructed-operators`, `first-iteration-unrolling`) carry no `edges: reference:`-only
  frontmatter yet** — they acquire the unified non-node encoding (scheme §5) as they are next
  touched (lazy convergence; the linter is invariant meanwhile). Not in scope here.
- No operator-semantics / prose change was made to either chapter beyond the frontmatter
  `edges:` block — the migration is frontmatter-only, as §(f) requires. The `variant_axes:` block
  on `ksp_solve` was retained verbatim (it is the human-facing variant catalogue, orthogonal to
  the typed-edge scheme).
