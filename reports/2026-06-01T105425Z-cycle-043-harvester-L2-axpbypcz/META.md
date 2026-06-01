---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T000000Z
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
---

# META: verification of "Formalize axpbypcz at L2" (L2 floor, cycle-043 D5)

## Critique

### Checks run

**citation-validity — pass.** `tools/citecheck/citecheck.py --scan` reports 20 ok, 0 failing (bounds + path-hygiene clean). Read-verified the load-bearing L0 anchors directly: `vector.cpp:745-758` is the real-real `AXPBYPCZ` specialisation with the `γ == 0` branch exactly as claimed — `--anchor` confirms the fast-path `add(alpha, x, beta, y, z)` at line 751 (report says `:749-751`/`:751`, in-range) and the slow-path split `AXPBY(alpha, x, gamma, z); z.Add(beta, y)` at 755-756 (`--anchor 'z.Add(beta, y)'` → line 756, in-range). `vector.cpp:760-765` (complex-complex, delegates to member `z.AXPBYPCZ(...)`), `vector.cpp:767-772` (real-on-complex, delegates to member) verified. `vector.hpp:133-136` (member decl with `(*this) = alpha * x + beta * y + gamma * (*this)` comment) and `vector.hpp:313-316` (free-function template with `z = alpha * x + beta * y + gamma * z` comment, `--anchor 'AXPBYPCZ'` → line 315) verified. The `γ==0` branch claim — the focus item — is fully supported: the fast-path constant-folds to MFEM's 5-arg `add`, which the report correctly maps to `linear_combination` law 5 (zero-coefficient term-drop). The fold-aliasing call sites (`nleps.cpp:343-344`, `romoperator.cpp:188-189`) are in-bounds and correctly framed as the fold-parent's case, not this leaf's. No +1-drift detected anywhere. No `verified_against:` block present (not a lowering-verifier audit), so that sub-check no-ops.

**surface-or-evidence — pass.** This is a new firm L2 chapter (`new:book/src/L2/axpbypcz.md`) plus a dep-map row and a SUMMARY entry — a new-operator floor, not a refinement of an existing operator/theme. The surface-vs-retroactive-evidence test is for refinement-shaped proposals; here the surface IS the new chapter and it carries full L0 evidence. Not the pure-rotation-claim-without-surface failure mode.

**rotation-quality — pass with note.** The report does not claim a compacting rotation — it explicitly and correctly declares the L2↔L1 relationship **identity-in-form** (value-thread-isomorphic; signature textually identical). Per the **Identity-lowerings still require both L levels** invariant this is the legitimate shape for a floor entry: the rotation-quality "must be strictly more compact" bar applies to asserted algebraic/structural rotations, not to identity-in-form floors authored for layer-coherence. The report is the arity-3 sibling of the cycle-041 `scal` floor (the established precedent for exactly this pattern). No renaming-masquerading-as-rotation problem; the fusion content is honestly deferred to the fold's §"Fusion note" rather than fabricated as a leaf-level rotation.

**variant-axis-coverage — pass.** Two axes (element-type real/complex; scalar-promotion sub-axis on complex) are carried, each tied to a distinct L0 specialisation (`:745-758` / `:760-765` / `:767-772` / `vector.hpp:133-136`). The two axes the report **scopes out** are explicitly and correctly placed: (1) **arity** is the fold's unification axis, not a leaf variant (the leaf is the arity-3 fixed point); (2) **output-aliasing** (in-place vs out-of-place) is the fold's variant axis (`linear_combination.md` §Variant-axes point 1, line 220 — verified), with the `γ=1` accumulate-into sites cited as the fold's aliasing case. The `γ==0` internal control-flow branch is correctly classified as an L0 transparent-performance specialisation (not an L2 variant axis), inherited from L1. No hidden branches.

**cross-reference-integrity — pass.** All referenced artifact files exist on disk: `L1/axpbypcz.md`, `L3/axpbypcz.md`, `L2/linear_combination.md`, `L2/scal.md`, `L2/index.md`, `concepts/scalar-promotion.md`, `L1-L0/axpbypcz-mutation-rotation.md`, `decisions/axpby-as-primitive.md`. Load-bearing pinpoint references INTO the artifact verify: `linear_combination.md` line 71 (the arity-3 specialization identity `axpbypcz(...) = linear_combination [(α,x),(β,y),(γ,z)]`), line 220 (output-aliasing variant-axes point 1), line 243 (§Fusion note). The forward-referenced lowering themes (`L2-L1/axpbypcz-fusion`, L3>L2 `axpbypcz-body-identity`) are correctly left as plain-text (files do not yet exist; "do not link" stated) per `rough-in-forward-reference-must-be-plain-text-not-live-link`. **Build-readiness fence guard — pass:** fence enumeration shows 12 fences (even parity, 6 balanced pairs); the firm body block `new:book/src/L2/axpbypcz.md` opens at line 62 and closes at line 512, and the full firm apparatus is INSIDE the fence — `## Signature` (141), `## Algebraic laws` (217), `## Status` (398), `## Evidence` (445). The inner signature was authored as 4-space-indented code (lines 143-144), NOT a nested triple-backtick fence — the focus item: this is the correct cycle-019 fence-truncation avoidance, and no nested code fence appears inside the body block. SUMMARY.md insertion anchor verified: line 58 is `- [scal](./L2/scal.md)` exactly as the report states.

