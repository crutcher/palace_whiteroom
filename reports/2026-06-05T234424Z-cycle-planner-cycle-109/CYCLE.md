---
agent: cycle-planner
invoked_at: 2026-06-05T234424Z
scope: cycle-109 dispatch plan (batch-35 cycle 1 of 3; LEAD = graded-stack-l2-l1-theme-cohort-grounding)
status: pending
---

# Cycle 109 dispatch plan

## Goals selected this cycle

Execute the batch-35 LEAD `graded-stack-l2-l1-theme-cohort-grounding` (priorities.md item 1): the bounded one-edge-per-theme GROUNDING pass over the ~10 L2-L1 lowering themes that stay `[garbage?]` because the L2/L3 `lowers-to` convention points operator→operator, never operator→theme. **A pre-dispatch on-disk audit (below) materially reshapes the LEAD's "rescues ~10 nodes" estimate into a FAITHFUL-PATH-OR-FINDING split:** only **4 of the 10** themes have an upper-endpoint L2 op that is itself **reachable** — those 4 flip reachable this cycle when the faithful `lowers-to depends-on` edge is added. The other **6** themes have an upper-endpoint L2 op that is **itself unreachable** (the op's own only inbound edges come from unreachable L3 reduce/orthogonalize/iteration ops), so the one-edge fix does NOT flip them — that is the deeper next-tranche finding (the L2 reduce/orthogonalize/chebyshev cohort is off-spine). One of the 6 (`deflate`) is a **demand-gated FRONTIER member on the STOP-PROPOSING list** — not touched. This cycle: ONE `layer-intro-author` dispatch grounds the 4 reachable-op themes (faithful, flips reachable now), lays the cheap faithful edge on `inner_product` (already has an `edges:` block; edge correct even if it does not flip yet), and routes the structured Group-B finding (the L2-op-itself-unreachable root cause + the next-tranche recommendation). Item 2 (`graded-stack-lazy-tail-typing`) is NOT co-scheduled (no clean low-cost disjoint slice this cycle; it stays lazy-tail).

## Linter baseline (live tree this invocation; `fd5fabd` cycle-108)

`python3 tools/graded-stack-lint/graded_stack_lint.py --show-inbound`:

```
files scanned: 355 ; typed nodes: 295 ; untyped (WARNING): 60 ; feature roots: 36
rank histogram: firm 201, typed-no-rank 80, rough-in 5, partly-constructive 3, obstruction 2, partial-obstruction 4
AXIS 1 — RANK VIOLATIONS: none.  (rank_violations = 0)
AXIS 2 — reachable from roots: 102
DETRITUS: 157  (STRONGER GARBAGE SIGNAL = 35 typed-but-unreachable ; edge-untyped pre-P1 artifact = 122)
PROMOTION FRONTIER (8): bicgstab-iteration, eigsolve-convergence-reason-mapping, minres-iteration,
  L2-L1/deflate-composition-lowering, L2/deflate, boundary-mode.{L0,L1,L4}
RESULT: 0 rank violation(s), 157 detritus, 60 untyped.
```

Matches the resume-notes pre-restart baseline exactly (`reachable=102, rank_violations=0, untyped=60, unresolved=0, promotion_frontier=8, detritus=157`).

## Per-theme faithful-edge table (the LEAD's 10 themes; on-disk verified)

Upper endpoint read from each theme's `## L2 form (LHS)` / opening prose. **Reachable?** = is the upper-endpoint L2 op itself root-reachable (so the `lowers-to` edge flips the theme reachable)? Confirmed via `graded_stack_lint.py --show-inbound` garbage-list membership.

