---
verifies: ../REPORT.md
critiqued_at: 2026-06-06T235500Z
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
repaired_at: 2026-06-07T000500Z
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
overall_status: ready
follow_up_agent: null
---

# META: verification of interpolator-construction-rotation (L1>L0 theme + coupled L1/interpolator edge upgrade)

## Critique

### Checks run

**citation-validity — warning.** I verified the load-bearing L0 ranges on disk
(`reference/palace/palace/fem/...`; citations are relative to `reference/`, so `palace/fem/...`
resolves correctly through the doubled `palace/palace/` clone prefix). The major anchors are
**accurate**:
- `fespace.cpp:173-238` — `BuildDiscreteInterpolator` full body confirmed: direction pin `:178-185`
  (forward `:178-179`, swap `:180-181`, `MFEM_VERIFY(!swap)` `:182-183`, `MFEM_VERIFY(forward)`
  `:184-185`), trial/test binding `:186-187`, map-type read `:188-189`, Grad `:190-198`, Curl-3D
  `:199-207`, Curl-2D native (libCEED-bypass comment `:211-212`, const_cast `:213-214`,
  `Assemble`/`Finalize` `:217-218`, `LoseMat` `:219`) `:208-221`, Div `:222-230`, abort `:231-235`. All pass.
- `fespace.hpp:107` accessor + `:109-114` lazy cache (`if` `:109`, `G.reset()` `:111`, re-point `:112`,
  return `:114`) + `mutable` members `aux_fespace` `:38` / `G` `:39`. All confirmed exactly.
- `bilinearform.hpp:95-115` — `DiscreteLinearOperator` class `:95`, ctor `:105-109`, `domain_interps`
  container `:102` / push at `:117`. Confirmed.
- GSLIB anchors all confirmed via grep: `FindPointsGSLIB` `:190`/`:293`; `MFEM_USE_GSLIB` guards
  `:27`/`:83`/`:135`/`:285`/`:311`; `MFEM_ABORT` GSLIB-absent fallbacks `:108` (ProbeField) / `:278` /
  `:304` (InterpolateFunction ×2) / `:363` (ComputeLineIntegral).
- Consumer-witness sites all confirmed: `divfree.cpp:117` (Grad), `boundarymodesolver.cpp:322` (curl
  `Bz`), `spaceoperator.hpp:224-227` (GetGradMatrix), `:228-236` (GetCurlMatrix 2D/3D split).

Two imprecisions drop this to `warning` (neither is a load-bearing artifact-block citation — both live
in the CYCLE.md narrative `## Supporting evidence` section, not in the proposed-changes blocks that
become artifact):
1. **AddDomainInterpolator-template -1 drift leaked into the narrative.** The dispatch claims to have
   caught a codemap -1 drift and uses the corrected `bilinearform.hpp:114-115` in the **proposed-changes
   blocks** (the `new:` theme line 182, the `edit:L1/interpolator.md` Evidence line 619) — and that is
   **correct on disk** (`template <typename T...>` `:114`, `void AddDomainInterpolator(...)` `:115`;
   `:113` is blank, `:112` is `GetTestSpace`). But CYCLE.md `## Supporting evidence` line 679 still
   carries the *pre-correction* value "`AddDomainInterpolator` template `:113-114`". So the artifact
   blocks are right; the dispatch's own evidence-log narrative contradicts them with the stale drifted
   value. Internal inconsistency, not an artifact defect.
