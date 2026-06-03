---
agent: lifter
invoked_at: 2026-06-03T205952Z
scope: feature/eigenmode.L4 stale-maturity-clause hygiene — eigenfreq_qfactor_reduce rough-in→firm sync
status: pending
integrated_at: 2026-06-03T212210Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-083 (batch-26 pos 2/3). Applied clean (D2, HYGIENE). eigenmode.L4.md 2 prose edits syncing the stale (its eigenfreq_qfactor_reduce verb is rough-in) clause to firm (c082) + an editorial-precision §Status touch; ZERO status/count change, column stays seed; no new OQ (folds into the c082-opened eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column); no promotion-rule re-authoring (pending batch-26 meta-phase). retroactive-budget 0; build exit 0."
inputs:
  - book/src/feature/eigenmode.L4.md
  - book/src/L4/eigenfreq_qfactor_reduce.md (firmness: firm; ## Status firm — c082 promotion)
  - book/src/feature/eigenfrequency-qfactor.L4.md (status: seed — the c081/c082 parallel-cleanup precedent)
  - scaffolding/open-questions.md:1056-1057 (the c082 verb-firming + the NEW seed-deadlock OQ)
---

# CYCLE: Re-anchor eigenmode.L4 stale maturity clause

## Summary
A LOW/hygiene pure-rewriting pass on `book/src/feature/eigenmode.L4.md`. Cycle-082 (D2 lowering-verifier law-confidence pass) promoted the L4 verb `eigenfreq_qfactor_reduce` from `rough-in (test-coverage-bounded)` to **`firm`** (firm-on-positive-structure / syntactic-identity escape; `book/src/L4/eigenfreq_qfactor_reduce.md:4` frontmatter `firmness: firm`, `:185` `## Status: firm`). The eigenmode driver column's prose at `:55` still describes that verb as `rough-in`, a now-stale maturity claim. This pass syncs the wording: the verb is firm; the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column it reduces into is **still `seed`** — but for a DIFFERENT reason than the (now-discharged) verb gate: that column stays seed because its OTHER constituent (the eigenmode driver column itself) is seed, the reciprocal cross-link recorded in OQ `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column` (open-questions.md:1057). No `status:` token changes (eigenmode.L4 stays `seed`); no promotion-rule re-authoring (PENDING batch-26 meta-phase, out of scope). The `:74` §Status block was checked and is NOT stale (it says the eigenfrequency-qfactor column is "itself `seed`", which remains true) — only one editorial precision touch there to align with the verb-firm fact, kept minimal.

## On-disk verification performed
- `book/src/L4/eigenfreq_qfactor_reduce.md:4` — frontmatter `firmness: firm` (confirmed on-disk this dispatch).
- `book/src/L4/eigenfreq_qfactor_reduce.md:185` — `## Status` body opens `` `firm`. `` (confirmed).
- `book/src/feature/eigenfrequency-qfactor.L4.md:5` — `status: seed` (the output-product column it reduces into; still seed — confirmed).
- `book/src/feature/eigenfrequency-qfactor.L4.md:55,68` — the c081/c082 parallel cleanup already narrates: verb is now **firm**, column STAYS `seed` because the OTHER constituent (the `eigenmode.L4` driver column) is itself seed. This is the precedent narration I mirror.
- `scaffolding/open-questions.md:1056` — verb-firming OQ CLOSED-RESOLVED-BY-AUDIT (c082); `:1057` — NEW `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column` (the reciprocal seed-deadlock).
- Stale loci in target: `:55` (the `(its eigenfreq_qfactor_reduce verb is rough-in)` parenthetical — the one definite staleness) and `:74` (§Status duplicate block — checked, says only "itself `seed`", not stale; one editorial-precision touch).

No NEW pinpoint citations are introduced by this hygiene pass (only maturity words change + a grammatical re-phrase of the surrounding deadlock clause), so the `--anchor` drift check has no new `path:lo-hi` to validate. The existing L0 anchors in the surrounding prose are untouched.

## Proposed changes

```edit:book/src/feature/eigenmode.L4.md
[old]: The whole feature therefore lowers cleanly outward to the L4 backend surface: `eigenmode = map readout ∘ eigsolve ∘ eig_pencil ∘ (fe_assemble ×3)`. Both composed combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm** — so the only thing keeping this column at `seed` (rather than promoting past it) is the readout stage's reduction into the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column, which is itself `seed` (its `eigenfreq_qfactor_reduce` verb is `rough-in`). This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: it advances cleanly because the constituent vocabulary is firm and composes without forcing the spine.
[new]: The whole feature therefore lowers cleanly outward to the L4 backend surface: `eigenmode = map readout ∘ eigsolve ∘ eig_pencil ∘ (fe_assemble ×3)`. Both composed combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm** — so the only thing keeping this column at `seed` (rather than promoting past it) is the readout stage's reduction into the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column, which is itself `seed`. (Its reduction verb `eigenfreq_qfactor_reduce` is now **firm** — promoted cycle-082; that column stays `seed` not on the verb but on the reciprocal cross-link to *this* driver column, which is itself `seed` — OQ `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column`.) This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: it advances cleanly because the constituent vocabulary is firm and composes without forcing the spine.
```

```edit:book/src/feature/eigenmode.L4.md
[old]: Stage (3) is a pure per-mode readout `map`; its reduction into the user-facing eigenfrequency/Q-factor product is owned by the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column (itself `seed`) — the one reason this column stays `seed` rather than promoting (the two solve-side constituents being firm).
[new]: Stage (3) is a pure per-mode readout `map`; its reduction into the user-facing eigenfrequency/Q-factor product is owned by the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column (itself `seed`, though its `eigenfreq_qfactor_reduce` reduction verb is now **firm** — cycle-082) — the one reason this column stays `seed` rather than promoting (the two solve-side constituents being firm).
```

## Discipline notes
- **Pure structural rewrite, no authorship.** The only content change is the maturity word: `eigenfreq_qfactor_reduce` is no longer `rough-in`, it is `firm` (verified on-disk `book/src/L4/eigenfreq_qfactor_reduce.md:4,185`). The surrounding clause is re-phrased only enough to stay grammatical and accurate: the `eigenfrequency-qfactor` column stays `seed` for a reason that is now the *reciprocal cross-link* (the eigenmode driver column being seed), NOT the (discharged) verb gate.
- **Bounded prose-correction (in scope per lifter §L0-evidence-driven prose correction).** The `:55` parenthetical "(its `eigenfreq_qfactor_reduce` verb is `rough-in`)" is a maturity claim contradicting the on-disk source (`book/src/L4/eigenfreq_qfactor_reduce.md` is `firm`). The fix is bounded (corrects a drifted maturity claim, does NOT re-architect the column's decomposition or the promotion rule) and evidenced (the on-disk verb file + OQ:1056-1057 read this dispatch). Recorded here per the discipline.
- **The `eigenfrequency-qfactor.L4` precedent.** The c081 D1 + c082 D2 passes already landed exactly this narration on the *output-product* side (`eigenfrequency-qfactor.L4.md:55,68`: verb now firm, column stays seed on the eigenmode-driver-column reciprocal). This eigenmode-driver-column edit is the mirror of that precedent on the *driver* side — the two columns are reciprocally cross-linked seed (the mutual-blocking deadlock the pending batch-26 directive will address).
- **Layer-definition discipline (high→low).** No directionality concern — this is L4 feature-column prose; no LHS/RHS rewrite direction is touched.
- **Status token unchanged.** `eigenmode.L4` frontmatter `status: seed` (`:5`) is NOT touched, and there is no index-table status cell to sync (the seed token is unchanged). The §Constituent down-links table cells at `:68-70` are also unaffected — they already read `firm`/`firm`/`seed (column)`, none of which references the verb maturity.

## Supporting evidence
- `book/src/L4/eigenfreq_qfactor_reduce.md:4` (`firmness: firm`), `:185` (`## Status: firm`) — the verb promotion this pass re-anchors to.
- `scaffolding/open-questions.md:1056` — `eigenfreq-qfactor-reduce-firm-needs-assembly-test` CLOSED-RESOLVED-BY-AUDIT (c082 D2 lowering-verifier; the verb firm-promotion record).
- `scaffolding/open-questions.md:1057` — NEW `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column` (the reciprocal seed-deadlock the corrected prose now cites).
- `book/src/feature/eigenfrequency-qfactor.L4.md:55,68` — the parallel-side precedent narration (verb firm / column stays seed on the reciprocal cross-link).

## Open questions / caveats
- **PENDING batch-26 meta-phase directive (out of scope, flagged not resolved).** The dispatch scope notes a USER DIRECTIVE to CHANGE the feature-column promotion rule (break the mutual-blocking seed deadlock between `eigenmode.L4` and `eigenfrequency-qfactor.L4`) is pending the batch-26 meta-phase. This pass deliberately narrates the deadlock against the CURRENT rule ("a column may promote past `seed` only once ALL constituents are firm" ⇒ the two columns mutually block). If the batch-26 directive lands and changes that rule, BOTH `:55` and `:74` clauses (and the `eigenfrequency-qfactor.L4.md:55,68` mirror) will need a follow-up re-narration to the amended rule — that re-narration is NOT done here. Folds into OQ `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column` (open-questions.md:1057).
- No abstractor reread is required — the firmed verb's signature did not change shape; only its maturity word did, which is a pure-rewrite sync.
