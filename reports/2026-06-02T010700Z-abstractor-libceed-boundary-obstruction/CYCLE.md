---
agent: abstractor
invoked_at: 2026-06-02T010700Z
scope: L1>L0 theme sketch — fe-assemble-libceed-boundary-obstruction (D5, cycle-055, batch-17)
status: integrated
integrated_at: 2026-06-02T034000Z
integration_commit: e9bbbbf9fcee8786ad94305a482f6835d2e0f40b
integration_notes: "D5 cycle-055. Applied clean — new book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md (obstruction (opaque-library-ownership), settles the c053 libCEED-boundary OQ per batch-16 meta ratification; libCEED owns the element-local quadrature kernel + COO materialization, Palace owns fold/dispatch/shuffle/BC-elimination; fe_assemble STAYS firm) + L1-L0/index dep-map row + SUMMARY. Repairer widened bilinearform.cpp:67-70→64-70. L1>L0 +1 obstruction annotation."
inputs:
  - reference/palace/palace/fem/bilinearform.cpp:64-70 (leaf CeedOperator inputs: CeedElemRestriction trial/test_restr + CeedBasis trial/test_basis built by integ->Assemble)
  - reference/palace/palace/fem/bilinearform.cpp:75 (integ->Assemble call)
  - reference/palace/palace/fem/bilinearform.cpp:77 (AddSubOperator integrator-fold — Palace-owned)
  - reference/palace/palace/fem/libceed/operator.cpp:455-490 (CeedOperatorFullAssemble: COO->CSR materialization)
  - reference/palace/palace/fem/integrator.hpp:58-61 (BilinearFormIntegrator::Assemble pure-virtual leaf signature)
  - book/src/L1-L0/triangular-solve-obstruction.md (HYPRE/SLEPc opaque-library-ownership precedent)
  - book/src/L1-L0/fe-operator-assemble-mutation-rotation.md (the rough-in thread-opener whose libCEED-boundary OQ this settles)
  - book/src/L1/fe_assemble.md (firm c054 — stays firm; this annotation documents the boundary, not the fold)
---

# CYCLE: L1>L0 theme sketch — fe-assemble-libceed-boundary-obstruction

## Summary

The FE-assembly thread-opener (`fe-operator-assemble-mutation-rotation.md`, rough-in,
cycle-053) left the libCEED matrix-materialization step logged as an **open question** —
"transitive-firm vs opaque-library-ownership vs tensor-contraction-respine." The batch-16
meta-phase RATIFIED the classification: it is **`opaque-library-ownership`**, a deeper-boundary
sibling of the HYPRE-relaxation / SLEPc-EPS / external-direct-solver precedent recorded in
`triangular-solve-obstruction.md`. This dispatch authors the thin L1>L0 annotation that settles
that OQ. The boundary is **precise and shallow**: only the *innermost element-local quadrature
kernel* (built by `integ->Assemble` into a `CeedOperator` at `bilinearform.cpp:67-70`/`:75`) and
the COO→CSR matrix *materialization* (`CeedOperatorFullAssemble` /`CeedOperatorAssembleCOO` at
`libceed/operator.cpp:455-490`) are libCEED-owned. **Palace OWNS the orchestration around it** —
the integrator-fold `AddSubOperator` (`bilinearform.cpp:77`), the PA-vs-FA dispatch
(`UseFullAssembly` `bilinearform.cpp:118-132`), and BC-elimination. Critically: the firm
`fe_assemble` operator (cycle-054) **stays FIRM** — its fold `K = Σ_i A(term_i)` quantifies over
the per-term contribution `A(term_i)` *opaquely*; the firmness of the fold is **independent** of
whether `A(·)` is Palace-authored or library-owned. This annotation documents the *boundary*; it
does **not** downgrade the fold. This is documentation so future producers (across all 5 solver
pipelines, all of which assemble FE operators through the same `BilinearForm`/`CeedOperator`
machinery) do not re-localize the boundary.

## Proposed changes

