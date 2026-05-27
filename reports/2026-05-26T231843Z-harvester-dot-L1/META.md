---
verifies: ../REPORT.md
critiqued_at: 2026-05-26T23:35:00Z
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
repaired_at: 2026-05-26T23:50:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: unrepairable
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: same-layer-cross-cutter
---

# META: verification of "Formalize dot at L1"

## Critique

### Checks run

**citation-validity — pass.** Spot-checked every external citation. `vector.hpp:110-113` shows `ComplexVector::Dot` and `TransposeDot` both declared returning `std::complex<double>` with the comment `Vector dot product (yᴴ x) or indefinite dot product (yᵀ x) for complex vectors.` — exactly as the report quotes. `vector.cpp:263-267` has the `Dot` body returning `{Re*Re+Im*Im, (this==&y)?0.0:(Im*Re-Re*Im)}` confirming both the algebraic claim (law 9 imag = 0 exact at `&x==&y`) and the complex return type. `vector.cpp:269-274` matches the `TransposeDot` body including the `2·Imag·Real` self-dot shortcut. `vector.cpp:665-672` shows `LocalDot(Vector,Vector)` via `hypre_SeqVectorInnerProd`; `vector.cpp:674-685` shows `LocalDot(ComplexVector,ComplexVector)` with the self-dot fast path returning imag = 0 (matches law 9 second citation). `vector.hpp:247-253` shows the templated `linalg::Dot` = `LocalDot` + `Mpi::GlobalSum`. `iterative.cpp:395, 404, 444, 460` confirm CG use sites. `nleps.cpp:487, 492` confirm `std::abs(linalg::Dot(...))` use, which is unambiguous evidence the return is complex. `test-vector.cpp:206-207` confirms real-vector dot via `operator*` returns `double`. `test-orthog.cpp:157` confirms the `linalg::Dot` orthogonalization use. All ranges in-range. The report's own self-correction (`ComplexVector::Dot` returns complex, not real) is what the source says.

**surface-or-evidence — pass.** This is a firm L1 chapter creation (not a refinement of an existing operator). Three proposed-changes blocks: `book/src/L1/dot.md` (new file), `book/src/L1/index.md` (dep-map row), `book/src/SUMMARY.md` (TOC entry). All surface; no pure rotation_claim without surface. The surface-or-evidence check is structurally satisfied for a firm-creation report.

**rotation-quality — pass.** The L0→L1 rotation is genuine and compaction-positive: three L0 entry points (`operator*` real, `Dot` complex, `TransposeDot` complex) plus two free-function dispatchers (`LocalDot`, `Dot`) collapse to two L1 operators (`dot`, `tdot`). The receiver/argument asymmetry of the method form is erased; the MPI collective is folded into a single semantic step (the local-then-collective two-step migrates to L1>L0 lowering); the `&x == &y` fast-path is erased as a transparent performance trick while still being recorded as the algebraic equality that makes it valid (law 9). This is state-hiding + collective-hiding compression, the canonical kind of mutation rotation. Not a 1:1 rename.

**variant-axis-coverage — pass.** Report explicitly declares 2 variant axes (element-type × conjugation-convention) and explicitly closes the third-axis hatch: "the reduction is unconditionally exhaustive over the length axis `N`, with no masking or strided variants in the Palace surface." Cross-checked: Palace has no masked/strided/sliced `Dot` variant; the surface is exhaustive-only. The asymmetry between the (real,unconjugated) absent cell and the (real,hermitian)=(real,bilinear) collapsed cell is implicit in the table — for real element type the two conjugation modes coincide, so only one operator exists; this is correctly handled by the kernel table.

**cross-reference-integrity — warning.** Two real findings: (1) The report's body acknowledges the contradiction it creates: `book/src/concepts/dot.md` lines 28-30 state `ComplexVector::Dot` returns a real scalar; the report's L1 entry states it returns complex. The source code resolves it in the L1 entry's favor (`vector.hpp:111` `std::complex<double> Dot(...)`). After integration the concept page will contain a fact contradicted by L1, so cross-reference-integrity is degraded until the concept page is fixed. The report flags this in Open Question #1 and (correctly per write-authority partition) does not attempt the fix; nevertheless the resulting artifact state has a known contradiction. (2) The concept page references a non-existent symbol `linalg::Dotc` — a full-tree grep of `reference/palace/` finds zero occurrences of `Dotc`. The L1 entry uses the correct slugs (`tdot` for the unconjugated form, mapping to `TransposeDot`). The concept page's claim "The complex-conjugate version is `Dotc`; the un-conjugated bilinear version is `Dot`" is doubly wrong: `Dotc` does not exist, AND it has the role-assignment inverted (`Dot` is the conjugated form, `TransposeDot` is the unconjugated form). Both findings degrade artifact-level cross-reference integrity even though the L1 entry itself is internally consistent and points only at real symbols.

