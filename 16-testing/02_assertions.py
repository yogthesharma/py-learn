"""
Assertions in Tests

assert condition  — if condition is False, raises AssertionError.

pytest rewrites assert statements to show rich comparisons on failure:
  assert result == expected
  # Failed: assert 5 == 6
  #  where 5 = add(2, 3)   (simplified idea)

Without pytest you still get AssertionError, but less detail.

Common patterns:
  assert result == expected          — equality
  assert item in collection          — membership
  assert not condition             — negation
  pytest.raises(Error)             — expect an exception (with pytest)

Use assert for test expectations — not for validating user input in
production code (assert can be stripped with python -O).

When writing tests: one logical assertion per concept; descriptive
variable names beat cryptic one-liners when a test fails.
"""

from __future__ import annotations


# ------------------------------------------------------------
# Basic assert
# ------------------------------------------------------------
def is_even(n: int) -> bool:
    return n % 2 == 0


print("Basic assert demos:")
assert is_even(4)
assert not is_even(7)
print("  is_even checks passed")
print()


# ------------------------------------------------------------
# Equality and membership
# ------------------------------------------------------------
def normalize_tags(tags: list[str]) -> list[str]:
    return sorted({t.strip().lower() for t in tags})


result = normalize_tags([" Python ", "pytest", "python"])
print("normalize_tags:", result)
assert result == ["pytest", "python"]
assert "pytest" in result
assert "Java" not in result
print("  equality and membership checks passed")
print()


# ------------------------------------------------------------
# Testing exceptions — manual (no pytest required)
# ------------------------------------------------------------
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b


print("Testing divide raises ValueError:")
try:
    divide(10, 0)
    print("  ERROR: expected ValueError")
except ValueError as error:
    print(f"  caught ValueError: {error}")

try:
    assert divide(10, 2) == 5.0
    print("  divide(10, 2) == 5.0  OK")
except AssertionError as error:
    print("  assertion failed:", error)
print()


# ------------------------------------------------------------
# pytest.raises (when pytest is available)
# ------------------------------------------------------------
try:
    import pytest

    print("pytest.raises demo:")

    def test_divide_by_zero() -> None:
        with pytest.raises(ValueError, match="division by zero"):
            divide(1, 0)

    test_divide_by_zero()
    print("  pytest.raises test passed")
    print()
except ImportError:
    print("pytest not installed — skipped pytest.raises demo")
    print()


# ------------------------------------------------------------
# Discoverable tests
# ------------------------------------------------------------
def test_normalize_tags() -> None:
    assert normalize_tags(["A", "b", "a"]) == ["a", "b"]


def test_divide_success() -> None:
    assert divide(9, 3) == 3.0


# ------------------------------------------------------------
# Challenge — assertions for divide
# ------------------------------------------------------------
# Assert: divide(8, 4) == 2.0
# Assert: divide(1, 3) is close enough (use pytest.approx if available)
# Assert: divide(5, 0) raises ValueError


def challenge_self_check() -> None:
    assert divide(8, 4) == 2.0
    approx = divide(1, 3)
    assert abs(approx - 0.3333333333333333) < 1e-9
    try:
        divide(5, 0)
        raise AssertionError("expected ValueError for divide(5, 0)")
    except ValueError:
        pass


print("Challenge solution:")
try:
    challenge_self_check()
    print("  all divide assertions passed")
except AssertionError as error:
    print("  challenge failed:", error)

try:
    import pytest

    def test_divide_fraction() -> None:
        assert divide(1, 3) == pytest.approx(0.3333333, rel=1e-6)

    test_divide_fraction()
    print("  pytest.approx check passed")
except ImportError:
    pass
