---
agent: layer-intro-author
invoked_at: 2026-06-06T201018Z
scope: cycle-116 D2 (WAVE-2) — semantic-consolidation restatement-cohort relocation sweep (Tier B + Tier C) + L4 bare-basename prose-ref cleanup
status: pending
integrated_at: 2026-06-06T210000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  cycle-116 finalize. VERIFY-NOT-REDO — the dispatch applied all edits directly in book/src;
  the per-report integrator verified the on-disk state. 24-file restatement-cohort relocation
  sweep (Tier B 5 + Tier C 19) completing the named-shape-groups general-rule consolidation
  (functional-unit entries now USE+LINK §1.2.1, do NOT RE-STATE) + 4-file L4 bare-basename
  prose-ref cleanup (l4_calculus.md:NNN -> index.md:NNN). Reachability/rank-NEUTRAL (no
  frontmatter touched). cargo make book EXIT 0. Graded-stack linter HELD. No new OQs; appended
  READY-TO-CLOSE resolution note to named-shape-groups-general-rule-restatement-cohort-extent
  (now FULLY SWEPT Tier A+B+C). Applied clean, no repair-phase warnings.
---

# CYCLE: named-shape-groups restatement-cohort relocation sweep (Tier B + Tier C) + l4_calculus.md basename cleanup

## Summary

Cycle-116 D2 (WAVE-2, depends on D1 which is DONE). Executes the
restatement-cohort relocation sweep that the SEMANTIC-CONSOLIDATION directive
(user, 2026-06-06) mandates: a semantic rule lives ONCE at the surface; the
"NOT rank-1" / "carries the same-shape contract" / migration-note general echoes
are RELOCATED out of functional-unit entries, leaving (i) the op's OWN concise
shape fact + (ii) the existing §1.2.1 (or §1.2.2) back-link to the surface at its
NEW path `../semantics/index.md` (D1 moved the surface there).

This is the DIRECTIVE-SUPERSEDED disposition of the c115-D3 open Tier-C judgment:
c115 D3 read Tier C as "below the bar (keep)"; the semantic-consolidation
directive supersedes that — the bare "(arbitrary, unknown rank — NOT rank-1)"
parenthetical IS a general-rule echo and is trimmed to the op's own "arbitrary,
unknown rank" admits-any-rank fact + the file's existing §1.2.1 back-link.

