---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T123000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
---

# META: verification of RE6 axpy/scal arity-leaf elimination into `linear_combination`

## Critique

### Checks run

- **citation-validity (pass).** All load-bearing L0 anchors verify EXACTLY on-disk (at the
  real path `reference/palace/palace/linalg/...`): `vector.cpp:749-751` = `if (gamma == 0.0)
  { add(alpha, x, beta, y, z);` (the γ==0 arity-collapse); `vector.cpp:702-712` = free-function
  `AXPY` with `if (alpha == 1.0) { y += x; }` (the load-bearing constant-fold fast-path);
  `vector.cpp:207-211` = `if (si == 0.0)` real fast-path; `nleps.cpp:486-491` =
  `c *= 1.0 / norm_c;` (eigenvector-normalisation `scal` consumer); `iterative.cpp:632,811`
  = `w *= 1.0 / Hj[j + 1];` (GMRES Arnoldi `scal` consumers). `citecheck --scan` reports
  these as `[MISS]`/`[AMBIG]`, but that is a citecheck-root artifact (the project's nested
  `palace/palace/` layout falls outside citecheck's search roots and `operator.cpp` is a
  basename collision the report disambiguates with the `linalg/` prefix) — NOT real drift; I
  confirmed every load-bearing pinpoint by direct on-disk read. The fold-in payload preserves
  every deleted leaf's unique anchor (no claim loses its anchor). PASS.
- **surface-or-evidence (pass).** This is a replace-and-propagate refactor of already-firm
  combinator surface, not a new-record proposal; no signature names an undefined record. The
  fold-in moves verified evidence in-layer. PASS.
- **rotation-quality (pass).** Not a rotation proposal — it is an arity-family elimination
  (combinator-as-entry, leaves-as-specialization-notes per the vocabulary-shift redirect). The
  combinator was already the strictly-more-abstract variadic fold; eliminating its specialization
  leaves shrinks the node count without re-asserting the rotation. No 1:1 rename smell. PASS.
- **variant-axis-coverage (pass).** The over-unification guard holds and is explicit: `dot` /
  `nrm2` / `inner_product` (reduce-to-`Scalar`, different codomain + combining step) are correctly
  OUT of RE6 scope and left standalone; I confirmed the deletion block (B) names only the 4
  `linear_combination` members at each of L2/L3, and that dot/nrm2/inner_product retain their
  SUMMARY + index rows. The arity axis (1/2/2/3) is preserved as the per-arity table rows. PASS.
- **cross-reference-integrity (FAIL).** Load-bearing for this destructive refactor. The 8 target
  files all exist and are correctly slated for deletion; the EXCLUDED set is correct (L1 leaf
  files + concept pages carrying `[scal](./scal.md)` resolve to the non-deleted `L1/scal.md` /
  `concepts/scal.md`, verified — they must NOT be touched, and the report excludes them); the
  combinator chapters + their `### Arity specializations` headings (L2 `:94`, L3 `:53`) +
  insertion points exist as cited; the 8 SUMMARY lines (106/107/108/113/154/155/156/159) are
  exactly the leaf entries and neither group goes empty after removal; the cross-Part L3-L2 links
  (`:134`, `:259`, `:260`) are correctly enumerated. HOWEVER, the report's per-line enumeration —
  which it bills as "exhaustive against this dispatch's grep" — MISSES four live markdown links to
  deleted files, and for one of them actively asserts (wrongly) "no dangling-link risk." Each is a
  hard `linkcheck2` exit-101 if the integrator follows the report's per-line guidance literally
  (the report's own closing post-edit grep WOULD catch all four, but only if the integrator runs
  it and does not trust the "exhaustive" enumeration). See Issues 1–4. FAIL.
- **edge-label-fidelity (pass).** No L_{n+1}→L_n edge claim; the demotion is purely in-layer (L2
  leaves → L2 combinator section, L3 leaves → L3 combinator section), correctly stated as
  "layer placement unchanged." PASS.
- **plan-kind-consistency (pass).** Declared as a replace-and-propagate combinator refactor
  (RE6 discharge by elimination, not grounding); content shape matches — fold-in + delete +
  de-register + re-point, no new chapter, no rank/liveness change to the combinator. PASS.
- **skill-uptake-survey (pass).** The report references the `tools/citecheck` self-verification
  provenance (cycle-052) and provides an explicit post-edit verification grep recipe. Adequate
  telemetry for a mechanical refactor. PASS.

### Issues found

