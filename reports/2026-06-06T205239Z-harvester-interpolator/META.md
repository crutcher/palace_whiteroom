---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T214500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
# rank-invariant (graded-stack check 9): warning
# reachability (graded-stack check 10): pass
repaired_at: 2026-06-06T221500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
  rank-invariant: repaired
  reachability: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize interpolator at L1"

## Critique

### Checks run

**citation-validity — warning.** `citecheck --scan` clears all 34 citations on bounds + path-hygiene (34 ok, 0 failing). I anchor-verified every load-bearing pinpoint: `fespace.cpp:173-238` (`BuildDiscreteInterpolator`, anchor at 173), the `forward`/`swap` direction pin `:179-185` (anchor at 180,184), the four de-Rham branch kernels (`GradientInterpolator` @195 in `:191-198`, `CurlInterpolator` @204 in `:200-208`, `LoseMat` @219 in `:209-223`, `DivergenceInterpolator` @227 in `:225-231`), the unsupported-pair abort `MFEM_ABORT` @233 in `:231-234`, the accessor `:104-115` + `G.reset()` cache @111, the Palace-owned `DiscreteLinearOperator` @95/105 + `AddDomainInterpolator` @115 in `bilinearform.hpp:95-115`, the GSLIB anchors (`InterpolateFunction` decls @52/56, both bodies, `FindPointsGSLIB` @190/293), and all six consumer sites. The `:238` body END (close brace) is confirmed by direct on-disk read — the producer's claim holds. **The one inaccuracy:** in **Variant axes** (CYCLE.md §Variant axes / Semantics narration) the report labels `palace/models/curlcurloperator.hpp:112` as "the curl-curl operator's **gradient**" — but that site is `GetCurlMatrix() { return GetCurlSpace().GetDiscreteInterpolator(GetNDSpace()); }`, i.e. a discrete **curl** (ND→RT/L2), not a gradient. The site is a correct de-Rham-edge witness, so the structural claim stands; only the per-site descriptive label is wrong. (`curlcurloperator.hpp` has no `GetGradMatrix`; `GetGradMatrix` is the separate `spaceoperator.hpp:224-227` site, correctly labelled.) Localized prose mislabel, not a citation-out-of-range — hence `warning`, not `fail`.

**surface-or-evidence — pass.** This is a new firm L1 operator entry (not a refinement of an existing operator), so the rotation_claim-vs-surface gate is the firm-on-positive-structure test, which holds robustly. The map-type dispatch is genuinely exhaustive over the four de-Rham edges with all others aborting — I read the full `fespace.cpp:173-238` body: VALUE→H_CURL (Grad), H_CURL→H_DIV (Curl-3D), H_CURL→INTEGRAL (Curl-2D native), H_DIV→INTEGRAL (Div), and a terminal `else { MFEM_ABORT(...) }`. The firm-on-positive-structure escape is correctly invoked (syntactic-identity laws on fully-read positive source; the no-dedicated-test caveat is non-gating per the `fe_space`/`fe_assemble`/`apply_linop` precedent). The GSLIB negative-finding exhaustiveness is genuinely established per skill `establish-negative-finding-exhaustiveness`: I independently grepped `interpolator.cpp` — every interpolation entry point (`InterpolationOperator` ctor + ×2 `ProbeField`, `InterpolateFunction` ×2, `ComputeLineIntegral`) is `#if defined(MFEM_USE_GSLIB)`-guarded with an `MFEM_ABORT`/`MFEM_VERIFY` GSLIB-absent fallback (@71,108,278,304,363) and there is no GSLIB-independent Palace-internal interpolation body. The report's cited anchor set matches the grep. Record-definition sub-check: the signature names `FiniteElementSpace` and `LinOp`; both already have definition homes (`fe_space` chapter; `apply_linop` / `concepts/constructed-operators`) and are merely referenced, so no new record needs a home — pass.

