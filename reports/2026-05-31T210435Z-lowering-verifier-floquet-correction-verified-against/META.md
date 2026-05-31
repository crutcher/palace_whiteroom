---
verifies: ../CYCLE.md
critiqued_at: 2026-05-31T214500Z
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
repaired_at: 2026-05-31T215200Z
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

# META: verification of "Audit floquet-correction-mutation-rotation"

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` on the report: `43 ok, 2 failing`. The 2 failures are `open-questions.md:899` and `:898` — `scaffolding/open-questions.md` ledger references, not Palace source citations; they are out-of-tree for the `--scan` path-resolver (it searches `reference/*` + `book/src`), so this is a path-hygiene artifact, not a source-citation defect. The report's own claim of "43 ok, 0 failing" is scoped to the *theme's* inline citations and is consistent with this. I then re-verified the load-bearing sites on-disk (codemap-independent):
- `floquetcorrection.cpp:61` = `pcg->SetInitialGuess(0)` ✓; `:73-78` `Mult` body verbatim (`Cross->Mult(x, rhs); ksp->Mult(rhs, y)`) ✓; `:80-86` `AddMult` body verbatim (`this->Mult(x, rhs); rhs *= a; y += rhs;`) ✓; `:88` sole `template class FloquetCorrSolver<ComplexVector>;` ✓.
- **The ONE finding's evidence verified on both legs.** (a) `ksp.cpp:297-310` IS `BaseKspSolver<OperType>::Mult` and IS a thin timing+convergence wrapper delegating to `ksp->Mult(x, y)` at `:300` — it does NOT exhibit the reads-x-once-then-writes-y mechanism, exactly as the report claims. (b) `iterative.cpp:361` IS `CgSolver<OperType>::Mult(const VecType &b, VecType &x)`; the `!initial_guess` else-branch at `:384-385` runs `r = b; x = 0.0;` (copies `b` into workspace `r` BEFORE zeroing the aliased `x`) — the genuine aliasing-safety mechanism, gated by `SetInitialGuess(0)` at `floquetcorrection.cpp:61`. Both legs of the finding hold precisely.
- `--anchor` spot-checks lit: `floquetcorrection.cpp:67` `'SetOperators'` ✓; `materialoperator.cpp:358` `'wave_vector_cross'` ✓.
- The `:25-26` over-extension nit the report self-flags is accurate: `:25` is the comment, `:26` is the `{`; non-load-bearing, range `:26-39` correct.

**surface-or-evidence — pass.** This is a pure retroactive-evidence-backfill report (emit a `verified_against:` block against an already-firm theme; "metadata addition only — no theme claim is changed"). The proposed-changes block touches no operator/theme surface text. Retroactive evidence backfill is explicitly allowed; no rotation_claim-without-surface concern arises.

**rotation-quality — pass (not a rotation-proposing report).** No new L_{n+1}→L_n rotation is asserted; the report audits an existing structural+algebraic rotation. The substantive judgment here is whether the AddMult-as-axpy *structural* rewrite remains sound under the finding — it does: the rewrite at `floquetcorrection.cpp:80-86` is positively witnessed and untouched by the citation gap (which lands on a precondition, not the rewrite). The compaction direction (L1 erases scratch member + output-arg mutation; AddMult unfolds to `axpy ∘ floquet_correction`) is genuine state-hiding, not a renaming.

**variant-axis-coverage — pass.** The operator's variant axes are covered: Mult vs. AddMult entry points (sub-patterns A/B), `<ComplexVector>` vs. hypothetical `<Vector>` element-type (sub-pattern D, scoped-out with the dead-code `if constexpr` real branches at `:35-38, :53-56` positively cited), and the construction-vs-application split (sub-pattern C). I confirmed the `<ComplexVector>`-only scope-out exhaustively on-disk: all six driver bindings (`drivensolver.cpp:138/141/289/292`, `eigensolver.cpp:237/240`) are `<ComplexVector>`; no `<Vector>` anywhere. No hidden branch.

**cross-reference-integrity — pass.** Not a firm-body-inside-fence case (the proposed-changes block is an `[append at end of file]` of a `verified_against:` YAML block, not a chapter body, so the fence-truncation guard no-ops on substance). Nonetheless I enumerated fences: the outer `````edit:` fence (4-backtick, `:143`/`:272`) correctly encloses the inner ```` ```yaml ```` fence (3-backtick, `:146`/`:271`); the `:134` occurrence is inline escaped-backtick prose, not a fence. Parity balanced, nested fence well-formed. The L1 anchor `book/src/L1/floquet-correction.md` and OQ `floquet-corrector-addmult-aliasing-applicability-audit` (open-questions.md:899) both resolve on-disk.

**edge-label-fidelity — pass.** The theme is an L1>L0 edge; every row of the audit discusses L1→L0 lowering content (the L1 `floquet_correction` form lowering into L0 `FloquetCorrSolver` member methods). The four AddMult call-site rows, three construction-site rows, and element-type scope-out rows all stay on the L1>L0 edge. The exhaustiveness claim ("all four AddMult call sites") I verified independently: exactly 4 sites (`drivensolver.cpp:212/336/468`, `eigensolver.cpp:454`), matching the four cited ranges. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is an `audit` (lowering-verifier `verified_against:` emission). Content shape matches: per-citation supports/partially-supports verdicts, an applicability-condition table, a single substantive finding routed (not enacted), theme left `firm`. The audit correctly did NOT mutate the theme or the OQ ledger — confirmed via `git status` (both files clean). This is the correct gated-unblock discipline for a lowering-verifier (confirm structure + identify exact firming edits, do not enact).

**skill-uptake-survey — pass.** The report references the mechanical `tools/citecheck/citecheck.py` realization (`--scan` + `--anchor`) of `verify-citation-range`, and self-applies `verified-against-note-no-leading-quote-of-either-kind` to the emitted block. Both are the shape-appropriate skills for an audit-class report. Telemetry only; non-blocking.

### Issues found

No blocking issues. The audit is well-executed; the one substantive finding is correctly classified and its evidence holds on-disk. The items below are observations for the integrator/repairer, none rising to a verdict change.

1. **(observation — disposition is correct, but worth surfacing for the integrator) The firm/partially-supports split is drawn at the right boundary.** CYCLE.md:75 / §Applicability-conditions row 2: the finding is an *applicability-condition citation insufficiency* (`ksp.cpp:297` is a delegating wrapper, the mechanism lives at the uncited `iterative.cpp:361` + `:384-385` gated by `floquetcorrection.cpp:61`), NOT a structural-rewrite defect. The theme's `firm` status rests on the AddMult-as-axpy structural rewrite (`floquetcorrection.cpp:80-86`), which is fully positively witnessed and untouched by the gap. Keeping `firm` while marking the single row `partially-supports` is the correct disposition: the load-bearing rewrite is sound; only an evidence pointer on a precondition is weak. A repairer should NOT widen the theme's citation in-cycle — the lowering-verifier's role is to UNBLOCK + route, not ENACT (the recommended carry-forward at CYCLE.md:287-290 is the right channel). The OQ is correctly left OPEN, not closed.

2. **(minor — non-blocking, for a future abstractor) Theme citation over-extension at `floquet-correction-mutation-rotation.md:230`.** The M-block comment is cited as `:25-26`; on-disk `:25` is the comment, `:26` is the opening brace `{`. The enclosing range `:26-39` is correct, so this is a one-line over-extension, not a citecheck-failing drift. The report records it in the `cpp:20-71` row note and flags it as opportunistically-tightenable. Confirmed accurate on-disk; agree it is non-blocking.

3. **(scan-hygiene note, not a defect) Two `--scan` MISS lines are ledger references, not source citations.** `open-questions.md:898/899` fail `--scan` only because the path-resolver does not search `scaffolding/`. The report's "43 ok / 0 failing" framing is scoped to the theme's inline source citations and is internally consistent; flagging here only so the repairer does not mistake these for real citation failures.

4. **(forward-looking, for the routed follow-up — NOT this report's scope) The `partially-supports` note correctly names the load-bearing precondition.** CYCLE.md:289 / proposed row note at CYCLE.md:173 record that aliasing safety is contingent on `SetInitialGuess(0)` (else-branch `r = b; x = 0.0;`); with `initial_guess == true` the `:379` `A->Mult(x, r)` path would read the aliased `x` while forming the residual — a different safety case the theme does not cover. The floquet ksp always sets `SetInitialGuess(0)` (`floquetcorrection.cpp:61`, verified on-disk), so the precondition holds; naming it is the correct firming edit for the follow-up dispatch to land. No action for this report.

## Repair

### Fixes attempted

This is an audit-class report the critic judged CLEAN — all 8 checks `pass`, zero warning/fail findings. No finding requires (or permits) a repair. Per-check disposition is `not-needed` across the board. The four critic "observations" are explicitly non-verdict-changing and either correctly-disposed-already or scoped to a future dispatch:

- **Finding (obs. 1 / the one `partially-supports` row)**: AddMult aliasing-tolerance mechanism cited to the thin wrapper `ksp.cpp:297` rather than the true mechanism site `iterative.cpp:361` / `:384-385` (gated by `SetInitialGuess(0)` at `floquetcorrection.cpp:61`).
  - **Decision**: not-needed (out of repair authority — do NOT enact in-cycle).
  - **Rationale**: This is NOT a repairable citation off-by-offset or forgotten-range slip. It is the lowering-verifier's *correct gated disposition*: the structural AddMult-as-axpy rewrite (`floquetcorrection.cpp:80-86`) is fully positively witnessed, so the theme correctly stays `firm`; only one applicability-condition citation is insufficient, marked `partially-supports`, and the fix is routed forward as the sharpened OQ `floquet-corrector-addmult-aliasing-applicability-audit` (open-questions.md:899) for a future dispatch. Widening the theme's citation here would ENACT what the verifier deliberately UNBLOCKED-but-did-not-enact — substantive authoring beyond repair scope. Left as-is.

- **Finding (obs. 2)**: theme citation over-extension at `floquet-correction-mutation-rotation.md:230` (`:25-26` where `:26` is the brace; correct range `:26-39`).
  - **Decision**: not-needed.
  - **Rationale**: The report self-flags this as opportunistically-tightenable and non-citecheck-failing; it lives in the *theme artifact* (`book/src/L1-L0/...`), which is out of repairer write-scope (artifact mutation is the integrator's domain). One-line over-extension, non-blocking; not a CYCLE.md defect.

- **Finding (obs. 3)**: two `--scan` MISS lines `open-questions.md:898/899`.
  - **Decision**: not-needed.
  - **Rationale**: These are `scaffolding/open-questions.md` ledger-path references, not Palace source citations — the `--scan` path-resolver does not search `scaffolding/`. Path-hygiene artifact, NOT a citation defect. The report's "43 ok / 0 failing" framing is scoped to the theme's inline source citations and is internally consistent. Nothing to repair.

- **Finding (obs. 4)**: forward-looking note on the `SetInitialGuess(0)` precondition.
  - **Decision**: not-needed (forward-looking; belongs to the routed follow-up).

### Regression sanity check (no-op edits, confirm only)

Independently re-confirmed the critic's build-readiness checks on the emitted `verified_against:` block (no edits applied):
- Round-trips through `yaml.safe_load` cleanly: **29 rows = 28 `supports` + 1 `partially-supports`**.
- **No `note:` begins with a quote of either kind** (0 leading-quote rows) — satisfies `verified-against-note-no-leading-quote-of-either-kind`.
- Nested ```` ```yaml ```` fence (3-backtick) is balanced inside the outer `````edit:```` fence (4-backtick); parity holds.

No regression. No content edits made (no theme mutation, no citation widening).

### Unrepairable findings

None. All findings are either correctly-disposed-already (obs. 1 — gated to a follow-up dispatch by design) or out-of-scope-for-repairer-but-non-blocking (obs. 2 artifact-side tightening; obs. 3 scan-hygiene). No finding routes a follow-up agent for *this* report — the obs. 1 follow-up is already captured as the OPEN OQ `floquet-corrector-addmult-aliasing-applicability-audit`, which the plan/OQ-ledger owns, not a repair carry-forward.

## Suggested resolution

`overall_status: ready`. No repairable findings; report is clean. The single `partially-supports` row is correctly routed to a future dispatch (sharpened OQ already OPEN), NOT repaired in-cycle — the verifier's UNBLOCK-not-ENACT discipline held. Integrator note: apply the `verified_against:` block append as-is; the theme stays `firm`; leave the OQ OPEN.
