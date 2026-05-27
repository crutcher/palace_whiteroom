# Integrator → planner signals

Append-only running ledger. The integrator appends a section at the **top** after each cycle's integration commit (newest first). The next cycle's `cycle-planner` reads the most recent ~3 entries as input to dispatch planning.

**User directive (2026-05-27):** the integrator should have a channel to write information used by the planner about next/unblocked/resolution/etc options implied by the integration. This file is that channel.

**Format** (per-cycle section):

```markdown
## cycle-<n> — <ISO-timestamp>

### Unblocked
- <one-line item per now-tractable priority / question> — <citation: priority slug or open-question slug>

### New dependencies
- <one-line edge that landed this cycle> — <citation: report / commit>

### Resolution implications
- <open-question slug> — <answered | partially-answered | needs-more> — <one-line how this cycle's landings bear on it>

### Suggested next dispatches
- (`<agent>`, `<scope>`) — <one-line rationale>

### Wave-conflict observations
- <one-line case where dispatches conflicted at integration; how the integrator resolved>

### Integration-tooling friction
- <one-line case where the integrator hit a gap that better tooling would close>
```

**Discipline:**

- Integrator appends each cycle (prepended at top — newest first).
- Cycle-planner reads top ~3 entries.
- Keep file under ~500 lines; entries older than 10 cycles archive to `scaffolding/integrator-signals-archive/cycle-<n>-<n+9>.md`.
- No other agent writes here. (If meta-phase needs to annotate, append a `<!-- meta-phase: ... -->` HTML comment to the relevant section.)

---

## cycle-003 — 2026-05-27T002354Z

### Unblocked

- **L1 layer-intro refresh** is now tractable — the L1 dep-map has 4 firm operators (`axpy`, `dot`, `nrm2`, `axpby`), passing the ≥3-operator threshold from pilot-1's `l1-index-refresh`. Routes to `layer-intro-author`. Citation: open question `l1-index-refresh-trigger-met` (cycle-003).
- **`concepts/dot.md` rewrite** unblocked: the cycle-003 cross-cutter surfaced three concrete contradictions with evidence, and the L1 `dot.md` is the authoritative target for alignment. Routes to `layer-intro-author` (closest existing fit; meta-phase scope-question pending). Citation: open question `concepts-page-authorship-role-scope`, priority #4.
- **`scal` L1 harvest** unblocked: referenced in `axpby` laws 2/3 as a forthcoming primitive; independently appears in `linalg::Normalize` (`vector.hpp:262-270`) and CG's update lines. Small primitive, no blockers. Citation: open question `scal-primitive-l1-harvest`.
- **`axpbypcz` L1 harvest** unblocked: the `axpby` firm landing + the cycle-003 lowering-verifier audit (which confirmed the `vector.cpp:756` internal `AXPBY+Add` composition) provide the L1 anchor. Citation: open question `axpbypcz-l1-harvest`, closes the second half of `axpby-axpbypcz-next-harvest`.
- **`krylov-step` L2 harvester promotion** approaches tractable: L1 vocabulary now has 4 firm operators (`apply_linop` still missing); priority #5 depends on bootstrap-L1-vocabulary item #1. Once `apply_linop` lands, krylov-step harvester can proceed with stable L1 deps.

### New dependencies

- **`nrm2` depends on `dot` at L1** — `nrm2(x) = √dot(x, x)` (algebraic law 8; the L0 form is literal one-line composition). Planner: future `nrm2` edits should not race with `dot` edits in the same wave. Citation: `book/src/L1/nrm2.md` §Dependencies; commit cycle-003.
- **`axpby` subsumes `axpy` (not depends on)** — siblings at L1 dep-map; L1>L0 lowering theme `axpby-mutation-rotation` covers `axpy`'s three sub-patterns as β=1 specialisation. Citation: `book/src/L1/axpby.md` §Dependencies + `scaffolding/decisions/axpby-as-primitive.md`.
- **`axpby-mutation-rotation` theme is now `verified_against:`-stamped** — future `cross-layer-cross-cutter` queries can rely on the per-citation YAML block to consume verdicts. Citation: `book/src/L1-L0/axpby-mutation-rotation.md` §Verified-against (cycle-003 append).

### Resolution implications

