---
agent: cross-layer-cross-cutter
invoked_at: 2026-05-28T22:31:27Z
scope: L1↔L1>L0 cross-cut — closure-nesting (constructed gate carrying a constructed gate as a sub-field)
status: integrated
integrated_at: 2026-05-28T230323Z
integration_commit: 80db8d6
integration_notes: |
  Applied cycle-017 (per-report position 5; FINAL). READ-ONLY cross-layer audit
  — ZERO book/ mutation (no proposed-changes block; OQ-ledger appends only).
  Refuted (critic VERIFIED-SOUND) the cycle-016 divfree theme's "first L1>L0
  closure carrying a constructed-operator gate / does not recur" premise: the
  firm eigsolve-mutation-rotation theme (cycle-011 8bb16b7, five cycles before
  divfree b54ea1c) is the prior + richer instance (two nested gates; eigsolve ⊃
  divfree ⊃ ksp transitively); divfree is the THIRD instance. ≥2-firm-instance
  bar cleared. OQ divfree-closure-nesting-constructed-gate-carrying-constructed-gate
  answered; NEW OQ nested-constructed-operator-gate-concept-and-divfree-correction
  opened (routes cycle-018: (a) concept page -> layer-intro-author; (b)
  divfree-theme "first"-claim correction -> lifter/harvester).
---

# CYCLE: Cross-layer observation — closure-nesting-constructed-gate-carrying-constructed-gate

## Summary

The cycle-016 `divfree-projector-mutation-rotation` theme (and its source OQ
`closure-nesting-constructed-gate-carrying-constructed-gate`) claims to be the
**first L1>L0 mutation-rotation whose closure carries another constructed-operator
gate as a sub-field**, and asserts the nesting pattern **does NOT recur** in the
current L1 op set. **Both claims are refuted by the existing firm
`eigsolve-mutation-rotation` theme** (landed cycle-011, commit `8bb16b7`), whose
closure `E` carries TWO nested constructed-operator gates — `E.linear : Solver[A]`
(an inner `ksp_solve` gate) and `E.projector : Maybe DivFreeSolver[ComplexVector]`
(the very projector the cycle-016 theme formalises) — and whose **core sub-pattern
B** is precisely the nested-gate lowering, delegating each `opInv->Mult` to the
firm `ksp-solve-mutation-rotation` theme. So divfree is the **third** L1>L0
mutation-rotation exhibiting gate-carrying-gate, not the first, and the L1
`eigsolve` operator entry already names the pattern in prose ("the first L1
operator to compose two layers of constructed-operator absorption",
`book/src/L1/eigsolve.md:136`). With **≥2 firm instances now confirmed**, the
pattern clears the ≥2-instance bar: it warrants a **named concept page** sibling to
`constructed-operator-factory` (provisional slug `nested-constructed-operator-gate`),
authored by `layer-intro-author`, replacing the in-line note currently in the
divfree theme.

## Observation kind

**Vocabulary mismatch / coverage gap (compound).** The cycle-016 theme + OQ assert
a uniqueness ("first", "does not recur") that is factually wrong against firm
artifact content authored five cycles earlier — a vocabulary/provenance mismatch.
The downstream consequence is a coverage gap: a recurring structural shape
(≥2 firm instances, prose-named in the `eigsolve` L1 entry) has no shared concept
home, so each instance re-narrates it ad hoc.

## Specific finding

The candidate L1 operators whose closure might carry a constructed-operator gate as
a sub-field, surveyed for the gate-carrying-gate shape:

| L1 operator | closure sub-fields | carries a constructed-operator gate? |
|---|---|---|
| `ksp_solve` | `K.A` (system op), `K.M⁻¹` (preconditioner) | **borderline** — see note below |
| `eigsolve` | `E.linear : Solver[A]`, `E.projector : Maybe DivFreeSolver`, `E.K/M/C/A2` (raw ops), `E.B` | **YES (two gates)** |
| `chebyshev-smoother` | `op.A : LinearOperator[N,N]` (raw op), `op.dinv`, `op.scalars` | NO — `op.A` is a raw `LinearOperator`, not a gate (`book/src/L1/chebyshev-smoother.md:58`) |
| `divfree-projector` | `P.M`, `P.WeakDiv`, `P.Grad`, `P.bdr_tdof_list_M`, `P.ksp : Solver[P.M]` | **YES (one gate, `P.ksp`)** |
| `apply_linop` | none (raw tensor + raw operator args) | NO |
| `axpy/axpby/axpbypcz/dot/nrm2/scal/orthogonalize/matrix-weighted-norm/bilinear-form` | raw tensors / scalars / raw operators | NO |

