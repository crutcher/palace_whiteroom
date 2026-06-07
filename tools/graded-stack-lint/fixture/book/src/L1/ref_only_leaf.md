---
layer: L1
operator: ref_only_leaf
rank: firm
edges:
  depends-on:
    - L0/leaf_cite
---
# ref_only_leaf (firm; reference-reachable ONLY — the §2g / RE11 cohort)

A firm op that NO feature root `depends-on`, but that a reachable root reaches
over a `reference`-class edge (`feature/widget.L4 --reference--> L1/ref_only_leaf`
— the combinator-primary leaf / DIRECTIVE-3 kernel-impl `realizes-kernel-api`
pattern). The depends-on-only GC marks it DETRITUS (`[GARBAGE*]`, since it
declares a typed `depends-on` dep), but the ASK-1 / scheme-§2g reference-
augmented mark reaches it, so it lands in the `reference_reachable` detritus
sub-bucket (RE11), NOT in `true_detritus`. This regression-guards that the
reference-reachable split separates the deliberate cohort from genuine garbage.
