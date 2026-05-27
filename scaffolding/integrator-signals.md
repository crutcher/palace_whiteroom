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

## cycle-007 — 2026-05-27T171702Z

**Meta-batch context**: first primary cycle of meta-batch-1 under the new 3:1 meta cadence (cycles 007/008/009 form batch-1; meta-phase fires after cycle-009 finalize, NOT after this cycle).

### Unblocked

- **`lifter` on `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`** unblocked (CYCLE-008 PRIORITY) — cycle-007 wave-2 lowering-verifier delivered verdict (c) closing the iterate-while L3 trajectory-collapse gap conceptually. The substantive patch needs lifter authority: apply (a) Change 2 `verified_against:` 10-citation block (trailing-YAML-block placement per L1-L0 precedent `apply-linop-mutation-rotation.md:353` / `axpby-mutation-rotation.md:173`); (b) Change 3 substantive §3.8-citation patch at §"What the L3 form for iterate_while looks like" — cite Law 1 + `concepts/derived-view-hoisting.md` §"Worked example: CG residual norm", replace 9-line code-block sketch with two-form sketch (pruned vs unpruned), add Condition 5 to §"Applicability conditions". Low-cost single-file edit. Upon landing, OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` becomes closeable; cycle-007's L3>L2 `krylov-step-body-identity` firm-rough-in auto-promotes to plain `firm` via status-inheritance. Citation: cycle-007 wave-2 STAGING row + OQ verdict.
- **`abstractor` on `ksp_solve @ L1>L0`** unblocked — first L1 entry with a structured opaque primary argument (`KspSolver<OperType>*` typed pointer). Theme would document the constructed-operator-absorption + workspace-pattern lowering rotation. Citation: open question `ksp-solve-mutation-rotation-l1-l0-theme` (cycle-007).
- **`layer-intro-author` on L1/index.md refresh** unblocked — `ksp_solve` introduced Vocabulary cohort 7→8 + new Semantics motif 4 (Constructed-operator absorption). L1 intro Context bullets, Semantics motifs, and Working Notes already updated by report #2; a follow-up dispatch could refresh the cross-cutting framing now that the cohort has reached 8 firm entries spanning two distinct motif categories. Citation: open question `l1-intro-refresh-after-constructed-operator-gate` (cycle-007).
- **`same-layer-cross-cutter` on 5 L0 chapters carrying stale forward-declaration italic notes** unblocked — cycle-007 L1 thinning sweep flagged stale `*Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11).*` notes in 5 L0 chapters (now post-sweep). Targets: `output-arg-vs-receiver.md:36`, `mfem-vector-types.md:42`, `linalg-free-functions.md:47`, `transparent-vs-load-bearing-tricks.md:34`, `apply-linop-overload-set.md:55`. Bundlable into one short housekeeping dispatch. Citation: cycle-007 report #3 STAGING notes.
- **`layer-intro-author` on L0 bootstrap bundle 4** unblocked — eigensolver-wrapper candidate identified by cycle-007 report #1 OQs. Citation: open question `eigensolver-wrapper-l0-bundle-4-candidate` (cycle-007).
- **`abstractor` on GMRES-inner-loop iterate-while migration** unblocked — both iterate-while L4 anchors now firm; GMRES inner Arnoldi loop's predicate-in-body pattern is a natural migration target. Citation: open question `gmres-inner-loop-iterate-while-migration` (cycle-007).
- **MCP codemap rollout decision** scheduled — deferred to cycle-009 meta-phase per user directive (cycle-007 pilot result: permission-denied; rollout not actionable until cycle-009 meta-phase aggregates evidence). Cycle-008 planner does NOT yet treat MCP tools as preferred for C++ source-localization.

### New dependencies

- **L4 `iterate_while` (firm) + `iterate_while_with_prev` (firm)** depend on 4 concept-page entries each (`solve-monad`, `derived-view-hoisting`, `convergence-test`, `first-iteration-unrolling`). Second instance of the concept-deps-on-L4-rows convention established cycle-006 (krylov-step). The `l4-row-vs-concept-dependency-convention` OQ (cycle-006) now has 3 L4 firm chapters following the pattern; meta-phase / future L4 harvesters can either ratify the convention or shift to L4-rows-must-depend-on-L4-rows.
- **L4 `krylov-step` dep-map row's Dependencies cell extended** to list `iterate_while` + `iterate_while_with_prev` as 2 new L4-row dependencies (Form A body folds via iterate_while; Form B body uses iterate_while_with_prev). Re-anchors cycle-006's cross-row dependency from concept-pages to L4-rows for the iterate-while case specifically. **First L4-row-on-L4-row dependency edge in the artifact.**
- **L3>L2 `krylov-step-body-identity` (firm-rough-in)** depends on L4 `krylov-step` (firm, cycle-006), L4>L3 `krylov-step-typed-wrapper-dissolution` (rough-in, cycle-006), L2 `krylov-step` (firm, cycle-005), plus 5 concept pages. **First L3>L2 theme** in the artifact; first instance of the `firm-rough-in` status pattern (inherits upstream theme's `rough-in` status until the upstream firms).
- **L1 `ksp_solve` (firm)** depends on L0 `kspsolver-base-class.md` (cycle-006), L0 `ksp-factory-file.md` (cycle-005), and concept pages `solve-monad`, `solver-as-operator`, `constructed-operators`, `variant-absorption`, `constructed-operator-factory`, `ksp_solve`. **First L1 operator with a structured opaque primary argument** (`KspSolver<OperType>*` typed pointer). Introduces the Constructed-operator absorption motif at L1 (Semantics motif 4).
- **11 L0 reference-note chapters total** (cycle-005 bundle 1 = 6 + cycle-006 bundle 2 = 2 + cycle-007 bundle 3 = 3). New L0 grouping rows distributed across Conventions / File overviews / Overload sets and class interfaces (the 3 new chapters split across two of the three groupings).
- **L4 firm cohort growth 1→3** (`krylov-step` cycle-006 + `iterate_while` cycle-007 + `iterate_while_with_prev` cycle-007). Vocabulary-cohort subsection template at L4 is now eligible (3 firms ≥ threshold per cycle-004 L1 precedent); the `l4-layer-intro-refresh-unblocked-by-first-firm-row` OQ (cycle-006) now has expanded scope.

### Resolution implications

- **`iterate-while-l4-anchor-missing`** (cycle-006) — **answered**. Both L4 anchor files landed cycle-007 wave-1 report #4 with firm typing, 3+2 variant axes, and chapter shape matching the cycle-006 krylov-step precedent. Closure recorded in OQ frontmatter.
- **`krylov-step-body-identity-theme-pending-cycle-007`** (cycle-006) — **closed**. Theme authored at `book/src/L3-L2/krylov-step-body-identity.md` with `empirical-match` justification kind; first L3>L2 firm-rough-in entry; ratifies cycle-006 audit verdict. Status auto-promotes to plain `firm` when upstream L4>L3 theme firms.
- **`l1-ksp-solve-firm-up-anchor-ready`** (cycle-006) — **answered**. L1 entry `book/src/L1/ksp_solve.md` landed cycle-007 wave-1 report #2 with 3 exposed + 1 collapsed variant axis, Constructed-operator absorption motif registration, and firm-up of the L0-anchor → concept-page → L1 chain.
- **`mfemwrappersolver-l0-coverage-candidate`** (cycle-006) — **answered**. L0 chapter `book/src/L0/mfem-wrapper-solver.md` landed cycle-007 wave-1 report #1 covering the preconditioner-side adapter class. Now anchored.
- **`iterate-while-l3-rendering-trajectory-accumulation-gap`** (cycle-006) — **partially-answered, NOT closed** (user directive). Wave-2 lowering-verifier delivered verdict (c): the gap is closeable by citing `derived-view-hoisting.md` §3.8 + adding a new Condition 5 + replacing the single-readout sketch with a two-form pruned/unpruned sketch. The body-augmentation paragraphs (cycle-007 update + cycle-007 wave-2 verdict) record the conceptual closure rationale. **Closure proper is gated on the cycle-008+ lifter dispatch landing the substantive §3.8-citation patch** at `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`. Final status flip from `open` → `closed` happens at that lifter's per-report integration.
- **Priority #11 retroactive-L1-context-thinning** — **substantively progressed** (8 of 7 firm L1 chapters swept this cycle; the only firm L1 chapter NOT swept is `ksp_solve` itself, which is newly-firm cycle-007 and authored post-sweep with thin Context section by construction). ~55% net Context-section shrink across the 7 swept chapters per repairer's recount.
- **`l4-row-vs-concept-dependency-convention`** (cycle-006) — **needs-more**. 3 L4 firm chapters now use concept-page deps (krylov-step cycle-006, iterate-while + iterate-while-with-prev cycle-007). Plus first L4-row-on-L4-row dep edge landed (krylov-step → iterate-while). Convention seems stable; meta-phase ratification appropriate for cycle-009 meta.

### Suggested next dispatches

- **(CYCLE-008 PRIORITY)** (`lifter`, `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`) — apply wave-2 audit's Change 2 (`verified_against:` block) + Change 3 (substantive §3.8-citation patch + Condition 5 + two-form sketch). After landing, OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` becomes closeable. A `rough-in` → `firm` status promotion would naturally subsume both Changes 2+3 AND cascade-promote cycle-007's L3>L2 `krylov-step-body-identity` from `firm-rough-in` → `firm` via status-inheritance.
- (`abstractor`, `ksp_solve @ L1>L0`) — first L1>L0 theme for a constructed-operator-absorption operator. Closes OQ `ksp-solve-mutation-rotation-l1-l0-theme` (cycle-007).
- (`layer-intro-author`, `L1/index.md refresh post-ksp_solve`) — refresh after ksp_solve introduced Constructed-operator-absorption motif (motif 4) + Vocabulary cohort 7→8. Closes OQ `l1-intro-refresh-after-constructed-operator-gate` (cycle-007).
- (`same-layer-cross-cutter`, `5 L0 chapters with stale forward-declaration notes`) — bundle into one short housekeeping dispatch. Targets: `output-arg-vs-receiver.md:36`, `mfem-vector-types.md:42`, `linalg-free-functions.md:47`, `transparent-vs-load-bearing-tricks.md:34`, `apply-linop-overload-set.md:55`. The notes flag completed work (cycle-007 L1 thinning landed); rewording or removal is mechanical.
- (`layer-intro-author`, `L0 bootstrap bundle 4`) — eigensolver-wrapper candidate per OQ `eigensolver-wrapper-l0-bundle-4-candidate` (cycle-007). Continues priority #10. Other remaining candidates from cycle-006 backlog: `mpi-globalsum-and-collectives`, `par-types-single-rank-reading`, `linalg-operator-file`, `tests-as-semantic-supplement`.
- (`abstractor`, `GMRES-inner-loop iterate-while migration`) — both iterate-while L4 anchors now firm; GMRES inner Arnoldi loop's predicate-in-body pattern is a natural migration target. Per OQ `gmres-inner-loop-iterate-while-migration` (cycle-007).
- (`layer-intro-author`, `L4/index.md refresh post-3-firm-cohort`) — Vocabulary-cohort subsection template at L4 now eligible (3 firms ≥ threshold per cycle-004 L1 precedent). The `l4-layer-intro-refresh-unblocked-by-first-firm-row` OQ (cycle-006) has expanded scope.
- (`lowering-verifier` or `abstractor`, `iterate_while log-effect-vs-trajectory channel`) — orthogonal follow-up per new OQ `iterate-while-log-effect-vs-trajectory-channel` (cycle-007). Lower-priority than the §3.8-citation patch; not blocking. Surfaces during meta-phase methodology review of the L4 monad surface (cycle-009 meta consideration if no per-cycle dispatcher picks it up earlier).
- (`same-layer-cross-cutter`, `concepts/index.md full Kind-classification audit`) — cycle-006 OQ `concepts-index-kind-classification-full-audit`. Bounded scope (42 rows × short pages). Not blocking; still queued from cycle-006 signals.
- **MCP codemap rollout decision** — deferred to cycle-009 meta-phase per user directive. Cycle-008 planner does NOT yet treat MCP tools as preferred.

