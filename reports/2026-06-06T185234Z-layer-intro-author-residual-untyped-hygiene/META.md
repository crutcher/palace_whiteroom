---
verifies: ../REPORT.md
critiqued_at: 2026-06-06T19:09:49Z
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
repaired_at: 2026-06-06T19:40:00Z
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

# META: verification of "residual untyped typed-edge hygiene (L1/fe_collection + 3 BLAS-1 L1>L0 themes)"

## Critique

### Checks run

**citation-validity — pass.** Load-bearing here. Every `cites-evidence` L0 range was read on disk via codemap `read_range` and confirmed in-range with the claimed anchor and close brace:
- `multigrid.hpp:22-73` (the planner-flagged END) — read 22-74: `// Construct sequence...` at :22, `template`/`ConstructFECollections` at :23-25, `std::reverse` at :70, `return fecs;` at :72, close `}` at :73. The producer's claim is exact; **no off-by-one**. (Per cycle-105 sharpening I confirmed END via direct `read_range` of the source body, not a prose-vs-read_range mismatch.)
- `vector.hpp:246-253` (`Dot` template, comment+body), `vector.hpp:254-259` (`Norml2` template, `std::sqrt(std::abs(Dot(...)))` at :259) — confirmed.
- `vector.cpp:263-267` (`ComplexVector::Dot`, `this==&y` self-dot fast path, `}` at :267) — confirmed.
- `vector.cpp:203-227` (`ComplexVector::operator*=`, `si==0.0` branch :207-211, `forall_switch` :212+, `}` at :227) — confirmed.
- `communication.hpp:266-270` (`GlobalSum` → `GlobalOp(...,MPI_SUM,...)`) and `communication.hpp:246-249` (`GlobalOp` body = `MPI_Allreduce(MPI_IN_PLACE,...)`) — confirmed.
The frontmatter ranges also match the theme bodies' own prose-cited ranges (grepped each theme): dot cites `vector.hpp:246-253`, `vector.cpp:263-267/665-672/674-685`, `communication.hpp:266-270/246-249` — all present in §Evidence; nrm2 cites `vector.hpp:254-259/246-253` + the two collective ranges; scal cites `vector.cpp:203-227` + `vector.hpp:98-99`. Minor span variants between frontmatter and prose (nrm2 frontmatter `vector.hpp:246-253` vs prose §Sub-pattern A `247-252`; `communication.hpp:266-270` vs prose `267-270`) are comment-inclusive vs comment-exclusive bounds on the *same* `Dot`/`GlobalSum` templates — both verified accurate on disk, and the comment-inclusive form matches the dot theme's own canonical citation. The two book-node `depends-on`/`reference` targets (`L1-L0/fe-collection-construction-rotation`, `L1/fe_space`) exist on disk.

**surface-or-evidence — pass.** This is a frontmatter-only typed-edge hygiene dispatch, not a surface refinement and not a rotation_claim — it adds declared `rank:`/`edges:` to nodes whose rank was previously prose-inferred. It backfills *machine-readable* representation of already-cited evidence; the underlying claims and surface are unchanged. Record-definition sub-check: no signature in scope names an undefined record (FECollection is MFEM-owned-read-as-given per fe_collection; the BLAS-1 themes operate on flat vectors). The producer's note (caveat 3) confirms this.

**rotation-quality — pass (not applicable).** No algebraic/structural rotation is asserted by this dispatch; it is metadata hygiene over existing firm chapters. No-op.

**variant-axis-coverage — pass.** No variant axes are introduced or modified. The scal theme's real-path (upstream `mfem::Vector::operator*=(double)`) vs complex-path split is faithfully scoped: the complex Palace overload is cited; the real path is named-in-prose-not-cited because it is upstream MFEM (correctly explained in caveat 2 and the §Faithful-citation derivation), which is consistent with the project's "cite Palace, not vendored upstream" rule.

**cross-reference-integrity — pass.** All edge targets resolve on disk: `book/src/L1-L0/fe-collection-construction-rotation.md`, `book/src/L1/fe_space.md`, `book/src/L1/fe_collection.md`, and the three BLAS-1 theme files all exist. The lint confirms `unresolved_depends_on_targets = 0` both pre- and post-edit. (Observation, not a defect of this dispatch: fe_collection's prose at :43 and :180 still says "Forward-reference `fe-collection-construction-rotation` until that theme is on disk" — but the theme IS on disk. Stale prose predating this dispatch; out of scope for a frontmatter-only edit.)

**edge-label-fidelity — pass.** The fe_collection edges are faithful to its prose: `lowers-to → L1-L0/fe-collection-construction-rotation` is backed by §"Downward (to L0)" (:173-180) and :42; `reference → L1/fe_space` is backed by §Dependencies (:164-171), which states verbatim "That is a consumed-by relation (producer→consumer ...), not a dependency" — exactly matching the `reference` (navigational, non-blocking) classification rather than `depends-on`; `cites-evidence → multigrid.hpp:22-73` is backed by §Evidence (:216) and §Downward (:177). The three themes' `cites-evidence` edges point only at L0 (rank-terminal ground truth), matching each theme's own evidence set, and deliberately omit the op→theme back-edge (correctly scoped out — that edge lives on the op side per c114).

**plan-kind-consistency — pass.** Declared kind is frontmatter-only hygiene (`rank: firm` + typed edges on already-firm nodes). Content matches: no new authoring, no placeholders, all four nodes carry firm status confirmed by both frontmatter/prose and the linter's `rank=3.0`.

**skill-uptake-survey — pass.** The report references `citecheck --anchor` for in-range verification and direct on-disk Read for close-brace ENDs (the documented brace-boundary procedure), and ran the graded-stack linter for the metric delta. Appropriate tool uptake for this shape.

**Graded-stack additions.** rank-invariant — **pass**: each new edge is firm→firm (the `lowers-to` to the construction-rotation theme, itself typed `rank: firm` this cycle) or firm→rank-terminal-L0 (`cites-evidence`). I applied all four edits and ran `graded_stack_lint.py --json`: `rank_violations = 0` HELD. reachability — **pass**: all four source nodes are reachable both pre- and post-edit; no node was orphaned.

### Issues found

1. **Inaccurate measurement claim: the move is NOT metric-neutral on reachability** — `reports/.../CYCLE.md` §"Standalone linter delta" (:250-256) and §Summary (:27-36, :251). The report repeatedly states `reachable=132` HELD and "no new inbound `depends-on` to a root." I applied the four proposed-changes blocks and measured: `reachable 132 → 133`, `detritus 127 → 126`. The newly-reachable node is `L1-L0/fe-collection-construction-rotation`, which IS detritus (unreachable) at baseline and becomes live once fe_collection (already reachable) gains its `depends-on` `lowers-to` edge to it. The producer's reasoning error: reachability is a forward mark-sweep FROM the roots, so it is the *outbound* `depends-on` from a reachable node (not an inbound edge to a root) that rescues the target. All other predicted metrics HELD exactly (`files=355, typed=295, untyped=60, roots=36, rank_violations=0, unresolved=0`), and the four nodes are confirmed NOT in the untyped-60 list (the producer's central finding is correct). Severity: low — the change is *beneficial* (it pulls a previously-orphaned firm theme into the live set; a strengthening, not a regression), but the report's stated finding ("metric-NEUTRAL", "reachable HELD") is factually wrong and should be corrected so the integrator's confirm-step is not misled into treating a 133/126 measurement as a discrepancy to investigate.

