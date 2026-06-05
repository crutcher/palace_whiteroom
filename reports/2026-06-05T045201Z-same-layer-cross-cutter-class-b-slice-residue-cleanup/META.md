---
verifies: ./CYCLE.md
critiqued_at: 2026-06-05T04:55:32Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-05T05:10:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "book-wide observation — class-B deleted-slice plaintext residue"

## Critique

### Checks run

**citation-validity** — `warning`. All eight edit OLD-strings were matched against disk and are exact (`L4/krylov-step.md:255-256`, `L4/chebyshev.md:579`, `L3/chebyshev.md:542`, `L2/chebyshev-iteration.md:269`, `L1/chebyshev-smoother.md:342`, `L2/index.md:133`, `L3/index.md:53` + `:99`, `L1/orthogonalize.md:300`). The three repoint targets exist on disk and the cited L0 ranges hold for two of three pointers: `ksp-solve-mutation-rotation.md` §"Sub-pattern C" cites `palace/linalg/iterative.cpp:543-705` verbatim (confirmed at `:374`, `:438`, `:689`, plus the audit-YAML at `:847-850`), and `L4-L3/gmres-inner-loop-iterate-while-migration.md` exists. The ONE imprecision: the report (NEW text line 99 + Supporting-evidence line 235) cites `palace/linalg/orthog.hpp:41-74` as the L0 ground for the arnoldiStep orthogonalization constituent, but `orthogonalize-mutation-rotation.md` carries no contiguous `41-74` citation — it cites `orthog.hpp:41-53` (MGS), `:57-74` (CGS, `refine=false`), and `:75-88` (refine block) separately. `41-74` is a reasonable *union* spanning the two `OrthogonalizeColumn*` paths, and the cited absorb-home (`orthogonalize-mutation-rotation.md`) genuinely documents `orthog.hpp:41-88`, so this is not a fabrication — but the range as written maps to no single in-file pinpoint and slightly under-shoots the documented region (drops the `refine`/`:75-88` sub-pattern). Flagging as `warning` so the repairer can decide whether to widen to `41-88` or split into `41-53` + `57-74` to match the absorb-home's own line-map. Everything else is in-range.

**surface-or-evidence** — `pass`. This is not a refinement-shaped operator/theme proposal; it is plaintext-residue cleanup on provenance/evidence sections of already-firm chapters. The two repoints carry their evidence (absorb-home + L0 ground) inline. No record is newly named in a signature, so the record-definition sub-check does not apply.

