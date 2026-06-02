---
agent: combinator-miner
invoked_at: 2026-06-02T195402Z
scope: cycle-068 D3 — rise linear_combination + inner_product to L4; correct L4/index.md:66 to per-case; sole L4/index.md consolidated-count/tally/frontier-prose owner
status: integrated
integrated_at: 2026-06-02T204500Z
integration_commit: PLACEHOLDER_SHA_CYCLE068
integration_notes: |
  Applied by integrator-per-report (staging row 3, applied_at 2026-06-02T203100Z); finalized by integrator-finalize cycle-068.
  linear_combination + inner_product PROMOTED FIRM L4 (the two BLAS-1 data-algebra combinators rise as feature-surface verbs; directive-2 §"combinators rise regardless"). New book/src/L4/{linear_combination,inner_product}.md + SUMMARY L4 alpha-inserts. SOLE L4/index count-owner: :66 13-of-18 per-case correction + firm tally (7+4)->(10+4) + active-frontier prose + 2 rows/bullets. L4 firm 7->10. Build-relevant: cargo make book exit 0. 2 OQs promoted. Zero gate hits.
---

# CYCLE: Combinator candidates — `linear_combination` + `inner_product` rise to L4 (+ L4/index per-case correction + count-ownership)

## Summary

Two firm L3 data-algebra combinators — `linear_combination` (scalar-weighted-tensor-sum
fold) and `inner_product` (reduce-to-scalar reduction) — currently stop at L3 with
explicit "no L4 entry" verdicts (the cycle-010 audit reading that *iteration-structural*
content is the L4 admission test). The 2026-06-01 VOCABULARY-SHIFT REDIRECT +
L4-is-the-backend-lowering-target framing **change that test**: L4 is the **feature
surface** whose semantics match the external GPU-tensor backend, and the data-algebra
combinators are **feature-surface verbs the backend wants**, so they **rise to L4
regardless** of carrying iteration structure (`concepts/black-box-vs-accelerated-kernels.md`
§"The combinators rise regardless"; project memory `project_blackbox_vs_accelerated_kernels`).
This dispatch (a) authors `book/src/L4/linear_combination.md` + `book/src/L4/inner_product.md`
as L4 combinator entries re-expressing **through** their firm L3 forms (replace-and-propagate;
the four `scal`/`axpy`/`axpby`/`axpbypcz` accelerated-kernel leaves and the `dot`/`tdot`/
`bilinear_form` specializations are notes tied below, NOT rectangular mirrors; the L4>L3
edge is identity-in-form, no dedicated theme file — the `eigsolve`/`chebyshev` in-line-marker
route); (b) corrects the `L4/index.md:66` blanket "13-of-18 no-L4-by-design" assertion to
the **per-case** form (combinators rise; kept named abstractions `dot`/`nrm2` rise as named
verbs — next-pull candidates; pure accelerated `axpy`-family leaves correctly stay low); and
(c) as this cycle's **sole `L4/index.md` consolidated-count/tally/frontier-prose owner**,
incorporates D1's landing `fe_assemble` L4 entry + these two new combinators into the firm
tally (counted from each chapter's `## Status` line) and §Active-frontier prose, with own
dep-map rows + cohort bullets in alpha position.

These are **not new mines** — they are the **upward in-layer propagation of two already-firm
mined combinators** (the c049 mine + c050/c051 L3 propagation), so the
`disciplined-cross-pipeline-combinator-mining-gate` 4 points are satisfied by the firm L3
endpoints, not re-mined. The candidate this report proposes is the *L4-layer rendering*, the
top-of-stack rung of the same combinator.

## Pattern instances

The pattern is "a firm L3 data-algebra combinator that the L4 feature surface must name as a
backend-lowering verb, currently stranded at L3 by the stale iteration-structural admission
test." Both qualify; the supporting in-layer + cross-layer instances:

- **Instance 1 — `linear_combination` firm at L3, stranded** (`book/src/L3/linear_combination.md`):
  firm whole-tensor variadic fold `[(Scalar, Tensor[N])] -> Tensor[N]`; §"Lifts from" (`:154-156`)
  + frontmatter `lifts_from` (`:7-8`) assert "no L4 entry." The four arity leaves
  (`scal`/`axpy`/`axpby`/`axpbypcz`) already speak *through* it as specialization notes.
- **Instance 2 — `inner_product` firm at L3, stranded** (`book/src/L3/inner_product.md`):
  firm reduce-to-scalar reduction `Tensor[N] -> Tensor[N] -> Scalar`; §Context (`:74-78`)
  + frontmatter (`:7-8`) assert "No `L4/inner_product` exists." The `dot`/`tdot`/`bilinear_form`
  specializations + the `nrm2` consumer already attach to it.
- **Instance 3 — the classification concept page explicitly queues both** (`book/src/concepts/black-box-vs-accelerated-kernels.md:128-136`):
  "Whichever disposition a special-cased operator lands in, the general combinators it
  specializes — `linear_combination` and `inner_product` — **rise to L4 regardless**…
  (Both combinators currently stop at L3 and are queued to rise to L4 — see the L3 entries.)"
- **Instance 4 — the L4 surface already consumes both inside firm bodies** (`book/src/L4/krylov-step.md:67`):
  the GMRES basis-correction sum is a `linear_combination` over scalar-weighted basis terms;
  CG `α`/`β` + GMRES orthogonalization coefficients are `inner_product` let-bindings — the
  combinators are *used* at L4 with no L4 *entry* naming them (the gap this dispatch closes).
- **Instance 5 — the next-pull L4 consumer is gated on the rise** (cycle-068 plan §Open questions;
  `book/src/L1/assemble_frequency_operator.md`): the driven per-ω system-operator assembly
  `A(ω) = K + iω·C − ω²·M + A2(ω)` is the operator-operand specialization of `linear_combination`;
  its c069 L4 lift re-expresses *through* `L4/linear_combination` — it cannot land until this
  entry is on disk.

## Proposed combinator(s)

Two combinators, both **risen (not newly mined)**:

### `linear_combination`
- **Slug**: `linear_combination` (L4 name matches L2/L3 for cross-layer continuity).
- **Layer**: **L4** (rationale: the *feature surface* / backend-lowering target must name the
  scalar-weighted-sum verb so every in-scope feature reaches L4 against the backend's verbs;
  not L3 — already firm there; not "no L4" — the iteration-structural admission test is
  superseded by the L4-is-the-backend-lowering-target framing).
- **Signature**: `linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]`;
  `= foldl (\acc (a,t) -> acc + scal a t) (zeros N) pairs`.
- **Algebraic intuition**: monoid homomorphism `([(Scalar,Tensor[N])], ++, []) -> (Tensor[N], +, zeros)`
  (concatenation-homomorphism is the defining/unifying law); multilinear in the scalar list;
  permutation-invariant in exact arithmetic (IEEE non-law deferred to the L2>L1 fusion-selection
  theme). Identity element `zeros[N]`.
- **Variant axes**: arity (the unification axis — recovered as term-list length; the four
  fused leaves are stopped-low accelerated kernels); output-aliasing (orthogonal; below-L3);
  element-type (`real ⊑ complex`); operand-category (tensor- | operator-operand, the latter the
  next-pull `assemble_frequency_operator` consumer).

### `inner_product`
- **Slug**: `inner_product` (L4 name matches L2/L3).
- **Layer**: **L4** (same rationale).
- **Signature**: `inner_product :: Tensor[N] -> Tensor[N] -> Scalar`;
  `inner_product_M :: Tensor[N] -> LinearOperator[N,N] -> Tensor[N] -> Scalar`;
  `= reduce (+) zero (zipWith kernel x y)`.
- **Algebraic intuition**: length-concatenation homomorphism `(length-concatenated tensors, ++) -> (Scalar, +)`
  (the defining/unifying law that licenses parallel reduction); conjugate-linear in arg-1,
  linear in arg-2; Hermitian symmetry; PSD at the diagonal (the law `nrm2`'s √ rests on).
  Identity element `zero`. IEEE reduction-tree non-law deferred to the L2>L1 theme.
- **Variant axes**: conjugation-convention (the unification axis — `dot` Hermitian / `tdot`
  unconjugated); element-type; weight-presence (`M = I` / pre-applied `M`).

**Over-unification guard (both):** `linear_combination` and `inner_product` are the small
**algebra of folds** — one tensor-producing (term-list fold), one scalar-producing
(length-axis reduction) — deliberately **NOT merged** (different result types, different
homomorphism domains, different combining steps). The guard is symmetric and carried
identically L2/L3/L4. Additionally `nrm2`/`matrix-weighted-norm` are `√ ∘ abs ∘ inner_product`
**consumers**, NOT fold members (merging would be a category error).

**Why these rise but the accelerated leaves do not (the three-way disposition applied):**
- `linear_combination` / `inner_product` — **the combinators** — rise to L4 regardless
  (`concepts/black-box-vs-accelerated-kernels.md:128-136`).
- `dot` / `nrm2` — **kept named abstractions** (case 2; literature-standard verbs like
  `dot(p, Ap)`, `nrm2(r)`) — rise to L4 **alongside** `inner_product` as named verbs (a
  permitted dual). **Next-pull L4 candidates** (`L4/dot`, `L4/nrm2`); noted, NOT authored this
  cycle (clean follow-on once `L4/inner_product` is on disk).
- `scal` / `axpy` / `axpby` / `axpbypcz` — **pure accelerated kernels** (case 3;
  performance-fused special cases, leaning toward fusion) — correctly **stay low**;
  `linear_combination` rises in their place. No L4 chapter.

**L4>L3 rotation (both):** identity-in-form on the body — value-thread-isomorphic; **no
dedicated L4>L3 theme file** (the in-line-marker route, `eigsolve`/`chebyshev` precedent).
There is no `Solve` monad / state-stratification record / convergence predicate / outer driver
to dissolve — a pure value-producing fold at both layers. An `L4-L3/*-dissolution.md` would be
a **degenerate identity-in-named-terms theme** (the §1d smell), so it is correctly an in-line
note, NOT a theme file.

## Proposed changes

### New file: `book/src/L4/linear_combination.md`

The full body is in this report's supporting doc `L4-linear_combination.md` (same directory).
The integrator applies it verbatim as `book/src/L4/linear_combination.md`. (Body kept in a
supporting file rather than inline to avoid nested-fence truncation per the
`convert-nested-fences-to-indented-code-in-proposed-changes-block` guard — the entry uses
indented code blocks throughout, not nested ```text fences.)

### New file: `book/src/L4/inner_product.md`

The full body is in this report's supporting doc `L4-inner_product.md` (same directory).
The integrator applies it verbatim as `book/src/L4/inner_product.md`.

### SUMMARY.md — register both new chapters (alpha position within the L4 Part)

```edit:book/src/SUMMARY.md
[Add two entries under the L4 Part, each in alpha position among the L4 chapter list:
 `inner_product` after `fold_solve`/before `iterate-while`;
 `linear_combination` after `ksp_solve`/before any later-alpha L4 entry.
 (Integrator: place per the active alpha-within-Part orchestrator carry, directive-3;
 the exact link form is `- [inner_product](./L4/inner_product.md)` /
 `- [linear_combination](./L4/linear_combination.md)`.)]
```

### `book/src/L4/index.md` — (b) per-case correction of the line-66 blanket assertion

```edit:book/src/L4/index.md
REPLACE the single line (currently line 66):

The 13-of-18 BLAS-1 / elementwise / smoother L3 operators remain no-L4-by-design (their L4 form would add no calculus beyond their firm L3 rendering) — that observation stands; what is retired is the inference that the *whole* L4 frontier is therefore exhausted. The solver-test-load is the live source of new combinators.

WITH:

The BLAS-1 / elementwise / smoother L3 cohort is **no longer uniformly no-L4-by-design** — the blanket "13-of-18 remain no-L4" assertion is corrected to the **per-case** disposition of [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) (cycle-068 D3): (1) the **general combinators** [`linear_combination`](./linear_combination.md) and [`inner_product`](./inner_product.md) **rise to L4 regardless** (they are feature-surface verbs the backend wants under L4-is-the-backend-lowering-target — landed firm this cycle; §"The combinators rise regardless"); (2) the **kept named abstractions** `dot` / `nrm2` rise to L4 as named verbs *alongside* `inner_product` (literature-standard units like `dot(p, Ap)` / `nrm2(r)` — the next-pull L4 candidates `L4/dot` / `L4/nrm2`, not yet authored); (3) the **pure accelerated kernels** `scal` / `axpy` / `axpby` / `axpbypcz` correctly **stay low** (performance-fused special cases with no standalone abstraction value — `linear_combination` rises in their place; no L4 chapter). What was retired earlier (the *whole* L4 frontier is exhausted) stays retired; what is corrected now is the over-broad "BLAS-1 cohort has no L4 form" inference. The solver-test-load remains the live source of new *iteration-structural* combinators; the data-algebra combinators are the feature-surface verbs that rise on the L4-is-the-backend-lowering-target warrant.
```

### `book/src/L4/index.md` — (c) consolidated firm-count tally (sole count-owner; counted from `## Status` lines)

Firm count audited this cycle from each linked chapter's `## Status` line (NEVER from index
cells, per the c057-meta count-owner guard):
- Pre-cycle firm per-operator chapters (7): `krylov-step`, `iterate-while`,
  `iterate-while-with-prev`, `chebyshev`, `ksp_solve`, `eigsolve`, `fold_solve` — all `firm`.
- Pre-cycle rough-in (1): `solve_family` — `rough-in (test-coverage-bounded)`.
- + 4 `solve-monad` outer-driver vocabulary anchors (`solve_loop`/`restart_cycle`/`Outcome`/`EigOutcome`; firm dep-map rows, not standalone chapters).
- **This cycle adds 3 firm per-operator chapters**: `fe_assemble` (D1, landing firm this
  cycle), `linear_combination` (D3), `inner_product` (D3).
- **New tally: 10 firm + 4 outer-driver** (per-operator firm 7→10; rough-in 1 unchanged).

```edit:book/src/L4/index.md
REPLACE the cohort-header opening of line 32:

**Firm at L4 (7 + 4 outer-driver)** — `fold_solve` joined the firm cohort cycle-058 (the SECOND solver-driven firm L4 combinator after `solve_family`'s rough-in):

WITH:

**Firm at L4 (10 + 4 outer-driver)** — three firm chapters landed cycle-068 (the FE-cohort→L4 frontier opener + the two BLAS-1 data-algebra combinators): the assemble-fold combinator [`fe_assemble`](./fe_assemble.md) (D1), and the two general data-algebra combinators [`linear_combination`](./linear_combination.md) + [`inner_product`](./inner_product.md) (D3) — the BLAS-1 combinators that rise to L4 regardless as feature-surface verbs the backend wants (`concepts/black-box-vs-accelerated-kernels.md` §"The combinators rise regardless"; L4>L3 identity-in-form on the body, the `eigsolve`/`chebyshev` in-line-marker route — no dedicated theme files). Before them `fold_solve` joined the firm cohort cycle-058 (the SECOND solver-driven firm L4 combinator after `solve_family`'s rough-in):
```

(Integrator note: the cohort-header **bullet list** that follows line 32 lists the firm
operators; D1 appends its OWN `fe_assemble` bullet, and I append the two data-algebra bullets
below as my own rows. The header count `(10 + 4)` is the consolidated tally I own; D1's bullet
is D1-owned. If D1's `fe_assemble` lands as a status OTHER than firm at integration time, the
integrator-finalize recounts from `## Status` and adjusts `10` → the audited value — the
count-owner rule is "count from `## Status` lines," and `10` reflects fe_assemble=firm +
both D3 entries=firm.)

### `book/src/L4/index.md` — (c) §Vocabulary-cohort bullets for the two new combinators (alpha position)

```edit:book/src/L4/index.md
[Add two bullets to the §"Vocabulary cohort" firm list (the bullet block after line 32),
 each in alpha position among the firm-operator bullets — `inner_product` in the i-region
 (after `fold_solve`'s/`eigsolve`'s bullets, before `iterate-while` / `krylov-step`),
 `linear_combination` in the l-region (after `ksp_solve`, before `solve_*`):]

- [`inner_product`](./inner_product.md) — the **reduce-to-scalar inner-product combinator**; a whole-tensor length-axis reduction `α = ⟨x, y⟩` risen to L4 as a feature-surface verb the backend wants (NOT iteration-structural — a pure value-producing data-parallel reduction with no `Solve` monad / carry / predicate). Re-expresses through the firm [`L3/inner_product`](../L3/inner_product.md) (identity-in-form on the body; no dedicated L4>L3 theme — the in-line-marker route). The conjugation / element-type / weight specializations (`dot` / `tdot` / `bilinear_form`) are notes under it; the kept named abstractions `dot` / `nrm2` rise *alongside* as named verbs (a permitted dual; next-pull `L4/dot` / `L4/nrm2`). Sibling of [`linear_combination`](./linear_combination.md) — the scalar-producing half of the L4 algebra of folds (do-NOT-merge over-unification guard).
- [`linear_combination`](./linear_combination.md) — the **scalar-weighted-tensor-sum combinator**; a variadic term-list fold `Σᵢ aᵢ·tᵢ` over `[(Scalar, Tensor[N])]` risen to L4 as a feature-surface verb the backend wants (NOT iteration-structural — a pure value-producing data-parallel fold). Re-expresses through the firm [`L3/linear_combination`](../L3/linear_combination.md) (identity-in-form on the body; no dedicated L4>L3 theme — the in-line-marker route). The four arity leaves `scal` / `axpy` / `axpby` / `axpbypcz` are accelerated-kernel specialization notes tied below (stopped low; the combinator rises in their place). The next-pull operator-operand consumer is the driven [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) (c069, GATED on this entry). Sibling of [`inner_product`](./inner_product.md) — the tensor-producing half of the L4 algebra of folds (do-NOT-merge over-unification guard).
```

### `book/src/L4/index.md` — (c) dep-map rows for the two new combinators (alpha position)

```edit:book/src/L4/index.md
[Add two rows to the §"Operator dep-map" table, alpha position:
 `inner_product` immediately BEFORE the `iterate-while` row (currently line 73);
 `linear_combination` immediately AFTER the `ksp_solve` row (currently line 80).]

| [`inner_product`](./inner_product.md) | `inner_product :: Tensor[N] -> Tensor[N] -> Scalar`; `inner_product_M :: Tensor[N] -> LinearOperator[N,N] -> Tensor[N] -> Scalar`. The reduce-to-scalar inner-product combinator; `= reduce (+) zero (zipWith kernel x y)`; conjugation pinned at arg-1 (`xᴴ y`). Pure value-producing length-axis reduction — no `Solve` monad / carry / predicate. | Concepts: `black-box-vs-accelerated-kernels` (rises-regardless), `dot` (element-type / BLAS-1 heritage), `scalar-promotion` (via the kernel table). L3 row: re-expresses through [`L3/inner_product`](../L3/inner_product.md). Specializations (notes, tied below): `dot` / `tdot` / `bilinear_form`; consumer (NOT member): `nrm2`. | L3 [`inner_product`](../L3/inner_product.md) by **identity-in-form on the body** (value-thread-isomorphic; **no dedicated L4>L3 theme** — in-line §"Downward to L3", the `eigsolve`/`chebyshev` in-line-marker route); substantive translation is the L2>L1 [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) (conjugation/weight dispatch + pinned reduction trees). | `firm` (cycle-068 D3 — risen from firm [`L3/inner_product`](../L3/inner_product.md); the BLAS-1 combinator that rises to L4 regardless as a feature-surface verb, `concepts/black-box-vs-accelerated-kernels.md` §"The combinators rise regardless"; laws carried up unchanged / syntactic-identity escape) |

| [`linear_combination`](./linear_combination.md) | `linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]`; `= foldl (\acc (a,t) -> acc + scal a t) (zeros N) pairs`. The scalar-weighted-tensor-sum combinator `Σᵢ aᵢ·tᵢ`. Pure value-producing term-list fold — no `Solve` monad / carry / predicate. | Concepts: `black-box-vs-accelerated-kernels` (rises-regardless), `scalar-promotion` (`real ⊑ complex` scalar list). L3 row: re-expresses through [`L3/linear_combination`](../L3/linear_combination.md). Arity specializations (accelerated-kernel notes, stopped low): `scal` / `axpy` / `axpby` / `axpbypcz`. Next-pull operator-operand consumer: [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md). | L3 [`linear_combination`](../L3/linear_combination.md) by **identity-in-form on the body** (value-thread-isomorphic; **no dedicated L4>L3 theme** — in-line §"Downward to L3", the `eigsolve`/`chebyshev` in-line-marker route); substantive translation is the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) (arity-dispatch + pinned summation order). | `firm` (cycle-068 D3 — risen from firm [`L3/linear_combination`](../L3/linear_combination.md); the BLAS-1 combinator that rises to L4 regardless as a feature-surface verb; laws carried up unchanged / syntactic-identity escape) |
```

### `book/src/L4/index.md` — (c) §Active-frontier prose: register the three cycle-068 firm landings

```edit:book/src/L4/index.md
[Append a paragraph to the §"Active frontier" block (after the `L4/orthogonalize` bullet,
 currently after line 64 / before the corrected line-66 paragraph):]

**Cycle-068 (batch-21) — the FE-cohort→L4 frontier opens + the data-algebra combinators rise.** Three firm chapters landed this cycle. [`fe_assemble`](./fe_assemble.md) (D1) is the **assemble-fold combinator** — the concatenation-homomorphism `foldr` over weak-form terms, the homomorphic sibling of [`solve_family`](./solve_family.md)'s map, wrapping the opaque libCEED quadrature leaf as a `readonly` black-box-kernel input; it opens the **assemble half** of the deliverable's L4 completeness (directive-1: L4 is the outward backend-lowering target; the FE-assembly cohort stranded at L1 is the hole). [`linear_combination`](./linear_combination.md) + [`inner_product`](./inner_product.md) (D3) are the **two BLAS-1 data-algebra combinators** risen as feature-surface verbs (NOT solver-test-load-driven — they are the data-algebra the iteration-structural combinators *consume* in their step bodies, `L4/krylov-step.md:67`). The data-algebra rise is GATE-clearing: the rank-2 driven [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) L4 lift (c069) re-expresses *through* `L4/linear_combination`'s operator-operand corner, and the kept named abstractions `L4/dot` / `L4/nrm2` are the next clean follow-ons through `L4/inner_product`.
```

Note: D1 adds its OWN `fe_assemble` dep-map row + §Vocabulary-cohort bullet (anchor-distinct,
parallel-safe). I (D3, sole count-owner) own the consolidated **firm-count tally** (the `(10 + 4)`
header), the §Active-frontier consolidated prose, and my own two combinators' rows+bullets.
I do NOT author D1's `fe_assemble` row/bullet.

## Supporting evidence

- Firm L3 endpoints (the value-isomorphism the L4 rises rest on):
  `book/src/L3/linear_combination.md` (firm cycle-050; signature `:36-37`, laws `:80-104`,
  §"Downward to L2" `:108-114`, status `:152`, the stale "no L4" lines `:7-8`/`:154-156`);
  `book/src/L3/inner_product.md` (firm cycle-051; signature+kernel `:82-115`, laws `:206-270`,
  §"Downward to L2" `:363-387`, status `:339-361`, the stale "no L4" lines `:7-8`/`:74-78`).
- L2 originals (transitive L0-evidence home): `book/src/L2/linear_combination.md` (firm
  cycle-018; inverted cycle-049 D1, commit `92327f7`); `book/src/L2/inner_product.md` (firm
  cycle-019; inverted cycle-049 D2).
- Substantive L2>L1 translations (the IEEE non-law / dispatch homes referenced, not restated):
  `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; cycle-049 D1(c) KEEP);
  `book/src/L2-L1/inner-product-fold-specialization.md` (KEPT; cycle-049 D2(c)).
- Classification: `book/src/concepts/black-box-vs-accelerated-kernels.md` (cycle-067 D3) —
  §"The combinators rise regardless" `:128-136`; §2 kept-named-abstractions `:88-109`;
  §3 accelerated-kernel-stopped-low `:111-126`.
- Mining gate: `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md` — satisfied
  by the firm L3 endpoints (these are propagations of settled mines, not new mines).
- L4 precedents for the entry shape + the in-line-marker L4>L3 route: `book/src/L4/eigsolve.md`
  (in-line marker-erasure, `L4/index.md:39`/`:81`); `book/src/L4/chebyshev.md` (no L4-L3 theme,
  `L4/index.md:75`); `book/src/L4/fold_solve.md` (the firm-entry frontmatter/status template).
- Strawman: `book/src/design/l4_calculus.md` — neither combinator adds a reduction rule.
- Tests as semantic supplement: `test/unit/test-vector.cpp:206-207` (real-dot value test,
  inherited via L2) is the positive `inner_product` witness; no dedicated `linear_combination`
  test (the firm-without-dedicated-test bar, the `chebyshev` precedent — every L4 law is a
  syntactic identity carried up from the firm combinator below).

## Open questions / caveats

- **Stale "no L4" lines in the firm L3 entries (re-anchor pass needed; OUT of this cycle's
  edit scope).** Both `book/src/L3/linear_combination.md` (frontmatter `lifts_from` `:7-8`;
  §"Lifts from" `:154-156`) and `book/src/L3/inner_product.md` (frontmatter `:7-8`; §Context
  `:74-78`) assert "no L4 entry exists." With these L4 entries on disk those lines are stale.
  I did NOT edit the L3 entries (one-operator-per-dispatch + they are outside this report's
  write-scope; the same routine `eigsolve` triggered for the seven stale `L3/eigsolve`
  §Upward "no L4 cap" assertions, `L4/index.md:81`). **Proposed follow-up:** a thin
  lifter / lowering-verifier re-anchor pass (c069 or batch-21 meta) flips both L3 entries'
  "no L4" lines to "lifts to `L4/{linear_combination,inner_product}` (firm cycle-068)." Filed
  as a plan candidate; flag for the c069 planner.
- **Kept named abstractions `L4/dot` + `L4/nrm2` are the next-pull (NOT authored this cycle).**
  Per directive-2 disposition-2 they rise to L4 alongside `inner_product` as named verbs (the
  permitted dual). I deliberately did not author them this cycle (D3 scope = the *combinators*;
  the named verbs are clean follow-ons once `L4/inner_product` is on disk, and authoring 4 L4
  entries in one dispatch breaks one-operator-per-dispatch). They are noted in the
  `L4/inner_product` §"Specializations" + the corrected index line as next-pull candidates.
  If a c069 consumer needs `dot(p, Ap)` named at L4 before then, author `L4/dot` re-expressing
  through `L4/inner_product`.
- **`fe_assemble` firm-count dependency on D1.** I counted `fe_assemble` as firm in the
  `(10 + 4)` header on the basis that D1's harvester scope lands it firm this cycle. If D1's
  entry lands a status OTHER than firm (e.g. `rough-in` on a libCEED-leaf caveat),
  integrator-finalize must recount from the `## Status` lines and adjust `10` → the audited
  value (the count-owner rule is "count from `## Status` lines"). Stated explicitly so the
  finalize recount has the rule, not just the number.
- **No L0 close-brace citations this dispatch (recurrence-6 N/A).** Both L4 entries inherit
  all L0 evidence transitively through the firm L3/L2 combinators (self-verified there
  cycle-018/019); no fresh `path:lo-hi` range is cited, so there is no close-brace END to
  on-disk-confirm. The recurrence-6 discipline is satisfied vacuously (nothing new localized).
- **`apply_linop` link target.** `L4/inner_product.md` links the weighted-member gate to
  `../L3/apply_linop.md` (confirmed on disk). There is no `L4/apply_linop` (the opaque
  linear-operator-apply gate is an L3 obstruction; the weighted inner product references it at
  its L3 home). If a future `L4/apply_linop` lands, the link upgrades; for now the L3 target is
  correct and live.
- **SUMMARY.md alpha placement is integrator-mechanical.** I specified the two new L4 chapters
  go in alpha position within the L4 Part per directive-3's active-immediately orchestrator
  carry; the exact insertion point is a `summary-md-surgical-insert` mechanical step for the
  per-report integrator (the L4 Part is not yet by-kind-grouped — that one-time reorg is c069 /
  meta-phase per the plan §Open questions; alpha-within-the-flat-L4-list is the interim rule).
