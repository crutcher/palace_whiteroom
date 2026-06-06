---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T17:08:39Z
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

# META: verification of "CYCLE: L3 scal + linear_combination typed-edge migration"

## Critique

This is a frontmatter-only typed-edge hygiene dispatch (graded-stack P1 lazy-tail, batch-36 D2): it migrates `book/src/L3/scal.md` and `book/src/L3/linear_combination.md` off the legacy `firmness:`/`lowers_to:`/`lifts_from:` representation onto the batch-33-ratified `rank:` + `edges:{depends-on,reference}` scheme. No body prose, no new operator algebra. As the dispatch framing anticipated, several of the 8 checks no-op for pure frontmatter; scrutiny concentrated on edge-label-fidelity, cross-reference-integrity, rank-well-foundedness, plan-kind-consistency, and the load-bearing zero-delta / detritus claims. All mechanical claims reproduce exactly. All 8 checks pass.

### Checks run

**citation-validity — pass.** The report's load-bearing claims all carry pinpoints that resolve in-range. Spot-verified against the reverted-to-baseline on-disk files: `scal.md:36` is the `## Status` `firm` line; `scal.md:16,20,22,24` carry the `scal(α,x)=linear_combination[(α,x)]` identity, the arity-1 row, the lowering-routing-through-§"Downward to L2", and the fold-specialization theme reference; `linear_combination.md:108-110` is the `## Downward to L2` identity-in-form passage, `:125` the "Upward (L2)" dependency, `:152` the `firm` status, `:154-156` the "Lifts from" L4 identity; `L2/linear_combination.md:4` is `rank: firm` (the well-foundedness anchor). The linter-shim citations are accurate in substance: the migration-mapping block is `graded_stack_lint.py:518-547`, and the `untyped` flag definition is exactly `:551` (`untyped = rank is None AND not read_any_edge AND not root AND not obstruction`). One minor pinpoint imprecision (non-blocking, noted as an issue below): the producer attaches the quote "their presence counts as 'typed' for the untyped flag" to `:546-547`, but at `:546-547` that comment governs the `l0_ground_truth` branch; the mechanism that actually makes scal/linear_combination "typed" is the `lowers_to`/`lifts_from`→depends-on mapping at `:527-532` (which sets `read_any_edge=True`). The conclusion is correct; only the quote's home line is off.

**surface-or-evidence — pass (largely no-op for this kind).** This is not a refinement proposal — it modifies no operator/theme surface text and asserts no new rotation_claim; it is a representation migration of existing frontmatter. The check therefore no-ops on its primary clause. The record-definition sub-check also no-ops correctly: both chapters are operator entries over scalars/tensors with no signature-named record needing a definition home, which the report itself flags ("No record-definition gaps surfaced"). Verified against the chapter signatures (`linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[$S]`; `scal(α,x)`) — no `{field:type}` record, no config/state carrier.

**rotation-quality — pass (not applicable to a frontmatter-typing dispatch).** No algebraic/structural rotation is asserted by this dispatch; the L3>L2 identity-in-form rotation already lives in the existing (untouched) chapter bodies. Nothing to grade here.

**variant-axis-coverage — pass (no-op).** The `variant_axes:` lists are preserved verbatim across the migration (scal: element-type + scalar-promotion; linear_combination: arity/output-aliasing/element-type/scalar-promotion/operand-category). The migration introduces no new branch and scopes nothing out.

**cross-reference-integrity — pass.** Every authored edge target resolves to an existing on-disk slug. Confirmed by file-existence check: `L2/linear_combination` (depends-on, both files), `L3/linear_combination`, `L1/scal`, `L4/linear_combination`, `L2-L1/linear-combination-fold-specialization` (references) all EXIST. The linter reports `unresolved_depends_on_targets=0` on the baseline tree, and since the new depends-on (`L2/linear_combination`) is the same target the legacy shim already resolved, no new unresolved target is introduced.

**edge-label-fidelity — pass.** Each authored edge faithfully reflects the chapter's OWN prose plus its legacy fields, and the two declinations are correct. (1) `depends-on: L2/linear_combination` in both files traces to the legacy `lowers_to` field naming the L2 op AND the body prose (`scal.md:16,22`; `linear_combination.md:108-110,125`); it is operator→operator, adjacent-edge, and the target is `rank: firm`. (2) The DECLINED L3→L1 `depends-on` over-links are correctly declined: the legacy `lowers_to` arrows tail to L1 (`… → book/src/L1/…`), but those are non-adjacent transitive in-line identity endpoints (cycle-012 non-adjacent-identity convention, no `L3-L1/` directory) — they belong under `reference` (scal puts `L1/scal` there), not depends-on past the adjacent L2 layer. (3) The DECLINED `kind: lowers-to` theme depends-on is correctly declined: the surface form mirrors `L3/dot` exactly — bare-slug `depends-on`/`reference` lists, NO `{target:, kind:}` block-mapping. I confirmed `L3/dot` uses bare slugs (`- L2/inner_product`, `- L4/dot`) and reserves no theme edge; the block-mapping `kind: lowers-to` form is the `L2/krylov-step` pattern (verified: `L2/linear_combination.md:11-12` uses it for the L2>L1 theme), which is the L2-pulls-theme-into-depends-on pattern, not the L3-leaf pattern. The lowering THEME (`L2-L1/linear-combination-fold-specialization`) is correctly placed under `reference`. No edge label misstates a layer relationship.

