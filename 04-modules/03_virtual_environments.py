"""
Virtual Environments (.venv)

Problem:
- Different projects require different package versions.
- Installing everything globally causes conflicts.

Solution:
- Create an isolated Python environment per project.

Commands:

Create:
python -m venv .venv

Activate (Linux/macOS):
source .venv/bin/activate

Deactivate:
deactivate

Check interpreter:
which python

Notes:
- Always add .venv/ to .gitignore
- Never commit the virtual environment
- VS Code usually detects it automatically
"""
