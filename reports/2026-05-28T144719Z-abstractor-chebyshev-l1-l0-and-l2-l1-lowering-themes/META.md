---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T15:42:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-28T16:05:00Z
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

# META: verification of "L1>L0 + L2>L1 theme sketches — chebyshev (two themes, one invocation pair)"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing Palace citation was re-read via
`palace-codemap read_range` and lands on the claimed construct. Spot-verified the
task's flagged ranges and more:
- `chebyshev.cpp:13-27` `GetLambdaMax` (real literal-`true` at :19; complex
  `A.IsReal()` at :27) — confirmed, both overloads + `SpectralNorm`.
- 4th-kind `SetOperator` is lines 170-188; `MFEM_VERIFY(lambda_max>0.0)` at
  183-184. Report cites `:169-186` (D sub-pattern) and `:170` (task framing) —
  in-range; the `:169-186` close is 2 lines short of the function's `}` at 188 but
  covers all cited content.
- 4th-kind `Mult2` is lines 189-220; the "Apply smoother" comment is at :191
  (matches the task's "`Mult2` :191"); the in-place `y += d` / `y = 0.0`,
  `ApplyOrder0`/`ApplyOrderK` passes all present. Report's `:188-220` is in-range
  (188 is the blank line before the template).
- 1st-kind `SetOperator` 232-258 (`sf_min` default at 245-248; `theta`/`delta` at
  253-254; `MFEM_VERIFY` at 250-251) and 1st-kind `Mult2` 260-291. Report cites
  `:232-259` and `:261-293` (task's `SetOperator :233` / `Mult2 :261`) — in-range;
  `:261-293` overshoots the `Mult2` close (291) by two blank lines, harmless.
- All header citations exact: `chebyshev.hpp:43` = `mutable VecType d, r;`;
  `:50-58` = `Mult` resize-forward; `:60-68` = `MultTranspose`; `:71` = `Mult2`
  decl; `:73-76` = `MultTranspose2 { Mult2(...); // Assumes operator symmetry }`;
  `:37` / `:106` = the `// real-valued for now` `dinv` comments.
- Consumer sites confirmed: `gmg.cpp:52-59` (per-level `cheby_4th_kind` choice);
  `distrelaxation.cpp:36` = `B_G->SetInitialGuess(false)`.
- Element-kernel ranges are slightly loose but in-range: `ApplyOrder0` real is
  68-78 (cited `:69-78` and within `:55-78`), `ApplyOrderK` real is 112-123 (cited
  `:114-123` and within `:80-123`). The `:55-78` start lands mid the accumulating
  `ApplyOp` overload; the intent (ApplyOrder0) is covered. Sub-blocking imprecision
  only.
No claim found without a citation; no citation found out of range.

**surface-or-evidence — pass.** Both entries are new lowering-theme surface (two
new chapter files), not modifications-to-existing with bare rotation_claims. Each
carries forward-narrated rewrite text grounded in re-read source. The
refinement-shaped concern does not apply; this is fresh constructive surface.

**rotation-quality — pass.** Both rotations are genuine, not 1:1 renamings.
(L2>L1) `chebyshev-iteration-fusion`: the L2 `order`-step three-term recurrence
(~4 primitive calls per degree: `apply_linop` + `axpby` + `scal`/`axpby` over
`elementwise_product` + `axpy`) collapses into the single L1 closed-form token
`p_order(D⁻¹ A)·(·)` — `order` iterations and their per-degree state (`d`, `r`,
scalar generator thread) are hidden behind one polynomial-action name. This is
structural compression (state hiding + per-degree-work fusion), strictly more
compact/abstract at L1. I verified the fusion is algebraically anchored, not
hand-waved: it rests on L2 anchor law 1 ("the recurrence *is* the matrix-free
evaluation of `p_order(D⁻¹ A)`" modulo float reassociation; `L2/chebyshev-iteration.md`
:125-131), law 2 (variant-invariant primitive sequence, :133-139), and law 3
(element-kernel fusion transparency, :141-144). The applicability conditions
correctly cite the L2 non-laws (polynomial-expansion non-equivalence,
`k`-recurrence non-reordering) as the load-bearing sequentiality. The "secondary,
transparent" element-kernel fusion is correctly nested inside the fused token.
(L1>L0) `chebyshev-smoother-mutation-rotation`: the standard mutation rotation —
pure-functional L1 value-producing action lowered to L0 output-arg mutation +
workspace erasure + construction-bound closure capture; the abstract side is L1
and the rewrite hides the destination buffer / workspaces, the canonical rotation
for the L1-L0 Part.

**variant-axis-coverage — pass.** Two orthogonal axes exist (polynomial-kind
4th/1st; element-type real/complex). I confirmed via `classify-variant-axis` that
both anchors carry full `## Variant axes` blocks (`L1/chebyshev-smoother.md`
:221-256; `L2/chebyshev-iteration.md` :203-219) disclosing both axes with the
load-bearing primitive and the setup-bound state. The lowering themes correctly
rely on that upstream disclosure and cover all four combinations via explicit
applicability conditions (L1>L0 conditions 4+5; L2>L1 condition 4). No hidden
branch — the polynomial-kind is correctly framed as a setup-time class choice
(`gmg.cpp:52-59` / `distrelaxation.cpp:21-36`), not a runtime tag. The granular
`## Variant axes` block requirement applies to the operator slices (satisfied
upstream), not the lowering themes, so the themes' applicability-condition
treatment is appropriate.

**cross-reference-integrity — warning.** All inline `[link]` targets resolve:
the L1/L2 anchors, the L1-L0 siblings (`apply-linop`, `axpby`, `ksp-solve`,
`eigsolve` mutation-rotations), the L1 leaf primitives (`apply_linop.md`,
`axpy.md`, `axpby.md`, `scal.md` — underscore form, matches), and the four
concepts (`elementwise-product`, `sequential-obstruction`, `variant-absorption`,
`constructed-operators`). The L2-L1 Part directory exists with only `index.md`,
confirming the L2>L1 theme is the first chapter. BUT: **the report proposes two
NEW chapter files yet provides no `SUMMARY.md` registration for either.** The
SUMMARY convention nests each chapter under its Part overview
(`SUMMARY.md:58-65` shows the L1-L0 chapter list); the report's edit blocks touch
`L1-L0/index.md` and `L2-L1/index.md` (theme-list tables) but not `SUMMARY.md`.
Without SUMMARY entries, `chebyshev-smoother-mutation-rotation.md` and
`chebyshev-iteration-fusion.md` will be orphaned from the mdBook nav (mdBook
builds them silently as unreferenced files). See Issue 1.

**edge-label-fidelity — pass.** L1>L0 theme (dir `L1-L0/`) narrates forward
L1→L0 ("the pure L1 form ... lowers into Palace's in-place L0 `Mult2`"); L2>L1
theme (dir `L2-L1/`) narrates forward L2→L1 ("the L2 ... recurrence ... fuses
upward into the L1 closed-form"). Both match their directory edge labels exactly;
no L_{n+1}/L_n direction confusion.

**plan-kind-consistency — pass.** Both entries declare `firm` and the content
shape matches: every form is a syntactic identity on fully-specified source
(verified) with no literature inference and no negative-anchor reconstruction.
The task's flagged call — classifying `MFEM_VERIFY(lambda_max > 0.0)` as a
setup-time precondition rather than a `partly-constructive` negative-anchor — is
**correct**: the guard is a POSITIVE source site (confirmed at `chebyshev.cpp:183-184`
4th-kind and `:250-251` 1st-kind), a runtime precondition assertion, fundamentally
distinct from the `eigsolve` `LinearSolveFailed` case where the error condition
was *reconstructed* from negative anchors. No partly-constructive caveat is owed;
`firm` is the right status for both themes.

**skill-uptake-survey — pass.** The report references the codified MCP-first
localization path (`palace-codemap read_range`, repeatedly, in both
verified-against blocks), names `lowering-verifier` exhaustiveness audits as the
standard follow-up for both themes, and its variant treatment is consistent with
`classify-variant-axis` (parametric/constructed-operator absorption). Rotation
skills (`verify-rotation-citation`, `propose-rotation`) are not invoked by name,
but rotation-shaped diligence is present; this is a non-blocking telemetry check.

### Issues found

1. **(cross-reference-integrity, both themes, warning)** No `SUMMARY.md`
   registration is proposed for either new chapter. `reports/.../CYCLE.md` §Proposed
   changes edits `book/src/L1-L0/index.md` and `book/src/L2-L1/index.md` (theme
   tables) but omits the corresponding `book/src/SUMMARY.md` nested-list entries
   that every existing chapter has (`SUMMARY.md:58-65`). Result: both new files
   would be orphaned from mdBook nav. Repair candidate: add SUMMARY entries
   `- [chebyshev-smoother-mutation-rotation](./L1-L0/chebyshev-smoother-mutation-rotation.md)`
   under the L1-L0 Overview, and
   `- [chebyshev-iteration-fusion](./L2-L1/chebyshev-iteration-fusion.md)` under
   the L2-L1 Overview (`SUMMARY.md:39`).

2. **(cross-reference-integrity, L2>L1 index edit, minor)** The
   `edit:book/src/L2-L1/index.md` block supplies `## Theme list` + the table, but
   the current `index.md:11-13` has a fenced placeholder `(empty — Phase B
   skeleton.)` between `## Theme list` (:9) and `## Working Notes` (:15). The
   integrator must REPLACE the placeholder fence, not merely append, or the
   rendered page will show both the placeholder and the table. Flag for the
   integrator's attention (the edit block's intent is clearly replacement).

3. **(citation-validity, fusion §Verified-against, sub-blocking minor)** The
   element-kernel ranges `chebyshev.cpp:55-78` (labeled `ApplyOrder0`) and
   `:80-123` (labeled `ApplyOp accumulating + ApplyOrderK`) start mid-prior-symbol
   (the accumulating `ApplyOp` overload begins at :49/:54, `ApplyOrder0` real
   begins at :68, `ApplyOrderK` real at :112). The ranges are in-range and cover
   the named kernels, but the start boundaries are loose. Optional tightening:
   `ApplyOrder0` real = `:68-78`, `ApplyOrderK` real = `:112-123`. Not a
   correctness defect.

4. **(observation, not an issue)** The L1 anchor cites the transpose alias at
   `chebyshev.hpp:72-75` (`L1/chebyshev-smoother.md:150`) while this report cites
   the more precise `:73-76`. The report is correct (`MultTranspose2` body spans
   73-76); the discrepancy is in the existing anchor, not this report. Noted for
   completeness — not a finding against this report.

## Repair

### Fixes attempted

- **Finding (Issue 1 — cross-reference-integrity, warning, primary):** No
  `SUMMARY.md` registration proposed for EITHER new chapter
  (`L1-L0/chebyshev-smoother-mutation-rotation.md`,
  `L2-L1/chebyshev-iteration-fusion.md`) → both orphaned from mdBook nav.
  - **Decision:** repaired.
  - **Action:** Added two `edit:book/src/SUMMARY.md` proposed-changes blocks to
    `CYCLE.md` §"SUMMARY.md registration (repairer-added, cycle-013)" (after the
    `L2-L1/index.md` edit block), per the `summary-md-surgical-insert` skill
    (literal-string anchors, not byte offsets):
    1. L1>L0 — surgical insert anchored on the `minres-iteration` sibling row
       (the alphabetically/positionally-last existing theme under
       `# L1 > L0 — Lowering`): append
       `- [chebyshev-smoother-mutation-rotation](./L1-L0/chebyshev-smoother-mutation-rotation.md)`.
    2. L2>L1 — surgical insert anchored on the `# L2 > L1 — Lowering` Part heading
       + its `Overview` row (the only existing entry; `chebyshev-iteration-fusion`
       is the FIRST chapter under that previously-empty Part): append
       `- [chebyshev-iteration-fusion](./L2-L1/chebyshev-iteration-fusion.md)`.
    Verified against the live `book/src/SUMMARY.md`: the `# L2 > L1 — Lowering`
    Part heading (SUMMARY.md:38) + lone `Overview` row (SUMMARY.md:39) exist with
    no chapter children — confirming first-chapter status; the `minres-iteration`
    row (SUMMARY.md:65) is the last L1-L0 theme. The L2-L1 Part header already
    exists, so no new Part header is needed (only the chapter row).

- **Finding (Issue 2 — cross-reference-integrity, minor):** The
  `edit:book/src/L2-L1/index.md` block supplies `## Theme list` + table but the
  live `index.md` has a fenced placeholder `(empty — Phase B skeleton.)` between
  `## Theme list` and `## Working Notes`; the integrator must REPLACE the
  placeholder fence, not append.
  - **Decision:** repaired.
  - **Action:** Added an explicit "Integrator note (repairer, cycle-013)" before
    the `L2-L1/index.md` edit block in `CYCLE.md` stating the edit is a
    REPLACEMENT of the three-line placeholder fence (` ``` ` /
    `(empty — Phase B skeleton.)` / ` ``` `), showing the current page structure
    so the rendered page shows only the table. Verified the placeholder against
    live `book/src/L2-L1/index.md:11-13`.

- **Finding (Issue 3 — citation-validity, sub-blocking minor):** Element-kernel
  citation ranges `chebyshev.cpp:55-78` (labeled `ApplyOrder0`) and `:80-123`
  (labeled `ApplyOp accumulating + ApplyOrderK`) have loose start boundaries
  relative to the named real kernels.
  - **Decision:** repaired (small-offset citation tightening).
  - **Action:** Re-read `chebyshev.cpp:49-123` via `palace-codemap read_range`;
    confirmed `ApplyOrder0` real kernel body is `:68-78` and `ApplyOrderK` real
    kernel body is `:112-123` (matching the critic's suggested tightenings).
    Tightened the two claim-attached citations in the fusion theme: §"The fusion"
    point 2 (`:55-78, :114-123` → `:68-78, :112-123`) and §Verified-against (the
    two element-kernel rows now cite `:68-78` ApplyOrder0 real and `:112-123`
    ApplyOrderK real, with overload labels). Left the bottom-level §Supporting
    evidence coverage spans (`:55-78`, `:80-123`) as-is — those are accurate
    multi-symbol read-coverage spans (labeled "non-accumulating + ApplyOrder0" /
    "accumulating overload + ApplyOrderK"), not claim-attached citations, so they
    correctly describe what was read.

- **Finding (Issue 4 — observation, not an issue):** L1-anchor transpose-alias
  citation `chebyshev.hpp:72-75` vs this report's more-precise `:73-76`.
  - **Decision:** not-needed.
  - **Rationale:** The discrepancy is in the existing artifact anchor
    (`L1/chebyshev-smoother.md`), NOT in this report; the report's `:73-76` is
    correct. Repairing the artifact is out of repair authority (repairer does not
    modify `book/`). No action on this report.

### Unrepairable findings

None. All four critic findings were either mechanically repaired (Issues 1, 2, 3)
or are not findings against this report (Issue 4). No substantive authoring was
required; all fixes were surgical (SUMMARY.md registration with obvious slugs,
placeholder-replacement note, small-offset citation tightening verified against
re-read source).

## Suggested resolution

`ready` — both themes passed all 8 critic checks (cross-reference-integrity was
the sole `warning`, now resolved by the repairer-added SUMMARY.md registrations).
Notes for the integrator:
- Apply the two new `edit:book/src/SUMMARY.md` blocks via surgical literal-string
  Edits (per `summary-md-surgical-insert`); re-read SUMMARY.md fresh just before
  each Edit in case other cycle-013 per-report integrators inserted rows upstream.
- The `L2-L1/index.md` edit is a REPLACEMENT of the Phase-B placeholder fence, not
  an append (see the repairer's integrator note in CYCLE.md).
- `chebyshev-iteration-fusion` is the FIRST chapter under the L2-L1 Part — the
  Part heading already exists in SUMMARY.md; only the chapter row is added.
