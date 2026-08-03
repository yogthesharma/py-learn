"""
For Loop

Iterate over any iterable: `range()`, lists, strings, dict keys, etc.
Syntax: `for item in iterable:` — no manual index unless you need one.

`continue` skips the rest of the current iteration and moves to the next.
Use `for` when you know what you're walking (a sequence, a fixed count).

Gotcha: changing a list while iterating it can skip or repeat elements;
iterate a copy or build a new list instead.
"""

for number in range(1, 11):
    print(number)

print("\n")

for number in range(1,25, 2):
    print(number)

print("\n")

for number in range(25):
    if number % 2 != 0:
        print(number)
    continue