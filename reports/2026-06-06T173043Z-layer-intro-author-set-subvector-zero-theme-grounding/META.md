---
verifies: ../REPORT.md
critiqued_at: 2026-06-06T180000Z
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

# META: verification of L1/set_subvector_zero theme-grounding edge upgrade

## Critique

### Checks run

**citation-validity** — pass. The report is an edge-typing + stale-prose-correction dispatch, so its load-bearing claims are about on-disk artifact state, not new Palace citations. Each was checked directly: the target op `book/src/L1/set_subvector_zero.md` is `rank: firm` (line 4) and pre-edit carries the theme at `reference:` (line 22) with the stale "rank-direction error" comment (lines 23–27); the target theme `book/src/L1-L0/set-subvector-zero-mutation-rotation.md` is `rank: firm` (line 6) and already carries the symmetric `depends-on target: L1/set_subvector_zero kind: lowers-to` (lines 9–10). The §5 convention citation (`graded-stack-scheme.md` §5, batch-34 "Reachability ≠ well-foundedness" clarification) was read on disk at lines 236–245 and says precisely what the report quotes: "an **L1 op**'s `lowers_to:` points operator → its **L1-L0 theme** (so typing the L1 op rescues its theme automatically)" and "The bounded fix per affected theme is one edge." The Palace `cites-evidence` ranges are preserved verbatim from the existing firm entry (untouched by this edit). No drift.

**surface-or-evidence** — pass. This is not a refinement-shaped operator/theme content change; it is a typed-edge grounding + co-located stale-prose correction. The surface change (frontmatter edge retype + three prose locations) is matched by the linter-measured liveness evidence (the reachability rescue, re-measured below). The record-definition sub-check is satisfied: the op's §Record definition (line 276) correctly states no new record is named, and `DofSet[N]` is referenced to its definition home `essential_dofs`, not redefined.

**rotation-quality** — pass. The edge being upgraded is a `lowers-to` edge to an L1>L0 lowering theme. The theme is a genuine cross-vocabulary rotation, not an identity smell: it lowers the pure-functional fresh-return projector `Z_idx = I − P_idx` into Palace's in-place receiver-argument zeroing `linalg::SetSubVector(x, rows, 0.0)`, where the destination IS the input argument `x` (`x.ReadWrite(use_dev)`). The theme's §"The crucial L0 facts the L1 form erases" enumerates four real erasures (receiver-as-destination mutation, `rows.Read` index gather, `forall_switch` device dispatch, complex two-buffer threading + hard literal-`0.0` imaginary write). This is a pure→in-place mutation rotation with a real vocabulary shift, exactly the c108 §5 case.

**variant-axis-coverage** — pass. No new variant axis is introduced by an edge retype. For completeness, the underlying op/theme already cover both axes explicitly: the element-type axis (real `Vector` / complex `ComplexVector`, the two L0 bodies) and the index-set-size axis (∅ identity → full zero), both marked absorbed.

**cross-reference-integrity** — pass. Both edge endpoints exist on disk (`L1/set_subvector_zero.md`, `L1-L0/set-subvector-zero-mutation-rotation.md`). The reachability chain endpoints were verified on disk: `feature/eigenmode.L4.md:13-14` carries `depends-on target: L3/divfree-projector kind: constrains-eigvec` (a grounding `depends-on`, not a reference), and `book/src/L3/divfree-projector.md:9-10` carries `depends-on target: L1/set_subvector_zero kind: uses` (also a grounding `depends-on`). So `L1/set_subvector_zero` is genuinely reachable from a feature root, and routing liveness down through the new op→theme edge is sound. The §5 cross-reference (`book/src/methodology/graded-stack-scheme.md` §5) resolves and supports the claim. The cited precedents `bc-elimination-post-composition-dissolution` / `divfree-projector-mutation-rotation` are named as the convention's establishing chain — accurate framing.