2. **Second-InterpolateFunction body over-range.** Both the theme (line 219/276) and the L1 entry
   (line 632) cite the point-list `InterpolateFunction` body as `:282-310`, but `ComputeLineIntegral`
   begins at `:308` — so `:282-310` over-runs ~2 lines into the next function (the 2nd
   InterpolateFunction's `MFEM_ABORT` is at `:304`, body ends ~`:306`). Minor over-range; does not
   affect the obstruction claim (the abort/guard anchors inside it are exact).

**surface-or-evidence — pass.** This is a refinement-shaped proposal (a new firm L1>L0 lowering theme +
a coupled surface edit to the existing `L1/interpolator.md`). It modifies surface (new theme chapter +
edge upgrade + index/SUMMARY rows) AND carries the rotation evidence (the L0 driver ranges + the L1
LHS form). The theme's evidence shape is the standard per-theme one (LHS L1 pure value, RHS L0 ctor
body, exhaustively cited). Record-definition sub-check: the signatures name `FiniteElementSpace`,
`LinOp`, and `DiscreteLinearOperator`. `FiniteElementSpace`/`LinOp` are L1 vocabulary defined in their
own firm entries (`L1/fe_space`, `L1/apply_linop` — both exist and are referenced), not records
introduced here; `DiscreteLinearOperator` is the Palace-owned C++ builder, fully read at its L0 home
(`bilinearform.hpp:95-117`) and characterized in-prose (ctor stores trial/test, `AddDomainInterpolator<T>`
pushes into `domain_interps`) — it is an L0 struct cited at its definition site, not an undefined
signature-named record. No definition-home gap.

**rotation-quality — pass.** The three translation axes are a genuine vocabulary shift, not a
named-term rename. Axis 1 (cache-drop + lazy-rebuild memoization) *erases* the entire `mutable`-member
mutate-on-miss idiom (`G.reset()` + auxiliary-space-keyed cache) — the L1 form is a pure
`(aux, primal) → LinOp` value with no cache, no rebuild, no mutation; that is state-hiding /
purity-recovery, the canonical construction-rotation pass. Axis 2 (map-type-pair dispatch → MFEM
kernel selection) compresses a four-branch `if/else if` dispatch + abort into the single L1
de-Rham-edge variant axis selected by the argument map-type pair — a coarser, more abstract
representation. Axis 3 is correctly NOT presented as a rotation but as a transparent one-line note (see
plan-kind below). The L1 form is strictly more compact/abstract than the L0 imperative ctor; not a 1:1
mapping.

**variant-axis-coverage — pass.** The orthogonal axes are explicitly enumerated and each is either
covered or scoped. The de-Rham edge axis (Grad / Curl-3D / Curl-2D / Div) is exhaustively covered with
a row per pair + the unsupported-pair abort (all four `else if` branches + the `else MFEM_ABORT` are
cited). The 2D-vs-3D curl dimension sub-axis is handled (Curl-2D native vs Curl-3D PA). The assembly
representation axis (libCEED-PA vs MFEM-native) is explicitly scoped as a transparent representation
note, not a hidden branch. The `Par*`/MPI axis is scoped out single-rank per §Scope. No hidden
branches — the abort half is the explicit catch-all.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk:
`L1-L0/fe-space-construction-rotation`, `essential-dofs-construction-rotation`,
`triangular-solve-obstruction`, `fe-collection-construction-rotation`, `L1/interpolator`,
`L1/apply_linop`, `L1/fe_space`, `L1/divfree-projector`, `concepts/constructed-operators`,
`semantics/index` — all EXIST. SUMMARY.md insert position is alpha-correct (`fe-space-...` <
`interpolator-...` < `weak-form-...`, matching the existing :269/:270 rows). L1-L0/index.md insert is
alpha-correct (between the existing fe-space row :66 and weak-form row :67). The `edit:L1/interpolator.md`
base matches disk (the current frontmatter carries the `reference: L1-L0/interpolator-construction-rotation`
FORTHCOMING note that the edit upgrades to `depends-on (kind: lowers-to)` — the upgrade is legitimate,
not fabricated). Build-readiness guard: the firm theme's body (`## Status` + L1/L0 forms + axes +
Verified-against) is authored INSIDE the `new:` fence (the fence opens at line 38, the `## Status`
heading is at line 76, well inside; fence closes at the block boundary) — no firm-body-outside-fence
defect.

**edge-label-fidelity — pass.** The theme carries the edge `L1/interpolator → L1-L0/interpolator-
construction-rotation` with `kind: lowers-to` (an L1>L0 lowering). The prose discusses exactly that
edge: LHS = the L1 `interpolator` pure value, RHS = the L0 `BuildDiscreteInterpolator` body. The coupled
`L1/interpolator` edge upgrade is the same L1→(L1>L0-theme) `lowers-to` relation. No L-level mismatch.

