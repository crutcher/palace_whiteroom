---
agent: lifter
invoked_at: 2026-06-03T030410Z
scope: L4 solve_family §Specializations re-anchor (confirm-first) + L4-L3/index.md bare-basename lint — solve-family-reanchor-lint
status: pending
inputs:
  - book/src/L4/solve_family.md
  - book/src/L4-L3/index.md
  - reference/palace/palace/drivers/electrostaticsolver.cpp
  - reference/palace/palace/drivers/magnetostaticsolver.cpp
  - reference/palace/palace/fem/integrator.hpp
  - reference/palace/palace/fem/libceed/integrator.hpp
integrated_at: 2026-06-03T214500Z
integration_commit: 03d43ae
integration_notes: "cycle-073 D5 (LOW hygiene). Applied clean — item-(b) only: L4-L3/index.md bare-basename citation lint integrator.hpp:58-61 -> palace/fem/integrator.hpp:58-61 (the fem/ BilinearFormIntegrator::Assemble pure-virtual). Item-(a) solve_family §Specializations re-anchor a CONFIRMED NO-OP (all 16 anchors hand-verified correct). Resolves the c068-landing AMBIG verbatim-moved by the c071 reorg. Build exit 0, linkcheck2 clean."
---

# CYCLE: Re-anchor solve-family-reanchor-lint

## Summary
Two surgical hygiene items, cycle-073 D5 (LOW). Item (a): the `solve_family.md`
§Specializations note (`:107`/`:109`) cites 16 electrostatic + magnetostatic
driver anchors that a priorities note ASSERTED had drifted +1. Hand-`Read`
verification against on-disk source confirms **all 16 anchors are correct** —
the priorities +1-drift assertion is itself the codemap-drift class the planner
warned about. **Item (a) is a complete NO-OP** (no edit). Item (b): the
`L4-L3/index.md:15` citation `integrator.hpp:58-61` is a bare basename; the
dispatch scope guessed `palace/fem/libceed/integrator.hpp`, but on-disk
verification shows that guess is WRONG (that file's `:58-61` is unrelated
libCEED free-functions). The correct leaf-kernel boundary
`BilinearFormIntegrator::Assemble` pure-virtual lives at
**`palace/fem/integrator.hpp:58-61`** — matching 4 firm sibling citations
already in the repo. One bare-basename → qualified-path edit proposed.

## Proposed changes

### Item (a) — solve_family.md §Specializations: NO CHANGE (confirmed correct)

No edit. All anchors hand-verified against on-disk source (full verification
table in §Discipline notes). The electrostatic `:30`/`:35`/`:36`/`:46`/`:60`/`:68`/`:69`/`:89`
and magnetostatic `:30`/`:35`/`:36`/`:47`/`:66`/`:76`/`:77`/`:99` anchors all land
exactly on the constructs the chapter claims. The priorities-note +1-drift
assertion is rejected as itself codemap-drift (the planner's
`read_range electrostaticsolver.cpp:28-37` was correct; the priorities note was
not).

### Item (b) — L4-L3/index.md:15: qualify bare basename to full reference-relative path

```edit:book/src/L4-L3/index.md
[old]: integ->Assemble`, `:75` → `integrator.hpp:58-61`
[new]: integ->Assemble`, `:75` → `palace/fem/integrator.hpp:58-61`
```

This qualifies the bare basename `integrator.hpp:58-61` to its full
reference-relative path `palace/fem/integrator.hpp:58-61`. The path is the
`fem/` integrator.hpp (the `BilinearFormIntegrator` base class), NOT the
`fem/libceed/` one the dispatch scope tentatively guessed — see §Discipline
notes for the disambiguation. The `:58-61` range and the libCEED-leaf-boundary
semantics are unchanged (path-hygiene only). This is the lift mandate: structure
of the entry stays, the citation firms up.

## Discipline notes

**Item (a) — full anchor verification (hand-`Read`, NOT citecheck --anchor, per
the off-by-one-on-brace-boundary discipline).**

Electrostatic (`reference/palace/palace/drivers/electrostaticsolver.cpp`, hand-read `:28-90`):

| Chapter cite | Claimed construct | On-disk line | Verdict |
|---|---|---|---|
| `:30` | `K = laplace_op.GetStiffnessMatrix()` | `:30` `auto K = laplace_op.GetStiffnessMatrix();` | OK |
| `:35` | `KspSolver ksp(...)` | `:35` `KspSolver ksp(iodata, laplace_op.GetH1Spaces());` | OK |
| `:36` | `ksp.SetOperators(*K, *K)` | `:36` `ksp.SetOperators(*K, *K);` | OK |
| `:46` | `std::vector<Vector> V(n_step)` | `:46` `std::vector<Vector> V(n_step);` | OK |
| `:60` | family `laplace_op.GetSources()` | `:60` `for (const auto &[idx, data] : laplace_op.GetSources())` | OK |
| `:68` | `laplace_op.GetExcitationVector(idx, *K, V[step], RHS)` | `:68` same | OK |
| `:69` | `ksp.Mult(RHS, V[step])` | `:69` `ksp.Mult(RHS, V[step]);` | OK |
| `:89` | `step++` | `:89` `step++;` | OK |

Magnetostatic (`reference/palace/palace/drivers/magnetostaticsolver.cpp`, hand-read `:28-100`):

