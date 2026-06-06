---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T203600Z
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
repaired_at: 2026-06-06T204500Z
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

# META: verification of cycle-116 D1 semantic-surface path move + 97-file cross-reference rewrite

## Critique

### Checks run

**citation-validity — warning.** This is a mechanical move + path rewrite that asserts no new algebraic/structural claims, so the citation check largely no-ops. The two load-bearing evidentiary claims it DOES make are verifiable and verified: (i) "the move is a verbatim `git mv`" — confirmed via `git diff --cached --stat` showing `book/src/{design/l4_calculus.md => semantics/index.md} | 0` (0 insertions, 0 deletions; git tracks it as a pure rename `R`); (ii) "line numbers are stable because content moved verbatim" — confirmed: the new file is 513 lines, identical to the HEAD version of `design/l4_calculus.md` (also 513). The **warning** is for a verifiably-false factual statement in the report's own caveat 1 (Issue 1 below): it claims bare-basename `l4_calculus.md:NNN` prose refs "remain" in 4 files, but `grep -rn 'l4_calculus\.md' book/src` returns zero — the report's own substitution rewrote those refs to `index.md:NNN`. The artifact is correct; the report's description of the artifact state is not. Routed to the repairer to correct the caveat text.

**surface-or-evidence — pass.** Not a refinement/rotation proposal — no surface modification of operator/theme algebra, no record introduced. Pure structural relocation of an existing surface file. No record-definition obligation triggered (the moved file IS the semantic surface; it defines, it is not newly named-in-a-signature). Not applicable to a file-move dispatch; marked pass.

**rotation-quality — pass.** No algebraic/structural rotation asserted. A physical path move rotates nothing. Not applicable to this report-kind; marked pass.

**variant-axis-coverage — pass.** No operator with orthogonal variant axes is in scope. Not applicable; marked pass.

**cross-reference-integrity — pass (load-bearing for this dispatch; independently re-verified).** I re-ran both hard gates from a clean checkout: `grep -rl 'design/l4_calculus' book/src` → **0** (confirmed); `cargo make book` → **EXIT 0**, "Build Done in 95.52 seconds", no linkcheck2 `does not exist` / broken-link ERROR (the two literal `does not exist` string hits in the log are both inside multi-line WARN-level render-prose blocks, not linkcheck failures; the 135 "Potential incomplete link" entries are pre-existing content-driven `[...]`/math-bracket warnings, not errors). The new file exists at `book/src/semantics/index.md`; the old path is gone. The `design/index.md` same-dir `(./l4_calculus.md)` link — which a `design/`-prefix grep would NOT have caught and which would have dangled after the move — was correctly converted to a relative `(../semantics/index.md)` pointer note (CYCLE.md §4, verified on disk). `SUMMARY.md`'s `./design/l4_calculus.md` → `./semantics/index.md` rewrite landed. All link-TEXT occurrences `[`l4_calculus`](../semantics/index.md)` correctly retarget while keeping the literal text — these resolve. The rewrite is complete and the build is clean.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label carried by a move dispatch. Not applicable; marked pass.

**plan-kind-consistency — pass.** The declared kind (mechanical file-move + bulk link-rewrite under a hard build gate, enacting the semantic-consolidation directive-A LEAD) matches the content shape exactly. This is precisely the right kind of work for WAVE-1 of the campaign: relocate the surface to its own top-level home before the restatement-cohort relocation sweeps reference it. No mis-classification.

**skill-uptake-survey — pass (telemetry).** A `proposed-changes-fence-encloses-full-body-guard`-style skill is not implicated (no firm-body authoring here). No move/link-rewrite-specific skill exists to reference; the dispatch's own grep+build gate IS the procedure. Nothing to flag.

### Issues found

**Issue 1 — Caveat 1 is factually inaccurate: the bare-basename `l4_calculus.md:NNN` refs do NOT remain; they were rewritten to `index.md:NNN` (CYCLE.md §"Open questions / caveats" item 1, severity: low-but-misleading).** Caveat 1 states that bare-basename prose citations of the form `l4_calculus.md:164-171`, `l4_calculus.md:418`, `l4_calculus.md:374-386` "remain (OUT OF SCOPE, non-breaking) in 4 files" (`L4/iterate-while.md`, `L4/chebyshev.md`, `L4/ksp_solve.md`, `L4/index.md`). This is not the on-disk state. `grep -rn 'l4_calculus\.md' book/src` returns **zero** matches anywhere — the basename `l4_calculus.md` does not exist in `book/src`. The git diff of `L4/iterate-while.md` shows the substitution rewrote `l4_calculus.md:186-213` → `index.md:186-213`, `l4_calculus.md:164-171` → `index.md:164-171`, etc. So the class-(b) substitution (described as replacing the full path `book/src/design/l4_calculus.md`) in fact ran as a bare-substring `l4_calculus.md` → `index.md` rewrite, which DID catch these prose refs. The caveat describes a residual-staleness state that does not exist; the report under-described the actual reach of its own substitution.

**Issue 2 — The substitution introduced ambiguous bare-basename `index.md:NNN` prose refs (consequence of the actual Issue-1 rewrite, severity: low; the genuine residual the caveat should have flagged).** Because the bare `l4_calculus.md:NNN` refs were rewritten to bare `index.md:NNN` (not to `semantics/index.md:NNN` or `book/src/semantics/index.md:NNN`), the surviving inline-code prose citations in those L4 files (e.g. `L4/iterate-while.md:64` `(`index.md:164-171`)`, `L4/ksp_solve.md:117` `(`index.md:178-182`)`, `L4/chebyshev.md:218` `(...):418`) now name a basename — `index.md` — that is shared by every Part overview in the book. They are non-breaking (inline-code, not link targets; the build is clean) and the `:NNN` ranges remain valid against the verbatim move, but they are now ambiguous-referent prose mentions where the old `l4_calculus.md` was at least unique. This is the real residual for a follow-up sweep to normalize (to `the semantic surface §N.N` or `book/src/semantics/index.md:NNN`). Per the dispatch framing, D2 / a follow-up was tasked to clean these up; the suggested OQ `bare-basename-l4_calculus-prose-refs-stale-after-move` is correctly motivated but should be re-scoped to "ambiguous bare `index.md:NNN` prose refs" (the `l4_calculus.md` name is already gone). Severity low — does not gate the build or the campaign.

