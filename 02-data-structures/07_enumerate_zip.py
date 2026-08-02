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
