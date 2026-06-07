---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-07T233317Z
scope: L-stack maintenance-floor full-hygiene sweep — batch-44 BATCH-CLOSING (c138), now COVERING the full synthesis/ Part
status: integrated
integrated_at: 2026-06-07T235126Z
integration_commit: f1b69f1
integration_notes: "cycle-138 (batch-44 BATCH-CLOSING). MAINTENANCE FLOOR clean-bill, AUDIT-CLASS; NO book/scaffolding mutation. The once-per-batch full-hygiene sweep (batch-43-enacted cadence). Verified rank_violations==0, unresolved_depends_on_targets==0, all 6 synthesis chapters reference-class-only (0 blocking edges, correct GC = expected_unreachable_outside_dag), 3 realizes-kernel-api reference-class edges, 3 #extern boundaries, 0 $-sigil-fence leaks, DIRECTIVE-1 MPI boundary clean. DISCHARGES OQ synthesis-edges-next-batch-maintenance-floor-audit. No OQ append needed. No build relevance. retroactive-budget 0."
---

# CYCLE: Cross-layer observation — maintenance-floor batch-44 full-hygiene sweep (clean-bill; full synthesis/ coverage)

## Summary

The once-per-BATCH full-hygiene maintenance-floor sweep for meta-batch-44 (BATCH-CLOSING cycle c138), now covering the full **6-chapter `# Synthesis` Part** that landed substantively complete this batch (the c136 sweep deferred the `synthesis/` edge-audit; c137 D2 pre-empted only `iteration`/`data-algebra` def-bodies). **Clean-bill: every hard invariant holds, the synthesis edge-typing is `reference`-class throughout (0 `depends-on` blocking edges), the 6 synthesis chapters classify correctly as navigational-container `expected_unreachable_outside_dag` / reference-reachable — NONE in any detritus list, the `$`-sigil-fence compliance holds in all rendered def bodies, the `#extern` kernel boundaries point at the correct kernel-API nodes, the 3 `realizes-kernel-api` edges stay `reference`-class, DIRECTIVE-1 holds (no MPI node lifted), and the semantic surface carries no stale-path drift or restatement smell.** The graded-stack lint reports `files=392, typed=331, untyped=61, roots=45, rank_violations=0, unresolved_depends_on_targets=0, promotion_frontier=12, reachable=163, reference_reachable=247, detritus=123, true_detritus=51` — matching the c137 finalize baseline (`log/cycle-137.md:22`) exactly. Audit-class clean-bill; NO `book/` mutation.

## Observation kind

**Audit residue** (standing-hygiene clean-bill, full-`synthesis/`-coverage extension). No coverage gap, edge-label mismatch, consistency drift, or vocabulary/semantic-restatement mismatch surfaced.

## Specific finding

### (i) graded-stack lint totals + hard invariants — PASS (held vs c137 baseline)

`python3 tools/graded-stack-lint/graded_stack_lint.py --json --reference-reachable` reports the two per-cycle tripwire invariants **`rank_violations=0`, `unresolved_depends_on_targets=0`**, and the full totals `files=392, typed=331, untyped=61, roots=45, promotion_frontier=12, reachable=163, reference_reachable=247, detritus=123, detritus_no_typed_edges_pre_p1_artifact=104, true_detritus=51, expected_unreachable_outside_dag=54`, rank-histogram `firm=224, typed-no-rank=89, rough-in=4, partly-constructive=3, obstruction=2, partial-obstruction=4, roadmap_goal=4, stub=1`. This **matches the c137 finalize baseline** (`log/cycle-137.md:22`: `files=392, typed=331, reachable=163, reference_reachable=247, rank_violations=0, unresolved=0, detritus=123, true_detritus=51`) — no node maturity moved, no newly-orphaned node, the detritus-count escalate-guard does not fire (`detritus=123` HELD).

### (ii) FULL `synthesis/` Part coverage — PASS (the deferred edge-audit, now discharged)

**(a) Edge-typing: `reference`-class ONLY, 0 `depends-on` blocking edges.** All 6 chapters (`coordination` / `data-algebra` / `drivers` / `index` / `iteration` / `types`) carry an `edges:` frontmatter block with a `reference:` list and NO `depends-on:` block. Every literal `depends-on` token across `book/src/synthesis/` is in **prose/comment text explicitly asserting the absence of a blocking edge** ("adds no `depends-on` blocking edge", "constrains no firm node's rank/liveness") — never an actual `depends-on:` frontmatter edge. The implementation-VIEW invariant (Synthesis renders + LINKS, it does not depend-on for build/rank/liveness) holds.

