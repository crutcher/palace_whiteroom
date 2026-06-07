---
agent: combinator-miner
invoked_at: 2026-06-07T064500Z
scope: Pattern proposal — preconditioned residual-correction step (the shared smoother/V-cycle/relaxation substrate across the c121 kernel-impl wide wave)
status: pending
inputs:
  - reports/2026-06-07T054924Z-cycle-planner-cycle-121/CYCLE.md (D6 scope)
  - reports/2026-06-07T054924Z-harvester-multigrid-relaxation-smoother/CYCLE.md (D3)
  - reports/2026-06-07T054924Z-abstractor-libceed-quadrature-kernel-impl/CYCLE.md (D4)
  - reports/2026-06-07T054924Z-abstractor-eigsolve-kernel-impl/CYCLE.md (D5)
  - reports/2026-06-07T054924Z-layer-intro-author-geometric-multigrid-preconditioner/CYCLE.md (D1)
  - book/src/L1/chebyshev-smoother.md, book/src/L1/jacobi-smoother.md (existing smoother bodies)
  - book/src/L3/smoother-intro.md, book/src/L4/iteration-combinators-intro.md, book/src/L4/iterate-while.md (existing cohort framing + iteration vocab)
  - palace/linalg/distrelaxation.cpp:101-119, palace/linalg/gmg.cpp:172-205 (Palace's own `Y <- Y + B(X - A Y)` comments)
integrated_at: 2026-06-07T054924Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean. L2/correction_step rough-in dep-map row; replace-and-propagate routed to harvester."
---

# CYCLE: Combinator candidate — preconditioned residual-correction step

## Summary

Probing the four kernel-impl reports of the c121 wide wave (D1 GMG V-cycle, D3
relaxation smoother, D4 libCEED contraction, D5 eigsolve Krylov) for the ONE
shared substrate worth lifting once, I find that **the iteration-loop axis is
already mined** — `iterate_while` / `iterate-while-with-prev` are firm L4
combinators whose own entry states they subsume CG / GMRES / Chebyshev / Arnoldi
/ eigenmode / time-stepping. The genuinely **un-mined** recurrent core is one
layer down: the **preconditioned residual-correction step**

    correct(A, B, x, y) = y + B·(x − A·y)

— form the residual `r = x − A·y`, apply a correction operator `B` to it, add
the correction back to the iterate. This is the **per-sweep body** of *every*
stationary/relaxation/multigrid smoother. It is currently **re-derived
independently** in `chebyshev-smoother` (`y + p_order(D⁻¹A)·(x − A·y)`),
`jacobi-smoother`'s Richardson form, the D3 `multigrid-relaxation-smoother`
primary leg, AND the D1 GMG V-cycle pre/post-smooth + coarse-grid correction —
Palace itself names the contract twice, verbatim, in source comments
(`gmg.cpp:174-176` "given X, Y, compute `Y <- Y + B (X - A Y)`";
`distrelaxation.cpp:104` "`y = y + B (x - A y)`"). I propose **`correction_step`**
(working slug `residual-correction-step`) as an **L2 combinator parameterized by
the correction operator `B`**, with the smoothers as specialization notes that
choose `B` — replace-and-propagate, not a new same-named floor. Its auxiliary /
inter-level **conjugated** form `y + T·B'·Tᵀ·(x − A·y)` (transfer `T = G` de-Rham
gradient in D3, `T = P` prolongation in D1) unifies the distributive-relaxation
auxiliary leg and the multigrid coarse-grid correction as ONE law.

## Pattern instances

The fixed-arity shape `y ← y + B·(x − A·y)` (and its conjugated lift
`y ← y + T·B'·Tᵀ·(x − A·y)`) recurs across all three substrate fronts the wide
wave was designed to amortize:

- **Instance 1 — `chebyshev-smoother` (L1, firm).** Signature body stated
  verbatim: `chebyshev_smoother(op, x, y, ig) = y + p_order(D⁻¹A)·(x − A·y)`
  repeated `pc_it` times (`book/src/L1/chebyshev-smoother.md:50-52`). The
  correction operator is `B = p_order(D⁻¹A)` (the degree-`order` Chebyshev
  polynomial). L0: `palace/linalg/chebyshev.cpp:190-220`.
- **Instance 2 — `jacobi-smoother` Richardson form (L1, firm).** The chapter
  states the consumer-side Richardson sweep `y ← y + M·(x − A·y)` with
  `M = ω·D⁻¹` (`book/src/L1/jacobi-smoother.md:264`). NOTE the over-unification
  guard below: the *bare* Jacobi apply `Y = M·X` is the correction **operator**
  `B`, not the step; the step is the Richardson form its consumers build around
  it.
- **Instance 3 — `multigrid-relaxation-smoother` primary leg (D3 kernel-impl,
  firm c121).** `y := y + B·(x − A·y)` — the primary-space relaxation leg,
  source-commented identically (`palace/linalg/distrelaxation.cpp:104`,
  `// y = y + B (x - A y)`). D3 §Signature lines it up as the first per-sweep
  leg (report lines 150-153, 176-187).
- **Instance 4 — `multigrid-relaxation-smoother` auxiliary leg (D3, firm c121),
  the CONJUGATED form.** `y := y + G·B_G·Gᵀ·(x − A·y)` — same residual `x − A·y`,
  correction lifted through the de-Rham discrete gradient `G`
  (`palace/linalg/distrelaxation.cpp:108-117`, comment
  `// y = y + G B_G Gᵀ (x - A y)`). This is `correct` with `B = G·B_G·Gᵀ` (a
  transfer-conjugated correction operator).
- **Instance 5 — GMG V-cycle pre/post-smooth (D1 column, rough-in c121).**
  Palace's own V-cycle comment: "the smoothers must respect the initial guess
  flag correctly (given X, Y, compute `Y <- Y + B (X - A Y)`)"
  (`palace/linalg/gmg.cpp:174-176`); pre-smooth `B[l]->Mult2(X,Y,R)` (`:184`),
  residual `A[l]->Mult(Y,R); AXPBY(1,X,-1,R)` (`:187-188`).
- **Instance 6 — GMG coarse-grid correction (D1 column, rough-in c121), the
  inter-level CONJUGATED form.** residual `R ← X − A·Y` → restrict
  `X[l-1] = Pᵀ·R` (`gmg.cpp:191`) → coarse solve `E` → prolong-add
  `Y += P·E` (`gmg.cpp:199-200`). This is `correct` with the correction operator
  `B = P·(coarse-solve)·Pᵀ` — the SAME transfer-conjugated shape as Instance 4
  with `T = P` (prolongation) replacing `T = G` (gradient). The de-Rham
  auxiliary-space correction and the multigrid coarse-space correction are the
  ONE conjugated-correction pattern.

(Eigsolve / D5 is the over-unification guard, not an instance — see below.)

≥3 same-shape instances (1, 3, 5) plus a clean **conjugation law** unifying the
auxiliary/coarse legs (4, 6) under the same combinator — well above the soft bar.
Palace naming the contract verbatim in two independent source files is the
strongest possible "this is one pattern" evidence.

## Proposed combinator

- **Slug**: `residual-correction-step` (operator name `correction_step`)
- **Layer**: **L2** — with rationale below.
- **Signature sketch** (best guess; harvester firms):

  ```text
  -- the base preconditioned residual-correction step, parameterized by the
  -- correction operator B (a LinOp[(S: ...), $S] supplied by the caller)
  correction_step
    :: (A: LinOp[(S: ...), $S], B: LinOp[(S: ...), $S], x: Tensor[(S: ...)], y: Tensor[(S: ...)])
       -> Tensor[(S: ...)]
  correction_step A B x y = axpby 1 y 1 (apply_linop B (axpby 1 x (-1) (apply_linop A y)))
                          -- = y + B·(x − A·y)

  -- the transfer-conjugated form: the correction acts in a transferred space
  -- reached by Tᵀ and lifted back by T (de-Rham gradient G, or prolongation P)
  conjugated_correction_step
    :: (A, T: LinOp[(S: ...), (U: ...)], B': LinOp[(U: ...), $U], x, y) -> Tensor[(S: ...)]
  conjugated_correction_step A T B' x y =
    axpby 1 y 1 (apply_linop T (apply_linop B' (apply_transpose T (axpby 1 x (-1) (apply_linop A y)))))
                          -- = y + T·B'·Tᵀ·(x − A·y)   [B = T·B'·Tᵀ]
  ```

  Both compose only firm L2/L1 base primitives (`apply_linop`, `axpby`); the
  correction operator `B` / `B'` is a parameter, not unfolded — that is the point
  of the combinator (it is the slot the smoother specializations fill).

- **Algebraic intuition**:
  - **Affine-in-`x`, affine-in-`y`.** `correct(A,B,·,y)` is affine in `x`
    (`B·x` + const); `correct(A,B,x,·)` is the affine map
    `y ↦ (I − B·A)·y + B·x`. The **error-propagation operator** is `E = I − B·A`
    (the contraction the smoother's convergence rests on) — a derived view the
    combinator makes structural.
  - **Fixed point.** `correct(A,B,x,y) = y ⟺ B·(x − A·y) = 0`; if `B` is
    invertible this is exactly `A·y = x` (the linear system). The smoother's
    "zero-residual fixed point" law (D3 law 3, `chebyshev-smoother`) is the
    combinator's fixed-point law, stated ONCE.
  - **Conjugation law (the unifier).** `conjugated_correction_step A T B' x y =
    correction_step A (T·B'·Tᵀ) x y` — the transferred form IS the base form
    with a conjugated correction operator. This is the single law that collapses
    the D3 auxiliary leg (`T = G`) and the D1 coarse-grid correction (`T = P`)
    into the base combinator. (`Tᵀ A T` is the Galerkin/RAP-conjugated operator
    in the transferred space — exactly `A_G = GᵀAG` in D3 and the coarse operator
    in D1.)
  - **Identity element.** `B = 0` ⇒ `correct = y` (no-op); `B = A⁻¹` ⇒
    `correct = A⁻¹·x` (exact solve in one step). The smoother spectrum
    (Jacobi → Chebyshev → exact) is `B` ranging from cheap-diagonal to full
    inverse.
  - **Iteration is NOT folded here.** The `pc_it`-sweep / V-cycle recursion is
    the *consumer's* `iterate_while` fold over this step body (the already-firm
    L4 combinator). `correction_step` is deliberately the SINGLE step — the
    sequential-obstruction lives in the loop, not the step (D3 NL1).

- **Variant axes**:
  - **correction-operator class** (the `B` slot): `D⁻¹` (Jacobi) /
    `p_order(D⁻¹A)` (Chebyshev) / `T·B'·Tᵀ` (distributive / multigrid). This is
    the specialization axis — each smoother is a choice of `B`, not a new step.
  - **plain vs transfer-conjugated** (`correction_step` vs
    `conjugated_correction_step`) — unified by the conjugation law; the
    conjugated form degenerates to plain when `T = I`.
  - **initial-guess fast path** (`ig = false`): the leading `A·y` matvec is
    skipped (`y` taken as 0). A degenerate-case absorption, not an algebraic
    variant (shared verbatim across D3, `chebyshev-smoother`, GMG pre-smooth).

## Layer rationale (L2, not L1 / L3)

- **Not L1**: at L1 the smoothers are *constructed-operator gates* whose `B` is
  an opaque closure (`chebyshev-smoother`, `jacobi-smoother`); the L1 entries
  legitimately keep their closure-carried `B`. The combinator's value is in the
  **fusion-rotation layer** where the smoother body is *unfolded into base
  algebra* (`apply_linop` + `axpby` + the `B` slot) — that is exactly L2's job
  (CLAUDE.md §Extraction-goal "L2 — fusion rotation … unfolded back into
  composition of base algebraic primitives"). L2 already hosts `jacobi-smoother`,
  `chebyshev-iteration`, `axpby`.
- **Not L3**: L3 is iteration-rotation; the *sweep* (the `pc_it` fold / V-cycle
  recursion) is the L3/L4 concern (already `iterate_while`). The single step is
  iteration-free — putting it at L3 would conflate the step with its loop.
- So: **L2 combinator `correction_step`**, consumed by the L2 smoother
  unfoldings and (via lowering) by the L1 smoother gates; the L4 V-cycle / sweep
  composes `iterate_while` over it.

## Over-unification guard (what must NOT be subsumed)

- **The bare correction operator `B` is NOT the step.** `jacobi-smoother`'s
  *apply* is `Y = M·X` (one elementwise product, `book/src/L1/jacobi-smoother.md:118-143`,
  source-asserts `!initial_guess` at `palace/linalg/jacobi.cpp:102`) — it is the
  `B` that plugs INTO `correction_step`, not an instance of it. Subsuming the
  bare diagonal apply into the step would wrongly attribute a residual matvec to
  Jacobi that it explicitly avoids. The step's `B` slot is filled BY these
  operators; they are its arguments, not its specializations-as-steps. (This is
  the cleanest possible specialization/argument boundary.)
- **D5 eigsolve / Krylov shift-invert is a DIFFERENT step — do NOT subsume.**
  The basis-extension body `w = apply_linop op.operand v ▷ ksp_solve op.inv w`
  (D5 report lines 118-124) is `(K−σM)⁻¹·M·v` — an **operator-product applied to
  a basis vector**, NOT a residual-correction update of an iterate. There is no
  `x − A·y` residual and no `y + …` accumulation; the result is a new basis
  column, not a corrected solution. It folds into `iterate_while` (basis
  extension), not `correction_step`. D5's own shared-substrate note (report
  line 328) correctly identifies its shared core as the `iterate_while_L3` loop
  (already mined) + `orthogonalize` — NOT the residual-correction step. Keeping
  these separate is the same discipline cycle-017/018 used keeping `dot` out of
  `linear_combination`.
- **D4 libCEED contraction is a DIFFERENT substrate — do NOT subsume.** The
  `Gᵀ Bᵀ D B G` element-quadrature pipeline (D4) is operator *assembly /
  application* (building/applying `A`), one layer beneath the residual-correction
  step (which *consumes* an assembled `A`). D4's shared core is the
  tensor-contraction substrate (`element_restrict`/`basis_apply`/…), a separate
  mining target (D4 report lines 219-230). `correction_step` is `A`-agnostic; how
  `A·y` is computed (matrix-free contraction or assembled matvec) is `apply_linop`'s
  concern, below this combinator. The naming collision is only that D4's
  restriction operator is also written `G` — a different `G` from D3's de-Rham
  gradient.

## Proposed changes

```edit:book/src/L2/index.md
| `correction_step` *(rough-in; no anchor yet)* | `(A: LinOp[(S: ...), $S], B: LinOp[(S: ...), $S], x: Tensor[(S: ...)], y: Tensor[(S: ...)]) → Tensor[(S: ...)]` (i.e. the preconditioned residual-correction step `y + B·(x − A·y)`; the conjugated form `y + T·B'·Tᵀ·(x − A·y)` unifies the de-Rham auxiliary leg `T=G` and the multigrid coarse-grid correction `T=P`) | `apply_linop`, `axpby` (the residual `x − A·y` + the `y + correction` add); `B` is a parameter slot filled by the smoother specializations (`jacobi-smoother` `B=ω·D⁻¹`, `chebyshev-iteration` `B=p_order(D⁻¹A)`, distributive `B=G·B_G·Gᵀ`) | `rough-in` (**combinator; replace-and-propagate**, proposed-by: combinator-miner:2026-06-07T054924Z-combinator-miner-kernel-shared-substrate; the shared per-sweep body Palace names verbatim at `gmg.cpp:174-176` + `distrelaxation.cpp:104`; the smoother bodies become specialization notes choosing `B`, NOT same-named floors; the `pc_it`/V-cycle sweep stays the consumer's `iterate_while` fold, NOT folded here; over-unification guard: the bare `B` apply / the D5 Krylov shift-invert step / the D4 contraction substrate are explicitly OUT) |
```

Note: this report does **not** create `book/src/L2/residual-correction-step.md`.
That is the harvester's formalization pass. This report only adds the dep-map
rough-in row (plain-text/inline-code slug per the forward-reference convention —
the chapter does not yet exist, so the cell is NOT a live link).

## Supporting evidence

- **Palace names the contract verbatim** — `palace/linalg/gmg.cpp:174-176`
  ("given X, Y, compute `Y <- Y + B (X - A Y)`") + `:184-188` (the realized
  pre-smooth + residual); `palace/linalg/distrelaxation.cpp:104`
  (`// y = y + B (x - A y)`) + `:108-117` (the conjugated auxiliary leg
  `// y = y + G B_G Gᵀ (x - A y)`). Both read on-disk this dispatch via
  codemap `read_range`.
