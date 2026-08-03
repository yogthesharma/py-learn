"""
Parametrize — Table-Driven Tests

Run the same test logic against many input/output rows instead of
copy-pasting nearly identical test functions.

pytest syntax:
  @pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (0, 0, 0)])
  def test_add(a, b, expected):
      assert add(a, b) == expected

Each row becomes a separate test in pytest output — easy to see which
case failed. Add ids=["case-name", ...] for readable names in -v output.

Without pytest, the same idea is a for-loop over (input, expected) tuples:
  for a, b, expected in CASES:
      assert add(a, b) == expected, f"add({a}, {b}) failed"

When to use:
  Pure functions with many edge cases (math, parsing, validation)
  Any test where only the inputs change, not the assertion logic

Gotcha: parametrize expands at collection time — a 100-row table means
100 tests. Keep tables readable; split by scenario if they grow huge.
"""

from __future__ import annotations


# ------------------------------------------------------------
# Code under test
# ------------------------------------------------------------
def add(a: int, b: int) -> int:
    return a + b


def is_even(n: int) -> bool:
    return n % 2 == 0


# ------------------------------------------------------------
# Manual table-driven tests (always works)
# ------------------------------------------------------------
ADD_CASES = [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
]


def run_add_cases() -> None:
    for a, b, expected in ADD_CASES:
        result = add(a, b)
        assert result == expected, f"add({a}, {b}) -> {result}, expected {expected}"
        print(f"  add({a}, {b}) == {expected}  OK")


print("Table-driven add (for-loop):")
run_add_cases()
print()


# ------------------------------------------------------------
# pytest.mark.parametrize (when pytest is available)
# ------------------------------------------------------------
try:
    import pytest

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (1, 2, 3),
            (0, 0, 0),
            (-1, 1, 0),
        ],
    )
    def test_add_parametrized(a: int, b: int, expected: int) -> None:
        assert add(a, b) == expected

    print("pytest.mark.parametrize registered for test_add_parametrized")
    print("  pytest runs one test per row in the table")
    print()
except ImportError:
    print("pytest not installed — using for-loop simulation only")
    print()


# ------------------------------------------------------------
# Parametrize with ids (readable names in output)
# ------------------------------------------------------------
try:
    import pytest

    @pytest.mark.parametrize(
        "n,expected",
        [(2, True), (3, False), (0, True)],
        ids=["even-two", "odd-three", "even-zero"],
    )
    def test_is_even_parametrized(n: int, expected: bool) -> None:
        assert is_even(n) == expected

    print("Parametrize ids: even-two, odd-three, even-zero")
    print()
except ImportError:
    pass


# ------------------------------------------------------------
# Challenge — parametrize is_even
# ------------------------------------------------------------
# Cases: (0, True), (1, False), (2, True), (-3, False)
# Implement with for-loop AND pytest parametrize if available.


IS_EVEN_CASES = [
    (0, True),
    (1, False),
    (2, True),
    (-3, False),
]


def run_is_even_cases() -> None:
    for n, expected in IS_EVEN_CASES:
        result = is_even(n)
        assert result == expected, f"is_even({n}) -> {result}, expected {expected}"
        print(f"  is_even({n}) == {expected}  OK")


print("Challenge solution (for-loop):")
run_is_even_cases()

try:
    import pytest

    @pytest.mark.parametrize("n,expected", IS_EVEN_CASES)
    def test_is_even(n: int, expected: bool) -> None:
        assert is_even(n) == expected

    print("  pytest parametrize version also defined")
except ImportError:
    pass
