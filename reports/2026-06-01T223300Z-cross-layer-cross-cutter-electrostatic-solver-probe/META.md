---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T234500Z
critic_version: 1
repaired_at: 2026-06-01T235900Z
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
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
---

# META: verification of cross-layer-cross-cutter electrostatic-solver-probe (D6)

## Critique

### Checks run

**citation-validity — warning.** Every claim carries a pointer, and all load-bearing
citations resolve to the right construct — but there is a consistent ~1-3 line forward
drift in the inner-loop pinpoints. Verified against Palace source via codemap `read_range` /
`search_text`:
- per-terminal RHS build `GetExcitationVector(idx,*K,V[step],RHS)`: report says `:69`,
  actual **line 68** (`[DRIFT +1]`).
- inner solve `ksp.Mult(RHS, V[step])`: report says `:70`, actual **line 69** (`[DRIFT +1]`) —
  this is the load-bearing "CLEAN → `ksp_solve`" claim; the mapping is honest, the line is off by one.
- field recovery `E = -∇V` (`E=0.0; Grad.AddMult(V[step],E,-1.0)`): report says `:76-77`,
  actual `E = 0.0;` at **line 78**, `Grad.AddMult` at **line 79** (`[DRIFT +2/+3]`).
- the `Norml2` postprocess print: report says `:71-72`, actual **lines 73-75** (`[DRIFT +2]`).
- capacitance kernel `Dot(V_gf, M_elec·V_gf)`: report says `:118-126`; actual `M_elec->Mult`
  at line 118, diagonal `Dot` at **119**, off-diagonal `Dot` at **126** — the `:118-126`
  bracket **contains** all three; this pinpoint is correct.
- outer terminal loop `for (const auto &[idx,data] : laplace_op.GetSources())`: `:60-89` —
  loop opens at **line 60** (exact), `step++` at line 89, closing brace at 90; the range is sound.
- `GetStiffnessMatrix` FE-assembly `:184-223`: resolves exactly — `BilinearForm k(GetH1Space());
  k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func); k.Assemble(...)`. Honest.
- `GetExcitationVector` BC-elimination `:225-253`: resolves — `ProjectBdrCoefficient(one,
  source_marker)` at **line 238** (report says `:240`, `[DRIFT +2]`), `EliminateRHS(X,RHS)` at
  **line 252** (exact). Honest.

The drift never inverts a mapping (every `[DRIFT]` still lands inside or one line off the
construct it names) and the broad ranges (`:20-98`, `:60-89`, `:111-137`, `:184-223`) are all
correct, so the findings are not mis-localized — hence `warning`, not `fail`. The repairer
should snap the four off-by-one/off-by-two inner-loop pinpoints (`:69→:68`, `:70→:69`,
`:76-77→:78-79`, `:71-72→:73-75`, `:240→:238`) to the verified lines.

**surface-or-evidence — pass.** Not a refinement-shaped proposal. D6 is an observation-first
probe that proposes NO `book/` mutation (Proposed-changes: NONE). It modifies no operator/theme
surface and makes no rotation_claim against an existing entry; it records a coverage-gap finding
plus OQ-ledger appends. The redirect's "solvers are a test-load; what a solver can't cleanly say
is a finding about the spine; never force the spine" rule makes no-surface-no-rotation the
correct shape here. Not applicable as a refinement check; passes as a well-formed observation.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is
asserted (no L_{n+1}→L_n compaction claim is being landed). The report *names candidate* future
rotations (solve-family combinator, gram-unification) but explicitly defers them to future
combinator-miner/abstractor dispatches rather than claiming them now. Nothing to grade.

**variant-axis-coverage — pass.** The probe enumerates the driver body exhaustively into six
structural steps and classifies each (clean / not-clean / partial), and explicitly scopes out
`MeasureAndPrintAll` and `GradFluxErrorEstimator` as "not decomposed — out-of-probe-scope,
not claimed clean or unclean" (caveat 3). The MPI/Par* variant axis is handled per scope
(single-rank read, flag-once-and-skip for `comm`/`Mpi::Print`/`GlobalSum`). No hidden branch:
the step-7 capacitance reduction is correctly split into the firm-kernel part (`bilinear-form`)
and the un-spined `O(n²)` accumulation + `Invert()` part — both surfaced, neither hidden.