```new:book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md
---
layer: L1-L0
theme: fe-assemble-libceed-boundary-obstruction
status: obstruction
sub_kind: opaque-library-ownership
lowers: (boundary annotation — the per-term contribution A(term_i) inside the L1 fe_assemble fold)
l0_anchor: palace/fem/bilinearform.cpp:64-70,75,77; palace/fem/libceed/operator.cpp:455-490; palace/fem/integrator.hpp:58-61
justification_kind: obstruction
---

# fe-assemble-libceed-boundary-obstruction

A thin L1>L0 **boundary annotation** documenting that the innermost element-local
quadrature kernel of FE assembly — the per-term contribution `A(term_i)` summed by the
firm [`fe_assemble`](../L1/fe_assemble.md) fold — is **library-owned (libCEED)**, not
Palace-authored. Palace owns the *orchestration* (the integrator-fold, the PA-vs-FA
dispatch, BC-elimination); only the leaf kernel and its COO→CSR materialization cross the
library boundary. This is a **deeper-boundary sibling** of the HYPRE-relaxation /
SLEPc-EPS / external-direct-solver `opaque-library-ownership` obstruction recorded in
[`triangular-solve-obstruction`](./triangular-solve-obstruction.md).

This annotation **settles the open question** logged by the FE-assembly thread-opener
[`fe-operator-assemble-mutation-rotation`](./fe-operator-assemble-mutation-rotation.md)
§"libCEED boundary" — "transitive-firm vs opaque-library-ownership vs
tensor-contraction-respine" — RATIFIED by the batch-16 meta-phase as
**`opaque-library-ownership`**.

## Status

`obstruction (opaque-library-ownership)` — the mandatory sub-kind tag (per CLAUDE.md
§Methodology-invariants "Obstruction themes have two sub-kinds"). The entire callable that
produces the element-local quadrature contribution lives **outside Palace** (in libCEED),
so the boundary is *structural ownership*, not unimplementation. Promotion route: **none**
in the conventional sense — the theme stays obstruction unless Palace re-architects its
consumption of libCEED (it will not; libCEED is the matrix-free quadrature engine Palace is
built on). The theme's value is *documenting the boundary precisely* + cataloguing the
anchors so future producers across the 5 solver pipelines do not re-localize it. This
matches the [`triangular-solve-obstruction`](./triangular-solve-obstruction.md) routing
(HYPRE relax-type enums + external direct-solver wrappers as the prior opaque-library-owned
sites).

**`fe_assemble` stays FIRM — this annotation does NOT downgrade the fold.** The firm
[`fe_assemble`](../L1/fe_assemble.md) operator (cycle-054) expresses FE assembly as the fold

    K = fe_assemble(space, [term_0, term_1, ...]) = Σ_i A(term_i)

where `A(·)` is the element-local→global assembly of one weak-form term. The fold
quantifies over `A(term_i)` **opaquely**: it is a sum of per-term contributions, and the
fold's structure (the term list, the summation, the separable BC-elimination
post-composition) is firm regardless of whether each `A(term_i)` is computed by a
Palace-authored kernel or a library-owned one. The boundary documented here sits **strictly
below** the fold — at the leaf `A(·)`. The firmness of `fe_assemble` is therefore
**independent** of this classification: this theme records *where the leaf comes from*, it
does not assert anything about the fold that the firm operator already establishes. (This is
the same structural relationship that lets `ksp_solve` stay firm while the inner MINRES/
BiCGStab Krylov kernels are obstruction-documented, and that lets the `eigsolve` per-step
body lift while the SLEPc EPS iteration loop is opaque-library-owned.)

## L1 form (LHS)

The L1 form is **not empty** here (unlike `triangular-solve-obstruction`, which has no
positive Palace site at all): the L1 fold *exists and is firm*. What this theme annotates is
a **sub-term inside the firm fold**. From [`fe_assemble`](../L1/fe_assemble.md):

    K = fe_assemble(space, terms) = Σ_{i} A(term_i)
        -- K :: LinearOperator[N, N]      (N = space.GetTrueVSize())
        -- term_i :: WeakFormTerm          (a coefficient-weighted differential bilinear form)
        -- A(·) :: WeakFormTerm -> LinearOperator[N, N]
        --        the element-local quadrature + element->global assembly of ONE term

The **boundary is on `A(·)`**. The L1 fold treats `A(term_i)` as an opaque per-term
contribution; the global operator is their sum. There is no L1 form *proposed* for the
interior of `A(·)` — that interior is the libCEED element-local quadrature kernel, which is
out of scope (per CLAUDE.md §Target-system, "cite Palace source, not vendored upstream").

## L0 form (RHS)

Palace's FE-assembly machinery splits cleanly into a **Palace-owned orchestration shell**
and a **libCEED-owned leaf**. The boundary runs through the body of `BilinearForm::Assemble`.

### Palace-owned (orchestration) — the fold, the dispatch, BC-elimination

The integrator-fold is Palace-authored. `BilinearForm::Assemble` loops over the domain
integrators and **accumulates** each leaf sub-operator into a composite `ceed::Operator`:

    // bilinearform.cpp:71-78  (the Palace-owned integrator-fold)
    for (const auto &integ : domain_integs)
    {
      CeedOperator sub_op;
      integ->SetMapTypes(trial_map_type, test_map_type);
      integ->Assemble(ceed, trial_restr, test_restr, trial_basis, test_basis,   // :75 leaf call
                      data.geom_data, data.geom_data_restr, &sub_op);
      op->AddSubOperator(sub_op);  // :77  Sub-operator owned by ceed::Operator — PALACE-OWNED FOLD
    }

`AddSubOperator` at `bilinearform.cpp:77` is the L0 realization of the L1 fold's `Σ_i`: the
global operator is the composite of the per-term sub-operators. This is **Palace's code**.
The PA-vs-FA dispatch is also Palace-owned (`UseFullAssembly` at `bilinearform.cpp:118-132`
chooses partial-assembly matrix-free vs full-assembly materialized based on the FE order
threshold), as is BC-elimination (the separable post-composition `eliminate_essential_bc` /
`eliminate_rhs` documented in the sibling thread-opener).

### libCEED-owned (leaf) — the element-local quadrature kernel

The per-term leaf `A(term_i)` is built by `integ->Assemble`, a **pure-virtual** dispatched
into a `CeedOperator`:

    // integrator.hpp:58-61  (the leaf-kernel signature — pure virtual, builds a CeedOperator)
    virtual void Assemble(Ceed ceed, CeedElemRestriction trial_restr,
                          CeedElemRestriction test_restr, CeedBasis trial_basis,
                          CeedBasis test_basis, CeedVector geom_data,
                          CeedElemRestriction geom_data_restr, CeedOperator *op) const = 0;

The constructed `CeedOperator` (`bilinearform.cpp:64-70` builds the `CeedElemRestriction` /
`CeedBasis` inputs — `trial_restr`/`test_restr` at 64/66, `trial_basis`/`test_basis` at
68/69; `:75` invokes the kernel) **encapsulates the element-local
quadrature contraction** — basis evaluation at quadrature points, the geometric-factor /
coefficient weighting, and the contract-back to element dofs. That contraction runs **inside
libCEED**; Palace supplies the restriction + basis + geometry-factor inputs and receives an
opaque `CeedOperator`. Palace authors **no** element-local quadrature loop.

### libCEED-owned (materialization) — COO→CSR

When full assembly is selected, the materialization of the composite `CeedOperator` into a
sparse CSR matrix is **also libCEED-owned**. `CeedOperatorFullAssemble` extracts the assembled
entries in COO format via the libCEED API and converts to CSR:

    // libceed/operator.cpp:455-490  (COO->CSR materialization — libCEED-owned extraction)
    std::unique_ptr<hypre::HypreCSRMatrix> CeedOperatorFullAssemble(const Operator &op, ...)
    {
      ...
      CeedOperatorAssembleCOO(ceed, op[id], skip_zeros, &nnz, &rows, &cols, &vals, &mem);  // :483
      ...
      loc_mat[id] =
          OperatorCOOtoCSR(ceed, op.Height(), op.Width(), nnz, rows, cols, vals, mem, set); // :487-488
    }

`CeedOperatorAssembleCOO` (`:483`) is the libCEED API call that extracts the assembled COO
triples — the actual numerical assembly is performed *inside libCEED*. `OperatorCOOtoCSR`
(`:487-488`) is a Palace-side reshuffle of the already-assembled triples into CSR layout
(format conversion, not the quadrature contraction). The **numerical materialization** —
evaluating each element's contribution and summing into the global nonzeros — is the
libCEED-owned half; the COO→CSR layout shuffle is the Palace-owned half. The boundary is
the COO output of `CeedOperatorAssembleCOO`: everything that produces those triples is
library-owned; everything that reshapes them is Palace-owned.

## Applicability conditions

The "applicability" of an obstruction is the *boundary of the negative finding* — where it
applies and where it stops:

1. **The element-local quadrature kernel** `A(·)` (basis evaluation at quadrature points,
   geometric-factor weighting, contract-to-dofs) — **libCEED-owned**. Obstruction applies.
   Do not author an L1 operator for the interior of `A(·)`; it is out of scope (vendored
   upstream).
2. **The COO numerical materialization** (`CeedOperatorAssembleCOO`, `libceed/operator.cpp:483`)
   — **libCEED-owned**. Obstruction applies (the numerical assembly is library-internal).
3. **The integrator-fold** `Σ_i` (`AddSubOperator`, `bilinearform.cpp:77`) — **Palace-owned**.
   Obstruction does **not** apply; this is the firm `fe_assemble` fold's L0 home.
4. **The PA-vs-FA dispatch** (`UseFullAssembly`, `bilinearform.cpp:118-132`) — **Palace-owned**.
   Obstruction does not apply; it is a Palace-authored variant axis on the firm fold.
5. **BC-elimination** (`eliminate_essential_bc` / `eliminate_rhs`) — **Palace-owned**.
   Obstruction does not apply; separable post-composition outside the assembly fold.
6. **The COO→CSR layout shuffle** (`OperatorCOOtoCSR`, `libceed/operator.cpp:487-488`) —
   **Palace-owned** format conversion (not the quadrature contraction). Obstruction does not
   apply to the reshuffle; it applies only to the *production* of the COO triples that feed it.

The boundary is **load-bearing for the 5-pipeline scope**: every Palace solver pipeline
(electrostatic / magnetostatic / eigenmode / driven / transient) assembles its FE operators
through this same `BilinearForm` / `CeedOperator` machinery. The boundary is identical across
all five — so this single annotation covers the FE-assembly leaf for **all** pipelines, and
future producers on any pipeline can cite it rather than re-localizing the libCEED boundary.

## Justification kind

`obstruction` (opaque-library-ownership) — **negative-result theme**, claim-free
documentation of a library boundary. The element-local quadrature kernel + COO numerical
materialization are *recognized* (they are the matrix-free FE-assembly leaf) but have **no
Palace-authored L0 form** to lift; the kernel lives entirely inside libCEED, consumed
opaquely by Palace through the `CeedOperator` API. Follows the
[`triangular-solve-obstruction`](./triangular-solve-obstruction.md) (cycle-029)
opaque-library-ownership precedent in routing: the value is documenting the boundary +
cataloguing negative anchors, with **no** promotion route (Palace will not re-architect its
libCEED consumption).

**Structural distinction from the precedents.** Unlike `triangular-solve-obstruction` (where
the L1 form is *empty* — there is no positive Palace site at all), this theme's surrounding
L1 fold **exists and is firm** (`fe_assemble`, c054). The obstruction is a *strict sub-term*
inside a firm fold, not a whole-operator absence. This makes it a **shallower** obstruction
than the triangular-solve case and a closer sibling of the `eigsolve` `partial-obstruction`
(where the per-step body lifts but the iteration loop is library-owned): here the fold lifts
and is firm, but the per-term leaf is library-owned. It is recorded as full `obstruction`
(opaque-library-ownership), not `partial-obstruction`, because the boundary is a clean
ownership split at the leaf, not an un-liftable loop structure inside a partly-lifting
operator — the loop (the `Σ_i` fold) DOES lift cleanly; only the leaf is opaque.

## Speculative L1 operators

**None proposed.** Per CLAUDE.md §Scope, the libCEED-owned element-local quadrature kernel
is not a Palace component to lift — it is vendored upstream ("cite Palace source, not
vendored upstream"). The firm `fe_assemble` fold already provides the L1 vocabulary; this
annotation adds no new operators, it only documents the boundary below the fold's leaf.

## Related

- [`fe-operator-assemble-mutation-rotation`](./fe-operator-assemble-mutation-rotation.md)
  (rough-in, cycle-053 thread-opener) — the sibling theme that maps the full FE-assembly
  surface and **logged the libCEED boundary as an OQ** (§"libCEED boundary":
  "transitive-firm vs opaque-library-ownership vs tensor-contraction-respine"). **This
  annotation settles that OQ** as `opaque-library-ownership`. The two cross-link: the
  thread-opener is the surface map; this annotation is the boundary classification. (D6 of
  this cycle re-anchors the thread-opener to the firm `fe_assemble` LHS — a distinct,
  parallel-safe edit; this annotation is a new file.)
- [`fe_assemble`](../L1/fe_assemble.md) (firm, cycle-054) — the L1 fold whose per-term leaf
  this annotation bounds. **Stays firm; not downgraded.**
- [`triangular-solve-obstruction`](./triangular-solve-obstruction.md) (cycle-029) — the
  prior `opaque-library-ownership` obstruction theme (HYPRE GS/SSOR relaxation +
  external direct-solver wrappers). The routing precedent for this sub-kind: document the
  boundary, catalogue the negative anchors, no promotion route.

## Verified-against

L0 evidence (a mix of **positive** Palace-owned anchors and **boundary** library-owned
anchors — the positive anchors establish what Palace OWNS; the boundary anchors establish
what is library-owned):

- `palace/fem/bilinearform.cpp:64-70` — boundary: the `CeedElemRestriction` / `CeedBasis`
  inputs Palace supplies to the libCEED leaf kernel (`trial_restr`/`test_restr` at 64/66,
  `trial_basis`/`test_basis` at 68/69); the leaf `CeedOperator` is built from these.
- `palace/fem/bilinearform.cpp:75` — boundary: `integ->Assemble(...)` — the call dispatching
  into the libCEED-owned element-local quadrature kernel (builds `sub_op`).
- `palace/fem/bilinearform.cpp:77` — **Palace-owned**: `op->AddSubOperator(sub_op);` — the
  integrator-fold `Σ_i`; the L0 home of the firm `fe_assemble` fold.
- `palace/fem/integrator.hpp:58-61` — boundary: `BilinearFormIntegrator::Assemble` pure-virtual
  signature — the leaf-kernel contract that produces a `CeedOperator` from restriction/basis/
  geometry inputs.
- `palace/fem/libceed/operator.cpp:455-490` — the `CeedOperatorFullAssemble` function: the
  COO→CSR materialization path.
- `palace/fem/libceed/operator.cpp:483` — boundary: `CeedOperatorAssembleCOO(...)` — the
  libCEED API call performing the numerical COO assembly (library-owned).
- `palace/fem/libceed/operator.cpp:487-488` — **Palace-owned**: `OperatorCOOtoCSR(...)` — the
  Palace-side COO→CSR layout shuffle (format conversion of already-assembled triples).
- `palace/fem/bilinearform.cpp:118-132` — **Palace-owned**: `UseFullAssembly` — the PA-vs-FA
  dispatch (Palace-authored variant axis).

Cross-references (positive):

- `book/src/L1/fe_assemble.md` — the firm fold this annotation bounds (stays firm).
- `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md` — the thread-opener whose
  libCEED-boundary OQ this settles.
- `book/src/L1-L0/triangular-solve-obstruction.md` — the opaque-library-ownership routing
  precedent.

    verified_against:
      - citation: reference/palace/palace/fem/bilinearform.cpp:64-70
        verdict: boundary-anchor
        audited_at: 2026-06-02T010700Z
        note: "CeedElemRestriction trial/test_restr (64/66) + CeedBasis trial/test_basis (68/69) inputs Palace supplies to the libCEED leaf; widened 67-70 to 64-70 to fully cover the named restriction inputs (repairer, D5 critique finding 1); citecheck in-bounds (file 284 lines)."
      - citation: reference/palace/palace/fem/bilinearform.cpp:75
        verdict: boundary-anchor
        audited_at: 2026-06-02T010700Z
        note: "integ->Assemble(...) leaf-kernel dispatch; citecheck --anchor 'integ->Assemble' zero-drift (line 75)."
      - citation: reference/palace/palace/fem/bilinearform.cpp:77
        verdict: positive-palace-owned
        audited_at: 2026-06-02T010700Z
        note: "op->AddSubOperator(sub_op) integrator-fold; citecheck --anchor 'AddSubOperator' zero-drift (line 77). The L0 home of the firm fe_assemble fold's Sigma_i."
      - citation: reference/palace/palace/fem/integrator.hpp:58-61
        verdict: boundary-anchor
        audited_at: 2026-06-02T010700Z
        note: "BilinearFormIntegrator::Assemble pure-virtual leaf-kernel signature (produces CeedOperator); verified line 58 = 'virtual void Assemble(Ceed ceed, CeedElemRestriction trial_restr,'."
      - citation: reference/palace/palace/fem/libceed/operator.cpp:455-490
        verdict: boundary-anchor
        audited_at: 2026-06-02T010700Z
        note: "CeedOperatorFullAssemble COO->CSR materialization function; citecheck --anchor 'CeedOperatorFullAssemble' zero-drift (line 455); in-bounds (file 587 lines)."
      - citation: reference/palace/palace/fem/libceed/operator.cpp:483
        verdict: boundary-anchor
        audited_at: 2026-06-02T010700Z
        note: "CeedOperatorAssembleCOO(...) libCEED API call — numerical COO assembly is library-owned; citecheck --anchor 'CeedOperatorAssembleCOO' zero-drift (line 483)."
      - citation: reference/palace/palace/fem/libceed/operator.cpp:487-488
        verdict: positive-palace-owned
        audited_at: 2026-06-02T010700Z
        note: "OperatorCOOtoCSR(...) Palace-side layout shuffle (format conversion, not the quadrature contraction); citecheck --anchor 'OperatorCOOtoCSR' lands line 488 (assignment spans 487-488)."
      - citation: book/src/L1/fe_assemble.md
        verdict: positive-cross-reference
        audited_at: 2026-06-02T010700Z
        note: "the firm c054 fold this annotation bounds; STAYS FIRM — boundary is a strict sub-term below the fold."
      - citation: book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
        verdict: positive-cross-reference
        audited_at: 2026-06-02T010700Z
        note: "the cycle-053 thread-opener whose libCEED-boundary OQ this annotation settles as opaque-library-ownership."
      - citation: book/src/L1-L0/triangular-solve-obstruction.md
        verdict: positive-cross-reference
        audited_at: 2026-06-02T010700Z
        note: "the opaque-library-ownership sub-kind routing precedent (HYPRE relax + external direct-solver wrappers)."
```