**rotation-quality — pass.** The ND→RT domain≠range `LinOp[(R: ...), (D: ...)]` notation is correct and load-bearing: the produced operator is genuinely rectangular (`R ≠ D`), and the report ties this to the existing `apply_linop` M≠N note (`apply_linop.md:36` explicitly lists `Grad`: H1→Nedelec as a genuine rectangular case — verified). This is an L1-operator harvest, not a cross-layer rotation claim; the "rotation" here is the L0→L1 purification (dropping the cached `unique_ptr G` + mutate-on-miss idiom; rebuilding the construction as a pure function of the two spaces), which is a genuine state-hiding compression, not a rename. Pass.

**variant-axis-coverage — pass.** The de-Rham-edge axis is named THE load-bearing variant axis and fully enumerated `{ Grad (H1→ND), Curl-3D (ND→RT), Curl-2D (ND→L2), Div (RT→L2) }`, each witnessed at a construction site, and all are absorbed into the single `interpolator` selecting on the `(aux_map_type, primal_map_type)` pair + dimension — not hidden branches. The assembly-representation axis (2D native vs libCEED PA) is explicitly scoped out as a transparent representation choice deferred to the L1>L0 lowering. The `Par*` axis is scoped out single-rank per CLAUDE.md §Scope. No hidden branches. Pass.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: `apply_linop.md`, `fe_space.md`, `divfree-projector.md`, `semantics/index.md` (§1.2.1–§1.2.3 present and matching the named-shape-group / `LinOp[(R:...),(D:...)]` convention — and correctly USE+LINKed, not restated, per the SEMANTIC-CONSOLIDATION discipline), `concepts/constructed-operators.md`. The new `book/src/L1/interpolator.md` does not already exist (clean create). The L1/index.md edit anchors are exact: the OLD Vocabulary-cohort bullet at line 112 matches verbatim; the dep-map row inserts at alpha position after `fe_space` (line 173, the last firm FE-space-sub-spine row). The SUMMARY.md insertion lands inside the correct `[FE-space sub-spine]` sub-chapter group at the right alpha slot (after `fe_space`, since `interpolator` sorts after it within that group). The forthcoming `L1-L0/interpolator-construction-rotation` theme is correctly written as a plain-text slug everywhere (dep-map `target:` + prose "forthcoming"), NOT a live markdown link — avoiding a linkcheck2 hard error. The divfree-projector forward-ref claim is accurate (`divfree.cpp:117` = `Grad` discrete interpolator; divfree-projector.md:98-99 names it the H1→Nedelec discrete interpolator). Pass.

**edge-label-fidelity — pass.** The obstruction sub-kind `obstruction (opaque-library-ownership)` is correctly applied to the GSLIB leaf: the entire facility lives behind `mfem::FindPointsGSLIB` (an external library boundary), Palace never exposes a standalone callable, and the promotion route is correctly stated as NONE — matching the CLAUDE.md sub-kind definition (vs `enum-only-stub`, which would be a Palace-owned TODO body; this is not that). The GSLIB sibling is correctly kept SEPARATE from the firm discrete operator: it is `palace/fem/interpolator.*` (GSLIB point-interp) vs `palace/fem/fespace.*` (de-Rham `DiscreteLinearOperator`), the report states they "share a directory and the word 'interpolate' but are different operations," and the firm claim does not fold the obstruction. The single `depends-on` `lowers-to` edge label (`L1-L0/interpolator-construction-rotation`) matches the prose ("L1>L0 construction-rotation"). Pass.

**plan-kind-consistency — pass.** Declared kind is a `firm` L1 operator harvest; the content shape matches — full Signature / Semantics / Algebraic-laws / Variant-axes / Dependencies / Status / Evidence sections, all populated, no rough-in placeholders. The obstruction sub-note is correctly an in-chapter sibling (facility-level boundary adjacent to the operator), not mis-declared as a separate theme. The body is authored INSIDE the ` ```new:book/src/L1/interpolator.md ` fence (the `## Operator content` section after the fence is an empty pointer back to it, not an outside-the-fence firm body) — no fence-truncation defect. Pass.

**skill-uptake-survey — pass.** The report's shape (a firm harvest with a co-located obstruction disposition) implies two skills, and both are referenced: `establish-negative-finding-exhaustiveness` (invoked by name for the GSLIB scan) and `citecheck --anchor` (invoked for self-verification, with the codemap range-END drift guard correctly applied — the `:238` END confirmed by direct on-disk Read, not a `read_range`). Pass.

