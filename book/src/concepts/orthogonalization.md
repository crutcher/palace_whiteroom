# concept: orthogonalization

The Arnoldi orthogonalisation step in Krylov-subspace methods: given an orthonormal basis `V[0..j]` and a new vector `w`, produce `(w', h)` where `w'` is the component of `w` orthogonal to `span(V[0..j])`, and `h = (h_0, …, h_{j+1})` are the projection coefficients (entries of the Hessenberg matrix's new column, with `h_{j+1} = ‖w'‖`).

## Variants

Three implementations occupy the same L1 primitive role but differ at L2 / L3 in `dot`/`axpy` batching and stability:

- **MGS (Modified Gram–Schmidt)**: sequential per-`k` project-and-subtract. For `k = 0..j`: `h[k] = dot(V[k], w); axpy(-h[k], V[k], w)`. Numerically more stable than CGS; requires `j+1` synchronisation points per Arnoldi step.
- **CGS (Classical Gram–Schmidt)**: batched. All `j+1` `dot`s first (one MPI reduction), then all `j+1` `axpy`s. One synchronisation point per Arnoldi step; loses orthogonality faster than MGS, especially for ill-conditioned bases.
- **CGS2 (CGS with re-orthogonalisation)**: CGS applied twice — one batched orthogonalisation, then a second batched correction. Two synchronisation points per step; recovers MGS-level orthogonality up to roundoff ("twice is enough" — Kahan/Parlett).

## L1 contract

At L1, orthogonalisation is a single primitive `orthogonalize(gs_orthog, V[0..j], w) → (w', h)` that dispatches on `gs_orthog ∈ {MGS, CGS, CGS2}` exactly once. Downstream code does not re-inspect the variant.

## L2 / L3 distinction

The primitive *set* — `dot`, `axpy`, `nrm2`, `scal` — is the same across all three variants. The variant axis affects only the *sequence and batching* of these calls. A dedicated `orthog` slice would carry the L2→L3 unfolding where the global-tensor / batched-collective form makes the MPI synchronisation structure explicit.

## Citations

- Palace `OrthogonalizeColumnMGS / CGS / CGS2` family, `palace/linalg/orthog.{hpp,cpp}` (separate slice).
- Dispatch site: `OrthogonalizeIteration(gs_orthog, V, w, Hj, j)`, `palace/linalg/iterative.cpp:307–326`.

## Concept: `orthogonalization` (Gram-Schmidt variants)

Given an orthonormal basis `V_j = [v_0 … v_{j-1}]` and a new vector
`w`, produce coefficients `h_{0..j-1}` and the orthogonal residual
`w' = w − Σ h_i v_i` such that `⟨w', v_i⟩ = 0` for all `i < j`.

## Background

The Gram-Schmidt orthogonalization step inside Arnoldi-style Krylov
basis construction. Two dominant variants (Saad 2003 §6.3.2):

- **MGS (modified Gram-Schmidt)**: sequential subtraction — for each
  `i = 0..j-1`: `h_i ← ⟨v_i, w⟩; w ← w − h_i v_i`. Better numerical
  stability than CGS but sequential (`j` synchronization points).
- **CGS (classical Gram-Schmidt)**: parallel — compute all `h_i ← ⟨v_i,
  w⟩` in one pass, then `w ← w − Σ h_i v_i`. Faster (one global reduce,
  one batched update) but loses orthogonality in finite precision.
- **CGS2 (CGS with reorthogonalization)**: CGS applied twice; the
  second pass recovers orthogonality. Palace uses CGS2 by default for
  parallel scalability while preserving the stability of MGS.

The variant is exposed as a runtime enum (`OrthogType`) on the GMRES
solver.

## Signature (canonical)

```
orthogonalize(variant, V_basis, w) → (h_coeffs, w')
  // w may be mutated; h_coeffs is a length-j vector
```

## Slices that use this primitive

- [gmres](../spec/slices/gmres.md) — orthogonalizing the new Arnoldi
  vector against the existing basis. The variant axis is absorbed at
  this primitive's contract: per-step procedure dispatches once on the
  variant and never re-inspects.