```edit:book/src/L1-L0/index.md
| [bicgstab-iteration](./bicgstab-iteration.md) | (speculative — `bicgstab_step`, …) | (no Palace anchor — `MFEM_ABORT` at `ksp.cpp:53-57`) | obstruction |
| [triangular-solve-obstruction](./triangular-solve-obstruction.md) | (none — general `trsv` has no positive Palace site; firm sibling `L1/back_solve` is small-dense only, NOT a general trsv) | (no Palace anchor — opaque-library-owned: HYPRE GS/SSOR `amg.cpp:19,29` + `ams.cpp:162,173`; external direct-solver wrappers `strumpack.hpp:21`, `superlu.hpp:22`, `mumps.hpp:21`; Palace-native smoothers GS-free `jacobi.hpp:19` + `chebyshev.hpp:23,82`; red-herring block-triangular non-example `blockprecond.hpp:16-29`) | obstruction *(claim-free; resolves `trsv` leaf of OQ `l3-vocabulary-inventory-gap` as resolved-by-obstruction; concrete L0 evidence behind `book/src/L3/index.md:7`)* |
| [fe-assemble-libceed-boundary-obstruction](./fe-assemble-libceed-boundary-obstruction.md) | (boundary annotation on the per-term leaf `A(term_i)` INSIDE the firm `L1/fe_assemble` fold — `fe_assemble` STAYS FIRM, not downgraded) | libCEED-owned leaf: element-local quadrature kernel `integ->Assemble`→`CeedOperator` `bilinearform.cpp:64-70,75` (+ pure-virtual `integrator.hpp:58-61`) + COO numerical materialization `CeedOperatorAssembleCOO` `libceed/operator.cpp:483`; Palace-owned shell: integrator-fold `AddSubOperator` `bilinearform.cpp:77`, PA/FA dispatch `bilinearform.cpp:118-132`, COO→CSR shuffle `libceed/operator.cpp:487-488`, BC-elimination | obstruction *(opaque-library-ownership; deeper-boundary sibling of `triangular-solve-obstruction`; settles the cycle-053 `fe-operator-assemble-mutation-rotation` libCEED-boundary OQ; boundary identical across all 5 solver pipelines)* |
```

