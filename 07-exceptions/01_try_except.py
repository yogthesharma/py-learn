"""
Try / Except

Exceptions are Python's way of saying something unexpected happened.
Handle them so the program can recover instead of crashing.

Never use a bare `except:` — always catch specific types
(or `except Exception` only when you truly mean "almost anything").

Use exceptions for unexpected failures (missing file, bad JSON, DB down).
For cheap, expected checks (e.g. index in range), a normal `if` is often clearer.
"""

import json
from pathlib import Path

DIR = Path(__file__).parent
CONFIG = DIR.parent / "06-files-and-json" / "config.json"


# ------------------------------------------------------------
# Common exceptions you'll see
# ------------------------------------------------------------
# ValueError, TypeError, ZeroDivisionError
# FileNotFoundError, KeyError, IndexError, ...


# ------------------------------------------------------------
# Without handling — program crashes
# ------------------------------------------------------------
# int("hello")   → ValueError
# 100 / 0        → ZeroDivisionError


# ------------------------------------------------------------
# try / except — catch a specific error
# ------------------------------------------------------------
try:
    number = int("hello")
    print(100 / number)
except ValueError as error:
    print("Please enter a valid number.")
    print(error)
print()


# ------------------------------------------------------------
# Multiple except blocks
# ------------------------------------------------------------
def divide_strings(a: str, b: str) -> None:
    try:
        first = int(a)
        second = int(b)
        print(first / second)
    except ValueError as error:
        print("Invalid number.")
        print(error)
    except ZeroDivisionError as error:
        print("Cannot divide by zero.")
        print(error)


divide_strings("hello", "2")  # Invalid number.
divide_strings("100", "0")  # Cannot divide by zero.
divide_strings("100", "2")  # 50.0
print()


# ------------------------------------------------------------
# Capture the exception object — `as error`
# ------------------------------------------------------------
try:
    int("hello")
except ValueError as error:
    print(error)
print()


# ------------------------------------------------------------
# Catch several types together
# ------------------------------------------------------------
try:
    print(100 / int("0"))
except (ValueError, ZeroDivisionError) as error:
    print(error)
print()


# ------------------------------------------------------------
# else — runs only if NO exception occurred
# ------------------------------------------------------------
try:
    number = int("42")
except ValueError as error:
    print("Invalid input")
    print(error)
else:
    print("Everything worked!", number)
print()


# ------------------------------------------------------------
# finally — ALWAYS runs (cleanup)
# ------------------------------------------------------------
try:
    print("Working...")
finally:
    print("Cleaning up...")
print()


# ------------------------------------------------------------
# Real backend-ish — reading config
# ------------------------------------------------------------
try:
    with open(CONFIG, encoding="utf-8") as file:
        config = json.load(file)
    print(config["host"])  # parsing succeeded
except FileNotFoundError:
    print("Config file missing.")
except json.JSONDecodeError as error:
    print("Invalid JSON.")
    print(error)
print()


# ------------------------------------------------------------
# Good vs bad
# ------------------------------------------------------------
# ❌ except: pass          — hides every bug
# ✅ except ValueError as e — specific and visible


# ------------------------------------------------------------
# Challenge
# ------------------------------------------------------------
# Ask for two numbers (here: pass as strings so the file runs).
# Convert to int, print first / second.
# Handle ValueError and ZeroDivisionError differently.
# finally: print "Program finished."


def challenge_divide(first: str, second: str) -> None:
    try:
        a = int(first)
        b = int(second)
        print(a / b)
    except ValueError as error:
        print("Please enter valid numbers.")
        print(error)
    except ZeroDivisionError as error:
        print("Cannot divide by zero.")
        print(error)
    finally:
        print("Program finished.")


print("--- Challenge demos ---")
challenge_divide("10", "2")
print()
challenge_divide("10", "0")
print()
challenge_divide("ten", "2")
print()

# Interactive version (uncomment to try):
# first = input("First number: ")
# second = input("Second number: ")
# challenge_divide(first, second)
