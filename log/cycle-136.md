# cycle-136 — 2026-06-07 — batch-44 position 1/3 (the LEAD / OPENER): the `# Synthesis` Part is STOOD UP — the synthesized-library implementation view

**Batch-44 LEAD / OPENER / FIRST primary cycle** of meta-batch-44 (cycles 136/137/138). The batch-44 meta-phase fires AFTER cycle-138's finalize, aggregating 136/137/138 as a separate dispatch/commit. The cycle counter does NOT reset.

**Direction.** Batch-44 = **the SYNTHESIS section** (USER DIRECTIVE 2026-06-07; `project_synthesis_section_directive`) is the **LEAD**; the **wind-to-maintenance floor** (`project_batch44_direction_wind_to_maintenance`) is the steady-state surround. c136 stands up the new top-level `# Synthesis` Part — the spec's surface rendered **as a synthesized implementation library** in the L4 pseudo-language, placed immediately before `# Feature surfaces`. One wide multi-dispatch: Wave-1 shell + Wave-2 def bodies, merged the same cycle.

## What landed

**D1 (`layer-intro-author`, `synthesis-section-shell`) — the `# Synthesis` Part created.** `book/src/synthesis/index.md` (Part overview) + `synthesis/types.md` (the `types` library BODY — IoData / OpParams / SimState rendered) + 4 stub library shells (`iteration` / `data-algebra` / `coordination` / `drivers`) + the `SUMMARY.md` `# Synthesis — synthesized-library implementation view` Part inserted immediately before `# Feature surfaces`. All 6 chapters are `navigational-container` (reference-class edges ONLY; no `rank:`, no `depends-on`); implementation VIEW (links to the authoritative L4/semantics/concepts defs, does not restate). 5 OQs promoted.

**D2 (`abstractor`, `synthesis-iteration-library-defs`) — Wave-2 def-body merge onto the iteration shell.** `iterate_while` / `iterate_while_pure` / `iterate_while_with_prev`, krylov-step Form A + Form B (CG worked def), chebyshev setup/apply; + clustering types Krylov / StepOutputs / PrevCarry + utility API. Reference edges 7→15.

**D3 (`abstractor`, `synthesis-data-algebra-library-defs`) — Wave-2 def-body merge onto the data-algebra shell.** 13 firm op defs (`linear_combination` / `inner_product` / `dot` / `nrm2` / `fe_assemble` / `mk_matrix_free_operator` / `eliminate_bc` / `assemble_frequency_operator` / `gram_reduce` / `domain_energy_reduce` / `eigenfreq_qfactor_reduce` / `sparameter_reduce` / `waveguide_mode_reduce`) + 2 clustering-type+utility blocks + 1 `sharding-decompose-reduce` rank-0 `roadmap_goal` note. **DIRECTIVE-3 dual surface INTACT:** `#extern assemble_term` (the libCEED element-quadrature kernel-API, after its type sig) AND the inline `mk_matrix_free_operator` kernel-impl (the five-stage contraction chain). **DIRECTIVE-1 boundary held:** `sharding-decompose-reduce` stays a `roadmap_goal` note, MPI mechanism cited-not-lifted. Reference edges 18→20.

**D4 (`harvester`, `synthesis-coordination-library-defs`) — Wave-2 def-body merge onto the coordination shell.** `preconditioning-framework` / `ksp_solve` / `eigsolve` / `solve_family` / `frequency_sweep` / `fold_solve` + the coordination type block (Solve monad / Outcome / EigOutcome / EigState / StepReturn). **The EigState in-chapter type block RESOLVES the D1 OQ `record-EigState-needs-definition-home`** (single-consumer → in-chapter block, back-linked to its `EigResult` field-schema home). 2 `#extern` kernel-API callouts after their type sigs (`eigen_iterate` SLEPc / `time_step_op` MFEM ODESolver).

**D5 (`cross-layer-cross-cutter`, `maintenance-floor-c136`) — MAINTENANCE FLOOR clean-bill.** Audit-class (NO book mutation; OQ append only). The first per-BATCH-cadence sweep (batch-43-enacted). 1 forward-looking OQ promoted (`synthesis-edges-next-batch-maintenance-floor-audit`).

## Finalize normalization (consistency fix)

The three Wave-2 calculus libraries landed with **inconsistent `status:` tokens** — `iteration` → `status: navigational-container`, `data-algebra` → left at `status: stub`, `coordination` → `status: seed` — all the same chapter KIND (filled implementation-VIEW navigational-container). NORMALIZED all three to the **index/types reference convention: a filled VIEW library chapter carries NO `status:` field** (kind-only, no resolution claim, no `rank:`). `drivers` keeps `status: stub` (deferred shell, body not yet rendered). Mechanical frontmatter edit within build-repair authority; resolves OQ `synthesis-coordination-chapter-status-seed-token-reconciliation-c136`.

