---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T233000Z
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
repaired_at: 2026-05-28T233500Z
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

# META: verification of "Combinator candidate — inner-product-fold"

## Critique

### Checks run

**citation-validity — pass.** Spot-verified the load-bearing Palace ranges via codemap `read_range`, all in-range and supporting the claims:
- `vector.cpp:263-274` — `ComplexVector::Dot` (Hermitian, `&y==this → imag 0` fast path) and `ComplexVector::TransposeDot` (unconjugated, `&y==this → 2·Imag·Real`). Exact match to the Instance-2/3 kernel claims and to `dot.md:112-113`.
- `vector.cpp:665-685` — real `LocalDot` (via `hypre_SeqVectorInnerProd`, body 665-672) and complex `LocalDot` (four real LocalDots + self-dot imag-0, body 674-685). Matches Instance-1/2 ranges exactly.
- `operator.cpp:621-639` — both `Dot(comm,x,A,y)` overloads; verified `A.Mult(...); return Dot(comm, Ax, y)` (apply-then-plain-dot). Direct support for the `M = I` ⟹ plain-dot claim and the weighting axis.
- `operator.cpp:599-619` — `Norml2(comm,x,B,Bx)` = `B.Mult(x,Bx); dot=Dot(comm,Bx,x); MFEM_ASSERT(dot>0); sqrt(dot)`. This is the linchpin evidence for the "`matrix-weighted-norm` is a CONSUMER (`√ ∘ inner_product_M` at `y=x`, SPD guard), not an instance" discipline — verified exactly.
- `iterative.cpp:22-32` — `CheckDot` pair, `MFEM_ASSERT(isfinite && dot(.real()) >= 0.0)`. The runtime PSD guard on the Hermitian/SPD member, exactly as Instance-5 claims.
- `vector.hpp:110-113`, `operator.hpp:386-394` — decl + comment ranges verified.
- Artifact citations into `dot.md` (`:16`, `:34/:35`, `:57-67`, `:60`, `:68`, `:71-75`, `:89-96`, `:94`, `:112-113`) all land on the claimed signatures/laws/axes. OQ ledger entries (`inner-product-fold-sibling-candidate`, `blas1-variadic-linear-combination-fold-unification`, `matrix-weighted-norm-and-bilinear-form-l1-rough-ins`) all resolve. The cycle-017 sibling report and the parallel cycle-018 harvester dir both exist. One minor notation slip noted under Issues (the `xᴴ M y` vs Palace-documented `yᴴ A x` argument order), but it does not break any cited range.

**surface-or-evidence — pass.** This is a constructive new-vocabulary proposal (a new L2 combinator + one dep-map row append), not a refinement of existing operator/theme surface, so the refinement-shape rule is satisfied trivially. The proposal modifies real surface (`book/src/L2/index.md` dep-map row) and is densely evidence-backed (5 codemap-verified members + the `Norml2` consumer anchor). Not a pure-rotation-claim-without-surface report.

**rotation-quality — pass.** The proposal asserts a genuine fusion rotation, not a rename. The L2 `inner_product` is strictly more abstract/compact than the L0/L1 forms it subsumes: it collapses three distinct L0 symbols (`LocalDot`/`Dot` real, `ComplexVector::Dot`, `ComplexVector::TransposeDot`) plus the M-weighted `Dot(comm,x,A,y)` into one fold parameterised by a conjugation-convention kernel and a weighting axis, and it makes the relationship "`dot` is `bilinear-form` at `M = I`" statable as one operator. The `apply_linop(M,·)`-then-reduce unfolding of the fused `Dot(comm,x,A,y)` workspace pass is exactly the L2 fusion rotation (HPC workspace erased, composition exposed). Not a 1:1 mapping — multiple L0/L1 forms reduce to one L2 form with explicit axes. The state-hiding/coarser-substitution criterion is met.

