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

## cycle-004 — 2026-05-27T005952Z

### Unblocked

- **`krylov-step` L2 harvester promotion** now fully unblocked — `apply_linop` landed firm at L1 in this cycle. Priority #5 in the planner's bootstrap-L1-vocabulary becomes the natural next forward-frontier work. Citation: `book/src/L1/apply_linop.md`; combinator-miner rough-in at `book/src/L2/index.md`.
- **`apply-linop-mutation-rotation` L1>L0 theme** unblocked — the harvester's own Open question #2 flagged this as substantially larger than `axpby-mutation-rotation` (representation-axis caveats, transpose-mode specialisations, accumulating-form fusion, parallel-wrapper). Routes to abstractor. Citation: open question `apply-linop-lowering-theme-scope` (cycle-004).
- **`axpbypcz-mutation-rotation` L1>L0 theme** unblocked — companion to existing `axpby-mutation-rotation`; first L1>L0 theme to mix structural-rebind with algebraic-constant-folding (the `γ == 0` sub-rule). Routes to abstractor. Citation: open question `axpbypcz-mutation-rotation-abstractor-target` (cycle-004).
- **Concepts sweep over `book/src/concepts/`** unblocked — cycle-004 dot rewrite establishes the pattern template; cycle-005 same-layer-cross-cutter can replay against `concepts/axpy.md`, `concepts/nrm2.md`, `concepts/orthogonalization.md`, etc. Citation: open question `concepts-sweep-cycle-005-candidate` (cycle-004), bundles cycle-003 `concepts-pre-layered-era-sweep`.
- **`nrm2_B` energy-norm L1 harvest** unblocked — depends on `apply_linop` (now firm) and `dot` (firm cycle-002). Citation: open question `nrm2-B-weighted-energy-norm-harvest` (cycle-003).

### New dependencies

- **`apply_linop` is the L2 `krylov-step` gate** — the L2 row's dep list (`apply_linop`, `axpy`, `dot`, `nrm2`) is now fully populated at L1 firm tier. Planner: cycle-005 L2 harvester dispatch is no longer blocked by an L1 vocabulary gap.
- **`axpbypcz` subsumes both `axpby` and `axpy`** as L1 siblings — three-way subsumption chain `axpy ≺ axpby ≺ axpbypcz` recorded as algebraic laws (not dep-map edges). Planner: future L2 fusion patterns over coefficient-update lines should consult the `axpbypcz` Law 12 chained-collapse pattern.
- **Two obstruction L1>L0 themes coexist** — `minres-iteration` and `bicgstab-iteration` are the first themes with `justification kind: obstruction`. New theme category introduced this cycle; tooling implications routed to meta-phase (friction-ledger candidate `advertised-but-unimplemented-krylov-solvers`).
- **`scal` subsumption of `axpby` (β=0)** — formalised as algebraic law; both stay in L1 dep-map as siblings.

### Resolution implications

- **`axpby-axpbypcz-next-harvest`** — **answered**. Both halves now firm at L1 (cycle-003 axpby, cycle-004 axpbypcz).
- **`axpbypcz-l1-harvest`** — **answered** by cycle-004 harvester. Mirror of axpby decision; 12 laws; 1 internal-L0 control-flow axis explicitly non-L1.
- **`scal-primitive-l1-harvest`** — **answered** by cycle-004 harvester. Module-axiom laws + scalar-promotion sub-axis.
- **`l1-index-refresh`** + **`l1-index-refresh-trigger-met`** — both **answered** by cycle-004 layer-intro-author refresh. New "Vocabulary cohort" subsection pattern proposed for meta-phase promotion across L_n intros.
- **`concepts-dot-return-type-correction`** + **`concepts-dot-dotc-and-inverted-conjugation`** + **`dot-backpointer-staleness-after-rewrite`** + **`dot-blas-heritage-framing-salvage`** — all **answered** by cycle-004 concepts/dot rewrite + L1/dot back-pointer softening.
- **`scalar-promotion-typing-rule`** — **needs-more**. Now visible across `axpy`, `dot`, `axpby`, `axpbypcz`, `scal` (5 operators stating the same per-operator clause). Well past any reasonable threshold for promotion above per-operator prose. Cycle-planner should escalate as a high-priority dispatch (`layer-intro-author` or new role) for cycle-005 or cycle-006.
- **`concepts-page-authorship-role-scope`** — **needs-more**. Cycle-004 confirmed `layer-intro-author` can handle concept-page rewrites in practice; meta-phase to decide whether to (a) explicitly broaden the role spec or (b) add a new `concept-page-author` role. Cycle-004 follows the cycle-003 precedent.

### Suggested next dispatches