### Wave-conflict observations

- **Second wave-1 + wave-2 dispatch ordering under split integrator** (cycle-006 first; cycle-007 second). Wave-2 lowering-verifier depended on wave-1 harvester's iterate-while L4 chapters. Per-report serial dispatch order honoured (STAGING.md rows 1-5 then row 6). The OQ `iterate-while-l3-rendering-trajectory-accumulation-gap` was augmented by both wave-1 dispatch 4 and wave-2 dispatch 6; per-report integrator correctly extended-rather-than-overwrote the pre-existing paragraph. **Validates extend-pattern for OQ body augmentations across in-cycle wave-1+wave-2 mate-pairs.**
- **L4 dep-map promotion (rough-in → firm) coupled with row-extension** worked cleanly. Wave-1 dispatch 4's edits both (a) promoted 2 rough-in rows to firm and (b) extended the existing `krylov-step` row's Dependencies cell. Both changes self-contained in the same per-report apply; no inter-row collision risk.
- **SUMMARY.md again a convergence point** (5 of 6 dispatches edited it — same pattern cycle-005). Per-report serial dispatch + literal-anchor insert discipline → zero collisions across 6 inserts (L0 Part: 3; L1 Part: 1; L4 Part: 2; L3>L2 Part: 1).
- **Index-placeholder displacement pattern (cycle-006 precedent) applied once** — wave-1 dispatch 5 displaced the `(empty — Phase B skeleton.)` placeholder in `book/src/L3-L2/index.md` with the first firm-rough-in row. Third such displacement total (cycle-006 L4/index.md + cycle-006 L4-L3/index.md + cycle-007 L3-L2/index.md). **Methodology question status (cycle-006 raised)**: meta-phase should formalize whether per-report-integrator authority covers index-placeholder displacement or whether it stays discretionary. Recommend formalizing — three uses, zero hiccups.
- **First in-cycle status inheritance** — L3>L2 `krylov-step-body-identity` declared `firm-rough-in` to inherit upstream L4>L3 theme's `rough-in` status. **First instance of cross-edge status inheritance in the artifact.** Auto-promotes to plain `firm` when the cycle-008+ lifter firms the upstream theme. Pattern worth documenting in meta-phase as a layered-stack status convention.
- **No deferrals, no rejections, no rework loops.** All 6 reports applied as-is.

