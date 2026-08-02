# Challange 1

age = int(input("Please provide your age: "));

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Challange 2
USERNAME = "admin"
PASSWORD = "python123"

username = input("Username: ")
password = input("Password: ")

if username == USERNAME and password == PASSWORD:
    print("Login Successful")
else:
    print("Invalid Credentials")

# Challange 3
amount = int(input("What is your total purchase amount: "))

if amount >= 1000:
    print(f"You're eligible for 20% discount and your total is {round(amount * 0.2, 2)}")
elif amount >= 500:
    print(f"You're eligible for 10% discount and your total is {round(amount * 0.1, 2)}")
else:
    print(f"Sorry you're not eligible for any discount")
