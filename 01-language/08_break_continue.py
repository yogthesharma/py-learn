"""
Break and Continue

`break` exits the innermost loop immediately (e.g. quit on "exit").
`continue` skips to the next iteration (skip multiples of 3, ignore negatives).
`pass` is a no-op placeholder for empty blocks.

Use `break` for early exit; `continue` to filter items without nesting
another `if` around the whole body.

Gotcha: `break`/`continue` only affect the loop they're inside — not outer
loops unless you use nested structure carefully.
"""

# Challange 1
for number in range(1, 21):
    if number % 3 == 0:
        continue

    print(number)

print("\n")

# Challange 2
EXIT_COMMAND = "exit"

while True:
    user_input = input("Write a number (write 'exit' to quit): ")

    if user_input.lower() == EXIT_COMMAND:
        break

    number = int(user_input)

    if number < 0:
        print("Negative numbers are ignored!")
        continue

    print(number ** 2)

# Bonus
# pass is used for a placeholder implementation



