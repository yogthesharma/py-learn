"""
Project Layout

Two common ways to organize importable package code in a repo.

Flat layout — package folder at repo root:
  myproject/mypackage/__init__.py
  Simple; fine for scripts and internal tools.

Src layout — package inside src/ (recommended for libraries):
  myproject/src/mypackage/__init__.py
  Prevents accidental imports from the working directory during dev.
  Tests exercise the package the way pip-installed users see it.

Minimal modern project also includes:
  pyproject.toml  — metadata, deps, build backend, tool config
  README.md       — install and usage
  tests/          — pytest tests (outside the package)
  .gitignore      — .venv/, dist/, __pycache__/, *.egg-info/

Configure src layout in pyproject.toml (e.g. hatchling packages path).

Pick src layout for PyPI libraries; flat or single-file may suffice for
internal scripts. Always use pyproject.toml for anything non-trivial.
"""

from __future__ import annotations

from pathlib import Path


# ------------------------------------------------------------
# Flat layout
# ------------------------------------------------------------
FLAT_TREE = """
myproject/
├── pyproject.toml
├── README.md
├── mypackage/
│   ├── __init__.py
│   └── core.py
└── tests/
    └── test_core.py
"""

print("Flat layout — package at repo root:")
print(FLAT_TREE)


# ------------------------------------------------------------
# Src layout (recommended for libraries)
# ------------------------------------------------------------
SRC_TREE = """
myproject/
├── pyproject.toml
├── README.md
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── core.py
└── tests/
    └── test_core.py
"""

print("Src layout — package under src/:")
print(SRC_TREE)
print("  Prevents accidental imports from the working directory")
print("  Tests behave like installed users see the package")
print()


# ------------------------------------------------------------
# What each piece does
# ------------------------------------------------------------
print("Key files and folders:")
print("  pyproject.toml  — metadata, deps, build, tool config")
print("  README.md       — install and usage docs")
print("  src/pkg/        — importable package code")
print("  tests/          — pytest tests (outside the package)")
print("  .gitignore      — ignore .venv/, dist/, __pycache__/, *.egg-info/")
print()


# ------------------------------------------------------------
# Print a tree for the examples folder
# ------------------------------------------------------------
def print_tree(root: Path, prefix: str = "") -> None:
    entries = sorted(root.iterdir(), key=lambda p: (p.is_file(), p.name))
    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{entry.name}{'/' if entry.is_dir() else ''}")
        if entry.is_dir():
            extension = "    " if is_last else "│   "
            print_tree(entry, prefix + extension)


examples_root = Path(__file__).parent / "examples"
if examples_root.exists():
    print("Current examples/ tree:")
    print("examples/")
    print_tree(examples_root, prefix="")
    print()


# ------------------------------------------------------------
# Challenge — choose a layout
# ------------------------------------------------------------
print("Challenge — pick a layout:")
print("  Library for PyPI     -> src layout + tests/")
print("  Internal script repo -> flat or single-file may be enough")
print("  Always: pyproject.toml, README, .gitignore, tests for non-trivial code")
