---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T091500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-02T093000Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "Formalize assemble_frequency_operator at L1"

## Critique

### Checks run

**citation-validity — pass.** The D3 harvester reported it could not run `tools/citecheck/citecheck.py` (claimed `reference/palace/` absent). I independently re-verified every load-bearing anchor via `palace-codemap read_range` — the clone IS present and readable to the codemap (D3's tooling failure was a working-directory/transient issue, not a genuine absence; D1 also ran citecheck this cycle, consistent with that). All anchors verify precisely:
- `drivensolver.cpp:91-93` — `K = GetStiffnessMatrix<ComplexOperator>(DIAG_ONE)`, `C = GetDampingMatrix<...>(DIAG_ZERO)`, `M = GetMassMatrix<...>(DIAG_ZERO)`, assembled ONCE before the sweep (the comment at :89-90 confirms "Assemble … for the initial frequency … Compute everything at the first frequency step"). ✓
- `drivensolver.cpp:175` — `A2 = space_op.GetExtraSystemMatrix<ComplexOperator>(omega, Operator::DIAG_ZERO)` (ω-dependent operand). ✓
- `drivensolver.cpp:176-177` — `A = space_op.GetSystemMatrix(1.0+0.0i, 1i*omega, -omega*omega+0.0i, K.get(), C.get(), M.get(), A2.get())` spans EXACTLY :176-177; weights `{1, iω, −ω²}` confirmed literal. ✓
- `drivensolver.cpp:180` — `ksp.SetOperators(*A, *P)` (per-ω capture). ✓
- `spaceoperator.cpp:521-528` (`GetSystemMatrix`) — template opens :521, body `return BuildParSumOperator({a0, a1, a2, ScalarType{1}}, {K, C, M, A2})` at :527, closes :528. The `ScalarType{1}` literal for the A2 slot is the exact source basis for the "A2 carries literal coefficient 1" caveat. ✓
- `rap.cpp:764-767` — `BuildParSumOperator<N>` template signature. ✓
- `rap.cpp:769-771` — `MFEM_VERIFY(it != ops.end(), "…requires at least one valid ParOperator")` (the empty-combination guard / fold-seed law). ✓
- `rap.cpp:779-780` — `auto sum = make_unique<SumOperator>(Height, Width)` (zero-operator seed). ✓
- `rap.cpp:781-783` — `for (i) if (ops[i] && coeff[i] != 0) sum->AddOperator(ops[i]->LocalOperator(), coeff[i])`; the `coeff[i] != 0` prune is at :782 and the `AddOperator` accumulate at :783 — both pinpoint anchors confirmed exactly. ✓

The core structural claims are all source-true: `{K,C,M}` assembled once before the ω-loop, only scalar weights ω-vary, `A=(K+iωC−ω²M+A2)`, A2 carries coeff 1, zero-coeff term-drop is positively anchored. No drift found. (One minor non-load-bearing note recorded under Issues.)

**surface-or-evidence — pass.** This is a NEW firm L1 operator + NEW firm L1>L0 rotation + a surgical refinement (operand-category axis extension) on existing L2/L3 `linear_combination`. The new entries carry full positive-source evidence. The refinement to L2/L3 `linear_combination` modifies surface (adds a real variant-axis point + a frontmatter axis entry) AND is backed by the `BuildParSumOperator` witness — it is not a pure rotation_claim. Pass.

**rotation-quality / anti-mirror — pass.** This is the load-bearing check and it is handled correctly. `assemble_frequency_operator` is NOT a new mirrored fold: it is re-expressed THROUGH `linear_combination` at the operator-operand corner of a newly-extended operand-category variant axis (`tensor-operand | operator-operand`). The report explicitly disclaims a mirrored `operator_linear_combination` chapter (§"Through linear_combination", §"Relationship to linear_combination") and enacts replace-and-propagate per the 2026-06-01 anti-mirror discipline. The operand-category axis extension on L2/L3 is genuinely surgical — it adds one variant-axis point (operand monoid lifted tensor→operator) citing the `BuildParSumOperator` witness, WITHOUT re-deriving the fold or duplicating its laws (the laws "hold verbatim at this corner"). The L1>L0 rotation is a real mutation rotation (pure affine-operator-family value → imperative per-ω `SumOperator` assembly + per-ω `SetOperators` capture), not a 1:1 rename: it hides the eager `SumOperator` allocation, the fixed-basis hoist, and the accumulation-order residue. Pass.

**variant-axis-coverage — pass.** Three axes declared (operand-category, weight-schedule, operand-stationarity) and each combination is either covered or explicitly scoped. The element-type axis general to `linear_combination` is explicitly scoped-out to complex-only for this driven specialization (`<ComplexOperator>`-typed, anchored at :175), not hidden. The A2 ω-dependence is surfaced as the `parameter-dependent-operand` stationarity case rather than buried. No hidden branches.

**cross-reference-integrity — pass.** All referenced chapter files exist on disk: `L2/linear_combination.md`, `L3/linear_combination.md`, `L1/apply_linop.md`, `L1/fe_assemble.md`, `L4/solve_family.md`. The new L1>L0 theme links the new L1 op and vice-versa (bidirectional). The L2 edit's `old` text matches lines 255-262 exactly; the L3 frontmatter `variant_axes` block (lines 9-13) and §"Variant axes" point 2 (line 137) match the edit targets exactly. The dual-registration is present (L1 dep-map row + cohort bullet + L1-L0/index row + ×2 SUMMARY lines); both SUMMARY insert-after anchors (`eliminate_rhs` at :133, `floquet-correction-mutation-rotation` at :152) exist. The `transientsolver.cpp:33` reference backing the single-pipeline-by-design rationale verifies (`TimeOperator time_op(…, dJdt_coef)` baked in at construction). This is a NEW-firm report, so the firm-body-inside-fence guard applies: both `new:` blocks ENCLOSE the full `## Status` + Signature + Algebraic-laws + Evidence INSIDE the fence (verified by reading the proposed-changes blocks — `## Status` for both new files sits inside its fence). Fence parity is balanced. Pass.

**edge-label-fidelity — pass.** The L1>L0 theme is labelled `edge: L1>L0` and the prose narrates exactly the L1→L0 rewrite (pure affine-operator-family value on the left, imperative C++ assembly + per-ω capture on the right), forward per the high→low discipline. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is `firm` (firm-on-positive-structure). The content shape matches: every law is a syntactic operator-algebra identity on fully-specified positive source, the term-drop law is POSITIVELY anchored in the operator domain (`rap.cpp:782`, not merely inherited), and the no-dedicated-test non-gating is correctly invoked per the `apply_linop`/`fe_assemble` precedent (both of which exist on disk and carry the same firm-on-positive-structure escape). The two caveats are correctly stated as non-laws / scope-notes, NOT as unconfirmed laws: (a) "affine modulo A2" is recorded as a stated fact (A2 = ω-dependent operand carrying coeff 1; the −ω² M-weight makes it degree-≤2 not strictly affine — both stated honestly as the affine-as-a-whole non-law), and (b) single-pipeline-by-design is framed as a finding (permanent driven-only witness), not a deferred discharge debt. No firm/rough-in mis-classification.

**skill-uptake-survey — warning.** The report's shape implies two relevant skills whose invocation is not referenced. (i) `verify-citation-range` / the mechanical `tools/citecheck/` `--anchor`/`--scan` realization is the on-ramp for exactly the anchor-pinpoint verification at issue here; the report says citecheck "could not run" and substituted manual `read_range`, but did not attempt the codemap-cross-check sub-procedure the verify-citation-range skill prescribes for the brace-boundary-drift case, nor flag a `problems/` skill-friction note for the citecheck-on-this-checkout failure. (ii) `classify-variant-axis` is directly applicable to the new operand-category axis extension and is not referenced. Pure telemetry — non-blocking. (The citecheck failure is itself worth a repairer/finalize follow-up: re-run citecheck now that the clone is confirmed codemap-readable.)

### Issues found

1. **[citecheck-failure-misattribution; severity: low; CYCLE.md §Supporting evidence + §Open questions "citecheck unavailable"]** The report asserts `reference/palace/` is "gitignored and absent from the working tree" so citecheck returns `[MISS]`. I confirmed via `palace-codemap read_range` that the Palace source IS present and readable (every anchor resolved). D1 this cycle ran citecheck successfully. The failure was therefore a working-directory / transient issue in D3's checkout, not a genuine absence — the report's stated root cause is wrong. Consequence is cosmetic (all anchors independently verified correct), but the caveat should be corrected and citecheck re-run before integration. Candidate repair: re-run `python3 tools/citecheck/citecheck.py --scan` on the report and the anchor `--anchor` pinpoints; correct the §Supporting-evidence framing.

2. **[coeff-array-type subtlety, non-load-bearing; severity: info; CYCLE.md §Evidence rap.cpp:764-767 + spaceoperator.cpp:527]** The `BuildParSumOperator<N>` signature I read declares `const std::array<double, N> &coeff` (real doubles), yet `GetSystemMatrix` on the driven `<ComplexOperator>` path passes `{a0, a1, a2, ScalarType{1}}` with `a1 = 1i*omega` complex. There is presumably a complex-coeff overload / templated variant of `BuildParSumOperator` not at `rap.cpp:764-767` that the `<ComplexOperator>` path actually resolves to. The report cites the `double`-coeff template as THE primitive. This does not affect any structural/algebraic claim (the fold shape, coeff-1-for-A2, zero-prune, accumulation order are all faithful), but the cited :764-767 signature is the real-coeff instantiation, not the complex one the driven path uses. Optional: note the complex overload or widen the citation. Not blocking.

3. **[skill-invocation telemetry; severity: low; CYCLE.md throughout]** No reference to `verify-citation-range` (incl. the codemap-cross-check sub-procedure for the citecheck-unavailable case) or `classify-variant-axis`, both directly applicable. Surfaced as telemetry per the skill-uptake-survey check; not blocking.

**Anchor verification verdict: `reference/palace` anchors ALL verified OK via `palace-codemap read_range`.** Every load-bearing pinpoint (`drivensolver.cpp:91-93,175,176-177,180`, `spaceoperator.cpp:521-528`/:527, `rap.cpp:764-767,769-771,779-780,781-783` incl. the `coeff[i]!=0` prune at :782 and `AddOperator` at :783) sits on the asserted line and says what the report claims. The clone is present and codemap-readable; D3's citecheck failure was environmental, not a real absence.

---

## Repair

### Fixes attempted

- **Finding (Issue 1, citecheck-failure-misattribution; low):** The report claims `reference/palace/` is gitignored/absent so `tools/citecheck/citecheck.py` returns `[MISS]` — a false root-cause for an environmental/transient dispatch-checkout failure.
  - **Decision:** repaired.
  - **Action:** Re-ran `python3 tools/citecheck/citecheck.py --scan` on the report from the repo root — **30 ok, 0 failing, exit 0** (the clone IS present at `reference/palace/palace/...` and citecheck's path-resolution handles it; consistent with the critic's independent codemap re-verification and D1's successful citecheck this same cycle). Corrected the false framing in two places in CYCLE.md: §Supporting-evidence (replaced the "citecheck could not run / clone absent" preamble with the actual `30 ok, 0 failing` re-run result + an explicit repairer correction note) and §Open-questions "citecheck unavailable" bullet (rewrote to record citecheck runs clean, the codemap↔citecheck cross-check is now satisfied, no outstanding availability issue). Re-scan after edits: **33 ok, 0 failing** (the 3 newly-added citations from the Issue-2 note also resolve clean).

- **Finding (Issue 2, coeff-array-type subtlety; info):** The cited `BuildParSumOperator<N>` at `rap.cpp:764-767` declares `std::array<double,N>` coeff, but the driven `<ComplexOperator>` path passes complex `iω` — there is a complex overload not at that line.
  - **Decision:** repaired (trivially locatable, surgical one-line note — non-load-bearing).
  - **Action:** Located the complex overload via `palace-codemap search_text`: `BuildParSumOperator(const std::array<std::complex<double>, N>& coeff, …)` at `rap.cpp:833` (declared `rap.hpp:238`; explicit `std::complex<double>` instantiations `rap.cpp:971-977`). Added a one-line **Coeff-type note** to the L1 entry's Evidence list entry for `rap.cpp:764-767` in CYCLE.md, pointing at the complex overload and noting both overloads share the identical fold shape so every structural/algebraic claim holds verbatim. No claim changed — the cited `:764-767` (real-coeff) signature remains valid as the primitive's signature; the note disambiguates which instantiation the driven path resolves to.

- **Finding (Issue 3, skill-invocation telemetry; low; non-blocking):** No reference to `verify-citation-range` or `classify-variant-axis` by name.
  - **Decision:** not-needed (pure telemetry; the underlying procedures were performed — the anchor verification and variant-axis classification are present and correct, only the by-name skill citation is absent). The critic already logged it under skill-uptake-survey=warning; no surface defect to repair.

### Unrepairable findings

None. Both substantive findings (Issues 1 and 2) were mechanical/surgical and repaired in place; Issue 3 is telemetry-only.

## Suggested resolution

`ready`. The critic returned 7 pass + 1 warning (skill-uptake-survey, pure telemetry, non-blocking) and independently re-verified every load-bearing anchor via codemap. The two non-pass items the critic flagged for repairer follow-up (the false "clone absent / citecheck unavailable" provenance and the real-vs-complex coeff-overload disambiguation) are both fixed surgically without authoring substantive content. citecheck now runs clean on this report (33 ok, 0 failing). Integrator notes: nothing blocking; the report's own §Open-questions correctly defers (a) the consolidated firm-count tally to D2 (layer-intro-author count-owner this cycle) and (b) the `book/src/L4/solve_family.md` cross-reference refresh to name `assemble_frequency_operator` as the per-element operator (out of this one-operator dispatch's scope) — both are legitimate cross-dispatch deferrals, not repair items.
