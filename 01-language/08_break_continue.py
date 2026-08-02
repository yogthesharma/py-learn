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



