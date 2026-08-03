# Modern Python Packaging — Cheat Sheet

## Minimal files

```
myproject/
├── pyproject.toml
├── README.md
├── src/mypackage/     # or flat: mypackage/
└── tests/
```

## pyproject.toml skeleton

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mypackage"
version = "0.1.0"
requires-python = ">=3.9"
dependencies = ["requests>=2.28"]

[project.optional-dependencies]
dev = ["pytest>=7"]
```

## Install for development

```bash
pip install -e ".[dev]"     # editable + dev extras
uv sync                     # uv: install from lockfile
```

## Build and publish

```bash
pip install build twine
python -m build
twine upload dist/*
# or: uv publish
```

## Dependency styles

| Approach | Use when |
|----------|----------|
| `requirements.txt` | Apps, Docker, simple deploys |
| `pyproject.toml` | Libraries, modern projects |
| Lockfile (`uv.lock`) | Reproducible CI and team installs |

## uv quick commands

```bash
uv init
uv add package
uv sync
uv run pytest
```

## Do not commit

`.venv/`, `dist/`, `__pycache__/`, `.env`, secrets.

Do commit: `pyproject.toml`, source, tests, README, lockfile (team choice).
