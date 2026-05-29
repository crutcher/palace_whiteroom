---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T161200Z
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
repaired_at: 2026-05-29T163000Z
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

# META: verification of "L1>L0 theme sketch — nleps-eigenvalue-correction-mutation-rotation"

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck --scan` over the whole CYCLE.md: 32 citations, 32 ok, 0 failing (all in-bounds, all paths resolve under `reference/palace/`). Then anchor-checked every load-bearing pinpoint with `--anchor`; all landed exactly with zero drift:
- Primary block: `:673` (`w2.adjoint() * u2`) → 673; `:674` (`delta_eig`) → 674; `:675` (`linalg::Dot(GetComm(), w, w0)`) → 675; `:676` (`z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)`) → 676; `:677` (`z2 = -u2`) → 677. The report's central claim — that the codemap +1 drift wave-1 found is confined to the deflation block at `:659+` and the primary `:672-677` site is on-disk-correct — is **mechanically confirmed**. (`:659` is indeed the `{` opening the `if (k > 0)` deflation block, consistent with where the +1 drift would live.)
- Secondary/context anchors all land: `:672` (comment) → 672; `:587` (`compute_residual(eig`) → 587; `:657` (`opJ->Mult(v, w)`) → 657; `:540` (projection-direction comment) → 540; `:682` (`deflated_solve(z, z2, du, du2)`) → 682; `:691` (`eig_trial = eig + alpha`) → 691; `:712` (`alpha *= backtrack_factor`) → 712; `:590` (`while (it < nleps_it)`) → 590; `vector.hpp:246` (inner-product comment) → 246; `vector.cpp:674` (`LocalDot`) → 674.
- Carry-forward drift claim **verified accurate**: `--show :596` on disk is `restart, res);` (the print arg, NOT the `while` loop, which is at `:590`) — so the L1 entry's `:596` is a real −6 drift; and `--show :709` on disk is `res = res_trial;` (NOT the Armijo backtrack-factor update, which is at `:712`) — so the L1 entry's reliance on `:709` for the `α` update is a real drift. The report's characterization of both L1-entry drifts is correct, and it correctly scopes them as a carry-forward *propose-not-apply* item (dispatch-phase write-authority partition), distinct from this report's own citations which all use the corrected on-disk numbers. This is exactly the friction-ledger `producer-citation-drift-verify-not-self-invoked` pattern handled well.

**surface-or-evidence — pass.** This is a new L1>L0 lowering theme (`new:` block), not a refinement of an existing operator/theme surface. It introduces new surface (a brand-new theme file) backed by exhaustive positive-source rotation_claim evidence (the `:672-677` block read in full). Not the refinement-without-surface failure mode.

**rotation-quality — pass.** The rotation is a genuine mutation rotation: the L1 form is a pure value-returning function `(resid, jac_action, proj_dir) -> { δλ, z, z2 }` with no destination buffers, no consume-then-reuse aliasing, no Armijo `α` in the signature; the L0 form is the in-place destination-buffer block (`z`/`z2` overwritten, `u`/`u2` consumed-then-reused, `α` damping threaded through the surrounding line search). The report explicitly enumerates the L0-only residues the L1 signature hides (destination buffers + aliasing, Armijo damping/commit, projection-direction lag+normalization). This is state-hiding / threaded-state compression, not a 1:1 renaming. The decomposition into three firm BLAS-1 leaves (dot/axpby/scal) over the `−num/den` scalar Newton ratio is a real abstraction lift.

**variant-axis-coverage — pass.** The deflation cardinality axis `k = 0` (un-deflated) vs `k > 0` (deflated) is covered: the report states the `k = 0` degeneration explicitly (Applicability condition 3 + L1-form `k = 0` note — `u2`/`w2`/`z2` zero-length, `num = w0ᴴu`, `w2.adjoint()*u2 = 0` runs uniformly). The big/coordinate RHS asymmetry (`δλ` couples into `z` only, never `z2`) is treated as a load-bearing structural recording rather than a hidden branch, with the negative consequence of collapsing it spelled out ("would silently invent a coordinate Jacobian-coupling the source never computes"). The element-type axis (complex-only, no real specialization witnessed) is scoped (condition 2). Single-rank/MPI axis is flagged-and-scoped (condition 6). No hidden branches.

**cross-reference-integrity — pass.** All `[link]` targets in the `new:` body resolve on disk: `../L1/dot.md`, `../L1/axpby.md`, `../L1/scal.md`, `../L1/axpbypcz.md`, and the sibling themes `./nleps-deflated-solve-mutation-rotation.md`, `./nleps-deflated-residual-mutation-rotation.md`, `./apply-nonlinear-pencil-mutation-rotation.md`, `./dot-mutation-rotation.md`, `./axpbypcz-mutation-rotation.md`, `./scal-mutation-rotation.md` all verified present. The forward-reference to `./nleps-jacobian-action-mutation-rotation.md` (dispatch-1's not-yet-landed file) is the report's own new sibling created by dispatch-1, which the integrator applies first serially — acceptable per the serial-dispatch dependency the report documents (OQ 3). Build-readiness fence-guard: the `new:` block has clean fence parity — `grep -n` shows 6 fence markers (lines 51/505 for the `new:` file, 507/518 for the index edit, 520/530 for the SUMMARY edit), even parity, three balanced blocks; the firm `## Status` apparatus (Status + L1-form signature + L0-form + Rewrite + Justification + Verified-against) sits **inside** the `new:...md` fence (lines 52–504), not authored as the report's own top-level sections outside the fence. No nested-fence hazard: the body uses 4-space-indented code blocks (the L1/L0 form listings) rather than nested triple-backtick fences, so no fence-parity collision. Not the cycle-019/021 fence-truncation defect.

**edge-label-fidelity — pass.** The declared edge is L1>L0 throughout (frontmatter `layer: L1>L0`, slug `...-mutation-rotation`). The prose narrates forward: LHS = the pure L1 `nleps_eigenvalue_correction`, RHS = the L0 `palace/linalg/nleps.cpp:672-677` block, with the "Rewrite — forward (L1 → L0)" section narrating the pure form rewriting into the destination-buffer block. Direction discipline is correct (high→low; L1 form defined in L1 vocabulary, the lowering work narrated forward to L0). The requested LHS/RHS check passes.

**plan-kind-consistency — pass.** Declared kind is `firm` (frontmatter `status: firm`; no `partly-constructive` / `rough-in` placeholders). Content shape matches: every sub-part (A/B/C) is read from a positive source site, the laws are syntactic identities on fully-specified positive source, and the report correctly invokes the firm-on-positive-structure escape (the `apply_nonlinear_pencil` precedent) to justify `firm` despite the NLEPS test-coverage absence. The two non-syntactic facts (`⟨w0,w⟩=0` near-singularity; undamped-`δλ`) are recorded as explicit non-laws, not asserted as firm identities — the correct handling that keeps the `firm` claim honest. No mis-classification.

**skill-uptake-survey — pass.** The report references its `verify-citation-range` invocation via `tools/citecheck/citecheck.py` (`--anchor`/`--show`) in §Verified-against and §Citation source-of-truth — the expected skill for a citation-heavy lowering theme. Telemetry present; the producer-side self-verify discipline was exercised (and independently confirmed correct here).

### Issues found

No blocking or warning issues in this report's own surface. Two observations for downstream awareness (neither is a defect in THIS report):

1. **Carry-forward L1-entry drift (informational, already correctly logged).** `book/src/L1/nleps_eigenvalue_correction.md:7` cites the `while (it < nleps_it)` loop as `:596` (on-disk `:590`, −6), and `:108` relies on `:709` for the Armijo `α` update (on-disk `:709` is `res = res_trial`; the update is `:712`). I verified both via `citecheck --show`: the report's drift claim is **accurate**. The report correctly files this as a propose-not-apply carry-forward (OQ 1) rather than mutating the L1 entry (out of dispatch write-authority). The repairer/integrator should note the theme deliberately uses the corrected on-disk numbers, so theme-vs-operator-entry will disagree on these two secondary anchors until a follow-up lifter/repairer re-anchors the L1 entry. Where: CYCLE.md §Open questions item 1; root cause in `book/src/L1/nleps_eigenvalue_correction.md:7,108`. Severity: informational (carry-forward, not in-report).

2. **Integration anchor coordination is plausible and distinct (informational).** The report anchors its `index.md` row and `SUMMARY.md` entry AFTER dispatch-1's `nleps-jacobian-action-mutation-rotation` row/entry, with a documented fallback to the `nleps-deflated-solve-mutation-rotation` row (`index.md:34`, verified present) and the `apply-nonlinear-pencil-mutation-rotation` entry (`SUMMARY.md:105`, verified present). The primary anchor (dispatch-1's row) does not yet exist on disk because dispatch-1 has not been integrated — consistent with the documented serial-dispatch dependency (dispatch-1 lands first). Both the primary and fallback anchors are distinct from the row/entry this report inserts, so no edit collision. The chosen anchors are plausible and distinct as required. Severity: informational (verified sound).

