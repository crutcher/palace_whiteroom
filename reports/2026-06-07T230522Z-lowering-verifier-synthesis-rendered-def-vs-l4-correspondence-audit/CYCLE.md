---
agent: lowering-verifier
invoked_at: 2026-06-07T230522Z
scope: cycle-137 synthesis-rendered-def-vs-l4-correspondence-audit — the c136-rendered Synthesis library defs vs their authoritative L4 chapter bodies
status: pending
integrated_at: 2026-06-07T231500Z
integration_commit: e24d757
integration_notes: |
  cycle-137 (batch-44 position 2/3). AUDIT-CLASS report (directive-sanctioned Synthesis
  rendered-def-vs-L4 correspondence audit; top-level verdict FULLY-SUPPORTED). NO `## Proposed
  changes` to book/ -> NO build relevance. Applied clean by integrator-per-report (STAGING row 2);
  3 OQ promotions only (index-per-library-status-cell-convention, correspondence-audit-coverage-
  coordination-drivers-types-next-pull, l4-krylov-step-cg-solve-worked-example-stale [intake_route:
  meta-phase]). No artifact mutation from this report.
inputs:
  - book/src/synthesis/iteration.md
  - book/src/synthesis/data-algebra.md
  - book/src/synthesis/index.md
  - book/src/L4/iterate-while.md
  - book/src/L4/iterate-while-with-prev.md
  - book/src/L4/krylov-step.md
  - book/src/L4/chebyshev.md
  - book/src/L4/linear_combination.md
  - book/src/L4/inner_product.md
  - book/src/L4/fe_assemble.md
  - book/src/L4/mk_matrix_free_operator.md
  - book/src/L4/sharding-decompose-reduce.md
  - book/src/L2/matrix-free-operator-apply.md
  - book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md
---

# CYCLE: Audit synthesis-rendered-def-vs-l4-correspondence

## Summary

This is the directive-sanctioned Synthesis correspondence audit ("a rendered def's
correspondence to its L4 chapter body is reviewable; `lowering-verifier` may audit it" —
CLAUDE.md §"The SYNTHESIS section"). I audited the c136-rendered Synthesis library defs in
`book/src/synthesis/iteration.md` and `book/src/synthesis/data-algebra.md` against their
authoritative L4 chapter bodies (and, for the DIRECTIVE-3 dual-surface, against the L2
contraction-chain chapter + the kernel-API obstruction node). **Top-level verdict:
FULLY-SUPPORTED — every audited rendered def is a FAITHFUL implementation-VIEW rendering of
its cited L4 chapter body; the synthesized code form = the L4 op; no divergence found.** The
Synthesis Part correctly behaves as an implementation VIEW: it renders the synthesized code
form, links `reference`-class to the authoritative L4 chapters for the laws/semantics, and
restates no law (no semantic-consolidation violation). The DIRECTIVE-3 dual-surface renders
correctly: `fe_assemble`'s `assemble_term` is `#extern` (the kernel-API leaf), while
`mk_matrix_free_operator`'s inline contraction chain renders the kernel-IMPL (the L2 chain
`Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`) — the API/impl correspondence is faithful and the edge classes are
correct. `sharding-decompose-reduce` correctly stays a rank-0 `roadmap_goal` stub note (no
filled def). No proposed changes to the artifact; clean audit disposition.

## Per-citation audit

### iteration.md defs

- **Citation**: `book/src/synthesis/iteration.md:144-159` (`iterate_while` + `iterate_while_pure`)
  vs `book/src/L4/iterate-while.md:28-43` (signatures), `:64-98` (small-step semantics), `:92-98`
  (the `iterate_while_pure` sugar).
  - **Theme claim**: the rendered def is a faithful transcription of the L4 `iterate_while`
    body (Solve-threaded extras-carrying form + the pure sugar).
  - **Found**: the rendered `iterate_while` signature `α -> (α -> Bool) -> (α -> Solve { state: α, ...e }) -> Solve { final_state: α, trajectory: [{ ...e }] }`
    matches L4 §Signature "Solve-threaded, extras-carrying" form (`:38-43`) exactly. The rendered
    body (the `if cont a then do {...} else pure {...}` recursion prepending `[{...e}]` to the
    recursive trajectory) is the prose-and-do-notation rendering of the L4 small-step rule
    (`:64-90`). `iterate_while_pure` renders the strawman sugar `(iterate_while ... (\x -> pure { state: f x })).final_state` matching L4 `:92-98` and the `:156-159` codeblock.
  - **Verdict**: supports.
  - **Notes**: The §1.2.1 named-shape-group congruence note and the demand-pruning Law-1 caveat
    are LINKED (to `../L4/iterate-while.md`), not restated — correct implementation-VIEW
    discipline.

