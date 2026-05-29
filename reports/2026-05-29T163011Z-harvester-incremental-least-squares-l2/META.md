---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T165439Z
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
repaired_at: 2026-05-29T170000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "Formalize incremental-least-squares at L2"

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` on the CYCLE.md: **46 ok, 0 failing** (exit 0), matching the report's self-reported count exactly. All 46 citations are in-range and path-hygienic. I then `--anchor`-verified every load-bearing pinpoint, with special attention to the four claimed codemap-drift corrections:
- `iterative.cpp:656` anchors `s[i] /= Hi[i]` (corrected from :655) — confirmed.
- `iterative.cpp:659` anchors `s[k] -= Hi[k] * s[i]` (corrected from :658) — confirmed.
- `iterative.hpp:193` anchors `mutable std::vector<ScalarType> s, sn;` (corrected +1) — confirmed.
- `iterative.hpp:194` anchors `mutable std::vector<RealType> cs;` (corrected +1) — confirmed.
All four drift-corrections land on the exact source line; the report's `--anchor` adjudication is itself adjudicated `[ok]` by the tool. I also `--show`-verified the GMRES stream `:632-644` (replay loop `:634-636`, generate `:638`, apply `:639`, apply_rhs `:640`, `beta = std::abs(s[j+1])` `:642`, `converged = (beta < eps)` `:644`), the back-solve `:652-660`, the GMRES correction `:662-680` (`x.Add(s[k], V[k])` `:666`; right-precond `r.Add` `:674`, `ApplyB`+`x += V[0]` `:676-677`), the FGMRES arm `:810-844` (stream `:813-819` line-for-line identical to GMRES, back-solve `:835`/`:838`, `x.Add(s[k], Z[k])` `:843`), the Givens kernels (`:73-108` real generate, `:112-118` complex generate with the in-comment `cs² + |sn|² = 1` contract at `:118`, `:227-241` apply with the `−conj(sn)` complex form at `:239`), `s[0] = beta` `:612`, and `Norml2` sub-diagonal `:631`. Independently confirmed the report's central codemap correction: there is **no** `gmres.cpp` on disk; `iterative.cpp` is the correct source (`GmresSolver::Mult` `:544`, `FgmresSolver::Mult` `:734`). Citations are clean.

**surface-or-evidence — pass.** This is a NEW firm operator promotion (stub→firm), not a refinement of existing surface. The proposed `edit:` block replaces the entire claim-free stub body (verified: the on-disk stub at `book/src/L2/incremental-least-squares.md` carries only the placeholder `## What this will be` / `## Implied by` / `## Refinement pending` skeleton) with a fully-cited firm chapter. Surface is added AND evidence is present (the §Evidence block is 17 distinct source pinpoints). Not applicable as a rotation_claim backfill — this is fresh firm surface.

**rotation-quality — pass.** The operator is correctly defined in L2 (fusion-rotation) vocabulary on its own layer. The L2 form names the canonical composition `replay ▷ generate ▷ apply ▷ apply_rhs` ▷ back-solve and states composition-level laws; it does NOT re-derive the constituent Givens-kernel algebra (inherited, per §Algebraic-laws preamble) and explicitly defers the L1 decomposition to a forthcoming `L2-L1/incremental-least-squares-composition-lowering` theme (high→low directive respected — the L1 leaf `ls_update_column` is referenced as the future lowering target, not used to define the L2 semantics). The fusion rotation is genuine and compactifying: Palace fuses the QR factorisation *into* the column-arrival loop and reads the residual off the rotated RHS; L2 de-fuses that into the named composition while preserving the load-bearing structure. The running-QR is correctly classified **load-bearing** (not transparent) per CLAUDE.md §Optimization tricks: the cheap-exact residual-norm estimate `β = |s[j+1]|` is the property bought (law 1, residual-exposure-by-unitarity), and the replay-before-generate ordering is a stated non-commutative algebraic claim (law 2, with the matching non-law "sub-step commutativity does NOT hold"). The bit-level non-associativity of the rotation stream vs. a from-scratch QR is recorded as an explicit load-bearing-numerical-trick caveat, not erased.

