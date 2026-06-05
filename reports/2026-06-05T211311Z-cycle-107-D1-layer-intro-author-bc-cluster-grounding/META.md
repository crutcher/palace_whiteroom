---
verifies: ./CYCLE.md
critiqued_at: 2026-06-05T214500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-05T215500Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "ground the BC-elimination + divfree absorbed clusters (dofset / set_subvector_zero rescue)"

## Critique

### Checks run

**citation-validity — warning.** Every load-bearing Palace source pinpoint was confirmed both mechanically (`citecheck --anchor`) AND by on-disk read. BC leg: `laplaceoperator.cpp:216-217` anchors `SetEssentialTrueDofs` (line 217 — `ParOperator` construction + `DIAG_ONE` essential-dof pin baked into the per-multigrid-level stiffness assembly inside `GetStiffnessMatrix`); `:252` anchors `EliminateRHS` (the RHS-side lift inside `GetExcitationVector`); `modeeigensolver.cpp:571,574,608,611` each anchor `EliminateBC` inside `BuildSystemMatrixA/B`. Divfree leg: `eigensolver.cpp:233` anchors `SetDivFreeProjector` (wiring into the eigensolver), `:262` anchors `divfree->Mult` (the projector applied to the starting vector `v0`), `divfree.cpp:171-174` anchors `SetSubVector(rhs, *bdr_tdof_list_M, 0.0)` (the step-2 essential-BC zeroing = `set_subvector_zero`). All 14 source/book citations resolve in-bounds; the cited lines genuinely support the claimed absorbed-construction / wiring relationships — these grounding edges are FAITHFUL, not fabricated. Two sub-issues hold this at `warning` (not `pass`): (a) one bare-path citation `graded_stack_lint.py:431` does not resolve under `reference/`/`book/src/` via `--scan` (it is a `tools/`-internal reference — content verified correct against `tools/graded-stack-lint/graded_stack_lint.py:431`, the `rank:` > `firmness:` > `status` precedence — but the bare filename is a path-hygiene nit); (b) a minor prose-semantics imprecision at CYCLE.md:79 / the eigenmode `[new]`-edge comment, see Issues.

**surface-or-evidence — pass.** This is a frontmatter-only edge-typing report (3 `depends-on` grounding edges), not a refinement of operator/theme surface text — so it is neither a rotation_claim-without-surface nor a surface-modification needing rotation evidence. The evidence shape is the linter before/after delta + the Palace absorbed-construction sites, which is the correct evidence for a reachability-grounding edit. No record is newly NAMED in a signature by this report (it references the pre-existing `concepts/dofset` and `concepts/set_subvector_zero` record pages, both of which exist on disk with `kind: record`), so the record-definition obligation does not fire.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted; this report adds liveness edges to the dependency graph. No L_{n+1}/L_n compaction claim to evaluate.

**variant-axis-coverage — pass (not applicable).** No new operator/theme with orthogonal variant axes is introduced. The edges attach to existing chapters whose axes are already documented.

**cross-reference-integrity — warning.** All edge targets resolve on disk: `L4/eliminate_bc`, `concepts/dofset`, `L3/divfree-projector`, `L2/divfree-projector`, `L1/divfree-projector`, `L1/set_subvector_zero`, `concepts/set_subvector_zero` all exist; the follow-up-routed L1 BC-op tail (`L1/eliminate_essential_bc`, `L1/eliminate_rhs`, `L1/essential_dofs`) and `L1-L0/set-subvector-zero-mutation-rotation` all exist; `L4-L3/bc-elimination-post-composition-dissolution` exists. The pre-existing `eliminate_bc → reference → L4/fe_assemble` edge (the post-composition pipeline-position see-also) is confirmed on disk, corroborating the report's directionality argument. The `warning` is for a **stale `[old]` anchor in the `fe_assemble.md` proposed-changes block** that would silently drop two existing `reference` edges if applied verbatim — see Issues #1 (a genuine build/integrity hazard, repairable).