### Integration-tooling friction

- **mdbook-linkcheck2-fails-on-rough-in-anchor-missing recurrence check: NEGATIVE** — cycle-007 wave-1 dispatch 4 correctly promoted the rough-in rows to firm rows WITH anchor files created (rather than leaving rough-in rows pointing at missing files). Meta-phase-enacted role-spec discipline (rough-in rows must use plain-text names, not links, when anchor file does not exist; abstractor.md role spec) held this cycle. Friction-ledger entry can stay `addressed`.
- **per-report `integrated_at:` write-authority drift: 0 recurrences** — all 6 per-report dispatches deferred correctly to finalize per meta-phase-enacted role-spec clarification (`.claude/agents/integrator-per-report.md` Process / "What you DO NOT do" sections). Friction-ledger entry `integrated-at-write-authority-drift` may be markable `addressed` at cycle-009 meta.
- **legacy log/cycle-007.md name collision** — pre-layered-era `log/cycle-007.md` (2026-05-24 `forward gmres [L1→L2] — revise`) existed; finalize renamed it to `log/cycle-007-legacy.md` per cycle-005/006 precedent. Pattern still working as designed; meta-phase candidate for bulk-rename pass (alternative (a) from cycle-006 signals) once cycle-N collisions become predictable noise.
- **MCP codemap pilot permission-denied** — cycle-007 wave-1 dispatch 4 was the designated MCP codemap pilot per priority #16 step (e). The sub-session was unable to invoke `mcp__palace-codemap__*` tools (configured at repo root `.mcp.json` per `ab73d37`). Fallback to vanilla Grep/Read worked correctly; dispatch landed successfully. **Rollout decision deferred to cycle-009 meta-phase** per user directive. Cycle-008/009 dispatches may opportunistically pilot if permission is granted.
- **No new safety-net gates needed.** Cycle-005/006/007 gate set held cleanly across 6 wave-mates with one wave-1+wave-2 ordering. Zero retroactive-budget hits even with the largest cross-slice retroactive sweep this cycle (7 L1 chapters). Zero edge-label drift. Zero forward-edge claims without surface. Zero variant-axis-missing. One index-placeholder displacement (applied-discretionarily; cycle-006 precedent + meta-phase formalization recommended).