**rank-invariant (graded-stack check 9) — warning.** The entry is `firm` (rank 3) and carries exactly one `depends-on` edge: `lowers-to` → `L1-L0/interpolator-construction-rotation`. That theme does **not exist yet** (the report flags it "forthcoming"), so its rank is undefined (effectively rank 0). The well-foundedness note (CYCLE.md §Status, lines 332-335) asserts "No `depends-on` edge rests on a sub-firm node, so the firm rank is well-founded" — but the `lowers-to` target is neither firm nor authored, so that statement is, as written, not accurate. Compare the sibling precedent `fe_space.md`: it carries the identical-shape `lowers-to` `depends-on` edge to `L1-L0/fe-space-construction-rotation` — but that theme EXISTS and is `status: firm` (rank 3 ≤ 3), and the fe_space frontmatter comment explicitly cites that fact to discharge the invariant. The FE-space-sub-spine convention has been to co-author the L1 operator and its L1>L0 rotation theme as a paired dispatch precisely so the invariant stays clean; here the rotation theme is deferred. This is a real (if soft) graded-stack tension worth surfacing — flagging `warning` rather than `fail` because (a) `lowers-to`-to-a-forthcoming-theme is the documented forward-ref pattern and the report flags the gap in Open questions (`interpolator-construction-rotation-l1-l0-theme-needed`), and (b) the firm claim itself rests on positive L0 source, not on the lowering theme.

**reachability (graded-stack check 10) — pass.** The entry is reachable from feature roots over `depends-on`/consumed-by edges: it is consumed by `divfree-projector` (the `Grad` step) and is the operator behind the boundary-mode `Bz = curl(Et)` readout, AMS setup, curl-curl, and post-processing — all on live solver/feature-surface paths. Not garbage.

### Issues found

1. **[citation-validity, warning] Per-site mislabel: `curlcurloperator.hpp:112` is a discrete curl, not a gradient.** In CYCLE.md §Variant axes (the de-Rham-edge axis witness list: "the curl-curl operator's gradient (`palace/models/curlcurloperator.hpp:112`)") the site is described as a gradient, but `curlcurloperator.hpp:110-112` is `GetCurlMatrix() { return GetCurlSpace().GetDiscreteInterpolator(GetNDSpace()); }` — a discrete **curl** (ND→RT/L2). The site is a valid de-Rham-edge witness (so the structural/variant-axis claim is unaffected), and the dep-map/Evidence listings cite it bare without the wrong label; only the Variant-axes descriptive phrase is inaccurate. Repair: change "the curl-curl operator's gradient" to "the curl-curl operator's discrete curl" (or drop the per-site edge label). Severity: low (cosmetic accuracy).

2. **[rank-invariant, warning] Well-foundedness note over-claims; the `lowers-to` `depends-on` target is unauthored.** CYCLE.md §Status (lines 332-335) states "No `depends-on` edge rests on a sub-firm node, so the firm rank is well-founded," but the sole `depends-on` edge (`lowers-to` → `L1-L0/interpolator-construction-rotation`) points at a theme that does not yet exist (rank undefined/0). The firm sibling `fe_space` discharged the identical invariant only because its `fe-space-construction-rotation` theme is authored + `status: firm` (rank 3 ≤ 3). Either the well-foundedness sentence should be softened to acknowledge the `lowers-to` target is a forthcoming forward-ref (the firm rank resting on positive L0 source, not on the lowering theme), or — matching the FE-space-sub-spine paired-dispatch precedent — the `interpolator-construction-rotation` L1>L0 theme should be authored before/with this entry so the edge resolves to a firm node. The report already flags the missing theme in Open questions, so the gap is acknowledged; the defect is the *well-foundedness wording*, which currently asserts a clean invariant that is not yet true. Severity: low-medium (graded-stack accuracy; does not block the firm claim itself).

## Repair

### Fixes attempted

