---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T21:05:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-28T21:40:00Z
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

# META: verification of chebyshev slice §L4 full-removal audit

## Critique

### Checks run

**citation-validity — pass.** Every Class-A re-point names a real, present `L4/chebyshev.md` section anchor. I independently confirmed §Semantics (`innerStep` lines 152-160, `apply` body 133-161), §Signature (`scalars` field, `ChebOp E S` field), and §"Initial-guess shape: branch vs derived view" (223-239) all exist as headers (`grep '^## \|^### ' book/src/L4/chebyshev.md`). The content-presence claims in §"Content-presence verification" hold against the on-disk (pre-re-anchor) file.

**surface-or-evidence — pass.** Not a refinement of an operator/theme surface; this is a Phase-1 slice-reduction audit (corpus removal + citation re-point), which is the explicitly-sanctioned class. No rotation_claim required.

**rotation-quality — pass.** No new rotation asserted (not applicable to a slice-removal audit). The report correctly leans on the already-firm L4>L3>L2 chain rather than claiming a new rotation.

**variant-axis-coverage — pass.** The polynomial-kind variant axis (4th-kind `Unit` vs 1st-kind `{rho_prev}`) is preserved by re-pointing R-6 onto the `ChebOp E S` type-level distinction; no axis is dropped or hidden.

**cross-reference-integrity — FAIL (the load-bearing check).** The report asserts a "complete whole-tree grep ... 12 inbound references in 9 files." My independent grep of `book/src/` (excluding `book/book/`) finds the inventory **MISSES 4 live stale references** to the slice (details under Issues). Crucially, none of the 4 misses are markdown-link form, so OQ-3's `cargo make book` / linkcheck backstop will NOT catch them — they become silently-dead `chebyshev.md` slice path/range strings post-removal. The build-breaking markdown-link class (`](...slices/chebyshev.md)`) IS complete: exactly `SUMMARY.md:101` (R-20), `spec/index.md:19` (R-21), `L0/...overview.md:102` (R-17); the apparent `L3/index.md:29` link `](./chebyshev.md)` resolves to the FIRM `L3/chebyshev.md`, not the slice — correctly untouched.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label carried; the prose discusses the L4-anchored re-points consistently.

**plan-kind-consistency — pass.** Declared an `observation`/audit (Redundancy kind) with a FULL-REMOVAL verdict; content shape matches.

**skill-uptake-survey — pass.** The `phase-1-slice-reduction-audit` skill is referenced with its START/END boundary verification documented (§Supporting evidence). Appropriate uptake.

### Issues found

1. **[cross-reference-integrity, HIGH] `L2/krylov-step.md:172` — uninventoried stale citation.** Line 172 cites `chebyshev.md:99-100` ("no direct unit tests on ... Chebyshev step kernels"). This is a bare-name range into the slice's §L1-era content (already removed cycle-014; becomes fully dead after R-22). Not in the report's Class-A/B/C inventory. Not a markdown link, so the build backstop won't flag it.

2. **[cross-reference-integrity, MED] `L2/index.md:31` — uninventoried stale reference.** Line 31 prose reads "`chebyshev.md §L4`" (alongside `cg.md §L4`, etc.). The report inventoried `L2/index.md:35` (the pattern-instance list, R-13) but NOT `:31`. The §L4 it names is removed; content now lives at `L4/chebyshev.md §Semantics`. Not a markdown link.

