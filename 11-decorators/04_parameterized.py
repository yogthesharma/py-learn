"""
Parameterized Decorators (Decorator Factories)

A decorator that takes arguments needs three nested levels:
  1. Outer function — receives decorator arguments (e.g. times=3)
  2. Middle function — receives the function to wrap
  3. Inner wrapper — receives call-time *args, **kwargs

  @repeat(3)
  def func(): ...

expands to: func = repeat(3)(func)

The outer call returns the actual decorator; the middle receives func;
the inner wrapper runs on each call.

Always combine with @functools.wraps(func) on the inner wrapper to
preserve metadata (see 03_functools_wraps.py).

Common examples: @retry(times), @timeout(seconds), @cache(maxsize).

Gotcha: forgetting a level — @repeat(3) needs repeat(3) to return
a decorator, not wrap the function directly.
"""

from __future__ import annotations

import functools
import time


# ------------------------------------------------------------
# @repeat(n) — run the function n times
# ------------------------------------------------------------
def repeat(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_result = None
            for _ in range(times):
                last_result = func(*args, **kwargs)
            return last_result

        return wrapper

    return decorator


@repeat(2)
def greet(name: str) -> str:
    print(f"Hello, {name}")
    return name


print("return value:", greet("Alice"))
print()


# ------------------------------------------------------------
# @slowdown(seconds) — delay before running
# ------------------------------------------------------------
def slowdown(seconds: float):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@slowdown(0.05)
def fetch() -> str:
    return "data"


print("fetch():", fetch())
print()


# ------------------------------------------------------------
# Optional arguments — @decorator vs @decorator()
# ------------------------------------------------------------
def debug(_func=None, *, prefix: str = "DEBUG"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix}: calling {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    if _func is None:
        return decorator
    return decorator(_func)


@debug
def plain() -> None:
    print("plain runs")


@debug(prefix="TRACE")
def traced() -> None:
    print("traced runs")


plain()
traced()
print()


# ------------------------------------------------------------
# Challenge — @retry(times=3)
# ------------------------------------------------------------
# Retries on exception up to `times` attempts, then re-raises.


def retry(times: int = 3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error: Exception | None = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    last_error = error
                    print(f"Attempt {attempt}/{times} failed: {error}")
            raise last_error  # type: ignore[misc]

        return wrapper

    return decorator


attempt = 0


@retry(times=3)
def flaky() -> str:
    global attempt
    attempt += 1
    if attempt < 3:
        raise ConnectionError("network down")
    return "success"


print("flaky():", flaky())
