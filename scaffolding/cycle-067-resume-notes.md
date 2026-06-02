# Cycle-067 resume notes (batch-20 meta-phase → batch-21 kickoff)

**SESSION RESTART REQUIRED before cycle-067.** The batch-20 meta-phase (post-cycle-066) enacted `.claude/agents/` role-spec changes; the parent orchestrator must restart the Claude Code session before dispatching cycle-067 so the new agent definitions load. (The restart also resets the primary conversation context — there is no separate `/compact` step.)

## Agent-defs changed (and why)

All six edits address friction-ledger `codemap-read-range-plus-one-drift-on-brace-boundary` (recurrence-6; the codemap `read_range` +1 drift went 3-of-3 across the FE-source batch, and a NEW finding surfaced: `citecheck --anchor` is BLIND to a range-END / close-brace off-by-one because the anchor token falls inside both candidate ranges — only a deliberate hand-`Read` of the closing brace catches it):

1. `.claude/agents/harvester.md` — appended a `--anchor`-blind-spot sub-bullet under the codemap-localization-only block: confirm any close-brace END line with a direct on-disk `Read`, not `--anchor`.
2. `.claude/agents/abstractor.md` — same `--anchor`-blind-spot sub-bullet.
3. `.claude/agents/lifter.md` — same sub-bullet, framed for the citation-sweep deliverable (cites the c066 D3 three-loci normalization as the worked case).
4. `.claude/agents/layer-intro-author.md` — same sub-bullet, framed for dep-map / cohort-bullet citations.
5. `.claude/agents/lowering-verifier.md` — same sub-bullet, framed for the `verified_against:` no-drift assertion (an END line is NOT discharged by `--anchor` alone).
6. `.claude/agents/cycle-planner.md` — a localization-hint sub-bullet on §77: pre-localized `path:lo-hi` END lines are drift-prone codemap hints, not authoritative; flag close-brace ENDs for the producer to on-disk-confirm.

## Batch-21 lead (CYCLE-067 active head, see `scaffolding/priorities.md`)

`fe-space-sub-spine-tail-cleanup` (LOW-MEDIUM, clean closes) — the 3 batch-20-migrated FE-space follow-ons: `eliminate_*` `DofSet[N]`→`essential_dofs` cross-ref; the `fe-space-construction-rotation` forward-ref→live-link upgrade; `fe_space_hierarchy` pull-gated. Then weigh the §5 strategic-ASK direction (UPWARD-propagation per-entry-warrant-gated / Mesh-wrapper / solver-test-load).

## Open ask to the human (batch-21 frontier direction)

The FE-space front is near its own plateau (3 firm members, consumer re-anchor complete). The batch-21+ direction is an inflection worth a steer — see the meta-phase report §Open ask items.

## ⟢⟢ USER DIRECTIVE 2026-06-02 (post-batch-20-meta, before c067) — L4 IS THE FEATURE SURFACE / BACKEND-LOWERING TARGET

The batch-20 meta-phase §5 strategic ASK is **ANSWERED by the user**: **L4 is the feature surface and the outward backend-lowering target** — its semantics were chosen to align with external GPU-tensor-accelerator + distributed backends, so L4 is ideal for lowering to other backends. **L4 must be COMPLETE over the in-scope feature set.**

