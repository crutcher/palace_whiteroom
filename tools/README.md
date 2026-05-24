# tools

Evaluation tooling — purpose-built scripts and small projects for verifying, validating, or exploring aspects of the Palace dissection beyond what the per-cycle agents do themselves.

Distinct from:

- `mcp/codemap/` — agent-loop infrastructure (the MCP server agents call).
- `orchestrator/` — the agent loop itself.
- `scaffolding/` — content notes, hypotheses, breadcrumbs.
- `skills/` — agent-invocable procedures (described, not executed).

Tools here are **executed code**. Skills in `skills/` can reference tools here when their procedure benefits from running code rather than just describing it.

## Layout

```
tools/
├── README.md           — this file
├── scratch/            — always-available sandbox for grab-bag exploration
│   └── README.md
└── <tool-name>/        — purpose-specific tool, created when needed
    ├── README.md
    ├── pyproject.toml or requirements.txt or Cargo.toml or ...
    ├── .venv/          — gitignored for Python tools
    └── src/ or tool source files
```

## Python tooling convention

Each Python tool gets its **own local virtual environment** under `.venv/`:

```bash
cd tools/<tool-name>
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt   # or pip install -e .
```

The `.venv/` directories are gitignored. Track `pyproject.toml` or `requirements.txt` so the env is reproducible. Each tool's `README.md` documents the setup command.

**Why per-tool venvs:** prevents dependency-version conflicts between tools, keeps each tool reproducible without polluting the system Python, and makes it explicit which deps each tool needs.

## Non-Python tooling

Rust tools follow the Cargo convention; `target/` is gitignored at the repo level. Shell-script tools don't need a venv — just commit the script(s).

## `tools/scratch/`

A sandbox. See `tools/scratch/README.md`. Different discipline from named tools: scratch is mutable and free-form; named tools are append-only-structurally and own a contract.

## Friction → `problems/`

If a tool consistently fights its task (deps don't install, the convention doesn't fit a category of work, the venv-per-tool overhead is real friction), file under `problems/` per the regular protocol — tooling concerns are valid `kind: tooling-gap` or `kind: skill-friction` entries.

## When to create a tool

When evaluation, validation, or symbolic-execution work benefits from **running code** rather than human reading. Examples that would belong here when needed:

- A solver-correctness check comparing Palace output against a hand-derived reference for a simple case.
- A schema-validation runner extending the inline `python -c` snippet in `schemas/README.md` to a re-runnable script.
- A small symbolic-execution check (z3, sympy) for an algebraic equivalence the Critic isn't sure of.
- A numerical-equivalence check between two L2 formulations (per the multi-formulation exploration principle).

**Don't create speculative tools "in case."** First need drives the first tool — same friction-from-use principle that applies to scaffolding and skills.

## Promotion from scratch

A scratch experiment that crystallizes into a worth-re-running tool gets promoted out: move to `tools/<named>/` with its own README, set up a venv if Python, document the setup. The scratch entry stays as a `→ promoted to tools/<name>/` stub if the breadcrumb has value; otherwise deleted (scratch has no append-only discipline).
