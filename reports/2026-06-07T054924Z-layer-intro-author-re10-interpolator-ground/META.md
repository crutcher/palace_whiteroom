---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T061500Z
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

# META: verification of D8 — re10-interpolator-ground (RE10 discharge: ground L1/interpolator via two faithful depends-on edges)

## Critique

### Checks run

**citation-validity — pass.** Both load-bearing source pinpoints were independently re-read via the palace-codemap `read_range`, NOT taken from the producer's chain-of-thought. `palace/linalg/divfree.cpp:117` is verbatim `Grad = &nd_fespace.GetDiscreteInterpolator(h1_fespaces.GetFinestFESpace());` (read `:111-120`). `palace/drivers/boundarymodesolver.cpp:319-323` contains `const auto &CurlOp = mode_op.GetCurlSpace().GetDiscreteInterpolator(mode_op.GetNDSpace());` (the call body spans `:320-321` within the cited `:319-323` range; read `:315-335`) — followed by `CurlOp.Mult(et.Real(), curl_etr)` / `Mult(et.Imag(), curl_eti)` forming `Bz`, exactly the prose's claim. `citecheck --scan` on CYCLE.md returns `7 ok, 0 failing` — all citations in-bounds, no path-hygiene issues, no drift. The cross-reference `L1/interpolator.md:42-43` (which formalizes `GetDiscreteInterpolator`) was confirmed against the target on disk.

**surface-or-evidence — pass.** This is a graded-stack GROUND (reachability-GC) dispatch, not a refinement-shaped operator/theme change: it adds typed `depends-on (kind: uses)` edges + supporting §Dependencies prose to two consumer chapters. The producer correctly takes the §2f GROUND disposition over remove/route — `interpolator` is a genuine, citation-grounded dependency of reachable goal nodes whose only defect was a missing typed edge. The supporting evidence (the two on-disk source reads + the pre-edit linter read) substantiates every structural claim. No record-definition gap: `interpolator` (the named operator) already has its full in-chapter definition home in `book/src/L1/interpolator.md`; no new record is named.

**rotation-quality — pass (not applicable to GROUND/edge-typing kind).** The dispatch asserts no algebraic/structural/reduction rotation — it types two dependency edges to discharge a reachability-GC garbage node. No L_{n+1}→L_n compaction claim is made, so the rotation-strictness criterion does not apply.

**variant-axis-coverage — pass.** No new operator/theme with variant axes is introduced; the edges attach to already-firm consumers whose own variant axes are unchanged. The `interpolator` de-Rham-edge variant axis (Grad/Curl-3D/Curl-2D/Div) is already documented in the target chapter and is not touched. Nothing to scope out.

**cross-reference-integrity — pass (load-bearing here, verified).** Both edge targets resolve to real on-disk chapters: `book/src/L1/interpolator.md` (the full `book/src/L1/...` path used, disambiguating the bare-basename `interpolator` AMBIG the planner flagged — good). Both new prose links (`[interpolator](./interpolator.md)` in divfree-projector, `[interpolator](../L1/interpolator.md)` in waveguide_mode_reduce) resolve. Both consumer chapters exist and carry `rank: firm`; the target `interpolator` carries `rank: firm`. Well-foundedness `rank(u) ≤ rank(v)` holds at firm/firm (3 ≤ 3) for BOTH edges. Independently re-ran `graded_stack_lint.py`: `L1/interpolator` is confirmed in the STRONGER GARBAGE list pre-edit; both consumers (`L1/divfree-projector`, `L4/waveguide_mode_reduce`) are absent from the garbage list (reachable) — so the inbound edges genuinely propagate liveness, exactly as claimed.

**edge-label-fidelity — pass (the focus check).** Both edges are genuinely faithful, independently confirmed at L0:
- Edge 1 (`L1/divfree-projector → L1/interpolator`, within-L1): the cited `divfree.cpp:117` IS a `GetDiscreteInterpolator` call constructing the `Grad` operator divfree-projector uses in steps 1/4. The prose discusses exactly this within-L1 construction-vs-application distinction (a build-time `uses` edge distinct from the run-time `apply_linop` edge) — accurate.
- Edge 2 (`L4/waveguide_mode_reduce → L1/interpolator`, L4→L1 altitude-skip): the cited `boundarymodesolver.cpp:319-323` IS a `GetDiscreteInterpolator` call constructing the discrete-curl `CurlOp` the `Bz = curl(Et)/(iω)` formation applies. The prose labels and discusses the exact altitude-skip edge it adds; the altitude-skip is justified by the reduce verb's own §Lowers-to ("identity-in-form on the body … no intervening L3/L2 absorption"), which I confirmed in the target chapter (`:226-236`). The source genuinely calls the L1 interpolator's exact lift directly, so there is no intervening L3/L2 node to route through — the L4→L1 edge is faithful, not forced.

**plan-kind-consistency — pass.** The dispatch declares itself a RE10 GROUND/edge-typing discharge; the content (two `depends-on (kind: uses)` edge additions + §Dependencies prose, no new chapter, no algebraic claims) matches that kind exactly. No firm-operator placeholders, no mis-classification.

**skill-uptake-survey — pass.** The shape implies the citecheck + graded-stack-lint procedures; the report references both (`citecheck --anchor`, `graded_stack_lint.py --show-inbound`) and the on-disk `read_range` verifications. Telemetry-positive.

### Issues found

None. All eight checks pass. The two source sites verify verbatim on disk; both edges are genuinely faithful `GetDiscreteInterpolator` invocations (no forced edge); the AMBIG is disambiguated with full `book/src/L1/...` paths; well-foundedness holds firm/firm; the pre-edit GARBAGE state and the consumers' reachability are both independently confirmed by re-running the linter. The two Open-questions caveats (the harmless backward `reference` note at `interpolator.md:23`; the post-landing c122 re-measure of the `27→25` count) are correctly scoped out of this dispatch and flagged rather than silently dropped. Clean report — `overall_status: ready` set.