**rotation-quality** — `pass`. Not applicable to a residue-cleanup observation; no algebraic/structural rotation is asserted (the entry's kind is Redundancy, declared at line 38).

**variant-axis-coverage** — `pass`. No operator with orthogonal variant axes is being proposed. The residue partition into three disposition classes (repoint / strike / keep-historical) is itself exhaustively enumerated against the 16-hit grep, with the kept-as-historical class explicitly scoped out with rationale — the inverse of a hidden branch.

**cross-reference-integrity** — `pass`, and this check is load-bearing here. Every new markdown link in the two repoints resolves: `../L1-L0/ksp-solve-mutation-rotation.md`, `../L4-L3/gmres-inner-loop-iterate-while-migration.md`, and `../L1-L0/orthogonalize-mutation-rotation.md` all exist on disk. The build-safety claim is independently confirmed: `grep -roE '\]\((\.\./)*spec/slices/[^)]*\)'` returns ONLY `concepts/index.md:42-43` (the `[slice X]`/`[slice Y]` placeholders), and those sit inside the ```` ```markdown ```` fence (verified opening at the region's line 27, the placeholders at file lines 42-43, fence closing at 47) — so `linkcheck2` ignores them and no edit introduces or touches a live broken link. The strikes replace dead `spec/slices/*` paths with prose and introduce no new links. The out-of-scope `concepts/dependency-map.md` is correctly noted as wired into `SUMMARY.md:292` (confirmed) with an inbound citation, justifying deferral over a drive-by string-swap.

**edge-label-fidelity** — `pass`. The report itself proposes NO Mermaid edge edits — it surfaces the ~40 stale dep-map edges as a follow-up for `layer-intro-author`, not as in-scope changes. Its characterization of those edges (keyed on deleted krylov-trio slugs `gmres`/`orthog`/`arnoldi_step`/`cg`/`plane-rotation-stream`, not a `cg_preconditioning_framework` node) was verified directly against `dependency-map.md` (edges at `:133-146` etc.; 88 lines mention the trio terms — consistent with the "~40 edges" estimate).

**plan-kind-consistency** — `pass`. Declared as a same-layer-cross-cutter observation (kind: Redundancy). Content shape matches: a book-wide enumeration, a disposition tally, and a recommendation routing the substantive structural staleness to a separate role. The proposed-changes are mechanical plaintext repoint/strike, consistent with the cross-cutter "surface, don't author" posture; the report explicitly declines to half-edit the legacy concept-index files.

**skill-uptake-survey** — `pass`. The report references skill `deleted-slug-inbound-live-link-sweep` (line 239) and demonstrably followed its load-bearing SOURCE-PATH-exclusion discipline: the cited grep commands use `grep -v meta-reviews/` and `grep -v 'book/src/concepts/dependency-map.md:'` (file-prefix exclusions), explicitly NOT the c098-D1 link-target-text form. I confirmed the skill's §"Exclude by SOURCE-PATH, NEVER by link-target text" rule and that the report's discipline matches it exactly.

### Issues found

1. **Imprecise L0 range `orthog.hpp:41-74` for the arnoldiStep repoint** — `CYCLE.md` §"Proposed changes" `L4/krylov-step.md` NEW line 99 and §"Supporting evidence" line 235. The absorb-home `orthogonalize-mutation-rotation.md` carries no contiguous `41-74` citation; it documents `orthog.hpp:41-53` + `:57-74` + `:75-88` as distinct sub-patterns. `41-74` is a defensible union of the two non-refine paths but maps to no single in-file pinpoint and omits the `refine` block (`:75-88`) that the absorb-home includes. Severity: low (the link itself resolves and the region is genuinely the orthogonalization L0 home; this is a citation-precision nit, not a dangling/false claim). Candidate repair: widen to `orthog.hpp:41-88` or render as `41-53`/`57-74` to match the absorb-home's own line-map.

2. **Migrated-OQ premise correction is correct and well-evidenced (no defect; recorded for the integrator).** Finding (1)'s claim — that the OQ `dependency-map-cg-precond-stale-mermaid-edges`'s literal `cg_preconditioning_framework` Mermaid-node premise is inaccurate — is verified. `cg_preconditioning_framework` appears in `book/src` ONLY in `meta-reviews/` (correctly excluded) and as accurate prose provenance in three firm chapters (`concepts/rotation.md:136`, `L4/index.md:119`, `L4/preconditioning-framework.md:336`); there is no such Mermaid node anywhere. The actual stale edges are keyed on the krylov-trio slice-slugs. This is a true finding the cycle-planner should act on (re-scope the OQ), not a report defect.

## Repair

### Fixes attempted

- **Finding**: Imprecise L0 range `orthog.hpp:41-74` for the arnoldiStep orthogonalization-constituent repoint — maps to no single in-file pinpoint and drops the `refine` sub-pattern (`:75-88`) that the absorb-home documents.
  - **Decision**: repaired
  - **Action**: Re-read `palace/linalg/orthog.hpp:41-90` via codemap `read_range` and cross-checked the absorb-home `orthogonalize-mutation-rotation.md`'s own line-map. Confirmed line-map: MGS `OrthogonalizeColumnMGS` = `41-53`; CGS `OrthogonalizeColumnCGS` non-refine path = `57-74`; the `if (refine)` block = `75-88`. The arnoldiStep orthogonalization constituent is the *full* orthogonalize operation (incl. refine), and the absorb-home documents exactly the three-way split. Widened the citation to the full contiguous orthogonalization span `orthog.hpp:41-88` and annotated the three sub-pattern breakdown inline (`MGS 41-53 + CGS 57-74 + refine 75-88`), so it both (a) is a single defensible in-file span and (b) no longer drops the refine block. Applied to all three occurrences in `CYCLE.md`:
    - §"Absorb-home facts established" (line 67)
    - §"Proposed changes" `L4/krylov-step.md` NEW arnoldiStep line (line 99) — the load-bearing repoint that lands in the book
    - §"Supporting evidence" absorb-home-L0-ranges bullet (line 235) — also corrected the absorb-home doc-line span `74-112`→`74-151` to cover all three sub-pattern citations.

### Unrepairable findings

None. The single warning-severity finding was a citation-precision nit (mechanical range correction), squarely within repair authority — the link already resolved and the region was the genuine orthogonalization L0 home; only the range bounds needed tightening against the verified source + absorb-home line-map.

The critic's two non-defect observations are correctly left as-is in CYCLE.md (NOT repair targets):
- The migrated-OQ premise correction (`cg_preconditioning_framework` literal-Mermaid-node premise inaccurate; actual stale edges keyed on krylov-trio slugs) — an accurate finding for the cycle-planner to re-scope the OQ.
- The `concepts/` whole-file refresh recommendation (orchestrator/slice-era framing) — surfaced as a `layer-intro-author` follow-up, out of micro-sweep scope.

The 8-file cleanup itself is preserved unchanged (all OLD-strings matched, build green at baseline, all repoint targets exist on disk).

## Suggested resolution

`ready` for the integrator. Notes for the integrator:
- The arnoldiStep repoint now cites `orthog.hpp:41-88` (full orthogonalization span, three sub-patterns named inline) — consistent with the absorb-home `orthogonalize-mutation-rotation.md`.
- The two non-defect observations are integrator/planner routing items, not blockers: (1) re-scope OQ `dependency-map-cg-precond-stale-mermaid-edges` to "dependency-map.md legacy slice-slug Mermaid nodes"; (2) dispatch `layer-intro-author` next cycle on `concepts/index.md` + `concepts/dependency-map.md` (dep-map refresh, natural pairing with the graded-stack typed-edge campaign).
