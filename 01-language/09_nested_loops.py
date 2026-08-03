"""
Nested Loops

A loop inside another loop: outer controls rows, inner controls columns
(grids, patterns, matrices).

`print(x, end="")` suppresses newline; call bare `print()` after an inner
loop for a new line. Walk 2D data with `for row in matrix: for cell in row`.

Use for tables, ASCII art, comparing every pair, or coordinate-style logic.

Gotcha: complexity grows as outer × inner — fine for small grids; for
large data prefer vectorized libraries or smarter algorithms.
"""

# Challange 1

for row in range(4):
    for col in range(4):
        print("#", end = "")
    print()

print()

# Challange 2
for row in range(5):
    for col in range(row + 1):
        print("#", end="")
    print()
for row in range(3, -1, -1):
    for col in range(row + 1):
        print("#", end="")
    print()

print()

# Challange 3

matrix = [
    [3, 7, 1],
    [9, 2, 5],
    [8, 4, 6]
]

for row in matrix:
    for col in row:
        print(col)

# Bonus i think it will be 0,0 0,1 1,0 1,1