**cross-reference-integrity — pass.** All referenced spine slugs resolve on disk: `L4/ksp_solve.md`,
`L1/apply_linop.md`, `L1/bilinear-form.md`, `L2/gram.md`, `L1/assemble-diagonal.md`,
`L1/nrm2.md`, `L1/dot.md` all exist. The four "no entry at any layer" gap claims are
corroborated by full L1/L2/L3/L4 directory listings — no parametric-solve-sweep, FE-assembly-
from-integrators, BC-elimination/excitation, or capacitance/solution-family-Gram slug exists at
any layer, so the gaps are real, not mis-localized. No `[link]` is emitted (no book mutation),
so the firm-body-inside-fence build-readiness guard no-ops (no proposed-changes fence to enumerate).

**edge-label-fidelity — pass (not applicable).** No edge label (L_{n+1}→L_n) is carried; this is
a cross-layer coverage observation, not a lowering entry. Nothing to cross-check.

**plan-kind-consistency — pass.** Declared shape is an observation/coverage-gap probe
(`status: pending`, "Observation kind: Coverage gap", Proposed-changes NONE). Content matches:
findings + OQ appends + deferred work-items, no firm/rough-in entry authored. This is the
correct kind for a low-priority observation-first solver probe — no mis-classification.

**skill-uptake-survey — pass (telemetry).** The probe's shape (clean-describability against the
spine, no surface) does not strongly imply a specific invocable skill; `classify-variant-axis`
would have been a reasonable touch for the six-step decomposition but is not load-bearing here.
The report does correctly route the candidate-rotation work to the right downstream roles
(combinator-miner for the solve-family + gram probes, abstractor/harvester for FE-assembly),
which is the substance the skill-survey is a proxy for. No blocking gap; surfaced for telemetry.

### Issues found

1. **Inner-loop citation drift (citation-validity, warning).** `CYCLE.md:28` (`ksp.Mult` says
   `:70`, actual `:69`), `CYCLE.md:27` (`GetExcitationVector` says `:69`, actual `:68`),
   `CYCLE.md:29` and `:56` (field recovery `E=-∇V` says `:76-77`, actual `:78-79`),
   `CYCLE.md:30`/`:56` (`Norml2` print says `:71-72`, actual `:73-75`), `CYCLE.md:59`
   (`ProjectBdrCoefficient` says `:240`, actual `:238`). Consistent +1/+2/+3 forward drift on
   the per-iteration pinpoints. Severity low — no mapping is inverted, every drifted pinpoint
   still lands on or adjacent to the construct it names, and the surrounding broad ranges are
   correct. Repair: snap each to the codemap-verified line.

2. **`bilinear-form` mislabeled "firm" in one place (citation-validity / internal consistency,
   low).** `CYCLE.md:44` (Recommendation item 2) calls the step-7 per-entry kernel
   "already `bilinear-form` (firm)", but `book/src/L1/bilinear-form.md:4` is `firmness: rough-in`
   and the report's own Supporting-evidence line (`CYCLE.md:63`) correctly labels it "(rough-in)".
   The kernel-maps-cleanly claim itself is honest (law 8 `nrm2_M(x)² = bilinear_form(x,M,x)` at
   `bilinear-form.md:218` is literally `Cᵢᵢ`, verified), but the parenthetical "(firm)" overstates
   the maturity of the spine entry the kernel lands on. Repair: change "(firm)" → "(rough-in)" at
   `:44` for consistency with `:63` and the actual entry status. Severity low.

### Notes for the integrator (not defects)

- **Observation-first discipline is correct.** D6 proposes no `book/` mutation, records the
  gaps as findings + OQ appends, and routes candidate rotations to future dispatches with an
  explicit "do not mine-and-strand; replace-and-propagate" note (`:43`). This is exactly the
  redirect's "never force the spine / advance only when cleanly describable" behavior. An honest
  "not clean → spine finding" is the intended outcome of a low-priority solver probe — this is a
  PASS, not a failure to land an entry.
