---
agent: cross-layer-cross-cutter
invoked_at: 2026-05-29T023000Z
scope: L1↔L0 cross-cut — divfree.hpp Mult doc-comment irrotational-vs-divergence-free tension (carry-forward OQ divfree-mult-doc-irrotational-vs-divfree-stale)
status: integrated
integrated_at: 2026-05-29T08:10:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-019 finalize. OPTIONAL cross-link prose-sharpening of divfree-projector-mutation-rotation.md §Open-questions stale-Mult-doc bullet (:460-468): class doc :28-31 named authoritative L0 site + :155-190 impl + divfree.cpp:176 third witness folded in; Helmholtz/Hodge framing. ZERO semantics change — divfree firm unchanged. OQ divfree-mult-doc-irrotational-vs-divfree-stale recorded RESOLVED/closure-ready (meta-phase enacts close + priorities.md flip). retroactive-budget 0; clean build."
---

# CYCLE: Cross-layer observation — divfree.hpp Mult doc-comment irrotational-vs-divergence-free tension

## Summary

The carry-forward OQ `divfree-mult-doc-irrotational-vs-divfree-stale` flags a
contradiction inside Palace's own `divfree.hpp`: the per-method doc comment on
`DivFreeSolver::Mult` (`palace/linalg/divfree.hpp:64-66`) says the output is
"the **irrotational** portion ... satisfying **∇ × y = 0**", while the class
doc comment (`palace/linalg/divfree.hpp:28-31`), the implementation
(`palace/linalg/divfree.cpp:155-190`), and both firm artifact entries
(`book/src/L1/divfree-projector.md`, `book/src/L1-L0/divfree-projector-mutation-rotation.md`)
all establish the output is the **divergence-free** component satisfying
`Gᵀ M y' = 0`. I verified the contradiction firsthand against L0 via codemap
`read_range`. The verdict is **(a) resolve**: the per-method doc comment is
stale/inverted (it describes the *removed* gradient component's curl property,
or simply a documentation error, and mislabels it "irrotational" — the term for
the gradient part, not the output). This is a **Palace-internal documentation
inconsistency**, not a defect in the artifact; the firm entries already pin the
correct semantics with full citations. **The OQ is fully answered and should be
closed** — no re-anchor, no artifact edit beyond an optional one-line
cross-link sharpening already covered below.

## Observation kind

**Consistency drift** — between two doc comments *inside the same Palace header*
(`divfree.hpp` class-level vs. method-level), where the method-level comment is
stale relative to both the class-level comment and the implementation. This is a
**source-internal** drift surfaced as a cross-layer fidelity question: does the
artifact's L1/L1-L0 "divergence-free" claim faithfully reflect L0, given that one
L0 doc-comment site says "irrotational"? Answer: yes, the artifact is faithful;
the deviant L0 site is the stale one.

## Specific finding

### The two contradicting L0 doc-comment sites (verified firsthand)

**Class-level doc comment** — `palace/linalg/divfree.hpp:28-31`:

```
// This solver implements a projection onto a divergence-free space satisfying Gᵀ M x = 0,
// where G represents the discrete gradient matrix with columns spanning the nullspace of
// the curl-curl operator.
```

**Method-level doc comment** — `palace/linalg/divfree.hpp:64-66` (immediately above the `Mult(VecType &y) const;` declaration at `:63`):

```
// Given a vector of Nedelec dofs for an arbitrary vector field, compute the Nedelec dofs
// of the irrotational portion of this vector field. The resulting vector will satisfy
// ∇ x y = 0.
```

These disagree on what `Mult` returns: the class comment says **divergence-free**
(`Gᵀ M x = 0`, solenoidal); the method comment says **irrotational** (`∇ × y = 0`,
curl-free, the gradient component).

### Which component the projector actually produces (grounded in the code)

The implementation (`palace/linalg/divfree.cpp:155-190`, `Mult(VecType &y)`) does:

1. `WeakDiv->Mult(y, rhs)` — `rhs = WeakDiv·y`, the ε-weighted weak divergence
   (Nedelec→H1), where `WeakDiv` carries a negating `-1.0`
   (`palace/fem/integ/mixedvecgrad.cpp:202`), so `WeakDiv = -Gᵀ` (ε-weighted)
   (`palace/linalg/divfree.cpp:159-168`).
2. `linalg::SetSubVector(rhs, *bdr_tdof_list_M, 0.0)` — essential-BC zeroing
   (`palace/linalg/divfree.cpp:170-174`).