Also folds in D1's flagged caveat: 4 L4 files carried stale BARE-basename prose
refs `l4_calculus.md:NNN-MMM` (NOT full-path, so D1's grep missed them) —
rewritten to the new surface filename `index.md` (line ranges preserved verbatim,
content moved verbatim by D1).

This dispatch is MECHANICAL/SURGICAL prose trimming (per dispatch instruction):
edits performed directly in `book/src/` with a `cargo make book` EXIT-0 gate;
this CYCLE.md records exactly what was done for the integrator to verify (not
redo). Frontmatter (`edges:`/`rank:`) UNTOUCHED — reachability/rank-neutral.

## Edits performed (verified on disk)

### Tier B (5 files — dropped the residual general echo; KEPT the §1.2.1 link)

Pattern: `(arbitrary unknown rank — NOT rank-1; named shape groups per [`l4_calculus`](…) §1.2.1)`
→ `(arbitrary unknown rank; see [`l4_calculus`](…) §1.2.1)`. The §1.2.1 back-link
is the relocation target — KEPT; only the "NOT rank-1; named shape groups per"
general teaching dropped.

- `book/src/L2/nrm2.md:77` — `(NOT rank-1; named shape groups per …)` → `(see … §1.2.1)`.
- `book/src/L3/nrm2.md:59-60` — same.
- `book/src/L2-L1/linear-combination-fold-specialization.md:35` — `— NOT rank-1; named shape groups per …` → `; see … §1.2.1`.
- `book/src/L3/blas1-intro.md:20` — `(arbitrary, unknown rank — NOT rank-1; named shape groups per …)` → `(arbitrary, unknown rank; see … §1.2.1)`.
- `book/src/concepts/elementwise-product.md:9,18` — `:9` base-primitive line: `— NOT rank-1)` → `— see §Contract / [`l4_calculus`](…) §1.2.1)` (added a back-link, since `:9` previously had none on-line; the §Contract section carries the §1.2.1 home); `:18` Contract line: `(named shape groups per …)` → `(see … §1.2.1)` AND `(arbitrary, unknown rank — NOT rank-1)` → `(arbitrary, unknown rank)`.

### Tier C (19 files, 25 occurrences — trimmed the bare "NOT rank-1" parenthetical)

Pattern: `(arbitrary[,] unknown rank[ —][,] NOT rank-1)` → `(arbitrary[,] unknown rank)`.
Each Tier-C file already carries ≥1 §1.2.1 back-link in its shape-contract
preamble (verified: all 19 have a `semantics/index.md` link), so the trimmed
entry retains (ii) the back-link without adding one.

- `book/src/L2/axpy.md:43`
- `book/src/L2/axpby.md:45`
- `book/src/L2/axpbypcz.md:48`
- `book/src/L2/scal.md:43`
- `book/src/L2/dot.md:38`
- `book/src/L2/normalize.md:52`
- `book/src/L2/reciprocal.md:38,102` (2)
- `book/src/L2/elementwise_product.md:41,97` (2)
- `book/src/L2/inner_product.md:166`
- `book/src/L2/gram.md:56` (`, NOT rank-1-pinned —` → ` —`)
- `book/src/L3/dot.md:49`
- `book/src/L3/inner_product.md:114`
- `book/src/L3/normalize.md:23,42` (2)
- `book/src/L3/reciprocal.md:21,40` (2)
- `book/src/L3/elementwise_product.md:41`
- `book/src/L4/dot.md:56,85` (2)
- `book/src/L4/inner_product.md:20,101` (2)
- `book/src/L4/nrm2.md:78`
- `book/src/L4/sparameter_reduce.md:100`

### L4 bare-basename prose-ref cleanup (4 files, 14 occurrences)

Stale inline-code citations `l4_calculus.md:NNN-MMM` rewritten to `index.md:NNN-MMM`
(the surface's new filename; D1 moved the content verbatim so the line ranges are
unchanged). These are non-breaking inline-code (not markdown links), but now
stale; rewritten for accuracy.

- `book/src/L4/iterate-while.md` — 10 occurrences (`:178-183`, `:186-213` ×3, `:164-171` ×3, `:374-386` ×2, `:382-385`).
- `book/src/L4/ksp_solve.md` — 4 occurrences (`:178-182`, `:119-136`, `:134`, `:123-125`). (The one `book/src/semantics/index.md:150-184` FULL-path ref on `:117` was already correct from D1 — untouched.)
- `book/src/L4/chebyshev.md` — 1 occurrence (`:418`). (The link-text `[`l4_calculus`](../semantics/index.md)` on `:80` is correct — untouched.)
- `book/src/L4/index.md` — 1 occurrence (`:418`).

## Kept-exceptions (faithful-trim-or-finding)

**NONE.** Every "NOT rank-1" / "carries the same-shape contract" /
"NOT rank-1-pinned" occurrence in the cohort was a GENERAL-rule echo (the §4.1
"a bare concrete axis Tensor[N] is a rank-1 commitment" rule restated at the
op-scope), not an irreducible per-op shape fact — so all were trimmed. The op's
own admits-any-rank fact ("arbitrary, unknown rank" over shape group `S`) is
retained in every entry; the general "why a group beats Tensor[N]" teaching now
lives only at the surface §1.2.1/§4.1.

The `linear_combination` Tier-A entries were already relocated by c115 D3 (not in
this dispatch's scope) — their bullets carry the clean "(The general
named-shape-group convention is in [`l4_calculus`](…) §1.2.1, linked above.)"
back-pointer form, untouched here.

## Verification

### Surface is the complete home at the NEW path (D1 moved it verbatim)

`book/src/semantics/index.md` (old `book/src/design/l4_calculus.md` — confirmed
DELETED from `book/src/design/`) carries:
- **§0.1 Active-management discipline** (`:24`) — the LIVENESS / single-home rule
  ("Every semantic rule/def/abstraction … lives here exactly once. A producer …
  cites + links here; it does not transcribe the rule into its own chapter …").
- **§1.2.1 Named shape groups** (`:73`) — binding `(S: ...)` / use `$S`, the
  `Tensor[N]`-as-rank-1 anti-pattern, the rank-wildcard semantics.
- **§1.2.2 Operator shapes — domain and range groups** (`:87`).
- **§4.1 Shape contracts on primitives** (`:297`/`:314`) — "A named group is the
  rank-agnostic same-shape contract; a bare concrete axis (`Tensor[N]`) is **not**
  — it is a rank-1 commitment." (the authoritative sentence every trimmed entry
  now defers to).

Nothing is lost by the relocation — the general rule is present + complete at the
surface.

### Greps (the GATE)

- `grep -rn 'l4_calculus\.md' book/src` → **0** (all bare-basename prose refs gone).
- `grep -rln 'NOT rank-1\|not rank-1\|carries the same-shape contract\|accidentally read as' book/src` → **0** (cohort echo fully swept; no kept-exception).
- `grep -rn 'l4_calculus' book/src` → 60 remaining, ALL the link-TEXT form
  `[`l4_calculus`](../semantics/index.md)` (link text = the surface's canonical
  short name; path = the correct new `../semantics/index.md`). These are CORRECT
  and intentional (same convention as c115-D3 — the link text stays "l4_calculus";
  only the path and bare-basename prose refs were the relocation targets). NOT a
  defect.

### Build gate

- `cargo make book` → **EXIT 0** ("Build Done in 93.15 seconds").
- linkcheck2 (0.12.0) ran; **no broken-link / does-not-exist errors** (a broken
  link is a hard linkcheck2 error → non-zero exit; exit was 0).
- The WARN (unclosed-HTML-tag `<vector>`/`<fecollection>`/… in unrelated files)
  and "Potential incomplete link" (`[Time]`, `[j+1]`, `[0..k, 0..k]` prose
  brackets) warnings are PRE-EXISTING, in files this dispatch did not touch, and
  non-fatal. None introduced by these edits.
- All 5 Tier-B + all 19 Tier-C touched files retain ≥1 resolving §1.2.1
  back-link to `../semantics/index.md`.

## Open questions / caveats

- **Tier-C judgment now resolved by directive** (was c115-D3 OQ
  `named-shape-groups-general-rule-restatement-cohort-extent`, Tier-C "keep"
  read). The semantic-consolidation directive ratified RELOCATE; this sweep
  enacts it. The OQ's 27-file extent: Tier A (3, c115 D3) + Tier B (5) + Tier C
  (19, 19 files / 25 occurrences) = the cohort. With this dispatch the cohort
  restatement sweep is COMPLETE (echo-marker grep → 0); the OQ can be closed by
  the meta-phase.
- **No frontmatter touched.** `edges:` / `rank:` blocks untouched on every file;
  reachability + rank invariants HELD (prose-only trim).
- **`l4_calculus` link-text retained** (not renamed to `semantics`/`index`). The
  inline-code link text is the surface's stable short name and matches c115-D3;
  renaming it is a separate cosmetic decision, out of this dispatch's scope. The
  PATH everywhere is the correct `../semantics/index.md`.
