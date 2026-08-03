"""
Custom Iterators

Implement __iter__ and __next__ on a class to create your own iterator.
Python calls these when you use for, list(), or next() on your object.

Protocol:
  __iter__(self)  → return an iterator (often self, or a fresh helper object)
  __next__(self)  → return the next value, or raise StopIteration when done

Iterable vs iterator:
  Iterable — __iter__ returns a new iterator each call (reusable in for-loops)
  Iterator — tracks position; exhausted after one full pass unless reset

When to use a class instead of a generator function:
  Stateful iteration (pagination, file chunks, tree traversal)
  Reusable iterables that hand out fresh iterators on each loop
  Explicit control over iteration lifecycle

Gotcha: if __iter__ returns self with leftover state, a second for-loop
may start mid-stream or yield nothing — return a new iterator object when
the container should be re-iterable.
"""

from __future__ import annotations


# ------------------------------------------------------------
# Simple custom iterator — counts from start to stop
# ------------------------------------------------------------
class Counter:
    def __init__(self, start: int, stop: int) -> None:
        self.current = start
        self.stop = stop

    def __iter__(self) -> Counter:
        return self

    def __next__(self) -> int:
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


print("Counter(1, 4):", list(Counter(1, 4)))
print()


# ------------------------------------------------------------
# Iterator vs iterable — separate objects
# ------------------------------------------------------------
class EvenNumbers:
    """Iterable — __iter__ returns a fresh iterator each time."""

    def __init__(self, limit: int) -> None:
        self.limit = limit

    def __iter__(self) -> EvenNumbersIterator:
        return EvenNumbersIterator(self.limit)


class EvenNumbersIterator:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.current = 0

    def __iter__(self) -> EvenNumbersIterator:
        return self

    def __next__(self) -> int:
        if self.current >= self.limit:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


evens = EvenNumbers(8)
print("First pass:", list(evens))
print("Second pass:", list(evens))  # works again — new iterator each time
print()


# ------------------------------------------------------------
# Real-world use — paginated data, file chunks, tree traversal
# ------------------------------------------------------------


# ------------------------------------------------------------
# Challenge — Countdown iterator
# ------------------------------------------------------------
# for n in Countdown(3):
#     print(n)
# 3
# 2
# 1
# print("Go!")
#
# (After the loop, print "Go!" separately.)


class Countdown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self) -> Countdown:
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


for n in Countdown(3):
    print(n)
print("Go!")
