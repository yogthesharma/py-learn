"""
Type Hints

Annotations that document what types a function expects and returns.
Python does NOT enforce them at runtime — they're for humans, IDEs,
and checkers like mypy / pyright (Cursor uses basedpyright / pyright).

Modern style (3.10+):
  str | None          instead of Optional[str]
  int | float         instead of Union[int, float]
  list[str]           instead of List[str]
  type Alias = ...    for reusable type names (3.12+)

`from __future__ import annotations` lets newer hint syntax work on 3.9+.
"""

from __future__ import annotations

from typing import Any, Literal


# ------------------------------------------------------------
# Without hints — unclear contract
# ------------------------------------------------------------
def greet_raw(name):
    return "Hello " + name


# ------------------------------------------------------------
# With hints — clear input and output
# ------------------------------------------------------------
def greet(name: str) -> str:
    return f"Hello {name}"


print(greet("Yog"))
print()


# ------------------------------------------------------------
# Not enforced at runtime
# ------------------------------------------------------------
def add_demo(a: int, b: int) -> int:
    return a + b


print(add_demo("10", "20"))  # "1020" — still runs! type checkers would warn
print()


# ------------------------------------------------------------
# Variable hints
# ------------------------------------------------------------
name: str = "Yog"
age: int = 25
is_admin: bool = False

print(name, age, is_admin)
print()


# ------------------------------------------------------------
# Collections — say what's inside
# ------------------------------------------------------------
users: list[str] = ["Yog", "Alice"]
scores: dict[str, int] = {
    "Math": 95,
    "Science": 88,
}

print(users)
print(scores)
print()


# ------------------------------------------------------------
# Optional — str | None
# ------------------------------------------------------------
def find_user_by_id(id: int) -> str | None:
    if id == 1:
        return "Yog"
    return None


print(find_user_by_id(1))
print(find_user_by_id(99))
print()


# ------------------------------------------------------------
# Union — int | float
# ------------------------------------------------------------
def square(value: int | float) -> int | float:
    return value * value


print(square(4))
print(square(2.5))
print()


# ------------------------------------------------------------
# Any — "I don't know" (avoid when possible)
# ------------------------------------------------------------
data: Any = {"ok": True}
print(data)
print()


# ------------------------------------------------------------
# Literal — only these exact values
# ------------------------------------------------------------
Status = Literal["pending", "approved", "rejected"]

status: Status = "pending"
print(status)
print()


# ------------------------------------------------------------
# Type alias — name a complex type
# ------------------------------------------------------------
# Python 3.12+: type UserMap = dict[str, list[tuple[int, str]]]
UserMap = dict[str, list[tuple[int, str]]]

# users_map: UserMap = {}


# ------------------------------------------------------------
# Real backend-ish
# ------------------------------------------------------------
def create_user(name: str, email: str, age: int) -> dict[str, str]:
    return {
        "name": name,
        "email": email,
    }


print(create_user("Yog", "yog@example.com", 25))
print()


# ------------------------------------------------------------
# Why FastAPI / Pydantic love this
# ------------------------------------------------------------
# Type hints drive validation, OpenAPI docs, and JSON parsing.


# ------------------------------------------------------------
# Challenge
# ------------------------------------------------------------
def add(a: int, b: int) -> int:
    return a + b


def greet_user(name: str) -> str:
    return f"Hello {name}"


def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


def find_user(user_id: int) -> str | None:
    lookup = {1: "Yog", 2: "Alice"}
    return lookup.get(user_id)


students: list[str] = ["Yog", "Alice", "Bob"]
challenge_scores: dict[str, int] = {"Yog": 88, "Alice": 92}


print(add(2, 3))
print(greet_user("Yog"))
print(average([10, 20, 30]))
print(find_user(1))
print(find_user(99))
print(students)
print(challenge_scores)
print()


# Bonus — Literal role
Role = Literal["admin", "editor", "viewer"]


def set_role(role: Role) -> str:
    return f"Role set to {role}"


print(set_role("admin"))
print(set_role("viewer"))
# set_role("superuser")  # type checker would flag this
