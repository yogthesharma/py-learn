EXIT_TEXT = "exit"

while True:
    text = input("Enter your text: ")

    if text.lower() == EXIT_TEXT:
        print("Goodbye!")
        break

    print(f"You Typed: {text}")