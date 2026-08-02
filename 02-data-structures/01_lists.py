# challange 1

languages = ["python", "rust", "go"]

languages.append("javascript")

languages.insert(1, "typescript")

print(languages)

print()

# challange 2
numbers = [10, 20, 30, 40, 50]

numbers.remove(30)

numbers.pop()

print(numbers)

print()

# challange 3
a = [1, 2]
b = [3, 4]

a.extend(b)

print(a)

print()

a = [1, 2, 3]

b = a.copy()

b.append(4)

print(a)
print(b)
