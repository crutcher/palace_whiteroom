---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T110846Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T111530Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "L2>L1 theme sketch — deflate-composition-lowering"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing Palace range was `read_range`-verified against
`palace/linalg/nleps.cpp` via the codemap MCP this dispatch. The inline anchors are *exact*, not
drifted: `deflated_solve` lambda opens at `:505` and closes at `:537`; `if (k == 0) { return; }`
at `:515-518`; the coordinate-extraction loop `:519-523` with the decisive
`x2(j) = b2(j) - linalg::Dot(GetComm(), x1, X[j])` at `:522`; the Gram materialization
`Eigen::MatrixXcd SS(k, k)` at `:524` and the assignment `SS(i, j) = linalg::Dot(...)` at `:529`;
the Schur block `S = eig_opInv * Identity(k,k) - H` at `:532`; the three `fullPivLu().solve` calls
at `:533` (`SS = -S...solve(SS)`), `:534` (`x2 = SS...solve(x2)`), `:535` (the fused
`MatVecMult(X, S...solve(x2))`); the `AXPY(-1.0, XSx2, x1)` at `:536`. `MatVecMult` definition
`:329-347` confirmed (the `z = 0; for j: AXPBYPCZ(...)` complex real/imag-split fold). Literature
anchors `:354-362` confirmed verbatim: JKM 2018 at `:354-355`, SLEPc-NEP minimality-index-1 at
`:356`, Effenberger 2013 at `:357-358`. Reuse/basis-growth sites all exact: residual reuse
`S=lam·I−H` at `:562` + `XSvv2 = MatVecMult(...)` at `:563`; Jacobian terms `:664-667`
(`S` at `:664`, `Sv2` at `:665`, `XSv2` at `:666`, `XSSv2` at `:667`); basis growth `X.resize(k+1)`
at `:614`, `X[k]=v` at `:615`, `k++` at `:619`, all within the cited `:606-619`. The artifact-side
citations into `book/src/L2/deflate.md` are in-range (Status `:362-415`; negative anchor `:343-348`
and `:386-391`; Signature `:55-66`; Context-stateless `:40-45`). No citation defects.

**surface-or-evidence — pass.** This is not a refinement of an existing operator/theme — it is a
*new* L2>L1 theme (`new:book/src/L2-L1/deflate-composition-lowering.md`) plus two append edits
(dep-map row + SUMMARY row). It carries surface (the full chapter) AND positive rotation evidence
(the `deflated_solve` block). No bare rotation_claim. The partly-constructive sub-part is framed as
retroactive/negative-anchor evidence backfill in the allowed shape (evidence FOR a faithful `S=I`
reduction, explicitly NOT licensing a positive claim). Passes.

**rotation-quality — pass.** The asserted rotation is a genuine fusion/reduction un-fold, L2→L1: the
single named L2 composition `deflate` fans down into a fixed small-step sequence of L1/L2 leaf calls
(`dot`-fold → `gram` → `lu_solve` sequence → `linear_combination` → `axpy`). The L2 form is strictly
more compact/abstract — it un-fuses the source's fused `MatVecMult(X, S.fullPivLu().solve(x2))` at
`:535` (Stage 3's final `S⁻¹·` folded into Stage 4's `X·`) back into a `lu_solve ▷ linear_combination`
composition, and it hides the `SS`-buffer in-place overwrite (`:524`→`:533`) behind two distinct L2
values. This is state-hiding + fusion-erasure, not a 1:1 rename. Passes.

**variant-axis-coverage — pass.** The central `op.block ∈ {Galerkin, Schur}` axis is the explicit
fan-out point (Stage 3) and BOTH values get their L1 `lu_solve`-sequence pinned: Schur = three solves
(`:533-535`, positively sourced); Galerkin = one bare-Gram solve (constructive, S=I reduction). The
secondary axes are each handled: `op.dot` hook (closure substitution, invariant to fan-down,
`deflate.md` law 6); element type complex/real (absorbed by `dot`/`linear_combination`); in-place vs
out-of-place (Stage 5 transparent-perf note). No hidden branch. Passes.