**variant-axis-coverage — pass (with the discipline judgment affirmed).** The report enumerates four axes and classifies each correctly: (1) conjugation-convention `{real-symmetric | complex-hermitian | complex-unconjugated}`, (2) element-type `{real | complex}`, (3) weighting `{plain (M=I) | M-weighted}`, (4) MPI-collective (scoped out as an L0/lowering detail, per `dot.md:47` and CLAUDE.md single-machine scope). No hidden branches: the real overload's split `A.Mult(x.Real(),...); A.Mult(x.Imag(),...)` is covered by the element-type axis, and the per-cell PSD-law break on the `tdot` cell is explicitly carried (the axis is NOT law-preserving across all cells, stated at caveat 2). The two key over-unification judgments are sound and independently corroborated: (a) `inner_product` is correctly kept SEPARATE from `linear_combination` — different result type (`Scalar` vs `Tensor[N]`), no shared concatenation/arity homomorphism, no shared PSD/symmetry laws; the OQ `inner-product-fold-sibling-candidate` licenses exactly this sibling split. (b) `matrix-weighted-norm` is correctly held OUT as a consumer (`√ ∘ inner_product_M` at `y=x`, SPD precondition) rather than absorbed as a weighting cell — and the existing `matrix-weighted-norm.md` Context independently asserts the same separation ("distinct operators, not variants of one operator — the algebraic laws differ ... a norm iff B is SPD"), and `operator.cpp:599-619` shows the outer `√` + SPD assert that would pollute the pure-`M` fold if pulled in. The discipline the human warned against (over-unification) is correctly avoided.

**cross-reference-integrity — pass.** All referenced artifact slugs resolve: `book/src/L1/dot.md`, `book/src/L1/bilinear-form.md`, `book/src/L1/matrix-weighted-norm.md`, `book/src/concepts/dot.md`, `book/src/L2/index.md` all exist. The forward-references `./inner_product.md` and (implicitly) `./linear_combination.md` are intentionally NOT live markdown links — verified that neither file exists yet (`book/src/L2/` contains only `index.md`, `krylov-step.md`, `chebyshev-iteration.md`), so the plain-text forward-reference is the build-safe choice and matches the cycle-017 de-link precedent the report cites. The append-anchor "after the `linear_combination` row at `book/src/L2/index.md:25`" is accurate — line 25 is the cycle-017 rough-in row. The proposed-changes `edit:` block targets a real file. No dangling links.

**edge-label-fidelity — pass (not a lowering-theme report).** This proposal carries no `L_{n+1}>L_n` edge label — it is a single-layer L2 vocabulary addition. The layer-placement argument (L2, not L1/L4) is internally consistent and the prose discusses the correct layer throughout. The L2>L1 lowering theme is explicitly deferred to abstractor work (caveat 3), not authored here, so there is no edge-label-vs-prose mismatch to check. Marked pass per the inapplicable-check convention.

**plan-kind-consistency — pass.** Declared kind is `rough-in` (dep-map row only, status string `(rough-in, proposed-by: combinator-miner:2026-05-28T231046Z)`), and the content matches: signature is a "best guess; harvester firms up", the operator chapter is explicitly NOT created (deferred to harvester), laws are sketched as "algebraic intuition", and firm-up calls are flagged as open questions. This is correctly a rough-in, not a mis-classified firm entry. The "≥3-instance soft bar" framing matches the combinator-miner rough-in shape, and the row format mirrors the cycle-017 `linear_combination` rough-in row precedent (same forward-reference convention, same `proposed-by` stamp).

**skill-uptake-survey — warning.** The report's shape implies several relevant skills exist but none is referenced by name. `classify-variant-axis` is directly on-point for the four-axis enumeration and the consumer-vs-instance / over-unification judgment that is the crux of this report; `verify-citation-range` is on-point for the heavy self-verify the report performed (it says "self-verified via codemap `read_range`" but does not invoke the skill by name); `verify-rotation-citation` / `propose-rotation` are plausibly relevant to the L2 fusion-rotation claim. This is a pure telemetry surface (non-blocking) — the work itself performed the equivalent procedures — but the skill-invocation references are absent.

