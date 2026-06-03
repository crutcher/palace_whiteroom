# L1 > L0 — Mutation-rotation themes

The bulk of the L1>L0 lowering: themes that rewrite a pure-functional L1 form into its L0 in-place-mutation C++ source pattern. The recurring rewrite shapes are the ones the Part overview names — in-place axpy as `x.Add(α, y)`, operator application as `A.Mult(x, y)` (output-arg convention), workspace-buffer reuse as mention-and-erase, and the constructed-operator absorption rules (timer erase, warning-to-structured-field, counter-to-driver-accumulator, destination-binding). Each theme carries `palace/<file>.cpp:<lines>` evidence and records load-bearing numerical tricks (pinned reduction-tree non-associativity, descending back-substitution order) as explicit non-laws.

Themes are listed alphabetically.
