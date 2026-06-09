---
edges:
  reference:
    - concepts/constructed-operators
    - concepts/variant-absorption
    - concepts/apply_BA
---
# rotation

## Concept

A **rotation** is the methodology's fundamental unit of progress: a re-expression of a piece of work from layer L_n into layer L_{n+1} that *changes the impedance* — mutation → purity (L0→L1), fusion-unfolding → algebraic decomposition (L1→L2), iteration → global tensor op (L2→L3), operator algebra → formal calculus (L3→L4).

This concept distinguishes **genuine rotations** from **renamings**. A renaming re-expresses the L_n form with primitive names but yields no algebraic compression and no abstraction shift — the rotation collapses, and the L_{n+1} form is L_n with different identifiers.

This concept is **methodology**, not a tensor primitive. It lives under `concepts/` because "what counts as a rotation" is a concept the agent loop needs in its working vocabulary. Most `concepts/` entries — `axpy`, `dot`, `matvec`, etc. — are algebraic primitives the layers reuse; this one is a primitive of the *methodology*, not of the spec content.

## When a rotation has occurred

For a proposed L_n → L_{n+1} rotation to count, **at least ONE** of the following must hold:

### (1) State hiding

L_{n+1} hides at least one piece of state that L_n exposed.

**Canonical route: constructed operators.** When the state to be hidden is a config, table, or factorization that's set once and applied many times, the standard pattern is to **construct an operator** at the appropriate scope and call its `apply` method. The construction-time inputs are hidden inside the operator; the apply-time caller doesn't see them. See `book/src/concepts/constructed-operators.md`.

**Worked example (GMRES).** L1 threads `(V, H, s, cs, sn, j, w-scratch)` through the inner loop; the indexing arithmetic — `H.data() + j*(max_dim+1)`, `Hj[k] = …` for `k=0..j`, `V[0..j_final]` — is visible to the reader of L1. A genuine L2 rotation introduces an `arnoldi_step` primitive whose signature hides those threaded buffers: the caller writes `(state', residual_norm) = arnoldi_step(state, A, B)`. The Givens accumulator, the Hessenberg column slot, the orthogonalization scratch — all hidden inside the primitive's contract.

If the proposed L2 still says `arnoldi_with_givens(V, H, j, ...)` with the same indices threading, no state was hidden, and (1) does not hold.

### (2) Coarser substitution

L_{n+1} admits substitution / replacement at a coarser grain than L_n.

**Worked example.** At L1, swapping MGS (modified Gram-Schmidt) for CGS (classical Gram-Schmidt) requires re-threading per-vector collectives, dot accumulators, and inner-loop structure. At a genuine L2, the choice is a single primitive substitution: `orthog := mgs_step | cgs_step | cgs2_step`. Whole-algorithm correctness arguments factor through the primitive's contract rather than its implementation.

If swapping a sub-algorithm at L_{n+1} still requires touching the same number of call sites and the same threaded state as at L_n, no coarser-substitution interface emerged, and (2) does not hold.

### (3) Threaded-state compression

The state bundle threaded through L_{n+1} is strictly smaller, or at least strictly more abstract, than at L_n.

**Worked example.** L1 of GMRES threads `(V[0..max_dim+1], H column-major packed, s, cs[max_dim], sn[max_dim], j, max_dim, w-scratch, restart)`. A genuine L2 restart-cycle primitive threads `(iterate, residual, basis_handle, convergence_flag)` — same per-step computation, much smaller surface. The implementation buffers are encapsulated in `basis_handle`.

If the L_{n+1} step's signature mentions the same buffers with the same shapes as L_n, the threaded state didn't compress, and (3) does not hold.

## If none of (1)/(2)/(3) hold

The proposed rotation is a **renaming**, not a rotation. The L_{n+1} form is L_n with different identifiers, providing no impedance change. Two possible responses:

