---
agent: combinator-miner
invoked_at: 2026-06-08T053000Z
scope: Pattern proposal — iterate-while-basis-extension-shared-core
status: integrated
integrated_at: 2026-06-08T165758Z
integration_commit: 292a301
integration_notes: "cycle-139 (batch-45 OPENER, 1/3). Clean NO-COMBINATOR finding (verdict (b)) — NO book mutation; the shared iterate_while_L3-over-basis-extension substrate is already lifted as iterate_while_L3 + correction_step, the 3 carry-shapes diverge, extend_while rejected as identity-in-named-terms. 2 OQs promoted. Applied clean per STAGING.md row 1; no gate hits."
---

# CYCLE: Combinator candidate — iterate-while-basis-extension-shared-core

## Summary

I examined whether the outer-iteration cores of the three named instances — the GMG V-cycle
recursion, the eigsolve-impl thick-restart + basis-extension loop, and the Chebyshev/relaxation
smoother sweep — share a *basis-extension* combinator that could be mined once and propagated
(replace-and-propagate). **The verdict is (b): NO new shared combinator is warranted, because
two distinct levels of structure are already correctly factored and the carry-shapes genuinely
diverge.** Concretely: (1) the *iteration-DRIVER* shape these three share is **already a single
combinator** — `iterate_while_L3` (the firm L4>L3 dissolution of `L4/iterate_while`,
`book/src/L4-L3/iterate-while-dissolution.md:55`), which `ksp_solve`, `eigsolve-impl`, and
`nleps-deflated-eigensolve` all already fold their per-step kernels through, and which the GMG
Richardson sweep specializes as `iterate` (the no-predicate, fixed-count degenerate). Mining a
"shared iteration core" would re-derive a combinator that exists and is consumed. (2) The
*body/carry* shapes are genuinely divergent and are correctly NOT unified: the V-cycle carry is a
**level-stack recursion** (a `vcycle as bs ps b0 l` that recurses on `l-1`, not a flat
predicate-driven fold over a growing set); the eigsolve carry is a **growing orthonormal basis**
`BV : Tensor[(B: ncv), (S: ...), complex]` extended column-by-column with an Arnoldi/Lanczos
recurrence; the Chebyshev carry is a **fixed-degree 3-term recurrence tuple** `(r, d, y, st)`
over a *static* range with no growing working set at all. Only one of the three (eigsolve) is
actually "basis-extension" in the prompt's sense; the V-cycle grows nothing (it recurses down a
fixed level stack) and Chebyshev grows nothing (fixed degree). The prompt's hypothesized
"`iterate_while`-over-basis-extension (an outer iteration that grows/refines a working set each
step)" is **not a shared pattern across these three** — it is a property of *one* of them. This
is a finding about the spine: the shared substrate was already lifted (it is `iterate_while_L3` +
`correction_step`), and what remains per-instance is irreducibly divergent carry structure.

## Pattern instances (and why they do NOT converge to one new combinator)

- **Instance 1 — GMG V-cycle** (`book/src/feature/geometric-multigrid-preconditioner.L1.md:44-62`).
  The driver is two nested non-`iterate_while` shapes: (i) an **outer Richardson sweep**
  `geometric_multigrid ... = iterate pc_it (vcycle ...) x` (`:61-62`) — a *fixed-count*
  `iterate`, the degenerate `iterate_while` with a step-count predicate and no growing set; (ii)
  the **V-cycle itself**, `vcycle as bs ps b0 l x` (`:51-58`), which is **level-stack tail
  recursion** on `l-1`, terminating at the `l==0` coarse solve. The carry is the per-level dof
  vector `x : Tensor[N]`; nothing is *grown* — the level stack `as/bs/ps` is fixed at
  construction. This is structurally a **catamorphism over a fixed level list**, not a basis
  extension. Each V-cycle leg is already factored as the L2 `correction_step` combinator
  (`book/src/feature/geometric-multigrid-preconditioner.L1.md:89-98`,
  `book/src/L2/correction_step.md:36-53`).

- **Instance 2 — eigsolve-impl** (`book/src/L3/eigsolve-impl.md:63-84`). The ONLY genuine
  basis-extension instance. Two nested `iterate_while_L3`: (i) **outer thick-restart driver**
  `iterate_while_L3 st0 (\st -> not (converged st control) && st.cycle < max_restarts) (...)`
  (`:65-71`); (ii) **inner basis-extension loop** `iterate_while_L3 st (\s -> s.j < control.ncv)
  (\s -> ... append_column s step)` (`:78-84`), each step one `krylov-step`/`lanczos_step` that
  *grows* the orthonormal basis `BV : Tensor[(B: ncv), (S: ...), complex]` by one column. This
  is the "grows/refines a working set each step" shape — but it is *already* expressed through
  the firm `iterate_while_L3` driver (`book/src/L3/eigsolve-impl.md:65,78`); the per-step kernel
  is already the firm `krylov-step` (`book/src/L3/krylov-step.md`). The substrate is already
  lifted.