| # | L2-L1 theme | upper-endpoint L2 op (host file) | op has `edges:`? | op REACHABLE? | faithful `lowers-to`? | grounding action this cycle |
|---|---|---|---|---|---|---|
| 1 | eigsolve-spectral-transform-composition | L2/eigsolve | YES (`:5`) | **REACHABLE** (←L3/eigsolve) | Y (prose `:171` names the theme) | **GROUND** — add `lowers-to depends-on` |
| 2 | krylov-step-kernel-defusion | L2/krylov-step | NO (pre-scheme) | **REACHABLE** (←L4/krylov-step, L3/krylov-step) | Y (theme LHS = `L2/krylov-step`) | **GROUND** — author `edges:` from scratch incl. `lowers-to` |
| 3 | ksp-solve-outer-driver-unfold | L2/ksp_solve | YES (`:5`) | **REACHABLE** (←L2/eigsolve, L2/divfree-projector, L3/ksp_solve) | Y (theme is the L2↔L1 edge of the firm ksp_solve) | **GROUND** — add `lowers-to depends-on` |
| 4 | linear-combination-fold-specialization | L2/linear_combination | YES (`:5`, has `reference` to theme `:14`) | **REACHABLE** (←L3/linear_combination, L1/assemble_frequency_operator, …) | Y (existing `reference` confirms) | **GROUND** — UPGRADE existing `reference`→`depends-on lowers-to` |
| 5 | inner-product-fold-specialization | L2/inner_product | YES (`:5`, has `reference` to theme `:13`) | **UNREACHABLE** `[GARBAGE*]` (only inbound from unreachable L3/dot, L3/inner_product) | Y | **edge-lay only** (upgrade `reference`→`depends-on lowers-to`) — does NOT flip until inner_product itself grounds → FINDING |
| 6 | chebyshev-iteration-fusion | L2/chebyshev-iteration | NO (pre-scheme) | **UNREACHABLE** `[garbage?]` (only inbound L3/chebyshev, unreachable) | Y | **FINDING** (op off-spine; authoring its `edges:` is next-tranche) |
| 7 | gram-fold-specialization | L2/gram | NO (pre-scheme) | **UNREACHABLE** `[garbage?]` | Y | **FINDING** (op off-spine) |
| 8 | incremental-least-squares-composition-lowering | L2/incremental-least-squares | NO (pre-scheme) | **UNREACHABLE** `[garbage?]` | Y | **FINDING** (op off-spine) |
| 9 | orthogonalize-composition-lowering | L2/orthogonalize | NO (pre-scheme) | **UNREACHABLE** `[garbage?]` | Y | **FINDING** (op off-spine) |
| 10 | deflate-composition-lowering | L2/deflate | NO (pre-scheme) | **UNREACHABLE** `[garbage?]` + **FRONTIER / STOP-PROPOSING** | Y but DEMAND-GATED | **DO NOT TOUCH** (opaque-library/demand-gated frontier member; the redirect forbids forcing it onto the spine) |

**Net rescue this cycle: 4 themes flip reachable** (rows 1-4) — `reachable 102 → 106` expected, `rank_violations` HOLDS 0. Row 5 lays a faithful (correct) edge that will flip when its op grounds. Rows 6-10 route as a structured Group-B finding. Row 10 excluded.

### The Group-B root cause (the finding to route to the batch-35 meta-phase)

The LEAD assumed all 10 themes are detritus for ONE reason (operator→operator-not-operator→theme). On-disk that is true of the *theme edge*, but for **6 of 10** there is a SECOND, dominating reason: the **upper-endpoint L2 op is ITSELF unreachable**, because the only inbound edges to these L2 reduce/orthogonalize/iteration ops come from **L3 ops that are themselves off-spine** (`L3/dot`, `L3/inner_product`, `L3/chebyshev`, `L3/orthogonalize`, `L3/krylov-step` etc. are all in the `STRONGER GARBAGE SIGNAL` / detritus set). Adding `L2/<op> →lowers-to→ theme` from an unreachable op cannot flip the theme — the mark-sweep never reaches the op. So the bounded one-edge fix lands the 4 reachable-op themes cleanly; grounding the other 5 (deflate excluded) is the **next tranche** = grounding the L2 reduce/orthogonalize/chebyshev cohort, which traces up through the unreachable L3 cohort (a larger, structurally-distinct pass — NOT the bounded one-edge-per-theme shape the LEAD scoped). This is a legitimate faithful-path-or-finding outcome, not a failed dispatch.

## Deliverable-presence verification

Per-dispatch four-step check (paste-inline-evidence). D1 is the only content dispatch.

