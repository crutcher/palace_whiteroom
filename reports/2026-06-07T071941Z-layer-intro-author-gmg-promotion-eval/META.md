---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T074500Z
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

# META: verification of geometric-multigrid-preconditioner column rough-in → firm

## Critique

This report is a **status-promotion** (rough-in → firm) on a feature-surface composition-root,
landing via a faithful L4 edge re-classification rather than a forced flip. It was scrutinized
hard. All claims were verified independently against on-disk artifact state and the Palace source
via palace-codemap (NOT the producer's reasoning).

### Checks run

**citation-validity — pass.** The two load-bearing source citations were read via codemap.
`gmg.cpp:126-205` is accurate: `GeometricMultigridSolver::Mult` (the `pc_it` Richardson outer
loop, `X.back()=x` … `for(it<pc_it) VCycle(n_levels-1, it>0)` … `y=Y.back()`) sits at 126-142,
and `VCycle` (presmooth `Mult2` → residual `A->Mult` + `AXPBY(1,-1)` → restrict
`RealMultTranspose(*P[l-1])` → recurse `VCycle(l-1)` → prolong-add `RealMult` + `Y[l]+=R[l]` →
postsmooth `MultTranspose2`) sits at 172-205 — the report's prose rendering matches the source
exactly. `ksp.cpp:206-234` is accurate: the GMG construction with `GetProlongationOperators()`,
the auxiliary-space discrete interpolators, and the smoother config. The constituent-table
citation `gmg.cpp:42-60` correctly shows the per-level `B[l]` smoother construction
(`DistRelaxationSmoother` / `ChebyshevSmoother`). No report carries a `verified_against:` YAML
block, so that sub-check no-ops. (Codemap `read_range` can carry a +1 brace-boundary drift; the
content matched verbatim and the ranges are well in-bounds, so no drift finding is warranted.)

**surface-or-evidence — pass (feature-surface adaptation applied).** This is a composition-root,
so the adapted shape governs: its evidence is the L0 driver-source range + the constituent
down-links, not a single decomposed op's site. The L0/V-cycle range (`gmg.cpp:126-205` +
`ksp.cpp:206-234`) is cited and verified, and every constituent down-link resolves on disk. No
NEW per-op algebraic claim is asserted here. No new record is named in a signature (the GMG
column reuses already-defined constituent records), so the record-definition sub-check no-ops.

**rotation-quality — pass (no-op, not applicable to feature-surface kind).** A feature chapter
rotates nothing; it recomposes already-firm vocabulary outward. Marked pass per the codified
feature-surface adaptation.

**variant-axis-coverage — pass (no-op, not applicable to feature-surface kind).** The variant
axes (Chebyshev-4th/1st, real/complex, primary/auxiliary smoother) live in the constituent ops
the column composes, not in the column.

**cross-reference-integrity — pass (load-bearing for this kind).** Every constituent down-link
was confirmed present on disk: `preconditioning-framework`, `fe_space_hierarchy`,
`multigrid-relaxation-smoother`, `reciprocal`, `normalize`, `chebyshev-smoother`, `L3/chebyshev`,
`L2/jacobi-smoother`. The maturity claims in the report's constituent table match on-disk
`## Status` lines: `multigrid-relaxation-smoother` = `firm` (kernel-impl), `chebyshev-smoother` =
`firm`, `jacobi-smoother` = `firm`, `fe_space_hierarchy` = `firm`, `reciprocal` = `firm`,
`normalize` = `firm` (`rank: firm`), `preconditioning-framework` = `firm`, `L3/chebyshev` =
`partial-obstruction` with NO `obstruction_resolution` (rankless to the linter). The promoted
column composing the `partial-obstruction` `L3/chebyshev` only over a `reference` edge is correct
(sibling-view; not a maturity overclaim). Every edit-block `[old]` text was confirmed to match
on-disk content, so all eight edits will apply cleanly.

