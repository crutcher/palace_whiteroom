---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T164500Z
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
repaired_at: 2026-06-01T165500Z
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

# META: verification of L2>L1 theme `krylov-step-kernel-defusion`

## Critique

### Checks run

**citation-validity — pass.** `tools/citecheck/citecheck.py --scan` returned 21 ok / 0 failing on the report (no bounds or path-hygiene drift). Spot-verified the load-bearing L0 anchors against the Palace source via `palace-codemap read_range iterative.cpp:438-464`: every cited anchor matches exactly — `linalg::AXPBY(1.0, z, beta/beta_prev, p)`@:440, `A->Mult(p, z)`@:443, `Dot(comm, z, p)`@:444, `CheckDot(denom, ...)`@:445, `x.Add(alpha, p)`@:448, `r.Add(-alpha, z)`@:449, `Dot(comm, z, r)`@:461, `res = std::sqrt(std::abs(beta))`@:462. The first-iteration `else { AXPBY ... }` branch and the `if (B) { ApplyB } else { z = r }` preconditioner branch are present as cited. The L2-entry internal anchors all resolve and mean what the report says: `book/src/L2/krylov-step.md:96` is the seven-leaf firm dependency list, `:121` is variant-axis-6 ("in-place vs out-of-place buffer use" carrying the explicit "reappearing in the L2>L1 lowering" forward-ref this theme resolves), and `:129-132` is the "L2 vs L1 distinction" section (correctly used as conceptual context, not as the lowering). The report carries no `verified_against:` YAML block (that is named as the standard lowering-verifier follow-up, not emitted here), so the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is a NEW `new:`-file theme (the `book/src/L2-L1/krylov-step-kernel-defusion.md` file does not pre-exist on disk), not a refinement of an existing operator/theme, so the refinement-surface/rotation-evidence dichotomy does not bind. The theme nonetheless carries full forward-narration evidence (the de-fusion table + the CG-specialisation worked example anchored on self-verified L0) and resolves a real dangling surface defect at `L2/krylov-step.md:121`. Not a pure rotation_claim.

**rotation-quality — pass.** This is a genuine L2→L1 de-fusion, not a rename or 1:1 map. The L2 form is one named fold-kernel composition (`krylov-step`); the L1 form is the explicit seven-leaf dataflow-forced sequence (`apply_linop ▷ axpby/axpy ▷ dot ▷ ... ▷ readout`). The rotation fans the single named L2 composition surface DOWN into its constituent L1 primitive sequence (the L1 side is strictly more spelled-out / less abstract — the correct direction for a lowering: L2 is the compact form, L1 the expanded). The in-place→out-of-place buffer rotation is correctly framed as transparent-performance-equivalent (CLAUDE.md §Optimization tricks) and correctly resolves the `:121` dangling forward-ref; the §"L2 vs L1 distinction" (`:129-132`) is used as CONTEXT and is NOT mis-presented as the lowering (the actual forward rewrite is authored fresh in §"The de-fusion rewrite"), honoring the cycle-046 caveat. Demand-pruning (Law 1) and the `CheckDot` guard are correctly carried-by-reference rather than re-derived.

**variant-axis-coverage — pass.** The six L2 variant axes are explicitly handled: absorbed-at-construction (axes 1/2/3/5 via `op.T`/`op.orthog`/`op.scalars`) per applicability-condition 2; the first-iteration branch (axis 4) is kept in the de-fused body for the v0.4 form and noted as split-out in v0.5; axis 6 (buffer use) is the central rotation the theme resolves, treated as a buffer-aliasing annotation with the in-place mechanics deferred to the per-leaf L1>L0 themes. No hidden branch — each axis is either covered or explicitly scoped (e.g. the MINRES/BiCGStab specialisations are scoped out as obstruction documentation).

