# CLAUDE.md

Operational guide for Claude Code working in this repository. The project is a multi-agent pipeline that dissects AWS Labs **Palace** (C++ electromagnetic simulator) into a **layered, citation-grounded specification** organized as an incremental impedance-matching stack L4→L0.

This file replaces the original CLAUDE.md (slice-vertical era, cycles 1–172) after the **structural redirect of 2026-05-26**. This CLAUDE.md is the redirect's operational distillation. The original redirect spec (`MIGRATION.md`) and the original phased build spec (`BOOTSTRAP.md`) are now **compacted history-stubs** (2026-06-05, batch-31 — full text in git history); the redirect they describe is fully internalized here.

## Repository status

- **Current flow**: 6-phase agent cycle (plan → dispatch → critique → repair → integrate → meta). See *Cycle structure* below (the original `MIGRATION.md` §2 derivation is now a history-stub — full text in git history).
- **Artifact in progress**: layered specification under `book/src/L4/`–`book/src/L0/` + 4 lowering Parts + the FEATURE-SURFACE SPINE Part. The Phase 1 slice corpus under `book/src/spec/slices/` was raw material for the layered artifact (not the deliverable); **it is now fully lifted and DELETED — the corpus shrank 9→0 across cycles 097/098/099 (the graded-stack P2 slice-deletion campaign, COMPLETE), and `book/src/spec/slices/` + `book/src/spec/index.md` no longer exist** (git history is the record; see §Methodology invariants "Phase 1 corpus was lifted and deleted").
- **First pilot cycle landed**: `pilot-1` (commit `a058f07`) — `axpy` at L1 via the new flow. See `log/pilot-1.md` and `reports/2026-05-26T223039Z-harvester-axpy-L1/`.
- **Decommissioned + DELETED** (batch-31 meta-phase non-book-orphan-review, post-cycle-099): the pre-redirect Python orchestrator (`orchestrator/`), its 6 prompted-role files (`prompts/`), its JSON schemas (`schemas/`), and the legacy ledgers (`lessons.md`, `questions.md`, the stale root `README.md`, `episodic.jsonl.README.md`) were removed (recoverable from git history). The 6 prompted roles (Planner/Explorer/Synthesizer/Critic + Meta-Critic + README Builder) had already been replaced by the 14 Claude Code subagents under `.claude/agents/`.

## What this system is

A multi-agent pipeline that lifts traditional C/Fortran tensor-field simulators — which evolve fields by array iteration with in-place mutation — into a **citation-grounded, incrementally-layered series of representations**, where each layer re-expresses the layer below in a representation that has rotated one specific impedance, and the rotation is explicitly stated and verified.

**No port is produced.** The output is a layered specification; a separate downstream effort uses it to incrementally build burn components.

The methodology was developed in the user's **bunsen** project (see `reference/bunsen/crates/bunsen/src/kits/sims/` for the working Rust+burn realization at L3). Palace is a substantial test case.

## Extraction goal — what the spec is for

The artifact is an **incremental stack of representations** L4→L0:

- **L0** — cited Palace/MFEM source ranges. Ground truth.
- **L1** — *mutation rotation*. Source operations re-expressed as pure functions.
- **L2** — *fusion rotation*. L1 unfolded back into composition of base algebraic primitives, HPC tricks erased.
- **L3** — *iteration rotation*. Where possible, global tensor-field operations; otherwise record the obstruction.
- **L4** — small, formally-defined graph-evaluation calculus. **Vocabulary, not architecture.** High-order combinators + state monads + immutable tensors.

Between adjacent layers, **lowering layers** `L_{n+1}>L_n` describe the rewrite themes that take an L_{n+1} form into its L_n form. Lowerings are batched by themes (e.g. "in-place mutation under monad threading", "loop-recurrence → tensor-field op"), not point-wise edges.

**Each layer is its own mdBook Part** with multiple chapters: one for the Part overview (`index.md`), one per operator (for L_n) or theme (for L_{n+1}>L_n). The Part shape is load-bearing — it prevents per-layer content from accumulating into one giant file and preserves cross-referencing.

**The FEATURE-SURFACE SPINE — a top-down composition-root spine parallel to the bottom-up vocabulary** (user directive 2026-06-02; memory `project_feature_surface_spine`; codified batch-22 meta-phase, post-cycle-072). Palace has high-level **entry-point features** — what Palace is *written for*. Even as each decomposes into collections of internal constructions, dedicated **feature-surface chapters** explain those entry points as coherent feature surfaces at each level. A feature chapter is a **composition-root**: inputs = config; outputs = the physical product; body = the **composition of the already-firm decomposed vocabulary** at that level; it links **DOWN** to the constituent ops/combinators. It COMPOSES the vocabulary, it does not replace it — a distinct **kind** of chapter from a per-operator entry or a lowering theme.
- **Feature set:** (1) the **5 simulation drivers** (electrostatic / magnetostatic / eigenmode / driven / transient, `palace/drivers/*solver`); (2) the **top-level lifecycle** (`main` → `BaseSolver`: config→mesh→assemble→solve→postprocess→output) — the spine ROOT; (3) the **output/postprocess products** (S-parameters / capacitance / inductance / eigenfrequencies+Q / energy-fields); (4) **wave-port / boundary-mode** (`boundarymodesolver`).
- **Two sub-kinds:** a **leaf feature column** (per-driver / output-product / boundary-mode; stage-(2) constituents are *vocabulary ops*) and a **meta-feature / spine-ROOT** (the lifecycle column; stage-(2) constituents are *other feature columns* + driver-agnostic firm vocabulary). Uniform `status: seed` token; the prose names the sub-kind.
- **Column promotion off `seed` — the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03; memory `project_feature_column_promotion_rule`).** A column promotes off `seed` when its **OWN composition + directly-owned constituents** are firm; **cross-linked SIBLING columns are references, NOT blocking constituents** (a driver column promotes on its own firm solve/assemble combinators + readout; an output-product column on its own firm reduce verb — neither blocks on the other it cross-links). This SUPERSEDED the earlier "promote only once ALL constituents incl. sibling columns are firm" rule, which created an output-product↔driver mutual-blocking deadlock that made `seed` permanent. Authoring mechanics (per-column judgment, index-cell + sibling-status grep coupling): `.claude/agents/layer-intro-author.md` §FEATURE-SURFACE.
- **Levels:** **L4 + L1 + L0** each get a feature-surface chapter (L4 = calculus/backend-lowering feature surface; L1 = pure-function surface; L0 = ground-truth driver source). L2/L3 feature chapters ONLY where the decomposition meaningfully reshapes.
- **Layout convention:** flat per-file `book/src/feature/<name>.{L4,L1,L0}.md`, under a top-level `# Feature surfaces — entry points` Part placed AFTER `# Methodology`, BEFORE `# L4`. Within a column the level ordering is **high→low (L4→L1→L0), DELIBERATELY NOT alphabetized**. The directive-3 by-kind grouping (spine-ROOT / driver-leaf / output-product) DOES apply to the Feature Part, with the within-column high→low exception preserved. Full layout + reorg mechanics: `.claude/agents/layer-intro-author.md` §FEATURE-SURFACE.
- **Priority:** **run in PARALLEL** — a co-equal standing goal interleaved with the bottom-up vocabulary frontier by fan-out (NOT a replacement frontier, NOT necessarily the lead). The L4 feature surfaces ARE the outward backend-lowering entry points (`project_l4_is_backend_lowering_target`); the per-pipeline L4-completeness picture is the 5-driver subset.