**Decisive instance — `eigsolve` (firm, cycle-011, predates divfree by 5 cycles):**

- L1 operator entry `book/src/L1/eigsolve.md:60` — `E` "additionally binds the
  inner linear solver (`linear : Solver[A]` …), the optional divergence-free
  projector (`projector : Maybe DivFreeSolver[ComplexVector]`)".
- L1 operator entry `book/src/L1/eigsolve.md:136` — "**This is the second L1
  operator (after `ksp_solve` itself depending on `apply_linop`) whose primary
  dependency is itself a constructed-operator type**, making `eigsolve` the **first
  L1 operator to compose two layers of constructed-operator absorption**."
- L1 operator entry `book/src/L1/eigsolve.md:140` — "This is structurally the same
  nesting pattern as preconditioner application inside an iterative solver —
  composed-not-inherited."
- L1>L0 theme `book/src/L1-L0/eigsolve-mutation-rotation.md:213-258` — **Sub-pattern
  B**, explicitly "the **core sub-pattern** of the theme": the L1 `E.linear` inner
  solver's per-step `opInv->Mult` (ten call sites) "rewrites by the firm
  `ksp-solve-mutation-rotation` theme" — i.e. the nested gate is lowered through its
  own gate's theme, exactly the structure the divfree theme describes as novel.
- Theme provenance: commit `8bb16b7` (cycle-011 integrator-finalize) landed it as
  "first partly-constructive".

**The divfree theme's own claims:**

- `book/src/L1-L0/divfree-projector-mutation-rotation.md:108-113` — sub-pattern A:
  "Inner solve is itself a constructed-operator gate. … This is **the first L1>L0
  mutation-rotation whose closure carries *another* constructed-operator gate as a
  sub-field** (`P.ksp : Solver[P.M]`)."
- `book/src/L1-L0/divfree-projector-mutation-rotation.md:457-464` — Open-questions
  item: "the first such case in the L1>L0 mutation-rotation family … a recurring
  structural shape shared with no other current L1 op."
- OQ ledger line 2897 — "it does not in the *current* set — no other L1 op carries a
  constructed gate as a closure sub-field".

All three are inaccurate. `eigsolve` is the prior (and a richer, two-gate) instance.

**`ksp_solve` borderline note (worth surfacing, not load-bearing for the verdict):**
`ksp_solve`'s closure `K` binds a preconditioner `M⁻¹` (`book/src/L1/ksp_solve.md:31`).
Via the `solver-as-operator` rotation, a preconditioner **is-an** operator and may
itself be a `Solver`-typed handle (e.g. a nested `ksp` used as a preconditioner, or
the chebyshev-smoother used as `B`). When `K.M⁻¹` is a `Solver`, `ksp_solve` is
*also* a gate-carrying-gate. But the L1 `ksp_solve` entry types `M⁻¹` as a plain
`LinearOperator[N, N]` (not necessarily a gate), and the `ksp-solve-mutation-rotation`
theme treats the preconditioner as opaque — so I count `ksp_solve` as a *latent*
nesting site, not a confirmed firm instance. This is itself evidence FOR the
concept: the pattern is structural to the whole constructed-operator family
(preconditioner-inside-solver, inner-solve-inside-eigensolver,
inner-solve-inside-projector), which is exactly why a shared concept page earns its
keep.

## Recommendation

**Dispatch `layer-intro-author` to author a new concept page** (provisional slug
`nested-constructed-operator-gate`, sibling to
`book/src/concepts/constructed-operator-factory.md`). The ≥2-instance bar is cleared
with two FIRM instances (`eigsolve`, cycle-011; `divfree-projector`, cycle-016) plus
the prose-named precedent in `book/src/L1/eigsolve.md:136,140` and the latent
`ksp_solve` preconditioner site. The concept page should:

- Name the shape: a constructed-operator closure whose **field is itself a
  constructed-operator gate** (`Solver[A]`, `DivFreeSolver`, …), distinct from a
  closure carrying a *raw* operator (`chebyshev-smoother`'s `op.A`, `apply_linop`'s
  operand).
