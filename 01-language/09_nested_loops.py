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