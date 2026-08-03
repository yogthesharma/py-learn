"""
Decorators

A decorator wraps a function to add behavior before, after, or around it
without changing the function's source at every call site.

Syntax sugar:
  @decorator
  def func(): ...

is exactly:
  func = decorator(func)

A decorator is a function that takes a callable and returns a callable.
The wrapper usually uses *args, **kwargs to preserve any signature.

Stacking applies bottom-up:
  @outer
  @inner
  def f(): ...
  → f = outer(inner(f))

Common patterns: logging, timing, auth checks, retries, caching.

Gotcha: the wrapper replaces the original function object — metadata
(__name__, __doc__) is lost unless you use functools.wraps (next lesson).

Use decorators for cross-cutting concerns shared across many functions.
"""

from __future__ import annotations

import time


# ------------------------------------------------------------
# Manual decoration — no @ syntax
# ------------------------------------------------------------
def shout(func):
    def wrapper(name: str) -> None:
        func(name)
        print("!!!")

    return wrapper


def greet(name: str) -> None:
    print(f"Hello, {name}")


greet = shout(greet)
greet("World")
print()


# ------------------------------------------------------------
# Decorator syntax with @
# ------------------------------------------------------------
def banner(func):
    def wrapper(*args, **kwargs):
        print("--- start ---")
        result = func(*args, **kwargs)
        print("--- end ---")
        return result

    return wrapper


@banner
def add(a: int, b: int) -> int:
    return a + b


print("add(2, 3):", add(2, 3))
print()


# ------------------------------------------------------------
# Timing decorator — practical example
# ------------------------------------------------------------
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result

    return wrapper


@timing
def slow_sum(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total


print("result:", slow_sum(500_000))
print()


# ------------------------------------------------------------
# Stacking decorators — applied bottom-up
# ------------------------------------------------------------
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result).upper()

    return wrapper


@uppercase_result
@banner
def status() -> str:
    return "ok"


print(status())
print()


# ------------------------------------------------------------
# Challenge — repeat decorator
# ------------------------------------------------------------
# @repeat(3)
# def say_hi():
#     print("hi")
#
# hi
# hi
# hi


def repeat(times: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_hi() -> None:
    print("hi")


say_hi()
