---
agent: lifter
invoked_at: 2026-05-28T214020Z
scope: L4>L3 theme re-anchor — chebyshev L4 entry residual forM_/foldM prose cleanup (surgical 3-site vocabulary refresh)
status: integrated
integrated_at: 2026-05-28T221238Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-016 (per-report position 6). Surgical 3-site descriptive-prose vocabulary refresh in firm L4/chebyshev.md (forM_/foldM → iterate_while_pure); 4 intentional historical-narrative occurrences left verbatim. Status stays firm (no semantics/structure/status change). OQ l4-chebyshev-residual-formm-foldm-prose-cleanup resolved (ledger:2834). Retroactive-budget 0. Book build clean (exit 0)."
inputs:
  - book/src/L4/chebyshev.md
  - book/src/L3/chebyshev.md (read-only — sibling re-anchor confirmation)
  - book/src/L4/iterate-while.md (canonical combinator naming, read transitively via chebyshev.md re-anchor blocks)
  - scaffolding/open-questions.md:2832-2843 (OQ l4-chebyshev-residual-formm-foldm-prose-cleanup)
---

# CYCLE: Re-anchor chebyshev (L4) — residual forM_/foldM prose cleanup

## Summary
Cycle-015 promoted `book/src/L4/chebyshev.md` from `rough-in` to `firm`, re-anchoring the `apply` body's two sequential obstructions from un-anchored `forM_` (outer `pc_it` sweep) / `foldM` (inner `k`-recurrence) binds onto nested [`iterate_while_pure`](./iterate-while.md) folds with **step-count predicates** (cycle-014 combinator-miner route (i): REUSE the firm `iterate-while` family). That re-anchor was scoped precisely to the body + §Status + dep-map row + directly-affected prose, leaving **three** descriptive prose mentions of the now-superseded `forM_`/`foldM` vocabulary untouched. This dispatch is a pure vocabulary-refresh pass over those three sites — no semantics change, no structural change. The three sites are L4-entry-local descriptions of the entry's OWN rendering of its obstructions, so each refreshes to the canonical `iterate_while_pure`. The intentional historical-narrative `forM_`/`foldM` strings in §Status (the "the obstructions WERE rendered as un-anchored forM_/foldM" reconcile narrative, lines 497/498/507) and §Evidence Provenance (the "slice's forM_/foldM rendering is superseded here" supersession note, line 581) are left verbatim — they document the supersession and must name the old vocabulary. Closes OQ `l4-chebyshev-residual-formm-foldm-prose-cleanup`.

## Proposed changes

```edit:book/src/L4/chebyshev.md
[old]:   discarded on return). The slice's four-way refinement (adding the
  scalar-recurrence stratum `S` threaded by `foldM`) is the worked example this
  entry instantiates.
[new]:   discarded on return). The slice's four-way refinement (adding the
  scalar-recurrence stratum `S` threaded through the inner `iterate_while_pure`
  carry) is the worked example this entry instantiates.
```

```edit:book/src/L4/chebyshev.md
[old]: - [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the
  classification surfacing as `forM_` (outer) and `foldM` (inner) binds.
[new]: - [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the
  classification surfacing as the two nested `iterate_while_pure` folds (outer
  `pc_it` sweep, inner `k`-recurrence) with step-count predicates.
```

```edit:book/src/L4/chebyshev.md
[old]: - `book/src/L3/chebyshev.md` (this cycle) — the value-threaded L3 form this L4
  entry lifts from; the partial-obstruction verdict (body lifts, loops do not)
  this entry's `forM_`/`foldM` binds inherit.
[new]: - `book/src/L3/chebyshev.md` (this cycle) — the value-threaded L3 form this L4
  entry lifts from; the partial-obstruction verdict (body lifts, loops do not)
  this entry's two `iterate_while_pure` folds inherit.
```

