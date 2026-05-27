---
agent: lifter
invoked_at: 2026-05-27T22:05:58Z
scope: L1 eigsolve LinearSolveFailed status — constructive-introduction annotation (resolves cycle-009 OQ eigsolve-linear-solve-failed-status-anchor)
status: integrated
integrated_at: 2026-05-27T230802Z
integration_commit: 30119eb
integration_notes: Applied cleanly via integrator-per-report pass 7 of cycle-010 (wave-2 #7). 5 edits to `book/src/L1/eigsolve.md` + 2 to `scaffolding/open-questions.md` (yaml status flip + prose append). Resolves cycle-009 OQ `eigsolve-linear-solve-failed-status-anchor` via option (b) — keep + annotate `LinearSolveFailed` as L1-constructive with 10 negative-anchor citations (`palace/linalg/ksp.cpp:297-310` `BaseKspSolver::Mult` void return + 4 ARPACK + 1 NLEPS + 5 SLEPc shell-matrix `opInv->Mult` call sites). OQ status flipped `open` → `partially-answered` (`partial_answer_at: cycle-010`); materialising `eigsolve-mutation-rotation` L1>L0 theme deferred to cycle-011+ abstractor. **First systematic use of negative-anchor citations at per-status-variant granularity** — distinguishable from existing per-operator obstruction-theme pattern; forwarded to cycle-012 meta-phase as friction signal at recurrence-1. **OQ-to-resolution latency**: cycle-009 OQ resolved within 1 cycle via the cycle-009 harvester-recommended option (b); strengthens the ≤2-cycle latency pattern. 3 sibling cycle-009 eigsolve OQs remain open (explicit out-of-scope per "one theme per invocation"); cycle-011 candidate cluster.
inputs:
  - book/src/L1/eigsolve.md
  - scaffolding/open-questions.md (entry eigsolve-linear-solve-failed-status-anchor)
  - reference/palace/palace/linalg/arpack.cpp:569-600 (ApplyOp body; opInv->Mult call sites)
  - reference/palace/palace/linalg/slepc.cpp:687-709 (Solve body; EPSConvergedReasonView print-only)
  - reference/palace/palace/linalg/nleps.cpp:500-540 (deflated_solve inner opInv->Mult)
  - reference/palace/palace/linalg/ksp.cpp:295-310 (BaseKspSolver::Mult — Mpi::Warning, void return)
---

# CYCLE: Resolve eigsolve-linear-solve-failed-status-anchor (option (b))

## Summary

This is a small, decisional re-anchor lift on the cycle-009 rough-in L1 `eigsolve` chapter (`book/src/L1/eigsolve.md`). The cycle-009 harvester landed the operator with a four-way `EigStatus = Converged | PartialConverged | MaxIterReached | LinearSolveFailed`. Three of the four cases are directly L0-anchored (`palace/drivers/eigensolver.cpp:367-374`); the fourth — `LinearSolveFailed` — is constructively introduced by the L1 form and has no L0 anchor: at L0, inner `opInv->Mult(...)` calls from ARPACK's `ApplyOp`, SLEPc's shell-matrix callbacks, and `NonLinearEigenvalueSolver::deflated_solve` all invoke `BaseKspSolver<ComplexOperator>::Mult` (`palace/linalg/ksp.cpp:300-307`), which returns `void` and emits only an `Mpi::Warning` on non-convergence — the warning is never bubbled, never queried via `ksp->GetConverged()` at any of the ten eigensolver call sites (4 ARPACK + 1 NLEPS + 5 SLEPc shell-matrix), so the inner failure is silent at the eigensolver outer loop. This dispatch adopts the cycle-009 harvester's recommended option (b): keep the `LinearSolveFailed` case, annotate it explicitly as **constructed by the L1 form**, and defer materialisation to a future `eigsolve-mutation-rotation` L1>L0 theme. The chapter already names the case as "constructively introduced" in Algebraic-laws §3 and §"Laws that explicitly do not hold"; this re-anchor surfaces that prose into a dedicated callout block at the §Signature/§Semantics seam and at the §Status block, so a reader skimming `EigStatus` reaches the constructive-introduction caveat at the same surface depth as the case itself.

The dispatch found one new piece of supporting evidence not currently cited in the chapter: the `ksp.cpp:295-310` `BaseKspSolver::Mult` body explicitly returning `void` with only `Mpi::Warning`, and the `ksp->GetConverged()` query existing-but-never-called from any of the ten `opInv->Mult` eigensolver call sites (`arpack.cpp:574, 580, 761, 778`; `nleps.cpp:514`; SLEPc shell callbacks at `slepc.cpp:1858, 1965, 1978, 2076, 2159`). The annotation cites these as **negative anchors** (proof of the silence).

This is option (b), not (a) or (c). Option (a) (drop the case) would collapse a semantic distinction the L1 form makes deliberate — the L4 monadic-coordination layer downstream of L1 will need to distinguish `LinearSolveFailed` from `MaxIterReached` to route error recovery (the two are caused by different upstream conditions and motivate different caller responses). Option (c) (require L1>L0 lowering to plumb it) is the eventual end-state but is out of scope for this dispatch — the `eigsolve-mutation-rotation` theme is queued for cycle-010+ abstractor; the L0 surface refactor (capturing `opInv->Mult` failure via `ksp->GetConverged()` and propagating) is part of that theme's body. The annotation here is the bridge: it lets the rough-in L1 chapter stand on its current evidence base while making explicit that the case is L1-constructive.

## Proposed changes

### Edit 1: `book/src/L1/eigsolve.md` — Signature block, add post-block constructive-introduction callout

This edit inserts a callout block between the closing fence of the signature-shape code block (source line 45) and the "Shape contract" paragraph that follows (source line 47). Specified as an `[insert-after]` to avoid embedding the source's triple-backtick fence inside the [old]/[new] block (cycle-010 critic flagged the prior non-contiguous form as a mechanical-clarity issue; the insert-after pattern matches Edit 6 below).

```edit:book/src/L1/eigsolve.md
[insert-after: the closing ``` fence of the signature-shape code block at source line 45 (the line immediately following `EigStatus = Converged | PartialConverged | MaxIterReached | LinearSolveFailed`) — i.e., the new callout block goes on what becomes source line 46, displacing the existing blank line to line 47+]
[content]:

