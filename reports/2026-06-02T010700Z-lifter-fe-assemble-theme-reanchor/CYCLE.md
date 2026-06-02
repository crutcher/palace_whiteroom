---
agent: lifter
invoked_at: 2026-06-02T01:14:53Z
scope: L1>L0 theme re-anchor — fe-operator-assemble-mutation-rotation (citation-drift cleanup + LHS re-anchor to firm fe_assemble)
status: integrated
integrated_at: 2026-06-02T034000Z
integration_commit: e9bbbbf9fcee8786ad94305a482f6835d2e0f40b
integration_notes: "D6 cycle-055. Applied clean — 8 surgical re-anchor edits to book/src/L1-L0/fe-operator-assemble-mutation-rotation.md: LHS → firm fe_assemble live link; citation drift :73-75/:93-95 → :77/:97 (AddSubOperator) + :75-76 (the one integ->Assemble site). Theme STAYS rough-in pending the eliminate_* elimination-leg re-anchors (future lifter). No SUMMARY/index/count touched."
inputs:
  - book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
  - book/src/L1/fe_assemble.md
  - reference/palace/palace/fem/bilinearform.cpp:60-113
---

# CYCLE: Re-anchor fe-operator-assemble-mutation-rotation

## Summary

The `fe-operator-assemble-mutation-rotation` L1>L0 theme (a cycle-053 thread-opener) predates the
firm L1 `fe_assemble` operator (landed cycle-054). Two mechanical fixes, no body re-authoring:
(1) the `AddSubOperator` body citations carry a verified **+2 line-drift** — `bilinearform.cpp:73-75`
(domain) and `:93-95` (boundary) point at the `CeedOperator sub_op;` declaration + `integ->Assemble(...)`
call, NOT the `op->AddSubOperator(sub_op)` call the prose describes, which is on-disk at `:77` (domain)
and `:97` (boundary); (2) the LHS framing references the **speculative** `fe_assemble` placeholder,
which is now a firm L1 operator on disk at `book/src/L1/fe_assemble.md` with frontmatter
`lowers_to: L1-L0/fe-operator-assemble-mutation-rotation` — so the theme's `lowers:` frontmatter +
LHS prose should re-anchor to the firm operator via a live link. This is citation hygiene + LHS
re-anchor; the theme's structural decomposition, applicability conditions, and the still-speculative
`eliminate_essential_bc` / `eliminate_rhs` / `weak_form_term` vocabulary are unchanged (the theme
stays `rough-in` — its non-`fe_assemble` speculative operators are not yet harvester-promoted).

All four corrected citations self-verified on disk via `tools/citecheck/citecheck.py --anchor`:
- `bilinearform.cpp:77` anchors `AddSubOperator` (domain branch). ✓
- `bilinearform.cpp:97` anchors `AddSubOperator` (boundary branch). ✓
- `bilinearform.cpp:75-76` anchors `integ->Assemble` (the libCEED-boundary quadrature-kernel site). ✓
- `book/src/L1/fe_assemble.md` exists on disk (live link resolves). ✓

## Proposed changes

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: status: rough-in
lowers: L1/fe_assemble (speculative rough-in)
[new]: status: rough-in
lowers: L1/fe_assemble (firm — landed cycle-054)
```

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: ## Status

`rough-in` (thread-opener). The structural decomposition is recognized and L0-anchored, but the
theme is **not promoted** because (a) the speculative L1 operators it lowers (`fe_assemble`,
`eliminate_essential_bc`, `eliminate_rhs`) are themselves rough-in placeholders awaiting harvester
promotion, (b) the libCEED matrix-materialization step crosses an **upstream library boundary**
[new]: ## Status

`rough-in` (thread-opener). The structural decomposition is recognized and L0-anchored, but the
theme is **not promoted** because (a) its LHS operator [`fe_assemble`](../L1/fe_assemble.md) is now
**firm** (landed cycle-054), but the remaining speculative L1 operators it lowers
(`eliminate_essential_bc`, `eliminate_rhs`) are still rough-in placeholders awaiting harvester
promotion, (b) the libCEED matrix-materialization step crosses an **upstream library boundary**
```

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: The pure-functional FE-assembly form consumes a finite-element space and an **immutable list of
weak-form terms** (each term a `(coefficient, differential-operator)` pair naming a bilinear
weak-form contribution `a_i(u, v)`), and produces a fresh global linear operator. Nothing is
mutated; there is no container built up in place, no sub-operator accumulator, no finalize step.
[new]: The LHS is the now-firm L1 operator [`fe_assemble`](../L1/fe_assemble.md) (landed cycle-054). It
consumes a finite-element space and an **immutable list of weak-form terms** (each term a
`(coefficient, differential-operator)` pair naming a bilinear weak-form contribution `a_i(u, v)`),
and produces a fresh global linear operator. Nothing is mutated; there is no container built up in
place, no sub-operator accumulator, no finalize step.
```

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: These three pieces — `fe_assemble`, `eliminate_essential_bc`, `eliminate_rhs` — are the speculative
L1 vocabulary this thread proposes. They are **rough-in placeholders**; signatures are best-guess.
[new]: Of these three pieces, [`fe_assemble`](../L1/fe_assemble.md) is now **firm** (landed cycle-054; its
signature is authoritative there). `eliminate_essential_bc` and `eliminate_rhs` remain **rough-in
placeholders** this thread proposes; their signatures are best-guess pending harvester promotion.
```

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]:    `integ->Assemble(...)` to build a libCEED sub-operator and `op->AddSubOperator(sub_op)` to
   accumulate it into the composite operator (`palace/fem/bilinearform.cpp:73-75` domain branch;
   `:93-95` boundary branch), then `op->Finalize()` (`:104`). `FullAssemble`
