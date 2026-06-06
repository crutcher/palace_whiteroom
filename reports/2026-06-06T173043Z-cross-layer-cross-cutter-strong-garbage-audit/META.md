---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T18:05:00Z
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
repaired_at: 2026-06-06T18:30:00Z
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

# META: verification of "Cross-layer observation — 11 un-excepted STRONGER-GARBAGE-SIGNAL members dispositioned"

## Critique

### Checks run

**citation-validity — pass.** This is an OBSERVATION/AUDIT dispatch that mutates no `book/` artifact, so the per-claim source-citation burden is the disposition prose, not a new operator entry. I verified the load-bearing pinpoints against on-disk prose and the live linter, not by hand-asserting line numbers. The groundable case is exactly cited: `book/src/L1/fe_assemble.md:60` carries `terms: [WeakFormTerm]` in the signature (verified — line 60 is the signature line), and `:71-72` says "Each element is a firm `weak_form_term`"; `book/src/L1/weak_form_term.md:21` ("the value `fe_assemble` folds over") and `:25` ("the **per-term value** the `fe_assemble` fold quantifies over") both check out verbatim. The RE6 anchor `L3/axpy.md:16` ("speak THROUGH the combinator, not as re-derived base forms") is present at line 16 word-for-word. The RE8 `lifts_from: L4/<op>` claims are corroborated by the inbound graph (below). All spot-checked anchors are real and in-range.

**surface-or-evidence — pass.** Not a refinement-shaped proposal — it proposes no surface edit to any existing operator/theme; it is a pure Axis-2 reachability disposition audit (a finding list routed to a future c114 grounding dispatch + a meta-phase RE-ratification recommendation). No rotation_claim-without-surface smell. No record is named in a new signature here, so the record-definition sub-check no-ops.

**rotation-quality — pass.** Not applicable to an observation/audit dispatch — it asserts no algebraic/structural rotation of its own; it characterizes the rotations already authored in the cited chapters (e.g. axpy-family combinator-primary absorption, the L3 iteration-views). No 1:1-rename masquerading as a rotation is being proposed.

**variant-axis-coverage — pass.** Not applicable — the audit composes/dispositions existing nodes; it introduces no operator with orthogonal variant axes of its own.

**cross-reference-integrity — warning.** All named nodes/slugs that the report DOES disposition resolve on disk (`L1/fe_assemble`, `L1/weak_form_term`, `L2|L3/axpy|axpby|axpbypcz`, `L2|L3/elementwise_product`, `L3/assemble-diagonal`, `L3/fold_solve`, `L3/krylov-step`, all RE-cited siblings) and the linter confirms each is a real STRONGER-GARBAGE member. The proposed grounding edge `L1/fe_assemble → L1/weak_form_term` is FAITHFUL, not manufactured (see Issue 1 — verified). HOWEVER, the audit's completeness claim is overstated: it asserts (lines 15, 136–138) that after RE6–RE8 land "no un-dispositioned typed-but-unreachable node remaining except `weak_form_term`," but `L3/jacobi-smoother` — a firm, typed STRONGER-GARBAGE member — is dispositioned NOWHERE (see Issue 2). That is exactly the residual the report itself warns about for `scal`. Warning, not fail, because the gap is an omission in a completeness claim, not a broken or manufactured edge.

**edge-label-fidelity — pass.** The directional reasoning is correct throughout and the prose matches each edge label. RE6: edge runs leaf→combinator (`L3/axpy → L3/linear_combination`), verified in the inbound graph (`L3/linear_combination <- L3/axpy, L3/axpby, L3/axpbypcz, L4/linear_combination`; `L2/linear_combination <- ...L3/axpy...`). RE8: edge runs L3→L4 UP (`lifts_from`), verified (`L4/fold_solve <- L3/fold_solve`; `L4/krylov-step <- L3/krylov-step, L4/ksp_solve`); the "grounding L4 does not carry liveness UP into the L3 view" reasoning is structurally correct (depends-on liveness flows consumer→constituent, i.e. in the edge direction). RE7: edge runs L3→L2 down, consistent with the inbound graph.

**plan-kind-consistency — pass.** Declared as an OBSERVATION/audit (coverage-gap / audit-residue), and the content is exactly that — a per-member disposition table + cluster rationales + routed recommendations, no artifact authoring. Kind matches shape. The GROUND→RE-except→delete priority is correctly applied: 0 GC-delete candidates, GROUND attempted first (→ weak_form_term), baseline-exception only after GROUND ruled unfaithful (lines 176–180), consistent with the GROUND-don't-remove directive.

**skill-uptake-survey — pass (telemetry).** The audit uses the prescribed tool path (`graded_stack_lint.py --show-inbound`) for the reachability/inbound-edge survey, which is the right instrument for an Axis-2 disposition. No dedicated skill is implied beyond that; nothing to flag.

