---
verifies: ../REPORT.md
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

# META: verification of REPORT: Formalize axpbypcz at L1

## Critique

### Checks run

- **citation-validity**: All cited ranges verified by direct read of `reference/palace/palace/linalg/vector.cpp:745-772` and `vector.hpp:131-136, 313-316`. Real-real specialisation at 745-758 (with γ==0 fast-path `add(α,x,β,y,z)` and slow-path `AXPBY(α,x,γ,z); z.Add(β,y)`), complex-complex at 760-765, and real-scalar-on-complex-vector at 767-772 all match the report exactly. Member decl at hpp:133-136 and free-function decl at hpp:313-316 also match. The user's framing "vector.hpp:131-133" appears off by two lines versus the report's 133-136, but the report's range is correct against the source. Pass.

- **surface-or-evidence**: New-operator landing (not refinement) — three proposed-changes blocks add a fresh L1/axpbypcz.md, an append-after row in L1/index.md, and an append-after line in SUMMARY.md. Surface present and evidence direct. Pass.

- **rotation-quality**: Not applicable to a same-layer L1 harvester; the report is the L1 algebraic form of fused AXPBYPCZ, not an L_{n+1}→L_n rotation claim. Pass (n/a to operator-firmup shape).

- **variant-axis-coverage**: Two axes documented (element-type real|complex; scalar-promotion sub-axis on complex). γ==0 internal branch correctly classified as L0 control-flow, not an L1 variant axis. Consistent with axpby precedent. Pass.

- **cross-reference-integrity**: `book/src/L1/axpby.md` exists and itself forward-references `axpbypcz` (line 76, 103-105) — the subsumption chain `axpy ≺ axpby ≺ axpbypcz` is coherent across landed entries. `axpy.md` exists. `scaffolding/decisions/axpby-as-primitive.md` reference path resolves. Forward references to L1-L0/axpbypcz-mutation-rotation.md are flagged as "forthcoming" — acceptable. Pass.

- **edge-label-fidelity**: No L_{n+1}→L_n edge label is carried by this report (firm L1 operator, no lowering theme authored). Pass (n/a).

- **plan-kind-consistency**: Declared as `firm` L1 operator. Content matches: signature canonical, laws fully written, evidence direct, status section affirms `firm`. No rough-in placeholders. Pass.

- **skill-uptake-survey**: Three relevant skills surveyed in front-matter (`verify-citation-range`, `classify-variant-axis`, `verify-refinement-surface`) with explicit decisions/rationales. Telemetry present. Pass.

### Issues found

- **Law 5 is purely a forward-pointer to Law 1**, not an independent law statement — counted in the "twelve laws" but contains no new content beyond restating γ=0 subsumption. Severity: low (numbering inflation, not error). Location: REPORT.md § Algebraic laws, Law 5.

- **Law 2 derivation chain is slightly indirect**: subsumption of axpy is stated as "composition of law 1 (γ=0 → axpby) and the axpby Law #1 (β=1 → axpy)". The composition is correct mathematically but introduces a cross-document dependency for verification; a direct statement `axpbypcz(α, x, 1, y, 0, z) = α·x + y = axpy(α, x, y)` would be self-contained. Severity: low.

- **Law 11 (Scalar absorption)** is weaker than axpby Law #8: the axpby version explicitly notes invertibility (`γ⁻¹·y` requires invertible γ); Law 11 omits the invertibility caveat for the second-form symmetric statement, though the way it is written ("each scalar absorbs into its paired vector") only states the forward absorption direction, which does not require invertibility. Severity: very low (defensible as stated, but cycle-003 axpby precedent was more explicit).

- **Open question 1 promises an L1>L0 lowering theme** with a γ==0 algebraic-sub-rule analogous to `axpy`'s `α == 1.0` sub-rule, but the axpby entry (line 85) explicitly states `axpby` has *no* such sub-rule. The `axpbypcz` lowering will therefore be the first in the L1>L0 corpus to mix structural-rebind with algebraic-constant-folding — an architectural observation worth flagging for the abstractor, but not currently surfaced beyond the parenthetical in §1. Severity: low (informational; not blocking).

- **L1 dep-map row count claim "after this report lands, the L1 dep-map has five firm operators"** — verified against current `book/src/L1/`: `axpy.md`, `dot.md`, `nrm2.md`, `axpby.md` are present (4); axpbypcz lands as 5. Correct. (No issue — flagging as confirmed.)

- **The note "the γ ≠ 0 slow-path uses a two-call split ... which computes the sum in a *different* order than the fused form would"** (under non-laws, IEEE-754) implicitly asserts the two L0 branches produce bit-different output for nonzero γ across the path-discontinuity at γ→0. This is plausible but uncited — there is no Palace comment or test confirming the branches were intended to be bit-divergent. Severity: low (the claim is hedged with "may differ", but the surrounding prose treats it as an established fact about Palace).
