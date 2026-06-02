---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T01:29:30Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-02T01:42:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L4>L3 theme sketch — solve-family-map-dissolution"

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` reports 12 ok / 0 failing. I re-verified all 14 L0 anchors by hand against on-disk source. Electrostatic (`palace/drivers/electrostaticsolver.cpp`): `:30` `GetStiffnessMatrix`, `:35` `KspSolver ksp(...)`, `:36` `SetOperators(*K,*K)`, `:42` `MFEM_VERIFY(n_step>0)`, `:46` `std::vector<Vector> V(n_step)`, `:60` `for (const auto &[idx,data] : laplace_op.GetSources())`, `:68` `GetExcitationVector`, `:69` `ksp.Mult(RHS, V[step])`, `:89` `step++` — all exact. Magnetostatic (`magnetostaticsolver.cpp`): `:30`/`:35`/`:36`/`:42`/`:47` (`std::vector<Vector> A`)/`:66` (`GetSurfaceCurrentOp`)/`:76`/`:77`/`:99` — all exact. Driven scope-boundary (`drivensolver.cpp`): `:176` `GetSystemMatrix(...)` (operator rebuilt per-ω) and `:180` `SetOperators(*A,*P)` are both inside the frequency loop opened at `:168` (verified the brace structure), so the "hoist absent" negative-witness claim is correct. The L3 cross-citations also check: `L3/ksp_solve.md:38-54` is the Signature line, `:100-104` is the "Iteration-rotation marker" documenting the per-solve outer-loop sequential-obstruction the theme contrasts against. Zero drift. No `verified_against:` fenced YAML block is emitted (this is an abstractor report, not a lowering-verifier audit), so the round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is a `new:` theme entry (not a refinement of an existing operator/theme), carrying a full rotation_claim (the three-piece map-shell dissolution) backed by positive L0 witnesses. New-surface-with-rotation-evidence is the canonical pass shape; the pure-rotation-without-surface fail mode does not apply.

**rotation-quality — pass (load-bearing check, scrutinized).** The dissolution is a genuine vocabulary translation, NOT an identity-in-named-terms rename. L4 vocabulary (`map` higher-order combinator; `readonly` once-captured operator stratum; order-preserving trajectory `[SimState]`) → L3 vocabulary (first-order explicit positional `for` over the family-index set; hand-hoisted `KspSolver ksp(...)` + `SetOperators` construction; pre-sized mutable `std::vector<Vector>` indexed by a running `step++`). The L3 form is strictly more concrete/imperative: the higher-order `map` collapses to a first-order accumulating loop, and the type-level capture-once stratum demotes to a coding convention (construction placed outside the loop by hand, no L3 type enforcement). Rotation direction is correct (L4 more abstract → L3 lower). The load-bearing operator-capture-hoist is verified exactly against both witnesses: `SetOperators(*K,*K)` at `:36` sits outside the `for` at `:60` (electrostatic) / `:66` (magnetostatic), and the driven negative witness (`SetOperators` inside the freq loop at `:180`) correctly grounds why driven is the `per-element` superset, not `solve_family`. The redirect smell-check (degenerate identity = smell) is satisfied: this is not degenerate.

**variant-axis-coverage — pass.** The operator-capture axis (`fixed | per-element`) is the central scope decision and is handled explicitly: the theme covers fixed-operator only (electrostatic + magnetostatic, 2-of-5 pipelines), and the `per-element` superset (driven, operator rebuilt per-ω) is explicitly scoped out to a batch-17 theme in §"What this lowering does NOT cover", §Applicability conditions (condition 1/4), and §Status. The absorbed family-index axis and collection-shape axis are noted as absorbed into the loop range / pre-sizing. The empty-family degenerate (axis: non-empty Palace path vs calculus-level `[] -> []`) is covered in §Applicability condition 4. No hidden branch — transient/eigenmode are explicitly marked unprobed.

**cross-reference-integrity — warning.** All on-disk references resolve: the three sibling L4-L3 themes (`ksp-solve-driver-dissolution`, `iterate-while-dissolution`, `krylov-step-typed-wrapper-dissolution`), `L4/ksp_solve.md`, `L4/iterate-while.md`, `L3/ksp_solve.md`, and the three concept pages (`state-stratification`, `variant-absorption`, `sequential-obstruction`) all exist. The index.md row-append target (after the `ksp-solve-driver-dissolution` row at line 20) and the SUMMARY.md insertion point (after line 22) are both accurate, and the §Vocabulary-cohort section genuinely does not pre-exist (the report's "seed it" assumption holds). The **warning** is for one live link that does NOT resolve at critique time: `../L4/solve_family.md` (the LHS), referenced as a live link throughout the new chapter and the index row. This is the same-cycle D1 sibling — the report is explicit and correct that D1's `new:` create lands before the single finalize build, so the link resolves at integration. This is the standard same-cycle forward-reference pattern (and is the precedent shape used by every prior `<cap>` + `<cap>-dissolution` pairing this cycle stack). Not a defect in the report; flagged as a warning solely so the integrator confirms D1's create is applied before (or in) the same finalize build — if D1's report is rejected or deferred, every `solve_family.md` live link in this chapter becomes a hard `linkcheck2` build break.

**edge-label-fidelity — pass.** The declared edge is L4→L3 with LHS = L4 `solve_family` (the map-over-RHS-family combinator) and RHS = the L3 explicit positional accumulating outer loop. Every section discusses exactly that edge: §L4 form transcribes `solve_family op rhss = map (\inp -> ksp_solve op inp) rhss`; §L3 form renders the accumulating loop; the three numbered dissolutions each map one L4 map-shell piece to its L3 image. The rotation-direction note and §"L4 vs L3 distinction" both narrate forward L4→L3 consistently. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is `firm` L4>L3 theme; content shape matches. The firm apparatus (Status / Slug / L4-form / L3-form / Applicability-conditions / Justification-kind / Verified-against) is all present and substantive — no rough-in placeholders, no TODO stubs. The firm-on-structure justification (see Issue 1) is a genuine reasoning, not a mis-classification: the rotation shape is read directly off positive source, and the test-coverage gate is correctly localized to the upstream cap's independence *law* (a semantics property governing reorderability) rather than the dissolution *shape*. The status is `firm`, not `partly-constructive` or `rough-in`, and the content supports that.

**skill-uptake-survey — pass.** The report's shape implies the citation-range verification skill (`verify-citation-range` / the `tools/citecheck` realization); the report states all 14 anchors were self-verified exact via `sed -n` this dispatch and reports zero drift, which I independently confirmed. No rotation-proposal or variant-axis skill invocation is named, but the survey is a pure presence check (non-blocking); the citation-verification uptake is evidenced.

### Issues found

1. **Firm-on-structure status reasoning is sound but rests on a same-cycle LHS that is itself `rough-in (test-coverage-bounded)` — severity: low (informational, for repairer/integrator awareness, not a defect).** §Status and §Open-questions argue the theme is `firm` (not inheriting D1's `rough-in (test-coverage-bounded)` caveat) because the rotation *shape* (map shell → accumulating loop + operator-hoist) is a structural identity on positive source, independent of the cap's test-gated *independence law* (which governs family-map reorderability semantics, not the dissolution shape). I find this reasoning correct and well-supported: the `SetOperators`-outside-`for`, the pre-sized `std::vector<Vector>`, and the `step++` accumulator are all present in source, not reconstructed, so the dissolution holds even if a future test demoted the cap's independence law (the loop would simply remain non-reorderable, as the sequential `for` already is). The report itself flags the alternative (conservative inheritance → `rough-in`) and files OQ `solve-family-map-dissolution-firm-on-structure-vs-lhs-test-coverage` for the batch-17 verifier. No action required of the repairer; this is the kind of well-scoped status judgment the integrator should ratify as-is. Recorded so the integrator does not silently re-open it.

2. **`../L4/solve_family.md` live link is unresolved at critique time (same-cycle D1 dependency) — severity: low.** See cross-reference-integrity above. The report handles this correctly per the same-cycle-sibling convention; the only residual is the integration-ordering dependency on D1's create landing before the finalize build. Flag for integrator confirmation, not a report fix.

3. **`L3/solve_family` referenced in prose only (correctly plain-text, not a live link) — severity: none (confirming correct handling).** The report notes (§Open-questions) that the L3 `solve_family` entry and the L3>L2 hop are batch-17/pending and that it referenced `L3/solve_family` "only in prose context (not as a live link, since it does not yet exist on disk)." I confirmed there is no live `[L3/solve_family](...)` link in the proposed chapter — the per-member delegation links go to `../L3/ksp_solve.md` (which exists) and `./ksp-solve-driver-dissolution.md` (which exists). Correct application of the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention. No issue.

4. **Dual-registration / DEFERRED-tally partition is internally consistent — severity: none (confirming).** The report writes (1) its own anchor-distinct index.md table row, (2) its own §Vocabulary-cohort bullet (seeding the section since none pre-exists, which I confirmed), (3) its own SUMMARY.md entry, and explicitly DEFERS the consolidated firm-count tally / coverage-gap line / growth-log to D7 (the count-owner). The seed-vs-merge instruction to the integrator ("if D7 establishes the section structure, my bullet merges under its 'Substantive themes (firm)' sub-list") is clear. Fence parity is clean (8 fence lines = 4 balanced blocks; the new firm chapter body — `## Status: firm` through `## Verified-against` — sits entirely inside the `new:` fence at lines 26–224, with L4/L3 code rendered as 4-space-indented code, no nested triple-backtick fences, so the cycle-019 fence-truncation defect does not apply). No issue.

