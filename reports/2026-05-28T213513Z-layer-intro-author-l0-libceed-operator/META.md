---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T223000Z
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
repaired_at: 2026-05-28T231500Z
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

# META: verification of "L0 file — palace/fem/libceed/operator.{hpp,cpp}"

## Critique

### Checks run

**citation-validity (pass).** This is a citation-dense L0 bundle chapter; producer-citation-drift was batch-3's strongest friction, so I spot-verified a representative sample of cited ranges with codemap `read_range` against the live source. All sampled citations are real and in-range:
- `CeedOperatorFullAssemble` @ `operator.cpp:455-523` — signature, empty short-circuit (`nsub_ops == 0`), set-mode `b_mat` all-ones count, cross-thread `hypre_CSRMatrixAdd` fold, and reciprocal `d_data[i] *= 1.0 / d_b_data[i]` scaling all confirmed verbatim. The function body ends at 523.
- `CeedOperatorCoarsen` @ `operator.cpp:525-585` — `SingleOperatorCoarsen` lambda, `CeedOperatorMultigridLevelCreate` (confirmed at 543-545), `SymmetricOperator` coarse target, `CeedOperatorCompositeGetSubList` per-sub-op loop, and `Finalize` all confirmed. Body ends at 585; `namespace palace::ceed` closes at 587 (report's subtree note says `:587` — correct).
- Test witness `test/unit/test-libceed.cpp` — `TestCeedOperatorFullAssemble` opens at 284; the assertion `REQUIRE(mat_diff->MaxNorm() < 1.0e-12 * std::max(mat_ref.MaxNorm(), 1.0))` is at line 298 exactly as quoted; `TestCeedOperator` template runs PA-apply (`TestCeedOperatorMult`) + `FullAssemble` against the same `mat_ref`.
- `set ? single-value : sum` fill lambda confirmed at `operator.cpp:404-423` exactly.
- `Mult`/`AddMult`/`MultTranspose`/`AddMultTranspose` bodies (`a==1.0` verify, `dof_multiplicity` paths, `mfem::forall` multiply-add) confirmed in the 181-240 block.
- Header (`operator.hpp:1-96`): doc comment 28-30, `Operator` body 32-65, members 35-38, `SymmetricOperator` 69-80, `CeedOperatorFullAssemble` decl 82-83, `CeedOperatorCoarsen` decl+comment 84-88, `namespace palace`/`namespace ceed` at 13/25 — all confirmed.
- `AddSubOperator` 60-87 (verify + `CeedOperatorCompositeAddSub`@73 + transpose 76-86) and `Finalize` 89-101 confirmed.
- `bilinearform.cpp:109-113` forwarder confirmed (call at 112); `bilinearform.cpp:168-181` coarsen loop confirmed (`ceed::CeedOperatorCoarsen` call at 174).
There is minor, non-material off-by-one drift between the prose tightened ranges and the producer's own subtree-derived spans (e.g. prose cites `Mult` as `181-189`/`185-188` while the subtree row gives `182-190`; the function opens at 182 with a blank at 181). Every such case is in-range and points at the right code, so this stays a pass, not a warning — but it is the same drift class batch-3 flagged and is noted for the repairer's awareness.

**surface-or-evidence (pass).** This is a net-new L0 file plus a retroactive link-retirement on an existing file, not a rotation-claim refinement. The two `fem-bilinearform-file.md` edits convert a deliberately-deferred plain-text forward reference into a live link now that the anchor lands — pure cross-reference backfill, which is allowed. No surfaceless rotation_claim present. Not the rotation-shaped proposal this check targets.

**rotation-quality (pass — not applicable).** No L_{n+1}→L_n rotation is asserted; this is an L0 ground-truth reference note. The "Notes for higher layers" section sketches future L1/L2 lift directions (PA/FA collapse, integrator-fold, set/accumulate variant axis) but explicitly frames them as forward-looking notes, not as a performed rotation. Marked pass as inapplicable to an L0-file-chapter.

**variant-axis-coverage (pass).** The file's orthogonal axes are surfaced and classified, not hidden: (i) `set` vs accumulate on full assembly — explicitly called load-bearing, both branches cited (`operator.cpp:404-423`, `496-521`); (ii) symmetric (`SymmetricOperator`, no `op_t`) vs general (forward+transpose composite) — covered; (iii) `dof_multiplicity` present (interpolation/`DiscreteLinearOperator`) vs empty (`BilinearForm`) — covered in both `Mult`/`AddMult` paths; (iv) matrix-free apply vs assembled `HypreCSRMatrix` (the PA/FA dual) — covered with the test witness. OMP/thread-count and device-copy branches are explicitly scoped out as transparent tricks under the single-rank reading rule. No hidden branch found.

**cross-reference-integrity (warning).** All five existing `[link]` targets resolve on disk (`fem-bilinearform-file.md`, `linalg-rap-file.md`, `par-types-single-rank-reading.md`, `transparent-vs-load-bearing-tricks.md`, `preconditioner-classes-overview.md`); the self-referential new-file slug `fem-libceed-operator-file.md` is correctly absent (it is what this report creates). The SUMMARY.md `[old]` anchor (the `fem-bilinearform-file` row) matches disk at line 89, so that insert will apply. **However, the third proposed edit's `[old]` block does not match the on-disk text** — see Issue 1. This is a edit-anchor (apply-time) integrity defect, hence warning rather than pass.

**edge-label-fidelity (pass — not applicable).** No L_{n+1}→L_n edge label is carried; this is a single-layer L0 file chapter. The forwarder/coarsen cross-file relationships are within-L0 source-to-source pointers, all verified against the cited call sites. Not applicable to an L0-file report.

**plan-kind-consistency (pass).** Declared shape is an L0 bundle-6 file reference note (firm L0 chapter). Content matches: concrete file-grounded prose, per-function citations, an "Evidence (representative)" block, a "Referenced from" forward-pointer section, and a self-verification supporting-evidence block. No rough-in placeholders, no `TODO`/`TBD` stubs in the authored chapter. The frontmatter `status: pending` is the dispatch-phase default and is consistent (the integrator sets terminal status). Classification is correct.

**skill-uptake-survey (pass).** The supporting-evidence block explicitly references the cycle-015 producer-citation self-verification bullet and documents `read_range`/`get_file_subtree`/`search_text` codemap usage to validate every cited range — the relevant procedural uptake for a citation-dense L0 chapter. No surfaceable gap.

### Issues found

**Issue 1 — edit-anchor mismatch on the `fem-bilinearform-file.md` Evidence-row edit (severity: medium; apply-time blocker).**
CYCLE.md "Proposed changes", third `edit:book/src/L0/fem-bilinearform-file.md` block (CYCLE.md:303-309). The `[old]` text is written as two wrapped lines with a continuation indent:
```
- `palace/fem/bilinearform.cpp:109-113` — `BilinearForm::FullAssemble`: forwards to
  `ceed::CeedOperatorFullAssemble(op, skip_zeros, set)`.
```
The on-disk content at `fem-bilinearform-file.md:158` is a **single line**:
```
- `palace/fem/bilinearform.cpp:109-113` — `BilinearForm::FullAssemble`: forwards to `ceed::CeedOperatorFullAssemble(op, skip_zeros, set)`.
```
The mid-sentence line break plus 2-space continuation indent in the `[old]` block do not exist on disk, so an exact-match application of this edit will fail to find its anchor. (The first `fem-bilinearform-file.md` edit, the prose at 61-66, and the SUMMARY.md insert both match disk and are fine.) Repair candidate: reflow the third edit's `[old]`/`[new]` to the single-line on-disk form, or otherwise reconcile the anchor whitespace.

**Issue 2 — prose-vs-subtree line-citation drift (severity: low; non-blocking).**
Throughout the chapter and "At a glance" / apply sections, several prose tightened ranges differ by ~1 line from the producer's own `get_file_subtree`-derived spans recorded in the Supporting-evidence block: e.g. `Mult` cited `181-189`/`185-188` in prose vs `182-190` in the subtree row; `AddMult` `191-211` vs `192-212`; `Finalize` `89-101` vs `89-101` (matches). All are in-range and point at the correct code, so no claim is unsupported. Flagged only because off-by-one citation drift is the recurring batch-3 friction class and a future lowering-verifier per-line audit would want the prose ranges reconciled to the verified function spans. Not a correctness defect.

**Note (not an issue) — phase-boundary clean.** Verified the producer stayed within the reports directory: `git status` shows zero uncommitted `book/` modifications, the new `book/src/L0/fem-libceed-operator-file.md` does not exist on disk (correctly deferred to the integrator), and the report dir contains only `CYCLE.md`. No repeat of the cycle-012 layer-intro-author write-authority phase-boundary violation.

## Repair

### Fixes attempted

- **Finding (Issue 1)**: cross-reference-integrity warning — edit-anchor mismatch on the third proposed edit (CYCLE.md:303-309, targeting the `fem-bilinearform-file.md:158` Evidence row). The `[old]` block was written as two wrapped lines with a 2-space continuation indent, but the on-disk content at `fem-bilinearform-file.md:158` is a single line, so an exact-match application would fail to find its anchor.
  - **Decision**: repaired.
  - **Action**: Read `book/src/L0/fem-bilinearform-file.md:158` to capture the exact on-disk single-line text, then reflowed the third proposed-changes block in `reports/2026-05-28T213513Z-layer-intro-author-l0-libceed-operator/CYCLE.md` ("Proposed changes", third `edit:book/src/L0/fem-bilinearform-file.md` block). The `[old]` now matches disk verbatim as a single line: `` - `palace/fem/bilinearform.cpp:109-113` — `BilinearForm::FullAssemble`: forwards to `ceed::CeedOperatorFullAssemble(op, skip_zeros, set)`. ``  The `[new]` is the corresponding single-line edited form with the plain-text reference converted to a live link: `` ... set)` (body in [`fem-libceed-operator-file`](./fem-libceed-operator-file.md)). ``  Pure whitespace/reflow reconciliation of the edit anchor — no content change to the proposed edit's substance (the link target and surrounding text are exactly as the producer authored). Mechanical and surgical.

- **Finding (Issue 2)**: prose-vs-subtree line-citation drift (severity: low; non-blocking) — several prose tightened ranges differ by ~1 line from the producer's own `get_file_subtree`-derived spans (e.g. `Mult` `181-189`/`185-188` vs subtree `182-190`; `AddMult` `191-211` vs `192-212`). All in-range, all point at the correct code; no claim unsupported.
  - **Decision**: not-needed (informational).
  - **Rationale**: the critic explicitly classified this as a pass-level, non-blocking note for a future lowering-verifier per-line reconciliation, not a correctness defect. There is no anchor that will fail to apply and no unsupported claim. Reconciling the prose ranges to the verified function spans is a content/precision decision over which sub-range to cite — that is substantive authoring, out of repair scope. Left for a downstream lowering-verifier per-line audit.

### Unrepairable findings

None. The single apply-time blocker (Issue 1) was mechanically repairable; Issue 2 is informational and requires no repair.

## Suggested resolution

`ready` for the integrator. All three proposed edits now match their on-disk anchors exactly:
- prose edit @ `fem-bilinearform-file.md:61-66` — matched disk (critic-verified, untouched);
- SUMMARY.md insert @ `:89` — matched disk (critic-verified, untouched);
- Evidence-row edit @ `fem-bilinearform-file.md:158` — reflowed to the single-line on-disk form (this repair).

Integrator note: the second `fem-bilinearform-file.md` edit's `[new]` introduces a live link to `./fem-libceed-operator-file.md`, which is the new file created by the same report's first proposed change — apply the new-file change before (or alongside) the link-retirement edits so the link target resolves. Issue 2's ~1-line prose/subtree drift is informational only and may be reconciled by a future lowering-verifier per-line audit; it does not gate application.