3. **Expected `:673-676` citation overlap with dispatch-1 (informational).** The report (OQ 2) flags that `:673`/`:675`/`:676` are shared with dispatch-1's jacobian-action theme, but with different roles (downstream-context there, primary-subject here). This is disclosed expected overlap, not a contradiction. Severity: informational.

## Repair

### Fixes attempted

All 8 checks were graded `pass` by the critic — no blocking or warning findings on this report's own surface. The three recorded observations are all informational (carry-forward / integration-coordination / expected-overlap), not defects in THIS report, so each is `not-needed` for repair. One mechanical frontmatter fix was applied (out of the per-check matrix).

- **Finding**: citation-validity — pass. 32/32 citations ok; every load-bearing anchor lands with zero drift; the `:672-677` on-disk-correct claim mechanically confirmed.
  - **Decision**: not-needed (no defect to repair).

- **Finding**: surface-or-evidence — pass. New `new:` theme file backed by exhaustive positive-source rotation evidence.
  - **Decision**: not-needed.

- **Finding**: rotation-quality — pass. Genuine mutation rotation (pure value-return vs in-place destination-buffer block); state-hiding, not 1:1 renaming.
  - **Decision**: not-needed.

- **Finding**: variant-axis-coverage — pass. Deflation cardinality `k=0`/`k>0` covered; big/coordinate RHS asymmetry recorded as load-bearing; element-type + single-rank axes scoped. No hidden branches.
  - **Decision**: not-needed.

