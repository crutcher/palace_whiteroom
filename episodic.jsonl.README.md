# episodic.jsonl moved

The per-cycle structured record was renamed to `scaffolding/cycle-record.jsonl` as part of the structural-redirect migration (Phase B of `MIGRATION.md`). Existing entries (cycles 1–172) are preserved at the new path.

The schema is unchanged for now; new fields under the redesigned cycle structure (plan / dispatch / critique / repair / integrate / meta) will accrete additively.

This README is a placeholder so the old path doesn't return file-not-found to any tooling still wired to it. Remove once Phase D (orchestrator decommission) completes.
