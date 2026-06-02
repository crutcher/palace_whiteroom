---
verifies: ./CYCLE.md
critiqued_at: 2026-06-02T21:07:18Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-02T21:10:15Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize dot + nrm2 at L4 (paired named-verb cohort)" (cycle-069 D2)

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` on the report returns `19 ok, 0 failing (19 citations checked)`, matching the report's own "19 ok / 0 failing" claim exactly. The two load-bearing L0 pinpoints were re-adjudicated with `--anchor`: `palace/linalg/vector.cpp:263-267 --anchor 'Dot'` → ok, anchor at `:263` (matches the report's "anchor confirmed at `:263`"); `palace/linalg/vector.hpp:255-260 --anchor 'Norml2'` → ok, anchor at `:257` (matches the report's "anchor confirmed at `:257`"); and the body line `vector.hpp:259 --anchor 'std::sqrt'` → ok (confirms the report's claim that `:259` is `std::sqrt(std::abs(Dot(comm, x, x)))` — the one-line `√ ∘ abs ∘ inner_product` composition). All transitive-anchor framing is faithful. No `verified_against:` YAML block is emitted by this report (harvester, not lowering-verifier), so the round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is not a refinement of an existing operator/theme; it is two NEW firm L4 chapters (`new:book/src/L4/dot.md`, `new:book/src/L4/nrm2.md`) authoring fresh surface, plus index/SUMMARY wiring. New-surface authoring with full evidence apparatus (Status + Signature + laws + variant axes + Evidence) is in-scope; the surface-vs-evidence-backfill dichotomy does not bite a greenfield-chapter report.

**rotation-quality — pass.** The two rotations are correctly classified as identity-in-form-on-the-body L4>L3 (no monadic wrapper / Solve-monad / convergence predicate to dissolve — the same in-line-marker route `inner_product`/`eigsolve`/`chebyshev` take), with the substantive rotation correctly placed downstream (the L2>L1 `inner-product-fold-specialization` for `dot`; the L1>L0 `nrm2-mutation-rotation` for `nrm2`). The report does NOT claim a fabricated compaction across L4>L3 — it explicitly states an `L4-L3/*-dissolution.md` would be a degenerate identity-in-named-terms theme (the §1d smell) and is correctly an in-line note. The do-NOT-merge over-unification guard is correctly applied: `nrm2` is framed as a CONSUMER not a fold member, and the stated reason (split-additivity `nrm2(x₁++x₂) = √(nrm2 x₁² + nrm2 x₂²) ≠ nrm2 x₁ + nrm2 x₂`, lost under `√`) is the genuine algebraic reason, verified against `inner_product.md` §"Consumer (NOT an instance)" on disk. `dot` is correctly the SPECIALIZATION (`inner_product` at `M = I`) — distinct from the consumer relationship. The keep-and-rise framing matches `concepts/black-box-vs-accelerated-kernels.md` §2 verbatim (read on disk `:88-136`): both named as confirmed keeps, both rise alongside the combinator as the permitted dual. Neither is a degenerate mirror — they are literature-standard named verbs (the directive-2 disposition-2 case), not renames.

**variant-axis-coverage — pass.** `dot` covers both orthogonal axes (conjugation-convention: `dot`/`tdot`; element-type: real/complex) with the per-element kernel table, and explicitly scopes out the weight axis (pinned at `M = I` — the pinning that makes it the named specialization) and diagonal degeneration (routed to the `nrm2` consumer, not a `dot` axis). `tdot`'s type-API-surface-only caveat (zero Palace call sites, declaration+definition only) is carried explicitly and inherited from L1/L2/L3. `nrm2` correctly collapses the element-type axis to a single operator (result always real ≥ 0) and explicitly scopes out the B-weighted `Norml2` overload as the separate `matrix-weighted-norm` consumer of `inner_product_M`. No hidden branches.

**cross-reference-integrity — warning.** The load-bearing count-ownership arithmetic is CORRECT and well-grounded (see below); the warning is for one link-target consistency item in the same edit. Details:
  - *Count-ownership (the load-bearing check) — verified correct.* I enumerated each L4 chapter's `## Status` firmness on disk (NOT from index cells, per the c057-meta guard): chebyshev, eigsolve, fe_assemble, fold_solve, inner_product, iterate-while, iterate-while-with-prev, krylov-step, ksp_solve, linear_combination = **10 firm**; solve_family = `rough-in (test-coverage-bounded)` (correctly NOT counted). This matches the report's "10 firm before this cycle" enumeration verbatim. The 4 outer-driver anchors (solve_loop, restart_cycle, Outcome, EigOutcome) are dep-map rows (confirmed at index `:82-85`), correctly kept as the `+4` and not double-counted as chapters. The new tally `13 + 4` = 10 + `assemble_frequency_operator` (D1) + `dot` + `nrm2`. I confirmed D1's sibling report (`reports/2026-06-02T205715Z-harvester-l4-assemble-frequency-operator/CYCLE.md`) authors `book/src/L4/assemble_frequency_operator.md` with `firmness: firm` — so D1 landed firm, the unconditional `13` is correct, and D2 counts D1's row but does NOT re-author it (verified: D2's blocks 4–5 author only `dot`/`nrm2` dep-map rows; the tally prose merely LINKS `assemble_frequency_operator` by slug). §Active-frontier prose registers all 3 c069 landings (assemble_frequency_operator D1, dot D2, nrm2 D2). Arithmetic and provenance basis both sound.
  - *Link-target inconsistency (the warning).* The tally `with:` block (block 1) links `assemble_frequency_operator` as `[`assemble_frequency_operator`](./assemble_frequency_operator.md)` — an **L4-relative** target (`book/src/L4/assemble_frequency_operator.md`). The EXISTING index links it 3× as `../L1/assemble_frequency_operator.md` (the L1 chapter), and D2's own block 3 anchor preserves an `../L1/...` link. Since D1 in fact authors the L4 chapter at `book/src/L4/assemble_frequency_operator.md` (firm), the `./assemble_frequency_operator.md` target DOES resolve on disk after D1 applies — so this is not a guaranteed dead link. BUT it is an ordering/consistency hazard: (a) it depends on D1's L4 chapter landing in the same cycle (a cross-dispatch dependency the integrator must apply D1-then-D2, or linkcheck2 fails if D2 lands first); and (b) the index now carries BOTH `./...` (L4) and `../L1/...` (L1) targets for the same slug, which is a latent inconsistency a follow-on pass should reconcile. The repairer/integrator should confirm apply-order and decide whether the tally link should point at the L4 chapter (consistent with the "reaching L4" framing) or be normalized against the existing `../L1/...` convention.
  - *Stale conditional fallback (informational, sub-item of the warning).* The tally `with:` block carries a "Count note: ... if D1 ... landed as a thin specialization note ... the firm tally is `12 + 4`" conditional, and §Open-questions repeats it. D1 in fact landed firm, so the conditional is now moot/misleading inline prose in a count-owner edit. Not an arithmetic error (the headline `13 + 4` is correct), but the integrator should strike the stale `12 + 4` conditional at apply-time to avoid shipping a contradicted hedge in the index.
  - All other cross-references resolve: both chapters re-express through `L4/inner_product` (firm c068, on disk), whose §"Specializations" names `dot` and §"Consumer (NOT an instance)" names `nrm2` — both confirmed on disk. All 5 index edit anchors (blocks 1–5) and the SUMMARY anchor (`linear_combination`→`eigsolve` contiguous at SUMMARY `:15-16`) were verified to match disk exactly, so the edits will apply.

**edge-label-fidelity — pass.** Both chapters carry the L4>L3 edge label; the §"Downward to L3" prose in each discusses exactly that edge (L4 verb → firm L3 dot/nrm2, identity-in-form), and the dep-map rows' L3 columns discuss the L3 form. No L3>L2/L2>L1 content is mislabeled as L4>L3 — the substantive lower-edge content is explicitly attributed to its own edge (L2>L1 fold-specialization; L1>L0 nrm2-mutation-rotation) and composed transitively, correctly annotated in-line per the no-non-adjacent-directory convention.

**plan-kind-consistency — pass.** Declared kind is firm L4 operator chapters; content shape matches — full Status/Signature/laws/variant-axes/Evidence apparatus, no rough-in placeholders. The `firm` claim rests on the firm-on-positive-structure / syntactic-identity escape (every law a read-off identity carried up from the firm combinator + firm L3/L1 leaves), the same bar `inner_product` cleared — a legitimate firm warrant for an identity-in-form rise, not an over-claim.

**cross-reference-integrity build-readiness (firm-body-inside-fence) — pass** (folded into the warning check above but verified clean here): fence enumeration shows the two `new:` blocks (lines 26→295, 297→566) contain NO nested triple-backtick fences (code samples use 4-space indent per the fence-parity guard), and each `## Status` section sits INSIDE its fence (dot at line 225, nrm2 at line 486 — both within their block bounds). The 29 raw backtick-fence-line count is odd only because line 656 carries an inline ` ``` ` prose mention (escaped, not a structural fence); structural fences are balanced. No fence-truncation defect.

**skill-uptake-survey — pass.** The report's shape (citation-bearing harvest + count-ownership) implies the `verify-citation-range` / `citecheck --anchor` procedure; the report explicitly references `citecheck --anchor` for the L0 anchors and cites the c057-meta count guard. Pure telemetry — uptake is present.

### Issues found

1. **(cross-reference-integrity, warning) Inconsistent + cross-dispatch-dependent link target for `assemble_frequency_operator` in the count-owner tally edit.** `reports/.../CYCLE.md` block 1 (the `with:` tally text, ~line 581) links `[`assemble_frequency_operator`](./assemble_frequency_operator.md)` (L4-relative), while the existing index and D2's own block-3 anchor use `../L1/assemble_frequency_operator.md`. The L4 target resolves only because D1 (sibling dispatch) authors `book/src/L4/assemble_frequency_operator.md` firm in the same cycle — so this is an apply-order dependency (D1 before D2, else linkcheck2 breaks) and a latent dual-target inconsistency in the index. Repair candidate: confirm apply order and normalize the target.

2. **(cross-reference-integrity, informational) Stale `12 + 4` conditional fallback in the count-owner tally + §Open-questions.** D1 landed firm, so the "if D1 lands a note → `12 + 4`" hedge in the tally `with:` block (~line 581) and the §Open-questions count-reconciliation bullet are now contradicted by disk state. The headline `13 + 4` is correct; the stale conditional should be struck at apply-time so the shipped index does not carry a moot hedge. Repair candidate: delete the conditional clause.

3. **(out-of-scope, correctly recorded — not a defect) Stale "no L4 entry" lines on firm L3 dot/nrm2.** `book/src/L3/dot.md:7-8` + `:107-110` and `book/src/L3/nrm2.md:7-8` + `:135-139` still assert "no L4 entry — leaf primitives are not first-class L4 vocabulary (cycle-010 audit verdict)" — verified on disk, and now genuinely stale once `L4/dot`/`L4/nrm2` land. The report correctly records this as an OQ for a follow-on lifter re-anchor (out of D2's one-operator write-scope), not dropped. No action for this report; flagged here only to confirm the staleness pointer is preserved as the report claims (it is).

---

## Repair

### Fixes attempted

- **Finding**: (cross-reference-integrity, warning) Inconsistent + cross-dispatch-dependent link target for `assemble_frequency_operator` in the count-owner tally edit — block 1 links `./assemble_frequency_operator.md` (L4-relative) while the old index referenced `../L1/`; the L4 target resolves only after D1 (sibling) lands its firm L4 chapter this cycle, an apply-order dependency.
  - **Decision**: repaired
  - **Action**: Verified block 1 (`reports/.../CYCLE.md` tally `with:` text) ALREADY uses the L4-relative `./assemble_frequency_operator.md` — which is the CORRECT target, since D1 lands `book/src/L4/assemble_frequency_operator.md` firm (its warrant resolved to a genuine L4 chapter, confirmed by the critic against D1's sibling report). No edit to the target was needed; it was already pointing at the right place. The actionable repair is the **apply-order constraint**: I recorded the **D1→D2 integration-ordering requirement** explicitly in the report's §Open-questions D1-count bullet (`reports/.../CYCLE.md` — "D1 must be applied before D2 so the `./assemble_frequency_operator.md` target is on disk when D2's index edit lands, else `linkcheck2` breaks") and in the §Supporting-evidence count-basis bullet. The pre-existing `../L1/...` link inside block 3's anchor is part of the existing `linear_combination` bullet text D2 anchors on (NOT D2's authored content), so normalizing it is out of repair scope — left as a latent index-consistency item for a follow-on pass (no dead link, both targets resolve on disk).
- **Finding**: (cross-reference-integrity, informational sub-item) Stale `12 + 4` conditional fallback in the count-owner tally `with:` block + the §Open-questions + §Supporting-evidence count-basis bullets — D1 landed firm, so the "if D1 lands a note → `12 + 4`" hedge is contradicted by disk state and would ship a moot conditional in the index.
  - **Decision**: repaired
  - **Action**: Struck the `12 + 4` conditional in all three places it appeared: (1) the block-1 tally `with:` text (`reports/.../CYCLE.md` §`book/src/L4/index.md` Block 1 — deleted the parenthetical "(Count note: if D1's `assemble_frequency_operator` landed as a thin specialization note … the firm tally is `12 + 4` …)"); (2) the §Supporting-evidence "Count basis" bullet (rewrote the conditional-+1 / `12 + 4` clause to the unconditional `13 + 4` with a repairer note recording the strike + the D1→D2 order); (3) the §Open-questions D1-count-reconciliation bullet (rewrote from the warrant-open conditional to the resolved firm `13 + 4` + the integration-order requirement). The headline `13 + 4 outer-driver` (which was always correct) now stands unconditionally.
- **Finding**: (out-of-scope, correctly recorded) Stale "no L4 entry" lines on firm L3 dot/nrm2.
  - **Decision**: not-needed
  - **Rationale**: The critic confirmed this is correctly recorded as an OQ for a follow-on lifter re-anchor and is out of D2's one-operator write-scope. The L3 entries are not D2's to edit; the staleness pointer is preserved in the report. No repair action; not a defect.

### Unrepairable findings

None. Both warning sub-items were mechanical/surgical (link-target confirmation + apply-order note; stale-hedge strike) and are repaired. The out-of-scope L3 staleness is correctly an OQ, not a finding requiring revision.

## Suggested resolution

`ready`. Notes for the integrator:

1. **Integration order is load-bearing this cycle: apply D1 (`assemble_frequency_operator`) BEFORE D2.** D2's count-owner tally edit links `[`assemble_frequency_operator`](./assemble_frequency_operator.md)` — the L4-relative target D1 creates at `book/src/L4/assemble_frequency_operator.md` (firm). If D2 lands before D1, that link has no on-disk target and `linkcheck2` (in `integrator-finalize`'s `cargo make book`) will break. D1-then-D2 is the required serial order.
2. The unconditional firm tally is **`13 + 4 outer-driver`** (10 prior firm + D1 `assemble_frequency_operator` + D2 `dot` + `nrm2`); the prior `12 + 4` conditional has been struck — apply the cleaned block as-is.
3. Latent (non-blocking) index consistency item for a follow-on pass: the index still carries `../L1/assemble_frequency_operator.md` references in pre-existing bullet text (e.g. the `linear_combination` cohort bullet D2 anchors on) alongside the new `./assemble_frequency_operator.md` L4 target. Both resolve on disk after D1 lands, so this is not a dead link — a future lifter/layer-intro-author pass may normalize the dual-target to the L4 chapter, consistent with the "reaching L4" framing. Out of repair scope (it would edit content D2 does not own).
4. The L3 dot/nrm2 "no L4 entry" staleness (OQ) is correctly deferred to a follow-on lifter re-anchor — promote the report's OQ as usual.
