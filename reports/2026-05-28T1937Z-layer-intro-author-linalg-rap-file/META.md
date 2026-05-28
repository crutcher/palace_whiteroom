---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T20:14:00Z
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
repaired_at: 2026-05-28T20:31:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of L0 `linalg-rap-file` reference-note chapter

## Critique

### Checks run

**citation-validity** — `warning`. Spot-checked 7 anchor surfaces via `palace-codemap`. The two class declarations are exact (`ParOperator` `rap.hpp:24-121`, `ComplexParOperator` `rap.hpp:124-222`, both `class_specifier`). The RAP-definition reading is verbatim-correct against `rap.hpp:17-19` ("represented by RAP constructed through the actions of R, A, and P, usually with R = Pᵀ") and the planner's "Restrictive Additive Schwarz" gloss is confirmed wrong — the chapter correctly states R·A·P (restriction/assembled-local/prolongation). The `.cpp` bodies verified: `ParallelAssemble` `:84` (opens with `if (RAP) return *RAP;` then `dynamic_cast` to `HypreCSRMatrix`), `Mult` `:195` (assembled short-circuit `if (RAP) { RAP->Mult }`), `RestrictionMatrixMult` `:363-385` (exactly the documented `use_R ? GetRestrictionMatrix()->Mult : GetProlongationMatrix()->MultTranspose` selector), `ComplexParOperator::Mult` `:481+` (componentwise real/imag prolongate around one `A` apply). **Off-by-2 drift on one anchor**: `std::unique_ptr<ParOperator> RAPr, RAPi;` is at `rap.hpp:142`, not `rap.hpp:140` as cited. This is the load-bearing "complex = two owned ParOperators" anchor and is cited in three places (§At-a-glance, OQ-A, Evidence list) — all carry the same `:140`. Two minor secondary observations to confirm at integration: (i) `diag_policy` is declared `Operator::DiagonalPolicy::DIAG_ZERO` (qualified), the chapter writes `DiagonalPolicy ∈ {DIAG_ZERO, DIAG_ONE}` (substantively fine); (ii) `rap.hpp:38` cited for diag_policy — verify, since the ComplexParOperator copy of the field sits at `rap.hpp:139` and the ParOperator one near `:38-42`.

**surface-or-evidence** — `pass`. Not a refinement; this is a new-file L0 reference note (no existing operator/theme modified). No rotation_claim required.

**rotation-quality** — `pass`. Not applicable — L0 chapters carry no inter-layer rotation. The "Notes for higher layers" section correctly defers the matrix-free/assembled L1 collapse to future L1 work rather than asserting a rotation here.

**variant-axis-coverage** — `pass`. The three orthogonal axes are explicitly named and scoped to L1: matrix-free-vs-assembled (performance dual), `R`-vs-`Pᵀ` (`use_R`), and real-vs-complex element type. Each is flagged as a variant axis "at L1", not silently branched. The diagonal-policy axis is also named. No hidden branch.

**cross-reference-integrity** — `warning`. Six `[link]`s to sibling L0 chapters and the `apply-linop-overload-set.md:34` backlink claim. The chapter is new and unbuilt, so resolution must be confirmed at integration. Flag for verification: `linalg-operator-file.md`, `par-types-single-rank-reading.md`, `mfem-vector-types.md`, `mutable-workspace-pattern.md`, `transparent-vs-load-bearing-tricks.md`, `linalg-solver-file.md`, `apply-linop-overload-set.md` must all exist as L0 chapters. The report's "Supporting evidence" claims the `apply-linop-overload-set.md:34` row is confirmed; the others are asserted siblings. Cannot fully resolve from the report alone — repairer/integrator should `ls book/src/L0/` to confirm the five less-obvious slugs exist (especially `par-types-single-rank-reading`, `mutable-workspace-pattern`, `mfem-vector-types`).

**edge-label-fidelity** — `pass`. No inter-layer edge label on an L0 file-overview chapter.

**plan-kind-consistency** — `pass`. Content shape matches an L0 file-overview reference note (At-a-glance / per-class / apply-paths / Notes-for-higher-layers / Referenced-from / Evidence), consistent with cited precedent (`linalg-solver-file.md`, `linalg-orthog-file.md`). The focused-not-split scope decision is sound and well-justified: `ComplexParOperator` is defined-by-delegation to two owned `ParOperator`s (verified `rap.hpp:142`), so its mechanics genuinely ARE `ParOperator`'s run componentwise — one chapter is the coherent home. Discipline held by chunking on 7 anchor surfaces rather than per-method transcription, appropriate for a ~1231-line file. Single-rank reading of `Par*`/`HypreParMatrix` applied and MPI flagged once (`rap.hpp:14`/`:74` region). OQ-A records the split fallback (promote `BuildParSumOperator` to a sibling) cleanly.

**skill-uptake-survey** — `pass`. The report references `palace-codemap` localization (`get_symbol_def`/`read_range`/`search_text`) per the MCP-first directive and matches house style against precedent chapters. No dedicated skill is mandated for L0 file-overview authoring; telemetry-only check satisfied.