2. **OQ reasoning is sound — surfacing endorsed** — `reports/.../CYCLE.md` §Open questions (:273-285). The producer's `oq:graded-stack-prose-status-inference-masks-untyped` is correct: the four targets register `untyped=False, rank=3.0` purely because the linter's `derive_rank` falls back to the prose `## Status` `firm` token when frontmatter lacks `rank:`/`edges:` — I confirmed all four are absent from the untyped-60 list while `grep -L "^edges:"` correctly flags them as edge-less. A firm-status, zero-declared-edge chapter is genuinely invisible to the `untyped` warning. The proposed `ranked-but-edgeless` linter signal is a reasonable maintenance ask for the meta-phase. Not a defect; informational, recorded so the repairer/integrator preserve the OQ.

### Disposition note

The change itself is clean — every citation verifies, every edge is faithful and resolves, rank-invariant and reachability both hold (the latter improves). The single substantive issue is the report's own measurement *narrative* (issue 1), which understates the benefit by claiming neutrality where the linter shows a +1 reachability / −1 detritus improvement. That is a finding-accuracy correction, not a content problem.

## Repair

### Fixes attempted

- **Finding (Issue 1)**: the report's metric narrative claims the move is metric-NEUTRAL / `reachable HELD 132`, but applying the proposed changes gives `reachable 132→133` (+1), `detritus 127→126` (−1) — `fe_collection`'s new outbound `lowers-to → L1-L0/fe-collection-construction-rotation` `depends-on` edge rescues that baseline-detritus theme into the live set. The producer reasoned about inbound-to-root edges instead of the forward-from-root mark-sweep.
  - **Decision**: repaired.
  - **Action**: surgical metric-narrative correction in three locations of `CYCLE.md`, with NO change to the proposed `edges:` blocks (which the critic confirmed correct):
    - §Summary "Key measurement finding" — replaced the "metric-NEUTRAL" / "does not move ... reachable" claim with the accurate `reachable 132→133` (+1), `detritus 127→126` (−1) beneficial delta + the forward-mark-sweep explanation of why the fe-collection-construction-rotation theme is rescued; kept the correct point that `untyped` does NOT drop.
    - §Standalone linter delta — added `detritus=127` to the baseline line; rewrote the "Expected post-edit / all metrics HELD / reachable HELD" block to the corrected `reachable=133, detritus=126` post-state with the rescue explanation.
    - §Standalone linter delta "Net value" paragraph — corrected the "not a count move" framing to acknowledge the count move on the reachability/detritus axis.
  - **Rationale for repairability**: this is a mechanical finding-accuracy correction of a self-narrated metric prediction; the deliverable (the typed `edges:` blocks) is unchanged and confirmed sound. The actual delta is beneficial. No substantive authoring involved.

- **Finding (Issue 2)**: producer OQ `graded-stack-prose-status-inference-masks-untyped` (firm-`## Status` edgeless chapters report as typed/rank-3, invisible to the untyped warning) confirmed sound by the critic.
  - **Decision**: not-needed.
  - **Rationale**: the critic endorsed the OQ as informational, not a defect. It remains in `CYCLE.md` §Open questions for `integrator-per-report`/`integrator-finalize` to carry forward to the OQ ledger / meta-phase. No repair action.

### Unrepairable findings

None.

## Suggested resolution

`ready`. Notes for the integrator: the `edges:` proposed-changes blocks are sound and apply as-is. On the post-apply linter confirm step, expect `reachable 132→133` (+1) and `detritus 127→126` (−1) — this is the EXPECTED, beneficial delta (fe_collection's `lowers-to` edge rescuing `L1-L0/fe-collection-construction-rotation` from baseline detritus), now matching the corrected report narrative; do NOT treat 133/126 as a discrepancy. `rank_violations=0`, `unresolved=0`, `untyped=60` all HELD. Carry forward the producer's OQ `graded-stack-prose-status-inference-masks-untyped` (proposed `ranked-but-edgeless` linter signal) to the meta-phase.
