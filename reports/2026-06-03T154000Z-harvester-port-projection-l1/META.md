---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T16:05:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-03T16:40:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize port_projection at L1"

## Critique

### Checks run

**citation-validity — warning.** I verified all load-bearing anchors against on-disk
Palace source via `palace-codemap read_range`/`search_text`. The two witness bodies match
the report exactly: lumped `GetSParameter` `lumpedportoperator.cpp:283-294` (`def :283`,
`(*s) * E.Real()` at `:287`, conditional `dot.imag((*s) * E.Imag())`, `Mpi::GlobalSum`
`:292`, close `}` `:294` — confirmed), and wave `GetSParameter`
`waveportoperator.cpp:780-793` (comment `(E × H_inc⋆)·n = E·(−n × H_inc⋆)` `:782-783`,
`MFEM_VERIFY(E.HasImag())` `:784-786`, the 2×2 real recombination
`Re = −(port_sr·Eᵣ) − (port_si·Eᵢ)` / `Im = −(port_sr·Eᵢ) + (port_si·Eᵣ)` at `:789-790`,
close `}` `:793` — confirmed; both END anchors are correct, the FE-source END-drift caveat
did not bite). The assembly site `lumpedportoperator.cpp:162-196` (`VectorFEBoundaryLFIntegrator`
over the port boundary marker) is correct. `waveportoperator.hpp:101`
(`std::unique_ptr<mfem::LinearForm> port_sr, port_si;`) is correct. All three test citations
verified exact (`test-lumpedportintegration.cpp:367,720` both `GetSParameter(...)`;
`test-romoperator.cpp:603` `auto S = port_data.GetSParameter(E)`). Cross-artifact citations
verified: `bilinear-form.md:62-94` is the `xᴴ M y` / `LinearOperator[M,N]` signature;
`dot.md` lines 34/63-68 are the Hermitian conjugate-linear form and lines 71-75 are the
`tdot` unconjugated-bilinear sibling; `sparameter_reduce.md:197-202` is the gate-b "no firm
L1 home" caveat. **The one defect:** the report repeatedly cites
`palace/models/lumpedportoperator.cpp:51` for the `mutable std::unique_ptr<mfem::LinearForm> s, v;`
member declaration. That declaration lives at `lumpedportoperator.**hpp**:51`, not the `.cpp`
(`search_text` resolves the snippet uniquely to the `.hpp`; `lumpedportoperator.cpp:48-53` is
loop body, `for (const auto &elem : data.elements)`). This is a `.cpp`/`.hpp` path-confusion
drift, not a line-number drift — the line `51` is right, the extension is wrong. It recurs in
~6 places (inputs frontmatter `:51` is given as part of the `lumpedportoperator.cpp` witness
block context, warrant point 1 line 47, Record-definition line 198, Evidence line 409,
Supporting-evidence line 493, dep-map row line 446 `lumpedportoperator.cpp:162-196,:51`). Warning,
not fail: the cited content is genuinely there at line 51, just in the sibling header file.

**surface-or-evidence — pass.** The unify-vs-mint verdict is the load-bearing claim and it is
**sound**. (1) The port mode `s` is genuinely an assembled `mfem::LinearForm` — an element of
the FE dual space, a covector — NOT the `Operator`/`LinearOperator[M,N]` matrix-weight that
`bilinear-form`'s `xᴴ M y` requires (confirmed: declaration is `unique_ptr<mfem::LinearForm>`,
assembled by `AddBoundaryIntegrator(new VectorFEBoundaryLFIntegrator(fb))` + `Assemble()` at
`lumpedportoperator.cpp:162-196`; `bilinear-form.md:69` types the weight as `LinearOperator[M,N]`).
Re-expressing `⟨s,E⟩` as `bilinear_form(s, I, E)` would indeed invent both a fake identity weight
and a fake second vector and attach the wrong Hermitian/conjugate-linear algebra — the NON-MATCH
is real, the verb is not redundantly minted. (2) The pairing `(*s) * E` is genuinely the
unconjugated real dual contraction `Σᵢ sᵢ Eᵢ` (MFEM `LinearForm::operator*`), not the Hermitian
`conj(x)·y` that `dot.md:34` carries — confirmed in both bodies (no `conj` anywhere; the wave case
is `(sr+i·si)(Eᵣ+i·Eᵢ)`, explicitly non-Hermitian). The wave 2×2 recombination on two distinct
functionals `port_sr`/`port_si` is genuinely not any single `dot`/`tdot` co-spatial inner product
— it forces the own-verb verdict. So the report neither minted a redundant verb (a `bilinear-form`
specialization would NOT have sufficed) nor wrongly subsumed a distinct op. Evidence shape is a
firm L1 operator entry with surface (the full chapter) + positive-source warrant — appropriate.