```edit:book/src/SUMMARY.md
- [triangular-solve-obstruction](./L1-L0/triangular-solve-obstruction.md)
- [fe-assemble-libceed-boundary-obstruction](./L1-L0/fe-assemble-libceed-boundary-obstruction.md)
```

## Speculative operators proposed

**None.** This is an obstruction (opaque-library-ownership) annotation. Per CLAUDE.md §Scope,
the libCEED-owned element-local quadrature kernel is vendored upstream and is not a Palace
component to lift; no L1 operator is proposed for it. The surrounding fold is already the firm
`fe_assemble` operator (cycle-054), which this annotation does NOT modify or downgrade.

## Supporting evidence

Citations all verified with `tools/citecheck/citecheck.py` at emit time:

- `bilinearform.cpp:75` `--anchor 'integ->Assemble'` → zero-drift (the leaf-kernel dispatch).
- `bilinearform.cpp:77` `--anchor 'AddSubOperator'` → zero-drift (the Palace-owned fold).
- `libceed/operator.cpp:455` `--anchor 'CeedOperatorFullAssemble'` → zero-drift.
- `libceed/operator.cpp:483` `--anchor 'CeedOperatorAssembleCOO'` → zero-drift (libCEED API).
- `libceed/operator.cpp:487` `--anchor 'OperatorCOOtoCSR'` → DRIFT +1, re-anchored to `:488`
  (the `loc_mat[id] = OperatorCOOtoCSR(...)` assignment spans `487-488`; I cite `487-488`).
