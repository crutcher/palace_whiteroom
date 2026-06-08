---
name: finalization-debulk
description: De-bulk process/judgment accounting out of a book/src chapter toward a static-state finalized surface, preserving all spec content + citations, lifting coupling concepts to explicit components.
---

# finalization-debulk

**Provenance:** USER DIRECTIVE 2026-06-08 (batch-47 finalization campaign; memory `project_finalization_debulk_directive`). Exemplar: `book/src/L4/krylov-step.md` (the pilot — −11% words, zero spec/citation loss).

The artifact is being finalized from a *process-accounting* surface into a *static-state* surface. A reader of the finished book should see **what each component IS**, not the cycle-by-cycle history of how it got there. This skill de-bulks ONE chapter.

## STRIP — process/judgment accounting (move OUT)

1. **`## Status` promotion-history prose.** For a `rank:`/`firmness:` frontmatter entry, delete the `## Status` section entirely — firmness lives in frontmatter. For a non-firm entry (`rough-in`/`roadmap_goal`/`stub`/`obstruction`/`partly-constructive`/`partial-obstruction`), KEEP a concise **static** statement of what is unresolved + the promotion condition, but strip the cycle-by-cycle history and the "promoted cycle-NNN" narrative. (The obstruction sub-kind tag and a roadmap_goal's declared-deps are static state — keep.)
   - **⚠ NO-FRONTMATTER-RANK files (load-bearing — check FIRST):** if the file has **NO YAML frontmatter `rank:`/`firmness:`** (it starts with `# Title`, not `---`), then its prose `## Status` leading token (`` `firm` `` / `` `rough-in` `` / etc., the first non-empty line after `## Status`) is the **SOLE rank carrier the graded-stack linter reads** — deleting it re-types the node to untyped and breaks the baseline. For these files, **do NOT delete the `## Status` section**: replace it with a CONCISE static one-line token — `` `firm` `` (or the exact HEAD sub-rank token) + a short static clause — stripping only the cycle-history/audit narrative. Verify the leading token survives as the first non-empty line after `## Status`.
2. **Inline `cycle-NNN` / `cNNN` attributions.** "per the cycle-005 cross-cutter report", "the cycle-006 wave-2 abstractor dispatch is auditing", "promoted cycle-010 per the … directive", "(cycle-005 firm)" tags. Delete the attribution; keep the underlying static claim.
3. **Forward-process speculation.** "an L3 row will follow in cycle-007", "this is the rotation the abstractor is auditing", "pending the cycle-NNN pass". Delete — state only what IS true now.
4. **Lifting / deletion / corpus narrative.** "lifted into firm … per the cycle-009 corpus reduction", "previously rendered in the now-deleted Phase-1 slice gmres.md:459-471, deleted cycle-099 graded-stack P2; git history is the record", "absorbed here in cycle-099 so the slice is clear-to-delete", "(original pre-reduction range: …)". Delete the history; keep the live citation it resolved to.
5. **`verified_against:` frontmatter yaml blocks** + "§Verified-against" audit pointers. Delete (audit trail is in git history / scaffolding).
6. **`reports/…` pointers.** "Cross-cutter motivating report: reports/2026-…/CYCLE.md", "(per reports/…)", "updated by repairer from the original placeholder …". Delete.
7. **Process-narrative clutter in frontmatter edge `kind:` comments.** Trim citation-line lists (`§Semantics :142,:145`) and cycle-tags to a concise semantic label. Keep the edge, the `kind:`, and a short what-it-means comment.
8. **Hedged process-judgment language** where it is about OUR confidence rather than the math: "plausibly identity-in-form" → "identity-in-form" when a firm theme already settled it; drop "to forestall the misreading", "to prevent decoration drift" meta-asides where they are process notes (keep them only if they state a genuine static non-law/caveat).

## KEEP — static spec content (do NOT touch)

- **Every citation.** `path:start-end` source ranges and `[text](../layer/file.md)` cross-links are mandatory grounding — preserve verbatim. (You MAY drop a link that pointed only at a `reports/…` process artifact.)
- Frontmatter `layer`/`operator`/`rank`/`firmness`/`edges` (the typed dependency graph).
- `## Signature`, `## Semantics`, worked examples, `## Algebraic laws` (laws AND non-laws), shape contracts, record definitions.
- Genuine cross-layer prose ("Downward to L_{n-1}", "L4 vs L2 distinction") — these are coupling components; see LIFT.

## LIFT — coupling concepts become explicit components

Where a stripped process/judgment note **anchored a coupling concept** — "this can be compared to X", "this is the same pattern as Y", "relationship to <other component> is Z" — do NOT just delete it: make the coupling an **explicit chapter component**:
- a named section (`## Relationship to <X>` / `## L4 vs L2 distinction` — the pilot's model), or
- a typed `reference` edge + a one-line static statement, or
- (if it recurs across ≥2 chapters) flag it for a `concepts/<slug>.md` page in Open questions.

The coupling is real spec content; only its *process framing* ("the cross-cutter noticed that…") is stripped.

## SAFETY (mandatory)

- **No citation may be lost.** Before/after, the set of `palace/…:N-M` source citations and `book/`-internal `[..](..)` links must be unchanged EXCEPT links that pointed only at `reports/…` or deleted-slice paths.
- **No `book/`-internal link may break.** Don't delete a chapter another chapter links to; don't turn a live link into prose that drops it.
- **No node/edge/rank/status MOVE.** De-bulk is prose + frontmatter-comment + `## Status`-section + `verified_against`-block editing only. The `rank:`/`firmness:`/`edges:` graph is unchanged → the graded-stack linter baseline must HOLD EXACTLY.
- **KaTeX `$`-sigil fence rule** still applies: a `$S`/`$N` token in a 4-space-indented block must be inside a ```text fence.
- Build must stay EXIT 0 (`cargo make book`).

## Scope

`book/src/**` ONLY. `scaffolding/` stays the process workshop (untouched). Do not de-bulk `concepts/` semantic definitions of their *content* — only their process framing.