> **Note on `EigStatus::LinearSolveFailed` (constructed by the L1 form).** The `LinearSolveFailed` variant has no direct L0 anchor. At L0, each of the ten inner `opInv->Mult(...)` call sites — ARPACK at `palace/linalg/arpack.cpp:574, 580, 761, 778`, NLEPS at `palace/linalg/nleps.cpp:514`, SLEPc shell-matrix callbacks at `palace/linalg/slepc.cpp:1858, 1965, 1978, 2076, 2159` — invokes `BaseKspSolver<ComplexOperator>::Mult` (`palace/linalg/ksp.cpp:297-310`), which has a `void` return and emits only an `Mpi::Warning` on non-convergence. None of the call sites query `ksp->GetConverged()` after the call; the inner-solver failure is silent at the eigensolver outer loop, manifesting downstream as outer non-convergence (typically captured as `MaxIterReached` or `PartialConverged`). The `LinearSolveFailed` variant is **introduced by the L1 form** to make the inner-linear-solve coupling visible at the L1 surface — the L4 monadic-coordination layer downstream needs to distinguish a stuck-inner-solver failure from a true outer-iteration max-iter exhaustion, and the L1 form pre-positions this distinction. A future `eigsolve-mutation-rotation` L1>L0 theme will materialise the variant by plumbing `ksp->GetConverged()` (and its analogues for the SLEPc `EPSConvergedReason` reasons in the `EPS_DIVERGED_BREAKDOWN` / `EPS_DIVERGED_SYMMETRY_LOST` family) from the inner-solver return path through the eigensolver outer loop. Until that theme lands, treat `LinearSolveFailed` as an L1-constructive value that will appear when (and only when) the future lowering plumbs it; current L0 instantiations of `eigsolve` will not produce it.
```

### Edit 2: `book/src/L1/eigsolve.md` — Algebraic-laws §3 `LinearSolveFailed` row, replace rough-in routing prose with resolution pointer

```edit:book/src/L1/eigsolve.md
[old]:   - `LinearSolveFailed` ↔ an inner `opInv->Mult` callback returns a non-converged result. **Note**: at L0 this is not currently a distinct return-code case from `MaxIterReached` — the inner solve's non-convergence (an `Mpi::Warning` from `ksp_solve`'s `palace/linalg/ksp.cpp:301-307`) propagates as continued use of a poorly-converged inverse, which typically manifests as outer-eigensolve non-convergence. The L1 form's `LinearSolveFailed` is a *constructive distinction* that the L1>L0 lowering theme would need to plumb explicitly; in the current Palace source, the `LinearSolveFailed` case is **not directly observable**. This is a rough-in promotion candidate — either drop the case (collapsing to `MaxIterReached`) or carry it forward with an explicit "constructed by the L1 form" annotation. Routes to open question below.
[new]:   - `LinearSolveFailed` ↔ an inner `opInv->Mult` callback returns a non-converged result. **Constructed by the L1 form** — at L0 this is not a distinct return-code case from `MaxIterReached`; the inner solve's non-convergence emits an `Mpi::Warning` from `palace/linalg/ksp.cpp:301-307` but `BaseKspSolver::Mult` returns `void` (`palace/linalg/ksp.cpp:297`), and none of the ten eigensolver-side `opInv->Mult` call sites (4 ARPACK + 1 NLEPS + 5 SLEPc shell-matrix: `arpack.cpp:574, 580, 761, 778`; `nleps.cpp:514`; SLEPc shell callbacks at `slepc.cpp:1858, 1965, 1978, 2076, 2159`) query `ksp->GetConverged()` after the call. The inner failure propagates as continued use of a poorly-converged inverse, which typically manifests as outer-eigensolve non-convergence and is reported as `MaxIterReached` or `PartialConverged` rather than `LinearSolveFailed`. The L1 form introduces the variant to make the inner-linear-solve coupling visible at the L1 surface; a future `eigsolve-mutation-rotation` L1>L0 theme will materialise it by plumbing `ksp->GetConverged()` (and the SLEPc `EPSConvergedReason` analogues) through the eigensolver outer loop. Resolved (cycle-010, lifter): keep the case with the constructive-introduction annotation; see the §Signature callout for the full treatment.
```

### Edit 3: `book/src/L1/eigsolve.md` — §"Laws that explicitly do not hold" sum-type completeness bullet, soften from rough-in caveat to resolved-with-annotation note

```edit:book/src/L1/eigsolve.md
[old]:- **Sum-type completeness of `EigStatus`** — as noted in §3 above, the `LinearSolveFailed` case is constructively introduced by the L1 form and is not directly observable in the current L0 surface. Until the L1>L0 lowering plumbs it explicitly, treating the four-way `EigStatus` as exhaustive over L0 termination cases is **not** a sound L0-grounded claim.
[new]:- **Sum-type completeness of `EigStatus` over current L0 terminations** — the `LinearSolveFailed` case is constructively introduced by the L1 form (per §3 and the §Signature callout) and is not directly observable in the current Palace L0 surface; current L0 instantiations of `eigsolve` will produce only `Converged`, `PartialConverged`, or `MaxIterReached`. Treating the four-way `EigStatus` as exhaustive over **L1-coordinated** termination cases (including the L1-constructive `LinearSolveFailed`) is sound; treating it as exhaustive over **L0-observable** termination cases is not — the L0 set is the three observable variants only. The future `eigsolve-mutation-rotation` L1>L0 theme will materialise the fourth variant.
```

### Edit 4: `book/src/L1/eigsolve.md` — §Status block, update the inner-solver-failure clause with the resolution pointer

```edit:book/src/L1/eigsolve.md
[old]:`rough-in (test-coverage-bounded, cycle-009)` — the structural signature (input/output shape, the four-way `EigStatus`, the `EigResult` record fields) is well-anchored by direct source reading of `eps.hpp` and the three `Solve()` bodies. The `Converged` / `PartialConverged` / `MaxIterReached` cases are directly source-witnessed (`palace/drivers/eigensolver.cpp:367-374`); the `LinearSolveFailed` case is constructively introduced and **does not currently have an L0 anchor** (the inner-solver non-convergence is silent at the eigensolver level — see Algebraic laws §3 caveat).
[new]:`rough-in (test-coverage-bounded, cycle-009; LinearSolveFailed-constructive resolved cycle-010)` — the structural signature (input/output shape, the four-way `EigStatus`, the `EigResult` record fields) is well-anchored by direct source reading of `eps.hpp` and the three `Solve()` bodies. The `Converged` / `PartialConverged` / `MaxIterReached` cases are directly source-witnessed (`palace/drivers/eigensolver.cpp:367-374`); the `LinearSolveFailed` case is **constructively introduced by the L1 form** (see §Signature callout and Algebraic-laws §3) — annotated as L1-constructive in cycle-010 (resolving cycle-009 OQ `eigsolve-linear-solve-failed-status-anchor`), with materialisation deferred to a future `eigsolve-mutation-rotation` L1>L0 theme.
```

### Edit 5: `book/src/L1/eigsolve.md` — §Evidence, append the negative-anchor evidence rows for the constructive-introduction annotation

```edit:book/src/L1/eigsolve.md
[old]:- `scaffolding/open-questions.md:1342-1351` — cycle-008 OQ `eigsolve-l1-operator-rough-in-candidate` (the dispatch target).
[new]:- `scaffolding/open-questions.md:1342-1351` — cycle-008 OQ `eigsolve-l1-operator-rough-in-candidate` (the cycle-009 harvester dispatch target).
- `scaffolding/open-questions.md:1470-1479` — cycle-009 OQ `eigsolve-linear-solve-failed-status-anchor` (the cycle-010 lifter dispatch target; resolved by this entry).
- `palace/linalg/ksp.cpp:297-310` — `BaseKspSolver<OperType>::Mult` body: `void` return, `Mpi::Warning` on `!ksp->GetConverged()`. Negative anchor for the `LinearSolveFailed` constructive-introduction annotation — the L0 surface for the inner linear solve does not return a status, only logs a warning.
- `palace/linalg/arpack.cpp:574, 580, 761, 778` — ARPACK `opInv->Mult` call sites (linear EPS and quadratic PEP). None query `ksp->GetConverged()` after the call.
- `palace/linalg/nleps.cpp:514` — NLEPS `deflated_solve` inner `opInv->Mult` call site. Same pattern.
- `palace/linalg/slepc.cpp:1858, 1965, 1978, 2076, 2159` — SLEPc shell-matrix callback `opInv->Mult` call sites (across linear-EPS / PEP / NEP variants). Same pattern.
```

### Edit 6: `scaffolding/open-questions.md` — append resolution note to `eigsolve-linear-solve-failed-status-anchor` entry

The OQ ledger is any-agent-appendable. Per standard pattern, the resolution narrative is appended (the original entry is not edited; the integrator-per-report applies an `append-after` edit just below the OQ body, before the next OQ's yaml block at line 1481).

```edit:scaffolding/open-questions.md
[append-after: line 1479, the prose body of the eigsolve-linear-solve-failed-status-anchor OQ ending with "Source: `reports/2026-05-27T191929Z-harvester-eigsolve-L1/CYCLE.md` §Open questions / caveats item 1."]
[content]:

