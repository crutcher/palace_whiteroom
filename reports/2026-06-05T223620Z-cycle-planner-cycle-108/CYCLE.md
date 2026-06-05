---
agent: cycle-planner
invoked_at: 2026-06-05T223620Z
scope: cycle-108 dispatch plan
status: pending
---

# Cycle 108 dispatch plan

Cycle-108 is the **THIRD / BATCH-CLOSING** primary cycle of meta-batch-34 (cycles 106/107/108); the batch-34 meta-phase fires AFTER this cycle's finalize, aggregating 106/107/108. NO session restart since c106 (mid-batch); context continuity holds. c107 landed `24c3e71`.

## Goals selected this cycle

Discharge the **ONE carried follow-up** (`lowering-chain-liveness-not-propagated-to-l1-ops`, c107 D1 routed OQ) as a systematic `lowers-to` typed-edge **GROUNDING** pass down the BC + divfree lowering chains — per the 2026-06-05 grounding directive, the L1/L0 lowering homes are genuine absorbed dependencies of already-reachable L_{n+1} goal nodes, so we GROUND them by typing the missing `edges:` on the intervening PRE-SCHEME chapters (NOT delete/file-detritus, NOT force a misclassifying constituent edge). Co-schedule the **single deferred c107 D2 node** (`concepts/counter-update` rank + depends-on typing). Batch-closing land-clean discipline: two disjoint dispatches, one wave, leaving the meta-phase a clean reachability picture.

## Deliverable-presence verification (paste-inline-evidence)

Linter baseline this invocation (`python3 tools/graded-stack-lint/graded_stack_lint.py`):
```
RESULT: 0 rank violation(s), 163 detritus node(s), 61 untyped (warning).
```
`--show-inbound` confirms the carried-gap nodes are unreachable:
```
[GARBAGE*] L1-L0/set-subvector-zero-mutation-rotation
[GARBAGE*] L1/eliminate_essential_bc
[GARBAGE*] L1/eliminate_rhs
[GARBAGE*] L1/essential_dofs
[garbage?] L1-L0/divfree-projector-mutation-rotation
[garbage?] L1/divfree-projector
[garbage?] L2-L1/divfree-projector-leaf-identity
  L2/divfree-projector  <-  L3/divfree-projector        (reachable inbound — but L2 has NO frontmatter, dead-ends the sweep)
  L3/divfree-projector  <-  feature/eigenmode.L4        (REACHABLE goal node, grounded c107)
```

### D1 — lowering-chain-liveness grounding pass (8–9 chapters)

1. **File existence** (`ls`):
```
EXISTS: book/src/L4-L3/bc-elimination-post-composition-dissolution.md
EXISTS: book/src/L1/eliminate_essential_bc.md
EXISTS: book/src/L1/eliminate_rhs.md
EXISTS: book/src/L1/essential_dofs.md
EXISTS: book/src/L2/divfree-projector.md
EXISTS: book/src/L1/divfree-projector.md
EXISTS: book/src/L2-L1/divfree-projector-leaf-identity.md
EXISTS: book/src/L1-L0/divfree-projector-mutation-rotation.md
EXISTS: book/src/L1-L0/essential-dofs-construction-rotation.md
EXISTS: book/src/L1-L0/fe-operator-assemble-mutation-rotation.md   (D1 only confirms eliminate_rhs's edge here)
```
2. **Maturity / already-discharged check** — the deliverable is `edges:` typing, NOT maturity promotion. On-disk frontmatter state (first-line / `edges:` grep):
   - `L4-L3/bc-elimination-post-composition-dissolution.md` — has frontmatter (`justification_kind: structural`), **NO `edges:` block** → grounding NOT yet applied.
   - `L1/eliminate_essential_bc.md` — has `---` frontmatter, **NO `edges:` block** (legacy keys) → not applied.
   - `L1/essential_dofs.md` — has `---` frontmatter, **NO `edges:` block** → not applied.
   - `L1/eliminate_rhs.md` — HAS `edges: depends-on lowers-to → L1-L0/fe-operator-assemble-mutation-rotation` (D1 only confirms/leaves; partial).
   - `L2/divfree-projector.md` — first line `# divfree-projector`, **NO frontmatter at all** → this is the c107 mark-sweep dead-end.
   - `L1/divfree-projector.md` — has `---` frontmatter, **NO `edges:` block**.
   - `L2-L1/divfree-projector-leaf-identity.md`, `L1-L0/divfree-projector-mutation-rotation.md`, `L1-L0/essential-dofs-construction-rotation.md` — first line `# <title>`, **NO frontmatter at all**.
   All deliverables are OPEN (the grounding edges are absent on disk).