- `integrator.hpp:58-61` — read-confirmed: line 58 = `virtual void Assemble(Ceed ceed,
  CeedElemRestriction trial_restr,` (the pure-virtual leaf signature, `= 0` at line 61).

The Palace-owns-orchestration / libCEED-owns-leaf split is read-confirmed from
`bilinearform.cpp:71-78` (the fold loop calling `integ->Assemble` then `AddSubOperator`) and
`libceed/operator.cpp:455-490` (the COO→CSR function calling `CeedOperatorAssembleCOO` then
`OperatorCOOtoCSR`).

## Open questions / caveats

- **DEFER consolidated tally to D7 (count-owner).** Per the dispatch instruction and the
  index-registration partition: I register my OWN index TABLE row + (this theme is its own
  cohort entry — the obstruction cohort) but DEFER the consolidated running-count tally /
  coverage-gap / growth-log lines to D7. I did not author any cohort-summing total.
- **Boundary anchors are a new verdict flavor.** I used `verdict: boundary-anchor` (distinct
  from `negative-anchor`) for the library-owned sites, because they are *positive Palace
  source* (the call sites exist and are cited at exact lines) that nonetheless mark a library
  boundary — they are not absence/negative anchors in the `triangular-solve-obstruction`
  sense. The lowering-verifier may want to normalize this verdict vocabulary; flagged for
  reconciliation. The triangular-solve precedent used `negative-anchor` because those sites
  document an *absence* (no Palace-authored kernel). Here Palace *does* author the
  orchestration; only the leaf is opaque — so the anchors are "boundary" not "negative."
