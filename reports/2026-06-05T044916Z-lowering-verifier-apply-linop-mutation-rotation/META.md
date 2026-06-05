---
verifies: ../REPORT.md
critiqued_at: 2026-06-05T05:12:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-05T05:30:00Z
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

# META: verification of "Audit apply-linop-mutation-rotation" (rough-in→firm)

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` (45 ok / 21 "failing"; every one of the 21 is an `[AMBIG]` basename-collision diagnostic because `operator.{hpp,cpp}` resolves to BOTH `palace/linalg/` and `palace/fem/libceed/` — NOT a bounds or content failure; the tool cannot disambiguate a bare basename, and the theme's intent is unambiguously `linalg/`). I then re-verified the load-bearing pinpoints directly via codemap `read_range`. **All three claimed drift corrections are CONFIRMED:** (1) `operator.cpp:509-519`→`520` — the `BaseDiagonalOperator<Operator>::AddMult` forall body is at line 519 and the closing `}` is at line 520; original range excluded the brace. (2) `rap.cpp:320-360`→`361` — `y.Add(a, tx);` is at line 360 and the closing `}` is at line 361. (3) `rap.cpp` note "line 220"→`219` — the inner `A->Mult(lx, ly);` is at line 219 (the `// Apply the operator on the L-vector.` comment at 218); original note was off by one. I also spot-confirmed `operator.cpp:428-441` (SumOperator::Mult, `y *= ops.front().second` at 435, `y = 0.0` / `AddMult(x, y)` reuse), `operator.hpp:158-175` (Hermitian-transpose composition witnesses), and `operator.hpp:220-225` (BaseProductOperator::AddMultTranspose body) — all exact. The `verified_against:` YAML payload (23 entries) round-trips under `yaml.safe_load` and no `note:` value begins with a quote character (the round-trip sub-check passes). The single finding: the **new corrected note** for `operator.cpp:428-441` (CYCLE.md line 284) states "y = 0.0 (438) then AddMult(x, y) (439)" but the actual lines are **439 and 440** — a fresh internal-line off-by-one introduced inside a note whose whole purpose was correcting off-by-ones. Range `:428-441` itself is exact, no recognition rule is affected, but the warning is warranted on precision grounds (same close-brace/internal-line class the report is auditing).

**surface-or-evidence — pass.** This is a refinement-shaped proposal (rough-in→firm status flip on an existing theme) that modifies surface (the `## Status` body + dep-map cell + an L3 cross-ref token) AND carries the rotation/recognition evidence (the per-citation audit + the syntactic-identity argument). It is the canonical "retroactive evidence backfill + status promotion" shape, fully grounded. Record-definition sub-check: the theme names no new record/struct in a signature — it lowers `apply_linop` onto the `Operator`/`ComplexOperator` virtual family, both of which are pre-existing L0 C++ types referenced (the `ComplexWrapperOperator` lift is explicitly routed to the `complex-from-real-lift` concept as out-of-theme), so no definition-home obligation is triggered.

**rotation-quality — pass.** Not a new rotation; the audit confirms an existing one. The firm verdict rests on the **firm-on-positive-structure / syntactic-identity escape** named in the CLAUDE.md `rough-in (test-coverage-bounded)` invariant. I verified the escape's precondition holds: every one of the five sub-rules (A structural; B/C/D/E algebraic) is a name-match identity read off a fully-specified *positive* `Mult`-family method body (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `ParOperator`, `ProductOperatorHelper` realisations all read on-disk), NOT a numerically-asserted axiom or convergence-semantics claim. The D/E composition path is correctly characterized as the composition of two already-firm syntactic rules (`apply_linop` + the firm sister theme `axpby-mutation-rotation`), so the deferred "integration testing" does not gate a syntactic identity. The rank check (`rank(theme) ≤ min(firm, firm)`, both endpoints firm) is correctly applied. The escape is legitimately invoked — this is the `apply_linop` situation, not the `eigsolve` situation.

**variant-axis-coverage — pass.** The orthogonal axes are transpose-mode (forward / transpose / Hermitian-transpose) × accumulate-mode (overwrite / accumulate). All combinations are covered by the five sub-patterns: A (forward×overwrite), B (transpose×overwrite), C (Hermitian×overwrite), D (forward×accumulate), E (transpose+Hermitian×accumulate). C is explicitly scoped complex-only (collapses to B on reals, stated). The D/E composition path is explicitly handled (composition of firm rules; inner accumulator delegated to the sister theme, not silently dropped). The operator-representation axis is correctly noted as absorbed at L1. No hidden branch.

