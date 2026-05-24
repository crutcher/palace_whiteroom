"""Loads config.toml from the repo root."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:
    target_repo: Path     # Absolute path to the target repo clone (e.g., reference/palace).
    target_language: str  # "cpp" for now.
    models: dict[str, str]  # role -> model_id
    explorer_max_input_tokens: int
    cycle_token_budget: int
    max_parallel_slices: int
    meta_review_every_n_cycles: int

    @property
    def repo_root(self) -> Path:
        """The whiteroom repo root — parent of config.toml."""
        return self._repo_root  # type: ignore[attr-defined]


def load_config(config_path: Path) -> Config:
    """Parse config.toml. Resolves [target].repo relative to the config dir."""
    with open(config_path, "rb") as f:
        raw = tomllib.load(f)

    target = raw["target"]
    models = raw["models"]
    limits = raw["limits"]

    config_dir = config_path.parent.resolve()
    target_repo = (config_dir / target["repo"]).resolve()

    cfg = Config(
        target_repo=target_repo,
        target_language=target["language"],
        models={
            "planner":     models["planner"],
            "explorer":    models["explorer"],
            "synthesizer": models["synthesizer"],
            "critic":      models["critic"],
            "meta_critic": models["meta_critic"],
        },
        explorer_max_input_tokens=limits["explorer_max_input_tokens"],
        cycle_token_budget=limits["cycle_token_budget"],
        max_parallel_slices=limits["max_parallel_slices"],
        meta_review_every_n_cycles=limits["meta_review_every_n_cycles"],
    )
    # Stash the repo root so other modules can address paths consistently.
    object.__setattr__(cfg, "_repo_root", config_dir)
    return cfg