**Issue 3 — Pre-existing line-range citation drift, NOT introduced by D1 (out of scope; observation only, severity: informational).** Several L4 entries cite §3.7 (`iterate_while`) at `index.md:151-184` / the small-step rule at `:164-171` (e.g. `L4/iterate-while.md:211`, `:222`; `L4/ksp_solve.md:117`, `:194`). On disk, §3.7 is at lines **190-225** (`### 3.7 Loops (\`iterate_while\`)` at line 190; the small-step block ~202-218); lines 151-184 are §3.5/§3.6 and 164-171 fall in §3.3/§3.4 (monad laws / state effects). This is a genuine citation-content drift — BUT it is **pre-existing and not a D1 defect**: the HEAD version of `design/l4_calculus.md` had §3.7 at the identical line 190 (513 lines, byte-identical), and the move was a verified 0-content-diff `git mv`. D1 faithfully preserved (did not introduce) the drift; correcting it was out of D1's stated scope. Flagging only so it is not lost — a candidate for the same follow-up sweep that re-anchors the prose refs in Issue 2.

### Disposition note for the repairer

The cross-reference rewrite and build gate are genuinely clean — the load-bearing work is correct. The findings are: a misdescription in the report's own caveat text (Issue 1, the refs were rewritten, not left), a low-severity ambiguous-basename residual that is the true follow-up item (Issue 2), and a pre-existing out-of-scope citation drift that D1 correctly did not touch (Issue 3). None block integration of the move itself. Issues 1 and 2 are caveat-text accuracy and follow-up-OQ-scoping matters; Issue 3 is a tracked observation for a downstream sweep.

## Repair

### Fixes attempted

- **Finding (Issue 1)**: Caveat 1 factually inaccurate — claims bare-basename `l4_calculus.md:NNN-MMM` refs "remain" in 4 files, but `grep -rn 'l4_calculus\.md' book/src` → 0 (the bulk substring rewrite + D2's folded-in cleanup reached them, rewriting to `index.md:NNN`).
  - **Decision**: repaired
  - **Action**: rewrote CYCLE.md §"Open questions / caveats" item 1. Caveat now states the bare-basename `l4_calculus.md:NNN` prose refs were rewritten to `index.md:NNN` (not left), records the corrected on-disk reality (zero `l4_calculus.md` basename refs anywhere), and identifies the genuine residual. Mechanical caveat-text correction of the report's own description of artifact state — no new content authored. Re-verified on disk: `grep -rn 'l4_calculus\.md' book/src` → 0.

- **Finding (Issue 2)**: Suggested OQ `bare-basename-l4_calculus-prose-refs-stale-after-move` mis-scoped (that name is gone); the true residual is ambiguous bare `index.md:NNN` inline-code prose refs (every Part has an `index.md`).
  - **Decision**: repaired
  - **Action**: re-scoped the suggested OQ in the corrected caveat 1 to `ambiguous-bare-index-md-prose-refs-after-semantic-surface-move`, with prose describing the ambiguity (shared `index.md` basename) and the non-breaking/build-neutral nature. Mechanical OQ slug + scope rewrite from clearly-stated critic context.

- **Finding (Issue 3)**: §3.7 line-range citation drift — several L4 entries cite §3.7 at `index.md:151-184`/`:164-171` but §3.7 is at lines 190-225; PRE-EXISTING (faithfully preserved by the verbatim move), NOT a D1 defect, out of D1 scope to fix.
  - **Decision**: repaired (recorded as a tracked observation only; the L4 citations were NOT touched, per the critic's out-of-scope instruction)
  - **Action**: added CYCLE.md caveat 4 recording the drift as a tracked observation for a downstream citation-drift sweep, with the corroborating fact (HEAD `design/l4_calculus.md` had §3.7 at the identical line 190; byte-identical 513-line `git mv`) and a suggested OQ `l4-entries-section-3.7-line-range-citation-drift`. Did NOT modify any L4 entry citations (out of scope). Re-verified §3.7 at line 190 on disk.

### Unrepairable findings

None. All three findings were caveat-text accuracy / OQ-scoping / tracked-observation touches within mechanical repair authority. The move itself (verified verbatim `git mv` + clean `cargo make book` EXIT 0 + `grep design/l4_calculus` gate = 0) is correct and integration-ready; the critic's load-bearing checks (cross-reference-integrity, plan-kind-consistency) passed independently.

## Suggested resolution

`ready`. The semantic-surface physical move and 97-file cross-reference rewrite are correct and the build is clean — the integrator should apply D1 as-is. The three repairs were confined to CYCLE.md caveat text and follow-up-OQ scoping; `book/` was NOT mutated by the repairer. Two follow-up OQs are suggested in the corrected caveats for a downstream citation-drift / prose-ref-normalize sweep (both non-breaking, build-neutral): `ambiguous-bare-index-md-prose-refs-after-semantic-surface-move` (caveat 1) and `l4-entries-section-3.7-line-range-citation-drift` (caveat 4) — the integrator may promote these to `scaffolding/open-questions.md`.