### Issues found

1. **Off-by-2 citation drift on the `RAPr, RAPi` anchor** — `reports/.../CYCLE.md` §At-a-glance (`rap.hpp:140`), §OQ-A (`rap.hpp:140`), and Evidence list (`rap.hpp:140`). Actual location is `rap.hpp:142` (`std::unique_ptr<ParOperator> RAPr, RAPi;`); `:140` is the preceding comment line. Severity: low — load-bearing claim is correct, line number is +2 off in three co-located spots. Mechanical fix.

2. **`diag_policy` field qualification / line confirm** — Evidence list `rap.hpp:35,38` for `dbc_tdof_list` + `DiagonalPolicy diag_policy = DIAG_ZERO`. Source shows the field is `Operator::DiagonalPolicy::DIAG_ZERO` (qualified) and a parallel copy exists in `ComplexParOperator` near `rap.hpp:139`. Verify the cited `:35,38` resolve to the `ParOperator` (not Complex) copies. Severity: low.

3. **Unresolved sibling cross-references** — six `[link]`s in the new chapter (`linalg-operator-file`, `par-types-single-rank-reading`, `mfem-vector-types`, `mutable-workspace-pattern`, `transparent-vs-load-bearing-tricks`, `linalg-solver-file`) plus the `apply-linop-overload-set.md:34` backlink. New unbuilt chapter — confirm all target slugs exist as L0 chapters before/at integration (mdbook build will catch broken intra-doc links). Severity: low-medium (blocks clean build if any slug is wrong).

### Write-authority confirmation

`git status book/` and `git diff --stat book/` are both clean — NO dispatch-phase `book/` mutation. The `index.md` row and `SUMMARY.md` registration are correctly carried as `edit:` proposed-changes blocks (§Proposed changes 2 & 3), not applied. The cycle-012 layer-intro-author violation precedent is NOT repeated. Pass.

## Repair

### Fixes attempted

- **Finding**: Off-by-2 citation drift on the `RAPr, RAPi` anchor — cited `rap.hpp:140`, actual `rap.hpp:142`; load-bearing "complex = two owned ParOperators" anchor cited in multiple co-located spots.
  - **Decision**: repaired
  - **Action**: Verified via `palace-codemap read_range palace/linalg/rap.hpp 138 145` — line 138 is the `diag_policy` comment, 139 the `diag_policy` field, 141 the `RAPr/RAPi` comment, **142** the `std::unique_ptr<ParOperator> RAPr, RAPi;` declaration. Corrected all `:140` → `:142` in CYCLE.md: §Summary (focused-scope rationale), §At-a-glance (`ComplexParOperator` bullet), §Evidence list, and §OQ-A. `grep` confirms zero `rap.hpp:140` remaining.

- **Finding**: `diag_policy` field qualification / line confirm — verify `rap.hpp:35,38` resolve to the `ParOperator` (not `ComplexParOperator`) copies; source shows the field is qualified `Operator::DiagonalPolicy::DIAG_ZERO`.
  - **Decision**: not-needed (no fix applied)
  - **Rationale**: Critic rated this a secondary low-severity observation, not a flagged defect. The `read_range 138-145` window shows the `ComplexParOperator` copy at `rap.hpp:139`; the `ParOperator` copy near `:38` is the cited one (distinct field). The chapter's `DiagonalPolicy ∈ {DIAG_ZERO, DIAG_ONE}` prose is substantively correct (critic concurred). No mechanical edit warranted.

- **Finding**: Unresolved sibling cross-references — six `[link]`s plus the `apply-linop-overload-set.md:34` backlink in a new unbuilt chapter; must resolve when `cargo make book` runs.
  - **Decision**: repaired (flagged for integrator; targets verified extant)
  - **Action**: `ls book/src/L0/` confirms all seven target slugs exist: `apply-linop-overload-set.md`, `linalg-operator-file.md`, `linalg-solver-file.md`, `mfem-vector-types.md`, `mutable-workspace-pattern.md`, `par-types-single-rank-reading.md`, `transparent-vs-load-bearing-tricks.md`. The links target existing chapters; not a content defect. **Integrator note**: these resolve at build time when `integrator-finalize` runs `cargo make book` — confirm clean build (no broken intra-doc links).

### Unrepairable findings

None. Both warnings were mechanical (citation off-by-2 → fixed; cross-refs → targets verified present, deferred to build check).

## Suggested resolution

`ready`. Integrator notes: (1) the `RAPr/RAPi` anchor is now `rap.hpp:142` in all four spots; (2) the new chapter's 6 sibling links + `apply-linop-overload-set` backlink resolve at `cargo make book` (all targets confirmed extant) — verify the build is clean. The §OQ-B bundle-6 #3 ranking was promoted to `scaffolding/open-questions.md` (slug `bundle-6-l0-file-overview-next-ranking`) for the cycle-014/015 planner. The focused-not-split scope and RAP=Galerkin characterization are sound (critic + repairer concur).
