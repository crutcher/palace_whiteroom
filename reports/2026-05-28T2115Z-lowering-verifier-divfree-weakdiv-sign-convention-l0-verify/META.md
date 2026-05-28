---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T21:40:00Z
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
repaired_at: 2026-05-28T21:55:00Z
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

# META: verification of "Audit divfree-projector — WeakDiv ≈ -GᵀM sign-convention promotion gate"

## Critique

### Checks run

**citation-validity** — WARNING. The two load-bearing sign anchors are verified Palace-owned and say what is claimed, with ONE uniform off-by-one. Via `palace-codemap`: `palace/fem/integrator.hpp:217` is exactly `// Integrator for a(u, v) = -(Q u, grad v) for u in H(curl) and v in H1.` and `class MixedVectorWeakDivergenceIntegrator` opens at `:218`. The sibling non-negated `MixedVectorGradientIntegrator` call `PopulateCoefficientContext(space_dim, Q, transpose)` is exact at `:142`. BUT the negating `-1.0` coefficient `PopulateCoefficientContext(space_dim, Q, transpose, -1.0)` is on line **`:202`**, NOT `:203`. The report cites `:203` uniformly (Summary, per-citation audit lines 100/102, Edits 1/2/3, Open-questions, Supporting-evidence). `:203` is the *following* `AssembleCeedOperator` line. The claim is correct; the anchor is off-by-one everywhere. Spot-checked `divfree.cpp` anchors `:113`/`:117`/`:119` — all exact.

**surface-or-evidence** — PASS. This is an audit report (rotation_claim / retroactive-evidence shape), not a surface-modifying refinement. It proposes evidence backfill (the positive sign anchor) plus gated firming edits routed to a follow-up — squarely the allowed retroactive-evidence path.

**rotation-quality** — PASS (n/a as primary axis). Audit, not a layer rotation. The sign-derivation logic is sound: `a(u,v) = -(εu,∇v)` with `(u,∇v)=(u,Gv)=(Gᵀu,v)` gives `WeakDiv = -Gᵀ(ε)`; the apply's additive `+1.0` then nets to subtraction, so `WeakDiv·(P·y)=0` on an already-divfree field and `P∘P=P` holds. The `-1.0` does establish the signed identity.

**variant-axis-coverage** — PASS. Real vs. complex branches both audited (`:161-162`/`:180-181`); dim/space_dim cases noted; no hidden branch.

**cross-reference-integrity** — PASS. `book/src/L1/divfree-projector.md` exists; all source slugs resolve; `palace/fem/integ/mixedvecgrad.cpp` and `palace/fem/integrator.hpp` both confirmed present in the Palace tree (codemap, which indexes only the target repo — not `reference/`-vendored MFEM).

**edge-label-fidelity** — PASS. L1 entry audit; prose stays at L1 with L0 anchors; no mismatched edge label.

**plan-kind-consistency** — PASS. Verdict UNBLOCK-PROMOTION with `## Status` left untouched (lines 39, 137-138, 246-250) — correctly gates rather than enacts, per the `partly-constructive` invariant. The 5 firming edits are coherent and consistent with that gate.

**skill-uptake-survey** — WARNING. Report shape (citation-range re-verification + inherited-citation audit) directly matches `verify-citation-range` (whose cycle-012 "Audit-report / inherited-citation sub-case" exists for exactly this), yet no skill invocation is referenced. Telemetry only; non-blocking. Ironically, invoking it might have caught the `:202`/`:203` slip.

### Issues found

1. **`mixedvecgrad.cpp:203` → `:202` — uniform off-by-one on THE central sign anchor.** The `-1.0` is on `:202`; `:203` is the next `AssembleCeedOperator` line. Occurs in CYCLE.md Summary (line 31), per-citation audit (lines 100, 102, 107), Edit 1 (line 148/156), Edit 2 (line 181), Edit 3 (line 190), Open-questions (line 236), Supporting-evidence (line 227). Severity: **medium-high** — the UNBLOCK verdict is correct and the file IS Palace-owned/in-scope, but the anchor that would be written into `book/` Evidence/Status by the follow-up is wrong on every occurrence. Repair = global `:203`→`:202`.

2. **`integrator.hpp` integrator-class range cited as `:218-226` / `:217-226` inconsistently.** Class opens at `:218` (doc at `:217`); report uses both `:217-226` (line 26) and `:218-226` (Edit 1 line 159). Minor; non-load-bearing. Severity: low.

