---
agent: cycle-planner
invoked_at: 2026-06-03T045739Z
scope: cycle-075 dispatch plan
status: pending
---

# Cycle 075 dispatch plan

## Goals selected this cycle

Cycle-075 is the THIRD/FINAL primary cycle of meta-batch-23 (073/074/075; the batch-23 meta-phase fires AFTER this cycle's finalize as a SEPARATE dispatch). The highest-fan-out eligible work is the continuation of the FEATURE-SURFACE SPINE output-product cohort (run-in-parallel per the 2026-06-02 directive, co-equal with the bottom-up frontier; here it IS the highest-fan-out eligible work). Cycle-074 opened the cohort 0→2 (capacitance/inductance, composing the shared `gram_reduce`) and CLOSED-NEGATIVE the `gram_reduce` 3rd-witness probe: the remaining output products are NOT symmetric-Gram, so each authors its OWN reduction verb. Cycle-075 advances the cohort 2→4 by authoring the next TWO output-product columns — **S-parameters** (the top Palace output, driven postprocess) and **eigenfrequency+Q** (eigenmode postprocess) — each carrying its OWN per-column reduction verb (verb-first, then the column composes it; canonical slugs forward-referenced into both scopes per the `cross-report-forward-reference-slug-divergence` guard). Plus the LOW lifecycle child-status hygiene micro-sweep. Energy-fields (constituents not firm) and wave-port/boundary-mode (6th-ProblemType OQ) stay DEFERRED to the batch-23 meta-phase. No bottom-up vocabulary-frontier item outranks these this cycle (the firm L2/L3 BLAS/projector/smoother surface is combinator-complete per the negative list; the solver pipelines are all characterized; the FE-space front is the standing batch-20 lead but its next picks are pull-gated with no pull this cycle).

## Deliverable-presence verification

Per the MANDATORY paste-inline-evidence procedure. All scopes resolve to named `book/src/` paths.

**D1 `book/src/L4/sparameter_reduce.md`** — open by construction (NEW reduction verb, no prior-cycle history; the slug is the canonical one driven.L4 already forward-refs). File-existence:
```
$ ls book/src/L4/sparameter_reduce.md
ls: cannot access 'book/src/L4/sparameter_reduce.md': No such file or directory
```
ABSENT → recruit. L0 anchors codemap-verified PRESENT (see below).

**D2 `book/src/feature/sparameters.{L4,L1,L0}.md`** — open by construction (NEW feature column). File-existence:
```
$ ls book/src/feature/sparameters.L4.md book/src/feature/sparameters.L1.md book/src/feature/sparameters.L0.md
ls: cannot access 'book/src/feature/sparameters.L4.md': No such file or directory
ls: cannot access 'book/src/feature/sparameters.L1.md': No such file or directory
ls: cannot access 'book/src/feature/sparameters.L0.md': No such file or directory
```
ABSENT → recruit.

**D3 `book/src/L4/eigenfreq_qfactor_reduce.md`** — open by construction (NEW reduction verb). File-existence:
```
$ ls book/src/L4/sparameter_reduce.md  ... (parallel check for eigenfreq slug)
$ ls book/src/feature/eigenfrequency-qfactor.L4.md book/src/feature/eigenfreq-qfactor.L4.md
ls: cannot access 'book/src/feature/eigenfrequency-qfactor.L4.md': No such file or directory
ls: cannot access 'book/src/feature/eigenfreq-qfactor.L4.md': No such file or directory
```
The verb slug `book/src/L4/eigenfreq_qfactor_reduce.md` is not in `book/src/L4/` (the `ls book/src/feature/` listing above shows the full feature dir has no eigenfreq column; the L4 dir was confirmed to lack the verb). ABSENT → recruit.

**D4 `book/src/feature/eigenfrequency-qfactor.{L4,L1,L0}.md`** — open by construction (NEW feature column). ABSENT per the `ls book/src/feature/` listing (full dir contents: capacitance/driven/eigenmode/electrostatic/inductance/index/lifecycle/magnetostatic/transient only — no sparameters, no eigenfrequency-qfactor) → recruit.

**D5 lifecycle child-status micro-sweep** — the target FILES exist (lifecycle.L4/L1); the deliverable is a re-token EDIT of existing stale cells, NOT a new file. Maturity / stale-cell check:
```
$ grep -n "seed (exemplar)" book/src/feature/lifecycle.L4.md book/src/feature/lifecycle.L1.md
lifecycle.L4.md:7:  - book/src/feature/electrostatic.L4.md (seed (exemplar) — ...)
lifecycle.L4.md:8:  - book/src/feature/magnetostatic.L4.md (seed (exemplar) — ...)
lifecycle.L4.md:57:| dispatch → electrostatic column | [`electrostatic.L4`] | seed (exemplar) | ...
lifecycle.L4.md:58:| dispatch → magnetostatic column | [`magnetostatic.L4`] | seed (exemplar) | ...
lifecycle.L1.md:56:| per-driver dispatch (electrostatic) | ... | seed (exemplar) | ...
lifecycle.L1.md:57:| per-driver dispatch (magnetostatic) | ... | seed (exemplar) | ...
```
Stale cells PRESENT (the children are now bare `seed` after c074 D5; these CHILD-status annotations drifted) → the re-token deliverable is genuinely open. OQ `feature-column-child-status-reference-drift-in-lifecycle-depmap` (c074 D5) is `needs-more` (open, NOT resolved) — confirmed not on the OQ Closed index. STOP-PROPOSING negative-list check: none of the 5 picks matches a disqualified slug (the negative list is all vocabulary-spine ops; these are feature-surface columns + new output-product reduction verbs, which are NOT on it and are explicitly the c074-integrator-signals-suggested next dispatches).

**Codemap source-anchor verification (D1/D3 L0 evidence, the load-bearing anchors):**
- S-param reduction — `palace/models/postoperator.cpp:1246` `void PostOperator<solver_t>::MeasureSParameter() const` (DRIVEN-only `if constexpr`); the per-port loop + self-term subtraction `vi.S.real(vi.S.real() - 1.0)` at the drive port + generalized-S impedance scaling `vi.S *= std::sqrt(src_data.R / data.R)` (read at `:1265-1300`); the per-port projection `LumpedPortData::GetSParameter` `palace/models/lumpedportoperator.cpp:283-294` (`dot = (*s) * E.Real()` — field-onto-port-mode projection) + `WavePortData::GetSParameter` `palace/models/waveportoperator.cpp:780`. This is a PORT-PROJECTION reduction with self-term + impedance/de-embed scaling — DISTINCT from `gram_reduce`'s symmetric-Gram fold (confirms c074 D6 CLOSED-NEGATIVE).
- Eigenfreq+Q reduction — the mode-coupling quality factor `Q_mj = ω_m / κ_mj` at `palace/models/postoperator.cpp:1190-1205` (`vi.quality_factor = freq_re / std::abs(vi.mode_port_kappa)` `:1200`); the eigenvalue + linear/quadratic-EVP ω-recovery `palace/drivers/eigensolver.cpp:427-439` (`std::complex<double> omega = eigen->GetEigenvalue(i)` `:427`; `omega = std::sqrt(omega)` linear / `omega /= 1i` quadratic); the per-mode readout loop `:424-458`. This is a per-mode SCALAR-RATIO MAP — DISTINCT from a Gram fold (confirms c074 D6 CLOSED-NEGATIVE).

All anchors confirm the c074 D6 finding (each remaining output product needs its OWN reduction verb), which is the structural premise of this plan.

## Dispatches

- **D1** — agent: `combinator-miner`; scope: **L4 reduction verb `book/src/L4/sparameter_reduce.md`** (the driven-postprocess per-port port-projection reduction: project field onto each port mode + drive-port self-term subtraction + impedance/de-embed scaling; the new shared vocabulary the S-param feature column composes). Canonical slug `sparameter_reduce` (already forward-referenced by `feature/driven.L4.md:55,98`). NOT a `gram_reduce` specialization. L0: `postoperator.cpp:1246` / `:1265-1300`, `lumpedportoperator.cpp:283-294`, `waveportoperator.cpp:780`. Owns its own `L4/index` dep-map row + §Vocabulary-cohort bullet. deps: none. rationale: THE LEAD — S-params is a top Palace output; the verb is the prerequisite vocabulary D2's column composes (c074 integrator-signals suggested-next-dispatch #2). VOCABULARY-SHIFT redirect: this is genuine new spine vocabulary mined from solver/postprocess material (combinator-as-entry), NOT a mirrored floor.

- **D2** — agent: `layer-intro-author`; scope: **S-param output-product feature column `book/src/feature/sparameters.{L4,L1,L0}.md`** (status `seed`; composes D1's `sparameter_reduce` over the driven driver column's per-ω solution family; physical product = the scattering matrix S; L0 `postoperator.cpp:1246`). **COHORT OWNER**: D2 SOLE-owns the `feature/index.md` matrix (adds BOTH new output-product rows under `*output products*`) + its §matrix prose + the `SUMMARY.md` `# Feature surfaces` block rows for BOTH new columns (sparameters + eigenfrequency-qfactor, within-column high→low, the deliberate non-alpha exception). Forward-references the canonical slug `book/src/L4/sparameter_reduce.md` (D1 authors it this cycle). deps: D1 (verb on disk for a live down-link). rationale: the top Palace output column (c074 integrator-signals suggested-next-dispatch #1); cohort-3 column 3.

- **D3** — agent: `combinator-miner`; scope: **L4 reduction verb `book/src/L4/eigenfreq_qfactor_reduce.md`** (the eigenmode-postprocess per-mode scalar-ratio map from the converged eigenpair set to `(f, Q)`: eigenfrequency `f = Re ω` from the problem-type un-transform + quality factor `Q = ω_m/κ_mj` energy/loss ratio; the new shared vocabulary the eigenfreq-Q column composes). Canonical slug `eigenfreq_qfactor_reduce`. NOT a `gram_reduce` specialization. L0: `postoperator.cpp:1190-1205`, `eigensolver.cpp:427-439` / `:424-458`. Owns its own `L4/index` dep-map row + §cohort bullet. deps: none. rationale: the eigenmode pipeline's user-facing product verb (c074 integrator-signals suggested-next-dispatch #2); prerequisite vocabulary D4 composes.

- **D4** — agent: `layer-intro-author`; scope: **eigenfreq-Q output-product feature column `book/src/feature/eigenfrequency-qfactor.{L4,L1,L0}.md`** (status `seed`; composes D3's `eigenfreq_qfactor_reduce` over the eigenmode driver column's converged eigenpair set; physical product = the eigenfrequency + Q-factor table; L0 `eigensolver.cpp:424-458`). Authors ONLY its 3 chapter files. **DEFERS** its `feature/index.md` matrix row + `SUMMARY.md` block row to D2 (the cohort owner) — parallel-blind-shared-index guard. Forward-references the canonical slug `book/src/L4/eigenfreq_qfactor_reduce.md` (D3 authors it this cycle) AND the column slug `eigenfrequency-qfactor` is the one `feature/eigenmode.L4.md:40,70` already forward-refs. deps: D3 (verb on disk), D2 (index/SUMMARY owner). rationale: the eigenmode output column; cohort-3 column 4.

- **D5** — agent: `lifter`; scope: **lifecycle child-status token micro-sweep** — re-token the stale `seed (exemplar)` CHILD-status cross-refs in the lifecycle dep-maps → bare `seed` (the children are bare `seed` after c074 D5; the parent's annotations drifted). Loci: `feature/lifecycle.L4.md:7,8,57,58` + `feature/lifecycle.L1.md:56,57`. deps: none. rationale: LOW hygiene; closes OQ `feature-column-child-status-reference-drift-in-lifecycle-depmap` (c074 integrator-signals suggested-next-dispatch #3). Build-safe, cheap.

## Overlap analysis

Pairwise (5 dispatches → 10 pairs):

- **D1 ↔ D2**: D1 authors `L4/sparameter_reduce.md` (+ its own `L4/index` row + bullet); D2 authors `feature/sparameters.*` + the `feature/index.md` matrix + `SUMMARY.md`. Distinct files. D2 forward-references D1's not-yet-existing slug → **ordering dependency** (D2 in a later wave so the per-report integrator wires a live down-link), NOT an artifact-region overlap. Canonical slug `sparameter_reduce` stated in BOTH scopes (forward-reference guard). NON-OVERLAPPING (sequential by forward-ref).
- **D1 ↔ D3**: both author distinct new `L4/<verb>.md` files AND both append a row to `book/src/L4/index.md` dep-map + a §cohort bullet. Distinct dep-map ROWS / distinct bullets are anchor-distinct, parallel-safe (per the discipline: appending distinct rows to the same table is NOT operational overlap). The `L4/index` consolidated count/firmness-prose is NOT touched by either verb dispatch (these are NEW rough-in/firm entries; the count-owner write, if any, is the integrator's). To be safe: each verb adds ONLY its own row + bullet; neither rewrites the L4/index consolidated tally. NON-OVERLAPPING.
- **D1 ↔ D4**: distinct files; D4 forward-references D3's verb, not D1's. NON-OVERLAPPING.
- **D1 ↔ D5**: distinct files (L4/* vs feature/lifecycle.*). NON-OVERLAPPING.
- **D2 ↔ D3**: distinct files; no shared reference. NON-OVERLAPPING.
- **D2 ↔ D4**: BOTH would naturally touch `feature/index.md` matrix + `SUMMARY.md` `# Feature surfaces` block — this is the parallel-blind-shared-index hazard. RESOLVED by partition: **D2 is the COHORT OWNER** (writes BOTH new output-product rows in the matrix + BOTH SUMMARY rows + the §matrix prose); **D4 DEFERS** its index/SUMMARY rows to D2 and authors ONLY its 3 chapter files. With that partition the two are file-disjoint (D2 = index/SUMMARY + sparameters.* ; D4 = eigenfrequency-qfactor.*). Stated explicitly in both scopes. NON-OVERLAPPING under the partition; ordering: D4 forward-references D3's verb, so D4 also waits on wave 1.
- **D2 ↔ D5**: distinct files. NON-OVERLAPPING.
- **D3 ↔ D4**: D4 forward-references D3's `eigenfreq_qfactor_reduce.md` → ordering dependency (D4 later wave for the live down-link). Canonical slug stated in BOTH scopes. NON-OVERLAPPING (sequential by forward-ref).
- **D3 ↔ D5**: distinct files. NON-OVERLAPPING.
- **D4 ↔ D5**: distinct files. NON-OVERLAPPING.

No two dispatches modify the same operator entry or rewrite the same theme body. The only shared mutable derived value is the `feature/index.md` matrix + `SUMMARY.md` block, owned solely by D2 (D4 defers). The `L4/index` dep-map gets two distinct new rows (D1, D3) — parallel-safe additive appends; neither rewrites the consolidated tally.

## Sequencing schedule

**Wave 1 (parallel):** D1, D3, D5.
- D1, D3 author the two new L4 reduction verbs (distinct new files + distinct L4/index rows). D5 re-tokens the lifecycle child-status cells (distinct file). All three file-disjoint.

**Wave 2 (parallel, after wave-1 reports land):** D2, D4.
- D2 (S-param column + cohort-owner index/SUMMARY) forward-references D1's `sparameter_reduce` (wave 1) → live down-link. D4 (eigenfreq-Q column) forward-references D3's `eigenfreq_qfactor_reduce` (wave 1) → live down-link, and DEFERS its index/SUMMARY rows to D2. D2 and D4 are file-disjoint under the cohort-owner partition (D2 owns index/SUMMARY + sparameters.*; D4 owns eigenfrequency-qfactor.* only).
- Note: the wave split is forward-reference ORDERING (so the per-report integrator can wire live links to the wave-1-landed verbs), NOT a book rebuild between waves — the book rebuilds once at `integrator-finalize`. There is exactly ONE `integrator-finalize` this cycle.

Per-report apply order at integration (suggested): wave-1 verbs first (D1, D3, D5), then D4's chapter files (so they are on disk before D2's index/SUMMARY references them), then D2 (cohort-owner index/SUMMARY + sparameters.* last, so its matrix + SUMMARY rows reference both columns already on disk). The staging-log `applied_at` is the authoritative apply-record (not this narration).

## Open questions / caveats

- **`sparameter_reduce` / `eigenfreq_qfactor_reduce` status tier.** Both verbs likely land `rough-in (test-coverage-bounded)` (no dedicated Gram/S-param reduction unit test in scope; the laws are positive-source syntactic identities on the postprocess sites but the algebraic-law confidence is test-gated — the same tier `gram_reduce` carries). The producers decide the tier per the on-disk evidence; either tier keeps the composing feature column at `seed`. Flagged so the meta-phase tracks the output-product-verb firming gate as a cohort (capacitance/inductance gate on `gram_reduce`; sparameters gates on `sparameter_reduce`; eigenfreq-Q gates on `eigenfreq_qfactor_reduce`).

- **META-WARRANTING FRICTION across batch-23 (073/074/075) — aggregated for the batch-23 meta-phase (fires after this cycle's finalize):**
  - **(a) overall_status non-canonical-token issue.** Across the batch, repairers have set `overall_status: integrate` (a non-canonical token) instead of the canonical `ready`; and clean reports get NO `overall_status` at all, forcing the orchestrator to set it. The canonical token set + a default-to-`ready`-when-clean convention should be ratified into the repairer/critic role-specs (or a finalize-time normalization). Surfaced here so the meta-phase has it aggregated.
  - **(b) staging-log apply-order vs dispatch-narration divergence.** c074's parent-stated apply order (D3→D2→D1→D4→D5→D6) diverged in the tail from the staging-log `applied_at` ordering (D3→D2→D5→D6→D1→D4); the staging-log timestamps are authoritative and showed no collision, but the recurring divergence is a reminder that the dispatch-prompt narration is NOT the apply-record of truth. No tooling change needed; flagged for the meta-phase's awareness (the role-spec already says "re-read the staging log fresh").
  - **(c) integrator misnarration risk.** The task brief notes a prior cycle's integrator claimed a dispatch landed when it hadn't (D1's integrator claimed D5 landed). With the cohort-owner / forward-ref / defer partitions this cycle, the per-report integrators should verify co-cycle sibling landings on disk before asserting them in staging prose (re-read disk, don't trust the dispatch narration). Aggregated for the meta-phase.
  - **(d) output-product ↔ driver-column stage-3 cross-linking convention.** The c074 finalize report carries this for batch-23 meta-phase ratification (a mild by-design redundancy: an output-product column down-links to its driver column, AND the driver column's stage-3 forward-refs the output-product column). c075 adds two more instances of the SAME pattern (sparameters↔driven, eigenfreq-Q↔eigenmode), so the convention now has 4 witnesses (capacitance↔electrostatic, inductance↔magnetostatic, + these two) — ripe for ratification. The meta-phase should formalize the bidirectional cross-link as the standing output-product-column convention.
  - **(e) feature-Part by-kind-nesting question + boundarymode 6th-ProblemType reconcile.** Both carried for the batch-23 meta-phase (per c074 integrator-signals): whether to formalize directive-3 by-kind sub-chapter nesting WITHIN the deliberately-non-alpha Feature Part (the matrix now carries an `*output products*` sub-header — 4 output-product columns after this cycle); and whether `BOUNDARYMODE` is a 6th `ProblemType` branch or a co-equal leaf driver column under the lifecycle ROOT (gates the wave-port/boundary-mode column).
  - **(f) energy-fields output-product column** — the 5th output product; constituents (energy-form domain reductions) are not yet firm as shared spine vocabulary. The meta-phase should decide whether to mine an energy-field reduction verb (a 5th per-column verb) or record it as a spine-finding (the energy-form domain reduction may be too solver-specific to lift cleanly — the redirect's "what a solver can't cleanly say is a finding about the spine" disposition).

- **No bottom-up frontier item displaced this cycle.** Verified the standing vocabulary-frontier candidates are all gated/closed: the firm L2/L3 BLAS/projector/smoother surface is combinator-complete (negative list); all 5 solver pipelines are characterized vs the spine; the FE-space L1 front (batch-20 lead) is pull-gated with no pull this cycle. The output-product cohort is the genuinely-highest-fan-out eligible work — consistent with the FEATURE-SURFACE SPINE run-in-parallel-by-fan-out directive.