**surface-or-evidence (record-definition sub-check) — pass.** The signature names one record,
`Covector[N]`. It has a proper in-chapter `## Record definition` section (lines 186-207): fields
(coefficients `Tensor[N]` real; domain axis), types, meaning, construction-vs-run-time stratum
(both construction-time, assembled once at port setup), and the L0 backing-struct home
(`mfem::LinearForm`, `lumpedportoperator.hpp:51` [see citation note] / `waveportoperator.hpp:101`).
Single-consumer justification is stated, and the ≥2-consumer promotion watch
(`assembled-fe-covector-record-definition-home`) is flagged in Open questions. Fully compliant
with the record-definition obligation.

**rotation-quality — pass.** Not a rotation report (a per-operator L1 harvest, not an L_{n+1}>L_n
theme). No rotation claim is asserted; the L1>L0 lowering is explicitly deferred (Open questions).
Not applicable to this report-kind.

**variant-axis-coverage — pass.** Three orthogonal axes declared and each handled: `port-kind`
(lumped/wave — THE load-bearing axis, both witnessed and both collapsed to one dual-pairing
operator parameterised by covector element type), `precision-mode` (Palace exposes one; recorded
for parallel structure), `parallel-wrapper` (MPI collective scoped out per CLAUDE.md single-rank,
recorded for L1>L0 reintroduction). The collapsed `covector element-type` axis is explicitly listed
under "Collapsed (absorbed) axes". No hidden branch — the lumped real-covector vs. wave
complex-covector split is exactly the surfaced port-kind axis.

**cross-reference-integrity — fail.** Two build-readiness defects. **(1) Nested bare fence inside
the `new:` block (cycle-019 truncation hazard).** The `new:book/src/L1/port_projection.md` block
opens at line 85 and the Signature code block at lines 153/156 uses a **bare ` ``` `** (no `text`
tag, not indented). A line-based proposed-changes fence parser reads line 153 as the CLOSE of the
`new:` block — capturing only lines 86-152 (frontmatter + intro + Context, ending right before
`## Signature`) and dropping the entire firm apparatus (`## Signature`, `## Record definition`,
`## Semantics`, `## Algebraic laws`, `## Status` [the firm claim], `## Evidence`) OUTSIDE the fence.
Fence enumeration in the proposed-changes region: open `:85`, bare-nested `:153`, bare-nested `:156`,
outer-close `:442`. This is precisely the friction-ledger `firm-chapter-body-authored-outside-
proposed-changes-fence` / nested-`text`-fence truncation defect; the firm body's `## Status` sits
between the nested-close and the outer-close, which naive matching does not capture. (Companion
repair: `convert-nested-fences-to-indented-code-in-proposed-changes-block`.) **(2) SUMMARY.md edit
indentation mismatch.** The `edit:book/src/SUMMARY.md` block (lines 454-456) writes the entry with
**8 leading spaces** (`        - [port_projection]...`). Existing L1 sub-chapter entries under
"Operator application & assembly" use **2 leading spaces** (`  - [apply_linop]`, SUMMARY.md:176).
mdBook SUMMARY nesting is indentation-sensitive; 8 spaces mis-nests the entry (two levels too deep)
or breaks the list. All resolvable `[link]` references and slugs check out (the bilinear-form/dot
NON-MATCH down-links, the `sparameter_reduce` up-link, the index/SUMMARY targets) — the failure is
purely the fence-truncation + indentation build hazards.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (this is an L1 operator entry,
not a lowering theme). The "L1 vs L0 distinction" section and the deferred L1>L0 lowering discuss
the correct direction (L1 form pure-functional; L0 the two kernels). Not applicable.