**cross-reference-integrity — warning.** Fence parity is clean: 13 fence lines total, even parity; the `new:` block (CYCLE.md:23-376) contains exactly its own opener+closer with the full chapter body (signatures, `## Status`, etc.) in 4-space indented-code form — NO nested fences, so no cycle-019 fence-truncation risk; `## Status` is confirmed INSIDE the fence. Both `edit:` FROM-anchors (the `incremental-least-squares-composition-lowering` index row at index.md:32, and the SUMMARY.md line) exist exactly once on disk, are unambiguous, and the index does not yet contain a `krylov-step-kernel-defusion` row (no collision). Link targets verified on disk: the L2 LHS, all seven L1 leaves, and the two CORRECTED L1>L0 links — `axpby-mutation-rotation.md` EXISTS and `axpy-mutation-rotation.md` does NOT (correction (a) confirmed: the `axpy` `x.Add`/`r.Add` overwrite is correctly routed to `axpby-mutation-rotation.md`), and `apply-linop-mutation-rotation.md` EXISTS with the hyphen while `apply_linop-mutation-rotation.md` (underscore) does NOT (correction (b) confirmed). `orthogonalize-composition-lowering.md`, `chebyshev-iteration-fusion.md`, `ksp-solve-mutation-rotation.md`, `orthogonalize-mutation-rotation.md`, and `concepts/derived-view-hoisting.md` all exist. The warning is the single same-cycle forward-reference: the chapter live-links `[ksp-solve-outer-driver-unfold](./ksp-solve-outer-driver-unfold.md)` (twice — §intro and §Verified-against) to the D3 sibling, which is NOT yet on disk. The report acknowledges this and prescribes the convention (apply after D3, or defang to plain-text per the missing-anchor convention), but as authored the live link will hard-break `linkcheck2` if applied before D3 lands — an integration-ordering hazard the integrator must handle.

**edge-label-fidelity — pass.** The edge label is L2>L1 throughout. The prose, the LHS/RHS sections, and the de-fusion table all discuss exactly the L2→L1 edge (L2 `krylov-step` fold-kernel → seven L1 leaves). The per-leaf in-place mechanics are correctly attributed to the adjacent L1>L0 edge (deferred, not conflated), and the L0 witnesses are cited as evidence-for the L1 leaf assignment, not as the lowering edge itself. No edge mislabeling.

**plan-kind-consistency — pass.** Declared kind is a `firm` L2>L1 theme. The content shape matches: both sides are firm vocabulary (LHS `krylov-step` firm cycle-004; all seven L1 leaves firm post-cycle-004), the de-fusion rule is the syntactic expansion of the L2 §Semantics body with no literature inference / negative-anchor reconstruction / speculative operator, and the status reasoning matches the `orthogonalize-composition-lowering` firmness bar it cites. No rough-in placeholders sit under the firm claim. The two stated caveats (Arnoldi/Chebyshev sub-sequences stated-not-per-line-verified; per-leaf delegation-boundary audit) are correctly framed as non-status-gating follow-ups, consistent with `firm`.

**skill-uptake-survey — pass.** The report references `verify-citation-range` (producer self-verification via `palace-codemap read_range` + `tools/citecheck/` anchor-drift checks) in §Verified-against, which is the relevant skill for a citation-heavy lowering theme. Telemetry present; no blocking.

### Issues found

1. **Same-cycle forward-reference live-link to not-yet-on-disk D3 sibling** — `book/src/L2-L1/krylov-step-kernel-defusion.md` (the `new:` block, §intro line ~42 and §Verified-against), severity **warning**. The chapter live-links `[ksp-solve-outer-driver-unfold](./ksp-solve-outer-driver-unfold.md)` in two places; that file is created by D3 in the same cycle and is absent from disk at critique time (confirmed `ls`: no such file). If this report is applied before D3's `new:` block lands, the live link is a hard `linkcheck2` build break. The report flags this and gives the integrator two valid remedies (order after D3, or defang both occurrences to plain-text per the missing-anchor convention), but the defect-as-authored is an unconditional live link. Integration-ordering hazard; candidate for the missing-anchor plain-text defang if D3 ordering cannot be guaranteed.

2. **Count-ownership / dual-registration partition — correctly observed, no defect.** Verified the report does NOT write the consolidated firm-count tally: the `L2-L1/index.md` cohort-growth-log + firm-count ("firm 15 → 19") lives at index.md:71 in §"Working Notes", and the report's `edit:` block touches ONLY the table row at index.md:32 (adds one row after it) and the SUMMARY.md line. The §Vocabulary-cohort bullet is delivered as a NOTE-to-integrator append (its own bullet), and the consolidated tally is explicitly deferred to D3 (`ksp-solve-outer-driver-unfold`, the sole count-owner). The partition is honored exactly as the dispatch prescribed — recorded here as a positive confirmation, not an issue.

