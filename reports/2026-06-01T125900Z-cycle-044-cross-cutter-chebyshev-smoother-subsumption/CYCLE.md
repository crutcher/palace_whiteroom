---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-01T125900Z
scope: L3↔L1 cross-cut — chebyshev-smoother L3 subsumption check (cycle-044 D2)
status: pending
integrated_at: 2026-06-01T150500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-044 batch integration; D2 cross-layer-cross-cutter — read-only OBSERVATION (NO book mutation). Verdict: chebyshev-smoother L3 SUBSUMED by firm L3 chebyshev (c013, partial-obstruction) — NO-LAND; discharges the c036 D2 index.md:48 subsumption-check caveat; a clean negative result that REMOVES the chebyshev-smoother (B)-candidate, leaving apply_nonlinear_pencil as the only remaining (B)-candidate. Scaffolding-only landings: priorities.md candidate-closure + closure OQ chebyshev-smoother-l3-candidate-subsumed-closed; see reports/2026-06-01T150500Z-integrator-finalize-cycle-44/CYCLE.md + cycle-044 STAGING row 4."
---

# CYCLE: Cross-layer observation — chebyshev-smoother-L3-subsumed-by-firm-chebyshev

## Summary

The c036 D2 (B)-substantive candidate `chebyshev-smoother` at L3 is **fully
subsumed** by the existing firm L3 [`chebyshev`](../../book/src/L3/chebyshev.md)
row (`partial-obstruction`, harvested cycle-013). "chebyshev-smoother" is not a
distinct Palace operation — it is the **L1 slug** (`book/src/L1/chebyshev-smoother.md`)
for the same polynomial iteration whose L3 iteration-rotation rendering already
exists as L3 `chebyshev`. Palace's `ChebyshevSmoother` / `ChebyshevSmoother1stKind`
classes (`palace/linalg/chebyshev.hpp:23, :86`) ARE the Chebyshev polynomial
iteration packaged behind the `Solver<OperType>` smoother/preconditioner `Mult`
interface — same `Mult2` body, no separate operation — and both classes are
*already cited* as the L0 source of the firm L3 `chebyshev` entry. A standalone
L3 `chebyshev-smoother` row would be a duplicate of L3 `chebyshev` under the L1
name, splitting one operator across two L3 entries and violating the
one-operator-per-layer coherence the firm row already satisfies. **Verdict:
SUBSUMED, NO-LAND.** Recommend closing the candidate in the plan.

## Observation kind

**Coverage gap (NEGATIVE result)** — the candidate names an L3 operator that
appears to be a coverage gap but is in fact already covered. The "gap" is an
artifact of the L1-slug name (`chebyshev-smoother`) differing from the L3-slug
name (`chebyshev`) for the same operator. No real gap exists; the candidate
should be retired rather than dispatched.

## Specific finding

**The candidate is a name-collision, not a missing operator.** Concretely:

1. **There is exactly one Chebyshev operation in Palace, exposed via two
   polynomial-kind classes — both already captured.** `search_text "class
   Chebyshev"` over the headers returns exactly two hits:
   - `ChebyshevSmoother : public Solver<OperType>` (`palace/linalg/chebyshev.hpp:23`,
     4th-kind);
   - `ChebyshevSmoother1stKind : public Solver<OperType>` (`palace/linalg/chebyshev.hpp:86`,
     1st-kind).
   These are the **polynomial-kind variant axis** (`Chebyshev-4th | Chebyshev-1st`),
   which the firm L3 `chebyshev` entry explicitly absorbs at construction into
   `op.scalars` / `op.scalar_init` (L3 `book/src/L3/chebyshev.md:415-420` Variant axes §1;
   Law 5 "variant-invariant body sequence", `book/src/L3/chebyshev.md:316-324`). The L3 entry
   already cites both classes by exact line: `book/src/L3/chebyshev.md:509-511`
   (`ChebyshevSmoother` decl), `book/src/L3/chebyshev.md:514-516` (`ChebyshevSmoother1stKind` decl).

