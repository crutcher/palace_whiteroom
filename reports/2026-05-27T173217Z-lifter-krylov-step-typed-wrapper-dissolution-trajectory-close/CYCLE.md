---
agent: lifter
invoked_at: 2026-05-27T173217Z
scope: L4>L3 theme re-anchor — krylov-step-typed-wrapper-dissolution (close §3.8 trajectory-collapse gap)
status: integrated
integrated_at: 2026-05-27T18:35:15Z
integration_commit: e4929aa
integration_notes: cycle-008 pass 2 (wave-1; PRIORITY). Promoted L4>L3 typed-wrapper-dissolution rough-in -> firm with §3.8-preamble + two-form sketch + Condition 5 + 10-citation verified_against block. Closed cycle-006 OQ iterate-while-l3-rendering-trajectory-accumulation-gap (first 2-cycle-carried OQ closed via lifter-driven artifact landing). Downstream L3>L2 krylov-step-body-identity auto-eligible for cycle-009 mechanical promotion via status-inheritance.
inputs:
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (cycle-006 wave-2 rough-in)
  - book/src/L4/iterate-while.md (cycle-007 wave-1 firm; Law 1 is the §3.8 demand-pruning law)
  - book/src/L4/iterate-while-with-prev.md (cycle-007 wave-1 firm; Law 2 lifts pruning to both step bodies)
  - book/src/concepts/derived-view-hoisting.md (the §3.8 demand-pruning algebra and CG worked example)
  - reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/CYCLE.md (cycle-007 wave-2 audit; verdict (c) — 10 citations)
  - reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/META.md (repairer tightened :222-232 → :222-224)
  - book/src/L1-L0/axpby-mutation-rotation.md:173-189 (verified_against trailing-block precedent)
  - book/src/L1-L0/apply-linop-mutation-rotation.md:353-369 (verified_against trailing-block precedent)
  - scaffolding/open-questions.md:1227-1241 (OQ iterate-while-l3-rendering-trajectory-accumulation-gap, cycle-007 wave-2 verdict-(c) augmentation)
---

# CYCLE: Re-anchor krylov-step-typed-wrapper-dissolution — close §3.8 trajectory-collapse gap

## Summary

Closes the cycle-006/cycle-007 trajectory-accumulation gap on the L4>L3 theme `krylov-step-typed-wrapper-dissolution`. Cycle-007 wave-1 firmed the L4 row `iterate_while` (carrying an explicit `trajectory: [{ ...e }]` accumulator with §3.8 demand-pruning as Law 1); cycle-007 wave-2 audited the inherited gap on the cycle-006 theme's L3 sketch and produced verdict (c): the L3 single-readout shape is correct *because* Law 1 fires for Palace's `final_state`-only KSP consumer surface, but the cycle-006 theme elides the rule-citation and renders the L3 form as if it were a different combinator. This dispatch re-anchors the theme to the firmed-up L4 vocabulary: it adds a §3.8 preamble + a two-form L3 sketch (pruned + unpruned) at §"What the L3 form for `iterate_while` looks like", adds a new applicability **Condition 5** naming the consumer-demand precondition, appends the cycle-007 audit's 10-citation `verified_against:` block as a trailing YAML, and promotes the theme `Status:` from `rough-in` to `firm`. Pure rewriting per lifter role spec — the lowering's structure stays; the §3.8 vocabulary firms up. The L4 form's signature is unchanged; the L3 form's shape is unchanged for Palace; only the justification path becomes operational.

## Proposed changes

### 1. EDIT book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md — §"What the L3 form for iterate_while looks like" (lines 156-167) — replace with §3.8 preamble + two-form sketch

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]
### What the L3 form for `iterate_while` looks like

For completeness — this is *not* a separate theme, but the natural fall-out of the `krylov-step` body's L4>L3 lowering. The L4 `iterate_while step carry₀` form lowers to a tail-recursive L3 loop:

```text
iterate_while_L3 step (carry, sim) =
  let (carry', sim', readout, continue) = step (carry, sim)
  in if continue then iterate_while_L3 step (carry', sim')
                 else (carry', sim', readout)
```

The tail-recursive shape is value-threaded; the monad has dissolved. The `sequential-obstruction` of the outer loop survives at L3 (per `cg.md:341-349`) — the L3 form names the loop tail-recursively but does not claim it lifts to a global tensor-field op. This is the expected outcome for Krylov methods at L3 per `sequential-obstruction.md`.

[new]
### What the L3 form for `iterate_while` looks like

For completeness — this is *not* a separate theme, but the natural fall-out of the `krylov-step` body's L4>L3 lowering. The L4 `iterate_while step carry₀` form (per the firm L4 row [`iterate-while`](../L4/iterate-while.md)) carries a `trajectory: [{ ...e }]` accumulator subject to §3.8 demand-driven pruning (Law 1 of `book/src/L4/iterate-while.md`, instantiated for the residual-norm case in `book/src/concepts/derived-view-hoisting.md` §"Worked example: CG residual norm"). The L3 shape therefore depends on the downstream consumer's observation pattern, with two forms arising from the same L4 invocation under different consumer demands.

**Unpruned form** — the direct value-threaded dissolution of the L4 form when a downstream consumer reads `.trajectory` (no §3.8 collapse fires; the accumulator is materialized at L3):

