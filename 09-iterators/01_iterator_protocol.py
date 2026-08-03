"""
The Iterator Protocol

Anything you can loop over with `for` follows the iterator protocol.
Understanding it explains how for-loops, list(), and next() work.

Steps:
  1. iter(obj)  → calls obj.__iter__(), returns an iterator
  2. next(it)   → calls it.__next__() for the next value
  3. StopIteration → signals "no more items" (for-loop catches this)

for item in collection: is roughly:
  it = iter(collection)
  while True:
      try: item = next(it)
      except StopIteration: break

Built-in iterables: list, str, dict, file, range, set — all implement
__iter__. Custom classes can too (see 02_custom_iterators.py).

Gotcha: an iterator is one-shot — after StopIteration, you need a fresh
iter(obj) or a new iterator from a reusable iterable.
"""

from __future__ import annotations


# ------------------------------------------------------------
# Manual iteration with iter() and next()
# ------------------------------------------------------------
numbers = [10, 20, 30]
it = iter(numbers)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30

try:
    next(it)
except StopIteration:
    print("StopIteration — iterator exhausted")
print()


# ------------------------------------------------------------
# for-loop uses the iterator protocol under the hood
# ------------------------------------------------------------
# for item in numbers:
#     print(item)
#
# Is roughly equivalent to:
it = iter(numbers)
while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break
print()


# ------------------------------------------------------------
# Strings are iterable too
# ------------------------------------------------------------
for char in "Hi":
    print(char, end=" ")
print("\n")


# ------------------------------------------------------------
# iter() on a callable — sentinel pattern (Python 3.10+: 3-arg form)
# ------------------------------------------------------------
import sys

if sys.version_info >= (3, 10):
    import random

    random.seed(42)
    roll = iter(random.randint, 1, 6)  # calls randint(1, 6) each next()
    print("random rolls:", [next(roll) for _ in range(5)])
else:
    # 3-argument iter() was added in Python 3.10
    print("3-arg iter(callable, sentinel) demo skipped (requires Python 3.10+)")
print()


# ------------------------------------------------------------
# Challenge — manual for-loop simulation
# ------------------------------------------------------------
# Given a list, print each item using only iter() / next() / StopIteration.


def manual_for(items: list[int]) -> None:
    iterator = iter(items)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


print("manual_for([1, 2, 3]):")
manual_for([1, 2, 3])
