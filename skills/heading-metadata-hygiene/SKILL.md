---
name: heading-metadata-hygiene
description: Move metadata/verbose tails OUT of section & chapter headings into a structured line below the heading, for TOC readability. Preserve anchors, never touch ## Status rank-carriers.
---

# heading-metadata-hygiene

**Provenance:** USER DIRECTIVE 2026-06-08 (batch-47 finalization, follow-on to `finalization-debulk`). Section & chapter titles embed metadata/verbose glosses that bloat the rendered chapter-TOC / on-page heading views. Move the metadata to a **structured line below the title**; keep the heading a clean noun phrase. Goal = **TOC readability** — let that goal arbitrate every judgment call.

Scope: `book/src/**` headings (`#` chapter H1 + `##`/`###`/`####` section headings) **and** `book/src/SUMMARY.md` sidebar link texts.

## The transform

For a heading `## Title — <tail>` or `## Title (<metadata>)`:

1. **Status / classification / provenance metadata in the tail** → relocate to a **bold label line immediately below** the heading (blank line between):
   ```
   ## Title

   **Status:** <rank/status token>
   **Kind:** <classification>
   ```
   - Rank/status tokens (`firm`, `rough-in`, `roadmap_goal`, `obstruction (opaque-library-ownership)`, `partial-obstruction`, `kernel-api`, `kernel-impl`, `NO claims`, `rank-N`) → `**Status:**`.
   - A structural classification ("additive-Schwarz decomposition-abstraction", "output-product column", "in-theme sub-note") → `**Kind:**`.
   - **PURE PROCESS metadata** that is redundant with frontmatter or is graded-stack bookkeeping — `(resolves cycle-7 / cycle-9 friction)`, `(reachability — why this is firm and not garbage)`, `(substantive)`, `(rank = min(endpoints) …)`, `DIRECTIVE-N`/`RE-N` refs — **DELETE it from the heading; do NOT relocate** (it is `finalization-debulk` process accounting; the rank lives in frontmatter / `## Status`).

2. **Descriptive gloss in the tail** (a real content descriptor, e.g. `— the no-extras sugar`, `— free-function real-real`, `— the global lift (no obstruction)`):
   - **SHORT (≤ ~3 words) AND distinguishes the heading from sibling headings** (the `Sub-pattern A/B/C — …`, `MGS/CGS — …` case): **KEEP it in the heading** — it is what makes the TOC navigable. Stripping it to identical `Sub-pattern A / Sub-pattern B` siblings HURTS readability (the opposite of the goal).
   - **LONG / a clause (> ~25 chars, or parenthetical sub-clauses)**: move the verbose descriptor to a plain line below, keeping the heading to its core noun phrase:
     ```
     ## Title

     <the descriptor sentence.>
     ```
     (Use a `**Label:**` prefix only if a natural key exists; otherwise a plain line.)

3. **Chapter H1**: a slug-name H1 (`# libceed-quadrature-kernel-impl`, `# fe-assemble-libceed-boundary-obstruction`) is the chapter NAME, not metadata — **leave it**. Only relocate a genuine metadata/gloss tail on an H1.

## SUMMARY.md sidebar

Shorten long left-sidebar link texts (the "chapter TOC"):
- `[2026-05-26 — twenty-first meta-review (cycles 104–115) — refinement fires, …]` → `[Meta-review 21 (cycles 104–115)]`
- `[Library — coordination (outer-driver caps & coordination combinators)]` → `[Library — coordination]`
- Keep the link TARGET unchanged; only shorten the bracketed text.

## SAFETY (mandatory)

- **NEVER touch a `## Status` heading or its first-line rank token.** It is the graded-stack linter's rank carrier — renaming/moving it breaks the baseline. Skip all `## Status` sections entirely.
- **ANCHOR SAFETY (load-bearing).** mdBook auto-generates each heading's anchor by slugifying its text. Changing a heading changes its anchor → any in-page link `](…#old-anchor)` breaks. Before changing a heading, **grep the whole book** for links to its old slug-anchor (`grep -rn '#<old-slug>'`). If any exist, **update those link sites** to the new anchor in the SAME change. The build (`cargo make book`, linkcheck) is the backstop — a broken anchor surfaces there.
- **Do NOT touch** frontmatter, citations, `## Evidence`, code fences, or the body prose other than inserting the relocated metadata line.
- **Preserve KaTeX `$`-fence rules** (don't move a `$S` token out of a fence).
- Build must stay EXIT 0.

## Judgment

The goal is TOC readability, not mechanical em-dash removal. A heading should read as a clean, distinguishable title; its status/classification belongs in a structured line below; a short distinguishing gloss stays. When unsure whether a tail is "metadata" or "a needed descriptor", ask: *does keeping it help someone scanning the TOC, or just clutter it?*