**edge-label-fidelity — pass (the central question of the cycle).** Each grounding edge honestly names its relationship and none reverses a genuine semantic separation:
- Edge 1 `fe_assemble → eliminate_bc (kind: absorbed-post-composition)`: I read `fe_assemble.md:118-124`. The documented law is "BC-elimination is NOT part of the **fold**" — i.e. not part of the algebraic *term-fold* `K = Σ assemble_term`. The edge does NOT claim BC-elimination is a fold step; `absorbed-post-composition` names the *separate* post-composition that the `models/`-level operator construction absorbs. The cited sites confirm the absorption is REAL (the `SetEssentialTrueDofs`/`EliminateBC` calls sit inside `GetStiffnessMatrix`/`BuildSystemMatrixA/B`, the very constructions every driver column reaches through `fe_assemble`). The edge runs `fe_assemble → eliminate_bc` (the abstraction depends on the absorbed elimination), the OPPOSITE direction from the existing `eliminate_bc → reference → fe_assemble` pipeline-position see-also — these are non-contradictory and the report distinguishes them explicitly (CYCLE.md:46-50). The separability law stands; the edge-kind is honest. This walks the directive's permitted-grounding / forbidden-false-edge line correctly.
- Edge 2 `eigenmode.L4 → divfree-projector (kind: constrains-eigvec)`: `eigensolver.cpp:222-234` builds the `DivFreeSolver` and `SetDivFreeProjector(*divfree)`; the eigenmode driver genuinely owns this wiring (OWN-COMPOSITION). Honest.
- Edge 3 `divfree-projector → {L1/set_subvector_zero, concepts/set_subvector_zero} (kind: uses)`: `divfree.cpp:171-174` is the step-2 essential-BC `SetSubVector(...,0.0)` that the L3 chapter already names as `set_subvector_zero`. `uses` faithfully types the prose dependency. Honest.

**plan-kind-consistency — pass.** Grounding (disposition path (a)) is the directive-mandated PREFERRED resolution for an unreachable node that is a genuine future/absorbed dependency of a goal node — consistent with the new 2026-06-05 directive over the planner's earlier "detritus-baseline-exception" fallback. The routed follow-up draws the faithful-path-or-finding boundary correctly: the L1 BC-op tail is left garbage rather than force-edged, with a cited reason that a `eliminate_bc → depends-on → L1 BC ops` edge would MISCLASSIFY a lowering relationship (L4-surface lowers-to L1-form; `eliminate_bc` only `reference`s those ops, confirmed on disk) as a blocking constituent — exactly the directive's prohibition on fabricating a false edge. Routing it to the batch-34 systematic lowering-chain-liveness pass is the correct finding-not-forced-fix disposition. The report's declared kind (reachability-grounding follow-up) matches its content.

**skill-uptake-survey — pass.** The report invokes the appropriate tool surface (`graded_stack_lint.py --show-inbound`, transient-apply→measure→revert) and the `citecheck`-equivalent on-disk reads for the absorbed-construction verification. No more-specific skill is implied by this edge-typing shape that the report omits.

### Issues found

**Issue #1 — stale `[old]` anchor drops two `reference` edges (cross-reference-integrity, MEDIUM, repairable).** In the `edit:book/src/L4/fe_assemble.md` proposed-changes block (CYCLE.md:140-157), the `[old]` block renders the `reference:` list as containing ONLY `- L4/index`. On disk (`book/src/L4/fe_assemble.md:9-12`) the `reference:` list has THREE entries: `L4/index`, `concepts/black-box-vs-accelerated-kernels`, `concepts/state-stratification`. The `[new]` block likewise re-emits `reference:` with only `- L4/index`. If an integrator applies this block as a literal region replacement, the two concept `reference` edges (`black-box-vs-accelerated-kernels`, `state-stratification`) are SILENTLY DELETED. The `depends-on` portion (where the grounding edge is added) is correctly anchored and is the substantive change; only the trailing `reference:` sub-list is truncated. Repair: re-emit the `[old]` AND `[new]` `reference:` blocks with all three on-disk entries preserved (add the grounding `depends-on` edge only). The other two edit blocks (`eigenmode.L4.md`, `divfree-projector.md`) were checked against on-disk content and their `[old]` anchors match exactly (the `eigenmode` anchor `eigsolve composes → cites-evidence` is correct and unique — the `config-record uses-record` edge sits AFTER `cites-evidence`, not within the anchored span).

**Issue #2 — bare tooling path in citation (citation-validity, LOW, path-hygiene).** `graded_stack_lint.py:431` (CYCLE.md:102, :208) is written as a bare filename and does not resolve via `citecheck --scan` (it lives at `tools/graded-stack-lint/graded_stack_lint.py`, outside `reference/`/`book/src/`). The cited content IS correct (line 431 is the `tok = fm.get("rank") or fm.get("firmness")` rank-source precedence). Repair (optional): write the full `tools/graded-stack-lint/graded_stack_lint.py:431` path. Non-blocking — it is a tooling-internal reference, not a Palace-source or artifact citation.

**Issue #3 — prose imprecision: "candidate eigenvector" vs initial starting vector (citation-validity / edge-label-fidelity, LOW).** CYCLE.md:79 says `divfree->Mult(v0)` keeps "the candidate eigenvector divergence-free", and the `eigenmode.L4.md` `[new]`-edge comment (CYCLE.md:169) says "per-candidate `divfree->Mult(v0)`". On disk (`eigensolver.cpp:247-264`) `divfree->Mult(v0)` is applied to the **initial starting vector** `v0` (inside the `init_v0` block, feeding `SetInitialSpace(v0)`), NOT a per-iteration candidate eigenvector. The edge claim itself ("the eigenmode driver wires the divfree projector into the eigensolver to keep eigenvectors in the divergence-free subspace") remains faithful — `SetDivFreeProjector` does constrain the solve — but "per-candidate" / "the candidate eigenvector" overstates the cited `:262` site (which is the one-time initial-vector projection). Repair (optional, surgical): soften to "the initial starting vector" for the `:262` site. Does not affect edge validity or the rescue measurement.

