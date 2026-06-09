---
verifies: ../CYCLE.md
critiqued_at: 2026-06-09T053000Z
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

# META: verification of c154-D2 three small de-bulks

## Critique

### Checks run

**citation-validity — pass.** This is a finalization de-bulk report (kind: hygiene), not a content-authoring report; it introduces no new L0 pinpoint citations and removes none. I confirmed losslessness instead: `git diff HEAD` across the 4 named files shows exactly `5 insertions / 47 deletions`, all accounted for by the 3 fixes. No `(file, start, end)` citation appears in any removed text (the removed block was a methodology concept body carrying markdown cross-links, not source pinpoints). The frontmatter `edges:` block of `constructed-operators.md` (the authoritative graph edges, lines 2-7: `concepts/rotation`, `concepts/variant-absorption`, `concepts/apply_BA`, `L2/krylov_step`) is byte-identical HEAD vs working (`diff` of lines 1-8 → IDENTICAL). No citation lost.

**surface-or-evidence — pass.** No refinement-shaped proposal here: no operator/theme surface is modified and no rotation_claim is asserted. All edits are pure hygiene de-bulk on concept/feature pages (TOC-gloss normalization, dateless-process-clause removal, duplicate-body de-dup). The record-definition sub-check is N/A — no record/struct is newly named in a signature; the two feature H1 edits only append `(output product)` to existing composition-root titles.

**rotation-quality — pass.** No algebraic/structural/reduction rotation is asserted (de-bulk hygiene). Not applicable to this report kind.

**variant-axis-coverage — pass.** No operator/theme with orthogonal variant axes is introduced or modified. Not applicable.

**cross-reference-integrity — load-bearing here, pass.** Fix 3 lifts two inline links into the canonical §Use-in-GMRES-FGMRES paragraph; both targets resolve on disk: `book/src/concepts/apply_BA.md` and `book/src/L2/krylov_step.md` exist, and both links are present at line 173. The inbound-anchor check passes: `grep -rn 'constructed-operators.md#' book/src` → no matches, so the removed headings (`#concept-constructed-operators`, `#when-to-use`, `#canonical-example`, `#slices-that-use-this-methodology`) had zero inbound `#`-anchor targets — no inbound link broke. Fix 2's two links (`rotation.md`, `variant-absorption.md`) are unchanged and resolve. No build link error on any touched file.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried by this report. Not applicable.

**plan-kind-consistency — pass.** Declared shape is "three small finite-backlog hygiene de-bulks (direct-edit, de-bulk convention)"; the content matches exactly — glosses normalized, process-attribution clauses stripped, a duplicate concept body de-duped. Consistent with the FINALIZATION de-bulk directive (strip process accounting; KEEP semantics/laws/citations/links; no rank/status movement). No mis-classification.

**skill-uptake-survey — pass.** The report's shape implies `finalization-debulk` (strip/keep/lift) and `heading-metadata-hygiene` (TOC-gloss normalization) — both are referenced by name in the report (Fix 1 cites `heading-metadata-hygiene`; the de-bulk convention is invoked throughout). Telemetry present.

### De-dup-lossless verification (Fix 3, the load-bearing one)

I confirmed the removed 42-line second block was a genuine RE-STATEMENT, with every piece of its definitional content covered by the canonical §9-171 block:

- `## Concept: constructed operators` (removed) — pattern definition + "achieves levels (b)+(c) even when (a) is awkward" → covered by canonical §Context (lines 13-22) + §Worked-example levels list (lines 75-81) + §To-variant-absorption (line 93).
- `## When to use` (removed) — variant-affects-which-operator / branching-breaks-(b) / fixed-for-solve / scalar-counter-pattern → covered by canonical §When-to-construct (lines 24-31) and §Limits-of-absorption / per-step-variants (lines 113-146).
- `## Canonical example` (removed) — GMRES preconditioner-side example → fuller version is canonical §Worked-example (lines 33-81).
- `## Slices that use this methodology` (removed) — the `krylov_step` link → lifted into canonical line 173 ("See the firm [krylov_step (GMRES instance)]").

The two unique inline links were correctly lifted BEFORE removal: bare-text `apply_BA(op, v) → (w, z)` upgraded to `[apply_BA(op, v) → (w, z)](./apply_BA.md)`, and `See the firm [krylov_step (GMRES instance)](../L2/krylov_step.md)` appended — both verified present at line 173 and both targets resolve. All 4 removed headings confirmed gone; the page ends cleanly at `## Use in GMRES / FGMRES`. No unique definitional content lost.

### Conservation verification (all 3 fixes)

- **Fix 1** — H1-diff scan across all `feature/*.L4.md` shows exactly 2 changed H1s (capacitance, sparameters), each appending `(output product)`; the other 4 output-product columns (inductance, eigenfrequency-qfactor, energy-fields, waveguide-mode) already carried the tail; driver-leaf / spine-ROOT / kernel columns untouched. The 6 output-product set is now uniform; no other H1 changed.
- **Fix 2** — `grep -nE 'meta-review #[0-9]' book/src/concepts/dependency-map.md` → 0 matches. Diff confirms only the `meta-review #N` process clauses were dropped; the static carry-through facts ("with a carry-through clause", "refined into levels of absorption (invariant / procedural / primitive-sequence)") and both links are kept. (Remaining `meta-review #N` refs in book/src — 29, all in the `meta-reviews/*` carve-out, which the finalization directive explicitly excludes from de-bulk.)
- **No rank/status at risk** — all 4 files are concept/feature pages with no `rank:` frontmatter and no `## Status` rank-carrier prose; no sole-rank-carrier touched.
- **Graded-stack baseline HELD EXACTLY** — `files=392, typed=331, untyped=61, rank_violations=0, unresolved_depends_on_targets=0, promotion_frontier=11, detritus=123, true_detritus=51` (re-run confirmed: typed 331, untyped 61, 0 rank violations, no unresolved targets, frontier 11, detritus 123 / 51 true). Matches the prescribed baseline.
- **Build EXIT 0** — `cargo make book` → exit 0. The only warnings are pre-existing "Potential incomplete link" KaTeX-in-text false positives (e.g. `concepts/plane-rotation-stream.md:17`); none of the 4 touched files appear in any build error/warning.

### Issues found

None. All 8 checks pass; the de-dup is verified lossless; the inbound-anchor check is clean; the lint baseline held exactly and the build is EXIT 0. Clean report.
