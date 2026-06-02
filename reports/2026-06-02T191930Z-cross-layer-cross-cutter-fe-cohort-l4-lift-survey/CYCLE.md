---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-02T191930Z
scope: L1↔L4 cross-cut — fe-cohort-l4-lift-survey (the FE-assembly + FE-space cohort is stranded at L1; L4 must be complete over the in-scope feature set)
status: pending
integrated_at: 2026-06-02T193833Z
integration_commit: 33a56f6
integration_notes: "cycle-067 D2 — applied clean (observation-only — NO book/ write; fourth/last per-report integrator). OBSERVATION-ONLY FE-cohort→L4 lift survey; 4 OQs promoted (the c068 fan-out dispatch ranking: rank-1 fe_assemble L4 assemble-fold the frontier opener; rank-2 assemble_frequency_operator via linear_combination GATED on the L4/index.md:66 13-of-18 sub-finding; ranks 3-4 the Dirichlet-BC post-compositions). citecheck --scan 38 ok / 1 [MISS] = path-hygiene shorthand in observation prose (NON-BLOCKING; the file resolves at the full path). Scaffolding-only. Staging row: cycle-067-integrator-staging/STAGING.md."
---

# CYCLE: Cross-layer observation — fe-cohort-l4-lift-survey

## Summary

The 8 firm-L1 FE-assembly + FE-space cohort entries (`fe_assemble`, `fe_space`, `fe_collection`,
`essential_dofs`, `weak_form_term`, `eliminate_essential_bc`, `eliminate_rhs`,
`assemble_frequency_operator`) are **verified-ABSENT from `book/src/L4/`** this cycle (the L4 chapter
inventory is `chebyshev / eigsolve / fold_solve / iterate-while / iterate-while-with-prev /
krylov-step / ksp_solve / solve_family` + the vocabulary anchors — no FE entry). This is the real
deliverable hole directive 1 (2026-06-02, L4-is-the-outward-backend-lowering-target) names: L4 must be
COMPLETE over the in-scope feature set, and the **entire FE-assembly/FE-space feature surface tops out
at L1**. Surveying the cohort under the directive-2 three-way black-box/accelerated/named-abstraction
test: **exactly one member rises as new L4 combinator vocabulary** — `fe_assemble`, which is literally a
concatenation-homomorphism `foldr` over the weak-form term list (`book/src/L1/fe_assemble.md:60-61`),
the natural L4 `assemble`-fold combinator, the **direct structural sibling of `solve_family`'s
concatenation-homomorphism map and `fold_solve`'s schedule-split fold** (the same §3.7 `iterate_while`
family). Its opaque per-element libCEED quadrature leaf `A(space, ·)` rises as a black-box-kernel
`readonly` L4 input — the SAME opaque-leaf-wrapping pattern `eigsolve` (`eigen_iterate`) and
`fold_solve` (`time_step_op`) already use. `assemble_frequency_operator` ALREADY rises through the
existing `linear_combination` operand-category axis (its L2 dep is firm) — so it is **L4-reachable
today** with no new vocabulary, only an operand-category propagation. The remaining six split into two
opaque-construction-input clusters: the **space-construction inputs** (`fe_space`, `fe_collection`,
`essential_dofs` — opaque typed construction inputs, NOT combinators) and the **assembly leaves /
post-compositions** (`weak_form_term` the inert fold element-type; `eliminate_essential_bc` /
`eliminate_rhs` the separable post-compositions, which are operator-algebra in already-firm L1/L2
vocabulary). The fan-out ranking puts `fe_assemble` (the combinator) first, `assemble_frequency_operator`
(the cheap propagation) second, the post-compositions third, the construction-inputs last.

## Observation kind

**Coverage gap** — the FE-assembly + FE-space cohort (8 firm L1 operators, the entire in-scope
FE-assembly/FE-space feature surface) has **ZERO presence above L1**. Under directive 1 (L4 is the
outward backend-lowering target; must be complete over the in-scope feature set) this is a coverage gap
at the L4 layer, not merely a missing L2 mirror.

