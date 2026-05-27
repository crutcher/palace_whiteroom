---
agent: combinator-miner
invoked_at: 2026-05-27T21:55:35Z
scope: Pattern reuse audit — `check_stop_into_carry` 3-condition convergence helper across Palace Krylov-family solvers (MCP codemap pilot retry)
status: integrated
integrated_at: 2026-05-27T230802Z
integration_commit: 30119eb
integration_notes: Applied via integrator-per-report pass 6 of cycle-010 (wave-2 #6). **MCP CODEMAP PILOT SUCCESS** — 14 tool calls (list_files × 2, search_text × 7, get_file_subtree × 1, read_range × 4), 0 permission-denied. First post-cycle-009-meta-phase pilot under commit `ceb87da` enablement. Validates option (a) enablement decision; friction-ledger entry `mcp-codemap-permission-denied-across-batch-1` is now resolution-candidate (meta-phase cycle-012 enacts the ledger entry update). **Inspection-only dispatch** — no `book/` mutation. Verdict: defer-with-routing on FGMRES sister-algorithm match (lower-edge reading). Cycle-009 OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker` held `open` with `last_revisited: cycle-010`; new OQ `fgmres-inner-loop-iterate-while-migration-lifter-candidate` promoted with explicit lifter-before-harvester sequencing directive for cycle-011 planner. Friction signals forwarded: `dispatch-brief-drift` recurrence-1 (eps.cpp/feast.cpp non-existent; MCP corrected); `localize-then-read` skill candidate (observation only; not promoted from integrator authority).
---

# CYCLE: Combinator candidate reuse audit — `check_stop_into_carry`

## Summary

The cycle-008 abstractor proposed `check_stop_into_carry` as a speculative L4 helper to hoist the GMRES inner-loop's 3-condition stop test (`converged || j + 1 == max_dim || it + 1 == max_it`) into the Krylov carry's `stop_reason` field, with promotion deferred until "second reuse found" (see `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md`, §Speculative L4 operators). This dispatch audits Palace's other Krylov-family and iterative-solver inner loops for the same structural fingerprint. **Verdict: one strong identical-pattern reuse site found (FGMRES, `palace/linalg/iterative.cpp:824`), structurally identical to the GMRES site at line 645; all other iterative-solver inner loops in `palace/linalg/` have *different* shapes (2-condition CG, 2-condition power iteration, single-condition Chebyshev fixed-degree, externally-delegated ARPACK/SLEPc convergence, multi-break nleps Quasi-Newton).** Per the "second reuse" promotion criterion this is **borderline pass**: GMRES is the originating site, FGMRES is one true reuse — only **two instances of the identical 3-condition fingerprint exist in Palace**, both inside the same translation unit on the same `GmresSolverBase`-shaped iteration. Recommendation: **defer-but-prepare** — file the reuse evidence as a `lifter` candidate, route formalization to cycle-011 (next batch) after the upstream `book/src/spec/slices/gmres.md` §L4 v0.6→v0.7 self-rotation lands, but do not promote the helper as a general L4 combinator on the strength of one structural twin in a single solver-family pair.

## Pattern instances

The pattern under audit: **3-condition stop test on `(converged_flag, restart_basis_full, global_iter_max)` evaluated together inside a Krylov inner loop, gating both a `break` and a status-write.**

- **Instance 1 (originating site — GMRES inner loop):** `palace/linalg/iterative.cpp:644-649` —
  ```
  converged = (beta < eps);
  if (converged || j + 1 == max_dim || it + 1 == max_it)
  {
    it++;
    break;
  }
  ```
  Inside `GmresSolver<OperType>::Mult` (line 544); this is the v0.6 form abstracted in the cycle-008 `gmres-inner-loop-iterate-while-migration` theme.

- **Instance 2 (FGMRES inner loop — structural-fingerprint-identical reuse):** `palace/linalg/iterative.cpp:823-828` —
  ```
  converged = (beta < eps);
  if (converged || j + 1 == max_dim || it + 1 == max_it)
  {
    it++;
    break;
  }
  ```
  Inside `FgmresSolver<OperType>::Mult` (line 734). The disjunct order, the `j + 1 == max_dim` restart-basis test, the `it + 1 == max_it` global-iteration test, the `converged` boolean source, and the `it++; break;` action are **textually identical** to the GMRES site modulo the surrounding function. Strongly suggests both forms would lower to the same `check_stop_into_carry` helper after the v0.6→v0.7 self-rotation.

- **Non-instance — CG (`palace/linalg/iterative.cpp:418-465`):** 2-condition only. Loop is `for (; it < max_it && !converged; it++)` (line 427); convergence is a single boolean `converged = (res < eps)` re-evaluated at the bottom of the body (line 463). There is **no restart-basis test**, no `j + 1 == max_dim` disjunct, no `it + 1 == max_it` lookahead, no status enum. Divergence is handled by `CheckDot` *throwing* on a non-positive denominator (lines 446, 462), not by a status-set enum. Structural fingerprint: **different-pattern** (2-condition + throw-on-divergence vs. 3-condition + status-via-carry).

- **Non-instance — Power iteration (`palace/linalg/operator.cpp:662-684`):** 2-condition only. Loop is `while (it < max_it)`; convergence is `res < tol` checked inside via an inner `break` (line 678). No restart basis, no divergence test, no status enum.

- **Non-instance — nleps Quasi-Newton (`palace/linalg/nleps.cpp:589-650`):** 4-exit loop with a *streak-counter* divergence test (`diverged_it > 10`, line 636), convergence-and-record-update (line 601), and outer fall-through on `it >= nleps_it`. Different shape — each exit independently breaks rather than feeding into a single 3-condition disjunct.

- **Non-instance — ARPACK / SLEPc eigensolvers (`palace/linalg/arpack.cpp`, `palace/linalg/slepc.cpp`):** Convergence is delegated to the external library via `EPSSetTolerances` / `iparam`-based ARPACK reverse-communication. Palace itself never evaluates the 3-condition disjunct on these — the structural fingerprint is opaque behind the upstream API. Out of scope for `check_stop_into_carry` reuse.

- **Non-instance — Chebyshev / distrelaxation (`palace/linalg/chebyshev.cpp`, `palace/linalg/distrelaxation.cpp`):** Fixed-degree polynomial smoothers with no convergence test at all (`search_text` returned zero hits for `converged|max_it|max_iter` in both files).

**Tally:** 2 strong instances (GMRES + FGMRES), 5+ non-instances. The "second reuse found" criterion is **satisfied at exactly the bar — one originating site + one identical twin**, both in the same `iterative.cpp` translation unit, both on the GMRES-family iteration shape.

## Proposed combinator (already proposed in cycle-008; this dispatch is a reuse audit, not a new proposal)

- **Slug**: `check-stop-into-carry`
- **Layer**: L4 (per cycle-008 abstractor's classification — pure scalar comparison + record update; L3-native lowering with identity-in-form per `gmres-inner-loop-iterate-while-migration.md` §"Audit of cycle-002 identity-in-form claim")
- **Signature sketch** (from cycle-008 rough-in entry in `book/src/L4-L3/index.md`):
  ```text
  check_stop_into_carry :: OpParams -> Convergence -> Krylov -> Int -> Krylov
    -- output is input Krylov with stop_reason field updated to Just _ or Nothing
  ```
- **Algebraic intuition**: idempotent (applying twice yields the same `stop_reason`); pure record update over the disjunction of three predicates; identity-in-form preserved under L4>L3 lowering.
- **Variant axes**: the **predicate disjunction members** (converged-bool / basis-full-int / iter-max-int) and the **carry's `stop_reason` codomain shape** (`Maybe StopReason` vs. a richer status-tag with reason discrimination).

## Proposed changes

This report does NOT propose a new dep-map entry — `check_stop_into_carry` is already a rough-in in `book/src/L4-L3/index.md` (cycle-008 abstractor) and `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` Speculative-L4-operators section. This dispatch instead provides the **reuse-evidence ledger** that informs the cycle-010 / cycle-011 planner's promotion decision.

**Routing recommendation (no `book/src/` mutation):**

- **Decision**: **defer-with-routing** to cycle-011. Two structurally-identical instances inside one translation unit on a single solver-family pair (GMRES + FGMRES) is the **minimum bar** for "second reuse found" but is weaker than the cross-solver-family reuse the cycle-008 rough-in's promotion-criterion language implicitly anticipated (e.g., reuse in CG, in MINRES, in an eigensolver inner Krylov). The pattern is real and the helper is well-shaped, but promoting on the basis of a single GMRES/FGMRES twinning risks fixing the helper's signature to the GMRES-specific Krylov carry record before any genuinely different consumer has stress-tested it.

- **Cycle-010-or-011 lifter dispatch scope** (when scheduled): re-anchor the cycle-008 `gmres-inner-loop-iterate-while-migration` theme against an upstream firm `book/src/spec/slices/gmres.md §L4 v0.7` form (currently still v0.6 inline; located at lines 1012 and 1106 of that slice), then apply the same migration theme as a separate `fgmres-inner-loop-iterate-while-migration` (or unify both under a parameterized theme) and verify that **both lowerings produce a structurally identical `check_stop_into_carry` callsite shape**. If they do, that is the second-reuse formalization. If they diverge (e.g., FGMRES's `pc_side` differences leak into the predicate), the helper's signature needs revision before promotion.

- **Cycle-planner directive**: do NOT schedule a `harvester` on `book/src/L4/check-stop-into-carry.md` until at least one of (a) the FGMRES theme is firmed with the helper at the same callsite shape as GMRES, or (b) a genuinely different consumer (a non-`GmresSolverBase` Krylov form, e.g. a future MINRES literature-anchored L1 form) is identified. The 2-instance evidence does not yet justify promoting the helper to firm L4 vocabulary.

## Supporting evidence

- **Originating site (GMRES inner loop):** `palace/linalg/iterative.cpp:644-649` (3-condition test); function definition `palace/linalg/iterative.cpp:544` (`GmresSolver<OperType>::Mult`).
- **Reuse site (FGMRES inner loop):** `palace/linalg/iterative.cpp:823-828`; function definition `palace/linalg/iterative.cpp:734` (`FgmresSolver<OperType>::Mult`).
- **Cycle-008 prior art:** `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` (Speculative L4 operators section; promotion-criterion language: "defer until second reuse"); `book/src/L4-L3/index.md` rough-in row.
- **Non-instance evidence (CG):** `palace/linalg/iterative.cpp:418-470` — 2-condition loop guard at line 427; throw-on-divergence at lines 446, 462 via `CheckDot`.
- **Non-instance evidence (nleps Quasi-Newton):** `palace/linalg/nleps.cpp:589-650` — 4-exit loop with streak-counter divergence at line 636.
- **Non-instance evidence (power iteration):** `palace/linalg/operator.cpp:662-684`.
- **Non-instance evidence (eigensolver delegation):** `palace/linalg/slepc.cpp:559-563, 1047-1051, 1398-1402` — convergence handed off to PETSc/SLEPc via `*SetTolerances` (the `SlepcEPSSolverBase::SetMaxIter`, `SlepcPEPSolverBase::SetMaxIter`, `SlepcNEPSolverBase::SetMaxIter` thunks); `palace/linalg/arpack.cpp:231-234, 271` — ARPACK reverse-communication (`SetMaxIter` thunk at 231-234; `iparam[3] = 1; // Block size` at line 271; the surrounding `iparam` block at 268-273 set the maxiter slot via `iparam[2] = (a_int)arpack_it` at line 270).
- **Empty hits (Chebyshev / distrelaxation):** `mcp__palace-codemap__search_text` returned zero hits for `converged|max_it|max_iter` in `palace/linalg/chebyshev.cpp` and `palace/linalg/distrelaxation.cpp`.

## Open questions / caveats

### MCP codemap pilot evaluation (primary friction-signal payload)

**MCP tools used successfully across the entire dispatch — no permission-denied errors.**

Tool-call inventory:
- `mcp__palace-codemap__list_files` — 2 calls (glob `palace/linalg/*.cpp` and `*.hpp`).
- `mcp__palace-codemap__search_text` — 7 calls (convergence-keyword sweep across `palace/linalg/iterative.cpp`, `arpack.cpp`, `slepc.cpp`, `nleps.cpp`, `chebyshev.cpp`, `distrelaxation.cpp`, `divfree.cpp`, plus a `^(int|void|bool).*Solve|::Solve\(|::Mult\(|::Iterate` pattern to enumerate solver entry points).
- `mcp__palace-codemap__get_file_subtree` — 1 call (`palace/linalg/iterative.cpp` at `max_depth=2`).
- `mcp__palace-codemap__read_range` — 4 calls (3 ranges in `iterative.cpp` for CG/GMRES/FGMRES inner loops, 1 range in `nleps.cpp` for the Quasi-Newton loop, 1 range in `operator.cpp` for power iteration — five reads total).

Total MCP tool calls: **14**. Equivalent vanilla `Grep` + `Read` workflow would have required roughly the same call count (1 enumeration `ls`, 6-7 `Grep` calls for the convergence sweep, 4-5 `Read` calls for the inner-loop ranges), so **call-count parity** with the baseline. The MCP advantage was qualitative, not quantitative:
1. **`search_text` glob-restriction** kept hit-sets tight (the `chebyshev.cpp` / `distrelaxation.cpp` zero-hit results were one call each and ruled out non-instances cheaply).
2. **`list_files` with glob** returned a clean inventory that immediately corrected the dispatch brief's outdated reference to `palace/linalg/eps.cpp` and `palace/linalg/feast.cpp` — neither file exists; the actual eigensolver implementations are `arpack.cpp` / `slepc.cpp` / `nleps.cpp`, with shared header `eps.hpp`. This early correction prevented wasted scope.
3. **`get_file_subtree` at depth 2** confirmed the file is a single anonymous-namespaced translation unit and surfaced the line numbers of the namespace block without reading any source — useful for orienting the line offsets.
4. **`read_range` discipline** kept source consumption focused: 4 ranges totaling ~250 lines read, vs. the ~880-line `iterative.cpp` that a vanilla `Read` would have ingested in one shot.

No latency concerns observed. No tool returned a stale or incorrect result. The pilot is **clearly successful for this dispatch shape** (pattern-reuse audit across a directory).

**Friction-signal observations for meta-phase:**
- One small ergonomic note: `search_text` snippets are single-line, which is fine for ripgrep-style triage but means follow-up `read_range` is almost always needed to see the disjunct shape. This is by design (the tool docstring explicitly says so) — flagged here only as a structural observation, not a complaint.
- The MCP tool inventory is well-aligned with the **localize-then-read** discipline encoded in the role spec. The server-instructions note from the harness ("use list_files / get_file_subtree / get_symbol_def / get_call_sites / list_dependencies / search_text to localize before reading; read_range is the only source-returning tool") matches how the dispatch naturally flowed.
- **Recommendation to cycle-010+ planner:** make MCP codemap tools the default localization path for combinator-miner / cross-cutter / lowering-verifier dispatches whose scope is "audit pattern X across directory Y." For dispatches whose scope is "formalize operator Z" (harvester) the cost-benefit is less clear because the read-set is narrow and pre-known; vanilla `Read` may still be appropriate.
- **Dispatch-brief drift signal (surfaced as friction-ledger candidate by repairer cycle-010):** the dispatch brief cited `palace/linalg/eps.cpp` and `palace/linalg/feast.cpp` (both non-existent — only `eps.hpp` shared header exists; actual implementations are `arpack.cpp` / `slepc.cpp` / `nleps.cpp`). MCP `list_files` corrected the brief on first call. **This is a candidate friction-pattern for the meta-phase ledger** — "cycle-planner reads stale file inventory and propagates non-existent files into dispatch briefs"; recurrence-1 in this batch (below the meta-phase pattern-promotion threshold of recurrence-2), but worth ledger-tracking because MCP localization makes the correction cheap-and-visible going forward. Distinct friction signal from the broader MCP-pilot-success payload above.

### Substantive caveats (non-MCP-related)

- **The "second reuse" criterion is mechanically satisfied but qualitatively weak.** GMRES and FGMRES share a common ancestor in the literature (FGMRES is "GMRES with right-preconditioning allowed to vary per iteration"); their inner loops are *expected* to share the 3-condition structural fingerprint. A genuinely independent reuse (e.g., in a future MINRES or IDR(s) form) would strengthen the promotion case substantially. The cycle-008 abstractor's promotion-criterion language was ambiguous on whether GMRES/FGMRES twinning counts; this dispatch defaults to "yes, but the bar is the lower edge."
- **Palace does NOT implement MINRES, BiCGStab, IDR(s), or other Krylov family members beyond CG / GMRES / FGMRES.** The dispatch brief mentioned "FGMRES, IRBL, IDR(s)" but `iterative.cpp` and `ksp.cpp` show only the implemented set (`CgSolver`, `GmresSolver`, `FgmresSolver`). MINRES and BiCGStab are present only as **stub enum cases that abort** (per cycle-006 obstruction documentation in `palace/linalg/ksp.cpp:53-56`), and per the project's **Unimplemented Palace stub policy** (see CLAUDE.md §Scope) they are not direct implementation targets. IRBL and IDR(s) do not appear anywhere in the Palace codebase. The structural population of potentially-reusing Krylov solvers in Palace is therefore exactly **{CG, GMRES, FGMRES}** — and CG's shape is different. **The cycle-008 promotion-criterion's "second reuse" search space is intrinsically narrow in this codebase.**
- **The cross-solver-family generalization the helper needs is forward-looking.** If `check_stop_into_carry` is to earn promotion to firm L4 vocabulary on its merits, it likely needs reuse-evidence from a *literature-anchored* L1 form (per the **Unimplemented Palace stub policy** clause: "the literature-anchored L1 form may inform higher abstractions") — e.g., a MINRES inner-loop L1 sketch that demonstrates the same 3-condition shape. The cycle-011+ planner should consider whether to schedule a `harvester` dispatch on a *literature-anchored* MINRES or BiCGStab inner loop specifically to test the helper's generality — not to extend Palace, but to validate the helper's L4 shape against a second algorithmic family.
- **Identity-in-form caveat on the L3 side.** Both GMRES and FGMRES inner loops lower to identity-in-form L3 worker shapes per the `krylov-step-typed-wrapper-dissolution`-parallel rotation in `gmres-inner-loop-iterate-while-migration.md`. This means the 2-instance GMRES/FGMRES reuse is "twin reuse" at the *callsite shape* level but does not stress the helper's signature in any new dimension. A reuse in a non-GMRES-family Krylov method would.

### Out-of-scope but observed

- **CG's `CheckDot`-on-denominator throw-on-divergence pattern** (`palace/linalg/iterative.cpp:446, 462`) is itself a recurrent helper across CG and GMRES/FGMRES — `CheckDot` is called from multiple solver inner loops with very similar contracts (validate a scalar inner product / norm is non-negative-and-finite, throw otherwise). This is a *different* pattern from `check_stop_into_carry` (it raises an exception rather than writing a carry-field), but it is a candidate for its own combinator-miner dispatch in a future cycle. **Not proposed in this report** (one pattern per invocation per role spec; surfaced here as a drive-by observation per the relaxed problems/ bar).