- **Finding**: [citation-validity, warning] §Variant axes mislabels `curlcurloperator.hpp:112` as the curl-curl operator's "gradient"; the site is `GetCurlMatrix` (a discrete curl).
  - **Decision**: repaired
  - **Action**: CYCLE.md §Variant axes (de-Rham-edge witness list) — relabeled "the curl-curl operator's gradient (`palace/models/curlcurloperator.hpp:112`)" → "the curl-curl operator's discrete curl `GetCurlMatrix` (`palace/models/curlcurloperator.hpp:112`)". Verified against on-disk `curlcurloperator.hpp:110-112` via codemap `read_range`: `const Operator &GetCurlMatrix() const { return GetCurlSpace().GetDiscreteInterpolator(GetNDSpace()); }` — a discrete curl (ND→RT/L2), confirming the critic's call. The site is a valid de-Rham-edge witness, so the structural/variant-axis claim is unaffected; this is a per-site descriptive-label correction only. (The §Summary narration at the same site already read "discrete `curl`" correctly — no change needed there.)

- **Finding**: [rank-invariant, warning] §Status well-foundedness note over-claims ("no `depends-on` edge rests on a sub-firm node") while the sole `depends-on` `lowers-to` edge points at `L1-L0/interpolator-construction-rotation`, which does not exist yet — a `depends-on` edge to a non-existent target that would regress the finalize rank-linter's `unresolved_depends_on_targets` 0→1.
  - **Decision**: repaired
  - **Action (frontmatter)**: CYCLE.md ` ```new:book/src/L1/interpolator.md ` frontmatter `edges:` — DEMOTED the forthcoming `L1-L0/interpolator-construction-rotation` theme from a blocking `depends-on (kind: lowers-to)` edge to a navigational `reference:` slug (slug-as-text, with an inline NB comment recording that it is promoted to `depends-on (kind: lowers-to)` once the theme is authored + `status: firm`, rank 3 ≤ 3). The `depends-on:` block is now absent entirely — the firm node carries only `reference:` edges, so there is NO `depends-on` target to resolve and the rank-linter stays `unresolved_depends_on_targets=0`, `rank_violations=0`. Verified against the linter (`tools/graded-stack-lint/graded_stack_lint.py`): both analyses consume ONLY the blocking `depends-on` bit; `reference` edges are navigational and not resolved.
  - **Action (§Status note)**: SOFTENED the well-foundedness paragraph to state the firm rank rests on positive L0 source (rank-terminal ground truth), NOT on the unauthored lowering theme; the `lowers-to` relation is carried as a navigational `reference` until the theme is authored, explicitly avoiding an unresolved-`depends-on` regression; and it cites the `fe_space → fe-space-construction-rotation` precedent (which carries the `lowers-to` `depends-on` edge ONLY because its theme exists and is firm — verified in `book/src/L1/fe_space.md:14,22-23`). OQ `interpolator-construction-rotation-l1-l0-theme-needed` (already present) is preserved as the authoring tracker.
  - **Scheme consistency note**: the fix is consistent with the graded-stack scheme — a `firm` node rests only on ≥-firm or rank-terminal targets, and the thing to avoid is a blocking edge to a non-existent slug. Demoting to `reference` removes the blocking edge without inventing a false `depends-on`; the firm-on-positive-structure rank is independently sound.

### Unrepairable findings

None. Both flagged warnings were mechanical/surgical (a per-site label correction + a frontmatter-edge classification + matching prose softening), within repair authority. No substantive authoring was required — the forthcoming L1>L0 theme is correctly left for a later abstractor dispatch (tracked in Open questions), NOT co-authored here.

## Suggested resolution

`ready`. Notes for the integrator:
- The `book/src/L1/interpolator.md` frontmatter carries NO `depends-on` block (only `reference:` edges), so the finalize rank-linter should report `unresolved_depends_on_targets=0` / `rank_violations=0` unchanged. The forthcoming `L1-L0/interpolator-construction-rotation` theme appears ONLY as a `reference:` slug + plain-text prose mentions (no live markdown link), so it does not create a `linkcheck2` hard error either.
- OQ `interpolator-construction-rotation-l1-l0-theme-needed` should be promoted as usual; authoring that L1>L0 theme is the trigger to later promote the `reference` slug back to a `depends-on (kind: lowers-to)` edge (the `fe_space` paired-dispatch shape).