**plan-kind-consistency / firm status — pass.** Declared kind is a firm L1 operator entry and the
content matches: full Signature + Record-definition + Semantics + Algebraic-laws (with explicit
absences) + Status + Evidence, no rough-in placeholders. The `firm` status is justified as
firm-on-positive-structure: the signature is read off two positive source sites and every law is a
syntactic identity on the dual-pairing fold (linearity in each argument from `Σ sᵢ(αE₁ᵢ+E₂ᵢ)`;
real/imag splitting from the lumped two-pairing body; the non-Hermitian/non-symmetric absences read
directly off the un-conjugated `Σ sᵢ Eᵢ`). The no-dedicated-test caveat is correctly treated as
non-gating per the `apply_linop`/`jacobi-smoother`/`elementwise_product` precedent, and the kernel
is in fact unit-tested (verified `test-lumpedportintegration.cpp:367,720`, `test-romoperator.cpp:603`).
Firm is warranted.

**skill-uptake-survey — pass.** The report references its citation self-verification
(`citecheck --anchor` on the lumped body + direct on-disk END reads per the FE-source END-drift
caveat, Supporting-evidence lines 497-501) — appropriate skill uptake for a positive-source harvest.
(Telemetry note only: the build-readiness fence guard / nested-fence-conversion skills were NOT
invoked, which is exactly why defect (1) below slipped through — surfaced, not blocking.)

### Issues found

1. **CYCLE.md proposed-changes (cross-reference-integrity, HIGH / build-blocking).** Bare nested
   ` ``` ` fence at lines 153/156 inside the `new:book/src/L1/port_projection.md` block (which opens
   `:85`, closes `:442`). Under line-based fence matching, line 153 is read as the `new:` block's
   close, truncating the captured chapter at line 152 and dropping the entire firm apparatus
   (`## Signature` through `## Evidence`, including the `## Status` firm claim) outside the fence.
   This is the cycle-019 `firm-chapter-body-authored-outside-proposed-changes-fence` defect family.

2. **CYCLE.md `edit:book/src/SUMMARY.md` block, lines 454-456 (cross-reference-integrity, build-
   readiness).** The entry is written with 8 leading spaces; existing L1 sub-chapter entries under
   "Operator application & assembly" use 2 leading spaces (SUMMARY.md:176). Indentation-sensitive
   mdBook nesting → mis-nested or broken list. (Also: the edit block carries no positioning anchor;
   alpha placement under the grouping puts `port_projection` after `assemble_frequency_operator`,
   SUMMARY.md:178 — the prose states this but the bare-line block does not encode it.)

3. **CYCLE.md, multiple sites (citation-validity, MEDIUM — and internally inconsistent).**
   `palace/models/lumpedportoperator.cpp:51` for the `mutable std::unique_ptr<mfem::LinearForm> s, v;`
   member declaration is the wrong file extension — the declaration is at `lumpedportoperator.hpp:51`
   (`search_text` resolves the snippet uniquely to the `.hpp`; `.cpp:48-53` is loop body,
   `for (const auto &elem : data.elements)`). The line number `51` is correct; only the `.cpp`→`.hpp`
   extension is wrong. **Wrong (`.cpp:51`) at lines 46, 409, 446 (`...162-196,:51` in the dep-map row),
   493, 522.** **Correct (`.hpp:51`) at line 198 (Record-definition).** So the report is internally
   inconsistent — it has the right extension once and the wrong extension five times; the `.hpp:51`
   form is the correct one. (Note line 522 also reuses `.cpp:51` for the sibling `v` linear form in
   the Open-questions watch — same fix.)