### Issues found

**Issue 1 (verification, NOT a defect — recorded as cleared): the groundable `L1/fe_assemble → L1/weak_form_term` edge is genuinely faithful.** I independently confirmed both halves of the producer's claim. (a) `L1/fe_assemble` IS reachable: the linter `--show-inbound` shows `L1/fe_assemble <- feature/boundary-mode.L1, feature/driven.L1, feature/eigenmode.L1, feature/electrostatic.L1, feature/lifecycle.L1, feature/magnetostatic.L1, feature/transient.L1` — exactly the 7 feature columns the report claims. (b) `weak_form_term` IS a by-name fold-element constituent: `fe_assemble.md:60` signature is `fe_assemble :: (space: ..., terms: [WeakFormTerm]) -> ...` and `fe_assemble(space, terms) = foldr (\t acc -> A(space,t)+acc) zero terms`; `weak_form_term.md` is the element type of that list. This is a real `depends-on` (a data-shape signature member), NOT a lowering and NOT a sibling reference. (c) `L1/weak_form_term` currently has zero inbound (confirmed — no `<-` line in the linter output), so it is genuinely ungrounded today. (d) The free-rider claim checks out: `L1-L0/fe-assemble-libceed-boundary-obstruction <- L1/weak_form_term` exists, so grounding `weak_form_term` transitively grounds the obstruction-leg. The disposition is sound; the proposed c114 edge is faithful.

