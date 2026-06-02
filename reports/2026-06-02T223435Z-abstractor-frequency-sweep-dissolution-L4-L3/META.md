---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T230000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-02T231500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of L4>L3 theme sketch — frequency-sweep-dissolution

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing L0 pinpoint was re-localized against `palace/drivers/drivensolver.cpp` via codemap `search_text` (the authoritative line-map). All nine flagged anchors verify exactly at the cited lines: `:80` `const auto &omega_sample = iodata.solver.driven.sample_f` (the SweepUniform block — distinct from the `:45` time-domain and `:234` SweepAdaptive copies, correctly disambiguated by the report); `:91`/`:92`/`:93` K/C/M; `:97` the comment "The operators are constructed for each frequency step and used to initialize the ksp" (cited as `:96-97` — `:96` is "// Set up the linear solver."; a 2-line range enclosing the quoted comment is in-bounds and acceptable, the quote text itself is solely on `:97`); `:98` `ComplexKspSolver ksp(...)`; `:168`-`:170` the `for (std::size_t omega_i = ...; omega_i < omega_sample.size(); omega_i++)` frequency loop; `:172` `auto omega = omega_sample[omega_i]`; `:174` `GetExtraSystemMatrix`; `:176` `auto A = space_op.GetSystemMatrix(...)` (the in-loop operator rebuild); `:180` `ksp.SetOperators(*A, *P)` (the in-loop re-binding); `:194` `space_op.GetExcitationVector(excitation_idx, omega, RHS)`; `:196` `ksp.Mult(RHS, E)`. The SweepAdaptive scope-boundary cite `:234`-context is correct (the second `omega_sample` definition at `:234`, its loop at `:443`/`:445`). No `verified_against:` fenced-YAML block is present (the §Verified-against section is prose), so the YAML round-trip sub-check is N/A.

**surface-or-evidence — pass (not applicable as a refinement).** This is a NEW firm L4>L3 theme creation (`edit:` block authoring `frequency-sweep-dissolution.md` from scratch), not a refinement of an existing operator/theme surface. It modifies surface (the full theme body + dep-map row + cohort bullet + SUMMARY line) AND carries direct positive-source rotation evidence (the `drivensolver.cpp` per-ω loop). No pure-rotation-claim-without-surface concern.

**rotation-quality — pass (the key check; the shift is genuine).** The lowering is a real vocabulary/semantic-organization shift, NOT a 1:1 named rename. L4: a single higher-order `map` combinator `frequency_sweep fam omegas = map (\w -> ksp_solve (assemble_frequency_operator fam w) (rhs_at fam w)) omegas` — the per-member operator-and-RHS function, an independent-family map with no cross-element carry, an order-preserving trajectory. L3: an explicit first-order sequential `for` over the frequency-sample list with the operator re-assembly (`GetSystemMatrix`) and solver re-binding (`SetOperators`) hand-placed INSIDE the loop body, the trajectory streamed as in-order per-ω post-processing over a re-used `E` vector. The L4 form is strictly more compact/abstract (one combinator naming the whole sweep; the operator-varying structure carried as `\w -> ... (A w) (b w)`); the L3 form materializes the higher-order application into an imperative sweep. This is state/combinator dissolution (map → for, per-member function → hand-placed in-loop construction), not a renaming. The operator-VARYING distinction is read directly off positive source and reinforced by Palace's own design comment.