**D1 — `graded-stack-l2-l1-theme-cohort-grounding` (the 4 Group-A op edits + Group-B finding):**
1. **File existence** — all 10 theme files + all 4 Group-A host op files present (`ls -la` exit 0):
   ```
   book/src/L2-L1/{chebyshev-iteration-fusion,deflate-composition-lowering,eigsolve-spectral-transform-composition,
     gram-fold-specialization,incremental-least-squares-composition-lowering,inner-product-fold-specialization,
     krylov-step-kernel-defusion,ksp-solve-outer-driver-unfold,linear-combination-fold-specialization,
     orthogonalize-composition-lowering}.md  → ALL EXIST (12367..41142 bytes)
   book/src/L2/{eigsolve,krylov-step,ksp_solve,linear_combination}.md  → ALL EXIST
   ```
2. **Maturity / already-discharged** — the grounding edge is NOT yet present on any Group-A op:
   - `L2/eigsolve.md`: `edges:` present (`:5`), `depends-on: [L2/ksp_solve, L1/apply_linop]`, `reference:` does NOT include `L2-L1/eigsolve-spectral-transform-composition` → edge ABSENT, dispatch is NOT a no-op.
   - `L2/ksp_solve.md`: `edges:` present (`:5`), `grep ksp-solve-outer-driver-unfold L2/ksp_solve.md` → no matches → edge ABSENT.
   - `L2/krylov-step.md`: NO frontmatter at all (line 1 = `# krylov-step`) → `edges:` authored from scratch → ABSENT.
   - `L2/linear_combination.md`: `edges:` present (`:5`) with `reference: - L2-L1/linear-combination-fold-specialization` (`:14`) — this is a NAVIGATIONAL `reference` (creates NO reachability, the c106-D4 lesson); the grounding requires UPGRADING it to `depends-on lowers-to` → substantive change, NOT a no-op.
   - `L2/inner_product.md`: `edges:` present (`:5`) with `reference: - L2-L1/inner-product-fold-specialization` (`:13`) — same upgrade target.
3. **OQ-ledger RESOLVED-grep** — the migrated OQ `l2-l1-theme-cohort-reachability-gap` is the LEAD's source (migrated to the plan as item 1, NOT closed). `grep 'l2-l1-theme-cohort.*RESOLVED\|l2-l1-theme-cohort.*CLOSED' scaffolding/open-questions.md` → no matches → OPEN, dispatch warranted.
4. **Structural-block check** — gate: the §(g) GROUND-don't-remove disposition (loaded post-restart in `layer-intro-author.md`) + the faithful-edge-or-finding discipline. NO block on the 4 Group-A themes (their op is reachable, the `lowers-to` relationship is real per the theme prose, the op is `rank: firm`/scheme-typed resting on firm L1 so well-foundedness holds firm→firm). The 6 Group-B themes are structurally gated by "the upper op is itself unreachable" → routed as a finding (NOT forced). `deflate` is gated by the STOP-PROPOSING negative list (FRONTIER member) → excluded. Open by construction otherwise (first grounding pass on this cohort; no prior-cycle history for these specific theme edges).

All checks pass for the 4 Group-A grounding edges. No STOP-PROPOSING violation (deflate explicitly excluded; no `promotion_frontier` member proposed as a forward pick). Framing = grounding-disposition (§(g)), correct for the typed-edge campaign.

## Dispatches

