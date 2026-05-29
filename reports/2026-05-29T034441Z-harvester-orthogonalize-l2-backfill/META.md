---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T035500Z
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
repaired_at: 2026-05-29T040000Z
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

# META: verification of "Formalize orthogonalize at L2 (corrective backfill)"

## Critique

This report is a CORRECTIVE BACKFILL of a cycle-019 fence-truncation defect: the landed
`book/src/L2/orthogonalize.md` is confirmed to be only the 14-line intro paragraph (I read it
this dispatch — lines 1-14 intro + blank line 15, no `## Status`, no Signature, no laws, no
Evidence), while `SUMMARY.md:41` and the `L2/index.md:27` dep-map row both already say `firm`.
The body content was pre-vetted in cycle-019; per the dispatch framing my focus was (1)
independently verifying citation line-exactness against source via `palace-codemap read_range`,
and (2) confirming the recovery is faithful and the fence-truncation bug is NOT reproduced. I
read every key cited range myself. The report passes all 8 checks.

### Checks run

**citation-validity (DOMINANT) — pass.** I independently re-read every L0 range cited in the
recovered body against source via `read_range` / `search_text`; all land on the asserted
construct, and the report's self-verification log is accurate. Confirmed: `orthog.hpp:22` is the
"Assumes that the input vectors are normalized, but does not normalize the output vectors!"
contract; `orthog.hpp:25-37` is `IdentityInnerProduct` + the `InnerProductHelper` concept;
`:38-53` is `OrthogonalizeColumnMGS` with the per-`j` `H[j]=dot_op(...)` / `Mpi::GlobalSum(1,&H[j],comm)`
/ `w.Add(-H[j],V[j])` interleaving; `:55-89` is `OrthogonalizeColumnCGS` with the `m==0` guard
at `:62-64` (`if (m == 0)` at 62, `return;` at 64), the batched `Mpi::GlobalSum(m, H, comm)`,
and the `refine`/`dH`/`H[j]+=dH[j]` CGS2 second pass; `iterative.cpp:308-325` is the
`OrthogonalizeIteration` switch with `CGS2 = OrthogonalizeColumnCGS(..., j+1, true)`;
`iterative.cpp:630-632` and `:809-811` are the GMRES/FGMRES `OrthogonalizeIteration` + `Norml2`
+ `*= 1.0/Hj[j+1]` consumer sequences (both verbatim identical at the cited lines);
`romoperator.cpp:51-66` is the ROM `OrthogonalizeColumn` wrapper forwarding `dot_op`;
`romoperator.cpp:224-226` is the canonical-hook consumer (`OrthogonalizeColumn` at 224, `Norml2`
at 225, `*= 1.0/R(dim_Q,dim_Q)` at 226); `romoperator.cpp:631-646` is the B-weighted closure
consumer with the `[&W = *(this->weight_op_W), &r = this->r]` capture (capture line 635,
`W.InnerProduct(x, y, r.Real())` at 636). All six `test-orthog.cpp` TEST_CASE boundaries
(`99`/`123`/`164`/`234`/`276`/`333`) match `search_text ^TEST_CASE` exactly; the orthogonality
assertion `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` is at line 158 inside the loop 154-159 (close
160); the empty-prefix `CHECK_THAT(w, RangeEquals(w_orig))` is at line 120. **The claimed
`71-96 → 71-97` correction is verified RIGHT:** the `orthogonalize_wrapper` class's `operator()`
closes with `}` at line 96 and the class closes with `};` at line 97, so `71-97` is the correct
class span and the cycle-019 `71-96` was an off-by-one (landed on the `operator()` close). The
backfill applied the right fix.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (full-file replacement of an
existing chapter), but it is pure recovery of pre-vetted firm content, which the surface-or-evidence
discipline treats as allowed (retroactive recovery of a defect-truncated landing, not a new
rotation_claim). Independent of that allowance, the body's load-bearing claims are grounded in
the source I read: the `gs_orthog` collective-shape residual axis (`m×1` MGS = `m` `GlobalSum(1,…)`
calls; `1×m` CGS = one `GlobalSum(m,…)`; `2×m` CGS2 = two) is directly witnessed by the MGS
per-`j` `Mpi::GlobalSum(1,&H[j],comm)` vs the CGS batched `Mpi::GlobalSum(m, H, comm)` vs the
CGS2 `refine` re-entry; the `project ▷ subtract` composition maps to the CGS `H[j]=dot_op(...)`
loop then `w.Add(-H[j],V[j])` loop; the no-output-normalisation boundary is the `orthog.hpp:22`
header contract plus the four consumer-side `Norml2`+`scal` sites. Composition-level laws are
restatements of inherited firm-L1 facts or standard Gram-Schmidt facts with the floating-point
caveats recorded as explicit non-laws. Grounded.

