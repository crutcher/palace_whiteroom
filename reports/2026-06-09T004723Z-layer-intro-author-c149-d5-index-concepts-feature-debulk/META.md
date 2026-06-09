---
verifies: ../CYCLE.md
critiqued_at: 2026-06-09T010500Z
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

# META: verification of c149-d5 — index / concepts / feature / synthesis-shell de-bulk

## Critique

This is a FINALIZATION de-bulk report (DIRECTIVE `project_finalization_debulk_directive`): a prose-only strip of 7 inline process/judgment attributions across 6 `book/src/**` index/concept/feature/synthesis-shell files toward the static-state finalized surface. It authors no new vocabulary, asserts no new claim, and moves no node/edge/rank. The 8 checks are therefore largely no-op (nothing to claim, nothing to rotate), and the load-bearing review is the CONSERVATION audit, which I ran against `git show HEAD:<file>` for all 6 files. All conservation invariants held; all 8 checks pass.

### Checks run

**citation-validity — pass.** No new citation introduced (de-bulk does not author). The only citation-bearing file, `L2/index.md`, claims 15 source ranges preserved; I verified HEAD and working tree both carry exactly 15 `path:line` source references (`grep -coE '[…].(cpp|hpp|cc|h):[0-9]'` = 15 = 15). The single diff line on that file is the `normalize` mid-cell prose — no citation in that segment. The other 5 files carry 0 citations (confirmed). Nothing lost.

**surface-or-evidence — pass (not applicable as a refinement-proposal check).** This is not a refinement of operator/theme surface and asserts no rotation_claim; it is a finalization strip. No record signature is newly named (no record-definition obligation triggered — all referenced records pre-exist their definition homes). The check no-ops; the substantive obligation here is conservation, audited below.

**rotation-quality — pass (not applicable).** No algebraic/structural rotation is asserted; de-bulk removes process accounting and does not touch the L_{n+1}/L_n representation relationship. The `normalize` factorisation, the `divfree_projector` four-step composition, etc. are all byte-identical except for the removed `cycle-N`/`batch-N` referents.

**variant-axis-coverage — pass (not applicable).** No operator with variant axes is authored or modified in its algebra. The `variant-absorption.md` and `constructed-operators.md` worked-example content (the `side ∈ {LEFT,RIGHT,NONE}` GMRES axis) is preserved in full — see conservation below.

**cross-reference-integrity — pass.** I hashed the full ordered `](…)` link set of each of the 6 files HEAD-vs-working: all 6 MATCH byte-for-byte. No internal link, slug, or anchor was added, dropped, or retargeted. No `reports/…` or deleted-slice link was present to drop. The 6 edits are pure mid-sentence prose.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is introduced or altered; the dep-map cells in `L2/index.md` (the only dep-map touched) are unchanged except the `normalize` mid-cell prose, with the trailing rank cell intact.

**plan-kind-consistency — pass.** Declared kind is a FINALIZATION de-bulk wave; content shape matches exactly — 7 inline attributions stripped, worked examples rephrased-not-deleted, no rank/status/citation touched, lint baseline asserted held. No mis-classification.

**skill-uptake-survey — pass.** The report explicitly references applying the `finalization-debulk` skill (STRIP-rule-2 inline attributions; rephrase-don't-delete worked examples) and observes its `concepts/` carve-out (Context/Origin narrative left out of scope). Skill uptake is surfaced.

### Conservation audit (the load-bearing review for a de-bulk report)

- **No citation lost — CONFIRMED.** `L2/index.md`: 15→15 source ranges (byte-verified). The other 5 files: 0→0. The `git diff` touches no citation token on any file.
- **No rank/status token lost — CONFIRMED.**
  - `L2/index.md` (NO-FRONTMATTER-RANK, dep-map rank cells are sole rank carriers): `` `firm` `` count 18→18, `partly-constructive` count 6→6 (the `deflate` row intact). The `normalize` row change is confined to mid-cell prose ("design-final on the batch-12 leaf-vs-fold fork (`dot-l2-leaf-floor-vs-fold-only-design`)" → "design-final under the leaf-vs-fold distinction"); word-diff shows the trailing `| `firm` |` rank cell is untouched.
  - `synthesis/data-algebra.md`: the `## Status` section (lines 470-474) is byte-identical — the `navigational-container` leading token AND the sole-on-disk-rank-carrier NOTE flagging the `stub`-token inconsistency both survive. The edit was at the `sharding-decompose-reduce` body note (line ~467), above the Status section. The `**Status:** roadmap_goal (no claims; not a filled def)` sub-head above the edited line is preserved.
  - `feature/index.md`, `feature/infrastructure.md`: navigational-container `kind:`-only frontmatter (no `rank:`) untouched.
- **Worked-example REPHRASED not deleted — CONFIRMED, rephrasing FAITHFUL.** `concepts/constructed-operators.md`, both tags:
  1. Heading "Without constructed operators (cycle-7 / cycle-9 shape)" → "(the deep-plumbed `side`-conditional shape)". Accurate: the section walks through `side ∈ {LEFT, RIGHT, NONE}` deep-plumbing (line 30 names "deep-plumbing"; the code block at lines 40-50 IS the `side`-conditional shape; line 52 names the procedural/primitive-sequence absorption failure). The static descriptor names the worked-example by its characterizing feature.
  2. "(cycle-7's `side` case is the worked counter-example)" → "(the GMRES preconditioner-`side` case is the worked counter-example)". Accurate: the enclosing section is titled "Worked example: GMRES preconditioning" and the `side` parameter IS the GMRES preconditioner side. The counter-example pointer is kept live.
  Both the full code blocks (Arnoldi-step + solution-update conditionals, the constructed-operator form, the (a)/(b)/(c) absorption-level walkthrough) remain fully present; only the `cycle-N` process referents were removed.
- **Graded-stack baseline HELD EXACTLY — CONFIRMED.** Re-ran `graded_stack_lint.py --book-src book/src` on the working tree: `files=392, typed=331, untyped=61, rank_violations=0, unresolved_depends_on_targets=0, promotion_frontier=11, detritus=123 (true_detritus=51 / reference-reachable=72)`. Rank histogram unchanged: `firm: 224, rough-in: 4, partly-constructive: 3, obstruction: 2, partial-obstruction: 4, roadmap_goal: 4, typed-no-rank: 90` (sum 331 = typed). Every claimed figure matches.
- **Deliberately-left residue — CORRECT scoping, NOT a defect.** `variant-absorption.md` retains `cycle-N`/`meta-review #N` matches ONLY in its `## Context` / `## Origin` ("Added … meta-review") / `## Working Notes` historical-methodology narrative blocks (lines 15-18, 64, 78, 84, 86, 123, 128, 133). The targeted inline tag `Per cycle 23 lesson:` WAS stripped (HEAD count 1 → working 0), with the surrounding sentence reflowed cleanly. This Context/Origin/Working-Notes narrative class is the `finalization-debulk` skill's `concepts/` carve-out and was a meta-phase scoping judgment; the agent recorded the disposition in CYCLE.md Open-questions. Per the prompt this is a correct out-of-scope decision and is NOT flagged.

### Issues found

None. All 8 checks pass; every conservation invariant (citation count, rank/status tokens, link/anchor set, worked-example fidelity, lint baseline) holds byte-for-byte against HEAD; the rephrasings are faithful; the deliberately-left concept-page narrative residue is a recorded, correct scoping decision. Setting `overall_status: ready` (all-pass clean report; no repairer will run).
