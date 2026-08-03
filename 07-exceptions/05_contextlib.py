"""
contextlib — Helpers for Context Managers

The `with` statement expects an object with __enter__ / __exit__ (or
__aenter__ / __aexit__ for async). contextlib provides shortcuts so you
do not hand-write a class for every resource wrapper.

Key tools:
  @contextmanager       — build a sync context manager from a generator
  @asynccontextmanager  — async version (see asyncio lesson)
  closing(obj)          — call obj.close() on exit
  suppress(*exceptions) — ignore specific exceptions inside the block

@contextmanager pattern:
  Code BEFORE yield runs on __enter__ (start of `with`)
  yield hands control to the `with` block
  Code AFTER yield runs on __exit__ (even if an exception occurred)
  Wrap yield in try/finally to guarantee cleanup.

Use @contextmanager for simple setup/teardown (timers, temp state, tags).
Use a class with __enter__/__exit__ when you need complex state or reuse.
"""

from __future__ import annotations

import contextlib
import time
from collections.abc import Iterator


# ------------------------------------------------------------
# @contextmanager — generator-based context manager
# ------------------------------------------------------------
@contextlib.contextmanager
def tag(name: str) -> Iterator[None]:
    print(f"[{name}] start")
    try:
        yield
    finally:
        print(f"[{name}] end")


with tag("section"):
    print("  doing work inside")
print()


# ------------------------------------------------------------
# How @contextmanager works
# ------------------------------------------------------------
# 1. Code BEFORE yield runs on __enter__ (start of `with`)
# 2. yield pauses and hands control to the `with` block
# 3. Code AFTER yield runs on __exit__ (even if an exception occurred)
#
# The `try/finally` around yield ensures cleanup always runs.


# ------------------------------------------------------------
# closing() — auto-close resources with a .close() method
# ------------------------------------------------------------
class SimpleWriter:
    def __init__(self, name: str) -> None:
        self.name = name
        self.closed = False

    def write(self, text: str) -> None:
        if self.closed:
            raise ValueError("Writer is closed")
        print(f"{self.name}: {text}")

    def close(self) -> None:
        self.closed = True
        print(f"{self.name} closed")


with contextlib.closing(SimpleWriter("log")) as writer:
    writer.write("first line")
    writer.write("second line")
print()


# ------------------------------------------------------------
# suppress() — ignore specific exceptions
# ------------------------------------------------------------
values = [10, 0, 5, 2]

for value in values:
    with contextlib.suppress(ZeroDivisionError):
        result = 100 / value
        print(f"100 / {value} = {result}")
print("Loop finished despite division by zero")
print()


# ------------------------------------------------------------
# Challenge — timer context manager via contextlib
# ------------------------------------------------------------
# with timer("fetch"):
#     time.sleep(0.1)
#
# fetch took 0.10s (approx)


@contextlib.contextmanager
def timer(label: str) -> Iterator[None]:
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label} took {elapsed:.2f}s (approx)")


with timer("fetch"):
    time.sleep(0.1)

with timer("compute"):
    total = sum(range(100_000))
    print(f"sum = {total}")
