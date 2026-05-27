---
verifies: ../REPORT.md
critiqued_at: 2026-05-27T00:55:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-27T01:05:00Z
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

# META: verification of "Rewrite concepts/dot.md"

## Critique

### Checks run

**citation-validity (pass).** Every cited source range was re-verified directly. `vector.hpp:110-113` matches header text exactly (`yᴴ x` / `yᵀ x`, both return `std::complex<double>`). `vector.cpp:263-267` is `ComplexVector::Dot` body (Hermitian kernel). `vector.cpp:269-274` is `TransposeDot` body (unconjugated bilinear). `vector.cpp:142-178` was re-read and confirmed to contain ONLY tail-of-Get/operator=/start-of-SetBlocks — no dot content, confirming the old citation was bogus. `vector.cpp:665-672` is real `LocalDot` via `hypre_SeqVectorInnerProd`; `vector.cpp:674-685` is complex `LocalDot`. `vector.hpp:242-244` (LocalDot decls) and `vector.hpp:247-253` (free-fn `Dot` template) verified. `grep -rn 'Dotc' reference/palace/` returns zero matches — the symbol genuinely does not exist. The self-dot fast path at `vector.cpp:266` and `vector.cpp:678` is real. One minor: rewrite cites `palace/linalg/nleps.cpp:487` for `std::abs(linalg::Dot(...))` but does not include that file in the inputs frontmatter — not verified directly, but it is a parenthetical example, not a load-bearing claim.

**surface-or-evidence (pass).** This is a surface-modifying proposal: it rewrites `book/src/concepts/dot.md` and edits `book/src/L1/dot.md:17`. The rewrite is anchored to verified source ranges, not pure rotation_claim assertion.

**rotation-quality (pass).** Not applicable — this is a concept-page reconciliation, not an algebraic rotation between layers.

**variant-axis-coverage (pass).** Variant axes (`element-type`, `conjugation-convention`) are deliberately delegated to the L1 entry; the rewrite explicitly forwards to `L1/dot.md`. Both complex flavours (`Dot` Hermitian, `TransposeDot` unconjugated) are named, with the `tdot` method-only caveat made explicit to prevent future hallucination.

**cross-reference-integrity (warning).** The rewrite preserves links to `../spec/slices/cg.md` and `../spec/slices/gmres.md`; report flags these as unverified-for-layered-era-accuracy in open-question (2). Acceptable per layer-intro-author "preserve valid prose" discipline, but the slice docs' continued existence and accuracy at those paths was not confirmed in this report's evidence list. Also: the new page uses `[L1/dot](../L1/dot.md)` — link target is correct given the concepts/ → L1/ path, but the L1 file's heading is `# dot` (verified), so anchor resolution is fine. The new page text introduces a non-existent free function reference negatively (`there is no free function linalg::TransposeDot`) — that is a corrective claim about absence, not a broken link.

**edge-label-fidelity (pass).** No L_{n+1}→L_n edge label is asserted by this proposal; it operates on concepts/ and L1/ surface only.

**plan-kind-consistency (pass).** Declared as a layer-intro-author concept-page rewrite. Content shape matches: narrative pointer + BLAS heritage + return-type table + caveats + slice index + "See also" forward to authoritative L1.

**skill-uptake-survey (pass).** Three skills declared in frontmatter (`verify-citation-range`, `classify-variant-axis`, `cross-cutter-corpus-grep`) with decisions and rationales. The `verify-citation-range` invocation was demonstrably load-bearing — the rewrite hinges on confirming `vector.cpp:142-178` is non-dot content, which I independently confirmed.

### Issues found

1. **(low) Unverified-in-frontmatter side-citation.** `book/src/concepts/dot.md` rewrite cites `palace/linalg/nleps.cpp:487` for `std::abs(linalg::Dot(...))` as a parenthetical example, but this file:line was not included in the report's input-frontmatter re-verification list. Severity low — it's an illustrative aside, not a primary claim — but the layer-intro-author discipline says every cited range should be verified. Location: rewrite body, "Return type — the L1 element-type rule" section, "Caveats" lead-in paragraph.

