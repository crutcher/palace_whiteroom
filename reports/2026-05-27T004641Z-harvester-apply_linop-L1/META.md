---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T01:05:00Z
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
---

# META: verification of harvester apply_linop L1

## Critique

### Checks run

- **citation-validity**: Spot-checked ~10 ranges. `operator.hpp:21,24-68,36-39,116-136,178-229,202-206`, `operator.cpp:428-441,458-466`, `rap.cpp:195-234,236-275,481-517`, `iterative.cpp:379,443` all verify. `BaseMultigridOperator` at `operator.hpp:298-367` (report says 298-367 in Evidence but uses `347` for Mult in Context — line 347 falls inside the class body, plausible for the Mult dispatch). `BaseDiagonalOperator` Mult decl at line 277 verified.
- **surface-or-evidence**: New L1 chapter + dep-map row + SUMMARY.md entry — pure surface emission; evidence-rich. No retroactive-evidence issue.
- **rotation-quality**: L0→L1 rotation is genuine compaction: destination-buffer erased; 6+ virtual methods (Mult/MultTranspose/MultHermitianTranspose × overwrite/accumulate) collapse to one functional `apply_linop(A, x)` with transpose-mode recovered via `Aᵀ`/`Aᴴ` and accumulate-mode recovered via `axpby` composition. Strictly more equational.
- **variant-axis-coverage**: 3 retained axes (element-type, transpose-mode, accumulate-mode) + 1 collapsed (operator-representation) with explicit justification via variant-absorption. Agree with classification — operator-representation genuinely invisible at the L1 contract surface. Rectangular `[M, N]` signature is consistent with `Height()`/`Width()` distinction at `operator.hpp:36-39` and rectangular witnesses (prolongation/restriction at `rap.cpp:212`, `Grad`/`WeakDiv`); not a hidden variant.
- **cross-reference-integrity**: All concept refs resolve (`apply_linop.md`, `constructed-operators.md`, `variant-absorption.md`, `apply_BA.md` all present under `book/src/concepts/`). L1 siblings (axpy/dot/nrm2/axpby) all present. SUMMARY.md insertion well-targeted.
- **edge-label-fidelity**: This is L1 firm-up, not a lowering edge. Lowering theme references say `L1>L0` consistently. Not applicable as critic-axis but consistent where invoked.
- **plan-kind-consistency**: Declared `firm` operator; content matches (canonical signature, 7 laws, 3+1 variant axes, evidence-cited). No rough-in placeholders.
- **skill-uptake-survey**: `classify-variant-axis` (artifact_landed), `verify-citation-range` (explained_non_applicable per cycle-002 pattern), `skill-selection` (artifact_landed). Survey present and fully populated.

### Issues found

1. **Line-number drift in Context paragraph** (CYCLE.md §Context, bullet for `BaseMultigridOperator`): cited as `operator.hpp:347` for the Mult dispatch, but the class spans 298-367 (Evidence section is correct). Minor — likely the Mult line within the class, not the class header. *Severity: low.*
2. **`AddMult` decomposition bit-equivalence caveat** (CYCLE.md §Semantics + Open question #3): the report acknowledges `AddMult = axpby(a, apply_linop(A, x), 1, y)` is bit-equivalent only for assembled operators, not matrix-free. Flagged in own Open questions but the Semantics prose states the equivalence without inline guard — repairer may want to add a single-clause hedge. *Severity: low.*
3. **L1>L0 lowering theme size flag** (CYCLE.md Open question #2): the report flags that the `apply-linop-mutation-rotation` lowering theme will be substantially larger than `axpby-mutation-rotation`, but does NOT route this as an entry in `scaffolding/open-questions.md`. Per the format used by sibling reports (e.g. `axpy-lowering-deliverables`, `nrm2-lowering-theme-deliverables`), this finding deserves an open-questions slug. *Severity: medium — surfacing pattern is established and skipped here.*
4. **Concept-page drift not problem-channel-routed** (CYCLE.md Open question #1): noted that `concepts/apply_linop.md` has structural drift (duplicate heading, "L3 tensor-field form" mis-located). Per the "in-reading drive-by observation" pattern relaxed 2026-05-26, this is a candidate for `problems/` filing, not just an in-report caveat. *Severity: low — discretionary.*
5. **Missing rectangular witness for square-case caveat** (CYCLE.md §Signature): the prose says "For square operators (the common case in iterative solvers: `A` is square in CG and GMRES, both squares of dimension `M = N`)". Phrasing "both squares of dimension M = N" reads oddly — appears to mean both CG and GMRES, but parses ambiguously. *Severity: low — copy-edit.*
