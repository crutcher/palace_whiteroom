---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T03:05:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T03:15:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of cross-layer observation `krylov-step` layer-placement

## Critique

### Checks run

- **citation-validity**: Spot-checked `book/src/concepts/solve-monad.md:14` (`restart_cycle op inp` line — present), `state-stratification.md:11` (ephemeral `Krylov` bundle description — present), `first-iteration-unrolling.md:21-37` (the `first_step` / `steady_step` signatures + driver — present and load-bearing to the argument). `book/src/L2/index.md:21-23` shows the `krylov-step` rough-in row. `book/src/L4/index.md:26-37` confirms the empty L4 dep-map. All citations land in-range. **pass**.
- **surface-or-evidence**: Not applicable in the refinement sense — this is an `observation`-shaped cross-cutter report, no surface diff is expected per role contract. Marked **pass**.
- **rotation-quality**: The implied L4→L2 rotation (typed-wrapper with state-monad threading → primitive-composition with value-threaded state) is genuinely a compression: state hiding via the monad + closure-threaded carry (per `first-iteration-unrolling.md:39`), not a 1:1 rename. **pass**.
- **variant-axis-coverage**: Variant axes are inherited from the L2 rough-in (preconditioner-side, orthogonalization, first-iteration-unrolling, flexibility) and explicitly carried into the L4 recommendation via `state-stratification` / `constructed-operators` absorption. Not authoring new variants here. **pass**.
- **cross-reference-integrity**: Every cited concept slug resolves under `book/src/concepts/` (`solve-monad`, `state-stratification`, `first-iteration-unrolling`, `iterate_while` via prose in solve-monad, `derived-view-hoisting`). `L4-L3/index.md` and `L3-L2/index.md` Parts exist (only `index.md` each — supports the "no lowering theme yet" claim). Pointers to `reports/2026-05-26T231843Z-combinator-miner-krylov-iteration-step/CYCLE.md` and parallel L2 harvester directory both exist. **pass**.
- **edge-label-fidelity**: Recommendation discusses L4>L3>L2 with body identity-in-form at L3>L2; prose discusses exactly that edge. **pass**.
- **plan-kind-consistency**: Declared as a cross-layer observation; role spec mandates "surfaces; doesn't enact". No proposed-changes block present; follow-up routing names three concrete dispatches (primary/secondary/tertiary) consumable by next-cycle planner. Single observation, no bundling. **pass**.
- **skill-uptake-survey**: The argument leans on multi-formulation-exploration (MEMORY) and could naturally cite `classify-variant-axis` (for the variant-axis absorption claim) or `verify-citation-range` (for the concept-prose citations). Neither is invoked in the report text. **warning** — telemetry only, non-blocking.

### Issues found

1. **skill-uptake-survey**: No reference to `verify-citation-range` despite four concept-line-range citations, nor to `classify-variant-axis` despite leaning on inherited variant absorption. CYCLE.md §1 (Specific finding) and §Supporting evidence. Severity: low (informational).
2. **Minor — caveat #2 self-references combinator-miner's audit deferral**: Caveat names cg.md:352-362 and arnoldi_step.md:185-188 as the L3-identity-in-form basis but does not verify the combinator-miner report's own claim independently. Not a blocking issue (it is properly deferred to L4>L3 abstractor), but the lack of even a smoke-check on those line ranges is worth noting. CYCLE.md line 57. Severity: low.
3. **Minor — slug-reuse open question is decided in the same paragraph**: Open-question #1 flags slug reuse `krylov-step` at both L2 and L4 then resolves itself ("Prefer same-slug-different-layer"). Either move the resolution to Recommendation or leave it genuinely open for harvester. CYCLE.md line 55. Severity: low.

## Repair

### Fixes attempted

- **Finding**: skill-uptake-survey warning — no `skill_uptake:` frontmatter block; report did not declare uptake of applicable skills.
  - **Decision**: repaired
  - **Action**: Added `skill_uptake:` block to CYCLE.md frontmatter listing `verify-citation-range` (informal, line-range spot-checks were done by hand), `classify-variant-axis` (not-applicable, no new axes authored), and `cross-cut-comparison` (informal, no formalized skill yet for cross-cutter pattern comparison). Mechanical-only — no substantive content added; survey reflects what the report already did.

- **Finding (minor #2)**: caveat #2 reuses combinator-miner's unaudited line ranges without smoke-check.
  - **Decision**: not-needed
  - **Rationale**: Critic flagged severity-low and explicitly noted "not a blocking issue (it is properly deferred to L4>L3 abstractor)". No frontmatter check failed; outside repair authority (audit work).

- **Finding (minor #3)**: open-question #1 self-resolves slug-reuse question.
  - **Decision**: not-needed
  - **Rationale**: Critic flagged severity-low, did not flag the corresponding `checks:` entry. Editing the recommendation/open-questions structure is substantive content reshaping, not mechanical.

### Unrepairable findings

None.

## Suggested resolution

`ready`. Integrator may apply. The two minor low-severity observations (caveats #2 and #3) are informational; no follow-up agent required for them. Primary/secondary/tertiary follow-up dispatches named in CYCLE.md §Recommendation remain as-written for cycle-planner consumption.
