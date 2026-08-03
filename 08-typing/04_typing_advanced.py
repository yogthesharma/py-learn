"""
Advanced Typing

Extra tools you'll see in real backends and libraries:

  TypedDict   — dict with known keys / value types
  Callable    — type a function parameter
  NewType     — distinct type based on an existing one
  Final       — should not be reassigned / overridden
  ClassVar    — class attribute, not per-instance
  overload    — different return types by input (for checkers)
  cast()      — tell the checker "trust me" (use sparingly)

Still not enforced at runtime — these help humans and type checkers.
"""

from __future__ import annotations

from typing import (
    Callable,
    ClassVar,
    Final,
    NewType,
    TypedDict,
    cast,
    overload,
)


# ------------------------------------------------------------
# TypedDict — structured dicts (JSON / API payloads)
# ------------------------------------------------------------
class UserDict(TypedDict):
    id: int
    name: str
    email: str


user: UserDict = {
    "id": 1,
    "name": "Yog",
    "email": "yog@example.com",
}

print(user["name"])
print()


class PartialUser(TypedDict, total=False):
    """All keys optional — common for PATCH bodies."""

    name: str
    email: str


patch: PartialUser = {"name": "Yog Sharma"}
print(patch)
print()


# ------------------------------------------------------------
# Callable — pass functions around safely
# ------------------------------------------------------------
Handler = Callable[[str], str]


def shout(text: str) -> str:
    return text.upper()


def whisper(text: str) -> str:
    return text.lower()


def apply(handler: Handler, text: str) -> str:
    return handler(text)


print(apply(shout, "hello"))
print(apply(whisper, "HELLO"))
print()


# ------------------------------------------------------------
# NewType — same at runtime, different to the type checker
# ------------------------------------------------------------
UserId = NewType("UserId", int)
OrderId = NewType("OrderId", int)


def get_user(user_id: UserId) -> str:
    return f"user:{user_id}"


uid = UserId(42)
print(get_user(uid))
# get_user(OrderId(1))  # type checker should flag this
# get_user(42)          # type checker should flag this (raw int)
print()


# ------------------------------------------------------------
# Final — don't reassign
# ------------------------------------------------------------
API_URL: Final = "https://api.example.com"
# API_URL = "other"  # type checker error

print(API_URL)
print()


# ------------------------------------------------------------
# ClassVar — shared on the class, not an instance field
# ------------------------------------------------------------
class Config:
    env: ClassVar[str] = "development"
    host: str

    def __init__(self, host: str) -> None:
        self.host = host


print(Config.env, Config("localhost").host)
print()


# ------------------------------------------------------------
# overload — different signatures for the type checker
# ------------------------------------------------------------
@overload
def parse(value: str) -> str: ...


@overload
def parse(value: int) -> int: ...


def parse(value: str | int) -> str | int:
    return value


print(parse("hi"))
print(parse(7))
print()


# ------------------------------------------------------------
# cast — assert a type to the checker (no runtime change)
# ------------------------------------------------------------
raw: object = "yog@example.com"
email = cast(str, raw)
print(email.upper())
print()


# ------------------------------------------------------------
# Real backend-ish — typed API response
# ------------------------------------------------------------
class ApiUser(TypedDict):
    id: int
    name: str


def fetch_user() -> ApiUser:
    return {"id": 1, "name": "Yog"}


def format_user(formatter: Callable[[ApiUser], str]) -> str:
    return formatter(fetch_user())


print(format_user(lambda u: f"{u['name']} (#{u['id']})"))
print()


# ------------------------------------------------------------
# Challenge
# ------------------------------------------------------------
# 1. Product TypedDict: id (int), title (str), price (float)
# 2. discount(product, percent) -> float
# 3. NewType ProductId
# 4. Callable that maps Product -> str and print it


class Product(TypedDict):
    id: int
    title: str
    price: float


ProductId = NewType("ProductId", int)


def discount(product: Product, percent: float) -> float:
    return product["price"] * (1 - percent / 100)


def describe(product: Product) -> str:
    return f"{product['title']}: ${product['price']:.2f}"


def show_product(product: Product, formatter: Callable[[Product], str]) -> None:
    print(formatter(product))


laptop: Product = {"id": 1, "title": "Laptop", "price": 1000.0}
pid = ProductId(laptop["id"])

print("id:", pid)
print("sale:", discount(laptop, 10))
show_product(laptop, describe)
