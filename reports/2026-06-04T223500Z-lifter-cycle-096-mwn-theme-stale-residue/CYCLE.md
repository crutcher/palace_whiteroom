---
agent: lifter
invoked_at: 2026-06-04T22:35:00Z
scope: L1>L0 theme within-file stale-residue re-anchor — matrix-weighted-norm-mutation-rotation
status: integrated
integrated_at: 2026-06-05T001500Z
integration_commit: 2b8cb55b1fe4d011c4fd384b0b6f6459097804ba
integration_notes: |
  Applied clean (D5, cycle-096 batch-30 position 3/3, the LAST staged report). book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md within-theme stale-residue fix (x2: :5 opening prose + :317 Speculative-L1 clause, both rough-in -> firm; theme's own ## Status untouched). Prose maturity-word swap only. rank-gate not-triggered (no node status flip). citecheck 9 ok / 0 failing. Build clean. OQ matrix-weighted-norm-mutation-rotation-within-theme-stale-rough-in-residue CLOSEABLE at meta unify. NEW OQ domain_energy_reduce-377-mwn-stale-rough-in-residue (cross-file grep-guard surfaced book/src/L4/domain_energy_reduce.md:377, FLAGGED-not-fixed, batch-31 land-clean).
inputs:
  - book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md
  - book/src/L1/matrix-weighted-norm.md
  - reports/2026-06-04T222917Z-cycle-planner-cycle-096/CYCLE.md
---

# CYCLE: Re-anchor matrix-weighted-norm-mutation-rotation (within-theme stale residue)

## Summary
The L1 operator `matrix-weighted-norm` was promoted to `firm` at cycle-091 (`book/src/L1/matrix-weighted-norm.md:4` `rank: firm`; entry firm c091). Its L1>L0 lowering theme `matrix-weighted-norm-mutation-rotation.md` still carried prose narrating that operator as `rough-in` / `rough-in (test-coverage-bounded)` in TWO body sites — the c095 signal flagged one (`:317`), and the planner D5 scope confirmed it. A whole-file grep confirms there are exactly **two** genuinely-stale operator-maturity assertions in this theme: line 5 (the opening prose qualifying the LHS L1 form as `rough-in`) and line 317 (the §Speculative-L1-operators "(rough-in, test-coverage-bounded)" clause). Both are re-anchored to the firm post-c091 reality. This is a surgical prose re-anchor only — the theme's structure, its own `## Status` (`firm`, line 434, a theme-maturity, NOT touched), and all evidence pointers are unchanged. The theme already carries a correct, fully-accurate "Note on the upstream L1 gate (now discharged)" (lines 447-455) and a correct cross-theme anchor "(firm, promoted cycle-091)" (line 412) — those remain as-is.

## Proposed changes

Two surgical prose re-anchors in the theme body. Neither touches the theme's own `## Status` verdict (the theme is firm independently; only references to the OPERATOR's maturity are re-anchored).