**Anti-mirror guard honored (load-bearing):** the existing NO-L2 warrants (`fe_assemble` c063,
`weak_form_term`, `L2/fe_assemble`) bar only the L1→L2 **rectangular MIRROR** — a degenerate
identity-in-named-terms L2 row. They do **NOT** close the upward-to-L4 question. The L4 `assemble`-fold
is NOT a mirror of L1 `fe_assemble`: it is the combinator-as-entry at the calculus layer with the
opaque per-term map lifted to a typed `readonly` input and the term list lifted to the calculus's list
type — exactly the relationship `solve_family` (L4 combinator) has to `ksp_solve` (the mapped cap), not
the relationship a mirror row has to its parent. This survey reads "no L2 mirror" as "the L1→L2 rung is
legitimately identity-skip (cycle-012 non-adjacent in-line rotation convention)," NOT as "upward climb
done."

## Specific finding

### (i) Three-way classification of the 8 cohort members (directive-2 judgment, not just "does it decompose")

The directive-2 test is **judgment about abstraction value**, not mechanical decomposability. Three
dispositions: **black-box-rises** (no decomposition + clean surface → rises as opaque-surface
primitive); **named-abstraction-keep-and-rise** (decomposes BUT is literature-standard AND aids
downstream algorithm simplification → kept as a named verb, rises, kernel tied below);
**accelerated-stopped-low** (decomposes + solely-for-speed + no abstraction value → stopped low,
combinator rises instead). I add a fourth disposition that the cohort forces and that the directive's
own examples (`fe_space` as opaque construction input) imply: **opaque-construction-input** — an entry
that constructs a typed value consumed `readonly` downstream, neither a combinator nor an accelerated
kernel; it rises (or not) as a typed L4 INPUT, not as L4 vocabulary.

