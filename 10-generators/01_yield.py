"""
Generators — yield vs return

A function with `yield` becomes a generator function.
Calling it returns a generator object (lazy iterator) — it does NOT
run the body immediately. Each next() advances to the next yield.

  return value   — ends a normal function with one result, all at once
  yield value    — pauses a generator and produces one value at a time

Memory trade-off:
  squares_list(n)  → builds full list in memory
  squares_gen(n)   → yields one square per next() call

Generators are iterators — usable in for-loops, list(), sum(), etc.
State is preserved between yields (local variables survive pauses).

When to use:
  Large or infinite sequences, streaming pipelines, lazy evaluation
  When you only need to iterate once and do not need random access

Gotcha: calling a generator function twice gives two independent
generators — each maintains its own position.
"""

from __future__ import annotations


# ------------------------------------------------------------
# return — computes everything at once
# ------------------------------------------------------------
def squares_list(n: int) -> list[int]:
    result = []
    for i in range(n):
        result.append(i * i)
    return result


print("squares_list(5):", squares_list(5))
print()


# ------------------------------------------------------------
# yield — lazy, one value at a time
# ------------------------------------------------------------
def squares_gen(n: int):
    for i in range(n):
        yield i * i


gen = squares_gen(5)
print("generator object:", gen)
print("first:", next(gen))
print("second:", next(gen))
print("rest:", list(gen))
print()


# ------------------------------------------------------------
# Generator functions pause and resume
# ------------------------------------------------------------
def step_demo():
    print("  step 1")
    yield "a"
    print("  step 2")
    yield "b"
    print("  step 3")


g = step_demo()
print("created generator — body has NOT run yet")
print("next:", next(g))
print("next:", next(g))
print()


# ------------------------------------------------------------
# Lazy evaluation — memory efficient for large sequences
# ------------------------------------------------------------
def read_lines_lazy(path: str):
    """Yield one line at a time instead of loading the whole file."""
    with open(path, encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")


# ------------------------------------------------------------
# Challenge — fibonacci generator
# ------------------------------------------------------------
# list(fibonacci(7)) -> [0, 1, 1, 2, 3, 5, 8]


def fibonacci(count: int):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b


print("fibonacci(7):", list(fibonacci(7)))
print("fibonacci(1):", list(fibonacci(1)))
