"""
Recursion

A function that calls itself to solve a smaller version of the same problem.
Every recursive function needs:
  1. Base case — stops the recursion (returns a known answer)
  2. Recursive case — calls itself with input closer to the base case

Without a base case you get infinite recursion → RecursionError.

Classic examples: factorial, fibonacci, tree traversal, divide-and-conquer.

Python has a default recursion limit (~1000 frames) — deep recursion can
hit RecursionError even with a correct base case. For very deep trees,
use an explicit stack or loop instead.

When to use:
  Problems naturally defined in terms of smaller sub-problems
  Tree/graph structures where the shape mirrors the algorithm

When to prefer a loop:
  Simple linear iteration, performance-critical hot paths, very deep nesting
"""

from __future__ import annotations


# ------------------------------------------------------------
# Countdown — simple recursion
# ------------------------------------------------------------
def countdown(n: int) -> None:
    if n <= 0:
        print("Blast off!")
        return
    print(n)
    countdown(n - 1)


print("Countdown from 3:")
countdown(3)
print()


# ------------------------------------------------------------
# Factorial — classic example
# ------------------------------------------------------------
# 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(f"factorial(5) = {factorial(5)}")
print(f"factorial(0) = {factorial(0)}")
print()


# ------------------------------------------------------------
# Base case importance
# ------------------------------------------------------------
def broken_count(n: int) -> int:
    # Missing base case — do NOT call this with real data!
    return 1 + broken_count(n - 1)


try:
    broken_count(3)
except RecursionError as error:
    print("RecursionError without base case:", error)
print()


# ------------------------------------------------------------
# Recursion vs loop
# ------------------------------------------------------------
def sum_loop(numbers: list[int]) -> int:
    total = 0
    for n in numbers:
        total += n
    return total


def sum_recursive(numbers: list[int]) -> int:
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])


data = [1, 2, 3, 4, 5]
print("Loop:", sum_loop(data))
print("Recursion:", sum_recursive(data))
print()

# Loops are usually faster and use less memory (no call stack growth).
# Recursion can be clearer for tree/graph problems and divide-and-conquer.


# ------------------------------------------------------------
# Challenge — sum_list (recursive)
# ------------------------------------------------------------
# sum_list([1, 2, 3]) -> 6
# sum_list([])        -> 0


def sum_list(numbers: list[int]) -> int:
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])


print(sum_list([1, 2, 3]))
print(sum_list([]))
print(sum_list([10, -3, 7]))
