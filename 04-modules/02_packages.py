"""
Packages

A package is a directory of modules with an `__init__.py` (namespace marker).
Import nested code: `from package.utils.calculator import add`.

Packages group related modules (utils, models, api) and scale beyond a
single flat folder of `.py` files.

Use when a project outgrows one file — split by feature, expose a clean
public API from `__init__.py`.

Gotcha: run scripts from the project root or install the package editable;
relative imports break if you execute a module file directly by path.
"""
