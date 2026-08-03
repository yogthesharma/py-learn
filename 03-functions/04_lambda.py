"""
Lambda

Anonymous one-expression functions: `lambda x: x ** 2`. Limited to a
single expression — no statements or assignments.

Common with `sorted(items, key=lambda x: x["marks"])` and similar
`key=` callbacks.

Use for tiny throwaway functions; prefer `def` when logic grows or you
need a name for debugging.

Gotcha: `sorted()` returns a new list; `.sort()` mutates in place —
pick the one that matches whether you need the original preserved.
"""

# Challenge 1

square = lambda number: number**2

print(square(2))
print()

# Challenge 2

is_positive = lambda number: number > 0

print(is_positive(2))
print(is_positive(-2))
print()

# Challenge 3

numbers = [5, 1, 4, 2, 3]
sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)

# Challenge 4
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 78},
]

students.sort(key=lambda student: student["marks"], reverse=True)

print(students)

# Interview question's answer the difference is sorted doesnt mutate the original list