**variant-axis-coverage — pass.** Two axes claimed: `op.basis_kind ∈ {V, Z}` (GMRES vs FGMRES back-solve reconstruction target) and `op.variant ∈ {real, complex}` (Givens kernel element type). Both are L0-grounded: the `{V, Z}` split is witnessed at `:666` (`x.Add(s[k], V[k])`) vs `:843` (`x.Add(s[k], Z[k])`), and the real/complex split is anchored at the `iterative.hpp:193-194` register declaration (`s, sn` ScalarType; `cs` RealType), verified on disk. The report does NOT hide the `pc_side ∈ {LEFT, RIGHT}` branch — I confirmed it exists in source (`:662` LEFT/unpreconditioned vs `:669` RIGHT with `ApplyB` post-application at `:676-677`); the report explicitly folds right-preconditioned GMRES into the `V` axis as a back-solve-reconstruction sub-case (the running-QR stream is invariant; only the correction post-processing differs), which is a faithful axis collapse rather than a hidden branch. Householder / two-sided reductions are explicitly scoped out, and I confirmed no alternate-reduction path exists in `iterative.cpp` (only the plane-rotation stream). Empty (`j = -1`) and single-column (`j = 0`, replay-skip) boundaries are both covered (law 5). Axes are exhaustive.

**cross-reference-integrity — pass (with one integrator-anchor note, below).** All `[link]` targets resolve on disk: `orthogonalize.md`, `ksp_solve.md`, `krylov-step.md`, `linear_combination.md`, `index.md`, `concepts/{incremental-least-squares,givens,givens_generate,givens_apply,sequential-obstruction}.md`, `SUMMARY.md` — all present. All forward-reference line citations resolve: `ksp_solve.md:63` (`materialise_iterate` let-binding), `:83` (phase-3 prose), `:123` (the "queued `incremental-least-squares`" dep bullet), `krylov-step.md:132` (the §"L2 vs L1 distinction" forecast naming this exact entry). The givens concept replay-order contract quoted in law 2 matches `concepts/givens.md:25` verbatim. **Build-readiness fence guard:** `grep -n '```'` yields exactly 6 fence markers (even parity), 3 balanced `edit:` blocks. The firm body is fully ENCLOSED inside the first fence (lines 27–535) — `## Status`, Signature, Algebraic-laws, Evidence, and all apparatus headings are INSIDE the fence; the report's own top-level sections (`## Operator content`, `## Supporting evidence`, `## Open questions`) sit OUTSIDE the fences as meta-prose, which is correct. No nested triple-backtick fences inside the block (Signature/Semantics use indented code), so no nested-fence escaping concern. This is the inverse of the cycle-019 fence-truncation defect — clean.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried by this report; it is a single-layer L2 operator entry. The directional discussions present (the L2-vs-L1 distinction §, the forward-reference to the future L2-L1 theme) are correctly oriented (L2 form named on its own layer; L1 leaf and L2>L1 lowering deferred). Not applicable to a single-layer operator promotion.

**plan-kind-consistency — pass.** Declared kind is `firm` and the content shape matches: a complete signature, full semantics, six composition-level laws + four explicit non-laws, exhaustive variant axes, and 17 source pinpoints read in both solver arms — no rough-in placeholders, no `TODO`/`pending` claims in the chapter body. The firm bar is the same as the sibling `orthogonalize` (cycle-019) and `linear_combination` (cycle-018) L2 named compositions; I confirmed `orthogonalize.md` carries the identical heading set and a `## Status` firm entry, so the firmness-precedent claim holds. The "firm-on-positive-structure" escape (laws are syntactic/unitarity identities on fully-read positive source, so the absent dedicated GMRES running-QR unit test does not gate them) is correctly invoked — this is the `apply_linop`/`apply_nonlinear_pencil` situation, not the `eigsolve`-convergence-semantics situation.

**skill-uptake-survey — pass.** The report's shape implies three skills, all referenced/exercised: `tools/citecheck/citecheck.py --anchor`/`--scan` (the citation-verification realization — invoked throughout §Evidence and §Supporting-evidence), `classify-variant-axis` (cited at §Variant-axes with the per-axis-value absorption-path / load-bearing-primitive / state-binding output contract followed), and the `proposed-changes-fence-encloses-full-body-guard` shape (satisfied by construction). Telemetry surfaced; no blocking finding.

### Issues found

No blocking or substantive issues. The report is exceptionally clean for a firm promotion — every load-bearing pinpoint self-verifies, the four claimed codemap drift-corrections all land exactly, the fence encloses the full firm body, and both variant axes are L0-grounded. Minor notes for the integrator (none are correctness defects in the report):