**Issue 1 — SEVERITY HIGH (dangling-link, false "no risk" assertion). `book/src/L2/index.md:161`
carries THREE live links to deleted files, but the report explicitly declares it safe.**
Group D (CYCLE.md lines 232–238) lists the §Working-Notes bullets that name the leaves —
"`e.g. :155 …, :164 …, :161/:165 cohort narratives`" — and asserts: "These bullets carry
inline-code leaf names (no live links), so the edit is prose-only — no dangling-link risk."
This is FALSE for `:161`. Line 161 (the "Cycle-043 leaf-cohort floor batch" Working-Notes
bullet) contains live markdown links `[`axpy`](./axpy.md)`, `[`axpby`](./axpby.md)`,
`[`axpbypcz`](./axpbypcz.md)`. If the integrator follows the report's "prose-only, no
dangling-link risk" guidance for the Working-Notes bullets, three links to deleted files survive
→ hard `linkcheck2` exit-101. The links must be re-pointed (or de-linked to inline-code) like
every other deleted-leaf link.

**Issue 2 — SEVERITY HIGH (dangling-link, omitted from enumeration). `book/src/L3/index.md:52`
(`elementwise_product` dep-map row) carries live `[`scal`](./scal.md)`.** Group D for
`L3/index.md` (CYCLE.md lines 242–264) enumerates the dropped dep-map rows (:39/:40/:41/:46),
the combinator row (:44), the retained-operator rows it deems link-bearing (`divfree-projector`
:68) vs inline-code (`chebyshev`/`krylov-step`/`eigsolve-impl`/`lanczos_step`), and the
narrative lines (:26, :29). It does NOT mention the `elementwise_product` dep-map row at :52,
which has a live `[`scal`](./scal.md)` link → dangling on delete.

**Issue 3 — SEVERITY HIGH (dangling-link, omitted). `book/src/L3/index.md:53` (`normalize`
dep-map row) carries live `[`scal`](./scal.md)`.** Same omission as Issue 2 — the `normalize`
dep-map §Dependencies cell links the deleted L3 `scal`; not in the group D enumeration →
dangling on delete.

**Issue 4 — SEVERITY HIGH (dangling-link, omitted). `book/src/L3/index.md:81` (`orthogonalize`
dep-map row) carries live `[`axpy`](./axpy.md)`.** Group D names several retained-operator index
rows but not `orthogonalize`'s dep-map row at :81, which links the deleted L3 `axpy` → dangling
on delete. (Note: the report DOES correctly handle `orthogonalize.md`'s own intra-chapter links
at :216/:405/:409 in group E — this miss is the `L3/index.md` dep-map row, a different file.)

**Net cross-reference picture.** No whole FILE is missed (every file carrying intra-Part
deleted-leaf links is covered by group D or E); the gap is four LINE-level live links inside
`L2/index.md` and `L3/index.md` whose §Dependencies / Working-Notes cells the report either
omitted or mis-classified as link-free. The report's claim that the group-E/D enumeration is
"exhaustive against this dispatch's grep" does not hold — re-running the report's own grep #1/#2
surfaces these four (`L2/index.md:161` ×3 links, `L3/index.md:{52,53,81}`). The fix is mechanical
(re-point each to `./linear_combination.md#arity-specializations`, preserving link text as the
readout label), and the report's closing post-edit grep is a correct safety net — but the
"no dangling-link risk" assertion for `:161` is actively misleading and the per-line list is
incomplete, so a reviewer/integrator trusting the enumeration over the grep would ship dangling
links.

**Non-blocking observation (NOT a check failure).** Several bare-code (non-link) stale prose
mentions of the deleted files survive in supporting-evidence/working-note prose the report does
not address — e.g. `L2/jacobi-smoother.md:524` (`book/src/L2/scal.md` …), `L3/linear_combination.md:167`
(`book/src/L3/axpy.md` …), `L3/elementwise_product.md:166`, `L3/normalize.md:158`,
`L3/reciprocal.md:155`, `L3-L2/orthogonalize-variant-split.md:293`. These are inline-code text
spans with NO `(./…)` link target, so they are NOT linkcheck2 errors and do not block the build;
they are stale references that will read as pointing at files that no longer exist on disk. Worth
a sweep but out of the hard-error scope; flagged for the integrator/repairer's awareness, not as
a cross-reference-integrity failure.

---
repaired_at: 2026-06-07T124500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

## Repair

### Fixes attempted

