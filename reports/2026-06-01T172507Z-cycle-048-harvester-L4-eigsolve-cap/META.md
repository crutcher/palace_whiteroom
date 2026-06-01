---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T17:48:45Z
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
repaired_at: 2026-06-01T18:05:00Z
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

# META: verification of "Formalize eigsolve at L4 (outer-driver cap over a partial-obstruction L3)"

## Critique

### Checks run

**citation-validity — warning.** The load-bearing L0 anchors all resolve in-range and on-token via palace-codemap `read_range`: `slepc.cpp:694` is `EPSSolve(eps)` inside `SlepcEPSSolverBase::Solve` (`:687-709` confirmed); `slepc.cpp:715` is `return l * gamma` inside `GetEigenvalue` (`:711-716` confirmed); `arpack.cpp:318` is the `naupd(...)` call inside the `while(true)` RCI loop (`:315-339` confirmed, with the `ido == 1 || ido == -1` → `ApplyOp` dispatch and `ido == 99` break exactly as the report describes); `slepc.cpp:1847-1876` is `__pc_apply_EPS` with the inner solve `ctx->opInv->Mult(ctx->x1, ctx->y1)` at `:1858`, the un-scale branches at `:1861`/`:1865`, and the projector tail at `:1870` — fully supporting the body-lift `apply_linop ▷ ksp_solve ▷ scale_untransform [▷ project]` claim. The L1 pinpoints all check in-range and on-token (`L1/eigsolve.md:51` = the `EigStatus` sum; `:54` = the `LinearSolveFailed` L1-constructive note; `:78` = the partial-success "distinguishing semantic feature relative to `ksp_solve`" paragraph, which does literally contain `PartialConverged`). `tools/citecheck/citecheck.py --scan` reports 10 ok / 0 failing on the `path:lo-hi` form anchors. The **one issue** (warning, not fail): the report repeatedly attaches the load-bearing "`PartialConverged k` / `0 < k < requested`, no `ksp_solve` analog" claim to the anchor `[L3/eigsolve]:166` (CYCLE.md §Summary, §Algebraic-laws law 3, §Variant-axes axis 1, and both `L4/index.md` table/prose appends), but disk `L3/eigsolve.md:166` is the `solve-monad` **dependency bullet** whose text reads only "the (future, unauthored) L4 outer-coordination surface … with sum-typed termination richer than `ksp_solve`'s soft-fail" — it does **not** name `PartialConverged`, the `0 < k < requested` band, or a first-class partial-success arm. The substantive anchor for that exact claim is `L1/eigsolve.md:78` (correctly co-cited everywhere). So `:166` is an imprecise/weak pinpoint: it supports the general "richer-than-soft-fail" theme but not the specific partial-success-arm proposition the report hangs on it. Mitigating: this `:166` usage is inherited verbatim from the pre-existing cycle-047 `L4/index.md` `Outcome`-row anchors (`L4/index.md:56`, `:68`), so the report is propagating an established (if loose) anchor rather than inventing one; and the L3:166 bullet will itself be rewritten by this dispatch's edit-6 (CYCLE.md:265), which keeps the same loose phrasing. Recommend re-pinning the partial-success claim to `L1/eigsolve.md:78` as the load-bearing anchor and demoting `:166` to a supporting/theme reference (or, post-rewrite, pointing at the rewritten bullet's actual content).

**surface-or-evidence — pass.** This is a NEW firm L4 operator (`book/src/L4/eigsolve.md`, verified absent on disk — a genuine create), not a refinement of existing surface, so the refinement-surface gate is satisfied by the full operator apparatus (Signature, Semantics, Algebraic-laws, Variant-axes, Status, Evidence) carried inside the `new:` fence. Rotation evidence is present and forward-narrated (the §"Lowers to" in-line marker-erasure to `L3/eigsolve`). Not a pure rotation-claim backfill.

**rotation-quality — pass.** The cap is a genuine altitude rotation, not a rename. The L4 form makes structural what L3 leaves positional: the `Solve = StateT EigState Identity` monad threads `EigState`, `OpParams` is `readonly`, and termination is a single typed `EigOutcome` decision site (a 4-arm sum extending the canonical `Outcome`). Critically, the report does NOT fake a fold the source doesn't have: it honestly frames the cap as a **role-naming `EigOutcome`-wrapper over an opaque-library obstruction marker** (`eigen_iterate` named by role, the `sequential-obstruction` marked, no Palace loop rendered because Palace authors none), the L4 echo of the L3 `partial-obstruction`. The `EigOutcome` extension is a real compaction (the `PartialConverged Int` arm carries payload the `Bool` sum cannot express), and the "more abstract" criterion is met by the monad/sum-type wrapper. The in-line marker-erasure rotation (no dedicated `L4-L3/` theme) is correctly justified by parallel to `chebyshev`'s in-line-by-design L4>L3 and the no-removable-recurrence/no-Palace-loop-to-render fact.

