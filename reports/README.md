# Reports

Per-invocation report channel for the new 6-phase cycle. See `../MIGRATION.md` §2 *Report channel* and `../.claude/agents/README.md`.

Each subdirectory is one agent invocation: `<timestamp>-<agent>-<scope>/`. Contains `REPORT.md` (the agent's proposed changes + supporting prose) and (post-verify-phase) a co-located `META.md` (critic + repairer output). The integrator marks consumed reports with `integrated_at:` / `integration_commit:` frontmatter and emits its own batch report.

Index newest-first below.

## Index