```text
iterate_while_L3 step carry₀ sim₀ =
  let go (carry, sim, traj) =
        if not (p carry)
          then (carry, sim, reverse traj)         -- final_state, sim', trajectory
          else let (carry', sim', readout) = step (carry, sim)
               in go (carry', sim', readout : traj)
  in go (carry₀, sim₀, [])
```

**Pruned form** — the §3.8-collapsed shape that arises when the consumer observes only `final_state`-equivalent quantities (Palace's KSP case, per the four-scalar consumer surface at `reference/palace/palace/linalg/iterative.hpp:52-55` consumed solely at `reference/palace/palace/linalg/ksp.cpp:296-310`). Law 1 rewrites the body to omit the extras computation; the L3 form drops the accumulator entirely and the `step` is rendered in its `state`-only subgraph:

```text
iterate_while_L3_pruned step carry₀ sim₀ =
  let go (carry, sim) =
        if not (p carry)
          then (carry, sim)                       -- final_state, sim'
          else let (carry', sim') = step_state (carry, sim)
               in go (carry', sim')
  in go (carry₀, sim₀)
```

where `step_state = λ(carry, sim) -> let (carry', sim', _readout) = step (carry, sim) in (carry', sim')` is the §3.8-pruned subgraph of `step` that computes only the next carry (the extras computation is eliminated as dead code at the call site, not merely unused at runtime). The L3-side `step_state` has shape `(carry, sim) -> (carry', sim')` — the positional-tuple image of the L4-side `f_state : α -> α` of Law 1 (`book/src/L4/iterate-while.md:123-133`), with the `sim` thread surfacing as a positional argument at L3 because the `Solve` monad has dissolved (per §"Concept-page references" entry for `solve-monad.md`); the L4 `α` collapses to the L3 carry alone, with `sim` carried alongside positionally rather than monadically.

The L4>L3 collapse from the unpruned to the pruned form is governed by the rule:

$$
\frac{
  \text{only } \textsf{final\_state} \text{ of the L3 result is observed downstream}
}{
  \textsf{iterate\_while\_L3}\ p\ \textsf{step}\ \textsf{carry}_0\ \textsf{sim}_0 \;\equiv\; \textsf{iterate\_while\_L3\_pruned}\ p\ \textsf{step}_{\textsf{state}}\ \textsf{carry}_0\ \textsf{sim}_0
}
$$

which is exactly the L3-side image of Law 1 of [`iterate-while`](../L4/iterate-while.md) — the L4 demand-pruning law transports through the L4>L3 wrapper dissolution because the dissolution is value-thread-isomorphic on the body (the §"Audit of cycle-002 identity-in-form claim" below establishes this). The applicability of the pruned form is selected by the new Condition 5 in §"Applicability conditions" below; for Palace's actual KSP consumer surface, Condition 5 holds and the pruned form is the rendered L3 shape.

Both forms are tail-recursive value-threaded loops; the `Solve` monad has dissolved (the `sim` argument is positional, not monadic), and the `sequential-obstruction` of the outer loop survives at L3 (per `cg.md:341-349`) — the L3 form names the loop tail-recursively but does not claim it lifts to a global tensor-field op. This is the expected outcome for Krylov methods at L3 per `sequential-obstruction.md`. The unpruned form additionally allocates the trajectory list (an `O(N)` accumulator); the pruned form does not.
```

### 2. EDIT book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md — §"Applicability conditions" — add Condition 5

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]
4. **The `Krylov` ephemeral bundle has plain-value lifecycle (born at restart, discarded at restart-or-return) and is not aliased by any other state.** The L4 typing makes this structural (`Krylov` is not a field of `SimState`; lifetime is restart-scoped); at L3 it becomes a discipline. The rewrite assumes no caller threads `Krylov` across restart boundaries (which would mis-type its lifetime). Per `solve-monad.md:53`, this discipline is honoured by `restart_cycle` building a fresh `Krylov` per cycle.

If a future Krylov-shaped slice violates any of these (e.g., a method whose `OpParams` needs per-step mutation, or whose step body needs effects beyond `SimState`), the L4>L3 lowering would need to be refined; the speculative-operator slot would be enlarged.

[new]
4. **The `Krylov` ephemeral bundle has plain-value lifecycle (born at restart, discarded at restart-or-return) and is not aliased by any other state.** The L4 typing makes this structural (`Krylov` is not a field of `SimState`; lifetime is restart-scoped); at L3 it becomes a discipline. The rewrite assumes no caller threads `Krylov` across restart boundaries (which would mis-type its lifetime). Per `solve-monad.md:53`, this discipline is honoured by `restart_cycle` building a fresh `Krylov` per cycle.

5. **The downstream consumer of the surrounding `iterate_while` invocation observes only `final_state`-equivalent quantities (no per-iteration trajectory readout).** This is the precondition for the §3.8 demand-pruning collapse from the unpruned L3 form (`[readout]` accumulator) to the pruned L3 form (single readout / accumulator dropped) shown in §"What the L3 form for `iterate_while` looks like" above. Per Law 1 of [`iterate-while`](../L4/iterate-while.md) and the worked example in `book/src/concepts/derived-view-hoisting.md`, when the consumer's destructuring reads only `final_state` (or the L3-positional equivalent — the final-iteration carry value), the per-step `extras` computation in the step body is eliminated by the §3.8 rewrite, the L4 `[readout]` trajectory collapses to `[]`, and the L3 form is the pruned shape. **Palace satisfies this condition by construction**: the `IterativeSolver` result-extraction surface materializes exactly four scalars (`converged`, `initial_res`, `final_res`, `final_it` at `reference/palace/palace/linalg/iterative.hpp:52-55`), each of which is either a carry field at the final iteration or a pre-loop initialization; the sole caller `BaseKspSolver::Mult` at `reference/palace/palace/linalg/ksp.cpp:296-310` consumes only those four scalars (branch on `GetConverged`, ratio in warning via `GetFinalRes()/GetInitialRes()`, sum into counter via `GetNumIterations`). No per-iteration consumption exists in `palace/`. **When violated** — e.g., a hypothetical future Palace surface `GetResidualHistory(): std::vector<double>` reading the per-step `residual_norm` extras — Condition 5 fails, §3.8 does not fire for that consumer, and the L3 form must be re-rendered with the accumulator restored (the unpruned form). The L4 form is invariant under this consumer change; only the L4>L3 lowering's rendered L3 shape selects between the two forms.

If a future Krylov-shaped slice violates any of these (e.g., a method whose `OpParams` needs per-step mutation, or whose step body needs effects beyond `SimState`, or whose consumer reads the trajectory), the L4>L3 lowering would need to be refined; the speculative-operator slot would be enlarged.
```

### 3. EDIT book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md — §"Status" — promote rough-in → firm

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]
## Status