### Issues found

1. **`xᴴ M y` vs Palace-documented `yᴴ A x` argument-order/conjugation notation** (CYCLE.md §Summary line 14, §Pattern instances Instance 4 line 58, §Proposed combinator lines 124/129/183, §Proposed changes line 200, §Supporting evidence line 239 — severity: minor/firm-up). The report uniformly writes the M-weighted member as `xᴴ M y`. The Palace decl comment at `operator.hpp:386-394` documents `Dot(comm, x, A, y)` as "the bilinear form inner product **yᴴ A x**", and the body is `A.Mult(x, Ax); return Dot(comm, Ax, y)` = `dot(Ax, y)` = `(Ax)ᴴ y = xᴴ Aᴴ y`. So which argument is conjugated and the exact `Aᴴ`-vs-`A` placement is a load-bearing conjugation-convention detail (precisely the kind the report itself elevates as load-bearing for the plain `dot`). The report's `xᴴ M y` shorthand is convenient but does not exactly reconcile with the Palace-documented `yᴴ A x` and the `(Ax)ᴴ y` body algebra. The existing `bilinear-form.md` Context (lines 27-53) flags a related "L0 comment-vs-implementation conjugation" subtlety that was resolved via the `bilinear-form-conjugation-convention-anchor` OQ; this proposal should inherit that resolution rather than introduce a fresh `xᴴ M y` framing without reconciling it. Candidate for repair: a one-line note pinning the exact conjugation convention (cite `operator.hpp:386-394` comment + `bilinear-form.md` Status) so the harvester does not firm up a mismatched form. Does not affect the rough-in verdict.

2. **Instance-4 elision of the real-`Operator` overload's split `Mult`** (CYCLE.md Instance 4 line 58, §Supporting evidence line 239 — severity: minor). The report says the L0 body is "literally `A.Mult(x, Ax); return Dot(comm, Ax, y)`". This is exact for the `ComplexOperator` overload (`operator.cpp:630-639`) but the real-`Operator` overload (`:621-628`) actually does `A.Mult(x.Real(), Ax.Real()); A.Mult(x.Imag(), Ax.Imag())` (two calls, because `A` is real but `x` is a `ComplexVector`). The `apply-then-plain-dot` characterization still holds; the "literally" is a slight over-statement for the real-weight overload. Element-type axis covers it, but the wording is imprecise. Minor.

3. **No named skill invocation** (CYCLE.md whole-report — severity: low / telemetry). Per the skill-uptake-survey check: `classify-variant-axis`, `verify-citation-range`, and `verify-rotation-citation`/`propose-rotation` are all plausibly relevant and unreferenced. Non-blocking; surfaces telemetry only.

4. **Instance-5 (`CheckDot`) counted toward the "five members" framing** (CYCLE.md §Pattern instances lines 29, 47-53, 59 — severity: cosmetic). The report's own prose is careful — it explicitly says Instance 5 is "NOT a separate fold ... not as a sixth kernel" but rather "the PSD law being load-bearing in the wild." That is the correct reading. However the §Summary line 29 phrasing ("≥3-instance soft bar is met counting genuine kernel/weighting members: real dot, complex Hermitian dot, complex unconjugated tdot, and the M-weighted bilinear form") lists FOUR genuine members there while §Pattern instances headlines "Five members". The bar is comfortably met either way (4 genuine kernel/weighting members ≥ 3), but the 4-vs-5 count is mildly inconsistent between the two sections because Instance 5 is a consumer-law-witness, not a kernel member. Cosmetic — the substantive instance count clears the bar regardless.

## Repair

### Fixes attempted