## Discipline notes
- **Pure rewriting, not authorship.** Structure, narrative, and direction (high→low: L4 LHS `iterate_while_pure` folds, L3 RHS `iterate_while_pure_L3` tail recursions) are all unchanged. Only the combinator-name vocabulary is refreshed to match the cycle-015 body re-anchor. No LHS/RHS shape change — the firmed-up `iterate_while_pure` signature was already enacted in the body during cycle-015; this pass only propagates the vocabulary into the three lagging prose descriptions.
- **Scope held to the 3 named sites.** I grepped all 7 `forM_`/`foldM` occurrences (7 lines: 368, 382, 497, 498, 507, 547, 581). Four occurrences (lines 497/498/507 in §Status "Wrapper-iteration-vocabulary reconcile"; line 581 in §Evidence Provenance) are **intentional historical-narrative** strings that describe what the obstructions WERE rendered as before the re-anchor / that the slice's rendering IS superseded. Those name the old vocabulary on purpose and are left verbatim, consistent with the OQ's explicit instruction ("Distinct from the INTENTIONAL historical-narrative forM_/foldM strings ... those stay"). Only the three descriptive-prose sites (368, 382, 547) are refreshed.
- **Naming matched to the canonical re-anchor blocks.** The cycle-015 body consistently calls the two obstructions "the two `iterate_while_pure` folds" (lines 44, 191, 334, 372, 487-488, 523-524), distinguishes them as outer `pc_it` sweep / inner `k`-recurrence (lines 249, 255, 524), and ties them to **step-count predicates** (`s.it <= op.pc_it`, `c.k <= op.order - 1`). My three replacements adopt exactly that phrasing:
  - Site 1 (state-stratification): `S` is threaded through the inner fold's value-carry — matches §Semantics body (lines 176/182/185: `st` rides the `{ r, d, st, k }` carry) and §"Sequential obstructions" (lines 262-264: "the 1st-kind `ρ_k` scalar update rides inside the carry's `st` field").
  - Site 2 (sequential-obstruction): "two nested `iterate_while_pure` folds (outer `pc_it` sweep, inner `k`-recurrence) with step-count predicates" — matches the §Semantics framing (lines 139-140) and the §Status sharpening (lines 486-488).
  - Site 3 (Evidence L3 bullet): "this entry's two `iterate_while_pure` folds inherit [the partial-obstruction verdict]" — the inherit relationship is to the L3 verdict (unchanged); only the combinator name on the L4 side is refreshed.
- **No content-correction beyond vocabulary.** No convention was stated backwards, no citation drifted, no claim contradicted L0; this was a clean vocabulary-lag-only pass. No bounded prose-correction was needed or made.

## Supporting evidence
- Cycle-015 re-anchor (the promotion this pass propagates): `reports/2026-05-28T202138Z-lifter-chebyshev-l4-firm-via-iterate-while-reanchor/` (referenced in §Status line 477-478).
- Cycle-014 combinator-miner route (i) REUSE verdict (the decision the re-anchor enacts): `reports/2026-05-28T193256Z-combinator-miner-chebyshev-l4-wrapper-iteration-vocabulary-reconcile/` (referenced §Status line 502).
- Canonical combinator naming source (read transitively via the chebyshev.md body re-anchor blocks): `book/src/L4/iterate-while.md` (cycle-007 firm) — `iterate_while_pure` + step-count-predicate discipline (`:57,102,165`), `iterate_while_pure_L3` lowering image (`:193-195`); `iterate-while.md:7` names Chebyshev as a consumer.
- OQ being closed: `scaffolding/open-questions.md:2832-2843` (`l4-chebyshev-residual-formm-foldm-prose-cleanup`, opened cycle-015 by integrator-finalize).

## Citation self-verification (producer-emit, per verify-citation-range §Producer self-verification)
No new `path:lo-hi` source citations are emitted by this pass — it is a pure intra-file combinator-name swap in descriptive prose; the three edits introduce no new line-range citations and relocate no dangling pointers. The unchanged citations adjacent to the three sites (e.g. the §Evidence L3-chebyshev bullet's reference to `book/src/L3/chebyshev.md`) are not modified. I confirmed the three target line locations against the live file (lines 368, 382, 547) via Read after grep, and confirmed the four intentional-historical occurrences (497/498/507/581) are NOT touched.

## Open questions / caveats
- **The L3 sibling entry `book/src/L3/chebyshev.md` STILL uses `forM_`/`foldM` throughout** (confirmed via grep: 6 occurrences at lines 46, 55, 96, 237, 475, 479). This means site 3's "inherit" relationship points at an L3 entry whose own combinator vocabulary has not yet been re-anchored — but the L3 re-anchor is OUT OF MY DISPATCH SCOPE (one theme/entry per invocation; this dispatch is the L4 entry only). This is ALREADY TRACKED: the sibling OQ `l3-chebyshev-downward-prose-iterate-while-refresh` (referenced in the L4 OQ's `relates_to` field, `open-questions.md:2839`) is the cycle-016 follow-up for the L3-side refresh. No new OQ needed; flagging only to confirm the self-check surfaced it and that refreshing the L4 entry's OWN combinator name is correct regardless of the L3 entry's lagging state (the L4 site describes the L4 entry's rendering, not the L3 entry's). No abstractor reread is implicated — the firmed-up `iterate_while_pure` signature is fully consistent with the L4 entry's body; this is pure vocabulary lag, not a signature contradiction.
- No other caveats. The three edits are mechanical vocabulary swaps; the firm flip is unaffected (these are descriptive-prose sites, not body/status/law content, exactly as the OQ characterized).
