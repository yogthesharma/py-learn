"""
Custom Exceptions

Built-in exceptions (ValueError, TypeError, ...) are fine for generic
failures. For business rules, create named exception types so callers
can catch exactly what they mean.

  except InsufficientBalanceError:  → clear intent
  except ValueError:                → could be anything

Every custom exception inherits from Exception (or a shared AppError base).
Name them after the problem: UserNotFoundError, not MyError.
"""


# ------------------------------------------------------------
# The problem — one ValueError for every business failure
# ------------------------------------------------------------
class VagueAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount


# Caller: except ValueError — was it age? email? balance? unclear.


# ------------------------------------------------------------
# Custom exception — empty subclass is enough
# ------------------------------------------------------------
class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance.")
        self.balance -= amount


try:
    BankAccount(100).withdraw(500)
except InsufficientBalanceError as error:
    print(error)
print()


# ------------------------------------------------------------
# Why it matters — map errors to API responses
# ------------------------------------------------------------
# except InvalidTokenError:         → 401
# except InsufficientBalanceError:  → 400
# except UserNotFoundError:         → 404


# ------------------------------------------------------------
# Custom exception with data
# ------------------------------------------------------------
class ValidationError(Exception):
    def __init__(self, field: str):
        self.field = field
        super().__init__(f"Invalid {field}")


try:
    raise ValidationError("email")
except ValidationError as error:
    print(error)  # Invalid email
    print(error.field)  # email
print()


# ------------------------------------------------------------
# Hierarchy — catch all app errors, or one specific type
# ------------------------------------------------------------
class AppError(Exception):
    pass


class AuthenticationError(AppError):
    pass


class DatabaseError(AppError):
    pass


try:
    raise AuthenticationError("Invalid token")
except AppError as error:
    print("Caught via AppError:", error)
print()


# ------------------------------------------------------------
# Real backend-ish — register
# ------------------------------------------------------------
class UserAlreadyExistsError(Exception):
    pass


def register(email: str) -> None:
    if email == "admin@example.com":
        raise UserAlreadyExistsError("User already exists.")
    print("Registered:", email)


try:
    register("admin@example.com")
except UserAlreadyExistsError:
    print("409 Conflict")
print()


# ------------------------------------------------------------
# Naming — describe the problem
# ------------------------------------------------------------
# ✅ UserNotFoundError, PaymentFailedError, InvalidTokenError
# ❌ MyError, CustomError, OopsError


# ------------------------------------------------------------
# Challenge
# ------------------------------------------------------------
# InvalidAgeError if age < 18
# EmailAlreadyExistsError if email == "admin@example.com"
# else print "User registered."


class InvalidAgeError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


def register_user(name: str, age: int, email: str) -> None:
    if age < 18:
        raise InvalidAgeError("Must be 18+.")
    if email == "admin@example.com":
        raise EmailAlreadyExistsError("Email already exists.")
    print("User registered.")


def try_register(name: str, age: int, email: str) -> None:
    try:
        register_user(name, age, email)
    except InvalidAgeError as error:
        print("Invalid age:", error)
    except EmailAlreadyExistsError as error:
        print("Email taken:", error)


try_register("Yog", 16, "yog@example.com")
try_register("Yog", 25, "admin@example.com")
try_register("Yog", 25, "yog@example.com")
