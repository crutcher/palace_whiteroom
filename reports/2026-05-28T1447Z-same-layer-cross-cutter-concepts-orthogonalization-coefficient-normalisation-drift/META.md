---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T14:56Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-05-28T15:10Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L1 observation — concepts/orthogonalization coefficient/normalisation drift"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing claim carries a pointer and the pointers
resolve in-range. I read both center files in full. The four drift points are all
verifiable against `book/src/concepts/orthogonalization.md`: line 3 does carry
`h = (h_0, …, h_{j+1})` with `h_{j+1} = ‖w'‖`; lines 26-63 are a genuine second concept
block; line 54 reads "`w` may be mutated; `h_coeffs` is a length-`j` vector"; lines 19/23
carry the "dedicated `orthog` slice would carry" / "(separate slice)" framing; lines 47-48
say the enum is "on the GMRES solver". The authoritative-side citations also check out:
`orthogonalize.md:30-33` ("returns the length-`m` coefficient vector only"; `H[j+1] = ‖w'‖`
is the caller's `nrm2`), `:51` (`w` read-only), `:58-59` (`H : Tensor[m]`), `:238` ("no
in-place overwrite of `w`"), `:247-250` (header "does not normalize the output"),
`:331-335` (the L1 entry's own pre-flag of this exact drift). One minor imprecision: the
report cites `orthogonalize.md:175-178` for "bound at solver setup and dispatched via
`OrthogonalizeIteration`, reused by the ROM path too" — lines 175-178 are the
*consumers* paragraph; the binding/dispatch claim is actually grounded at `:14-16` /
`:54-55` / `:264-267`. The substance holds (the L1 entry does say all of this); only the
one line-anchor is loose. Not enough to fail the check.

**surface-or-evidence — pass.** This is not a refinement-shaped proposal against an
existing operator/theme; it is a cross-cut observation that modifies a concept page's
*surface* (the proposed-changes block fully rewrites `concepts/orthogonalization.md`) and
backs every change with evidence from the firm L1 entry and the L0 header. The change is
surface + evidence, so the check is satisfied. (No rotation_claim is involved — concept
pages are narrative, not rotations.)

**rotation-quality — pass (not applicable to a same-layer cross-cut).** The proposal
asserts no algebraic/structural/reduction rotation between layers; it is a same-layer
consistency correction of a narrative page against the firm L1 operator. No compaction
claim to evaluate.

**variant-axis-coverage — pass.** The operator carries two orthogonal variant axes
(`MGS|CGS|CGS2` and the `dot_op` inner-product hook). The rewrite covers both: the three
GS variants are each described with their collective shape (m×1 / 1×m / 2×m), and the
B-weighted `dot_op` substitution axis is called out as a second axis citing
`romoperator.cpp:51-66`. Householder is explicitly scoped out ("out of scope, no Palace L0
path"), matching the L1 entry's scope-out. No hidden branch.

**cross-reference-integrity — warning.** Most links in the rewrite resolve: I confirmed
`L1/orthogonalize.md`, `L1/dot.md`, `L1/axpy.md`, `L2/krylov-step.md`,
`concepts/sequential-obstruction.md`, `concepts/variant-absorption.md`,
`spec/slices/orthog.md`, and `spec/slices/gmres.md` all exist. The named slugs
(`orthogonalize`, `dot`, `axpy`, `krylov-step`, `OrthogonalizeIteration`) all exist. The
wave-1 theme slug `orthogonalize-mutation-rotation` is confirmed (the abstractor report's
scope produces exactly that file). **However**, the rewrite links
`../L1-L0/orthogonalize-mutation-rotation.md` in three places (proposed-changes lines
~121, ~149, ~181) and that file does **not yet exist** in `book/src/L1-L0/` (current
contents: apply-linop, axpby, axpbypcz, bicgstab, eigsolve, index, ksp-solve, minres). It
is the cycle-013 wave-1 theme pending in the same batch. The link dangles until that
report's proposed-changes land. The report flags this itself (caveats, CYCLE.md:240-247)
and prescribes the batch ordering (apply the theme before/with this one). This is a real
but self-disclosed ordering hazard, hence warning not fail.

**edge-label-fidelity — pass (not applicable).** This report carries no L_{n+1}→L_n edge
label; it is a same-layer concept-vs-operator cross-cut. The prose's directional claims
(L1 entry is authoritative; caller owns `nrm2`; L1>L0 theme is the forward lowering) are
all consistent with the artifact.

**plan-kind-consistency — warning.** The report self-declares
"`drift-found-with-corrections`" and frames itself as a same-layer-cross-cutter
*observation*. The content shape is mostly consistent with an observation (one contradiction,
clearly scoped, evidence-backed). The tension is the **proposed-changes block**: it is a
near-total authored rewrite of a concept page (~100 lines of new narrative content),
which is layer-intro-author territory per the write-authority partition, not a surgical
same-layer-cross-cutter correction. The report acknowledges this directly (caveats,
CYCLE.md:235-239) and offers two routes (apply directly, or re-route through
layer-intro-author). The content does NOT over-reach into enacting a unification — it
defers all mechanics to the L1 entry + the wave-1 theme and adds no new operator/theme — so
the observation discipline holds on substance. The classification mismatch is purely the
authoring-vs-observing boundary: a same-layer-cross-cutter emitting a full concept-page
rewrite is a kind-shape drift the integrator should resolve (apply-as-is vs route to
layer-intro-author). Flagging as warning, not fail, because the report itself surfaces the
boundary rather than hiding it.

**skill-uptake-survey — warning (telemetry only).** The report's shape implies relevant
skills exist and were not referenced. `verify-citation-range` would naturally apply to the
~10 cross-file citations this report makes (especially the inherited-citation sub-case the
cycle-012 meta-phase added to that skill, since this report inherits citations from the L1
entry and the wave-1 theme). No skill invocation is recorded. This is a pure presence
check (non-blocking); surfacing it as telemetry.

### Issues found

1. **Dangling cross-reference to a not-yet-landed file (cross-reference-integrity).**
   Proposed-changes block, three occurrences of `../L1-L0/orthogonalize-mutation-rotation.md`
   (CYCLE.md proposed-changes ~lines 121, 149, 181). Target file does not exist in
   `book/src/L1-L0/`; it is the cycle-013 wave-1 abstractor theme pending in the same batch.
   Severity: medium. `cargo make book` at integrator-finalize will break on this link unless
   the wave-1 theme's proposed-changes land first/together. The report flags the ordering
   (CYCLE.md:240-247); the integrator must honor it.

2. **Kind-shape drift: same-layer-cross-cutter emitting a full concept-page rewrite
   (plan-kind-consistency).** CYCLE.md "Proposed changes" (lines 108-208) is a ~100-line
   authored replacement of `concepts/orthogonalization.md`, which is layer-intro-author
   territory per the write-authority partition. Severity: low (self-disclosed at
   CYCLE.md:235-239; integrator decides apply-direct vs route-through-layer-intro-author).
   The observation discipline holds on substance (no enacted unification, no new
   operator/theme), so this is a routing/authority question, not a content over-reach.

3. **Loose line-anchor on one inherited citation (citation-validity).** CYCLE.md:80-81
   cites `orthogonalize.md:175-178` for the "bound at solver setup … reused by the ROM
   path" claim; that line range is the consumers paragraph, and the binding/dispatch fact
   is actually at `:14-16` / `:54-55` / `:264-267`. Severity: low. The claim is true and
   well-grounded elsewhere in the same file; only the pointer is imprecise.

4. **Internal citation-style inconsistency in the rewrite vs the L1 entry (citation-validity,
   cosmetic).** The rewrite cites the GMRES/FGMRES Arnoldi call sites as
   `iterative.cpp:629-632, 808-811` (proposed-changes ~line 194) while the firm L1 entry
   cites `:630, 809` and the wave-1 theme cites `:630` / `:809`. The ranges overlap (the
   rewrite includes the call + the following `nrm2`/`scal`), so this is consistent in
   substance, but the integrator may want to align the anchors across the three artifacts.
   Severity: cosmetic.

### Verification notes (positive confirmations the task requested)

- **(a) Drift verdict is real.** Confirmed by reading both files. `concepts/orthogonalization.md`
  carries (i) line-3 normalisation conflation (`h_{j+1}=‖w'‖` folded in → length `j+2`),
  (ii) a genuine duplicate second concept block (lines 26-63) with an L0-mutating signature
  ("`w` may be mutated") and a length-`j` coefficient claim, and (iii) stale "separate
  slice" framing (lines 19, 23). The firm `L1/orthogonalize.md` is correctly the authority:
  it states the operator "does not normalize its output" (`:29`, `:247-250`, header
  `orthog.hpp:18-23`), returns `H : Tensor[m]` length-`m` only (`:58-59`), and `w` is
  read-only with "no in-place overwrite" (`:51`, `:238`). The L1 entry itself pre-flags this
  exact concept-page drift (`:331-335`). Contradiction confirmed; authority correctly assigned.
- **Three inconsistent coefficient lengths confirmed.** Concept page: line 3 ⟹ `j+2`;
  line 15 (`V[0..j]`, m = j+1) ⟹ `j+1`; line 54 ⟹ `j`. Three distinct lengths in one file.
- **(c) Rewrite resolves to one correct length.** The proposed single-block rewrite uses
  length-`m` `H[0..m-1]` throughout (proposed-changes lines ~116, ~132-133, ~135, ~177),
  matching the L1 entry's `Tensor[m]`, and the sub-diagonal `H[m]=‖w'‖` is explicitly
  excluded as the caller's `nrm2` step. Internally consistent; resolves the three-length
  drift to the one correct convention.
- **(b) No over-reach.** The rewrite enacts no unification: it adds no new operator or
  theme, defers all mechanics to the L1 entry + wave-1 theme, and explicitly labels the L1
  entry as "the load-bearing contract; this page is the narrative cross-cut … Where this page
  and the L1 entry disagree, the L1 entry wins." The substance stays within observation
  discipline. (The only kind-tension is the authoring volume — issue 2, a routing question,
  not a unification.)
- **(d) Cross-reference with the wave-1 theme confirmed.** Read the wave-1
  `orthogonalize-mutation-rotation` report. It agrees with the L1 entry on every checked
  point: three variant loop-structures (MGS single interleaved / CGS split two-phase / CGS2
  doubled, sub-patterns A/B/C lines 85-192), "basis normalised; output not — the
  sub-diagonal `Hj[j+1]=‖w'‖` is the caller's, not a coefficient this rewrite produces"
  (applicability condition 3, lines 209-213), and the length-`m` `H` distinct from the
  caller's `nrm2`. The concept page is correctly identified as the lone outlier.

## Repair

### Fixes attempted

- **Finding (cross-reference-integrity, warning)**: rewrite links
  `../L1-L0/orthogonalize-mutation-rotation.md` (3 places) to a file that does not exist yet —
  it is the cycle-013 wave-1 abstractor theme pending in THIS SAME batch
  (`reports/2026-05-28T0915Z-abstractor-orthogonalize-mutation-rotation-l1-l0-theme/`).
  - **Decision**: repaired (as a staging-order directive, not a link edit).
  - **Action**: Links left intact (target is real, lands this batch). Integrator note:
    integrator-per-report must apply the `orthogonalize-mutation-rotation` L1>L0 theme report
    BEFORE this concept-audit report (serial apply ordering) so the link resolves before
    `cargo make book` runs at integrator-finalize. This is a staging-order hazard, not a broken
    link — removing the links would be wrong (the firm forward-lowering target is the correct
    cross-ref).

- **Finding (citation-validity, low)**: loose anchor `orthogonalize.md:175-178` (CYCLE.md
  drift point 4) cited for the binding/dispatch fact, which actually lives at
  `:14-16` / `:54-55` / `:264-267` (175-178 is the consumers paragraph).
  - **Decision**: repaired.
  - **Action**: CYCLE.md §"Specific finding" point 4 — corrected
    `orthogonalize.md:175-178` → `orthogonalize.md:14-16, 54-55, 264-267`. Mechanical anchor
    offset fix; substance unchanged (the L1 entry does ground this claim).

- **Finding (plan-kind-consistency, warning)**: same-layer-cross-cutter emitting a ~100-line
  full concept-page rewrite is layer-intro-author territory per the write-authority partition.
  - **Decision**: repaired (acknowledged-and-flagged; no content change).
  - **Action**: Recorded for integrator awareness — NOT shrunk. The rewrite is sound: it
    collapses the page's three mutually-inconsistent coefficient lengths (`j+2` / `j+1` / `j`)
    to the one correct length-`m` convention, drops the L0 "`w` may be mutated" leak, and
    defers all mechanics to the L1 entry + wave-1 theme (no new operator/theme, no enacted
    unification — observation discipline holds on substance). The kind-tension is purely the
    authoring volume; it is self-disclosed at CYCLE.md:235-239. Integrator decides
    apply-direct vs route-through-layer-intro-author; the content is ready either way.

- **Finding (citation-validity, cosmetic — issue 4)**: rewrite cites Arnoldi call sites as
  `iterative.cpp:629-632, 808-811` while the L1 entry cites `:630, 809`.
  - **Decision**: not-needed (ranges overlap; the rewrite's wider ranges intentionally include
    the following `nrm2`/`scal`; consistent in substance). Left for optional integrator
    alignment.

- **Finding (skill-uptake-survey, warning — telemetry)**: no skill invocation recorded.
  - **Decision**: not-needed (pure presence telemetry, non-blocking; nothing to repair).

### Unrepairable findings

None. All flagged findings are either mechanically repaired or acknowledged staging/routing
notes within repair authority.

## Suggested resolution

**`ready`.** Integrator notes:
1. **Serial apply ordering (load-bearing).** Apply the wave-1
   `orthogonalize-mutation-rotation` L1>L0 theme report
   (`reports/2026-05-28T0915Z-abstractor-orthogonalize-mutation-rotation-l1-l0-theme/`) BEFORE
   this report, so `../L1-L0/orthogonalize-mutation-rotation.md` exists when this concept-page
   rewrite lands and `cargo make book` passes at finalize.
2. **Authority routing (integrator choice).** This is a same-layer-cross-cutter emitting a
   layer-intro-author-shaped concept-page rewrite. The content is sound and ready; apply
   directly or route through a layer-intro-author dispatch — substance is identical.
3. Applying this report **closes** the L1 entry's pre-flagged OQ
   "`concepts/orthogonalization.md` coefficient/normalisation drift"
   (`orthogonalize.md:331-335`).
