---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T091500Z
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

# META: verification of "L2 observation — correction_step wider propagation reaches L1 smoother + GMG columns as a DOWNWARD annotation, not a depends-on edge"

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` returns 9 ok / 0 failing (path-hygiene + bounds clean). The two load-bearing source ranges were independently read **on-disk** (not trusting the report's codemap-`read_range` provenance, per the codemap-is-not-source-of-truth rule): `distrelaxation.cpp:101-119` and `gmg.cpp:172-205`. Every pinpoint the report makes is exact against the on-disk text — distrelaxation `:104` primary comment, `:106` `B->Mult2`, `:108` aux comment, `:109-110` residual `A->Mult; AXPBY`, `:111` `RealMultTranspose(*G,...)`, `:112-115` ess-pin, `:116` `B_G->Mult2`, `:117` `RealAddMult(*G,...)`; gmg `:176` contract comment "compute Y <- Y + B (X - A Y)", `:184` `B[l]->Mult2`, `:187-188` residual + `AXPBY(1.0, X[l], -1.0, R[l])`, `:191` `RealMultTranspose(*P[l-1],...)`, `:196` `VCycle(l-1)`, `:199-200` `RealMult(*P[l-1],...); Y[l]+=R[l]`, `:204` `MultTranspose2`. The book-file claims also verify: all four referenced book files exist, and `grep -c correction_step` = 0 in the three would-be-back-link targets, exactly as the report states.

**surface-or-evidence — pass (not applicable to observation kind).** This is a same-layer-cross-cutter observation that surfaces and recommends; it mutates no operator/theme surface. No rotation_claim is asserted. Record-definition sub-check: the combinator `correction_step` named throughout has its definition home in the firm `L2/correction_step.md` (signature, six laws, variant axes, status) — it is only *referenced* here, not newly named-without-a-home.

**rotation-quality — pass (N/A).** No algebraic/structural/reduction rotation is asserted by an observation report; the combinator's compaction-over-the-smoother-family already lives (firm) in `L2/correction_step.md`. No-op for this kind.

**variant-axis-coverage — pass (N/A).** The observation does not introduce or modify a variant-axis-bearing operator. The B-slot / initial-guess axes are enumerated in the combinator's own chapter, out of this report's scope.

**cross-reference-integrity — pass.** All four referenced book files exist (`L2/correction_step.md`, `L1/multigrid-relaxation-smoother.md`, `feature/geometric-multigrid-preconditioner.{L1,L4}.md`). The proposed link target `../L2/correction_step.md` resolves from `feature/`. Layer attributions are correct on disk: `multigrid-relaxation-smoother` is `layer: L1` with `depends-on` edges all to L1 primitives (`chebyshev-smoother`, `apply_linop`, `axpby`, `interpolator`) — none pointing up; the GMG columns are `level: L1` and `level: L4`. The report's claim that the L1 smoother is already well-grounded in L1 vocabulary (and does not NEED the L2 combinator) is verified against its frontmatter.

**edge-label-fidelity — pass; the load-bearing claim is sound.** The two central edges are (a) L1↛L2 (the smoother / GMG-L1 column CANNOT `depends-on` the L2 combinator → downward annotation, not an edge) and (b) L4→L2 reference (permitted). The prose discusses exactly these edges. I verified the layer-direction reasoning against the CLAUDE.md invariant "Layers are defined high→low; lifting notes go in working notes" (higher-layer entries are defined in own-layer or *higher*-layer references, NOT lower-layer vocabulary): an L1 entry referencing an L2 abstraction as a definitional/blocking edge would define L1 in *higher*-layer vocabulary — forbidden; an L4→L2 reference is a downward reference — permitted. The report also correctly separates the **rank** well-foundedness invariant (`rank(u) ≤ rank(v)`, maturity — which would actually *permit* firm(L1)→firm(L2) since both are rank 3) from the **independent L-layer-direction** rule that does the forbidding (lines 64-68). That distinction is accurate and is the crux of the correct verdict. The combinator's own §"L2 vs lower-layer distinction" ("There is no L1 `correction_step` primitive — the body is realized per-smoother") corroborates the downward-annotation framing.

**plan-kind-consistency — pass.** Declared an observation ("Observation kind: Shared sub-pattern … the actionable surface is a layer-direction-constrained reference-wiring observation"); the content surfaces a per-site verdict + three follow-up candidates and enacts nothing (routing to harvester / combinator-miner / layer-intro-author). Content shape matches the observation kind.

**skill-uptake-survey — pass (telemetry only).** The report references codemap `read_range` for localization and the planner `ls` for the no-distrelax-chapter confirmation. No skill is strongly implied by a same-layer-cross-cutter observation shape. Telemetry note (non-blocking): the report relied on codemap `read_range` for its source pinpoints rather than self-invoking `citecheck --anchor`; the lines happened to be correct (I confirmed on-disk), and the combinator chapter it cross-references DID self-verify via `citecheck --anchor`, so no drift surfaced — but the producer leaning on `read_range` for load-bearing pinpoints is the recurring `producer-citation-drift-verify-not-self-invoked` shape worth noting.

### Issues found

None. All 8 checks pass.

The verdict's load-bearing claim — that the L1 sites resolve to a downward annotation (not a `depends-on` edge) while only the L4 column admits a `reference`-class edge to `L2/correction_step` — is correctly derived from the high→low layer-direction invariant and independently verified against the on-disk frontmatter of all four chapters and the two Palace source ranges. The conjugation-law instances (`B=T·B'·Tᵀ`, T=G for the auxiliary leg, T=P for the coarse-grid leg) match law 6 of the combinator chapter and the cited source bodies. The over-unification guards (bare B apply, Krylov shift-invert, libCEED quadrature, divfree-projector borderline) are correctly reported as respected — each matches the combinator chapter's §"Over-unification guards" / §Borderline. The "distributive-relaxation has no separate L1 chapter, so site #2 is subsumed by site #1" claim is confirmed (`ls book/src/L1/` shows no distrelax chapter).