- **Merge.** Drop the proposed L_{n+1} for this slice and treat the L_n form as the highest layer the slice has reached. The next attempted rotation on this slice should reach further, with one of (1)/(2)/(3) clearly in view.
- **Redesign.** Reframe the L_{n+1} attempt so one of the criteria holds — typically by identifying a primitive that hides the threaded state (route (1)) or by recognizing a substitution interface that L_n was obscuring (route (2)).

## Carry-through: not every concept must rotate

A genuine rotation moves *some* of the slice forward (via (1) state hiding, (2) coarser substitution, or (3) threaded-state compression). It does **not** require every concept in the slice to be transformed.

A concept that **carries through unchanged** from L_n to L_{n+1} is **legitimate** when:

- **Idiomatic at L_{n+1}.** Its current shape is at the right grain for L_{n+1}'s abstraction; "rotating" it would be cosmetic — a renaming for renaming's sake.
- **Not in conflict with L_{n+1}'s framing.** The rotation of *other* parts of the slice doesn't expose tension with this carry-through (e.g., the carried-through concept doesn't force the rotated parts to re-expose state they hid).

The renaming anti-pattern is **"ALL concepts carry through unchanged with new names"** — nothing moved toward the next layer. A genuine rotation may pass some concepts through unchanged; what matters is that **something** rotated.

**Worked example.** In a hypothetical CG L1→L2 rotation:
- The `axpy(α, x, y)` primitive is already at the right grain for L2 (it's an algebraic operation, not an iterative mutation pattern). L1 already uses `axpy` extracted from the source's `x.Add(α, y)`. At L2, `axpy` carries through unchanged — **legitimate carry-through**.
- The `dot(x, y)` primitive likewise carries through unchanged from L1 to L2 — already idiomatic at L2.
- The actual rotation work at L1→L2 is hiding the explicit per-step indexing of `r_k → r_{k+1}` behind a `cg_step(state) → state'` primitive. That's the **state-hiding** criterion (1) firing for the changed portion.
- An honest rotation identifies: criterion (1) state-hiding satisfied for the iteration-index threading; `axpy`/`dot` carry through as already-idiomatic L2 primitives.

Concepts carrying through are **not** failures unless ALL concepts carry through — that's the genuine-rename anti-pattern.

## What this is NOT

- **Not a quality-of-prose test.** A rotation can be terse or verbose; what matters is whether it changes the abstraction shape.
- **Not a "fewer-symbols" test.** L_{n+1} may have *more* identifiers if those identifiers are now reusable across slices (the unification pattern).
- **Not a requirement that all three criteria hold.** One is enough — they characterize different ways a rotation can succeed.
- **Not a blocker for negative results.** An L2→L3 rotation that fails because the algorithm is genuinely sequential (Gauss-Seidel, triangular solve, …) is **not** a rename-not-rotation failure — it's an `obstruction` result, first-class output. The criteria here distinguish "did a rotation happen at all" from "could a rotation happen given the algorithm's structure."

## Renaming vs. coarser substitution — the algorithmic-substitution test

The trap is that criterion (2) "coarser substitution" can be misread as "uses primitive names instead of operations" — but renaming an operation does NOT make a coarser substitution. The substitution must be *algorithmic*, not nominal.

### The test

Before claiming criterion (2), ask:

> Could a reader replace the L_{n+1} primitive with a **different algorithm** (not just a different implementation of the same algorithm) and still satisfy the L_n contract?

If the answer is "no — the L_{n+1} primitive is just a named version of the L_n operation," it is renaming. If "yes — multiple distinct algorithms could occupy this primitive's slot," it is coarser substitution.

### Worked counter-example: CG L1 → L2

**L1 form (CG inner step):**
```
r ← r - α·Ap        # axpby in-place
β ← (r·r)_new / (r·r)_old
p ← r + β·p         # axpby in-place
```

**Proposed L2 form:**
```
axpby(α, Ap, -1, r)
β ← dot(r, r) / dot(r_old, r_old)
axpby(1, r, β, p)
```

The L2 form names BLAS-1 primitives but does not enable algorithmic substitution. The reader cannot replace `axpby` with "a different algorithm that also satisfies the L1 contract `r ← r - α·Ap`" — there IS only one operation. Same for `dot`. The L2 is a faithful name-mapping of L1, not a rotation.

**Genuine L2 form (alternative):**
```
inner_update := cg_step(state, A) | cgne_step(state, A) | minres_step(state, A)
```

Where `cg_step` performs the three-line update above, `cgne_step` performs the normal-equation variant, and `minres_step` performs the symmetric-indefinite Lanczos-three-term recurrence. Now the L2 primitive `inner_update` admits genuine algorithmic substitution at a coarser grain — the L1 contract "advance the iterate, decrease the residual" is satisfied by multiple distinct algorithms.

### Framework-tier slices and role-parametrized factories

The algorithmic-substitution test above is designed for axis-value variants — `MGS` vs `CGS` are two values of one `gs_orthog` parameter, and the test asks whether a third value (a different algorithm) could occupy the same primitive slot.

**Framework-tier slices** (operator/preconditioner contracts consumed by algorithm slices) sometimes propose role-parametrized factory primitives like:

```
constructed_operator_factory(role: 'krylov' | 'preconditioner', op_a: LinOp, op_m: LinOp) → LinOp
```

This **fails the substitution test even though it looks parametric**: the two role values aren't two values of one algorithm — they're two distinct callable surfaces (a Krylov-step constructor vs. a preconditioner constructor) collapsed into one primitive whose body is `if role == 'krylov' ...`. A reader cannot replace `constructed_operator_factory` with a different algorithm: there is no algorithm at this primitive level. It's a renaming wrapper.

**The fix**: split the factory by role into two named primitives (`make_krylov_constructed_operator`, `make_preconditioner_constructed_operator`), each of which admits genuine substitution at its own level. The L1 form references the appropriate primitive directly; the role-parameter is gone, replaced by a callable choice at construction time.

The general rule: **when a "variant" is two materially-different callable surfaces (different signatures, different bodies, different effects), it's not a variant — it's two primitives**. The parametric collapse fails the substitution test because it hides what the reader needs to see.

### The carry-through escape hatch

Renaming-shaped claims pass the gate when the cycle ALSO rotates other parts of the slice — state hiding on the outer loop, coarser substitution on a different primitive, threaded-state compression on the overall state bundle. Explicitly mark renaming claims as carry-through with criterion-(1)/(2)/(3) at the slice level; the gate fires only when NO claim in the cycle achieves an actual rotation.

## Rotation-quality criteria (restated)

A rotation is *real* (as opposed to renaming) when it satisfies at least one of:

- **(a) State hiding**: the L_n form mentions state that the L_{n+1} form does not. The hidden state is named in the rotation's justification.
- **(b) Coarser substitution**: the L_n form describes a specific algorithm; the L_{n+1} form describes an interface that admits the L_n algorithm as one of multiple implementations. A reader could substitute a different algorithm at L_{n+1} and still satisfy the L_n contract.
- **(c) Threaded-state compression**: state that L_n carries explicitly through every step is bundled or abstracted at L_{n+1}, reducing the number of named variables the procedure manipulates.

These are the same three criteria as (1)/(2)/(3) above, in the compact rotation-claim phrasing.

## Justification kinds

A rotation's justification is one of:

- `algebraic`: an algebraic identity makes the rotation manifest (associativity, distributivity, linearity).
- `structural`: a structural property of the primitives makes the rotation work (commutativity of operator application with scalar-vector ops; locality of element-wise ops).
- `reduction_chain`: a sequence of small algebraic / structural steps, each named.
- `empirical_match`: an executed test confirms the to-form matches the from-form numerically. Preferred when available.
- `obstruction`: the rotation does NOT go through; the justification records the reason as a first-class result (e.g., L2→L3 negative results for genuinely sequential algorithms).

## Slices that use this methodology

All slices; rotation is the universal vocabulary for layer-to-layer mapping.
