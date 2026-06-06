---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T020000Z
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
  rank-invariant: pass
  reachability: pass
overall_status: ready
---

# META: verification of cycle-111 D2 — L1>L0 axpy-family theme typed-edge frontmatter

## Critique

### Checks run

**citation-validity — pass.** This is a frontmatter-only typing report; every load-bearing
claim is a `cites-evidence` L0 source range. I spot-checked 5 ranges directly on disk against
`reference/palace/palace/linalg/vector.{cpp,hpp}` (more than the required 3):
- `vector.cpp:710` — `y.Add(alpha, x);`, the α≠1 `else` branch of real `AXPY(double,Vector,Vector)`. EXACT.
- `vector.cpp:715-723` — first complex `AXPY(double, ComplexVector, ComplexVector)` body (715-718) plus the second `AXPY(std::complex<double>, ...)` overload through its body line `y.AXPY(alpha, x);` (723); the closing brace of the second overload is at 724, so the range ends one line short of the full second body but does enclose both overload signatures + both delegating-call statements. The report's label "covers both overload bodies through the second `y.AXPY(alpha, x);`" is faithful. PASS.
- `vector.cpp:739-743` — `AXPBY(double alpha, const ComplexVector &x, double beta, ComplexVector &y)` body `{ y.AXPBY(alpha, x, beta); }`, the real-x→ComplexVector AXPBY overload. EXACT; matches the report's accurate frontmatter-comment label.
- `vector.cpp:745-758` — the real-real `AXPBYPCZ(double,Vector,double,Vector,double,Vector)` free-function body including the `if (gamma == 0.0)` branch. EXACT. The report correctly flags that this is the AXPBYPCZ real-real body (NOT an AXPBY body), and that the in-frontmatter comment label is accurate even though the *body prose* mislabels it (see edge-label-fidelity).
- `vector.hpp:313-316` — `// Addition z = alpha*x + beta*y + gamma*z.` (313) + `template <typename VecType, typename ScalarType>` (314) + `void AXPBYPCZ(...)` decl (315-316). EXACT.
- Also confirmed `vector.hpp:116-117` (ComplexVector::AXPY decl + Add alias), `vector.cpp:749-751` (γ==0 fast-path `add(alpha,x,beta,y,z)`), `vector.cpp:755-756` (γ≠0 slow-path `AXPBY(...); z.Add(...)`). All EXACT.
The lint reports `unresolved_depends_on_targets: 0` with the frontmatter applied, so every `cites-evidence` target is well-formed. PASS.

**surface-or-evidence — pass.** Frontmatter-only typing of an existing firm lowering theme — no surface (chapter body) is modified, and the report is explicit that it is hygiene, not a refinement. This is the typed-edge-backfill shape; the `cites-evidence` L0 ranges ARE the evidence backing the `firm` rank. No record is named in a signature here (the themes already carry their L1/L0 forms in the body). Not a refinement-shaped proposal. PASS.

**rotation-quality — pass (not applicable).** No new algebraic/structural rotation is asserted; the rotation content lives in the pre-existing theme bodies, untouched. This dispatch only types the edges. No-op.

**variant-axis-coverage — pass (not applicable).** No variant-axis claims are made or scoped by a frontmatter-typing dispatch. The complex/real AXPY/AXPBY overload variants are catalogued in the body, out of this scope. No-op.

**cross-reference-integrity — pass.** All four `reference` slug targets resolve on disk: `book/src/L1/axpy.md`, `book/src/L1/axpby.md`, `book/src/L1/axpbypcz.md` all exist. All `cites-evidence` targets resolve (lint `unresolved_depends_on_targets: 0`). The `reference`-edge justification (which L1 parents each theme body cross-links) is accurate: I confirmed `L1/axpby` + `L1/axpy` appear in the axpby theme body and `L1/axpbypcz` is the axpbypcz theme's primary parent. PASS.

