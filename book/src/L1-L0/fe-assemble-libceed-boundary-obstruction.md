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
tensor-contraction-respine" — as **`opaque-library-ownership`**.

## Status

`obstruction (opaque-library-ownership)` — **kernel-api** (the DIRECTIVE-3 role-label: this
node IS the opaque kernel-API CONTRACT the spine calls; the from-our-tensor-algebra realization
is the separate **kernel-impl** node
[`libceed-quadrature-kernel-impl`](../L1/libceed-quadrature-kernel-impl.md), linked back here by
a `realizes-kernel-api` `reference`-class edge — free, navigational, NOT a `depends-on`; a
reviewer reads both and checks they match, `lowering-verifier` audits the correspondence). The
role-label does NOT change the obstruction disposition; this remains the mandatory sub-kind tag
(per CLAUDE.md §Methodology-invariants "Obstruction themes have two sub-kinds"). The entire callable that
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
[`fe_assemble`](../L1/fe_assemble.md) operator expresses FE assembly as the fold

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
[`triangular-solve-obstruction`](./triangular-solve-obstruction.md)
opaque-library-ownership precedent in routing: the value is documenting the boundary +
cataloguing negative anchors, with **no** promotion route (Palace will not re-architect its
libCEED consumption).

**Structural distinction from the precedents.** Unlike `triangular-solve-obstruction` (where
the L1 form is *empty* — there is no positive Palace site at all), this theme's surrounding
L1 fold **exists and is firm** (`fe_assemble`). The obstruction is a *strict sub-term*
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

- [`fe-operator-assemble-mutation-rotation`](./fe-operator-assemble-mutation-rotation.md) —
  the sibling theme that maps the full FE-assembly surface and **logged the libCEED boundary
  as an OQ** (§"libCEED boundary": "transitive-firm vs opaque-library-ownership vs
  tensor-contraction-respine"). **This annotation settles that OQ** as
  `opaque-library-ownership`. The two cross-link: the thread-opener is the surface map; this
  annotation is the boundary classification.
- [`fe_assemble`](../L1/fe_assemble.md) (firm) — the L1 fold whose per-term leaf this
  annotation bounds. **Stays firm; not downgraded.**
- [`triangular-solve-obstruction`](./triangular-solve-obstruction.md) — the prior
  `opaque-library-ownership` obstruction theme (HYPRE GS/SSOR relaxation + external
  direct-solver wrappers). The routing precedent for this sub-kind: document the boundary,
  catalogue the negative anchors, no promotion route.