```edit:book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md
[old]: `matrix_weighted_norm(x, B) = √(xᴴ B x)` ([`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md),
rough-in) into Palace's L0 `linalg::Norml2(comm, x, B, Bx)` three-step composition
[new]: `matrix_weighted_norm(x, B) = √(xᴴ B x)` ([`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md),
firm) into Palace's L0 `linalg::Norml2(comm, x, B, Bx)` three-step composition
```

```edit:book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md
[old]: **None.** This theme lowers the existing L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
operator (rough-in, test-coverage-bounded) into existing firm L1 vocabulary — `apply_linop` for the
[new]: **None.** This theme lowers the existing L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
operator (firm, promoted cycle-091) into existing firm L1 vocabulary — `apply_linop` for the
```

## Discipline notes

- **What changed and why.** Two within-theme prose clauses asserted the OPERATOR `matrix-weighted-norm`'s maturity as `rough-in` / `rough-in (test-coverage-bounded)`. The operator promoted to `firm` at cycle-091 (`book/src/L1/matrix-weighted-norm.md:4` `rank: firm`, self-verified via `citecheck --anchor 'rank: firm'` → anchor at line 4 within range 1-12). These are stale references to the operator's maturity (the within-file self-consistency class the c091 cascade missed; sibling of the cross-file whole-book-grep guard in `.claude/agents/lifter.md`). Re-anchored both to the firm reality. This is a bounded prose re-anchor — no decomposition / signature / structural change.
- **Theme `## Status` deliberately NOT touched** (line 434 `firm`). Per the D5 scope and the lifter discipline ("a theme has its own maturity — only re-anchor references to the OPERATOR's maturity"). The theme was already `firm` while the operator was rough-in (a firm lowering of a rough-in L1 operator is consistent — structural fidelity is independent of the L1 law-confidence gate); the operator's promotion did not change the theme's status. The theme's own "Note on the upstream L1 gate (now discharged)" (lines 447-455) already narrates this correctly and is left intact.
- **Sites confirmed NOT stale (left unchanged):**
  - Line 412 — "(firm, promoted cycle-091)" — already correct.
  - Lines 447-455 — the "Note on the upstream L1 gate (now discharged)" block — already correct post-c091 narration.
  - Line 441 — "reuses the firm/rough-in sibling sub-themes (`apply_linop` ... `dot` ... `scal`)" — describes the *sibling sub-themes'* maturity, NOT the matrix-weighted-norm operator's; out of D5 scope (the scope is references to the OPERATOR's maturity). Left as-is.
- **Whole-file grep result:** exactly two genuinely-stale operator-maturity assertions in this theme (lines 5, 317). The c095 signal flagged only :317; I confirm :5 is the same class — fixed in the same pass. No other in-theme `matrix-weighted-norm ... rough-in` narration survives.
- **Citation hygiene:** the only citation I emit/rely on is `book/src/L1/matrix-weighted-norm.md:4` (`rank: firm`), self-verified at emit time via `citecheck --anchor`. The two edits change prose maturity-words only; they introduce no new `path:lo-hi` pinpoint citations.

## Supporting evidence

- `book/src/L1/matrix-weighted-norm.md:4` — `rank: firm` (operator firm; promoted c091). Self-verified via `python3 tools/citecheck/citecheck.py book/src/L1/matrix-weighted-norm.md:1-12 --anchor 'rank: firm'` → `[ok] anchor at line(s) [4]`.
- `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md:5` and `:317` — the two stale operator-maturity assertions re-anchored.
- `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md:412`, `:447-455` — the already-correct post-c091 narrations confirming the firm reality the residue contradicted.
- Planner D5 scope: `reports/2026-06-04T222917Z-cycle-planner-cycle-096/CYCLE.md:228-239`.
- Resolves OQ `matrix-weighted-norm-mutation-rotation-within-theme-stale-rough-in-residue`.

## Open questions / caveats

- **Cross-file residue flagged for a co-scheduled / batch-31 land-clean lifter (NOT in D5's one-theme scope).** The whole-book maturity-token grep (`.claude/agents/lifter.md` cross-file guard) surfaced one CLEAN cross-file genuinely-stale operator-maturity assertion outside this theme:
  - **`book/src/L4/domain_energy_reduce.md:377`** — `[matrix-weighted-norm](../L1/matrix-weighted-norm.md) (rough-in (test-coverage-bounded) — the ½⟨field, M field⟩ energy-form half)`. This asserts the operator's OWN maturity at the old token and is falsified by the c091 firm-flip. It should be re-anchored to `(firm, promoted cycle-091 — ...)` in a follow-up pass. D5 is scoped to ONE theme (`matrix-weighted-norm-mutation-rotation.md`) per the lifter one-theme-per-invocation discipline, so I flag rather than fix.
- **Meta-phase-owned residue (explicitly left for the batch-30 meta-phase by the planner):** `book/src/methodology/goal-flow.md:218` carries `... domain_energy_reduce + matrix-weighted-norm rough-in)`. The planner's §Open-questions explicitly partitions `goal-flow.md` to the meta-phase (it is meta-phase-owned, carrying the same stale cascade narration as the `resolution-ladder.md` worked example D2 fixes). Not touched here; flagged so the partition is explicit.
- **Secondary / borderline (NOT re-anchored — judged non-stale):** `book/src/L2/index.md:121` and `:112` describe `normalize_B` as a sibling rough-in note "`matrix-weighted-norm`-gated". The sentence asserts `normalize_B`'s status (rough-in on no-live-consumer ground), and `book/src/L1/normalize.md:26` already correctly states "`matrix-weighted-norm` (firm) ... but the fused B-Normalize is uncalled" — i.e. `normalize_B`'s real gate is no-live-consumer, NOT a constituent-maturity gate. The "mwn-gated" phrasing in the L2 index cells is mildly stale-in-framing but does NOT assert mwn's maturity as rough-in; a fuller normalize_B-gate-rewording is a separate normalize cohort follow-up, not an operator-maturity residue. Noted, not fixed.
