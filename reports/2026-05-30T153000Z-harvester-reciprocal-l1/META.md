---
verifies: ../CYCLE.md
critiqued_at: 2026-05-30T15:45:00Z
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
repaired_at: 2026-05-30T16:15:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: repaired
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize reciprocal at L1"

## Critique

### Checks run

**citation-validity** — Ran `tools/citecheck/citecheck.py --scan` over CYCLE.md: **22 ok, 0 failing** for bounds + path-hygiene. Then ran `--anchor` on the load-bearing pinpoints: `vector.cpp:248-261` anchor `ComplexVector::Reciprocal` ✓ at 248; `vector.hpp:107` anchor `Set all entries to their reciprocal` ✓; `vector.hpp:108` anchor `Reciprocal` ✓; `vector.hpp:20` anchor `using Vector = mfem::Vector` ✓; `jacobi.cpp:80` anchor `dinv.Reciprocal` ✓; `chebyshev.cpp:178` and `:241` anchor `dinv.Reciprocal` ✓✓; `bilinearform.cpp:278` anchor `test_multiplicity.Reciprocal` ✓; `jacobi.cpp:16` anchor `diag(A) > 0` ✓ and `:92` anchor `omega` ✓; finer-grained `vector.cpp:257-259`, `:253-260`, `:255-260` anchors all ✓. Direct read of `vector.cpp:248-261` matches the body verbatim quoted in §Evidence (the `s = 1.0 / (XR² + XI²); XR *= s; XI *= -s` triple). The jacobi.cpp:16 SPD comment is technically inside the `GetLambdaMax` helper (the helper invoked from `JacobiSmoother::SetOperator` on the `ω = 0.0` path), not inside `SetOperator` proper — the report's §Evidence wording "ensures the diagonal-preconditioner consumer never invokes `reciprocal`" is still correct, but the citation's surrounding function-scope context (it is inside a setup-time helper, NOT the `Reciprocal()` call site itself) is mildly imprecise. Not a fail. **pass**.

**surface-or-evidence** — This is a **new-firm-operator** harvest (a `new:` proposed-changes block creating `book/src/L1/reciprocal.md`), not a refinement to an existing operator. Refinement-shaped checks (surface change + rotation_claim evidence) don't apply directly; instead the surface-or-evidence check evaluates whether the new operator is anchored by direct positive citations vs. literature/reconstruction. Every algebraic law is justified by either a syntactic-identity reading of `vector.cpp:255-260` (laws 1, 5, 6) or by standard field-algebra identities applied pointwise (laws 2, 3, 4, 7, 8). The upstream-MFEM real overload is correctly NOT asserted with a Palace cite — it is named via the `using Vector = mfem::Vector` alias at `vector.hpp:20` (Palace cite) and the behaviour is qualified as "documented in MFEM as element-wise `1/x[i]` without runtime check" / "taken as given per the CLAUDE.md upstream policy" with the OQ "MFEM `Vector::Reciprocal()` upstream behaviour" logged. The §Status "Caveats (not status reductions)" first bullet makes the policy alignment explicit. **pass**.

**rotation-quality** — Not directly applicable: this is a new firm L1 operator harvest, not an L_{n+1}→L_n rotation proposal. The L1>L0 lowering (in-place receiver mutation → pure functional out-of-place) is correctly **deferred** to a forthcoming `reciprocal-mutation-rotation` theme (named in §OQ and §Dependencies, plain-text per the rough-in-forward-reference convention). The §L1 vs L0 distinction block does the standard work of stating what L0 holds (in-place mutation, `forall_switch` host/device split, no zero-guard) vs. what L1 surfaces (pure functional, partial at `x[i]=0`); this is the rotation set-up not the rotation itself, and is correctly framed as such. **pass** (not applicable to new-firm-operator-harvest report shape).

