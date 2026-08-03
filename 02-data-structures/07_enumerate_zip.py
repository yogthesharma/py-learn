"""
Enumerate and Zip

`enumerate(iterable, start=0)` yields `(index, item)` — avoid manual
counters when you need both.

`zip(a, b, ...)` pairs elements until the shortest iterable ends; wrap
in `list()` to materialize.

Use `enumerate` for numbered lists; `zip` for parallel columns (names +
scores, keys + values from two lists).

Gotcha: `zip` stops at the shortest input — unequal lengths silently drop
extra items unless you use `zip(..., strict=True)` (3.10+).
"""

# challange 1
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

print()

# challange 2
students = ["Alice", "Bob", "Charlie"]
scores = [95, 88, 91]

for student, score in zip(students, scores):
    print(f"{student} -> {score}")

print()

# challange 3: dont wanna write the full output but list of tuples till two values
a = [1, 2, 3]
b = ["A", "B"]


print(list(zip(a, b)))
print()


# challange 4
languages = ["Python", "Rust", "Go"]

for index, language in enumerate(languages):
    print("Index", index, ":", language)
