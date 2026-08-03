"""
Pytest Introduction

Why write tests?
  - Catch bugs before users do
  - Document expected behavior
  - Refactor with confidence

pytest is the most popular Python test runner. It discovers tests automatically,
provides helpful failure output, and needs less boilerplate than unittest.

Run tests (when pytest is installed):
  pytest                          # discover tests in current tree
  pytest 16-testing/01_pytest_intro.py   # one file
  pytest -v                       # verbose names
  pytest -k add                   # name filter
"""

from __future__ import annotations


# ------------------------------------------------------------
# Code under test — keep it simple
# ------------------------------------------------------------
def add(a: int, b: int) -> int:
    return a + b


# ------------------------------------------------------------
# What a pytest test looks like
# ------------------------------------------------------------
# Rules pytest uses to find tests:
#   - file name: test_*.py or *_test.py
#   - function name: test_*
#   - class name: Test* (methods must be test_*)
#
# A test is just a function that uses assert. No special base class required.


def test_add_positive_numbers() -> None:
    assert add(2, 3) == 5


def test_add_negative_numbers() -> None:
    assert add(-1, -1) == -2


def test_add_zero() -> None:
    assert add(0, 7) == 7


# ------------------------------------------------------------
# pytest vs unittest (brief)
# ------------------------------------------------------------
print("pytest vs unittest:")
print("  unittest — built-in, class-based, lots of self.assertEqual(...) calls")
print("  pytest   — third-party, function-based, plain assert, richer plugins")
print("  Both work. pytest is usually less code for the same coverage.")
print()


# ------------------------------------------------------------
# Demo — assert as a self-check (works without pytest)
# ------------------------------------------------------------
def self_check_add() -> None:
    cases = [(2, 3, 5), (-1, -1, -2), (0, 7, 7)]
    for a, b, expected in cases:
        result = add(a, b)
        assert result == expected, f"add({a}, {b}) -> {result}, expected {expected}"
        print(f"  add({a}, {b}) == {expected}  OK")


print("Self-check (assert-based, no pytest needed):")
try:
    self_check_add()
    print("All self-checks passed.")
except AssertionError as error:
    print("Self-check failed (this demo caught it):", error)
print()


# ------------------------------------------------------------
# How to run pytest
# ------------------------------------------------------------
print("Run with pytest when installed:")
print("  pip install pytest")
print("  pytest 16-testing/01_pytest_intro.py -v")
print()

try:
    import pytest  # noqa: F401

    print("pytest is installed — test functions in this file can be discovered.")
except ImportError:
    print("pytest is not installed — that's fine for this lesson.")
    print("The script still runs; install pytest to run the test_* functions.")
print()


# ------------------------------------------------------------
# Challenge — test subtract(a, b)
# ------------------------------------------------------------
# Write subtract and test_subtract (or self-check) like add above.
# subtract(10, 3) -> 7
# subtract(3, 10) -> -7


def subtract(a: int, b: int) -> int:
    return a - b


def test_subtract() -> None:
    assert subtract(10, 3) == 7
    assert subtract(3, 10) == -7


print("Challenge solution:")
print(f"  subtract(10, 3) = {subtract(10, 3)}")
print(f"  subtract(3, 10) = {subtract(3, 10)}")