**variant-axis-coverage — pass.** The operator-capture axis (`fixed | per-element`) is the distinguishing variant and is exhaustively handled: this theme is the `per-element` corner (driven), the `fixed` corner is scoped to the `solve-family-map-dissolution` sibling with explicit cross-references both directions. The schedule-source axis (`fixed-list | state-generated`) is covered: this theme is `fixed-list` (`omega_sample = iodata.solver.driven.sample_f`, `:80`); the `state-generated` SweepAdaptive/PROM sweep (`:234`-context) is explicitly scoped OUT to `fold-solve-time-step-dissolution`. The collection-shape sub-axis (re-used `E` streamed post-processing vs the sibling's pre-sized `std::vector`) is noted as a secondary realization detail. The `freq_restart_idx`/restart machinery (`:147-170`) is explicitly scoped out as orthogonal checkpoint logic. No hidden branches.

**cross-reference-integrity — pass.** The canonical forward-reference `frequency_sweep` matches D1's authored slug exactly: D1's dispatch (`reports/2026-06-02T223435Z-harvester-frequency-sweep-L4/CYCLE.md`) authors `edit:book/src/L4/frequency_sweep.md` (operator slug `frequency_sweep`) with the identical signature `frequency_sweep fam omegas = map (\w -> ksp_solve (assemble_frequency_operator fam w) (rhs_at fam w)) omegas` that D2 transcribed — no slug or signature divergence. The same-cycle dependency (the target file is not yet on disk at critique time) is correctly flagged as an OQ; the live link `../L4/frequency_sweep.md` resolves once D1's create lands before the single finalize build. All other named sibling targets exist on disk and verified: `solve_family.md`, `ksp_solve.md` (L4), `iterate-while.md`, `solve-family-map-dissolution.md`, `ksp-solve-driver-dissolution.md`, `fold-solve-time-step-dissolution.md`, `L3/ksp_solve.md`. Concept references (`state-stratification`, `variant-absorption`, `sequential-obstruction`) are the standard concept pages used across the cohort. The load-bearing fixed-operator contrast is reciprocally confirmed: the sibling `solve-family-map-dissolution.md` explicitly forward-references the driven `:176`/`:180` per-element superset as its own scope boundary (its §"does NOT cover" + §Applicability + §Verified-against L0 lines), so the two themes' contrast is mutually consistent.

**edge-label-fidelity — pass.** The edge label is L4→L3 throughout; the prose discusses exactly that edge (L4 `map` combinator → L3 explicit `for`). The reverse-lift note is correctly deferred to working notes / the cap's §"L4 vs L3 distinction" per the high→low discipline. The transitive delegations (per-member solve → `ksp-solve-driver-dissolution`, inner fold → `iterate-while-dissolution`) are correctly named as separate adjacent-edge themes composed below, not conflated into this edge.

**plan-kind-consistency — pass.** Declared kind is `firm` L4>L3 theme; content shape matches — a complete dissolution body (L4 form, L3 form, three coordinated rewrites, applicability conditions, justification kind, scope, L4-vs-L3 distinction) with no rough-in placeholders. The firm claim rests on direct positive-source reading of the rotation shape; no constructed/negative-anchor sub-parts that would force `partly-constructive`. Status reasoning is explicit and load-bearing-distinction-aware.

**skill-uptake-survey — pass.** The report references mechanical citation verification (`tools/citecheck/citecheck.py --anchor`) for the L0 anchors, consistent with the citation-validity skill realization. No other skill is strongly implied by this theme's shape. Pure telemetry; non-blocking.

### Build-readiness (fence guard)

The firm theme body is fully ENCLOSED inside the `edit:book/src/L4-L3/frequency-sweep-dissolution.md` fence (the `## Status`, signature/L4-form, the three rewrite sections, and the L4-vs-L3 distinction all sit between the opening ```` ```edit: ```` and its closing ```` ``` ````). Indented-code blocks (the L4/L3 pseudo-code) are used inside the fence rather than nested `text` fences, avoiding the cycle-019 fence-truncation defect. The three additional `edit:` blocks (`index.md` dep-map row, `index.md` cohort bullet, `SUMMARY.md` line) are each independently fenced and balanced. No firm-body-outside-fence concern.

### Issues found

No blocking issues. Minor / advisory observations (candidates for the repairer, none mechanical-error-level):

1. **Comment-quote line attribution — advisory, `book/src/L4-L3/frequency-sweep-dissolution.md` §"L3 form" + §Verified-against (`:96-97`).** The quoted comment "The operators are constructed for each frequency step..." is solely on `:97`; `:96` is "// Set up the linear solver." The 2-line range is in-bounds and harmless, but the pinpoint for the quote is strictly `:97`. Not a drift (the range encloses the anchor); flagged only for tightness.

2. **SUMMARY.md L4>L3 section is not currently alpha-sorted — advisory, integrator-facing.** The report emits the bare SUMMARY line and (in its OQ) correctly defers the alpha-insert anchor to the integrator. The existing SUMMARY L4-L3 block (`solve-family` → `fold-solve` → `fe-assemble`) is NOT alpha-ordered on disk, so the integrator cannot mechanically "insert after `fold-solve-time-step-dissolution`, before `gmres-...`" as the OQ suggests without first reconciling the section ordering against the alpha-within-kind-group directive. This is an integrator reconciliation note, not a report defect.

3. **Consolidated-tally deferral — advisory, index dep-map.** The report authored its own dep-map row + cohort bullet but deferred the consolidated-tally bump (on-disk reads "8 → 9 this cycle" from c068; should refresh to "9 → 10" for this c070 landing) to the integrator, citing no named L4>L3 count-owner this cycle. The deferral is consistent with the count-ownership partition; flagged so the integrator does not miss the tally refresh (the prior c068 row claims sole-D2-authorship of its tally, so the precedent supports D2 folding the bump — the integrator should resolve which).

## Repair

### Fixes attempted

- **Finding 1 — Comment-quote line attribution (`:96-97` → `:97`).**
  - **Decision**: repaired (citation-validity).
  - **Action**: tightened every quote-attribution of the `:97`-only comment ("The operators are constructed for each frequency step and used to initialize the ksp") from the 2-line range `:96-97` to the exact pinpoint `:97`. Edited `CYCLE.md` at the §"L3 form (RHS)" where-clause, the §"1. Per-member..." rewrite, the §"Justification kind" structural bullet, the §Status operator-varying paragraph, the dep-map row `edit:book/src/L4-L3/index.md` block, the §Verified-against L0 list (now annotates `:96` as the excluded "// Set up the linear solver." line), and the §"Supporting evidence" L0 list. Every occurrence is a quote-attribution of text that lives solely on `:97`, so the tightening is unambiguous and surface-preserving; `:96` is preceding context, not part of the quoted sentence.
  - **Rationale (judgment)**: the prose quotes ONLY the `:97` line in each occurrence (no place relies on `:96` as natural surrounding context), so per the finding's guidance the pinpoint tightens rather than `not-needed`. The remaining unchanged `:96-93` family-matrix and `:98` solver-object cites are unaffected (correct as-is).

- **Finding 2 — Consolidated-tally deferral.**
  - **Decision**: repaired (folded into cross-reference-integrity bucket — the index tally is the consolidated cross-reference state).
  - **Action**: added a full-paragraph replacement `edit:book/src/L4-L3/index.md` proposed-change to `CYCLE.md` that refreshes the on-disk c068 consolidated-tally paragraph ("firm L4>L3 themes: 8 → 9 this cycle"; 9 firm) to "firm L4>L3 themes: 9 → 10 this cycle" (10 firm), appending `frequency-sweep-dissolution` (cycle-070 D2) to the enumerated firm list and updating the coverage-summary sentence to name the operator-capture axis (fixed vs per-element) the c070 landing completes against the c055 fixed-operator sibling. Also corrected the trailing count-owner note to "D1 owns the distinct `L4/index.md` tally" (the report frontmatter + OQ confirm D1 firmed `L4/frequency_sweep.md` this cycle, so D1 — not the c068 paragraph's stale "D3" — owns the L4 tally). Updated the §Open-questions "Index count-ownership" caveat to record the repair and drop the deferral.
  - **Rationale**: the critic established D2 is the SOLE L4>L3-index toucher this cycle and the c068 precedent shows the index toucher folds its own tally; the on-disk paragraph body already counts 9 firm (the "8 → 9" wording was the prior cycle's bump), so this is a mechanical count refresh, not substantive authoring. Within repair authority (forgotten consolidated-tally entry with the count trivially derivable from the on-disk table).

- **Finding 3 — SUMMARY.md alpha-position / global re-sort.**
  - **Decision**: not-needed.
  - **Action**: none. Verified the local alpha placement is sane — `frequency-sweep-dissolution` lands after `fold-solve-time-step-dissolution` (`fo` < `fr`) and before `gmres-inner-loop-...`, exactly as the report's OQ states and the critic confirmed.
  - **Rationale**: the L4-L3 SUMMARY block is not yet globally alpha-sorted on disk; the global re-sort is the deferred directive-3 wave (an integrator/meta reconciliation), not a per-report repair. The local insert position is correct, so no report-level defect remains. Transitional-state-acceptable.

### Unrepairable findings

None. All three advisory findings were either repaired in-place (1, 2) or are correct-as-emitted transitional state for the integrator (3).

## Suggested resolution

`ready`. All 8 critic checks pass; the two repairable advisories (comment-quote tightening, consolidated-tally bump) are applied to `CYCLE.md`; the SUMMARY alpha-position is correct locally and defers globally to the directive-3 re-sort wave as intended.

Notes for the integrator:
- The new `edit:book/src/L4-L3/index.md` consolidated-tally block is a **full-paragraph replacement** of the existing §Vocabulary-cohort closing paragraph (the one currently reading "Consolidated tally (firm L4>L3 themes: 8 → 9 this cycle)..."). Apply it as a replace, not an append, to avoid a duplicate tally paragraph.
- The SUMMARY.md L4-L3 block is not globally alpha-sorted on disk; insert `frequency-sweep-dissolution` after `fold-solve-time-step-dissolution`, before `gmres-inner-loop-...` (local alpha), deferring the global re-sort to the directive-3 wave.
- Same-cycle dependency on D1's `book/src/L4/frequency_sweep.md` (the LHS live link) stands as the report's standing OQ — resolves once D1's create lands before the single finalize build.