**cross-reference-integrity — pass.** All three edit targets exist on disk: `book/src/L1-L0/index.md` (row at line 21 matches the report's quoted pre-edit text exactly — `rough-in` status cell, status-column-only flip), `book/src/L3/apply_linop.md` (line 169 matches the quoted `(rough-in; cycle-007)` parenthetical exactly), and the theme file itself. The L1 anchor (`book/src/L1/apply_linop.md`), sister theme (`book/src/L1-L0/axpby-mutation-rotation.md`), and L3 entry all exist. All `[link]` references in the proposed prose resolve.

**edge-label-fidelity — pass.** This is an L1>L0 theme; the dep-map row flip is in `book/src/L1-L0/index.md` (the L1>L0 Part index), and the prose discusses the L1 `apply_linop` form lowering to the L0 `Mult`-family — exactly the L1→L0 edge. The coupled Change-3 touch is in the L3 entry's "Downward to L_n" cross-reference and correctly re-anchors only this theme's *own* maturity token (rough-in→firm), not an edge re-label. Directions consistent throughout.

**plan-kind-consistency — pass.** Declared kind is a `lowering-verifier` audit issuing a firm-promotion verdict. Content shape matches: a complete per-citation audit table, applicability-condition verification, an algebraic-laws/escape-reasoning section, and three surgical proposed-changes (status flip + dep-map cell + coupled L3 re-anchor). No rough-in placeholders remain in the firm-claimed body; the verdict is decisive (FULLY-SUPPORTED → FIRM) with the deferred gate explicitly discharged via the escape.

**skill-uptake-survey — warning.** The report's shape implies two relevant skills exist and were not referenced: `verify-citation-range` (the audit is wall-to-wall citation-range verification) and `verify-rotation-citation` (the rotation/escape argument). The report describes doing the equivalent work by hand (direct `read_range` on every range, with a note that the close-brace off-by-ones "needed a direct on-disk Read, which I did"). Pure telemetry, non-blocking — surfaces that the citation-verification skills were not invoked by slug even though the work matched them.

### Issues found

1. **citation-validity (minor, precision) — CYCLE.md line 284, the new `verified_against` note for `operator.cpp:428-441`.** The note states the size>1 reuse path as "y = 0.0 (438) then AddMult(x, y) (439)". On-disk the lines are **439** (`y = 0.0;`) and **440** (`AddMult(x, y);`); the closing `}` is at 441. This is a fresh internal-line off-by-one introduced in a corrected note. Severity: low — the cited range `:428-441` is exact, the recognition rule (Mult-via-AddMult reuse) is unaffected, and the verdict does not turn on it. Repair: change "(438)"→"(439)" and "(439)"→"(440)" in that single note. (Candidate for the repairer.)

2. **skill-uptake-survey (telemetry, non-blocking).** The audit performed citation-range and rotation-citation verification by hand without referencing the matching skill slugs (`verify-citation-range`, `verify-rotation-citation`). No correctness impact; recorded as uptake telemetry only.

### Notes for the repairer / integrator

- The three drift corrections the report makes are all CORRECT and independently confirmed via codemap; they should be applied as-is (they fix real off-by-ones in the pre-existing theme citations).
- The `[AMBIG]` citecheck diagnostics are basename-collisions (`operator.{hpp,cpp}` exists in both `linalg/` and `fem/libceed/`), NOT defects in this report — the theme's `palace/linalg/` intent is unambiguous from context. Not a repair item; flagged only so the integrator does not misread the citecheck summary as 21 real failures.
- The firm verdict and the escape application are sound; the only fix-worthy item is the single internal-line off-by-one in issue 1.

## Repair

### Fixes attempted

- **Finding**: citation-validity (minor, precision) — CYCLE.md line 284, the new `verified_against` note for `operator.cpp:428-441` states the size>1 reuse path as "y = 0.0 (438) then AddMult(x, y) (439)"; actual lines are 439/440 (closing `}` at 441). A fresh internal-line off-by-one introduced inside a note correcting other off-by-ones.
  - **Decision**: repaired
  - **Action**: Re-confirmed via codemap `read_range palace/linalg/operator.cpp:428-441` — line 428 is the `void SumOperator::Mult` signature, `y = 0.0;` lands at 439, `AddMult(x, y);` at 440, `}` at 441. Edited the note in CYCLE.md (`verified_against:` payload for `palace/linalg/operator.cpp:428-441`): "(438)"→"(439)" and "(439)"→"(440)". The unflagged "(line 435)" for the size-1 `y *= ops.front().second` fast path was also independently confirmed correct and left as-is. Cited range `:428-441` was already exact; no recognition rule affected.

- **Finding**: skill-uptake-survey (telemetry, non-blocking) — citation-range / rotation-citation verification done by hand without referencing `verify-citation-range` / `verify-rotation-citation` slugs.
  - **Decision**: not-needed
  - **Rationale**: pure uptake telemetry, no correctness impact and nothing in CYCLE.md to mechanically change. Recorded by the critic; no repair action.

### Unrepairable findings

None.

## Suggested resolution

`ready`. The single precision off-by-one is fixed and re-confirmed against codemap; the firm-promotion verdict, the syntactic-identity / firm-on-positive-structure escape application, and the three pre-existing-citation drift corrections are all sound per the critic and preserved unchanged.

Note for the integrator: the 21 citecheck "failing" lines are `[AMBIG]` basename collisions (`operator.{hpp,cpp}` resolves to both `palace/linalg/` and `palace/fem/libceed/`), NOT real bounds/content failures — the theme's `palace/linalg/` intent is unambiguous from context. Do not misread the citecheck summary as 21 real failures.