**edge-label-fidelity — pass (both judgment calls verified correct).**
- The DECLINED `L1-L0/dot-mutation-rotation` reference: I grepped both theme bodies for `dot-mutation` and got zero hits, exactly as the report states. Declining to manufacture an edge the chapter does not carry is the correct don't-manufacture discipline. CORRECT.
- The FLAGGED body-prose mislabel at `axpby-mutation-rotation.md:25-26`: verified on disk — the body prose reads "Palace's L0 `AXPBYPCZ(...)` ... (member form at `vector.cpp:739-743`, free-function template at `vector.cpp:745-758`)". On disk, `739-743` is the `AXPBY(double, const ComplexVector&, ...)` overload (an AXPBY, NOT an AXPBYPCZ member), and `745-758` is the AXPBYPCZ real-real free-function body. So the body genuinely mislabels `739-743` as an "AXPBYPCZ member form". The report flagged it as out-of-scope (frontmatter-only) and deferred to a future body pass rather than silently editing — correct deferral, and the frontmatter comments themselves use accurate labels. CORRECT.

**plan-kind-consistency — pass.** The content shape (typed `edges:` frontmatter, `rank: firm`, `cites-evidence` depends-on + `reference` see-also) matches the declared graded-stack scheme-hygiene kind. No rough-in placeholders in a firm-claimed block. PASS.

**skill-uptake-survey — pass (telemetry).** No graded-stack-typing skill is referenced; the report does its own on-disk citation verification and isolated lint diff by hand. This shape (per-theme typed-edge backfill + isolated reachability diff) recurs across the typing campaign and may warrant a skill, but this is surfacing telemetry, not a blocker. PASS.

**rank-invariant — pass.** `rank: firm` is well-founded: both themes are firm lowering homes for firm L1 ops, and their blocking `depends-on` edges are all `cites-evidence` to rank-terminal POSITIVE L0 source (L0 ranges have no further deps, so they do not violate `rank(u) ≤ rank(v)`). The `reference` edges to the L1 parents constrain nothing (navigational). I confirmed all three L1 parents (`L1/axpy`, `L1/axpby`, `L1/axpbypcz`) carry `rank: firm`. The lint reports `rank_violations: 0` both before and after applying the frontmatter. HELD 0. PASS.

**reachability — pass (independently reproduced).** I reproduced the isolated-effect claim against a TRULY CLEAN tree (the report's "before" baseline). Clean baseline: reachable 119, detritus 140, untyped 60, rank_violations 0. After applying both proposed frontmatter blocks: reachable 119, detritus 140, untyped 60, rank_violations 0 — every metric HELD, and a detritus set-diff (`comm`) showed ZERO nodes entering or leaving detritus. This confirms the report's reachability-neutral claim exactly. The clean-baseline `inbound_reference_report` already lists `L1-L0/axpby-mutation-rotation <- [L1/axpby, L1/axpy]` and `L1-L0/axpbypcz-mutation-rotation <- [L1/axpbypcz]`, and neither theme is in the clean-baseline detritus list — so both were ALREADY reachable via legacy inbound edges before this typing, confirming "hygiene, not a flip." The report's D1-attribution note (very-first 122 baseline vs current 119 baseline = D1's effect, not mine) is consistent with what I observed: a transient presence of D1's orthogonalize edits in the working tree raised the baseline to 122/137; with that confound removed the clean baseline is 119/140 and my isolated effect is HELD. The tree was left clean after my reproduction (`git status book/` clean). PASS.

### Issues found

No blocking issues. All 10 checks pass. Two non-blocking notes, both already correctly identified and handled by the report itself (recorded here for the integrator's awareness, NOT as new findings against this dispatch):

1. **Pre-existing body-prose mislabel (out of this dispatch's scope), `axpby-mutation-rotation.md:25-26`** — the body prose labels `vector.cpp:739-743` as an "AXPBYPCZ member form"; on disk that range is the `AXPBY(double, const ComplexVector&, double, ComplexVector&)` overload, not an AXPBYPCZ member. The report flagged this and correctly deferred it to a future harvester/lowering-verifier body pass (it is a body-content accuracy issue, not a frontmatter-typing issue). The frontmatter comments authored by this dispatch use the accurate labels. Carry-forward candidate for an Open question / body-pass, not a defect of this report.

2. **`vector.cpp:715-723` ends one line short of the second complex-AXPY overload's closing brace (`}` at 724)** — the range encloses both overload signatures and both delegating-call statements (the semantically load-bearing content) but stops at line 723. This is a benign off-by-one at the trailing brace, faithful to the report's own description, and does not affect the claim. Noted for completeness only; not a `warning`.
