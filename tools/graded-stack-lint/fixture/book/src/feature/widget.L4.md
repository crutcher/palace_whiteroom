---
kind: feature-surface
feature: widget
level: L4
feature_root: seed
rank: firm
edges:
  depends-on:
    - L1/good_op          # firm vocabulary op (well-founded)
    - L1/prose_firm_provenance  # firm via prose ## Status (provenance-mention bug guard) -> NO violation
    - L1/weak_op          # rough-in op -> RANK VIOLATION (firm rests on rough-in)
  reference:
    - feature/sibling.L4  # sibling root: reference, not blocking
---
# widget (L4 feature column)

Seed fixture: a feature-root column whose own composition includes a rough-in
op, so the rank linter must flag `feature/widget.L4 (firm) -> L1/weak_op (rough-in)`.
