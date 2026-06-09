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

**Carve-out (the files that ARE the process record): `methodology/` GENERALLY + `meta-reviews/*`** (batch-50 codification of OQ `af-scan-de-carveout-widen-methodology-general`). The earlier `methodology/goal-flow`-only carve-out was too narrow — `methodology/resolution-ladder.md` + `methodology/graded-stack-scheme.md` carry legitimate, deliberately-kept worked-example cycle/date refs, and those pages ARE methodology process records (like `goal-flow.md`). The A–F scan greps (below) carve out `meta-reviews|methodology/` so the completion gate does not false-positive on them. A `methodology/` page is NOT a de-bulk target; it is the standing exception, exactly like `meta-reviews/*`.

## `## Context` is NOT an F-target — orientation vs. slice-era process narrative (batch-50 codification of OQ `f-class-context-heading-orientation-vs-process-narrative`)

**The F-class completion grep MUST EXCLUDE `## Context`.** The skill's actual F-grep (`^## (Origin|Working Notes|Critic'?s role)`) already excludes it and is correct — but be explicit, because the c151 dispatch prompt's prose F-definition once over-listed `## Context` and over-captured by **121 files**:

- **On per-operator / per-theme chapters (the ~121 files): `## Context` is a KEEP** — it is the *orientation* section (what the operator/theme IS, its layer, cross-layer relationships, evidence base, live citations). It is the legitimate analog of the finalization "what each component IS" surface. Verified batch-50: of the 121 `## Context`-only files, **0** carried any retired-infra reference / cycle-tag / forward-process-speculation marker. **Do NOT strip these.**
- **On slice-era CONCEPT pages (`concepts/<slug>.md`): `## Context` IS a de-bulk target** (batch-50 adjudication, ratified at the meta-phase; the `rotation.md` c151 pilot + `variant-absorption.md` c153 precedents). A concept page's `## Context` is slice-era process framing (dated extraction narrative, `Cycle-N` back-push bullets, retired-`prompts/` references). De-bulk it the same way: **KEEP** the orientation definition + methodology classification + the `## Context` heading itself; **STRIP** the dated extraction narrative / cycle-attribution bullets / retired-infra paragraphs; **LIFT** any buried coupling fact (e.g. "relationship to rotation") to an explicit `## Relationship` section.

The one-line per-file rule: `## Context` on an **operator/theme chapter = orientation (KEEP)**; `## Context` on a **slice-era concept page = process narrative (STRIP its process content, keep the orientation + heading)`. Carry this distinction in every de-bulk dispatch scope.

## Date-LESS `meta-review #N` refs — an E-class SUB-CLASS the dated grep misses (batch-50; friction `completeness-claim-vs-comprehensive-scan`)

The E-grep keys on a `2026-0X-XX` date, so it MISSES date-less process refs like "Codified meta-review #1; expanded … meta-review #2" / "levels-of-absorption refinement meta-review #3" (found batch-50 in `concepts/dependency-map.md:92-93`). These are the same E-class (process accounting of *when/how we decided*, woven into static prose). **Default: rephrase to drop the `meta-review #N` clause, keep the structural fact** — "Codified meta-review #1; expanded with carry-through clause meta-review #2" → drop entirely (the carry-through clause is already documented in `rotation.md` itself). The standing A–F scan E-grep now includes a `meta-review #[0-9]` arm (see below) so this sub-class is caught book-wide, not only by a comprehensive prose read.

## Concept-page + layer-index `## Origin` / `## Working Notes` / `## Critic's role` narrative — STRIP (NOT a carve-out) (meta-150 adjudication)

The batch-49 c149 D5 producer DELIBERATELY left, and flagged for adjudication (OQ `concept-page-context-origin-working-notes-narrative-debulk-scope`), the slice-era process-record sections on `concepts/<slug>.md` pages + the layer/lowering `index.md` cohort: `## Origin` ("Codified during the 2026-05-24 meta-review …"), `## Working Notes` ("Future meta-reviews should look for …", "Watch the next 3 cycles"), `## Critic's role` (references the DELETED `prompts/critic.md` / `lessons.md` / `episodic.jsonl`). **Meta-150 verdict: these are PROCESS FRAMING, not semantic content → they ARE de-bulk targets, NOT a methodology carve-out.** The `methodology/` + `meta-reviews/*` carve-out exists because those files ARE the process record; a *concept page* and a *layer index* state what the concept/layer IS, not its slice-era methodological origin or forward-process speculation. This makes the existing Scope sentence concrete: "do not de-bulk `concepts/` *content*" means the **semantic definition** (what the concept IS — the criteria, the canonical examples, the shape facts), NOT these process-framed sections.