- State the lowering consequence (the cross-layer fidelity rule): **the inner gate's
  iteration stays interior to the inner gate's own theme** and does not leak into the
  outer theme — at the outer theme's resolution the inner gate is an opaque action
  (`ksp->Mult(rhs, psi)` = opaque `K⁻¹`; `opInv->Mult(b,x)` = opaque inner solve).
  This is the "composed-not-inherited" remark at `book/src/L1/eigsolve.md:140`.
- Index the instances: `eigsolve` (`E.linear`, `E.projector` — two gates),
  `divfree-projector` (`P.ksp` — one gate), latent `ksp_solve` (`K.M⁻¹` when the
  preconditioner is a `Solver`).
- Relate to siblings: `constructed-operator-factory` (the construction site of a
  gate), `solver-as-operator` (the type rotation that lets a gate appear as an
  operator field), `variant-absorption`.

This is `layer-intro-author` authority (it writes `book/src/concepts/<slug>.md`
pages per its role spec). A `combinator-miner` pass is the alternative if the pattern
should crystallise into an L2/L4 combinator rather than a concept page — but the
shape is presently a *naming/documentation* shape (how themes treat nesting), not a
new evaluation primitive, so the concept page is the right first home; defer
combinator-mining until/unless the nesting needs a calculus-level operator.

**Two follow-up corrections** (NOT my authority to enact — surface only):

1. **harvester / lifter on `book/src/L1-L0/divfree-projector-mutation-rotation.md`** —
   correct the three "first" / "no other current L1 op" claims (lines 111-113,
   457-464) to cite `eigsolve-mutation-rotation` sub-pattern B as the prior instance,
   and re-point the in-line note at the new concept page once it lands. (After
   `integrated_at:` is set the theme is append-only; this should be a scoped
   correction dispatch, not a free edit.)
2. **OQ-ledger update** — the `closure-nesting-...` OQ premise ("does not recur")
   is refuted; it should be ANSWERED with the `eigsolve` precedent + the concept-page
   recommendation, not left asserting non-recurrence.

## Supporting evidence

- `book/src/L1/eigsolve.md:60` — `E.linear : Solver[A]` + `E.projector : Maybe
  DivFreeSolver[ComplexVector]` closure sub-fields (two nested gates).
- `book/src/L1/eigsolve.md:136` — "first L1 operator to compose two layers of
  constructed-operator absorption".
- `book/src/L1/eigsolve.md:140-142` — "structurally the same nesting pattern …
  composed-not-inherited"; ties to `constructed-operator-factory`.
- `book/src/L1-L0/eigsolve-mutation-rotation.md:14-16,157-162,213-258` — closure
  carries `E.linear`/`E.projector`; sub-pattern B (the **core** sub-pattern) lowers
  the nested `opInv->Mult` gate via the firm `ksp-solve-mutation-rotation` theme.
