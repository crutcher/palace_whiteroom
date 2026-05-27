---
verifies: ../REPORT.md
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
repaired_at: 2026-05-27T03:20:00Z
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

# META: verification of harvester `krylov-step` at L2

## Critique

### Checks run

**citation-validity** — Spot-checked cg.md:103-115 (CG L2 step body — matches), cg.md:172-188 (cg_step v0.4 — matches), gmres.md:459-471 (inner_loop — matches), chebyshev.md:354-362 (innerStep — matches), arnoldi_step.md:99-105 (procedure — matches), polynomial_recurrence_step.md:119-160 (catalog — matches). All five pattern-instance citations resolve and content fits the claimed shape. Pass.

**surface-or-evidence** — Proposal promotes rough-in row to firm L2 chapter (new surface: `book/src/L2/krylov-step.md`); modifies `L2/index.md` dep-map; updates `SUMMARY.md`; proposes new decision artifact. Substantive surface authored, well beyond pure rotation_claims. Pass.

**rotation-quality** — Not the primary shape (this is an L2 harvest, not a layer-to-layer rotation); the implicit L2-vs-L1 compaction is exhibited (single fold-kernel name replaces five slice-specific step bodies; one non-trivial law + structural invariants replace per-slice derivations). Pass.

**variant-axis-coverage** — Six axes (preconditioner, orthogonalization, polynomial-kind, first-iter-unrolled, restart, in-place/out-of-place) match cycle-002 combinator-miner enumeration verbatim. None added, none dropped, none merged. Explicitly stated at line 147. Pass.

**cross-reference-integrity** — All 11 referenced concept pages verified present in `book/src/concepts/`. All seven L1 deps present in `book/src/L1/`. Both L1-L0 guidance themes present. Pass.

**edge-label-fidelity** — No layer-edge label (this is intra-L2 firm-up); not applicable. Pass.

**plan-kind-consistency** — Declared `firm` status; content delivers full signature, semantics, three laws + six non-laws, six variant axes, dependencies, evidence — shape matches firm-operator template. Pass.

**skill-uptake-survey** — `verify-citation-range` and `classify-variant-axis` would be natural invocations for the five pattern-instance citations and the six-axis enumeration; CYCLE.md does not reference invoking either skill. Pure-telemetry warning.

### Issues found

1. **Speculative-decision file path is referenced but not self-consistent (minor)** — CYCLE.md L2/index.md edit at line 236 states the decision file is "proposed for integrator wiring"; the REPORT prose at line 20 and §"Supporting evidence" both reference `scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md`. The proposed `edit:` block for that file (lines 373-409) is well-formed. Cross-reference is clean; flagging for integrator awareness only — not a defect.

2. **Operator count claim in Decision file (verify-empirical)** — Decision file line 389 states bicgstab uses "**two** `apply_linop` calls per step instead of `krylov-step`'s typical one". CYCLE.md §Algebraic laws Law 2 declares per-step `apply_linop` count "a structural invariant of the slice's variant-axis profile" — this is consistent (BiCGStab's 2-per-step is its own profile), but a careful reader might see tension between "structural invariant" and "the typical one". No real contradiction; flag as a phrasing-clarity issue, not a fault.

3. **Skill uptake telemetry** — No skill invocation telemetry recorded in CYCLE.md frontmatter or body despite obvious applicability of `verify-citation-range` (6 multi-line-range citations) and `classify-variant-axis` (6-axis enumeration). Telemetry only; non-blocking.

4. **Open Question #5 (no-L0-source) is pre-emptively defensive** — Author flags this as a "feature, not a bug" before any critic raises it; acceptable harvester-self-disclosure for L2 named compositions whose anchor is the slice corpus rather than C++ source. No action required.

## Repair

### Fixes attempted

- **Finding**: skill-uptake-survey warning — CYCLE.md frontmatter missing `skill_uptake:` block despite obvious applicability of `verify-citation-range` (5+ multi-line-range citations) and `classify-variant-axis` (six-axis enumeration).
  - **Decision**: repaired
  - **Action**: Added `skill_uptake:` frontmatter block to CYCLE.md mirroring the cycle-004 harvester format. Three entries: `classify-variant-axis` (triggered, artifact_landed — six axes classified matching cycle-002 enumeration verbatim); `verify-citation-range` (triggered, explained_non_applicable — citations verified inline, skill invocation deferred per cycle-002/cycle-004 pattern); `skill-selection` (triggered, artifact_landed — three skills considered, refinement-surface verification ruled non-applicable since this is a rough-in→firm promotion, not refinement of a prior coarser surface). Per-skill rationale text drawn from the report's own variant-axis enumeration and citation-handling discipline; no substantive content authored.
  - **Rationale**: Mechanical — the critic explicitly flagged this as pure telemetry, the cycle-004 harvester format is established precedent, and all three skill entries are recoverable from the existing REPORT body (axis enumeration at §"Variant axes", citation lists at §"Evidence", skill-selection logic by elimination).

### Unrepairable findings

None. The critic's three issue-list items (speculative-decision cross-reference, BiCGStab phrasing-tension, no-L0-source defensiveness) were all explicitly flagged as non-defects / no-action-required, not as repair candidates.

## Suggested resolution

`ready` — proceed to integrator. The firm `book/src/L2/krylov-step.md` chapter, the L2 dep-map update, the SUMMARY.md insert, and the proposed `scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md` entry are ready to apply as a single atomic batch. Skill telemetry is now complete per the cycle-004 precedent.
