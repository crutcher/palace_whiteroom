---
verifies: ../REPORT.md
critiqued_at: 2026-06-04T23:05:00Z
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

# META: verification of "Re-anchor matrix-weighted-norm-mutation-rotation (within-theme stale residue)"

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` on the report: **9 ok, 0 failing**. The single load-bearing pinpoint — `book/src/L1/matrix-weighted-norm.md:4` `rank: firm`, the entire warrant for the re-anchor — was confirmed with `--anchor 'rank: firm'`: `[ok] anchor at line(s) [4] within range 1-12`. The operator is genuinely `firm` (frontmatter `:4`, and §Status `book/src/L1/matrix-weighted-norm.md:121-137` narrates the cycle-091 firm-flip). The report introduces no new `path:lo-hi` pinpoints in its two edits (prose maturity-words only), consistent with the discipline note at CYCLE.md:44. No `verified_against:` block is emitted by this report (it carries none of its own; it only references the theme's pre-existing block), so that sub-check is inapplicable.

**surface-or-evidence — pass.** This is a surface-modifying refinement (two prose clauses in an existing theme) backed by rotation-context evidence (the operator's firm-flip at `matrix-weighted-norm.md:4`/§Status). It is framed correctly as a stale-residue re-anchor — neither a pure rotation_claim without surface nor an un-framed evidence backfill. No record/struct is named in a signature by this report (it changes maturity words, not signatures), so the record-definition sub-check is inapplicable.

**rotation-quality — pass (not applicable to a stale-prose re-anchor).** The report asserts no new algebraic/structural rotation; it re-anchors two maturity-word clauses in an already-firm theme. There is no L_{n+1}/L_n compaction claim to grade. The theme's own rotation (the `Norml2` three-step structural expansion) is untouched.

**variant-axis-coverage — pass.** No variant axes are introduced or modified. The theme's existing element-type / weight-operator-representation axes (`matrix-weighted-norm-mutation-rotation.md:328-363`) are not in scope of the two edits and remain intact.

**cross-reference-integrity — pass.** Both edit `old_string`s match the on-disk theme exactly: edit 1 spans the file's lines 4-5 (`...matrix-weighted-norm.md),` / `rough-in) into Palace's...`); edit 2 spans lines 316-317 (`operator` / `(rough-in, test-coverage-bounded) into existing firm L1 vocabulary — \`apply_linop\` for the`). The `[link]` references inside both clauses (`../L1/matrix-weighted-norm.md`) resolve (the file exists and is firm). No new links added. Verified the report's "already-correct, left unchanged" claims: line 412 reads "(firm, promoted cycle-091)" — correct, untouched; lines 447-455 ("Note on the upstream L1 gate (now discharged)") narrate the history correctly, untouched.

**edge-label-fidelity — pass (the central correctness question, confirmed clean).** This is the load-bearing check for D5. Verified the theme's OWN `## Status` verdict at line 434 (`firm` — the theme-maturity) is NOT in either edit block and is untouched; both edits target references to the *operator's* maturity (lines 5, 317), exactly as the discipline note (CYCLE.md:38) and the D5 scope require. Whole-file `grep -ni 'rough-in'` returns 6 hits: the two D5 fixed (5, 317), plus three that D5 correctly left as non-stale — line 441 ("the firm/rough-in sibling sub-themes") describes the *sibling sub-themes'* maturity (apply_linop/dot/scal), not the mwn operator; lines 450/454/455 are the post-c091 history narration ("was already firm while the L1 operator was still rough-in"; "firm over the still-rough-in L1/eigsolve") — correct narrative content, not stale claims. The whole-file grep is therefore complete: exactly two genuinely-stale operator-maturity assertions existed, both re-anchored. The c095 signal flagged only :317; D5's catch of :5 is independently confirmed correct.

**plan-kind-consistency — pass.** Declared as a within-theme stale-prose re-anchor (lifter kind). Content matches: two surgical prose edits, no decomposition/signature/structural change, theme `## Status` deliberately untouched. No mis-classification.

**skill-uptake-survey — pass.** The report references `citecheck --anchor` for its self-verification of `rank: firm` (CYCLE.md:37, 48) and the `.claude/agents/lifter.md` cross-file whole-book-grep guard (CYCLE.md:37, 56). Both are the relevant procedures for a within-theme/cross-file maturity re-anchor; uptake is surfaced.

### Issues found

None. All eight checks pass.

Cross-file residue claim verified (not an issue — confirms the report's judgment): `book/src/L4/domain_energy_reduce.md:377` reads `[matrix-weighted-norm](../L1/matrix-weighted-norm.md) (rough-in (test-coverage-bounded) — the ½⟨field, M field⟩ energy-form half)`. This IS a genuinely-stale assertion of the operator's OWN maturity, falsified by the c091 firm-flip, and D5 correctly flagged it for a batch-31 follow-up rather than silently editing it (correctly out of D5's one-theme scope per the lifter one-theme-per-invocation discipline; CYCLE.md:56-57). The two further out-of-scope residues the report notes — `goal-flow.md:218` (partitioned to the batch-30 meta-phase) and the `L2/index.md:112,121` `normalize_B`-gate borderline (judged non-stale-in-claim) — are appropriately routed/noted, not introduced as defects here.
