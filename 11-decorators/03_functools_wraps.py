"""
functools.wraps — Preserve Function Metadata

A bare decorator wrapper becomes the function users see — its __name__,
__doc__, __module__, and __annotations__ come from the wrapper, not the
original. That breaks help(), debuggers, and pytest discovery.

Fix — decorate the wrapper with @functools.wraps(func):
  def my_decorator(func):
      @functools.wraps(func)
      def wrapper(*args, **kwargs):
          return func(*args, **kwargs)
      return wrapper

wraps copies metadata from func onto wrapper so help(decorated_func)
still shows the original docstring and name.

Always use @wraps(func) when writing decorators — one line prevents
confusing stack traces and broken introspection.

Does not preserve the exact signature for type checkers; for that,
look at functools.wraps plus typing.ParamSpec (advanced).
"""

from __future__ import annotations

import functools


# ------------------------------------------------------------
# Without wraps — metadata is lost
# ------------------------------------------------------------
def bare_decorator(func):
    def wrapper(*args, **kwargs):
        """Wrapper docstring."""
        return func(*args, **kwargs)

    return wrapper


@bare_decorator
def original_bad() -> None:
    """Original docstring."""
    pass


print("Without wraps:")
print("  __name__:", original_bad.__name__)
print("  __doc__:", original_bad.__doc__)
print()


# ------------------------------------------------------------
# With wraps — metadata preserved
# ------------------------------------------------------------
def good_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper docstring."""
        return func(*args, **kwargs)

    return wrapper


@good_decorator
def original_good() -> None:
    """Original docstring."""
    pass


print("With wraps:")
print("  __name__:", original_good.__name__)
print("  __doc__:", original_good.__doc__)
print()


# ------------------------------------------------------------
# Why it matters — debugging and introspection
# ------------------------------------------------------------
# stack traces, help(), logging, and test frameworks use __name__.
# Lost metadata makes "which function failed?" much harder to answer.


# ------------------------------------------------------------
# Challenge — logged decorator with wraps
# ------------------------------------------------------------
# @logged
# def add(a, b):
#     return a + b
#
# Calling add(2, 3) prints:
#   Calling add(2, 3)
#   add returned 5


def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}{args}{kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


@logged
def add(a: int, b: int) -> int:
    return a + b


print("add(2, 3):", add(2, 3))
print("add.__name__:", add.__name__)