[new]:    `integ->Assemble(...)` to build a libCEED sub-operator and `op->AddSubOperator(sub_op)` to
   accumulate it into the composite operator (`palace/fem/bilinearform.cpp:77` domain branch;
   `:97` boundary branch), then `op->Finalize()` (`:104`). `FullAssemble`
```

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: `palace/fem/bilinearform.cpp:73-75`) bottom out in libCEED basis-apply + restriction operations.
[new]: `palace/fem/bilinearform.cpp:75-76`) bottom out in libCEED basis-apply + restriction operations.
```

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: - `palace/fem/bilinearform.cpp:28-107` — `PartialAssemble`: the integrator-fold core
  (`AddSubOperator` accumulation at `:73-75` domain / `:93-95` boundary; `Finalize` at `:104`).
[new]: - `palace/fem/bilinearform.cpp:28-107` — `PartialAssemble`: the integrator-fold core
  (`AddSubOperator` accumulation at `:77` domain / `:97` boundary; `Finalize` at `:104`).
```

```edit:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
[old]: ## Speculative L1 operators (need harvester promotion)

- `fe_assemble` — assemble a global FE operator from a space + immutable weak-form term list.
- `eliminate_essential_bc` — pin essential (Dirichlet) dofs into the assembled operator.
[new]: ## Speculative L1 operators (need harvester promotion)