**Resolved cycle-010 (lifter)**: Dispatched at `reports/2026-05-27T220558Z-lifter-eigsolve-linear-solve-failed-anchor/`. Adopted option (b) — keep the `LinearSolveFailed` variant in `EigStatus` and annotate it as **constructed by the L1 form** with explicit negative-anchor citations. The lifter dispatch verified that all ten eigensolver-side `opInv->Mult` call sites (4 ARPACK + 1 NLEPS + 5 SLEPc shell-matrix: `arpack.cpp:574, 580, 761, 778`; `nleps.cpp:514`; SLEPc shell callbacks at `slepc.cpp:1858, 1965, 1978, 2076, 2159`) invoke `BaseKspSolver<ComplexOperator>::Mult` (`palace/linalg/ksp.cpp:297-310`), which returns `void` and emits only `Mpi::Warning`, and that none of the call sites query `ksp->GetConverged()` after the call — confirming the inner-solver failure is silent at the eigensolver outer loop. The L1 form's `LinearSolveFailed` variant is therefore L1-constructive (introduced to make the inner-linear-solve coupling visible at the L1 surface for downstream L4 monadic-coordination consumers); materialisation defers to the future `eigsolve-mutation-rotation` L1>L0 theme (cycle-010+ abstractor candidate). The cycle-010 lifter applied four edits to `book/src/L1/eigsolve.md` (§Signature callout, §Algebraic-laws §3 row, §"Laws that explicitly do not hold" sum-type-completeness bullet, §Status block) and one evidence-section append. Status: resolved.
```

### Edit 7: `scaffolding/open-questions.md` — update yaml block of `eigsolve-linear-solve-failed-status-anchor` to `partially-answered`

Per the cycle-009 precedent visible in the ledger itself (the predecessor OQ `eigsolve-l1-operator-rough-in-candidate` at `scaffolding/open-questions.md:1342-1351` was updated from `status: open` to `status: partially-answered` with `partial_answer_at: cycle-009` and `partial_answer_in: reports/...`), yaml-status updates to existing OQ entries are permitted when the partial-answer / resolution is unambiguous and traceable. Edit 6's resolution narrative is unambiguous (option (b) adopted, four reader-touchpoint edits in `book/src/L1/eigsolve.md`, negative-anchor evidence at `ksp.cpp:297-310` + 10 call sites verified); the lifter therefore proposes the yaml-status update here rather than leaving it to a separate meta-phase pass. (cycle-010 critic flagged the prior "meta-phase only" framing as over-cautious; this edit follows critic guidance.)

The status is `partially-answered` (not fully `resolved`) because the constructive-introduction annotation lands now while the materialising L1>L0 theme (`eigsolve-mutation-rotation`) is still deferred to a cycle-010+ abstractor — analogous to how cycle-009 closed the harvester-rough-in part of `eigsolve-l1-operator-rough-in-candidate` while leaving the firm-promotion follow-ups partially-answered.

```edit:scaffolding/open-questions.md
[old]:slug: eigsolve-linear-solve-failed-status-anchor
opened_at: cycle-009
opened_by: harvester
status: open
[new]:slug: eigsolve-linear-solve-failed-status-anchor
opened_at: cycle-009
opened_by: harvester
status: partially-answered
partial_answer_at: cycle-010
partial_answer_in: reports/2026-05-27T220558Z-lifter-eigsolve-linear-solve-failed-anchor/
```

## Discipline notes

This is a pure-rewriting re-anchor: no operator semantics changed; no L1 vocabulary changed; the rough-in caveats in the existing chapter were already option-(b)-shaped (the harvester named option (b) as the recommendation, with the routing-to-OQ caveat the only thing this dispatch resolves). The five edits surface the resolution into the chapter at four reader-touchpoints (Signature callout, Algebraic-laws §3, §"Laws that explicitly do not hold", §Status) plus an evidence-section update; this is consistent with the lifter discipline of "preserve the theme's narrative; firm up the vocabulary" (CLAUDE.md role spec).

Three small notes on choices:

1. **Why a §Signature callout and not just an Algebraic-laws §3 edit?** Readers of `EigStatus` first encounter it at the signature block (line 44), then later at Algebraic-laws §3 (line 97). The cycle-009 harvester's prose placed the constructive caveat in §3 and §"Laws that explicitly do not hold"; a reader skimming only the signature would miss it. The §Signature callout placement (just after the `EigStatus` line, before the shape-contract bullets) gives the caveat the same reader-touchpoint depth as the case itself.

2. **Why "constructed by the L1 form" as the canonical phrasing?** The cycle-009 OQ named three option labels (drop / accept-constructive-with-annotation / require-L1>L0-lowering). The phrase "constructed by the L1 form" is the option-(b) annotation language the OQ specified; using it verbatim throughout keeps the resolution traceable to the OQ via grep. The phrase also surfaces in the harvester's own rough-in §3 language ("constructive distinction"), so the resolution is continuous with the harvester's intent.

3. **Why defer the L1>L0 theme rather than triggering it now?** The `eigsolve-mutation-rotation` theme is queued as a cycle-010+ abstractor candidate per the cycle-009 harvester report. Per CLAUDE.md "push-forward, one slice / theme / operator at a time" and the lifter discipline ("if you find yourself making non-trivial content decisions, stop and flag in Open questions — likely an abstractor reread is needed"), authoring the lowering theme during a re-anchor would substantially exceed lifter scope. The annotation makes the rough-in survivable in the meantime.

## Supporting evidence

- `book/src/L1/eigsolve.md` (the chapter being re-anchored).
- `reports/2026-05-27T191929Z-harvester-eigsolve-L1/CYCLE.md` (the cycle-009 harvester report that landed the rough-in and named option (b) as the recommendation).
- `palace/linalg/ksp.cpp:297-310` (verified by lifter — `BaseKspSolver::Mult` void return + `Mpi::Warning`).
- `palace/linalg/arpack.cpp:560-600` (verified by lifter — `ArpackEPSSolver::ApplyOp` body; no `ksp->GetConverged()` check).
- `palace/linalg/nleps.cpp:500-540` (verified by lifter — `deflated_solve` lambda body; `opInv->Mult(b1, x1)` followed by deflation math, no status check).
- `palace/linalg/slepc.cpp:687-709` (verified by lifter — `SlepcEPSSolverBase::Solve` body; `EPSConvergedReasonView` is print-only, no status propagation).
- `mcp__palace-codemap__search_text` confirmed ten eigensolver-side `opInv->Mult` call sites (4 ARPACK + 1 NLEPS + 5 SLEPc shell-matrix; no `GetConverged` follow-up at any of them; only `EPSConvergedReasonView` print in `slepc.cpp:699`).
- Cycle-009 integrator-finalize signal (`scaffolding/integrator-signals.md` cycle-009 section): "highest-priority of the four eigsolve firm-promotion follow-ups; smallest-cost (mechanical decision)".

## Open questions / caveats

- **OQ yaml-status flip IS part of proposed-changes (Edit 7)** — the original framing of this report (pre-cycle-010-critic) treated the yaml-status update as a meta-phase concern under a "do not edit original entries" reading of the OQ ledger convention. The cycle-010 critic flagged this as over-cautious: the ledger itself contains the cycle-009 precedent (the predecessor OQ `eigsolve-l1-operator-rough-in-candidate` at `scaffolding/open-questions.md:1342-1351` is `status: partially-answered` with `partial_answer_at: cycle-009` and `partial_answer_in: reports/...`, demonstrating that status updates to existing yaml blocks are permitted when the resolution is unambiguous and traceable to a report). Edit 7 (added by repairer cycle-010) flips the yaml status to `partially-answered` by analogy. The status is partial (not fully `resolved`) because the materialising L1>L0 theme is still deferred. **Not a blocker; this footnote retained as audit trail of the cycle-010 critic/repairer adjustment.**

- **Three sibling cycle-009 eigsolve OQs remain open** — `eigsolve-scaling-coordinate-convention` (Algebraic-laws §5 routes; harvester / lifter review needed during firm-promotion), `eigsolve-initial-space-axis-placement` (lifter / lowering-verifier review needed), `eigsolve-iteration-count-result-field` (harvester re-evaluation during firm-promotion). This dispatch resolves only `eigsolve-linear-solve-failed-status-anchor`; the other three are out of scope per "one theme per invocation". Cycle-010+ planner: consider dispatching the three remaining as a small lifter/abstractor cluster or rolling them into the `eigsolve-mutation-rotation` abstractor dispatch.

- **The eventual L1>L0 lowering theme will introduce a refactor obligation on Palace's eigensolver code** — to materialise `LinearSolveFailed`, the lowering theme must specify the source-side refactor that captures `ksp->GetConverged()` at the ten call sites and propagates the failure to the eigensolver outer-loop status. This is not a stub-implementation case (it would be a behaviour change to Palace, adding a status path that does not currently exist); per CLAUDE.md "Unimplemented Palace stub policy" / "literature-anchored L1 form may inform higher abstractions", the L1>L0 lowering theme would need to be authored as a partly-constructive lowering (the L0 form does not have the variant; the lowering says "if Palace were to plumb the inner-solver status, here is the rewrite shape; current source is silent on this case"). Flag to cycle-010+ abstractor: this is a richer L1>L0 theme than the standard mutation-rotation pattern — the rewrite shape includes a "rewriting requires upstream behaviour change" caveat.

- **Negative-anchor citation pattern surface for L1-constructive cases** — this dispatch introduces a small pattern: citing L0 lines that demonstrate the *absence* of a behaviour (e.g., `BaseKspSolver::Mult` returning `void`; the ten eigensolver-side call sites not querying `GetConverged()`) as evidence that a case is L1-constructive. This is analogous to the obstruction-theme negative-anchor pattern at `book/src/L1-L0/minres-iteration.md` and `book/src/L1-L0/bicgstab-iteration.md`, but applied at the per-status-variant granularity rather than the per-operator granularity. If this pattern recurs (e.g., when `EigResult.iterations` is debated per the sibling OQ `eigsolve-iteration-count-result-field`, the case for adding it will rest on similar negative-anchor evidence), it may warrant a methodology / friction-ledger note for cross-cutter sweeps to consume. **Not a blocker; flagging for meta-phase consideration.**
