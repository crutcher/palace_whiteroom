---
rank: firm
edges:
  depends-on:
    - L1/weak_op
    - L0/leaf_cite
---
# widget-lowering (lowering theme)

A lowering theme declaring rank firm, but one endpoint (weak_op) is rough-in, so
the lowering-theme rule (rank = min endpoints) must NOTE that declared firm
exceeds min-of-endpoints rough-in.
