# audit-slug-meaning-before-coordinated-cross-report-rename

**Promoted:** cycle-027 meta-phase (batch-7). **Proposer:** repairer (cycle-027, repair of `2026-05-29T175529Z-abstractor-incremental-ls-composition-lowering`). **Friction-ledger:** `coordinated-cross-report-rename-premise-inversion`.

**Audience:** repairer (the gating audit before applying a coordinated rename); also a producer/integrator self-check when a slug collision forces a cross-report rename.

## Motivating observation

When two same-cycle dispatches collide on a slug, the orchestrator/integrator may hand the second dispatch's repairer a **coordinated cross-report rename** instruction (e.g. "dispatch-4 renamed its leaf `X` → `Y` to resolve a collision; in THIS report, rename every `X` that means the leaf → `Y`, but do NOT touch `X` references that mean the other operation"). The hazard is that the **dispatcher's premise about which references mean what can be inverted relative to the artifact**.

Concrete cycle-027 case: dispatch-4 harvested the terminal back-solve leaf and renamed it `ls_update_column` → `back_solve` (collision — `ls_update_column` was already bound to a *different* column-streaming operation `(K,j,h_new)→K'` in the L2 entry + concept page). The repairer was told "this theme forward-references the back-solve leaf as `ls_update_column`; rename those → `back_solve`." An exhaustive grep showed the **opposite**: in this theme *every* `ls_update_column` meant the column-streaming step (the CAUTION's protected meaning), NONE meant the back-solve leaf — and the back-solve target was referenced under a *different* slug (`trsv` / `back_solve`). So the literal rename target set was **empty** (the CAUTION protected exactly the references that existed), and the genuine consistency gap was the *inverse* (`trsv` back-solve-target vs the landed `back_solve` slug) — a cross-report content reclassification, not a mechanical rename. Blindly trusting the dispatch premise would have **corrupted** correct streaming-step references while leaving the real gap unfixed.

This is a generalization of the `verify-citation-range` discipline ("verify the claim against on-disk source, not the producer's paraphrase") applied to slug-rename coordination rather than citation ranges.

## Procedure (gate the rename before applying any edit)

1. **Read the LANDING report's ground truth, not the dispatch's paraphrase.** `grep -n '```new:' <landing-report>/CYCLE.md` to confirm which slug the landing report actually creates on-disk, and read its signature. Establish what `Y` (the rename target) really is and what operation it denotes — do not infer it from the rename instruction's wording.
2. **Enumerate + classify every occurrence of the old slug in the report under repair.** `grep -n '<old-slug>'` the report; for EACH occurrence, read the signature / surrounding prose and classify it by **the operation it denotes** — partition into (a) rename-target meaning (should become `Y`) vs (b) protected meaning (the colliding other operation, stays as-is). Denote-by-signature, not denote-by-position.
3. **Gate on premise contradiction.** Compare the partition against the dispatch's stated premise. If the partition **contradicts** the premise — e.g. zero occurrences fall in partition (a), or every occurrence falls under the CAUTION's protected meaning (b) — then the literal rename is a **no-op**: apply ZERO edits and record the rename as `not-needed` (with the per-occurrence classification as evidence). Do NOT apply a rename whose premise is inverted; that corrupts correct references.
4. **Assess whether a DIFFERENT slug carries the real gap.** After ruling out the literal rename, check whether the genuine consistency gap is elsewhere (a different slug is the true lowering/landing target — an overload disambiguation, not a 1:1 string swap). If so, this is a **content reclassification** beyond surgical-repair scope → mark `unrepairable` and route to the integrator / a follow-up dispatch, citing the landing report's own critic flag if it raised the same collision.
5. **Record the outcome explicitly** in the META repair section: the ground-truth read (step 1), the per-occurrence denote-by-signature partition (step 2), the no-op/contradiction verdict (step 3), and the routed real gap (step 4). `needs-revision` with one `unrepairable` cross-report finding is the correct disposition — it is not a defect in the report's own authoring, it is a cross-report reconciliation the integrator owns.

## Prevention (producer / planner side)

The collision was avoidable: the L2 entry already used BOTH colliding slugs with distinct meanings. Before a harvester/abstractor introduces a NEW slug, **grep the existing artifact vocabulary** (`book/src/**/*.md`, `concepts/`) for the candidate slug; if it already names a distinct operation, pick a non-colliding name up front. A pre-harvest slug-collision check is the cheapest place to stop this (see the cycle-027 meta-phase report's `ask` on whether to make it a standing producer-spec bullet).

## Why this is a distinct skill, not folded into `verify-citation-range`

`verify-citation-range` gates *line-number* claims against on-disk source. This skill gates *slug-rename* claims against the artifact's denote-by-signature meaning — a different object (a name's meaning across reports), a different hazard (an inverted rename corrupts correct references AND misses the real gap), and a different routing (no-op + reclassification→unrepairable, not a citation re-anchor). The shared root is "verify the coordination premise against the artifact, never assume the dispatcher's paraphrase."