**variant-axis-coverage** — The report identifies one orthogonal variant axis (`element-type: real | complex`) and explicitly enumerates non-axes (`zero-guard policy`: not a variant axis, treated as input precondition; `in-place vs out-of-place`: L1>L0 mutation-rotation concern, not L1 axis). The real/complex axis is treated as collapse-to-one-operator-at-L1 — the same elementwise multiplicative-inverse map parameterised by element type, with the complex `1/z = z̄/|z|²` decomposition recorded as law 5 (a law, not a variant axis). The §Variant axes block recapitulates this cleanly. No hidden branches: the four consumer sites are all on one of `Vector::Reciprocal()` or `ComplexVector::Reciprocal()`, all element-type-dispatched at the C++ overload level; no third overload, no fast-path, no constant-folding variant. **pass**.

**cross-reference-integrity** — Cross-references audited:
- `[`assemble-diagonal`](./assemble-diagonal.md)`, `[`jacobi-smoother`](./jacobi-smoother.md)`, `[`scal`](./scal.md)`, `[`nrm2`](./nrm2.md)`, `[`normalize`](./normalize.md)`, `[`axpy`](./axpy.md)`, `[`dot`](./dot.md)`, `[`apply_linop`](./apply_linop.md)`, `[`chebyshev-smoother`](./chebyshev-smoother.md)`, `[`axpby`](./axpby.md)`, `[`axpbypcz`](./axpbypcz.md)` — all live links, all targets exist on disk (verified by `ls book/src/L1/*.md`). ✓
- `elementwise_product` (the sibling) — correctly plain-text in the chapter body, since it is the parallel D3 dispatch and the file `book/src/L1/elementwise_product.md` does NOT yet exist on disk (the rough-in-forward-reference convention applies). ✓
- L1>L0 `reciprocal-mutation-rotation` theme — correctly plain-text (forthcoming). ✓
- L2 `elementwise_pencil` / `elementwise(f, ...)` candidate — correctly logged in §OQ as forthcoming. ✓

Fence parity: 6 fences total (`new:.../reciprocal.md` + close; `edit:.../index.md` + close; `edit:.../SUMMARY.md` + close) = even, no nested-fence issues. The firm body (Status + Signature + Algebraic-laws + Evidence + Semantics) IS enclosed inside the `new:book/src/L1/reciprocal.md` fence (lines 24-158) — the build-readiness fence-encloses-full-body guard PASSES.