- ~~`fe_assemble`~~ — **PROMOTED firm cycle-054**, see [`L1/fe_assemble`](../L1/fe_assemble.md).
- `eliminate_essential_bc` — pin essential (Dirichlet) dofs into the assembled operator.
```

## Discipline notes

This is a structural re-anchor + citation-hygiene pass, not authoring. Three classes of change:

1. **+2 line-drift correction on the `AddSubOperator` body citations** (the cycle-054 D2 deferral).
   The theme's `:73-75` (domain) / `:93-95` (boundary) ranges point at the `CeedOperator sub_op;`
   declaration through the `integ->Assemble(...)` call; the prose at each site describes
   `op->AddSubOperator(sub_op)`, which is on-disk at `:77` (domain) / `:97` (boundary). Three theme
   sites carried the drift — the §"L0 form" step-3 prose (~theme-lines 84-85), the §"Verified-against"
   `PartialAssemble` row (~line 162), and (a related-but-distinct case) the §"libCEED boundary" prose
   (~line 134). Corrected to single-line pinpoints `:77` / `:97`. Verified via
   `citecheck.py palace/fem/bilinearform.cpp:77 --anchor 'AddSubOperator'` (ok) and `:97` (ok).

2. **Bounded prose-correction on the §"libCEED boundary" citation** (line 134). That citation's prose
   describes `integ->Assemble(...)` — "the per-integrator `integ->Assemble(...)` that builds each
   `CeedOperator` sub-operator" — NOT `AddSubOperator`. So unlike the other two sites it does NOT
   re-anchor to `:77`; its actual referent `integ->Assemble(...)` is on-disk at `:75-76`. Re-anchored
   to `:75-76` (verified via `citecheck.py palace/fem/bilinearform.cpp:75-76 --anchor 'integ->Assemble'`,
   ok). This is a bounded, L0-evidenced, here-recorded prose-correction (per the lifter
   `lifter-scope-content-correction-boundary` discipline): the citation had drifted off the construct
   its own prose names; the fix points it at the construct, no decomposition change.

3. **LHS re-anchor to firm `fe_assemble`** (the cycle-054 promotion). The theme predates the firm L1
   operator; its `lowers:` frontmatter, §Status, §"L1 form (LHS)", §"L1 form" closing prose, and
   §"Speculative L1 operators" list all framed `fe_assemble` as a speculative rough-in placeholder.
   `book/src/L1/fe_assemble.md` is now firm on disk (frontmatter `firmness: firm`,
   `lowers_to: L1-L0/fe-operator-assemble-mutation-rotation` — the theme IS its canonical lowering).
   Re-pointed the LHS framing at the firm operator via live links `../L1/fe_assemble.md`. The theme
   itself **stays `rough-in`**: its OTHER speculative operators (`eliminate_essential_bc`,
   `eliminate_rhs`, `weak_form_term`) are not yet promoted, and the libCEED-boundary classification
   is still open — so a full theme `firm` flip is NOT warranted by this pass (only one of three
   speculative operators firmed). The §Status promotion-route prose was updated to reflect that
   `fe_assemble`'s leg of the route is now satisfied.

**High→low discipline honored**: all edits keep the theme's LHS = L1, RHS = L0, prose narrating the
rewrite forward (L1 `fe_assemble` into L0 build-up-then-assemble). No inversion. The firm
`fe_assemble` entry already carries the upward (L0→L1 lift) notes in its own §Context; nothing about
the reverse direction is introduced into this theme.

**Slug-collision preserved**: the firm `fe_assemble` entry carries a load-bearing slug-collision
warning (`fe_assemble` the assembly-constructor vs. `bilinear-form` the scalar reduction `xᴴMy`).
All re-anchored live links point at `../L1/fe_assemble.md`, never at `bilinear-form` — collision honored.

## Supporting evidence

- `reference/palace/palace/fem/bilinearform.cpp:60-107` — `PartialAssemble` body read on-disk;
  confirms `op->AddSubOperator(sub_op)` at `:77` (domain, inside `for (const auto &integ : domain_integs)`)
  and `:97` (boundary, inside `for (... boundary_integs)`); `integ->Assemble(...)` at `:75-76` and
  `:95-96`; `op->Finalize()` at `:104`.
- `book/src/L1/fe_assemble.md:1-55` — firm L1 operator (frontmatter `firmness: firm`,
  `lowers_to: L1-L0/fe-operator-assemble-mutation-rotation`); its §Context cites the `AddSubOperator`
  accumulation as `bilinearform.cpp:71-77 domain / :91-97 boundary` (range form spanning the `for`
  body, consistent with the corrected pinpoints).
- `tools/citecheck/citecheck.py` `--anchor` runs (all ok): `:77`/`AddSubOperator`, `:97`/`AddSubOperator`,
  `:75-76`/`integ->Assemble`.

## Open questions / caveats

- **`fe_assemble`'s firm §Context uses RANGE citations `:71-77` / `:91-97`** for the `AddSubOperator`
  accumulation (spanning the whole `for`-body), whereas this theme now uses PINPOINTS `:77` / `:97`
  (the `AddSubOperator` call line itself). Both are correct — the range names the per-term fold-body,
  the pinpoint names the accumulation call. Not a contradiction; flagged so a future lowering-verifier
  cross-checking the two entries doesn't read the differing forms as drift. If a uniform convention is
  desired, the pinpoint is the more precise anchor for the prose "`AddSubOperator` accumulation".
- **Theme stays `rough-in`, not promoted to `firm`.** Only `fe_assemble` (1 of 3 speculative
  operators) is firmed. Promoting the theme to `firm` requires (a) `eliminate_essential_bc` +
  `eliminate_rhs` harvester-promoted, AND (b) the libCEED-boundary classification settled
  (transitive-firm leaf vs. `obstruction (opaque-library-ownership)` vs. spine-primitive re-expression
  — still the thread's central open decision, logged in §"libCEED boundary"). This pass does NOT
  attempt that flip; it only re-anchors the one firmed leg. A future lifter/abstractor pass flips the
  theme once the other two operators land and the libCEED boundary is classified.
- No abstractor reread is needed — the firm `fe_assemble` signature
  (`(space: FiniteElementSpace[N], terms: [WeakFormTerm]) -> LinearOperator[N, N]`) matches the
  theme's LHS sketch `K = fe_assemble(space, [term_0, ...])` exactly; the firmed signature did NOT
  contradict the theme's assumption, so this remained a pure re-anchor.