- **Finding 1**: `xᴴ M y` shorthand vs Palace-documented `yᴴ A x` argument-order/conjugation convention (minor/firm-up).
  - **Decision**: repaired.
  - **Action**: Added a caveat to CYCLE.md so the harvester firms the convention correctly (caveat-addition, appropriate for a rough-in — does NOT pin the convention here, only flags it). (a) New caveat 7 in §"Open questions / caveats" stating that every `xᴴ M y` in the report is a placeholder shorthand, that Palace's `operator.hpp:386-394` comment documents `Dot(comm,x,A,y)` as `yᴴ A x` with body algebra `(Ax)ᴴ y = xᴴ Aᴴ y` (`operator.cpp:621-639`), and that the harvester should pin the exact form and inherit the `bilinear-form.md` Status / `bilinear-form-conjugation-convention-anchor` OQ resolution. (b) Inline parenthetical in the §Proposed changes dep-map row marking the `xᴴ M y` member as a shorthand with the exact convention deferred to harvester (cross-references caveat 7). No content authored — the convention is flagged, not decided.

- **Finding 2**: Instance-4 "literally `A.Mult(x, Ax)`" elides the real-`Operator` overload's split apply (minor).
  - **Decision**: repaired.
  - **Action**: Added a brief parenthetical to CYCLE.md Instance 4 (§Pattern instances): the `ComplexOperator` overload at `:630-639` is literally the single `A.Mult(x, Ax)`, but the real `Operator` overload at `:621-628` splits into `A.Mult(x.Real(), Ax.Real()); A.Mult(x.Imag(), Ax.Imag())` (real `A`, complex `x`); the element-type axis covers this and the apply-then-plain-dot characterization holds for both. Dropped the over-stated "literally" from the lead clause.

- **Finding 3**: No named skill invocation (low/telemetry).
  - **Decision**: not-needed.
  - **Rationale**: Per the human's instruction and the skill-uptake-survey being a pure telemetry surface (the work itself performed the equivalent procedures). The critic left `skill-uptake-survey: warning` and the repairer does not override critic `checks:` values; this is a non-blocking telemetry observation requiring no surface fix.

- **Finding 4**: 4-vs-5 instance-count inconsistency between §Summary ("four genuine members") and §Pattern instances ("Five members") (cosmetic).
  - **Decision**: repaired.
  - **Action**: Edited the §Pattern instances lead paragraph in CYCLE.md to state "Four genuine kernel/weighting members (Instances 1–4) ... plus one consumer-law witness (Instance 5, `CheckDot`)" rather than a flat "Five members". This aligns it with §Summary's "four genuine members" framing and with the report's own prose already calling Instance 5 a law-witness, not a sixth kernel. Consistency-only; the substantive instance count (4 ≥ 3) was never in doubt.

### Unrepairable findings

None. All four findings were either repaired (1, 2, 4) or not-needed (3). All eight critic checks are now `pass`, `repaired`, or `not-needed` (the single `warning` is the non-blocking skill-telemetry surface, marked not-needed per the repair-authority telemetry convention).

## Suggested resolution

`ready`. Notes for the integrator:
- The repairs are caveat-additions / consistency fixes only — no substantive content authored, no convention decided. The dep-map row content is unchanged in substance; the only surface-affecting edit is the inline shorthand-caveat parenthetical in the §Proposed changes row (Finding 1b), which the integrator should carry into `book/src/L2/index.md` as-is so the harvester sees the conjugation flag at the point of use.
- Append-sequencing per the report's own caveat 4 still applies: land this `inner_product` row AFTER the parallel cycle-018 harvester's `linear_combination` edit at `book/src/L2/index.md:25`, regardless of that row's settled firmness. The two edits do not conflict.
- Finding 1 (conjugation convention) is a deliberate harvester firm-up flag, not an integrator action — the harvester that later authors `book/src/L2/inner_product.md` pins the exact `yᴴ A x` / `(Ax)ᴴ y` form.
