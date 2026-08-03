"""
Unpacking

Split iterables into variables: `first, *middle, last = numbers` — `*`
captures the rest as a list.

Spread into new collections: `[*a, *b]` merges lists; `{**d1, **d2}` merges
dicts (later keys overwrite earlier ones).

Use when splitting head/tail, combining configs, or forwarding arguments.

Gotcha: `{**a, **b}` with duplicate keys keeps the right-hand value —
order matters when merging dicts.
"""

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
