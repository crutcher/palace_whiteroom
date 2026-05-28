---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T231500Z
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
---

# META: verification of combinator candidate — linear-combination-fold

## Critique

### Checks run

**citation-validity — pass.** Spot-verified 12 of the cited ranges against `reference/palace/` via codemap `read_range`/`search_text`. All exact:
- `vector.cpp:745-758` AXPBYPCZ real-real — confirmed `if (gamma == 0.0) { add(alpha, x, beta, y, z); } else { AXPBY(alpha, x, gamma, z); z.Add(beta, y); }`. The proposal's load-bearing claim — that the `γ==0` branch at `:749-751` is the in-source arity-collapse and the exact algebraic content of the zero-coefficient term-drop law — is faithful to the source.
- `vector.cpp:702-712` AXPY with `if (alpha == 1.0) y += x; else y.Add(alpha, x)` — confirmed; the α==1 fast path is real.
- `vector.cpp:203-227` `ComplexVector::operator*=` with `si == 0.0` real fast-path — confirmed (the `scal` L0 home, member-only).
- `vector.hpp:305-316` AXPY/AXPBY/AXPBYPCZ free-function template decls with comments `y += alpha * x` / `y = alpha * x + beta * y` / `z = alpha * x + beta * y + gamma * z` — confirmed verbatim.
- Live call sites: `nleps.cpp:343-344` (γ=1 fold-into-output, `z.Real()`/`z.Imag()`), `romoperator.cpp:188-189` (γ=1 ROM reconstruction), `timeoperator.cpp:217` (γ=0 collapse, `k2 = rhs2 + dt k1`) — all confirmed exactly as quoted.
- `search_text linalg::(Scal|Scale)\b` → zero hits — confirmed, grounding the member-only-`scal` claim and scal.md:7's "notable absence."
- `iterative.cpp:632` `w *= 1.0 / Hj[j+1]` (GMRES arity-1) and `operator.cpp:458-466` SumOperator `y.Add(a*c, z)` (arity-2 accumulation) — confirmed.
Artifact citations all resolve: the four L1 leaves (`scal/axpy/axpby/axpbypcz.md`), `dot.md`, `concepts/scalar-promotion.md`, `decisions/axpby-as-primitive.md`, `book/src/L2/index.md`, and OQ `blas1-variadic-linear-combination-fold-unification` (slug at line 2937, range 2937-2946 as cited). The decision-file `:49-52` "What would change the decision" range was read and confirms the proposal's read — that section governs L1 leaf-vs-decompose only and does not preclude an L2 fold. The axpby.md/axpbypcz.md law-line anchors the algebraic generalizations lean on (distribution, scalar absorption, the floating-point non-law) were read and match.

**surface-or-evidence — pass.** This is a new-combinator proposal (not a refinement of an existing operator/theme), so the refinement-surface rule applies in its constructive sense: the proposal modifies surface (adds a dep-map row to `book/src/L2/index.md`) AND carries evidence (the parametric-arity family with both the four operator-definition instances and ≥6 live L0 call sites). It is not a pure rotation_claim without surface. Well clear of the bar.