**However**: a real coordination concern with the parallel D3 dispatch (`reports/2026-05-30T153000Z-harvester-elementwise-product-l1/`) surfaces here. Both D2 (this report) and D3 target the **same anchor regions** in `book/src/L1/index.md` and `book/src/SUMMARY.md`:
1. Both append after the `jacobi-smoother` bullet in §Vocabulary cohort Firm list (D2's `new` bullet uses prose-form "append after the jacobi-smoother bullet"; D3 uses an OLD/NEW patch around the jacobi-smoother bullet that adds `elementwise_product`).
2. Both append a row after the `jacobi-smoother` dep-map row at line 99 (and before `lanczos_step` at line 100).
3. Both append after `- [jacobi-smoother](./L1/jacobi-smoother.md)` (line 88) in SUMMARY.md.
4. **The Firm count is uncoordinated**: D2 explicitly bumps "Firm (23)" → "Firm (24)"; D3's OLD/NEW is text-anchored and does not bump the count. If D2 lands first, the count becomes 24; D3 has nothing about counts, so it stays at 24. If D3 lands first, the count stays at 23; D2 then bumps to 24. **Either ordering leaves the final on-disk count at 24, not the correct 25** (since both `reciprocal` and `elementwise_product` will be firm in the cohort). D3 explicitly acknowledges this in its §Open questions point 6 ("the count becomes 24 + 1 = 25 firm operators") but neither report's `edit:` block alone produces 25.
5. **Edit form mismatch**: D2 uses imperative natural-language prose-form (`[insert two lines... bump count... append row...]`); D3 uses surgical OLD/NEW anchored diff hunks. The integrator must accept both forms but the integration is per-report-serial, so D2's "line 99" / "line 88" line numbers are pre-D3 absolute line numbers and will shift if D3 lands first. **The natural-language form is harder to apply mechanically than the OLD/NEW form** — this is a coordination-style asymmetry.

The collision is integrator-resolvable (it serializes per-report), but the **Firm-count miscount is a real defect** that will silently mis-state the cohort size if not caught. Flagging as warning.

Overall: cross-reference targets all resolve, fence-parity good, but the D2/D3 coordination defect (Firm-count bump unsynchronised) is real. **warning**.

**edge-label-fidelity** — This is a single-layer L1 operator harvest, not a cross-layer rotation (no L_{n+1}→L_n edge label). The §L1 vs L0 distinction block correctly labels L0 vs. L1; the L1>L0 lowering theme is named-but-deferred ("forthcoming `reciprocal-mutation-rotation` theme"). No edge-label drift. **pass** (not applicable to single-layer harvest shape).

**plan-kind-consistency** — Declared status `firm`. Content shape: full Status + Signature + Algebraic-laws (8 laws + 5 non-laws) + Evidence (12 citation items incl. negative anchor) + Variant axes + L1 vs L0 distinction + Dependencies + OQ. This is firm-shaped content. The firm-on-positive-structure justification (per the `apply_linop` / `chebyshev-smoother` / `jacobi-smoother` / `axpy`/`scal`/`dot`/`nrm2` BLAS-1-leaf precedent — syntactic identities on positive complex-elementwise kernel body, no literature-inferred convergence claims) is correctly invoked and matches the precedent cited. The partial-definedness (`x[i] ≠ 0`) is correctly handled as an **input precondition** (recorded once in §Signature and §Semantics, not re-stated per law, and explicitly NOT a downgrade reason in §Status "Caveats (not status reductions)"). This is **not** `partly-constructive` (no constructive sub-part from negative anchors — the partial-at-zero is a precondition, not a reconstruction), **not** `rough-in (test-coverage-bounded)` (the laws are syntactic identities not literature-inferred — the `apply_linop` precedent applies, not the `eigsolve` precedent), **not** `obstruction` (functionality IS implemented in Palace's `ComplexVector::Reciprocal()` and the upstream `mfem::Vector::Reciprocal()`). `firm` is the correct kind. **pass**.

**skill-uptake-survey** — The report references mechanical-citation verification via `tools/citecheck/citecheck.py --anchor` (in §Supporting evidence, lines 184-191), which is the cycle-024-codified mechanical realization of the `verify-citation-range` skill. The skill name itself is not explicitly invoked, but the tool invocation IS surfaced, which satisfies the telemetry purpose of this check. Relevant adjacent skills not invoked but possibly applicable: `classify-variant-axis` (the report does a clean variant-axis treatment without invoking the skill — the result looks correct so this is not a defect, just a non-invocation). The MCP codemap is mentioned indirectly via the "codemap `search_text 'Reciprocal'` with `glob: test/unit/**` returns zero hits" negative-anchor verification — appropriate use. No skill-related concerns. **pass**.

### Issues found

1. **D2/D3 Firm-count desync (cross-reference-integrity)** — `book/src/L1/index.md` §Vocabulary cohort heading currently reads "Firm (23)". D2 (this report) bumps to `Firm (24)`; D3 (`elementwise_product`) does not touch the count. If both reports integrate this cycle, the final on-disk count will be `Firm (24)` but the actual firm bullet count will be 25. The defect is silent (no build break, no link failure) — it surfaces only as a stale cohort heading. **Where:** lines 161-165 of CYCLE.md (the `(a) Bump the "Firm (23)" count to "Firm (24)"` directive). **Severity:** medium — a real numeric defect that will mis-state the cohort size; integrator-resolvable but only if the integrator explicitly tracks "did the sibling D3 also land in this cycle". Repair candidate: have D2's `edit:` block instead bump conditionally on whether the sibling D3 has landed (or have D2's bump target `24` with a §Open-question note that the second sibling needs an additional `→25` bump). The cleaner alternative is for the integrator-per-report (when applying D2 second, after D3) to compose the bump correctly.

2. **D2/D3 same-anchor structural collision (cross-reference-integrity)** — Both D2 and D3 insert after the `jacobi-smoother` bullet in `book/src/L1/index.md` §Vocabulary Firm list, after the `jacobi-smoother` dep-map row (line 99), and after `- [jacobi-smoother](./L1/jacobi-smoother.md)` in `book/src/SUMMARY.md` (line 88). The integrator serializes per-report, so the second one applied will see shifted line numbers; D2's prose-form `(a) ... after the jacobi-smoother bullet` / `(b) ... after the jacobi-smoother row (line 99) and before the lanczos_step rough-in row (line 100)` does NOT specify behaviour if `reciprocal` or `elementwise_product` is now between `jacobi-smoother` and `lanczos_step`. **Where:** lines 161-178 of CYCLE.md (the three `edit:` blocks). **Severity:** low-to-medium — the natural-language directives are interpretable by the integrator, but the literal "line 99" / "line 100" / "line 88" line numbers will be stale if D3 lands first. Repair candidate: replace the line-number-bearing prose directives with surgical OLD/NEW patches anchored on the `jacobi-smoother` row text (mirroring D3's style), so that the apply order is irrelevant.

