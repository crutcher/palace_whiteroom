# tools/scratch

Sandbox for grab-bag evaluation work — symbolic execution, quick numeric checks, throwaway scripts, anything that doesn't merit its own named tool directory yet.

## Rules (or lack thereof)

- **Free to mutate, delete, restructure.** This space is exempt from the append-only structural discipline that applies to `scaffolding/`, `skills/`, and named tools under `tools/<name>/`.
- **Subdirectories for separation.** When multiple investigations coexist, give each its own subdirectory: `scratch/cg-residual-check/`, `scratch/2026-06-04-axpy-equivalence/`. Loose files at the top level get confusing fast.
- **Promote when it crystallizes.** When a scratch experiment becomes a tool worth re-running, move it to `tools/<named-tool>/` with its own README and (for Python) its own venv. See `tools/README.md` *Promotion from scratch*.
- **No secrets, API keys, or large data dumps.** The `.gitignore` covers `.venv` and common cache patterns; everything else is your responsibility. If you accidentally commit a secret, rotate the credential immediately and use `git rm` + a follow-up commit (don't try to rewrite history).

## Python expectations

Either:

- **Use the system Python via inline commands** (the `python3 -c "import jsonschema; ..."` style) when deps are common.
- **Set up a scratch-local venv** (`tools/scratch/.venv/` or `tools/scratch/<subdir>/.venv/`) when deps are non-trivial.

Both are gitignored. Document setup in the subdirectory's own README if it grows enough to warrant one.

## When NOT to use scratch

- **Persistent verification tooling** — promote to a named `tools/<name>/` directory.
- **Anything an agent should invoke procedurally** — that's a `skills/` entry pointing at a `tools/<name>/` execution.
- **Methodology questions** — that's `scaffolding/decisions/` or `problems/`, not scratch.

## Current contents

(none yet — first scratch experiment lands as needed)
