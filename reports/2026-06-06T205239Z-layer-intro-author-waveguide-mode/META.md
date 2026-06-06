---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T211500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: warning
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-06T212000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: repaired
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "waveguide-mode 6th output-product feature column"

## Critique

This report authors a **feature-surface composition-root column** (the `waveguide-mode` output product, new files `book/src/feature/waveguide-mode.{L4,L1,L0}.md`) plus the sole-owned shared `feature/index.md` + `feature/output-product.md` + `SUMMARY.md` edits. The 8-check checklist is applied with the FEATURE-SURFACE composition-root adaptations (rotation-quality / variant-axis-coverage no-op; surface-or-evidence and cross-reference-integrity adapted/load-bearing per the codified composition-root rules).

### Checks run

1. **citation-validity — pass.** Ran `citecheck.py --scan` on the report: **30 ok, 0 failing** — all bounds in range, all paths hygienic. Hand-verified the load-bearing pinpoints against an on-disk read of `reference/palace/palace/drivers/boundarymodesolver.cpp:195-344`: the report-loop `:273` (`for (int i = 0; i < num_conv; i++)`), `:275` (`auto kn = eig.GetPropagationConstant(i)`), `n_eff` print `:276-277`, readout loop `:292`, `GetEigenvector(i,e0)` `:297`, `GetPropagationConstant` `:299`, `ApplyVDBackTransform` `:300`, `ComputePoyntingPower` `:304`, power-normalization `:305-307`, `MeasureAndPrintAll` `:314`, `IsPropagating` branch `:316`, the `Bz` block `:318-331` / `CurlOp.Mult` `:326-327` / accumulations `:328-331`, `AddErrorIndicator` `:332`, `MeasureFinalize` `:337`, return `:339-340` — **all confirmed at the cited lines.** One sub-tolerance nit (NOT a fail): the report cites the per-pair error reads at `:309-310`, but `error_bkwd` is at line 310 and `error_abs` at line 311 — the lower bound 309 is a blank line and the upper bound 310 captures only the first of the two reads (`error_abs` at 311 sits just outside). `citecheck --anchor 'error'` confirms line 310 is in range and is an error read, so the anchor resolves and bounds pass; the range is one line short of enclosing both reads. Minor.

2. **surface-or-evidence — warning.** Adapted for the composition-root kind: the evidence shape is the **L0 driver-range + constituent down-links**, not a single decomposed-op site. That bar is met — the L0 readout range `boundarymodesolver.cpp:273-340` is cited and self-verified, the `boundary-mode.{L4,L1,L0}` down-links all resolve on disk, and the composed `eigsolve` is firm (on-disk `L1/eigsolve.md:4` `rank: firm`, Status lines 178-188). The composition is supported (no phantom constituent). **The warning is the record-definition obligation:** the output record `WaveguideModeTable` / `WaveguideModeResult` is NAMED in signatures across all 3 waveguide-mode chapters (and cross-named `BoundaryModeResult` in the 3 boundary-mode chapters) but has **no definition home** — no in-chapter `## Record definition` section and no `concepts/<record>.md` page exists yet. The producer correctly and explicitly flags this as Open question `record-WaveguideModeResult-needs-definition-home` (≥2-consumer bar → routes to a concept page), enumerating the fields. This is the acknowledged-and-routed path, not an unflagged gap — hence `warning`, not `fail`. (The *input* config record `BoundaryModeConfig` HAS a home: the `concepts/config-record` page exists on disk and the L4 chapter carries the resolving `uses-record` edge to it — that record is fine.)

3. **rotation-quality — pass (not applicable to feature-surface kind).** A composition-root rotates nothing; it recomposes already-firm vocabulary outward. The chapters make no new per-op algebraic claim, correctly deferring per-op algebra to the linked constituents and L0 sites.

4. **variant-axis-coverage — pass (not applicable to feature-surface kind).** No variant axes of its own; the propagating-vs-non-propagating split (the `IsPropagating` branch, `Bz` present only for propagating modes) is faithfully reflected as `Bz : Maybe (Tensor[N_curl, complex])` in the shape contract and as the conditional in the L1 comprehension, matching the source `if (... IsPropagating(kn))` at `:316`.