**(b) GC classification: navigational-container, NOT detritus.** All 6 synthesis nodes appear in `expected_unreachable_outside_dag` (lint output lines 1074-1079) — the correct navigational-container disposition. `synthesis/data-algebra` is additionally in `promotion_frontier` (line 92; reference-reachable-inbound but its own rank unset — benign for a navigational container). `synthesis/iteration` appears as an INBOUND reference source in the `reference_reachable_inbound` trace for `L4/chebyshev` (line 693), `L4/iterate-while-with-prev` (line 697), and two more — i.e. it carries `reference`-class outbound edges TO those L4 chapters (the implementation-VIEW-links-to-L4 pattern, exactly correct). **NO synthesis node appears in `detritus`, `true_detritus`, or `stronger_signal_true_detritus`** (the `stronger_signal_true_detritus` list 487-495 contains zero synthesis nodes).

**(c) Frontmatter convention uniform.** All 6 chapters: `kind: navigational-container (...)`, NO `rank:`, NO `status:` field — the filled implementation-VIEW convention the c136/c137 finalize normalized the libraries to. No residual per-chapter status-token inconsistency observed (the OQ caveat the planner forward-flagged for the meta: the index matrix cells were normalized to `navigational (rendered)` at c137 finalize; the per-chapter frontmatter is now uniform `kind`-only — no `status: seed`/`status: stub` token remains in any synthesis frontmatter). Nothing to flag for the meta on this front.

