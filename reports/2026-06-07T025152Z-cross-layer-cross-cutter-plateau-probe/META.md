---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T033000Z
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

# META: verification of c120 D1 plateau-probe terminal-state audit

## Critique

This is an OBSERVATION-ONLY plateau-confirmation report (the c115 D1 precedent): no
`book/` mutation, no proposed-changes block. It emits a terminal-state verdict + 2 structured
findings for the batch-38 meta-phase to migrate. Per the critic role-spec the rotation /
variant-axis / edge-label / plan-kind-as-operator-entry checks no-op; the load-bearing job is
verifying the two findings are SOUND (a false finding would mislead the meta-phase's
terminal-state decision). I verified both findings on disk + via codemap, re-ran the linter,
and spot-checked the cited anchors. Both findings are sound and the verdict's coverage sweep
is corroborated.

### Checks run

**citation-validity — pass.** The two load-bearing L0 anchors verify exactly on the Palace
source (read via codemap `read_range`, the line-map source-of-truth). `boundarymodesolver.cpp:319-323`
contains the `Bz` formation block with `const auto &CurlOp = mode_op.GetCurlSpace().GetDiscreteInterpolator(mode_op.GetNDSpace());`
(line 321-322) followed by `CurlOp.Mult(et.Real(), curl_etr)` (line 323) — exactly as the report
quotes. `divfree.cpp:117` contains `Grad = &nd_fespace.GetDiscreteInterpolator(h1_fespaces.GetFinestFESpace());`
— the discrete-`Grad` interpolator, as cited. The book-side cites resolve: `interpolator.md`
opening paragraph (lines 35-38) names both consumers; `divfree-projector.md:99-100,319` cites
`divfree.cpp:117`; `waveguide_mode_reduce.md:218-234,296,326` narrates the discrete-curl
interpolator at `:319-323`. The linter baseline the report re-confirmed
(`files=369, reachable=139, roots=39, detritus=132, STRONGER=27, rank_violations=0, untyped=61,
promotion_frontier=6, unresolved=0`) reproduces EXACTLY on a fresh on-disk run.

**surface-or-evidence — pass (adapted: observation-only).** No surface mutation is proposed, so
the refinement-shaped surface-or-evidence gate is not triggered. The findings are evidence-backed
observations, each carrying its L0 + book-side citations. No un-homed signature-named record is
introduced.

**rotation-quality — pass (not applicable to observation-only report).** No algebraic/structural
rotation is asserted; the report recomposes existing reachability/grounding facts.

**variant-axis-coverage — pass (not applicable to observation-only report).** No operator/theme
with variant axes is proposed.

**cross-reference-integrity — pass.** All cross-references in the findings resolve on disk:
`L1/interpolator.md`, `L4/waveguide_mode_reduce.md`, `L1/divfree-projector.md`,
`feature/waveguide-mode.{L0,L1,L4}.md`, `feature/index.md`, `feature/output-product.md` all exist.
The RE-set node names in the STRONGER=27 reconciliation map to real book chapters; I spot-confirmed
`L1/interpolator` + `L1-L0/interpolator-construction-rotation` + `L1/fe_space_hierarchy` ARE in the
linter's STRONGER-garbage list, and the two named consumers are NOT in the detritus list (i.e.
reachable) — both load-bearing reachability claims hold.

**edge-label-fidelity — pass (not applicable as authored, but the proposed-edge directions are
correct).** No L_{n+1}→L_n edge label is carried on an authored chapter. The two recommended
grounding edges are direction-checked: `L4/waveguide_mode_reduce → L1/interpolator` (L4→L1
altitude-crossing constituent-use) and `L1/divfree-projector → L1/interpolator` (L1→L1
constituent-use) both point consumer→producer, the correct `depends-on` direction, and the report
itself flags the L4→L1 altitude crossing as needing the layer-intro-author to confirm the
convention against existing `feature → L1` precedents — an appropriately-hedged caveat, not an
over-claim.

**plan-kind-consistency — pass.** The declared kind (observation / pre-meta audit) matches the
content shape: a verdict + findings + recommendations, no proposed-changes block, explicit
"no `book/` mutation performed" discipline statement. Correctly classified as observation, not a
firm/rough-in authoring entry.

**skill-uptake-survey — pass.** The report references on-disk linter re-runs
(`graded_stack_lint.py`) and codemap `read_range` localization, the relevant procedures for a
plateau-probe sweep. No additional skill invocation is implied for an observation-only audit.

### Findings verified (the load-bearing job)