3. **D2 `edit:` blocks use older imperative-prose form rather than surgical OLD/NEW patches (cross-reference-integrity, minor)** — D2's three `edit:` blocks (`book/src/L1/index.md`, `book/src/SUMMARY.md`) contain natural-language directives bracketed `[insert two lines...]` / `[insert one chapter entry...]`. D3's parallel blocks use surgical `<<<OLD ... === NEW ... >>>` patches. The OLD/NEW form is the post-cycle-024 surface-of-truth-as-anchored-diff convention; prose-form remains valid but is more brittle under simultaneous-sibling integration. **Where:** lines 160-178 of CYCLE.md. **Severity:** low — interpretable but causes the line-number-shift collision flagged in issue 2.

4. **§Evidence `jacobi.cpp:16` SPD-precondition citation is inside `GetLambdaMax` helper, not `JacobiSmoother::SetOperator` (citation-validity, minor)** — The cited line `// Assumes A SPD (diag(A) > 0) to use Hermitian eigenvalue solver.` is inside the file-static `GetLambdaMax(MPI_Comm comm, const Operator &A, const Vector &dinv)` helper (line 14-31 of `jacobi.cpp`), invoked from `JacobiSmoother::SetOperator` only on the `ω = 0.0` damping-estimate path (line 86). The report's wording in §Evidence — "the SPD precondition that ensures the diagonal-preconditioner consumer never invokes `reciprocal` on a vector with a zero entry; the consumer-side enforcement of the L1 `x[i] ≠ 0` precondition" — slightly overstates the scope of the comment (the comment is about the Hermitian eigensolver in `GetLambdaMax`, not the broader Jacobi consumer's `Reciprocal()` call at line 80). The SPD precondition IS the broader consumer assumption (jacobi requires `diag(A) > 0` to be invertible, full stop), so the substantive claim is correct; the citation is just a slightly indirect anchor for it. **Where:** §Evidence bullet at CYCLE.md line 149 ("`palace/linalg/jacobi.cpp:16` — comment `// Assumes A SPD (diag(A) > 0)`"). **Severity:** very low — anchor verifies, claim is substantively correct, only the function-scope-of-citation is mildly imprecise. Repair candidate: rephrase the §Evidence bullet to clarify the comment is on the `ω=0.0` setup-helper, OR cite the broader pattern (the operator-class-level Jacobi-implies-SPD-`diag(A)>0` assumption is not separately cited but is the substantive ground for the precondition).

