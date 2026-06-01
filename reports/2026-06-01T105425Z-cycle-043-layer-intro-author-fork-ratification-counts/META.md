---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T120000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
---

# META: verification of "L2 fork-ratification + cycle-043 consolidated index counts"

## Critique

This is an index/governance-refresh report (fork-ratification touch + sole consolidated-tally owner across three indices). Several checks no-op on this shape; the load-bearing checks are count-correctness (folded into citation-validity + cross-reference-integrity), fork-ratification accuracy, count-ownership disjointness, and anchor-fidelity. Two real cross-reference warnings surfaced; everything else is clean.

### Checks run

**citation-validity — pass.** `citecheck --scan` reports 4 ok / 5 "MISS"; all 5 misses are abbreviated sibling-report pointers (`reports/.../harvester-L2-axpy/CYCLE.md:46`, `-axpby/CYCLE.md:60`, `cycle-planner-cycle-043/CYCLE.md:18-19`, etc.) with `...`-elided paths — provenance references to co-dispatched cycle-043 reports, not Palace-source citations; not resolvable by the tool by design, not defects. The one load-bearing NEW Palace anchor is `palace/linalg/vector.hpp:262-270` (the `normalize` floor source in E6) — verified via `--anchor 'Normalize'`: OK, anchor at lines 262/264 in range. The pre-existing `vector.cpp:248-261` (reciprocal row, on-disk, untouched by this report) is not load-bearing here. No `verified_against:` block in this report, so that sub-check is not applicable. **Count claims verified against on-disk enumeration** (all confirmed): L2 dep-map 18 rows (17 firm + 1 PC `deflate`) → +4 = 22 rows (21 firm + 1 PC); L2-L1 16 rows (15 firm + 1 PC `deflate-composition-lowering`) → +4 = 20 (19 firm + 1 PC); L3-L2 10 rows (10 firm, 0 PC) → +4 = 14 firm = 14-of-18. `deflate`/`deflate-composition-lowering` correctly held OUT of the firm tallies. D1's three renames are theme-slug renames (verified net-zero on counts). The four cycle-043 floors (axpy/axpby/axpbypcz/normalize) and their L2-L1 `-leaf-identity` / L3-L2 `-body-identity` edges account for exactly the +4 in each index. Arithmetic is internally consistent across all three indices and the supporting-evidence enumeration.

**surface-or-evidence — pass.** Not a refinement-of-existing-operator proposal in the rotation sense; this is governance/index surface (status-language flips + tally rows + cohort narrative). The fork-ratification flips are surface edits faithful to the cited batch-12 meta-phase decision (the c042 cross-cutter audit `reports/2026-06-01T063231Z-cycle-042-cross-cutter-leaf-vs-fold-audit/` it adopts). No rotation_claim is asserted; nothing to backfill. Inapplicable-but-pass.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted. The 4 new dep-map rows describe identity-in-form floors authored by sibling harvesters (D3/D4/D5/D9); this report only tallies them. The `normalize` "fused composite `nrm2 ∘ scal`" framing is a description of D9's floor, not a rotation claim this report makes.

**variant-axis-coverage — pass.** The report correctly records the variant-axis facts it inherits: the axpy-family output-aliasing axis is "the FOLD's, not leaf-specific" (planner OQ `arity-family-leaf-floors-output-aliasing-axis-is-the-folds`); `normalize` element-type (real/complex; norm always real); `nrm2` carve-out (fork-invariant on membership). No hidden branches in the governance edits.

**cross-reference-integrity — warning.** Anchor fidelity is clean: all 11 `[old]` anchors (E1/E2/E4/E5/E6 in L2/index; E8/E9 in L2-L1; E10/E11 in L3-L2) match on-disk verbatim and are each unique (grep count 1). E6's eigsolve-row `[old]`==`[new]` prefix confirmed byte-identical (1826 chars each) — the row is an unchanged append-anchor, only the 4 floor rows are added. E7 appends after the unique line-105 trailing sentence; disjoint from D1's line-106/108 content (report does NOT contain "Cycle-041 BLAS-1-floor cohort" or "Slug-naming inconsistency" text — confirmed). Fence parity clean (20 fences = 10 paired `edit:` blocks, no nested-fence truncation; build-readiness guard N/A — index prose, no firm-chapter body). The new dep-map links (`./axpy.md`, `./axpby.md`, `./axpbypcz.md`, `./normalize.md`) point at L2 files that do NOT yet exist on disk — they are created by co-dispatched D3/D4/D5/D9 this same cycle (L3/L1 anchors + scalar-promotion concept + nrm2/scal/inner_product/linear_combination/orthogonalize/krylov-step L2 all confirmed present). This resolves at build time ONLY if those four sibling reports land; flagged as an integration dependency, not a defect. **Two genuine warnings** (see Issues 1 + 2): (1) the report claims a decision-3 directive-slug rename `l2-floor-under-l3-blas1-cohort`→`l2-floor-under-l3-leaf-cohort` but only renames the cohort *heading* (E2) and uses the new slug in new content — **12 on-disk occurrences of the old slug survive** (L2/index §Semantics line 27 + dep-map status-cells 70/72/73/74/75/76 + working-notes 105/106/107), none swept by this report and none by D1 (D1 renames theme slugs, not the directive); post-cycle the artifact carries the directive under two names. (2) L3-L2 §Working-Notes has TWO "Design fork" bullets (lines 49 + 50); E11 flips only line 50 to RATIFIED, leaving line 49 ("reaches ONLY the cycle-041 cohort"; "the c042 audit *recommends* KEEPING (b)") in provisional/recommendation language — the two adjacent bullets contradict on whether the fork is decided.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried as the report's own claim. The L2-L1 and L3-L2 cohort narratives discuss exactly their own edges (L2>L1 `-leaf-identity`, L3>L2 `-body-identity`); LHS/RHS layer assignments are correct (L3 body-identity LHS=L3, RHS=L2 same-named floor).

