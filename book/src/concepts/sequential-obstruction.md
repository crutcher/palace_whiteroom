# Concept: sequential-obstruction

A *sequential obstruction* is a structural failure of the L2→L3 lift: a sub-procedure whose loop-carried dependency cannot be hidden behind a global tensor-field statement. Recording the obstruction as a first-class L3 result is preferred over forcing a contrived global form.

Sequential obstructions are a structural feature of the algorithm, not a defect of the spec. They surface algorithmic choice points: the obstruction either (a) is benign — the sequential state is small dense, costs nothing relative to field-side work — or (b) drives algorithmic substitution — e.g., picking Jacobi over Gauss-Seidel to recover parallelism, or picking CGS over MGS for the same reason.

## How to record an obstruction

When a slice's L2→L3 lift encounters a sequential sub-procedure:

1. **Name the recurrence.** State the loop variable, the loop-carried state, and the dependency that prevents a parallel reduction. For GMRES `ls_update_column`: the loop variable is the rotation index `k`, the state is the column `h[0..j+1]`, and the dependency is that rotation `k+1` operates on the output of rotation `k`.
2. **Classify the state.** Is the loop-carried state *field state* (per-DoF over the mesh, O(n)) or *small dense state* (O(j) or O(constant), not indexed by the mesh)?
   - **Field state, sequential** — heavy obstruction. Drives algorithmic substitution (Gauss-Seidel ⇒ Jacobi or multicolor). Spec records the obstruction and lists the substitutions considered.
   - **Small dense state, sequential** — benign obstruction. The sequential cost is O(j) or O(j²) on a buffer that fits in cache; the field-side work dominates. Spec records the obstruction and notes that no substitution is pursued.
3. **Consider alternative formulations.** Could the sequential form be reformulated as a batched / parallel operation at higher cost? If yes, record the alternative and the cost comparison. If no, say so.
4. **State the L3 form.** For a small-dense-state obstruction, the L3 form is the L1 form unchanged — there is no field-side rewrite. For a field-state obstruction, the L3 form may name the substituted algorithm (e.g., "L3 uses Jacobi") and route the original sequential algorithm to a separate slice or note.

## Examples

- **GMRES `ls_update_column`** (small dense state, sequential, benign). Loop over rotation index `k` on dense state of size O(j) ≤ O(max_dim). No substitution pursued; the L3 form is the L1 form.
- **GMRES `back_solve`** (small dense state, sequential, benign). Triangular solve on O(j²) dense state; deferred once at end of cycle.
- **MGS orthogonalization** (mixed: field state per `k`, but the recurrence is over `k`, not over DoFs). Each `k` step is a global `dot`+`axpy` on field state; the recurrence is over the basis index. Classifying as sequential on the *basis index* with field state operated on inside each step. CGS is the parallel-reduction alternative; the choice is exposed as the `gs_orthog` variant.
- **Gauss-Seidel smoothers** (field state, sequential, heavy). The canonical heavy obstruction; drives Jacobi substitution or multicolor reordering for parallelism. Not yet a slice but the example motivating this concept.
- **Triangular solves on assembled sparse triangular matrices** (field state, sequential, heavy). The forward / backward solve in a sparse factorisation; no parallel form without level-set scheduling.

## Why first-class

A spec that silently absorbs a sequential algorithm into a fictional global form misrepresents the algorithm. The reader cannot tell from the spec whether the L3 form is genuinely parallelisable or whether the parallelism was hand-waved. Recording the obstruction explicitly is the auditable form.

The Synthesizer's per-edge `rotation_claim` for an obstructed L2→L3 should use `justification_kind: "obstruction"` and name the recurrence and state classification.

## See also

- [concept: tensor-field-lift](tensor-field-lift.md) — the lift that fails, and the conditions under which it succeeds.
- [concept: rotation](rotation.md) — obstructions are *negative* rotations: the to_form is the from_form, with an explanation of why no rotation exists.