**variant-axis-coverage — pass.** Five axes are enumerated and each given a disposition: `eig-outcome-classification` (the one coordination-shaping axis — the 4-arm sum), and `problem-type` / `spectral-transformation` / `backend-orchestration` / `element-type` all explicitly absorbed into `OpParams` (per `variant-absorption`, `readonly` typing) with stated rationale. No hidden branches — the report explicitly states the driver does not branch on any `OpParams` field. The five-axis profile matches the firm L3 parent's five-axis profile (modulo the cap-specific outcome-classification axis replacing L3's `scaling` informational axis — a defensible re-framing at the coordination layer).

**cross-reference-integrity — pass.** Build-readiness fence guard: fence parity is even (22 backtick-fences = 11 balanced blocks); the `new:book/src/L4/eigsolve.md` block (lines 42-250) ENCLOSES the full firm body — `## Status` (CYCLE.md:218), `## Signature` (:79), `## Algebraic laws` (:145), `## Evidence` (:231) are all INSIDE the fence; inner code uses 4-space indentation with no nested triple-backtick fences (the firm-body-outside-fence / nested-fence-truncation defect is absent). The **7-site re-anchor was independently verified load-bearing and COMPLETE**: `grep -n -i "not yet authored|future|no firm L4|unauthored"` on `book/src/L3/eigsolve.md` returns exactly the 7 sites the report claims (`:19, :34, :78, :166, :172, :203, :214`) plus `:236` — and the report correctly scopes `:236` OUT as a soft cross-cutting-concept gloss ("the future L4 outer-coordination surface") rather than a load-bearing "no L4 cap" assertion, flagging it as optional follow-up. The 7 `edit:` blocks map cleanly to the 7 disk paragraphs by content, and each rewrite (a) eliminates the "not yet authored"/"future dispatch" phrasing (grep confirms no stale residue inside the rewrite blocks) and (b) correctly points to the now-firm `L4/eigsolve` cap with the in-line marker-erasure framing. The same-cycle sibling live-link `./ksp_solve.md` (D1's `L4/ksp_solve.md`, not yet on disk) is handled per the same-cycle-co-land forward-ref convention (report states "cross-ref live at finalize"; integrator's serial per-report re-read resolves it). The two `L4/index.md` edits append DISTINCT additive rows (`L4/eigsolve` prose bullet + table row, and the separate `EigOutcome` table row) after D1's `ksp_solve` row — confirmed distinct from D1's appends; the consolidated count-token (`(4 + 3 outer-driver)`, `L4/index.md:32`) and §Queued prose flip (`:53-56`) are correctly DEFERRED to D4 (the report does not touch them, consistent with `L4/index.md:56`'s own note that the "no L4 cap" assertions remain TRUE until the cap chapter lands). All 8 referenced concept pages exist on disk; `iterate-while.md` exists.

**edge-label-fidelity — pass.** The L4>L3 edge is discussed consistently as L4→L3 (the cap lowers to `L3/eigsolve` via in-line marker-erasure) throughout §"Lowers to", §"L4 vs L3 distinction", and the `L4/index.md` dep-map "Lowers to" cell. The 7 L3 re-anchors point Upward to L4 correctly. `L3/eigsolve` frontmatter `firmness: partial-obstruction` (disk:4) is NOT touched by any edit block, and the intro rewrite explicitly states "This entry's status is unchanged by the cap landing" — so the status is correctly NOT flipped. No L_{n}→L_{n-1} label/prose mismatch found.

**plan-kind-consistency — pass.** The declared kind (firm L4 operator cap) matches the content shape: full operator apparatus, no rough-in placeholders, an honest `firm` Status that scopes its own firmness ("firm as a cap; the obstruction it carries is the same one L3 carries"). The `firm` claim is for the coordination apparatus + body-lift + obstruction-marker — consistent with the L3 `partial-obstruction` parent and the firm-on-positive-structure escape (the body laws are syntactic identities on positive source). The `EigOutcome` row is correctly declared `firm` as a clean-addition extension, not a contradiction of the canonical `Outcome`.

**skill-uptake-survey — pass (telemetry).** The report's shape implies the `verify-citation-range` (codemap `read_range` self-verification — invoked, per §Evidence "Citations self-verified against source this dispatch") and `summary-md-surgical-insert` (the SUMMARY.md append shape — referenced in §Registration) skills; both are surfaced. The build-readiness fence guard (`proposed-changes-fence-encloses-full-body-guard`) is the critic-side check and is satisfied. No skill-uptake gap blocks the report.

### Issues found

1. **Weak/imprecise pinpoint anchor `[L3/eigsolve]:166` for the partial-success claim** — `reports/.../CYCLE.md` §Summary, §Algebraic-laws law 3, §Variant-axes axis 1, and both `L4/index.md` appends (CYCLE.md:113, :153, :210, :282, :286, :287). Severity: low-medium (warning). `L3/eigsolve.md:166` is the `solve-monad` dependency bullet ("sum-typed termination richer than `ksp_solve`'s soft-fail") — it does not name `PartialConverged` / `0 < k < requested` / a first-class partial-success arm, which is the exact proposition the report attaches to it. The load-bearing anchor (`L1/eigsolve.md:78`) is correctly co-cited. The `:166` usage is inherited from the pre-existing cycle-047 `L4/index.md:56`/`:68` anchors (propagated, not invented). Repair candidate: re-pin the partial-success-arm claim to `L1/eigsolve.md:78` as primary and demote `:166` to a supporting theme reference; or, since edit-6 (CYCLE.md:265) rewrites the `:166` bullet anyway, ensure the post-rewrite bullet's content actually carries the partial-success phrasing the citation implies.

2. **(Sub-threshold, non-blocking) Self-cross-reference to `:166` is to a line this same dispatch rewrites** — the report cites `L3/eigsolve.md:166` while edit-6 simultaneously rewrites that line. After integration the line content shifts; the `:166` anchor will still be in-range but its on-token meaning depends on the rewritten bullet. Severity: very low. Mentioned for the repairer/integrator's awareness; folds into issue 1's repair.

No fence-truncation, no stale-residue, no status-flip, no missing-site, and no fabricated-fold defects were found. The opaque-library framing is honest and the 7-site floor-landing re-anchor is complete and correctly scoped.

## Repair

### Fixes attempted

- **Finding**: Weak/imprecise pinpoint anchor `[L3/eigsolve]:166` for the partial-success-arm claim (`PartialConverged k` / `0 < k < requested`, no `ksp_solve` analog). The disk line `L3/eigsolve.md:166` is the `solve-monad` dependency bullet ("richer than `ksp_solve`'s soft-fail") — it does NOT name the partial-success arm; the substantive anchor is `L1/eigsolve.md:78`.
  - **Decision**: repaired (citation-precision re-pin; not verdict-inverting).
  - **Disk verification before editing**:
    - `book/src/L1/eigsolve.md:78` — confirmed the substantive partial-success-arm anchor: "**Partial convergence is the L1 form's distinguishing semantic feature relative to `ksp_solve`**", with the count-less-than-requested / sum-typed-`status` semantics and `PartialConverged` named. Supports the claim exactly.
    - `book/src/L3/eigsolve.md:166` — confirmed it is the `solve-monad` Dependencies bullet ("the (future, unauthored) L4 outer-coordination surface … with sum-typed termination richer than `ksp_solve`'s soft-fail"); does NOT name `PartialConverged` / `0 < k < requested` / a first-class partial-success arm. Weak pinpoint confirmed.
  - **Action**: re-pinned the two in-body co-citations where the partial-success claim leaned on `:166` alongside `:78`, making `L1/eigsolve.md:78` the explicit PRIMARY anchor and demoting `L3/eigsolve.md:166` to a labeled supporting/theme reference:
    - CYCLE.md §Summary (line 26).
    - CYCLE.md §Variant-axes axis 1 (line 210, inside the `new:` cap body).
    The critic also listed §Algebraic-laws law 3 and both `L4/index.md` appends as `:166` sites, but on inspection those cite only `:78` for the partial-success claim already (no `:166` co-citation present) — no edit needed there.
  - **Scope discipline**: the `:166` re-anchor edit (one of the 7 stale-assertion floor-landing rewrites to `L3/eigsolve.md`, CYCLE.md:264-266) is the Dependencies `solve-monad` bullet rewrite — left UNTOUCHED (correct, per critic). The §Supporting-evidence re-anchor-site documentation (line 312) that names `:166` as a re-anchor target is likewise left as-is (accurate). Only the citation-precision usages in the cap's own prose were re-pinned.

### Unrepairable findings

None. The sole warning was a citation-precision re-pin within repair authority (citation line/anchor correction — the loose anchor was propagated from the c047 `L4/index.md` rows, not invented, so this is a re-pin not a deletion).

## Suggested resolution

`ready`. Content is sound and high-quality (all library-source anchors codemap-verified, opaque-library framing honest, EigOutcome clean-addition correct, fence-parity even, 7-site re-anchor complete and correctly scoped, D2 count-tally correctly deferred to D4). The lone warning is now repaired by a citation-precision re-pin that does not invert any verdict. Integrator note: the partial-success claim is now load-bearing-anchored to `L1/eigsolve.md:78` with `L3/eigsolve.md:166` demoted to a supporting theme reference, consistent with the post-rewrite content of that L3 bullet.
