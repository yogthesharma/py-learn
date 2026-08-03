"""
Decorators Intro

Functions are first-class: assign them, pass them, return them from other
functions. Closures capture variables from the enclosing scope.

A decorator wraps a function: `wrapper` runs before/after the original.
Manual: `greet = decorator(greet)`. Sugar: `@decorator` above `def`.

Use for cross-cutting behavior (logging, timing, auth) without changing
every call site.

Gotcha: `@decorator` replaces the function object — use `functools.wraps`
(later lesson) to preserve `__name__` and docstrings.
"""

# Challenge 1


def greet():
    print("Hello")


hello = greet

hello()

# Output Hello


# Challenge 2


def outer():

    def inner():
        print("Python")

    return inner


func = outer()

func()

# Output: Python


# Challenge 3


# Given:
def decorator(function):

    def wrapper():
        print("Before")

        function()

        print("After")

    return wrapper


# Decorate:
def greet():
    print("Hello")


greet = decorator(greet)

greet()

print()

# Challenge 4: This means that we're wrapping this function with another functions that runs before and after the invocation of this funtion


@decorator
def greet():
    print("Hello")


greet()