1. **Dep-map `edit:` anchor (integrator-facing, not a report defect).** `CYCLE.md:538-540` (`edit:book/src/L2/index.md`) supplies the new firm dep-map row but does not reproduce the existing stub row text as a replacement anchor. The existing stub row is at `book/src/L2/index.md:57` (`*(stub — signature pending harvester refinement)* … | \`stub\` …`). The integrator must replace the line-57 row (not append a duplicate). Severity: low — standard single-target `edit:` resolution; flagged so the integrator-per-report matches it to the existing stub row rather than creating a second `incremental-least-squares` row.

2. **SUMMARY `(stub)` suffix drop (integrator-facing).** `CYCLE.md:542-544` (`edit:book/src/SUMMARY.md`) provides the un-suffixed entry `- [incremental-least-squares](./L2/incremental-least-squares.md)`, but the on-disk `SUMMARY.md:45` reads `- [incremental-least-squares (stub)](./L2/incremental-least-squares.md)`. The edit is a line replacement (the report calls this out itself in §Open-questions). Severity: low — confirmed the report intends and documents the de-stub; flagged only so the integrator anchors on the `(stub)`-suffixed line.

3. **Stale L2/index Working-Notes prose (correctly deferred, out of scope).** `book/src/L2/index.md:21`, `:46`, `:78-79` still describe `incremental-least-squares` as a "queued stub"; once this lands firm those notes are stale. The report correctly flags this as layer-intro-author scope (§Open-questions, OQ `L2-layer-intro-refresh-for-named-compositions`) and does NOT touch it (one-operator-per-dispatch discipline). Severity: informational — not a defect; noted so the deferral is visible to the integrator/planner. The dep-map row flip (issue 1) is in-scope; the surrounding Working-Notes prose is not.

