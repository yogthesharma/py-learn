"""
Range

`range(stop)`, `range(start, stop)`, `range(start, stop, step)` produces
lazy integers — memory-efficient for large spans.

Index like a sequence: `range(50)[0]`, `len(range(50))`. Membership:
`n in range(1, 100, 3)`.

Use instead of building `[0, 1, 2, ...]` when you only need counting
or looping; pair with `for` for most cases.

Gotcha: `range` excludes the stop value; step can be negative for
countdowns.
"""

# challange 1
numbers = range(50)
numbers_length = len(numbers)

print(f"First: ", numbers[0])
print(f"Last: ", numbers[numbers_length - 1])

print("\n")

# challange 2
EXIT_COMMAND = "exit"

numbers_for_check = range(1, 100, 3)

print("Welcome to number checking in the current range!")

while True:
    user_input = input("Write your number (write 'exit' to quit): ")
    
    if user_input.lower() == EXIT_COMMAND:
        break

    number = int(user_input)

    if number in numbers_for_check:
        print(f"{number} is in the range")
    else:
        print(f"{number} is not in the range")

    
