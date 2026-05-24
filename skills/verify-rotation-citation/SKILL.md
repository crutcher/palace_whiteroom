---
name: verify-rotation-citation
description: Verify a rotation_claim end-to-end — citation chain, mutation/ownership accuracy, test consistency, missing cases, load-bearing-trick classification. Produces a critic_verdict. Invoke per claim during the Critic cycle.
status: active
---

# verify-rotation-citation

The Critic's per-claim verification workflow. Adversarial — finds errors, not agreement.

## When to invoke

- **Critic**, once per rotation_claim produced by the Synthesizer in a cycle.

## Inputs (prefetched by orchestrator)

- The rotation_claim JSON.
- The cited source ranges (text fetched ahead of time; do not re-fetch).
- Any tests cited or named in `scaffolding/test-linkages/` for the source range.
- The prior-layer claim(s) (Li-1 forms the from_form is rotating from).
- The current `concepts/` library state for any primitive referenced.

You do NOT see the Synthesizer's chain-of-thought. You do NOT see the in-flight cycle's scaffolding. Only the claims, the cited source, and the persistent project state.

## Procedure

For each rotation_claim, evaluate sequentially:

1. **Citation supports `from_form`?** Read the cited source range; does it contain the structure `from_form` asserts? If not → `citation_does_not_support`.

2. **Reduction mechanical?** The justification's argument — does it skip steps or hand-wave? An L1→L2 algebraic argument that elides which kernel-fusion is being unfolded is suspect → `rotation_chain_breaks`.

3. **Mutation pattern accurate?** For L0→L1: does the cited source actually exhibit the mutation pattern claimed (`in_place_overwrite` vs `accumulator` vs `alias_with_input` vs `scratch_buffer` vs `pure`)? Look for the destination buffer's use: is it read first then written (accumulator) or just written (overwrite)? Is it the same buffer as one of the inputs (alias)? → `mutation_pattern_mismatch`.

4. **Ownership accurate (L4 only)?** For L3→L4: does the L4 form correctly distinguish sim state (evolves) / operator internal params (closure-held, constant during solve) / ephemeral intermediates (per-step, doesn't survive)? Misclassification of a closure-held matrix as sim state, or a per-step temp as state, → `ownership_misclassified`.

5. **Missing cases?** Does the source have error paths, special branches, edge conditions that the rotation doesn't address? An L1 claim that omits a branch is missing the branch's semantics → `missing_case`.

6. **Load-bearing vs transparent classification?** A numerical trick (non-associative reduction ordering, mixed precision, fast-math, deterministic-vs-atomic) marked transparent when it changes results under naïve reformulation → `load_bearing_trick_classified_as_transparent`. When in doubt, mark `unclear` and let the human triage.

7. **TEST CONSISTENCY.** Where tests exist (cited by Synthesizer, listed in `scaffolding/test-linkages/`, or discoverable via the `find-tests-for-region` skill), do the test inputs and assertions support the L1 mutation pattern and the L2/L3 algebraic claims? A test assertion contradicting a claim → `citation_does_not_support` (tests are L0-equivalent evidence).

8. **Labored rotation?** Is the rotation technically correct but obviously forced — special cases, exception branches, forced-fit transformations? → `labored_rotation_push_back_candidate`. Include a `push_back_suggestion`: which lower-layer change would eliminate the friction?

## Verdict assembly

- If issues found are all `unclear` or `labored_rotation_push_back_candidate` → verdict = `revise` (claim is on the right track but needs refinement).
- If issues include `citation_does_not_support`, `rotation_chain_breaks`, `mutation_pattern_mismatch`, `ownership_misclassified`, `missing_case`, or `load_bearing_trick_classified_as_transparent` → verdict = `revise` or `reject` depending on severity.
- No issues → verdict = `pass`.

## Cross-cycle pattern → `lesson`

If you notice a pattern across the cycle's claims — the Synthesizer consistently misclassifying mutation, two slices' L3 forms hinting at a missing shared primitive — write a one-sentence `lesson` for `lessons.md`. Lessons are cheap and disproportionately effective.

## Output

A single JSON object validating against `schemas/critic_verdict.json`. Nothing outside the JSON. (The orchestrator handles `lessons.md` append and `episodic.jsonl` write.)

## Friction → `problems/`

If the verdict schema's `kind` enum doesn't have a category for what you're seeing, or the Synthesizer's diff is structurally hard to evaluate (mixed concerns in one diff, claims that span multiple edges without separation), file as a `problems/` entry.