## Repair

### Fixes attempted

- **Finding**: cross-reference-integrity warning — `../L4/solve_family.md` live link (the LHS) does not resolve at critique time because `solve_family.md` is the same-cycle D1 sibling (D1 authors it this cycle).
  - **Decision**: not-needed
  - **Rationale**: This is not a report defect. The report handles the link correctly per the standard same-cycle-sibling forward-reference convention — D1's `new:` create lands before the single finalize build, so `../L4/solve_family.md` resolves at integration. The only residual is an integration-ordering dependency, which is the integrator's concern (apply D1 wave-1 before D2 wave-2), not a mechanical edit to the report. No surgical fix exists or is warranted; rewriting the live link to plain-text would be wrong (the target lands this cycle, and the same-cycle convention prefers the live link). Recorded as an integrator note below.

The remaining seven checks are `pass` (citation-validity, surface-or-evidence, rotation-quality, variant-axis-coverage, edge-label-fidelity, plan-kind-consistency, skill-uptake-survey). The critic's Issues 1/3/4 are explicitly confirmations / informational awareness items requiring no repairer action. No `repaired` or `unrepairable` findings.

### Unrepairable findings

None. The single warning is convention-correct and routed to the integrator as an ordering note, not deferred for substantive rework.

## Suggested resolution