`rough-in` — the theme's rewrite shape is sketched against the cycle-006 wave-1 firm L4 entry; the L3 form is the value-threaded dissolution of the L4 wrapper; the audit of the cycle-002 identity-in-form claim is included; the speculative `iterate_while` / `iterate_while_with_prev` L4 operators are flagged for harvester promotion. The theme is **non-blocking on L4 vocab promotion**: even with `iterate_while` unanchored, the L4>L3 rewrite on the `krylov-step` body itself is fully specified; the unanchored combinator is the *consumer*, not the rewrite target. **Lowering-verifier follow-up** (cycle-007 candidate) should confirm that the value-threaded L3 form produced by applying this theme to `L4/krylov-step` is textually equivalent to `L2/krylov-step` §Semantics body modulo the L3-level outer-loop tail-recursion wrapping. If the verifier finds a mismatch (e.g., a primitive call shape that does not survive the rewrite), the theme is refined.

[new]
## Status

`firm` — the theme's rewrite shape is fully anchored against the cycle-006 wave-1 firm L4 entry [`krylov-step`](../L4/krylov-step.md), the cycle-007 wave-1 firm L4 row [`iterate-while`](../L4/iterate-while.md) (with its Law 1 §3.8 demand-pruning rule), the cycle-007 wave-1 firm L4 row [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md), and the cycle-007 wave-2 lowering-verifier audit (`reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/CYCLE.md`, verdict (c) — L3 single-readout is correct under §3.8 pruning for Palace's KSP consumer surface). The L3 form is rendered in two shapes (pruned + unpruned) governed by Condition 5; the §"What the L3 form for `iterate_while` looks like" subsection cites the §3.8 collapse rule explicitly; the trailing `verified_against:` block carries the cycle-007 wave-2 audit's 10-citation evidence base. The two speculative L4 operators (`iterate_while`, `iterate_while_with_prev`) are now firm; the audit of the cycle-002 identity-in-form claim is preserved. The cycle-006 / cycle-007 OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` is closed by this dispatch.
```

### 4. EDIT book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md — append trailing verified_against block at end-of-file

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]
**Open question disposition**: this dispatch *audits* the cycle-005 open question `krylov-step-l3-identity-in-form-audit` and proposes closing it as **confirmed-with-refinement** — the assertion holds, the framing is sharpened, no L3 row needed. Integrator will mark accordingly; if integration uncovers a non-identity finding (e.g., a corpus check on a slice this dispatch did not re-verify reveals body-level rotation), the question stays open and a cycle-007 L3 row promotion follows.

## Verified-against

L4 source (the input form of this lowering):

- `book/src/L4/krylov-step.md` (wave-1 harvester output, this cycle; the firm L4 entry this lowering applies to) — §Signature (Form A and Form B signatures), §Semantics (body shape, monadic effect placement), §"L4 vs L2 distinction" (the wrapper-vs-composition framing).
- `reports/2026-05-27T080944Z-harvester-krylov-step-L4/CYCLE.md` — the harvester dispatch report carrying the same content plus open questions (caveat 2 on `iterate_while` anchoring, cited above).

L3 evidence (the target form of this lowering, including the identity-in-form audit):

- `book/src/spec/slices/cg.md:341-362` — the combinator-miner cycle-002 evidence for L2>L3 body identity. Claim 2 ("step body lifts as identity") is the cited support. Re-read for this audit; assertion confirmed.
- `book/src/spec/slices/arnoldi_step.md:178-213` — L2>L3 lift for arnoldi step. Three uncontested primitives plus the variant-dependent `op.orthog` obstruction (which is localised below the step body, not at the body level). Confirms the audit.
- `book/src/spec/slices/cg.md:347-350` (Claim 1, outer-loop obstruction) — the negative L3 result for the *outer* loop. Cited for completeness; the outer-loop obstruction is independent of the step-body rotation handled by this theme.

L2 sink (the eventual target after L3>L2):

- `book/src/L2/krylov-step.md` (cycle-005 firm) — the L2 entry whose body shape matches the L3 form produced by this lowering. The L2 entry's §Semantics body and the L3 form's body are textually equivalent up to wrapper packaging.

Concept-page references (for the dissolved L4 vocabulary):

- `book/src/concepts/state-stratification.md:1-45` — the typed three-stratum record convention this lowering dissolves.
- `book/src/concepts/solve-monad.md:1-69` — the `Solve = StateT SimState Identity` monad this lowering dissolves.
- `book/src/concepts/first-iteration-unrolling.md:21-37` — the Form-A/Form-B distinction this lowering collapses.
- `book/src/concepts/sequential-obstruction.md` — the obstruction classification the L3 outer loop carries (referenced for completeness, not introduced).
- `book/src/concepts/derived-view-hoisting.md` — the demand-pruning algebra preserved across the rotation.

[new]
**Open question disposition**: this dispatch *audits* the cycle-005 open question `krylov-step-l3-identity-in-form-audit` and proposes closing it as **confirmed-with-refinement** — the assertion holds, the framing is sharpened, no L3 row needed. Integrator will mark accordingly; if integration uncovers a non-identity finding (e.g., a corpus check on a slice this dispatch did not re-verify reveals body-level rotation), the question stays open and a cycle-007 L3 row promotion follows.

## Verified-against

L4 source (the input form of this lowering):

- `book/src/L4/krylov-step.md` (wave-1 harvester output, this cycle; the firm L4 entry this lowering applies to) — §Signature (Form A and Form B signatures), §Semantics (body shape, monadic effect placement), §"L4 vs L2 distinction" (the wrapper-vs-composition framing).
- `reports/2026-05-27T080944Z-harvester-krylov-step-L4/CYCLE.md` — the harvester dispatch report carrying the same content plus open questions (caveat 2 on `iterate_while` anchoring, cited above).

L3 evidence (the target form of this lowering, including the identity-in-form audit):

- `book/src/spec/slices/cg.md:341-362` — the combinator-miner cycle-002 evidence for L2>L3 body identity. Claim 2 ("step body lifts as identity") is the cited support. Re-read for this audit; assertion confirmed.
- `book/src/spec/slices/arnoldi_step.md:178-213` — L2>L3 lift for arnoldi step. Three uncontested primitives plus the variant-dependent `op.orthog` obstruction (which is localised below the step body, not at the body level). Confirms the audit.
- `book/src/spec/slices/cg.md:347-350` (Claim 1, outer-loop obstruction) — the negative L3 result for the *outer* loop. Cited for completeness; the outer-loop obstruction is independent of the step-body rotation handled by this theme.

L2 sink (the eventual target after L3>L2):

- `book/src/L2/krylov-step.md` (cycle-005 firm) — the L2 entry whose body shape matches the L3 form produced by this lowering. The L2 entry's §Semantics body and the L3 form's body are textually equivalent up to wrapper packaging.

Concept-page references (for the dissolved L4 vocabulary):

- `book/src/concepts/state-stratification.md:1-45` — the typed three-stratum record convention this lowering dissolves.
- `book/src/concepts/solve-monad.md:1-69` — the `Solve = StateT SimState Identity` monad this lowering dissolves.
- `book/src/concepts/first-iteration-unrolling.md:21-37` — the Form-A/Form-B distinction this lowering collapses.
- `book/src/concepts/sequential-obstruction.md` — the obstruction classification the L3 outer loop carries (referenced for completeness, not introduced).
- `book/src/concepts/derived-view-hoisting.md` — the demand-pruning algebra preserved across the rotation; the §"Worked example: CG residual norm" (lines 14-19) is the canonical §3.8 instantiation for `residual_norm` extras, cited by Condition 5 and the §"What the L3 form for `iterate_while` looks like" §3.8 preamble.

<!-- The narrative §"Verified-against" list above carries the cycle-006 evidence registry (prose-shaped: file + section descriptor); the trailing `verified_against:` YAML block below carries the cycle-007 wave-2 audit's structured evidence trail (per-citation verdict + audited_at + note), per the trailing-YAML precedent at `book/src/L1-L0/axpby-mutation-rotation.md:173-189`. Both lists are intentionally retained: the prose form is the human-readable evidence registry; the YAML form is the machine-checkable audit-trail. -->

verified_against:
  - citation: book/src/L4/iterate-while.md:28-43
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: cycle-007 firm L4 signature explicitly carries trajectory:[{...e}]; cycle-006 L3 rendering correctly omits it per §3.8 collapse but elides the rule-citation. This dispatch adds the citation.
  - citation: book/src/L4/iterate-while.md:123-133
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: Law 1 (trajectory pruning) is the rule that justifies the cycle-006 L3 single-readout rendering for Palace; now cited explicitly in §"What the L3 form for iterate_while looks like" and Condition 5.
  - citation: book/src/L4/iterate-while-with-prev.md:137-147
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: Law 2 of the with-prev chapter lifts the pruning rule to both step bodies; same disposition for the Form B L3 rendering covered by this theme.
  - citation: reference/palace/palace/linalg/iterative.cpp:420-485
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: PCG outer loop retains no per-iteration residual history; final_res, final_it captured as scalars at lines 484-485. Confirms Condition 5 holds for CG.
  - citation: reference/palace/palace/linalg/iterative.cpp:614-705
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: GMRES inner Arnoldi loop same disposition as PCG; per-iteration beta either printed or overwritten; final_res, final_it captured at 703-704. Confirms Condition 5 holds for GMRES.
  - citation: reference/palace/palace/linalg/iterative.cpp:734-870
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: FGMRES structurally identical to GMRES (one more workspace Z[] for flexible-preconditioner Krylov basis); same per-iteration beta discipline. Confirms Condition 5 holds for FGMRES.
  - citation: reference/palace/palace/linalg/iterative.hpp:52-55
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: KSP result-extraction surface is exactly four mutable scalars (converged, initial_res, final_res, final_it); no list-shaped or trajectory-shaped field. Canonical structural evidence that Condition 5 holds in Palace.
  - citation: reference/palace/palace/linalg/iterative.hpp:97-108
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: Four public Get* accessors parallel to the four scalars (GetConverged, GetInitialRes, GetFinalRes, GetNumIterations); no GetResidualHistory() or analogue.
  - citation: reference/palace/palace/linalg/ksp.cpp:296-310
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: Sole caller of KSP result-extraction surface; consumes converged (branch), final_res/initial_res (warning ratio), final_it (counter sum); no per-iteration consumption anywhere in palace/. Operational evidence that Condition 5 holds.
  - citation: book/src/concepts/derived-view-hoisting.md:14-19
    verdict: supports
    audited_at: 2026-05-27T170121Z
    note: §"Worked example: CG residual norm" is the canonical instantiation of the §3.8 pruning for iterate_while's residual_norm extras; cross-referenced from §"What the L3 form for iterate_while looks like" §3.8 preamble and from Condition 5.
```