**rotation-quality — pass.** The entry is authored high→low in L2 vocabulary: it names the
composition and surfaces composition-level laws without re-deriving L1-primitive laws, and the
L2>L1 lowering is correctly a plain-text forward-reference (not embedded). The rotation is a
genuine fusion-rotation: L1's single opaque parameterised dispatch wrapper is unfolded into the
canonical `project ▷ subtract` composition with the per-variant batching/sequencing made
first-class (the residual axis), which is strictly more abstract/equational than the L1 leaf's
opaque-parameter form — not a renaming. The recovered body matches the canonical firm-L2 shape:
no YAML frontmatter (begins `# orthogonalize`, like `inner_product.md` / `linear_combination.md`
/ `krylov-step.md`), and the section sequence (Context → Signature → Semantics → Algebraic laws →
Dependencies → Variant axes → Status → L2 vs L1 distinction → Evidence) matches the
`linear_combination.md` core sequence. It folds the "Sibling fold" / "Fusion note" material into
§Dependencies and §Semantics rather than carrying them as standalone sections — a reasonable
variation, not a shape defect.

**variant-axis-coverage — pass.** Both orthogonal axes are covered explicitly. The `gs_orthog ∈
{MGS, CGS, CGS2}` axis is the visible content of the entry, each value with its own
batching/sequencing characterisation and load-bearing primitive. The `dot`-hook axis (`canonical
⟨·,·⟩` vs `B-weighted`) is covered as a parametric closure substitution (laws-invariant). The
element-type axis (`real | complex`) is explicitly scoped as fully parametric (absorbed by the
`dot` dependency, tests at `:123/:234/:276/:333`). Householder is explicitly scoped OUT with a
citation-backed justification (`variant-absorption.md:131` + the absence of a Householder path in
`orthog.hpp`, per the unimplemented-component policy). No hidden branches.

**cross-reference-integrity — pass (the fence-correctness crux is clean).** All `[link]`
references resolve: `../L1/orthogonalize.md`, `../L1/dot.md`, `../L1/axpy.md`,
`./inner_product.md`, `./linear_combination.md`, `./krylov-step.md`, and concepts
`orthogonalization.md` / `sequential-obstruction.md` / `variant-absorption.md` all exist; the
`../../../skills/classify-variant-axis/SKILL.md` link points at an existing file and is covered
by the `book.toml` `traverse-parent-directories = true` + `.*/skills/.*` linkcheck-exclude
convention (will NOT break the build; same link inherited verbatim from the cycle-019 body at
report line 329). The `L2-L1/orthogonalize-composition-lowering.md` forward-reference correctly
stays plain-text — the chapter does not exist. **Fence-correctness verified: the truncation bug
is NOT reproduced.** The single `edit:book/src/L2/orthogonalize.md` block opens at report line 51
and closes at report line 473, which is the line immediately AFTER the final Evidence bullet
(line 472, `variant-absorption.md:131`). The three nested ` ```text ` fences (108/110, 142/144,
165/170) are all balanced pairs inside the block. Fence parity is even and correct. **No
double-edit:** the report proposes NO change to `L2/index.md` or `SUMMARY.md` — I confirmed both
already say `firm` (dep-map row `L2/index.md:27`, `SUMMARY.md:41`), so the no-re-touch decision is
correct.

**edge-label-fidelity — pass (not applicable to this report-kind).** This is an L2 operator entry,
not a lowering theme; it carries no `L_{n+1}→L_n` edge label. The L2-vs-L1 framing throughout is
internally consistent (L1 = opaque parameterised leaf; L2 = named composition).

**plan-kind-consistency — pass.** The declared shape (a corrective backfill landing a full firm
L2 chapter) matches the content: the `## Status` section asserts `firm` with full-read L0
justification, the Signature/Semantics/laws/Evidence are complete, and there are no rough-in
placeholders. One forward-reference (the L2>L1 lowering) is correctly plain-text, consistent with
a firm operator entry whose lowering theme is not yet authored.