- **Finding**: cross-reference-integrity — pass. All `[link]` targets resolve; forward-reference to dispatch-1's not-yet-landed sibling is the documented serial dependency; fence parity clean (6 markers, three balanced blocks; 4-space-indented code, no nested-fence hazard).
  - **Decision**: not-needed.

- **Finding**: edge-label-fidelity — pass. L1>L0 throughout; LHS = pure L1 form, RHS = L0 `:672-677` block; forward narration; direction discipline correct.
  - **Decision**: not-needed.

- **Finding**: plan-kind-consistency — pass. `firm` matches content shape (every sub-part positive-source; syntactic-identity laws; firm-on-positive-structure escape correctly invoked; two non-syntactic facts recorded as explicit non-laws).
  - **Decision**: not-needed.

- **Finding**: skill-uptake-survey — pass. `verify-citation-range` exercised via `tools/citecheck/citecheck.py` (`--anchor`/`--show`); telemetry present and independently confirmed correct.
  - **Decision**: not-needed.

- **Finding** (out-of-matrix, mechanical): stale `verifies: ../REPORT.md` frontmatter pointer.
  - **Decision**: repaired.
  - **Action**: `reports/.../META.md` frontmatter — rewrote `verifies: ../REPORT.md` → `verifies: ../CYCLE.md` (the report file is `CYCLE.md` per the cycle-004 rename; the critic's frontmatter carried the legacy pointer).

### Unrepairable findings

None. No finding exceeds repair authority — all 8 checks pass, and the three observations are informational, not defects in this report.

### Carry-forward note for the integrator / follow-up (informational; NOT repaired here)

The critic's note 1 records a **carry-forward L1-entry drift** in `book/src/L1/nleps_eigenvalue_correction.md` — root cause is the L1 *operator entry*, NOT this theme report:
- `book/src/L1/nleps_eigenvalue_correction.md:7` cites the `while (it < nleps_it)` loop as `:596`; on-disk is `:590` (−6 drift; `:596` lands on a `restart, res` print arg).
- the Armijo `α` backtrack-factor is relied on via `:709`; on-disk `:709` is `res = res_trial`, and the `alpha *= backtrack_factor` update is at on-disk `:712`.

This is **out of repair scope here**: the L1 entry is artifact content (not this report's CYCLE.md / supporting docs), and the repairer does not mutate `book/`. The report correctly files it as a propose-not-apply carry-forward (CYCLE.md OQ 1) and deliberately uses the corrected on-disk numbers throughout, so the theme will disagree with the L1 entry on these two secondary anchors until the entry is re-anchored. Route to a **follow-up lifter/repairer pass on the L1 entry** (`book/src/L1/nleps_eigenvalue_correction.md:7,108`): re-anchor `:596`→`:590` and add the `:712` `alpha *= backtrack_factor` anchor. This does not gate THIS report's readiness (the theme's own citations are all verified correct).

Notes 2 (integration anchor coordination with dispatch-1, with documented fallback) and 3 (expected `:673-676` overlap with dispatch-1) are informational integrator-awareness items already disclosed in the report's OQs — no action needed.

## Suggested resolution

`ready`. The report is clean — all 8 critic checks pass and the only repair was the mechanical `verifies:` frontmatter pointer fix. For the integrator:
- Apply per the documented serial-dispatch dependency: **dispatch-1 (`nleps-jacobian-action-mutation-rotation`) lands first**, then this report anchors its `index.md` row + `SUMMARY.md` entry after dispatch-1's just-landed row/entry, with the documented fallback (`nleps-deflated-solve-mutation-rotation` row at `index.md:34` / `apply-nonlinear-pencil-mutation-rotation` entry at `SUMMARY.md:105`) if dispatch-1's row is not yet present.
- The expected `:673-676` citation overlap with dispatch-1 is disclosed expected overlap, not a contradiction.
- Spawn a follow-up lifter/repairer to re-anchor the L1 operator entry's two secondary drifts (carry-forward note above) — independent of this report's application.
