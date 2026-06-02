---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T07:05:00Z
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
repaired_at: 2026-06-02T07:30:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Cross-layer observation — eigenmode pipeline OUTER machinery is spine-complete"

## Critique

### Checks run

**citation-validity — pass.** All load-bearing L0 anchors codemap-verified against on-disk `reference/palace/`. `eigensolver.cpp:367` is exactly `int num_conv = eigen->Solve();` (confirmed single call; the only other `Solve()` is the HYBRID `:404`). `:377-406` is the HYBRID `QuasiNewtonSolver` block, constructed via `std::move(eigen)` + `num_conv` seed (`:379-381`) and re-`Solve()`d (`:404`) — verbatim. The post-processing loop is `for (int i = 0; i < num_conv; i++)` at `:424`, body `:425-471` (report's `:425-471` range is correct; the `for` keyword is at `:424`, a harmless off-by-one on the loop-header line that does not affect the body range cited). Inside: `GetEigenvalue(i)` `:427`, ω-map `:436`/`:441`, `GetEigenvector(i)` + `NormalizePhase` `:445`, `Curl.Mult` `:447-448` + `B *= -1/(iω)` `:450`, `MeasureAndPrintAll` `:458` — all confirmed. `vector.hpp:298-303` `NormalizePhase` confirmed (`x *= conj(mean)/abs(mean)`). `errorindicator.cpp:11-47` `AddIndicator` confirmed — the RMS running-average reduction with the in-source comment formula `eₖ = √(1/N ∑ₙ ηₖₙ²)` matching the report's transcription exactly. Artifact-side: map-witness signature `solve_family.md:40-41` (`map (\inp -> ksp_solve op inp)`) and fold-shell `fold_solve.md:20,27` both confirmed. The §Status "eigenmode … unprobed" item is at `solve_family.md:146` (report cites `:146` — correct). Two minor non-load-bearing precision notes recorded as issues below (the `:137` map-combinator cite and the "paragraph currently ends" framing). The verdict's three structural claims (one opaque solve; no operator/RHS family; post-loop is a readout map not a solve loop) are all directly supported by the read ranges.

**surface-or-evidence — pass.** This is an observation-kind report (coverage-gap / spine-coverage finding), not a refinement of an existing operator/theme — so the refinement-surface gate largely no-ops. The lone surface touch is the small `solve_family.md` §Status scope-note. The SPINE-COMPLETE verdict is evidence-backed: every one of the four dispositioned regions is tied to a specific source range, and the "neither a `solve_family` map witness nor a `fold_solve` fold witness" classification is grounded in the actual map/fold combinator signatures (`solve_family.md:40-41`, `fold_solve.md:20,27`) — the report shows the eigenmode driver instantiates neither shape (one opaque `Solve()`, readout-only loop). The negative result is properly framed as a spine-coverage finding, which is the legitimate observation-report shape.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted; the report explicitly records spine-complete with no new vocabulary and no L_{n+1}→L_n rewrite. Check no-ops on observation-kind content.

**variant-axis-coverage — pass.** No new operator/theme with variant axes is proposed. The report does, in effect, enumerate the eigenmode driver's structural regions (setup/cap/HYBRID/readout) and disposition each, which is the analogous coverage discipline for a probe — no region is left as a hidden branch (HYBRID two-phase and the readout loop are both explicitly classified, not silently dropped).

**cross-reference-integrity — pass.** Referenced slugs all resolve: `book/src/L4/eigsolve.md`, `book/src/L3/eigsolve.md`, `book/src/L4/solve_family.md`, `book/src/L4/fold_solve.md`, and `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md` all exist on disk. The proposed §Status replacement text adds two live links (`./fold_solve.md`, and a `reports/...` plain-text path) — `fold_solve.md` resolves; the report path is the report's own dir. No firm-body-inside-fence concern (the proposed change is a one-paragraph scope-note edit, not a firm chapter body).

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried; the report sits *above* the already-firm eigsolve chain and discusses cross-pipeline combinator-witness classification, not a specific lowering edge.

**plan-kind-consistency — pass.** Declared as an observation (coverage gap resolved-as-no-gap). Content matches: a probe that records a negative/spine-complete result, with one surgical scope-note. The single proposed-changes block does not convert this into a "firm operator" or other mismatched kind — it is a documentation touch consistent with the observation framing (see scope-expansion adjudication in Issues).

**skill-uptake-survey — pass.** The `disciplined-cross-pipeline-combinator-mining-gate` skill is cited by name (Observation kind §, the Combinator-witness classification block, Supporting evidence) and applied: step 1 (witness count — eigenmode is single-/zero-witness, recorded as spine-coverage finding not mined), step 2 (scope-boundary vs break-witness — explicitly distinguishes "does not exhibit the shape" from "breaks the invariant," correctly classing eigenmode as out-of-domain), step 3 (map-vs-fold over-unification flag — checks both the `solve_family` map and the `fold_solve` fold and rejects both). Citation present + the gate's points addressed → pass.

### Issues found

1. **Minor citation imprecision — `solve_family.md:137` cited as "the map combinator + the §Status item"** (CYCLE.md §Supporting evidence, line 80). Line 137 is actually variant-axis-1 (`operator-capture`), not the map-combinator definition. The map combinator is named at `solve_family.md:33` and its signature is at `:40-41`; the §Status "eigenmode unprobed" item is at `:146` (cited correctly elsewhere, line 46/59). Severity: low. The `:146` citation that the proposed edit depends on is correct; only the secondary `:137` evidence-list pinpoint drifts.

2. **"Paragraph currently ends" framing is inaccurate** (CYCLE.md §Proposed changes, lines 53-55). The report says the §Status paragraph "currently ends: … two fixed-operator witnesses." It does not — the actual paragraph (`solve_family.md:146`) continues past that clause with "The general superset is **batch-17 future work** (OQ …)…". The clause to be replaced ("**transient** and **eigenmode** are unprobed") is mid-paragraph, not at the end. The *quoted clause text itself matches the source exactly*, so the replacement target is unambiguously locatable, but the "currently ends" description could mislead an integrator into expecting a paragraph-terminal edit. Severity: low (repair = reword the edit instruction to "the clause within the §Status 'Scope (load-bearing)' paragraph reads … replace with …").

3. **Loop-header off-by-one (informational, not a defect).** The post-processing loop body is correctly cited `:425-471`; the `for (int i = 0; i < num_conv; i++)` header is at `:424`. The report attributes the loop to "`:425-471`" which is the body range — accurate for the body, one line short of including the header. No correction needed; noted for completeness.

4. **Scope-expansion adjudication: the proposed `solve_family.md` §Status edit is acceptable, not an overstep.** The report was dispatched observation-first, but the single surgical scope-note (i) writes the probe's negative result *exactly where the open item it closes already lives* (the `solve_family.md:146` "eigenmode unprobed" clause), (ii) is fully citation-grounded (`eigensolver.cpp:367` single solve; `:425-471` readout loop — both verified), (iii) is consistent with the probe finding (NOT a witness of either combinator), and (iv) is correctly handed to `integrator-per-report` with the producer NOT touching `book/` (write-authority partition honored). This is the legitimate "close the open item where it lives" move, not substantive authoring — it adds no new operator/theme and asserts no new vocabulary. No finding against the scope expansion. The report even self-flags the stale-by-batch risk (the transient half of the clause, since `fold_solve` has landed transient) and offers the trim — a reasonable note for the integrator. The repairer may optionally tighten the edit instruction per issues 1-2, but the edit content is sound.

## Repair

### Fixes attempted

- **Finding (critic issue 1)**: `solve_family.md:137` cited as "the map combinator" in the §Supporting evidence pinpoint — but `:137` is variant-axis-1 (`operator-capture`); the map combinator is named at `:33` and its signature is at `:40-41`; the §Status "eigenmode unprobed" item is at `:146`.
  - **Decision**: repaired.
  - **Action**: CYCLE.md §Supporting evidence — rewrote the `solve_family.md:137,146` evidence pinpoint to `:33,40-41` (map combinator: named `:33`, signature `:40-41`) `+ :146` (the §Status item), with an explicit note that `:137` is variant-axis-1 `operator-capture`. Also corrected the same `:40-41, 137` cite in the §Combinator-witness-classification "`solve_family` (map) witness? NO" bullet to attribute `:40-41` to the map-combinator signature and `:137` to the `operator-capture = fixed` load-bearing axis (not the combinator). Verified against `book/src/L4/solve_family.md` on disk: `:33` is the prose naming the combinator, `:40-41` is `solve_family op rhss = map (\inp -> ksp_solve op inp) rhss`, `:137` is variant-axis-1, `:146` is the §Status "Scope (load-bearing)" paragraph carrying the eigenmode-unprobed clause.

- **Finding (critic issue 2)**: the proposed §Status edit's framing "the 'Scope (load-bearing)' paragraph currently ends: … two fixed-operator witnesses" is inaccurate — the target clause "**transient** and **eigenmode** are unprobed" is mid-paragraph (the paragraph at `:146` continues with the "Do NOT claim…" and "batch-17 future work" sentences), not paragraph-terminal.
  - **Decision**: repaired.
  - **Action**: CYCLE.md §Proposed changes — reworded the edit instruction from "the paragraph currently ends: …" to "contains, mid-paragraph, the clause: …", added a parenthetical noting the paragraph continues past the clause and that this is an in-place clause replacement (not a paragraph-terminal append), and pinned the §Status paragraph at `solve_family.md:146`. The `[old]` clause text quoted for replacement is unchanged and still matches the source exactly, so the edit remains unambiguously locatable; only the framing wording was corrected so the integrator applies it as an in-place mid-paragraph replacement.

Both repairs are surgical edits to the report's evidence/proposed-changes wording — no substantive authoring, no change to the SPINE-COMPLETE verdict or the scope-note edit's substance (critic-confirmed sound). Critic issue 3 (loop-header off-by-one) was explicitly recorded by the critic as informational / no-correction-needed; issue 4 (scope-expansion adjudication) was a no-finding affirmation. Neither requires repair.

### Unrepairable findings

None. All critic issues were either mechanically repairable (issues 1, 2 — done) or informational/no-finding (issues 3, 4).

## Suggested resolution

`ready`. All 8 checks pass; the two low-severity precision issues are repaired in place. Integrator notes: (i) the proposed §Status edit is an **in-place mid-paragraph clause replacement** at `solve_family.md:146` — replace only the exact clause "**transient** and **eigenmode** are unprobed", leaving the rest of the "Scope (load-bearing)" paragraph (the "Do NOT claim…" + "batch-17 future work" sentences) intact; (ii) the report self-flags a reasonable stale-by-batch trim option (the transient half of the clause, since `fold_solve` now homes transient) — integrator size-judgment, the load-bearing addition is the eigenmode no-witness record.
