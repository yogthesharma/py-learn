"""
Protocols

Duck typing, with type checker support:

  "If it walks like a duck and quacks like a duck..."

A Protocol describes the *shape* (methods/attributes) something must have.
You don't need to inherit from it — matching the interface is enough.

Contrast:
  ABC / inheritance  → nominal typing (must subclass)
  Protocol           → structural typing (just have the methods)
"""

from __future__ import annotations

from typing import Iterable, Protocol, runtime_checkable


# ------------------------------------------------------------
# The idea — care about behavior, not class name
# ------------------------------------------------------------
class Duck:
    def quack(self) -> str:
        return "quack"


class Person:
    def quack(self) -> str:
        return "I'm pretending to quack"


def make_it_quack(thing) -> None:  # untyped — anything goes
    print(thing.quack())


make_it_quack(Duck())
make_it_quack(Person())
print()


# ------------------------------------------------------------
# Protocol — typed duck typing
# ------------------------------------------------------------
class Quackable(Protocol):
    def quack(self) -> str: ...


def make_it_quack_typed(thing: Quackable) -> None:
    print(thing.quack())


make_it_quack_typed(Duck())
make_it_quack_typed(Person())
print()


# ------------------------------------------------------------
# Useful protocol — anything with .read()
# ------------------------------------------------------------
class Readable(Protocol):
    def read(self) -> str: ...


class FileLike:
    def read(self) -> str:
        return "file contents"


class FakeResponse:
    def read(self) -> str:
        return '{"ok": true}'


def load_text(source: Readable) -> str:
    return source.read()


print(load_text(FileLike()))
print(load_text(FakeResponse()))
print()


# ------------------------------------------------------------
# runtime_checkable — isinstance works (methods only)
# ------------------------------------------------------------
@runtime_checkable
class Closable(Protocol):
    def close(self) -> None: ...


class Connection:
    def close(self) -> None:
        print("closed")


print(isinstance(Connection(), Closable))  # True
print(isinstance(object(), Closable))  # False
print()


# ------------------------------------------------------------
# Iterable is a Protocol (built-in idea)
# ------------------------------------------------------------
def print_all(items: Iterable[str]) -> None:
    for item in items:
        print(item)


print_all(["a", "b"])
print_all(("x", "y"))
print()


# ------------------------------------------------------------
# Real backend-ish — payment processor shape
# ------------------------------------------------------------
class PaymentProcessor(Protocol):
    def charge(self, amount: float) -> bool: ...


class StripeClient:
    def charge(self, amount: float) -> bool:
        print(f"Stripe charged {amount}")
        return True


class FakePayment:
    def charge(self, amount: float) -> bool:
        print(f"Fake charged {amount}")
        return True


def checkout(processor: PaymentProcessor, amount: float) -> None:
    ok = processor.charge(amount)
    print("Success:" if ok else "Failed:", amount)


checkout(StripeClient(), 19.99)
checkout(FakePayment(), 5.0)
print()


# ------------------------------------------------------------
# Challenge — Speaks protocol + say_hello()
# ------------------------------------------------------------
# class Speaks(Protocol):
#     def speak(self) -> str: ...
#
# def say_hello(speaker: Speaks) -> None:
#     print(speaker.speak())


class Speaks(Protocol):
    def speak(self) -> str: ...


class Dog:
    def speak(self) -> str:
        return "Woof!"


class Robot:
    def speak(self) -> str:
        return "Beep boop"


def say_hello(speaker: Speaks) -> None:
    print(speaker.speak())


say_hello(Dog())
say_hello(Robot())