**skill-uptake-survey — pass.** The report references `classify-variant-axis` and follows its
per-axis output contract (absorption path / load-bearing primitive / state binding) in §Variant
axes, which is the relevant skill for this operator's variant-axis shape. The citation
re-verification is consistent with `verify-citation-range`'s audit-report/inherited-citation
sub-case (re-verify inherited pointers rather than trust them). Pure telemetry; no blocking
finding.

### Issues found

No blocking or warning-level issues. The recovery is faithful, the fence-truncation bug is not
reproduced, and every independently-checked citation lands on its asserted construct. The items
below are minor prose imprecisions in the recovered body (each is candidate-for-repair only at the
copy-edit level; none affects citation validity, the rotation, or build-readiness):

- **`test-orthog.cpp:154-159` is a per-RANK loop, called "per-column" in the body** —
  `book/src/L2/orthogonalize.md` §Algebraic laws law 1 and the Evidence bullet describe the
  orthogonality-check loop as "the per-column orthogonality-check loop." The actual loop (read
  this dispatch) iterates `for (int i = 0; i < mpi_size; i++)` over MPI ranks, with the assertion
  `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` at line 158. The substantive claim (`⟨residual, V[i]⟩ ≈
  0` is asserted to `1e-12`) and the cited line numbers are exact; only the "per-column"
  descriptor is imprecise (it is per-rank within the orthogonality check). Severity: cosmetic.

- **FGMRES `Z[j]` framing in the frontmatter/body vs the cited `:809-811` lines** — the report's
  frontmatter and §Semantics describe the FGMRES consumer as using a "`Z[j]` flexible-preconditioner
  basis"; the cited `iterative.cpp:809-811` range I read shows the same `V`/`w`
  `OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j)` + `Norml2` + `scal` sequence as GMRES
  (the `Z[j]` distinction lives elsewhere in the FGMRES routine, not at 809-811). The cited lines
  correctly land on the call+norm+scal sequence the body attributes to them; the `Z[j]` mention is
  contextual color, not a claim pinned to `:809-811`. Severity: cosmetic.

- **Out-of-book `skills/` markdown link is a not-previously-exercised pattern in the firm L2/L1
  corpus** (no sibling L2/L1 entry currently links `../../../skills/...`). It is build-safe under
  the existing `book.toml` linkcheck-exclude (`.*/skills/.*`) + `traverse-parent-directories`
  convention, so this is NOT a defect — surfaced only as telemetry that this entry is the first
  firm-corpus consumer of that link form, in case the integrator wants to confirm `cargo make
  book` clean on it.

- **(Telemetry, not a report defect) Producer-side fencing-discipline gap** — the report's own OQ
  section already recommends the meta-phase log a friction-ledger entry for the recurring "firm
  chapter body authored outside the proposed-changes fenced block" pattern and add a critic
  build-readiness guard (flag when a dep-map/SUMMARY row says `firm` but the target chapter has no
  `## Status`). I concur this is the right escalation: the cycle-019 critic+repairer validated
  content but the truncation slipped because the prose carried the body. This belongs in the
  friction-ledger / meta-phase channel, not as a finding against this (correcting) report.

## Repair

### Fixes attempted

