"""
While Loop

Repeats while a condition is True. `while True:` plus `break` is a common
pattern for menus and REPL-style input until the user quits.

Use when you do not know how many iterations you need (read until "exit",
retry on bad input, poll until a flag changes).

Gotcha: if the condition never becomes False and you never `break`, you
get an infinite loop — always have an exit path.
"""

EXIT_TEXT = "exit"

while True:
    text = input("Enter your text: ")

    if text.lower() == EXIT_TEXT:
        print("Goodbye!")
        break

    print(f"You Typed: {text}")