- **Instance 3 — Chebyshev / relaxation sweep** (`book/src/L3/chebyshev.md:225-248`). Two nested
  `iterate_while_pure_L3` tail recursions over **static step-count ranges** (`kloop` over
  `k = 1..order-1` at `:237-244`; `itloop` over `it = 1..pc_it` at `:246-247`). The carry is the
  **fixed-arity 3-term-recurrence tuple** `(r, d, y, st)` (`:234`); there is **no growing working
  set** — the degree `order` is a construction parameter, the recurrence overwrites a
  fixed-size carry each step (`book/src/L3/chebyshev.md:266-289`). This is inner-product-free,
  convergence-test-free, and explicitly "*not* a Krylov method"
  (`book/src/L3/chebyshev.md:35-49`). It shares NOTHING of the basis-extension shape; it shares
  the `correction_step` *body* (it is the `B = p_order(D⁻¹A)` specialization,
  `book/src/L2/correction_step.md:283-289`) and the `iterate_while_pure_L3` *driver shell* — both
  already lifted.

**Convergence check.** The three share exactly two things, and **both are already single firm
combinators**: the driver `iterate_while_L3` / `iterate_while_pure_L3`
(`book/src/L4-L3/iterate-while-dissolution.md:55-98`) and the per-sweep body `correction_step`
(`book/src/L2/correction_step.md`; the V-cycle and Chebyshev are its specializations; eigsolve's
shift-invert step is the explicit over-unification guard at `book/src/L2/correction_step.md:78-81`
that says the Krylov step is NOT a correction_step). What does NOT converge is the carry: a fixed
level stack (catamorphism) vs a growing orthonormal basis (Arnoldi/Lanczos anamorphism) vs a
fixed-degree recurrence tuple (static fold). A combinator unifying these would have to abstract
over "the carry is whatever it is and the recurrence is whatever it is" — which is *precisely*
`iterate_while_L3` and nothing more. There is no intermediate shared structure to mine.

## Proposed combinator

**NONE.** This is the clean no-combinator finding. The "shared iteration core" the prompt
hypothesized is already discharged by two existing firm combinators (`iterate_while_L3` driver +
`correction_step` body), and the residual per-instance structure (level-stack recursion /
basis-column growth / fixed-degree recurrence) is genuinely divergent — no shared combinator
sits between `iterate_while_L3` and the three concrete carries.

### Why not "basis-extension fold" as a new L3 combinator

A candidate one might try: `extend_while :: WorkingSet -> (WorkingSet -> Bool) -> (WorkingSet ->
WorkingSet) -> WorkingSet`, the "grow a working set until done" fold. **Rejected on three
grounds:** (1) it is *definitionally `iterate_while_pure_L3`* with `α = WorkingSet`
(`book/src/L4-L3/iterate-while-dissolution.md:97-98`) — it adds zero structure, the canonical
mine-and-strand degenerate the redirect's replace-and-propagate mandate forbids
(`METHODOLOGY-REDIRECT.md` §combinator-primary; the identity-in-named-terms smell). (2) Only ONE
of the three instances (eigsolve) actually grows a working set; forcing the V-cycle
(level-stack recursion, fixed stack) and Chebyshev (fixed degree, no set) into a
"working-set-growth" frame would be a false unification (the over-unification guard the prompt
explicitly asks me to apply). (3) The eigsolve basis-extension is **already** the firm
`krylov-step` kernel folded by `iterate_while_L3` (`book/src/L3/eigsolve-impl.md:78-84`); the
column-append `append_column s step` is the kernel's job, the fold is `iterate_while_L3`'s — the
same kernel/driver split `correction_step`/`krylov-step` (kernels) vs `iterate_while_L3`
(driver) already establish.

## Proposed changes

No dep-map rough-in row. This dispatch produces a **finding**, not a candidate operator. The
finding is recorded as an Open question (below) so the spine-shape conclusion is durable and a
future miner does not re-open the same hypothesis. No `book/` mutation is proposed.

(Per the role-spec: "a finding about the spine is a legitimate, valuable outcome" — recorded as
an OQ rather than a dep-map row, since there is no combinator to register.)

## Supporting evidence

- `book/src/feature/geometric-multigrid-preconditioner.L1.md:44-62` — the pure V-cycle: level
  recursion `vcycle ... l x = ... vcycle ... (l-1) rc ...` (`:51-58`) + outer `iterate pc_it`
  Richardson sweep (`:61-62`). Carry = per-level `Tensor[N]`; the level stack is fixed.
- `book/src/feature/geometric-multigrid-preconditioner.L1.md:89-98` — each V-cycle leg is the L1
  realization of the L2 `correction_step` combinator (the body already lifted).