- **Cross-pipeline generality caveat is present and load-bearing.** All four gaps are explicitly
  marked single-witness / generality-unverified (`:78`, `:81`, and the OQ entries at `:73-75`),
  with the requirement that combinator-miner confirm the shape recurs across ≥2 pipelines before
  any entry lands. This honest caveat correctly gates any future authoring; it should be carried
  forward into the OQ-ledger appends verbatim.

---

## Repair

### Fixes attempted

- **Finding**: Inner-loop citation drift — consistent +1/+2/+3 forward drift on per-iteration
  pinpoints (`citation-validity`, warning).
  - **Decision**: repaired
  - **Action**: Snapped the five drifted pinpoints to codemap `read_range`-verified lines in both
    the step table (`CYCLE.md` §Specific finding) and the §Supporting evidence list. Independently
    re-verified each against `reference/palace/`:
    - `GetExcitationVector(idx,*K,V[step],RHS)`: `:69` → `:68` (verified at `electrostaticsolver.cpp:68`).
    - `ksp.Mult(RHS, V[step])`: `:70` → `:69` (verified at `:69`).
    - field recovery `E=0.0; Grad.AddMult(...)` (`E=-∇V`): `:76-77` → `:78-79` (`E = 0.0;` at 78, `Grad.AddMult` at 79).
    - `Norml2` postprocess print: `:71-72` → `:73-75` (verified at `:73-75`).
    - `ProjectBdrCoefficient`: `:240` → `:238` (verified at `laplaceoperator.cpp:238`).
    Corrected in both the step table (rows 4/5/6a/6b) and the §Supporting evidence bullets (line-56
    electrostaticsolver bullet + line-59 laplaceoperator bullet). The capacitance `Dot`-kernel
    `:118-126` bracket was left unchanged — the critic confirmed it correctly contains the diagonal
    `Dot` (119) and off-diagonal `Dot` (126), and codemap re-read confirms (`:119`, `:126`). The
    broad ranges (`:20-98`, `:60-89`, `:111-137`, `:184-223`, `:225-253`) were verified-correct by
    the critic and left unchanged. Pure mechanical pinpoint snap — no mapping or claim altered.

- **Finding**: `bilinear-form` mislabeled "(firm)" at `CYCLE.md:44` while the entry is
  `firmness: rough-in` and `:63` correctly says "(rough-in)" (internal inconsistency, low).
  - **Decision**: repaired
  - **Action**: Changed "(firm)" → "(rough-in)" in Recommendation item 2 (`CYCLE.md` §Recommendation)
    for consistency with `:63` and the actual `book/src/L1/bilinear-form.md` status. The kernel-maps-
    cleanly claim itself was untouched (it is honest per the critic); only the parenthetical maturity
    label was corrected. Trivial in-place consistency fix.

### Unrepairable findings

None. Both flagged issues are mechanical (pinpoint snap; consistency-label fix) and within repair
authority. No surface, rotation-quality, or variant-axis authoring was implicated. Proposed-changes
remains NONE (observation-only probe; confirmed no `book/` mutation introduced by repair).

## Suggested resolution

`ready`. Notes for the integrator:
- The probe proposes NO `book/` mutation — the deliverable is the spine-coverage finding + the
  three OQ-ledger appends (`electrostatic-outer-terminal-sweep-needs-solve-family-combinator`,
  `capacitance-reduction-may-be-gram-variant-axis-extension`,
  `fe-assembly-from-integrators-is-an-unspined-surface`) plus the four ranked spine work-items.
  Promote the OQ appends verbatim, carrying the single-witness / generality-unverified caveats
  (`:78`–`:81`) forward intact — combinator-miner must confirm the solve-family shape recurs across
  ≥2 pipelines before any entry lands.
- The convergence of item 1 (solve-family combinator, "next combinator from solver material") with
  D5's negative finding is a batch-16 frontier signal worth surfacing to the meta-phase.
