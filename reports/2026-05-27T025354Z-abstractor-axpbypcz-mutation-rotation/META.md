---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T030000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T031500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of L1>L0 theme sketch — axpbypcz-mutation-rotation

## Critique

### Checks run

**citation-validity** — Spot-checked all cited Palace ranges. Member-form
trampoline at `vector.cpp:381-386` confirmed (sig at 381, delegation at 385,
brace 386). Static member body cited as `388-455` is correct (sig 388, body
opens 391, closes at 455). γ==0 branch cited at `vector.cpp:402-426` confirmed
(line 402 holds the `if (gamma == 0.0)` test). Free-fn γ==0 branch cited at
`vector.cpp:749-751` confirmed. **Minor warning**: the three free-function
specialisation ranges cited as `745-758`, `760-765`, `767-772` are each
off-by-one — the `template <>` line precedes each by one (actual ranges
`744-758`, `759-765`, `766-772`). The signatures and bodies are correct; only
the `template <>` line is excluded. Worth surfacing because the L0 spec relies
on these ranges being exactly quotable.

**surface-or-evidence** — The proposal is the creation of a new theme file
(`book/src/L1-L0/axpbypcz-mutation-rotation.md`) with full surface authored,
plus a SUMMARY.md insertion. This is firmly surface-shaped, not pure rotation
claim — pass.

**rotation-quality** — Not a refinement; this is the first articulation of the
edge L1>L0 for `axpbypcz`. The four sub-patterns are a structural enumeration,
not a renaming. The γ==0 sub-rule compresses a 3-vector form into a 2-vector
form (more compact at L1), which is a genuine algebraic rotation, not a
1:1 mapping. Pass.

**variant-axis-coverage** — Four sub-patterns cover the (real-scalar,
complex-scalar) × (real-vector, complex-vector, member-vs-free) cross-product
explicitly. Scalar-promotion sub-axis is explicitly scoped out as covered
upstream in L1. Inner imaginary-scalar branches in the member-form are
explicitly classified as transparent and *not* sub-patterns. Open question #5
documents the scope-out reasoning. Pass.

**cross-reference-integrity** — All `[link]` references resolve:
`L1/axpbypcz.md`, `L1/axpby.md`, `L1/axpy.md`, `L1-L0/axpby-mutation-rotation.md`
all exist in `book/src/`. `scaffolding/decisions/axpby-as-primitive.md` exists.
Pass.

**edge-label-fidelity** — The proposal's edge label is L1>L0 and the prose
discusses exactly that edge (L1 `axpbypcz` lowered into L0 Palace
specialisations). Pass.

**plan-kind-consistency** — Declared `Status: rough-in`. Content shape matches:
sub-pattern recognition rules sketched, but exhaustive corpus audit is
deferred to a `lowering-verifier` invocation. The reported call sites are
"illustrative, not exhaustive". Consistent with rough-in semantics. Pass.

**skill-uptake-survey** — The report's shape implies relevant skills exist
(`verify-refinement-surface`, `verify-citation-range`, `classify-variant-axis`).
The report makes no mention of invoking any of these. The minor off-by-one
citation errors in three locations suggest `verify-citation-range` would have
been useful and was likely not consulted. Telemetry warning, non-blocking.

### Issues found

1. **citation-validity (warning)** — Three free-function template
   specialisations are cited as `vector.cpp:745-758`, `760-765`, `767-772`,
   but the actual ranges begin one line earlier on the `template <>` token:
   `744-758`, `759-765`, `766-772`. Locations in report: Citations under
   sub-patterns A, B, D; and the `## Verified-against` block. Severity: minor
   — bodies and signatures are within range, but the `template <>`
   specialisation marker is excluded.

2. **skill-uptake-survey (warning)** — No skill invocations referenced.
   Pattern of off-by-one citation ranges (Issue #1) suggests
   `verify-citation-range` would have been useful. Severity: low; telemetry.

3. **methodology-novelty advisory (non-blocking observation)** — The
   "first mixed-justification sub-rule" claim is verified against
   `book/src/L1-L0/axpby-mutation-rotation.md` (precedent theme has only
   pure-structural and pure-algebraic sub-rules; no mixed). The claim is
   genuinely novel. The report self-flags this via Open Question #2 and
   requests `cross-layer-cross-cutter` review. No action needed by repairer,
   but integrator should ensure the methodology-attention flag survives the
   apply step.

4. **scope-confidence on Sub-pattern B (non-blocking)** — Verified via
   `grep -rn 'AXPBYPCZ'` across Palace source that no call site exists for
   the complex-complex free-function form (sub-pattern B); all complex
   uses go either via member-form directly or via the real-on-complex
   free-function (sub-pattern D). The "defined-not-used trampoline"
   characterization is empirically correct against the current corpus.
   Report's Open Question #4 already flags the exhaustive-audit
   responsibility appropriately.

## Repair

### Fixes attempted

- **Finding**: citation-validity warning — three free-fn template
  specialisation ranges (`745-758`, `760-765`, `767-772`) alleged off-by-one
  (critic claimed `template <>` line precedes each by one).
  - **Decision**: not-needed.
  - **Rationale**: Re-verification of `palace/linalg/vector.cpp` shows the
    `template <>` tokens are on lines **745, 760, 767** respectively (per
    `grep -n "template <>" vector.cpp`), which are already the start lines
    of the cited ranges. The cited ranges therefore already include the
    `template <>` specialisation markers; they are NOT off-by-one. The
    critic's claim that `template <>` lives one line earlier (at 744, 759,
    766) does not match the source. No edit applied — applying the
    suggested shift would broaden ranges to include preceding blank lines
    or the prior function's closing brace. Repairer authority is
    mechanical; overriding a critic finding with a content-bearing
    counter-claim about source layout is borderline, but the source
    evidence is direct and unambiguous (see `grep -n` output recorded in
    the repair trace), so marking not-needed rather than escalating.

- **Finding**: skill-uptake-survey warning — no `skill_uptake:`
  frontmatter block in CYCLE.md.
  - **Decision**: repaired.
  - **Action**: Added `skill_uptake:` block to CYCLE.md frontmatter
    (between `status:` and `inputs:`) listing the three applicable skills
    (`verify-citation-range`, `verify-refinement-surface`,
    `classify-variant-axis`) under `applicable_but_not_used:` with an
    explicit `consulted: []` and a rationale noting this was a
    retrospective repairer-added record.

### Unrepairable findings

None. The two flagged findings are resolved: one as not-needed (citation
ranges verified correct against source), one as repaired (frontmatter
added).

## Suggested resolution

`ready` — integrator may apply the SUMMARY edit and the new theme file
under `book/src/L1-L0/axpbypcz-mutation-rotation.md` as proposed. Note for
integrator: the methodology-novelty advisory (mixed-justification
sub-rule, critic finding #3) is non-blocking but should survive into
post-apply visibility — the report's Open Question #2 explicitly requests
`cross-layer-cross-cutter` review of the framing in a later cycle.
