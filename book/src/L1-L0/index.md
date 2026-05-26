# L1 > L0 — Lowering layer

The transformation from L1 (mutation-lifted forms) to L0 (cited Palace source ranges). Batched by **themes**.

## Context

L0 is the ground truth: cited Palace C++ source. L1 is its pure-functional lift. This lowering describes how a pure-functional L1 form is the abstract view of the C++ source pattern at L0.

Many themes here capture **how Palace expresses common patterns**:
- In-place axpy as `x.Add(α, y)` → vector-method-call shape
- Operator application as `A.Mult(x, y)` → matrix-method-call shape (output-arg convention)
- Workspace buffer reuse → mention-and-erase patterns

## Theme list

```
(empty — Phase B skeleton.)
```

## Working Notes

- Themes here are the bridge to source citations; every theme entry carries `palace/<file>.cpp:<lines>` evidence.