**The discipline (this is a MIXED, coupling-lift-aware de-bulk — per-file judgment, NOT a mechanical section delete):**
- **STRIP** the pure-process content of `## Origin` / `## Working Notes` / `## Critic's role`: meta-review-enactment narrative, `cycle-N` attributions, references to retired infrastructure (`prompts/`, `lessons.md`, `episodic.jsonl`, the Synthesizer/Critic role names), forward-process speculation ("future meta-reviews should …", "watch the next N cycles", "if genuine rotations are being rejected, soften …").
- **LIFT** any coupling/semantic fact buried in those sections to an explicit static component — e.g. variant-absorption's `## Working Notes` bullet "This concept's relationship to `rotation.md`: …" becomes a `## Relationship to rotation` section (the coupling is real spec content; only its process framing is stripped). A parenthetical-dated section header like `## Structurally-distinct variants … (Added 2026-05-25 meta-review #11 after cycle 40 …)` KEEPS the section (it is load-bearing semantic content) and drops the date-tag header parenthetical.
- **PRESERVE** the no-frontmatter-rank `index.md` files' SOLE-rank-carrier dep-map status tokens + every citation/link exactly (the L1-index pass model: 136→136 citations, 57→57 tokens, baseline held). The `## Working Notes` on a layer `index.md` often carries LOAD-BEARING structural prose (fold-cohort boundaries, kernel/driver pairs, gate-floor enumerations) — that is semantic content to KEEP (optionally re-homed to a non-process-framed heading); only the slice-era cohort-growth-log / deleted-section-history narrative is stripped.

This is a careful **pilot-first multi-file campaign** (`priorities.md` batch-50 item-1a), not a blanket sweep: one `layer-intro-author` de-bulk dispatch per affected file, with the coupling-lift judgment applied per section.

## Directive-date provenance (E-class: "per the 2026-MM-DD redirect") — MIXED, rephrase-to-drop-the-date by default (meta-150)

A `2026-MM-DD` directive-date woven into "why this structure is shaped this way" prose is process framing of a fact that is itself static. **Default: rephrase to drop the date, keep the structural fact.** "Per the 2026-06-01 vocabulary-shift redirect, this degenerate edge is recorded in-line" → "This degenerate identity-in-named-terms edge is recorded in-line (the vocabulary does not shift across it, so there is no translation to narrate)." **KEEP the date only in a genuine governing-directive HEADER blockquote** whose job IS to record the directive that governs the file's active-management discipline — e.g. `semantics/index.md`'s `> **⟢ SEMANTIC-CONSOLIDATION DIRECTIVE (user directive 2026-06-06).**` header and the `methodology/` discipline pages (which are carve-outs anyway). When unsure whether a date is load-bearing: it is load-bearing iff deleting it changes *what the reader must do / how the surface is governed*, not merely *when we decided it*.

## The A–F residue-class scan (the comprehensive completeness gate)

A FINALIZATION de-bulk campaign declaring a residue class "complete" must show a **clean book-wide grep for that class**, not a self-characterized cohort tally (friction `completeness-claim-vs-comprehensive-scan`). The standing per-batch maintenance-floor hygiene sweep runs the full A–F scan:
- **A** `grep -rlE '^## Verified-against' book/src` → 0
- **B** `grep -rlE '^verified_against:' book/src` → 0
- **C** `grep -rlE 'reports/[0-9]' book/src | grep -v meta-reviews` → 0
- **D** `grep -rlE 'cycle-[0-9]+|\bc[0-9]{2,3}\b|batch-[0-9]+|wave-[0-9]' book/src | grep -vE 'meta-reviews|methodology/'` → 0 (carve-out: `methodology/` GENERALLY + `meta-reviews/`)
- **E** `grep -rlE '2026-0[0-9]-[0-9]{2}|meta-review #[0-9]' book/src | grep -vE 'meta-reviews|methodology/'` → only the 2 KEEP governing-directive headers (`semantics/index.md` SEMANTIC-CONSOLIDATION header + `SUMMARY.md`) remain. **The `meta-review #[0-9]` arm (batch-50) catches the date-LESS E-sub-class the date grep misses.**
- **F** `grep -rlE "^## (Origin|Working Notes|Critic'?s role)" book/src | grep -vE 'meta-reviews|methodology/'` → 0 (Context is NOT an F-target — see the `## Context` distinction above)
