---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T071500Z
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
repaired_at: 2026-06-01T072500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "two adjacent thin-identity lowering themes — assemble-diagonal (L2>L1 + L3>L2)"

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` reports 12 ok / 0 failing. I `--anchor`-verified every load-bearing pinpoint: `hypre.cpp:88` (`hypre_CSRMatrixExtractDiagonal`), `operator.cpp:139` (`CeedOperatorLinearAssembleAddDiagonal`), `rap.cpp:163-164` (`convergent`), `test-libceed.cpp:367-376` (`rtol` @371,375), `rap.cpp:174` (`P`), `operator.cpp:85-96`, `rap.cpp:467-479`, and the cross-artifact anchor `krylov-step-body-identity.md:97` (`L3-native`) — all OK. The load-bearing matrix-free high-order-Nedelec approximate-diagonal non-law is genuinely present at both endpoints: `L1/assemble-diagonal.md:58` ("Exactness across representations") and `L3/assemble-diagonal.md:77` (same non-law, "the representation can change the diagonal *value*"), each positively anchored at `rap.cpp:163-164` + `test-libceed.cpp:367-376`. The report's coarser section-anchor citations (e.g. L1 laws `:47-52`, non-laws `:54-59`, evidence `:100-119`; L3 sig `:34-35`, marker `:54-60`, "Lowers to" `:128-134`) all land in-range and on the correct section by Read. No `verified_against:` YAML block is emitted (the report uses a prose §Verified-against section), so the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** Not a refinement of existing surface; both proposals are `new:` theme files (two new chapters), not edits to existing operator/theme text. The `edit:` blocks touch only index tables + SUMMARY registration (wiring), which is the expected new-chapter plumbing, not surface modification of an existing entry. New-content shape; check no-ops favorably.

**rotation-quality — pass (identity-in-form, correctly justified).** Both themes assert an *identity-in-form* rotation, not a compaction rotation, and they justify it correctly: the operator is value-thread-isomorphic across each edge (same signature, same six laws + four non-laws, same one-orthogonal + one-absorbed variant profile). This is the sanctioned identity-lowering case (CLAUDE.md "Identity-lowerings still require both L levels"), exercised as the precedented `dot-leaf-identity` / `dot-body-identity` shape. The report does not over-claim a compaction that isn't there; the §"The rewrite" tables are explicitly total-and-bijective identity maps. The one genuine rotation content (the L2 kernel-fusion de-fusion) is correctly identified as *degenerate* for `assemble_diagonal` (no fold-parent, no multi-operation fusion at the operator-to-data boundary) and deferred to L1>L0 — not erased. This is a faithful identity claim, not a renaming-only mislabel.

**variant-axis-coverage — pass.** The operator's variant axes (one orthogonal element-type, one absorbed operator-representation) are explicitly carried unchanged across both edges and the §"The rewrite" tables enumerate the representation-absorption row. No hidden branch: the four representation realizations (sparse-CSR / matrix-free / parallel-wrapped / complex-wrapped) are named and scoped to the L1>L0 lowering, and the load-bearing exact-vs-approximate value split (the one place the absorbed axis surfaces semantically) is preserved by reference. Confirmed against `L1/assemble-diagonal.md:75-89` and `L3/assemble-diagonal.md:100-118`, which carry the identical profile.

**cross-reference-integrity — pass.** All live-link targets resolve: `L1/assemble-diagonal.md` (firm, on disk), `L3/assemble-diagonal.md` (firm, on disk), `dot-leaf-identity.md` / `dot-body-identity.md` / `krylov-step-body-identity.md` (on disk), `L1-L0/assemble-diagonal-mutation-rotation.md` (on disk). `L2/assemble-diagonal.md` is referenced as a live link but is **not yet on disk** — this is the explicitly-declared co-landing D4 dependency (frontmatter `inputs`, §Summary, §Context), with wave-2 serial sequencing applying D4 before these themes; flagged as a sequencing presupposition below, not a broken link, since the integrator applies D4 first this cycle. `apply_linop` is referenced only as prose (no live link), so its slug needn't resolve — and it exists anyway (`book/src/L1/apply_linop.md`, `book/src/L3/apply_linop.md`). The `edit:` blocks anchor to real existing rows (`nrm2-fold-specialization` in L2-L1 index, `scal-body-identity` in L3-L2 index) and real SUMMARY context lines (`SUMMARY.md:71`, `:46`); no preexisting duplicate of the two new slugs. Firm-body-inside-fence guard: both `new:` bodies enclose their full apparatus (`## Status` + Signature + rewrite + Verified-against) INSIDE the fence — verified by fence enumeration (12 ` ``` ` markers, even parity, 6 balanced blocks; no nested fences); no fence-truncation defect.