## Build + linters

- `cargo make book` (mdbook + linkcheck2): **Build Done EXIT 0** (`Build Done in 92.47 s`). **ZERO build-repairs.** All 6 synthesis chapters built to HTML (`book/book/html/synthesis/{index,types,iteration,data-algebra,coordination,drivers}.html`).
- **Step-5c KaTeX `$`-sigil collision assertion PASS:** `class="katex"` inside any `<pre>` block across ALL built HTML = **0**. (The named-shape-group `$`-sigils in the rendered def bodies are all inside ` ```text ` fences.)
- Only the pre-existing benign KaTeX/markdown-bracket "Potential incomplete link" WARNs in **untouched** files (`concepts/plane-rotation-stream.md` `[k+1]`/`[g]`, `concepts/step-outputs.md` `[j+1]`) — math-bracket false positives, NOT dangling-fragment errors, NOT in the new synthesis chapters.
- **Step-5b graded-stack linters (LANDED tree, authoritative; `--reference-reachable` tier active):** both block-conditions **PASS** — `rank_violations: 0` (baseline fully discharged → any violation would be NEW; held 0) + NO newly-orphaned node. The 6 new synthesis chapters classify as `expected_unreachable_outside_dag` (the correct navigational-container disposition — NOT in the rank DAG, **NOT detritus**); `synthesis/iteration` is additionally reference-reachable-inbound. **NO synthesis chapter appears in any detritus list.** Counts: `files=386→392 (+6), typed=325→331 (+6), untyped=61, roots=45, reachable=163, reference_reachable=247, rank_violations=0, unresolved=0, promotion_frontier=11→13, detritus=123 (HELD), true_detritus=51 (HELD), expected_unreachable_outside_dag=48→54 (+6)`. Trend: `rank_violations` …→0 (c134)→0 (c135)→0 (c136).

## Counts + process

- NO vocabulary firm-count FLIP (no status/rank flip on any existing node; the 6 new files are navigational-containers with no `rank:`). The 3 filled calculus libraries carry def BODIES but make no resolution claim (implementation VIEW). SLICE CORPUS: 0.
- 5 of 5 dispatched-ready reports applied clean (5/5 staging rows == dispatched-ready — **117th consecutive clean staging**); zero deferrals / rejections / per-report gate-hits.
- retroactive-budget global = 0; per-report gates all PASS/N/A; 0 implied-component stubs.
- OQ activity (per-report integrators): ~20 OQs promoted, incl. the EigState D1-OQ resolution (`record-EigState-schema-home-is-EigResult`).
- SESSION WAS RESTARTED before c136 per the batch-43 meta (5 agent-defs changed: `integrator-finalize` step-5c + `harvester`/`abstractor`/`lifter`/`layer-intro-author` `$`-sigil-fence bullets).
- The slice-era `cycle-136.md` was renamed to `cycle-136-slice-era.md` (c123–c135 precedent).
- `scaffolding/{roadmap,integrator-signals,cycle-record}` + `log/` committed atomically + the 5 consumed-report `integrated_at` touches; two-phase SHA-patch follows; NO `.claude/agents/` changes FROM THIS FINALIZE.

## The `# Synthesis` Part is STOOD UP

The synthesized-library implementation view landed: index + types + 3 filled calculus libraries (iteration / data-algebra / coordination) + drivers stub shell, SUMMARY-wired immediately before `# Feature surfaces`. **5 of 6 chapters have bodies; `drivers` body is deferred** to a later batch-44 cycle (lifts the 5 sim drivers + lifecycle ROOT + output products from the Feature spine, composing the calculus libraries). DIRECTIVE-3 dual-surface intact; DIRECTIVE-1 boundary held.

## Carry to c137/c138 + the batch-44 meta (fires after c138, aggregating 136/137/138)

**(1)** Fill the `drivers` library body — the deferred 6th chapter. **(2)** The per-operator synthesized-def rendering may deepen (abstractor/harvester own per-op renders per the directive; `lowering-verifier` may audit the rendered def correspondence to the L4 chapter bodies). **(3)** Maintenance floor is the steady-state surround on the per-batch sweep + per-cycle two-invariant tripwire cadence. The in-scope FEATURE-SURFACE SPINE remains L4-COMPLETE; the Synthesis section is the new substantive forward work.