| # | Member | L1 status | Decomposes? | Three-way disposition | L4 destination |
|---|---|---|---|---|---|
| 1 | `fe_assemble` | firm | YES — `foldr (\t acc -> A(space,t) + acc) zero terms` (`fe_assemble.md:61`) | **named-abstraction-keep-and-rise** — the fold is literature-standard FE assembly AND the combinator simplifies every downstream solver-K build (it is the `K`-source for `ksp_solve`/`eigsolve`/`assemble_frequency_operator`). The combinator rises; the per-term map `A` is the black-box leaf tied below. | **RISES as the L4 `assemble`-fold combinator** (NEW L4 vocabulary). |
| 2 | `A(space, ·)` (the per-term libCEED quadrature leaf — sub-component of #1, filed `obstruction (opaque-library-ownership)` at `L1-L0/fe-assemble-libceed-boundary-obstruction`) | obstruction (opaque-library-ownership) | NO — kernel body is libCEED-owned (`integ->Assemble`, `bilinearform.cpp:75-76` / `:95-96`; `CeedOperatorFullAssemble`, `libceed/operator.cpp:455-523`) | **black-box-rises** — clean surface (`WeakFormTerm × FiniteElementSpace → LinearOperator[N,N]`), non-decomposable, library-owned. The POSITIVE reframe of the opaque-library obstruction (directive 2 disposition 1). | **RISES as a black-box-kernel `readonly` L4 input** to the `assemble`-fold (the SAME pattern `eigsolve`/`fold_solve` use for `eigen_iterate`/`time_step_op`). |
| 3 | `assemble_frequency_operator` | firm | YES — already re-expressed THROUGH `linear_combination` operand-category axis (`assemble_frequency_operator.md:43-49`) | **named-abstraction-keep-and-rise (already in flight)** — it is the operator-operand specialization of the firm `linear_combination` fold; rises through that combinator, NOT as a new fold. | **RISES through the existing `linear_combination` L4 reach** (operand-category propagation; cheapest L4 landing — see (iii)). |
| 4 | `weak_form_term` | firm | NO — inert `(coefficient, diff_op)` pair constructor (`weak_form_term.md:60`) | **opaque-construction-input** — inert data, the element-type the `assemble`-fold quantifies over; "specification of WHICH contribution," not an operation (`weak_form_term.md:25-31`). No abstraction value as a standalone L4 verb (the fold reads it opaquely). | **RISES as the L4 element-type of the `assemble`-fold's list** (a typed input/data declaration, NOT a combinator). |
| 5 | `eliminate_essential_bc` | firm | YES — block-decomposition `K ↦ P_F K P_F (+ I_E)` on free/essential partition (`eliminate_essential_bc.md:80-84`) | **named-abstraction-keep-and-rise** — a separable post-composition in operator-algebra vocabulary (free-block projection + operator addition); literature-standard (Dirichlet BC elimination); aids downstream (the solve-side `DIAG_ONE` convention). Decomposes but is a named verb, not solely-for-speed. | **RISES as an L4 post-composition operator** (operator-algebra; sits AFTER the `assemble`-fold). |
| 6 | `eliminate_rhs` | firm | YES — `apply_linop` + `axpy` + `set_essential` pin (`eliminate_rhs.md:54-57`) | **named-abstraction-keep-and-rise** — the inhomogeneous-Dirichlet RHS lift; a separable post-composition entirely in firm L1 spine vocabulary (`apply_linop`/`axpy`/`set_essential`); literature-standard; aids the solve. Decomposes into firm primitives but is a named verb. | **RISES as an L4 post-composition operator** (composed from already-L4-reachable primitives — see caveat on `apply_linop`/`axpy` L4 presence). |
| 7 | `fe_space` | firm | NO at L1 (the dof/numbering/prolongation internals are MFEM-owned-read-as-given, `fe_space.md:92-107`) | **opaque-construction-input** — the typed `(mesh, collection) → FiniteElementSpace[N]` construction; the shared substrate consumed `readonly` by every assembly. The directive's OWN named example of an opaque construction input. | **RISES as an opaque typed L4 construction INPUT** (`FiniteElementSpace[N]` defines the axis `N`; not a combinator). |
| 8 | `fe_collection` | firm | YES (a bounded enumeration loop + `std::reverse`, `fe_collection.md:28-33`) — BUT the decomposition is a deterministic schedule, not an algorithm | **opaque-construction-input** (with a schedule-loop caveat) — produces the `[FECollection]` list `fe_space` consumes one-per-level. The p-multigrid order schedule. Its loop is a finite deterministic enumeration with no convergence/iteration semantics; the schedule could be seen as a degenerate `fold`, but it carries no cross-pipeline-general combinator value (single producer, single consumer). | **RISES as an opaque typed L4 construction INPUT** (the `[FECollection]` schedule; NOT a combinator — see (iii) caveat). |
| — | `essential_dofs` | firm | partial — Palace-authored head (`AttrToMarker`) + MFEM-opaque tail (`GetEssentialTrueDofs`) (`essential_dofs.md:39-58`) | **opaque-construction-input** — constructs the `DofSet[N]` that `eliminate_essential_bc`/`eliminate_rhs` consume opaquely. The marker construction is a join-semilattice homomorphism (a small in-layer structure) but not an L4 combinator. | **RISES as an opaque typed L4 construction INPUT** (`DofSet[N]`; the marker-union law is an in-layer note, not L4 vocabulary). |

**Classification summary:** 1 black-box-rises (`A`, the libCEED leaf), 3 named-abstraction-keep-and-rise
(`fe_assemble`, `eliminate_essential_bc`, `eliminate_rhs`; + `assemble_frequency_operator` already in
flight through `linear_combination`), 4 opaque-construction-inputs (`weak_form_term`, `fe_space`,
`fe_collection`, `essential_dofs`). **Zero accelerated-stopped-low** in this cohort — the PA/FA
performance dual is absorbed INSIDE `fe_assemble`'s assembly-representation variant axis
(`fe_assemble.md:107-110`, the `pa_order_threshold` selector is "a performance selector, not an
algebraic distinction"), so the speed trick never surfaces as a separate stoppable entry; it is already
collapsed.

### (ii) The L4 `assemble`-fold combinator shape + the black-box quadrature leaf

`fe_assemble` is the natural L4 `assemble`-fold combinator. The L1 entry already states it as a
concatenation-homomorphism `foldr`:

```text
fe_assemble(space, terms) = foldr (\t acc -> A(space, t) + acc) zero terms
                          = Σ_{t ∈ terms} A(space, t)        (fe_assemble.md:60-62)
```

This is **structurally the same family** as the two firm solver-driven L4 combinators — and the
`disciplined-cross-pipeline-combinator-mining-gate` skill (owners: combinator-miner,
cross-layer-cross-cutter) is the procedure that licenses the L4 landing:

- **Gate step 1 (≥2 positive witnesses, structurally identical at the load-bearing shape):**
  CLEARED. The `BilinearForm`-fold is witnessed across pipelines differing ONLY in the integrator slot
  (a leaf difference, not structural): electrostatic `(ε, ∇)` (`laplaceoperator.cpp:191-192`),
  magnetostatic `(μ⁻¹, ∇×)` (`curlcurloperator.cpp:179-181`), mass `(Q, I)`
  (`spaceoperator.cpp:278`). The assemble-fold skeleton (iterate term list → build one sub-op per term
  → accumulate into the composite → finalize) is the structure; the integrator is the leaf. Codemap-
  confirmed on disk this cycle: `integ->Assemble(...)` domain branch `bilinearform.cpp:75-76` with
  `op->AddSubOperator(sub_op)` `:77`; boundary branch `:95-96` / `:97`; `op->Finalize()` `:104`;
  `PartialAssemble` close `:107`.
- **Gate step 2 (classify every break-witness as a SCOPE BOUNDARY):** No structural break-witness
  inside the assemble cohort — the domain/boundary two-list split is a single concatenated term list at
  L1 (the concatenation-homomorphism law, `fe_assemble.md:125-130`), NOT a break. The PA/FA
  representation dual is absorbed (variant axis), NOT a scope boundary.
- **Gate step 3 (name unprobed pipelines with the fold-vs-map flag):** the `assemble`-fold is a
  **fold producing a sum** whose per-element steps are **independent and commutative** (term-position
  commutativity, `fe_assemble.md:136-142`) — so it is closer to a `map`-then-reduce than a state-threaded
  fold; there is NO cross-term coupling (`fe_assemble.md:96-99`). This is a load-bearing distinction
  from `fold_solve` (whose carry-threading forbids reorder): the `assemble`-fold's concatenation
  homomorphism HOLDS (the algebraic structure `solve_family` has, not the one `fold_solve` has). No
  over-unification risk: it does not get folded into `fold_solve`.
- **Gate step 4 (replace-and-propagate; pick + justify the layer):** the combinator is the L4 entry;
  the per-pipeline K-builds (electrostatic/magnetostatic/mass) become specialization notes
  re-expressing THROUGH it (differing only in the term-list content), exactly the
  `solve_family`-combinator-as-entry model. **Layer choice: L4 vocabulary** — it is a calculus-level
  combinator (a list-homomorphism over an immutable list, the strawman's list type), one tier of the
  same family tree as `iterate_while` / `solve_family` / `fold_solve`.

**The opaque per-element libCEED quadrature leaf `A(space, ·)` as a black-box-kernel `readonly` L4
input.** The per-term assembly map `A` (element-local restriction + basis-apply + quadrature
contraction → one `LinearOperator[N,N]` contribution) is libCEED-owned. Codemap-confirmed on disk: the
kernel boundary is `integ->Assemble(...)` (`bilinearform.cpp:75-76` domain / `:95-96` boundary) building
one `CeedOperator` sub-op, and the materialization is `CeedOperatorFullAssemble`
(`libceed/operator.cpp:455-523`, the COO→CSR assembly). This is filed `obstruction
(opaque-library-ownership)` at `L1-L0/fe-assemble-libceed-boundary-obstruction` (cycle-055). The
**positive reframe** (directive 2, disposition 1): at L4 this is NOT an obstruction — it is a
**black-box kernel rising to L4 as an opaque-surface primitive**, a `readonly` typed input the
`assemble`-fold quantifies over. The shape:

```text
-- L4 assemble-fold combinator (sketch; authoritative form is the c068 harvester's)
assemble :: FiniteElementSpace[N] -> [WeakFormTerm] -> LinearOperator[N, N]
assemble space terms = foldr (\t acc -> assemble_term space t `op_add` acc) op_zero terms

-- the black-box quadrature kernel — opaque readonly L4 input (libCEED-owned), the
-- direct analog of eigsolve's eigen_iterate and fold_solve's time_step_op:
assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinearOperator[N, N]   -- readonly, opaque
```

This is the **identical opaque-leaf-wrapping pattern** the firm L4 cohort already uses: `eigsolve`
names `eigen_iterate` by role and marks the `sequential-obstruction` without rendering a loop Palace
doesn't author (`L4/index.md:39`); `fold_solve` threads `time_step_op` as one opaque per-step operator
(`L4/index.md:40,83`). `assemble`'s `assemble_term` is the same: a role-named opaque kernel input. The
black-box leaf RISES (clean surface, non-local, library-owned), and the combinator wrapping it RISES —
both per directive 2.

### (iii) Which members rise as L4 vocabulary vs opaque construction inputs vs identity-skip rungs

**Rises as NEW L4 combinator vocabulary (1):**
- `fe_assemble` → the `assemble`-fold combinator (the only genuinely-new L4 calculus contribution in
  the cohort).

**Rises through EXISTING L4 vocabulary (1; cheapest landing):**
- `assemble_frequency_operator` → already the operator-operand specialization of `linear_combination`
  (`assemble_frequency_operator.md:18,43-49`; its L2 dep `book/src/L2/linear_combination.md` is firm).
  Reaching L4 is an **operand-category propagation** onto the existing `linear_combination` reach, NOT a
  new entry. **Caveat: is `linear_combination` itself at L4?** It is firm at L2/L3
  (`assemble_frequency_operator.md:148-149`) but `L4/index.md:66` lists the BLAS-1 cohort as
  no-L4-by-design. Per the sub-observation below, the `linear_combination` COMBINATOR (as opposed to the
  BLAS-1 leaves) is exactly the kind of thing that DOES rise to L4 under directive 2 — so
  `assemble_frequency_operator`'s L4 reach is gated on `linear_combination` rising to L4 (see
  sub-observation).

**Rise as L4 post-composition operators (2; operator-algebra, after the assemble-fold):**
- `eliminate_essential_bc` → free-block projection `K ↦ P_F K P_F (+ I_E)`; operator-algebra vocabulary.
- `eliminate_rhs` → `apply_linop` + `axpy` + `set_essential` pin. **Caveat: are `apply_linop`/`axpy` at
  L4?** They are firm at L1; `apply_linop` appears as an L4 concept reference but is not a standalone L4
  combinator chapter, and `axpy` is in the BLAS-1 no-L4-by-design cohort. `eliminate_rhs`'s L4 form is
  thin (a 3-step composition); its L4 landing is gated on whether the operator-action / axpy primitives
  it composes are L4-reachable. This is the weakest L4-rise case in the cohort (it may legitimately be
  an L4 post-composition expressed in terms of primitives that themselves stay lower — an identity-skip
  on the primitives, a real entry on the composition).

**Rise as opaque typed L4 construction INPUTS (4; NOT combinators):**
- `fe_space` → `FiniteElementSpace[N]` (the axis-defining substrate; the directive's named example).
- `fe_collection` → `[FECollection]` (the p-multigrid order schedule list).
- `essential_dofs` → `DofSet[N]` (the Dirichlet true-dof set).
- `weak_form_term` → `WeakFormTerm` (the inert element-type of the `assemble`-fold's list).

  These four are typed VALUES the L4 forms quantify over `readonly` — the `state-stratification`
  `OpParams`/`readonly` discipline (`L4/index.md:24`) is the existing L4 home for exactly this
  ("variant selectors absorbed at construction into `OpParams` ... `readonly`"). They do NOT each need a
  combinator chapter; they need typed declarations in the `assemble`-fold's signature + the construction
  context. Whether each gets a thin L4 input-declaration chapter or is absorbed into the `assemble`
  entry's shape contract is a c068 harvester judgment — but **none is L4 vocabulary in the combinator
  sense.**

**Intermediate L2/L3 identity-skip (cycle-012 non-adjacent in-line rotation convention):** the cohort's
L1→L2→L3→L4 climb does NOT require populating every intermediate rung. `fe_assemble` has a NO-L2 warrant
(c063) — the L1→L2 rung is legitimately identity-skip (a degenerate L2 mirror would be the
anti-mirror smell). The destination is L4 regardless; the intermediate L2/L3 rungs may be in-line
non-adjacent identity annotations (the L3→L1 inline-identity convention, `friction-ledger
l3-l1-inline-identity-rotation-convention`), NOT mandatory mirror entries. This is the precise reading
of directive 1's anti-mirror note: "no L2 mirror" ≠ "upward climb done"; it means the L2 rung is
identity and the L4 rung is still owed.

### (iv) Fan-out-ranked per-member L4 dispatches for c068

Ranked by fan-out impact (`|concepts| × |downstream-reuse| × 1/cost`), highest first:

1. **`fe_assemble` → L4 `assemble`-fold combinator** (HIGHEST fan-out; the frontier opener).
   Fan-out: it is the `K`-source for EVERY solver pipeline (the entire in-scope FE feature surface tops
   out here); it is genuinely-new L4 calculus vocabulary (the assemble-fold sibling of
   `solve_family`/`fold_solve`); it pulls the black-box `assemble_term` leaf up as a `readonly` input
   (positive reframe of the libCEED obstruction) and the `WeakFormTerm` element-type with it. Cost:
   moderate (a harvester authoring one combinator + the opaque-leaf input, citing the
   mining-gate skill). Dispatch: `harvester` on `book/src/L4/fe_assemble.md` (or `assemble.md`) —
   author the `assemble`-fold combinator + the black-box quadrature leaf as a `readonly` L4 input +
   `WeakFormTerm` as the list element-type; cite `disciplined-cross-pipeline-combinator-mining-gate`
   (4 points cleared above) + `propose-rotation` for the L4>L3 dissolution.

2. **`assemble_frequency_operator` → L4 reach via `linear_combination` operand-category propagation**
   (HIGH fan-out, LOWEST cost). Fan-out: it is the driven-pipeline `map_solve` scope boundary
   (`assemble_frequency_operator.md:24`); reaching L4 also drives `linear_combination` to L4 (which the
   no-L4-by-design sub-observation flags as warranted). Cost: cheap (a propagation onto an existing firm
   combinator, no new fold algebra). Dispatch: `combinator-miner` or `lifter` — propagate the
   `linear_combination` operand-category axis to L4 (gated on / paired with `linear_combination` rising
   to L4 per the sub-observation), landing `assemble_frequency_operator` as the operator-operand driven
   specialization at L4. **Order note:** sequence this AFTER the sub-observation's `linear_combination`
   L4-rise decision (deps: the no-L4-by-design re-examination).

3. **`eliminate_essential_bc` → L4 post-composition operator** (MEDIUM fan-out). Fan-out: every
   solve-side BC application; operator-algebra in existing vocabulary; pairs with #4. Cost: moderate
   (clean block-projection algebra). Dispatch: `harvester` on `book/src/L4/eliminate_essential_bc.md`.

4. **`eliminate_rhs` → L4 post-composition operator** (MEDIUM-LOW fan-out; the weakest rise).
   Fan-out: the inhomogeneous-Dirichlet RHS lift; thin (3-step composition). Cost: low BUT gated on
   `apply_linop`/`axpy` L4-reachability (may legitimately compose lower primitives that stay below L4).
   Dispatch: `harvester` on `book/src/L4/eliminate_rhs.md`, paired with #3 (the two together are the
   full Dirichlet-BC L4 surface); flag the primitive-L4-presence gate.

5. **`fe_space` / `fe_collection` / `essential_dofs` / `weak_form_term` → opaque typed L4 construction
   inputs** (LOWEST fan-out as standalone work; likely absorbed). Fan-out: shared substrate, but as
   `readonly` typed inputs they do NOT each warrant a combinator chapter. Cost: very low if absorbed
   into the `assemble`-fold entry's shape contract + an `OpParams`/`readonly` construction note; higher
   (and lower-value) if each gets a standalone thin chapter. Dispatch: FOLD INTO #1 — the c068
   `harvester` on the `assemble`-fold declares these as the typed inputs in the signature/shape-contract
   rather than dispatching four separate low-fan-out chapters. (`weak_form_term` is the fold's
   element-type and rides #1 directly; the three construction inputs are the assemble-fold's
   `(space, collection-schedule, dof-set)` upstream context.) Surface a c069+ judgment on whether any
   needs a self-standing L4 input-declaration chapter only if a downstream L4 consumer demands a
   navigable home.

## Recommendation

- **Dispatch `harvester` on the L4 `assemble`-fold combinator (`fe_assemble`) as the c068 LEAD** — it
  is the frontier opener, the highest-fan-out item, and the natural sibling of the already-firm
  `solve_family`/`fold_solve` L4 combinators. Author it citing
  `disciplined-cross-pipeline-combinator-mining-gate` (the 4 gate points are cleared in this survey,
  ready to copy) and wrapping the black-box `assemble_term` libCEED leaf as a `readonly` L4 input (the
  `eigsolve`/`fold_solve` opaque-leaf-wrapping precedent). Fold `weak_form_term` + the three
  construction inputs into its signature rather than dispatching them separately.
- **Dispatch the `linear_combination` no-L4-by-design re-examination FIRST (or paired)**, then
  `assemble_frequency_operator`'s L4 reach as a cheap operand-category propagation onto it (rank-2;
  it is L4-reachable today modulo `linear_combination` rising).
- **Queue `eliminate_essential_bc` + `eliminate_rhs` as the paired L4 Dirichlet-BC post-composition
  surface** (ranks 3–4), flagging the `apply_linop`/`axpy` L4-presence gate on `eliminate_rhs`.
- **Defer** standalone L4 chapters for `fe_space`/`fe_collection`/`essential_dofs` — absorb as
  `readonly` typed construction inputs; re-open only if a downstream L4 consumer needs a navigable home.

## Supporting evidence

- L4 absence (verified this cycle): `book/src/L4/` inventory = `chebyshev / eigsolve / fold_solve /
  iterate-while / iterate-while-with-prev / krylov-step / ksp_solve / solve_family / index` — no FE
  entry. (Bash `ls book/src/L4/`.)
- `book/src/L1/fe_assemble.md:60-62` — the `foldr` concatenation-homomorphism (the L4 combinator shape);
  `:125-130` concatenation-homomorphism law; `:136-142` term-position commutativity (the map-not-fold
  independence); `:107-110` PA/FA absorbed (no accelerated-stopped-low entry); `:172-178` + `:266-268`
  the `A` libCEED leaf.
- `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` (cycle-055) — the
  `opaque-library-ownership` filing of `A`, the positive-reframe target.
- Codemap on-disk confirmation (recurrence-6 — direct `Read`/`awk`, NOT `citecheck --anchor`):
  `palace/fem/bilinearform.cpp:75-76` (`integ->Assemble` domain) / `:77` AddSubOperator / `:95-96`
  boundary / `:97` / `:104` Finalize / `:107` PartialAssemble close / `:109-113` FullAssemble;
  `palace/fem/libceed/operator.cpp:455-523` (`CeedOperatorFullAssemble` full span — the hint `:455` is
  the function-open line, confirmed; close brace at `:523`).
- `book/src/L4/index.md:39` (`eigsolve` `eigen_iterate` opaque-leaf marker), `:40,83` (`fold_solve`
  `time_step_op` opaque per-step), `:24` (`OpParams`/`readonly` variant-absorption — the construction-
  input L4 home), `:66` (the 13-of-18 no-L4-by-design claim — the sub-observation target).
- `book/src/L1/assemble_frequency_operator.md:18,43-49,148-149` — the `linear_combination`
  operand-category specialization (the cheap L4-reach path) + firm L2/L3 `linear_combination` deps.
- `book/src/L1/fe_space.md:92-107` (MFEM-owned-read-as-given → opaque construction input),
  `book/src/L1/fe_collection.md:28-33` (schedule loop), `book/src/L1/essential_dofs.md:39-58`
  (Palace-head/MFEM-tail), `book/src/L1/weak_form_term.md:25-31,60` (inert pair element-type),
  `book/src/L1/eliminate_essential_bc.md:80-84` (block projection),
  `book/src/L1/eliminate_rhs.md:54-57` (apply_linop+axpy+pin composition).
- `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md` — the 4-point gate cited for the
  `assemble`-fold L4 landing.

## Sub-observation: re-examine the "13-of-18 no-L4-by-design" claim (directive 1; survey sub-finding, NOT a c067 landing)

`book/src/L4/index.md:66` asserts the 13-of-18 BLAS-1 / elementwise / smoother L3 ops remain
no-L4-by-design ("their L4 form would add no calculus beyond their firm L3 rendering"). Under directive
2 (black-box vs accelerated kernels — judgment by abstraction value) and the project memory
`project_blackbox_vs_accelerated_kernels`, this claim needs **per-case** re-examination, NOT blanket
acceptance:

- **The COMBINATORS in that cohort DO rise to L4.** `linear_combination` / `inner_product` are
  combinators (memory disposition 2: "Combinators (linear_combination/inner_product) must reach L4
  regardless"). The blanket "no-L4-by-design" line predates directive 2 and over-claims by lumping the
  combinators with the leaves. **This directly gates rank-2 above** (`assemble_frequency_operator`'s L4
  reach rides `linear_combination` rising to L4).
- **The KEPT NAMED ABSTRACTIONS rise.** `dot` / `nrm2` are literature-standard named abstractions that
  decompose but aid downstream algorithm simplification (memory disposition 2) — they rise to L4 as
  named verbs with the kernel tied below, NOT stopped low.
- **The PURE ACCELERATED leaves legitimately stay low.** The per-case `axpy`-family fused special cases
  (memory disposition 3: only-for-speed, no abstraction value) are correctly no-L4 — the combinator
  (`linear_combination`) rises in their place.

So the `L4/index.md:66` claim is **partially wrong as stated**: it is correct for the pure-accelerated
leaves but incorrect for the combinators and the kept named abstractions in the same 13-of-18 set.
**Recommendation (survey sub-finding, route to c068+ NOT c067):** dispatch a `combinator-miner` or
`layer-intro-author` pass to (a) re-classify the 13-of-18 set per the directive-2 three-way test, (b)
rise `linear_combination` / `inner_product` (and `dot` / `nrm2`) to L4, (c) correct the `L4/index.md:66`
blanket assertion to the per-case form. This unblocks rank-2 and is itself MEDIUM-HIGH fan-out (it is
the BLAS-1 combinator surface that the whole solver test-load reuses). Pair-or-precede with rank-2.

## Open questions / caveats

- **`fe_assemble` map-vs-fold framing.** The L1 entry calls it a `foldr`, but its per-element steps are
  independent and commutative (term-position commutativity) — algebraically it is a `map`-then-reduce
  (concatenation-homomorphism HOLDS), unlike `fold_solve` (carry-threaded, homomorphism does NOT hold).
  The c068 harvester should land it as the **homomorphic** fold (the `solve_family` algebraic shape),
  NOT conflate it with `fold_solve`'s sequential carry-threading. Flagged so the mining-gate step-3
  over-unification check is honored at landing.
- **`assemble_term` (`A`) opaque-leaf classification at L4.** The L1 obstruction filing is
  `opaque-library-ownership`. The positive L4 reframe (black-box-rises) does NOT change the L0-side
  obstruction — it adds an L4-side opaque-input view. The c068 harvester should cite BOTH (the L4
  black-box input AND the L1>L0 obstruction it lifts), as `eigsolve` does for `eigen_iterate`.
- **`eliminate_rhs` L4 thinness gate.** Its L4 form composes `apply_linop` + `axpy` + `set_essential` —
  primitives that may themselves stay below L4 (the BLAS-1 no-L4 question). If they don't rise,
  `eliminate_rhs`'s L4 entry is a thin composition over lower primitives (an identity-skip on the
  primitives, a real entry on the composition). Verify primitive-L4-presence before landing — this is
  the case most at risk of being a degenerate L4 mirror. (Routes through the sub-observation: if
  `inner_product`/`apply_linop` rise, this clears.)
- **Construction-input chapter-vs-absorb judgment.** Whether `fe_space`/`fe_collection`/
  `essential_dofs` get standalone thin L4 input-declaration chapters or are absorbed into the
  `assemble`-fold's shape contract is a c068 harvester call (this survey recommends absorb; re-open per
  downstream-consumer demand). The `state-stratification` `OpParams`/`readonly` discipline is the
  existing L4 home either way.
- **`fe_collection` schedule-as-degenerate-fold.** Its bounded enumeration loop + `std::reverse` COULD
  be read as a degenerate fold, but it is single-producer/single-consumer with no cross-pipeline
  generality, so it does NOT clear the mining-gate ≥2-witness bar as a combinator — classified as
  opaque construction input, not vocabulary. Flagged in case a future pipeline forces it.
- **L1>L0 lowering re-anchor residue (out of scope here, noted for completeness).** Several cohort
  members carry forward-referenced / rough-in L1>L0 themes (`fe-operator-assemble-mutation-rotation`
  rough-in; `eliminate-rhs-mutation-rotation` not-yet-authored). These are DOWNWARD residue, orthogonal
  to the upward L4 climb this survey scopes; named so they are not mistaken for L4 gaps.
- **Survey authored nothing to `book/`** (observation-only dispatch per spec). The per-member L4
  landings open c068 from this ranking; the `linear_combination` no-L4-by-design re-examination is the
  paired unblocker for rank-2.
