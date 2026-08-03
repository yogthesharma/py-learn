"""
Input

`input()` always returns a string — even when the user types digits.
Cast with `int()`, `float()`, etc. before doing math.

Use `input()` for interactive scripts and small CLI tools; for anything
non-interactive prefer config files, env vars, or command-line args.

Gotcha: invalid casts (e.g. `int("abc")`) raise ValueError; validate or
wrap in try/except when input is untrusted.
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(type(age))
city = input("Enter your city: ")
favourite_language = input("Enter your favourite programing language: ")

print(f"Name: {name.title()}")
print(f"Age: {age}")
print(f"City: {city.capitalize()}")
print(f"Favourite Programing Language: {favourite_language.capitalize()}")
