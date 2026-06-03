---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T194500Z
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

# META: verification of "Re-anchor eigenfrequency-qfactor.{L4,L1} — clear the c080 D3-staleness clause"

## Critique

This is a **feature-surface (composition-root) kind** report executed as a `lifter` LOW/hygiene pure-rewriting pass closing OQ-1016. The adapted feature-surface checklist applies (rotation-quality + variant-axis-coverage no-op; cross-reference-integrity + edge-label-fidelity load-bearing).

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` on CYCLE.md: `10 ok, 2 failing (12 citations checked)`. The 2 `[MISS]` are exactly `open-questions.md:1016` and `open-questions.md:1013` — scaffolding-ledger pointers, NOT source citations; the tool cannot resolve `open-questions.md` (it lives under `scaffolding/`, outside the citecheck search roots), and the report explicitly frames them as scaffolding-ledger refs (Supporting evidence §OQ chain). This is the expected non-resolving-scaffolding-ref distinction, not citation drift. The 10 real citations (source ranges + book live-links) all pass. I independently re-ran the two load-bearing L0 anchors the report self-verifies: `eigensolver.cpp:430-439 --anchor 'std::sqrt'` → anchor at `:433` in-range `[ok]`; `postoperator.cpp:1188-1203 --anchor 'quality_factor'` → anchor at `:1200` in-range `[ok]`. No `verified_against:` block in this report (lifter pass), so the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass (feature-surface adaptation applied).** This pass modifies surface (feature-column prose + dep-map cells) but makes NO new per-op algebraic claim — it re-anchors a maturity narration. Per the composition-root adaptation, the evidence shape is the L0 driver-range citations + constituent down-links, both of which are present and resolve: the eigenvalue-un-transform half re-anchors to firm L1 `eigenvalue-untransform` (verified firm on-disk), the κ-half to firm L1 `participation_ratio`. No record is named-in-signature without a definition home (the constituent primitives are referenced, not newly defined here), so the record-definition sub-check no-ops.

**rotation-quality — pass (not applicable to feature-surface kind).** A feature column rotates nothing — it recomposes already-firm vocabulary outward. Formal no-op per the composition-root adaptation. (This pass is additionally a pure-rewriting hygiene pass, which asserts no rotation at all.)

**variant-axis-coverage — pass (not applicable to feature-surface kind).** The variant axes (the problem-type `√μ` vs `λ/i` un-transform) live in the composed constituent `eigenvalue-untransform`, not in the feature column; the column references the axis but does not own it. Formal no-op.

**cross-reference-integrity — pass (load-bearing for this kind).** Verified the load-bearing re-anchor: `book/src/L1/eigenvalue-untransform.md` exists on-disk (`firmness: firm`, 18806 bytes, landed c080) — the live-link `../L1/eigenvalue-untransform.md` resolves and the maturity claim ("firm L1 (cycle-080)") matches the on-disk `## Status`. The sibling link `../L1/participation_ratio.md` also resolves (firm, c077). The two dep-map cell flips are accurate: the `[old]` anchors match on-disk content EXACTLY at the cited lines — L4.md:63 (`| eigenfrequency un-transform (folded) | ... | rough-in |`) and L1.md:59 (`| eigenfrequency un-transform | ... §Semantics ... | rough-in |`), both flip `rough-in`→`firm` and re-point at the now-firm primitive. The L1 frontmatter `composes` cell at line 8 also matches. All 7 `[old]` blocks anchor cleanly, so the edits will apply. Both columns are wired into `SUMMARY.md` (lines 36–37). The maturity claims are NOT overclaims: the linked-constituent maturity matches on-disk, and the column correctly stays `seed` because the composing verb stays `rough-in`.

**edge-label-fidelity — pass.** The dep-map cell flips are accurate against on-disk state: `eigenvalue-untransform` IS firm (c080), so `rough-in`→`firm` is correct, and the composing-by relationship (`folded by eigenfreq_qfactor_reduce`) is the true structural fact. The column correctly STAYS `seed`: I confirmed the L4 verb `eigenfreq_qfactor_reduce.md` is on-disk `firmness: rough-in` with §Status stating gate-(a) DISCHARGED (c080) and gate-(b) the sole remaining gate — so the feature-column `seed` is correct (a seed feature column composing a rough-in constituent is the expected state until all constituents firm). The residual blocker re-anchored onto gate-(b) (the eigenpair→`(f,Q)` assembly test, OQ at open-questions.md:1013, out of write-scope) matches the OQ ledger exactly. No maturity overclaim.

**plan-kind-consistency — pass.** Declared as a `lifter` pure-rewriting hygiene pass with zero status/count change. Content matches: 7 surgical prose/dep-map-cell edits, no `## Status` line flipped (both columns stay `seed`, verb stays `rough-in (test-coverage-bounded)`). The report correctly notes the index-table status-cell guard does NOT fire (no promotion to mirror). The report does NOT touch the L4 verb file (correctly — it was already re-anchored c080 D2) and does NOT overclaim the verb as firm. Shape matches kind.

**skill-uptake-survey — pass.** The report references the relevant skill: `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (cited in Discipline notes, justifying the live-link re-anchor against the verified-on-disk target) and the `tools/citecheck/` mechanical anchor self-verification. Telemetry present; appropriate skill uptake for a lifter re-anchor pass.

### Issues found

None. All 7 `[old]` anchors match on-disk content at the cited lines, the live-link re-anchor target exists firm on-disk, the dep-map flips are accurate against on-disk maturity, the column-stays-`seed` reasoning is correct (composing verb stays `rough-in`, gated solely on out-of-write-scope gate-(b)), the L4 verb file is correctly untouched and not overclaimed, the L0 column is correctly out of scope (no maturity prose — confirmed via grep, 0 matches), and the 2 citecheck "failures" are confirmed expected non-resolving scaffolding-ledger pointers, not source-citation drift. All 8 checks pass; the report is clean. Setting `overall_status: ready` per the all-pass clean-report path.