3. `ksp->Mult(rhs, psi)` — solves `M·ψ = rhs`; `M` is the ε-weighted H1
   mass-like (Poisson) operator, "real and SPD"
   (`palace/linalg/divfree.cpp:119`); the solved system is `(Gᵀ M G) ψ = Gᵀ M y`
   with `M` materialized and `Gᵀ`/`G` realized by `WeakDiv`/`Grad`
   (`palace/linalg/divfree.cpp:111-117`, `:175`).
4. `Grad->AddMult(psi, y, 1.0)` — `y += Grad·ψ` (additive `+1.0`)
   (`palace/linalg/divfree.cpp:177-186`). Palace's own inline comment immediately
   above this step states the intent directly: `// Compute the irrotational
   portion of y and subtract.` (`palace/linalg/divfree.cpp:176`) — i.e. the
   *irrotational* component is the part being *removed*, leaving the
   divergence-free remainder. This is a third independent L0 witness against the
   method doc-comment.

The mathematical operator is `P = I − Grad (Gᵀ M G)⁻¹ Gᵀ M`, the **M-orthogonal
projection onto the divergence-free (solenoidal) subspace**
(`book/src/L1/divfree-projector.md:137-145`). The additive `+Grad·ψ` *removes*
the gradient part precisely because `WeakDiv` carries the negating sign — so the
net result is `y` with its irrotational (gradient-range) component **subtracted
out**. The output `y'` satisfies `Gᵀ M y' = 0` (divergence-free), per the class
doc `palace/linalg/divfree.hpp:28-31`.

So: in the Helmholtz/Hodge decomposition `y = y_divfree + Grad·ψ`, the
**`Grad·ψ` term is the irrotational (curl-free, gradient-range) component**, and
the projector **returns `y_divfree`, the divergence-free (solenoidal)
remainder**. The method comment is exactly inverted — it names the output
"irrotational portion" (the term for the part that is *removed*) and asserts
`∇ × y = 0` (the curl-free property of the *removed* gradient component, which is
trivially curl-free since `∇ × ∇ψ = 0`). The implementation, the class doc, and
both firm artifact entries agree the output is the divergence-free remainder.

### The artifact is already faithful and already documents this

This OQ is not new and the artifact already pins the correct semantics:

- `book/src/L1/divfree-projector.md:145-150` (§Semantics) explicitly calls the
  `:64-66` comment "**stale/misleading relative to the implemented behavior** (a
  Palace-internal documentation inconsistency, OQ
  `divfree-mult-doc-irrotational-vs-divfree-stale`)" and pins the divergence-free
  target with citations.
- `book/src/L1-L0/divfree-projector-mutation-rotation.md:175-181` (sub-pattern B
  citation) and `:460-468` (§Open questions) both annotate the `:63-66` comment
  as "**stale/misleading relative to the divergence-free implemented behaviour**"
  and instruct the lowering-verifier NOT to treat it as a citation against the
  divergence-free claim.
- The integrator-signals tail records the OQ as "**unblocked**" already
  (`scaffolding/integrator-signals.md:158`): "a documentation-fidelity caveat in
  Palace source, NOT a theme defect."

In other words, the cross-layer fidelity question this OQ poses has already been
answered, consistently, in the firm surface. What has not happened is the OQ's
**closure** — it has carried as a live plan/intake item across batches 3 and 4
(`scaffolding/priorities.md:27`, `scaffolding/cycle-019-resume-notes.md:88`)
because no dispatch had been scoped to formally adjudicate "resolve vs. re-anchor
vs. non-actionable" until now.

### Citation-range nuance (minor, surfaced for the integrator)

The L1-L0 theme cites the stale comment as `palace/linalg/divfree.hpp:63-66`
(sub-pattern B citation, `:175-181`) and as `:63-66` in §Open questions
(`:460-461`). The L1 entry cites it as `:64-66` (`:146`, `:147`). From firsthand
`read_range`: line `:63` is the declaration `void Mult(VecType &y) const;`; the
three-line doc comment proper is `:64-66`. Both citations are defensible (the
theme's `:63-66` bundles the declaration the comment documents; the L1 entry's
`:64-66` is the comment text alone), so this is **not** an error — but the two
firm entries cite the same site with a one-line boundary difference. Flag for an
optional future harvester/verifier normalization, not blocking.

## Recommendation

**Resolve and close the OQ.** Concretely:

