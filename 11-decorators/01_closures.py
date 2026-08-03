"""
Closures

Functions are first-class objects in Python — assign them to variables,
pass them as arguments, return them from other functions.

A closure is a nested function that remembers variables from its
enclosing scope, even after the outer function has finished.

  def make_multiplier(factor):
      def multiply(n):
          return n * factor   # `factor` captured from enclosing scope
      return multiply

  double = make_multiplier(2)
  double(5)  → 10

The inner function "closes over" free variables from the outer scope.
Each call to the outer function creates a new closure with its own captured values.

Closures are the foundation of decorators — a decorator factory returns
a closure that wraps the original function.

Gotcha: closures capture variables by reference, not by value at definition
time — mutating a captured mutable (list, dict) affects all closures sharing it.
Use default args (lambda x, f=factor: ...) to capture by value when needed.
"""

from __future__ import annotations


# ------------------------------------------------------------
# Functions as objects
# ------------------------------------------------------------
def greet(name: str) -> str:
    return f"Hello, {name}!"


say_hello = greet  # same function object, different name
print(say_hello("World"))
print("greet is say_hello:", greet is say_hello)
print()


# ------------------------------------------------------------
# Nested functions
# ------------------------------------------------------------
def outer(message: str):
    def inner(name: str) -> str:
        return f"{message}, {name}!"

    return inner


welcome = outer("Welcome")
print(welcome("Alice"))
print()


# ------------------------------------------------------------
# Closures capture variables
# ------------------------------------------------------------
def make_multiplier(factor: int):
    def multiply(n: int) -> int:
        return n * factor  # `factor` captured from enclosing scope

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print("double(5):", double(5))
print("triple(5):", triple(5))
print()


# ------------------------------------------------------------
# Late binding gotcha — use default args to capture loop vars
# ------------------------------------------------------------
def make_adders_bad():
    funcs = []
    for i in range(3):
        funcs.append(lambda x: x + i)  # i is looked up when called
    return funcs


def make_adders_good():
    funcs = []
    for i in range(3):
        funcs.append(lambda x, i=i: x + i)  # i captured at definition time
    return funcs


bad = make_adders_bad()
good = make_adders_good()

print("bad adders:", [f(10) for f in bad])    # all use final i=2
print("good adders:", [f(10) for f in good])  # 10, 11, 12
print()


# ------------------------------------------------------------
# Challenge — make_counter
# ------------------------------------------------------------
# counter = make_counter()
# counter() -> 1
# counter() -> 2
# counter() -> 3


def make_counter():
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()
print(counter())
print(counter())
print(counter())