**(d) `$`-sigil-fence compliance in rendered def bodies — PASS.** A fence-context scan (track ` ``` ` open/close, flag any `$[SN]` outside a fence) over the three def-body chapters reports **CLEAN for all three** (`data-algebra`, `coordination`, `iteration`): every `Tensor[$S]` / `LinOp[$S,$S]` / `$N` shape-group sigil sits inside a ` ```text ` fence. The `index.md` `$`-sigil mentions (lines 53-54) are inline-backtick prose in the rendering-convention docs, not code blocks — not `$`-sigil-fence-relevant. The integrator-finalize step-5c post-build assertion (no `<pre>` may contain `class="katex"`) backstops this; a source-level scan of any already-built `book/book/synthesis/*` pages returned no leak.

**(e) Semantic-restatement (link-don't-restate) — PASS.** The synthesis chapters consistently mark law-deferral: "Renders [`../L4/<op>.md`]" + "Authoritative semantics/laws live in the linked chapter" (e.g. `iteration.md` 15 `authoritative` markers, `coordination.md` 13, `data-algebra.md` 13 `Renders [` + 7 `authoritative`). The defs render the synthesized CODE form and LINK to the authoritative L4/`semantics/index.md`/`concepts/<record>.md` homes for the laws — they do not RE-STATE the semantics. No semantic-consolidation smell (no general rule/def restated at the synthesis functional-unit scope).

### (iii) kernel-API/impl integrity — PASS

The three `realizes-kernel-api` edges all sit under `reference:` blocks (navigational, free; separate `depends-on:` blocks carry the from-our-primitives constituents), confirmed on disk: `book/src/L1/multigrid-relaxation-smoother.md:24-26`, `book/src/L1/libceed-quadrature-kernel-impl.md:21-23`, `book/src/L3/eigsolve-impl.md:19-23` (the latter carries TWO — the L3 partial-obstruction kernel-api + the L4 cap sibling). The synthesis `#extern` kernel boundaries trace correctly to the kernel-API nodes:
- `synthesis/data-algebra.md:194` `#extern assemble_term` → the libCEED element-quadrature kernel-API (`L1-L0/fe-assemble-libceed-boundary-obstruction`, named at `:167,:191`).
- `synthesis/coordination.md:243` `#extern eigen_iterate` → the SLEPc EPS opaque loop kernel-API; `:254` names the `eigsolve-impl` constructive realization via the `realizes-kernel-api` correspondence.
- `synthesis/coordination.md:327` `#extern time_step_op` → the opaque MFEM `ODESolver::Step` per-step boundary (composed by reference from `synthesis/drivers.md:149,:355`, not re-rendered). DIRECTIVE-3 dual-surface intact.

### (iv) RE-set premise re-check — HELD

RE4 stays consumer-gated (no GMRES-variant feature column on disk; the named-consumer promotion condition unfired). The sharding `roadmap_goal` (`L4/sharding-decompose-reduce`) carries `rank: roadmap_goal` / `status: roadmap_goal` (confirmed `:4-5`) and remains a reference-emitting leaf under the §2g extension (batch-43 meta `ad9e2b2`). `roadmap_goal` bucket = 4 (held). The RE11 §2g escalate-guard does NOT fire (`detritus=123` held, no climb).

### (v) DIRECTIVE-1 boundary — HELD

No MPI/distributed version lifted. A grep for any `depends-on:` edge onto an MPI-associated node (`rap` / `geodata` / `communication` / `ParOperator` / `HypreParVector`) returns ZERO actual edges — all matches are PROSE in the `L4/sharding-decompose-reduce` row (`L4/index.md:121`) + the L4-L3 tally + methodology mirrors, each correctly stating the MPI mechanism is "cited NOT lifted" under `reference:` only. The sharding-MATH decomposition-abstraction is lifted ONLY (rank-0 roadmap_goal, `reference`-class edges to the 5 firm reduce roots); the MPI mechanism (`geodata.cpp`, `rap.{hpp,cpp}` `ParOperator`/RAP) stays deferred-mechanism-cited. The Dörfler cross-rank bisection stays deferred.

### (vi) semantic-surface liveness — PASS

`book/src/semantics/index.md` carries no stale path/anchor drift (grep for `design/l4_calculus|book/src/design|REPORT.md|spec/slices` returns 0). No degenerate identity-lowering smell or restated-semantics detritus surfaced this sweep.

## Recommendation

**Defer — clean-bill, no follow-up dispatch warranted.** This is the audit-class once-per-batch full-hygiene maintenance-floor sweep; all standing invariants hold, the full `synthesis/` Part is verified (`reference`-class edge-typing, navigational-container GC classification, `$`-sigil-fence compliance, `#extern`/kernel-API integrity, link-don't-restate), the disposition matches the c137 finalize baseline, and DIRECTIVE-1 holds. No `book/` mutation needed (no stale token surfaced). The batch-44 meta-phase inherits a fully-verified Synthesis surface; the remaining Synthesis items it owns (chapter-KIND role-spec codification, standing-duty surface liveness refresh) are correctly out of this closer's audit-only scope — none surfaced a defect.

## Supporting evidence

- `tools/graded-stack-lint/graded_stack_lint.py --json --reference-reachable` — `rank_violations=0`, `unresolved=0`; `files=392, typed=331, reachable=163, reference_reachable=247, detritus=123, true_detritus=51, promotion_frontier=12, roadmap_goal=4` — matches c137 finalize baseline (`log/cycle-137.md:22`).
- Lint classification lists: synthesis nodes in `expected_unreachable_outside_dag` (lines 1074-1079) + `promotion_frontier` (`synthesis/data-algebra`, line 92) + `reference_reachable_inbound` (`synthesis/iteration` as source for `L4/chebyshev`/`L4/iterate-while-with-prev`, lines 693/697); NONE in `detritus`/`true_detritus`/`stronger_signal_true_detritus`.
- `book/src/synthesis/{coordination,data-algebra,drivers,index,iteration,types}.md` frontmatter — `kind: navigational-container`, no `rank:`/`status:`, `edges.reference:` only, 0 `depends-on:` blocks.
- `$`-sigil fence-context scan over `synthesis/{data-algebra,coordination,iteration}.md` — CLEAN (all sigils inside ` ```text ` fences).
- `synthesis/data-algebra.md:194`, `synthesis/coordination.md:243,:327` — the three `#extern` boundaries → libCEED / SLEPc-EPS / ODESolver kernel-API nodes.
- `book/src/L1/multigrid-relaxation-smoother.md:24-26`, `book/src/L1/libceed-quadrature-kernel-impl.md:21-23`, `book/src/L3/eigsolve-impl.md:19-23` — the three `realizes-kernel-api` edges, all `reference`-class with separate `depends-on:` blocks.
- `book/src/L4/sharding-decompose-reduce.md:4-5` — `rank: roadmap_goal` / `status: roadmap_goal` held; `book/src/L4/index.md:121` — MPI mechanism "cited NOT lifted" under `reference:` only (DIRECTIVE-1).
- `book/src/semantics/index.md` — no stale path/anchor drift (grep returns 0).

## Open questions / caveats

- Clean-bill; no OQ append needed. The deferred `synthesis/` edge-audit OQ (`synthesis-edges-next-batch-maintenance-floor-audit`, opened c136) is **discharged by this sweep** — the full Part's edge-typing is now verified `reference`-class with 0 blocking edges and correct GC classification; the meta-phase / integrator may mark it resolved.
- This is the second per-BATCH-cadence full-hygiene sweep (batch-43 meta `ad9e2b2`): the full sweep is once-per-batch (this dispatch), the per-cycle floor is the `integrator-finalize` step-5b two-invariant tripwire. No dedicated maintenance-floor cross-cutter is dispatched every cycle.
- No baseline-exception ledger edit needed: `scaffolding/graded-stack-baseline-exceptions.md` remains the closed c094→c096 burn-down record with 0 tracked open exceptions.