**edge-label-fidelity — pass.** L2>L1 theme (`assemble-diagonal-leaf-identity`): LHS = L2 floor, RHS = L1 leaf; §"L2 form (LHS)" → §"L1 form (RHS)" → §"The rewrite (L2 → L1)" — narration is consistently high→low (L_{n+1} LHS lowering forward into L_n RHS). L3>L2 theme (`assemble-diagonal-body-identity`): LHS = L3 field op, RHS = L2 floor; §"L3 form (LHS)" → §"L2 form (RHS)" → §"The rewrite (L3 → L2)" — same forward high→low direction. The dep-map rows in both index `edit:` blocks place L3/L2 as the LHS column and L2/L1 as the RHS column, matching. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is two `firm` themes; content shape matches. Each carries a complete `## Status: firm` with the firm-on-syntactic-identity-laws rationale (value-thread-isomorphic on a firm L1 home; laws are syntactic identities on the matrix-diagonal map), explicitly distinguishing `firm` from `partly-constructive` (no negative-anchor reconstruction) and from `rough-in (test-coverage-bounded)` (the missing bare-operator test does not gate syntactic-identity laws — the `apply_linop` escape, correctly invoked). No rough-in placeholders inside a firm-claimed body. The slug convention is correct: `-leaf-identity` / `-body-identity` (matching the cycle-041 `dot-*` landed convention), explicitly NOT the `-fold-specialization` outlier — appropriate, since `assemble_diagonal` is fork-independent and has no fold to specialize.

**skill-uptake-survey — pass (telemetry).** The report references `tools/citecheck/citecheck.py --anchor` as self-invoked on the L0 anchors this invocation, consistent with the `verify-citation-range` mechanical realization. The thin-identity shape is precedented (cycle-041 `dot-*`) and the report follows it explicitly. No unreferenced obviously-relevant skill.

### Issues found

No blocking issues. The report is clean against all eight checks. The items below are non-blocking observations recorded for the repairer / integrator, all of which the report itself already surfaces in §Open-questions.

1. **(informational, sequencing presupposition — already declared) `L2/assemble-diagonal.md` is a live link to a not-yet-on-disk target.** Both theme bodies and both index rows link `../L2/assemble-diagonal.md`, which lands only when D4 (wave-1 harvester) is applied. The report declares this co-landing dependency in frontmatter `inputs`, §Summary, §Context, and §Supporting-evidence, and notes wave-2 serial sequencing applies D4 first. Where: both `new:` blocks (CYCLE.md:28, :289) + both index `edit:` rows (CYCLE.md:535, :540). Severity: low — contingent on the integrator honoring the stated D4-before-themes ordering; if D4 slips, `linkcheck2` would fail on these links. Flagged so the integrator confirms the ordering (not a defect in this report).

