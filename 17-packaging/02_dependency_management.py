"""
Dependency Management

Ways to declare what your project needs to run and develop.

requirements.txt:
  One package per line: requests>=2.28
  Good for: apps, Docker images, quick prototypes
  Install: pip install -r requirements.txt

pyproject.toml [project]:
  dependencies = ["requests>=2.28"]
  optional-dependencies dev = ["pytest>=7"]
  Good for: libraries and modern apps (PEP 621 standard)
  Install dev extras: pip install -e ".[dev]"

Version pin styles:
  >=2.28     — minimum version, allow upgrades (libraries)
  ==2.28.1   — exact pin (reproducible deploys)
  ~=2.28.0   — compatible release (>=2.28.0, <2.29)

Lockfiles (uv.lock, poetry.lock, pip-tools output) pin exact resolved
versions so CI and teammates get identical installs.

Split runtime deps (needed in production) from dev deps (pytest, ruff).
"""

from __future__ import annotations


# ------------------------------------------------------------
# requirements.txt style
# ------------------------------------------------------------
REQUIREMENTS_TXT = """\
# Loose pins — minimum versions
requests>=2.28
click>=8.0

# Exact pin — reproducible deploy
# gunicorn==21.2.0
"""

print("requirements.txt")
print("  One package per line")
print("  Good for: apps, Docker, quick prototypes")
print("  Install: pip install -r requirements.txt")
print()
print("Sample:")
print(REQUIREMENTS_TXT)


# ------------------------------------------------------------
# pyproject.toml dependencies
# ------------------------------------------------------------
PYPROJECT_DEPS = """\
[project]
dependencies = [
    "requests>=2.28",
    "click>=8.0",
]

[project.optional-dependencies]
dev = ["pytest>=7", "ruff>=0.1"]
docs = ["sphinx>=7"]
"""

print("pyproject.toml [project.dependencies]")
print("  Standard for publishable packages")
print("  Optional groups: pip install mypkg[dev]")
print()
print("Sample:")
print(PYPROJECT_DEPS)


# ------------------------------------------------------------
# Pins — why and when
# ------------------------------------------------------------
print("Version pins:")
print("  >=2.28     — allow compatible upgrades (libraries)")
print("  ==2.28.1   — exact pin (production lock / security audit)")
print("  ~=2.28.0   — compatible release (~= means >=2.28.0, <2.29)")
print()


# ------------------------------------------------------------
# Lockfiles
# ------------------------------------------------------------
print("Lockfiles (concept):")
print("  pip-tools  -> requirements.lock from requirements.in")
print("  Poetry     -> poetry.lock")
print("  uv         -> uv.lock")
print("  Purpose: same versions on every machine and in CI")
print()


# ------------------------------------------------------------
# Challenge — split runtime vs dev deps
# ------------------------------------------------------------
print("Challenge — organize dependencies:")
print("  Runtime:  requests, pydantic  -> [project] dependencies")
print("  Dev only: pytest, ruff        -> [project.optional-dependencies] dev")
print("  Install dev: pip install -e \".[dev]\"  or  uv sync --group dev")
