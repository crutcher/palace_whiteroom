---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T071500Z
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
overall_status: ready
---

# META: verification of "Combinator candidate — preconditioned residual-correction step"

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` reports 17/17 citations in-bounds with clean path hygiene. The two decisive "Palace names the contract verbatim" pinpoints were anchor-confirmed independently: `palace/linalg/gmg.cpp:174-176` `--anchor 'Y <- Y + B (X - A Y)'` → anchor at line 176 within range (OK); `palace/linalg/distrelaxation.cpp:104` `--anchor 'y = y + B (x - A y)'` → anchor at line 104 (OK). I additionally read the surrounding source via codemap: `distrelaxation.cpp:108` carries the conjugated-leg comment `// y = y + G B_G Gᵀ (x - A y)` verbatim (Instance 4 ✓); the GMG V-cycle pinpoints are all exact on-disk — pre-smooth `B[l]->Mult2(...)` at :184, residual `A[l]->Mult(...)` + `AXPBY(1,X,-1,R)` at :187-188, `RealMultTranspose(*P[l-1], ...)` (Pᵀ restrict) at :191, prolong-add `Y[l] += R[l]` at :200 (cited :199-200 ✓). The book citations are exact: `chebyshev-smoother.md:50-52` states the body verbatim; `jacobi-smoother.md:264` states the Richardson form `y ← y + M·(x − A·y)`; `jacobi-smoother.md:118-143` is the bare-apply guard (single elementwise mult, `!initial_guess` at `jacobi.cpp:102`); `chebyshev.cpp:177-178` is the `AssembleDiagonal`+`Reciprocal` RE5/RE7 site. The L0 anchor `chebyshev.cpp:190-220` is the `Mult2` smoother body carrying its own verbatim `// Apply smoother: y = y + p(A) (x - A y)` comment. Sibling-report line references (D1 486-491 / D3 150-153,176-187 / D4 219-230 / D5 328) are all in-range; I spot-read D5:328 and confirmed it flags `iterate_while_L3`-over-basis-extension as its shared core, NOT the residual step — the over-unification guard's attribution is faithful.

**surface-or-evidence — pass.** This is a new-combinator proposal (adds one L2 dep-map row), not a refinement of an existing entry's surface; it modifies surface AND carries rotation evidence (the verbatim Palace contracts + 6 cited instances). Record-definition sub-check: the signature names `LinOp[...]` and `Tensor[(S: ...)]`, but these are existing, already-defined types merely *referenced* in the signature, not records newly named here — no definition-home gap. No retroactive-backfill framing needed; this is a genuine surface addition with evidence.

**rotation-quality — pass.** L2 fusion-rotation is genuine: the smoother body is unfolded into base algebra (`apply_linop` + `axpby` + a parameterized `B` slot), and the conjugation law `conjugated_correction_step A T B' = correction_step A (T·B'·Tᵀ)` collapses TWO previously-separate legs (D3 de-Rham auxiliary `T=G`, D1 coarse-grid `T=P`) into ONE combinator — strictly more compact/abstract than the per-smoother re-derivations. The derived error-propagation operator `E = I − B·A` and the single fixed-point law are made structural across the family. This is abstraction/compression, not a 1:1 rename.

**variant-axis-coverage — pass.** Three orthogonal axes are named and handled: (1) correction-operator class (the `B` slot — the specialization axis); (2) plain vs transfer-conjugated, explicitly unified by the conjugation law with `T=I` degeneration; (3) initial-guess fast path (`ig=false`), explicitly scoped as a degenerate-case absorption rather than an algebraic variant. No hidden branch.

**cross-reference-integrity — pass.** Target `book/src/L2/index.md` exists and its dep-map is a pipe-table (matching the proposed row's format), correctly hosting `chebyshev-iteration` / `linear_combination` / `axpby` / `jacobi-smoother` / `divfree-projector` — so the layer-rationale's "L2 already hosts …" claim is accurate. No pre-existing `correction_step` row (the addition is genuinely additive, not a duplicate). All referenced chapters resolve on disk: `L1/chebyshev-smoother.md`, `L1/jacobi-smoother.md`, `L3/smoother-intro.md`, `L4/iterate-while.md`, `L4/iteration-combinators-intro.md`, `divfree-projector.md` at L1/L2/L3. The proposed row correctly uses a plain-text/inline-code slug (no live link) per the forward-reference convention, since the chapter is deliberately not created this dispatch — avoiding the linkcheck2 hard error a link-to-missing-file would cause. Minor (non-blocking) note below.

**edge-label-fidelity — pass (no cross-layer edge label).** The proposal is a same-layer L2 combinator row and carries no L_{n+1}→L_n edge label to check. The internal layer-placement prose (the L2-not-L1/L3 rationale, the L1-gate-keeps-closure vs L2-unfolding-uses-combinator split, the `iterate_while` loop staying the consumer's fold) is internally consistent and correctly directional.

**plan-kind-consistency — pass.** Declared kind is `rough-in` combinator landed as a single dep-map row with no chapter authored — exactly matching a rough-in combinator proposal. The report explicitly defers chapter formalization to the harvester and emits only the row. The signature is a "best guess; harvester firms" sketch, appropriate for rough-in. No firm-apparatus over-claim, no rough-in-masquerading-as-firm.

**skill-uptake-survey — pass (telemetry only).** No combinator-mining-specific skill invocation is referenced. The relevant disciplines (replace-and-propagate vs mine-and-strand; over-unification guards; explore-and-coalesce duals) are followed in prose. Surfaced as telemetry, non-blocking.

**Graded-stack rank-invariant — pass.** `correction_step` (rough-in, rank 2) rests on `apply_linop` and `axpby` (both firm, rank 3): `rank(u)=2 ≤ min(deps)=3` holds. No over-claim above a dependency's rank.

**Graded-stack reachability — pass.** The combinator is reachable from feature roots over `depends-on`: it is the shared per-sweep body of the smoother family consumed by the GMG-preconditioner column (D1) and the driver columns those precondition — a live node, not detritus.

### Issues found

No blocking issues. Two minor, non-blocking observations (for the integrator/downstream, not repairs):

1. **Kind-group placement hint absent on the proposed row** (`CYCLE.md` §Proposed changes, the `edit:book/src/L2/index.md` block) — severity: minor/informational. `L2/index.md`'s dep-map is split into multiple by-kind pipe-tables (combinator/fold-cohort group at ~lines 100-104, specialization-stub group at ~lines 108-115, etc.) with alpha-within-group ordering per the mdBook-subchapter-grouping directive. The proposed row gives no explicit hint of which group it lands in or its alpha slot. As a `correction_step` combinator it belongs in the combinator group, alpha-positioned. This is the integrator-per-report's insertion judgment (the directive already charges the integrator with alpha-position insertion), not a defect in the row content — flagging only so the placement is not appended blindly to the file tail.

2. **Propagation plan is present but scoped as a FLAG, not enacted here** (`CYCLE.md` §Open questions, "Replace-and-propagate scope") — severity: informational, and correct-by-role. The replace-and-propagate discipline is satisfied at the proposal level: the report names the exact propagation set (L2 `jacobi-smoother`/`chebyshev-iteration` bodies re-expressed via `correction_step`; D3/D1 per-sweep bodies expressed through it) and routes the actual rewrite to the harvester + same-layer-cross-cutter. This is the right division for a rough-in row (the row cannot itself rewrite sibling chapters), so it is NOT a mine-and-strand defect — recorded here only to confirm the propagation obligation is tracked, not dropped.