- `book/src/L3/eigsolve-impl.md:63-84` — the only genuine basis-extension: outer thick-restart
  `iterate_while_L3` (`:65`) + inner basis-column `iterate_while_L3` (`:78`) over `krylov-step` /
  `lanczos_step`; carry = growing `BV : Tensor[(B: ncv), (S: ...), complex]` (`:56`).
- `book/src/L3/eigsolve-impl.md:78-84` — `append_column s step`: the basis grows one column per
  step; the fold is `iterate_while_L3`, the kernel is `krylov-step` — both already firm.
- `book/src/L3/chebyshev.md:225-248` — the relaxation sweep: two `iterate_while_pure_L3` tail
  recursions over *static* ranges (`kloop` `:237-244`, `itloop` `:246-247`); carry = fixed
  `(r, d, y, st)` tuple (`:234`); no growing set.
- `book/src/L3/chebyshev.md:35-49` — Chebyshev is explicitly NOT a Krylov method,
  inner-product-free, convergence-test-free, static-range loops — structurally disjoint from
  basis-extension.
- `book/src/L4-L3/iterate-while-dissolution.md:55-98` — the firm `iterate_while_L3` /
  `iterate_while_pure_L3` ground forms: the single shared *driver* combinator all three already
  use (directly or as `iterate`/`iterate_while_pure` degenerates).
- `book/src/L2/correction_step.md:36-53,78-81,283-294` — the firm shared *body* combinator: the
  V-cycle and Chebyshev are its `B`-specializations (`:283-294`); the eigsolve Krylov step is the
  explicit over-unification guard kept OUT of it (`:78-81`). Confirms the body-level shared
  substrate is already mined-and-propagated (not stranded).
- `book/src/L3/ksp_solve.md:88,135` — the canonical kernel/driver split: `iterate_while_L3
  (krylov-step op)` — the precedent that the driver is one combinator and the per-step kernel is
  another, which is exactly why no third "shared iteration core" combinator is needed.
- `book/src/L3/nleps-deflated-eigensolve.md:111-120` — a fourth consumer (NEP deflation) also
  folding through `iterate_while_L3`, corroborating that the driver is already the universal
  shared substrate.

## Open questions / caveats

- **[FINDING — record durably] `iterate-while-basis-extension-no-shared-combinator`** — The
  batch-45 shared-iteration-core hypothesis (that GMG vcycle + eigsolve-impl + chebyshev share a
  mineable basis-extension combinator) resolves in the **negative**. The shared substrate is
  already two firm combinators — the `iterate_while_L3` driver
  (`book/src/L4-L3/iterate-while-dissolution.md`) and the `correction_step` body
  (`book/src/L2/correction_step.md`) — and the residual per-instance carry shapes genuinely
  diverge: V-cycle = fixed-level-stack catamorphism (`Tensor[N]` carry); eigsolve = growing
  orthonormal basis anamorphism (`BV : Tensor[(B: ncv), (S: ...), complex]` carry, the only true
  basis-extension); Chebyshev = fixed-degree static 3-term recurrence (`(r,d,y,st)` carry, no
  growing set). A "basis-extension fold" combinator would be identity-in-named-terms to
  `iterate_while_pure_L3` (the forbidden mine-and-strand degenerate) AND would false-unify two
  non-basis-extension instances. Disposition: **no dep-map row, no new chapter.** A future miner
  should NOT re-open this without a *fourth* instance that genuinely grows a working set with a
  carry shape distinct from `BV` (e.g. a ROM/POD basis growth, or an AMR refinement-set growth) —
  and even then the unifier would be `iterate_while_L3`, with the new growth as a `krylov-step`-style
  kernel, not a new driver combinator.

- **Caveat (hard constraint honored).** No V-cycle entry was manufactured (front-1/GMG is firm
  c122; a new node would be a forbidden rectangular pull-up). The V-cycle is cited only as
  existing evidence for the no-convergence finding.

- **Adjacent observation (not in scope this dispatch).** If a future AMR consumer (DIRECTIVE-2
  consumer-(2), `book/src/...` AMR estimate→mark→refine loop) lifts its mark→refine *working-set
  growth* (the Dörfler-marked element set growing the refinement set), THAT would be a genuine
  second basis-extension-shaped instance distinct from eigsolve's `BV` — at which point the
  *kernel* (the marker step) is the new vocabulary and `iterate_while_L3` stays the driver. Flagged
  as a watch-item for the AMR front (already-firm c121/c122 per the dispatch context; re-check if
  AMR's refinement-set growth was rendered as `iterate_while_L3` — if so, this finding is
  corroborated a fifth time; if it was rendered ad-hoc, that is a lift-to-`iterate_while_L3`
  opportunity, NOT a new combinator).