- **Citation**: `book/src/synthesis/iteration.md:178-199` (`iterate_while_with_prev`) vs
  `book/src/L4/iterate-while-with-prev.md:44-50` (signature), `:74-95` (bootstrap-then-steady_loop
  small-step rule), `:52` (the canonical boot/init/steady/cont argument order + carry-first/prev-second).
  - **Theme claim**: faithful transcription of the carry-bootstrapped variant.
  - **Found**: the rendered signature (boot first, a0 second, steady third, cont fourth) matches
    L4 `:44-50` and the canonical-order note `:52`. The rendered body — boot once, then a
    `where`-local `steady_loop a b` tail recursion threading `prev` as a second positional arg —
    is exactly the L4 §Semantics `steady_loop` worker (`:84-95`), with the bootstrap's extras
    prepended (`[{ ...e0 }] ++ trajectory`) per L4 `:79`.
  - **Verdict**: supports.
  - **Notes**: the carry-first/prev-second steady closure order is preserved (`steady (a, b)`),
    matching the L4 canonical convention.

- **Citation**: `book/src/synthesis/iteration.md:220-237` (`krylov_step` Form A) vs
  `book/src/L4/krylov-step.md:94-116` (the Form-A dataflow body).
  - **Theme claim**: faithful render of the Form-A typed-wrapper step kernel body.
  - **Found**: the rendered body reproduces the L4 Form-A five-group dataflow line-for-line — the
    `apply_linop op.T K.<input_field>` operator apply (L4 `:97`), the variant-absorbed optional
    auxiliary stage (L4 `:99-102`, rendered as a comment block + `optionally_apply_auxiliary`),
    the pure `krylov_update` (L4 `:107`), the demand-pruned `derived_views` (L4 `:110`), and the
    sole monadic `modify (\s -> s { it = s.it + 1 })` effect (L4 `:113`), returning
    `{ krylov: K', outputs }` (L4 `:115`). The signature is rendered in the closure-returning
    paren-grouped form `OpParams -> Krylov -> (SimState -> Solve {...})` matching L4 `:63` and the
    §1.3.1 closure-signature convention.
  - **Verdict**: supports.
  - **Notes**: the synthesis result record `{ krylov, outputs }` follows the L4 §Semantics body
    (`:115`) rather than the §Signature narrative record `{ sim, krylov, outputs }` (`:63`) — this
    is FAITHFUL, not a divergence: the L4 chapter itself states (`:79`, `:80`, `:114`) that the
    next SimState is returned through the monadic `modify`, not by structural projection, so the
    body's `pure { krylov, outputs }` is the authoritative dataflow rendering. The synthesis
    code-doc reproduces exactly this caveat ("the next SimState is returned through the monadic
    state transition (modify), not by structural projection").

- **Citation**: `book/src/synthesis/iteration.md:241-299` (`krylov_step` Form B — `CgState`,
  `cg_first_step`, `cg_steady_step`, `cg_solve`) vs `book/src/L4/krylov-step.md:128-199` (the worked
  CG Form B: `CgState<S>` schema `:128-140`, `cg_first_step` `:144-158`, `cg_steady_step` `:160-174`,
  `cg_solve` driver `:178-199`).
  - **Theme claim**: faithful render of the canonical CG Form B instantiation.
  - **Found**: the `CgState` schema (one scalar lighter, `beta_prev` gone) matches L4 `:129-136`.
    `cg_first_step` renders `p' = s.r` / `Ap = apply_linop opA p'` / `alpha = s.beta / dot Ap p'` /
    `x' = axpy alpha p' s.x` / `r' = axpy (negate alpha) Ap s.r` / `beta' = dot r' r'` /
    `res' = sqrt (abs beta')` — line-for-line the L4 `cg_first_step` body (`:147-158`).
    `cg_steady_step` renders the identical body with the `p' = axpby 1.0 s.r (s.beta / beta_prev) s.p`
    direction update (L4 `:164`) and `it: s.it + 1`. The `cg_solve` driver renders the
    convergence pre-check, the first-step short-circuit, and the `iterate_while_with_prev` fold
    threading the prior step's `beta` as the next step's `beta_prev` — matching L4 `:182-199`.
  - **Verdict**: supports.
  - **Notes**: the synthesis renders the `iterate_while_with_prev` call with the bootstrap as an
    explicit closure `(\_ -> pure { state: s1, prev: s0.beta })` and the steady closure returning
    `{ state, prev: s.beta, residual_norm }` — this matches the L4 `:193-197` form modulo the
    Synthesis chapter's own (consistent, faithful) record-return spelling. The numerics, primitive
    sequence, and threading are identical. The synthesis correctly uses the `iterate_while_with_prev`
    arg order it rendered above in the same library (boot/init/steady/cont).

- **Citation**: `book/src/synthesis/iteration.md:305-375` (`chebyshev` — `ChebOp`/`ChebSim`/`Variant`
  types, `setup`, `apply`+`sweep`) vs `book/src/L4/chebyshev.md:67-76` (signatures), `:153-194`
  (the `apply`+`sweep` body), `:229-245` (`setup`).
  - **Theme claim**: faithful render of the constructed-`ChebOp`-closure smoother, the two nested
    `iterate_while_pure` step-count-predicate folds, and the variant-absorbing `setup`.
  - **Found**: the `ChebOp`/`ChebSim`/`Variant` type renders match L4 `:67-76` + `:116`. The
    rendered `setup` reproduces the L4 `:229-245` body exactly — `dinv = recip (extractDiagonal A)`,
    the `spectrumEstimate` Solve sub-action, the `Kind4`/`Kind1` case split with the `sf_min_eff`
    fallback `1.69 / (p.order ** 1.68 + 2.11 * p.order + 1.98)`, `theta`/`delta`, and the
    `scalarInit`/`scalars` closure population. The rendered `apply`+`sweep` reproduces the L4
    `:153-194` body line-for-line: the outer `iterate_while_pure { it: 1 } (\s -> s.it <= op.pc_it) ...`
    sweep fold, the `initial_guess`-degenerate-case residual branch, the `d0 = c0 .* (op.dinv .*. r0)`
    initial direction, the inner `iterate_while_pure { r, d, st, k: 1 } (\c -> c.k <= op.order - 1) ...`
    k-recurrence with `modifyY (\y -> y .+. c.d)` / `r' = c.r .-. ad` / `d' = sd .* c.d .+. sr .* t`,
    and the final `modifyY (\y -> y .+. cN.d)` accumulation.
  - **Verdict**: supports.
  - **Notes**: the `MultTranspose`-trivial-under-symmetry note (synthesis `:375`) matches L4
    `:298-301`. The step-count-predicate (NOT convergence-predicate) distinction is preserved and
    correctly noted in the synthesis intro prose.

### data-algebra.md defs

- **Citation**: `book/src/synthesis/data-algebra.md:56-64` (`linear_combination` + four arity
  leaves) vs `book/src/L4/linear_combination.md:88-89` (the entry-point fold).
  - **Theme claim**: faithful render of the variadic scalar-weighted-tensor-sum fold; the four
    arity leaves rendered as `where`-local specialization aliases.
  - **Found**: the rendered `linear_combination pairs = foldl (\acc (a, t) -> acc + scal a t) (zeros $S) pairs`
    matches L4 `:88-89` exactly. The four arity leaves (`scal`/`axpy`/`axpby`/`axpbypcz`) are
    rendered as `where`-local readout aliases re-expressed THROUGH the combinator at fixed term-list
    length — the correct "accelerated kernels stopped low; the combinator rises" disposition
    (L4 §Context + variant_axes `arity`).
  - **Verdict**: supports.

- **Citation**: `book/src/synthesis/data-algebra.md:82-93` (`inner_product` / `inner_product_M` +
  the conjugation kernel) vs `book/src/L4/inner_product.md:85-91` (the three equations + the
  per-element kernel table).
  - **Theme claim**: faithful render of the reduce-to-scalar inner-product fold; the per-element
    conjugation kernel rendered inline as the unchanged lower artifact.
  - **Found**: the rendered `inner_product x y = reduce (+) zero (zipWith kernel x y)`,
    `inner_product_M x M y = inner_product (apply_linop M x) y`, and `inner_product x y = inner_product_M x I y`
    match L4 `:88-90` exactly. The per-element kernel (`real: x·y`, `complex: conj(x)·y`) is rendered
    inline matching the L4 kernel table (`:106-110`+) and the conjugate-linear-in-arg-1 convention.
  - **Verdict**: supports.

- **Citation**: `book/src/synthesis/data-algebra.md:110-114` (`dot`/`tdot`) and `:131-132` (`nrm2`)
  vs `book/src/L4/dot.md` + `book/src/L4/nrm2.md` (kept named verbs).
  - **Theme claim**: `dot` IS `inner_product` at M=I (Hermitian/symmetric kernel); `tdot` the
    unconjugated co-variant; `nrm2 = √ ∘ abs ∘ inner_product` at the diagonal, a CONSUMER not a
    fold member.
  - **Found**: `dot x y = inner_product x y` / `tdot x y = inner_product x y` (unconjugated kernel)
    and `nrm2 x = sqrt (abs (inner_product x x))` render the kept-verb dispositions. The `abs`
    load-bearing defensive non-negativity guard is preserved and explicitly noted (the do-NOT-merge
    guard for nrm2).
  - **Verdict**: supports.
  - **Notes**: light spot-check (not the dispatch's primary target); the renderings are consistent
    with the data-algebra intro's stated dispositions and the `inner_product` chapter's
    specialization notes.

- **Citation**: `book/src/synthesis/data-algebra.md:153-165` (`mk_matrix_free_operator` + the
  inline `apply_chain`) vs `book/src/L4/mk_matrix_free_operator.md:60-73` (signature + apply-lowering)
  and `book/src/L2/matrix-free-operator-apply.md:70-83` (the five-stage contraction chain).
  - **Theme claim** (the DIRECTIVE-3 kernel-IMPL surface): the constructor builds an operator
    VALUE whose `apply` is the five-stage L2 contraction chain, rendered inline as the unchanged
    lower artifact.
  - **Found**: the rendered signature `FESpace -> WeakFormTerm -> GeomFactors -> Op[Tensor[(N: ...)] → Tensor[(N: ...)]]`
    matches L4 `:60` exactly (the operator-VALUE codomain spelling, §1.3.1). The inline `apply_chain v`
    renders `element_restrict_T (basis_apply_T term (quad_point_contract geom (basis_apply term (element_restrict space v))))`
    — the nested-call rendering of the L2 chain `Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (L2 `:70-83`, L4 `:69-73`).
    The `where`-comment maps G/Gᵀ→`element_restrict`, B_𝒟/B_𝒟ᵀ→`basis_apply`, D→`quad_point_contract`
    against `[E, P, G]` geom — matching the L2 chapter's stage map (`:78-82`).
  - **Verdict**: supports.
  - **Notes**: this is the kernel-IMPL (the from-our-primitives constructive realization). The
    rendered chain is the faithful inline rendering of the firm L2 combinator. The constructor/apply
    split (build the contraction graph once at construction; run per apply) is preserved as the
    GPU-backend-relevant factoring.

- **Citation**: `book/src/synthesis/data-algebra.md:184-194` (`fe_assemble` + `#extern assemble_term`)
  vs `book/src/L4/fe_assemble.md:61-72` (the foldr/sum entry + the opaque leaf) and
  `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` (the kernel-API node).
  - **Theme claim** (the DIRECTIVE-3 kernel-API surface): the assemble-fold `K = Σ_t assemble_term(space, t)`
    is a foldr over a commutative-monoid (operator-+) sum; the per-term leaf `assemble_term` is the
    libCEED-owned opaque kernel, rendered `#extern` after its type signature.
  - **Found**: the rendered `fe_assemble space terms = foldr (\t acc -> assemble_term space t + acc) zero terms`
    matches L4 `:62` exactly, with the map-then-reduce equivalent comment (L4 `:66`). The leaf
    `assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinOp[(N: ...), $N]` is rendered with
    `#extern assemble_term` AFTER its type signature — exactly the §index `#extern NAME` convention
    (`synthesis/index.md:55`). The `#extern` correctly points at the kernel-API node
    (`fe-assemble-libceed-boundary-obstruction.md`, role-label `kernel-api`, status
    `obstruction (opaque-library-ownership)` — confirmed at the node's frontmatter + §Status `:28-30`).
  - **Verdict**: supports.
  - **Notes**: the dual-surface is rendered EXACTLY per DIRECTIVE-3 — the API leaf is `#extern`
    (opaque), the constructive interior (`mk_matrix_free_operator`) renders the impl inline. The two
    Synthesis defs together correctly mirror the kernel-API / kernel-impl distinction.

- **Citation**: `book/src/synthesis/data-algebra.md:456-458` (`sharding-decompose-reduce` stub note)
  vs `book/src/L4/sharding-decompose-reduce.md` (the rank-0 roadmap_goal chapter).
  - **Theme claim**: `sharding-decompose-reduce` stays a rank-0 roadmap_goal — NOT a filled def;
    carried only as a stub note.
  - **Found**: the synthesis renders it as prose ONLY (the intended `subdomain_reduce = mconcat ∘ map (reduce ∘ restrict_to_block) ∘ blocks`
    combinator-pair sketch, with "no implementation is rendered (a roadmap_goal has no firm def to
    synthesize)"). The L4 chapter confirms `rank: roadmap_goal` / `status: roadmap_goal` with
    `reference:`-only edges (no `depends-on`). The MPI/distributed mechanism is cited-not-lifted
    (DIRECTIVE-1).
  - **Verdict**: supports.
  - **Notes**: correct — a roadmap_goal asserts no claims and has no firm def to render; the stub
    note is the faithful Synthesis disposition.

## Applicability conditions

The Synthesis-chapter-KIND obligations (from CLAUDE.md §"The SYNTHESIS section" + `synthesis/index.md`
§"Rendering conventions") each function as an applicability condition on every rendered def:

- **Condition**: Implementation VIEW — renders the synthesized code form; does NOT restate
  laws/semantics (those live ONCE at the L4 chapter / semantic surface / concept page; the def
  LINKS to them).
  - **Verifiable**: yes — each audited def opens with a one-line link to its `../L4/<op>.md`
    chapter and renders only the code body + code-doc; no §Algebraic laws section, no reduction
    rules, no record-field-definition restatement. The laws are pointed to ("Laws … see
    ../L4/<op>.md §Algebraic laws").
  - **Found counter-example?**: no. No semantic-consolidation violation found.

- **Condition**: `reference`-class edges only — no `depends-on` blocking edge, no rank claim.
  - **Verifiable**: yes — `iteration.md` and `data-algebra.md` frontmatter both carry `edges: reference:`
    ONLY (no `depends-on:` key), `kind: navigational-container`, no `rank:`. The synthesis index
    (`:3-7`) states the Part adds no `depends-on` and constrains no rank/liveness.
  - **Found counter-example?**: no. No spurious `depends-on` (the specific defect this audit guards
    against, per the rescope kernel-API/impl correspondence bullet — an impl must NOT depends-on
    the opaque API; here the Synthesis Part never depends-on anything).

- **Condition**: `#extern NAME` after the type signature for opaque-library kernels; the
  from-our-primitives impl rendered inline where firm.
  - **Verifiable**: yes — `fe_assemble`'s `assemble_term` is `#extern` after its sig (the kernel-API
    leaf); `mk_matrix_free_operator`'s `apply_chain` is rendered inline (the kernel-impl). The
    iteration.md §"Kernel boundaries" correctly states it has NO `#extern` of its own (the opaque
    boundary kernels belong to the operators that own those applies — `fe_assemble`/`mk_matrix_free_operator`
    in data-algebra, `eigsolve` in coordination).
  - **Found counter-example?**: no. The `#extern`-vs-inline split exactly tracks the kernel-API /
    kernel-impl distinction.

- **Condition**: deep-linked-unchanged lower artifacts rendered INLINE (not linked-away).
  - **Verifiable**: yes — `mk_matrix_free_operator`'s L2 contraction chain and `inner_product`'s
    per-element conjugation kernel are both rendered inline (they ARE the implementation), matching
    the convention.
  - **Found counter-example?**: no.

- **Condition**: topological def order (a def appears after everything it uses).
  - **Verifiable**: yes — iteration.md orders `iterate_while` → `iterate_while_with_prev` →
    `krylov-step` (consumes both) → `chebyshev` (consumes `iterate_while_pure`). data-algebra.md
    orders the general folds (`linear_combination`/`inner_product`) before the named-verb consumers
    (`dot`/`nrm2`) and the constructor/assemble/reduce consumers. The types cluster immediately
    before their consuming groups.
  - **Found counter-example?**: no.

## Algebraic laws (if cited)

N/A as a primary check — the Synthesis chapter KIND deliberately does NOT state algebraic laws
(they live ONCE at the L4 chapters). The audit's law-relevant check is the converse: that the
rendered code BODY is semantics-preserving w.r.t. the L4 body whose laws are stated elsewhere.
That body-equivalence is the per-citation audit above (all `supports`). Spot-confirmation of the
law-bearing structure each rendered body must preserve:

- **Law (linear_combination concatenation-homomorphism / multilinearity)**: preserved — the
  rendered `foldl (\acc (a,t) -> acc + scal a t) (zeros $S)` is the exact fold the L4 laws are
  stated against; the arity leaves are length-specializations through it (no law-altering shortcut).
- **Law (inner_product conjugate-linear-in-arg-1)**: preserved — the inline kernel conjugates arg-1
  (`conj_if_complex xi * yi`), the convention the Hermitian-symmetry law rests on.
- **Law (fe_assemble commutative-monoid sum / term-position commutativity)**: preserved — the
  rendered `foldr (... + ...) zero` reduces by operator-+, the commutative monoid the homomorphism
  law requires; `assemble_term` is folded opaquely (not cracked open), preserving the law's scope.
- **Law (mk_matrix_free_operator apply linearity / Gᵀ…G symmetry sandwich)**: preserved — the
  rendered five-stage chain is the exact composition the L2 composition-level laws hold of.

## Proposed changes

**None.** Every audited rendered def is a faithful implementation-VIEW rendering of its cited L4
chapter body. The Synthesis Part correctly: (i) renders the synthesized code form, (ii) links
`reference`-class to the authoritative L4/semantics/concept defs for laws/semantics, (iii) restates
no law, (iv) renders the DIRECTIVE-3 dual-surface correctly (kernel-API `#extern` leaf + inline
kernel-impl), (v) keeps `sharding-decompose-reduce` a rank-0 roadmap_goal stub note, (vi) uses
`reference`-class edges only with no spurious `depends-on`. No contradiction was found, so no
`verified_against:` correction block and no edit to any theme/chapter is proposed.

(Optional, non-blocking, NOT proposed as an edit — routed to §Open questions as a navigational
nicety for a future shell author: the Synthesis index lists the per-library chapter `Status` as
`stub (Wave 2)` even though the bodies are now rendered; the chapters' own §Status notes already
flag this — see Open questions.)

## Supporting evidence

- `book/src/synthesis/index.md:48-59` — the rendering conventions every library chapter honors
  (topological order, L4 pseudo-language, `#extern` after sig, inline unchanged artifacts,
  `where` helpers, code-doc, link-don't-re-cite, reference-class-only edges). All confirmed
  satisfied by the audited defs.
- `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` frontmatter + §Status `:28-30` —
  the kernel-API node (`kernel-api` role-label, `obstruction (opaque-library-ownership)`) the
  `#extern assemble_term` points at. Confirms the kernel-API surface the impl realizes.
- `book/src/L2/matrix-free-operator-apply.md:70-83` — the firm five-stage L2 contraction chain
  the synthesis `mk_matrix_free_operator` `apply_chain` renders inline (the kernel-impl).
- L0 anchor spot-checks via `tools/citecheck/citecheck.py --anchor` (the no-drift adjudicator —
  these confirm the L0 substrate the synthesis chain ultimately rests on; the synthesis defs
  themselves carry no L0 citations per the link-don't-re-cite convention):
  - `reference/palace/palace/fem/libceed/operator.cpp:182-189` anchor `Operator::Mult` → `[ok]`
    (anchor at :182 within range) — the L2 chain's whole-operator apply witness.
  - `reference/palace/palace/fem/bilinearform.cpp:77` anchor `AddSubOperator` → `[ok]` — the
    per-term fold-summation `K = Σ_i A(space, term_i)` witness (the `fe_assemble` consumer).
  - `reference/palace/palace/linalg/iterative.cpp:434-441` anchor `beta_prev` → `[ok]`
    (anchor at :440 within range) — the CG Form-B in-step branch the unrolling rotation (rendered
    in the synthesis `cg_first_step`/`cg_steady_step` split) hoists out.

## Open questions / caveats

- **Per-library `Status: stub (Wave 2)` in the Synthesis index vs the rendered bodies (navigational,
  non-blocking).** `book/src/synthesis/index.md:37-39` lists `iteration` / `data-algebra` /
  `coordination` as `stub (Wave 2)`, but the iteration.md / data-algebra.md bodies are now fully
  rendered (c136). Each chapter's own §Status note already flags this ("the shell author /
  integrator may flip the chapter frontmatter `status: stub` → a rendered marker if the project
  tracks per-library rendering completeness; left as `stub` here pending the shell's own
  convention" — data-algebra.md `:462`). This is a per-chapter-status / index-cell consistency
  question for a future `layer-intro-author` shell pass (whether the project tracks per-library
  rendering completeness as a status token), NOT a correspondence defect — the rendered bodies are
  faithful regardless of the cell label. Routed here, not auto-fixed (out of audit scope: the
  Synthesis status convention is the shell author's to set).

- **`coordination.md` (eigsolve `#extern`) and `drivers.md` / `types.md` were NOT in this dispatch's
  audit scope.** The plan scoped the audit to `iteration.md` (vs the four L4 iteration chapters) and
  `data-algebra.md` (vs its L4 chapters + the DIRECTIVE-3 dual-surface). The iteration.md §"Kernel
  boundaries" CLAIMS that `eigsolve`'s `#extern` (the SLEPc EPS loop) renders in `coordination.md`;
  I confirmed the claim's INTERNAL consistency (the index `:38-39` partition assigns `eigsolve` to
  `coordination`), but did NOT audit the `coordination.md` `eigsolve` rendered def against
  `L4/eigsolve.md`. A follow-up `lowering-verifier` dispatch auditing `coordination.md` (the
  `eigsolve` SLEPc-EPS kernel-API/impl dual-surface in particular) and the `drivers.md` /
  `types.md` renderings would complete the Synthesis correspondence-audit coverage. Filed as a
  next-pull audit candidate, not a finding.

- **No directionality / rank-violation / mis-typed-edge issues found.** The Synthesis Part is an
  implementation VIEW (not a lowering theme), so the high→low theme-directionality check is N/A;
  the reference-class-only edge discipline means no rank-violation or mis-typed-`realizes`-edge
  surface exists to flag (the Part adds no blocking edges at all).
