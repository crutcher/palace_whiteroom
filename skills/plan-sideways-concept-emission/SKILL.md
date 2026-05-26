---
name: plan-sideways-concept-emission
description: Pre-emit procedure for the Synthesizer on SIDEWAYS pushes that emit multiple concept_writes. Catches the bulk-concept mode=create-on-existing pattern that the integrator auto-rewrites (meta-19) but which generates high-volume push-back signals. Cycle 161 emitted 10 concept creates of which all 10 already existed — 20 push-back signals from one plan.
status: active
---

# plan-sideways-concept-emission

SIDEWAYS cycles often emit many concept references because they compare two slices' primitive vocabularies. The pattern recurs that the Synthesizer emits `concept_writes mode=create` for ≥3 concepts at once, of which most already exist on disk. The integrator auto-rewrites each to `mode=append-section` (meta-19) but the volume signals discipline erosion.

Cycle 161 (SIDEWAYS cg,gmres) emitted 10 concept_writes mode=create on 10 already-existing concepts, producing 20 push-back signals (one per auto-rewrite + one per content-shape normalization).

## Trigger

Apply this skill before emitting a plan with ≥3 `concept_writes` entries, especially on SIDEWAYS pushes.

## Procedure

1. **Enumerate the concepts the plan references.** List the names of all concept_writes entries plus any concepts referenced by name in slice_writes / section_appends / file_edits content (for cross-slice comparison prose).

2. **Check each name against the on-disk concept index.** The plan's input includes the current state of `book/src/concepts/index.md`. For each name, determine: exists-on-disk (true/false).

3. **Classify each emission:**
   - Existing concept being extended → `concept_writes mode=append-section` with heading naming the new angle.
   - Genuinely new concept → `concept_writes mode=create` with full file content.
   - Concept being referenced but not edited → no `concept_writes` entry; just markdown links in the slice prose.

4. **Default to `mode=append-section` on SIDEWAYS.** SIDEWAYS plans rarely introduce genuinely new concepts — they compare existing slices' vocabularies. The default for any concept the SIDEWAYS plan touches should be:
   - Already exists in the dep-map → `append-section` (add a "## Cross-slice notes (cg, gmres)" section showing the comparison).
   - Not in the dep-map → carefully consider: is this a genuinely new concept, or am I about to duplicate something? If new, `mode=create`. If unsure, omit the `concept_writes` entry and rely on the slice cross-references.

## Existing concepts (as of meta-25)

For convenience, the well-established concepts that SIDEWAYS plans MUST NOT recreate (use `mode=append-section`):

- BLAS-style: `apply_linop`, `axpy`, `dot`, `nrm2`, `scal`, `givens`, `trsv`, `gemv_basis`, `elementwise-product`, `set_subvector_zero`, `ksp_solve`
- Methodology: `rotation`, `variant-absorption`, `constructed-operators`, `state-stratification`, `solve-monad`, `tensor-field-lift`, `sequential-obstruction`, `derived-view-hoisting`, `convergence-test`, `negative-result-slice`
- Algorithm: `gmres`, `chebyshev-iteration`, `orthogonalization`, `incremental-least-squares`
- Framework: `solver-as-operator`, `complex-from-real-lift`, `two_operator_split`, `constructed-operator-factory`, `finest-level-unwrap`, `counter-update`

If your SIDEWAYS plan creates any of these, it WILL be auto-rewritten — emit them as `mode=append-section` directly.

## Cross-references

- Synthesizer prompt *SIDEWAYS output discipline* (the higher-level rule).
- meta-19 integrator auto-rewrite (the safety net this skill exists to make unnecessary).
- `book/src/concepts/index.md` — authoritative list of concepts on disk.
