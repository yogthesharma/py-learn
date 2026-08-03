"""
pyproject.toml — Modern Python Project Config

One file at the project root that describes how to build, install, and
configure a Python project — replacing setup.py + setup.cfg for most work.

Key sections:
  [build-system]           — requires + build-backend (e.g. hatchling)
  [project]                — name, version, dependencies (PEP 621)
  [project.optional-dependencies] — dev, docs, etc.
  [tool.pytest.ini_options] — pytest config
  [tool.ruff], [tool.mypy]  — linter and type checker settings

Install from pyproject.toml:
  pip install .              — runtime deps only
  pip install -e ".[dev]"    — editable + dev extras

PEP 518 introduced [build-system]; PEP 621 standardized [project] metadata.
Modern backends: hatchling, setuptools, flit, poetry-core.

Use pyproject.toml for any project you might share, publish, or run in CI.
"""

from __future__ import annotations

from pathlib import Path


# ------------------------------------------------------------
# Minimal pyproject.toml (sample)
# ------------------------------------------------------------
MINIMAL_PYPROJECT = '''\
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myapp"
version = "0.1.0"
description = "A small example package"
readme = "README.md"
requires-python = ">=3.9"
dependencies = [
    "requests>=2.28",
]

[project.optional-dependencies]
dev = ["pytest>=7", "ruff>=0.1"]

[tool.pytest.ini_options]
testpaths = ["tests"]
'''

print("What is pyproject.toml?")
print("  Single config file for building and packaging Python projects.")
print("  Replaces setup.py + setup.cfg for many projects.")
print()
print("Minimal sample:")
print("-" * 60)
print(MINIMAL_PYPROJECT)
print("-" * 60)
print()


# ------------------------------------------------------------
# [build-system] table
# ------------------------------------------------------------
print("[build-system]")
print("  requires      — packages needed to build (e.g. hatchling, setuptools)")
print("  build-backend — module that performs the build (PEP 517)")
print("  Common backends: hatchling, setuptools, flit, poetry-core")
print()


# ------------------------------------------------------------
# [project] table
# ------------------------------------------------------------
print("[project] — package metadata (PEP 621)")
print("  name, version, description, readme, license")
print("  requires-python — supported Python versions")
print("  dependencies    — runtime packages")
print("  optional-dependencies — extras like dev, docs")
print("  scripts         — console entry points")
print()


# ------------------------------------------------------------
# Write example to examples/ (optional demo artifact)
# ------------------------------------------------------------
EXAMPLES_DIR = Path(__file__).parent / "examples" / "minimal-project"
EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)
pyproject_path = EXAMPLES_DIR / "pyproject.toml"
pyproject_path.write_text(MINIMAL_PYPROJECT, encoding="utf-8")
print(f"Wrote sample to: {pyproject_path.relative_to(Path(__file__).parent)}")
print()


# ------------------------------------------------------------
# Challenge — add a script entry point
# ------------------------------------------------------------
# Entry point runs: myapp = myapp.cli:main
# Add under [project.scripts] in your mental model.


ENTRY_POINT_SNIPPET = '''\
[project.scripts]
myapp = "myapp.cli:main"
'''

print("Challenge — console script entry point:")
print(ENTRY_POINT_SNIPPET)
print("After install: user runs `myapp` on the command line.")