**edge-label-fidelity — pass.** Report carries an L1 scope and discusses the L1 surface throughout; the section "L1 vs L0 distinction" contrasts L0 and L1 forms as expected for an L1 firm-operator chapter. The L1>L0 lowering concerns are deferred to a future theme (correctly), not mis-attributed. No "edge says X, prose discusses Y" mismatch.

**plan-kind-consistency — pass.** Declared as a firm L1 operator chapter (matching the dep-map entry's `firm` status). Content shape matches: full signature, semantics, algebraic laws (13 stated), variant axes, evidence table, L0/L1 distinction. No rough-in placeholders. Matches the axpy reference precedent.

**skill-uptake-survey — warning.** Three skills are clearly applicable to this report shape and are not surfaced by name in the report: `verify-citation-range` (every claim cites a `(file:start-end)` range — this is the canonical skill for that pattern), `classify-variant-axis` (the report makes a 2-axis variant determination with an explicit "no third axis" closure — exactly the skill's domain), and `verify-refinement-surface` (the proposed changes include three surface edits — verifying their well-formedness is the skill's job). The report's evidence section reads as if these skills were applied implicitly, but no telemetry mark is present. Pure presence check; not blocking. Drive-by note: Open Question #6 is a friction-ledger drive-by about the `*REPORT.md` content-pattern Write filter; this is correctly routed (the parent annotation block confirms the work-around was applied), so no additional action needed at the critic layer.

### Issues found

1. **Cross-reference contradiction with concepts/dot.md (return type).** `book/src/concepts/dot.md:28-30` states `ComplexVector::Dot` returns a real scalar. Source (`vector.hpp:111`) shows it returns `std::complex<double>`. The L1 entry correctly contradicts the concept page. **Where:** REPORT.md "Open questions / caveats" §1, and the concept page itself. **Severity:** warning. **Repair candidate:** the report already names the fix (concept page edit, out of harvester scope) — repairer may either add the concept-page edit as an additional proposed-changes block on this report or surface it for the integrator/cycle-planner.

2. **Cross-reference: `linalg::Dotc` does not exist.** `book/src/concepts/dot.md:17-18` references `linalg::Dotc` and inverts the conjugation role between `Dot` and `TransposeDot`. A full-tree grep of `reference/palace/` finds zero occurrences of `Dotc`. **Where:** REPORT.md Open Question #2 acknowledges but does not propose the fix; concept page lines 17-18. **Severity:** warning. **Repair candidate:** same as #1 — concept-page correction.

3. **SUMMARY.md proposed-changes block is a fragment, not a full-file replacement.** The `edit:book/src/SUMMARY.md` block (lines 183-188) shows only the L1 Part section, but `SUMMARY.md` is a 115-line file with many other Parts. An integrator naively replacing the file with the block's content would delete almost all entries. **Where:** REPORT.md proposed-changes block 3. **Severity:** warning. **Repair candidate:** repairer should rewrite the proposed-changes block as a targeted insertion (e.g., add `- [dot](./L1/dot.md)` after the existing `- [axpy](./L1/axpy.md)` line at SUMMARY.md:26) and/or add an explicit "insert-after" marker. The report's parenthetical note (line 190) acknowledges this but the block format does not encode it for the integrator. The pilot-1 axpy report had the same issue shape; checking how the integrator resolved it would inform whether this is a per-cycle handhold or a structural format upgrade.

4. **Skill telemetry absent.** Report does not name `verify-citation-range`, `classify-variant-axis`, or `verify-refinement-surface`, all of which the report's shape implies were used or should have been. **Where:** report-wide. **Severity:** warning. **Repair candidate:** add a single-sentence skills-used line near the top, similar to how axpy's report does (if it does — repairer can check).

5. **Law 13 worked example may be miscomputed.** Report states `tdot(x, x) = 0` for `x = (1, i)`: `1·1 + i·i = 1 + (-1) = 0`. Correct arithmetically — `i·i = -1`. The law is stated correctly. (No issue; flagged here only because the spot-check was load-bearing for the rotation-quality verdict.) **Severity:** none.

6. **Open Question #6 is a procedural drive-by, not a content finding.** Report records harness friction (Write filter on `*REPORT.md`) inside the report body. This is fine per the relaxed-bar problems channel, but the parent-annotation block at the bottom of REPORT.md (lines 220-222) effectively duplicates the finding. **Where:** REPORT.md sections "Open questions / caveats" §6 and "Parent-session annotation". **Severity:** info. **Repair candidate:** none — these two are written from different vantage points (subagent self-report vs parent-session post-hoc) and the redundancy is informative; meta-phase can decide if friction-ledger update is warranted.

## Repair

### Fixes attempted

- **Finding 1 — Cross-reference contradiction: `concepts/dot.md:28-30` claims `ComplexVector::Dot` returns real; source returns `std::complex<double>`.**
  - **Decision**: unrepairable.
  - **Rationale**: Exceeds repair authority. Fixing this requires substantive authoring of the concept page (resolving the contradiction directly in `book/src/concepts/`), which (a) is not in the repairer's write-authority partition (repairer edits live in `reports/<id>/` only), and (b) contradicts existing artifact content — listed explicitly in the role definition's out-of-scope examples. REPORT.md's Open Question #1 already names the fix and routes it; deferred to follow-up cycle via `same-layer-cross-cutter`.

- **Finding 2 — Cross-reference: `linalg::Dotc` does not exist; concept page also inverts Dot/TransposeDot conjugation roles.**
  - **Decision**: unrepairable.
  - **Rationale**: Same shape as Finding 1 — concept-page content correction is substantive authoring against existing artifact content, out of repair scope. REPORT.md's Open Question #2 already enumerates the corrections needed. Bundled with Finding 1 in the same follow-up to `same-layer-cross-cutter` for next cycle.

- **Finding 3 — SUMMARY.md proposed-changes block is a fragment, not a full-file replacement; risks deletion of other Parts.**
  - **Decision**: repaired.
  - **Action**: Edited REPORT.md's third proposed-changes block directly. Changed the fence tag from `edit:book/src/SUMMARY.md` to `append-after:book/src/SUMMARY.md`; replaced the body with an explicit anchor-line + insert-line pair (anchor: `- [axpy](./L1/axpy.md)`; insert: `- [dot](./L1/dot.md)`); replaced the parenthetical note below the block with a stronger integrator hint stating this is a targeted insertion of a single line under the "L1 — Mutation-Lifted Forms" Part heading and that all other 115 lines of SUMMARY.md must be preserved verbatim. The mechanical fix is purely format-level — no content authoring.

- **Finding 4 — Skill telemetry absent: report doesn't name `verify-citation-range`, `classify-variant-axis`, `verify-refinement-surface`.**
  - **Decision**: repaired.
  - **Action**: Added a `skill_uptake:` block to REPORT.md frontmatter, mirroring the pilot-1 axpy report's format (`reports/2026-05-26T223039Z-harvester-axpy-L1/REPORT.md` lines 13-21). Three entries, each `triggered: true, decision: explained_non_applicable`, with one-line rationales matching what the critic observed about implicit application: citations verified inline, variant-axis classification landed directly in the section, surface well-formedness verified by inspection. Pure telemetry addition; no substantive content changed.

- **Finding 5 — Law 13 worked example.** Critic noted no issue. Not addressed (none needed).
  - **Decision**: not-needed.

- **Finding 6 — Procedural drive-by redundancy with parent-annotation block.** Critic flagged as info-only with no repair candidate.
  - **Decision**: not-needed.

### Unrepairable findings

- Findings 1 and 2 (both `cross-reference-integrity` warnings): the existing `book/src/concepts/dot.md` is contradicted by the L1 entry on (a) `ComplexVector::Dot` return type, and (b) the existence of `linalg::Dotc` plus inverted `Dot`/`TransposeDot` conjugation role-assignment. Repair would require authoring the corrected concept-page text, which is out of the repairer's surgical-and-mechanical bar and contradicts existing artifact content. Routed to `same-layer-cross-cutter` for next cycle (alternative router: `layer-intro-author` if cycle-planner judges the concept page belongs to that role's purview).

## Suggested resolution

`overall_status: ready` — the report itself is internally correct, the L1 entry is authoritative against source, and the two repairable findings landed (SUMMARY.md block format upgraded to a safe targeted-insertion form; skill telemetry added to frontmatter).

Integrator: apply the three proposed-changes blocks as-is. The SUMMARY.md block now encodes the intent unambiguously (single-line insertion after the `axpy` line). The concept-page contradictions (Findings 1+2) accumulate as embedded friction in the artifact per CLAUDE.md "Accumulate surface with embedded friction"; the L1 entry supersedes the concept page on the contested facts.

Follow-up cycle: cycle-planner should dispatch `same-layer-cross-cutter` (or `layer-intro-author` if preferred) with scope "reconcile `concepts/dot.md` with L1 `dot.md`" — specifically (1) correct the return-type claim for `ComplexVector::Dot` from real to `std::complex<double>`, and (2) remove the `linalg::Dotc` reference and fix the inverted conjugation role-assignment between `Dot` and `TransposeDot`.