5. **Law 6 (conjugate–reciprocal commutation) derivation has a typo (rotation-quality / surface, minor)** — Law 6's parenthetical derivation reads `1/conj(z) = conj(1/z)` followed by the chain `conj(z)/|conj(z)|² = conj(z)/|z|² = conj(z/|z|²) = conj(1/z̄·|z|²/|z|²)` — the final term `conj(1/z̄·|z|²/|z|²)` is munged (the `|z|²/|z|²` would cancel to 1, leaving `conj(1/z̄)`, which is correct; but the way it's written is unclear). The "more direct" alternative chain immediately after `conj(1/z) = conj(z̄/|z|²) = z/|z|² = 1/z̄` is correct (`z/|z|² = z/(z·z̄) = 1/z̄`). The law itself is correct; the first parenthetical derivation is just garbled. **Where:** CYCLE.md line 85 (the parenthetical inside law 6). **Severity:** very low — does not invalidate the law, just a clarity issue in the derivation. Repair candidate: drop the garbled first chain and keep only the clean second chain `conj(1/z) = conj(z̄/|z|²) = z/|z|² = 1/z̄`.

6. **§Closed-form-for-real-element-type-matches-complex non-law description is internally tangled (clarity, minor)** — The fifth "Does not hold" entry says "Closed-form for real element-type matches complex" and then explains the closed form `x̄/|x|² = x/x² = 1/x` does recover the real case as the degenerate of the complex form, BUT the law is *stated* in complex-specific form. So the entry is asserting that law 5 does NOT generalise to a unified real+complex statement — which is fine — but the wording flip-flops on whether the equivalence holds (it says "law 5 is complex-specific" then says the closed form "recovers the real reciprocal as the degenerate case"). **Where:** CYCLE.md line 95. **Severity:** very low — the substance is correct (law 5 is recorded in complex-specific form because the L0 kernel realises it that way); the prose just reads inconsistently. Repair candidate: rephrase to "Law 5 is recorded in complex-specific form because Palace's complex kernel realises it as a non-trivial decomposition; the closed form degenerates to the trivial real reciprocal `1/x` in `ℝ`, but the law is not stated in unified form."

7. **OQ "Layer intro refresh" overlaps with parallel D3 sibling's same OQ (skill-uptake-survey / cross-reference-integrity, minor)** — D2 §Open questions point 5 ("Layer intro refresh") and D3's §Open questions point 6 ("Layer intro refresh — minimal") propose substantially the same hint to the layer-intro-author (extend §Vocabulary motif 1 to name `reciprocal` AND `elementwise_product`). The OQs are not duplicates per se (each report only knows its own dispatch's scope), but the integrator/meta-phase will see two near-identical OQ candidates from the same cycle. **Where:** CYCLE.md line 205. **Severity:** very low — the right outcome is one consolidated OQ filed by the integrator-finalize, not two; not a defect of either report individually. Repair candidate: no per-report repair needed; flag for integrator-finalize to dedupe.

8. **§Status promotion-condition language for `reciprocal` is implicit / not explicit (plan-kind-consistency, very minor)** — The report lands `firm` directly (not `partly-constructive`, not `rough-in (test-coverage-bounded)`), so the promotion-condition machinery isn't applicable. However, the §Status block could helpfully say one short sentence on **what would NOT cause a downgrade** if surfaced later (e.g., a future MFEM-side NaN policy detail, a future safe-reciprocal variant) — these are already in §OQ but the explicit alignment with §Status would harden the framing. **Where:** CYCLE.md lines 125-136. **Severity:** very low — not a defect, just a clarity opportunity. Repair candidate: optional, defer to integrator's discretion.

## Repair

### Fixes attempted

- **Finding 1 (D2/D3 Firm-count desync, medium)**
  - **Decision**: repaired
  - **Action**: (a) D2's `edit:` block on `book/src/L1/index.md` §Vocabulary cohort heading bumps "Firm (23)" → "Firm (24)" via a clean surgical OLD/NEW patch keyed on the full on-disk cohort-heading line, plus extends the heading prose tail to name "the elementwise multiplicative-inverse primitive" (i.e. `reciprocal`). D2 lands FIRST per the dispatch sequencing. (b) Added a new §Open-questions bullet ("Integrator-note: cycle-033 D2/D3 Firm-count coordination") that explicitly states D3, applied second, must bump "Firm (24)" → "Firm (25)" and extend the heading prose tail to also name `elementwise_product`. The correct both-landed final count is documented as 25. Integrator-per-report has explicit guidance for the second bump.
  - **Where applied**: CYCLE.md edit-block at lines 160-166 (count-heading surgical OLD/NEW); §Open-questions bullet appended at the end of §Open-questions / caveats.

- **Finding 2 (D2/D3 same-anchor structural collision, low-medium)**
  - **Decision**: repaired
  - **Action**: Replaced the three line-number-bearing prose directives with **four** surgical OLD/NEW patches keyed on the on-disk text content (not line numbers): one for the cohort-heading count bump (Finding 1 above), one for the `jacobi-smoother` bullet block in §Vocabulary (the `reciprocal` bullet is appended in the NEW arm directly after the `jacobi-smoother` bullet), one for the `jacobi-smoother` dep-map row (the `reciprocal` row is appended in the NEW arm directly after the `jacobi-smoother` row), and one for the SUMMARY.md `jacobi-smoother` chapter line (the `reciprocal` line is appended in the NEW arm directly after). All four OLD anchors are verified unique-in-target (4× `grep -c` confirmed 1 match each on `book/src/L1/index.md` and `book/src/SUMMARY.md`). Line numbers no longer appear anywhere in the edit blocks, so D3-first ordering does not shift D2's anchors (D3 inserts `elementwise_product` after `jacobi-smoother`; D2's anchors are still keyed on the `jacobi-smoother` row text and remain unique).
  - **Where applied**: CYCLE.md edit-blocks at lines 160-193 (all four OLD/NEW patches).

