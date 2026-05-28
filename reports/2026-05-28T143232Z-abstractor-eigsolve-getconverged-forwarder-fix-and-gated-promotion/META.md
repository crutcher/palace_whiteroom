---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T14:55:28Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: warning
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-05-28T151012Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: unrepairable
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: unrepairable
  skill-uptake-survey: not-needed
overall_status: needs-revision
follow_up_agent: null
---

# META: verification of "L1>L0 eigsolve-mutation-rotation — GetConverged forwarder fix + citation refinements + gated partly-constructive→firm promotion"

## Critique

### Checks run

**citation-validity — warning.** I re-read every source range the report touches via `mcp__palace-codemap__read_range` against `reference/palace`. The ARPACK refinements (the heart of the dispatch) verify cleanly: `SetWhichEigenpairs` body at `arpack.cpp:236-239` is the trivial `which_type = type;` field-set (confirmed); the per-`WhichType` switch is `switch (which_type)` at line 279 with body to the closing `}` at 305 (report's `279-305` ✓); the `MFEM_ABORT` is at 302-303 with `case TARGET_REAL/TARGET_IMAGINARY` at 300-301 and `break` at 304; the ncv-clamp triplet is exact (`N = linalg::GlobalSize(...)` at 517, `if (ncv > N){...}` 518-521, `arpack_it` default 522-525) — Change 4's `518-521` / `517` / `522-525` are all correct. The SLEPc asymmetry claim added in Change 2 (per-`WhichType` switch lives *inside* `SlepcEPSSolverBase::SetWhichEigenpairs` at `slepc.cpp:565-600`, unlike ARPACK) is confirmed (switch opens at line 567). The `iterative.hpp:98` `GetConverged()` definition is exact. **However**, the report introduces NEW off-by-2 drift on the very forwarder family it is correcting: the `BaseKspSolver` `ksp` member is at `ksp.hpp:41` (line 39 is `protected:`), not `ksp.hpp:39` as the applied NEW text states (CYCLE.md Change 1, "reachable only through the **protected** `ksp` member (`palace/linalg/ksp.hpp:39`)"); and the `GetRelTol` forwarder is at `ksp.hpp:64`, not `ksp.hpp:62` as the applied NEW text states (CYCLE.md Change 1, "mirroring the existing `GetRelTol` accessor (`palace/linalg/ksp.hpp:62`...)"). Both wrong citations land *in the artifact* (they are inside Change 1's NEW block, not just the report narration). Line 62 is `int NumTotalMultIterations()...`; line 39 is the `protected:` label. The public-surface range `ksp.hpp:50-71` is in-range (public: at 51, Mult decl at 71) and acceptable. Net: the dispatch fixes 3 citation drifts and introduces 2 new (smaller, same-region) ones — a warning because the dispatch's stated purpose is citation-drift elimination.

**surface-or-evidence — pass.** This is a refinement-shaped proposal against an existing firm theme. It modifies surface (the Sub-pattern B snippet, two citation lists, the Status section prose) AND is grounded in retroactive/forward evidence (the embedded cycle-012 lowering-verifier audit + fresh `read_range` this cycle). It is not a pure-rotation-claim-without-surface. Passes.

**rotation-quality — warning.** Not a new rotation claim (no L_{n+1} representation is made more compact). The check applies here only to the *status-promotion judgment*, which is the load-bearing structural claim of the dispatch. The promotion reasoning is well-argued and the audit's literal gate IS satisfied (Edit 2 applied this pass, not deferred — CYCLE.md §"Promotion judgment" + the embedded audit's gate at artifact lines 875-880). But there is a genuine unresolved interpretive tension (detailed in Issues #2): the constructive sub-part `LinearSolveFailed` STILL has only negative-anchor support after this pass (Palace's `void`-returning `Mult` is unchanged; the forward-looking note stays in prose), so the CLAUDE.md clause "Do NOT mark such an entry `firm` (the constructive sub-part isn't [firm])" is resolved only by the report's *interpretation* that "firm" means "no open promotion condition + structure confirmed." Warning — the interpretation should be ratified by integrator/meta-phase, not silently inherited.

**variant-axis-coverage — pass.** The variant axes (3 backends × 9 spectrum targets × 2 spectral transforms × 3 problem types) are already covered by the existing firm theme; this dispatch does not touch coverage. The ARPACK `(TARGET_REAL, TARGET_IMAGINARY)` stub branch is explicitly scoped out as a constructor-time validity constraint (unchanged). The forwarder snippet correctly presents both materialisation options (option-1 forwarder / option-2 `Mult` status-return) rather than hiding the alternative. Passes.

**cross-reference-integrity — pass.** All `[link]` targets in the touched regions resolve on disk (`L1-L0/ksp-solve-mutation-rotation.md`, `L1-L0/apply-linop-mutation-rotation.md`, `L1/eigsolve.md`, `L1/ksp_solve.md`, `L1/apply_linop.md`, `L1/dot.md`, `L1/nrm2.md`, `L1/axpy.md`, `L1/axpby.md`, `L0/eigensolver-wrapper.md`, `L0/mutable-workspace-pattern.md`, `L0/output-arg-vs-receiver.md` — all present). The self-reference to the report dir in Change 5d resolves. All five proposed-changes OLD strings exactly match the current artifact content at the cited line ranges (verified against the full file read), so the edits are mechanically applicable. Passes.

**edge-label-fidelity — pass.** The report carries the L1>L0 edge label throughout; the prose, snippets, and citations all discuss the L1→L0 lowering of `eigsolve` / Sub-pattern B. No edge-label/prose mismatch. Passes.

**plan-kind-consistency — warning.** The frontmatter declares `verdict: PROMOTED` and the content shape is a citation/snippet refinement that ALSO carries out a status-class transition (`partly-constructive`→`firm`). The refinement content is consistent with a firm-theme touch-up. The warning is on the status-transition half: an abstractor dispatch is enacting a methodology-gated status promotion that the CLAUDE.md invariant frames as needing the two-dispatch protocol — the audit (UNBLOCK) already ran cycle-012, and this is the ENACT pass, so the kind is *procedurally* correct, but the promotion folds an interpretive adjudication ("firm" = "no open promotion condition") into a producer dispatch. Flagging so the integrator treats the status flip as a deliberate decision, not a mechanical citation edit bundled with four others.

**skill-uptake-survey — warning (telemetry, non-blocking).** The dispatch's shape implies several relevant skills that go unreferenced: `verify-citation-range` (extended cycle-012 with an inherited-citation sub-case — directly applicable to validating the inherited audit citations and the corrected ranges), `verify-refinement-surface`, and `verify-rotation-citation`. The report documents extensive `read_range` verification but does not name any skill invocation. Pure telemetry surface, not blocking — but for the FIRST live test of the partly-constructive promotion mechanism, an explicit `verify-citation-range` audit-report sub-case invocation would have caught the ksp.hpp off-by-2 drift.

### Issues found

**Issue 1 (citation-validity, low severity) — off-by-2 drift introduced into the artifact on the `ksp.hpp` forwarder family.** Location: `book/src/L1-L0/eigsolve-mutation-rotation.md` via CYCLE.md Change 1 NEW block. Two wrong citations land in the applied artifact text: (a) the protected `ksp` member is cited as `palace/linalg/ksp.hpp:39` but is actually at line 41 (line 39 is the `protected:` label); (b) the `GetRelTol` forwarder is cited as `palace/linalg/ksp.hpp:62` but is actually at line 64 (line 62 is `int NumTotalMultIterations() const`). Both are in-region, same-class, off by 2. Ironic given the dispatch's stated purpose is citation-drift elimination. The public-surface range `ksp.hpp:50-71` is acceptable. Candidate fix: bump the two cites to `:41` and `:64`.

**Issue 2 (rotation-quality / plan-kind, MEDIUM severity — the dispatch's load-bearing claim) — the `partly-constructive`→`firm` promotion rests on an interpretation that resolves a real CLAUDE.md tension in the dispatch's own favor.** Location: CYCLE.md §"Promotion judgment" + Changes 5a–5d (`book/src/L1-L0/eigsolve-mutation-rotation.md` Status section). The factual state after this pass: `LinearSolveFailed` STILL has only negative-anchor support (`ksp.cpp:297-310` `void` return is unchanged); Palace does NOT positively produce the variant; the report explicitly keeps the forward-looking-reconstruction note in prose. So the CLAUDE.md invariant's motivating condition "(i) a constructive sub-part has only negative-anchor support" REMAINS TRUE; only condition "(ii) an open promotion condition remains" is argued closed. The invariant's literal clause is "Do NOT mark such an entry `firm` (the constructive sub-part isn't [firm])." The report dissolves this by reading "firm" as "no open promotion condition + structural decomposition confirmed" (CYCLE.md §"The apparent conflict resolves cleanly"). Additionally: the CLAUDE.md invariant enumerates the lowering-verifier promotion route as "a **per-line** lowering-verifier audit" (an evidence upgrade), whereas the theme's own `## Status` gate option (b) — the one actually invoked — is "a lowering-verifier audit that confirms the partly-constructive **shape is acceptable as a methodology-level pattern**" (a methodology-acceptance upgrade). These are not the same route; the cycle-012 audit did the latter (confirmed structure + identified firming edits + supported the meta-phase codification), not a per-line evidence upgrade of `LinearSolveFailed` to a positive site. The promotion IS defensible and the audit's literal gate (apply Edit 2, don't defer) IS satisfied — but the reading is an interpretive adjudication that, on the first live test of the mechanism, should be consciously ratified by integrator/meta-phase rather than silently baked in by a producer dispatch. Surface this as the key decision point.

**Issue 3 (low severity, historical-record hygiene) — embedded cycle-012 audit YAML still carries pre-fix `partially-supports` entries and the now-superseded ncv-clamp `518-520` phrasing without a resolution marker.** Location: `book/src/L1-L0/eigsolve-mutation-rotation.md` lines 808-811, 824-827, 860-863 (the embedded audit block, lines 762-881). The report (Open question #3) deliberately leaves the audit YAML untouched to avoid falsifying the historical record, which is reasonable, but the artifact will now contain (a) a firm-status Status section and (b) an embedded audit recording the `partially-supports` / gating state with no "resolved cycle-013" cross-link. A reader hitting the YAML first may be confused about whether the gate is open. Candidate (optional) fix: append a one-line `resolved cycle-013` note to the three affected YAML entries, or a single header line on the audit block. Not blocking.

**Issue 4 (low severity, citation-precision) — ARPACK abort citation `301-304` is marginally less precise than the superseded `300-304`.** Location: CYCLE.md Change 2 NEW + Change 3 NEW (`arpack.cpp:301-304` for the `MFEM_ABORT`). The abort statement spans 302-303; the logical abort block begins at `case WhichType::TARGET_REAL:` (line 300). The OLD artifact cited `300-304`; the NEW narrows to `301-304`, dropping the `TARGET_REAL` case line. Both are defensible as "the abort block," but `300-305` (case-open through switch-close) or `300-304` is the more faithful span. Cosmetic.

---

## Repair

### Fixes attempted

- **Finding (citation-validity / Issue 1)**: Change 1 NEW text introduced fresh off-by-2 drift on the `ksp.hpp` forwarder family — protected `ksp` member cited `ksp.hpp:39`, `GetRelTol` forwarder cited `ksp.hpp:62`.
  - **Decision**: repaired
  - **Action**: Verified exact lines via `mcp__palace-codemap__read_range` against `reference/palace`: line 41 = `std::unique_ptr<IterativeSolver<OperType>> ksp;` (line 38 = `protected:`, line 40 = the comment); line 64 = `double GetRelTol() const { return ksp->GetRelTol(); }` (line 63 = the comment). Bumped both cites `:39 → :41` and `:62 → :64` in all four occurrences across CYCLE.md: the artifact-landing Change 1 NEW block (`book/src/L1-L0/eigsolve-mutation-rotation.md` Sub-pattern B materialisation prose, both cites) and the three report-narration sites for internal consistency (§Summary Edit-2 bullet, §"Source verification" `ksp.hpp:28-72` bullet, §"Supporting evidence" `ksp.hpp:28-72` bullet). Note: the critic's stated truth-line for the `ksp` member was `:41`, which matches; the report's `:39` and the critic's incidental `:39 is the protected: label` framing both differ from the literal layout (`protected:` is line 38, comment line 40, member line 41) — the corrected citation `:41` is the verified-correct value.

- **Finding (surface-or-evidence / no issue)**: critic pass.
  - **Decision**: not-needed

- **Finding (rotation-quality / Issue 2)**: the `partly-constructive`→`firm` promotion rests on an interpretation that resolves a real CLAUDE.md tension (the "Do NOT mark such an entry `firm`" clause; per-line-audit route vs. methodology-acceptance route) in the dispatch's own favor; should be consciously ratified, not silently inherited.
  - **Decision**: unrepairable
  - **Rationale**: This is a methodology-judgment / content-adjudication finding, not a mechanical edit. Reverting the promotion or rewriting the §"Promotion judgment" reasoning would be substantive authoring and would pre-empt a decision the CLAUDE.md `partly-constructive`-is-first-class invariant explicitly reserves for the meta-phase (precedent named as exactly this theme's Sub-pattern B; promotion "should eventually close" via integrator/meta-phase ratification). Exceeds repair authority. Escalated (see Unrepairable findings).

- **Finding (variant-axis-coverage / no issue)**: critic pass.
  - **Decision**: not-needed

- **Finding (cross-reference-integrity / no issue)**: critic pass (all `[link]` targets + all five OLD strings verified by critic to match the artifact mechanically).
  - **Decision**: not-needed

- **Finding (edge-label-fidelity / no issue)**: critic pass.
  - **Decision**: not-needed

- **Finding (plan-kind-consistency / Issue 2 second face)**: an abstractor (producer) dispatch folds a methodology-gated status-class transition (`partly-constructive`→`firm`) and an interpretive adjudication into a citation/snippet refinement; the status flip should be treated as a deliberate decision, not a mechanical edit bundle.
  - **Decision**: unrepairable
  - **Rationale**: Same root as the rotation-quality finding — the kind is *procedurally* correct (this is the ENACT pass of the two-dispatch UNBLOCK→ENACT protocol), and the only remaining concern is conscious ratification of the status flip. That is a judgment for the integrator/meta-phase, not a mechanical repair. Not separable from Issue 2.

- **Finding (skill-uptake-survey / telemetry warning)**: dispatch did not name `verify-citation-range` (inherited-citation sub-case), `verify-refinement-surface`, or `verify-rotation-citation`.
  - **Decision**: not-needed
  - **Rationale**: Pure telemetry surface, explicitly non-blocking per the critic. The underlying gap it would have caught (the ksp.hpp off-by-2) is now repaired. No mechanical edit applies; back-filling a skill-invocation claim into the report would falsify the record.

- **Finding (Issue 3, historical-record hygiene — not a check-level finding)**: embedded cycle-012 audit YAML retains pre-fix `partially-supports` entries + the `518-520` ncv phrasing with no `resolved cycle-013` marker.
  - **Decision**: not-needed
  - **Rationale**: The report's Open Question #3 already documents this as a deliberate, defensible choice (not falsifying the historical audit record); the critic agreed it is "reasonable" and "not blocking." Optional hygiene, not a repair-authority item. An integrator may append a single `resolved cycle-013` cross-link header to the audit block if desired — flagged, not enacted.

- **Finding (Issue 4, citation-precision — cosmetic)**: ARPACK abort cited `301-304` vs the superseded `300-304`.
  - **Decision**: not-needed
  - **Rationale**: Verified lines 300=`case TARGET_REAL:`, 301=`case TARGET_IMAGINARY:`, 302-303=`MFEM_ABORT(...)`, 304=`break;`. The cited `301-304` is in-range and contains the full abort statement plus one case — defensible, not a clear off-by-N error. The critic itself calls both spans defensible and the issue cosmetic. Left as-cited (within repair-leave discretion); an integrator may widen to `300-304` if a more faithful span is preferred.

### Unrepairable findings

- **Issue 2 / rotation-quality + plan-kind-consistency (MEDIUM) — `partly-constructive`→`firm` promotion adjudication.** This is the **first live partly-constructive→firm promotion** of the mechanism the cycle-012 meta-phase codified, and the route actually invoked (theme `## Status` gate option-b: "lowering-verifier audit confirms the shape is acceptable as a methodology-level pattern") differs from the CLAUDE.md invariant's enumerated "per-line lowering-verifier audit" (evidence-upgrade) route. The constructive sub-part `LinearSolveFailed` still has only negative-anchor support after this pass (Palace's `void`-returning `Mult` at `ksp.cpp:297-310` is unchanged; the forward-looking-reconstruction note stays in prose), so the invariant's literal "Do NOT mark such an entry `firm` (the constructive sub-part isn't)" clause is dissolved only by the report's *interpretation* that "firm" scopes to "no open promotion condition + structural decomposition confirmed."
  - **Routing**: **Escalate to integrator-per-report + meta-phase for conscious ratification.** Do NOT revert the promotion and do NOT force a rewrite (the reading is defensible and the audit's literal gate — apply Edit 2 this pass, do not defer — IS satisfied). `follow_up_agent: null` — no producer re-dispatch is warranted; the decision belongs to the application/methodology phases, not another authoring pass. The integrator should apply the report with this status flip flagged as a deliberate decision (not a mechanical edit bundled with the four citation fixes); the cycle-013 meta-phase (or the next meta-batch boundary) should ratify or refine the "firm = no open promotion condition" reading and reconcile the two promotion routes (option-b methodology-acceptance vs. the invariant's per-line evidence-upgrade) so the precedent is consciously set rather than silently inherited.

## Suggested resolution

`needs-revision` — not because the report is wrong, but because its load-bearing claim (the first live partly-constructive→firm promotion) carries an interpretive adjudication that must be **consciously ratified by the integrator/meta-phase rather than silently inherited** from a producer dispatch.

For the integrator-per-report: the four citation fixes (Issue 1, now repaired) and the ARPACK refinements (Changes 2–4, critic-verified clean) are mechanically ready to apply. Apply Changes 5a–5d (the status flip) **as a flagged, deliberate decision** — surface it in STAGING.md as the first live exercise of the partly-constructive→firm mechanism, not as a routine citation touch-up. Optionally append a `resolved cycle-013` cross-link to the embedded cycle-012 audit block (Issue 3) so a reader hitting the YAML does not read the gate as still-open.

For the meta-phase (cycle-013 batch): ratify or refine the precedent — (i) the "firm = no open promotion condition + structural decomposition confirmed" reading of the invariant's "Do NOT mark firm" clause, and (ii) the reconciliation of the theme's `## Status` option-b (methodology-acceptance) route with the invariant's enumerated per-line-audit (evidence-upgrade) route. This is the precedent-setting decision for every future partly-constructive→firm promotion; it should be set on the record.
