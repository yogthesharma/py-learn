"""
raise

Catching exceptions is only half the story — something has to create them.
`raise` lets YOUR code signal failures so callers can handle them.

print() is for humans.
raise is for programs.

Bare `raise` (with no exception) re-raises the current exception — common after logging.
"""


# ------------------------------------------------------------
# The problem — print + return hides failure from the caller
# ------------------------------------------------------------
class BadBankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        if amount < 0:
            print("Invalid amount")
            return
        self.balance -= amount


bad = BadBankAccount(100)
bad.withdraw(-100)
print("Money transferred.")  # still prints — oops
print()


# ------------------------------------------------------------
# raise — fail loudly with a clear message
# ------------------------------------------------------------
class SimpleAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.balance -= amount


try:
    SimpleAccount(100).withdraw(-100)
except ValueError as error:
    print(error)
print()


# ------------------------------------------------------------
# Built-in exception types — pick the best fit
# ------------------------------------------------------------
# raise ValueError("Invalid value")
# raise TypeError("Expected string")
# raise RuntimeError("Unexpected state")
# raise FileNotFoundError("Missing config")


# ------------------------------------------------------------
# Validation — most common use of raise
# ------------------------------------------------------------
def create_user(email: str) -> dict:
    if "@" not in email:
        raise ValueError("Invalid email address.")
    return {"email": email}


try:
    create_user("hello")
except ValueError as error:
    print(error)
print()


def register(name: str, age: int) -> None:
    if not name:
        raise ValueError("Name required.")
    if age < 18:
        raise ValueError("Must be 18+.")
    print("Registered.")


try:
    register("", 25)
except ValueError as error:
    print(error)

try:
    register("Yog", 16)
except ValueError as error:
    print(error)

register("Yog", 25)
print()


# ------------------------------------------------------------
# Re-raise — log, then throw the SAME exception again
# ------------------------------------------------------------
try:
    try:
        int("hello")
    except ValueError as error:
        print("Logged:", error)
        raise  # bare raise → re-throw current exception
except ValueError as error:
    print("Caller handled:", error)
print()


# ------------------------------------------------------------
# Chaining — keep both errors for debugging
# ------------------------------------------------------------
try:
    try:
        int("hello")
    except ValueError as error:
        raise RuntimeError("User input failed.") from error
except RuntimeError as error:
    print(error)
    print("Cause:", error.__cause__)
print()


# ------------------------------------------------------------
# Library style — report the problem, don't catch it here
# ------------------------------------------------------------
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


try:
    print(divide(10, 2))
    divide(10, 0)
except ZeroDivisionError as error:
    print(error)
print()


# ------------------------------------------------------------
# Challenge — BankAccount with raise instead of print/return
# ------------------------------------------------------------
# deposit(0) / deposit(-1) → ValueError: Deposit amount must be positive.
# withdraw(0) / withdraw(-1) → ValueError: Withdraw amount must be positive.
# withdraw(too much) → ValueError: Insufficient balance.


class BankAccount:
    def __init__(self, balance: float = 0):
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount


account = BankAccount(100)

try:
    account.deposit(-100)
except ValueError as error:
    print(error)

try:
    account.withdraw(0)
except ValueError as error:
    print(error)

try:
    account.withdraw(500)
except ValueError as error:
    print(error)

account.deposit(50)
account.withdraw(30)
print("Balance:", account.balance)