**plan-kind-consistency — pass.** Declared shape is layer-intro-author governance refresh (fork-ratification + sole consolidated-tally owner). Content matches: status-language flips, tally rows, cohort-growth notes, two items explicitly routed to the batch-13 meta-phase (chebyshev count reconciliation; the `fused-composite-no-fold-parent` sub-shape). The report correctly does NOT renumber the cohort denominator or author chapter bodies (those are D3-D10's / the meta-phase's).

**skill-uptake-survey — pass (telemetry).** No skill invocation referenced. The relevant procedure would be a count-ownership / on-disk-enumeration discipline; the report does perform the Phase-2 on-disk enumeration the count-ownership convention requires (supporting-evidence section). No blocking concern; the `proposed-changes-fence-encloses-full-body-guard` is N/A (no firm body authored).

### Issues found

**Issue 1 (cross-reference-integrity, warning) — incomplete directive-slug rename; dual-slug coexistence.** `CYCLE.md` §(b) E7 (working-note line: "the now-cohort-neutral `l2-floor-under-l3-leaf-cohort` directive (renamed this cycle, decision 3)") asserts the directive was renamed from `l2-floor-under-l3-blas1-cohort`. The report renames only the §Vocabulary-cohort *heading* (E2) and uses the new slug in its new tallies/rows. **12 on-disk occurrences of `l2-floor-under-l3-blas1-cohort` survive unswept** across the three indices — in `book/src/L2/index.md`: §Semantics intro line 27, dep-map status-cells for `scal`/`dot`/`nrm2`/`reciprocal`/`elementwise_product`/`assemble-diagonal` (lines 70/72/73/74/75/76), and working-notes lines 105/106/107. Per the report's own disjointness account, D1 renames *theme* slugs (`nrm2-fold-specialization`→`nrm2-leaf-identity`, etc.), NOT the *directive* slug — so no co-dispatched report sweeps these either. After this cycle the artifact will refer to one directive under two names. Severity: warning (prose inconsistency, not a build-breaking link). The report should either (a) propagate the directive rename to the surviving on-disk references, or (b) explicitly route the residual `-blas1-cohort` propagation as a follow-up sweep (it currently does neither — it asserts the rename as done).

**Issue 2 (cross-reference-integrity, warning) — stale provisional bullet left after fork-ratification flip.** `book/src/L3-L2/index.md` §Working-Notes carries two adjacent "Design fork" bullets: line 49 ("Design fork ... reaches ONLY the cycle-041 cohort"; the c042 audit "**recommends** KEEPING leaf-floor (b)") and line 50 ("Design fork ... load-bearing batch-12 meta-phase signal"). `CYCLE.md` E11 flips only the line-50 bullet to "Design fork RATIFIED". The line-49 bullet is left in recommendation/provisional language and is NOT addressed anywhere in the report. Post-cycle the same §Working-Notes section asserts both "RATIFIED" (line 50→new) and "the audit recommends ... [un-decided]" (line 49). Severity: warning — a fork-ratification job that leaves a live "recommends, not decided" bullet adjacent to the RATIFIED one is internally contradictory. The line-49 bullet needs a parallel flip (or merge into the line-50 flip).

**Issue 3 (informational, not blocking) — new dep-map links depend on un-landed sibling files.** The 4 appended L2 dep-map rows (E6) carry live links `./axpy.md` / `./axpby.md` / `./axpbypcz.md` / `./normalize.md` to files not yet on disk (created by co-dispatched D3/D4/D5/D9). Cross-reference resolution at `cargo make book` time requires those four sibling reports to land in the same cycle. This is the expected wave-3 sole-tally-owner ordering (the report is explicit it runs LAST and presupposes the floors landed), not a defect — recorded so the integrator confirms the full cohort applies together before build.

