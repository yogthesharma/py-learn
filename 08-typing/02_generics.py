"""
Generics

Sometimes a function or class works the SAME way for many types.
Instead of copying code for list[int], list[str], ... use a type variable.

  T = TypeVar("T")
  def first(items: list[T]) -> T: ...

T is a placeholder — the type checker fills it in from how you call it.

Also: Generic[T] on classes (Stack, Repository, Result, ...).
"""

from __future__ import annotations

from typing import Any, Generic, TypeVar

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


# ------------------------------------------------------------
# Without generics — duplicate or use Any (lose type info)
# ------------------------------------------------------------
def first_any(items: list[Any]) -> Any:
    return items[0]


# ------------------------------------------------------------
# With TypeVar — one function, preserved types
# ------------------------------------------------------------
def first(items: list[T]) -> T:
    return items[0]


print(first([1, 2, 3]))  # type checker knows → int
print(first(["a", "b"]))  # type checker knows → str
print()


# ------------------------------------------------------------
# Multiple type vars
# ------------------------------------------------------------
def get_item(mapping: dict[K, V], key: K) -> V:
    return mapping[key]


print(get_item({"age": 25}, "age"))
print()


# ------------------------------------------------------------
# Generic class — Stack[T]
# ------------------------------------------------------------
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)


numbers = Stack[int]()
numbers.push(10)
numbers.push(20)
print(numbers.pop())  # 20
print(len(numbers))
print()

names = Stack[str]()
names.push("Yog")
print(names.pop())
print()


# ------------------------------------------------------------
# Bounded TypeVar — only subtypes of a base
# ------------------------------------------------------------
NumberT = TypeVar("NumberT", int, float)


def double(value: NumberT) -> NumberT:
    return value * 2  # type: ignore[return-value]


print(double(5))
print(double(2.5))
print()


# ------------------------------------------------------------
# Real backend-ish — generic repository
# ------------------------------------------------------------
class Repository(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def all(self) -> list[T]:
        return list(self._items)


user_repo: Repository[dict[str, str]] = Repository()
user_repo.add({"name": "Yog", "email": "yog@example.com"})
print(user_repo.all())
print()


# ------------------------------------------------------------
# Challenge — Box[T] that holds one value
# ------------------------------------------------------------
# box = Box[int](42)
# print(box.get())  → 42
# box.set(100)


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

    def get(self) -> T:
        return self._value

    def set(self, value: T) -> None:
        self._value = value


box = Box[int](42)
print(box.get())
box.set(100)
print(box.get())

str_box = Box[str]("hello")
print(str_box.get())
