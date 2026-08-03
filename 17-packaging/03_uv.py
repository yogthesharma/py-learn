"""
uv — Fast Python Package Manager

uv (by Astral, makers of Ruff) is a Rust-based CLI that replaces much
of the pip + venv + pip-tools workflow with one fast tool.

It can: create projects, manage Python versions, sync venvs, resolve
deps, run scripts, and publish — all driven by pyproject.toml.

Common commands:
  uv init myproject        — scaffold pyproject.toml
  uv add requests          — add runtime dep + update uv.lock
  uv add --dev pytest      — add dev dependency
  uv sync                  — install from lockfile into .venv
  uv run pytest            — run command inside project venv
  uv lock                  — refresh lockfile without installing
  uv python install 3.12   — install a Python version
  uv publish               — build and upload to PyPI

uv vs pip + venv:
  Single tool, faster resolves, built-in lockfile (uv.lock)
  Drop-in for new projects; existing pip workflows still work

When to use: new projects, teams wanting fast CI installs and reproducible
lockfiles without juggling pip, venv, and pip-tools separately.
"""

from __future__ import annotations


# ------------------------------------------------------------
# What is uv?
# ------------------------------------------------------------
print("What is uv?")
print("  All-in-one: Python version, venv, deps, scripts, publish")
print("  Much faster than pip for resolve and install")
print("  Uses pyproject.toml and can generate uv.lock")
print()


# ------------------------------------------------------------
# Common commands (documented)
# ------------------------------------------------------------
COMMANDS = [
    ("uv init myproject", "Create a new project with pyproject.toml"),
    ("uv add requests", "Add a runtime dependency and update lockfile"),
    ("uv add --dev pytest", "Add a dev dependency"),
    ("uv sync", "Install deps from lockfile into .venv"),
    ("uv run pytest", "Run a command inside the project venv"),
    ("uv run python script.py", "Run script with project deps available"),
    ("uv lock", "Update lockfile without installing"),
    ("uv python install 3.12", "Install a Python version"),
    ("uv publish", "Build and upload to PyPI (with credentials)"),
]

print("Common uv commands:")
print("-" * 60)
for cmd, desc in COMMANDS:
    print(f"  {cmd:<30}  {desc}")
print("-" * 60)
print()


# ------------------------------------------------------------
# uv vs pip + venv
# ------------------------------------------------------------
print("uv vs traditional pip + venv:")
print()
print("  pip + venv:")
print("    python -m venv .venv")
print("    source .venv/bin/activate")
print("    pip install -r requirements.txt")
print()
print("  uv:")
print("    uv sync          # creates .venv + installs from lock")
print("    uv run pytest    # no manual activate needed")
print()
print("  Both are valid. uv shines on speed and unified workflow.")
print()


# ------------------------------------------------------------
# Challenge — workflow for a new app
# ------------------------------------------------------------
print("Challenge — start a new app with uv:")
print("  1. uv init myapp && cd myapp")
print("  2. uv add fastapi uvicorn")
print("  3. uv add --dev pytest httpx")
print("  4. uv run uvicorn myapp.main:app --reload")
print("  5. Commit pyproject.toml and uv.lock (not .venv/)")