## Repair

### Fixes attempted

- **Finding 1 — cross-reference-integrity (warning): same-cycle sibling live-link to not-yet-on-disk D3 sibling.** The chapter live-links `[ksp-solve-outer-driver-unfold](./ksp-solve-outer-driver-unfold.md)` twice (§intro CYCLE.md:42, §Verified-against CYCLE.md:320), targeting the D3 sibling that lands this same cycle but is absent from disk at critique time.
  - **Decision**: not-needed (KEEP the live links — do NOT defang to plain-text).
  - **Action**: no edit. The links are kept as authored. See the INTEGRATOR-ORDERING NOTE below.
  - **Rationale**: this is an integration-ordering artifact, not a verdict-inverting content defect. Both D3 and D4 (this report) co-land THIS cycle. Under the default split-integrator pipeline, every ready report's `new:`/`edit:` blocks apply via `integrator-per-report` (serial) BEFORE `integrator-finalize` runs `cargo make book` + linkcheck2 exactly ONCE at cycle-end. Therefore D3's `book/src/L2-L1/ksp-solve-outer-driver-unfold.md` will be on disk by the single finalize build, and both live links resolve. Defanging to plain-text would be a needless mechanical change that would then have to be re-linked. Link path spelling verified: the chapter links `./ksp-solve-outer-driver-unfold.md`, which matches the dispatch-scoped D3 slug `ksp-solve-outer-driver-unfold` exactly — it will resolve once D3 lands.

- **Finding 2 — count-ownership / dual-registration partition: correctly observed, no defect.**
  - **Decision**: not-needed (confirmed-correct).
  - **Rationale**: the critic's positive confirmation holds. The report's `edit:` blocks touch only its own index table row (index.md:32, FROM-anchor present exactly once on disk; no `krylov-step-kernel-defusion` row pre-exists → no collision) and the SUMMARY.md line (FROM-anchor present exactly once), and delivers its own §Vocabulary-cohort bullet as a NOTE-to-integrator append. The consolidated firm-count tally + cohort-growth-log are explicitly deferred to D3 (the sole count-owner). The dual-registration partition (own row + own bullet are this report's; consolidated tally deferred) is honored as the dispatch prescribed. No repair.

Supporting verifications re-confirmed on disk this pass: `axpby-mutation-rotation.md` EXISTS / no standalone `axpy-mutation-rotation.md`; `apply-linop-mutation-rotation.md` EXISTS (hyphen); fence parity even (13 fence lines). No mechanical edits surfaced.

### Unrepairable findings

None. The single warning is an integration-ordering note resolved by the default finalize build ordering, not a substantive-authoring defect.

### INTEGRATOR-ORDERING NOTE

Both D3 (`ksp-solve-outer-driver-unfold`) and D4 (this report, `krylov-step-kernel-defusion`) `new:` blocks apply via the serial `integrator-per-report` passes BEFORE the single `integrator-finalize` `cargo make book` + linkcheck2 run. The two `ksp-solve-outer-driver-unfold` live links (CYCLE.md §intro + §Verified-against) therefore resolve at that single finalize linkcheck regardless of which of D3/D4 applies first — no defang needed. (Defang to plain-text is the fallback ONLY if D3 is dropped/rejected this cycle so its file never lands; if that occurs, the integrator-finalize build-repair step should de-link the two occurrences per the missing-anchor convention.)

## Suggested resolution

`ready`. Content is sound per the critic (7 pass, 1 warning). The lone warning is integration-ordering, not verdict-inverting, and is resolved by the standard split-integrator finalize-build ordering. Integrator notes: keep the `ksp-solve-outer-driver-unfold` live links intact; honor the count-ownership partition (this report registers its own row + bullet; D3 owns the consolidated tally); the index/SUMMARY FROM-anchors are unambiguous (each present exactly once, no collision).