**edge-label-fidelity** — pass (load-bearing for this dispatch; verified in depth). The upgraded edge label `depends-on (kind: lowers-to)` from `L1/set_subvector_zero` → `L1-L0/set-subvector-zero-mutation-rotation` is genuinely faithful. The theme's whole content IS the lowering of this exact op (its intro: "Lowers the pure L1 form [`set_subvector_zero`] … into Palace's L0 in-place index-set overwrite `linalg::SetSubVector(x, rows, 0.0)`"; §Justification kind: "a clean syntactic-identity mutation rotation"). The theme carries the symmetric back-edge (`depends-on target: L1/set_subvector_zero kind: lowers-to`, lines 9–10), so the §5 asymmetric pair is correctly completed by the op→theme edge this dispatch supplies. Both endpoints are `rank: firm`, so `rank(op=3) ≤ rank(theme=3)` — the edge is rank-clean and introduces NO well-foundedness violation.

**plan-kind-consistency** — pass. The dispatch is declared as a single confirmed-faithful P1 typed-edge grounding (+ co-located stale-prose correction), and the content matches exactly: one frontmatter edge retype plus three prose corrections, all in one file, applied/measured/reverted to a clean tree with the proposed-changes blocks as the integrator channel. No mis-classification.

**skill-uptake-survey** — pass. The report cites self-verification via `tools/graded-stack-lint/graded_stack_lint.py --show-inbound` for the liveness claim and references the §5 convention as the procedural home. The dispatch shape (single-edge faithful grounding with a measured reachability delta) does not imply an unused skill. Telemetry only.

### Issues found

No blocking or warning issues. Independent re-verification of every load-bearing claim:

- **Reachability rescue re-measured (matches the report exactly).** Clean-tree baseline: `reachable=123, detritus=136, STRONGER GARBAGE SIGNAL=25, rank_violations=0`; the theme `L1-L0/set-subvector-zero-mutation-rotation` confirmed present in the STRONGER GARBAGE SIGNAL set (`[GARBAGE*]`). After applying the frontmatter edge change: `reachable=124 (+1), detritus=135 (−1), STRONGER GARBAGE SIGNAL=24 (−1), rank_violations=0 (HELD)`; `--show-inbound` confirms `L1-L0/set-subvector-zero-mutation-rotation <- L1/set_subvector_zero` and the theme is no longer in the garbage-signal list. Reverted to the clean tree afterward (no artifact mutation left behind). Every number the report predicted is correct.

- **Stale-prose correction is accurate, introduces no new error.** The OLD prose genuinely asserted the now-wrong claim. Verified in all three locations on disk: frontmatter comment (lines 26–27: "a depends-on from here to the theme would be a rank-direction error as well as redundant"), §Status well-foundedness paragraph (lines 261–270, framing the theme as "a downward narration, not an upward rank-blocking dependency"), and §Downward (lines 284–287, "with the theme as a downward `reference` pointer, not a blocking edge"). The correction is accurate: both endpoints are firm so `rank(op=3) ≤ rank(theme=3)` and the edge is rank-clean (linter-confirmed: `rank_violations` HELD 0); §5 deliberately routes liveness down via this edge. The replacement prose cites §5 and the precedent chain correctly and does not over-claim (it preserves the true statement that firmness still GROUNDS on the positive L0 read; the theme edge ADDS liveness, it does not change the firmness basis).

- **Candidate friction `stale-pre-c108-rank-direction-error-prose-on-L1-ops` is a real pattern (worth a c114 sweep).** Sanity-checked: the c104-era repair pattern (re-ground firm L1 leaf onto positive L0 reads, demote the L1>L0 theme to a `reference` edge, and add the "rank-direction error" justification) was applied across multiple BLAS-1/cleanup leaves in the same era. The post-edit STRONGER GARBAGE SIGNAL set still contains 24 nodes including `L1/normalize`-adjacent themes, and the edge-untyped detritus is dominated by L1-L0 themes — consistent with the same un-upgraded `reference`-to-theme edge sitting on many firm L1 leaves (`reciprocal`, `elementwise_product`, `scal`, etc.). Each is a single faithful §5 edge with the same measurable rescue shape. The recommendation to open a friction-ledger entry and schedule a batch-36/37 L1-op→theme sweep is well-founded; it is correctly scoped OUT of this one-edge dispatch and flagged in Open questions, not parked.

All 8 checks pass; `overall_status: ready` set. No repairer dispatch required.
