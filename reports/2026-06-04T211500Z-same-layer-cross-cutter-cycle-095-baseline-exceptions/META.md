---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T214500Z
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
overall_status: ready
---

# META: verification of "L-cross observation — GRADED-STACK P1 baseline rank-violation exception set" (D7, cycle-095)

## Critique

### Checks run

**citation-validity — pass.** This is an observation/ledger report whose load-bearing claims are the linter violation count, the partition arithmetic, and the on-disk firmness of the dep nodes. I re-ran every mechanical claim:
- `python3 tools/graded-stack-lint/graded_stack_lint.py --json` returns **exactly 22 rank violations** and histogram `firm 158, partly-constructive 8, rough-in 26, obstruction 10, stub 1, partial-obstruction 4` — matching the report's stated `rank_violations = 22` and histogram (the report lists the histogram in a different field order; the counts are identical) verbatim. ✓
- The genuine-residual verification: `book/src/L4-L3/solve-family-map-dissolution.md` carries **no** `rank:`/`firmness:`/`status:` frontmatter token (grep confirms — prose-fallback path confirmed); the `## Status` heading is at `:183` and the leading token `` `firm` — on the **structural rotation** `` is at `:185` (the report cites `:185` for the leading token — accurate); the provenance caveat `it was previously status `rough-in (test-coverage-bounded)`` is at `:187`, inside the 5-line blob (`lines[i+1:i+6]` = lines 184–188 after the `:183` heading) the scan reads. The off-by-position is exactly as D7 describes. ✓
- The four representative dep §Status pinpoints (`L1/eigsolve.md:167`, `L1/normalize.md:99`, `L2/inner_product.md:449`, `L1/matrix-weighted-norm.md:110`) all read `firm` on disk with the cited "rough-in" provenance/sibling/disclaimer phrases present in-blob. The report cites `L1/eigsolve.md:165/167` — `:165` is the `## Status` heading, `:167` the firm token; both in-range and accurate. ✓
- `tools/graded-stack-lint/graded_stack_lint.py:310-326` `read_status_line` reads as quoted: `blob = " ".join(lines[i + 1 : i + 6]).lower()` with the token scan ordering `rough-in (test-coverage-bounded)` / `rough-in` ahead of `firm`, and the docstring (`:311-314`) does claim "first non-empty line" while the implementation blob-scans. The bug description is exact. ✓
- The authority citations both resolve: `scaffolding/decisions/2026-06-04-graded-stack-p1-edge-home.md` exists; `METHODOLOGY-GRADED-STACK.md:102-110` §5 step-3 contains the quoted "explicit, tracked baseline-exception set with promotion conditions ... not open-ended fix-forward" text verbatim. ✓
No `verified_against:` block is proposed by this report (it is observation/ledger-only), so that YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This report proposes no `book/` surface change — it is a pure observation/ledger dispatch (`## Proposed changes` explicitly records "No `book/` proposed-changes blocks ... D7 is observation/ledger only"). The deliverable `scaffolding/graded-stack-baseline-exceptions.md` is a `scaffolding/` artifact within the same-layer-cross-cutter write authority, authored directly (verified on disk, 14676 bytes). No refinement-shaped operator/theme change is asserted, so the surface+rotation_claim coupling does not bind. The record-definition sub-check is not applicable — this report names no record/struct in a signature. The evidentiary backbone (linter run + on-disk §Status reads + D1–D6 cross-references) is the appropriate evidence shape for a discharge-ledger observation.

**rotation-quality — pass.** Not applicable to this report-kind: it asserts no algebraic/structural/reduction rotation of its own. The "Observation kind" is redundancy (the prose `## Status` vs the absent typed `rank:` token) + shared-sub-pattern (one root cause for 12 of 22) — a cross-cutting observation, not a layer-rotation claim. No-op.

**variant-axis-coverage — pass.** Not applicable: a baseline-exception ledger has no orthogonal variant axes. The partition does, however, exhaustively cover the violation space (10 cascade + 11 retyping + 1 tracked-open = 22, with the C2 duplicate-edge case explicitly called out rather than hidden), which is the analogous completeness obligation and is met.

