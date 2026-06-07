---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T061858Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
# rank-invariant: pass
# reachability: pass
repaired_at: 2026-06-07T063500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired   # the two minor convention/wording drifts repaired; the forward-ref sub-finding is unrepairable (defers to integration)
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: needs-revision
follow_up_agent: integrator-per-report
---

# META: verification of "geometric-multigrid preconditioner feature-surface column"

## Critique

### Checks run

**citation-validity — warning.** Mechanical scan clean: `citecheck --scan CYCLE.md --quiet` → **39 ok, 0 failing** (all bounds + path-hygiene pass). The load-bearing pinpoints were then anchor-verified against the authoritative `citecheck --anchor` line map (NOT codemap `read_range`, which displayed a ~1-line shift and is not a source-of-truth). The **range-end / envelope citations are all sound**: `gmg.cpp:172-205` (VCycle — def `VCycle(int l` at 172, close brace at 205), `gmg.cpp:126-142` (Mult — def at 126), `gmg.cpp:16-63` (ctor, `DistRelaxationSmoother` at 44, `ChebyshevSmoother` at 53/58), `ksp.cpp:207-234` (GMG construction — `GeometricMultigridSolver` at 210/220/227, `GetNumLevels` at 207, `GetProlongationOperators` at 221 **and** 228), `chebyshev.cpp:177-178` (`AssembleDiagonal` at 177 + `Reciprocal` at 178 — exact), `distrelaxation.cpp:13-36`, `divfree.cpp:128`, `multigrid.hpp:78-126`, `fespace.cpp:240`, `hcurl.cpp:101`, `errorestimator.cpp:86` — all anchor-confirmed in range. The RE5/RE7 grounding site (`chebyshev.cpp:177-178`), the RE9 prolongation site (`ksp.cpp:221`), and the `ksp.cpp:228` / spine-dependency `divfree.cpp:128` are exactly correct. The **warning** is for a systematic **+1 drift in the fine-grained inline pinpoints** in the "Supporting evidence" section (CYCLE.md:421-429) and the L4 vcycle code-block comments (CYCLE.md:133-141): several cited single-line refs land one line short of the anchor (see Issues). These all fall *inside* the load-bearing `gmg.cpp:172-205` envelope, so no `cites-evidence` edge target is wrong; the drift is purely in narrative line annotations.

**surface-or-evidence — pass.** Feature-surface composition-root kind: applied the adapted check. The column's evidence is the L0 driver-source range (`gmg.cpp:126-205` VCycle/Mult + `ksp.cpp:207-234` construction) PLUS the constituent down-links — both present and resolving. No new per-op algebraic claim is made (the per-op evidence lives in the linked constituents), correctly so. Record-definition sub-check: the L4 signature names `MultigridConfig`; the report does NOT silently use-without-defining — it explicitly flags `record-MultigridConfig-needs-definition-home` in Open questions (CYCLE.md:472-480) with the L0 home (`ksp.cpp` `LinearSolverData` / `IoData Solver.Linear`), routing it to the record-definition dispatcher. That satisfies the producer obligation (define-or-flag), so no record-home failure.

**rotation-quality — pass (not applicable to feature-surface kind).** A feature/composition-root chapter rotates nothing — it recomposes already-firm vocabulary outward. Formal no-op per the adapted checklist.

**variant-axis-coverage — pass (not applicable to feature-surface kind).** The variant axes (Chebyshev-1st-kind vs 2nd-kind smoother, DistRelaxation/Hiptmair-when-auxiliary-space-present vs bare ChebyshevSmoother) live in the constituent smoother chapters, not this column. The report nonetheless correctly *narrates* the auxiliary-space branch (`gmg.cpp:42-46` DistRelaxationSmoother vs `:50-60` bare Chebyshev) rather than hiding it. No-op for this kind; no hidden branch.

