"""
Generator Expressions

Syntax: (expression for item in iterable if condition)

Same shape as a list comprehension but with parentheses — returns a
generator (lazy iterator) instead of building a full list in memory.

  [x * x for x in range(n)]   → list, all values computed immediately
  (x * x for x in range(n))   → generator, one value at a time

When to use:
  Large or unbounded data you only need to iterate once
  Pipelines where you do not need len(), indexing, or multiple passes
  Passing to a function: sum(x * x for x in data) — extra parens optional

When to use a list instead:
  You need random access, sorting, or to iterate multiple times
  The dataset is small enough that memory does not matter

Gotcha: a generator is exhausted after one full iteration — calling
list(gen) again yields [] unless you recreate the expression.
"""

from __future__ import annotations

import sys


# ------------------------------------------------------------
# List comprehension — eager, builds full list
# ------------------------------------------------------------
squares_list = [x * x for x in range(6)]
print("list:", squares_list)
print("size:", sys.getsizeof(squares_list), "bytes")
print()


# ------------------------------------------------------------
# Generator expression — lazy, yields one at a time
# ------------------------------------------------------------
squares_gen = (x * x for x in range(6))
print("generator:", squares_gen)
print("first:", next(squares_gen))
print("rest:", list(squares_gen))
print()


# ------------------------------------------------------------
# Memory note — generator wins for large data
# ------------------------------------------------------------
big_list = [x for x in range(1_000_000)]
big_gen = (x for x in range(1_000_000))

print("list of 1M ints:", sys.getsizeof(big_list), "bytes (plus element storage)")
print("gen of 1M ints:", sys.getsizeof(big_gen), "bytes")
print()

# Use a generator when you only need to iterate once and don't need
# random access or len().


# ------------------------------------------------------------
# Generator expressions in function calls — extra parens optional
# ------------------------------------------------------------
total = sum(x * x for x in range(10))
print("sum of squares 0-9:", total)
print()


# ------------------------------------------------------------
# Filtering with generator expressions
# ------------------------------------------------------------
words = ["apple", "banana", "cherry", "date"]
long_words = (w for w in words if len(w) > 5)
print("long words:", list(long_words))
print()


# ------------------------------------------------------------
# Challenge — first_n_evens
# ------------------------------------------------------------
# list(first_n_evens(5)) -> [0, 2, 4, 6, 8]


def first_n_evens(n: int):
    return (i * 2 for i in range(n))


print("first_n_evens(5):", list(first_n_evens(5)))