3. **[cross-reference-integrity, MED] `L3/index.md:29` and `:41` — uninventoried stale references.** Both lines name the full slice path in inline-code prose ("unblocks full reduction of the Phase-1 slice `book/src/spec/slices/chebyshev.md`"). After R-22 these name a non-existent file. Not markdown links (won't break build), but they are live narrative referencing a removed path. At minimum they should be re-pointed to "now-reduced/removed" framing or dropped, consistent with the report's own honest-fix treatment of Class-B provenance.

4. **[cross-reference-integrity, INFO — likely correct disposition] bare-name slice-corpus enumerations.** `L4/index.md:28,40`, `L4/krylov-step.md:126`, `L2/krylov-step.md:7` (Context, R-1 fixes the first instance only) all mention bare `chebyshev.md` in slice-corpus lists. These are corpus-enumeration prose mentioning the slice by short name alongside `cg.md`/`gmres.md`/`arnoldi_step.md` (those slices still exist on disk). Whether these need touching depends on whether the project treats bare-name corpus enumerations as live citations — the report's Class-C disposition for `meta-reviews/...` (leave frozen history) suggests bare corpus mentions are tolerated, but the report did not state a policy for the L4-index / L4-krylov-step bare mentions. Flagging for repairer/integrator triage; lower severity than 1-3.

5. **[count discrepancy, LOW] inventory count understated.** Report titles claim "13 citations" / "12 inbound references in 9 files"; with the 4 misses above the true live-reference count is higher. The dispatch instruction asked whether the 13-citation set is COMPLETE — it is **NOT complete** for non-link stale references; it IS complete for build-breaking markdown links.

### Verified-correct claims (for the repairer's benefit)

- OQ-1 ordering dependency (apply AFTER wave-1 lifter; the wave-1 Change 11/15 rewrite `L4/chebyshev.md:412`/`:489` self-citations) — CONFIRMED by reading those lines on disk; the deferral of the L4-self-citation provenance fixup is appropriate and the write-conflict rationale is sound.
- Build-breaking markdown-link class is COMPLETE (3 real links + 1 false-positive correctly identified).
- Content-presence (check b) holds; re-points use stable section-name anchors, not shifted line numbers — correct given the wave-1 re-anchor.
- Class-B already-dangling provenance treatment (R-14/15/16) and the meta-reviews leave-as-is (OQ-2) dispositions are sound.

### One-line per-check + completeness verdict

citation-validity pass / surface-or-evidence pass / rotation-quality pass / variant-axis-coverage pass / **cross-reference-integrity FAIL** / edge-label-fidelity pass / plan-kind-consistency pass / skill-uptake-survey pass. **The 13-citation set is NOT complete (independently verified): 4 non-link stale slice references missed — `L2/krylov-step.md:172`, `L2/index.md:31`, `L3/index.md:29`, `L3/index.md:41` — none caught by the build backstop. Build-breaking markdown-link subset IS complete.**

## Repair

### Fixes attempted

- **Finding** (critic issue #1, HIGH): `L2/krylov-step.md:172` cites `chebyshev.md:99-100` — a live "no direct unit tests on Chebyshev step kernels" coverage-gap fact, uninventoried, dead after R-22.
  - **Decision**: repaired.
  - **Action**: added **Change R-1b** (`book/src/L2/krylov-step.md`). Re-pointed the chebyshev mention onto the firm `book/src/L1/chebyshev-smoother.md:260`, which carries the identical "no dedicated unit test under `reference/palace/test/unit/`; behaviour exercised only through multigrid integration" status (verified on disk). The `cg.md`/`gmres.md` siblings still exist, left intact — mechanical one-mention re-point onto an existing-firm status line, not authoring.

- **Finding** (critic issue #2, MED): `L2/index.md:31` "Consumed-by" §L4 prose names `chebyshev.md §L4` (sibling of the `:35` list the report DID fix at R-13).
  - **Decision**: repaired.
  - **Action**: added **Change R-13b** (`book/src/L2/index.md`). Re-pointed the one stale chebyshev §L4 mention onto `book/src/L4/chebyshev.md` §Semantics, matching R-13's treatment of the `:35` sibling. `cg.md`/`gmres.md`/`arnoldi_step.md` mentions untouched (slices persist).

- **Finding** (critic issue #3, MED): `L3/index.md:29` and `:41` name the full slice path `book/src/spec/slices/chebyshev.md` in inline-code prose (dead after R-22).
  - **Decision**: repaired.
  - **Action**: added **Change R-23** (`L3/index.md:29` row status parenthetical) and **Change R-24** (`L3/index.md:41` Working-Notes bullet). Both re-framed to "removed cycle-015; material now authoritative across the firm `L1`–`L4` chebyshev cohort" — the report's own Class-B honest-fix style. **Confirmed the critic's distinction**: the markdown LINK `[chebyshev](./chebyshev.md)` in the `:29` row resolves to the FIRM `L3/chebyshev.md` and is correctly UNTOUCHED; only the trailing inline-code-prose slice path is stale. The `[old]` strings were scoped to the stale path fragment, NOT the link.

- **Finding** (critic issue #4, INFO): bare short-name `chebyshev.md` mentions in collective slice-corpus enumerations at `L4/index.md:28,40`, `L4/krylov-step.md:126`.
  - **Decision**: not-needed (left as-is).
  - **Rationale**: these are collective corpus-name enumerations (`cg.md, gmres.md, chebyshev.md, arnoldi_step.md, polynomial_recurrence_step.md`) with no path / no line-range / no link — the four sibling slices still exist on disk. Nothing is stranded by R-22 (no removed target is referenced). Editing a collective narrative enumeration to surgically drop one short name is a content/narrative-accuracy decision, not a mechanical citation re-point — out of repair authority, and within the project's tolerance for bare corpus mentions where siblings persist (consistent with the report's Class-C `meta-reviews` leave-frozen disposition). Not stale-citation rot; no follow-up required.

### Unrepairable findings

None. All four missed live stale references (critic issues #1–#3) were mechanically re-pointed onto existing firm targets verified on disk. Issue #4 is a no-op-by-disposition (not unrepairable; nothing to fix).

## Suggested resolution

`overall_status: ready`. With R-1b / R-13b / R-23 / R-24 added, the citation set is now **complete** for all live stale references — every inbound mention of the to-be-removed slice (markdown-link AND non-link prose/inline-code/range forms) is either re-pointed to the firm cohort or removed. **FULL-REMOVAL (R-22) is now safe**: it strands nothing.

Notes for the integrator:
- **Ordering dependency stands** (report Recommendation + OQ 1): apply the cycle-015 wave-1 lifter (`L4/chebyshev.md` rough-in→firm re-anchor) FIRST, then this report. The Class-A re-points anchor onto `L4/chebyshev.md` firm section names.
- **Residual OQ (unchanged, not a blocker)**: OQ 1 — after R-22, the wave-1 lifter's post-re-anchor `L4/chebyshev.md` §Status/§Evidence **self-citations** (`chebyshev.md:289,325,396-397` / `:287-439`) name a removed file. They need a post-apply one-line provenance touch (same treatment as R-14..R-16). The report correctly did NOT emit this (write-conflict with the wave-1 lifter's same-line rewrites; post-rewrite text not yet on disk). Integrator should fold a post-apply fixup, or route a one-line follow-up touch after both reports land. This strands no reader (content is in-file) — only a dead path string.
- Build backstop (`cargo make book` linkcheck) remains the final gate per OQ 3; the markdown-link subset was already complete, and the 4 non-link re-points close the silent-staleness gap the linkcheck would not have caught.