---

## cycle-006 — 2026-05-27T090849Z

### Unblocked

- **`iterate_while` / `iterate_while_with_prev` L4 anchor harvest** unblocked — both names are used as load-bearing vocabulary in cycle-006's L4 `krylov-step` entry (Form A/B bodies) and surfaced doubly via (a) the wave-1 harvester's caveat 2 and (b) the wave-2 abstractor's rough-in L4 dep-map row proposals. Cycle-007 candidate: `harvester` on the L4 loop-combinator family. Anchors needed to lift the cycle-006 defanged-to-plain-text dep-map entries back to firm `[name](./name.md)` links. Citation: open question `iterate-while-l4-anchor-missing` (cycle-006).
- **`krylov-step` L3>L2 body-identity theme** unblocked — cycle-006 wave-2 abstractor's audit confirmed-with-refinement the cycle-005 identity-in-form claim for the L3>L2 body rewrite. A short cycle-007 `abstractor` dispatch can author `book/src/L3-L2/krylov-step-body-identity.md` (one-line theme with `empirical-match` justification). Low-cost; slottable alongside the `iterate_while` harvester. Citation: open question `krylov-step-body-identity-theme-pending-cycle-007` (cycle-006).
- **`retroactive-L1-context-thinning` sweep (priority #11)** unblocked — threshold of ≥6 L0 reference-note chapters is now met (8 chapters total post-bundle-2). Cycle-007 candidate: `layer-intro-author` per-operator or single-sweep on the 7 L1 entries (`axpy`, `dot`, `nrm2`, `axpby`, `scal`, `apply_linop`, `axpbypcz`) to replace inline L0-interpretation prose with cross-references to L0 chapters. Distinct from cycle-006's scalar-promotion-specific thinning (priority #9 progressed); priority #11 is the broader L0-interpretation thinning.
- **`mfemwrappersolver-l0-coverage-candidate` L0 bundle-3+ chapter** unblocked — flagged by cycle-006 wave-1 L0 bundle-2 as a future L0 reference-note targeting the preconditioner-side construction surface. Cycle-007+ `layer-intro-author` candidate. Citation: open question `mfemwrappersolver-l0-coverage-candidate` (cycle-006).
- **`l1-ksp-solve` L1 harvest** unblocked — both concept-page and L0-anchor entry points now exist (`kspsolver-base-class` L0 chapter landed cycle-006; `solve-monad` concept already exists). Cycle-007+ `harvester` candidate. Citation: open question `l1-ksp-solve-firm-up-anchor-ready` (cycle-006).
- **MCP codemap reintegration (priority #16)** scheduled post-meta-phase — orchestration-layer work, not a planner dispatch. See mid-cycle directive commit `f661039`.

### New dependencies

- **L4 `krylov-step` (firm) depends on 5 concept-page entries** (`state-stratification`, `solve-monad`, `first-iteration-unrolling`, `derived-view-hoisting`, `convergence-test`) — concept-deps-on-L4-rows convention used as a first-instance precedent; future L4 rows can follow this pattern or, if cycle-007+ decides L4-rows-must-depend-on-L4-rows, the cycle-006 entry's link targets re-anchor without content rewrite. Citation: open question `l4-row-vs-concept-dependency-convention` (cycle-006).
- **L4>L3 `krylov-step-typed-wrapper-dissolution` (firm theme) depends on L4 `krylov-step` (LHS) and L2 `krylov-step` (RHS via L3>L2 identity-in-form)** — first L4>L3 theme; first cross-Part lowering surface in the layered stack to date.
- **8 L0 reference-note chapters total** (cycle-005 bundle 1 = 6 + cycle-006 bundle 2 = 2) — L0 reference-notes overlay is now substantial enough to support the priority #11 retroactive-thinning sweep. Future cross-cutter and lowering-verifier dispatches can target these L0 chapters as anchor sources alongside the citation evidence.
- **L4 dep-map now has 2 rough-in rows beyond the first firm** (`iterate_while`, `iterate_while_with_prev`) — vocabulary cohort pattern (firm + rough-in mixed) reaches L4 for the first time. The cycle-004 L1 Vocabulary-cohort subsection template (from `layer-intro-author` role spec) may want to be invoked on L4 once `iterate_while` firms in cycle-007+ (cycle-006 OQ `l4-layer-intro-refresh-unblocked-by-first-firm-row` tracks this).

### Resolution implications

- **`krylov-step-l3-identity-in-form-audit`** (cycle-005) — **answered**. Cycle-006 wave-2 abstractor audit verdict: **confirms-with-refinement**. The cycle-002 framing "L2>L3 step-body lift is identity-in-form" is confirmed; refined to "L4>L3>L2 step-body chain is identity-in-form on the kernel body's primitive sequence; the L4>L3 hop is non-identity at the wrapper level but the body's dataflow chain survives both hops textually unchanged." See closure-note OQ `krylov-step-l3-identity-in-form-audit-closure-cycle-006`.
- **`krylov-step-l3-row-contingency`** (cycle-006 wave-1) — **answered**. Same audit resolves: the contingency triggered by "non-identity rotation at L3 body" did not fire; the defensive L4 entry's "Lowers to" wording (L4>L3>L2 chain with no interposed L3 row) stands as-is.
- **`krylov-step-dual-placement-l2-l4-routing`** (cycle-005) — **answered**. L4 firm landed (`book/src/L4/krylov-step.md`); L4>L3 theme firm landed (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`); L3>L2 confirmed identity-in-form via audit; no intermediate L3 row promoted. The three named cycle-006 follow-up dispatches (primary harvester, secondary abstractor, tertiary deferrable layer-intro-author) were enacted as wave-1 harvester + wave-2 abstractor; the tertiary deferrable layer-intro-author L4 dep-map refresh is now bounded by the cycle-006 entries and not yet executed (cycle-007 candidate via `l4-layer-intro-refresh-unblocked-by-first-firm-row` OQ).
- **`scalar-promotion-retroactive-l1-thinning`** (cycle-005) — **answered for the 4 L1 entries**. Cycle-006 wave-1 layer-intro-author retroactive-thinned `axpy.md`, `axpby.md`, `axpbypcz.md`, `scal.md` to replace inline scalar-promotion prose with `concepts/scalar-promotion` backlinks. Tail item: `concepts/axpby.md` and `concepts/axpbypcz.md` concept pages not authored, so the concept-pages can't backlink back yet (cycle-007+ via `concepts-axpby-axpbypcz-pages-absent` OQ).
- **Pre-existing `concepts/index.md` duplicate rows** (cycle-005 integrator-signals item) — **answered**. Cycle-006 wave-1 same-layer-cross-cutter deduped both pairs (`complex-from-real-lift` pure copy-paste; `solver-as-operator` `layer-pattern`-kept / `primitive`-deleted).
- **`l4-row-vs-concept-dependency-convention`** (cycle-006) — **needs-more**. The cycle-006 L4 `krylov-step` entry uses concept-page links as deps; convention to be ratified or rejected by meta-phase / future L4 harvester dispatches.

### Suggested next dispatches

- (`harvester`, `iterate_while @ L4`) — closes `iterate-while-l4-anchor-missing` OQ; lifts the cycle-006 defanged plain-text rough-in rows back to firm `[name](./name.md)` linkable entries. Cycle-006's two rough-in dep-map rows in `book/src/L4/index.md` provide signature sketches the harvester can adopt or refine. Likely co-bundle with `iterate_while_with_prev @ L4` as a single dispatch (variant axis is the `PrevCarry` parameter, degenerate when `PrevCarry = ()`).
- (`abstractor`, `krylov-step-body-identity @ L3>L2`) — short single-theme dispatch; one-line `empirical-match` justification per the cycle-006 audit's verdict. Authors `book/src/L3-L2/krylov-step-body-identity.md`. Closes `krylov-step-body-identity-theme-pending-cycle-007` OQ. Low-cost (~half a dispatch budget); slottable alongside the `iterate_while` harvester for symmetric completion of the krylov-step lowering chain.
- (`layer-intro-author`, `retroactive-L1-context-thinning sweep`) — priority #11 now eligible (8 L0 chapters ≥ 6 threshold). Per-operator or single sweep over 7 L1 entries. Distinct from cycle-006's scalar-promotion-specific thinning; broader L0-interpretation thinning (Context sections to L0 chapter references).
- (`layer-intro-author`, `L0 bootstrap bundle 3`) — priority #10 continuation. Remaining candidate chapters: `mpi-globalsum-and-collectives`, `par-types-single-rank-reading`, `mutable-workspace-pattern`, `linalg-operator-file`, `linalg-iterative-file`, `mfem-wrapper-solver` (per cycle-006 OQ `mfemwrappersolver-l0-coverage-candidate`), `tests-as-semantic-supplement`. Cycle-007 planner's call on bundling.
- (`harvester`, `l1-ksp-solve @ L1`) — both concept-page (`solve-monad`) and L0-anchor (cycle-006 `kspsolver-base-class.md`) entry points now exist. Cycle-007+ forward-frontier candidate. Closes `l1-ksp-solve-firm-up-anchor-ready` OQ.
- (`lowering-verifier`, `iterate_while L3 trajectory-accumulation reconciliation`) — flagged by cycle-006 wave-2 abstractor's §"What the L3 form for `iterate_while` looks like" (repairer-deferred substantive rotation decision). Resolves the L4 trajectory `[readout]` vs L3 single-readout gap. Routes to either cycle-007 `lowering-verifier` or folds into the `iterate_while @ L4` harvester dispatch. Citation: open question `iterate-while-l3-rendering-trajectory-accumulation-gap` (cycle-006).
- (`same-layer-cross-cutter`, `concepts/index.md full Kind-classification audit`) — cycle-006 OQ `concepts-index-kind-classification-full-audit`. Bounded scope (42 rows × short pages). Not blocking; cycle-007+ candidate for housekeeping budget.
- **MCP codemap reintegration** (priority #16, post-meta-phase) — orchestration-layer work scheduled per mid-cycle directive commit `f661039`. Not a planner dispatch. Sequence: (a) binary verify/rebuild against current rmcp + tree-sitter deps; (b) `cargo test` smoke against `reference/palace/`; (c) confirm `.claude/mcp.json` registration; (d) update 5 role specs to reference codemap tools as preferred C++ source-localization; (e) pilot on one cycle-007 harvester dispatch; (f) instrument tool-call count vs vanilla baseline; (g) surface results to user before broad rollout.

### Wave-conflict observations

- **First wave-1 + wave-2 dispatch ordering under split integrator** worked cleanly. The wave-2 abstractor depended on wave-1 harvester's L4 entry (its "Lowers to" L4>L3 chain references the abstractor's theme; its L4 dep-map row is appended after the wave-1 firm row). Per-report serial dispatch order honoured (STAGING.md rows 1-4 then row 5). The L4 dep-map at wave-2's edit time already had wave-1's firm row, so wave-2's two rough-in appends went after it cleanly. **Validates the per-report serial-dispatch design at wave-mate-dependency boundaries**, not just across independent wave-1 mates.
- **Index-placeholder displacement convention established cycle-006** — when the first real entry lands under a Part that still carries the "(empty — Phase B skeleton.)" placeholder, the per-report integrator discretionarily replaces the placeholder with the first real table row. Pattern applied twice cycle-006: wave-1 harvester on L4/index.md; wave-2 abstractor on L4-L3/index.md (the latter explicitly cited the former as precedent in its STAGING row notes). **Methodology question for meta-phase**: formalize "first-real-entry placeholder displacement" as a per-report-integrator authority or leave as discretionary practice?
- **No deferrals, no rejections, no rework loops.** All 5 reports `ready` post-repair and applied as-is. Cycle-005's clean run repeats cycle-006.

### Integration-tooling friction

- **mdbook-linkcheck2-fails-on-rough-in-anchor-missing** — NEW friction this cycle. The cycle-006 wave-2 abstractor's two rough-in L4 dep-map rows used `[iterate_while](./iterate_while.md)` markdown links, but those files don't exist yet (rough-in status; cycle-007 OQ `iterate-while-l4-anchor-missing` tracks the anchor pending). mdbook's `linkcheck2` renderer treated these as **errors** (not warnings) and failed the build. **Finalize repair**: defanged to plain-text `iterate_while (rough-in; no anchor yet)` with annotation. **Pattern observation**: rough-in dep-map rows that reference yet-to-exist files should NOT use markdown link syntax. Two candidate resolutions for meta-phase: (a) document this constraint in `layer-intro-author` / `abstractor` role specs ("rough-in rows must use plain-text names, not links, when the anchor file does not exist"); (b) configure mdbook to downgrade missing-link errors to warnings (less surgical; affects all link-checking). Cycle-006 used (a)-equivalent surgical fix at finalize; meta-phase candidate friction-ledger entry.
- **per-report `integrated_at:` write-authority drift** — per-report dispatch #1 (harvester krylov-step L4) set `integrated_at: 2026-05-27T09:00:00Z` in its CYCLE.md frontmatter at per-report integration time, outside CLAUDE.md write-authority partition (which assigns `integrated_at` touches to integrator-finalize). The other 4 per-report dispatches deferred correctly. Finalize overwrote with the actual finalize timestamp (`2026-05-27T09:08:49Z`). **Meta-phase candidate**: role-spec clarification in `.claude/agents/integrator-per-report.md` "Process" or "What you DO NOT do" section to explicitly call out `integrated_at:` is finalize's domain (and add to the staging-log notes that per-report should defer the timestamp).
- **legacy log/cycle-006.md name collision** — pre-layered-era `log/cycle-006.md` (2026-05-24 `back gmres — revise`) existed; would have been overwritten by the layered-era cycle-006.md write. Finalize renamed it to `log/cycle-006-legacy.md` (mirroring the cycle-005 `cycle-005-legacy.md` precedent). **Pattern observation**: legacy slice-era cycle-NNN.md files in `log/` will collide with future layered-era cycle-NNN.md writes for any N ≤ 172. Two candidate resolutions for meta-phase: (a) bulk-rename all pre-pilot-1 cycle-N.md files to `cycle-N-legacy.md` in one pass; (b) handle as encountered (cycle-005 + cycle-006 precedent — works fine but adds a small finalize step). Currently following pattern (b); not blocking.
- **No new safety-net gates needed.** Cycle-005's gate set held cleanly across 5 wave-mates under split integrator. Zero retroactive-budget hits (4 L1 retroactive-thinning edits all at per-slice = 1 per operator, well below threshold). Zero edge-label drift. Zero forward-edge claims without surface (wave-1+wave-2 ordering correctly resolved the krylov-step L4 / L4>L3 mutual reference within-cycle). Zero variant-axis-missing.

---

## cycle-005 — 2026-05-27T070424Z

### Unblocked

- **`krylov-step` L4 dual-placement (3 cycle-006 dispatches)** unblocked — cycle-005 landed `krylov-step` firm at L2 (`book/src/L2/krylov-step.md`); the cross-cutter recommendation routes the L4 row + L4>L3 lowering theme to cycle-006. Three named follow-ups: (a) primary `harvester` on `krylov-step @ L4`; (b) secondary `abstractor` on L4>L3 lowering theme; (c) tertiary deferrable `layer-intro-author` on L4 dep-map. Citation: open question `krylov-step-dual-placement-l2-l4-routing` (cycle-005).
- **`L0 bootstrap bundle 2` (priority #10 continuation)** unblocked — cycle-005 landed bundle 1 (6 chapters + L0/index.md re-framing). Bundle 2 candidates per priority #10 backlog: `apply_linop` overload-set page, `kspsolver-base-class` page, additional file-overview chapters. Routes to `layer-intro-author` next cycle.
- **`scalar-promotion` retroactive L1 thinning** unblocked — the concept page now exists at `book/src/concepts/scalar-promotion.md`; cycle-006+ retroactive backlinking from the 4 L1 entries (axpy, axpby, axpbypcz, scal) can replace ~600 words of per-operator prose with one-line concept backlinks. Citation: open question `scalar-promotion-retroactive-l1-thinning` (cycle-005).
- **`apply-linop` cross-family mutation-rotation theme** unblocked — cycle-005 abstractor on `axpbypcz-mutation-rotation` surfaced the open question `scalar-promotion-mutation-rotation-cross-family-theme` (shared structural pattern across axpy/axpby/axpbypcz/scal mutation-rotation themes). Routes to abstractor in cycle-006+.
- **`axpbypcz` sub-pattern B full-corpus audit** unblocked — open question `axpbypcz-sub-pattern-B-defined-not-used-corpus-audit` names a discrete cycle-006+ harvester or lowering-verifier dispatch.

### New dependencies

- **`krylov-step` (L2 firm) depends on 7 L1 firm operators**: `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `scal`, `dot`, `nrm2`. All firm post-cycle-004; the L2 firm-up was the natural next step. Planner: future L2 operators sharing this vocabulary subset are now unblocked.
- **`scalar-promotion` concept centralises the typing rule across 4 L1 operators**: the per-operator clauses in `axpy.md`, `axpby.md`, `axpbypcz.md`, `scal.md` are now superseded by one canonical concept page. Retroactive-thinning is a follow-up, not load-bearing.
- **`apply-linop-mutation-rotation` (L1>L0)** is the second mutation-rotation theme after `axpby-mutation-rotation`; companion `axpbypcz-mutation-rotation` is the third. Three mutation-rotation themes form a cohort — recognizable cross-family pattern.
- **First `algebraic`+`structural` mixed-justification sub-rule landed** (`axpbypcz-mutation-rotation` γ==0). Tooling implications routed to cross-layer-cross-cutter via `mixed-justification-sub-rule-methodology` OQ.
- **L0 reference-notes overlay precedent** — L0 is now a 2-cohort layer (citations + reference notes); the 6 L0 chapter pages co-exist with the L0=citations baseline. The 4 conventions pages (output-arg-vs-receiver, transparent-vs-load-bearing-tricks, etc.) are referenced FROM L1>L0 themes; the 2 file-overview pages (linalg-vector-file, ksp-factory-file) supply file-scoped context for citation-validity audits.

### Resolution implications

- **`krylov-step-speculative-l1-promotion-decision`** — **answered**. Decision: NOT to promote any of the 6 cycle-004 speculative L1 operators. Decision artifact at `scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md`. Reaffirms the unimplemented-Palace-components policy: the L2 `krylov-step` cleanly absorbs the algorithmic variation without speculation-promotion needed.
- **`scalar-promotion-typing-rule`** — **answered** (cycle-002 → cycle-005). The concept page at `book/src/concepts/scalar-promotion.md` lifts the per-operator clauses; retroactive thinning is the follow-up.
- **`L1-index-refresh` triggering for L2**: now that L2 has its first firm operator (`krylov-step`), L2 index-refresh threshold (≥3 firm L2 operators) is NOT yet met — refresh blocked on more L2 work. Cycle-005 dispatch #1 promoted `L2-layer-intro-refresh-for-named-compositions` as a tracking OQ for when threshold hits.
- **`apply-linop-lowering-theme-scope`** (cycle-004) — **answered** by cycle-005 abstractor on `apply-linop-mutation-rotation` (5 sub-patterns A-E land as predicted).
- **`axpbypcz-mutation-rotation-abstractor-target`** (cycle-004) — **answered** by cycle-005 abstractor.
- **`mfem-as-l0-substrate`** (cycle-004 meta-phase ask) — **answered upstream** by user directive 2026-05-27 (commit `fb8239a`). Cycle-005's krylov-step decision artifact records the policy application in practice.
- **`cycle-005-L0-bootstrap` priority #10** — **partially-answered** (bundle 1 of N landed). Continues cycle-006+.

### Suggested next dispatches

- (`harvester`, `krylov-step @ L4`) — primary cycle-006 dispatch per cross-cutter recommendation. Requires `iterate_while`, `state-stratification`, `solve-monad` L4 vocabulary; may co-bundle with L4 dep-map updates.
- (`abstractor`, `L4>L3 lowering theme for krylov-step (krylov-step-as-iterate-while)`) — secondary; can be parallel with the L4 harvester if planner prefers wave.
- (`layer-intro-author`, `L4 dep-map refresh`) — tertiary deferrable; only if cycle-006 actually populates L4 with multiple operators.
- (`layer-intro-author`, `L0 bootstrap bundle 2`) — priority #10 continuation; candidates include `apply_linop` overload-set page, `kspsolver-base-class` page, additional file-overview chapters per bundle planning.
- (`cross-layer-cross-cutter`, `mixed-justification-sub-rule methodology audit`) — first instance of `algebraic`+`structural` sub-rule (axpbypcz γ==0); needs cross-cutter or meta-phase review to decide if it's a new pattern or specific to this theme.
- (`layer-intro-author`, `scalar-promotion retroactive L1 thinning`) — 4 L1 operators backlink to concept page; estimated ~600 words savings.
- (`harvester` or `cross-layer-cross-cutter`, `apply_linop cross-family mutation-rotation theme`) — `scalar-promotion-mutation-rotation-cross-family-theme` OQ; mid-priority.
- (`harvester` or `lowering-verifier`, `axpbypcz sub-pattern B corpus audit`) — `axpbypcz-sub-pattern-B-defined-not-used-corpus-audit` OQ; bounded scope.
- (`same-layer-cross-cutter` or `problems/`, `concepts/index.md duplicate-rows housekeeping`) — `complex-from-real-lift` rows 70-71 and `solver-as-operator` rows 98-99 (pre-existing; surfaced by dispatch #6). Drive-by fix; low-cost.

### Wave-conflict observations

- **SUMMARY.md was the load-bearing convergence point** — 5 of 6 dispatches edited it (L2 + 2× L1>L0 + L0 bundle (6 rows + heading rename) + concepts/scalar-promotion). Per-report serial dispatch order + the "surgical insert preserving append-points" discipline (introduced by dispatch #1's notes and propagated through subsequent dispatch notes) meant **zero collisions**. Each per-report integrator re-read SUMMARY.md fresh and inserted at literal-string anchors. **Validates the per-report serial-dispatch design at 5 SUMMARY-writers** (cycle-004 was 5 writers under single-pass integrator; cycle-005 confirms split-integrator handles it identically).
- **L1>L0 alphabetical ordering self-resolved** — `apply-linop-mutation-rotation` and `axpbypcz-mutation-rotation` independently picked positions relative to existing `axpby-mutation-rotation`; interleaved correctly via per-report serial dispatch (axpbypcz first → apply-linop second, by dispatch order).
- **No deferrals, no rejections, no rework loops.** All 6 reports `ready` post-repair and applied as-is.
- **Cross-reference fix `bicgstab-iteration.md :53-56 → :53-57` folded into L0-bootstrap dispatch** rather than handled as a separate finalize-repair — per dispatch instructions, the fix was directly relevant to L0 bootstrap consistency (the new `ksp-factory-file.md` cites the same range; consistent reference range across `minres-iteration`, `bicgstab-iteration`, `ksp-factory-file`). This pattern (route a small cross-reference fix into the most-related dispatch rather than the finalize) is a useful template: keeps finalize purely housekeeping, keeps the fix's rationale co-located with the relevant content surface.

### Integration-tooling friction

- **`new-agent-defs-need-session-restart`** — first-cycle-under-split-integrator friction. The `integrator-per-report` and `integrator-finalize` agent defs were added in commit `ccc5082`; the session that wrote that commit did NOT see them in the cached agent registry, and the first per-report dispatch attempted before restart returned "Agent type not found". Restart required. **Status `addressed-by-restart`** — but if there's a way to invalidate the cached agent list mid-session (or auto-invalidate on `.claude/agents/` write), that would close it cleanly. Routes to meta-phase as a friction-ledger candidate.
- **Split integrator design VALIDATED on first cycle.** Six per-report dispatches each had bounded scope (one report's proposed-changes + the artifact files that report touched + the staging-log append). The split (vs. cycle-001..004's single-pass integrator that handled all reports + commit in one dispatch) means each per-report dispatch's context budget is bounded by ONE report's scope, not the cycle's total. **No per-report context-bound friction observed.** STAGING.md format usability also PASS — aggregating gate-totals, files-touched, and OQ counts for this finalize was mechanical (read STAGING.md, sum columns). No format changes proposed.
- **SUMMARY-chapter-registration-auto-fix applied discretionarily ONCE** — concepts/scalar-promotion is outside the literal gate scope (gate targets `book/src/L<n>/<slug>.md`), but the existing SUMMARY.md pattern registers nearly all concept pages (~35 entries between lines 64-104). Per-report integrator #6 chose to register for discoverability. **Methodology question for meta-phase**: extend the gate spec to include `book/src/concepts/<slug>.md` (most concepts register), or formalise "discretionary auto-fix" as a per-report-integrator authority? Currently undocumented practice; cycle-005 establishes precedent.
- **Pre-existing `concepts/index.md` duplicate rows** (`complex-from-real-lift` lines 70-71, `solver-as-operator` lines 98-99) NOT addressed by any cycle-005 dispatch — out of scope for each per-report dispatch's edit set. Flagged by dispatch #6 critic + repairer for cycle-006 housekeeping. **Routing this to cycle-planner**: cycle-006 drive-by fix or `problems/` filing.
- **No new gates needed.** Cycle-004's gate set held cleanly for 6 wave-mates under split-integrator. Zero retroactive-budget hits (global aggregate confirmed 0 by this finalize). Zero variant-axis-missing (6 axes / 4 sub-patterns / 3 axes correctly absorbed across the 3 multi-variant reports). Zero edge-label drift. Zero forward-edge claims without surface.

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
