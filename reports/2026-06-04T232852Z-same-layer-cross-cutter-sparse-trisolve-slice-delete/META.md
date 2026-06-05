---
verifies: ../REPORT.md
critiqued_at: 2026-06-04T23:46:14Z
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
repaired_at: 2026-06-04T235640Z
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

# META: verification of L1-L0 observation — sparse-trisolve slice absorb-and-delete

## Critique

### Checks run

**citation-validity — pass.** This is a negative-result absorption, so the L0 citations are the load-bearing axis; I re-read a sample directly against `reference/palace` via codemap `read_range` / `search_text`. Every sampled cite verifies EXACTLY in range and in content:
- `superlu.hpp:43-58` — the four forwarding bodies (`Mult` / `ArrayMult` / `MultTranspose` / `ArrayMultTranspose`), each a literal `solver.X(...)` forward. Confirmed verbatim.
- `superlu.cpp:78` — `solver.SetIterativeRefine(mfem::superlu::NOREFINE);` confirmed, sitting in the constructor immediately before `SetSymmetricPattern(true)` (matches the report's context claim). `superlu.cpp:88` — `solver.SetFact(mfem::superlu::SamePattern_SameRowPerm);` confirmed inside `SetOperator`, in the `if (A && reorder_reuse)` branch (matches).
- `solver.hpp:43-63` — `SetOperator` pure-virtual (`:43`), `MultTranspose` override with `MFEM_ABORT` (`:45-49`), `Mult2` (`:52-56`) and `MultTranspose2` (`:59-63`) both `virtual` with base-class `MFEM_ABORT` and a preallocated scratch `r`, comments documenting purpose. Confirmed.
- `communication.hpp:337-344` — the `Mpi::Allgatherv` variable-count wrapper template wrapping `MPI_Allgatherv`. Confirmed.
- `geodata.cpp:1538-1539` — the sole `Mpi::Allgatherv` call site gathering `all_edge_attrs` (edge-attribute counts), NOT a factor. Confirmed.
- `ksp.cpp:104` (`MakeWrapperSolver` decl), `:155` (SuperLU), `:165` (Strumpack), `:187` (MUMPS) installs to `pc` — confirmed exactly via `search_text` line map.
Additionally, the proposed Change-2 `verified_against` YAML `note:` (the `absorbed-and-deleted` entry, which opens with a double-quoted scalar containing backticks and parens) round-trips under `yaml.safe_load` — no leading-bare-quote ParserError. No drift found anywhere; the absorption rests on a sound L0 record.

**surface-or-evidence — pass.** The proposal modifies the firm theme's surface (new §(d) subsection + 7 Verified-against bullets) and the evidence is retroactive negative-anchor backfill into an existing firm obstruction theme — the explicitly-allowed "pure retroactive evidence backfill" shape, not a bare rotation_claim. The record-definition sub-check is not triggered: no record/struct is named in a new signature here (the only `{...}` types referenced — `Solver<OperType>`, `Vector` — are pre-existing and merely cited, not freshly introduced). The "what is NOT unique" section correctly scopes out the four already-held anchors so no duplicate claim is made.

**rotation-quality — pass (not applicable to this report-kind).** No algebraic/structural rotation is asserted — this is an obstruction/negative-result absorption (the finding is the *absence* of a Palace-level triangular-solve form). There is no L_{n+1}-more-compact-than-L_n claim to grade.

**variant-axis-coverage — pass.** The original scope question's variant axes (forward vs. transpose apply, in-place vs. out-of-place / scratch-`r` workspace, factor-Allgatherv, residual check) are each explicitly resolved on the negative side in §(d1)-(d3): forward/transpose are the literal forwards (d1); the `*2` scratch-`r` axis is dispositioned as multigrid-smoother workspace not triangular-solve workspace (d2); Allgatherv and residual are closed at the Palace boundary (d3). The closing paragraph enumerates all four and states each resolves to an MFEM/third-party-internal or deliberately-disabled path. No hidden branch.

**cross-reference-integrity — warning.** Load-bearing for a deletion dispatch. I enumerated every reference to `sparse_triangular_solve.md` in `book/src/` and classified link-vs-token. The seven markdown LINKS are: `SUMMARY.md:300`, `spec/index.md:21`, `triangular-solve-obstruction.md:277` (+ the `:464` YAML citation), `scope-out-obstruction.md:68`, `sequential-obstruction.md:53`, `negative-result-slice.md:47`. Of these, Changes 2/3 repoint five (theme §Related 273-308 replacement covers `:277`; theme YAML `:464-467` replacement; concept `:68`/`:53`/`:47`) — each repoint target verified to land on the cited line. All remaining hits (`back_solve.md:46/:256`, `incremental-least-squares-...:148/326/447`, `meta-reviews/*`, the theme's `:208`/`:471`/`:475` and concept `:79` token mentions, and the slice file itself) are confirmed plain-text prose tokens that do not break on deletion. The **warning** is the cross-dispatch coupling the report itself surfaces in Change-4's NOTE: `SUMMARY.md:300` and `spec/index.md:21` are live markdown links to the slice that are OWNED BY D5 (out of this dispatch's scope) — so this report's slice-deletion is NOT independently `linkcheck2`-safe; it produces two dangling-link errors unless D5 removes those two rows in the SAME cycle. This is correctly flagged, but it is a real build-readiness gate (a deletion whose link-safety depends on a sibling dispatch), so I surface it as a warning for the integrator's sequencing rather than a clean pass. The D3/D4 collision boundary on `sequential-obstruction.md` is clean: D3 edits only `:53` (verified — the §"Sub-kind" slice link) and D4 owns `:83-85` (verified — the Givens-stream worked example, 30 lines away); the report's net-+1 line-shift caveat and bottom-up-apply recommendation are correct.

**edge-label-fidelity — pass.** The edge throughout is L1>L0 (the firm home is `book/src/L1-L0/triangular-solve-obstruction.md`); the absorbed findings are L0 wrapper-surface facts feeding the L0→L1 scope-out obstruction, and the prose discusses exactly that edge. The concept cross-refs correctly distinguish this L0→L1 scope-out obstruction from `sequential-obstruction`'s L2→L3 case (no edge mislabel).

**plan-kind-consistency — pass.** Declared as a same-layer-cross-cutter Redundancy observation (with residue), resolved as a graded-stack P2 slice absorb-and-delete. The content shape matches: an overlap analysis, a 3-finding residue absorption, link repoints, carve-out retirement, and deletion — no firm-operator-with-rough-in-placeholder mismatch. The `roadmap_goal`-vs-detritus reasoning (the slice is GC detritus, not orphaned intent, so no stub/roadmap_goal replacement is left) is consistent with the graded-stack §Axis-2 framing.

**skill-uptake-survey — pass (telemetry).** The `phase-1-slice-reduction-audit` skill is the relevant procedure (its concept-page-grep-before-reduction step is exactly what a slice-deletion needs). The report performs the substance of that procedure — the inbound `grep -rn` and the canonical-instance concept-page check before recommending deletion — but does not name the skill by its invocation. Pure telemetry, non-blocking; the audit substance is present.

### Issues found

1. **Cross-dispatch link-safety coupling (build-readiness)** — `book/src/spec/slices/sparse_triangular_solve.md` Change 4 (deletion) is not independently `linkcheck2`-safe: two live markdown links to the slice remain at `book/src/SUMMARY.md:300` and `book/src/spec/index.md:21`, both declared D5-owned and out of this dispatch's write-scope. Severity: medium / integration-sequencing. The report flags this explicitly in Change-4's NOTE, so it is a known coupling, not an oversight — but the integrator MUST confirm D5 lands in the same cycle (or the slice deletion must defer) or the book build breaks on two dangling links. (CYCLE.md §Proposed-changes Change 4 + §Summary.)

2. **D3/D4 same-file edit ordering on `concepts/sequential-obstruction.md`** — D3 edits `:53`, D4 edits `:83-85`; D3's repoint is net +1 line, shifting D4's target down by one if D3 applies first. Severity: low / mechanical. The report already prescribes the fix (apply bottom-up / re-anchor). Surfaced for the per-report integrator's serial sequencing. (CYCLE.md §Open-questions "Collision boundary with D4".)

3. **Verified-against YAML line-anchor drift (minor)** — the theme's `verified_against` entries for the two concept pages (`:468-475`, citing `scope-out-obstruction.md:68` and `sequential-obstruction.md:53`) stay valid in meaning after the Change-3 repoints, but the repoints (each turning one link line into two prose lines) may nudge those `:68`/`:53` line ints by ±1. Severity: low / mechanical re-anchor. The report flags this for the integrator. (CYCLE.md §Open-questions "YAML re-anchoring".)

4. **skill-uptake telemetry** — the report executes the `phase-1-slice-reduction-audit` procedure (concept-page-grep + inbound-link classification) without naming the skill. Non-blocking surface note only. (CYCLE.md §Supporting-evidence "Inbound-link grep".)

---
repaired_at: 2026-06-04T235640Z
repairer_version: 1

## Repair

### Fixes attempted

- **Finding 1 — Cross-dispatch link-safety coupling (D5 owns `SUMMARY.md:300` + `spec/index.md:21`).**
  - **Decision**: not-needed (confirmed; no edit).
  - **Rationale**: This is a correct *cross-dispatch sequencing* note, not a repairable defect in this report. The two remaining live links to the slice are out of this dispatch's write-scope (D5-owned) and D5 is dispatched in this same cycle (cycle-097). The slice deletion is link-safe iff D5 co-lands its two-row removal in the same integration batch — a build-readiness gate the integrator enforces by serializing/co-landing D5, NOT something the repairer can or should fix by editing CYCLE.md. The report already flags this explicitly in Change-4's NOTE. Confirmed accurate against disk: `SUMMARY.md:300` and `spec/index.md:21` are indeed live markdown links D5 must remove. Surfaced to the integrator in §Suggested resolution.

- **Finding 2 — D3/D4 same-file edit ordering on `concepts/sequential-obstruction.md`.**
  - **Decision**: repaired.
  - **Action**: CYCLE.md §Proposed-changes Change 3b. The proposed change used a fragile bare `replace_lines: 53-53` line-number anchor for the slice-link repoint. D4 edits the same file at `:83-85` (the Givens-stream worked example, 30 lines below); whichever applies first shifts the other's line targets. I hardened Change 3b's edit block from the bare line-number form into a **context-anchored** `old:`/`new:` block that carries the unique line-52 sentence opener (`A structurally distinct sub-kind of obstruction surfaced in the`) as match context. The integrator's by-context apply now locates the slice link by surrounding prose, so D3's repoint applies correctly regardless of whether D4's same-file edit lands first or second — the D3↔D4 ordering coupling is dissolved on the D3 side. Verified against disk that lines 52-53 read exactly the matched text. Also updated the §Open-questions "Collision boundary with D4" caveat to record that the bottom-up-apply recommendation is now belt-and-suspenders for D3 (no longer a correctness requirement), so the report stays internally consistent.
  - **Note**: D4's own `:83-85` edit is not in this report's scope; the repair only makes D3's side order-independent. The integrator's serial per-report apply + the surviving bottom-up recommendation still cover D4's side.

- **Finding 3 — Verified-against YAML line-anchor drift (minor).**
  - **Decision**: not-needed (re-verified; no drift in any proposed-change `[old]`/citation anchor).
  - **Rationale**: I re-verified all four concept-page targets against disk: `scope-out-obstruction.md:68`, `sequential-obstruction.md:53`, `negative-result-slice.md:47` each land EXACTLY on the cited line as the proposed changes assume, and the absorbed L0 citations are unchanged (the critic already re-verified those). The only "drift" the critic flagged is the *prospective* ±1-2 nudge to the theme's `verified_against` YAML `:68`/`:53` *referent* line-ints **after** the Change-3 repoints land — i.e. a re-anchor the integrator performs post-apply, not a drifted anchor sitting in an `[old]` block that the repairer can pre-correct. There is no specific drifted line-anchor in any proposed-change to mechanically fix; the report already directs the integrator to re-anchor those two YAML ints post-apply (CYCLE.md §Open-questions "YAML re-anchoring"). Nothing repairable here.

- **Finding 4 — skill-uptake telemetry.**
  - **Decision**: not-needed (informational).
  - **Rationale**: Pure telemetry; the audit substance (concept-page-grep before reduction + inbound-link classification) is present even though the `phase-1-slice-reduction-audit` skill is not named by its invocation. No edit warranted.

### Unrepairable findings

None. The one warning (cross-reference-integrity) decomposes into: a cross-dispatch sequencing gate (Finding 1, integrator-enforced, not a report defect) and a same-file ordering coupling (Finding 2, repaired by context-anchoring D3's edit). No finding required substantive authoring or contradicted artifact content; the load-bearing citation-validity check passed unaltered.

## Suggested resolution

`ready`. Notes for the integrator:

1. **D5 co-land gate (load-bearing).** This report's slice deletion (Change 4) is NOT independently `linkcheck2`-safe — `book/src/SUMMARY.md:300` and `book/src/spec/index.md:21` are live markdown links to `spec/slices/sparse_triangular_solve.md` owned by D5. Apply this report's deletion ONLY in a batch where D5's removal of those two rows co-lands; otherwise the `cargo make book` linkcheck2 step breaks on two dangling links. If D5 does not land this cycle, defer Change 4 (the absorption Changes 1-3 are independently safe and may land regardless).
2. **D3/D4 same-file (`sequential-obstruction.md`).** Change 3b is now context-anchored and order-independent on the D3 side. Still apply the file's edits bottom-up (or re-anchor) to protect D4's `:83-85` target, per the report's standing recommendation.
3. **Post-apply YAML re-anchor.** After Change 3 repoints land, re-verify the theme's `verified_against` YAML referent line-ints for `scope-out-obstruction.md:68` and `sequential-obstruction.md:53` (each may nudge ±1-2 as one link line becomes two prose lines); the citations stay valid, only the int may drift.
4. **OQ closure (report-flagged).** The report recommends closing the two slice-carried OQs (rename-to-`sparse_direct_solver_wrapper`; MFEM/SuperLU factor-Allgatherv family) as resolved-by-obstruction rather than migrating them. OQ-ledger authority is the per-report integrator / meta-phase.