- **Finding**: `test-orthog.cpp:154-159` orthogonality-check loop is a per-RANK loop (iterates
  `for (int i = 0; i < mpi_size; i++)`), described as "per-column" in the recovered body.
  - **Decision**: repaired
  - **Action**: CYCLE.md §Algebraic laws law 1 (inside the `edit:book/src/L2/orthogonalize.md`
    fenced block, so it lands in `book/`): "the per-column orthogonality-check loop" →
    "the per-rank orthogonality-check loop". Also corrected the matching descriptor in the
    Citation self-verification log table row for `:154-159` (report telemetry, outside the fenced
    block) and annotated it "(iterates over MPI ranks)" for clarity. Trivial wording swap; the
    substantive claim (`⟨residual, V[i]⟩ ≈ 0` to `1e-12`) and the cited line numbers (assertion
    at `:158`, loop `:154-159`) are unchanged and remain exact per the critic.

- **Finding**: FGMRES `Z[j]` flexible-preconditioner framing in §Semantics / the Evidence bullet
  vs the cited `iterative.cpp:809-811` lines (which show the same `V`/`w`
  `OrthogonalizeIteration` + `Norml2` + `scal` sequence as GMRES; the `Z[j]` distinction lives
  elsewhere in the FGMRES routine).
  - **Decision**: not-needed
  - **Rationale**: The critic confirmed the cited `:809-811` lines land correctly on the
    call+norm+scal sequence the body attributes to them; the `Z[j]` mention is accurate
    contextual color about FGMRES (it does carry a flexible-preconditioner basis), not a claim
    pinned to those three lines. No citation defect to repair. Deciding how much surrounding
    context to retain is an authoring judgment, not a mechanical fix — out of repair scope, and
    nothing is wrong to begin with.

- **Finding**: the out-of-book `../../../skills/classify-variant-axis/SKILL.md` markdown link is a
  not-previously-exercised pattern in the firm L2/L1 corpus.
  - **Decision**: not-needed
  - **Rationale**: The critic explicitly classified this as NOT a defect — the link points at an
    existing file and is build-safe under the `book.toml` `traverse-parent-directories = true` +
    `.*/skills/.*` linkcheck-exclude convention (and is inherited verbatim from the cycle-019
    body). Pure telemetry for the integrator's `cargo make book` confirmation; nothing to repair.

- **Finding (telemetry, not a report defect)**: producer-side fencing-discipline gap (the
  recurring "firm chapter body authored outside the proposed-changes fenced block" pattern that
  caused the cycle-019 truncation this report corrects).
  - **Decision**: not-needed
  - **Rationale**: Not a finding against this (correcting) report. The critic routed it to the
    friction-ledger / meta-phase channel, and the report's own OQ section already recommends the
    meta-phase log the friction-ledger entry + add a critic build-readiness guard. This exceeds
    repair authority (methodology-level) and is correctly addressed there, not by editing this
    report.

### Unrepairable findings

None. The one substantive cosmetic finding (per-column → per-rank) was trivially repairable and
applied; the remaining three items are non-defects / methodology telemetry, marked not-needed.
All 8 critic checks pass and the recovery is faithful (fence-truncation bug not reproduced,
every independently-checked citation lands on its asserted construct, the `71-96 → 71-97`
boundary correction verified right).

## Suggested resolution

`ready` — apply the report's single `edit:book/src/L2/orthogonalize.md` full-file-replacement to
land the complete firm L2 `orthogonalize` body (recovering the cycle-019 fence-truncated content).
No dep-map / SUMMARY edit is proposed (both already say `firm` from cycle-019, `efb8a0b`); do NOT
re-touch them.

**ORDERING CONSTRAINT (load-bearing for the integrator):** this backfill MUST be applied to `book/`
**BEFORE** the L2-refresh report
(`reports/2026-05-29T034441Z-layer-intro-author-l2-refresh/`). The L2-refresh's
firm-`orthogonalize` assertions depend on this backfill having landed (the firm body must exist
in `book/src/L2/orthogonalize.md` before the layer-intro references it as firm). Serialize the
per-report integration so this report is applied first.

Notes for the integrator:
- After `cargo make book`, confirm the build is clean on the `../../../skills/...` link (first
  firm-corpus consumer of that out-of-book link form; expected clean under the existing
  linkcheck-exclude — telemetry only).
- The L2>L1 lowering theme (`L2-L1/orthogonalize-composition-lowering`) forward-reference
  correctly stays plain-text; that chapter does not exist yet (abstractor follow-up, already in
  the OQ ledger from cycle-019 — not re-appended here).