**Note (not an issue) — linter measurements are self-reported.** The reachable 88→95 / detritus 156→149 / rank_violations-held-0 deltas were produced by the report's own transient-apply→measure→revert and cannot be independently re-derived by the critic without re-applying the edits (out of critic write-authority). The arithmetic is internally consistent (7 rescued nodes enumerated; +7 reachable / −7 detritus matches) and the rank/well-foundedness reasoning checks out (all three edges are firm→firm on confirmed on-disk `rank:`/`firmness: firm` for `fe_assemble`, `eliminate_bc`, `eigenmode.L4`, `divfree-projector`, `L1/set_subvector_zero`, `concepts/set_subvector_zero`; the one firm→untyped tail to the non-node concept page is tolerated exactly as the pre-existing `divfree-projector → L2/divfree-projector` untyped edge). Integrator should re-run the linter post-apply to confirm the measured delta survives the (repaired) edit blocks.

---

## Repair

### Fixes attempted

- **Finding (Issue #1)**: stale `[old]` anchor in the `edit:book/src/L4/fe_assemble.md` proposed-changes block — `reference:` rendered as only `- L4/index` in both `[old]` and `[new]`, while on-disk the list has three entries; applied verbatim it would silently DELETE the two existing `reference` edges (`concepts/black-box-vs-accelerated-kernels`, `concepts/state-stratification`).
  - **Decision**: repaired.
  - **Action**: Re-read on-disk `book/src/L4/fe_assemble.md:9-12` (on-disk `Read`, NOT codemap) to confirm the byte-exact `reference:` list — three entries: `L4/index`, `concepts/black-box-vs-accelerated-kernels`, `concepts/state-stratification`. Re-emitted the full three-entry `reference:` list in BOTH the `[old]` and `[new]` blocks (CYCLE.md proposed-changes `edit:book/src/L4/fe_assemble.md`), so the `[old]` anchor now matches on-disk byte-for-byte and the `[new]` block preserves all existing reference edges while adding the grounding `depends-on` to `L4/eliminate_bc`. The substantive `depends-on` grounding edge was already correctly anchored and was left untouched. The two clean edit blocks (`feature/eigenmode.L4.md`, `L3/divfree-projector.md`) were NOT modified.

- **Finding (Issue #2)**: bare tooling-path citation `graded_stack_lint.py:431` (CYCLE.md:102, :208) — path-hygiene nit; content verified correct by critic.
  - **Decision**: repaired.
  - **Action**: Rewrote both occurrences to the full path `tools/graded-stack-lint/graded_stack_lint.py:431` (CYCLE.md §Rank/well-foundedness check + §Supporting evidence).

- **Finding (Issue #3)**: prose imprecision — `divfree->Mult(v0)` (`:262`) is the one-time initial starting-vector projection, but CYCLE.md:79 said "the candidate eigenvector" and the `eigenmode.L4.md` `[new]`-edge comment (CYCLE.md:169) said "per-candidate".
  - **Decision**: repaired.
  - **Action**: Softened CYCLE.md:79 to "the projector applied to the initial starting vector `v0` to keep it divergence-free", and the `eigenmode.L4.md` `[new]`-edge comment to "the initial starting vector projected `divfree->Mult(v0)` :262" (drops "per-candidate"). This is load-bearing in the comment case because the comment text becomes part of the applied artifact frontmatter. The edge claim itself (the projector constrains the solve to the divergence-free subspace) was already faithful and unchanged.

### Unrepairable findings

None. Both warnings reduced to mechanical/surgical fixes within repair authority (stale-anchor re-emission with on-disk verification + citation-path hygiene + prose softening). No substantive authoring or content decisions required.

## Suggested resolution

`ready`. Notes for the integrator:
- The `fe_assemble.md` `[old]` anchor now matches on-disk byte-for-byte (three-entry `reference:` list); applying the `[new]` block preserves `concepts/black-box-vs-accelerated-kernels` + `concepts/state-stratification` and adds only the `L4/eliminate_bc` grounding `depends-on`.
- Per the critic's closing note, the reachable 88→95 / detritus 156→149 / rank_violations-held-0 deltas were self-reported via transient-apply→measure→revert. Re-run `graded_stack_lint.py --show-inbound` post-apply to confirm the measured delta survives the repaired edit blocks (the repair preserves two extra reference edges but reference edges do not carry liveness, so the reachable/detritus delta is expected to be unchanged).
