---
name: verify-refinement-surface
description: Pre-emit self-check for the Synthesizer when emitting a refinement / self-rotation / L_n→L_n cycle. Verifies that the plan carries either an actual surface edit on the named slice (slice_writes / section_appends / file_edits) OR a retroactive_claim_evidence block in log_synthesis quoting the existing on-disk prose. Catches the recurring claims-without-surface pattern (8+ recurrences through meta-25) before plan emission instead of letting the integrator gate downgrade.
status: active
---

# verify-refinement-surface

The claims-without-surface pattern has recurred across cycles 115, 116, 125, 136, 147, 156, 165, 166 — eight observed instances. The integrator surface-or-evidence gate (meta-22/23) catches each and downgrades the cycle, but the Synthesizer keeps re-emitting the same shape. Producer-side discipline needs a procedural self-check at plan emission time.

## Trigger

Apply this skill before emitting any plan with:

- `push_kind = refinement`, OR
- any `rotation_claim` whose `edge` is a self-edge (`L_n→L_n` or `Ln→Ln`), OR
- `plan_kind = tightening` with rotation_claims targeting an existing on-disk layer.

## Procedure

For each rotation_claim in the plan:

1. **Identify the claim's target prose.** The rotation_claim describes a transformation: from_form → to_form on a named slice's named layer. The transformation must be visible somewhere — either it's landing as new prose in this plan, or it's already on disk and the claim is retroactive.

2. **Search the plan for a surface edit on the named slice.** Scan:
   - `slice_writes[i]` where `path` matches the named slice.
   - `section_appends[i]` where `path` matches the named slice file AND `heading` matches the target layer.
   - `file_edits[i]` where `path` matches the named slice file.

   If any match, the surface lands in this plan — proceed to next claim.

3. **If no surface edit, search log_synthesis for retroactive evidence.** Check:
   - `log_synthesis.retroactive_claim_evidence` is non-empty.
   - At least one entry has `claim_index == i` (matching this rotation_claim's index).
   - That entry's `quoted_lines` is non-empty and quotes existing on-disk prose.

   If both match, the claim is retroactive against existing surface — proceed to next claim.

4. **If neither, this claim FAILS the self-check.** Either:
   - Add the surface edit (section_appends carrying the new prose to the slice).
   - Add retroactive_claim_evidence quoting the existing on-disk prose this claim refers to.
   - Drop the rotation_claim — it has no visible surface.

## Framework-slice-specific anti-pattern (meta-25)

Cycles 156, 165, 166 on `cg_preconditioning_framework` all emitted:

```yaml
plan:
  rotation_claims: [{edge: "L4→L4", target: "v0.X capability-typing introduction"}]
  concept_writes: [{name: "capability-typing", mode: "create", content: "..."}]
  dependency_map_edges: [...]
  lessons: [...]
  # ← NO slice_writes/section_appends/file_edits to cg_preconditioning_framework.md
```

The supporting concept_writes is NOT the surface for the rotation_claim — the rotation_claim points at the slice's L4 prose, which doesn't exist on disk and isn't being added in this plan. The Critic check #14 downgrades.

**Correct form**:

```yaml
plan:
  rotation_claims: [{edge: "L4→L4", target: "v0.X capability-typing introduction"}]
  section_appends:
    - path: "book/src/spec/slices/cg_preconditioning_framework.md"
      heading: "## L4 v0.2 — capability-typing brands"
      content: "... the actual prose describing OpBinding<E>, setOperators, finestLevelUnwrap ..."
  concept_writes: [{name: "capability-typing", mode: "create", content: "..."}]
  ...
```

The section_appends to the slice IS the surface; the concept_writes is the supporting vocabulary.

## Cross-references

- Synthesizer prompt *Self-rotation/refinement surface-or-evidence discipline* (the producer-side rule this skill operationalizes).
- Critic check #14 (rotation_claims_require_surface) — verifies the same constraint at verdict time.
- orchestrator/loop.py refinement-surface integrator gate (meta-22 + meta-23) — downgrades when both surface and evidence missing.