**cross-reference-integrity — warning.** Most references resolve: `L2/deflate.md`, `L1/lu_solve.md`,
`L2/gram.md`, `L1/dot.md`, `L2/linear_combination.md`, `L2-L1/orthogonalize-composition-lowering.md`,
`L1/nleps_deflated_residual.md` all exist on disk. The negative anchor is *confirmed* — codemap
`search_text` for `fullPivLu` over `palace/linalg/*.cpp` returns hits ONLY inside `nleps.cpp` (lines
533/534/535/563/665/667), all Schur-wrapped; no bare-Gram deflation solve exists elsewhere. The
dep-map `edit` anchor (the `orthogonalize-composition-lowering` row) matches `index.md:16` verbatim,
and the SUMMARY `edit` anchor matches `SUMMARY.md:56` verbatim — both well-formed appends. The
warning is the **`gram-fold-specialization` forward-reference**: `book/src/L2-L1/gram-fold-specialization.md`
does NOT exist (unintegrated parallel-cycle sibling), yet the chapter body renders it as a **live
markdown link** `[gram-fold-specialization](./gram-fold-specialization.md)` in two places
(CYCLE.md:60–62 in the intro "Sibling to ..." sentence, and CYCLE.md:192 in Stage 2). A live link to a
missing file is a hard `linkcheck2` build error per the `rough-in-rows-must-be-plain-text-when-anchor-missing`
convention. The report is *aware* and flags it for the integrator (OQ #2: "If the sibling's theme is
NOT integrated this cycle, the Stage-2 link must defang to plain-text") — but it does NOT itself
defang the link, and it leaves TWO live occurrences (the OQ names only the "Stage-2 link", missing the
intro-sentence occurrence at :60–62). This is build-readiness friction the integrator must resolve;
flagged `warning` not `fail` because it is correctly surfaced as a known forward-reference and the fix
is a mechanical defang.

**edge-label-fidelity — pass.** The edge label is L2>L1 (declared in scope, frontmatter, slug
location `book/src/L2-L1/`, and dep-map placement). The prose discusses exactly that edge throughout:
LHS = L2 `deflate` composition, RHS = L1 leaf fan-down, narrated forward high→low. The leaf targets
that are themselves L2 (`gram`, `linear_combination`) are correctly named as L2 vocabulary consumed
whole (with their own L2>L1 fan-downs deferred to sibling themes), not mislabeled. No edge mismatch.

**plan-kind-consistency — pass.** Declared kind is a `partly-constructive` L2>L1 theme; the content
matches that shape exactly. The `partly-constructive` status is applied *correctly* per the CLAUDE.md
status-tier definition: (i) it states which sub-part is constructive — the Galerkin-core single
`lu_solve(XᴴX, c)` with `S=I` (§Status "Constructive sub-part", Stage 3 "Galerkin variant"); (ii) it
cites the negative anchors — no bare-Gram deflation solve anywhere in `palace/linalg/*.cpp`, plus the
literature anchors `:354-362`, cross-referenced to the L2 entry's same anchor `deflate.md:343-348,
386-391`; (iii) it gives the explicit promotion condition — a positive bare-Gram-solve site outside
the `S=λI−H` Schur wrapping (future linear-EVP / preconditioner / ROM-Galerkin deflation). It does
NOT mark the whole theme firm (the constructive sub-part isn't), does NOT downgrade to rough-in (the
structure IS firm), and — critically — explicitly does NOT close the gate ("This theme does not make
that call and does not close the gate", §Status; reaffirmed in OQ #1 and Working-notes). The
inheritance from the L2 `deflate` entry is faithful and the gate is shared, not duplicated. The
"Speculative operators proposed: None" section is consistent — verified no new operators are promoted;
the fan-down lands entirely on pre-existing firm leaves (`dot`/`gram`/`lu_solve`/`linear_combination`/
`axpy`). Passes.

**skill-uptake-survey — warning.** Telemetry only, non-blocking. The report's shape implies several
relevant skills that are not referenced by name: `verify-rotation-citation` and
`verify-citation-range` (the dispatch is citation-heavy with a partly-constructive split, and the
verify-citation-range skill has an explicit "inherited-citation sub-case" added cycle-012 that fits
the L2-entry-inherited anchors here), `propose-rotation` (a reduction-chain rotation), and
`classify-variant-axis` (the `op.block` Galerkin/Schur axis treatment reads like a clean
classify-variant-axis application). The report demonstrates the *procedures* (read_range verification
log in §Verified-against, explicit variant-axis enumeration) but does not cite skill invocation. Pure
presence check — surfaced as telemetry, not a content defect.

### Issues found

1. **Live link to non-existent `gram-fold-specialization.md` (×2)** — `CYCLE.md` proposed-changes
   block, `new:book/src/L2-L1/deflate-composition-lowering.md`, at body lines CYCLE.md:60–62 (intro
   "Sibling to ... [gram-fold-specialization](./gram-fold-specialization.md)") and CYCLE.md:192
   (Stage 2 "[gram-fold-specialization](./gram-fold-specialization.md) theme's content"). The target
   file does not exist on disk (confirmed). A live `[text](./gram-fold-specialization.md)` link is a
   hard `linkcheck2` build break unless the sibling abstractor's theme integrates this same cycle
   under that exact slug. Severity: **medium** (build-readiness; blocks `cargo make book` if the
   sibling does not land). Note the report's own OQ #2 names only the *Stage-2* occurrence — the
   intro-sentence occurrence (:60–62) is a second live link the OQ does not enumerate; both need
   defanging-or-confirming. Candidate for repair (mechanical defang to plain-text per
   `rough-in-rows-must-be-plain-text-when-anchor-missing`, OR integrator confirms sibling slug landed).

2. **Minor framing — `x1` vs `v` in Stage 1 coordinate** — `CYCLE.md` §"L1 form (RHS)" Stage 1
   (CYCLE.md:169–185) and §Conjugation. Palace computes the deflation coordinate against `x1` (the
   freshly `opInv->Mult(b1, x1)`-computed vector at `:514`), not against the lambda's nominal input;
   the report's L2 form names this vector `v` and the prose at CYCLE.md:181 correctly identifies the
   coordinate as `X[j]ᴴ x1`. The mapping (`v` := the post-`opInv->Mult` `x1`) is faithful but is left
   implicit. Severity: **low / informational** (not a citation or rotation defect; the reading is
   correct). Optional clarity note only — not blocking.

3. **Gram double-loop range framing differs from L2 entry** — §"L1 form (RHS)" Stage 2 / §Verified-against
   cite the Gram build at `:524-531` (including the `Eigen::MatrixXcd SS(k,k)` materialization at
   `:524`), whereas the L2 `deflate.md` entry cites `:526-531` (loop body only). Both are in-range and
   correct; the assignment line `:529` agrees in both. Severity: **none / informational** — noted for
   cross-entry consistency awareness, no action required.

## Repair

### Fixes attempted

- **Finding 1 (cross-reference-integrity, MEDIUM build-breaker)**: live markdown link
  `[`gram-fold-specialization`](./gram-fold-specialization.md)` to a non-existent file rendered in
  TWO places — the intro "Sibling to …" sentence (body ~:60–62) and the Stage-2 sentence (body ~:192).
  - **Decision**: repaired.
  - **Action**: Confirmed `book/src/L2-L1/gram-fold-specialization.md` is absent from disk (the
    L2-L1 directory has `inner-product-fold-specialization.md` and
    `linear-combination-fold-specialization.md` but no `gram-fold-specialization.md`). Defanged BOTH
    live links to plain-text backtick-slug per the `rough-in-rows-must-be-plain-text-when-anchor-missing`
    convention:
    - `CYCLE.md` `new:book/src/L2-L1/deflate-composition-lowering.md` intro sentence — link → plain
      ``gram-fold-specialization`` with an inline note that the chapter is not yet on disk so the
      reference stays plain-text per the convention.
    - `CYCLE.md` same proposed-changes block, Stage 2 — link → plain ``gram-fold-specialization``
      with an inline "chapter not yet on disk" forward-reference note.
    - `CYCLE.md` §Open questions OQ #2 — updated to record that BOTH occurrences (not just the
      Stage-2 one the original OQ enumerated) are now defanged, and added an **integrator note**: if
      the `gram-fold-specialization` sibling lands earlier in the same integration pass (file exists
      on disk at integration time), the integrator MAY re-link both to a live reference, but the safe
      committed state is plain-text.
  - Verified post-edit: `grep` for `gram-fold-specialization` shows zero remaining `](./…)` link
    syntax; all six mentions are now plain-text. Mechanical defang only — no content authored.

- **Finding 2 (LOW — split across critic issues #2 and #3)**:
  - **Issue #2 — `x1` vs `v` Stage-1 framing left implicit.** **Decision**: not-needed. The critic
    confirms the reading is correct and faithful, rated it "low / informational … optional clarity
    note only — not blocking." Making the `v := post-`opInv->Mult` `x1`` mapping explicit requires
    authoring an explanatory sentence about the lambda-input semantics — a content/clarity decision,
    not a mechanical fix. Out of repair scope; not a defect blocking integration.
  - **Issue #3 — Gram-loop range `:524-531` vs L2 entry's `:526-531`.** **Decision**: not-needed.
    The critic confirms BOTH ranges are in-range and correct (severity "none / informational, no
    action required"); the report's `:524-531` legitimately includes the `Eigen::MatrixXcd SS(k,k)`
    materialization at `:524` that Stage 2 describes. Nothing is broken to repair — both framings are
    valid; narrowing to match the L2 entry would not be a fix.

- **skill-uptake-survey (warning)**: not-needed. Telemetry-only, non-blocking presence check — the
  critic explicitly framed it as "Pure presence check — surfaced as telemetry, not a content defect."
  No repair action; not a defect.

### Unrepairable findings

None. The single MEDIUM build-breaker was mechanically repairable (link defang) and is fixed. The
two LOW items are cosmetic/informational with the critic's own "no action required" / "not blocking"
ratings — marked `not-needed`, not deferred for substantive authoring.

## Suggested resolution

`ready`. Notes for the integrator:

- The `gram-fold-specialization` forward-reference is committed-safe as plain-text in both
  locations. If the parallel-cycle `gram-fold-specialization` sibling theme integrates **earlier**
  in this same pass (the file lands on disk at integration time), the integrator MAY re-link both
  plain-text references to the live `[`gram-fold-specialization`](./gram-fold-specialization.md)`
  form — but the plain-text state is the safe default and passes `linkcheck2` regardless of sibling
  ordering. See CYCLE.md OQ #2 for the integrator note.
- All other references in the chapter resolve on disk (critic-confirmed: `L2/deflate.md`,
  `L1/lu_solve.md`, `L2/gram.md`, `L1/dot.md`, `L2/linear_combination.md`,
  `L2-L1/orthogonalize-composition-lowering.md`, `L1/nleps_deflated_residual.md`); the dep-map and
  SUMMARY append anchors were critic-verified verbatim against `index.md:16` and `SUMMARY.md:56`.
- The `partly-constructive` status content was critic-verified correct (plan-kind-consistency pass)
  and was NOT touched by repair.