**D1 — (`layer-intro-author`, the LEAD: L2-L1 theme-cohort grounding, the bounded reachable-op tranche + Group-B finding, deps: none)**
- **scope:** Ground the 4 L2-L1 themes whose upper-endpoint L2 op is itself root-reachable, by adding a faithful `lowers-to`-kind `depends-on` edge `L2/<op> → L2-L1/<theme>` (block-mapping edge form, mirroring the c108 `L2/divfree-projector` precedent at `book/src/L2/divfree-projector.md:9-13`). **VERIFY each `lowers-to` relationship is REAL from the theme prose before typing** (faithful-path-or-finding):
  - `L2/eigsolve.md` (`edges:` present) — ADD to `depends-on`: `{ target: L2-L1/eigsolve-spectral-transform-composition, kind: lowers-to }` (the theme prose `:171` already names this lowering; it dissolves the per-step `apply_shift_invert` fold body into L1 `apply_linop ▷ ksp_solve`).
  - `L2/ksp_solve.md` (`edges:` present, uses block-mapping `lifts-to`/`lowers-from` form) — ADD to `depends-on`: `{ target: L2-L1/ksp-solve-outer-driver-unfold, kind: lowers-to }` (the theme is the canonical forward-narrated L2↔L1 edge of the firm L2 `ksp_solve`).
  - `L2/krylov-step.md` (NO frontmatter — line 1 is `# krylov-step`) — AUTHOR an `edges:` block FROM SCRATCH (mirror the c108 `L2/divfree-projector` from-scratch authoring): `rank: firm`; `depends-on` = its firm L1 leaves per its own §Dependencies (`book/src/L2/krylov-step.md` body names the 7 firm L1 leaves `apply_linop, axpy, axpby, axpbypcz, dot, nrm2, scal` — confirm the list on-disk before typing) + `{ target: L2-L1/krylov-step-kernel-defusion, kind: lowers-to }`; `reference` = its concept pages (`solver-as-operator`, `sequential-obstruction`, `derived-view-hoisting`, …) + L4/L3 consumers. Well-foundedness: krylov-step is firm resting on firm L1 leaves → holds.
  - `L2/linear_combination.md` (`edges:` present, has `reference: - L2-L1/linear-combination-fold-specialization` at `:14`) — UPGRADE that line: REMOVE it from `reference`, ADD to `depends-on` as `{ target: L2-L1/linear-combination-fold-specialization, kind: lowers-to }` (a navigational `reference` creates no reachability — the c106-D4 lesson; the `lowers-to depends-on` is what flips the theme).
- **ALSO (cheap, faithful edge-lay — does NOT flip reachable):** `L2/inner_product.md` (`edges:` present, `reference: - L2-L1/inner-product-fold-specialization` at `:13`) — UPGRADE `reference`→`depends-on lowers-to` same as linear_combination. State explicitly in the report that this edge is faithful + correct but does NOT flip the theme reachable this cycle because `L2/inner_product` is itself `[GARBAGE*]` (its only inbound is from unreachable `L3/dot`/`L3/inner_product`); it lays the edge for when the inner_product/reduce cohort is grounded.
- **DO NOT TOUCH:** `L2/deflate.md` / `L2-L1/deflate-composition-lowering.md` — demand-gated FRONTIER member on the STOP-PROPOSING negative list (opaque-library `nleps_deflated_*` deps; the redirect forbids forcing it onto the spine).
- **ROUTE AS A FINDING (Group-B, to the batch-35 meta-phase via Open questions):** the 5 themes whose upper-endpoint L2 op is itself unreachable — `inner-product-fold-specialization` (`L2/inner_product`), `chebyshev-iteration-fusion` (`L2/chebyshev-iteration`), `gram-fold-specialization` (`L2/gram`), `incremental-least-squares-composition-lowering` (`L2/incremental-least-squares`), `orthogonalize-composition-lowering` (`L2/orthogonalize`). The faithful `lowers-to` relationship is real for all 5, but the one-edge fix cannot flip them because the **upper op is off-spine** (reached only by unreachable L3 reduce/orthogonalize/iteration ops). Recommend the next tranche: grounding the L2 reduce/orthogonalize/chebyshev cohort (a larger pass that traces up through the unreachable L3 cohort — structurally distinct from the bounded one-edge-per-theme LEAD). Name this OQ `l2-reduce-orthogonalize-cohort-itself-unreachable-blocks-theme-grounding`.
- **VERIFY:** after authoring, re-run `python3 tools/graded-stack-lint/graded_stack_lint.py --show-inbound` and CONFIRM (i) the 4 Group-A themes (`eigsolve-spectral-transform-composition`, `krylov-step-kernel-defusion`, `ksp-solve-outer-driver-unfold`, `linear-combination-fold-specialization`) flip OUT of the `[garbage?]` list (reachable should climb 102→~106); (ii) `rank_violations` HOLDS 0; (iii) the 5 Group-B themes + deflate REMAIN `[garbage?]` (expected — documented as the finding). If any Group-A `lowers-to` relationship is NOT cleanly faithful on a re-read, type only the faithful subset and route the rest as a finding (do NOT force an edge).
- **rationale:** the batch-35 LEAD `graded-stack-l2-l1-theme-cohort-grounding` (priorities item 1); the §(g) GROUND-don't-remove disposition applied as faithful-path-or-finding; drives the `[garbage?]` theme-cohort count down by 4 this cycle and surfaces the deeper L2-cohort-off-spine finding for the meta-phase.

