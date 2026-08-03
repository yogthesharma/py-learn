"""
*args and **kwargs

`*args` collects extra positional arguments as a tuple.
`**kwargs` collects extra keyword arguments as a dict.

Signature order: positional, `*args`, keyword-only, `**kwargs`.
Call with `func(**dict)` to expand a dict into keyword args.

Use when arity is variable (logging, wrappers, forwarding to another API).

Gotcha: names `*args` / `**kwargs` are convention — the stars matter,
not the identifiers.
"""

# Challenge 1
def total(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum


print(total(1, 2, 3), end="\n")


# Challenge 2
def print_user(**details):
    for key, value in details.items():
        print(key, "=>", value)


print_user(name="Yog", age=25, city="Gurgaon")
print()


# Challenge 3
def introduce(greeting, *names):
    print(greeting)

    for name in names:
        print(name)


introduce("Hello", "Yog", "Alice", "Bob")


# Challange 4
def create_user(**user):
    print(user)


user = {"name": "Yog", "age": 25}
create_user(name="Yog", age=25)