3. **OQ-ledger RESOLVED-grep** (`grep -c 'lowering-chain-liveness-not-propagated-to-l1-ops.*RESOLVED\|...CLOSED'`): `0` matches → the carried OQ is OPEN (routed follow-up, opened c107 D1).
4. **Structural-block check** — NOT blocked. This is edge-typing on existing firm chapters; no maturity-promotion gate applies. The `lowers-to` relationships are documented in the chapter prose (the dissolution theme's §"Operator-side"/§"RHS-side" name the L1 sources `:35,:61,:100,:134`; the divfree L2/L2-L1 chapters narrate the `WeakDiv → ... → Grad` lowering). No STOP-PROPOSING slug touched. The grounding directive (2026-06-05) explicitly licenses this kind of edge.

D1 = **OPEN, 4/4 checks pass.**

### D2 — `concepts/counter-update` node-typing

1. **File existence**: `EXISTS: book/src/concepts/counter-update.md`.
2. **Maturity check** — read the page: it has NO `## Status` line, NO `rank:`, NO `edges:` frontmatter (it is the c107 D2 deferral — held out of the 15 `reference`-only edits because it ratified→NODE and needs a `rank:`). Deliverable (rank + depends-on + reference) is ABSENT → OPEN.
3. **OQ-ledger RESOLVED-grep**: the OQ `concepts-counter-update-needs-node-rank-and-depends-on-edges` is OPEN (opened c107 D2, "DEFERRAL", recommended-resolution = a batch-34 node-typing dispatch) — no RESOLVED/CLOSED marker.
4. **Structural-block check** — NOT blocked. The OQ records "no DAG node carries a typed `depends-on: concepts/counter-update` today" (confirmed: `--show-inbound | grep counter-update` returns nothing) → no live rank/liveness risk; the deferral was purely "do not guess a rank without a dedicated pass." This dispatch IS that dedicated pass. Reference targets verified present: `concepts/state-stratification.md`, `L4/preconditioning-framework.md`, `L3/krylov-step.md` all EXIST.

D2 = **OPEN, 4/4 checks pass.**

Neither dispatch is on the STOP-PROPOSING negative list (`lu_solve`/`back_solve`/`ls-update-column`/the 4 NLEPS atoms — none touched). No `promotion_frontier` obstruction-/demand-gated member proposed.

## Dispatches

1. **agent**: `layer-intro-author`
   **scope**: **The carried lowering-chain-liveness grounding pass — type the missing `edges:` blocks down the BC + divfree lowering chains so the already-reachable L4/L3 goal nodes propagate liveness to their L1/L0 lowering homes.** Verify each `lowers-to`/`uses`/`cites-evidence` relationship is REAL from the chapter prose before typing (these are documented lowerings, not invented edges). **(BC chain — dissolves DIRECTLY L4→L1, the theme warrants "no interposed L3/eliminate_bc entry" `:105,:114-119`):** (i) `L4-L3/bc-elimination-post-composition-dissolution.md` — add `edges: depends-on` with `lowers-to` → `L1/eliminate_essential_bc`, `L1/eliminate_rhs`, `L1/essential_dofs` (named as the L1 dissolution sources at `:35,:61,:100,:134`); the theme is REACHABLE (`← L4/eliminate_bc lowers-to`), so this flips the 3 L1 BC ops reachable. (ii) `L1/eliminate_essential_bc.md` + `L1/essential_dofs.md` — add `edges:` blocks (legacy frontmatter, no `edges:`) with `lowers-to` → their `L1-L0` themes (`eliminate_essential_bc`→`L1-L0/fe-operator-assemble-mutation-rotation`; `essential_dofs`→`L1-L0/essential-dofs-construction-rotation`) + `cites-evidence` L0 + `reference` siblings; `L1/eliminate_rhs.md` already carries its `lowers-to` edge → confirm/leave. (iii) `L1-L0/essential-dofs-construction-rotation.md` — author `edges:` from scratch (no frontmatter) as a lowering-theme leaf (`cites-evidence` L0). **(divfree chain):** (iv) `L2/divfree-projector.md` — author `edges:` from scratch (NO frontmatter — this is the c107 dead-end): `rank: firm`-floor, `depends-on lowers-to → L1/divfree-projector` + `reference → {L2-L1/divfree-projector-leaf-identity, L3/divfree-projector}`. (v) `L1/divfree-projector.md` — add `edges:` block with `lowers-to → L1-L0/divfree-projector-mutation-rotation` + `cites-evidence` L0 + `reference`. (vi) `L2-L1/divfree-projector-leaf-identity.md` + `L1-L0/divfree-projector-mutation-rotation.md` — author `edges:` from scratch as lowering-theme leaves. Block-mapping edge form. **Re-run `python3 tools/graded-stack-lint/graded_stack_lint.py --show-inbound` and CONFIRM** the L1 nodes flip reachable (`L1/divfree-projector`, `L1/eliminate_essential_bc`, `L1/eliminate_rhs`, `L1/essential_dofs`, + the L2-L1/L1-L0 themes leave garbage) and `rank_violations` HOLDS 0. **faithful-path-or-finding:** if any `lowers-to` is NOT cleanly faithful on re-read, type only the faithful ones and route the rest as a finding — do NOT force.
   **deps**: none
   **rationale**: Discharges the ONE carried OQ `lowering-chain-liveness-not-propagated-to-l1-ops` (c107 D1 routed follow-up; priorities item-1 residual). The grounding directive (2026-06-05) licenses typing these `lowers-to` edges to ground the absorbed L1/L0 lowering homes from their reachable L_{n+1} sources. fan-out: MEDIUM (grounds the whole L1/L0 BC+divfree lowering-home tail; closes the last carried P1 reachability gap; clean meta-phase picture).

2. **agent**: `layer-intro-author`
   **scope**: **Type `concepts/counter-update.md` as a NODE (rank + depends-on + reference)** — the single c107 D2 deferral. The batch-33 §5 reconciliation ratified `counter-update`→NODE (sole-definition home of the L2 `counter_update` primitive; no `L1/L2 counter-update` operator chapter exists). Read the page: it carries a fully-specified `## L2 form` (`c ← c + δ` in-place primitive), a `## State classification` basis (`state-stratification`), and named consumers (`preconditioning-framework`; also `L3/krylov-step`, `L1-L0/ksp-solve-mutation-rotation` per the OQ). Judge `rank:` against this firm small-primitive apparatus (fully-specified L2 form + classification basis + ≥2 consumers reads `firm` by the firm-on-positive-structure logic; if the producer judges the apparatus insufficient, assign the most-conservative defensible rank and STATE the basis — do NOT invent firmness). Author the `edges:` block: `depends-on (kind: classifies)` → `concepts/state-stratification` (classification basis) + `reference` → use-sites (`L4/preconditioning-framework`, `L3/krylov-step`). Re-run the linter; `untyped` drops 1, `rank_violations` HOLDS 0.
   **deps**: none
   **rationale**: Resolves OQ `concepts-counter-update-needs-node-rank-and-depends-on-edges` (c107 D2 deferral; priorities item-3c residual). NO live rank/liveness risk today (no DAG node carries a typed `depends-on: concepts/counter-update`). Small, clean, disjoint — ideal batch-closing co-schedulable. fan-out: LOW.

## Overlap analysis

- **D1 ∩ D2**: D1 writes `{L4-L3/bc-elimination-post-composition-dissolution, L1/eliminate_essential_bc, L1/essential_dofs, L1-L0/essential-dofs-construction-rotation, L2/divfree-projector, L1/divfree-projector, L2-L1/divfree-projector-leaf-identity, L1-L0/divfree-projector-mutation-rotation}.md` (optionally confirms `L1/eliminate_rhs.md`). D2 writes `concepts/counter-update.md` ONLY. **DISJOINT write-sets** — D1 touches NO `concepts/` page; D2 touches NO lowering-chain chapter. → **NOT overlapping; parallel.**
- **Shared-index / consolidated-tally**: NONE. Both dispatches author per-page frontmatter `edges:` blocks; neither writes a layer-index Working-Notes count or any cohort aggregate. No consolidated-tally owner needed.
- **Dual-registration partition**: N/A — no §Vocabulary-cohort bullet / dep-map TABLE row is authored this cycle (pure edge-typing on existing chapters).
- **Cross-report forward-reference slug divergence**: NONE. Every `lowers-to`/`depends-on`/`reference` target is an EXISTING stable slug already on disk (verified: all 11 D1 targets + D2's `state-stratification`/`preconditioning-framework`/`krylov-step` present). NO new-slug forward-reference anywhere this cycle → no inter-dispatch slug-coordination needed.

## Sequencing schedule

**ONE wave — both dispatches parallel (D1, D2).** Disjoint write-sets, no forward-reference coupling, no shared tally. Per the conflict-tolerance philosophy, even the trivial worst case is parallel.

Pipeline after the producer wave: 2 critics (parallel) → repairers as needed → `integrator-per-report` ×2 (serial) → ONE `integrator-finalize` (rebuild book + linter step-5b re-run + commit + push + cycle-end housekeeping). The reachability rescue is verified at finalize step-5b (`reachable` should climb past 95 as the L1 BC+divfree ops flip; `rank_violations` HOLDS 0; `untyped` drops ~1+ from D2 plus the newly-typed pre-scheme chapters).

## Open questions / caveats

- **D1 faithful-path-or-finding latitude is REAL, not pro-forma.** The BC dissolution theme genuinely dissolves L4→L1 (no interposed L3/L2 BC entry — warranted on-disk). If the producer finds, on re-read, that a specific `lowers-to` is a `reference`-grade navigational pointer rather than a liveness-carrying dissolution, it should type it as `reference` and route the residual liveness gap as a finding to the batch-34 meta-phase — that is a clean outcome, not a failed dispatch. The expected outcome is a clean rescue (the prose evidence for the L1-source dissolutions is strong), but the discipline holds.
- **`L1-L0/set-subvector-zero-mutation-rotation` is ALSO `[GARBAGE*]`** (shown in the baseline) — it is reached via `L1/set_subvector_zero` (already reachable, grounded c107) → it should flip when `L1/set_subvector_zero`'s own `lowers-to → L1-L0/set-subvector-zero-mutation-rotation` edge is typed. I did NOT scope this into D1 (it is the set_subvector_zero chain, not the BC/divfree chains, and the `set_subvector_zero` L1 entry's frontmatter state is unverified this cycle). If D1's chain-typing momentum makes it cheap to also type `L1/set_subvector_zero`'s `lowers-to` edge, that is in-spirit — but I leave it as a NOTE for the meta-phase rather than scoping it, to keep D1 bounded and the batch-closing cycle clean. **Flagging for the batch-34 meta-phase: the set_subvector_zero L1-L0 leg is a sibling instance of the same lowering-chain-liveness pattern and may want a one-edge follow-up if D1 does not absorb it.**
- **No third filler dispatch.** The standing forward frontier is exhausted (all `promotion_frontier: 8` members obstruction-/demand-gated; the redirect forbids a rectangular pull-up). Batch-closing discipline keeps the big standing campaigns (lazy-tail typing, linter-reader bug) with the meta-phase that fires next. Two clean dispatches discharging the two open carried items is the right batch-closing shape.
- **Latent items for the batch-34 meta-phase (NOT dispatched, carried):** the block-mapping-misparse linter-reader bug (c106 D5 OQ, latent); the `detritus`-total misleading-single-cycle-signal observation (c107 finalize §integration-tooling-friction — recommend a linter `totals` split of typed-non-node-detritus vs newly-orphaned); the lazy-untyped tail (26 L0 + 26 meta-reviews + methodology/design/SUMMARY); the set_subvector_zero L1-L0 sibling leg (above); the grounding-vs-route-vs-baseline-exception disposition codification (the 2026-06-05 directive, proven across c107/c108 — wants METHODOLOGY-GRADED-STACK.md + role-spec codification).
