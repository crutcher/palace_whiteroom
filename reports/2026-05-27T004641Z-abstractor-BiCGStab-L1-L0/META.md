---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T00:55:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T01:05:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: meta-phase
---

# META: verification of BiCGStab L1>L0 obstruction theme sketch

## Critique

### Checks run

- **citation-validity**: All three negative anchors verify exactly. `ksp.cpp:53-56` is the `MINRES/BICGSTAB/DEFAULT` abort branch; `labels.hpp:111` is the `BICGSTAB` enum entry; `configfile.cpp:132` is the JSON `"BiCGSTAB"` mapping. Repo-wide grep returns only those three hits — claim of "exactly three sites" holds. **pass**.
- **surface-or-evidence**: New theme file + dep-map edits + SUMMARY edit = surface present. **pass**.
- **rotation-quality**: Obstruction theme; L1 form is more abstract than the (empty) L0. Saad §7.4.2 shape is structurally consistent — `ρ/β` update, `α = ρ/⟨r̂₀,v⟩`, half-step `ω = ⟨t,r⟩/⟨t,t⟩`, two axpy updates. **pass**.
- **variant-axis-coverage**: Preconditioner axis covered (`M` slot, identity allowed); state vector explicit. **pass**.
- **cross-reference-integrity**: Dep-map links `./bicgstab_step.md`, `./omega_update.md`, `./stabilisation_update.md` are rough-in placeholders — they will 404 in link-check until harvester promotes. **warning**.
- **edge-label-fidelity**: Edge L1>L0 discussed consistently. **pass**.
- **plan-kind-consistency**: `rough-in (obstruction)` matches content shape. **pass**.
- **skill-uptake-survey**: No `verify-citation-range` invocation referenced despite three citations being load-bearing. **warning**.

### Issues found

1. **bicgstab-iteration.md §Speculative L1 operators** (severity: low) — links to per-operator pages that don't yet exist; will break mdBook link-check at integration. Integrator may need to inline-style the names or stage stub pages.
2. **CYCLE.md frontmatter** (severity: low) — `skill-uptake-survey` telemetry only; no skill invocations recorded for citation verification.

## Repair

### Fixes attempted

- **Finding**: rough-in dep-map links to nonexistent chapter files will 404 in mdBook link-check.
  - **Decision**: repaired
  - **Action**: In CYCLE.md "Proposed changes" block targeting `book/src/L1/index.md`, converted the three rough-in operator names from `[\`name\`](./name.md)` link form to plain `` `name` `` (no link target), per the cycle-002/003 rough-in convention. Applies to `bicgstab_step`, `omega_update`, `stabilisation_update`.

- **Finding**: `skill_uptake:` frontmatter block missing.
  - **Decision**: repaired
  - **Action**: Added `skill_uptake:` block to CYCLE.md frontmatter listing the five abstractor-relevant skills (`verify-citation-range`, `classify-variant-axis`, `verify-refinement-surface`, `plan-sideways-concept-emission`, `skill-selection`) with status (`not-invoked` / `not-applicable`) and brief rationale for each.

### Unrepairable findings

None. Both critic warnings were mechanical/surgical.

## Suggested resolution

`overall_status: ready` — both warnings fully repaired; report is applicable as-is.

**For meta-phase follow-up (not blocking integration):**
1. The `bicgstab-mfem-reanchor-policy` open question is co-pending with the cycle-004 MINRES dispatch; warrants a methodology decision in `scaffolding/decisions/` about whether MFEM is admitted as L0 substrate for advertised-but-aborting Krylov solvers.
2. The `advertised-but-unimplemented-krylov-solvers` pattern (now appearing in MINRES + BiCGStab back-to-back) is a strong friction-ledger candidate; meta-phase should record it and watch for the third instance.
3. The parent-session annotation (subagent-skips-edit-on-explicit-instruction) is an opus-tier instance of the cycle-002 haiku pattern; meta-phase may want to surface it.