2. **(informational — already declared as a caveat, NOT a proposed change) stale §"Lowers to" / §"Downward" on `L3/assemble-diagonal.md`.** Confirmed accurate: `L3/assemble-diagonal.md:128-134` currently records the L3 lowering as "identity-in-form on the primitive's signature — **no interposed L2 entry and no `L3-L2`/`L3-L1` theme file**" via the cycle-012 non-adjacent convention, and `:28` ("Downward") says the same. With this `assemble-diagonal-body-identity` theme + the D4 L2 floor present, those passages become stale (the L3 form now lowers to an adjacent L2 parent via this theme). The report correctly files this as a downstream lifter/repairer touch (out of this dispatch's one-theme scope), mirroring the `dot-body-identity` precedent. Where: §Open-questions, CYCLE.md:611-621. Severity: low; a follow-up consistency touch, not a defect introduced here.

3. **(informational — count-ownership correctly deferred) no consolidated-tally update.** Per the dispatch's count-ownership instruction, the report appends ONLY the two theme rows (one per index), two SUMMARY entries, and the two bodies — it does NOT touch the consolidated L2>L1 / L3>L2 firm-count / coverage-gap tallies (D11-owned). Verified: the `edit:` blocks add exactly one row to each index table and one SUMMARY line per index; no tally line is in the diff. Where: §Open-questions, CYCLE.md:623-629. This is the intended partition (count-divergence avoidance); flagged so the integrator knows the tally update is intentionally absent and routed to D11.

4. **(informational — fork-independence) themes correctly scoped OUT of the `dot-l2-leaf-floor-vs-fold-only-design` fork.** Both bodies carry a §Status fork-independence note asserting `assemble_diagonal` has NO fold-parent (operator-to-data sibling of `apply_linop`), so neither edge presupposes the wave-1 (b) leaf-floor reading and neither re-anchors under the (a) fold-only reading. This is internally consistent with the L1/L3 home chapters, which both record `assemble_diagonal` as the `apply_linop` sibling, explicitly "not an `apply_linop` variant" and not a BLAS-1/fold member. Surfaced for the batch-12 meta-phase (do-not-sweep-into-fork). No action needed; correct scoping.

---

## Repair

### Fixes attempted

All 8 checks returned `pass` from the critic with no blocking issues. The four §"Issues found" items are non-blocking informational/follow-up observations, each already self-surfaced in the report's §Open-questions. None is a defect in this report, so no per-check repair was applicable; all `repairs:` entries are `not-needed`.

- **Finding 1**: `L2/assemble-diagonal.md` is a live link to a not-yet-on-disk D4 co-landing target.
  - **Decision**: not-needed.
  - **Rationale**: not a defect in this report. The link is a correctly-declared co-landing dependency (frontmatter `inputs`, §Summary, §Context, §Supporting-evidence) under wave-2 serial sequencing that applies D4 before these themes. Converting the live link to plain-text would be wrong (the target lands this cycle); the resolution is the integrator honoring the stated D4-before-themes ordering, which is integrator-phase scope, not a repair edit. Recorded for the integrator in §Suggested resolution.

- **Finding 2**: stale `L3/assemble-diagonal.md` §"Lowers to" / §"Downward" (cycle-012 non-adjacent "no interposed L2 entry / no `L3-L2` theme" passages become stale once the D4 L2 floor + this `assemble-diagonal-body-identity` theme land).
  - **Decision**: not-needed (here) → routed as a follow-up OQ for a future lifter touch.
  - **Rationale**: out of repair authority on two counts — (a) the stale passages live in `book/src/L3/assemble-diagonal.md`, an existing artifact entry the repairer must not modify directly; (b) re-writing the §Downward / §Lowers-to prose to narrate the now-adjacent L3>L2 lowering is substantive authoring, not a mechanical/surgical edit. The report already files this in §Open-questions (CYCLE.md:611-621), mirroring the `dot-body-identity` precedent. Routed to a downstream `lifter` consistency touch (post-D4) via the OQ ledger; no `follow_up_agent` is set on this report because the touch targets a *different* chapter than this report applies and is not a precondition for applying this report.

- **Finding 3**: no consolidated-tally update (count-ownership deferred to D11).
  - **Decision**: not-needed.
  - **Rationale**: intended partition, not an omission. Per the dispatch's count-ownership instruction the report appends exactly the two theme rows + two SUMMARY lines + two bodies and deliberately leaves the consolidated L2>L1 / L3>L2 firm-count / coverage-gap tallies to D11 (count-divergence avoidance). Adding a tally line here would re-introduce the parallel-blind count divergence the partition exists to prevent. Flagged for the integrator so the absent tally reads as intentional.

- **Finding 4**: themes correctly scoped OUT of the `dot-l2-leaf-floor-vs-fold-only-design` fork (fork-independence).
  - **Decision**: not-needed.
  - **Rationale**: correct scoping, internally consistent with the L1/L3 home chapters (both record `assemble_diagonal` as the `apply_linop` operator-to-data sibling, fork-independent). Surfaced for the batch-12 meta-phase as a do-not-sweep-into-fork note. No edit warranted.

### Unrepairable findings

None. No finding is a defect; all four are informational/follow-up. Finding 2 is the only one that generates downstream work — a future `lifter` consistency touch on `L3/assemble-diagonal.md` §Downward/§Lowers-to once the D4 L2 floor is firm — and it is recorded in the report's §Open-questions ledger (CYCLE.md:611-621) for the integrator to promote. It is not a blocker on applying this report.

## Suggested resolution

`ready`. Notes for the integrator:

1. **Honor the D4-before-themes ordering (Finding 1).** Apply D4 (wave-1 harvester, `L2/assemble-diagonal.md`) before these two themes this cycle so the `../L2/assemble-diagonal.md` live links in both `new:` bodies (CYCLE.md:28, :289) and both index `edit:` rows (CYCLE.md:535, :540) resolve under `linkcheck2`. If D4 slips out of this cycle, hold these two themes rather than de-linking — the links are correct, only the sequencing is contingent.
2. **Promote the Finding-2 OQ** (stale `L3/assemble-diagonal.md` §Downward/§Lowers-to) from the report's §Open-questions into the ledger, routed to a downstream `lifter` consistency touch post-D4. Out of scope for both this report and the repairer (existing-chapter substantive edit).
3. **Tally update is intentionally absent (Finding 3)** — routed to D11 by the count-ownership partition. Do not treat the missing consolidated-count line as an integration gap.
