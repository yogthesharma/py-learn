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
