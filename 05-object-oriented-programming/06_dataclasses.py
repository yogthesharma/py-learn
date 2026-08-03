"""
Dataclasses

@dataclass generates __init__, __repr__, and __eq__ from type-annotated
fields — ideal for classes that are mostly data (DTOs, config, API responses).

Key syntax:
  @dataclass
  class User:
      name: str
      age: int = 18
      tags: list[str] = field(default_factory=list)

Important:
  Never use mutable defaults directly (items: list = []) — all instances
  share the same object. Use field(default_factory=list) instead.
  Type hints guide code generation; Python does not enforce them at runtime.

Options you'll see:
  frozen=True       — immutable instances (config, hashable keys)
  order=True        — generate comparison methods (<, >, ...)
  field(repr=False) — hide sensitive fields from __repr__
  __post_init__     — custom logic after the generated __init__

Use @dataclass for typed bags of fields. Use a normal class when behavior
(deposit/withdraw, validation, complex invariants) is the main focus.
"""

from dataclasses import dataclass, field


# ------------------------------------------------------------
# The problem — repetitive __init__
# ------------------------------------------------------------
class UserManual:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


print(UserManual("Yog", 25, "yog@example.com"))
# <__main__.UserManual object at 0x...>  — no nice __repr__
print()


# ------------------------------------------------------------
# @dataclass — Python generates __init__, __repr__, __eq__
# ------------------------------------------------------------
@dataclass
class User:
    name: str
    age: int
    email: str


user = User("Yog", 25, "yog@example.com")
print(user)  # User(name='Yog', age=25, email='yog@example.com')
print(user.name)
print()


# ------------------------------------------------------------
# Type hints — not assignments
# ------------------------------------------------------------
# name: str   → tells dataclass the field type
# They help generate the constructor; they don't enforce types at runtime.


# ------------------------------------------------------------
# Default values
# ------------------------------------------------------------
@dataclass
class UserWithDefault:
    name: str
    age: int = 18


print(UserWithDefault("Yog"))  # UserWithDefault(name='Yog', age=18)
print()


# ------------------------------------------------------------
# Mutable defaults ❌ — shared across ALL instances
# ------------------------------------------------------------
# Don't do: items: list[str] = []
# Every Cart would share the SAME list.


# ------------------------------------------------------------
# field(default_factory=...) — each object gets its own list
# Prefer list[str] over bare list (what the list contains)
# Older Python: from typing import List → List[str]
# ------------------------------------------------------------
@dataclass
class Cart:
    items: list[str] = field(default_factory=list)


cart_a = Cart()
cart_b = Cart()
cart_a.items.append("Laptop")

print(cart_a.items)  # ['Laptop']
print(cart_b.items)  # []  — separate lists
print()


# ------------------------------------------------------------
# __post_init__ — custom logic AFTER generated __init__
# ------------------------------------------------------------
@dataclass
class GreetingUser:
    name: str

    def __post_init__(self):
        print(f"Created {self.name}")


GreetingUser("Yog")
print()


# ------------------------------------------------------------
# frozen=True — immutable (great for config)
# ------------------------------------------------------------
@dataclass(frozen=True)
class FrozenUser:
    id: int
    name: str


frozen = FrozenUser(1, "Yog")
print(frozen)
# frozen.name = "John"  # raises FrozenInstanceError
print()


# ------------------------------------------------------------
# Real backend-ish example — config
# field(repr=False) keeps secrets out of the generated __repr__
# ------------------------------------------------------------
@dataclass
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str = field(repr=False)


config = DatabaseConfig("localhost", 5432, "admin", "secret")
print(config)
# DatabaseConfig(host='localhost', port=5432, username='admin')
# password still exists on the object — just omitted from print/repr
print()


# ------------------------------------------------------------
# Also exists: @dataclass(order=True)
# ------------------------------------------------------------
# Generates comparison methods so student1 < student2 works
# (e.g. by marks). Useful to know — not needed for every class.


# ------------------------------------------------------------
# When to use
# ------------------------------------------------------------
# ✅ data-focused: User DTO, API response, settings, coordinates
# ❌ behavior-focused: BankAccount with deposit/withdraw/transfer


# ------------------------------------------------------------
# Challenge
# ------------------------------------------------------------
# Create Student with name, age, course, marks (default = 0).
#
# student = Student("Yog", 25, "Computer Science")
# print(student)
# → Student(name='Yog', age=25, course='Computer Science', marks=0)
#
# Bonus: ShoppingCart with items = field(default_factory=list)
# cart1.items.append("Laptop") should NOT appear in cart2.items


@dataclass
class Student:
    name: str
    age: int
    course: str
    marks: int = 0


student = Student("Yog", 25, "Computer Science")
print(student)
print()


@dataclass
class ShoppingCart:
    items: list[str] = field(default_factory=list)


cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.items.append("Laptop")

print(cart1.items)  # ['Laptop']
print(cart2.items)  # []