- **Finding 3 (D2 imperative-prose edit-block form, low)**
  - **Decision**: repaired
  - **Action**: The prose-form imperative directives are entirely replaced by the four surgical OLD/NEW patches under Finding 2 above. Convention now matches D3's post-cycle-024 anchored-diff style (`<<<OLD ... === NEW ... >>>` blocks inside ` ```edit:<path> ` fences).
  - **Where applied**: same as Finding 2 — CYCLE.md lines 160-193.

- **Finding 4 (jacobi.cpp:16 attribution to `SetOperator` instead of `GetLambdaMax` helper, very low)**
  - **Decision**: repaired
  - **Action**: Corrected the attribution in three places:
    1. §Evidence bullet for `jacobi.cpp:16`: now states the comment is inside the file-static `GetLambdaMax(MPI_Comm, const Operator&, const Vector&)` setup-helper (lines 14-20), invoked from `JacobiSmoother::SetOperator` only on the `ω = 0.0` damping-estimate path. The substantive claim (the comment names the broader operator-class-level Jacobi `diag(A) > 0` precondition that applies to all consumer paths) is preserved.
    2. `reciprocal.md` body §Signature / Precondition paragraph: added the "inside the `GetLambdaMax` setup-helper, which names the broader operator-class-level Jacobi precondition" qualifier on the in-line `jacobi.cpp:16` citation.
    3. `reciprocal.md` body §Semantics / No zero-guard paragraph: same qualifier appended to the in-line `jacobi.cpp:16` citation.
  - **Where applied**: CYCLE.md §Evidence bullet (line 149); §Signature Precondition paragraph (around line 56); §Semantics No zero-guard paragraph (around line 72).

- **Finding 5 (Law 6 derivation typo, very low)**
  - **Decision**: repaired
  - **Action**: Dropped the garbled first chain (`conj(z)/|conj(z)|² = conj(z)/|z|² = conj(z/|z|²) = conj(1/z̄·|z|²/|z|²)`) and kept only the clean derivation `conj(1/z) = conj(z̄/|z|²) = z/|z|² = 1/z̄`. Law statement itself unchanged.
  - **Where applied**: CYCLE.md law-6 line (around line 85).