- `book/src/L1-L0/divfree-projector-mutation-rotation.md:108-113` (sub-pattern A
  "inner solve is itself a constructed-operator gate" + "first" claim),
  `:193-198` (sub-pattern C `P.ksp` materialisation), `:457-464` (OQ note "no other
  current L1 op").
- `book/src/L1/ksp_solve.md:31` — `K` binds preconditioner `M⁻¹` (latent
  gate-carrying-gate via `solver-as-operator`).
- `book/src/L1/chebyshev-smoother.md:56-58` — `op.A : LinearOperator[N,N]` is a RAW
  operator, NOT a gate (negative case: closure carrying a raw operator ≠ nesting).
- `book/src/concepts/constructed-operator-factory.md:1-42` — the existing sibling
  concept (construction site of a gate); the new page is the *nesting* counterpart.
- `scaffolding/open-questions.md:2888-2897` — the OQ being addressed (the refuted
  "does not recur" premise).
- Provenance: `git log` — `8bb16b7` (cycle-011, eigsolve theme landed) predates
  `b54ea1c` (cycle-016, divfree theme landed) by five cycles.

## Open questions / caveats

**Follow-up dispatches to route (the deliverable of this read-only audit — restated
here for OQ-ledger promotion; full justification in §Recommendation):**

- **`nested-constructed-operator-gate` concept page (route to cycle-018
  `layer-intro-author`).** The ≥2-firm-instance bar is cleared (`eigsolve`,
  cycle-011 `8bb16b7`; `divfree-projector`, cycle-016 `b54ea1c`), so the
  gate-carrying-gate shape warrants a named concept page sibling to
  `book/src/concepts/constructed-operator-factory.md` (provisional slug
  `nested-constructed-operator-gate`), replacing the in-line note in the divfree
  theme. Scope + page contents specified in §Recommendation.
- **Divfree-theme "first" / "no other op" correction (route to cycle-018
  lifter/harvester on `book/src/L1-L0/divfree-projector-mutation-rotation.md`).**
  Three claims are inaccurate against firm artifact authored five cycles earlier:
  `:108-113` ("the first L1>L0 mutation-rotation whose closure carries another
  constructed-operator gate"), `:457-464` ("the first such case … shared with no
  other current L1 op"), and OQ-ledger `:2897` ("does not … no other L1 op carries a
  constructed gate"). All should cite `eigsolve-mutation-rotation` sub-pattern B
  (`book/src/L1-L0/eigsolve-mutation-rotation.md:213-258`) as the prior, richer
  (two-gate) instance and re-point the in-line note at the new concept page once it
  lands. Append-only after `integrated_at:` — scoped correction dispatch, not a free
  edit.
- **ANSWER the OQ `closure-nesting-constructed-gate-carrying-constructed-gate` (a.k.a.
  `divfree-closure-nesting-…`).** Its "does not recur" premise is refuted by the
  `eigsolve` precedent; the OQ should be ANSWERED (not left asserting non-recurrence)
  with the precedent citation + the concept-page recommendation above.

- **Resolution-disposition for `eigsolve` partly-constructive context.** The
  `eigsolve-mutation-rotation` theme is `firm (structural)` overall but its
  `LinearSolveFailed` sub-part is partly-constructive (a *separate* status concern
  from the nesting shape). The nesting (sub-pattern B's `opInv->Mult` → firm
  `ksp-solve-mutation-rotation`) is itself firm and source-anchored — the
  partly-constructive caveat is about the discarded convergence status, not about
  the gate-nesting structure. So `eigsolve` is a valid FIRM instance of the nesting
  shape for the ≥2-instance count, independent of the `LinearSolveFailed` caveat. I
  verified this reading but a `layer-instro-author` authoring the concept page
  should confirm it before citing `eigsolve` as a clean instance.
- **`E.projector` is a SECOND gate inside `eigsolve` and it is the divfree projector
  itself.** `E.projector : Maybe DivFreeSolver` means the cycle-016 divfree projector
  is *itself* a sub-field of the `eigsolve` closure — so the two confirmed instances
  are not merely parallel, they are *transitively nested* (eigsolve ⊃ divfree ⊃ ksp).
  The concept page should note this three-deep transitivity; it strengthens the
  "recurring structural shape" case considerably and is direct evidence the pattern
  is load-bearing across the eigenmode pipeline, not incidental.
- **Concept vs combinator boundary.** I recommend a concept page over a combinator
  because the shape is currently a documentation/fidelity convention (how nested
  themes delegate), not a new evaluation primitive. If a later cycle finds the
  nesting needs explicit calculus-level support (e.g. an L4 `withInnerSolver`
  bracket), re-route to `combinator-miner`. Flag, don't pre-decide.
- **Did NOT verify the latent `ksp_solve` preconditioner-as-`Solver` claim against
  L0 source.** The `solver-as-operator`-via-preconditioner nesting is asserted from
  the L1 entry's type structure (`book/src/L1/ksp_solve.md:31`) + the
  `solver-as-operator` concept; I did not confirm a concrete Palace site where a
  `BaseKspSolver`'s preconditioner is itself a `BaseKspSolver`. The concept page
  author (or a harvester) should confirm before listing `ksp_solve` as more than a
  *latent* site. (Chebyshev-as-preconditioner inside a Krylov solver IS such a site
  in principle — `chebyshev-smoother` §"used as the `B` preconditioner inside an
  outer Krylov method", `book/src/L1/chebyshev-smoother.md:140` — but chebyshev is
  not itself a `Solver`-gate; it is a smoother-as-operator, a weaker nesting.)