5. **cross-reference-integrity — warning.** **Load-bearing for this kind.** All `[link]` targets resolve on disk (boundary-mode {L4,L1,L0}, sparameters {L4,L1,L0}, energy-fields.L4, eigsolve {L1,L4}, fe_assemble {L1,L4}, participation_ratio, matrix-weighted-norm, gram_reduce, sparameter_reduce, semantics/index.md). All six `feature/index.md` / `output-product.md` / `SUMMARY.md` edit old-string anchors are present and **unique** (count=1 each), so the edits apply cleanly and insert in correct alpha+high→low position. **The warning is a maturity-claim coupling:** the index edits (edit 4 promoting the `firm`-block to "12 columns" with boundary-mode firm; edit 3 / edit 5 reflecting boundary-mode's cleared gate) assert boundary-mode is now `firm`, but the on-disk `feature/boundary-mode.L4.md` is still `feature_root: seed` / `rank: rough-in` with a `## Status` line reading `seed` (verified this dispatch). The promotion is owned by the co-dispatched **D2** boundary-mode dispatch; the producer explicitly flags this in Open questions ("If D2 does NOT land this cycle, the index-cell calling boundary-mode `firm` will lead its chapter `## Status` — flag for finalize to reconcile"). So this is an acknowledged cross-dispatch coordination dependency, not an unflagged overclaim — but it is a real integrity coupling the integrator must enforce (both land or both defer). Hence `warning`.

6. **edge-label-fidelity — pass.** The `depends-on` edges carry `composes` (to boundary-mode), `cites-evidence` (to the L0 driver range), and `uses-record` (to config-record); each kind matches its prose role. No L_{n+1}→L_n edge label is mis-applied. The within-column high→low (L4→L1→L0) ordering and the "this records only the L_n composition, lower lift in working notes" discipline are honored in all three chapters.

7. **plan-kind-consistency — pass.** Declared `kind: feature-surface`, `status/feature_root: seed`, `rank: rough-in`. Content shape is a genuine composition-root (config→product, down-links, no new algebraic claim, composes firm vocabulary), matching directive-B front (i). The `seed`/`rough-in` landing is correctly justified under the OWN-COMPOSITION rule (own reduce verb `waveguide_mode_reduce` has no firm L4 home), parallel to the cited `sparameters`-pre-c083 precedent. Rank-invariant (graded check 9) holds: a `rough-in` (rank 2) entry resting on `rough-in` deps (boundary-mode rough-in; the unhomed reduce verb) satisfies `rank(u) ≤ rank(v)`. Reachability (graded check 10) holds: wired into the index matrix, the output-product group-intro, and SUMMARY, hanging off the boundary-mode driver root.

8. **skill-uptake-survey — pass.** The report's shape (output-product column authoring) does not imply a single dedicated skill; it correctly USES+LINKS the semantic-surface §1.2.1 named-shape-groups convention (linked to `semantics/index.md`, not restated) per the SEMANTIC-CONSOLIDATION discipline, and reuses the documented index-cell-drift / OWN-COMPOSITION / record-definition procedures. No missing skill invocation surfaced.

### Issues found

- **[warning] surface-or-evidence — `CYCLE.md` §Open questions / the 3 new chapters.** The output record `WaveguideModeTable` / `WaveguideModeResult` is named in signatures across 6 chapters (3 waveguide-mode + 3 boundary-mode, where it is cross-named `BoundaryModeResult`) but has no definition home (no in-chapter `## Record definition` section, no `concepts/` page). Explicitly flagged as `record-WaveguideModeResult-needs-definition-home` and routed to a concept page with fields enumerated — acknowledged-and-routed, but unresolved this cycle. Severity: low-medium (record described by USE only until the flagged concept page lands; also carries an unreconciled naming dual `WaveguideModeTable` vs `WaveguideModeResult` vs the boundary-mode `BoundaryModeResult`, which the producer notes the future concept page should settle).

- **[warning] cross-reference-integrity — `CYCLE.md` index edits 3, 4, 5 (`book/src/feature/index.md`).** The index edits assert boundary-mode is `firm` (12-column firm block; cleared own-readout gate), but on-disk `feature/boundary-mode.L4.md` is still `seed` / `rough-in`. The body promotion is owned by the co-dispatched D2; the producer explicitly flags the coupling and requests finalize reconcile both-land-or-both-defer. Severity: medium — if D2 does not land, the index will overclaim boundary-mode's maturity (the exact index-cell-drift the producer warns of). Integrator must enforce the joint-land/joint-defer.

- **[nit] internal-consistency — `CYCLE.md` §Open questions, "Boundary-mode chapter-body promotion is owned by D2" bullet.** References "index edits 3/5/6", but the report contains only index edits 1–5 (no edit 6); the intended set appears to be 3/4/5. Cosmetic; does not affect application.

- **[nit] citation-validity — `CYCLE.md` §Source-range self-verification + L0 chapter.** The per-pair error-read citation `boundarymodesolver.cpp:309-310` encloses `error_bkwd` (line 310) but not `error_abs` (line 311); a one-line-short range. Anchor resolves and bounds pass, so non-blocking; tightening to `:310-311` would be exact.

## Repair

### Fixes attempted

- **Finding**: surface-or-evidence (warning) — output record named inconsistently (`WaveguideModeTable` vs `WaveguideModeResult` vs `BoundaryModeResult`); naming dual must reconcile to one canonical name.
  - **Decision**: repaired
  - **Action**: Reconciled the naming dual to ONE canonical record name **`WaveguideModeTable`** across the report. Decision basis: the critique's rule is "prefer `WaveguideModeResult` (the OQ slug) UNLESS the chapters predominantly use another." All 6 chapter-body proposed-change signature/output sites (`CYCLE.md:68,84,108,113` L4 + `:178,204` L1) **already uniformly use `WaveguideModeTable`** — the only stray uses of `WaveguideModeResult` were the Summary prose (`CYCLE.md:16`) and the OQ bullet/slug (`CYCLE.md:419`), neither inside a proposed-change block. So `WaveguideModeTable` is the chapter-predominant name and is canonical; reconciling the two outliers to it (rather than renaming all 6 chapter signatures to `WaveguideModeResult`) is the smaller, more-mechanical edit. Edits: (1) `CYCLE.md:16` Summary — `WaveguideModeResult` → `WaveguideModeTable`; (2) `CYCLE.md:419` OQ — renamed the slug `record-WaveguideModeResult-needs-definition-home` → `record-WaveguideModeTable-needs-definition-home` and rewrote the bullet to declare `WaveguideModeTable` canonical, retaining the note that the future ≥2-consumer concept page reconciles the boundary-mode chapters' cross-name `BoundaryModeResult` (owned by D2, outside this report's proposed-change blocks) to the canonical name. The proposed-change blocks are now internally consistent on `WaveguideModeTable`, and the OQ slug matches. The record-definition home itself stays deferred-to-concept-page (correctly flagged, non-blocking) — this repair settles only the NAME, not the home.

- **Finding**: cross-reference-integrity (warning) — index edits 3/4/5 assert boundary-mode `firm` while on-disk `feature/boundary-mode.L4.md` is still `seed`/`rough-in`; a both-land maturity coupling with co-dispatched D2.
  - **Decision**: not-needed (coupling SATISFIED; no mechanical repair appropriate in D1)
  - **Action**: None to the index-cell delta — it is left intact and is CORRECT given D2 lands. Per the dispatch context, D2 (the boundary-mode promotion, `overall_status: ready`) DOES land this cycle, flipping the boundary-mode chapter bodies `rank: rough-in → firm` and `feature_root`/`## Status` to firm. After integration the index-cell (firm) and the on-disk chapter bodies (firm) WILL match, so the both-land coupling holds. D1's index-cell reflection of boundary-mode→firm (edit 4 `firm (12 columns)` block, edit 3 directive-scope line, edit 5 `seed` block now holding only waveguide-mode) is the correct half of the joint promotion and must NOT be removed. **Integrator-finalize note**: verify D1 (this report) and D2 (boundary-mode promotion) land in the SAME cycle — both the index-cell delta (here) and the boundary-mode body flips (D2) must apply together; if D2 were to defer, the index-cell would lead the chapter bodies (the index-cell-drift the producer warned of) and finalize must reconcile (both-land-or-both-defer). Given D2 is ready, the joint-land condition is met.

- **Finding**: citation-validity (nit) — per-pair error-read range `boundarymodesolver.cpp:309-310` is one line short (captures `error_bkwd`@310, misses `error_abs`@311).
  - **Decision**: repaired
  - **Action**: Tightened to `:310-311` (exact) in both occurrences: the §Source-range self-verification table (`CYCLE.md:41`) and the L0 chapter mode-field readout loop (`CYCLE.md:270`). Verified against on-disk source via codemap `read_range boundarymodesolver.cpp:308-312` — `error_bkwd` is at line 310, `error_abs` at line 311; `:310-311` is exact. Small-offset slip, squarely in repair authority.

- **Finding**: internal-consistency (nit) — §Open questions D2-ownership bullet references "index edits 3/5/6" but the report has only edits 1–5.
  - **Decision**: repaired
  - **Action**: Corrected "index edits 3/5/6" → "index edits 3/4/5" (the intended set: the three index edits reflecting boundary-mode's cleared gate) at `CYCLE.md:421`. Cosmetic; no application impact.

### Unrepairable findings

None. Both warnings resolved (surface-or-evidence naming dual reconciled mechanically; cross-reference-integrity coupling confirmed satisfied by co-dispatched D2 landing this cycle) and both nits applied. No substantive authoring was required — the record-definition home and the `waveguide_mode_reduce` L4 verb home remain correctly-flagged deferred Open questions (the demand-gate / promotion route), not repair-phase obligations.

## Suggested resolution

`ready`. Notes for the integrator-finalize:
- **Both-land coupling (load-bearing)**: This report (D1) and D2 (boundary-mode promotion, `overall_status: ready`) MUST land in the same cycle. D1 carries the `feature/index.md` cell reflecting boundary-mode→`firm` (edits 3/4/5); D2 carries the boundary-mode chapter-body `rank`/`feature_root`/`## Status` flips. Apply both together — if D2 unexpectedly fails to apply, reconcile by deferring D1's three boundary-mode-firm index edits (3/4/5) to avoid index-cell-drift (index leading chapter bodies). Given D2 is ready, expect a clean joint land.
- Record name is now canonical **`WaveguideModeTable`** throughout this report; the OQ slug `record-WaveguideModeTable-needs-definition-home` (deferred ≥2-consumer concept page) and the `waveguide-mode-reduce-needs-l4-verb-home` verb-home OQ are both legitimate forward-gates to promote into the plan, not blockers for this `seed`/`rough-in` landing.