## Repair

### Fixes attempted

- **Finding (1)**: (FAIL, build-blocking) Nested bare ` ``` ` fence at lines 153/156 inside the `new:book/src/L1/port_projection.md` proposed-changes block — a line-based fence parser reads line 153 as the block close, truncating the chapter at line 152 and dropping the entire firm apparatus (`## Signature` through `## Evidence`, incl. `## Status`) outside the fence (friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence`, nested-`text`-fence variant).
  - **Decision**: repaired
  - **Action**: Applied `convert-nested-fences-to-indented-code-in-proposed-changes-block`. Converted the `## Signature` nested code block (CYCLE.md §Proposed changes) from a bare ` ``` ` fence to a 4-space-indented code block, preserving the two signature lines byte-for-byte. This was the only nested fence inside the `new:` block (the element-type table and the rest of the body are prose/Markdown tables, not fenced code). Verified with `proposed-changes-fence-encloses-full-body-guard`: fence count is now 8 (= 2 × 4 proposed-changes blocks), all paired; the `new:` block opens at `:85` and closes at `:440`; `## Signature` (151), `## Status` (351), and `## Evidence` (401) all sit INSIDE the fence. The full firm body is now enclosed.

- **Finding (2)**: (FAIL, build-readiness) `edit:book/src/SUMMARY.md` block used 8-space indentation; existing L1 sub-chapter entries under "Operator application & assembly" use 2 spaces (SUMMARY.md:176).
  - **Decision**: repaired
  - **Action**: Changed the SUMMARY.md edit-block line from 8 leading spaces to 2 (`  - [port_projection](./L1/port_projection.md)`), matching the existing L1 sub-chapter nesting depth (verified against SUMMARY.md:174-178). The alpha position under the grouping (after `assemble_frequency_operator`) is the integrator's placement call; the report prose already states it.

- **Finding (3)**: (warning, citation extension) `lumpedportoperator.cpp:51` is the wrong file extension for the `mutable std::unique_ptr<mfem::LinearForm> s, v;` member declaration — it lives at `lumpedportoperator.hpp:51`. Wrong at report lines 46, 409, 446, 493, 522; correct once at 198.
  - **Decision**: repaired
  - **Action**: Verified on-disk via `palace-codemap read_range`: `lumpedportoperator.hpp:51` is `mutable std::unique_ptr<mfem::LinearForm> s, v;` (the member declaration); `lumpedportoperator.cpp:51` is loop body (`for (const auto &elem : data.elements)`). Fixed all 5 `.cpp`→`.hpp` occurrences (warrant point 1, Evidence, dep-map row, Supporting-evidence, Open-questions sibling-`v` watch). The dep-map row was split to `...162-196` + decl `...hpp:51` so the assembly range (correctly `.cpp`) and the declaration (`.hpp`) each carry the right extension. `grep` confirms zero residual `lumpedportoperator.cpp:51`. The line number `51` was already correct everywhere; only the extension changed.

### Unrepairable findings

None. All three flagged findings were mechanical/surgical and fully repaired in-place; no substantive content or the unify-vs-mint verdict was touched.

## Suggested resolution

`ready`. Both build-blocking FAILs (nested-fence truncation, SUMMARY indent) are repaired and the citation-extension warning is fixed. Notes for the integrator:
- The `new:book/src/L1/port_projection.md` block now encloses the full firm body (frontmatter through `## Evidence`); landing it produces the complete firm chapter, not an intro stub.
- The SUMMARY.md entry should land in alpha position under the L1 "Operator application & assembly" sub-grouping (after `assemble_frequency_operator`, SUMMARY.md:178), per the report's index-registration note.
- The report explicitly DEFERS the `book/src/L1/index.md:31` running-count increment (34→35) to the cycle's index-count owner (D4 also touches this index this cycle) — do not let the two index-touching reports diverge on the absolute tally.