`overall_status: ready`. No follow-up agent (`follow_up_agent: null`).

Integrator notes:

1. **Apply D1 before D2 (wave order: D1 wave-1, D2 wave-2).** D2's `../L4/solve_family.md` live links (chapter body + index row) only resolve once D1's `new:book/src/L4/solve_family.md` create has landed. If D1 is rejected/deferred, every `solve_family.md` live link in this chapter becomes a hard `linkcheck2` break — confirm D1's create is in the same finalize build before rebuilding.
2. **D2 proposed-changes** = `new:book/src/L4-L3/solve-family-map-dissolution.md` (firm) + its own `L4-L3/index.md` row (anchor-distinct, after the `ksp-solve-driver-dissolution` row at line 20) + its own §Vocabulary-cohort bullet (D2 seeds no consolidated tally; D7 owns the section header + consolidated firm-count/coverage-gap tally — merge D2's bullet under D7's "Substantive themes (firm)" sub-list if D7 establishes the section structure) + its own `SUMMARY.md` line (after line 22).
3. **`L3/solve_family` is correctly plain-text** (not on disk; batch-17/pending) — do not upgrade to a live link.
4. **Firm-on-structure status (Issue 1) is a sound, well-scoped judgment** — ratify as-is; do not silently re-open. OQ `solve-family-map-dissolution-firm-on-structure-vs-lhs-test-coverage` is filed for the batch-17 verifier.