**rotation-quality — pass.** The rotation is genuine: the variadic `linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]` is strictly more compact and more abstract than the four fixed-arity L0/L1 symbols — it is a one-form fold subsuming `scal`/`axpy`/`axpby`/`axpbypcz` along the arity axis, not a 1:1 rename. The concatenation-homomorphism law `lc(a ++ b) = lc a + lc b` is sound (it is the standard fold/monoid-homomorphism over the additive monoid of `Tensor[N]`; the `axpbypcz` 3-term list = `axpby` 2-term ++ `scal` 1-term decomposition is correct, and it generalizes axpby.md laws 6-9 / axpbypcz.md laws 7-11, which were read and match). The empty-list identity (`zeros`), multilinearity in the scalar list, scalar absorption, and zero-coefficient term-drop are all correct generalizations of the per-op laws. Permutation-invariance is handled correctly per the load-bearing-numerical-trick discipline: stated as an EXACT-ARITHMETIC law with the IEEE-754 non-associative-reduction caveat as an explicit paired non-law (matching axpby.md "Floating-point associativity" and axpbypcz.md's two-branch bit-mismatch note, both read and confirmed). The `foldl` left-to-right order is correctly named as the canonical L2 order with the pinned-L0-order reproduction deferred to the L2>L1 theme.

**variant-axis-coverage — pass.** The proposal enumerates three orthogonal axes (output-aliasing in-place-vs-out-of-place, element-type real|complex with the scalar-promotion sub-axis, fusion-order L0-detail) and correctly scopes each: aliasing and fusion-order are declared L2>L1/L1>L0 lowering concerns (not arity axes), element-type is inherited from `scalar-promotion` unchanged. The key axis-discipline point — that aliasing is orthogonal to arity (every arity has both an aliasing and a fresh-output form) — is correct and the γ=1 accumulate-into-output call sites are correctly identified as the aliasing case. No hidden branches: the `γ==0` vs `γ!=0` L0 control-flow is surfaced as the term-drop law + fusion-order axis, not buried.

**cross-reference-integrity — pass.** All `[link]` targets in the proposed dep-map row resolve or are correctly forward-referenced: `./linear_combination.md` does NOT yet exist, which is correct and intentional — the report explicitly states it does not create the operator file (harvester's job) and proposes only the dep-map row; the forward link is the same pattern the existing `krylov-step`/`chebyshev-iteration` rows use. All named slugs exist (`scal`, `axpy`, `axpby`, `axpbypcz`, `dot`, `scalar-promotion`). The insertion instruction ("after the `chebyshev-iteration` row at `book/src/L2/index.md:24`") is accurate — that row is at line 24 and the table ends there. The provenance-bullet companion correctly mirrors the krylov-step precedent at `:30-37`.

**edge-label-fidelity — pass (not applicable).** This is a combinator/operator proposal, not a lowering-theme proposal — it carries no `L_{n+1}>L_n` edge label. The report correctly defers the `L2-L1/linear-combination-fold-specialization` lowering theme to abstractor work (Open question 2) and does not author edge prose. No edge-label/prose mismatch possible.

**plan-kind-consistency — pass.** Declared kind is rough-in (`(rough-in, proposed-by: combinator-miner:2026-05-28T223022Z)`), and the content shape matches: a dep-map row only, signature explicitly flagged "best guess; harvester firms up," formalization (operator file, per-arity test-assertion empirical-match, L2>L1 theme) all deferred. No firm-grade claims are smuggled in under a rough-in label. The layer placement (L2, not L1/L4) is well-argued: (a) not-L1 because L1 must mirror Palace's distinct C++ symbols one-to-one for the L1>L0 mutation rotation (consistent with `axpby-as-primitive.md`, which I verified does not preclude an upward L2 fold); (b) is-L2 because L2 is the fusion-rotation layer whose charter (verified at `book/src/L2/index.md:3,9,17,28`) explicitly covers unfolding kernel-fusion choices and is "most populated by combinator-miner output"; (c) not-L4 because the fold is a pure value-producing reduction with no monadic state threading or convergence predicate (contrasted correctly with `iterate_while`). The layer argument is sound. The over-unification guard is also correct: `dot` is kept distinct (reduce-to-scalar inner product; result type `Scalar` not `Tensor[N]`; symmetry/Hermitian/PSD laws with no `linear_combination` analogue), framed as a separate future `inner_product` family along a conjugation-convention axis — the "algebra of folds, not one mega-combinator" nuance the OQ itself requested.

**skill-uptake-survey — warning.** The proposal's shape is exactly a parametric/variadic-family unification, and the OQ it enacts (prong a) calls for extending the `combinator-miner` spec with a "parametric/variadic-family detection mode" — i.e. the methodology has flagged that the existing `skill-selection` / combinator-mining procedure is arity-blind. The report works in an ad-hoc "explicit parametric-family mode" but references no skill invocation for the variant-axis classification (`classify-variant-axis` exists and would naturally apply to the three-axis enumeration) nor any rotation-citation skill (`verify-rotation-citation` / `propose-rotation` exist). This is a pure-presence telemetry warning, not a blocking finding: the variant-axis enumeration and rotation sketch are correct on their merits; the survey simply notes that relevant skills exist and were not cited as invoked. Surfaces telemetry for the batch-4 meta-phase's already-planned combinator-miner spec extension.

### Issues found

No blocking issues. The proposal is well-evidenced, correctly placed, and algebraically sound for a rough-in. Minor / telemetry items only:

1. **[telemetry, skill-uptake-survey] No skill invocation cited** — `reports/.../CYCLE.md` §"Variant axes" + §Proposed combinator. The three-axis enumeration and rotation sketch do not reference `classify-variant-axis` / `verify-rotation-citation` / `propose-rotation` despite their applicability. Non-blocking; correctness stands on its own. Relevant to the OQ's prong-(a) combinator-miner spec extension (batch-4 meta-phase).

2. **[minor, citation precision] `iterative.cpp:632, 811` and `nleps.cpp` extra sites under-verified** — §"Pattern instances (B)" and §"Supporting evidence." I verified `iterative.cpp:632` (GMRES normalize) but not `:811`; verified `nleps.cpp:343-344` but not the `:471,676,693` hits cited only as a search-text count. The verified subset already far exceeds the ≥3 instance bar across distinct arities (arity-1 iterative.cpp:632; arity-2 operator.cpp:458-466; arity-3 nleps.cpp:343-344, romoperator.cpp:188-189, timeoperator.cpp:217), so the evidentiary claim holds regardless; the unverified sites are corroborating, not load-bearing. Flagged for completeness only.

3. **[minor, deferred-by-design] test empirical-match not pulled** — §"Supporting evidence" + Open question 5. `test/unit/test-vector.cpp` per-arity value assertions are cited transitively via the L1 entries, not re-read; the concatenation law is therefore an algebraic claim, not yet an `empirical_match`. The report itself flags this as a harvester follow-up, consistent with the rough-in bar. Not an issue with this proposal; noted so the harvester does not lose the thread.

---
repaired_at: 2026-05-28T232500Z
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

## Repair

### Fixes attempted

The critic returned 7/8 `pass` and 1 `warning` (skill-uptake-survey), plus 3 non-blocking §Issues items. All flagged items are telemetry/informational; none triggers a mechanical fix within repair authority. No edits applied to CYCLE.md or supporting docs.

- **Finding**: [skill-uptake-survey — warning] The three-axis variant enumeration + rotation sketch reference no skill invocation (`classify-variant-axis` / `verify-rotation-citation` / `propose-rotation` exist and would apply).
  - **Decision**: not-needed
  - **Rationale**: Pure-presence telemetry. The critic explicitly states correctness stands on its own merits, and the survey only notes that relevant skills exist and were not cited as invoked. This is a methodology-level signal the critic routed to the batch-4 meta-phase (combinator-miner parametric/variadic-family spec extension per OQ `blas1-variadic-linear-combination-fold-unification` prong a). Out of repair scope (methodology-level concern); no surgical edit can or should manufacture a skill-invocation citation post-hoc.

- **Finding**: [§Issue 1 — telemetry, skill-uptake-survey] No skill invocation cited in §"Variant axes" / §Proposed combinator.
  - **Decision**: not-needed
  - **Rationale**: Duplicate framing of the skill-uptake-survey warning above. Same disposition — telemetry for the meta-phase, not a repairable defect.

- **Finding**: [§Issue 2 — minor, citation precision] Corroborating call sites `iterative.cpp:811` and the `nleps.cpp:471,676,693` search-text-count hits under-verified.
  - **Decision**: not-needed
  - **Rationale**: The critic confirms the verified subset (arity-1 `iterative.cpp:632`; arity-2 `operator.cpp:458-466`; arity-3 `nleps.cpp:343-344`, `romoperator.cpp:188-189`, `timeoperator.cpp:217`) already far exceeds the ≥3-instance bar across distinct arities, so the evidentiary claim holds regardless. The unverified sites are corroborating, not load-bearing. Re-verifying additional ranges is substantive evidentiary work, not a surgical citation-offset fix; no claim is wrong. The flag is "for completeness only" per the critic.

- **Finding**: [§Issue 3 — minor, deferred-by-design] Test empirical-match not pulled (`test/unit/test-vector.cpp` cited transitively, concatenation law is algebraic not `empirical_match`).
  - **Decision**: not-needed
  - **Rationale**: Explicitly deferred-by-design to harvester; the report self-flags it (Open question 5) consistent with the rough-in bar. Pulling per-arity test assertions to anchor the concatenation law is substantive authoring (harvester's formalization job), out of repair scope. Not a defect in this rough-in proposal.

### Unrepairable findings

None. No finding requires deferral as a blocking unrepairable item — all are non-blocking telemetry/informational, and the skill-uptake-survey signal is already routed to the batch-4 meta-phase by the critic.

## Suggested resolution

`ready`. Notes for the integrator:

- The proposed change is a single rough-in dep-map row append to `book/src/L2/index.md` (after the `chebyshev-iteration` row at `:24`), with a forward-link `./linear_combination.md` that intentionally does not yet exist (harvester creates the operator file). This matches the existing `krylov-step`/`chebyshev-iteration` forward-reference pattern in the same table.
- The optional companion provenance bullet (mirroring the `krylov-step` precedent at `:30-37`) is integrator's-discretion-or-defer-to-harvester per the report; either is consistent with the rough-in scope.
- Carry-forward telemetry (already in the report, no integrator action required): (a) skill-uptake-survey warning → batch-4 meta-phase combinator-miner spec extension; (b) harvester follow-ups on formalization — operator file, per-arity test-assertion empirical-match for the concatenation law, and the `L2-L1/linear-combination-fold-specialization` lowering theme (abstractor) — all correctly deferred per the rough-in bar.
