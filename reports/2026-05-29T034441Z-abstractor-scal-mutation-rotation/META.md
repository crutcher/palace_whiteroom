---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T040447Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-05-29T041530Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L1>L0 theme — scal-mutation-rotation (stub→firm)"

## Critique

### Checks run

**citation-validity — warning.** I independently re-read every cited L0 range via
`palace-codemap read_range` against `reference/palace/`. The core surface citations
are all **line-exact**: `vector.hpp:98-99` (line 98 = `// Scale all entries by s.`,
line 99 = `ComplexVector &operator*=(std::complex<double> s);`); `vector.cpp:203-227`
(signature 203, `if (si == 0.0)` at 207, the two-real-call branch `Real() *= sr;
Imag() *= sr;` at 209-210 within 207-211, the general `forall_switch` complex kernel
with the `XR/XI` cross-term at 212-225, `return *this;` at 226); `vector.hpp:262-270`
(`Normalize` template; `x *= 1.0 / norm;` exactly on line 268). The GMRES sites are
exact: `iterative.cpp:632` and `:811` both `w *= 1.0 / Hj[j + 1];`; the
`iterative.cpp:222` `cs *= w;` non-instance is correctly identified as a
scalar-scalar plane-rotation `*=`, not a vector `scal`. The `operator.cpp:661`
(`Normalize(comm, u);`) and `:673` (`l = Normalize(comm, u);`) call sites are exact.
All four test sites are exact: `test-orthog.cpp:193` (`V[0] *= 1 / v0_norm;`,
preceded by the `CHECK_THAT(v0_norm, ...)` at 192), `test-orthog.cpp:208`
(`V[1] *= 1 / v1_norm;`), `test-lumpedportintegration.cpp:394` (`RHS *= 0.5;` on a
`ComplexVector`), and the second instance at `:746`. The named zero-hit absence is
real: `linalg::Scal`/`linalg::Scale` free-function symbols return no hits; the only
`Scale` matches are the unrelated `ScaleType` eigenvalue-scaling enum and the
`// Scale all entries by s.` comment — neither a vector-scal free function. The
warning is driven by one inline-anchor-drift instance (see Issues #1) plus a
stale-OQ reference (#3) and a maturity-mischaracterization (#2) — substance is sound,
but two anchors do not point where the prose says.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (stub→firm
promotion of an existing theme) that modifies surface (rewrites the full
`L1-L0/scal-mutation-rotation.md` chapter, the `L1-L0/index.md` row, the SUMMARY
entry) AND supplies rotation/lowering evidence (positive L0 sites + two
empirical-match tests). The "no scalar-value constant-folding" claim is substantiated:
I confirmed the sibling `axpby-mutation-rotation` does carry α==1 (sub-pattern B) and
α==-1 (sub-pattern C) value-folding branches, so the contrast is accurate; `scal`'s
only L0 branch is the `imag(s)==0.0` *shape* branch, correctly distinguished from a
*value* branch. The no-aliasing-precondition claim (element-local: `x[i]` depends only
on `x[i]`, no separate read buffer) is sound and is the genuine structural reason the
`scal` lowering is simpler than `axpby`'s. The empirical-match test corroboration is
real and direct (real path + real-on-complex promotion path).

**rotation-quality — pass.** The theme narrates forward, high→low: pure L1 `scal(α, x)
= α·x` (carrying no destination buffer) lowers into the in-place L0 `x *= α` receiver
mutation. The rotation is faithful — the L1 form genuinely hides the in-place
overwrite / destination buffer that the L0 form materializes, which is exactly the
mutation rotation. Not a renaming or 1:1 mapping: the L1→L0 step reintroduces buffer
identity and the receiver-mutation calling convention. Pass.

**variant-axis-coverage — pass.** The two orthogonal axes are covered explicitly:
(a) element type — real path (sub-pattern A, `mfem::Vector::operator*=(double)`) vs
complex path (sub-pattern B, `ComplexVector::operator*=(std::complex<double>)`); and
(b) scalar promotion (real α against complex x) — handled inside sub-pattern B via the
`s.imag()==0.0` branch, classified as a transparent shape-specialisation. The
complex-α-against-real-x combination is explicitly scoped out ("no L0 overload and
does not occur in the corpus", Applicability condition 2). The classification of the
`imag(s)==0.0` branch as transparent (algebraically `(sr+0i)·x = sr·x`, disappears at
L1) is consistent with the independent classification in
`concepts/scalar-promotion.md` (which cites the identical `vector.cpp:207-211` /
line-207 anchors). No hidden branches.

**cross-reference-integrity — warning.** All `[link]` targets resolve as files
(`L1/scal.md`, `L1-L0/{axpby,axpbypcz,nrm2}-mutation-rotation.md`,
`L0/linalg-free-functions.md`, `concepts/scalar-promotion.md`, `L1-L0/index.md`,
`SUMMARY.md` all exist), and the existing stub at
`L1-L0/scal-mutation-rotation.md` is confirmed `status: stub` (so the promotion shape
is correct). However: the `normalize-fused-primitive` OQ slug does not resolve to any
registered OQ (Issue #4); two sibling themes are mislabeled "firm" (Issue #2); and the
`scalar-promotion-typing-rule` reference points at an OQ that is already resolved
(Issue #3). Link resolution passes; named-slug / status fidelity does not.

**edge-label-fidelity — pass.** The declared edge is L1>L0 and the prose narrates that
exact edge throughout (L1 form LHS → L0 form RHS, forward lowering), consistent with
the high→low discipline. The "Lifting note" (reverse L0→L1 direction) is correctly
quarantined to the CYCLE.md working notes and explicitly excluded from the formal
chapter content. No edge mismatch.

**plan-kind-consistency — warning.** The declared kind (firm L1>L0 theme) matches the
content shape — exhaustively-cited structural rewrite, no rough-in placeholders, no
constructive sub-part (correctly contrasted against `partly-constructive`
`eigsolve-mutation-rotation`), positive zero-hit corpus result rather than a
negative-anchor reconstruction. The chapter body follows the firm-theme house style
(no YAML frontmatter, `## Status: firm` section, matching the firm
`nrm2-mutation-rotation`). The warning is for the proposed-changes edit-target
ambiguity (Issue #5): the `edit:book/src/SUMMARY.md` block is a bare line that must
be applied as an *in-place de-stub* of the existing line 84 (`- [scal-mutation-rotation
(stub)](...)`), not an append — a naive append would duplicate the SUMMARY entry or
leave the stale `(stub)` label. The `edit:book/src/L1-L0/index.md` block uses the
verbatim nrm2 row as an insert-after anchor, which is the established idiom but is also
implicit. Content classification is correct; edit-application targets are
under-specified.

**skill-uptake-survey — warning.** The report references no skills by name. For this
shape (firm theme promotion with citation + rotation + variant-axis content),
`verify-citation-range`, `verify-rotation-citation`, `verify-refinement-surface`, and
`classify-variant-axis` are all applicable and exist under `skills/`. The report does
self-verify citations via codemap `read_range` (which I confirmed was accurate), but
does not invoke or cite the verification skills. Non-blocking telemetry only.

### Issues found

**Issue #1 — inline-anchor-drift in the `nleps.cpp` normalization citation (moderate).**
CYCLE.md "Verified-against" block (line 211-213) and §Speculative-operators cite
`palace/linalg/nleps.cpp:486-491` with inline anchors `c *= 1.0/norm_c;` (488),
`c2 *= 1.0/norm_c;` (489), and `v *= 1.0/norm_v;` (**491**). I verified: lines 488 and
489 are exact, but `v *= 1.0 / norm_v;` is at line **492**, not 491. Line 491 is the
`double norm_v = std::sqrt(...);` declaration. Consequently the cited *range*
`486-491` ends one line short of the `v *= ...` statement it claims to contain, and
the per-citation audit-table note (CYCLE.md:271) repeats the wrong "(491)" anchor. The
recurring inline-anchor-drift pattern flagged for this cycle. Location:
CYCLE.md §Verified-against citation `nleps.cpp:486-491` (lines 211-213, 268-271).

**Issue #2 — two sibling themes mischaracterized as "firm" (moderate).** The report
asserts it is "a sibling of the **firm** `axpby-mutation-rotation` /
`axpbypcz-mutation-rotation` / `nrm2-mutation-rotation` themes" (CYCLE.md:39-41) and
"the fourth-and-last BLAS-1 floor lowering theme" (CYCLE.md:41). On inspection only
`nrm2-mutation-rotation.md` is `firm` (Status line 225). `axpby-mutation-rotation.md`
is **`rough-in`** (Status line 226) and `axpbypcz-mutation-rotation.md` is
**`rough-in`** (Status line 318). The "fourth-and-last … floor" framing overstates the
completeness of the BLAS-1 lowering floor (two of the four siblings are still
rough-in). The links resolve, but the "firm" characterization is inaccurate for two
of three. Location: CYCLE.md §Summary (lines 39-41); the same "sibling" phrasing in the
proposed chapter (lines 51-54) does not assert "firm" and is fine.

**Issue #3 — stale reference to a resolved OQ `scalar-promotion-typing-rule`
(moderate).** The report treats `scalar-promotion-typing-rule` as a live open question
("see ... and open question `scalar-promotion-typing-rule`", CYCLE.md:155-156; listed
under "Open questions / caveats" as "(existing OQ)" whose "typing rule itself remains
the OQ's concern", CYCLE.md:339-343). The ledger
(`scaffolding/open-questions.md:239`) records this OQ as **resolved cycle-005** —
`concepts/scalar-promotion.md` formalizes the real⊑complex rule. The substance the
report defers to (the concept page) exists and is the resolution, so the technical
content is not wrong, but the OQ-status framing is stale (cites a closed OQ as open).
Location: CYCLE.md Applicability condition 2 (line 155-156), §Open-questions first
bullet (line 339-343).

**Issue #4 — dangling `normalize-fused-primitive` OQ slug (minor).** The report
references "an existing open question (`normalize-fused-primitive`, recorded at
`L1/scal` §Dependencies)" (CYCLE.md:187-188, :344-352) and instructs the planner on it.
The named slug `normalize-fused-primitive` appears neither in `book/src/L1/scal.md`
(its §Dependencies discusses the fused-normalize question in prose at line 85 but
carries no such slug) nor in `scaffolding/open-questions.md`. The underlying question
is genuinely discussed, but the slug does not resolve to a registered OQ — it reads as
an invented/informal handle. Location: CYCLE.md §Speculative-L1-operators (line
187-189), §Open-questions second bullet (lines 344-352).

**Issue #5 — SUMMARY.md edit-target ambiguity (minor).** The
`edit:book/src/SUMMARY.md` proposed-changes block (CYCLE.md:315-317) is a bare line
`- [scal-mutation-rotation](./L1-L0/scal-mutation-rotation.md)` with no anchoring
context. The current SUMMARY.md line 84 is
`- [scal-mutation-rotation (stub)](./L1-L0/scal-mutation-rotation.md)`. The edit must
be applied as an **in-place de-stub** (drop the ` (stub)` label) of line 84, not an
append — otherwise a duplicate SUMMARY entry results or the stale `(stub)` label
persists. The intent is clear from context but the edit block does not encode the
replace-target. (The `edit:book/src/L1-L0/index.md` block similarly relies on the
verbatim nrm2 row as an implicit insert-after anchor; that is the established idiom but
worth noting.) Location: CYCLE.md §Proposed-changes (lines 310-317).

**Issue #6 — `scal-mutation-rotation-l1-l0-theme` closure target is a rolled-up
constituent, not a standalone OQ (minor).** CYCLE.md:365-366 declares OQ
`scal-mutation-rotation-l1-l0-theme` "closed by this theme" and instructs the
integrator to "mark it resolved/migrated in the ledger." In the ledger this slug is a
*constituent* listed inside the migrated plan item `blas1-l1-l0-lowering-theme-gap`
(`scaffolding/open-questions.md:25`), not a standalone entry. The closure instruction
is reasonable but the integrator must edit the constituent list at line 25 (and check
whether the parent plan item also needs status movement), not a standalone OQ row.
Location: CYCLE.md §Open-questions final bullet (lines 365-366).

---

## Repair

### Fixes attempted

**Finding #1 — inline-anchor-drift in the `nleps.cpp` normalization citation (moderate).**
- **Decision**: repaired
- **Action**: Re-verified `palace/linalg/nleps.cpp` via codemap `read_range`. Confirmed
  the contiguous block: line 488 = `c *= 1.0 / norm_c;`, line 489 = `c2 *= 1.0 / norm_c;`,
  line 491 = `// Normalize eigenvector estimate.`, line 492 = `double norm_v = std::sqrt(...);`,
  line 493 = `v *= 1.0 / norm_v;`. The `v *= ...` statement is at line **493** (not 491 as
  the prose anchored, and not 492 as the finding's first guess stated — line 492 is the
  `norm_v` declaration). The cited range `486-491` ended two lines short of the statement it
  claimed to contain. Corrected both the range (`486-491` → `486-493`) and the inline anchor
  (`(491)` → `(493)`) in §Verified-against (CYCLE.md:211-213) and the per-citation audit-table
  note (CYCLE.md:268-271). Small-offset citation fix, squarely within repair authority.

**Finding #2 — two sibling themes mischaracterized as "firm" (moderate).**
- **Decision**: repaired
- **Action**: Read the Status sections of the sibling chapters: `nrm2-mutation-rotation.md:225`
  is `firm`; `axpby-mutation-rotation.md:226` is `rough-in`; `axpbypcz-mutation-rotation.md:318`
  is `rough-in`. Rewrote the §Summary sibling sentence (CYCLE.md:39-41) to label each sibling
  with its verified maturity (`nrm2` firm, `axpby`/`axpbypcz` rough-in) and replaced the
  "fourth-and-last … floor" framing with an accurate statement that promoting `scal` leaves
  the BLAS-1 floor incomplete (two siblings still rough-in). The proposed-chapter prose
  (CYCLE.md:51-54) and the index.md row do not assert "firm" for siblings, so no edit there.
  Mechanical fact-correction against verified frontmatter — no content authoring.

**Finding #3 — stale reference to a resolved OQ `scalar-promotion-typing-rule` (moderate).**
- **Decision**: repaired
- **Action**: Confirmed `scaffolding/open-questions.md:239` records `scalar-promotion-typing-rule`
  as `resolved cycle-005` (`concepts/scalar-promotion.md` formalizes the real⊑complex rule). The
  report's substance (deferring to that concept page) was correct; only the open/closed framing
  was stale. Re-anchored both mentions — Applicability condition 2 (CYCLE.md:155-160) and the
  §Open-questions first bullet (CYCLE.md:339-343) — from "open question" / "(existing OQ)" to an
  explicit "resolved cycle-005 — no live OQ remains, recorded for cross-reference only" framing,
  pointing at the resolving concept page. Stale-status correction, mechanical.

**Finding #4 — dangling `normalize-fused-primitive` OQ slug (minor).**
- **Decision**: repaired
- **Action**: `grep` confirmed `normalize-fused-primitive` resolves to no registered OQ anywhere
  in `scaffolding/` or `book/`, and `L1/scal.md` §Dependencies (lines 59-65) discusses the
  fused-normalize question in prose with NO slug attached. The actual registered slug is
  `normalize-as-fused-l1-primitive` (a constituent of the `normalize-l1-primitive-harvest` plan
  item, `open-questions.md:27`). Corrected both references — §Speculative-L1-operators
  (CYCLE.md:187-189) and the §Open-questions second bullet (CYCLE.md:344-352) — to the registered
  slug and dropped the false "recorded at §Dependencies" claim (replaced with "also discussed in
  prose at §Dependencies"). Slug-resolution fix to the obvious correct registered handle.

**Finding #5 — SUMMARY.md edit-target ambiguity (minor).**
- **Decision**: repaired
- **Action**: Confirmed `book/src/SUMMARY.md:84` is
  `- [scal-mutation-rotation (stub)](./L1-L0/scal-mutation-rotation.md)`. Converted the bare
  `edit:book/src/SUMMARY.md` proposed-change block (which read as an append) into an explicit
  in-place de-stub: a "replace the existing line … with …" form showing the old `(stub)`-labelled
  line and the de-stubbed replacement, with a note that a bare append would duplicate or leave
  the stale label. Edit-target disambiguation — encodes the replace-target the prose already
  implied; no content change.

**Finding #6 — OQ-closure imprecision (minor).**
- **Decision**: repaired
- **Action**: Confirmed `scal-mutation-rotation-l1-l0-theme` is a constituent OQ listed inside
  the migrated plan item `blas1-l1-l0-lowering-theme-gap` (`open-questions.md:25`), not a
  standalone ledger row. Rewrote the §Open-questions final bullet (CYCLE.md:365-366) to instruct
  the integrator to strike the constituent slug from the line-25 constituent list (and check
  whether the parent plan item warrants status movement now that `nrm2` and `scal` are firm while
  `dot` is still a stub), rather than edit a standalone OQ row. Closure-note precision fix.

### Unrepairable findings

None. All six findings were mechanical/surgical: a small-offset citation range + anchor fix
(#1), fact-corrections against verified frontmatter / ledger state (#2, #3, #6), a slug-resolution
correction to the obvious registered handle (#4), and an edit-target disambiguation (#5). None
required authoring substantive content or resolving a contradiction reserved for the
human/meta-phase.

## Suggested resolution

`overall_status: ready`. The critic's core checks (surface-or-evidence, rotation-quality,
variant-axis-coverage, edge-label-fidelity) all passed and are untouched. The four warnings
(citation-validity, cross-reference-integrity, plan-kind-consistency, skill-uptake-survey) were
driven entirely by the six mechanical findings above, all now repaired; skill-uptake-survey was
non-blocking telemetry only. No follow-up agent required.

Integrator notes:
- The SUMMARY.md change (Finding #5) is now an explicit **in-place de-stub** of line 84 — drop
  ` (stub)`, do not append.
- The OQ closure (Finding #6) targets the **constituent list** at `open-questions.md:25` inside
  `blas1-l1-l0-lowering-theme-gap`, not a standalone row; consider whether the parent plan item
  needs status movement (BLAS-1 floor: `nrm2` + `scal` firm, `axpby`/`axpbypcz` rough-in, `dot`
  stub — floor not yet complete).
- The `nleps.cpp` citation now reads `486-493` with the `v *= 1.0 / norm_v;` anchor at line 493.
