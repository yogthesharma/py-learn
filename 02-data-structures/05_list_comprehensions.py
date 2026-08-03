"""
List Comprehensions

Build a list in one expression: `[expr for item in iterable if condition]`.
Often clearer and faster than a manual loop + `.append()`.

Optional filter (`if number % 2`), transform (`number ** 2`), or ternary
(`"even" if n % 2 == 0 else "odd"`).

Use when mapping or filtering a sequence into a new list; prefer a plain
loop when side effects or multi-step logic dominate.

Gotcha: keep comprehensions readable — nested or very long ones are
harder to debug than a `for` loop.
"""

# challange 1
numbers = [number for number in range(1, 6)]

print(numbers)
print()

# challange 2
numbers_2 = [1, 2, 3, 4, 5]
numbers_2_sqrd = [number**2 for number in numbers_2]

print(numbers_2_sqrd)
print()

# challange 3
numbers_odd = [number for number in range(20) if number % 2 != 0]
print(numbers_odd)
print()

# challange 4
languages = ["Python", "Rust", "Go"]
languages_uppercase = [language.upper() for language in languages]
print(languages_uppercase)
print()

# bonus
even_odd = ["even" if number % 2 == 0 else "odd" for number in range(5)]
print(even_odd)
