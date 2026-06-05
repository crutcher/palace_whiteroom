---
agent: cycle-planner
invoked_at: 2026-06-05T062537Z
scope: cycle-102 dispatch plan
status: pending
---

# Cycle 102 dispatch plan

## Goals selected this cycle

Cycle-102 is the **batch-CLOSING cycle of meta-batch-32** (position 3/3; the batch-32 meta-phase fires AFTER this cycle's finalize, aggregating 100/101/102). Per batch-closing discipline (the c096/c099 precedent) this cycle takes **LOW-RISK, cleanly-closeable hygiene** — NOT a new multi-dispatch campaign straddling the meta boundary. The substantive forward frontier was worked off across c100 (the two L1>L0 mutation-rotation floors firmed + the L4-completeness survey) and c101 (the BC-elimination L4 hole CLOSED — the in-scope stack is now substantially L4-complete for backend-lowering). The genuine remaining frontier members are obstruction/demand-gated (`promotion_frontier: 8` per the c101 linter), and the redirect forbids manufacturing a rectangular pull-up. So c102 lands the **two clean hygiene residues the c101 finalize explicitly flagged**: (1) the lagging `L4/index.md` §Vocabulary-cohort firm-count prose (says "19 + 4"; on-disk is 21 main / 25 grand after the c101 `eliminate_bc` landing), and (2) the 2 pre-existing basename-only/ambiguous citecheck flags in `fe-assemble-fold-dissolution.md`. The two new OQs from c101 (`record-DofSet-needs-definition-home`, `eliminate-rhs-mutation-rotation` L1>L0 leg) are **explicitly meta-phase-routed + trigger-gated** and are NOT dispatched (the OQ ledger says "do NOT treat as fresh independent item" / "Trigger: a layer-intro-author concept-page cohort pass"); they are surfaced to the batch-32 meta-phase below.

## Dispatches

**D1 — `layer-intro-author` — `L4/index.md` §Vocabulary-cohort firm-count + narration refresh (`book/src/L4/index.md`).**
Refresh the §"Vocabulary cohort" prose to current on-disk artifact state. The count header reads **"Firm at L4 (19 + 4 outer-driver)"** (line 32) and the narration's most-recent landing block is cycle-095 (`gram_reduce`) — it predates the cycle-101 `eliminate_bc` firm landing. The on-disk truth (cycle-101 `counts_after`): **L4 firm 21 main / 25 grand** (`eliminate_bc` added the dep-map row at line 100 + the L4>L3 tally it owns, but the §Vocabulary-cohort count header + narration lag). The author recounts from each linked chapter's `## Status` line (the c057-meta guard — count from chapters, NOT index cells), updates the "(19 + 4 outer-driver)" header to the reconciled current main/outer-driver split (on-disk grand = 25), and prepends a cycle-101 narration sentence naming `eliminate_bc` (the post-assembly BC-application verb-pair, the assemble-half-completing companion of `fe_assemble`; route (a) firm L4 cap; DISSOLUTION-HOME L4>L3 theme `bc-elimination-post-composition-dissolution`). Mechanical / build-relevant; no new vocabulary, no new edges.
- **deps:** none.
- **rationale:** c101 finalize suggested-next-dispatch (`L4/index.md §Vocabulary-cohort firm-count + §Cycle-068 narration refresh`); staging row 1 D1-caveat. layer-intro-author owns the index narrative. Clean, mechanical, batch-closing-appropriate.

**D2 — `lifter` — citation-hygiene full-path pass on `book/src/L4-L3/fe-assemble-fold-dissolution.md`.**
Full-path the 2 pre-existing citecheck-flagged citations (both on lines NOT touched by the c101 c069-re-anchor diff, so genuinely open hygiene residue):
  - **`integrator.hpp:58-61`** — `[AMBIG]` basename collision (matches `palace/fem/integrator.hpp` AND `palace/fem/libceed/integrator.hpp`). The cited referent is the pure-virtual `Assemble(...) const = 0;` dispatch of `BilinearFormIntegrator` — **codemap-confirmed to be `palace/fem/integrator.hpp:58-61`** (line 58 `virtual void Assemble(Ceed ceed, ...` through `:61` the `= 0;` terminator; the `libceed/integrator.hpp:55-63` region is `AssembleCeedOperator`, NOT the pure-virtual). Occurs at `fe-assemble-fold-dissolution.md:86`, `:102`, `:106`. Rewrite the basename `integrator.hpp:58-61` → `fem/integrator.hpp:58-61` at all 3 sites.
  - **`libceed/operator.cpp:455`** — `[MISS]` basename-only (the basename `libceed/operator.cpp` does not resolve; the full path does). **codemap-confirmed** `palace/fem/libceed/operator.cpp:455` is `CeedOperatorFullAssemble(...)`. Occurs at `:106`, `:126`. Rewrite `libceed/operator.cpp:455` → `fem/libceed/operator.cpp:455` at both sites.
The lifter does NOT touch any claim, status, or structure — pure citation-format hygiene (full-path the basename-only/ambiguous forms). Re-run citecheck on the file post-edit to confirm 16/16 clean.
- **deps:** none.
- **rationale:** c101 finalize integration-tooling-friction + suggested-next-dispatch (`lifter`, `fe-assemble-fold-dissolution.md citation-hygiene`). The disambiguating full paths are codemap-confirmed in this plan (no localization loop needed). Clean, surgical, batch-closing-appropriate.

## Deliverable-presence verification

Both dispatches resolve to named `book/src/` file paths → four-step deliverable-presence sequence run, evidence pasted inline.

**D1 — `book/src/L4/index.md` (§Vocabulary-cohort firm-count refresh):**
1. **File existence:** `ls -la book/src/L4/index.md` → `-rw-rw-r-- 1 crutcher crutcher 99539 Jun 4 23:02 book/src/L4/index.md` — EXISTS.
2. **Maturity / already-discharged:** the deliverable is a PROSE refresh, not a status flip. On-disk the §Vocabulary-cohort header reads `**Firm at L4 (19 + 4 outer-driver)**` (line 32) with the most-recent narration block dated cycle-095 (`gram_reduce`); the cycle-101 `eliminate_bc` landing is in the dep-map (line 100, alpha-placed) but NOT in the count header or narration. cycle-101 `counts_after` (cycle-record.jsonl): `L4_firm_main: 21, L4_firm_grand: 25`. The prose (23 grand) is STALE by 2 → deliverable is OPEN (the refresh has NOT been applied). NOT a no-op.
3. **OQ-ledger RESOLVED-grep:** no closure exists — this is a finalize-flagged prose lag, not an OQ-tracked item; `grep 'L4.*index.*firm-count.*RESOLVED' scaffolding/open-questions.md` → no matches.
4. **Structural-block check:** no gate — a prose/count refresh on an already-firm index is layer-intro-author domain, unblocked. (No rank/status concern: no node changes maturity.)
→ ALL CHECKS PASS, not on STOP-PROPOSING list, framing correct (layer-intro-author owns the index narrative). RECRUIT.

**D2 — `book/src/L4-L3/fe-assemble-fold-dissolution.md` (citation-hygiene full-path):**
1. **File existence:** `ls -la book/src/L4-L3/fe-assemble-fold-dissolution.md` → `-rw-rw-r-- 1 crutcher crutcher 51474 Jun 4 23:00 book/src/L4-L3/fe-assemble-fold-dissolution.md` — EXISTS.
2. **Maturity / already-discharged:** the 2 citecheck flags are CONFIRMED on-disk present (`grep -n 'integrator.hpp:58-61\|libceed/operator.cpp:455'` → `:86`, `:102`, `:106` carry `integrator.hpp:58-61`; `:106`, `:126` carry `libceed/operator.cpp:455` — both basename-only/ambiguous forms, NOT yet full-pathed). c101 finalize citecheck reported `14/16 ok with 2 PRE-EXISTING out-of-scope flags`. Deliverable (full-path them to 16/16) is OPEN — NOT a no-op.
3. **OQ-ledger RESOLVED-grep:** `grep 'fe-assemble-fold-dissolution.*RESOLVED\|citation-hygiene.*RESOLVED' scaffolding/open-questions.md` → no matches; the c101 finalize routed it to meta-phase intake as "a thin citation-hygiene lifter pass is the cheap fix" — open.
4. **Structural-block check:** no gate — the disambiguating full paths are codemap-confirmed (this plan): `palace/fem/integrator.hpp:58-61` is the `BilinearFormIntegrator::Assemble` pure-virtual (`virtual void Assemble(... ) const = 0;`), `palace/fem/libceed/operator.cpp:455` is `CeedOperatorFullAssemble`. The lifter touches NO claim — pure citation-format hygiene; the redirect/anti-mirror disciplines do not apply (no vocabulary).
→ ALL CHECKS PASS, not on STOP-PROPOSING list, framing correct (lifter = citation re-anchor to firm/correct source). RECRUIT.

**Codemap-confirmed source anchors (pre-localized for D2 so no localization loop):**
- `palace/fem/integrator.hpp:58-61` — `virtual void Assemble(Ceed ceed, CeedElemRestriction trial_restr, CeedElemRestriction test_restr, CeedBasis trial_basis, CeedBasis test_basis, CeedVector geom_data, CeedElemRestriction geom_data_restr, CeedOperator *op) const = 0;` (read_range confirmed; `:58` is the `virtual void Assemble(` open, `:61` the `= 0;` terminator — END line is the brace-boundary candidate; the producer on-disk-confirms).
- `palace/fem/libceed/operator.cpp:455` — `std::unique_ptr<hypre::HypreCSRMatrix> CeedOperatorFullAssemble(const Operator &op, bool skip_zeros, bool set)` (read_range confirmed at `:455`).
- The competing AMBIG candidate `palace/fem/libceed/integrator.hpp:55-63` is `AssembleCeedOperator` (a libCEED-construct helper), NOT the pure-virtual — confirms the disambiguation to `fem/integrator.hpp`.

## Overlap analysis

- **D1 ↔ D2:** D1 edits `book/src/L4/index.md` (the L4 Part overview). D2 edits `book/src/L4-L3/fe-assemble-fold-dissolution.md` (an L4>L3 lowering-theme chapter). **DISJOINT files**, no shared operator names (D1 touches the index count-prose + narration; D2 touches citation strings inside a theme body). No shared running-count / consolidated tally is co-written (D1 is the sole writer of the L4/index count; D2 writes no index). No cross-report forward-reference (neither references the other's not-yet-existing slug). **NOT overlapping → PARALLEL.**

## Sequencing schedule

**ONE wave (both parallel):**
- Wave 1: D1 (`layer-intro-author`, L4/index firm-count refresh), D2 (`lifter`, fe-assemble-fold-dissolution citation-hygiene).

No forward-reference ordering (neither dispatch references the other's output); the per-report integrator applies both serially in staging order (artifact writes naturally serialize), then the single `integrator-finalize` rebuilds + commits once.

## Open questions / caveats

- **Two c101 OQs are deliberately NOT dispatched this cycle (meta-phase-routed + trigger-gated):**
  - `record-DofSet-needs-definition-home` — `DofSet[N]` now has a 3rd consumer (the c101 `eliminate_bc` cap) and no `concepts/DofSet.md`. The OQ ledger (line ~1533) explicitly says *"the meta-phase should unify these under one plan candidate"* with the c055 cohort (`dof-set-concept-page` / `fe-bc-dof-set-and-set-subvector-concept-pages`), *Trigger: a layer-intro-author concept-page pass (the DofSet/set_subvector-mask concept-page cohort)*. It is a `concepts/` page (data-shape definition, layer-intro-author domain) but is correctly a **unify-first meta-phase decision** + part of a cohort pass, NOT a standalone batch-closing micro-dispatch. **Surfaced to the batch-32 meta-phase to unify the c055 + c101 DofSet/set_subvector record-definition cohort and decide the concept-page pass.**
  - `eliminate-rhs-mutation-rotation` L1>L0 leg (forthcoming-vs-already-folded) — the OQ ledger (line ~1537) explicitly says *"do NOT treat as a fresh independent item — it is `fe-bc-elimination-l1-l0-theme-split-vs-fold` viewed from L4"*; the legs already fold inline into the firm `fe-operator-assemble-mutation-rotation.md`; *Trigger: an abstractor decides to split (LOW fan-out)*. NOT a batch-closing pick. **Surfaced to the meta-phase to reconcile the split-vs-fold naming with `fe-bc-elimination-l1-l0-theme-split-vs-fold`.**
- **Memory `project_l4_is_backend_lowering_target` is DOUBLY-STALE** (its named hole "FE-assembly/FE-space cohort stranded at L1" is falsified twice over: assemble-half closed c068, BC-half closed c101 — NO remaining named FE-cohort L4 hole). Memory edits are out of finalize/planner scope. **STRONG recommend the batch-32 meta-phase update it** (recorded by c100 + c101 finalize signals).
- **No third filler dispatch** — `promotion_frontier: 8` (c101 linter) with remaining members obstruction/demand-gated (`bicgstab`/`minres`/`deflate*`/`boundary-mode.*` are NOT targets; `eigsolve-convergence-reason-mapping` structurally blocked; `waveguide-mode`/`boundary-mode` columns demand-gated). The redirect forbids manufacturing a rectangular pull-up (c088/c090/c092/c100/c101 light-frontier precedent). STOP-PROPOSING NEGATIVE LIST remains in force; no candidate this cycle matches it.
- **The full graded-stack edge-typing pass + dead orchestrator-era skills retirement** are explicitly the **meta-phase's owned standing campaigns** (priorities item 0 standing duty; `orphan-review-follow-ons` 3a) — deliberately left to the batch-32 meta-phase per batch-closing discipline, NOT launched here.