**⟢ POST-CONSOLIDATION: OPEN ALL REMAINING FEATURE FRONTS SIMULTANEOUSLY (user directive 2026-06-06; answers the batch-36 plateau ASK).** The batch-36 plateau ASK (reachability + forward-vocabulary frontiers substantially exhausted under the then-current clean-gate scope) was independently CONFIRMED by the c115 plateau-probe — the remaining in-scope work IS the demand-gated deferred fronts, and the user now **fires the demand-gate trigger for ALL of them AT ONCE**. The **complete set** of remaining fronts: (1) the **`waveguide-mode` 6th output-product column** (the boundary-mode readout's reduction product); (2) the **`boundary-mode` driver-leaf column** promotion off `seed` (its waveguide-mode readout gate fires once waveguide-mode lands); (3) the **`fe_space` deferred siblings** (`essential_dofs` / `fe_space_hierarchy` / de-Rham interpolator); (4) the **mesh-wrapper vocabulary proper** — the candidate-(c) `Mesh` / `build_mesh` front, **within single-machine scope** (`Par*` / distributed mesh-partitioning stays OUT per §Scope; MFEM-opaque mesh-refinement leaves stay obstruction-documented, not forced); (5) any other in-scope deferred feature surface the planner enumerates. **Rationale — shared-exploration lifting:** these fronts are naturally related / variants of each other and **share implementation cores and details**, so opening them SIMULTANEOUSLY (one wide multi-dispatch fan-out) lets the shared substrate be lifted once across all of them rather than re-discovered per-front. **Sequencing:** the SEMANTIC-CONSOLIDATION campaign lands FIRST ("post consolidation…"), THEN a single wide all-fronts fan-out opens the fronts together (NOT one-at-a-time, NOT a serial frontier). This LIFTS the STOP-PROPOSING posture for these specific demand-gated fronts (the redirect's no-forced-rectangular-pull-up still governs *vocabulary* picks; this directive is the user firing the *feature demand-gate*). (Memory `project_open_all_feature_fronts_simultaneously`.)

## The SYNTHESIS section — the synthesized-library implementation view (user directive 2026-06-07)

A new top-level Part **`# Synthesis`**, placed **immediately before `# Feature surfaces`** in `SUMMARY.md` (order: `# Methodology` → **`# Synthesis`** → `# Feature surfaces` → `# Semantic surface` → `# L4` → lowerings → `# L0`). It renders the spec's surface **as though it were a real implementation library** — the synthesized codebase the layered spec describes — written in the **L4 pseudo-language** (Haskell + TypeScript notation, fenced ```text; the same convention as L4/L3, `book/src/semantics/index.md`; the KaTeX `$`-sigil-must-be-fenced rule applies).