1. **Close** `divfree-mult-doc-irrotational-vs-divfree-stale` in
   `scaffolding/open-questions.md` (meta-phase has the unify/close authority;
   this dispatch surfaces the closure-ready verdict). Disposition: **answered —
   Palace-internal stale method doc-comment; output is divergence-free
   (`Gᵀ M y' = 0`), the method comment's "irrotational / ∇×y=0" describes the
   removed gradient component and is inverted; artifact faithfully documents the
   correct semantics at `book/src/L1/divfree-projector.md:145-150` +
   `book/src/L1-L0/divfree-projector-mutation-rotation.md:460-468`; no artifact
   defect.**
2. **Mark the plan item done** (`scaffolding/priorities.md:27` — already struck
   as DISPATCHED; flip to resolved at integration).
3. **Optional** (proposed-changes block below) — a one-line sharpening of the
   L1-L0 theme's §Open-questions note so the closure is self-contained (cite the
   *class* doc as the authoritative L0 site and explicitly state the inversion).
   This is a cross-link sharpening, not a semantics change; defer if the
   integrator prefers a zero-edit closure.

No re-anchor (the source is **not** genuinely ambiguous — the class doc + the
implementation are decisive). Not non-actionable (the actionable step is closure
of a carry-forward OQ that has lingered two batches without migration; per
CLAUDE.md "an open question that lingers in its intake channel without a plan
item means migration hasn't happened — that is the defect to catch").

No follow-up combinator-miner / lifter candidate surfaces — the semantics are
firm and the projector's nested-gate / sign sub-notes are already mined.

## Proposed-changes block (OPTIONAL — cross-link sharpening only; integrator may skip for zero-edit closure)

File: `book/src/L1-L0/divfree-projector-mutation-rotation.md`

Replace the first bullet of §"Open questions / caveats" (the "Stale `Mult` doc
comment" bullet, lines ~460-468):

OLD:
```
- **Stale `Mult` doc comment.** `palace/linalg/divfree.hpp:63-66` describes the
  output as "the irrotational portion ... satisfying ∇ × y = 0", contradicting
  the divergence-free implemented behaviour and the class doc
  `palace/linalg/divfree.hpp:28-31` (`Gᵀ M x = 0`). This is a pre-existing
  Palace-internal documentation inconsistency, already tracked as OQ
  `divfree-mult-doc-irrotational-vs-divfree-stale` (carried from the L1 entry,
  cycle-013). Not a defect in this theme; the rewrite honours the *implemented*
  divergence-free semantics. Flag for the `lowering-verifier` (it should NOT
  treat the stale comment as a citation against the divergence-free claim).
```

NEW:
```
- **Stale `Mult` doc comment (resolved cycle-019 — OQ closed).** The per-method
  doc comment `palace/linalg/divfree.hpp:64-66` describes the output as "the
  irrotational portion ... satisfying ∇ × y = 0". This is **inverted**: in the
  Helmholtz/Hodge decomposition `y = y_divfree + Grad·ψ`, the *irrotational*
  (curl-free, gradient-range) component is the `Grad·ψ` term that the projector
  *removes* — the comment names the removed part and its trivially-curl-free
  property (`∇ × ∇ψ = 0`) where it should describe the divergence-free
  *remainder* the projector returns. The authoritative L0 site is the **class**
  doc `palace/linalg/divfree.hpp:28-31` ("projection onto a divergence-free
  space satisfying `Gᵀ M x = 0`"), which the implementation
  (`palace/linalg/divfree.cpp:155-190`) realises; Palace's own inline comment at
  `palace/linalg/divfree.cpp:176` ("Compute the irrotational portion of y and
  subtract.") confirms the irrotational component is the *subtracted* part. A
  pre-existing Palace-internal
  documentation inconsistency, NOT a defect in this theme; the rewrite honours
  the *implemented* divergence-free semantics. The `lowering-verifier` must NOT
  treat the per-method comment as a citation against the divergence-free claim.
  (OQ `divfree-mult-doc-irrotational-vs-divfree-stale`, carried from the L1
  entry cycle-013, re-surfaced cycle-016, resolved cycle-019.)
```

Rationale: makes the resolution self-contained inside the firm theme (names the
authoritative class-doc site, states the inversion explicitly, records the
closure cycle), so a future reader/verifier does not re-open the question. No
semantics change; the divergence-free claim and all step citations are unchanged.
The integrator-finalize/per-report applies this if it wants the closure recorded
in the artifact; otherwise the OQ-ledger closure (recommendation #1) suffices.

## Supporting evidence

L0 (Palace source, verified firsthand via codemap `read_range` this dispatch):
- `palace/linalg/divfree.hpp:28-31` — **class** doc comment: "projection onto a
  divergence-free space satisfying `Gᵀ M x = 0`". The authoritative site.
- `palace/linalg/divfree.hpp:63` — `void Mult(VecType &y) const;` declaration.
- `palace/linalg/divfree.hpp:64-66` — **method** doc comment: "irrotational
  portion ... ∇ x y = 0". The stale/inverted site.
- `palace/linalg/divfree.hpp:68-72` — `Mult(const VecType &x, VecType &y) { y =
  x; Mult(y); }` out-of-place wrapper.
- `palace/linalg/divfree.cpp:155-190` — `Mult(VecType &y)` body (four steps +
  the `Vector`/`ComplexVector` instantiations at `:189-190`).
- `palace/linalg/divfree.cpp:176` — inline implementation comment `// Compute the
  irrotational portion of y and subtract.` — a third independent L0 witness that
  the irrotational component is the *removed* part (the divergence-free remainder
  is what `Mult` returns), directly corroborating the inversion in the
  `:64-66` method doc-comment.
- `palace/linalg/divfree.cpp:111-117` — `WeakDiv`
  (`MixedVectorWeakDivergenceIntegrator`, partially assembled, `:111-115`) and
  `Grad` (discrete gradient interpolator, `:117`) construction.
- `palace/linalg/divfree.cpp:119` — `// The system matrix for the projection is
  real and SPD.` (the `M` Poisson operator solved by `ksp`).
- `palace/fem/integ/mixedvecgrad.cpp:202` — the negating `-1.0` making
  `WeakDiv = -Gᵀ` (so the additive `+Grad·ψ` net-removes the gradient part).

Artifact (firm entries — already document the resolution):
- `book/src/L1/divfree-projector.md:113-150` — §Semantics; Helmholtz
  decomposition, projector `P = I − Grad(GᵀMG)⁻¹GᵀM`, and the `:145-150`
  stale-comment annotation.
- `book/src/L1-L0/divfree-projector-mutation-rotation.md:175-181` — sub-pattern
  B citation annotating the `:63-66` comment as stale.
- `book/src/L1-L0/divfree-projector-mutation-rotation.md:460-468` — §Open
  questions "Stale `Mult` doc comment" bullet (target of the optional edit).

Scaffolding (OQ lineage):
- `scaffolding/priorities.md:27` — plan item #6, DISPATCHED cycle-019 wave-1.
- `scaffolding/cycle-019-resume-notes.md:88` — carry-forward note (batches 3/4).
- `scaffolding/integrator-signals.md:158` — prior "unblocked" signal (cycle-016,
  carried from cycle-013).
- `scaffolding/open-questions.md` — the OQ is currently tracked via the plan
  item (the exact slug is not in the Closed index; closing it there is the
  meta-phase unify-pass action this report unblocks).

## Open questions / caveats

- **OQ closure-ready, not yet closed.** This report adjudicates the carry-forward
  OQ `divfree-mult-doc-irrotational-vs-divfree-stale` as **resolved (answered)**.
  Closure in `scaffolding/open-questions.md` is meta-phase unify-pass authority;
  this dispatch surfaces the closure-ready verdict + disposition text
  (Recommendation #1). If the meta-phase does not close it at the next batch
  boundary, that is the "lingering-without-migration" defect to catch — flag it
  again.
- **Minor citation-range divergence between the two firm entries** for the same
  stale-comment site: the L1-L0 theme cites `palace/linalg/divfree.hpp:63-66`
  (declaration + comment), the L1 entry cites `:64-66` (comment only). Both
  defensible; line `:63` is the declaration, `:64-66` the three-line comment.
  Not blocking; candidate for a future harvester/verifier normalization pass on
  the divfree cohort. No new OQ recommended (too minor; note it here for the
  record).
- **Upstream-fix scope.** The clean fix would be to correct Palace's own
  `divfree.hpp:64-66` comment upstream, but that is **out of this project's
  scope** (we dissect Palace, we don't patch it). The artifact documents the
  Palace-internal inconsistency faithfully; that is the correct disposition for a
  source-side doc bug.
- **No re-anchor / no lifter follow-up.** The source is unambiguous (class doc +
  implementation are decisive); the L1 and L1-L0 entries are firm and faithful.
  No abstractor/lifter dispatch is warranted.