- The **assemble half** (FE-assembly + FE-space cohort: `fe_assemble`/`fe_space`/`fe_collection`/`essential_dofs`/`weak_form_term`/`eliminate_*`/`assemble_frequency_operator`) is **stranded at L1** — a hole in the deliverable. **Batch-21 lead (after the item-1 FE-space tail cleanup): LIFT THIS COHORT TO L4** (assemble-fold combinator + construction terms over opaque libCEED/MFEM leaves, the `fold_solve`/`eigsolve` opaque-leaf pattern). Target = L4, NOT L2/L3.
- The NO-L2 warrants bar only L1→L2 *mirrors*; they do NOT close the upward-to-L4 question (intermediate L2/L3 may be identity — non-adjacent rotation; L4 is the destination).
- Re-examine the "no-L4-by-design" calls (BLAS-1 etc.) per-case under this directive.
- Recorded: project memory `project_l4_is_backend_lowering_target`; priorities.md batch-21 active-head banner (supersedes the meta-phase's "(b)→L2/L3" framing).

This directive supersedes the meta-phase's default `(a)→(b)-per-entry-warrant-gated-to-L2/L3`. The c067 planner promotes the FE-cohort→**L4** lift to the batch-21 frontier.

## ⟢⟢ USER DIRECTIVE 2026-06-02 (companion) — BLACK-BOX vs ACCELERATED KERNELS

Two opposite dispositions at the bottom of the stack (full def: project memory `project_blackbox_vs_accelerated_kernels`; concepts page to author early batch-21):

- **Black-box operation kernel → RISES to L4.** No easy decomposition + clean operation surface + heavy non-local iterative value exploration. Permitted-when-necessary-to-lift; a first-class primitive, NOT a failure. Clean surface rises to L4, body opaque (backend supplies impl). Canonical = `eigsolve`; also `ksp_solve`, the FE per-element quadrature leaf, `fold_solve`'s `ode->Step`. POSITIVE reframe of the current `obstruction (opaque-library-ownership)` filing.
- **Accelerated (special-case) kernel → STOPPED LOW; combinator rises.** Exists solely to speed a decomposable common op (a perf-fused special case of a combinator). `axpy`/`axpby`/`axpbypcz`/`scal` → `linear_combination`; `dot`/`nrm2` → `inner_product`. Identify low, tie to combinator, prevent rising.
- **Test:** clean decomposition? No→rises, Yes→stopped-low.
- **Batch-21 consequences:** (i) `linear_combination`/`inner_product` (combinators) must RISE to L4 (currently stop at L3); (ii) the `axpy`/`scal`/`dot`/`nrm2` L2+L3 chapters are over-risen accelerated kernels (2026-06-01 leaf-collapse refactor incomplete — re-examine per-case); (iii) FE-cohort→L4 lift = assemble-fold combinator (rises) + FE quadrature leaf black-box kernel (rises as opaque input).

### Refinement (USER 2026-06-02, same session): keep well-studied named abstractions even though they decompose

The black-box/accelerated split is **three-way, by judgment** — abstraction value, not just "does it decompose":
1. no decomposition + clean surface → **rises** (black-box kernel).
2. decomposes BUT literature-standard + aids downstream-algorithm simplification + literature tie-back → **KEEP-and-RISE** as a named abstraction (kernel tied below; parent combinator rises too — a permitted dual). **Confirmed keeps: `dot`, `nrm2`.**
3. decomposes AND solely-for-speed, no standalone abstraction value → **stopped-low** (combinator rises in its place); `axpy`-family is the per-case candidate.

Correction to the earlier "(ii) axpy/axpby/axpbypcz/scal/dot/nrm2 chapters are over-risen" claim: that was an over-correction. `dot`/`nrm2` are KEEPS (rise, incl. to L4). The `axpy`-family is a per-case demote-vs-keep judgment weighing literature + downstream-simplification value. `linear_combination`/`inner_product` combinators rise to L4 regardless.

## ⟢⟢ USER DIRECTIVE 2026-06-02 (integrate + meta cycles) — mdBook sub-chapter groupings + alphabetical API lists

Full def: memory `feedback_mdbook_subchapter_grouping_and_alpha_api`; priorities.md batch-21 banner.

1. **Group each layer Part's chapters into mdBook sub-chapter groupings BY KIND** (nested in SUMMARY.md, each with an intro page) — make the §Vocabulary-cohort prose groupings structural navigation.
2. **Sort the list-of-API / dep-map tables ALPHABETICALLY** (alpha-within-each-kind-grouping).

- `integrator-per-report`/`finalize`: new SUMMARY entries go INSIDE the right kind grouping; dep-map rows insert in ALPHA position (not append). `layer-intro-author`: authors/maintains group intros + alpha order. `meta-phase`: drives the one-time reorg pass (regroup existing flat SUMMARY + author group intros + alphabetize all dep-map tables) + codifies into role-specs (restart).
- Active immediately via orchestrator per-dispatch prompts (cycle-067+) until role-spec-codified. The one-time reorg is heavy book/-structure work → its own dispatch wave, NOT bundled with a forward-frontier cycle.
- Respects count-ownership/dual-registration (producer adds row in alpha position; count-owner owns tally).
