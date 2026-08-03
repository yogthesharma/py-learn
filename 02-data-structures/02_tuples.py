"""
Tuples

Ordered, immutable sequences: `(1, 2, 3)`. Unpack with `a, b, c = t`.

Single-element tuple needs a trailing comma: `("Python",)` — without it
you get a plain string in parentheses.

Use when a fixed bundle of values should not change (coordinates, DB
rows, function return of multiple values).

Gotcha: tuples cannot be appended to; create a new tuple if you need
different data.
"""

# challange 1

person = ("Yog", 25, "Engineer")

name, age, job = person

print(name)
print(age)
print(job)

print()

# challange 2
languages = ("Python",)

print(type(languages))

# challange 3: output 1, 2, 3

numbers = (1, 2, 3)

a, b, c = numbers

print(a)
print(b)
print(c)
