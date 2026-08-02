# challange 1

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers

print(first, last)
print()

# challange 2
frontend = ["React", "Vue"]
backend = ["Python", "Go"]

full_stack = [*frontend, *backend]

print(full_stack)
print()

# challange 3
user = {"name": "Yog"}
details = {"city": "Gurgaon"}

user_details = {**user, **details}

print(user_details)
print()

# challange 4: output = {x: 2}
a = {"x": 1}
b = {"x": 2}

print({**a, **b})