2. **"Smoother" is the consumer wrapper, not a distinct body.** Both classes
   subclass `Solver<OperType>` and implement `Mult` / `Mult2`; the smoother/
   preconditioner role is the `Mult` interface, not a separate algorithm. The
   `Mult2` bodies (`palace/linalg/chebyshev.cpp:191-220` 4th-kind, `:261-293`
   1st-kind) ARE the cited L0 source of the firm L3 `chebyshev` entry
   (`book/src/L3/chebyshev.md:496-508` Evidence). The smoother-as-linear-preconditioner
   consumer role (the use the *name* "smoother" connotes — applying the
   polynomial as the `B` preconditioner in an outer Krylov method / multigrid
   V-cycle correction) is already an explicit law: **Law 2 "Linear
   preconditioner form (zero initial guess, single sweep)"**, `y' =
   p_order(D⁻¹ A)·x` (`book/src/L3/chebyshev.md:299-304`). The symmetry-alias `MultTranspose2
   → Mult2` (`palace/linalg/chebyshev.hpp:72-75`, verified `:60-75`) is Law 3.

3. **The firm L3 `chebyshev` entry's body + obstruction analysis already says
   everything an L3 `chebyshev-smoother` entry would.** The entry's title is
   literally "the iteration-rotation rendering of the **Chebyshev smoother**"
   (`book/src/L3/chebyshev.md:16-17`); its L1 sibling is `chebyshev-smoother`
   (`book/src/L3/chebyshev.md:404-405`, `book/src/L3/chebyshev.md:91`); the body identity-in-form law transitively
   ties the L3 body to the L1 `chebyshev-smoother` closed-form action (Law 6,
   `book/src/L3/chebyshev.md:325-331`). The `partial-obstruction` verdict (body lifts; inner
   `k`-recurrence + outer `pc_it` Richardson sweep are witnessed sequential
   obstructions per Phillips & Fischer 2022 §2) is the honest, complete L3 story
   for the fixed-degree polynomial smoother. There is no residual content a
   second entry would carry.

4. **The L3 index already routes the name correctly.** The L3 dep-map row for
   `chebyshev` (`book/src/L3/index.md:30`) describes it as the "value-threaded
   fixed-degree polynomial smoother" and points its L1 anchor chain at the
   `chebyshev-smoother` slug. The §Working-notes already record `chebyshev` as
   the canonical first L3 `partial-obstruction` (`book/src/L3/index.md:55`). A standalone
   `chebyshev-smoother` L3 row would create a second index entry for the same
   operator.

**Net:** landing `chebyshev-smoother` standalone at L3 would split one operator
across two L3 chapters under two names (L1-name vs L3-name), duplicate the entire
body + obstruction analysis, and create a cross-reference ambiguity (which entry
does L2 `chebyshev-iteration` / L4 `chebyshev` lower-to / lift-from?). This is
the exact duplication-explosion the methodology guards against.

## Recommendation

**Close the `chebyshev-smoother` (B)-candidate in the plan — SUBSUMED, NO-LAND.**

- The c036 D2 audit listed `chebyshev-smoother` as a (B)-substantive candidate
  *with the explicit caveat* "possibly subsumed by the existing firm L3
  `chebyshev` row — requires a subsumption check first" (`book/src/L3/index.md:48`).
  This dispatch IS that subsumption check; it resolves **subsumed**.
- **Proposed plan action (for cycle-planner):** mark the `chebyshev-smoother`
  L3 (B)-candidate **closed / retired** in `scaffolding/priorities.md`, with the
  resolution note "subsumed by firm L3 `chebyshev` (c013); `chebyshev-smoother`
  is the L1-slug name for the same operator whose L3 rendering is L3 `chebyshev`;
  Palace `ChebyshevSmoother`/`ChebyshevSmoother1stKind` are the polynomial-kind
  variant axis already absorbed at L3, cited `book/src/L3/chebyshev.md:509-516`."
- **No abstractor / harvester / lifter dispatch needed.** No theme to author, no
  re-anchor, no audit gap.
- **No `book/` edit required.** The firm L3 `chebyshev` entry, the L3 index row,
  and the §Working-notes are already correct and complete. This is a pure
  read-only audit (OQ-ledger + plan-close only); **no proposed-changes block**.

This is a clean negative result that *removes* a (B)-candidate from the batch-13
substantive-L3 frontier rather than adding work — useful input for the
cycle-planner's next-cohort selection.

## Supporting evidence

- `book/src/L3/chebyshev.md` — the firm L3 entry (`partial-obstruction`, c013).
  Title `:16-17` ("iteration-rotation rendering of the Chebyshev smoother");
  Law 2 linear-preconditioner-form (smoother-as-`B`) `:299-304`; Law 3 symmetry
  alias `:306-309`; Law 5 variant-invariant body `:316-324`; Law 6 body
  identity-in-form across L3↔L2↔L1 incl. L1 `chebyshev-smoother` `:325-331`;
  Variant axes §1 polynomial-kind absorption + both-class citations `:415-425`;
  Evidence block citing both `Mult2` bodies + both class decls `:496-518`.
- `book/src/L2/chebyshev-iteration.md` — the L2 primitive-composition form the
  L3 body is identity-in-form to (the L3 entry's `lowers_to`); `firm` cycle-012.
- `book/src/L1/chebyshev-smoother.md` — the L1 operator the candidate name comes
  from; the closed-form action the L3 body is value-thread-isomorphic to.
- `book/src/L4/chebyshev.md` — the L4 typed-wrapper the L3 entry lifts from.
- `book/src/L3/index.md:30` — the L3 dep-map `chebyshev` row ("fixed-degree
  polynomial smoother"); `:48` — the c036 D2 (B)-candidate line carrying the
  "requires a subsumption check first" caveat this dispatch resolves; `:55` —
  §Working-notes recording `chebyshev` as the first L3 `partial-obstruction`.
- Palace source (verified via codemap this dispatch):
  - `palace/linalg/chebyshev.hpp:23` — `class ChebyshevSmoother : public
    Solver<OperType>` (4th-kind); `:86` — `class ChebyshevSmoother1stKind :
    public Solver<OperType>` (1st-kind). The only two `class Chebyshev*` hits in
    the tree.
  - `palace/linalg/chebyshev.hpp:15-19` — class doc: "Matrix-free
    diagonally-scaled Chebyshev smoothing … Phillips and Fischer."
  - `palace/linalg/chebyshev.hpp:60-75` — `MultTranspose` → `MultTranspose2` →
    `Mult2` (symmetry alias `:72-75`); the `Mult2` body is the cited L0 source
    of the firm L3 entry. The `Solver<OperType>` `Mult` interface IS the
    smoother/preconditioner consumer surface (no separate operation).

## Open questions / caveats

- **None blocking the verdict.** The subsumption is unambiguous: one operation,
  two polynomial-kind classes, both cited; the L3 rendering exists and is firm.
- Minor note (not action-bearing): the L1 / L3 slug-name asymmetry
  (`chebyshev-smoother` at L1, `chebyshev` at L3/L4, `chebyshev-iteration` at L2)
  is benign and intentional — each layer names the operator in its own
  vocabulary (L1 names the Palace class role "smoother"; L2 names the unfolded
  "iteration"; L3/L4 name the bare operator). The cross-references between layers
  are all correct and live. No rename is warranted; raising one would be churn.
  Recording only so a future audit does not re-flag the name asymmetry as a
  coverage gap (it is the same false-positive this dispatch resolved).
- Follow-up candidates surfaced: none. This closes a candidate; it does not spawn
  one. The other two c036 D2 (B)-candidates remain as the planner left them:
  `orthogonalize` (LANDED c040) and `apply_nonlinear_pencil` (the c036 audit
  already routed it as "fold into a future eigsolve-variant deepening pass, NOT a
  separate L3 row", `book/src/L3/index.md:48` — a similar interior-to-`eigsolve` non-land
  that a future dispatch could confirm, but out of this observation's scope).
