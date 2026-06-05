---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/back_solve
    - L1/ls-update-column
    - L1/orthogonalize
---

# L1 — Krylov least-squares leaves

The per-column and restart-close leaves of the GMRES/FGMRES Krylov state advance — the L1 projections of the firm L2 named composition `incremental-least-squares`. `orthogonalize` is the basis-streaming leaf (Gram–Schmidt of a candidate against a stored basis, `MGS | CGS | CGS2` variant axis); `ls_update_column` is the factorisation-streaming producer (one running-QR column: replay ▷ generate ▷ apply, exposing the LS residual norm as a unitary byproduct); `back_solve` is the terminal consumer (the upper-triangular `R·y = s` restart-correction back-solve). The producer/consumer relation `ls_update_column ▷ back_solve` and the per-column co-invocation with `orthogonalize` inside `krylov-step` are dep-map siblings, not dependencies.

`back_solve` is explicitly **not** a general `trsv` (the unanchored sparse-triangular smoother kernel; that obstruction stays open) and is small-dense-triangular only.

Chapters are listed alphabetically.