| Chapter cite | Claimed construct | On-disk line | Verdict |
|---|---|---|---|
| `:30` | `K = curlcurl_op.GetStiffnessMatrix()` | `:30` `auto K = curlcurl_op.GetStiffnessMatrix();` | OK |
| `:35` | `KspSolver ksp(...)` | `:35` `KspSolver ksp(iodata, curlcurl_op.GetNDSpaces(), &curlcurl_op.GetH1Spaces());` | OK |
| `:36` | `ksp.SetOperators(*K, *K)` | `:36` `ksp.SetOperators(*K, *K);` | OK |
| `:47` | `std::vector<Vector> A(n_step)` | `:47` `std::vector<Vector> A(n_step);` | OK |
| `:66` | family `curlcurl_op.GetSurfaceCurrentOp()` | `:66` `for (const auto &[idx, data] : curlcurl_op.GetSurfaceCurrentOp())` | OK |
| `:76` | `curlcurl_op.GetExcitationVector(idx, RHS)` | `:76` `curlcurl_op.GetExcitationVector(idx, RHS);` | OK |
| `:77` | `ksp.Mult(RHS, A[step])` | `:77` `ksp.Mult(RHS, A[step]);` | OK |
| `:99` | `step++` | `:99` `step++;` | OK |

16-of-16 correct. **Item (a) is a no-op.** The +1-drift priorities assertion is
rejected; the cycle-073 planner's codemap-read-confirmed verdict (anchors
correct) is upheld. This is exactly the
`codemap-read-range-plus-one-drift-on-brace-boundary` trap stated in reverse:
here a *human-readable priorities note* claimed drift where on-disk shows none.

**Item (b) — disambiguation of two integrator.hpp files (the load-bearing
finding).** There are TWO files named `integrator.hpp`:
- `reference/palace/palace/fem/integrator.hpp`
- `reference/palace/palace/fem/libceed/integrator.hpp`

The dispatch scope tentatively guessed the `libceed/` one. I hand-read both at
`:58-61`:
- `fem/libceed/integrator.hpp:58-61` = the tail of the free function
  `AssembleCeedGeometryData(...)` (`:58` `CeedElemRestriction geom_data_restr);`)
  + a blank line + the doc-comment opening for `AssembleCeedOperator`
  (`:60-61`). This is NOT a pure-virtual `Assemble` and does NOT match the
  chapter's "leaf-kernel signature — pure virtual" description.
- `fem/integrator.hpp:58-61` = exactly
  `virtual void Assemble(Ceed ceed, ... CeedOperator *op) const = 0;` — the
  `BilinearFormIntegrator::Assemble` pure-virtual declaration, ending on `:61`
  with `= 0;`. This IS the `integ->Assemble` dispatch target the chapter names.

So the correct qualification is `palace/fem/integrator.hpp:58-61`, NOT the
`libceed/` path. This is corroborated by 4 firm sibling citations already in the
repo that all use `palace/fem/integrator.hpp:58-61` for this exact boundary:
- `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md:7,234,267`
- `book/src/L4-L3/fe-assemble-fold-dissolution.md:86,102,106,197`
- `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md:203` (a wider
  `:39-130` range over the same base class)
- `book/src/L1-L0/weak-form-term-rotation.md:12,201,...`

The lint thus also harmonizes `L4-L3/index.md` with the rest of the artifact's
citation of this boundary. Path-hygiene only; range + semantics untouched.

**Citation self-verification (emit-time).** `citecheck` confirms
`palace/fem/integrator.hpp:58-61 --anchor Assemble` → `[ok]` (anchor at `:58`,
in range). END line `:61` confirmed by direct on-disk `Read` (the `= 0;`
terminus of the pure-virtual decl), per the close-brace/END-line discipline (the
END here is a `= 0;` statement terminus, not a brace, and the Read confirms it).

**Bounded-scope note.** Per dispatch instruction, the edit is surgical to the
single `integrator.hpp:58-61` bare basename. Line 15 also carries
`bilinearform.cpp:64-70`/`:75`/`:77`/`:97`/`:104` and a `:60`-style shorthand
chain; these are out of this dispatch's scope (and the `:NN` shorthands resolve
contextually to the just-named `bilinearform.cpp`). I did not touch them — see
§Open questions for whether a follow-up bare-basename sweep is warranted.

## Supporting evidence
- `reference/palace/palace/drivers/electrostaticsolver.cpp:28-90` — electrostatic anchors (item a, all confirmed).
- `reference/palace/palace/drivers/magnetostaticsolver.cpp:28-100` — magnetostatic anchors (item a, all confirmed).
- `reference/palace/palace/fem/integrator.hpp:58-61` — `BilinearFormIntegrator::Assemble` pure-virtual (item b, correct target).
- `reference/palace/palace/fem/libceed/integrator.hpp:58-61` — the WRONG-guess target (free functions; documented for the record).
- Sibling firm citations using `palace/fem/integrator.hpp:58-61`:
  `fe-assemble-libceed-boundary-obstruction.md`, `fe-assemble-fold-dissolution.md`,
  `weak-form-term-rotation.md`, `fe-operator-assemble-mutation-rotation.md`.

## Open questions / caveats
- The dispatch scope's tentative `palace/fem/libceed/integrator.hpp` guess was
  wrong; the resolution (`palace/fem/integrator.hpp`) is firmly evidenced and
  needs no escalation. Flagging only so the planner notes the guess-vs-confirmed
  delta.
- `L4-L3/index.md:15` carries other shorthand `:NN` citations
  (`bilinearform.cpp` chain). They are NOT bare basenames in the lint sense (they
  are `:NN` continuations of a just-named file) and were left untouched per
  surgical scope. If a future hygiene pass wants every citation in the index
  table fully-qualified (no `:NN` shorthand), that is a broader index-table
  convention decision — out of this LOW-hygiene dispatch's scope. Not appending
  to open-questions.md as this is a convention-preference, not a defect.