### 5. EDIT scaffolding/open-questions.md — close OQ iterate-while-l3-rendering-trajectory-accumulation-gap (status flip + cycle-008 closure paragraph)

```edit:scaffolding/open-questions.md
[old]
```yaml
---
slug: iterate-while-l3-rendering-trajectory-accumulation-gap
opened_at: cycle-006
opened_by: abstractor
status: open
relates_to: iterate-while-l4-anchor-missing (cycle-006)
---
```

[new]
```yaml
---
slug: iterate-while-l3-rendering-trajectory-accumulation-gap
opened_at: cycle-006
opened_by: abstractor
status: answered
answered_at: cycle-008
answered_in: reports/2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close/CYCLE.md
relates_to: iterate-while-l4-anchor-missing (cycle-006)
---
```
```

```edit:scaffolding/open-questions.md
[old]
**Cycle-007 wave-2 verdict (audit verdict-(c); status remains `open` pending cycle-008+ lifter)**: the cycle-007 wave-2 lowering-verifier dispatch (`reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/`) audited the gap against the just-firmed L4 chapters and the Palace KSP consumer surface. **Verdict: (c) — L3 single-readout is correct; L4>L3 lowering needs explicit §3.8 collapse-rule citation.** The audit's key L0/L1 findings: (i) Palace's `IterativeSolver` result-extraction surface materializes exactly four scalars (`converged`, `initial_res`, `final_res`, `final_it`) at `reference/palace/palace/linalg/iterative.hpp:52-55` with four getters at `:97-108`; (ii) the sole caller of that surface is `BaseKspSolver::Mult` at `reference/palace/palace/linalg/ksp.cpp:296-310`, consuming exactly those four scalars (branch on `GetConverged`, ratio in warning via `GetFinalRes()/GetInitialRes()`, sum into counter via `GetNumIterations`); (iii) the PCG outer loop (`iterative.cpp:420-485`) and GMRES inner loop (`:614-705`) retain no per-iteration residual history — per-iteration `res`/`beta` is either printed inline under `print_opts.iterations` or overwritten; (iv) no Palace unit test asserts on per-iteration residual values (`test/unit/` directory has no `test-ksp*`/`test-cg*`/`test-gmres*`). The four scalars are all `final_state`-equivalent (carry fields at termination or pre-loop initialization), so Law 1 of `book/src/L4/iterate-while.md` fires and the trajectory collapses to `[]` — the L3 single-readout form is the §3.8-pruned form of the L4 generality, not a different combinator. Both originally-enumerated candidate resolutions are subsumed: (a) [promote L3 to trajectory] was the wrong direction (would have promoted L3 to a trajectory it does not need); (b) [explicit demand-pruning step] was a less-precise framing of verdict-(c). A new applicability **Condition 5** for the cycle-006 theme surfaces from this audit: *"The downstream consumer observes only `final_state`-equivalent quantities of the `iterate_while` invocation; per Law 1 (§3.8 demand-pruning), the trajectory then prunes to `[]` and the L3 form is the single-readout shape."* The full audit including `verified_against:` evidence-block proposal lives in `reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/CYCLE.md`. **Status remains `open`**: the audit produces evidence + verdict but the substantive patch (cite Law 1 + `concepts/derived-view-hoisting.md` §"Worked example: CG residual norm" at `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like"; add Condition 5 to §"Applicability conditions") is out-of-lowering-verifier-authority and routes to a cycle-008+ `lifter` dispatch. Closure becomes appropriate once that lifter patch lands. Orthogonal new OQ `iterate-while-log-effect-vs-trajectory-channel` (cycle-007, opened by lowering-verifier) tracks the unrelated logging-effect channel question.

