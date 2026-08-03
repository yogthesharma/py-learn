"""
Enumerations (enum.Enum)

Enums give named constants — safer and clearer than raw strings or ints
scattered through your code. Members are unique, comparable by identity,
and iterable.

Key syntax:
  class Color(Enum):
      RED = 1
      GREEN = auto()     # auto() assigns sequential values

  Color.RED.name         → "RED"
  Color.RED.value        → 1
  Color(1)               → Color.RED  (lookup by value)
  Color["RED"]           → Color.RED  (lookup by name)

Comparison:
  Color.RED == Color.RED   → True
  Color.RED == Color.GREEN → False
  Prefer `is` in if/match — members are singletons

When to use:
  Fixed sets of choices: status codes, roles, order states, config modes
  Function parameters that should only accept known values

Gotcha: plain Enum members are not equal to raw ints/strings —
Color.RED == 1 is False. Use IntEnum or StrEnum when you need that.
"""

from __future__ import annotations

from enum import Enum, auto


# ------------------------------------------------------------
# Basic Enum
# ------------------------------------------------------------
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
print(Color.RED.name, Color.RED.value)
print()


# ------------------------------------------------------------
# auto() — automatic values
# ------------------------------------------------------------
class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


print(Priority.LOW.value, Priority.MEDIUM.value, Priority.HIGH.value)
print()


# ------------------------------------------------------------
# Iterating and membership
# ------------------------------------------------------------
print("All colors:")
for color in Color:
    print(f"  {color.name} = {color.value}")

print(Color.RED in Color)
print()


# ------------------------------------------------------------
# Comparison — members compare by identity, not value
# ------------------------------------------------------------
print(Color.RED == Color.RED)
print(Color.RED == Color.GREEN)
print(Color.RED is Color.RED)
print()


# ------------------------------------------------------------
# Getting a member by value or name
# ------------------------------------------------------------
print(Color(2))           # by value
print(Color["GREEN"])     # by name
print()


# ------------------------------------------------------------
# Challenge — OrderStatus
# ------------------------------------------------------------
# OrderStatus.PENDING.value  -> "pending"
# OrderStatus.SHIPPED.name   -> "SHIPPED"
# list(OrderStatus) has 4 members


class OrderStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


def describe_order(status: OrderStatus) -> str:
    if status is OrderStatus.PENDING:
        return "Waiting for payment"
    if status is OrderStatus.PAID:
        return "Payment received, preparing shipment"
    if status is OrderStatus.SHIPPED:
        return "On the way"
    if status is OrderStatus.DELIVERED:
        return "Delivered"
    return "Unknown"


print(OrderStatus.PENDING.value)
print(OrderStatus.SHIPPED.name)
print("Member count:", len(list(OrderStatus)))
print(describe_order(OrderStatus.SHIPPED))