- **Existing L1 smoother bodies re-deriving the shape** —
  `book/src/L1/chebyshev-smoother.md:50-52` (`y + p_order(D⁻¹A)·(x − A·y)`);
  `book/src/L1/jacobi-smoother.md:264` (`y ← y + M·(x − A·y)` Richardson form),
  `:118-143` (the bare-apply over-unification guard).
- **The conjugated coarse-grid correction** — `palace/linalg/gmg.cpp:188-200`
  (residual → `Pᵀ` restrict → coarse solve → `P` prolong-add); the de-Rham
  analog `palace/linalg/distrelaxation.cpp:108-117` (`Gᵀ` restrict → `B_G` →
  `G` prolong-add). Same shape, `T = P` vs `T = G`.
- **Iteration axis already mined (why NOT the loop)** —
  `book/src/L4/iterate-while.md:6-7,211` (firm; "every iterative algorithm in
  the spec … reduces at L4 to one or more `iterate_while`-folds");
  `book/src/L4/iteration-combinators-intro.md` (the firm
  `iterate-while`/`iterate-while-with-prev`/`krylov-step`/`chebyshev` family).
- **Existing cohort framing that does NOT extract this step** —
  `book/src/L3/smoother-intro.md` (groups jacobi/divfree/chebyshev by
  *obstruction profile*, not by the shared residual-correction body — the gap
  this combinator fills).
- **Wide-wave shared-substrate handoffs pointing here** — D5 report line 328
  (flags the `iterate_while_L3`-over-basis-extension shape, correctly NOT the
  residual step); D1 report lines 486-491 (flags the V-cycle level-recursion as
  a combinator candidate — its per-level body IS this step); D3 report
  §Algebraic-laws 1-3 (the single-sweep decomposition, fixed-point, and
  residual-linearity laws that become THIS combinator's laws).

## Open questions / caveats

- **Replace-and-propagate scope (for harvester + same-layer-cross-cutter).**
  The intended refactor: `correction_step` becomes the L2 entry; the L2
  `jacobi-smoother` and `chebyshev-iteration` bodies are re-expressed as
  `correction_step` with their specific `B` (specialization notes under it), and
  the D3 `multigrid-relaxation-smoother` L1>L0 lowering / the D1 V-cycle L1
  surface express their per-sweep bodies THROUGH `correction_step` (or its L1
  analog) rather than re-deriving `y + B(x−A·y)`. Whether the L1 smoother
  *gates* (closure-carried `B`) also re-express through it, or keep their opaque
  form and only the L2 unfoldings use the combinator, is a layer-placement
  refinement for the harvester (my read: L1 gates keep the closure; L2
  unfoldings + the V-cycle body use the combinator). Flagged for
  same-layer-cross-cutter to confirm the propagation set.
- **Conjugated form: one combinator with `T=I` default, or two?** I sketched
  `correction_step` + `conjugated_correction_step` with a conjugation law tying
  them. The cleaner design may be a single `correction_step` whose `B` is *any*
  LinOp (the conjugated `T·B'·Tᵀ` is just one such `B`), with the
  conjugation/Galerkin structure a *note* rather than a second operator. The
  argument for two: the transferred-space `B'` + transfer `T` is the form the
  distributive smoother and multigrid actually carry (the conjugation is not
  pre-formed). Harvester to decide; both are stated for the multi-formulation
  explore-and-coalesce discipline.
- **`assemble-diagonal` / `reciprocal` relation (RE5/RE7).** The Jacobi/Chebyshev
  `B` is built from `dinv = reciprocal(assemble_diagonal A)` (`chebyshev.cpp:177-178`,
  the D1 RE5/RE7 grounding site). That construction is the *building of `B`*, a
  setup-stratum step distinct from `correction_step`'s run-time apply — should
  NOT be folded into the step combinator. Noted to keep the construction/apply
  strata separate.
- **Does the divfree-projector belong?** `divfree-projector`'s
  `I − Grad(GᵀMG)⁻¹GᵀM` is a residual-*projection* (`x − correction`), the same
  conjugated shape with `A = M`, `T = Grad`, `B' = (GᵀMG)⁻¹`, but it is an exact
  auxiliary *solve* and a one-shot projector (not an iterate-update). It is a
  borderline 7th instance — likely a specialization-note ("exact-solve
  conjugated correction, used as a projector") rather than a core instance.
  Flagged for the harvester / same-layer-cross-cutter; I did not count it toward
  the bar (instances 1-6 clear it).
- **No book/ write performed.** Per the dispatch-phase write-authority partition,
  this report emits only the proposed-changes dep-map rough-in row;
  integrator-per-report applies it in Phase 5.