**plan-kind-consistency — pass.** The content shape is genuinely typed-edge hygiene, not disguised authoring: the proposed-changes blocks touch ONLY the frontmatter (the `[new]` payloads are pure `rank:` + `edges:` + preserved `variant_axes:`); no body lines are added or rewritten in either edit. The declared scope ("frontmatter-only — no body rewrite, no new operator algebra") matches.

**skill-uptake-survey — pass.** No skill is squarely implied by a pure frontmatter-typing migration (the graded-stack scheme is encoded in the linter + role-spec, not a skill). The report appropriately leans on the linter (`graded_stack_lint.py --json` / `--show-inbound`) as the authoritative measurement, which is the correct telemetry path for this dispatch.

### Load-bearing claim verification (reproduced mechanically)

I re-ran `graded_stack_lint.py --json` on the baseline (reverted) tree to adjudicate the report's three central claims:

- **Shim claim — ACCURATE.** `graded_stack_lint.py:527-532` maps `lowers_to`/`lifts_from`/`lifts_to`/`consumes` to depends-on edges and sets `read_any_edge=True`; `:551` defines `untyped` as `rank is None AND not read_any_edge AND …`. Since both files carried `lowers_to:` + `lifts_from:`, they were already `read_any_edge=True` → never in the untyped-60. Confirmed directly: `'L3/scal' in untyped == False` and `'L3/linear_combination' in untyped == False`. The `untyped 60→58` expectation correctly does NOT hold; the migration is a representation upgrade, not a typed-count delta. The producer's finding is right.
- **Zero standalone delta — sound.** Baseline TOTALS reproduce the report's reported baseline exactly: `files=355, typed=295, untyped=60, roots=36, reachable=122, rank_violations=0, unresolved=0`. The migration preserves the graph: the new `depends-on: L2/linear_combination` is the same target the legacy `lowers_to` shim already resolved. The one semantic shift — moving the `lifts_from` up-edge from depends-on (under the shim) to `reference` — only removes OUTBOUND depends-on edges from these nodes; it cannot create a rank violation (fewer constraints) and cannot reduce these nodes' INBOUND reachability. I confirmed `L4/linear_combination` retains independent inbound (`L4/assemble_frequency_operator`, `L4/eliminate_bc`) so it stays reachable regardless, and `L3/linear_combination`'s reachability comes from `L4/linear_combination`'s downward depends-on, not from its own outbound lift-edge. The "all totals HOLD" claim is logically sound.
- **Detritus disposition — correct (faithful-edge-or-finding).** Confirmed: `L3/scal` IS in `detritus` (and in `detritus_with_typed_edges_stronger_signal`), with its only inbound being `L3/normalize` (itself unreachable). `L3/linear_combination` is NOT detritus (reachable via `L4/linear_combination`). The producer correctly DECLINED to manufacture an inbound edge to force-flip `L3/scal` and instead flagged the GROUND-candidate `L3-scal-reachable-via-normalize-grounding` for a future pass that types an upstream consumer's edge. This is the right disposition under the GROUND-don't-remove directive: grounding `L3/scal` requires typing an out-of-scope upstream consumer (`L3/normalize` and its reachable consumer), not faking an inbound edge here. Faithful-edge-or-finding upheld.

### Issues found

- **Minor (non-blocking) — citation pinpoint imprecision, CYCLE.md §"Standalone linter delta" / Open questions.** The quote "their presence counts as 'typed' for the untyped flag" is attributed to `graded_stack_lint.py:546-547`, but at `:546-547` that comment governs the `l0_ground_truth` branch. The mechanism that actually makes `L3/scal` / `L3/linear_combination` "typed" is the `lowers_to`/`lifts_from`→depends-on mapping at `:527-532`. The producer's overall range citation `:518-547` (for the migration shim block) and the `:551` untyped-flag citation are both correct; only the inner quote's home line is off-target. The finding's conclusion is unaffected. No other issues.

No content, surface, rotation, variant-axis, cross-reference, edge-label, or kind defects. The dispatch is a clean, faithful, mechanically-reproduced typed-edge migration.