3. **Self-flagged anchor-hygiene fixes (Edit 5) carry forward unverified `:142` abs-tol → `:142`.** The report's own Edit 5 corrections (`:141`→`:142`, `:68-72`→`:67-71`) are internally consistent but were not independently re-confirmed in this critique beyond the sign anchors; flagged for repairer attention alongside issue 1. Severity: low.

**Integ files confirmed Palace-owned, in scope.** `palace/fem/integrator.hpp:217` (`a(u,v)=-(Q u,grad v)`) and `palace/fem/integ/mixedvecgrad.cpp` `-1.0` (`:202`, not `:203`) + sibling no-`-1.0` (`:142`) verified via codemap — NOT MFEM-vendored. UNBLOCK premise holds; one uniform `:203`→`:202` off-by-one.

## Repair

### Fixes attempted

- **Finding (citation-validity, issue 1)**: the `-1.0` weak-div sign coefficient `PopulateCoefficientContext(space_dim, Q, transpose, -1.0)` cited uniformly at `mixedvecgrad.cpp:203`; the actual line is `:202` (`:203` is the following `AssembleCeedOperator` call).
  - **Decision**: repaired.
  - **Action**: re-confirmed via `palace-codemap read_range palace/fem/integ/mixedvecgrad.cpp:198-206` — line `:202` is `auto ctx = PopulateCoefficientContext(space_dim, Q, transpose, -1.0);`, `:203` is `AssembleCeedOperator(...)`. Corrected all 9 occurrences of `mixedvecgrad.cpp:203` → `:202` in CYCLE.md: Summary, per-citation-audit (THE SIGN ANCHOR heading + the `:148-205` Found body), Algebraic-laws "Non-law sign convention", Applicability-conditions, Evidence within Edit 1, Edit 2 Caveat-rewrite, Edit 3 Status-rewrite text, Open-questions OQ-resolution, Supporting-evidence. Zero `:203` references remain (verified by grep). The off-by-one was mechanical; the cited content is exactly what the report claims, the file is Palace-owned/in-scope, and the UNBLOCK-PROMOTION verdict stands.

- **Finding (citation-validity, issue 2)**: integrator-class range cited as both `:217-226` and `:218-226` (class opens `:218`, doc line `:217`).
  - **Decision**: not-needed.
  - **Rationale**: both ranges are valid and enclose the same construct (`:218-226` = the class body; `:217-226` = doc-comment-inclusive). Non-load-bearing; the central anchor for the doc text is `:217` which is correct everywhere. No content decision involved; left as-is.

- **Finding (citation-validity, issue 3)**: Edit 5 self-flagged anchor-hygiene fixes (`:141`→`:142` abs-tol, `:68-72`→`:67-71` out-of-place `Mult`) not independently re-confirmed by the critic.
  - **Decision**: not-needed (verified-correct).
  - **Action/Rationale**: independently re-confirmed via codemap — `divfree.cpp:142` is `pcg->SetAbsTol(std::numeric_limits<double>::epsilon());` and `divfree.hpp:67` opens `void Mult(const VecType &x, VecType &y) const` with body `{ y=x; Mult(y); }` at `:69-70`. The report's Edit 5 corrections are accurate as written; nothing to change.

- **Finding (skill-uptake-survey)**: report shape matches `verify-citation-range` (incl. its cycle-012 inherited-citation sub-case) but no invocation referenced.
  - **Decision**: not-needed.
  - **Rationale**: telemetry-only / non-blocking per critic; no content or citation defect to repair. Noted for meta-phase batch-3 telemetry.

### Unrepairable findings

None. The sole load-bearing finding (the `:203`→`:202` off-by-one) was mechanical and surgically repaired; the remaining two citation-validity sub-notes were either benign (issue 2) or already-correct (issue 3).

### Gated firming edits preserved

The 5 firming edits under `## Proposed changes` (Edits 1-5, for the cycle-015 follow-up that enacts the `partly-constructive`→`firm` promotion on `book/src/L1/divfree-projector.md` and closes OQ `divfree-weakdiv-sign-convention-l0-verify`) remain a clean, delimited, GATED block. They were not enacted; only the embedded `:203`→`:202` sign anchor was corrected within them so the follow-up writes the correct line into `book/`.

## Suggested resolution

`ready`. The UNBLOCK-PROMOTION audit is sound and now citation-clean. Integrator note: this report does NOT mutate `book/` — it gates a promotion. Carry the 5 firming edits forward to the cycle-015 follow-up (abstractor on `divfree-projector`) which applies Edits 1-5 then flips `## Status` to `firm` and closes the OQ. The corrected sign anchor is `palace/fem/integ/mixedvecgrad.cpp:202` (with `palace/fem/integrator.hpp:217`).
