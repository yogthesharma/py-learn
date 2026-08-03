"""
Lists

Ordered, mutable sequences: `[1, 2, 3]`. Index from 0; negative indices
from the end.

Mutate in place: `.append()`, `.insert()`, `.remove()`, `.pop()`, `.extend()`.
Copy with `.copy()` or `list(x)` — assignment `b = a` shares the same list.

Use for collections that grow, shrink, or reorder (queues of work, lines
in a file, tags on a post).

Gotcha: `b = a` is not a copy; mutating `b` changes `a` too unless you
copied explicitly.
"""

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