**plan-kind-consistency — pass.** Declared kind is `firm` L1>L0 theme; content matches. Every piece of
the rewrite is positively anchored and verified; the firm-on-positive-structure escape is invoked
correctly (syntactic structural mapping on fully-specified positive source; no constructed sub-part
materialized from negative anchors → correctly NOT `partly-constructive`). **GSLIB obstruction sub-kind
verified per the special-attention directive:** it is carried as `obstruction (opaque-library-ownership)`
(theme line 221, L1 entry line 513) with the mandatory sub-kind tag, negative anchors (every entry
point routes through `mfem::FindPointsGSLIB` with `MFEM_ABORT` GSLIB-absent fallbacks — exhaustiveness
established via `establish-negative-finding-exhaustiveness`), and **promotion route NONE** (lines 227,
528). It is correctly framed as a *sub-note* (boundary + negative anchors), NOT a lowering rule and NOT
a fill-in target — explicitly stated per §Scope unimplemented/opaque policy (lines 211-212, 232-236).
The transparent-2D-PA note is correctly classified as a **transparent performance/representation trick**
(one-line note per §Optimization-tricks): the prose states "same matrix, forced by libCEED capability
gap" and "No load-bearing numerical property rides on the choice" (lines 199-204) — not load-bearing,
not a distinct L1 operator. Both classifications are correct.

**skill-uptake-survey — pass.** The obstruction sub-note's shape implies the
`establish-negative-finding-exhaustiveness` skill — and the report references its invocation explicitly
(L1 entry line 522, "per skill `establish-negative-finding-exhaustiveness`"; theme line 258). The
firm-on-positive-structure / no-dedicated-test escape is invoked with precedent citations. Telemetry
present; no gap.

**Graded-stack additions.** (9) **rank-invariant — pass.** The theme is `rank: firm` (rank 3). Its
`depends-on` edges: `L1/interpolator` (`lowers-to`, firm rank 3 — `3 ≤ 3` holds) and three
`cites-evidence` edges to L0 source (rank-terminal ground truth). The coupled `L1/interpolator` edge
upgrade promotes the `lowers-to` edge to `depends-on` only NOW that the theme exists + is firm
(`3 ≤ 3`) — correctly gated (a `depends-on` to a non-existent target would have been a rank-linter
error, which is why the prior state held it as `reference`). No `firm` node rests on a sub-firm or
non-existent `depends-on` dep. The `reference` edges (apply_linop, fe_space, divfree-projector,
constructed-operators) carry no rank constraint. Well-founded. (10) **reachability — pass / noted.** The
theme grounds the *home* of the firm `interpolator` op. The report is explicit and correct that it does
NOT force an inbound consumer edge on `interpolator` the OP — the RE10 baseline-exception is preserved
(line 706-711): the faithful inbound consumers (`divfree-projector` Grad, boundary-mode `Bz` curl) stay
`reference`-classified consumed-by relations; promoting one to a blocking `depends-on` is flagged as a
separate reachability-grounding judgment out of this dispatch's scope. This matches the special-attention
RE10 directive exactly — no inbound edge forced.

### Issues found

1. **[citation-validity, warning] CYCLE.md `## Supporting evidence` line 679 — stale -1 drift.** Reads
   "`DiscreteLinearOperator` class `:95`, ctor `:105-109`, `AddDomainInterpolator` template `:113-114`
   confirmed." The on-disk template is at `bilinearform.hpp:114-115` (`:113` is blank). The
   proposed-changes blocks (theme line 182, L1 Evidence line 619) correctly say `:114-115`. This is the
   pre-correction value leaking into the dispatch's own evidence narrative — internal inconsistency with
   the (correct) artifact blocks. Severity: low (narrative-only; the artifact citations are correct).

2. **[citation-validity, warning] Second-`InterpolateFunction` body over-range `:282-310`.** Theme
   lines 219/276 and L1 entry line 632 cite the point-list `InterpolateFunction` body as
   `interpolator.cpp:282-310`, but `ComputeLineIntegral` starts at `:308`, so the range over-runs ~2-4
   lines into the next function (the 2nd InterpolateFunction body ends ~`:306` after its `MFEM_ABORT`
   `:304`). Severity: low (the load-bearing guard/abort anchors inside the range are exact; the
   obstruction claim is unaffected).

