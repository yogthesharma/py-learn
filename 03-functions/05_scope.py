"""
Scope

LEGB: Local → Enclosing → Global → Built-in. Assignment inside a function
creates a local name unless declared `global` or `nonlocal`.

Reading an enclosing name works; rebinding it in an inner function needs
`nonlocal`. Locals vanish when the function returns.

Use nested functions for helpers that need enclosing state; avoid
`global` except for small scripts.

Gotcha: `count += 1` inside a function makes `count` local — it does not
update the outer variable without `nonlocal`/`global`.
"""

# Challenge 1

name = "Yog"


def greet():
    name = "Alice"
    print(name)


greet()

print(name)

# Output: Alice, Yog


# Challenge 2
def test():
    value = 10


test()

print(value)

# Will this work no value is outta scope


# Challenge 3
count = 0


def increment(count):
    count += 1


count = increment(count)

print(count)

# Challenge 4
x = 100


def outer():
    x = 50

    def inner():
        print(x)

    inner()


outer()
# output 50

# Interview question
# I dont know may be because we can read it but can't mutate
