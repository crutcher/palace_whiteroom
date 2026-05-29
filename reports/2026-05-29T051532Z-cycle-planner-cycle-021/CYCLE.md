---
agent: cycle-planner
invoked_at: 2026-05-29T051532Z
scope: cycle-021 dispatch plan
status: pending
---

# Cycle-021 dispatch plan

## Goals selected this cycle

Cycle-021 (third and final primary cycle of meta-batch-5) closes high-fan-out BLAS-1 L1>L0 lowering themes that every solver depends on, unblocks L2 `ksp_solve` maturity-gradient inversion via firm promotion, and executes the large gmres-sibling fgmres lifter held explicitly for this cycle. The batch-5 meta-phase will follow this cycle's integrator-finalize commit, so the plan leaves intake in clean shape (integration-signals suggest-next dispatches folded into this cycle's roster).

## Dispatches

| # | Agent | Scope | Dependencies | Rationale |
|---|-------|-------|---|-----------|
| 1 | lifter | `fgmres-inner-loop-iterate-while-migration` L4>L3 theme firm re-anchor | none | Held explicitly from cycle-020 (integrator-signals "unblocked" + "suggested next"); gmres sibling rotation landed firm cycle-020, making fgmres now re-anchorable to firm precedent. Closes a large carry-forward (batches 2/3/4). **Fan-out:** unblocks all downstream Krylov L2/L3 work. |
| 2 | harvester | `L2/ksp_solve` outer-driver stub→firm | none | Cycle-020 integrator-signals "unblocked" + "suggested next"; L3 `ksp_solve` now firm, maturity-gradient inversion (L3 firm above L2 stub) warrants reversal. Substantive non-identity rotation (L3>L2 theme warranted per integrator-signals note). **Fan-out:** gates the `L3-L2/ksp-solve-outer-driver` theme + all per-solver pipeline drivers (5 solvers wrap `ksp_solve`). |
| 3 | abstractor | `L3-L2/ksp-solve-outer-driver` L3>L2 theme firm | #2 | Integrator-signals "suggested next" (gated on #2); cycle-020 notes theme is WARRANTED (L3>L2 rotation substantive). **Fan-out:** closes gap between firm L3 inventory and L2 lowering surface for the krylov-step / ksp_solve kernel/driver architecture. |
| 4 | abstractor | `axpby-mutation-rotation` + `axpbypcz-mutation-rotation` L1>L0 themes firm | none | Integrator-signals "suggested next" (explicit line); remaining BLAS-1 L1>L0 lowering-floor closure (dot/scal/nrm2/assemble-diagonal all firmed cycle-019/020). Both rough-in stubs exist at `L1-L0/index.md` + SUMMARY. Pairs with the lowering-verifier audit (#9 below) to close the BLAS-1 family. **Fan-out:** completes foundational lowering coverage every solver lowering theme reuses. |
| 5 | combinator-miner | `deflate` / `gram` deflation-subspace combinator candidate | none | Cycle-020 integrator-signals "unblocked" + "suggested next"; nleps.cpp recurrent `X[j]ᴴ·` projection pattern (:522, :529, :568) is a combinator-miner target. Pins conjugation convention at combinator boundary. **Fan-out:** supports NLEPS lowering (dispatch #7) + future polynomial preconditioner variants. |
| 6 | same-layer-cross-cutter | `orthog.hpp:35` `LocalDot`+`GlobalSum` unweighted-inner-product surface audit | none | Cycle-020 integrator-signals "unblocked" + "suggested next"; second unweighted inner-product surface (out of Dot-caller census), likely Condition-5 coverage gap extension. Routes to a harvester anchor follow-up OR in-line elevation to L1 if trivial. **Fan-out:** closes the Condition-5 Gram-Schmidt coverage gap. |
| 7 | harvester | NLEPS at L1+ (large carry-forward, sustained context) | none | Cycle-020 integrator-signals "suggested next"; multi-cycle carry-forward (plan carried-forward from earlier batches); blocks `check_stop_into_carry` L4 promotion + eigsolve substantive lowering. Requires sustained per-operator context. **Fan-out:** unblocks iterate-while/eigsolve L4 promotion pathway + all NEP solver coverage. |
| 8 | layer-intro-author | L2 Part-intro refresh (`book/src/L2/index.md` Working-Notes + dep-map) | none | Cycle-020 integrator-signals "unblocked" + "suggested next"; L2 now at 5 firm ops (cycle-019 `orthogonalize` + cycle-020 `inner_product`) + 2 live-linked stubs (`ksp_solve` stub→firm this cycle via #2, `incremental-least-squares`); two converging refresh flags fold into one. **Fan-out:** narrative clarity for the fold-cohort + L2 vocabulary status. |
| 8b | lowering-verifier | `axpby-mutation-rotation` + `axpbypcz-mutation-rotation` audit (`verified_against:` block) | #4 | After #4 lands firm themes, audit per-line dispatch rules + mutation surface-form exhaustiveness. **Fan-out:** validates the BLAS-1 lowering floor. Non-blocking (themes are firm on structure; audit confirms coverage). |
| 9 | harvester | `L3/eigsolve` kernel+driver pair L3 backfill | none | Cycle-020 integrator-signals "unblocked next-inventory item"; mirrors the krylov-step kernel / ksp_solve driver split; `trsv` stays blocked (no L1 anchor). Backlog priority per cycle-009 "lower-vocabulary priority" + cycle-010 audit: L3 one of the thinnest layers (needs weight). **Fan-out:** next major L3 inventory backfill (first non-identity after ksp_solve). |

---

## Overlap analysis

**Non-overlapping groups:**

- **Group A (parallel):** Dispatches #1 (lifter, fgmres theme) + #2 (harvester, L2 ksp_solve stub→firm) + #5 (combinator-miner, deflate/gram) + #6 (same-layer-cross-cutter, orthog.hpp surface) + #7 (harvester, NLEPS L1+) + #8 (layer-intro-author, L2 intro) + #9 (harvester, eigsolve L3) — each operates on a distinct file region; no shared operators or artifact edits.

- **Group B (sequential after #4):** Dispatch #4 (abstractor, axpby/axpbypcz themes) must complete before #8b (lowering-verifier audit) can run (audit consumes the firmed theme file).

- **Group C (sequential after #2):** Dispatch #3 (abstractor, L3-L2/ksp-solve-outer-driver theme) depends on #2 (L2 ksp_solve must be firm before the lowering theme can narrate its L3→L2 rotation).

**Potential wave-1 conflicts (minor, acceptable per conflict-tolerance philosophy):**
- None. Group A is purely parallel.

---

## Sequencing schedule

**Wave 1 (all parallel, 1 hour):** Dispatches #1, #2, #5, #6, #7, #8, #9.
- All operate on distinct files (different operators, different themes, different layers).
- Integrator-per-report reads disk before each edit; serial per-report dispatch + append-only patterns handle any multi-report appends to shared indices cleanly (as validated cycle-019/020).

**Wave 2 (after wave-1 reports land, 1 hour):** Dispatch #3 (depends on #2 landing firm).
- Once #2's proposed-changes block lands and integrator writes `book/src/L2/ksp_solve.md` firm, #3 can author the L3>L2 theme anchored to the now-firm L2 entry.

**Wave 3 (after #4 lands, 30 min):** Dispatch #8b (depends on #4 landing firm).
- Once #4's proposed-changes blocks land and integrator writes the axpby/axpbypcz themes firm, the lowering-verifier can audit the per-line rules against the now-firm chapter bodies.

---

## Open questions / caveats

**Dispatch #6 (orthog.hpp:35 surface):**
- Codemap verification located `LocalDot` callers at `palace/linalg/orthog.hpp:35` (confirmed; it is a real site, likely in an Orthogonalize / CGS variant code path).
- The "LocalDot+GlobalSum" framing in integrator-signals is descriptive (unweighted inner-product composed via local + global phases). The actual code structure requires reading `orthog.hpp:35` context to confirm whether this surfaces as a distinct L1 primitive candidate or warrants a citation-only audit into an existing operator's variant-axis.
- Recommend: same-layer-cross-cutter to read the site + classify; if it unearths a new primitive, route to a harvester follow-up; if it is a variant axis of `dot` or `inner_product`, inline-elevate the citation into the appropriate operator's entry.

**Dispatch #7 (NLEPS L1+):**
- NLEPS is large and carries forward across batches; this dispatch assumes 2-3 hours sustained per-operator context. If the token budget per dispatch tightens, the integrator's cycle-record will signal whether a split into two smaller cycles is warranted.
- Blocked completion: `check_stop_into_carry` L4 promotion and the eigsolve substantive lowering pathway both depend on NLEPS landing firm at L1.

**Batch-5 meta-phase immediately follows integrator-finalize:**
- This is the final primary cycle of the batch. The integrator-finalize commit closes the cycle-021 integration and immediately triggers the batch-5 meta-phase (cycles 019/020/021 aggregate).
- All cycle-021 intake (open-questions, friction-ledger entries, forward-refs) should be left clean — no unresolved forward-pointer dangling or stale plan items — so the meta-phase can execute its unification pass on a coherent ledger.

**Dispatch #8b (lowering-verifier) placed in Wave 3 but queued here:**
- The dispatch roster is 9 items (plus the 8b lowering-verifier). If the planner prefers to keep the primary roster ≤12 and treat audits as a separate follow-on phase, this is acceptable; the integrator-signals suggest-next list does NOT explicitly call out the lowering-verifier audit, so it is a secondary/implied follow-up.
- Recommend: include #8b in the dispatch if density allows (it is a small audit, ~30 min); defer to a potential cycle-021.5 or cycle-022 if context is tight.

---

## Plan updates

Marked the following cycle-021 dispatches in `scaffolding/priorities.md`:

**Cycle-020 "Now" entries (all completed cycle-020; cleared per active-head focus discipline):**
- Dispatches #1–#6 completed and removed from active head.

**Cycle-021 "Now" entries (active head; picked from backlog High tier):**
- **ksp-solve-l2-promotion-non-identity-substantive-gap** → dispatch #2 (harvester).
- **l3-vocabulary-inventory-gap** (ksp_solve constituent) → dispatch #3 (abstractor, L3-L2 theme + #9 harvester, eigsolve L3).
- **fgmres-inner-loop-iterate-while-migration** held → dispatch #1 (lifter).
- **blas1-l1-l0-lowering-theme-gap** (axpby/axpbypcz remainder) → dispatch #4 (abstractor).

**Backlog items carried forward (not this cycle, but next-ranked):**
- **gmres §L4 self-rotation** — cycle-020 completed; removed from backlog.
- **matrix-weighted-norm + bilinear-form firm-promotion** — held Medium fan-out, cycle-020 re-ranked to lower priority pending the axpby/axpbypcz BLAS-1 close.
- **normalize-l1-primitive-harvest** — Medium fan-out, retained backlog.

**New plan-candidate from integrator-signals:**
- **deflate/gram combinator candidate** — appended to backlog High tier (fan-out: NLEPS + polynomial preconditioner variants).
- **orthog.hpp:35 LocalDot+GlobalSum surface** — appended to backlog High tier (fan-out: Condition-5 coverage gap closure).

All dispatches map to the highest-fan-out active/backlog items from `priorities.md` per the planner's read (cycle-020 integrator-signals "Suggested next dispatches" section mirrors the plan ranking; cycle-021 roster is a realization of that suggestion).
