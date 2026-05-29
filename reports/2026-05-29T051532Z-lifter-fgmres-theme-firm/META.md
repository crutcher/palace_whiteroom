---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T05:34:41Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-05-29T05:38:43Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Re-anchor fgmres-inner-loop-iterate-while-migration"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing citation in the report was independently re-verified, the L0 source via `palace-codemap read_range` and the slice/index claims via direct on-disk reads.

- FGMRES L0 (all confirmed exact): `class FgmresSolver : public GmresSolver<OperType>` at `iterative.hpp:222`; `// Temporary workspace for solve.` + `mutable std::vector<VecType> Z;` at `iterative.hpp:256-257`; the constructor `FgmresSolver(MPI_Comm comm, int print)` pinning `pc_side = PreconditionerSide::RIGHT;` at `iterative.hpp:263-266`; the `SetPreconditionerSide` override `MFEM_VERIFY`-ing `RIGHT` at `iterative.hpp:268-273`; `for (;; j++, it++)` at `iterative.cpp:794`. **The crux claim that line 806 carries BOTH FGMRES deltas — `ApplyBA(PreconditionerSide::RIGHT, A, B, V[j], w, Z[j], this->use_timer);` (hard-coded `RIGHT` AND `Z[j]` workspace) — is confirmed on a single line.** `converged = (beta < eps);` at `:823`; `if (converged || j + 1 == max_dim || it + 1 == max_it)` at `:824`; the 3-condition break fingerprint `:823-828` (`converged=` 823, `if` 824, `it++; break;` 826-827, close 828) is textually identical to the GMRES site (`converged=` 644, `if` 645, close 649) modulo the `CheckDot` message string and `ApplyBA`'s 3rd arg + workspace. The out-of-scope `restart_cycle` `true_beta = linalg::Norml2(comm, Z[0]);` at `:756` after `InitialResidual` and the drift-warning compare `std::abs(beta - true_beta) > 0.1 * true_beta` (`:772-780`) confirmed and correctly scoped out.
- Slice re-anchor sweep (the cycle-019/020 inline-drift risk area — rigorously checked, ALL confirmed exact against `book/src/spec/slices/gmres.md` on disk): `inner_loop :: ... Solve (Krylov, StopReason)` signature at line **594** (`:594-606`); `check_stop :: ... -> Maybe StopReason` at **587** (`:587-592`); `data StopReason` at **551** (`:551-554`); the v0.6 constructed-operator surface-table rows `apply_BA | pc_side, (Mk if flexible)` at **648**, `orthogonalize | gs_orthog | MGS/CGS/CGS2` at **649**, `apply_correction | pc_side, flexible` at **650**, `check_stop | max_it, max_dim | stop-witness producer` at **652** (table `:645-654`); the `K.j + 1 == op.max_dim = Just StoppedMaxDim` guard at **591**; the §"Variant axes the slice exposes" L0 list at `:172-176` and the §L1 "**Variant axes** and their absorption levels" list at `:248-252`; `restart_cycle` at `:613-631`; the appended §L4 v0.7 section header at **673** (`## L4 v0.7 — inner-loop iterate_while migration`), the v0.7 `check_stop_into_carry` + migrated `inner_loop` code at **694-716**, and line **746** naming FGMRES as the second-consumer promotion trigger. The re-anchor targets are **identical to the homes the firm gmres sibling uses** (cross-checked against `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md:116-119,121,176`) — the report's claim of parallel re-anchoring holds line-for-line.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (rough-in→firm of an existing theme) carrying surface edits (Edits 1–6, 8–12) plus a status flip (Edit 11). The witness-into-carry hoist is shared with the now-firm gmres sibling (confirmed firm; its §Status reads `firm`, authored cycle-020 wave-1). The two FGMRES variant collapses are faithful to L0: `pc_side = RIGHT` is structurally pinned at the `FgmresSolver` constructor (`iterative.hpp:265`) and read at the single `ApplyBA(PreconditionerSide::RIGHT, ...)` site (`iterative.cpp:806`); `flexible = true` makes the sibling's `if op.flexible then K { Z = ... } else K` carry-update unconditional, matching the FGMRES-only `Z[j]` member being written every iteration at `:806`. The per-iteration `Z[j]` workspace is modeled as the unconditional `K { Z = K.Z `with` (K.j, z) }` — a faithful L4 representation of the L0 per-step capture. The LHS code block is genuinely unchanged (the rough-in already sketched the option-(a) `check_stop_into_carry` shape the v0.7 rotation took), so the firming rests on the now-authored shared rotation, not on new surface authorship — appropriate for a lifter re-anchor.

