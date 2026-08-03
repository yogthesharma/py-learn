"""
yield from — Delegating to Subgenerators

yield from subgen forwards every value from another generator or iterable
into the current generator — and delegates send()/throw() in advanced code.

  def outer():
      yield from inner()   # forwards all values from inner
      yield 3

Manual equivalent:
  for value in subgen:
      yield value

Common uses:
  Flatten nested lists or trees without building intermediate lists
  Delegate to a sub-generator instead of copy-pasting loops
  yield from some_string  — forwards each character

Compared to yield inside a for-loop: yield from is shorter and preserves
the subgenerator's full protocol (including return values in Python 3.3+).

Use when you are proxying iteration to another iterable.
Use a plain for/yield loop when you transform each item on the way out.
"""

from __future__ import annotations


# ------------------------------------------------------------
# Basic yield from — forwards all values
# ------------------------------------------------------------
def inner():
    yield 1
    yield 2


def outer():
    yield from inner()
    yield 3


print("outer():", list(outer()))
print()


# ------------------------------------------------------------
# yield from vs manual loop
# ------------------------------------------------------------
def flatten_manual(nested: list[list[int]]) -> list[int]:
    result = []
    for sublist in nested:
        for item in sublist:
            result.append(item)
    return result


def flatten_gen(nested: list[list[int]]):
    for sublist in nested:
        yield from sublist


data = [[1, 2], [3], [4, 5, 6]]
print("manual:", flatten_manual(data))
print("yield from:", list(flatten_gen(data)))
print()


# ------------------------------------------------------------
# yield from a string (iterable)
# ------------------------------------------------------------
def chars(word: str):
    yield from word


print("chars('abc'):", list(chars("abc")))
print()


# ------------------------------------------------------------
# Recursive generator — tree flattening intuition
# ------------------------------------------------------------
def walk(node: list | int):
    if isinstance(node, int):
        yield node
    else:
        for child in node:
            yield from walk(child)


tree = [1, [2, [3, 4]], 5]
print("walk tree:", list(walk(tree)))
print()


# ------------------------------------------------------------
# Challenge — flatten nested lists with yield from
# ------------------------------------------------------------
# flatten([[1, 2], [3, [4, 5]], 6]) -> [1, 2, 3, 4, 5, 6]
# (One level of nesting in sublists; sublists may contain ints or lists.)


def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


print("flatten:", list(flatten([[1, 2], [3, [4, 5]], 6])))
