---
verifies: ../REPORT.md
critiqued_at: 2026-06-06T193000Z
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

# META: verification of the cycle-115 D1 plateau-probe (independent frontier-exhaustion audit)

## Critique

This is an OBSERVATION-ONLY plateau-confirmation probe (mutates no artifact, proposed-changes: None). Per the CLAUDE.md observation/negative-result handling, the citation/surface/rotation/variant checks do not gate an authored chapter here — the load-bearing output is the NEGATIVE VERDICT ("exhaustion CONFIRMED" on three fronts), which the batch-37 meta-phase terminal-state decision is gated on. I therefore audited the soundness of the verdict directly: I re-ran the linter, re-counted the RE membership, verified the load-bearing Front-1/Front-2 citations on disk, and scrutinized the Front-3 `build_mesh` deferral hardest (the whole point of the probe is to catch a missed in-scope hole).

### Checks run

**citation-validity — pass.** I re-ran `python3 tools/graded-stack-lint/graded_stack_lint.py` and confirmed every headline number the report rests on is exact: `rank_violations: 0`, `promotion_frontier: 8`, `detritus: 127`, `detritus_with_typed_edges_stronger_signal: 23`, `reachable: 132`, `roots: 36`. I then verified the three load-bearing pinpoint citations on disk: (1) `palace/linalg/ksp.cpp:53-56` — the MINRES/BICGSTAB/DEFAULT case falls through to `MFEM_ABORT("Unexpected solver type for Krylov solver configuration!")` (read :48-60; the abort is at :56, the report's `:53-57` range correctly encloses the case labels + abort). (2) `book/src/L4/krylov-step.md:14-15` — the typed `composes` edge points to `L2/orthogonalize` with the explicit inline note "no L4 orthogonalize op exists, so the body edge crosses to the L2 named composition the kernel folds." (3) `book/src/L3/fold_solve.md:5-6` — `lifts_from: book/src/L4/fold_solve.md`, confirming the typed edge runs L3→L4 (UP). All resolve in-range and back the claims they support.

**surface-or-evidence — pass (not applicable to observation-only kind).** The report modifies no operator/theme surface and makes no new per-op algebraic claim; it is a coverage/reachability sweep whose evidence is the linter state + on-disk RE/§Status reads. No record-definition obligation applies (no signature naming a new record). This is a pure negative-result observation, which is allowed.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted; the report's content is a frontier-exhaustion audit, not a layer-to-layer rotation.

**variant-axis-coverage — pass (not applicable).** No operator/theme with variant axes is proposed; the audit enumerates an already-ratified RE set.

**cross-reference-integrity — pass.** The 23 STRONGER-GARBAGE members the linter reports match the report's RE decomposition EXACTLY, member-for-member: RE6=8 (L2/L3 axpy/axpby/axpbypcz + L2/L3 scal) + RE7=4 (L2/L3 elementwise_product + L3/assemble-diagonal + L3/jacobi-smoother) + RE8=2 (L3/fold_solve, L3/krylov-step) + RE1=3 (L4/preconditioning-framework, L2/jacobi-smoother, L3/chebyshev) + RE2=1 (L3/orthogonalize) + RE5=5 (L1/L2/L3 normalize + L2/L3 reciprocal) = 23, zero undispositioned. I cross-checked each against `scaffolding/graded-stack-baseline-exceptions.md` (RE1-RE5 §116-136; RE6-RE8 §140-154) — the membership and the §2f GROUND dispositions the report re-checks (RE2 unfaithful because krylov-step composes L2/orthogonalize not the L3 view; RE8 unfaithful because the `lifts_from` edge runs UP) are faithfully restated from the ledger and confirmed against live prose. The promotion_frontier of 8 also matches the linter set exactly.

**edge-label-fidelity — pass.** The report's two would-be-ground edge analyses discuss the exact edges they label: RE2's `L4/krylov-step → L3/orthogonalize` candidate is correctly adjudicated against the actual on-disk `L4/krylov-step → L2/orthogonalize` composes edge (the L4→L2 altitude is faithful); RE8's `transient/lifecycle → L3/fold_solve` candidate is correctly adjudicated against the actual L3→L4 `lifts_from` (UP) edge. The edge directions in the prose match the on-disk typed edges I read.

**plan-kind-consistency — pass.** Declared kind is "Coverage gap (NEGATIVE result)" / observation-only; the content shape (exhaustive sweep confirming no gap, no mis-gate, no missed ground; recommendation "Defer / record the negative verdict") matches an observation entry. No firm/rough-in apparatus is claimed, none expected.

**skill-uptake-survey — pass.** The probe invokes the graded-stack linter (`--json`, `--show-inbound`) as its core mechanical instrument, and reads the RE ledger + §Status lines + typed edges directly — the relevant tooling for a reachability/exhaustion audit is referenced and used.

### Front-by-front verdict scrutiny

**Front 1 (no missed faithful ground) — SOUND.** The 23-member RE map is exact (verified above). I ran `--show-inbound` and confirmed the decisive check: every inbound edge into the 23 points at ANOTHER garbage node or is absent (the absorbed-below-combinator leaves), and no reachable consumer points at any of the 23. The two most-plausible would-be grounds are correctly judged unfaithful on disk: krylov-step's typed edge is to `L2/orthogonalize` (not L3), and `L3/fold_solve`'s `lifts_from` runs UP to L4 — forcing either would assert a non-existent constituent-use. No missed faithful ground.

**Front 2 (promotion_frontier all gated) — SOUND.** The 8 frontier members match the linter. Spot-checked gates resolve: `ksp.cpp:53-56` is a real `MFEM_ABORT` (bicgstab/minres `obstruction (enum-only-stub)`, correctly NOT a clean pick per §Scope unimplemented-component policy); the deflate/eigsolve-reason/boundary-mode gates are each a `partly-constructive` / demand-gate / unhomed-own-readout gate as described. No mis-gated clean pick.

**Front 3 (no true coverage holes) — SOUND, scrutinized hardest.** I checked whether `build_mesh` is a genuine tracked deferral or a hand-waved hole. The lifecycle.L1 dep-map row (`lifecycle.L1.md:67`) confirms `mesh::Load/Partition/RefineMesh` is marked "— (L0 scaffold)" with no link, exactly as described. The constituent decomposition is consistent with CLAUDE.md §Scope: `Partition` is MPI/`Par*` → out of scope; `RefineMesh` is MFEM-opaque (obstruction-documented, not filled); `Load` is the standing candidate-(c) "Mesh-wrapper vocabulary proper" deferral. The priorities.md anchors back the claim — item 5(c)/6(c) at :801/:816 name the Mesh-wrapper deferral, and the CLEAN-GATE ruling at :848 ("what the mesh can't cleanly say ... is a spine-finding, not a forced land") is verbatim. §Scope does say mesh/FE-space construction is IN scope, but it ALSO carves out Par*/distributed and MFEM-opaque-leaf; build_mesh's content falls in those carve-outs, so the deferral is principled, not hand-waving. The probe scrutinized the correct candidate and reached a defensible verdict.

**Two benign linter-semantics caveats — confirmed real measurement notes, not content defects.** I confirmed `roots: 36` = 12 columns × 3 levels (L4/L1/L0; L2/L3 feature chapters omitted per "only where reshaped"), reconciling the "40 columns" task-brief headline as a counting convention, not a missing column. I also confirmed `feature/boundary-mode.{L0,L1,L4}` appears in BOTH the `roots` set AND the `promotion_frontier` set — so the `seed` root is double-counted into the "8", exactly as Caveat-2 flags. Both are accurate linter-convention observations the meta-phase may want to reconcile in the headline number; neither is a content finding.

### Issues found

None. Every load-bearing claim in the report verifies against the live linter state, the RE ledger, and on-disk source. The numbers are exact, the RE membership is complete (zero undispositioned), the unfaithful-ground judgments (RE2, RE8) are correct against on-disk typed edges, the Front-2 gates are real, and the Front-3 `build_mesh` deferral is principled per §Scope. The two self-flagged caveats are genuine measurement-convention notes, correctly framed as linter-semantics questions for the meta-phase rather than holes. The negative verdict ("exhaustion CONFIRMED") is sound and may be relied on for the batch-37 terminal-state decision.

Minor, non-blocking observation (not an issue requiring repair): the report's priorities.md line-anchor glosses (`:801#5c`, `:816#c`) use an informal `#<item>` suffix rather than a plain line range; the cited content is present and correct at those lines, so this is cosmetic citation style, not a drift.