3. **[citation-validity, note — not a defect] First-`InterpolateFunction` body `:133-280` and
   `interpolator.hpp:50-56` decl-range are header/span labels.** `:133` start confirmed; the `:50-56`
   header label covers a comment + two decls where the point-list decl actually spans `:56-58` (cited by
   its first line `:56`). These are acceptable span/start conventions, not errors — recorded for the
   repairer's awareness only.

No fail-level issues. The two `warning` citation imprecisions are confined to the CYCLE.md narrative /
span-label conventions; the artifact-bound proposed-changes citations are accurate on disk, the GSLIB
obstruction sub-kind + transparent-PA classification + RE10 non-forcing are all correct per directive,
and the rotation/rank/edge structure is sound.

## Repair

### Fixes attempted

- **Finding 1 [citation-validity, warning]**: CYCLE.md `## Supporting evidence` line ~679 carries the
  stale pre-correction `bilinearform.hpp:113-114` for the `AddDomainInterpolator` template, contradicting
  its own (correct) proposed-changes blocks which use `:114-115`.
  - **Decision**: repaired
  - **Action**: CYCLE.md `## Supporting evidence` — rewrote the `bilinearform.hpp` evidence line from
    "`AddDomainInterpolator` template `:113-114` confirmed." to "`AddDomainInterpolator` template
    `:114-115` confirmed (`:113` is blank)." Verified on disk via `read_range` (`bilinearform.hpp`:
    `:113` blank, `template <typename T...>` `:114`, `void AddDomainInterpolator(...)` `:115`). This is a
    pure off-by-one narrative correction aligning the evidence log to the already-correct artifact blocks
    (theme line 182, L1 Evidence line 619) — mechanical, no content authored.

- **Finding 2 [citation-validity, warning]**: CYCLE.md `## Supporting evidence` line ~683 cites the
  second (point-list) `InterpolateFunction` body as `interpolator.cpp:282-310`, which over-runs ~3 lines
  past the function end into `ComputeLineIntegral`.
  - **Decision**: repaired
  - **Action**: CYCLE.md `## Supporting evidence` — trimmed the cited END from `:282-310` to `:282-307`
    and annotated "(`ComputeLineIntegral` starts `:309`)". Verified on disk via `read_range`: the second
    `InterpolateFunction` body's closing `}` is `:307`, `:308` is blank, `ComputeLineIntegral`'s
    declaration begins `:309`. Off-by-N range trim within repair authority; the load-bearing guard/abort
    anchors inside the range (`MFEM_ABORT` `:304`) are unaffected. Note: the theme (line 219/276) and L1
    entry (line 632) artifact blocks also carry `:282-310`, but per the critic these are proposed-changes
    citations and per the dispatch brief the artifact blocks were declared correct — the repair brief
    scoped this to the narrative line only, so the artifact-block occurrence is left for the
    integrator/critic disposition (it is a ~3-line over-range with exact internal anchors, not a
    load-bearing defect).

- **Finding 3 [citation-validity, note — not a defect]**: span/start-label conventions for the
  first-`InterpolateFunction` body `:133-280` and the `interpolator.hpp:50-56` decl-range.
  - **Decision**: not-needed
  - **Rationale**: the critic explicitly recorded this as an acceptable span/start convention, not an
    error — no fix required.

### Unrepairable findings

None. Both `warning` findings were narrative off-by-N citation corrections (in repair scope:
"citation line range off by a small offset"); applied surgically with on-disk verification. No
substantive authoring or content decisions were required.

## Suggested resolution

`ready`. All checks now `pass`, `repaired`, or `not-needed`. The two narrative imprecisions are
corrected and disk-verified; the artifact-bound proposed-changes blocks were already correct per the
critic. Integrator note: the second-`InterpolateFunction` over-range (`:282-310` → `:282-307`) also
appears in the theme/L1 artifact blocks; trivially trimmable at apply time if the integrator chooses,
but it is a non-load-bearing ~3-line over-range with exact internal anchors and does not gate the
obstruction claim.