4. **Concept-page source staleness (drive-by, not this report's defect).** `book/src/concepts/givens.md:29` still attributes the `ls_update_column` sequence to `gmres.md` (a file that does not exist; the source is `iterative.cpp`). This report correctly cites `iterative.cpp` throughout. Severity: informational — a pre-existing concept-page staleness the integrator/lifter may want to log; this report neither introduces nor inherits it.

### Notes on the OQ resolution (`gmres-givens-stream-as-step-kernel-borderline`)

The report resolves this OQ in the **negative** (the Givens-stream is a distinct named composition, NOT a `krylov-step` axis). The justification is sound and source-grounded: the composition operates on the small-dense `(j+2)×(j+1)` Hessenberg (work `O(j)` scalar, independent of field dimension `N`), whereas `krylov-step` builds and orthogonalises a length-`N` basis vector. The "folded *by* the step, not a step variant" framing is consistent with the `krylov-step.md:132` forecast (which names `incremental-least-squares` as a *separate* future L2 composition, not a `krylov-step` axis) and with the `ksp_solve.md:123` dep bullet (which lists it as a transitively-folded named composition alongside `orthogonalize`). The negative resolution is justified and internally consistent across the three cross-referenced surfaces.

---

## Repair

All 8 critic checks graded `pass`. No warning/fail findings to repair — `repairs:` are uniformly `not-needed`. The critic surfaced four low/informational integrator-awareness notes (explicitly NOT defects); each is verified against on-disk artifact state below and routed appropriately. One stale-frontmatter housekeeping fix (`verifies:` path) was applied.

### Fixes attempted

- **Finding (housekeeping): stale `verifies: ../REPORT.md` frontmatter.**
  - **Decision**: repaired.
  - **Action**: `reports/2026-05-29T163011Z-harvester-incremental-least-squares-l2/META.md` frontmatter — `verifies: ../REPORT.md` → `verifies: ../CYCLE.md` (the cycle-004 REPORT.md→CYCLE.md rename; the report file on disk is `CYCLE.md`). Mechanical path correction; no content touched.

- **Finding (critic note 1, integrator-facing, NOT a report defect): dep-map `edit:` must REPLACE the existing stub row, not append.**
  - **Decision**: not-needed (no report edit required; verified for the integrator).
  - **Verification**: confirmed the existing stub row is on disk at `book/src/L2/index.md:57` (`| [\`incremental-least-squares\`](./incremental-least-squares.md) | *(stub — signature pending harvester refinement)* | … | \`stub\` … |`). The report's `CYCLE.md:538-540` `edit:book/src/L2/index.md` block supplies a single new **firm** row carrying the full signature + dep summary + `firm` status. The proposed change is a stub-row REPLACEMENT (correct intent — one `incremental-least-squares` row). Integrator-per-report anchors the `edit:` on the line-57 stub row rather than appending a duplicate. No content authoring involved; this is a single-target `edit:` resolution the integrator handles at apply-time.

- **Finding (critic note 2, integrator-facing): SUMMARY edit drops the `(stub)` suffix.**
  - **Decision**: not-needed (verified for the integrator).
  - **Verification**: confirmed `book/src/SUMMARY.md:45` reads `- [incremental-least-squares (stub)](./L2/incremental-least-squares.md)`. The report's `CYCLE.md:542-544` `edit:book/src/SUMMARY.md` supplies the un-suffixed `- [incremental-least-squares](./L2/incremental-least-squares.md)`. The de-stub is intentional and self-documented by the report (§Open questions, CYCLE.md:571). The edit is a line replacement anchored on the `(stub)`-suffixed line — standard integrator line-match. No defect.

- **Finding (critic note 3, informational): stale L2/index Working-Notes prose.**
  - **Decision**: not-needed (correctly deferred; out of repair scope).
  - **Verification**: confirmed `book/src/L2/index.md` Working-Notes prose (`:21` "Named compositions" motif bullet, `:44-46` "Queued at L2", `:78-79` "One stub queued") will be stale once this lands firm. The report correctly flags this as `layer-intro-author` scope (§Open questions, OQ `L2-layer-intro-refresh-for-named-compositions`, CYCLE.md:569) and does NOT touch it (one-operator-per-dispatch discipline). The dep-map row flip (note 1) is in-scope for this report; the surrounding Working-Notes prose is not. Repairing this would require substantive re-authoring of the index narrative — out of repair authority. Deferral stands.

- **Finding (critic note 4, drive-by, NOT this report's defect): `concepts/givens.md:29` source staleness.**
  - **Decision**: not-needed here (do NOT fix in this repair pass, per task instruction); surfaced as an OQ for follow-up.
  - **Verification**: confirmed `book/src/concepts/givens.md:29` reads `In GMRES (\`gmres.md\`), the inner step's \`ls_update_column\` …` — it attributes the `ls_update_column` sequence to `gmres.md`, a file that does not exist on disk (the source is `iterative.cpp`). This report neither introduces nor inherits the staleness (it cites `iterative.cpp` throughout, e.g. the §Palace-mapping block at `givens.md:33-34` already correctly cites `iterative.cpp:73-108` / `:227-241`). Editing a concept page is out of this report's write-scope and out of repair authority (it is a separate artifact the report does not own). Routed below as a surfaced OQ; the integrator/lifter logs it for a follow-up concept-page re-cite dispatch.

### Unrepairable findings

None. No warning/fail finding required deferral. The four integrator-awareness notes are not defects (verified above); the one staleness (note 4) is a pre-existing drive-by on a non-owned artifact, surfaced as an OQ rather than repaired.

## Suggested resolution

`overall_status: ready`. Clean firm-operator promotion (stub→firm) — all 8 checks pass, citecheck self-verified 46 ok / 0 failing, all four codemap-drift corrections independently confirmed by the critic. Integrator-per-report notes for application:

1. Anchor the `edit:book/src/L2/index.md` block on the line-57 stub row (REPLACE, do not append a second `incremental-least-squares` row).
2. Anchor the `edit:book/src/SUMMARY.md` block on the `(stub)`-suffixed line-45 entry (de-stub line replacement).
3. The report's three deferred OQs (`L2-layer-intro-refresh-for-named-compositions`, `l2-ksp-solve-materialise-iterate-recite`, the `L2-L1/incremental-least-squares-composition-lowering` theme unblock) promote normally per the report's §Open questions.

**Surfaced OQ for follow-up (drive-by, repairer-surfaced):** `concepts/givens.md:29` attributes `ls_update_column` to a non-existent `gmres.md`; the live source is `iterative.cpp` (already correctly cited in the same page's §Palace-mapping at `:33-34`). A future low-fan-out `lifter` / concept-page re-cite dispatch should fix the `:29` prose reference. Not blocking this report's integration.
