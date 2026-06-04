---
layer: L1
operator: orphan
rank: firm
edges:
  depends-on:
    - L0/leaf_cite
---
# orphan (firm but UNREACHABLE)

A firm op that no feature root depends on. The reachability GC must report it
as DETRITUS even though its rank is firm.