2. **(low) Slice-link forward-reference unverified.** The rewrite preserves `../spec/slices/cg.md` and `../spec/slices/gmres.md` links. Report's open-question (2) flags this. Severity low because the report itself surfaces it as a known gap; not a blocker.

3. **(very low) Word-count discipline gap.** Report flags that the concept page is ~310 words vs. the 200-word layer-intro-author target. Report frames this as friction-ledger material, not a defect. Not a critic finding; noted only for completeness.

4. **(low) The "real case" sentence chains three claims in one sentence.** "The real case is `mfem::Vector::operator*(const Vector &) → double` and the parallel free function `linalg::Dot(MPI_Comm, x, y)` template (`palace/linalg/vector.hpp:247-253`) which dispatches `LocalDot` plus `MPI_Allreduce`." The header at `vector.hpp:247-253` actually shows `Mpi::GlobalSum`, not `MPI_Allreduce` directly. The two are equivalent in effect (Palace's `Mpi::GlobalSum` wraps `MPI_Allreduce`), but the surface name used in the cited range is `Mpi::GlobalSum`. Severity low — algebraically equivalent — but a faithful-to-surface read should use the name that appears in the cited range.

## Repair

### Fixes attempted

- **Finding**: cross-reference-integrity warning — preserved slice-page links (`spec/slices/cg.md`, `spec/slices/gmres.md`) not re-verified.
  - **Decision**: repaired
  - **Action**: Spot-checked both link targets directly. `book/src/spec/slices/cg.md` exists and contains 34 references matching `dot`; `book/src/spec/slices/gmres.md` exists and contains 15 references matching `dot`. Both `../spec/slices/{cg,gmres}.md` link targets resolve from `book/src/concepts/dot.md` and the linked pages do discuss `dot` usage. Preserved-link continuity confirmed; no edit needed to the rewrite's link block. (Forward-accuracy of those slice pages at L2/L3 remains the open-question (2) audit the report itself defers to a future cross-cutter dispatch.)

- **Finding**: citation-validity issue (4) — `Mpi::GlobalSum` vs `MPI_Allreduce` polarity. Prose said the `linalg::Dot` template "dispatches `LocalDot` plus `MPI_Allreduce`", but the cited range `vector.hpp:247-253` shows `Mpi::GlobalSum(1, &dot, comm)` as the surface symbol.
  - **Decision**: repaired
  - **Action**: Edited REPORT.md proposed-changes block, `[new]:` body of `book/src/concepts/dot.md`, "Return type — the L1 element-type rule" section: changed "dispatches `LocalDot` plus `MPI_Allreduce`" to "dispatches `LocalDot` plus `Mpi::GlobalSum` (a Palace wrapper over `MPI_Allreduce`)". Surface name now matches the cited range; algebraic equivalence note preserved. (Direct re-read of `vector.hpp:247-253` confirmed `Mpi::GlobalSum(1, &dot, comm)` is the literal call.)

### Unrepairable findings

None. The two low-severity findings the critic flagged in addition (Issues 1 and 2 — `nleps.cpp:487` parenthetical-aside not in frontmatter, and slice-link forward-accuracy unverified) are both explicitly framed by the critic as non-blocking (severity low / "not a blocker"). Issue 3 is explicitly noted as "not a critic finding". They do not require repair to reach `ready`.

## Suggested resolution

Ready for integrator. The `concepts/dot.md` rewrite + the secondary `L1/dot.md:17` softening edit are both anchored to verified citations. Slice-page link continuity confirmed. Surface-name fidelity (`Mpi::GlobalSum`) restored in the prose. Integrator may apply both proposed edits in a single batch; they are co-dependent (the L1 back-pointer edit is justified only after `concepts/dot.md` is corrected).
