---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T010000Z
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

# META: verification of "Re-anchor domain_energy_reduce.md:313-316 (gram_reduce/bilinear-form firm cascade)"

## Critique

### Checks run

**citation-validity — pass.** The two load-bearing on-disk citations were re-verified directly. `book/src/L4/gram_reduce.md:4-5` is `firmness: firm` / `rank: firm`, and `book/src/L1/bilinear-form.md:4-5` is `firmness: firm` / `rank: firm` — both confirmed on disk, matching the report's paste-inline block (CYCLE.md:29-49) verbatim. The report's premise (the c095 flip is real, the `:313-316` parenthetical's "STAYS rough-in" / "is still rough-in" claim is falsified) is therefore grounded. The proposed `[old]` block (CYCLE.md:54-57) matches the on-disk `:313-316` text character-for-character, so the edit anchors cleanly. No `verified_against:` payload is *proposed* by this report (the block visible in the on-disk chapter is pre-existing and untouched by the edit), so the YAML round-trip sub-check no-ops. All other supporting citations (`:133-139`, `:181-183`, `:222-223`) were spot-checked and resolve in range.

**surface-or-evidence — pass.** This is a refinement-shaped change to existing chapter surface (the `:313-316` parenthetical), and it carries direct disk evidence (the two firm-flip frontmatter reads) — it is a within-file land-clean re-anchor correcting a falsified maturity assertion, exactly the retroactive-correction shape the check permits. The `[new]` text (CYCLE.md:58-65) accurately reflects post-c095 reality (both reductions now rest on firm folded primitives) AND preserves the legitimate `domain_energy_reduce`-vs-`gram_reduce` distinction by recasting it from a (now-false) maturity contrast to the SHAPE contrast (rank-1 single-field vs rank-2 family-PAIR, the c074 D6 over-unification guard). I confirmed this recast is consistent with the shape distinction the file already carries at `:133-139` (rank-1-vs-rank-2 family-PAIR), `:181-183` ("Not a symmetric-Gram reduction… rank-1 vs rank-2… c074 D6 over-unification guard"), and `:222-223` (the gram_reduce dependency-list over-unification guard). The re-anchored parenthetical now agrees with the rest of the file rather than contradicting the on-disk maturity state. No record is newly named by the edit (record-definition sub-check inapplicable; `DomainOpMap` / `DomainData` homes are untouched).

**rotation-quality — pass (not applicable).** No algebraic/structural rotation is asserted by this report — it is a pure within-file prose re-anchor of a maturity parenthetical, no L_{n+1}→L_n representational claim.

**variant-axis-coverage — pass (not applicable).** The edit touches neither the variant_axes frontmatter nor any variant-axis prose; no axis coverage is introduced or modified.

**cross-reference-integrity — pass.** The `[new]` text retains exactly two links: `[gram_reduce](./gram_reduce.md)` and `[bilinear-form](../L1/bilinear-form.md)`. Both targets exist on disk. No new slugs are introduced. No frontmatter `rank:`/`edges:` change is proposed (correctly — `domain_energy_reduce` is already `rank: firm` on `depends-on: participation_ratio + matrix-weighted-norm`, both verified firm on disk this cycle, so the rank invariant `rank(u) ≤ min(deps)` holds unchanged). The build-readiness fence guard is not triggered (no firm-flip claim authored outside a fence; this is a single `edit:` block).

**edge-label-fidelity — pass.** No edge label is carried or flipped by this report. The dispatch's check-(4) expectation (no `rank:`/`edges:` flip needed) is confirmed: the file is already `rank: firm`, both `depends-on` deps are firm, and the edit is prose-only.

**plan-kind-consistency — pass.** Declared kind is a lifter within-file land-clean re-anchor (item-2). The content shape matches exactly: a single bounded prose correction of a drifted maturity assertion, decomposition/signature untouched, evidenced by two L0/disk citations, recorded in the report — squarely within the lifter scope-content-correction boundary.

**skill-uptake-survey — pass.** The report's shape (firm-flip cascade verification + within-file maturity-drift sweep) is telemetry-surfacing, not blocking. The report invokes the within-file conclusion-narration guard (the c093 lifter bullet, CYCLE.md:112-114) as its worked instance and cites citecheck `--anchor` usage in the chapter's Evidence section. No missing skill-invocation gap.

### Issues found

None. This is a clean, single-site within-file land-clean.

- The within-file self-consistency claim (CYCLE.md:78-96) was spot-checked and holds: a fresh grep confirms `:313-316` is the ONLY co-mention of a `gram_reduce`/`bilinear-form` maturity assertion; `:314` is the file's only `bilinear-form` mention (inside the re-anchored parenthetical); every other `rough-in` mention (`:212`, `:274`, `:280`, `:282`, `:288`, `:295`, `:402`) narrates `domain_energy_reduce`'s OWN promotion history, not a stale cross-reference; and every other `gram_reduce` mention is a maturity-free structural / over-unification-guard distinction.
- The two falsifying frontmatter reads (`gram_reduce.md` firm, `bilinear-form.md` firm) and the two `depends-on` dep reads (`participation_ratio` firm, `matrix-weighted-norm` firm) all confirmed on disk this cycle — the rank invariant is preserved and the edit is correctly frontmatter-free.

All 8 checks pass; `overall_status: ready` set (clean all-pass report; no repairer will run).