**edge-label-fidelity — pass (the decisive check; verified independently).** The report's central
move is re-typing the L4 `L3/chebyshev` and `L2/jacobi-smoother` edges from blocking
`depends-on (composes)` to `reference`. This was scrutinized against the §2g GROUND-faithfully
discipline (decline an over-edge; do not edge-launder to force a firm flip), and it is FAITHFUL:
(1) the firm `multigrid-relaxation-smoother`'s OWN on-disk `depends-on` block points at
`L1/chebyshev-smoother` (firm), `L1/apply_linop`, `L1/axpby`, `L1/interpolator` — NOT at
`L3/chebyshev`; `L3/chebyshev` appears in the smoother only in PROSE (lines 239, 353) as the
"parallel L3-lift partial-obstruction finding," never as an edge. (2) `L3/chebyshev` self-
describes in its own chapter as "the **iteration-rotation** rendering of the Chebyshev smoother"
— i.e. an iteration-VIEW, not a build constituent. (3) The L1 feature file ALREADY types both as
`reference` (verified on disk); the fix brings the L4 file into agreement with the already-correct
L1 file rather than inventing a new disposition. The would-be `column →depends-on→
L3-iteration-view` edge is exactly the §2g over-edge being declined. The re-typing is faithful,
not laundering.

**plan-kind-consistency — pass.** Declared as a feature-surface promotion-eval landing
`status: seed` / `rank: firm`; the content is a status-promotion with a faithful edge
re-classification, exhaustively cited composition, and documented-sequential-obstruction
disposition. Content shape matches the declared kind. No rough-in placeholders remain in the
proposed firm body.

**skill-uptake-survey — pass (telemetry).** The report references the §2g GROUND-faithfully
priority order and the firm-on-positive-structure + documented-sequential-obstruction discipline
by name, and cites the linter mechanics directly (`graded_stack_lint.py` rank_check). The
relevant procedural disciplines are surfaced.

**rank-invariant (graded-stack #9) — pass.** Post-retype, every remaining blocking `depends-on`
constituent is `firm` on disk: `preconditioning-framework`, `fe_space_hierarchy`,
`multigrid-relaxation-smoother`, `reciprocal`, `normalize`. So `rank(firm) ≤ min(deps) = firm`
holds and the `firm` claim is well-founded. The two demoted edges become `reference`, which the
rank check ignores. (Independently confirmed: the linter's `rank_check` skips rankless deps —
`if dep.rank is None: continue` — so even the pre-fix `firm`-on-rankless-`L3/chebyshev` edge was
EXIT-0; the report correctly distinguishes "linter-clean" from "faithful," and the re-type makes
it faithful in fact.)

**reachability (graded-stack #10) — pass, with an honest self-flag.** The column is a feature-
surface GC-root (`feature_root: seed`) and reaches its firm constituents over `depends-on`. The
report transparently flags (Open questions) that moving `L3/chebyshev`/`L2/jacobi-smoother` to
`reference` means the column no longer reaches the L2/L3 chebyshev/jacobi iteration-VIEWS over
`depends-on` — but this is the FAITHFUL position (a `column →depends-on→ iteration-view` edge
would be the §2g over-edge), the L1 chebyshev-smoother stays reachable via the smoother chain,
and the routing to the c123/batch-39 meta's standing RE-recheck is the correct disposition (not a
regression — it removes the prior unfaithful over-edge). This is exemplary self-disclosure, not a
defect.

### Issues found

None. This is an all-pass clean report. The promotion rests on independently-verified on-disk
state (all blocking constituents firm; `L3/chebyshev` genuinely a partial-obstruction iteration-
view, not a build dependency of the V-cycle) and verified Palace source (`gmg.cpp:126-205`,
`ksp.cpp:206-234`, `gmg.cpp:42-60`). The edge re-classification is faithful (matches the firm
smoother's own `depends-on` and the already-correct L1 file), not edge-laundering to force the
firm flip. The RE1-reachability consequence is honestly surfaced and routed to the meta-phase
rather than papered over. `overall_status: ready`.

#### Non-blocking observations (informational; not findings)

- The L4 Haskell pseudo-code body (line 63: `bs = [ smoother cfg l | l <- levels ] -- …
  L1/multigrid-relaxation-smoother / L3/chebyshev / L2/jacobi-smoother`) still lists all three
  smoother slugs in an inline annotation comment. This is a code-comment, not a status/edge
  claim, and is consistent with the iteration-view framing — no edit needed, noted only for
  completeness.
- The report's reciprocal/normalize "GROUNDS RE5/RE7" framing and the `record-
  FiniteElementSpaceHierarchy-promote-watch` reconcile note are correctly scoped as flags for the
  meta-phase (out of this report's write-scope), consistent with the partition.