**edge-label-fidelity — pass.** The report's lowering/lifting prose discusses exactly the L2↔L1 identity-in-form edge it labels; the L3 relationship is referenced only as the consumer this floor supports (correct direction, high→low). No mismatched edge labels.

**plan-kind-consistency — pass.** Declared kind is `firm` floor. The content shape matches: full signature, twelve laws + four non-laws, two variant axes, complete L0 evidence chain, no rough-in placeholders. The `firm`-without-dedicated-test justification correctly invokes the firm-on-positive-structure escape (syntactic-identity laws on the fully-present `AXPBYPCZ` template specialisations) — the `apply_linop` situation, matching the sibling `scal`/`linear_combination` bar. The count-ownership discipline is respected: the report appends ONLY its dep-map row + body + SUMMARY entry and explicitly defers the consolidated firm running-count tally / §Working-Notes prose to D2 (no tally touch — verified the edit blocks carry no count mutation).

**skill-uptake-survey — warning (non-blocking).** The report's shape (firm operator with multiple L0 citations + a variant-axis classification + a fence-bearing proposed-changes block) implies several skills could have been referenced: `verify-citation-range` (L0 anchor verification), `classify-variant-axis` (the two-axis / two-scoped-out determination), and `proposed-changes-fence-encloses-full-body-guard` (the deliberate 4-space-indent-not-nested-fence choice). The report documents the underlying work (on-disk verification, the fence/indent decision) but does not name any skill invocation. Pure presence telemetry — surfaces a gap, does not block. (The work itself is correct regardless.)

### Issues found

No blocking issues. The report is clean on all seven substantive checks; the single `warning` is skill-uptake telemetry only.

Minor, non-blocking observations (candidates for repair only if cheap; none gate integration):

1. **skill-uptake telemetry gap** — `reports/.../CYCLE.md` §Supporting evidence / throughout: no skill invocation is named despite the citation-verification, variant-axis-classification, and fence-guard work being skill-shaped. Severity: low (telemetry). Not a correctness defect.

2. **L3 staleness is correctly out-of-scope** — the report's §Open-questions flags that `L3/axpbypcz.md:106,125` carries now-stale prose ("does not pass through L2 because `axpbypcz` is an L1 leaf, not an L2 composition" — verified at `:106` "no L2 intermediate is required" and `:125`). The deferral to a cycle-044 sweep is the right call; the floor itself is correct as written (lifts-from/lowers-to L1 directly, identity-in-form). Recorded here so the integrator/planner sees the staleness is real and tracked, NOT a defect in this report. Severity: informational.

---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T000000Z
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
repaired_at: 2026-06-01T111500Z
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

## Repair

### Fixes attempted

The critic returned 7 PASS on the substantive checks and a single non-blocking `warning` on `skill-uptake-survey` (telemetry only). No repairable defect is present. Per-finding:

- **Finding**: skill-uptake telemetry gap — no skill invocation named despite citation-verification / variant-axis-classification / fence-guard work being skill-shaped (Issues §1).
  - **Decision**: not-needed.
  - **Rationale**: pure presence telemetry. The critic itself classifies this as non-blocking and notes "the work itself is correct regardless." Naming a skill invocation retroactively in an append-only report would be (a) substantive editorial fabrication of process provenance, not a mechanical fix, and (b) outside repair authority. The check is `warning`, not `fail`; the underlying work (on-disk verification, the deliberate 4-space-indent-not-nested-fence choice) is documented in the report body. No edit.

- **Finding**: L3 staleness at `L3/axpbypcz.md:106,125` is correctly out-of-scope (Issues §2).
  - **Decision**: not-needed (informational — not a defect in this report).
  - **Rationale**: the report's §Open-questions already flags the stale L3 prose and defers it to the cycle-044 sweep. The repairer does not modify the artifact (`book/`) directly, and the floor itself is correct as written (identity-in-form, lifts-from/lowers-to L1 directly). The staleness is real and tracked; it is an out-of-band L3 follow-up, not a flaw in the L2 floor. Recording for integrator/planner visibility only. No edit.

### Unrepairable findings

None. No finding exceeds repair authority; both non-blocking observations are `not-needed` (one telemetry-only `warning`, one informational cross-report note). The CYCLE.md is unmodified by the repairer.

## Suggested resolution

`ready`. Integrator notes:
- The report is clean on all seven substantive checks; the lone `skill-uptake-survey` warning is telemetry and does not gate integration.
- The L3 staleness at `L3/axpbypcz.md:106,125` is a **tracked, deferred** c044 sweep item (already in the report's §Open-questions) — promote it to the OQ ledger / plan at integration so the c044 sweep picks it up. It is NOT a defect in this L2 floor.
- Count-ownership discipline is respected: this report touches only its dep-map row + body + SUMMARY entry; the consolidated L2 firm running-count tally / §Working-Notes prose is deferred to D2 (do not expect a tally mutation here).