**cross-reference-integrity — pass.** All cross-references resolve. The six cited sibling reports (D1 harvester-bilinear-form-firm-flip, D3 gram-reduce-rejudgment, D4 four-column-reeval, D5 feature-root-closure-typing, D6 vocab-frontier-typing) all exist on disk. The on-disk `solve-family-map-dissolution.md`, the four dep nodes, the decision file, and METHODOLOGY-GRADED-STACK.md all resolve. The partition is cross-checked against what the dispatches actually did: D1 flips `bilinear-form` rough-in→firm; D3 verdicts `gram_reduce` DISCHARGE→FIRM; D4 flips the 4 columns seed→firm under OWN-COMPOSITION — matching D7's CLEARED-BY-CASCADE provenance exactly. D6 independently root-causes the identical `read_status_line` blob-scan bug. No broken link or maturity overclaim found.

**edge-label-fidelity — pass.** The report carries explicit edge labels (e.g. `L4/solve_family → L4-L3/solve-family-map-dissolution`, `L4/gram_reduce → L1/bilinear-form`) and the prose discusses each exact edge. Every edge label in the partition tables corresponds 1:1 to a linter-emitted `{src, dep}` pair (I diffed the report's 22-row partition against the linter's 22-element `rank_violations` array — exact match, including the duplicated `gram_reduce → bilinear-form` edge correctly flagged as the C2 artifact). ✓

**plan-kind-consistency — pass.** Declared shape is an observation / ledger (same-layer-cross-cutter "Redundancy" + "Shared sub-pattern" observation kinds), and the content matches: it is analysis + a discharge-burn-down ledger with promotion conditions, carrying no firm-operator apparatus or rough-in placeholders that would indicate mis-classification. The "TRACKED-OPEN with promotion condition" framing correctly uses the `partly-constructive`-pattern transient-gate shape mandated by §5 — appropriate for a tracked-exception entry, not a maturity claim.

**skill-uptake-survey — pass (telemetry).** No directly-matching skill is mandated for a baseline-exception-ledger shape. The report's mechanical core (linter re-run + leading-token on-disk verification) is ad-hoc tooling invocation rather than a catalogued skill; nothing missing. Surfaces only that a "graded-stack-baseline-burn-down-audit" procedure does not yet exist as a skill — pure telemetry, non-blocking.

### Targeted-question findings (from the dispatch brief)

(a) **Partition arithmetic — correct.** 10 + 11 + 1 = 22, matching the linter's exact 22-violation count. The 10 CLEARED-BY-CASCADE map 1:1 to the bilinear-form-family edges (`gram_reduce→bilinear-form` ×2 incl. the C2 dup, plus the 4 columns' L0→L1 and L1→bilinear-form pairs); the 11 CLEARED-BY-RETYPING map 1:1 to the eigsolve ×3 / normalize ×2 / inner_product ×3 / matrix-weighted-norm ×3 false-positive edges; O1 is the lone solve_family edge. No double-count, no omission.

(b) **O1 = false-positive claim — correct.** Spot-checked on disk: `solve-family-map-dissolution.md` §Status leads with `firm` (`:185`), carries no frontmatter rank token, and `:187` is a resolved provenance caveat about the LHS cap (not a maturity statement about the theme). The blob-scan trips on the `rough-in (test-coverage-bounded)` caveat token before reaching `firm` — identical mechanism to R1–R11.

(c) **Promotion conditions per §5 — present.** O1 (the only TRACKED-OPEN) carries an explicit, mechanical promotion condition (type `rank: firm` + typed `edges:` block; both endpoints firm so it clears immediately). The CLEARED categories carry "discharged by" provenance rather than promotion conditions, which is correct — they are already discharged, not open exceptions.

(d) **Linter-re-run caveat — honest.** The report (and the ledger §"Mechanical completion check") correctly state the D1–D6 typed frontmatter is in proposed-changes, NOT on disk, so a NOW run shows the pre-typing 22 and `integrator-finalize` confirms the residual on the LANDED state. I verified this is the actual current state: the live linter returns the full 22 (the typed changes have not landed), exactly as the caveat predicts.

(e) **Bounded exception set — yes.** The ledger is a fixed, enumerated 22-row baseline partition burning down to a single tracked item with a mechanical promotion condition — the §5 "explicit, tracked baseline-exception set ... not open-ended fix-forward" shape, not a fix-forward list.

### Issues found

None. All eight checks pass; every mechanical claim (22-violation count, histogram, partition arithmetic, O1 false-positive on-disk verification, the four dep firmness spot-checks, the `read_status_line` source quote, the D1–D6 discharge cross-references, and the two authority citations) reproduced exactly against disk and the live linter. The report is clean.
