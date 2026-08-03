"""
Sets

Unordered collections of unique hashable items: `{1, 2, 3}`. `set(list)`
deduplicates.

Set algebra: `|` union, `&` intersection, `-` difference, `^` symmetric
difference. `.add()` ignores duplicates.

Use for membership tests, removing duplicates, and comparing collections
(shared tags, unique visitors, allowed IDs).

Gotcha: sets are unordered — no indexing. Elements must be immutable
(no lists inside sets).
"""

# challange 1
numbers = [1, 2, 2, 3, 4, 4, 5]

print(set(numbers))
print()

# challange 2
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union: ", a | b)
print("Intersection: ", a & b)
print("Difference: ", a - b)
print("Symmetric Difference: ", a ^ b)

# challange 3: output = {"Python", "Rust"}
languages = {"Python", "Rust"}

languages.add("Python")

print(languages)
