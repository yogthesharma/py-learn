"""
Static Methods & Class Methods

Instance methods need an object (self).
Class methods need the class (cls) — often factory methods.
Static methods need neither — related utilities.

Ask:
  Needs object data?     → instance method (self)
  Needs the class?       → class method (cls)
  Needs neither?         → static method
"""


# ------------------------------------------------------------
# Reminder — instance methods need an object
# ------------------------------------------------------------
class User:
    def __init__(self, name: str):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")


user = User("Yog")
user.greet()  # Python roughly does: User.greet(user)
print()


# ------------------------------------------------------------
# Problem — utility that doesn't need object data
# ------------------------------------------------------------
# Creating Math() just to call add() is pointless.


# ------------------------------------------------------------
# @staticmethod — no self, no cls, call on the class
# ------------------------------------------------------------
class Math:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b


print(Math.add(10, 20))  # 30 — no object created
print()


class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return (c * 9 / 5) + 32


print(Temperature.celsius_to_fahrenheit(30))
print()


# ------------------------------------------------------------
# @classmethod — first arg is the class (cls), not an object
# Common for factory methods: from_dict, from_json, from_api
# ------------------------------------------------------------
class NamedUser:
    def __init__(self, name: str):
        self.name = name

    @classmethod
    def from_dict(cls, data: dict):
        # cls is NamedUser when you call NamedUser.from_dict(...)
        return cls(data["name"])


data = {"name": "Yog"}
named = NamedUser.from_dict(data)
print(named.name)  # Yog
print()


# ------------------------------------------------------------
# Class variables — shared by every instance
# ------------------------------------------------------------
# Instance var (self.name): each object has its own
# Class var (company): one value shared by the class / all objects


class EmployeeInfo:
    company = "Google"

    @classmethod
    def company_name(cls) -> str:
        return cls.company


print(EmployeeInfo.company_name())  # Google
print()


# ------------------------------------------------------------
# Real backend-ish example — factory from a "row"
# ------------------------------------------------------------
class UserResponse:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @classmethod
    def from_database(cls, row: dict):
        return cls(row["id"], row["name"])

    def __repr__(self):
        return f"UserResponse(id={self.id}, name='{self.name}')"


print(UserResponse.from_database({"id": 1, "name": "Yog"}))
print()


# ------------------------------------------------------------
# Quick comparison
# ------------------------------------------------------------
# Instance | self | needs object data
# Class    | cls  | needs class (factories, class vars)
# Static   | —    | related utility, no object/class state


# ------------------------------------------------------------
# Challenge
# ------------------------------------------------------------
# Employee with:
#   class var: company = "OpenAI"
#   __init__(name, salary)
#   display()          → "Yog earns 100000"
#   from_dict(data)    → classmethod factory
#   is_valid_salary()  → staticmethod, True if amount > 0


class Employee:
    company = "OpenAI"

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name} earns {self.salary}")

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["salary"])

    @staticmethod
    def is_valid_salary(amount: int) -> bool:
        return amount > 0


employee = Employee.from_dict({"name": "Yog", "salary": 100000})

employee.display()
print(Employee.company)
print(Employee.is_valid_salary(100000))
print(Employee.is_valid_salary(-10))
