# verify-slug-rename-completeness

**Promoted:** cycle-045 meta-phase (batch-13). **Proposer:** critic (cycle-043 lifter-consolidated-sweep verification). **Friction-ledger:** none opened (the procedure is captured here; the c043 sweep landed clean — this skill crystallizes the repeatable verification so the next multi-file rename does not hand-roll it).

**Audience:** producer (lifter / harvester / abstractor) who emits a multi-file slug rename in a proposed-changes block; AND the critic verifying cross-reference-integrity before clearing the report; AND the integrator-per-report re-confirming at apply time.

## Motivating observation

A slug rename across the artifact is the genuinely-fragile multi-file operation: the load-bearing risk is a **dangling old-slug path-link surviving the apply as a `linkcheck2` hard build break** (exit 101, `File not found`). The cycle-043 D1 consolidated sweep renamed three theme slugs — `nrm2-fold-specialization`→`nrm2-leaf-identity`, `scal-fold-specialization`→`scal-leaf-identity`, `elementwise_product-body-identity`→`elementwise-product-body-identity` — across ~15 files / ~36 occurrences. The lifter hand-rolled a grep inventory; the critic then had to independently re-run `grep -rn` for all three old slugs and map every occurrence to a report edit to clear cross-reference-integrity, **distinguishing path-based links (build-fragile if missed) from prose slug-mentions (soft)** AND **confirming the three same-suffix-but-NOT-renamed sibling themes** (`inner-product-fold-specialization` / `linear-combination-fold-specialization` / `gram-fold-specialization`) were neither swept by accident (substring collision on `-fold-specialization`) nor left referencing a renamed target. This grep → map → confirm-zero-residual procedure is repeatable and error-prone enough to crystallize.

This is the rename-*completeness* companion to `audit-slug-meaning-before-coordinated-cross-report-rename` (which gates the rename *premise* — is the rename even correct?). This skill assumes the rename is correct and verifies it is *complete and collision-free*.

## Procedure (producer emits + critic re-runs independently)

For each `git mv old.md new.md` slug rename in the sweep:

1. **Inventory the COMPLETE occurrence set.** `grep -rn '<old-slug>' book/src/` — capture every hit. Do this per old-slug (not a combined regex; substring collisions hide otherwise).
2. **Partition by reference kind.** Split the occurrences into:
   - **path-links** — `](...<old-slug>.md)` or a `lowers_to:` / dep-map href pointing at the renamed file. **Build-fragile**: each MUST become the new path or the build breaks.
   - **bare slug-mentions** — prose / status / provenance text naming the slug. Soft (no build break) but should still be rewritten for consistency, EXCEPT intentional `renamed-from <old-slug>` provenance prose (which is the historical record — keep it).
3. **Map every path-link + consistency-mention to a report edit.** Each path-link occurrence maps to a `[old]`/`[new]` edit in the proposed-changes block (or to the `git mv` itself for the file's own H1 / §Slug). Confirm none is unaccounted.
4. **Substring-collision guard — enumerate the same-suffix siblings that are NOT being renamed.** A rename of `<stem>-<suffix>` can accidentally rewrite a sibling `<other-stem>-<suffix>` (the c043 case: `-fold-specialization` is shared by `nrm2`/`scal` (renamed) AND `inner-product`/`linear-combination`/`gram` (NOT renamed)). Explicitly list the not-renamed siblings; confirm (a) none is accidentally rewritten by an over-broad edit, and (b) none references the renamed target via a now-stale path.
5. **Assert zero residual.** Post-apply (or as a pre-emit dry-run on the proposed edits): `grep -rn '<old-slug>' book/src/` returns zero hits **modulo** the not-renamed siblings (step 4) and intentional `renamed-from` provenance prose (step 2). The producer pastes the inventory + this zero-residual assertion in the report; the critic re-runs the grep independently and re-maps before clearing cross-reference-integrity; the integrator re-confirms zero-residual at apply time.

## Boundary

- This skill is about **completeness + collision-safety** of an already-decided rename. Whether the rename should happen at all (premise correctness) is `audit-slug-meaning-before-coordinated-cross-report-rename`.
- Scaffolding files (`scaffolding/priorities.md`, `roadmap.md`) and append-only historical records (`cycle-record.jsonl`, `integrator-signals.md`) are OUT of the `book/src/` build scope: the build cannot break on them, so they are not part of the zero-residual assertion. The active-plan slug refresh in `priorities.md`/`roadmap.md` is meta-phase territory; append-only historical mentions are left as the record.
- The mechanical `tools/citecheck/citecheck.py --scan` pass complements this (it catches dead path-links generally); this skill adds the rename-specific substring-collision + not-renamed-sibling guard the scanner does not encode.
