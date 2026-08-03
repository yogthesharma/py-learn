# Testing — Quick Reference

## Install

```bash
pip install pytest pytest-asyncio
```

## Run tests

```bash
pytest                          # all tests under current directory
pytest 16-testing/ -v           # verbose, one folder
pytest 16-testing/01_pytest_intro.py
pytest -k "add and not slow"      # name filter
pytest --tb=short               # shorter tracebacks
```

## Lesson scripts (always exit 0)

Each `.py` file teaches concepts when run directly:

```bash
python3 16-testing/01_pytest_intro.py
```

Install pytest to also run the `test_*` functions inside those files.

## Concepts covered

| File | Topic |
|------|-------|
| `01_pytest_intro.py` | Why test, naming, running pytest |
| `02_assertions.py` | assert, raises, pytest.approx |
| `03_fixtures.py` | setup data, yield teardown |
| `04_parametrize.py` | table-driven tests |
| `05_mocking.py` | MagicMock, patch |
| `06_testing_async.py` | pytest-asyncio, asyncio.run |
