"""
Publishing a Package

Turn your project into installable artifacts and upload to PyPI.

Build step (reads pyproject.toml):
  pip install build && python -m build
  # or: uv build
  Produces:
    dist/myapp-0.1.0.tar.gz              — source distribution (sdist)
    dist/myapp-0.1.0-py3-none-any.whl    — wheel (preferred for installs)

Upload:
  twine upload dist/*
  # or: uv publish

Always test on TestPyPI first: twine upload --repository testpypi dist/*

Before each release:
  Bump version in pyproject.toml (semantic versioning: MAJOR.MINOR.PATCH)
  Run pytest, tag in git (git tag v0.1.0)
  Verify wheel installs in a clean venv

Do not commit: .venv/, dist/, secrets, .env
Many teams DO commit lockfiles (uv.lock) — never commit credentials.
"""

from __future__ import annotations


# ------------------------------------------------------------
# Build artifacts
# ------------------------------------------------------------
print("Build step produces:")
print("  dist/myapp-0.1.0.tar.gz   — source distribution (sdist)")
print("  dist/myapp-0.1.0-py3-none-any.whl — wheel (preferred install)")
print()
print("Build commands:")
print("  pip install build")
print("  python -m build          # reads pyproject.toml")
print("  # or: uv build")
print()


# ------------------------------------------------------------
# Upload to PyPI
# ------------------------------------------------------------
print("Upload options:")
print("  twine upload dist/*")
print("  uv publish               # build + upload in uv workflow")
print()
print("Use TestPyPI first: https://test.pypi.org/")
print("  twine upload --repository testpypi dist/*")
print()


# ------------------------------------------------------------
# Versioning
# ------------------------------------------------------------
print("Versioning:")
print("  Start at 0.1.0 for early releases")
print("  Semantic versioning: MAJOR.MINOR.PATCH")
print("  Bump version in pyproject.toml before each release")
print("  Tag in git: git tag v0.1.0")
print()


# ------------------------------------------------------------
# What NOT to commit
# ------------------------------------------------------------
DO_NOT_COMMIT = [
    ".venv/",
    "venv/",
    "dist/",
    "build/",
    "*.egg-info/",
    "__pycache__/",
    ".pytest_cache/",
    "*.pyc",
    ".env",
    "uv.lock",  # optional: many teams DO commit lockfiles; never commit secrets
]

print("What NOT to commit (typical .gitignore):")
for item in DO_NOT_COMMIT:
    note = ""
    if item == "uv.lock":
        note = "  # teams often commit lockfiles; listed as 'do not commit secrets'"
    print(f"  {item}{note}")
print()


# ------------------------------------------------------------
# Challenge checklist — ready to publish?
# ------------------------------------------------------------
CHECKLIST = [
    "pyproject.toml has name, version, description, requires-python",
    "README explains install and basic usage",
    "LICENSE file present",
    "tests pass: pytest",
    "Version bumped for this release",
    "python -m build succeeds",
    "Tested install from wheel in a clean venv",
    "Uploaded to TestPyPI and pip install tested",
    "No secrets or .env in the repo",
]

print("Challenge — publish readiness checklist:")
for index, item in enumerate(CHECKLIST, start=1):
    print(f"  [{index}] {item}")
