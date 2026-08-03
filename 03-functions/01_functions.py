"""
Functions

Define reusable blocks with `def name():`. Call with `name()`.
`return` sends a value back; omitting `return` gives `None`.

Functions can return multiple values as a tuple: `return a, b`.

Use to name behavior, avoid duplication, and test logic in isolation.

Gotcha: `print()` inside a function displays output but does not return
a value — callers get `None` unless you `return` something.
"""

# Challange 1


def say_hello():
    print("Hello, Python!")


say_hello()
print()


# Challange 2


def square(number):
    return number**2


print(square(3))
print()

# Challange 3

user_profile = {"name": "Yog", "age": 25}


def get_profile():
    return user_profile["name"], user_profile["age"]


print(get_profile())
print()

# Challange 4, i think output will be None as nothing is being returned


def test():
    print("Inside")


result = test()

print()

print(result)
