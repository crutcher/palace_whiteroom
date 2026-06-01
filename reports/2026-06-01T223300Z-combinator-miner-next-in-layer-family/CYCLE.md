---
agent: combinator-miner
invoked_at: 2026-06-01T22:33:00Z
scope: Pattern proposal — next in-layer utility combinator family (redirect item 2b); NEGATIVE finding
status: pending
integrated_at: 2026-06-02T010000Z
integration_commit: 9633c134b333932b31f2823c558398fafdaa9750
integration_notes: "cycle-052 D5 — applied clean (NEGATIVE / spine-coverage finding; NO book mutation — firm L2/L3 surface is combinator-complete for in-layer conciseness; 2 OQs promoted; next combinator from solver test-load material). Build-relevant: no."
---

# CYCLE: Combinator candidate — next-in-layer-family (NEGATIVE / spine-coverage result)

## Summary

Surveying the firm L2/L3 surface for the NEXT recurrent base-form pattern a
combinator would simplify (redirect program item 2b, replace-and-propagate,
INWARD/conciseness-driven), I examined all three candidate families named in the
dispatch: **(a) the smoother family**, **(b) the projector/gate family**, and
**(c) the Krylov inner-fold**. **None yields a genuine new in-layer combinator.**
This is a deliberate NEGATIVE finding recorded as a spine-coverage result — NOT a
forced combinator. The redirect explicitly forbids the mine-and-strand
anti-pattern (a combinator that adds vocabulary without simplifying anything
upstream), and each of the three candidates either re-confirms a previously
retired gap or names a pattern the artifact has **already mined and deliberately
kept un-unified with a load-bearing over-unification guard**. The first two
BLAS-1 families (`linear_combination`, `inner_product`) were the genuine
in-layer folds; the remaining firm L2/L3 surface does not present a third
recurrent base-form whose unification would be conciseness-positive. The
candidate-by-candidate adjudication is below.

The redirect's low-priority `l4-propagation-depth-linear-combination`
"flag, don't force" note is not actionable from this dispatch (no L4 propagation
change is implied by a negative in-layer finding); it is mentioned here only to
confirm it was considered and rides forward unchanged.

## Candidate adjudication (all three surveyed; all NEGATIVE)

### (a) Smoother family — RE-CONFIRMS the retired richardson gap. NEGATIVE.

The `jacobi-smoother` (`op.dinv ⊙ x`) + `chebyshev-iteration` / `chebyshev`
apply-shape unification (`polynomial_smoother` subsuming Jacobi as `order=0` and
Chebyshev as `order≥1`) is **CLOSED-BLOCKED-RETIRED** (OQ
`polynomial-smoother-l2-combinator-from-jacobi-and-chebyshev`,
`scaffolding/open-questions.md:578, :628`, closed cycle-036 meta-phase: Palace
has no third Richardson sibling; out of scope per the unimplemented-Palace-
components policy). I did NOT re-propose the retired richardson-sibling form.