- **Finding (Issue 1)**: `book/src/L2/index.md:161` carries THREE live links (`[`axpy`](./axpy.md)`,
  `[`axpby`](./axpby.md)`, `[`axpbypcz`](./axpbypcz.md)`) but the report's group-D Working-Notes
  bullet wrongly asserts "no dangling-link risk."
  - **Decision**: repaired
  - **Action**: Verified all three live links on-disk at `book/src/L2/index.md:161` (the
    cycle-043 leaf-cohort-floor-batch bullet, clause "(i) the fold-PARENTED arity-family leaves
    of `linear_combination`"). Edited CYCLE.md group D (`L2/index.md` block): removed the false
    "no dangling-link risk" claim by dropping `:161` from the inline-code-only bullet list and
    added an explicit CORRECTION sub-bullet instructing the integrator to re-point all three
    links to `./linear_combination.md#arity-specializations` (link text preserved as readout
    label) + reword the stub framing. Mechanical re-point — squarely in repair authority
    ("trivial cross-reference fix, broken `[link]` to a renamed/deleted file").

- **Finding (Issue 2)**: `book/src/L3/index.md:52` (`elementwise_product` dep-map row)
  §Dependencies cell carries live `[`scal`](./scal.md)`, omitted from the group-D enumeration.
  - **Decision**: repaired
  - **Action**: Verified live on-disk (`Sibling-subsumes [`scal`](./scal.md)` at `:52`). Added a
    CORRECTION sub-bullet to CYCLE.md group D (`L3/index.md` block) re-pointing it to
    `./linear_combination.md#arity-specializations`.

- **Finding (Issue 3)**: `book/src/L3/index.md:53` (`normalize` dep-map row) §Dependencies cell
  carries live `[`scal`](./scal.md)`, omitted.
  - **Decision**: repaired
  - **Action**: Verified live on-disk (`[`scal`](./scal.md) (the rescale `û = scal(1/β, x)`…)`
    at `:53`). Added to the same group-D CORRECTION sub-bullet, re-pointed to
    `./linear_combination.md#arity-specializations`.

- **Finding (Issue 4)**: `book/src/L3/index.md:81` (`orthogonalize` dep-map row) §Dependencies
  cell carries live `[`axpy`](./axpy.md)`, omitted.
  - **Decision**: repaired
  - **Action**: Verified live on-disk (`[`axpy`](./axpy.md) (the residual update `w − H_j·V[j]`…)`
    at `:81`). Added to the same group-D CORRECTION sub-bullet, re-pointed to
    `./linear_combination.md#arity-specializations`.

- **Finding (non-blocking observation)**: stale bare-code (non-link) prose mentions of deleted
  files survive in supporting-evidence/working-note prose (e.g. `L2/jacobi-smoother.md:524`,
  `L3/linear_combination.md:167`, `L3/elementwise_product.md:166`, `L3/normalize.md:158`,
  `L3/reciprocal.md:155`, `L3-L2/orthogonalize-variant-split.md:293`).
  - **Decision**: not-needed (left for awareness; not a repair-authority item)
  - **Rationale**: The critic explicitly classified these as NON-errors — they are inline-code
    text spans with NO `(./…)` link target, so they are not `linkcheck2` errors and do not block
    the build. Sweeping them is a content-quality judgment across ~6 supporting files (deciding
    whether each stale `book/src/L*/<leaf>.md` mention should be re-texted vs left as historical
    provenance), which is not mechanical/surgical. The report's post-edit grep (group E) keys on
    `(./…)` link syntax and correctly does NOT flag these — consistent with them being build-safe.
    Left flagged for the integrator's optional awareness sweep; does NOT gate `ready`.

### Unrepairable findings

None. All four hard-error (dangling-link) findings in the FAIL'd `cross-reference-integrity`
check were mechanical re-point omissions / one mis-classification, each verified live on-disk and
corrected in CYCLE.md by adding the explicit re-point instruction. No substantive authoring was
required.

## Suggested resolution

`ready`. The four previously-omitted/mis-classified live links (`L2/index.md:161` ×3,
`L3/index.md:{52,53,81}`) now each carry an explicit re-point instruction to
`./linear_combination.md#arity-specializations` in CYCLE.md groups D, matching the disposition of
every other deleted-leaf link in group E. The full set of links-to-deleted-files is now covered.

Integrator notes:
- After applying groups A–E **plus the two CORRECTION sub-bullets added this repair pass**, run
  the report's group-E post-edit grep recipe (`grep -rn -E '\((\.\./)?(L2|L3)/(axpy|axpby|axpbypcz|scal)\.md' book/src/`
  and the intra-Part variant) — it MUST return zero hits before `cargo make book`. This grep is
  the authoritative safety net and will catch any link the per-line enumeration still missed.
- Honor the EXCLUDED list precisely (group E): `[`scal`](./scal.md)` / `[`axpy`](./axpy.md)`
  links inside `book/src/L1/*` and `book/src/concepts/*` resolve to the NON-deleted L1 leaves /
  concept pages and must NOT be retargeted.
- Optional (non-blocking): the stale bare-code prose mentions noted above may be swept for
  readability, but they are not build errors and do not block integration.