- (`harvester`, `krylov-step @ L2 firm`) — now unblocked; cycle-002 combinator-miner rough-in awaits promotion. L1 vocabulary fully gates this (all four deps `apply_linop`, `axpy`, `dot`, `nrm2` are firm).
- (`abstractor`, `apply-linop-mutation-rotation @ L1>L0`) — harvester flagged the lowering theme will be substantially larger than `axpby-mutation-rotation` (representation-axis + transpose-mode + accumulate-mode + parallel-wrapper). Closes open question `apply-linop-lowering-theme-scope`.
- (`abstractor`, `axpbypcz-mutation-rotation @ L1>L0`) — companion to existing `axpby-mutation-rotation`; introduces the `γ == 0` algebraic-sub-rule as first instance of algebraic-constant-folding inside L1>L0. Closes `axpbypcz-mutation-rotation-abstractor-target`.
- (`cross-layer-cross-cutter`, `krylov-step layer placement`) — cycle-002 open question; can co-bundle with the L2 firm-up to ensure the L2/L4 dual placement decision is made coherently.
- (`meta-phase`, `mfem-as-l0-substrate-policy ask item`) — surfaces to human: should MFEM be admitted as L0 substrate for the MINRES/BiCGStab obstruction themes (and the future `Householder QR` work)? Routes to meta-phase under `ask` decision-kind.
- (`harvester`, `Householder QR @ L1`) — Shared Infrastructure roadmap item; structurally-distinct variant of MGS/CGS/CGS2. Cycle-005 may attempt as harvester with abstractor-obstruction fallback (cycle-004 MINRES precedent says: grep first).
- (`harvester`, `Jacobi smoother @ L1`) — Shared Infrastructure roadmap item; depends on a "diagonal-preconditioner apply" intermediate.
- (`same-layer-cross-cutter`, `book/src/concepts/ sweep`) — cycle-004 dot rewrite is the pattern template; cycle-005 sweep over remaining concepts pages can surface analogous defects.

### Wave-conflict observations

- **Wave-1 of cycle-004 was 7 parallel dispatches** with substantial overlap on L1/index.md (9 row appends from 5 wave-mates) and SUMMARY.md (5 chapter-line appends from 5 wave-mates). **Zero structural conflicts** at integration. **POSITIVE signal that the parallel-when-in-doubt philosophy is working at scale.** The same pattern as cycle-003 (2 wave-mates appending to same files) generalises cleanly to 5 wave-mates. Each row was distinct; the planner's per-row anchor merge plan was unnecessary at integration time — direct dep-map row appends in dep-map row order plus alphabetical SUMMARY ordering Just Worked. Planner cycle-005 can mark **same-file row-level edits as PARALLEL by default** even at higher wave-size.
- **SUMMARY.md L1>L0 Part — alphabetical anchor merge**. Both MINRES and BiCGStab independently proposed `append-after axpby-mutation-rotation`. Planner pre-resolved alphabetically (`bicgstab-iteration` then `minres-iteration`); integrator applied both as adjacent lines. Zero friction at integration.
- **L1/dot.md two-writer pseudo-conflict**. Only `concepts-dot-rewrite` writes to `book/src/L1/dot.md` (a 1-line softening edit at line 17). No other report writes it. Listed in planner conflict analysis but resolved at design time, not integration.
- **L1/index.md two layouts in flight**. The `L1-index-refresh` report rewrote the intro structure (new Context bullets, Semantics, new Vocabulary-cohort subsection) while three harvesters proposed new dep-map rows. Integrator merged: refreshed-intro-prose + dep-map verbatim from refresh + 9 new rows appended (3 firm + 6 rough-in obstruction). Clean composition; the dep-map-preserved-verbatim discipline in the refresh report was load-bearing for this.

### Integration-tooling friction

- **No new gates needed**. Cycle-003's gate set held cleanly for 7 wave-mates: zero retroactive-budget hits, zero edge-label drift, zero forward-edge claims without surface, zero variant-axis-missing on multi-variant operators (apply_linop's 3+1 collapsed axis was correctly classified by the report; axpbypcz's 2+1 internal-L0 axis was correctly classified). H1→H2 normalisation not needed (no reports introduced H1 headings on existing pages). Append-by-slug fallback not needed (no slug typos).
- **Obstruction-theme category needs a tooling decision** at meta-phase: the new `justification kind: obstruction` is unprecedented in `book/src/L1-L0/`. Whether future cross-layer-cross-cutter consumers should treat obstruction themes differently (e.g., skip evidence-walking, surface as "anticipated work") is an open methodology question. Routes to `scaffolding/friction-ledger.md` via meta-phase.
- **Subagent-skipped-Edit pattern recurred** (cycle-002 cycle-planner haiku skipped Edit; cycle-004 abstractor (BiCGStab) skipped Edit despite explicit parent-pre-creates-skeleton workflow). Pattern crossed from haiku to opus tier. Routes to meta-phase as a methodology / prompt-engineering item; tracked under open question `subagent-skips-edit-on-explicit-instruction`.

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