[new]
**Cycle-007 wave-2 verdict (audit verdict-(c); status remains `open` pending cycle-008+ lifter)**: the cycle-007 wave-2 lowering-verifier dispatch (`reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/`) audited the gap against the just-firmed L4 chapters and the Palace KSP consumer surface. **Verdict: (c) — L3 single-readout is correct; L4>L3 lowering needs explicit §3.8 collapse-rule citation.** The audit's key L0/L1 findings: (i) Palace's `IterativeSolver` result-extraction surface materializes exactly four scalars (`converged`, `initial_res`, `final_res`, `final_it`) at `reference/palace/palace/linalg/iterative.hpp:52-55` with four getters at `:97-108`; (ii) the sole caller of that surface is `BaseKspSolver::Mult` at `reference/palace/palace/linalg/ksp.cpp:296-310`, consuming exactly those four scalars (branch on `GetConverged`, ratio in warning via `GetFinalRes()/GetInitialRes()`, sum into counter via `GetNumIterations`); (iii) the PCG outer loop (`iterative.cpp:420-485`) and GMRES inner loop (`:614-705`) retain no per-iteration residual history — per-iteration `res`/`beta` is either printed inline under `print_opts.iterations` or overwritten; (iv) no Palace unit test asserts on per-iteration residual values (`test/unit/` directory has no `test-ksp*`/`test-cg*`/`test-gmres*`). The four scalars are all `final_state`-equivalent (carry fields at termination or pre-loop initialization), so Law 1 of `book/src/L4/iterate-while.md` fires and the trajectory collapses to `[]` — the L3 single-readout form is the §3.8-pruned form of the L4 generality, not a different combinator. Both originally-enumerated candidate resolutions are subsumed: (a) [promote L3 to trajectory] was the wrong direction (would have promoted L3 to a trajectory it does not need); (b) [explicit demand-pruning step] was a less-precise framing of verdict-(c). A new applicability **Condition 5** for the cycle-006 theme surfaces from this audit: *"The downstream consumer observes only `final_state`-equivalent quantities of the `iterate_while` invocation; per Law 1 (§3.8 demand-pruning), the trajectory then prunes to `[]` and the L3 form is the single-readout shape."* The full audit including `verified_against:` evidence-block proposal lives in `reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/CYCLE.md`. **Status remains `open`**: the audit produces evidence + verdict but the substantive patch (cite Law 1 + `concepts/derived-view-hoisting.md` §"Worked example: CG residual norm" at `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like"; add Condition 5 to §"Applicability conditions") is out-of-lowering-verifier-authority and routes to a cycle-008+ `lifter` dispatch. Closure becomes appropriate once that lifter patch lands. Orthogonal new OQ `iterate-while-log-effect-vs-trajectory-channel` (cycle-007, opened by lowering-verifier) tracks the unrelated logging-effect channel question.

**Cycle-008 closure** (lifter dispatch `2026-05-27T173217Z`): the cycle-008 lifter dispatch on `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (`reports/2026-05-27T173217Z-lifter-krylov-step-typed-wrapper-dissolution-trajectory-close/CYCLE.md`) applied the cycle-007 wave-2 audit's three proposed substantive changes: (1) §"What the L3 form for `iterate_while` looks like" was rewritten with a §3.8 preamble citing Law 1 of `book/src/L4/iterate-while.md` and `book/src/concepts/derived-view-hoisting.md` §"Worked example: CG residual norm", plus a two-form sketch (pruned + unpruned) governed by Condition 5 and exhibiting the L3-side image of Law 1 as a $$ ... $$ reduction rule; (2) §"Applicability conditions" gained a new Condition 5 naming the consumer-demand precondition with Palace-specific evidence (`iterative.hpp:52-55` four-scalar surface + `ksp.cpp:296-310` sole caller); (3) a trailing `verified_against:` block was appended carrying the 10-citation audit evidence base; (4) `Status:` was promoted from `rough-in` to `firm`. The OQ is **closed** as `answered` (status: answered, answered_at: cycle-008, answered_in: the cycle-008 lifter dispatch report). The L3>L2 theme `book/src/L3-L2/krylov-step-body-identity.md` is now auto-eligible for `firm-rough-in` → `firm` promotion via status-inheritance (the upstream L4>L3 theme is now firm); this promotion is not applied by this dispatch and is routed as a cycle-009 integrator-signals suggestion. The orthogonal new OQ `iterate-while-log-effect-vs-trajectory-channel` (cycle-007, opened by lowering-verifier) remains open and is unaffected by this closure.
```

### Note on downstream propagation (NOT applied here — integrator-signals suggestion only)

The L3>L2 theme `book/src/L3-L2/krylov-step-body-identity.md` currently carries `Status: firm-rough-in` with `rough-in` inherited from this upstream L4>L3 theme. With this dispatch promoting the upstream to `firm`, the downstream L3>L2 theme is auto-eligible for `firm-rough-in` → `firm` promotion via the inheritance convention recorded at `scaffolding/open-questions.md:1225` ("promotion to plain `firm` follows automatically when the upstream theme is itself promoted"). This dispatch deliberately does NOT edit `book/src/L3-L2/krylov-step-body-identity.md` — that file is out of this lifter's scope per the lifter role spec ("one theme per invocation"). The propagation is flagged as an integrator-signals "Suggested next dispatches" item for cycle-009 to apply (likely a one-line `Status:` edit on the L3>L2 file plus a brief inheritance-note paragraph; alternatively a tiny lifter dispatch).

## Discipline notes

This is a **pure rewriting pass** per the lifter role spec — the lowering's structure is preserved; the vocabulary firms up against the cycle-007 wave-1 firm L4 entries:

- **No new structural rotation introduced.** The L4 form's signature (`krylov-step :: OpParams -> Krylov -> (SimState -> Solve { sim: SimState', krylov: Krylov', outputs: StepOutputs })`) is unchanged. The L3 form's shape for the Palace-actual consumer pattern is unchanged (the single-readout / no-accumulator form already in the theme is the correct Palace rendering). What changes is the *justification chain*: the L3 form is no longer presented as a stand-alone tail-recursive sketch but as the §3.8-pruned image of the L4 trajectory-carrying form, with the unpruned counterpart shown for completeness and the consumer-demand precondition named as Condition 5.
- **The two-form sketch is not a new variant axis.** Per cycle-007 wave-2 audit's variant-axis-coverage check (`META.md` `variant-axis-coverage: pass`), the L4 combinator is invariant under consumer-demand differences; the L4>L3 lowering's *result shape* depends on consumer demand. Condition 5 is therefore correctly placed as an applicability condition on the lowering, not as a fourth variant axis on the L4 combinator. (The cycle-007 firm L4 `iterate-while.md` enumerates three variant axes — pure-vs-Solve, extras-vs-no-extras, bootstrap-free-vs-carry-bootstrapped — and the consumer-demand axis is structurally outside those.)
- **Pseudo-language preservation per CLAUDE.md L4/L3 invariant.** Both the pruned and unpruned L3 sketches use ` ```text ... ``` ` fenced code blocks with Haskell-style do-notation and lambda forms (`λ(carry, sim) -> ...`); the §3.8 collapse rule uses `$$ ... $$` LaTeX math display. The signatures continue the existing theme's notation conventions (positional tuples for value-threading, no new record syntax introduced). Strawman §3.7 conventions preserved.
- **`verified_against:` block placement.** Trailing-YAML form at end-of-file per the established L1-L0 precedent at `book/src/L1-L0/axpby-mutation-rotation.md:173-189` and `book/src/L1-L0/apply-linop-mutation-rotation.md:353-369`; meta's repair-finding-5 confirmed this is the cycle-006-aligned placement. The 10 citations are exactly the cycle-007 wave-2 audit's verified set (with `iterative.cpp:734-870` for FGMRES included per the audit text at META.md line 35 / CYCLE.md citation 6 notes, which mentions FGMRES at `:734-870` is structurally identical). The repairer's tightening of `book/src/L4/iterate-while.md:222-232` → `:222-224` is preserved (not in the verified_against block since it cites a different range — `:28-43` and `:123-133`).
- **OQ closure rationale.** The cycle-007 wave-2 audit explicitly framed closure as "becomes appropriate once that lifter patch lands" (META.md notes-for-integrator). This dispatch lands the patch; the status flip from `open` to `answered` and the cycle-008 closure paragraph append are mechanical follow-throughs on the audit's deferred closure.
- **Status promotion rationale.** The cycle-006 `rough-in` qualification was specifically gated on (a) L4 vocab promotion of `iterate_while` / `iterate_while_with_prev` (cycle-007 wave-1: done — both firm), and (b) lowering-verifier follow-up confirming L3-form correctness (cycle-007 wave-2: verdict (c), evidence-base 10 citations). Both gates are met. The theme is fully anchored to firm L4 vocabulary; the L3 form is justified by Condition 5 + Law 1 with explicit citations; the speculative-operator section can be read as historical (the rough-in operators are now firm). Promotion to `firm` is the correct status transition. (Note: the §"Speculative L4 operators" section is preserved as-is rather than trimmed — it carries the design history of how the L4 vocabulary was firmed up across cycle-006 wave-2 → cycle-007 wave-1, which is load-bearing context for a reader auditing the promotion path.)

## Supporting evidence

Files read for this dispatch:

- `/home/crutcher/git/palace_whiteroom/book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` — the target file (full read, 217 lines); §"What the L3 form for `iterate_while` looks like" identified at lines 156-167; §"Applicability conditions" at lines 101-113; §"Status" at lines 214-216; §"Verified-against" at lines 189-212.
- `/home/crutcher/git/palace_whiteroom/book/src/L4/iterate-while.md` — full read (235 lines); Law 1 (the §3.8 demand-driven trajectory pruning law) confirmed at lines 123-133; the §"Lowers to" section's explicit deferral to cycle-008+ confirmed at lines 180-198.
- `/home/crutcher/git/palace_whiteroom/book/src/concepts/derived-view-hoisting.md` — full read (40 lines); §"Worked example: CG residual norm" at lines 14-19 confirmed as the canonical §3.8 instantiation for `residual_norm` extras.
- `/home/crutcher/git/palace_whiteroom/reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/CYCLE.md` — full read (300 lines); cycle-007 wave-2 audit with 10-citation evidence base; verdict (c); proposed Change 1/2/3 (Change 1 + Change 2 applied at cycle-007; Change 3 deferred to this cycle-008 lifter dispatch).
- `/home/crutcher/git/palace_whiteroom/reports/2026-05-27T170121Z-lowering-verifier-iterate-while-L3-trajectory-reconciliation/META.md` — full read (106 lines); `overall_status: ready`; repairer tightened `:222-232` → `:222-224` (preserved in the audit citation chain, does not affect the verified_against block in this dispatch); five not-needed findings either stylistic, telemetry, or per-precedent.
- `/home/crutcher/git/palace_whiteroom/book/src/L1-L0/axpby-mutation-rotation.md:1-30,160-189` — verified_against trailing-block precedent.
- `/home/crutcher/git/palace_whiteroom/book/src/L1-L0/apply-linop-mutation-rotation.md:340-369` — second verified_against trailing-block precedent.
- `/home/crutcher/git/palace_whiteroom/scaffolding/open-questions.md:1225-1314` — OQ block for `iterate-while-l3-rendering-trajectory-accumulation-gap` (lines 1227-1241) and the surrounding cycle-007 wave-2 augmentation paragraph; OQ block for orthogonal `iterate-while-log-effect-vs-trajectory-channel` at lines 1306-1314 (not modified).

No new file ranges cited beyond those already in the cycle-007 wave-2 audit's evidence base; the lifter's job is to operationalize the audit's verdict, not to extend its evidence.

## Open questions / caveats

1. **The `verified_against:` block uses bare YAML rather than a wrapped `## Verified-against (audit)` H2.** Both styles are precedented (`axpby-mutation-rotation.md` and `apply-linop-mutation-rotation.md` use trailing-YAML; `bicgstab-iteration.md` wraps in an H2 per cycle-007 wave-2 META.md note-5). The trailing-YAML form was chosen because the theme already has a §"Verified-against" H2 (lines 189-212) carrying the *narrative* evidence list, and the YAML block is the cycle-007 wave-2 audit's *structured* evidence trail. Placing them adjacent (narrative §Verified-against immediately followed by trailing `verified_against:` YAML) matches the L1-L0 precedent more closely than wrapping the YAML in a duplicate-named H2. **Caveat for integrator**: if the integrator prefers H2 wrapping for consistency with `bicgstab-iteration.md`, a one-line wrap is mechanical and can be applied as a repairer-style edit.

2. **The §3.8 collapse rule's $$ ... $$ math display uses the same notation as `book/src/L4/iterate-while.md` Law 1** (the `\frac{ antecedent }{ consequent }` form). This is the canonical strawman §3.8 presentation. The two-form sketch's pruned form uses positional `(carry, sim)` (no `readout` slot in the carry) while the unpruned form uses `(carry, sim, traj)` (with `traj` as the third positional accumulator). The `step_state` definition uses Haskell-style lambda with positional destructuring (`λ(carry, sim) -> let ... in ...`) — consistent with the L4 strawman's body-shape notation. No new notation convention introduced.

3. **L3>L2 inheritance auto-promotion not applied here.** Per the lifter role spec ("one theme per invocation"), the downstream L3>L2 theme `book/src/L3-L2/krylov-step-body-identity.md` is out of scope. The integrator-signals suggestion (flagged in §"Note on downstream propagation" above) is the correct routing channel for a cycle-009 follow-up. A flat lifter-on-L3>L2 dispatch would be the cleanest mechanism (single `Status:` edit + inheritance-note paragraph); alternatively the integrator-per-report could apply it as a mechanical inheritance update during cycle-008 integration. **Caveat for integrator**: if integrating an in-cycle propagation pass, confirm the L3>L2 theme's current status text reads `firm-rough-in` (cycle-007 wave-1 abstractor's wording per `scaffolding/open-questions.md:1225`) before flipping to `firm`.

4. **No primary-content structural decisions were made.** Per the lifter discipline ("If you find yourself making non-trivial content decisions, **stop** and flag in Open questions — likely an abstractor reread is needed"), the dispatch's edits are wholly mechanical re-anchoring: the §3.8 preamble cites pre-existing Law 1 and a pre-existing concept page; the two-form sketch's pruned form is verbatim the existing cycle-006 L3 sketch (modulo positional cleanup matching the strawman pseudo-language); the unpruned form is the direct value-threaded image of the L4 form's small-step rule at `book/src/L4/iterate-while.md:64-88`; Condition 5 is the cycle-007 wave-2 audit's proposed Condition 5 verbatim with Palace-specific evidence inlined. No reformulation of the theme's structure; no new variant axes; no new operator promotion; no evidence pointers broken. The promotion to `firm` reflects the closure of the two gates the cycle-006 `rough-in` qualifier was waiting on.

5. **Codemap MCP tools not invoked.** Per the dispatch directive ("No MCP codemap calls (permission-denied, deferred to cycle-009 meta-phase per user directive)"), all file localization performed via vanilla `Read(offset, limit)` and `Bash(grep)` calls. The MCP server instructions appearing in the inputs section are noted but not invoked, consistent with the dispatch directive.