**FINDING-1 (missed §2f GROUND edge for RE10) — SOUND.** The central correctness question is
whether the report conflates "uses a discrete derivative" with "composes the `interpolator` op
node". It does NOT. Both consumers call `GetDiscreteInterpolator` — the *exact* accessor
`L1/interpolator` formalizes (`fespace.hpp:107`, cited in-chapter):
(a) `waveguide_mode_reduce`'s `Bz` formation calls `GetCurlSpace().GetDiscreteInterpolator(GetNDSpace())`
then `CurlOp.Mult(...)` (`boundarymodesolver.cpp:321-323`) — a genuine apply of the
interpolator-produced `LinOp`;
(b) `divfree-projector` reads `Grad = &nd_fespace.GetDiscreteInterpolator(...)` (`divfree.cpp:117`)
— the discrete-`Grad` interpolator.
The faithfulness premise holds. The reachability premise holds: `L1/interpolator` IS in the
STRONGER-27 garbage set (confirmed via linter), both consumers ARE reachable firm nodes (firmness:
firm / rank: firm confirmed in both chapter frontmatters; neither appears in the detritus list), and
NEITHER consumer carries a `depends-on` (or any) edge to `L1/interpolator` (confirmed by reading
both `edges:` blocks — `waveguide_mode_reduce` depends-on = {eigsolve, cites-evidence};
`divfree-projector` depends-on = {mutation-rotation theme, ksp_solve, apply_linop, axpy}). Both
relationships ARE already prose-documented (`interpolator.md:35-38` names both;
`divfree-projector.md:99,319`; `waveguide_mode_reduce.md:218-234,296,326`). So a faithful typed
`depends-on` edge from either reachable consumer down to `interpolator` would genuinely flip RE10
live and discharge the baseline-exception — exactly the §2f GROUND case the report claims. Well-
foundedness holds (3≤3, all three nodes firm). The RE9 contrast also holds: `fe_space_hierarchy`
is likewise STRONGER-garbage but its "no consumer yet" premise is genuinely correct (its prospective
multigrid-preconditioner consumer is unbuilt). The asymmetry the report rests FINDING-1 on (RE9
premise survives, RE10 premise falsified by c118's landing of `waveguide_mode_reduce`) is real.

**FINDING-2 (consistency drift) — SOUND.** Confirmed on disk: `feature/waveguide-mode.L0.md` is
still `rank: rough-in` (frontmatter line 6) with a `## Status` note citing the now-resolved
`waveguide-mode-reduce-needs-l4-verb-home` gate, while `.L1.md` / `.L4.md` are both `rank: firm`
(flipped c118 D5) — and `waveguide_mode_reduce.md` is itself `firmness: firm / rank: firm` (the
gate's resolution). The index/group-intro surfaces are stale: `feature/output-product.md:39`
("**The column is `seed`** (own reduce verb rough-in)" + "is the sole **`seed`** output-product
column — its own reduce verb `waveguide_mode_reduce` is rough-in") and `feature/index.md:69,82`
("only `waveguide-mode` remains `seed` ... promotes once that verb firms" / "has no firm L4 verb
home yet"). All three stale surfaces named in the report reproduce verbatim. The report's nuance
is also correct: `feature_root: seed` IS correctly retained on all three levels (confirmed: all
carry `feature_root: seed`) — that token is the permanent GC-root marker, not a maturity tier; the
drift is only the maturity prose. This is the index-cell drift the OWN-COMPOSITION mechanics exist
to catch.

**Verdict coverage-hole sweep — corroborated.** `ls book/src/feature/` shows all 5 drivers +
lifecycle spine-root (3 levels) + 6 output products (incl. waveguide-mode) + boundary-mode;
`ls book/src/L1/` shows the full mesh / fe_space / assembly cohort (build_mesh, fe_space,
fe_space_hierarchy, fe_collection, essential_dofs, interpolator, fe_assemble, bilinear-form,
assemble-diagonal, assemble_frequency_operator). The "NONE" coverage-hole claim is not obviously
wrong. The promotion-frontier=6 gating rationale (2 obstruction, 1 partly-constructive, 2
demand-gated deflate, 1 = the FINDING-2 stale L0 level) is internally consistent.

### Issues found

NONE blocking. The report is an internally-consistent, on-disk-verified observation. Both findings
are sound and correctly typed as low-fan-out honesty/fidelity cleanups for the meta-phase to
migrate (not proposed-changes for this cycle). One minor, non-blocking note for the meta-phase's
downstream consideration (NOT a defect in this report): FINDING-1's recommended L4→L1
altitude-crossing edge (`waveguide_mode_reduce → interpolator`) should have its edge-convention
confirmed against the existing `feature → L1` grounding precedents before authoring — which the
report itself already flags as a caveat (Open questions / caveats, the FINDING-1 caveat bullet).
The safer minimal grounding (`divfree-projector → interpolator`, an L1→L1 constituent-use) alone
suffices to discharge RE10, as the report notes. This is forward-authoring guidance, not a
correctness problem with the audit.

All 8 checks pass; this is an all-pass clean observation report with nothing to repair, so the
critic sets `overall_status: ready`.