- **A small set of `library` chapters.** The partition **mirrors the 3 L4 doc-groups** — `iteration` (iteration & step combinators), `data-algebra` (data-algebra combinators & named verbs), `coordination` (outer-driver caps & coordination) — **bracketed** by a foundational **`types`** library (the genuinely *shared / cross-cutting* data-struct / record / type defs only — see the type-placement rule below) and a top **`drivers`** library (the entry-point surfaces lifted from the Feature section — the 5 sim drivers + lifecycle ROOT + output products — composing the calculus libraries). Seed design (5 libraries); the exact modularization is **refinable by use**.
- **Type placement — cluster a type with the API group it belongs to (user directive 2026-06-07).** A type / record def that **clusters with one implementation-API group** (e.g. `CgState` ↔ `iteration`, `EigState`/`SimState` ↔ `coordination`, a per-driver config record ↔ its `drivers` column) is placed **immediately BEFORE that API group**, **bundled with the type's *utility* API** — the type's own intrinsic namespace: constructors / smart-constructors, field accessors, predicates, trivial projections (a Haskell-style `where`/module-local utility cluster). The type's **consumer methods are NOT moved with it** — the substantive operators that *consume* the type to do the algorithm stay in the API group proper, AFTER the type+utility block. Only types that are **genuinely shared across ≥2 API groups** live in the foundational `types` library, ahead of all the groups that use them. (Topological order still governs overall: a type + its utility API precede their consumers.)
- **Each chapter is the IMPLEMENTATION rendering** of its operators — concrete def bodies in the L4 pseudo-language, **with code-doc sections** (per-def docstrings: explicit I/O sets, named shape contracts, the bunsen `# Arguments` / `# Returns` style).
- **Completeness — the library includes everything needed to "implement" the surface:** (i) the **data-struct / type defs** (all records — config records, per-solver state carriers, result types); (ii) **deep-linked unchanged lower-level artifacts** — where an L4 form is identity-in-form to its L3/L2/L1 version (deep-linked *because unchanged* across the rotation), the unchanged artifact is **rendered inline** in the library (it IS the implementation), not linked-away; (iii) **external kernels** — the opaque-library boundary kernels (libCEED quadrature, SLEPc eigsolve loop, triangular-solve / GS-SSOR — the existing kernel-API nodes) appear as **`#extern NAME`** in place of their implementation def, **after their type signature**.
- **Within a library, defs are in TOPOLOGICAL order** (a def appears after everything it uses).
- **Defs may use Haskell-style `where` clauses** to define private utility namespaces (a library's internal helpers).
- **A distinct chapter KIND — implementation-rendering, NOT a semantic restatement.** Per §SEMANTIC CONSOLIDATION + the record-definition obligation, the authoritative semantics / laws / record-defs live ONCE (in the L4 operator chapters / `semantics/index.md` / `concepts/<record>.md`); Synthesis **links to them** and renders the *synthesized code form*. It is the implementation VIEW (like generated code), parallel to the Feature spine's top-down entry-point VIEW. A rendered def's correspondence to its L4 chapter body is reviewable (`lowering-verifier` may audit it).
- **Ownership:** `layer-intro-author` authors the `# Synthesis` Part shell + the per-library chapter intros + the `types` / `drivers` libraries; `abstractor` / `harvester` render the per-operator synthesized defs; the `#extern` leaves trace to the kernel-API nodes (DIRECTIVE 3). (Memory `project_synthesis_section_directive`.)

## Cycle structure: primary cycle (5 phases) + meta-phase every 3rd

There are **two cadences**:

- **Primary cycle (5 phases)**: plan → dispatch → critique → repair → integrate. Fires every cycle. The forward-frontier loop.
- **Meta-phase**: fires **every 3rd primary cycle** (user directive 2026-05-27, post-cycle-006 meta). Examines evidence aggregated across the **last 3 primary cycles** and adjusts methodology.

```
  Primary cycle (×3 between meta-phases):
    cycle-planner → N specialized agents → N critics → N repairers →
      integrator-per-report ×N → integrator-finalize
      (serial)        (scatter; parallel)     (scatter)    (scatter)
                                                                (serial; one-at-a-time)  (serial)

  Every 3rd primary cycle, after integrator-finalize:
    meta-phase (serial; aggregates evidence across the 3-cycle batch)
```

**Cycle counter** keeps incrementing across batches: cycles 007, 008, 009 form one meta-batch; meta-phase fires after 009; then 010, 011, 012 form the next batch; meta-phase after 012; and so on. The cycle counter does NOT reset at meta-batch boundaries.

**Phase 1 — plan**: `cycle-planner` reads roadmap, priorities, friction-ledger, open-questions, recent integrator batches, integrator-signals tail. Emits a dispatch plan with `(agent, scope, deps)` tuples and an overlap analysis. Does not mutate the artifact.

**Phase 2 — dispatch**: up to 12 specialized agents per plan (user directive 2026-05-27 — raised from 8 mid-cycle-006 after first split-integrator cycle (005) ran 6 wave-mates with no token-budget pressure), parallel where non-overlapping. Each writes a single `CYCLE.md` under `reports/<timestamp>-<agent>-<scope>/`. No artifact mutation in this phase.

**Phase 3 — critique**: `critic` agent runs on each report (parallel). Runs the 8-check checklist (citation-validity, surface-or-evidence, rotation-quality, variant-axis-coverage, cross-reference-integrity, edge-label-fidelity, plan-kind-consistency, skill-uptake-survey). Writes META.md critique section.

**Phase 4 — repair**: `repairer` agent runs on reports with warning/fail findings (parallel). Mechanical and surgical fixes only — not substantive authoring. Writes META.md repair section. Sets `overall_status`.

**Phase 5 — integrate** (split cycle-004 → cycle-005 boundary for context-bound per-dispatch budget):
- `integrator-per-report` runs **once per ready report, dispatched serially** (not parallel — artifact writes naturally serialize). Each per-report dispatch applies ONE report's proposed-changes, runs per-report safety-net gates, promotes that report's Open questions, and appends a row to a per-cycle staging log (`reports/<cycle-id>-integrator-staging/STAGING.md`). Does NOT rebuild book, does NOT commit.
- `integrator-finalize` runs **once at the end**. Reads the staging log, runs `cargo make book`, repairs build breakage, updates roadmap (when measurable), appends to `cycle-record.jsonl`, writes `log/cycle-N.md`, prepends to `log/README.md`, appends to `scaffolding/integrator-signals.md`, marks consumed reports' `integrated_at`, emits the batch CYCLE.md, runs single `git commit && git push origin main`.

Sole writers of `book/`, `scaffolding/roadmap.md`, `log/`, `scaffolding/cycle-record.jsonl`, `scaffolding/open-questions.md`, `scaffolding/integrator-signals.md` — partitioned per role spec (per-report writes artifact + open-questions + staging; finalize writes roadmap, cycle-record, log, integrator-signals, plus commit).

**Meta-phase (fires after every 3rd primary cycle)**: `meta-phase` examines evidence **aggregated across the last 3 primary cycles** + running history. Records escalating trends in `scaffolding/friction-ledger.md`. Proposes plans, judges them, decides `go` / `no-go` / `ask` per plan. Enacts `go` items directly: writes to `.claude/agents/`, `skills/`, `scaffolding/priorities.md`. Surfaces `ask` items to human. Separate commit from integrator-finalize. The aggregated-batch view is intentional — single-cycle noise washes out; persistent 2-of-3-cycle patterns surface as real friction.

## The 14 agents

Definitions live under `.claude/agents/`. Dispatch via `Agent(subagent_type=<name>, ...)`. Per-dispatch report file convention is `CYCLE.md` (renamed from `REPORT.md` cycle-004 to bypass the Claude Code subagent Write filter on `report|summary|findings|analysis` keywords).

**Pre-dispatch (1):**
- `cycle-planner` (opus) — serial dispatch planner.

**Specialized dispatch (8, all opus):**
- `layer-intro-author` — writes L_n / L_{n+1}>L_n Part overviews + dep-maps + `book/src/concepts/<slug>.md` pages (broadened cycle-003).
- `harvester` — formalizes one L_n operator per invocation.
- `abstractor` — sketches one L_{n+1}>L_n theme + speculative L_{n+1} operators.
- `lifter` — re-anchors a theme to firmed-up vocabulary.
- `lowering-verifier` — audits one theme against evidence.
- `combinator-miner` — finds one recurrent pattern, proposes a combinator.
- `same-layer-cross-cutter` — one unification/redundancy/contradiction observation.
- `cross-layer-cross-cutter` — one cross-layer coverage-gap/edge-mismatch observation.

**Post-dispatch validation (2):**
- `critic` — runs 8-check checklist per report; META.md critique section.
- `repairer` — attempts mechanical fixes per finding; META.md repair section + CYCLE.md in-place edits; sets `overall_status`.

**Application (2 — split cycle-004 → cycle-005):**
- `integrator-per-report` — applies ONE report; appends row to STAGING.md; dispatched serially once per ready report.
- `integrator-finalize` — runs ONCE at cycle-end; rebuild book + commit + push + cycle-end housekeeping (cycle-record, log, integrator-signals, roadmap, batch CYCLE.md).
- (RETIRED) `integrator` — single-pass version; kept as historical reference.

**Methodology (1):**
- `meta-phase` — examines cycle evidence; records trends; proposes / judges / decides; enacts methodology adjustments.

## Layout

```
book/src/                  # the mdBook artifact
  L4/                      # Part: graph-evaluation calculus
    index.md               (overview + dep-map)
    <operator>.md          (one chapter per operator)
  L4-L3/                   # Part: L4>L3 lowering
    index.md
    <theme>.md
  L3/, L3-L2/, ..., L0/    # one Part per layer + lowering layer
  synthesis/               # Part: SYNTHESIS — synthesized-library implementation view (the L4 surface rendered as library code; placed BEFORE feature/)
  feature/                 # Part: FEATURE-SURFACE SPINE (entry-point composition roots)
  concepts/                # shared concept library (kept)
  design/                  # L4 calculus strawman (seeds L4 layer)
  meta-reviews/            # historical meta-review records (cycles 1–172)
.claude/agents/            # 13 agent definitions
reports/                   # per-invocation CYCLE.md + META.md channel
  <timestamp>-<agent>-<scope>/
    CYCLE.md
    META.md                (post-critique + repair)
    [supporting docs]
scaffolding/               # cumulative cross-cycle state (the workshop)
  roadmap.md               (relative-progress vs goals; integrator-maintained)
  priorities.md            (next-up list; meta-phase + cycle-planner co-edit)
  friction-ledger.md       (named friction patterns + recurrence; meta-phase-maintained)
  skill-candidates.md      (skill proposals; any-agent appendable)
  open-questions.md        (cross-cycle question ledger; any-agent appendable)
  cycle-record.jsonl       (per-cycle structured record; integrator + meta-phase append)
  problems-sensitivity.md  (problems/ filing-rate self-tuning; meta-phase-maintained)
  concept-dependency-map.md
  decisions/               (persistent-dual trade-off logs)
  test-linkages/           (source→test maps)
problems/                  # out-of-band concerns (any agent files; human reviews)
skills/                    # agent-invocable procedures (verbs; meta-phase promotes)
tools/                     # purpose-built evaluation tooling
log/                       # per-cycle human-readable summaries + README index
reference/                 # local clones of palace, bunsen, burn (gitignored)
mcp/codemap/               # the palace-codemap MCP server (Rust; backs MCP-first localization)
MIGRATION.md               # structural-redirect spec — compacted history-stub (full text in git history)
BOOTSTRAP.md               # original phased build spec — compacted history-stub (full text in git history)
# (batch-31 meta-phase non-book-orphan-review DELETED the decommissioned pre-redirect artifacts:
#  orchestrator/ + prompts/ + schemas/ + lessons.md + questions.md + README.md + episodic.jsonl.README.md.
#  All are recoverable from git history; CLAUDE.md is now the live operational guide.)
```

## Write-authority partition

| Agent | Writes to |
|---|---|
| cycle-planner | `reports/<id>/CYCLE.md` + `scaffolding/priorities.md` (**the plan** — co-owned with meta-phase; append fresh fan-out-ranked candidates + mark dispatched picks; does NOT do batch-level intake migration/compaction) |
| 8 specialized | `reports/<id>/CYCLE.md` + supporting docs in same dir only |
| critic | `reports/<id>/META.md` critique section |
| repairer | `reports/<id>/META.md` repair section + in-place edits to CYCLE.md / supporting docs |
| integrator-per-report | `book/` (per-report proposed-changes), `scaffolding/open-questions.md` (append-only), `reports/<cycle-id>-integrator-staging/STAGING.md` (append-only) |
| integrator-finalize | `book/` (build-repair only), `scaffolding/roadmap.md`, `scaffolding/cycle-record.jsonl`, `scaffolding/integrator-signals.md`, `log/`, `reports/<id>-integrator-finalize-cycle-N/CYCLE.md`, per-consumed-report `integrated_at` frontmatter touches |
| meta-phase | `.claude/agents/`, `skills/`, `scaffolding/priorities.md`, `scaffolding/friction-ledger.md`, `scaffolding/skill-candidates.md` (status updates), `scaffolding/problems-sensitivity.md`, `scaffolding/open-questions.md` (**unify only** — close/migrate/compact at meta-phase; see §Methodology invariants "Open-questions ledger is unified by the meta-phase"), channel-format specs |

**Any-agent-appendable** (append sections, never edit existing):
- `scaffolding/skill-candidates.md`
- `scaffolding/open-questions.md` (append-only between meta-phases; meta-phase has unify/edit authority — see partition note above)
- `scaffolding/decisions/`
- `scaffolding/test-linkages/`

## Methodology invariants

These are load-bearing — do not "improve" them away.

- **⟢ VOCABULARY-SHIFT REDIRECT (user directive 2026-06-01; full spec `METHODOLOGY-REDIRECT.md`).** The stack is a sequence of genuine **representational + component-vocabulary shifts**, NOT a rectangular projection. Each layer is complete/concise/correct **in itself**, and the **conciseness** constraint is the engine that drives **in-layer utility combinators/abstractions** (mined *inward* to simplify the layer; distinct from cross-layer themes). Each lowering is a **translation across vocabularies and semantic organizations — NOT a 1:1 named-term rename**; a degenerate identity-in-named-terms lowering is a **smell** (the vocabulary failed to shift — resolve as a thin in-line note or a combinator re-expression, NOT a mirrored entry + thin theme). The model is **fold/combinator-primary**: the combinator is the entry, leaves are specialization notes. **Combinator-miner re-mandate:** replace-and-propagate, not mine-and-strand. **Solvers (all 5 pipelines + FE assembly) are a LOW-PRIORITY test-load on the shared spine** — they advance a layer only when **cleanly describable** in existing shared vocabulary, NEVER by forcing the spine; what a solver can't cleanly say is a finding about the spine. (Supersedes the 2026-05-31 rectangular-floor machinery + the batch-14 "L4 complete / pivot" framing — see `METHODOLOGY-CHANGELOG.md`.) **The combinator-miner / harvester / abstractor / cycle-planner / layer-intro-author role-specs carry the matching bullets.**
- **⟢ SEMANTIC CONSOLIDATION — semantic definitions are a first-class actively-managed surface (user directive 2026-06-06).** Semantic rules/defs/abstractions **about the language and the spec** (the calculus grammar, shape semantics + named shape groups, the L4/L3 pseudo-language notation invariant, monad/ownership/reduction-rule/scalar-promotion conventions) are held under the **same liveness / unification / consolidation discipline** the graded-stack two-axis machinery applies to vocabulary. **The rule: a semantic rule/def/abstraction lives ONCE, at the semantic surface; functional-unit (operator/theme/layer-intro) entries USE + LINK, they do NOT RE-STATE.** A semantic rule restated at a functional-unit scope is the **semantic analog of a degenerate identity-lowering smell / un-grounded detritus** — resolve it by **relocation-to-the-surface + a back-link**, not duplication. **The surface** is `book/src/semantics/index.md` (relocated from `book/src/design/l4_calculus.md` at cycle-116) — promoted out of "design strawman" status into the project's **active semantic-management surface**, placed **BEFORE the `# L4` Part** in `SUMMARY.md` ordering (under the top-level `# Semantic surface — calculus, rules & abstractions` Part). Its active-management discipline is `semantics/index.md` §0.1. **Ownership:** `layer-intro-author` authors/maintains the surface + executes the restatement-cohort relocation sweeps; the producers (`harvester`/`abstractor`/`combinator-miner`/`cross-layer-cross-cutter`/`same-layer-cross-cutter`) carry the USE+LINK-don't-restate-semantics discipline; the `meta-phase` owns the surface's every-batch liveness/unification refresh (a standing duty, the semantic analog of the GC sweep) + migrates restatement-cohort sweeps into the plan. The c115 D3 `linear_combination`-entry relocation was the pilot; the 27-file restatement cohort (OQ `named-shape-groups-general-rule-restatement-cohort-extent`) is governed by this directive. (Memory `project_semantic_consolidation_surface`.)
- **⟢ FINALIZATION — the book is a STATIC-STATE finalized surface, not a process log (user directive 2026-06-08; batch-47; codified batch-48 meta-phase; memory `project_finalization_debulk_directive`).** A `book/src/**` chapter states **what each component IS** in finished form; it carries **NO process/judgment accounting** — no `## Status` promotion-history prose, no inline `cycle-NNN`/`cNNN` attributions, no `verified_against:` yaml blocks or `## Verified-against` sections (citations live under `## Evidence`), no `reports/…` pointers, no "this dispatch"/"self-verified"/lifting-deletion/corpus narrative, no forward-process speculation. **Firmness lives in frontmatter `rank:`/`firmness:`** — a firm frontmatter-rank entry has NO `## Status` prose; a **non-firm** entry keeps a CONCISE static unresolved-state token + promotion-condition. **`## Status`-as-sole-rank-carrier subtlety:** for the no-frontmatter-rank chapters (the L1/L1-L0/L2/L3/L0 prose-dep-map convention), the prose `## Status` leading token IS the sole rank carrier — keep it concise, **never strip it** (de-bulk must not delete it). Coupling concepts ("compare to X", "relationship to Y") are LIFTED to explicit `## Relationship`/`## Structural fact`/`## Scope` sections, not left as process notes. **This is a standing invariant, not a transient campaign:** producers do not re-introduce the accounting (the 5 content-authoring role-specs carry the matching re-accretion blockquote); the 2 skills are `finalization-debulk` (strip/keep/lift discipline) + `heading-metadata-hygiene` (heading status/classification tails → structured `**Status:**`/`**Kind:**`/italic lines, distinguishing glosses KEPT for TOC navigability, `## Status` rank-carriers NEVER touched). Exemplar: `book/src/L4/krylov-step.md`. **Carve-out (NOT de-bulked):** `book/src/methodology/goal-flow.md` + `book/src/meta-reviews/*` are process records / regenerated mirrors. **Build invariant (integrator-finalize step-5d):** no rendered page may contain its own frontmatter — the `book/strip-frontmatter.py` mdBook preprocessor strips the leading YAML block for rendering; the step-5d post-build guard asserts no built HTML leaks a frontmatter `key:` paragraph (analog of the step-5c KaTeX assertion). **Legal-identifier chapter-naming convention** (user directive 2026-06-08; memory `project_code_identifier_chapter_naming`): chapters for named **code artifacts** use legal-identifier filenames — **operators snake_case** (`iterate_while.md`, `krylov_step.md`), **struct/record concept pages PascalCase** (`concepts/OpParams.md`, `concepts/SimState.md`); **descriptive theme/multi-word chapters stay hyphenated** (`*-mutation-rotation`, `*-dissolution`, `matrix-free-operator-apply`, `eigsolve-impl`). The `harvester`/`abstractor`/`layer-intro-author` role-specs carry this.
- **⟢ KERNEL-API vs kernel-IMPLEMENTATION distinction — spine-dependency opaque-library kernels get BOTH surfaces, reviewably linked (user directive 2026-06-07, DIRECTIVE 3; full enactment in the rescope meta-phase report; memory `project_kernel_api_impl_distinction`).** EXTENDS the `project_blackbox_vs_accelerated_kernels` disposition: a black-box / opaque-library kernel that is **a dependency of something firm in the spine** AND has **a well-understood implementation in terms of the semantics we already have** now gets BOTH (a) a **kernel-API surface** node and (b) a **kernel-implementation** node — instead of only the opaque-rise. **The structural mechanics (sensible-default, decision-to-be-refined-from-use):**
  - **(a) kernel-API surface** = the EXISTING obstruction theme, **repositioned as "the API."** It keeps `status: obstruction (opaque-library-ownership)` (it genuinely IS the opaque boundary/contract the spine calls), and its `## Status` line gains the role-label **`kernel-api`** (the reviewable token; "this node is the kernel API contract"). It documents what the spine calls — signature + semantics + the library boundary. NO claim that it is implemented; the claim-free obstruction discipline is intact.
  - **(b) kernel-implementation** = a NEW **constructive chapter** (at the appropriate L-layer) realizing the kernel **in our L-vocabulary / tensor-algebra**, from our already-firm primitives. It carries a normal `rank`/`status` (`rough-in`→`firm` on the usual gates) and its `## Status` line gains the role-label **`kernel-impl`**. It has the ordinary `depends-on` edges to its from-our-primitives constituents (rank-constrained, GC-live).
  - **The reviewable link** = a typed **`realizes-kernel-api`** edge from the impl node → the API node, of edge-class `reference` (navigational, free — the impl does NOT block on / depend-on the opaque API; the relationship is a *correspondence to be reviewed*, not a build dependency, so it must NOT constrain rank or carry liveness). The linters ignore the `realizes-kernel-api` label via the existing optional-`kind:`-is-documentation mechanism — **no new linter edge-semantics required** (minimal blast radius). A reviewer reads BOTH the black-box contract (a) AND the from-our-primitives version (b) and checks they match; `lowering-verifier` audits the impl-realizes-API correspondence.
  - **Carve-out (PRESERVED):** **enum-only-stubs** (MINRES/BiCGStab, `MFEM_ABORT`) are NOT external-kernel callouts and are NOT spine dependencies → they STAY single-node obstruction-documented; do NOT manufacture an impl node for them (`project_unimplemented_palace_components` governs). The trigger for the dual-surface is the conjunction **spine-dependency AND well-understood-in-our-semantics**; absent either, the single obstruction node stands.
  - The founding kernels (each a spine-dependency opaque-library obstruction with a known in-our-semantics impl): the **libCEED element-quadrature kernel** (`fe-assemble-libceed-boundary-obstruction.md` → impl = matrix-free FE operator application as tensor contractions), the **triangular-solve / GS-SSOR relaxation** (`triangular-solve-obstruction.md` → impl behind the multigrid smoother, sequential-obstruction noted for the recurrence), the **SLEPc EPS eigsolve loop** (`L3/eigsolve.md` partial-obstruction → impl = constructive Lanczos/Arnoldi/Krylov-Schur in our `lanczos_step`/`krylov-step` vocabulary). `harvester`/`abstractor`/`combinator-miner` carry the author-both-and-link discipline; `layer-intro-author` carries the chapter-kind mechanics; `lowering-verifier` audits the correspondence; `meta-phase` tracks the API/impl integrity as a standing duty.
- **The plan is the single ongoing work artifact; intake channels feed it, they don't hold work** (user directive 2026-05-28). `scaffolding/priorities.md` is **the plan**: the durable, fan-out-ranked backlog, co-owned by `meta-phase` + `cycle-planner`. `open-questions.md`, `friction-ledger.md`, `problems/` are **intake channels** — issues are *reported* there, not parked. **Resolution = migration:** the meta-phase's every-batch §Intake→plan migration triages intake, migrates actionable items into the plan (ranked by fan-out), closes resolved/stale/duplicate, keeps blocked items compacted with a trigger. `cycle-planner` dispatches **highest-fan-out work first**. `roadmap.md` is the coverage map + the **fan-out impact model** (`|concepts| × |downstream-reuse| × 1/cost`) that ranks the plan. An item lingering in its intake channel without a plan item means migration hasn't happened — that is the defect to catch, not unbounded ledger growth.
- **Citations are mandatory.** Every claim carries `(file, start_line, end_line)`. No citation, no claim. Citation format: plain text `relative/path/file.ext:start-end` (relative to `reference/`).
- **Roles do not share context.** Each subagent dispatch gets its own isolated context. The critic in particular must not see the producer's chain-of-thought.
- **Reports are append-only after integration.** After `integrated_at:` is set, CYCLE.md content is not edited. (Repairer may edit pre-integration; bounded by repair authority.)
- **Commit every cycle, pass or fail.** The integrator commits + pushes. Atomic operation: artifact + scaffolding + log + book output as one commit.
- **Push after every commit.** `git commit ... && git push origin main` chained. No commits sitting locally between turns.
- **Spec growth is monotonic and visible in `git log`.** Realized as CYCLE.md proposed-changes blocks parsed by the integrator.
- **If a step is ambiguous, stop and ask the human.** Don't improvise around the spec.
- **L4 strawman (`book/src/semantics/index.md`, relocated from `book/src/design/l4_calculus.md` at cycle-116) is in-management for L4 and L3 work** (user directive 2026-05-27). It is the authoritative reference for L4 calculus conventions (BNF grammar, reduction-rule format, `iterate_while` / pruning / monad semantics); L4 and L3 entries cite and continue it, they do not displace it. Precedent examples to read before authoring new L4/L3 content: `book/src/L4/krylov-step.md` + `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`.
- **L4 and L3 pseudo-language is Haskell + TypeScript notation in fenced code blocks** (user directive 2026-05-27). Signatures use Haskell `::` arrow form; records use TS brace form `{ field: type }`; bodies use do-notation + lambda; fenced as ` ```text `. Reduction rules / small-step semantics use LaTeX `$$ ... $$`. Do not transcribe L4/L3 forms into prose or invent new notation — the strawman (`book/src/semantics/index.md`, relocated from `book/src/design/l4_calculus.md` at cycle-116) carries the canonical, settled convention.
- **Primary-context reset is covered by the post-meta session restart; there is no separate `/compact` step** (user directive 2026-05-29). The meta-phase routinely enacts role-spec changes, so the parent restarts the session before the next cycle (friction-ledger `new-agent-defs-need-session-restart`); the restart resets primary context, subsuming the old `/compact` step. Do **not** emit `/compact` asks at meta-phase end. Mechanics + retired-directive history: `.claude/agents/meta-phase.md` §Post-meta session restart + `METHODOLOGY-CHANGELOG.md`.
- **Meta-phase runs every 3rd primary cycle** (user directive 2026-05-27) — see §Cycle structure for the cadence. Rationale: single-cycle noise washes out in a 3-cycle window, so persistent patterns surface cleanly. The cycle counter does not reset at batch boundaries. The meta-phase report filename uses the cycle-id of the third (final) cycle in the batch.
- **Layers are defined high→low; lifting notes go in working notes** (user directive 2026-05-27). Higher-layer entries are defined **in terms of themselves** (own-layer vocabulary, or higher-layer references), NOT in terms of lower-layer vocabulary. Lowering themes (`L_{n+1}>L_n`) narrate "**how the L_{n+1} form lowers into the L_n form**" (LHS L_{n+1}, RHS L_n). Reverse-direction notes (how L_n lifts up, what evidence/structure the lift needs) live in **working notes** (`scaffolding/`, supporting docs, OQ ledger), NOT formal chapter content. Practical consequence: an L_n operator entry's Semantics/Laws/Signature live in L_n vocabulary; the L_n>L_{n-1} dispatch does the lowering. Defining an L_n operator via L_{n-1} primitives means the content belongs in an L_n>L_{n-1} theme, not the entry.
- **Lower-level shared vocabulary takes priority** (user directive 2026-05-27). When choosing between (a) expanding higher-layer vocabulary further and (b) populating lower-layer shared utility, **prefer (b)**. Reusable lower-level vocabulary makes other components cheaper and simpler to describe, enables unification of seemingly-distinct higher-layer patterns, and reduces duplication explosion in adjacent layers. (A cycle-006/010-era concrete snapshot that illustrated this is archived in `METHODOLOGY-CHANGELOG.md`.)
- **Uniform pull-up L0→L4; foundation-solidity is a ranking weight** (user directive 2026-05-31) — **SUPERSEDED by the VOCABULARY-SHIFT REDIRECT** (the "rectangular" success metric was the bug; the `foundation_solidity` / count-ownership / dual-registration rectangular-floor machinery is retired). Full text in `METHODOLOGY-CHANGELOG.md`. The surviving principle is "Lower-level shared vocabulary takes priority" (above), which the redirect keeps.
- **Identity-lowerings still require both L levels** (user directive 2026-05-27) — **SUPERSEDED by the VOCABULARY-SHIFT REDIRECT** (a degenerate identity-in-named-terms lowering is now a *smell*, not a mirrored entry). Full retired text in `METHODOLOGY-CHANGELOG.md`. The live convention for genuine non-adjacent identity relationships is the "Identity rotations across non-adjacent layers are annotated in-line" bullet below.
- **Phase 1 corpus was lifted and deleted** (user directive 2026-05-27; campaign COMPLETE cycles 097/098/099, batch-31 graded-stack P2). `book/src/spec/slices/` was **raw material for the layered artifact**, not the deliverable. Every slice's material has now been lifted into firm layered entries (or homed in a `roadmap_goal` chapter), the lifted form is authoritative, and **the corpus has been fully deleted — 9→0; `book/src/spec/` no longer exists** (the corpus shrank monotonically; git history is the record). **The `annotated-and-retained` canonical-instance carve-out is RETIRED** (corpus-complete moot) and the skill `phase-1-slice-reduction-audit` is **archived under `skills/_retired/`** — both were transient mechanisms for the now-finished campaign. The in-discipline replacement for "a real-but-undissected referent that needs a live home" is the graded-stack **rank-0 `roadmap_goal` chapter** (§GRADED RESOLUTION LADDER below), not a retained slice. (Full retired text of the reduction-audit invariant + carve-out: `METHODOLOGY-CHANGELOG.md`.)

- **Theme/operator status `partly-constructive` is first-class** (cycle-012). Alongside `firm` / `rough-in` / `obstruction`: firm in structural decomposition (the rewrite is recognized and exhaustively cited) but carrying a named, citation-backed caveat on one or more **constructive sub-parts** — a status value / result field / error condition materialized from negative anchors / literature rather than read from a positive Palace site. The entry MUST state (i) which sub-part is constructive, (ii) its negative-anchor citations, (iii) an explicit **promotion condition**. Do NOT mark it `firm` (the sub-part isn't) and do NOT downgrade to `rough-in` (the structure IS firm). These negative anchors are evidence FOR a faithful reconstruction; they do NOT license a positive claim without a positive site. A transient gate, not a permanent escape hatch. Promotion checklist: skill `partly-constructive-promotion-checklist`.

- **Two rough-in qualifiers are first-class: `rough-in (test-coverage-bounded)` and `partial-obstruction`** (cycle-021 meta-phase codification of two status tiers in live use since cycles 009/013). These sit alongside `stub` / `rough-in` / `partly-constructive` / `firm` / `obstruction` and name two recurring "structurally-anchored-but-not-promotable-yet" situations distinct from `partly-constructive`:
  - **`rough-in (test-coverage-bounded)`** — the structural signature is well-anchored at L0 but **algebraic-law confidence is reduced pending dedicated test coverage OR expanded literature anchoring**. Stays `rough-in` because the laws are stated-but-unconfirmed, not because the structure is unknown. Promotion route: a dedicated unit test at the exact entry point (may be out of write-scope), OR a literature-anchor harvester/lowering-verifier pass raising law-confidence to `ksp_solve`-equivalent. Distinct from `partly-constructive` (structure firm, *laws* test-gated, not a constructed sub-part). **The firm-on-positive-structure escape** (load-bearing): an entry whose laws are **syntactic identities on fully-specified positive source** (operator-algebra on a read closure) is `firm` even with no surrounding test, because the missing test does not gate syntactic-identity laws — the `apply_linop` situation, NOT the `eigsolve`-convergence-semantics situation. (This escape promoted `apply_nonlinear_pencil`, `eigenfreq_qfactor_reduce` c082, `sparameter_reduce` c083, `solve_family` c086.)
  - **`partial-obstruction`** — used at L3 for an operator whose **per-step body lifts cleanly to a global tensor-field expression but whose loop structure does NOT lift** (an inner recurrence and/or outer sweep is a witnessed `sequential-obstruction` with a cited non-removability reason). The status reflects the **loop, not the body** (the body is identity-in-form to the lower layer; the obstruction is the un-liftable iteration). Distinct from a whole-operator `obstruction` — here the operator IS implemented and its body IS lifted; only the loop resists. Precedent: `book/src/L3/chebyshev.md`.

- **Obstruction themes have two sub-kinds, named inline in the `## Status` line** (cycle-030), because the routing each encodes differs:
  - **`obstruction (enum-only-stub)`** — Palace ships an *internal* stub (JSON / enum / aborting-branch config whose method body is `// TODO` / `MFEM_ABORT` / empty): named in the config surface but not implemented. Promotion route: a future Palace upstream change fills in the body. Default when the TODO/aborting branch is on a Palace-owned method body.
  - **`obstruction (opaque-library-ownership)`** — the functionality is available ONLY through a library boundary (HYPRE relax-types, SLEPc EPS loop, external direct-solver wrappers); Palace never exposes it as a standalone callable. Promotion route: NONE (stays obstruction unless Palace re-architects). The theme's value is documenting the boundary + cataloguing negative anchors. Default when the entire callable lives outside Palace.

  The sub-kind tag is mandatory for new obstruction themes. Producer-side detail in `abstractor` §Discipline; the negative-anchor procedure is skill `establish-negative-finding-exhaustiveness`.

- **⟢ GRADED RESOLUTION LADDER + FEATURE-ROOT REACHABILITY (user directive 2026-06-04; full spec `METHODOLOGY-GRADED-STACK.md`).** The artifact has **two orthogonal, mechanically-checkable axes**. **Axis 1 — resolution + well-foundedness:** the maturity ladder is a total order with a rank — `roadmap_goal = 0 < stub = 1 < rough-in = 2 < firm = 3` (`partly-constructive` / `rough-in (test-coverage-bounded)` are sub-ranks ≈2.5; `obstruction` is a separate *kind*, itself rankable). The **well-foundedness invariant**: for every `depends-on` edge `u → v`, `rank(u) ≤ rank(v)` — **an entry is at most as resolved as its least-resolved dependency** (so `firm` rests only on `firm`; `roadmap_goal` may rest on anything, including other roadmap_goals). This subsumes "a reduction is as firm as its least-firm folded primitive" (the `k=3` case) and the feature OWN-COMPOSITION rule. **`roadmap_goal` is a real book chapter** (rank 0) — the in-discipline replacement for the retired `annotated-and-retained` slice: claim-free, carries intent + pulled-by provenance + declared deps + accreting working context, links resolve natively. The abstractor's speculative L_{n+1} sketches land here. **Axis 2 — reachability / liveness:** the FEATURE-SURFACE SPINE columns are the **root set** (`seed` = root marker, NOT a ladder rung); reachability from the roots over `depends-on` edges = liveness; an unreachable node is **garbage** (the detritus hunt IS a mark-sweep from the roots; orphaned-intent GC and detritus GC are one sweep). **Shared substrate:** one typed dependency graph — `depends-on` (blocking: constrains rank AND carries liveness) vs `reference` (navigational, free; an edge to a *root* is `reference` — which is where OWN-COMPOSITION comes from); optional `kind:` is documentation the linters ignore. **Two linters under `tools/`** (rank check + reachability GC). **Adoption:** type-the-edges-and-audit is ONE whole-artifact campaign; audit-first, hard-gate-new, bounded tracked baseline-exceptions (not open-ended fix-forward). Role bullets carry the matching responsibilities; `book/src/methodology/resolution-ladder.md` is the reader-facing mirror.
- **Integration may materialize implied components as stubs** (user directive 2026-05-28; **maturity-tier language revised by the 2026-06-04 graded-ladder directive above** — the thinnest tier is now `roadmap_goal` (rank 0), and `stub` is rank 1). A **`stub`** is a *claim-free placeholder*: a real file (or dep-map row) with `status: stub` frontmatter, a one-or-two-line sketch, an **"Implied by"** provenance list, and a "Refinement pending" note. (The `stub` vs `roadmap_goal` line: a `stub`'s referent is *real but undissected* and rests on ≥-stub deps; a `roadmap_goal`'s referent is *intended/speculative* and may rest on anything — see `METHODOLOGY-GRADED-STACK.md` §1e.) Purpose: cross-references resolve to a **live link** instead of a perpetually-deferred plain-text forward-ref (a live link to a missing file is a hard `linkcheck2` error). **Who/when:** `integrator-per-report` or `integrator-finalize` MAY create a stub for a *clearly-implied* component (**bar:** ≥2 converging references, or a rough-in row already standing for it — not merely speculative); stub-creation is the **preferred** resolution, plain-text-defer the fallback. **Critic handling:** a stub makes no claims, so the citation/surface/rotation/variant-axis checks no-op; the critic verifies only that it carries provenance and is wired into `SUMMARY.md`.
- **Records/structs get a definition home — never described only by their USE** (the record-definition obligation, user directive 2026-06-03). A record named in a signature (config record, per-solver state carrier, L4 record type, `{ field: type }` result) must have a home defining it **in itself** — fields, types, meaning, the construction-vs-run-time stratum of each, and the L0 home of the backing C++ struct / `IoData` surface — NOT only how functions use it. By reuse: **only one** consumer → in-chapter `## Record definition` section (harvester/layer-intro-author); **≥2** consumers → a `book/src/concepts/<record>.md` page (layer-intro-author). The page defines the *data shape*; operators define the *behavior* (don't restate operator algebra there). Producer obligation: define it (single-consumer) or flag `record-<name>-needs-definition-home` in Open questions. Critic `surface-or-evidence` sub-check flags a signature-named record with no home. Codified into `harvester`/`layer-intro-author`/`critic`.
- **Identity rotations across non-adjacent layers are annotated in-line, not via a dedicated lowering directory** (cycle-012). Lowering directories are **per-adjacent-edge only** (`L4-L3/`, `L3-L2/`, `L2-L1/`, `L1-L0/`). When an operator's identity-in-form spans **non-adjacent** layers (e.g. its L3 body is value-thread-isomorphic to its L1 form via an identity-like L2 absorption), that relationship is the transitive consequence of the adjacent-edge themes — annotate it **in-line** in the L_n entry ("Downward to L_{n-1}" prose + dep-map) citing those themes; do NOT create an `L3-L1/`, `L4-L2/` directory. Re-open only if a genuine NON-identity non-adjacent rotation surfaces that the adjacent themes don't compose to capture (none has).

## Process model: push-forward, push-back; the stack is a research artifact

**The stack is not the deliverable. It is a research artifact whose construction yields the understanding that *is* the deliverable.** Layers exist to expose friction. The valuable signal lives in the friction.

- **Push-forward, one slice / theme / operator at a time.** A layer's job ends as soon as the next layer can speak.
- **Push-back when friction surfaces.** While working at layer N+1, if a different framing of layer N would make N+1 dramatically easier, restructure layer N.
- **Move sideways** when progress on one slice is blocked. Use the sideways move to surface unification opportunities.
- **Explore alternative formulations when they exist; coalesce by use.** Persistent duals are permitted when they capture genuinely distinct aspects; not permitted when they cause duplication explosion in adjacent layers.
- **Accumulate a working surface with embedded problems.** Revise verdicts APPLY the diff (surface accumulates with friction embedded). Only `reject` blocks application.

## Optimization tricks vs. base algebra

A significant fraction of Palace's C++ exists because it was tuned for CPU + cache + SIMD. That cost model is not burn's, and most of the resulting code shape is counter to the goals of a pure GPU tensor implementation.

- **Transparent performance tricks** (fusion, tiling, packing, batching, memory layout, recomputation-vs-lookup) — algebraically equivalent to their unfolded form. The L1 form is the unfolded form; the trick gets a one-line note.
- **Load-bearing numerical tricks** (non-associative reduction orderings, fast-math, mixed-precision intermediates, deterministic-vs-atomic accumulation) — **part of the algorithm**. Preserve as explicit algebraic claims with the property they buy (determinism, condition-number, IEEE compliance) called out.

When in doubt, the critic flags as `unclear` and the human triages. Mis-classifying a load-bearing trick as transparent silently changes the algorithm.

## Tests as semantic supplement

Palace's unittests under `reference/palace/test/unit/` are **semantic documentation**, not just regression scaffolding. A test that constructs input, calls a function, and asserts on the resulting state is direct evidence of mutation pattern, algebraic semantics, and whether a trick is load-bearing.

- **Specialized agents** look for tests when localizing source. Cite tests alongside source ranges — tests are L0-equivalent.
- **Critic** consults tests when verifying claims. A test assertion contradicting a claim is `citation-does-not-support`.
- Test linkages tracked in `scaffolding/test-linkages/`.

## Scope

**⟢ THE 2026-06-07 RE-SCOPE — three directives that END the plateau (full enactment: the out-of-band rescope meta-phase `reports/2026-06-07T035336Z-meta-phase-rescope-directive/CYCLE.md`; memory `project_rescope_2026_06_07`).** The batch-36/37/38 plateau was an artifact of three now-LIFTED postures. The redirect's HOW-to-express-vocabulary discipline (vocabulary-shift, graded stack, no-forced-rectangular-pull-up) is UNCHANGED; this re-scope governs WHAT is now the forward frontier. The three directives, in scope terms:

- **DIRECTIVE 1 — Sharding / MPI is a DEFERRED future direction, NOT active work** (supersedes the bare "MPI out of scope, flag once" line below, refining it). The MPI implementation is grounded in a sharding theory assuming a lifetime structure **the spine has deeply re-written**; lifting the MPI-associated version (`linalg/rap.{hpp,cpp}` `ParOperator`/RAP parallel assembly; the mesh-distribution protocol `utils/geodata.cpp`; the MPI collectives `linalg/vector.hpp`, `utils/communication.hpp`) **may be DESTRUCTIVE to the current abstraction spine → DO NOT lift it now.** Record **sharding-into-component-blocks as a FUTURE GOAL** (a `roadmap_goal`-class future-direction note, NOT active work). The **sharding MATH** (decomposition as a mathematical abstraction on tensor-field problems) MAY be lifted **IFF non-destabilizing to the spine** — exploratory/optional, explicitly NOT the active campaign, gated behind a HARD non-destabilization check. NET: MPI/distributed stays OUT of active scope; the sharding-math-as-decomposition-abstraction is a deferred candidate with a hard spine-non-destabilization gate.
- **DIRECTIVE 2 — Existing deferred IN-SCOPE work is LIFTED THROUGH** (LIFTS the STOP-PROPOSING / demand-gated-deferral posture for the in-scope deferred set). The forward frontier is now: **build the grounded in-scope consumers and discharge the RE1-RE10 baseline-exceptions + the demand-gated vocabulary.** The grounded consumers, ranked by fan-out: **(1) the geometric-multigrid preconditioner** — THE highest-fan-out lead (Palace-authored: `linalg/gmg.cpp` V-cycle, `linalg/distrelaxation.cpp` Hiptmair smoother, `linalg/ams.cpp` AMS auxiliary-matrix construction); building it is the named consumer that discharges **RE9** (`fe_space_hierarchy` level-stack prolongation), **RE1** (chebyshev/jacobi smoother leg), **RE5/RE7** (diagonal-preconditioner apply/extract + normalize/reciprocal chains); single-machine-valid (parallelism is by composition). **(2) AMR** (adaptive mesh refinement) — Palace-authored estimate→mark→refine loop (`drivers/basesolver.cpp:188-272`, flagged-OUT at `main.cpp:304`; the Dörfler marker `utils/dorfler.cpp` read single-rank; the ZZ flux-recovery estimators `linalg/errorestimator.cpp`); single-machine-valid. **(3) deflate / NLEPS (RE3)** — lifts through when its NLEPS-deflated-eigensolve / preconditioner consumer surfaces. **(4) the L3 iteration-views (RE2 orthogonalize, RE8 fold_solve/krylov-step)** — need a feature column composing the iteration-rotation form BY NAME. **(5) the axpy-family arity leaves (RE6)** — the combinator-arity-notes refactor. Building these consumers FIRES several RE promotion conditions — re-check the RE set as each lands.
- **DIRECTIVE 3 — External-kernel callout stubs that are SPINE DEPENDENCIES are LIFTED, preserving the kernel-API vs kernel-IMPLEMENTATION distinction** (revises "document obstructions, don't fill them" FOR opaque-library obstructions that are spine dependencies; the enum-only-stub carve-out below is PRESERVED). See §Methodology-invariants "Kernel-API vs kernel-IMPLEMENTATION distinction" for the structural mechanics. The spine-dependency opaque-library kernels to DEVELOP a constructive impl for: the **libCEED element-quadrature kernel** (inside the firm `fe_assemble` fold; impl = matrix-free FE operator application as tensor contractions); **triangular-solve / GS-SSOR relaxation** (behind the multigrid smoother; impl well-understood, sequential-obstruction noted for the recurrence); the **SLEPc EPS eigsolve loop** (under the eigenmode driver; impl = constructive Lanczos/Arnoldi/Krylov-Schur in our existing `lanczos_step`/`krylov-step` vocabulary).

- **Target deployment is a single machine.** CPU → GPU via burn's device backends. MPI / multi-rank distribution is **out of active scope** (DIRECTIVE 1: a deferred future direction with a hard spine-non-destabilization gate, NOT merely "skip") — flag once and skip the MPI-associated version. In MFEM, `Par*` types (`ParGridFunction`, `ParBilinearForm`, `HypreParVector`, …) are read as their single-rank equivalents. **Single-machine-valid grounded consumers (geometric-multigrid preconditioner, AMR) ARE in active scope** — their parallelism is by composition; read the distributed Dörfler marker / RAP assembly single-rank.
- **Solvers in scope: all 5.** Electrostatic, magnetostatic, eigenmode, driven, transient.
- **Mesh / FE-space construction in scope.** MFEM-equivalent FE assembly is dissected alongside the solver pipelines. **AMR (adaptive mesh refinement) is now in active scope** (DIRECTIVE 2 grounded consumer-(2)).
- **Unimplemented Palace components: TWO distinct sub-kinds with DIFFERENT dispositions** (user directive 2026-05-27, REFINED by the 2026-06-07 DIRECTIVE 3).
  - **Enum-only-stubs STAY obstruction-documented** (the carve-out, PRESERVED). When Palace ships a stub (enum-only / JSON-only / aborting-branch config — e.g. MINRES/BiCGStab routing to `MFEM_ABORT` at `linalg/ksp.cpp:53-57`): **document it** as an L1>L0 obstruction theme with negative-anchor citations; **do not target it for filling in**. These are NOT external-kernel callouts and are NOT spine dependencies (nothing firm depends on them; they are alternative config tokens). The literature-anchored L1 form may inform higher abstractions (promote a speculative L1 operator to firm only when small AND it simplifies higher forms — e.g. `lanczos_step` factoring `krylov-step`'s symmetric case). (Memory `project_unimplemented_palace_components` — stays valid for enum-stubs.)
  - **Spine-dependency opaque-library kernels are now LIFTED with a constructive impl** (DIRECTIVE 3). An `obstruction (opaque-library-ownership)` theme that is a **dependency of something firm in the spine** AND has a **well-understood implementation in terms of the semantics we already have** now gets BOTH a kernel-API surface (the existing obstruction theme, repositioned as "the API") AND a kernel-implementation node (the constructive realization). See §Methodology-invariants "Kernel-API vs kernel-IMPLEMENTATION distinction". (Memory `project_kernel_api_impl_distinction`.)

## Target system

**AWS Labs Palace** — <https://github.com/awslabs/palace>. C++ (~85% of tree), CMake ≥ 3.24, MFEM + libCEED + MPI + BLAS/LAPACK + optional CUDA/ROCm.

- Many symbols resolve into upstream libraries (MFEM, libCEED). Specialized agents cite Palace source, not vendored upstream. If a question requires upstream behavior, log as open question.
- Heavy C++ templates — read tightened regions; prefer narrow text-search before reading.
- **MCP-first localization** (cycle-012). The `palace-codemap` MCP server is the **preferred localization path** for the Palace C++ tree: localize via `list_files` / `search_text` / `get_symbol_def` / `get_call_sites` / `list_dependencies` / `get_file_subtree`, then `read_range` for the actual source (the only source-returning codemap tool). The cycle-planner should verify file paths / symbol locations via the codemap before citing them in dispatch scopes (it has drifted on `linalg/*` paths). Vanilla `Grep`/`Read` remain available; apply judgment on which is faster.

## Reference repos (local clones, gitignored under `reference/`)

- `reference/palace/` — the C++ source being dissected.
- `reference/bunsen/` — the user's burn-overlay library. `reference/bunsen/crates/bunsen/src/kits/sims/` is the methodology reference (Conway, LBM).
- `reference/burn/` — the target tensor library.

## Bunsen methodology conventions (carried forward)

Visible in `reference/bunsen/crates/bunsen/src/kits/sims/`:

- **Pure tensor-in / tensor-out functions are the algebra.** State-bearing wrappers are *thin*.
- **Decompose into named algebraic pieces** in separate files.
- **Symbolic shape contracts at boundaries** — `[H, W, VY=3, VX=3]` with named axes.
- **Docstrings declare I/O sets explicitly** — `# Arguments` / `# Returns` blocks.
- **L1↔L2 equivalence tested concretely** when feasible.
- **Performance notes are inline `// Timing:` comments**, not abstractions.

## Problems channel — out-of-band concerns

`problems/` is the channel for any agent to raise concerns that exceed their own role's authority. **Relaxed bar (2026-05-26):**

- **(A) Out-of-role conflicts** — e.g., critic notices a producer-prompt-level pattern.
- **(B) Observed-but-not-in-focus drive-by observations** — phrasing pattern: "In reading the context for this work [...]; the following contradiction, duplication, miss-framing, etc in reference work was noticed."

Filing rate is self-tuned per `scaffolding/problems-sensitivity.md`; target ~1/15 cycles. Meta-phase recalibrates each cycle.

## Skills

Agent-invocable procedures under `skills/<name>/SKILL.md`. Any agent can propose via `scaffolding/skill-candidates.md`; meta-phase promotes with default-accept under low-bar policy. Promotion bar: pattern observed ≥2 cycles OR candidate sketch concrete enough to write as SKILL.md OR friction-ledger entry exists for the addressed pattern.

The current skill set is the `skills/<name>/` directory itself (each carries a `SKILL.md` with its own provenance); `skills/README.md` is the index + authoring policy. `scaffolding/skill-candidates.md` holds proposals. Do not maintain a duplicate enumeration here — `ls skills/` is the live list.

## Models

- **All agents** — `claude-opus-4-8` (user directive 2026-05-31: all models set to Opus 4.8). Subsumes the prior per-agent split; history in `METHODOLOGY-CHANGELOG.md`.

## Escalation triggers

Surface to the human immediately rather than working around — these signal architectural problems, not content problems:

- Critic rejects three consecutive reports on the same scope (prompt bug, not content).
- A specialized agent's input exceeds reasonable token budgets on one region (scope too coarse — cycle-planner needs to subdivide).
- Open-questions ledger grows monotonically over 20 cycles with zero closures (generating questions faster than answering).
- Two specialized agents produce contradictory claims about the same source range across consecutive cycles (source itself may be ambiguous).
- Friction-ledger pattern reaches recurrence ≥5 with status not yet `addressed` (meta-phase isn't catching it).
- Custom `.claude/agents/<name>.md` definitions don't resolve via `Agent(subagent_type=<name>, ...)` (architectural — affects every dispatch).

## Inputs the human supplies

Before invoking the loop:
- Anthropic API access (env or harness credentials).
- `reference/` checkouts of palace + bunsen + burn (already in place).

If anything is missing or ambiguous, stop and ask.