**Note (no issue) — count-ownership disjointness holds.** Verified D2 touches only orientation prose (fork-status flips) + tallies + the 4 dep-map rows + cohort-growth notes; it does NOT write chapter bodies, the per-slug rename rows, or SUMMARY (D1/D3-D10's). The claimed disjointness with D1's L2/index lines 106/108 is sound (the report's text contains neither line's distinctive content). The chebyshev 12-of-13 reconciliation and the `normalize` `fused-composite-no-fold-parent` sub-shape are correctly surfaced as batch-13 meta-phase routes, not enacted.

---
repaired_at: 2026-06-01T123000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

## Repair

### Fixes attempted

- **Finding (Issue 1, cross-reference-integrity warning)**: incomplete directive-slug rename — decision 3 renamed `l2-floor-under-l3-blas1-cohort` → `l2-floor-under-l3-leaf-cohort` but only the cohort heading (E2) + the line-107 fork-signal bullet (E5) were swept; 9 on-disk occurrences of the old slug survive in `book/src/L2/index.md` (§Semantics line 27, dep-map status-cells lines 70/72/73/74/75/76 for `scal`/`dot`/`nrm2`/`reciprocal`/`elementwise_product`/`assemble-diagonal`, working-notes lines 105/106). Line 107 is already swept by the report's E5; the L2-L1/index occurrence is already swept by the report's E9.
  - **Decision**: repaired.
  - **Action**: appended block **E7b** to `CYCLE.md` §(a)/(b) (after E7, before the L2-L1 section) — 9 mechanical `edit:book/src/L2/index.md` slug-rename blocks, each a unique full-substring `[old]` span differing from `[new]` only in the slug token. Verified all 9 `[old]` anchors match on-disk verbatim and grep-count exactly 1; verified the line-105 sweep anchors a substring disjoint from E7's trailing-sentence anchor (non-overlapping spans on the same line, order-independent). Post-application, `book/src/L2/index.md` carries zero occurrences of the old slug (10 on-disk lines: line 107 via E5 + lines 27/70/72/73/74/75/76/105/106 via E7b = full coverage). Out-of-scope scaffolding residuals (`priorities.md` ×10, `roadmap.md` ×2, append-only `integrator-signals.md` / `cycle-record.jsonl`) routed to a new OQ `l2-floor-directive-slug-rename-scaffolding-residual-sweep` for the batch-13 meta-phase (which owns the plan) — NOT edited here (book/-scope discipline + meta-phase plan-ownership partition).

- **Finding (Issue 2, cross-reference-integrity warning)**: stale provisional fork bullet — `book/src/L3-L2/index.md` §Working-Notes has two adjacent "Design fork" bullets (lines 49 + 50); E11 flips only line 50 to RATIFIED, leaving line 49 in "reaches ONLY"/"recommends KEEPING"/"under (a)" un-decided language, so the two bullets contradict on whether the fork is decided.
  - **Decision**: repaired.
  - **Action**: appended block **E11b** to `CYCLE.md` §(b) (after E11) — one `edit:book/src/L3-L2/index.md` block flipping the line-49 bullet to RATIFIED footing consistent with E11/E5/E9 (the decision content already exists in those blocks; this is wording reconciliation only, no new decision authored). The bullet's distinct payload (the fork reached ONLY the fold-parented edges; the cycle-042 standalone + cycle-043 `normalize` fused-composite edges were never touched) is preserved, now in the ratified/past-tense frame. Verified the `[old]` anchor matches on-disk verbatim and grep-counts exactly 1.

### Unrepairable findings

None. Issue 3 (the 4 new dep-map links depend on D3/D4/D5/D9 co-landing) is informational wave-3 sole-tally-owner ordering, not a defect — recorded for the integrator, no repair needed.

## Suggested resolution

`ready`. Notes for the integrator:
- Both repairs are additive `edit:` blocks (E7b ×9, E11b ×1) appended to the report's proposed-changes; total `edit:` fence count is now 20 paired (40 fence lines, even parity verified). They apply with the same serial by-substring matching as the report's original blocks.
- This is a **wave-3 sole-tally-owner** report: it presupposes the cycle-043 floor siblings (D3/D4/D5/D9) + the lifter rename sweep (D1) have already landed (the 4 new dep-map links `./axpy.md`/`./axpby.md`/`./axpbypcz.md`/`./normalize.md` resolve at `cargo make book` time only if those files exist on disk). Confirm the full cohort applies together before the finalize build — per the report's own §Disjointness note and the critic's Issue 3.
- After application, `book/` is free of the old directory slug `l2-floor-under-l3-blas1-cohort`; the residual scaffolding-file occurrences (`priorities.md`/`roadmap.md`) are routed to OQ `l2-floor-directive-slug-rename-scaffolding-residual-sweep` for the batch-13 meta-phase. Append-only `cycle-record.jsonl` / `integrator-signals.md` historical mentions are intentionally left untouched.