- **Finding 6 (§Closed-form non-law phrasing tangled, very low)**
  - **Decision**: repaired
  - **Action**: Rephrased the fifth "Does not hold" entry to (i) lead with why law 5 is recorded complex-specific (Palace's complex kernel realises it as the non-trivial `z̄/|z|²` decomposition with three explicit steps at `vector.cpp:257-259`), (ii) acknowledge the closed form does degenerate to `1/x` in `ℝ` via the `x̄ = x` / `|x|² = x²` algebra, (iii) explain why the unified statement is not chosen (it would erase the non-trivial complex decomposition; the real-case body is `1/x[i]` directly with no decomposition step). No flip-flop on whether the equivalence holds.
  - **Where applied**: CYCLE.md §Algebraic laws / "Does not hold" fifth entry (around line 95).

- **Finding 7 (OQ Layer intro refresh overlap with D3, very low)**
  - **Decision**: not-needed
  - **Rationale**: Critic explicitly noted "no per-report repair needed; flag for integrator-finalize to dedupe." The OQ-overlap is a cross-report concern resolved at integrator-finalize when both reports land; per-report edit cannot anticipate D3's exact OQ wording and any consolidation belongs to the integrator's dedupe pass. (D2's OQ point 5 retains its own scoped wording — naming `reciprocal` AND the forthcoming `elementwise_product` for motif 1 extension — which is independently coherent.)

- **Finding 8 (§Status promotion-condition explicit framing, very minor)**
  - **Decision**: not-needed
  - **Rationale**: Critic explicitly tagged "optional, defer to integrator's discretion." Not a defect; the §Status "Caveats (not status reductions)" block already names the relevant out-of-status-modification considerations (upstream MFEM as given; safe-reciprocal as separate sibling, not variant; `forall_switch` host/device split as transparent). The §OQ already covers the same ground. Adding redundant prose under §Status would not improve clarity.

### Unrepairable findings

None. All critic-flagged findings are either repaired in place or formally not-needed per the critic's own resolution guidance.

### Verification

- **Citecheck**: re-ran `python3 tools/citecheck/citecheck.py --scan reports/2026-05-30T153000Z-harvester-reciprocal-l1/CYCLE.md`: **30 ok, 0 failing** (post-repair; same `jacobi.cpp:16` anchor still verifies — the Finding 4 fix is purely prose, the citation pinpoint is unchanged).
- **Fence parity**: 10 fences total, even — `new:book/src/L1/reciprocal.md` (1 open, 1 close) + four `edit:` blocks (4 open, 4 close). The firm body for `reciprocal.md` (Status + Signature + Algebraic-laws + Evidence + Semantics) IS enclosed inside the `new:` fence (lines 24-158). The build-readiness fence-encloses-full-body guard PASSES post-repair.
- **OLD/NEW anchor uniqueness**: 4× `grep -c` confirmed each OLD anchor matches exactly 1 line in its target file (`book/src/L1/index.md` for three patches; `book/src/SUMMARY.md` for one). Patches will apply mechanically regardless of D3 integration order.

## Suggested resolution

`ready`. All low / very-low severity findings repaired in place; the medium D2/D3 Firm-count coordination is handled by (a) D2 making its 23→24 bump as the first applier (the on-disk text supports D2's OLD anchor unmodified) and (b) an explicit integrator-note in D2's §Open questions describing the exact second-bump action D3's integrator-per-report dispatch must take (24→25 + heading-tail extension to name `elementwise_product`). The same integrator-note is mirrored on D3's repair (the parallel D3 repair pass is the proper home for the D3-side count-bump enactment).

Integrator-per-report can apply D2 unchanged; integrator-per-report on D3 will need to re-key D3's heading-count edit (if it has one) on "Firm (24)" or apply a separate count-bump patch keyed on "Firm (24)" → "Firm (25)". The D3 repair pass (separate report) is the right place to enforce this — flagged here for cross-report integrator coordination, not as a D2-side defect.