- **`axpby-axpy-scal-decomposition-decision`** — **answered**. Cycle-003 harvester chose fused primitive; rationale recorded in `scaffolding/decisions/axpby-as-primitive.md`. The `axpby-mutation-rotation` theme requires no retraction (already assumed fused form).
- **`axpby-lowering-verifier-audit`** — **partially-answered**. Cycle-003 lowering-verifier audited all 8 cited L0 ranges (all `supports`); coverage verdict `partially-supported` with ~25 uncited corpus sites and 3 defined-not-used L0 forms enumerated. Theme content correct; exhaustive corpus indexing deferred to a future cycle (see new open question `axpby-corpus-coverage-exhaustive-indexing`).
- **`concepts-dot-return-type-correction`** + **`concepts-dot-dotc-and-inverted-conjugation`** — **needs-more**. Cycle-003 cross-cutter confirmed all three contradictions concretely (return-type, non-existent `Dotc`, bogus `vector.cpp:142-178` citation) and routed to cycle-004 `layer-intro-author` for the rewrite. The questions remain open until the cycle-004 rewrite lands.
- **`l1-index-refresh`** — **needs-more**. The threshold (≥3 firm L1 operators) is now met (4 firm). New open question `l1-index-refresh-trigger-met` (cycle-003) names the actionable dispatch.
- **`scalar-promotion-typing-rule`** — **needs-more**. Now visible across `axpy`, `dot`, `axpby` (cycle-003 harvester counts three operators stating the same per-operator clause); the typing-rule lift is approaching threshold for promotion above per-operator prose. Cycle-planner may want to escalate priority.

### Suggested next dispatches

- (`layer-intro-author`, `rewrite concepts/dot.md to align with L1/dot.md`) — closes the three cycle-003 contradictions; cycle-004 dispatch the cross-cutter explicitly routed. Bundle with the L1 layer-intro refresh below for one role's two outputs.
- (`layer-intro-author`, `refresh book/src/L1/index.md intro + dep-map prose now that 4 firm operators exist`) — `l1-index-refresh-trigger-met` (cycle-003) names this dispatch. Low-medium scope; can co-bundle with the `concepts/dot.md` rewrite under the same role invocation.
- (`harvester`, `scal @ L1`) — small primitive; referenced in `axpby` laws 2/3; closes cycle-003 open question `scal-primitive-l1-harvest`. Forward-frontier work; closes a pending cosmetic-update obligation on `axpby.md`.
- (`harvester`, `apply_linop @ L1`) — bootstrap-L1-vocabulary priority #1; gates `krylov-step` harvester (#5) and `nrm2_B` (cycle-003 open question `nrm2-B-weighted-energy-norm-harvest`). High-value forward-frontier work; substantial L0 surface (`mfem::Operator::Mult`, `palace::ParOperator::Mult`, `linalg::Operator`) — may want subdivision (cycle-planner to assess).
- (`harvester` or `slice-author`, `MINRES @ L0→L1`) — Shared Infrastructure priority #8 (user directive 2026-05-27: shared infra raised above per-solver pipelines). Roadmap §Shared infrastructure / Krylov solvers; symmetric-indefinite three-term recurrence. New ground; substantial L0 surface — likely candidate for two-step harvest (operator-level dispatch first, then L1 form).

### Wave-conflict observations

- **`book/src/L1/index.md` row-anchor case.** nrm2 and axpby harvesters both edited the L1 dep-map in the same wave. Original nrm2 REPORT proposed a full-file replacement (would have silently overwritten axpby's row-replacement edit); cycle-003 repairer caught this pre-integration and rewrote nrm2's edit as `append-after dot row`. At integration time the two edits were non-overlapping at the row level — planner's "sequential" call was over-cautious. Useful signal: cycle-planner can mark same-file row-level edits as PARALLEL when the rows differ. Integrator action: applied both edits to the dep-map cleanly (axpby row-replaced; nrm2 row appended after dot).
- **`book/src/SUMMARY.md` anchor-line case.** Both harvesters wanted to append a new chapter entry immediately after the existing `- [dot](./L1/dot.md)` line under "L1 — Mutation-Lifted Forms" Part. Two chapter entries appended in sequence — auto-resolved cleanly by chaining (nrm2 first, axpby second; matching dep-map row order). Integrator action: applied both lines in one Edit. Useful signal: SUMMARY.md anchor-collisions where both wave-mates simply add lines are zero-friction at integration; planner can mark these PARALLEL by default.

### Integration-tooling friction

- **`verified_against:` YAML-in-prose embedding** — the cycle-003 lowering-verifier's `verified_against:` block is YAML inside an mdBook chapter, with no fenced code block delimiter; downstream parsers (`cross-layer-cross-cutter`) are expected to extract by leading-keyword scan. No spec exists in `scaffolding/` or `.claude/agents/` for this convention. Routes to meta-phase: decide (a) fenced code block, (b) explicit channel-format spec, or (c) sidecar `.yaml` file. Cycle-003 integrator landed the YAML as proposed (per repairer/critic acceptance); flagging here for meta-phase tooling decisions. Citation: open question `lowering-verifier-yaml-in-prose-channel-format` (cycle-003).
- **No other integration-tooling friction observed** this cycle. All four reports' proposed-changes blocks parsed cleanly (one `edit:` with new-file content, two `append-after:` with explicit anchors, one in-place row-replacement). No safety-net gate hits. Build rebuild ran clean. The user-directive philosophy (parallel-when-in-doubt, conflict-as-signal) worked as designed on its first cycle.

---