**rotation-quality — pass (not a fresh rotation; re-anchoring of an existing dissolution).** This dispatch authors no new rotation; it re-anchors an existing L4>L3 dissolution theme to its now-firm upstream LHS. The body primitive sequence in both the L4 LHS (theme lines 49-70) and the L3 RHS (lines 85-106) is `apply_BA → orthogonalize → ls_update_column → modify-it → check_stop_into_carry → carry-update`, unchanged from the rough-in and parallel to the firm gmres sibling's body modulo the two documented FGMRES simplifications (unconditional `Z` capture, implicit `pc_side`). The underlying L4>L3 dissolution itself is a genuine compaction (Solve-monad → positional threading; `iterate_while` combinator → tail-recursive worker; trajectory pruned to `[]` under the `final_state`-only consumer) — state-hiding/threaded-state-compression, not a 1:1 rename. The L4→L3 direction (LHS=L4, RHS=L3, prose narrates forward) is preserved.

**variant-axis-coverage — pass.** The four GMRES variant axes are each accounted for: `pc_side` collapsed to `RIGHT` (constructor pin), `flexible` collapsed to `true` (unconditional `Z` capture), `gs_orthog ∈ {MGS,CGS,CGS2}` pass-through (absorbed in `orthogonalize`), `max_dim` pass-through (folded into the stop-witness via `check_stop_into_carry`). The FGMRES-specific structural delta (`Z[j]` per-iteration workspace) is modeled in the carry, and the FGMRES initial-residual policy (`true_beta = nrm2(comm, Z[0])`) is explicitly scoped OUT to `restart_cycle` (one level up) with L0 citation. Applicability condition 6 records the subclass-level enforcement and the relaxation case (a hypothetical left-preconditioned FGMRES). No hidden branches. The `check_stop_into_carry` helper correctly stays rough-in (promotion blocked on a non-`GmresSolverBase` consumer per OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`), and the report does not over-claim a promotion.

**cross-reference-integrity — pass.** Edit 12's premise verified: `grep fgmres book/src/L4/index.md` returns no hits (the theme was genuinely absent from the L4 index — only wired into `SUMMARY.md:17`, confirmed). The Edit 12 `[old]` block matches the gmres prose-list row at `index.md:44` verbatim; the appended fgmres row is well-formed (live link `[`fgmres-inner-loop-iterate-while-migration`](../L4-L3/fgmres-inner-loop-iterate-while-migration.md)` resolves to an existing file). All other cross-referenced targets resolve on disk: `gmres-inner-loop-iterate-while-migration.md`, `krylov-step-typed-wrapper-dissolution.md`, `L4/iterate-while.md`, `L3/krylov-step.md`, `concepts/derived-view-hoisting.md`, `concepts/sequential-obstruction.md`, `concepts/variant-absorption.md`. Edit 11's `[new]` re-points the lowering-verifier follow-up from the rough-in's `gmres.md §L3` to the firm `L3/krylov-step` — that target exists, so the re-point is an integrity improvement, not just a re-anchor.

**edge-label-fidelity — pass.** The theme carries the L4>L3 edge (LHS=L4 `iterate_while` invocation, RHS=L3 value-threaded worker). All 12 proposed-changes blocks and the prose discuss exactly that edge; the §"Justification kind" abstraction-direction note (theme line 141) states "The rotation direction is L4 → L3", consistent with the edge label. No mis-labeling.

**plan-kind-consistency — warning.** The declared shape (theme rough-in→firm + L4/index add + slice-ref corrections) matches the content for 11 of 12 blocks. **Edit 7 is a non-edit**: it is a `### Edit 7` heading whose body explicitly states "No edit needed to the condition text. (Recorded for the record ...)" — it carries no `[old]`/`[new]` pair and proposes no change. This is a mis-labeled proposed-changes block (a note dressed as an edit). It is harmless (the integrator will no-op it), but it inflates the "12 proposed-changes blocks" count to an effective 11 and could confuse a mechanical parser that expects every `### Edit N` to carry an edit fence. See Issue 1.

**skill-uptake-survey — warning.** The report performs work for which relevant skills exist — a citation-range verification sweep (`verify-citation-range`, extended cycle-012 with the inherited-citation sub-case, squarely applicable to this audit-style re-anchor of inherited slice citations), a rotation-citation check (`verify-rotation-citation`), and a variant-axis collapse analysis (`classify-variant-axis`) — but references none of them (grep for `skill|verify-citation|verify-rotation|classify-variant` returns no hits). The verification was done by "direct read"/`read_range` instead. Pure telemetry, non-blocking: the work is sound; the surfaced signal is that an applicable skill (notably `verify-citation-range`'s inherited-citation sub-case) was not invoked or cited. See Issue 2.

### Issues found

1. **Edit 7 is a non-edit mis-labeled as a proposed-changes block.** `reports/.../CYCLE.md` §"Proposed changes" Edit 7 (lines 84-86) — the block declares "This is a one-word framing touch only ... No edit needed to the condition text." and carries no `[old]`/`[new]` fence. Severity: **low**. It proposes no change, so it is integration-harmless, but it should either be dropped or moved out of the numbered Proposed-changes sequence (e.g., into Discipline notes) so the proposed-changes list is all-edits. Mildly weakens the report's own "12 proposed-changes blocks" framing (effective count is 11).

2. **No skill invocation referenced for the citation/variant verification.** `reports/.../CYCLE.md` §"Discipline notes" + §"Supporting evidence" — the slice-ref re-anchor sweep and the variant-axis collapse analysis are exactly the shapes `verify-citation-range` (inherited-citation sub-case), `verify-rotation-citation`, and `classify-variant-axis` cover, but none is cited. Severity: **low / telemetry**. The verification is independently confirmed sound, so this is not a correctness defect — only an uptake signal for the meta-phase's skill-usage tracking.

3. **Minor framing overstatement in OQ item 3 ("dep-map table").** `reports/.../CYCLE.md` §"Open questions / caveats" item 3 (lines 202) says the fgmres theme is absent from "neither the L4>L3 prose-list nor the dep-map table". The L4/index dep-map *table* (`index.md:50-55`) is operator-rows-only; L4>L3 themes are not listed in that table at all (they appear only in the prose-list at lines 41-44 and in operators' "Lowers to" cells). Edit 12 correctly targets only the prose-list, which is the right and sufficient home. Severity: **low / cosmetic** — the fix is correct; only the OQ prose implies a table-row gap that does not exist. No action needed beyond noting the report's stated gap is narrower than worded.

---

## Repair

### Fixes attempted

- **Finding 1 [plan-kind-consistency]**: Edit 7 is a non-edit (no `[old]`/`[new]` fence; body says "No edit needed") mis-labeled as a numbered proposed-changes block, inflating the "12 blocks" framing to an effective 11 and risking confusing a mechanical parser that expects every `### Edit N` to carry an edit fence.
  - **Decision**: repaired.
  - **Action**: Re-labeled the `### Edit 7` heading to `### Note (not an edit) — §"Applicability conditions": no change needed` in `reports/2026-05-29T051532Z-lifter-fgmres-theme-firm/CYCLE.md` §"Proposed changes". Added an explicit lead-in — "**This is a NON-edit note, not a proposed-changes block** — it carries no `[old]`/`[new]` fence and the integrator must not attempt to apply it" — and a parenthetical recording the corrected count ("**11 applicable edits**: Edits 1–6 and 8–12"). This removes the `Edit N` framing the integrator's parser keys on while preserving the note's content; the surrounding numbered edits (1–6, 8–12) are unchanged (no renumbering — Edit references elsewhere in the report stay valid). Mechanical re-label; no content authored.

- **Finding 2 [skill-uptake-survey]**: relevant skills (`verify-citation-range` inherited-citation sub-case, `verify-rotation-citation`, `classify-variant-axis`) applicable to the verification work but not cited. Critic marked pure telemetry / non-blocking.
  - **Decision**: not-needed. Per the critic, this is an uptake signal for meta-phase skill-usage tracking, not a correctness defect — the verification was independently confirmed sound. Not a repairer concern (no mechanical fix; adding skill-invocation telemetry would be authoring report content, out of scope).

- **Finding 3 [minor framing — OQ item 3]**: OQ item 3 overstates the gap as covering "the dep-map table"; the L4 dep-map table is operator-rows-only, so only the prose-list is the gap (which Edit 12 correctly targets). Critic: cosmetic, "fix the wording if trivial".
  - **Decision**: repaired.
  - **Action**: Tightened OQ item 3 in `CYCLE.md` §"Open questions / caveats" to read "the L4>L3 prose-list does not mention it" and added the clarifying parenthetical "(The L4 dep-map *table* is operator-rows-only — L4>L3 themes are not table rows there — so the prose-list is the correct and sufficient home; Edit 12 targets it.)". Trivial cosmetic wording fix; removes the implied non-existent table-row gap without changing the report's substance.

### Unrepairable findings

None. Both warnings were low-severity and either repaired (the two framing/labeling issues) or telemetry-only (skill-uptake, not-needed). The two cruxes (slice-ref re-anchor accuracy + L4/index-add correctness) were verified CLEAN by the critic, so no substantive authoring was implicated.

## Suggested resolution

`ready`. Notes for the integrator:

- The report now declares **11 applicable proposed-changes edits** (Edits 1–6, 8–12). The former "Edit 7" is now an explicit **non-edit note** — do not attempt to apply it (it carries no `[old]`/`[new]` fence).
- **Edit 12** (L4 index prose-list row, `book/src/L4/index.md`) is `layer-intro-author` territory per the report's own flag — apply as a consistency-repair with the report's sibling-parallel wording, or route the exact wording to a `layer-intro-author` follow-up, mirroring how cycle-020 handled the gmres dep-map firm-sync. **Do not silently drop it** (a firm theme absent from its layer's prose-list is a cross-reference-integrity gap).
- Edit 10 proposes closing OQ `fgmres-inner-loop-iterate-while-migration-lifter-candidate` as `resolved` (a 5-batch cycle-010→cycle-021 carry-forward); Edit 11 flips the theme `rough-in` → `firm`.