Beyond the retired-OQ status, the **structural** reason the unification fails is
recorded in the firm L2 entry itself: `book/src/L2/jacobi-smoother.md:73-78`
states the `polynomial_smoother` combinator "is a candidate but **not pursued
here** — Jacobi's per-call action is a plain elementwise scaling, not a
polynomial action, and the unification would obscure the apply's identity with
the underlying elementwise-product field operation." The Jacobi apply is the
degree-zero fixed point of the fusion rotation with **no fused multi-operation
kernel to unfold** (`book/src/L2/jacobi-smoother.md:160-185`, the "Negative
fusion observation"), whereas `chebyshev-iteration`'s apply de-fuses into a
genuine three-term recurrence (`book/src/L2/chebyshev-iteration.md:78-100`). A
`polynomial_smoother` combinator would have to special-case `order=0` into a
non-recurrence — adding vocabulary that obscures rather than simplifies. This is
the exact mine-and-strand shape the redirect forbids. **NEGATIVE — gap
re-confirmed.**

### (b) Projector / gate family — ALREADY MINED; over-unification guard is load-bearing. NEGATIVE.

`divfree-projector` + `deflate` (+ the related `orthogonalize`) all surface a
tempting `subspace_project`-shaped pattern: *extract coordinates against a
subspace ▷ solve/correct ▷ back-project and subtract*. The artifact has
**already mined this family and deliberately kept the three projectors distinct
with an explicit, load-bearing over-unification guard**:

- `book/src/L2/deflate.md:248-276` (§"Over-unification guard: `deflate` vs
  `orthogonalize`") — "They are RELATED but DISTINCT. Do NOT collapse them into
  one combinator." The cycle-021 combinator-miner proposal flagged this collapse
  explicitly as an over-unification to avoid. The **decisive distinguisher** is
  the Gram-matrix `lu_solve`: `orthogonalize` is `deflate` at `gram = I`
  (orthonormal basis, Gram-solve-free sequential rank-1 subtraction), while
  `deflate` is the general non-orthonormal-basis parent whose `(XᴴX)⁻¹` / Schur
  correction is **load-bearing** — erasing it "would silently assume the
  deflation basis is orthonormal (it is not), changing the algorithm and the
  result" (the §Algebraic-laws "orthogonality of the projector" non-law,
  `book/src/L2/deflate.md:230-234`).
- `divfree-projector` is structurally a **third thing**: a constructed-operator
  gate whose subspace "solve" is a nested **iterative** `ksp_solve` of `P.M·ψ =
  rhs` (`book/src/L2/divfree-projector.md:114-134`, the four-step
  `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad`), carrying a `sequential-obstruction`
  BY REFERENCE — not a small-dense `lu_solve` (deflate) and not a sequential
  rank-1 MGS subtraction (orthogonalize). Its "coordinates" are an H1-side weak
  divergence, not a `dot` against basis columns; its "subspace" is the discrete
  gradient range, not a stored column basis. It is explicitly framed as a
  standalone gate with NO fold-parent, sibling to `ksp_solve` / `eigsolve`, not
  to the projector compositions (`book/src/L2/divfree-projector.md:47-59`).

A `subspace_project` combinator over these three would have to be parameterised
along (i) basis-storage (stored columns `X` vs. implicit gradient range), (ii)
solve-kind (Gram `lu_solve` vs. Schur-modified vs. nested iterative `ksp_solve`
vs. *no solve at all* for orthonormal MGS), and (iii) coordinate-extraction
(`dot`-against-columns vs. `WeakDiv` operator-apply). At that point the
"combinator" is a tagged union with a per-tag body and **no shared combining
step** — it would NOT simplify any of the three entries (each still needs its
full body), and it would re-introduce exactly the collapse the cycle-021
over-unification guard was authored to prevent. This is mine-and-strand: added
vocabulary, zero upstream simplification. **NEGATIVE — family already mined,
deliberate-distinctness is the correct result.**

The legitimate cross-reference (`orthogonalize = deflate |_{gram=I}` as a
specialization *edge*, `book/src/L2/deflate.md:261, :271`) is a
`same-layer-cross-cutter` concern (a cross-link, not a combinator) and is already
recorded. No combinator-miner action.

### (c) Krylov inner-fold — already the firm `inner_product` / `dot` / `nrm2`; krylov-step is NOT an algebra. NEGATIVE.

`krylov-step`'s scalar-stratum updates (`dot Ap p`, `dot r' r'` for CG; `dot v_i
w` per orthogonalize iteration for GMRES; `β = |s[j+1]|`) are inner-product /
norm reductions (`book/src/L2/krylov-step.md:50, :60`). But these are **already
the firm L2 `inner_product` / `dot` / `nrm2` fold** — the second BLAS-1 family
already crystallized (the D1–D4 territory of this very cycle). There is no
*third* fold here; the inner products inside `krylov-step` are *consumers* of the
existing `inner_product` combinator, not instances of a new one.

Moreover `krylov-step` is explicitly **"a fold kernel, not an algebra in its own
right"** (`book/src/L2/krylov-step.md:73`): it is a unary endomorphism on
`IterState` whose only non-trivial law is the demand-pruning
output-extras-distributivity law (`:77`), and it carries explicit *non*-laws for
commutativity, associativity, identity, and linearity (`:85-89`). It is the body
the L4 `iterate_while` outer driver folds — there is no in-layer combinator to
extract from it that isn't already the `inner_product` fold or the `iterate_while`
driver. **NEGATIVE — no new fold; the inner products are the existing one.**

## Why this is a spine-coverage result, not a miss

The first two genuine in-layer folds (`linear_combination` over the
scalar-weighted-sum BLAS-1 leaves; `inner_product` over the reduce-to-scalar
BLAS-1 leaves) were crystallized because they had (i) ≥3 fixed-arity
specializations sharing (ii) a single combining step with (iii) a stateable
fold-law (concatenation-homomorphism). Scanning the remaining firm L2/L3 surface
in **both** modes (same-shape and parametric-family, including the
constructed-operator-action-family mode):

- **Same-shape mode**: the recurrent base-form shapes are already named
  (`apply_linop`, `elementwise_product`, `reciprocal`, `assemble-diagonal` for
  the elementwise/operator-to-data primitives; `dot`/`nrm2`/`scal`/`axpy`/`axpby`/
  `axpbypcz` for BLAS-1, now stub-reduced per CYCLE-052 #1). No un-named ≥3
  recurrence remains.
- **Parametric-family / fold mode**: the two folds are taken. The projector
  "family" (b) fails the fold-law guard — there is no single combining step the
  three projectors share (Gram-`lu_solve` vs. Schur-solve vs. nested
  `ksp_solve` vs. no-solve-MGS), so per the mode's own guard it is NOT a fold
  family.
- **Constructed-operator-action-family mode**: the smoother cohort (a) is exactly
  the `constructed-operator-action family` this mode targets (`JacobiSmoother` /
  `ChebyshevSmoother` siblings sharing a `Solver<OperType>::Mult` contract). But
  it is **already captured** — `jacobi-smoother` and `chebyshev-iteration` are
  firm L2 entries, both citing the shared `AssembleDiagonal + Reciprocal` setup
  chain (`book/src/L2/jacobi-smoother.md:66-78`), and the unifying parametric
  view (`polynomial_smoother`) was deliberately declined for the structural
  reason above. The cohort is captured; the unification is correctly NOT pursued.

The remaining firm L2/L3 surface is **combinator-complete for in-layer
conciseness** as of the BLAS-1 fold crystallization. The next genuine in-layer
combinator, if one exists, will surface from *new* L2/L3 material (e.g. an FE
assembly cohort or a transient-solver time-stepping cohort pulled up as the
low-priority solver test-load), not from the currently-firm surface. That is the
spine-coverage signal this dispatch contributes: **the firm L2/L3 surface has no
un-mined in-layer family left** — forcing a third would be mine-and-strand.

## Proposed combinator

**NONE.** This is a deliberate negative finding. No `book/src/L<n>/index.md`
dep-map rough-in row is proposed (a rough-in for a combinator that simplifies
nothing would be the mine-and-strand defect the redirect forbids).

## Proposed changes

**No artifact changes.** (A negative finding produces no dep-map row.) The
spine-coverage result is recorded here and surfaced as an Open question for the
meta-phase to fold into the plan's frontier assessment.

## Supporting evidence

- `book/src/L2/jacobi-smoother.md:73-78` — the `polynomial_smoother` combinator
  considered and declined (Jacobi apply is plain elementwise scaling, not a
  polynomial action).
- `book/src/L2/jacobi-smoother.md:160-185` — the "Negative fusion observation":
  the Jacobi apply is the degree-zero fixed point with no fused kernel to unfold.
- `book/src/L2/chebyshev-iteration.md:78-100, :142-148` — the genuine three-term
  recurrence the Chebyshev apply de-fuses into (the structural contrast that
  blocks a clean `order=0`/`order≥1` unification).
- `scaffolding/open-questions.md:543, :578, :628` —
  `polynomial-smoother-l2-combinator-from-jacobi-and-chebyshev` deferred-then-
  CLOSED-BLOCKED-RETIRED (no third Richardson sibling in Palace).
- `book/src/L2/deflate.md:248-276` — the `deflate` vs `orthogonalize`
  over-unification guard (Gram-`lu_solve` is the load-bearing distinguisher; do
  NOT collapse).
- `book/src/L2/deflate.md:230-234` — the "orthogonality of the projector"
  non-law (erasing `(XᴴX)⁻¹` silently assumes orthonormality, changing the
  algorithm).
- `book/src/L2/divfree-projector.md:47-59, :114-134, :149-171` — `divfree-projector`
  as a standalone constructed-operator gate with a nested iterative `ksp_solve`
  (carried-by-reference obstruction), structurally distinct from both
  composition-projectors.
- `book/src/L2/krylov-step.md:50, :60, :73, :85-89` — the scalar-stratum inner
  products are consumers of the existing `inner_product` fold; `krylov-step` is a
  fold kernel, not an algebra (explicit non-laws for commutativity / associativity
  / identity / linearity).
- `book/src/L2/index.md:21-26, :29` — the four firm named-compositions + two
  fold-cohorts + the fork-INDEPENDENT standalone-floor cohort; the do-NOT-merge
  boundaries that confirm the surface is already mined.
- Palace source (transitive, cited in the entries above):
  `palace/linalg/jacobi.cpp:30-39, :79-93` (Jacobi apply + setup);
  `palace/linalg/chebyshev.cpp:68-78, :112-123, :177-178` (Chebyshev fused
  kernels + shared setup chain);
  `palace/linalg/nleps.cpp:505-537` (deflate Schur block);
  `palace/linalg/divfree.cpp:155-187` (divfree four-step apply).

## Open questions / caveats

- **`firm-l2-l3-surface-is-combinator-complete-for-in-layer-conciseness`
  (spine-coverage result, NEW).** After the two BLAS-1 folds
  (`linear_combination`, `inner_product`) were crystallized, the remaining firm
  L2/L3 surface presents NO un-mined in-layer family: the smoother cohort (a) is
  captured-but-correctly-not-unified (retired richardson gap + Jacobi-degree-zero
  structural mismatch), the projector family (b) is mined-and-deliberately-kept-
  distinct (load-bearing over-unification guard), and the Krylov inner-fold (c)
  IS the already-firm `inner_product` fold. The next genuine in-layer combinator
  will surface from *new* L2/L3 material (the low-priority solver test-load: FE
  assembly, transient time-stepping), not from the currently-firm surface.
  **Implication for the plan**: combinator-miner dispatches on the *current* firm
  surface are now low-yield; combinator-miner is best re-pointed at newly-lifted
  solver-test-load material as it lands, rather than re-scanning the saturated
  BLAS/projector/smoother surface. Meta-phase to weigh whether to pause
  in-layer combinator-mining until new material arrives.

- **`orthogonalize-deflate-specialization-edge-is-cross-cutter-not-combinator`
  (caveat).** The legitimate `orthogonalize = deflate |_{gram=I}` specialization
  relationship (`book/src/L2/deflate.md:261, :271`) is a same-layer cross-reference
  EDGE, already recorded, NOT a combinator. If a future pass is tempted to read
  it as a combinator-mining opportunity, the over-unification guard
  (`book/src/L2/deflate.md:248-276`) is the standing answer: the edge is a
  cross-link, the entries stay distinct.

- **`l4-propagation-depth-linear-combination` (rode-along, not actionable here).**
  The low-priority "flag, don't force" L4-propagation-depth note was considered;
  a negative in-layer finding implies no L4 propagation change, so it rides
  forward unchanged. No action proposed.

- **CYCLE.md filter note:** no filter block encountered writing this CYCLE.md.
