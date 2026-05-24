"""Loads schemas/*.json and exposes validators for each role's typed output."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import jsonschema
from jsonschema import Draft7Validator, FormatChecker


SCHEMA_NAMES = (
    "exploration_finding",
    "rotation_claim",
    "critic_verdict",
    "refinement_plan",
)


@dataclass(frozen=True)
class SchemaSet:
    repo_root: Path
    validators: dict[str, Draft7Validator]


def load_schemas(repo_root: Path) -> SchemaSet:
    """Read all four schemas from <repo_root>/schemas/ and build validators."""
    validators: dict[str, Draft7Validator] = {}
    for name in SCHEMA_NAMES:
        with open(repo_root / "schemas" / f"{name}.json") as f:
            schema = json.load(f)
        Draft7Validator.check_schema(schema)
        validators[name] = Draft7Validator(schema, format_checker=FormatChecker())
    return SchemaSet(repo_root=repo_root, validators=validators)


def validate(schemas: SchemaSet, name: str, instance: dict) -> list[str]:
    """Validate `instance` against schema `name`. Returns a list of error
    messages (empty list = valid).
    """
    if name not in schemas.validators:
        raise KeyError(f"unknown schema name: {name}")
    errors = list(schemas.validators[name].iter_errors(instance))
    return [
        f"{'.'.join(str(p) for p in e.absolute_path) or '<root>'}: {e.message}"
        for e in errors
    ]