- **`OperatorCOOtoCSR` ownership is a fine line.** I classified `OperatorCOOtoCSR`
  (`:487-488`) as Palace-owned *format conversion* and `CeedOperatorAssembleCOO` (`:483`) as
  the libCEED-owned *numerical assembly*. The boundary is the COO triples: their *production*
  is library-owned, their *reshaping* is Palace-owned. If a future lowering-verifier reads
  `OperatorCOOtoCSR`'s body and finds it does more than a layout shuffle (e.g. re-summing
  duplicate entries with numerical scaling — note `palace/fem/libceed/operator.cpp:492-499`
  does scale duplicated nonzeros), the boundary line may shift slightly. The shell/leaf split is
  robust regardless; only the exact placement of the COO→CSR step is the fine line. Flagged.
- **Cross-layer consequence (not in scope here).** This boundary will recur at L3 (the
  iteration-rotation layer) for FE assembly: the element-local quadrature contraction is a
  natural tensor-contraction at L4 (`tensor-contraction-respine`, the third OQ option the
  thread-opener listed), but at L1>L0 it is firmly opaque-library-ownership. The L4 view —
  whether the libCEED contraction RE-EXPRESSES as a clean L4 tensor-contraction combinator
  (making the boundary a *transparent* lowering rather than an opaque one at the top of the
  stack) — is a genuine open question for a future L4/L3 FE-assembly pass. It does NOT change
  the L1>L0 classification (the L0 kernel is library-owned at L0 regardless of how cleanly it
  lifts to L4). Logged as a forward note for the FE-assembly L3/L4 cohort.