**cross-reference-integrity — warning.** Load-bearing for this kind (the composition-root's value IS its down-links). All constituent chapters exist on disk EXCEPT `L1/multigrid-relaxation-smoother.md`, which is **not yet on disk** — a disclosed D3 forward-reference (CYCLE.md:23,58-60,458). Live `[link]`s and `depends-on` edges point at it; this is a hard `linkcheck2` error unless D3 lands the file in the same integration. Maturity-claim cross-check (the directive's "does on-disk `## Status` match the claim?" sub-check): **every other constituent's claimed status matches on disk** — `preconditioning-framework` firm, `fe_space_hierarchy` firm (and `GetProlongationOperators` is referenced there, ×2), `chebyshev` `partial-obstruction` (exact `## Status` match — load-bearing for the rough-in argument), `jacobi-smoother` firm, `reciprocal` firm, `normalize` firm, `divfree-projector` firm. No maturity overclaim. The SUMMARY.md / index.md edit anchors both exist and match exactly; the new top-level grouping nests correctly (0-indent group + 2-space children, mirroring `Output-product columns`, placed before `# Semantic surface`). Two minor convention drifts in the new `infrastructure.md` (see Issues). Warning driven solely by the not-yet-on-disk forward-referenced file.

**edge-label-fidelity — pass.** The `depends-on (composes)` edges each name a constituent the prose actually composes, and the rank-invariant / well-foundedness claim is sound. Verified `rank(u) ≤ rank(v)` for every blocking edge at rough-in (rank 2): preconditioning-framework/fe_space_hierarchy/jacobi/reciprocal/normalize firm (3) ≥ 2; chebyshev partial-obstruction (~2.5) ≥ 2; multigrid-relaxation-smoother rough-in (2) ≥ 2. The report's claim "held at rough-in by the smoother leg" is correct: the column cannot be firm because `multigrid-relaxation-smoother` is not yet firm, so the well-foundedness cap binds exactly there. The `reference`-class edges (to lifecycle.L4, eigenmode.L4, the sibling columns) correctly carry no rank constraint. The L4-vs-L3 chebyshev edge-target choice is flagged by the producer as deliberate (CYCLE.md:499-504), not an oversight.

**plan-kind-consistency — pass.** Declared `kind: feature-surface`, `rank: rough-in`, `feature_root: seed` — content shape matches: a composition-root that wires constituents by name, links DOWN, makes a compositional (not per-op-algebraic) claim. The new infrastructure / shared-substrate sub-kind is coherently introduced with its own group-intro page in the same landing (per the new-summary-kind-grouping rule). The `rough-in` (not firm) classification is correctly justified by the well-foundedness gate, not a placeholder-with-firm-label mismatch. The dual `feature_root: seed` (root marker, separate axis) + `rank: rough-in` (ladder rung) is the correct two-axis treatment.

