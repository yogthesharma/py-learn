"""
Parameters

Positional args match in order: `greet(name)`. Default values:
`def f(city="Gurugram")` — defaults apply when the arg is omitted.

Defaults are evaluated once at definition time; avoid mutable defaults
like `def f(items=[])` — use `None` and create inside the body.

Use defaults for optional settings; required args first, optional after.

Gotcha: `add(5)` uses `b=10` from the default; overriding requires
passing both positionally or by keyword.
"""

# Challange 1
def greet(name):
    print(f"Hello {name}")


greet("Yog")
print()


# Challange 2
def multiply(a, b):
    return a * b


print(multiply(6, 7), end="\n")


# Challenge 3
def introduce(name, city="Gurugram"):
    print(f"Hello my name is {name} and I am from {city}")


introduce("Yog")
introduce("Twinkle", "Ahmedabad")
print()


# Bonus: 15, 25
def add(a, b=10):
    return a + b


print(add(5))
print(add(5, 20))