**Issue 2 (warning; cross-reference-integrity / completeness): `L3/jacobi-smoother` is an un-dispositioned STRONGER-GARBAGE member the audit misses.** Location: CYCLE.md disposition table (§Specific finding) + the completeness claim at lines 15 and 136–138. The live linter lists 25 STRONGER-GARBAGE members. Subtracting the RE1–RE5-ratified node-set (8 of the 25: `L2/jacobi-smoother`, `L2/normalize`, `L2/reciprocal`, `L3/chebyshev`, `L3/normalize`, `L3/orthogonalize`, `L3/reciprocal`, `L4/preconditioning-framework`), the report's 12-row table, and the 4 explicitly-flagged out-of-scope/already-handled members (`set-subvector-zero` = c113-D2 grounded exemplar; `L1/normalize` = RE5 consumer-side per line 181–184; `L2/scal`+`L3/scal` = RE6 companion per lines 67–72/131–135) leaves exactly ONE node with NO disposition: **`L3/jacobi-smoother`**. It is `firmness: firm`, typed (`depends-on: L1/jacobi-smoother`, `kind: lowers-to`), and its only inbound is `L3/jacobi-smoother <- L2/jacobi-smoother` (the RE1 member) — so it is the L3 iteration-view of the diagonal-preconditioner leg whose per-call body is `op.dinv ⊙ x` (one elementwise product, `L3/jacobi-smoother.md:19`). It belongs naturally in RE7's diagonal-preconditioner-apply cluster (or RE1's node-list, which today contains only the L2 form), but the report names it only as a *cross-ref consumer* of elementwise_product (lines 49, 77, 128), never as a node requiring its own disposition. This is precisely the "STRONGER-GARBAGE count climbs without a ratified RE entry" re-open trigger the report itself raises for `scal` (lines 131–135) — leaving `L3/jacobi-smoother` stranded would re-trip it. Severity warning: the dispositions the report DOES make are faithful, but the audit's headline completeness claim ("0 un-dispositioned remaining except weak_form_term") is false by one node; the fix is to fold `L3/jacobi-smoother` into the RE7 cluster (or RE1's node list).

**Issue 3 (minor / observation; member-count phrasing): the table holds 12 rows but the prose says "11 un-dispositioned remainder."** Location: §Summary line 13–15 ("11 un-dispositioned remainder," "1 GROUNDABLE + 10 baseline-exception") vs the disposition table (12 rows: 1 groundable + 11 RE-dispositioned). The arithmetic 1+10=11 does not match the 12-row table (1 groundable + 6 RE6 + 3 RE7 + 2 RE8 = 12). The "14 ratified as RE1–RE5" + "11 un-dispositioned remainder" = 25 framing is also loose: only 8 of the 25 live STRONGER-GARBAGE members are RE1–RE5 node-set members; the other RE1–RE5 nodes (e.g. `L4/chebyshev`, `L2/chebyshev-iteration`, `L2/gram`, `L2/incremental-least-squares`, `L2/nrm2`, the `L*-L*` lowering themes) are not in this 25-list at all (they are edge-untyped or otherwise distinct). The dispositions themselves are unaffected; this is a counting/framing imprecision worth correcting so the meta-phase's RE6–RE8 ratification starts from an exact member ledger. Compounds with Issue 2 (the off-by-one in the table-vs-prose count is a symptom of the same incomplete enumeration that dropped `L3/jacobi-smoother`).

### Notes on the sound dispositions (no action)

- RE6 (axpy-family) is faithful: `L3/axpy.md:16` + `lifts_from: L3/linear_combination` confirm the leaf→combinator direction; forcing `linear_combination → axpy` would invert combinator-primary. No hidden groundable edge.
- RE8 (L3 iteration-views) is faithful: both `L3/fold_solve` and `L3/krylov-step` carry `lifts_from: L4/<op>` (edge UP), the L4 targets are independently reachable (`L4/fold_solve` via lifecycle/transient columns; `L4/krylov-step` via `L4/ksp_solve`), and no consumer reaches the L3 view. No hidden groundable edge.
- RE7 (diagonal-apply kernels) is faithful for the three nodes it names; its only defect is the *omission* of `L3/jacobi-smoother` from the same cluster (Issue 2), not a wrong disposition of the nodes it does cover.
- The author's own RE7-vs-RE1 and RE8-vs-RE2 id-split caveats (Open questions) correctly defer the merge/split judgment to the meta-phase rather than pre-deciding — appropriate scoping.

## Repair

### Fixes attempted

- **Finding** (Issue 2, cross-reference-integrity warning): the audit misses `L3/jacobi-smoother`, an un-dispositioned firm/typed STRONGER-GARBAGE member that is the L3 view of the RE1 jacobi diagonal-apply leg.
  - **Decision**: repaired.
  - **Verification (faithful-edge-or-finding)**: read `book/src/L3/jacobi-smoother.md` before editing. Confirmed it IS the L3 diagonal-apply view: `firmness: firm`; `depends-on: L1/jacobi-smoother` kind `lowers-to` (`:7`); per-call body is one elementwise product `op.dinv ⊙ x = (ω · D⁻¹) ⊙ x`, named "the thinnest constructed-operator gate" (`:19`); obstruction-leaf, one elementwise product, no loop (`:65`). Same diagonal-preconditioner cohort (jacobi/chebyshev) as the existing RE7 `elementwise_product`/`assemble-diagonal` kernels. The disposition is plainly RE7-extension with the same rationale (absorbed below the RE1 preconditioner leg) and the same promotion condition (grounds transitively when RE1 grounds). This is a surgical add, not a content authorship — the disposition rationale is mechanically transcribed from the established RE7 cluster logic the report already wrote for its sibling nodes.
  - **Action**: added an `L3/jacobi-smoother` row to the per-member disposition table (§Specific finding), updated structural-class-2 narrative (3→4 nodes), and added it to the RE7 row of the §(b) meta-phase ratification table — all in `reports/<id>/CYCLE.md`.

- **Finding** (Issue 3, minor / count imprecision): the disposition table holds more rows than the prose "11 un-dispositioned remainder" / "1 GROUNDABLE + 10 baseline-exception" claims; the framing of "14 ratified RE1–RE5" + "11 remainder" = 25 is loose.
  - **Decision**: repaired.
  - **Action**: corrected the §Summary count to the accurate enumeration — after subtracting the 8 RE1–RE5 node-set members and the 4 out-of-scope/already-handled members, **13 members remain** (1 GROUNDABLE + 12 baseline-exception: 6 RE6 + 4 RE7 + 2 RE8), with `L3/jacobi-smoother` named as the 13th (RE7). Replaced the loose "14 ratified as RE1–RE5" framing with the exact "8 of the 25 members are in the RE1–RE5 node-set." Updated the headline completeness claim (frontmatter scope line + H1 title: "11"→"13") and the cluster-completeness caveat to reflect RE7 now including `L3/jacobi-smoother`. All edits in `reports/<id>/CYCLE.md`.

### Unrepairable findings

None. The warning was a surgical omission (one un-dispositioned node whose disposition is mechanically determined by the report's own established cluster logic + verified chapter prose) and the minor finding was a pure counting/framing correction. Neither required substantive authoring or a content judgment the report had not already made for its sibling nodes.

## Suggested resolution

`ready`. Notes for the integrator: this was an observation-only dispatch (no `book/` mutation); the repairs are confined to the report's own CYCLE.md. The corrected enumeration (13 = 1 GROUNDABLE + 12 RE6–RE8) and the RE7 cluster now including `L3/jacobi-smoother` should feed the c114 grounding dispatch (the single `L1/fe_assemble → L1/weak_form_term` edge) and the batch-36 meta-phase RE6–RE8 ratification with an exact member ledger. The author's RE7-vs-RE1 / RE8-vs-RE2 id-split caveats and the `scal` cluster-completeness note remain open for the meta-phase to ratify.