**skill-uptake-survey — pass (telemetry).** The report references the codemap `read_range` verification path and the partly-constructive/well-foundedness discipline. No specific skill invocation is mandatory for the feature-surface composition-root shape; the proposed-changes-fence-encloses-full-body guard is satisfied (the full chapter bodies are INSIDE the `new-file:` fences, not authored as the report's own top-level sections). Pure presence check; nothing blocking.

**rank-invariant (graded-stack) — pass.** See edge-label-fidelity: every `depends-on` dep is rank ≥ the entry's own rough-in (2). No over-claim above a dep's rank.

**reachability (graded-stack) — pass.** The column carries `feature_root: seed` — it IS a GC root (the FEATURE-SURFACE SPINE root set), reachable by definition; and it makes RE9/RE1/RE5/RE7 reachable through its composition chain (the c122 re-check target), which is the intended liveness contribution.

### Issues found

1. **(citation-validity, warning, minor) +1 inline-pinpoint drift in `gmg.cpp` narrative refs.** In CYCLE.md "Supporting evidence" (lines 423-429) and the L4 vcycle code-block comments (lines 133-141), several fine-grained single-line refs are off by +1 vs the `citecheck --anchor` authoritative line map: pre-smooth `Mult2` cited `:185` → true **184**; restrict `RealMultTranspose` cited `:192` → true **191**; recurse `VCycle(l-1,false)` cited `:197` → true **196**; prolong-add cited `:200-201` but `RealMult` is at **199** (`Y[l] += R[l]` at 200); coarse-solve `l==0` cited `:178-184` → the `l==0` test is at **178** (block 177-183). Post-smooth `MultTranspose2` `:204` and `AXPBY` `:188` are correct. All land inside the cited `gmg.cpp:172-205` envelope, so no edge target is wrong; this is narrative-annotation drift only. Repair = renumber the inline refs to the anchor-true lines.

2. **(cross-reference-integrity, warning, load-bearing) `L1/multigrid-relaxation-smoother.md` not on disk.** The column carries live `[link]`s + two `depends-on (composes)` edges (L4 and L1 surfaces) + a constituent-table row to `book/src/L1/multigrid-relaxation-smoother.md`, which does not exist (confirmed MISSING). Disclosed as a D3 same-cycle forward-reference, but it is a hard `linkcheck2` error if D3's file does not land in the same integration. Integrator must either confirm D3 lands the file first or materialize a `stub` (the preferred resolution per the stub policy) so the link resolves.

3. **(cross-reference-integrity, minor) `infrastructure.md` "third feature sub-kind" off-by-one.** CYCLE.md:371 (the new `infrastructure.md` body) says "The third feature sub-kind, alongside the Spine ROOT (lifecycle), Driver-leaf columns, and Output-product columns" — it lists THREE pre-existing kinds and calls itself the third; it is the **fourth** sub-kind (or "the fourth, the third non-root"). Wording fix.

4. **(cross-reference-integrity, minor) `infrastructure.md` group-intro convention drift.** (a) Its `reference` edges list only `feature/geometric-multigrid-preconditioner.L4` whereas the established group-intros (`output-product.md`, `driver-leaf.md`) list every level (L4/L1/L0) of each grouped column — the .L1 surface is omitted. (b) The `kind:` token is `navigational-container (feature Part sub-grouping intro)` vs the established `navigational-container (feature group intro)`. Both functionally navigational-container; harmonize for consistency.

5. **(observation, non-blocking) strawman notation path.** CYCLE.md:119 cites the notation home as `book/src/semantics/index.md`; that file exists on disk (the active semantic surface), so the citation resolves. Note CLAUDE.md still names `book/src/design/l4_calculus.md`, which does NOT exist — the surface appears to have been relocated to `semantics/index.md`. The report's path is the correct (live) one; flagged only as a cross-cycle consistency note, not a defect in this report.

---

## Repair

### Fixes attempted

- **Finding 1 — citation-validity (warning): +1 inline-pinpoint drift in `gmg.cpp` narrative refs.**
  - **Decision:** repaired.
  - **Action:** Re-verified the VCycle region against the disk-authoritative source `reference/palace/palace/linalg/gmg.cpp:126-205` (read directly from disk — the critic's `citecheck --anchor` map was confirmed exactly; codemap `read_range` is NOT source-of-truth per the critic). Renumbered every drifted narrative pinpoint to the anchor-true line in BOTH the "Supporting evidence" section (CYCLE.md ~426-429) AND the L1 pure-V-cycle code block (CYCLE.md ~313-318), which carried the same (and a larger) drift:
    - pre-smooth `Mult2`: `:185`→**184** (Supporting ev.); L1 block `:178`→**184**.
    - residual: split `:188-189`→`A[l]->Mult` **187** + `AXPBY` **188**; L1 block `:182-183`→**187-188**.
    - restrict `RealMultTranspose`: `:192`→**191** (Supporting ev.); L1 block `:186`→**191**.
    - recurse `VCycle(l-1)`: `:197`→**196** (Supporting ev.); L1 block `:190`→**196**.
    - prolong-add: `:200-201`→`RealMult` **199** + `Y[l]+=R[l]` **200**; L1 block `:193-194`→**199-200**.
    - coarse-solve base case: `:178-184`→**178-183** (Supporting ev.); L1 §3 `gmg.cpp:131-134` (was the MFEM_ASSERT lines, not the coarse solve)→**178-183** (`B[l]->Mult` at `:181`).
    - L1 §"composed pieces" restrict/prolong L0 refs `:186`/`:193`→**191**/**199**.
    - post-smooth `MultTranspose2` `:204` was already correct (left as-is).
  - All corrected refs stay inside the sound `gmg.cpp:172-205` envelope (no `cites-evidence` edge target changed). Re-ran `citecheck --scan` on the repaired report: **40 ok, 0 failing** (was 39; the `:188-189`→`:187`+`:188` split adds one). Within repair authority ("citation line range off by a small offset").

- **Finding 2 — cross-reference-integrity (warning, load-bearing): `L1/multigrid-relaxation-smoother.md` not on disk.**
  - **Decision:** unrepairable (deferred-to-integration / not-a-repair).
  - **Rationale:** This is a *sanctioned same-cycle D3 forward-reference* — D3 (`reports/2026-06-07T054924Z-harvester-multigrid-relaxation-smoother/CYCLE.md`) authors the file THIS cycle. The live `[link]`s + two `depends-on (composes)` edges + the constituent-table row are CORRECT as authored and were left intact (deleting them would be the wrong fix). Resolution is an integration-sequencing action, not a mechanical edit: the integrator must sequence D3's per-report apply before/with D1, OR materialize a `stub` at `book/src/L1/multigrid-relaxation-smoother.md` (the preferred stub-policy resolution) so the link resolves under `linkcheck2`. That is integrator authority, outside repair scope.

- **Finding 3 — cross-reference-integrity (minor): "third feature sub-kind" off-by-one.**
  - **Decision:** repaired.
  - **Action:** `infrastructure.md` body (CYCLE.md ~372): "The third feature sub-kind, alongside [Spine ROOT], [Driver-leaf], and [Output-product]" → **"The fourth feature sub-kind, alongside …"** (it lists three pre-existing sub-kinds and is itself the fourth). Surgical wording fix.

- **Finding 4 — cross-reference-integrity (minor): `infrastructure.md` group-intro convention drift.**
  - **Decision:** repaired.
  - **Action:** Verified the established convention against the sibling group-intros on disk (`book/src/feature/output-product.md`, `driver-leaf.md`). Harmonized the new `infrastructure.md` frontmatter to match: (a) `kind:` token `navigational-container (feature Part sub-grouping intro)` → **`navigational-container (feature group intro)`** (+ matched the established frontmatter comment text); (b) added the omitted **`feature/geometric-multigrid-preconditioner.L1`** `reference` edge (the established group-intros list every on-disk level of each grouped column; GMG has L4+L1, no L0 — consistent with the index.md `—` L0 cell).

- **Finding 5 — observation, non-blocking: strawman notation path.**
  - **Decision:** not-needed (the critic flagged it as a cross-cycle consistency note, not a defect in this report; the report's `semantics/index.md` path is the live one).

### Unrepairable findings

- **`L1/multigrid-relaxation-smoother.md` forward-reference (Finding 2).** Resolves at integration, not by the repairer. Routing: **`integrator-per-report`** must sequence D3 (`reports/2026-06-07T054924Z-harvester-multigrid-relaxation-smoother/`) before/with this D1 report in the serial per-report apply order, OR create a `book/src/L1/multigrid-relaxation-smoother.md` stub so the live links resolve. Do NOT delete the live links / edges — they are correct as authored.

## Suggested resolution

`needs-revision` — NOT because the report has an unfixed defect of its own (all of its own warnings/minors are now repaired and the mechanical citecheck is clean: 40 ok, 0 failing), but because the one remaining warning is an integration-sequencing dependency that the integrator must discharge. **Action for `integrator-per-report`:** apply D3 (`multigrid-relaxation-smoother`) before/with this report, OR stub `book/src/L1/multigrid-relaxation-smoother.md`; then this column's live links + `depends-on` edges resolve and the column is integrable as-authored at `rank: rough-in`. No content authoring is outstanding on D1's side.
