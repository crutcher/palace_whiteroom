---
edges:
  reference:
    - concepts/axpy                  # L2 form being lifted
    - concepts/dot                   # L2 form being lifted
    - concepts/nrm2                  # L2 form being lifted
    - concepts/scal                  # L2 form being lifted
    - concepts/apply_linop           # L2 form being lifted
    - concepts/sequential-obstruction  # when the lift fails
    - concepts/rotation              # underlying rotation methodology
---

# Concept: tensor-field-lift

The L2→L3 lift for the support-operator family (`axpy`, `dot`, `nrm2`, `scal`, `apply_linop`). At L2 these primitives are defined per-DoF / per-element; at L3 they are statements about global tensor fields over the discretised mesh, with no surviving per-element loop in the spec form.

## The lifts

Let `x`, `y` be global field vectors over a DoF index set `I` (with `|I| = n`), `α` a scalar, `L` a linear operator on the field.

- `axpy(α, x, y) → y'`: at L3, `y' = α · x + y` as a vector equation in `R^n` (or `C^n`). The per-DoF loop is implicit in the vector-space statement.
- `scal(α, x) → x'`: at L3, `x' = α · x`.
- `dot(x, y) → r`: at L3, `r = xᴴ · y` (Hermitian inner product). The reduction is implicit; MPI-collective semantics live below L3 (see [concept: dot](dot.md)).
- `nrm2(x) → ‖x‖₂`: at L3, `‖x‖₂ = sqrt((xᴴ · x).real)`.
- `apply_linop(L, x, y) → y`: at L3, `y = L · x` as a field-to-field linear map. Assembly form, matrix-free form, and partial-assembly form are L2 / implementation choices; the L3 spec form is the single linear-map application.

## When the lift is valid

The lift is valid when the L2 primitive operates on each DoF / element independently of the others, OR when the inter-DoF coupling is the *defining* coupling of the operator (as in `apply_linop`). The lift is **not** valid when:

- The L2 form contains a *sequential* reduction over the DoF index where the loop-carried dependency is essential (e.g., a Gauss-Seidel sweep — the `i`-th update reads the `(i-1)`-th output). See [concept: sequential-obstruction](sequential-obstruction.md).
- The state being operated on is not field state — e.g., the dense O(j) LS state in GMRES does not lift; it is not a tensor field.

## Use across slices

- All field-side primitives in the cg, gmres, fgmres slices use this lift.
- The support-operator primitives' L3 form is uniformly the global vector-space statement; the lift is mechanical and does not require per-slice re-derivation.
- The point of recording this as a concept is to make explicit that the L2→L3 edge for the support-operator family is *transparent* (no spec content beyond the vector-space restatement), so that slices can focus their L3 prose on the non-transparent edges (operator compositions, sequential obstructions).

## See also

- [concept: axpy](axpy.md), [concept: dot](dot.md), [concept: nrm2](nrm2.md), [concept: apply_linop](apply_linop.md) — the L2 forms.
- [concept: sequential-obstruction](sequential-obstruction.md) — when the lift fails and what to record instead.
- [concept: rotation](rotation.md) — the underlying rotation methodology; the lift is a state-hiding rotation (the per-DoF loop is hidden) when it succeeds.
