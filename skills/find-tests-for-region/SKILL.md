---
name: find-tests-for-region
description: For a Palace source region (file or symbol), find unittests that exercise it; check scaffolding/test-linkages/ before re-discovering; write back new linkages. Invoke whenever the Explorer (or Critic) needs tests as semantic evidence.
status: active
---

# find-tests-for-region

A test that constructs an input, calls a function, and asserts on the result is **L0-equivalent evidence** — equal-status to source for verification (see CLAUDE.md *Tests as semantic supplement*). This skill is the workflow for finding those tests.

## When to invoke

- **Explorer**, after localizing a source region and before producing L1 claims.
- **Critic**, when verifying a rotation_claim and tests have not been surfaced.
- **Synthesizer**, when an `empirical_match` justification is plausible.

## Procedure

1. **Check `scaffolding/test-linkages/` first.** Look for a per-area file matching the source region's topic (`linalg/vector.cpp` → `scaffolding/test-linkages/vector.md`). If found, use the known linkages; if incomplete, you'll write back.

2. **Search by name in `reference/palace/test/unit/`.** Use `search_text` (or grep) for: the function/class/type name; the source file's base name; topic-keyed file matches (`test-<topic>.cpp`).

3. **Verify the linkage.** A test name implies a likely topic, not guaranteed coverage. Read the test's `#include`s and call sites to confirm it exercises the source region. Don't assume.

4. **Cite tests alongside source.** Same format: `palace/test/unit/test-<topic>.cpp:start-end`. Same evidence weight.

5. **Write back to `scaffolding/test-linkages/`.** When you discover or refine a linkage, update or create the per-area file. Minimum content: source file(s), test file, test name(s), one-line note per test on what it pins (mutation pattern / algebraic equivalence / load-bearing-trick evidence / boundary case).

## Edge cases

- **No test found.** Note "no test found for <region>" and proceed. Tests are supplement, not prerequisite.
- **Multiple test files cover the same source.** Cite all; the scaffolding entry lists all linkages.
- **One test covers multiple source files.** Primary linkage goes in the matching area file; cross-references in others.
- **End-to-end example tests** (`test/examples/`) are valid evidence but coarser than unit tests — prefer unit tests for fine-grained semantic claims.

## What this skill is NOT

- Not test-running (that's Phase 7 execution grounding).
- Not test authoring (Palace's tests are input; we don't add to them).

## Friction → `problems/`

Per `skills/README.md`, recurring difficulties with this skill — `scaffolding/test-linkages/` format not accommodating a case, an MCP-tool gap that makes the procedure 10x harder than it should be, a Palace subsystem where test/source linkage is fundamentally untrackable — file as a `problems/` entry for meta-review.
