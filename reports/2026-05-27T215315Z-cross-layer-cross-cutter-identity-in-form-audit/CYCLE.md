---
agent: cross-layer-cross-cutter
invoked_at: 2026-05-27T21:53:15Z
scope: identity-in-form audit across L4/L3/L2/L1 cohorts (priority #20 second target)
status: integrated
integrated_at: 2026-05-27T230802Z
integration_commit: 30119eb
integration_notes: Applied via integrator-per-report pass 2 of cycle-010 (wave-1 sibling to pass 1 harvester). **Inspection-only dispatch** — no `book/` mutation. 4 routing OQs promoted to `scaffolding/open-questions.md` per write-authority partition (priorities.md is meta-phase + cycle-planner co-edit, not integrator-per-report): `l3-backfill-apply-linop-and-blas1-cohort` (HIGH CONFIDENCE), `ksp-solve-l2-promotion-non-identity-substantive-gap` (MEDIUM CONFIDENCE), `l3-l1-directory-naming-structure-policy`, `l3-vocabulary-inventory-gap`. META Issue 1 flagged `book/src/L4/index.md:40` SUPERSEDED text drift not introduced by this audit; left for finalize/future lifter dispatch. Together with pass 1, enacts priority #20 (identity-lowering-both-levels backfill) from two angles.
---

# CYCLE: identity-in-form audit across L4/L3/L2/L1 cohorts

## Summary

Surveyed the 10 operator candidates listed in the dispatch brief (`apply_linop`, `dot`, `axpy`, `nrm2`, `axpby`, `scal`, `axpbypcz`, `ksp_solve`, `krylov-step`, `eigsolve`) against the L4/L3/L2/L1 + lowering-layer landscape to identify operator entries that should be backfilled at adjacent layers under the new methodology invariant **"Identity-lowerings still require both L levels"** (CLAUDE.md, mid-cycle-009; supersedes the cycle-006 "no L3 row needed" verdict for krylov-step). Found **two confirmed high-confidence backfill candidates**, **one medium-confidence candidate awaiting upstream stabilization**, and a **broader latent-pattern observation** about the BLAS-1 cohort's place in L3 vocabulary that warrants explicit policy capture but no immediate dispatch. The two confirmed candidates are both L3 entries on `krylov-step`'s primitive-call set (`apply_linop` and the BLAS-1 element-wise / reduction primitives), each carrying a structural rationale tied directly to the body-identity theme that the wave-1 sibling harvester is operating on.

## Observation kind

**Coverage gap** — L4/L3/L2 entries are missing for several operators whose lower-layer form is identity-in-form (or thin-theme-dissolution) to the layer they currently inhabit, in violation of the new "each layer is internally coherent" methodology invariant.

## Specific finding

### Landscape snapshot (current state, post-cycle-009)

| Layer | Existing entries (operators) | Existing lowering themes (slugs) |
|---|---|---|
| **L4** | `krylov-step`, `iterate-while`, `iterate-while-with-prev` | — |
| **L4-L3** | — | `krylov-step-typed-wrapper-dissolution`, `gmres-inner-loop-iterate-while-migration` (rough-in) |
| **L3** | (empty; placeholder only) | — |
| **L3-L2** | — | `krylov-step-body-identity` |
| **L2** | `krylov-step` | — |
| **L2-L1** | — | (empty; placeholder only) |
| **L1** | `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`, `ksp_solve` (firm); `eigsolve` (rough-in); plus 6 obstruction-rough-in operators | `apply-linop-mutation-rotation`, `axpby-mutation-rotation`, `axpbypcz-mutation-rotation`, `ksp-solve-mutation-rotation` (firm); `minres-iteration`, `bicgstab-iteration` (obstruction) |

### Wave-1 sibling dispatch

The wave-1 sibling (harvester on `book/src/L3/krylov-step.md`) is closing the L3 gap for `krylov-step` itself. This audit assesses the **other** candidates beyond krylov-step.

### Per-candidate verdict

**(1) `apply_linop`** — firm at L1 only.

- **L3 candidate (HIGH CONFIDENCE BACKFILL).** Both the L4-L3 wrapper-dissolution theme (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:64`) and the L3-L2 body-identity theme (`book/src/L3-L2/krylov-step-body-identity.md:30, 97`) reference `apply_linop` as an **L3-native global op** with no element loop exposed. The L3-L2 theme explicitly states (line 97) that the seven L1 primitives "operate on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native because its signature has no per-element loop visible)." The L3 form is referenced repeatedly across multiple firm themes as `apply_linop op.T K.<input_field>` with whole-tensor semantics, yet `book/src/L3/apply_linop.md` does not exist. The rotation L3→L1 is identity-in-form on the primitive's signature; only the surrounding stratum-typing-vs-positional treatment differs (the same surface adjustment as krylov-step's L3>L2). The L3 index (`book/src/L3/index.md:11-14`) explicitly lists `matvec` as a whole-tensor primitive at L3 — `apply_linop` is the matvec generalization.
- **L2 candidate (CONFIRMED-NOT-NEEDED-BY-AUTHORITATIVE-STATEMENT).** The L2 entry on `krylov-step` (`book/src/L2/krylov-step.md:96, 130-132`) names `apply_linop` as an "L1 primitive" cited via `[apply_linop](../L1/apply_linop.md)`; the L2 index (`book/src/L2/index.md:17`) lists "axpy, dot, matvec, gemv, trsv, scal, nrm2" as L2 vocabulary while pointing back at L1 entries. The L2 layer's purpose per its index is "compositions of L1 primitives into method-step shapes" — `apply_linop` is itself a primitive, not a composition. A standalone L2 entry would duplicate content with no algebraic novelty. **However**, this verdict is in tension with priority #17's "lower-layer shared vocabulary priority" — if the L2 layer is to grow shared vocabulary, an L2 `apply_linop` row that points at L3 might be coherent. Defer this judgement to the cycle-010 planner pending more L2 traffic.
- **L4 candidate (CONFIRMED-NOT-NEEDED).** L4 is the typed-wrapper / monadic-coordination layer; primitives like `apply_linop` appear inside L4 entries as let-bindings (per the L4 krylov-step §Semantics body, `book/src/L4/krylov-step.md:59`) but are not first-class L4 vocabulary — `apply_linop` carries no monadic effect, no state-stratification typing, no novel calculus content at L4. A standalone L4 entry would over-promote a leaf primitive.

**(2) `axpy` / `axpby` / `axpbypcz` / `dot` / `nrm2` / `scal` (the BLAS-1 cohort)** — firm at L1.

- **L3 candidate (HIGH CONFIDENCE BACKFILL — bundle).** Same structural rationale as apply_linop: the L3-L2 body-identity theme (`book/src/L3-L2/krylov-step-body-identity.md:30-37, 97`) treats these primitives as L3-native by signature shape — each is a whole-tensor / reduction operation with no element loop exposed. The L3 index (`book/src/L3/index.md:13`) explicitly lists "axpy, dot, nrm2 as field operations" as L3 vocabulary. The L4-L3 typed-wrapper-dissolution theme (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:65-68`) renders these primitives in the L3 body let-chain identically to L1. **L3 entries on these six primitives would close the broader L3 vocabulary gap that the L3 index already advertises**, restoring the "each layer is internally coherent" property: a reader navigating L3 (which the L3 index promises includes these primitives as field operations) cannot currently find them. Bundling considerations: six entries, all narrow scope, all share the same rotation rationale (whole-tensor signature already identity-in-form); a single harvester dispatch can plausibly cover ≥2 of them per invocation by following the wave-1 `krylov-step` L3 backfill precedent (use L3 vocabulary, point at L1 for primitive-composition body, identity-in-form lowering noted in a thin L3-L2 theme).
- **L2 candidate (CONFIRMED-NOT-NEEDED-WITH-CAVEAT).** Same logic as apply_linop's L2 verdict — the BLAS-1 primitives are referenced from L2's `krylov-step` and the L2 index lists them by name but does not surface them as standalone L2 rows. L2's role is composition of these primitives, not naming them anew. Caveat: priority #17 ("lower-layer shared vocabulary priority") may eventually compel L2 entries on these primitives if more L2 operators emerge; currently the L2 cohort is just `krylov-step`, so the duplication risk is acute. Defer.
- **L4 candidate (CONFIRMED-NOT-NEEDED).** Same logic as apply_linop's L4 verdict — leaf primitives don't get L4 rows.

**(3) `ksp_solve`** — firm at L1.

- **L2 candidate (MEDIUM CONFIDENCE — DEFER pending firm `krylov-step` L1 surface).** `ksp_solve` is described in its L1 entry (`book/src/L1/ksp_solve.md:55, 83, 142`) as the **constructed-operator gate** from L1 BLAS-1 vocabulary to the L2 `krylov-step` vocabulary — "the L2 `krylov-step` operator is the layer at which they become direct dependencies" (line 81). There is a candidate L2 entry shape: `ksp_solve` at L2 would be the outer driver (`solve_loop` + `restart_cycle`) that folds `krylov-step` via an iteration combinator, threading SolveResult statistics. The rotation L2→L1 is **NOT identity-in-form** — at L2 the per-method body is unfolded into an explicit krylov-step fold; at L1 the body is opaque inside `Solver[A]`. This means the missing L2 row would carry **substantive content** (the outer-loop framing), so this is a real coverage gap, but it is **not an identity-in-form backfill** — it would be a fresh harvester dispatch with new algebraic content, not a mechanical backfill. **Recommendation: do NOT dispatch under priority #20** (which targets identity-in-form backfills). Surface as a separate priority candidate for cycle-010+ planner if appropriate.
- **L4 candidate (DEFER).** `ksp_solve` at L4 would be the typed-wrapper Solve-monad driver. Like the L2 candidate, this would be substantive (non-identity) content, not an identity-in-form backfill. Out of scope for priority #20.
- **L3 candidate (DEFER pending L2).** L3 form of `ksp_solve` is the value-threaded version of the L4 driver. If L4 and L2 are not yet authored, the L3 row's identity-vs-substantive question is undetermined.

**(4) `eigsolve`** — rough-in at L1.

- **L2/L3/L4 candidates (DEFER).** `eigsolve` is rough-in at L1 (test-coverage-bounded per `book/src/L1/index.md:42`). Upper-layer entries should not lead the firmness frontier. The `eigsolve` L1 entry (`book/src/L1/eigsolve.md:131, 151, 197, 204`) already names L4 `iterate_while` as the natural composition target; L1 firming is the prerequisite. Defer until eigsolve is firm at L1, then re-audit.

**(5) `krylov-step`** — firm at L4, firm at L2, **L3 backfill in flight (wave-1 sibling dispatch)**.

- **L1 candidate (CONFIRMED-NOT-NEEDED).** `krylov-step` is a **composition**, not a primitive — it consumes the seven L1 primitives in a five-group sequence. An L1 entry would have to either (a) flatten the composition (defeating the purpose of L2 naming), or (b) introduce a new opaque primitive. The L1 cohort already absorbs the closest analog as `ksp_solve` (the constructed-operator gate); there is no L1 vocabulary slot for the step-body sans outer-driver wrapping. The methodology invariant "each layer is internally coherent" does not compel L1 `krylov-step` because L1's coherence is about primitives and L2's coherence is about compositions; the layer roles differ. **Distinguish from the bare-identity case (apply_linop, BLAS-1) which IS a primitive at the lower layer and IS missing.**

### Latent observation: L3 vocabulary inventory gap

The L3 index (`book/src/L3/index.md:11-14`) advertises whole-tensor primitives (matvec, axpy, dot, nrm2) as L3 vocabulary, but the L3 directory contains only the index file and (post-wave-1) `krylov-step.md`. The new methodology invariant "Identity-lowerings still require both L levels" makes the gap actionable: every primitive the L3 index advertises as an L3 field operation should have a corresponding L3 entry, even if the rotation L3→L1 is identity-in-form. This is the broader pattern — the audit's two confirmed candidates (apply_linop + the BLAS-1 cohort) are instances of a layer-coherence gap that may extend to other operators as L2/L3/L4 vocabulary grows. This pattern should be tracked, not enacted in one cycle.

## Recommendation

```yaml
proposed_changes:
  # ===== HIGH CONFIDENCE — dispatch in cycle-010 (if capacity) or cycle-011 =====

  - kind: backfill-harvester-dispatch
    target_file: book/src/L3/apply_linop.md
    source_layers_cited:
      - book/src/L1/apply_linop.md  # firm at L1, cycle-004
      - book/src/L3-L2/krylov-step-body-identity.md  # firm; cites apply_linop as L3-native
      - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md  # firm; renders apply_linop in L3 let-chain
      - book/src/L3/index.md  # L3 vocabulary inventory naming matvec as field op
    rotation_type: identity-in-form
    recommendation: dispatch-harvester-cycle-010-or-011
    rationale: |
      apply_linop is the matvec generalization explicitly named in the L3 index
      (line 13) and rendered in two firm L4-L3 / L3-L2 themes as an L3-native
      whole-tensor operation. The L3 form is value-thread-isomorphic to the L1
      form modulo the surrounding stratum-typing-vs-positional treatment (per
      the krylov-step L3>L2 surface-adjustment pattern). Backfilling this row
      makes the L3 layer internally coherent for the apply_linop primitive that
      every Krylov method's L3 body invokes.
    suggested_dispatch_pattern: |
      Single harvester invocation; mirror the wave-1 L3/krylov-step.md harvest
      precedent (use L3 vocabulary, point at L1 for the primitive's algebraic
      laws, surface the identity-in-form L3>L1 rewrite as a thin L3-L1 theme
      if/when the L3-L1 theme directory is created — currently no `L3-L1/`
      directory exists; the precedent will be set by wave-1's siblings).

  - kind: backfill-harvester-dispatch-bundle
    target_files:
      - book/src/L3/axpy.md
      - book/src/L3/dot.md
      - book/src/L3/nrm2.md
      - book/src/L3/axpby.md
      - book/src/L3/axpbypcz.md
      - book/src/L3/scal.md
    source_layers_cited:
      - book/src/L1/axpy.md, book/src/L1/dot.md, book/src/L1/nrm2.md,
        book/src/L1/axpby.md, book/src/L1/axpbypcz.md, book/src/L1/scal.md  # all firm at L1
      - book/src/L3-L2/krylov-step-body-identity.md:97  # explicitly names these seven primitives as L3-native by signature
      - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:67  # renders these in L3 let-chain
      - book/src/L3/index.md:13  # L3 vocabulary inventory naming axpy/dot/nrm2 as field ops
    rotation_type: identity-in-form
    recommendation: dispatch-harvester-cycle-010-or-011-bundle-by-2-or-3
    rationale: |
      The six BLAS-1 primitives share the same rotation rationale as apply_linop
      (whole-tensor signature, no element loop exposed, identity-in-form on the
      primitive itself with surface-adjustment at the stratum-typing level).
      The L3 index already advertises three of them (axpy/dot/nrm2) by name as
      field operations. Bundling: 2-3 entries per harvester dispatch keeps each
      dispatch narrow while clearing the broader L3 vocabulary gap over 2-3
      cycles. Suggested bundles (by algebraic shape): (a) axpy + axpby + axpbypcz
      (the linear-update family; shared subsumption laws), (b) dot + nrm2 (the
      reduction family; nrm2 depends on dot), (c) scal (standalone leaf,
      subsumed by axpby; smallest dispatch).
    suggested_dispatch_pattern: |
      Three harvester dispatches over cycle-010+ — one per bundle. Each
      dispatch follows the wave-1 L3/krylov-step.md precedent. Entries are
      short (the L3 form is identical to L1; the entry exists for navigation
      and for the layer-coherence invariant, not for new algebraic content).

  # ===== MEDIUM CONFIDENCE — NOT priority #20 scope, surface for separate priority =====

  - kind: NOT-priority-20-but-real-coverage-gap
    candidate: book/src/L2/ksp_solve.md
    source_layers_cited:
      - book/src/L1/ksp_solve.md  # firm at L1, cycle-007
      - book/src/L2/krylov-step.md:96, 130-132  # references ksp_solve as L1
    rotation_type: NOT-identity (substantive — outer-loop / restart_cycle / solve_loop framing)
    recommendation: confirm-not-needed-under-priority-20 + surface-for-separate-cycle-010+-planner-priority
    rationale: |
      ksp_solve's L2 form would carry substantive content (the outer driver
      around krylov-step, threading SolveResult statistics). This is real
      coverage gap material, but it is NOT an identity-in-form backfill —
      it is fresh harvester work. Priority #20 explicitly targets identity-
      in-form backfills; this candidate is out of scope. Cycle-010 planner
      may consider authoring a separate priority for "ksp_solve L2/L4
      promotion" (the constructed-operator gate's upward extension), tracked
      independently from priority #20's identity-in-form sweep.

  # ===== DEFER =====

  - kind: defer-pending-upstream
    candidate: book/src/L2/eigsolve.md (and L3, L4)
    source_layers_cited:
      - book/src/L1/eigsolve.md  # rough-in at L1, cycle-009
    rotation_type: undetermined
    recommendation: defer-pending-eigsolve-L1-firm-promotion
    rationale: |
      eigsolve is rough-in at L1 (test-coverage-bounded). Upper-layer entries
      must not lead the firmness frontier. Defer until eigsolve is firm at L1
      and re-audit then.

  - kind: defer-not-applicable
    candidate: book/src/L1/krylov-step.md
    source_layers_cited:
      - book/src/L2/krylov-step.md  # firm at L2
      - book/src/L4/krylov-step.md  # firm at L4
    rotation_type: not-applicable (composition vs primitive layer mismatch)
    recommendation: confirm-not-needed-with-reason
    rationale: |
      krylov-step is a composition of L1 primitives, not a primitive itself.
      The methodology invariant "each layer is internally coherent" governs
      layer-appropriate vocabulary; L1's role is primitives, L2's role is
      compositions of primitives. An L1 krylov-step would defeat the layer-
      role distinction. The closest analog at L1 (the constructed-operator
      gate) already exists as ksp_solve.

  # ===== LATENT OBSERVATION (NO IMMEDIATE DISPATCH) =====

  - kind: latent-pattern-observation
    candidate: L3-vocabulary-inventory-gap
    rationale: |
      The L3 index (book/src/L3/index.md:11-14) advertises whole-tensor
      primitives (matvec, axpy, dot, nrm2) as L3 vocabulary, but the L3
      directory currently contains only index.md + (post-wave-1) krylov-step.md.
      Under the new methodology invariant "Identity-lowerings still require
      both L levels", every primitive the L3 index advertises should have a
      corresponding L3 entry, even when the rotation L3→L1 is identity-in-form.
      This audit's two HIGH CONFIDENCE backfill candidates (apply_linop +
      BLAS-1 bundle) are instances of this broader pattern. Other operators
      may follow as L2/L3/L4 vocabulary grows. Tracked here, not enacted —
      enaction is via the specific backfill dispatches above.
    suggested_action: |
      Surface to cycle-010+ planner as evidence supporting the broader L3
      cohort growth that priority #17 already targets. The two HIGH CONFIDENCE
      candidates are the next concrete realization of that policy.
```

## Supporting evidence

**Files inspected** (full reads, not just searches):

- `/home/crutcher/git/palace_whiteroom/CLAUDE.md` — methodology invariants §"Identity-lowerings still require both L levels" + §"Lower-level shared vocabulary takes priority"
- `/home/crutcher/git/palace_whiteroom/scaffolding/priorities.md` — priority #20 (identity-lowering-both-levels-backfill) + #17 (lower-layer-shared-vocabulary-priority) + #18 (layer-definition-discipline-high-to-low)
- `/home/crutcher/git/palace_whiteroom/book/src/L1/index.md` — L1 vocabulary cohort + dep-map
- `/home/crutcher/git/palace_whiteroom/book/src/L1/apply_linop.md` — firm L1 entry, §Context, §Signature, §Algebraic laws, §"L1 vs L0 distinction"
- `/home/crutcher/git/palace_whiteroom/book/src/L1/axpy.md`, `dot.md`, `nrm2.md` — firm L1 entries; algebraic shapes
- `/home/crutcher/git/palace_whiteroom/book/src/L1/ksp_solve.md` (sectional reads) — firm L1 entry, constructed-operator gate framing
- `/home/crutcher/git/palace_whiteroom/book/src/L1/eigsolve.md` (sectional reads) — rough-in L1 entry
- `/home/crutcher/git/palace_whiteroom/book/src/L2/index.md` — L2 vocabulary cohort
- `/home/crutcher/git/palace_whiteroom/book/src/L2/krylov-step.md` — firm L2 entry, §Dependencies (line 96), §"L2 vs L1 distinction" (lines 130-132)
- `/home/crutcher/git/palace_whiteroom/book/src/L3/index.md` — L3 vocabulary inventory (lines 11-14 advertising matvec/axpy/dot/nrm2 as field ops)
- `/home/crutcher/git/palace_whiteroom/book/src/L3-L2/krylov-step-body-identity.md` — firm theme; §"Applicability conditions" (line 97) explicitly names the seven primitives as L3-native by signature shape; §"L3 form (LHS)" (lines 27-37) renders the L3 body with primitive calls
- `/home/crutcher/git/palace_whiteroom/book/src/L4/index.md` — L4 vocabulary cohort
- `/home/crutcher/git/palace_whiteroom/book/src/L4/krylov-step.md` — firm L4 entry, §Semantics body (line 59)
- `/home/crutcher/git/palace_whiteroom/book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` — firm theme; §"L3 form (RHS)" (lines 55-89) renders L3 body with primitive calls identical to L1 signature

**Key supporting passages (paraphrased; not load-bearing for the recommendation but cited for the audit's reasoning chain):**

- `book/src/L3-L2/krylov-step-body-identity.md:97` — "The seven L1 primitives used (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`) are firm post-cycle-004; each operates on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native because its signature has no per-element loop visible)."
- `book/src/L3/index.md:11-14` — "L3 expresses: Whole-tensor primitives (matvec, axpy, dot, nrm2 as field operations); ..."
- `scaffolding/priorities.md:46` (priority #20) — "Second target (audit): which other operators in the current chain (apply_linop, dot, axpy, etc.) have identity-in-form rotations between adjacent layers that have not been explicitly landed at the lower layer?"

## Open questions / caveats

1. **L3-L1 lowering theme directory does not exist.** The new L3 backfill entries (per the HIGH CONFIDENCE recommendations) would presumably get thin identity-in-form L3-L1 themes documenting the no-op rotation, analogous to `L3-L2/krylov-step-body-identity.md`. There is no `book/src/L3-L1/` directory currently. The wave-1 sibling dispatch (`L3/krylov-step.md`) may or may not be creating one; this audit cannot foresee. **If the wave-1 dispatch does NOT create `L3-L1/`, the cycle-010+ planner needs to decide whether each L3 backfill comes with a sibling L3-L1 theme or whether the identity rotation is captured in-line at the L3 entry itself.** Either is consistent with the methodology invariant; the layer-intro-author role spec would benefit from a per-cycle policy decision.

2. **The L2 candidate for apply_linop / BLAS-1 is genuinely contested.** The audit's verdict ("CONFIRMED-NOT-NEEDED" for L2 entries on apply_linop and the BLAS-1 cohort) rests on the L2 layer's stated role being "compositions of L1 primitives, not naming them anew" (per `book/src/L2/index.md:17`, `book/src/L2/krylov-step.md:130-132`). However, priority #17 ("lower-layer shared vocabulary priority") suggests L2 should grow shared vocabulary, and one reading of that priority is that the BLAS-1 primitives should have L2 entries for the same internal-coherence reason as the L3 entries. **The audit's defer-this-judgement-to-planner posture is intentional**: the cycle-010 planner needs to decide whether L2 entries should mirror L3 entries for the same primitives (giving four layers' worth of identity-in-form entries: L1 + L2 + L3 + L4-mention) or whether L2's composition-focused role keeps the BLAS-1 primitives out of L2 (leaving L1 + L3 only). The methodology invariant text ("each layer is coherent within itself") does not unambiguously resolve this — it depends on what the L2 layer's coherent vocabulary scope is.

3. **Eigsolve cohort growth deferred but flagged for re-audit.** Once eigsolve is promoted from rough-in to firm at L1 (per the four follow-up OQs in priorities #17), the audit's defer-pending-upstream verdict should be revisited. Cycle-010+ planner should put a watch-list entry for "re-audit eigsolve upper-layer placement after L1 firm promotion".

4. **The "ksp_solve at L2/L4" candidate is real but out-of-priority-20-scope.** Surfacing this here (rather than silently dropping it) because the audit found it during inspection and the cycle-010 planner may want to schedule it independently. **Not enacted by this audit.** If the cycle-010 planner schedules it, it routes to harvester (not me) and is substantive work, not a backfill.

5. **Tool access (MCP codemap):** This dispatch did not invoke `mcp__palace-codemap__*` tools because the audit's scope was entirely within `book/src/` (no Palace source-line walking was needed — the existing themes already cite the load-bearing L0 evidence). The MCP tool availability check via ToolSearch succeeded; no permission-denied was observed. **This is a positive signal for the cycle-010 pilot retry** (priority #16). Dispatches that require Palace source inspection (e.g., the eigsolve re-audit, or any harvester dispatch backfilling an L3 entry that needs to re-verify L0 line ranges) should now exercise the MCP tools to validate the permission fix.