## Overlap analysis

Only ONE content dispatch (D1). No pairwise overlap to analyze. Within D1 the write-set is **5 disjoint frontmatter blocks** (`L2/eigsolve.md`, `L2/ksp_solve.md`, `L2/krylov-step.md`, `L2/linear_combination.md`, `L2/inner_product.md`) — all distinct files, all single-owner (one dispatch), no consolidated-tally collision (per-page frontmatter edits, NOT a cohort-count aggregate). No `book/src/L_n/index.md` running-count touched (pure edge-typing, no chapter landing). No cross-report forward-reference slug divergence (every `lowers-to`/`depends-on`/`reference` target — the 5 theme slugs + krylov-step's 7 firm L1 leaves + its concept pages — is an EXISTING stable slug on disk; no new-slug forward-reference anywhere this cycle). No DUAL-REGISTRATION partition needed (no layer-index landing). The single-dispatch design is deliberate: the whole bounded cohort is small (5 small frontmatter edits + a finding write-up), the host files are disjoint, and one author keeps the `lowers-to` convention applied consistently (the divfree precedent).

## Sequencing schedule

**Single wave (one dispatch).**
- **Wave 1 (D1):** `layer-intro-author` — the L2-L1 theme-cohort grounding (4 Group-A edges + inner_product edge-lay + Group-B finding).

Then the standard tail: critic on D1 → repairer if warn/fail → `integrator-per-report` (×1) → `integrator-finalize` (×1: `cargo make book`, commit+push, cycle-record, log, integrator-signals, roadmap, linter step-5b re-run confirming `reachable` climbs 102→~106 and `rank_violations` HOLDS 0).

## Open questions / caveats

- **The LEAD's "rescues ~10 nodes" is over-estimated by ~6 — the dominant cause for 6 of 10 themes is that the upper L2 op is ITSELF unreachable, not the operator→theme edge convention.** This cycle faithfully grounds the 4 themes whose op is on-spine (the bounded clean tranche) and routes the 5 (deflate excluded) as a structured finding. I have NOT added this re-scope to `priorities.md` mid-batch beyond the plan-tag — flagging it here so the batch-35 meta-phase (fires after c111) can re-rank: the residual L2-L1 theme grounding is gated on a SEPARATE next-tranche pass (grounding the L2 reduce/orthogonalize/chebyshev cohort, which is gated in turn on the unreachable L3 reduce/iteration cohort). New OQ to be filed by D1: `l2-reduce-orthogonalize-cohort-itself-unreachable-blocks-theme-grounding`.
- **`deflate` / `deflate-composition-lowering` correctly stay garbage** — they are a demand-gated FRONTIER member (opaque-library `nleps_deflated_*`); excluding them is the redirect-mandated behavior, not an omission. If the meta-phase ever wants the deflate theme on-spine, that is a demand-gated trigger, not a grounding pass.
- **`L2/inner_product` being `[GARBAGE*]` while it is a high-fan-out combinator is itself notable** — a high-reuse reduce-to-scalar combinator unreachable from any feature root means the reduce cohort (dot/inner_product/nrm2 at L2/L3) has no live `depends-on` path from a driver column. This may be a genuine spine gap (a driver column should `depends-on` a reduce verb somewhere) OR an expected absorbed-below-column situation like the BC/divfree clusters (c107). The Group-B finding should note this for the meta-phase to judge (ground-from-column vs absorbed-detritus-baseline-exception, the c107 disposition pattern).
- **Item 2 (`graded-stack-lazy-tail-typing`) not co-scheduled** — no clean low-cost disjoint slice this cycle; the lazy tail acquires `edges:` as files are next-touched (linters warn-not-fail on untyped). Not forcing a heavy untyped-tail wave to fill a slot (false-throughput).
