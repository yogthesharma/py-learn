# Challange 1

student = {"name": "Yog", "age": 25, "course": "python"}

student.update({"age": 26})
student["city"] = "Gurgaon"

print(student)
print()

# Challange 2

student_2 = {"name": "Yog Sharma", "course": "Python"}

print("Name: ", student_2["name"])
print("Age: ", student_2.get("age", "Unknown"))
print()

# challange 3

for key, value in student.items():
    print(f"{key} -> {value}")
print()

# challange 4
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 28},
]

for user in users:
    print(user["name"])
